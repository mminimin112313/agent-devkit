# Mobile-First Experience Principles

Mobile-first means content priority and interaction order are decided at the narrowest useful width first.

```text
MOBILE_FIRST := PASS IF
  single_most_important_task_is_defined_before_desktop_enhancements
  AND primary_action_stays_visible_without_relying_on_wide_layouts
  AND content_is_grouped_by_task_importance_not_desktop_symmetry
  AND touch_thumb_reach_and_interruption_are_treated_as_default_constraints
  AND tablet_and_desktop_expansion_happens_only_after_mobile_hierarchy_is_coherent

ACROSS_WIDTH_DECISIONS := {
  navigation := { persistent, collapsed, segmented },
  media_treatment := { full_width, cropped, deferred },
  dense_desktop_modules := simplify_or_stack_cleanly_on_narrow_screens,
  validation_empty_and_error_states := remain_readable_on_narrow_layouts,
  touch_targets := stay_at_or_above_44px_when_touch_input_is_expected
}

CHECKS := PASS IF
  first_screen_answers(identity, available_action, next_step)
  AND controls_remain_usable_at_touch_size
  AND long_text_empty_states_and_validation_messages_fit_narrow_widths
  AND layout_changes_preserve_reading_order_and_keyboard_order
  AND dense_desktop_modules_collapse_into_clear_stacked_groups
  AND performance_sensitive_elements_are_called_out_before_mobile_regressions
  AND browser_or_platform_assumptions_are_explicit_when_layout_or_interaction_depends_on_them

OUTPUT := {
  mobile_first_screen_content,
  mobile_content_priority,
  navigation_behavior_across_widths,
  breakpoint_sensitive_risks,
  interaction_changes_across_widths,
  performance_sensitive_elements,
  browser_or_support_assumptions,
  accessibility_or_comprehension_risks_from_density
}
```
