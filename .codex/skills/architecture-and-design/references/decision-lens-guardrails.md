# Decision Lens Guardrails

Use this reference when architecture needs a bounded reasoning lens without importing a parallel mental-model catalog.

```text
LENS_SELECTION := {
  constraint_challenge -> first_principles,
  downstream_coupling -> second_order,
  cross_component_behavior -> systems,
  bottleneck_or_throughput -> theory_of_constraints,
  contradiction_between_requirements -> triz,
  dependency_longevity -> lindy,
  intervention_depth -> leverage_points,
  remove_vs_add_layer -> via_negativa,
  rollback_cost -> reversibility
}

GENERAL_GATE := PASS IF
  chosen_lens_answers_one_named_architecture_question
  AND direct_source_runtime_or_dependency_evidence_is_gathered_first_when_available
  AND lens_output_changes(seam OR contract OR dependency_direction OR rollback_shape)

GENERAL_GATE := FAIL IF
  lens_is_used_as_aesthetic_label
  OR framework_name_substitutes_for_tradeoff_evidence
  OR long_tutorial_delays_the_required_design_record

FIRST_PRINCIPLES_GATE := PASS IF
  alleged_constraint_is_classified_as(real_constraint OR convention)
  AND rebuild_respects_actual_law_security_cost_or_contract_limits

SECOND_ORDER_GATE := PASS IF
  design_records(immediate_effect, next_deploy_effect, at_scale_effect)
  AND incentive_or_feedback_change_is_named_when_present

SYSTEMS_GATE := PASS IF
  components_connections_delays_and_feedback_loops_are_mapped
  AND fix_in_one_component_is_checked_against_downstream_consumers

CONSTRAINT_GATE := PASS IF
  bottleneck_has_metric(queue OR utilization OR latency_share OR throughput_cap)
  AND non_constraint_optimization_is_rejected_until_constraint_moves

REVERSIBILITY_GATE := PASS IF
  decision_is_classified(one_way OR two_way OR mixed)
  AND irreversible_part_is_reduced_by(flag OR pilot OR abstraction OR staged_cutover) WHEN feasible

VIA_NEGATIVA_GATE := PASS IF
  removal_candidate_is_checked_against_current_usage_and_contract_ownership
  AND deletion_has_rollback_or_recovery_path
```
