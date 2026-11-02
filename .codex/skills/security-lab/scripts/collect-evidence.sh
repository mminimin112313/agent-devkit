#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'EOF'
Usage: collect-evidence.sh

Collects container logs and creates a tarball for a completed security-lab run.

Required environment:
  RUN_DIR  Completed run directory

Optional environment:
  TARGET_CONTAINER   Target container name to capture logs from
  ATTACKER_NAME      Attacker container name to capture logs from
EOF
}

if [[ "${1:-}" == "--help" ]]; then
  usage
  exit 0
fi

: "${RUN_DIR:?set RUN_DIR}"

if ! command -v docker >/dev/null 2>&1; then
  echo "missing required command: docker" >&2
  exit 2
fi

if [[ ! -d "$RUN_DIR" ]]; then
  echo "RUN_DIR does not exist: $RUN_DIR" >&2
  exit 3
fi

mkdir -p "$RUN_DIR/logs"

capture_logs() {
  local container_name="$1"
  local output_file="$2"
  if [[ -n "$container_name" ]] && docker inspect "$container_name" >/dev/null 2>&1; then
    docker logs "$container_name" >"$output_file" 2>&1 || true
  fi
}

capture_logs "${TARGET_CONTAINER:-}" "$RUN_DIR/logs/target.log"
capture_logs "${ATTACKER_NAME:-}" "$RUN_DIR/logs/attacker.log"

(
  cd "$RUN_DIR/.."
  tar -czf "$(basename "$RUN_DIR").tar.gz" "$(basename "$RUN_DIR")"
)

printf 'evidence bundled\nbundle=%s\n' "${RUN_DIR}.tar.gz"
