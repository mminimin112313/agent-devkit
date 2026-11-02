#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'EOF'
Usage: inventory-target.sh

Collects bounded inventory for a lab target using ZAP baseline and simple header probes.

Required environment:
  NETWORK_NAME  Docker network containing the target
  TARGET_URL    Target URL on the lab network, for example http://target-app:3000

Optional environment:
  RUN_ID        Reuse an existing run directory name
  OUTPUT_ROOT   Artifact root. Default: <repo>/artifacts/security-lab
  ZAP_IMAGE     Default: ghcr.io/zaproxy/zaproxy:stable
  CURL_IMAGE    Default: curlimages/curl:8.12.1
EOF
}

if [[ "${1:-}" == "--help" ]]; then
  usage
  exit 0
fi

: "${NETWORK_NAME:?set NETWORK_NAME}"
: "${TARGET_URL:?set TARGET_URL}"

script_dir="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"
skill_dir="$(CDPATH= cd -- "$script_dir/.." && pwd)"
repo_root="$(CDPATH= cd -- "$skill_dir/../../.." && pwd)"
OUTPUT_ROOT="${OUTPUT_ROOT:-$repo_root/artifacts/security-lab}"
ZAP_IMAGE="${ZAP_IMAGE:-ghcr.io/zaproxy/zaproxy:stable}"
CURL_IMAGE="${CURL_IMAGE:-curlimages/curl:8.12.1}"
run_id="${RUN_ID:-$(date +%Y%m%d-%H%M%S)}"
run_dir="$OUTPUT_ROOT/$run_id"
mkdir -p "$run_dir/inventory"

if ! command -v docker >/dev/null 2>&1; then
  echo "missing required command: docker" >&2
  exit 2
fi

docker network inspect "$NETWORK_NAME" >/dev/null

case "$TARGET_URL" in
  http://*|https://*) ;;
  *)
    echo "TARGET_URL must include http:// or https://" >&2
    exit 2
    ;;
esac

target_host="${TARGET_URL#http://}"
target_host="${target_host#https://}"
target_host="${target_host%%/*}"
case "$target_host" in
  localhost*|127.*|0.0.0.0*|*.*)
    echo "TARGET_URL host must be a Docker lab alias, not localhost or public DNS: $target_host" >&2
    exit 2
    ;;
esac

docker run --rm --network "$NETWORK_NAME" "$CURL_IMAGE" -fsSIL "$TARGET_URL" \
  >"$run_dir/inventory/headers.txt"

docker run --rm --network "$NETWORK_NAME" -v "$run_dir/inventory:/zap/wrk" "$ZAP_IMAGE" \
  zap-baseline.py -t "$TARGET_URL" -m 2 -J inventory.json -w inventory.md -r inventory.html -x inventory.xml \
  >"$run_dir/inventory/zap-baseline.log" 2>&1 || true

printf 'inventory ready\nrun_dir=%s\nheaders=%s\nzap=%s\n' \
  "$run_dir" "$run_dir/inventory/headers.txt" "$run_dir/inventory/inventory.html"
