# Responsive Layout Patterns

```text
INPUT := {
  mobile_content_priority,
  breakpoint_contract,
  navigation_behavior,
  image_or_media_behavior,
  css_method_or_framework,
  browser_support_assumption,
  presentation_proof
}

WORKING_ORDER :=
  1 -> mobile_baseline
  2 -> tablet_and_desktop_expansion
  3 -> extreme_content_and_zoom_cases

CHECKS := PASS IF
  content_width_matches_readability_before_canvas_fill
  AND readable_measure_survives_breakpoint_expansion_without_turning_into_canvas_fill
  AND supporting_content_can_move_to_adjacent_columns_before_core_content_is_widened
  AND container_behavior_and_overflow_are_safe
  AND text_wrapping_and_truncation_are_safe
  AND touch_target_size_is_safe
  AND keyboard_and_screen_reader_compatibility_is_safe
  AND content_order_stays_logical_across_breakpoints
  AND primary_action_remains_visible_on_narrow_widths
  AND fixed_or_max_widths_follow_content_stability_before_grid_symmetry
  AND large_elements_shrink_faster_than_small_elements_when_needed
  AND screenshots_or_media_are_cropped_or_reframed_before_being_scaled_to_unreadability
  AND icons_logos_and_screenshots_render_near_intended_size_or_switch_to_a_simpler_representation
  AND asset_size_rules_prevent_icons_logos_and_screenshots_from_drifting_into_generic_fill_behavior
  AND interactive_targets_stay_at_or_above_44px_when_touch_is_expected
  AND zoom_to_200_percent_preserves_meaning_and_control_access

PROOF := {
  mobile_tablet_desktop_manual_check,
  zoom_check,
  image_sizing_and_aspect_ratio_check,
  screenshot_or_media_cropping_check,
  late_loading_media_overflow_check,
  cross_browser_spot_check
}
```
