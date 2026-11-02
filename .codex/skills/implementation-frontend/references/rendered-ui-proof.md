# Rendered UI Proof

Use this lens when interaction proof depends on a dynamic UI, browser automation, or hydrated DOM state.

```text
INPUT := {
  page_or_component_surface,
  runtime_type,
  readiness_signal,
  proof_mode,
  helper_scripts
}

WORKING_ORDER :=
  1 -> establish_readiness_signal
  2 -> inspect_rendered_state
  3 -> choose_selectors_from_rendered_state
  4 -> execute_actions
  5 -> capture_proof_artifacts

HELPER_RULE := PASS IF
  bundled_helpers_are_checked_via_help_output_before_source_read
  AND helper_scripts_are_used_as_black_boxes_when_they_cover_common_setup_or_runtime_work

CHECKS := PASS IF
  readiness_wait_happens_before_dom_or_screenshot_inspection
  AND selectors_come_from(rendered_dom OR accessibility_tree OR visible_ui_copy)
  AND screenshot_or_dom_snapshot_exists_before_action_when_ui_state_is_unclear
  AND proof_artifacts_show(the_state_before_action AND the_result_after_action) WHEN interaction_risk_is_high
  AND helper_usage_does_not_replace_behavior_verification

FAIL IF
  selectors_are_guessed_from_source_before_rendered_state_is_checked
  OR dynamic_ui_is_treated_like_static_markup
  OR helper_script_source_is_read_first_when_help_output_would_suffice
  OR actions_run_before_readiness_signal_is_confirmed
```
