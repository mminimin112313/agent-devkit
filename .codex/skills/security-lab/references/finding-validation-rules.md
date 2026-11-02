# Finding Validation Rules

```text
USE BEFORE escalating_lead -> confirmed_finding

CONFIRMED_FINDING := PASS IF
  deterministic_request_and_response_evidence_exists
  OR repeated_behavior_across_reruns_exists
  OR target_side_log_proves_unsafe_action
  OR before_and_after_fix_rerun_proves_defect_disappeared

LEAD_ONLY := PASS IF
  scanner_alert_has_no_reproducer
  OR error_page_only_hints_at_risk
  OR anomaly_is_one_off_or_intermittent
  OR symptom_is_client_side_without_server_confirmation

FALSE_POSITIVE_CONTROLS := PASS IF
  baseline_request_is_recorded_before_modified_request
  AND one_variable_changes_at_a_time
  AND auth_context_stays_constant UNLESS authz_is_under_test
  AND timing_checks_repeat_enough_to_separate_noise
  AND xss_distinguishes_reflection_from_script_execution
  AND ssrf_proves_server_made_outbound_request
```
