# Design System Methodology

Turn visual direction into shared rules before asking implementation to improvise.

```text
DISCOVERY_INPUTS := {
  feature_slice_to_design_first,
  target_users_and_technical_comfort,
  industry_norms_to_respect_or_break,
  brand_traits_that_must_survive_implementation,
  primary_task_and_trust_level_to_create,
  accessibility_and_mode_expectations := {
    contrast_target,
    reduced_motion_expectations,
    light_or_dark_mode_strategy
  }
}

BUILD_ORDER :=
  1 -> choose_feature_slice_before_shell(feature_slice_to_design_first)
  2 -> define_brand_and_task_intent(primary_feeling, safety_urgency_or_calm_targets)
  3 -> define_semantic_tokens(color_roles, type_scale, spacing_rhythm, corner_elevation_and_motion_rules)
  4 -> define_primitives(buttons, fields, cards, navigation_shells)
  5 -> define_pattern_level_guidance(forms, dashboards, lists, dialogs)

FEATURE_FIRST_EXPLORATION := PASS IF
  first_design_work_targets_a_real_user_task_not_global_shell_chrome
  AND low_fidelity_structure_is_validated_before_decorative_detail
  AND personality_is_chosen_through_a_small_repeatable_set_of_levers

PERSONALITY_SIGNALS_REINFORCE_EACH_OTHER := PASS IF
  photography_type_voice_corner_treatment_and_supporting_patterns_point_toward_one_product_character
  AND contradictory_personality_signals_are_removed_before_polish

PALETTE_METHOD := {
  choose_primary_color_role_based_on(trust OR urgency OR emotional_tone),
  choose_harmony_only_after_primary_role_is_clear,
  define_full_palette_ladders_before_component_polish(neutrals, primary, semantic_accents),
  set_shades_up_front_instead_of_runtime_lighten_or_darken,
  allow_small_hue_shifts_or_temperature_bias_when_vividness_or_neutral_character_improves,
  define_neutral_and_status_semantics(success, warning, error, info),
  treat_color_as_accent_only IF it_cannot_become_a_stable_semantic_role
}

TYPOGRAPHY_AND_SPACING_BASE := PASS IF
  type_hierarchy_is_defined_mobile_first_before_scaling_up
  AND type_scale_is_constrained_and_handcrafted_instead_of_formula_driven
  AND font_weight_and_text_contrast_roles_stay_small_and_repeatable
  AND one_spacing_rhythm_is_kept_consistent_across_components
  AND spacing_scale_is_built_on_4pt_or_8pt_steps
  AND content_width_respects_readable_measure_instead_of_canvas_fill
  AND line_height_and_tracking_change_with_text_role_not_one_global_value
  AND density_exceptions_are_recorded_without_breaking_the_system
  AND generous_spacing_is_the_default_before_density_is_earned

COMPONENT_STATE_AND_VARIANT_MATRIX := {
  name_core_component_set,
  required_states := { default, hover_or_focus, disabled, error, loading_when_applicable },
  distinguish(reusable_variants, one_off_exceptions)
}

MOTION_RULES := PASS IF
  motion_groups_are_defined_as(entrance, interaction, ambient, attention)
  AND reduced_motion_expectations_are_respected
  AND motion_supports_hierarchy_instead_of_decorative_noise

QUALITY_GATES := PASS IF
  semantic_status_colors_stay_understandable_without_decorative_context
  AND mode_strategy_is_explicit
  AND hierarchy_survives_mobile_density
  AND supporting_or_empty_states_are_designed_before_polish
  AND component_variants_cover_important_states
  AND accessibility_constraints_are_written_as_rules
  AND primary_vs_secondary_vs_tertiary_emphasis_is_explicit
  AND label_treatment_follows_scan_priority_not_database_shape

HIERARCHY_METHODS := PASS IF
  important_elements_are_emphasized_before_secondary_elements_gain_weight
  AND competing_elements_are_softened_before_primary_elements_gain_more_decoration
  AND hierarchy_is_resolved_before_decorative_surface_treatment
  AND supporting_context_is_softened_or_removed_before_new_labels_borders_or_fills_are_added
  AND semantic_headings_do_not_force_visual_prominence
  AND action_tiers_follow(actual_priority, not_just_action_severity)
  AND destructive_actions_only_gain_dominant_styling_when_they_are_primary_decisions

HIERARCHY_TUNING_PREFERS_CONTRAST_AND_CONTEXT_OVER_EXTRA_LABELING := PASS IF
  secondary_context_is_deemphasized_before_explanatory_chrome_is_added
  AND labels_removed_for_hierarchy_do_not_carry_unique_meaning

SYSTEM_BUILDING := PASS IF
  color_ladders_have_enough_shades_for(text, surfaces, accents, states)
  AND typography_scale_is_constrained_but_practical
  AND spacing_or_sizing_choices_come_from_named_scales
  AND elevation_rules_map_to_repeatable_shadow_or_tonal_layers
  AND asset_treatment_rules_exist_for(images, screenshots, and_empty_states)

GUARDRAILS := PASS IF
  semantic_token_names_replace_raw_color_debate
  AND allowed_meaning_carrying_accents_are_documented
  AND spacing_system_stays_consistent_across_mobile_and_desktop
  AND every_visual_direction_choice_records_accessibility_implications
  AND taste_statements_are_converted_into_rules_or_deleted
  AND personality_is_expressed_through(font, color, radius, copy_tone)_choices_instead_of_unstructured_polish

OUTPUT := {
  token_intent,
  semantic_status_colors,
  mode_strategy,
  typography_and_spacing_base,
  hierarchy_rules,
  spacing_rhythm,
  allowed_component_variants,
  state_behavior,
  accessibility_constraints
}
```
