# Release Evidence

```text
PASS IF
  shipping_scope IS explicit
  AND fresh_verification IS present
  AND security_automation_is_fresh_or_explicitly_waived
  AND rollback_owner IS explicit
  AND unresolved_risk IS explicit

FAIL IF
  verification_is_stale
  OR security_automation_is_stale_without_waiver
  OR rollback_owner IS missing
  OR unresolved_risk IS implicit

IF shipping_scope IS vague THEN FAIL

AND record(change_type, risk_level, evidence_timeframe, rollback_method, recovery_verifier, before_after_state_when_risky)
AND record(security_scan_jobs, security_artifacts, security_owner)

IF endpoint_or_method_matters THEN
  record(endpoint, method, observed_response)

IF environment_is_resource_constrained THEN
  record(build_strategy, recovery_path)

IF ship_decision_depends_on_runtime_monitoring THEN
  record(observability_coverage, alert_coverage)

keep_branch_as_is_is_allowed_without_forced_cleanup
discard_requires_explicit_confirmation

IF security_findings_exist THEN ROUTE -> security-review

NOT(can_deploy = safe_to_operate)
AND prefer(fresh_runtime_checks_over_inherited_confidence)
```
