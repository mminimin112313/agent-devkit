# UX Research Methods

Choose the smallest method that can reduce the active product risk.

```text
QUESTION_FIRST := PASS IF
  research_question_is_written_before_method_selection
  AND segment_scope_is_recorded
  AND evidence_strength_goal_is_recorded
  AND likely_limitations_are_recorded

METHOD_SELECTION :=
  interviews -> uncover_goals_language_and_decision_criteria
  usability_tests -> expose_friction_in_a_known_flow
  prototype_reviews -> test_hierarchy_interaction_and_comprehension_before_build
  first_click_tests -> validate_navigation_and_emphasis_against_user_expectations
  concept_comparison -> compare_two_or_three_plausible_directions_before_implementation
  surveys -> measure_prevalence_after_themes_already_exist
  analytics_review -> validate_behavioral_scale_drop_off_and_frequency

RESEARCH_SPINE :=
  1 -> state_product_decision_at_risk
  2 -> write_exact_research_questions
  3 -> define_participant_criteria_and_exclusion_rules
  4 -> choose_method_and_justify_it
  5 -> define_artifact_under_review(live_product, wireframe_or_prototype, message_or_content_draft, mobile_and_desktop_variants_when_layout_differs_materially)
  6 -> write_repeatable_protocol
  7 -> synthesize_findings_with(evidence_strength, limitations, segment_scope, implication)

GUARDRAILS := PASS IF
  accessibility_and_inclusion_questions_are_included_when_the_flow_can_exclude_users
  AND at_least_one_mobile_width_review_happens_when_small_screen_flow_changes_meaningfully
  AND low_fidelity_wireframes_are_used_when_flow_shape_matters_more_than_surface_polish
  AND hierarchy_spacing_and_labeling_comprehension_issues_are_tracked_before_visual_polish_discussions
  AND bias_risks_are_named(convenience_sampling, leading_prompts, tiny_samples)
  AND quotes_are_kept_as_evidence_not_the_conclusion
  AND every_finding_ends_with(action OR decision OR open_question)
```
