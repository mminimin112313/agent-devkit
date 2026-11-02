# Thinking Skill Absorption

Use this reference when importing mental-model or reasoning-framework skill packs.

```text
SOURCE := cc-thinking-skills@0313ee0d476bf9db2c38ad8bd11d9933a61350d4
SOURCE_SHAPE := 39 Claude Code thinking skills + eval harness + analysis docs
ABSORPTION_RULE := compile_judgment_into_existing_repo_local_owners
CATALOG_RULE := do_not_create(thinking_*) AS top_level_repo_local_skills

EVIDENCE_NOTE := {
  source_reports_zero_robust_replicated_elevate_skills,
  source_reports_trigger_vs_full_guide_parity_for_many_conceptual_skills,
  source_recommends_agent_native_boundaries_over_framework_textbooks
}

KEEP := {
  trigger_boundaries,
  when_not_to_use_gates,
  evidence_ladders,
  falsifiable_hypothesis_ordering,
  map_vs_territory_runtime_checks,
  reversible_decision_classification,
  prospective_failure_risk_review,
  opportunity_cost_and_do_nothing_comparison,
  concrete_attack_path_requirement
}

DROP := {
  parallel_model_router_namespace,
  long_mental_model_tutorials,
  human_only_facilitation_steps,
  personal_life_or_career_surfaces,
  confidence_claims_from_unreplicated_eval_results,
  static_router_tables_that_compete_with_repo_local_skills
}

OWNER_MAP := {
  thinking_archetypes -> architecture-and-design OR quality-and-review WHEN recurring_system_pattern_is_evidence_backed,
  thinking_bayesian -> quality-and-review WHEN interpreting_evidence_with_base_rate,
  thinking_bounded_rationality -> planning-and-scoping WHEN stop_rule_or_good_enough_threshold_is_needed,
  thinking_circle_of_competence -> intake-and-routing OR quality-and-review WHEN answer_requires_abstain_ask_or_fetch,
  thinking_cynefin -> intake-and-routing OR architecture-and-design WHEN approach_depends_on_clear_complicated_complex_chaotic_domain,
  thinking_debiasing -> quality-and-review WHEN committed_path_is_explaining_away_contrary_evidence,
  thinking_dual_process -> quality-and-review WHEN fast_plausible_answer_needs_verification_pass,
  thinking_effectuation -> product-and-ux WHEN novel_domain_requires_affordable_loss_exploration,
  thinking_feedback_loops -> architecture-and-design WHEN causal_loops_or_delays_change_the_design,
  thinking_fermi_estimation -> planning-and-scoping OR performance-and-complexity WHEN lookup_is_unavailable_and_order_of_magnitude_bounds_are_enough,
  thinking_first_principles -> architecture-and-design WHEN fixed_constraint_may_be_convention_not_real_constraint,
  thinking_five_whys_plus -> quality-and-review WHEN localized_fault_needs_evidence_backed_systemic_root_cause,
  thinking_inversion -> planning-and-scoping WHEN failure_paths_must_become requirements,
  thinking_jobs_to_be_done -> product-and-ux WHEN feature_direction_or_adoption_depends_on_user_job,
  thinking_kepner_tregoe -> quality-and-review WHEN selective_defect_has_is_vs_is_not_boundary,
  thinking_leverage_points -> architecture-and-design WHEN intervention_choice_in_system_has_multiple_depths,
  thinking_lindy_effect -> architecture-and-design WHEN longevity_of_dependency_or_standard_matters,
  thinking_map_territory -> quality-and-review WHEN docs_tests_diagrams_or_recall_conflict_with_runtime_or_source,
  thinking_margin_of_safety -> planning-and-scoping OR release-and-operations WHEN buffer_size_depends_on_cost_of_being_wrong,
  thinking_model_combination -> intake-and-routing WHEN more_than_one_lens_is_justified_by_distinct_blind_spots,
  thinking_model_router -> intake-and-routing AS absorbed_metadata_not_public_router,
  thinking_model_selection -> intake-and-routing AS absorbed_classification_not_public_router,
  thinking_occams_razor -> quality-and-review WHEN simplest_explanatory_test_should_run_before_complex_theory,
  thinking_ooda -> release-and-operations WHEN time_pressure_requires observe_orient_decide_act_cycle,
  thinking_opportunity_cost -> planning-and-scoping OR product-and-ux WHEN scarce_resources_have_next_best_alternative,
  thinking_pre_mortem -> planning-and-scoping OR release-and-operations WHEN plan_or_launch_failure_modes_must_be converted_to_mitigations,
  thinking_probabilistic -> quality-and-review WHEN forecast_or_risk_needs_range_and_update_condition,
  thinking_red_team -> security-review OR security-lab WHEN concrete_reproducible_attack_path_is_required,
  thinking_regret_minimization -> EXCLUDE_AS_NON_FIT WHEN personal_life_career_surface_has_no_repo_local_owner,
  thinking_reversibility -> planning-and-scoping OR architecture-and-design WHEN commitment_depth_or_rollback_cost_changes_process,
  thinking_scientific_method -> quality-and-review WHEN competing_fault_hypotheses_need_cheapest_discriminating_observation,
  thinking_second_order -> architecture-and-design OR planning-and-scoping WHEN downstream_effects_or_incentives_change_decision,
  thinking_socratic -> intake-and-routing WHEN hidden_assumption_requires_one_focused_question,
  thinking_steel_manning -> quality-and-review WHEN strongest_opposing_case_should_be_checked_before_rejection_or_agreement,
  thinking_systems -> architecture-and-design OR quality-and-review WHEN behavior_spans_components_or_feedback_loops,
  thinking_theory_of_constraints -> performance-and-complexity OR architecture-and-design WHEN one_bottleneck_sets_throughput,
  thinking_thought_experiment -> architecture-and-design WHEN scale_or_failure_scenario_cannot_be_cheaply_tested,
  thinking_triz -> architecture-and-design WHEN requirements_conflict_and_need_separation_by_time_space_or_condition,
  thinking_via_negativa -> architecture-and-design OR planning-and-scoping WHEN removing_scope_or_layer_may_be_better_than_adding
}

ABSORB_AS_RULES := PASS IF
  every_source_skill_has(owner_or_exclusion)
  AND imported_name_is_not_added_to_active_catalog
  AND destination_skill_gains_specific_gate_or_reference
  AND source_evidence_limits_are_preserved
  AND operator_can_skip_the_lens_when_direct_evidence_or_direct_fix_exists

FAIL IF
  mental_model_name_becomes_a_new_public_route_without_admission_gate
  OR framework_is_used_to_delay_file_reading_test_running_or_runtime_verification
  OR source_eval_results_are_claimed_as_proof_for_this_repo
  OR long_framework_tutorial_is_copied_without_agent_executable_stop_conditions
```
