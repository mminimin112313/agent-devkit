# ARIA And Keyboard Baseline

```text
INPUT := { component_type, framework_or_runtime, wcag_target, screen_reader_and_browser_matrix }

MINIMUM_CHECKS := PASS IF
  semantic_html_is_used_first
  AND interactive_elements_are_keyboard_reachable_and_operable
  AND labels_and_descriptions_are_defined
  AND state_attributes_exist_when_behavior_changes
  AND focus_is_visible_and_predictable_after(open, close, submit, error)
  AND dynamic_status_changes_are_announced
  AND live_regions_exist_when_async_or_validation_updates_would_be_silent
  AND visual_state_maps_to(accessible_name, role, state)
  AND high_contrast_and_reduced_motion_are_checked_when_relevant
  AND navigation_instructions_exist_when_keyboard_model_is_not_obvious
  AND positive_tabindex_is_not_used
  AND disclosure_controls_expose(aria_expanded, aria_controls)
  AND information_is_not_delivered_only_through_a_transient_toast

COMMON_COMPONENT_RULES := {
  dialogs := initial_focus AND escape_handling AND return_focus_on_close,
  menus_and_listboxes := arrow_key_movement AND expanded_state,
  tabs := selected_state AND tab_order AND panel_labeling,
  forms := labels AND descriptions AND errors AND invalid_state
}

PROOF := PASS IF
  keyboard_path_for_main_task_exists
  AND tab_and_shift_tab_path_exists
  AND arrow_key_behavior_is_checked_when_composite_widget_exists
  AND esc_behavior_is_checked_when_dismissible_ui_exists
  AND screen_reader_visible_labels_and_state_changes_are_checked
  AND voiceover_plus_nvda_or_jaws_path_is_checked_for_complex_widgets
  AND no_trap_dead_end_or_invisible_focus_transition_exists
```
