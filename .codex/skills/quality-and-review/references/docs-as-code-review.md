# Docs As Code Review

Documentation gaps are product and operations gaps.

```text
REVIEW_TRIGGERS := {
  changed_api_or_cli_behavior,
  changed_onboarding_or_operator_workflow,
  new_config_env_var_or_dependency,
  removed_or_renamed_contract_fields
}

REVIEW_STANDARD := PASS IF
  docs_match_current_behavior
  AND examples_still_run_or_remain_believable
  AND migration_note_exists_for_breaking_changes
  AND operator_facing_risk_is_visible_without_reading_code

RECORD_WHEN_DOCS_REVIEW_MATTERS := {
  docs_checked,
  examples_exercised_vs_only_inspected,
  whether_stale_or_broken_references_remain,
  residual_user_or_operator_risk_after_review
}
```
