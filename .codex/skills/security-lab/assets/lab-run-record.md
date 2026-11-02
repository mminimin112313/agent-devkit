# Security Lab Run Record

```text
PASS IF
  declared_assets_are_named
  AND files_read_before_lab_execution_are_named
  AND run_id_is_present
  AND network_name_is_present
  AND target_url_is_present
  AND artifacts_root_is_present

FAIL IF
  files_actually_used_are_missing
  OR run_id_is_missing
  OR network_name_is_missing
  OR target_url_is_missing

RUN_RECORD := {
  declared_assets,
  declared_references,
  files_read_before_lab_execution,
  why_each_file_was_loaded,
  files_actually_used,
  run_id,
  network_name,
  target_url,
  target_container,
  attacker_container,
  run_mode,
  artifacts_root,
  auth_context,
  checks_executed,
  blocked_checks,
  next_action
}
```
