#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'EOF'
Usage: run-web-checks.sh

Runs bounded passive and active checks from disposable Docker tool containers.

Required environment:
  NETWORK_NAME  Docker network containing the target
  TARGET_URL    Target URL on the lab network

Optional environment:
  RUN_ID             Reuse an existing run directory name
  OUTPUT_ROOT        Artifact root. Default: <repo>/artifacts/security-lab
  ZAP_IMAGE          Default: ghcr.io/zaproxy/zaproxy:stable
  NUCLEI_IMAGE       Default: projectdiscovery/nuclei:latest
  SQLMAP_IMAGE       Default: ghcr.io/sqlmapproject/sqlmap:latest
  ENABLE_ACTIVE_SCAN Set to 1 to run ZAP full scan
  ENABLE_SQLMAP      Set to 1 to run sqlmap against SQLMAP_TARGET
  SQLMAP_TARGET      Exact URL with injectable parameter for sqlmap
  SQLMAP_DATA        Optional POST data for sqlmap
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
NUCLEI_IMAGE="${NUCLEI_IMAGE:-projectdiscovery/nuclei:latest}"
SQLMAP_IMAGE="${SQLMAP_IMAGE:-ghcr.io/sqlmapproject/sqlmap:latest}"
run_id="${RUN_ID:-$(date +%Y%m%d-%H%M%S)}"
run_dir="$OUTPUT_ROOT/$run_id"
mkdir -p "$run_dir/checks"
status_file="$run_dir/checks/tool-status.tsv"
: >"$status_file"

if ! command -v docker >/dev/null 2>&1; then
  echo "missing required command: docker" >&2
  exit 2
fi

docker network inspect "$NETWORK_NAME" >/dev/null

target_host="${TARGET_URL#http://}"
target_host="${target_host#https://}"
target_host="${target_host%%/*}"
case "$target_host" in
  localhost*|127.*|0.0.0.0*|*.*)
    echo "TARGET_URL host must be a Docker lab alias, not localhost or public DNS: $target_host" >&2
    exit 2
    ;;
esac

set +e
docker run --rm --network "$NETWORK_NAME" -v "$run_dir/checks:/zap/wrk" "$ZAP_IMAGE" \
  zap-baseline.py -t "$TARGET_URL" -m 2 -J zap-baseline.json -w zap-baseline.md -r zap-baseline.html -x zap-baseline.xml \
  >"$run_dir/checks/zap-baseline.log" 2>&1
zap_baseline_status=$?
set -e
printf 'zap-baseline\t%s\n' "$zap_baseline_status" >>"$status_file"

if [[ "${ENABLE_ACTIVE_SCAN:-0}" == "1" ]]; then
  set +e
  docker run --rm --network "$NETWORK_NAME" -v "$run_dir/checks:/zap/wrk" "$ZAP_IMAGE" \
    zap-full-scan.py -t "$TARGET_URL" -J zap-active.json -w zap-active.md -r zap-active.html -x zap-active.xml \
    >"$run_dir/checks/zap-active.log" 2>&1
  zap_active_status=$?
  set -e
  printf 'zap-active\t%s\n' "$zap_active_status" >>"$status_file"
fi

set +e
docker run --rm --network "$NETWORK_NAME" -v "$run_dir/checks:/work" "$NUCLEI_IMAGE" \
  -u "$TARGET_URL" -severity low,medium,high,critical -json-export /work/nuclei.jsonl \
  >"$run_dir/checks/nuclei.log" 2>&1
nuclei_status=$?
set -e
printf 'nuclei\t%s\n' "$nuclei_status" >>"$status_file"

if [[ "${ENABLE_SQLMAP:-0}" == "1" ]]; then
  : "${SQLMAP_TARGET:?set SQLMAP_TARGET when ENABLE_SQLMAP=1}"
  sqlmap_args=(-u "$SQLMAP_TARGET" --batch --output-dir=/work/sqlmap)
  if [[ -n "${SQLMAP_DATA:-}" ]]; then
    sqlmap_args+=(--data "$SQLMAP_DATA")
  fi
  set +e
  docker run --rm --network "$NETWORK_NAME" -v "$run_dir/checks:/work" "$SQLMAP_IMAGE" "${sqlmap_args[@]}" \
    >"$run_dir/checks/sqlmap.log" 2>&1
  sqlmap_status=$?
  set -e
  printf 'sqlmap\t%s\n' "$sqlmap_status" >>"$status_file"
fi

python3 - "$run_dir/checks/nuclei.jsonl" "$run_dir/checks/findings-summary.json" <<'PY'
import json
import sys
from collections import Counter
from pathlib import Path

source = Path(sys.argv[1])
target = Path(sys.argv[2])
severity_counts = Counter()
signatures = []

if source.exists():
    for raw in source.read_text(encoding="utf-8", errors="replace").splitlines():
        if not raw.strip():
            continue
        payload = json.loads(raw)
        info = payload.get("info") or {}
        severity = str(info.get("severity") or payload.get("severity") or "unknown").lower()
        template_id = str(payload.get("template-id") or payload.get("templateID") or "unknown")
        matched_at = str(payload.get("matched-at") or payload.get("matched") or payload.get("host") or "unknown")
        severity_counts[severity] += 1
        signatures.append(
            {
                "template_id": template_id,
                "matched_at": matched_at,
                "severity": severity,
                "signature": f"{template_id}|{matched_at}|{severity}",
            }
        )

target.write_text(
    json.dumps(
        {
            "scanner": "nuclei",
            "severity_counts": dict(sorted(severity_counts.items())),
            "signatures": sorted(signatures, key=lambda item: item["signature"]),
        },
        indent=2,
        sort_keys=True,
    )
    + "\n",
    encoding="utf-8",
)
PY

cat >"$run_dir/checks/summary.md" <<EOF
# Security Lab Check Summary

- target: $TARGET_URL
- network: $NETWORK_NAME
- tool status: $status_file
- zap baseline: $run_dir/checks/zap-baseline.log
- nuclei: $run_dir/checks/nuclei.log
- nuclei summary: $run_dir/checks/findings-summary.json
- zap active enabled: ${ENABLE_ACTIVE_SCAN:-0}
- sqlmap enabled: ${ENABLE_SQLMAP:-0}
EOF

printf 'checks complete\nrun_dir=%s\nsummary=%s\n' \
  "$run_dir" "$run_dir/checks/summary.md"
