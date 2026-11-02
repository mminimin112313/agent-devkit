# Security Remediation Handoff

```text
PASS IF
  finding_id_is_present
  AND affected_seam_is_present
  AND fix_target_is_present
  AND owner_is_present

FAIL IF
  finding_id_is_missing
  OR affected_seam_is_missing
  OR fix_target_is_missing

HANDOFF := {
  finding_id,
  affected_seam,
  suspected_payload_family,
  proof_already_available,
  scan_jobs,
  automation_artifacts,
  automation_findings,
  fix_target,
  lab_repro_needed,
  desired_verification_run,
  expected_safe_result_after_fix,
  stop_conditions,
  owner
}
```
