# Security Finding Record

```text
PASS IF
  id_is_present
  AND boundary_is_present
  AND weakness_is_present
  AND exploit_path_is_present
  AND severity_is_present
  AND owner_is_present

FAIL IF
  weakness_is_missing
  OR exploit_path_is_missing
  OR owner_is_missing

FINDING := {
  id,
  boundary,
  weakness,
  affected_code_or_config_seam,
  exploit_path,
  preconditions,
  impact,
  severity,
  evidence,
  false_positive_guard,
  remediation,
  owner,
  verification_path
}
```
