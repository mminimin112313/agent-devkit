#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'EOF'
Usage: verify-fix.sh

Reruns the bounded checks for a fixed target and writes a verification summary.

Required environment:
  NETWORK_NAME   Docker network containing the target
  TARGET_URL     Target URL on the lab network
  BASELINE_DIR   Previous run directory to compare against

Optional environment:
  RUN_ID         Verification run id
  OUTPUT_ROOT    Artifact root. Default: <repo>/artifacts/security-lab
  EXPECT_CLEAN   Set to 1 to fail when high or critical findings remain in nuclei output
EOF
}

if [[ "${1:-}" == "--help" ]]; then
  usage
  exit 0
fi

: "${NETWORK_NAME:?set NETWORK_NAME}"
: "${TARGET_URL:?set TARGET_URL}"
: "${BASELINE_DIR:?set BASELINE_DIR}"

script_dir="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"
skill_dir="$(CDPATH= cd -- "$script_dir/.." && pwd)"
repo_root="$(CDPATH= cd -- "$skill_dir/../../.." && pwd)"
OUTPUT_ROOT="${OUTPUT_ROOT:-$repo_root/artifacts/security-lab}"
verify_run_id="${RUN_ID:-verify-$(date +%Y%m%d-%H%M%S)}"

if ! command -v docker >/dev/null 2>&1; then
  echo "missing required command: docker" >&2
  exit 2
fi

RUN_ID="$verify_run_id" OUTPUT_ROOT="$OUTPUT_ROOT" NETWORK_NAME="$NETWORK_NAME" TARGET_URL="$TARGET_URL" \
  "$script_dir/run-web-checks.sh" >/dev/null

verify_dir="$OUTPUT_ROOT/$verify_run_id"
baseline_summary="$BASELINE_DIR/checks/findings-summary.json"
verify_summary="$verify_dir/checks/findings-summary.json"

compare_json="$(python3 - "$baseline_summary" "$verify_summary" <<'PY'
import json
import sys
from pathlib import Path

def load(path: str) -> dict:
    p = Path(path)
    if not p.exists():
        return {"severity_counts": {}, "signatures": []}
    return json.loads(p.read_text(encoding="utf-8"))

baseline = load(sys.argv[1])
verify = load(sys.argv[2])
baseline_sigs = {item["signature"] for item in baseline.get("signatures", [])}
verify_sigs = {item["signature"] for item in verify.get("signatures", [])}
remaining_high_or_critical = [
    item for item in verify.get("signatures", [])
    if item.get("severity") in {"high", "critical"}
]
print(json.dumps({
    "baseline_count": len(baseline_sigs),
    "verification_count": len(verify_sigs),
    "resolved": sorted(baseline_sigs - verify_sigs),
    "introduced": sorted(verify_sigs - baseline_sigs),
    "remaining_high_or_critical_count": len(remaining_high_or_critical),
}, indent=2, sort_keys=True))
PY
)"
printf '%s\n' "$compare_json" >"$verify_dir/verification-diff.json"

cat >"$verify_dir/verification-summary.md" <<EOF
# Verification Summary

- baseline dir: $BASELINE_DIR
- verification dir: $verify_dir
- diff: $verify_dir/verification-diff.json
EOF

remaining_high_or_critical_count="$(python3 - "$verify_dir/verification-diff.json" <<'PY'
import json
import sys
from pathlib import Path
print(json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))["remaining_high_or_critical_count"])
PY
)"

if [[ "${EXPECT_CLEAN:-0}" == "1" ]] && [[ "$remaining_high_or_critical_count" != "0" ]]; then
  echo "verification failed: high or critical findings remain; see $verify_dir/verification-diff.json" >&2
  exit 4
fi

printf 'verification complete\nverification_dir=%s\nsummary=%s\n' \
  "$verify_dir" "$verify_dir/verification-summary.md"
