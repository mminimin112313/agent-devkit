# Inclusive Visual Review

Generated or designed visuals should preserve dignity, specificity, and usability.

```text
REVIEW_PASS :=
  1 -> identify(people, context, activity)_being_represented
  2 -> check_for(stereotype_defaults, tokenism, unrealistic_composition)
  3 -> add_negative_constraints_for_common_failure_modes
  4 -> verify(lighting, setting, language, props)_fit_the_intended_context
  5 -> check_information_hierarchy(primary_message_visible_within_three_seconds, decorative_treatment_not_hiding_actions_or_status, spacing_rhythm_reinforcing_grouping)
  6 -> review_with_accessibility_and_comprehension_in_mind

COMMON_FAILURE_MODES := FAIL IF
  cloned_faces_or_bodies_appear_in_group_scenes
  OR decorative_diversity_has_no_meaningful_context
  OR symbols_text_or_environments_are_culturally_inaccurate
  OR whimsy_reduces_legibility_or_trust
  OR contrast_or_color_encodes_meaning_without_a_backup_cue
  OR visual_density_looks_polished_on_desktop_but_collapses_on_mobile

DESIGN_DIRECTION_CHECKS := PASS IF
  token_rule_need_is_called_out_for(accent_usage, type_scale, spacing_rhythm, corner_or_elevation_style)
  AND visual_only_concerns_are_separated_from_interaction_accessibility_concerns
  AND responsive_risk_is_labeled_when_composition_depends_on_wide_layouts
  AND accessibility_risk_is_marked_separately_from_aesthetic_preference

ROUTE -> `interaction-accessibility-principles.md` IF behavior_is_the_main_issue

OUTPUT := {
  explicit_constraints,
  review_notes,
  disposition := safe_to_use_as_is OR revise OR reject
}
```
