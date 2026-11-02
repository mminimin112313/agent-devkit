# Security Review Record

```text
PASS IF
  declared_assets_are_named
  AND files_read_before_classification_are_named
  AND seam_reviewed_is_named
  AND trust_boundary_is_named
  AND evidence_checked_is_named
  AND next_skill_or_next_owner_is_named

FAIL IF
  files_actually_used_are_missing
  OR seam_reviewed_is_missing
  OR trust_boundary_is_missing

RECORD := {
  declared_assets,
  declared_references,
  files_read_before_classification,
  why_each_file_was_loaded,
  files_actually_used,
  seam_reviewed,
  trust_boundary,
  code_or_config_paths,
  entry_points,
  sensitive_assets,
  evidence_checked,
  references_used,
  findings,
  repro_required,
  remediation_owner,
  next_skill_or_next_owner
}
```
