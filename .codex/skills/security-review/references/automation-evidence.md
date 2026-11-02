# Automation Evidence

```text
USE IF
  ci_scan_artifacts_exist
  OR scanner_output_is_being_cited_as_security_evidence

AUTOMATION_EVIDENCE := PASS IF
  ci_scan_artifacts_are_named
  AND scan_jobs_are_named
  AND commit_or_pr_scope_is_named
  AND automation_output_does_not_replace_reading_the_affected_seam
  AND each_tool_output_is_classified_as(finding OR repro_required OR cleared_with_rationale)

TOOL_MAPPING := {
  trufflehog -> secrets_and_credential_history_signals,
  trivy -> filesystem_dependency_and_misconfiguration_signals,
  kingfisher -> repository_secret_and_validation_signals
}

IF tool_output_names(secret OR credential OR token_exposure) THEN
  START -> assets/finding-record.md
  ROUTE -> remediation_owner

ELSE IF tool_output_suggests(runtime_exploitability_without_proof) THEN
  START -> assets/remediation-handoff.md
  ROUTE -> security-lab

ELSE
  RECORD(cleared_with_rationale, artifact_path, scan_job, commit_scope)

FAIL IF
  tool_output_is_treated_as_final_without_code_or_config_review
  OR scanner_findings_lack_artifact_paths
  OR scan_scope_is_unknown
```
