#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'EOF'
Usage: bootstrap-lab.sh

Bootstraps a bounded Docker lab with a target container and an attacker utility container.

Environment:
  LAB_NAME              Lab prefix. Default: security-lab
  NETWORK_NAME          Docker network name. Default: ${LAB_NAME}-net
  TARGET_CONTAINER      Existing target container to join to the lab network
  TARGET_IMAGE          Target image to run when TARGET_CONTAINER is not set
  ALLOW_SAMPLE_TARGET   Set to 1 to allow the built-in Juice Shop training image
  TARGET_NAME           Target container name. Default: target-app
  TARGET_INTERNAL_PORT  Port inside the target container. Default: 3000
  TARGET_HOST_PORT      Optional host port to publish
  ATTACKER_IMAGE        Utility attacker image. Default: nicolaka/netshoot:latest
  ATTACKER_NAME         Attacker container name. Default: attacker-box
  ENABLE_PROXY          Set to 1 to launch a mitmproxy helper container
  PROXY_IMAGE           Proxy image. Default: mitmproxy/mitmproxy:latest
  OUTPUT_ROOT           Artifact root. Default: <repo>/artifacts/security-lab

Examples:
  ALLOW_SAMPLE_TARGET=1 TARGET_HOST_PORT=8080 ./bootstrap-lab.sh
  TARGET_IMAGE=my-target:local TARGET_HOST_PORT=8080 ./bootstrap-lab.sh
  TARGET_CONTAINER=my-site TARGET_INTERNAL_PORT=8080 ./bootstrap-lab.sh
EOF
}

if [[ "${1:-}" == "--help" ]]; then
  usage
  exit 0
fi

script_dir="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"
skill_dir="$(CDPATH= cd -- "$script_dir/.." && pwd)"
repo_root="$(CDPATH= cd -- "$skill_dir/../../.." && pwd)"

LAB_NAME="${LAB_NAME:-security-lab}"
NETWORK_NAME="${NETWORK_NAME:-${LAB_NAME}-net}"
TARGET_NAME="${TARGET_NAME:-target-app}"
TARGET_INTERNAL_PORT="${TARGET_INTERNAL_PORT:-3000}"
ATTACKER_IMAGE="${ATTACKER_IMAGE:-nicolaka/netshoot:latest}"
ATTACKER_NAME="${ATTACKER_NAME:-attacker-box}"
PROXY_IMAGE="${PROXY_IMAGE:-mitmproxy/mitmproxy:latest}"
OUTPUT_ROOT="${OUTPUT_ROOT:-$repo_root/artifacts/security-lab}"

timestamp="$(date +%Y%m%d-%H%M%S)"
run_dir="$OUTPUT_ROOT/$timestamp"
latest_link="$OUTPUT_ROOT/latest"
mkdir -p "$run_dir"

require_cmd() {
  if ! command -v "$1" >/dev/null 2>&1; then
    echo "missing required command: $1" >&2
    exit 2
  fi
}

require_cmd docker

if ! docker network inspect "$NETWORK_NAME" >/dev/null 2>&1; then
  docker network create "$NETWORK_NAME" >/dev/null
fi

if [[ -n "${TARGET_CONTAINER:-}" ]]; then
  docker inspect "$TARGET_CONTAINER" >/dev/null
  docker network connect "$NETWORK_NAME" "$TARGET_CONTAINER" >/dev/null 2>&1 || true
  target_container="$TARGET_CONTAINER"
else
  if [[ -z "${TARGET_IMAGE:-}" ]]; then
    if [[ "${ALLOW_SAMPLE_TARGET:-0}" != "1" ]]; then
      echo "set TARGET_CONTAINER or TARGET_IMAGE; set ALLOW_SAMPLE_TARGET=1 only for the built-in training target" >&2
      exit 2
    fi
    TARGET_IMAGE="bkimminich/juice-shop:latest"
  fi
  if docker inspect "$TARGET_NAME" >/dev/null 2>&1; then
    docker rm -f "$TARGET_NAME" >/dev/null
  fi

  docker_args=(run -d --name "$TARGET_NAME" --network "$NETWORK_NAME")
  if [[ -n "${TARGET_HOST_PORT:-}" ]]; then
    docker_args+=(-p "${TARGET_HOST_PORT}:${TARGET_INTERNAL_PORT}")
  fi
  docker_args+=("$TARGET_IMAGE")
  docker "${docker_args[@]}" >/dev/null
  target_container="$TARGET_NAME"
fi

if docker inspect "$ATTACKER_NAME" >/dev/null 2>&1; then
  docker rm -f "$ATTACKER_NAME" >/dev/null
fi
docker run -d --name "$ATTACKER_NAME" --network "$NETWORK_NAME" "$ATTACKER_IMAGE" sleep infinity >/dev/null

proxy_container=""
if [[ "${ENABLE_PROXY:-0}" == "1" ]]; then
  proxy_container="${LAB_NAME}-proxy"
  if docker inspect "$proxy_container" >/dev/null 2>&1; then
    docker rm -f "$proxy_container" >/dev/null
  fi
  docker run -d --name "$proxy_container" --network "$NETWORK_NAME" "$PROXY_IMAGE" mitmdump >/dev/null
fi

target_url="http://${target_container}:${TARGET_INTERNAL_PORT}/"
if ! docker run --rm --network "$NETWORK_NAME" curlimages/curl:8.12.1 -fsS "$target_url" >/dev/null 2>&1; then
  echo "target is not reachable on lab network: $target_url" >&2
  exit 3
fi

cat >"$run_dir/lab.env" <<EOF
LAB_NAME=$LAB_NAME
NETWORK_NAME=$NETWORK_NAME
TARGET_CONTAINER=$target_container
TARGET_URL=$target_url
ATTACKER_NAME=$ATTACKER_NAME
PROXY_CONTAINER=$proxy_container
EOF

rm -f "$latest_link"
ln -s "$run_dir" "$latest_link"

printf 'lab ready\nnetwork=%s\ntarget=%s\nattacker=%s\nartifacts=%s\n' \
  "$NETWORK_NAME" "$target_container" "$ATTACKER_NAME" "$run_dir"
