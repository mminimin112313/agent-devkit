from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


def _read(path: str) -> str:
    return (REPO_ROOT / path).read_text(encoding="utf-8")


def test_product_and_ux_absorbs_refactoring_ui_direction_rules() -> None:
    skill = _read(".codex/skills/product-and-ux/SKILL.md")
    brief = _read(".codex/skills/product-and-ux/assets/product-brief.md")
    methodology = _read(".codex/skills/product-and-ux/references/design-system-methodology.md")
    wireframe = _read(".codex/skills/product-and-ux/references/wireframe-discipline.md")
    ideation = _read(".codex/skills/product-and-ux/references/ui-ideation-prompt-patterns.md")
    extraction = _read(".codex/skills/product-and-ux/references/design-system-extraction.md")

    assert "direction_is_still_low_fidelity_or_flow_shaping OR hierarchy_or_state_clarity_is_unproven" in skill
    assert "- hierarchy before decoration:" in brief
    assert "- empty or missing-state strategy:" in brief
    assert "- visual personality levers:" in brief
    assert "FEATURE_FIRST_EXPLORATION := PASS IF" in methodology
    assert "allow_small_hue_shifts_or_temperature_bias_when_vividness_or_neutral_character_improves" in methodology
    assert "hierarchy_is_resolved_before_decorative_surface_treatment" in methodology
    assert "supporting_or_empty_states_are_designed_before_polish" in methodology
    assert "font_weight_and_text_contrast_roles_stay_small_and_repeatable" in methodology
    assert "PERSONALITY_SIGNALS_REINFORCE_EACH_OTHER := PASS IF" in methodology
    assert "HIERARCHY_TUNING_PREFERS_CONTRAST_AND_CONTEXT_OVER_EXTRA_LABELING := PASS IF" in methodology
    assert "destructive_actions_only_gain_dominant_styling_when_they_are_primary_decisions" in methodology
    assert "generous_spacing_is_the_default_before_density_is_earned" in methodology
    assert "spacing_contrast_and_size_do_the_heavy_lifting_before_color" in wireframe
    assert "empty_or_missing_states_are_shaped_before_polish" in wireframe
    assert "visual_hierarchy_is_proven_with_spacing_contrast_and_labels_before_surface_treatment" in wireframe
    assert "spacing_within_groups_stays_tighter_than_spacing_between_groups" in wireframe
    assert "prompts_request_empty_state_and_missing_state_behavior_when_relevant" in ideation
    assert "prompts_request_mobile_first_type_and_spacing_direction" in ideation
    assert "prompts_request_personality_calibration_against_surrounding_products_without_cloning" in ideation
    assert "prompts_request_font_comparison_in_real_ui_copy_and_dense_controls_when_typography_is_a_direction_variable" in ideation
    assert "COMPONENT_REFRAMING := PASS IF" in ideation
    assert "image_treatment_rules" in extraction
    assert "image_contrast_cropping_and_background_decoration_rules_are_generalized" in extraction
    assert "image_treatment_rules_capture_when_brand_colorizations_or_tints_can_unify_photography_without_becoming_the_primary_signal" in extraction
    assert "empty_state_media_and_supporting_illustration_rules_are_separated_from_content_imagery" in extraction
    assert "empty_state_rules_separate_primary_recovery_action_from_secondary_navigation_or_filter_controls" in extraction
    assert "accent_color_usage_is_extracted_as_structural_emphasis_not_surface_decoration" in extraction
    assert "semantic_state_palettes_are_extracted_as(surface, text, border_or_badge)_pairs_not_as_isolated_swatches" in extraction
    assert "default_element_upgrades_are_generalized_for(links, lists, quotes, controls)" in extraction


def test_implementation_frontend_absorbs_refactoring_ui_system_rules() -> None:
    foundations = _read(".codex/skills/implementation-frontend/references/design-system-foundations.md")
    playbook = _read(".codex/skills/implementation-frontend/references/component-implementation-playbook.md")
    responsive = _read(".codex/skills/implementation-frontend/references/responsive-layout-patterns.md")

    assert "color_tokens_include_surface_text_accent_and_state_ladders" in foundations
    assert "shadow_tokens_map_to_named_elevation_tiers" in foundations
    assert "TYPEFACE_WEIGHT_RANGE_SUPPORTS_HIERARCHY := PASS IF" in foundations
    assert "crisp_offset_shadow_tokens_are_allowed_when_flat_interfaces_need_depth_without_soft_blur" in foundations
    assert "empty_state_variants_remove_inactive_controls_when_those_controls_have_no_effect" in playbook
    assert "text_on_images_requires_overlay_or_contrast_normalization_before_shipping" in playbook
    assert "visual_weight_is_compensated_before_size_is_reduced" in playbook
    assert "semantic_state_feedback_prefers_tinted_surfaces_with_same_hue_text_icons_or_badges_before_full_strength_fill_blocks" in playbook
    assert "hero_or_banner_images_use_a_single_contrast_strategy_across_the_full_text_zone_instead_of_patchy_local_fixes" in playbook
    assert "background_image_treatments_change_image_energy_before_foreground_chrome_is_restyled" in playbook
    assert "overlap_is_reserved_for_real_surface_transitions_or_focus_moments_not_for_random_internal_collisions" in playbook
    assert "overlapping_images_or_cards_keep_background_colored_buffer_space_so_touching_edges_do_not_clash" in playbook
    assert "empty_state_layouts_remove_or_demote_surrounding_scaffolding_when_that_scaffolding_competes_with_the_recovery_action" in playbook
    assert "empty_state_illustration_or_supporting_media_is_kept_secondary_to_headline_explanation_and_primary_action" in playbook
    assert "content_width_matches_readability_before_canvas_fill" in responsive
    assert "icons_logos_and_screenshots_render_near_intended_size" in responsive
