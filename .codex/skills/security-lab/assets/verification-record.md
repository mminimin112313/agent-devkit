# Verification Record

```text
PASS IF
  baseline_run_is_present
  AND verification_run_is_present
  AND fix_target_is_present
  AND verdict_is_present

FAIL IF
  baseline_run_is_missing
  OR verification_run_is_missing
  OR verdict_is_missing

VERIFICATION := {
  baseline_run,
  verification_run,
  fix_target,
  checks_rerun,
  findings_removed,
  findings_remaining,
  exact_artifacts_compared,
  regression_notes,
  verdict
}
```
