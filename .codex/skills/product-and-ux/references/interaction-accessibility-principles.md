# Interaction Accessibility Principles

Interactive accessibility is not the same as visual accessibility.

```text
USE_THIS_LENS IF
  ux_decision_changes_semantic_structure
  OR custom_controls_or_composite_widgets_exist
  OR focus_order_or_keyboard_behavior_is_part_of_the_interaction
  OR dynamic_status_changes_need_announcement

CORE_RULES := PASS IF
  semantic_html_is_used_first_with_aria_only_when_needed
  AND keyboard_path_for_the_primary_task_is_defined
  AND focus_entry_movement_and_exit_for_transient_ui_are_defined
  AND visual_state_maps_to_accessible_name_role_and_state
  AND screen_reader_announcements_for_status_changes_are_defined

REVIEW_PROMPTS := {
  semantic_structure_of_the_flow,
  expected_behavior_for(Tab, Arrow_keys, Enter, Space, Esc),
  focus_destination_after(open, submit, error, close),
  updates_that_need_live_announcements,
  assistive_tech_proof_required_before_approval
}

PROOF := PASS IF
  keyboard_path_for_the_primary_task_is_validated
  AND focus_restoration_is_confirmed_for(open, submit, error, close)
  AND at_least_one_screen_reader_verification_pass_happens_before_approval

OUTPUT := {
  semantic_structure_risk,
  keyboard_or_focus_expectations,
  screen_reader_or_state_change_behavior,
  test_or_evidence_gap
}
```
