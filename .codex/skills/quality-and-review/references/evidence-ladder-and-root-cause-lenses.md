# Evidence Ladder And Root Cause Lenses

Select tests for the meaningful regression they can expose at the affected consumer boundary. Reading internal code can reveal missing cases, but assertions should protect observable results rather than every helper name or call sequence. A behavior-preserving restructuring should not force unrelated test rewrites merely because implementation details moved.

Keep a reproduction of current behavior distinct from the specification of the intended change. Match the verification mechanism to the uncertainty: use real persistence or an integration fixture where that interaction matters, and keep synthetic data and clocks controlled enough to explain failures. Do not use a high coverage count, a passing mock, or a planned experiment as a substitute for the actual acceptance evidence.

A check that passes immediately can still protect current behavior; do not confuse it with evidence that a requested behavioral change has occurred. Inspect impact through callers, shared mutable state and aliases, dynamic dispatch, and externally observable I/O or events before choosing the verification boundary. For test-enabling edits, distinguish available build or source checks from observed behavior and keep the limitation visible until baseline behavior can be checked.

Evidence remains useful while the changed state, claimed outcome, and relevant environment remain covered. Repeat invalidated checks and required project acceptance, rather than rerunning an unrelated full suite for every status message. A narrower result supports a narrower claim.

For a regression test written after a functional change, inspect its expected failure on an isolated pre-change comparison before claiming that it catches the defect. An initially passing preservation baseline has a different purpose. Review test-enabling edits for unchanged production wiring, initialization and failure timing, and error propagation; a build alone cannot establish those properties. An unavailable environment must be named with its unverified scope, rather than inferred from inconvenient setup.

Judge test suite quality by four multiplicative attributes—protection against regressions, resistance to refactoring, fast feedback, and maintainability—where resistance to refactoring is non-negotiable because false alarms erode trust in test failures. Prefer output-based tests first, state-based tests second, and communication-based interaction tests only for unmanaged external dependencies at the outermost consumer-owned adapter edge. Never assert interactions on stubs, never mock in-process domain collaborators or managed dependencies such as an application-owned database, and verify database integration with separate transaction or unit-of-work scopes across arrange, act, and assert. Verify support logging only when log entries are an explicit externally observable contract for operators or external consumers, and never unit-test developer diagnostic logging.

Use this reference when review, debugging, or acceptance needs a disciplined reasoning lens before a fix or completion claim.

```text
EVIDENCE_LADDER := [
  inspect_changed_source,
  inspect_runtime_or_generated_artifact,
  reproduce_or_query_real_data,
  run_focused_test_or_trace,
  run_full_acceptance_command,
  ask_user_only_when_access_or_intent_is_missing
]

MAP_TERRITORY_GATE := PASS IF
  trusted_map IS named(doc OR test OR diagram OR comment OR recall)
  AND territory IS verified(source OR runtime OR data OR artifact)
  AND delta_changes_next_action IS recorded

MAP_TERRITORY_GATE := FAIL IF
  reasoning_continues_from_description_after_runtime_or_source_contradicts_it
  OR same_verified_path_is_rechecked_without_new_reason

HYPOTHESIS_DIFFERENTIAL := PASS IF
  symptom_has_multiple_plausible_causes
  AND hypotheses_are_specific_to(file OR function OR config OR invariant OR data_path)
  AND each_hypothesis_has(cheap_observation, falsifier)
  AND observation_order_is_ranked_by(likelihood, cheapness, discrimination_power)

HYPOTHESIS_DIFFERENTIAL := FAIL IF
  uncertain_cause_is_patched_without_a_discriminating_observation
  OR expensive_experiment_runs_before_available_source_log_diff_or_test_observation

SELECTIVE_DEFECT_LENS := PASS IF
  defect_has_is_and_is_not_boundary
  AND affected_unaffected_dimensions_are_compared(what, where, when, extent)
  AND candidate_cause_explains_both_affected_and_unaffected_cases

SELECTIVE_DEFECT_LENS := FAIL IF
  failure_is_uniform
  OR matrix_is_filled_after_stack_trace_or_recent_diff_already_localized_cause

ROOT_CAUSE_CHAIN := PASS IF
  fault_is_already_localized
  AND each_why_answer_has_evidence_confidence_and_alternative_checked
  AND root_cause_passes_counterfactual_test
  AND recommended_action_targets_prevention_not_only_symptom

ROOT_CAUSE_CHAIN := FAIL IF
  why_chain_starts_before_fault_localization
  OR chain_stops_at_human_error
  OR answer_becomes_speculation_without_evidence

SIMPLEST_TEST_FIRST := PASS IF
  simplest_explanation_that_fits_evidence_is_tested_before_complex_theory
  AND complexity_escalates_only_after_simpler_explanation_is_falsified

ANTI_FABRICATION_REVIEW := PASS IF
  security_or_risk_finding_has(entry_point, exact_steps, observed_behavior, realized_impact)

ANTI_FABRICATION_REVIEW := FAIL IF
  report_is_padded_with_theoretical_best_practice_items_without_reproducible_path

TEST_VALUE_FOUR_PILLARS_GATE := PASS IF
  tests_verify_observable_behavior_using_output_or_state_checks_before_mocks
  AND managed_dependencies_are_checked_against_real_state_with_separate_arrange_act_assert_units_of_work
  AND unmanaged_dependencies_are_verified_at_outermost_owned_adapters_with_exact_expected_and_no_unexpected_calls
  AND expectations_use_independent_concrete_values_rather_than_duplicating_production_algorithms

TEST_VALUE_FOUR_PILLARS_GATE := FAIL IF
  tests_assert_interactions_on_stubs_or_mock_intra_system_or_managed_dependencies
  OR private_methods_or_state_are_exposed_or_production_code_adds_test_only_switches
  OR unit_tests_contain_multiple_act_sections_or_conditional_branching
  OR coverage_percentage_is_cited_as_positive_proof_over_assertion_free_or_tautological_checks

DESIGN_RED_FLAG_AUDIT_GATE := FAIL IF
  changed_code_introduces_shallow_modules_or_pass_through_methods_or_pass_through_variables
  OR temporal_decomposition_or_back_door_information_leakage_splits_shared_representations
  OR conjoined_methods_or_overcomplicated_quadrant_classes_mix_deep_decisions_with_many_collaborators
  OR interface_comments_leak_implementation_details_or_implementation_comments_merely_repeat_code
```
