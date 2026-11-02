# Visual Direction Differentiation Rules

Use this lens when product direction must shape a UI-facing visual system without drifting into implementation.

```text
VISUAL_DIRECTION := PASS IF
  aesthetic_direction_is_named_as_a_clear_point_of_view
  AND the_direction_matches(user_job + audience + context)
  AND layout_typography_color_and_motion_implications_are_named_at_the_rule_level

MEMORABLE_DIFFERENTIATOR := PASS IF
  one_distinctive_trait_is_named
  AND the_trait_is_specific_enough_that_another_operator_could_preserve_it
  AND the_trait_is_not_just("clean" OR "modern" OR "premium")

ANTI_GENERIC_FRONTEND := PASS IF
  avoid_list_names_generic_patterns_to_reject
  AND the_same_visual_formula_could_fit_any_saas_landing_page = FALSE
  AND default_font_gradient_and_card_stack_habits_are_rejected_when_they_weaken_identity

THEME_COMPARISON := PASS IF
  at_least_two_contrasted_theme_systems_are_compared_before_approval
  AND each_option_names(palette_direction AND typography_pairing)
  AND the_user_visible_difference_between_options_is_explicit
  AND recommendation_is_named_before_commitment

FAIL IF
  aesthetic_direction_is_only_mood_words
  OR memorable_differentiator_is_missing
  OR theme_system_choice_is_committed_without_visible_comparison
  OR anti_generic_constraints_are_implicit
  OR visual_direction_requires_implementation_details_before_the_product_choice_is_clear
```
