# Risk And Commitment Lenses

Use this reference when a plan needs commitment sizing, risk discovery, resource trade-off, or stopping rules.

```text
PRE_MORTEM_GATE := PASS IF
  plan_is_significant_or_launch_affecting
  AND failure_is_stated_as_already_happened
  AND concrete_failure_modes_are_generated_before_ranking
  AND top_risks_become(plan_steps OR mitigations OR proof_checkpoints)

PRE_MORTEM_GATE := FAIL IF
  only_generic_risks_are_listed
  OR automated_existing_gates_are_relisted_without_plan_change

REVERSIBILITY_GATE := PASS IF
  active_decision_is_classified(two_way OR one_way OR mixed)
  AND two_way_decisions_are_not_overplanned
  AND one_way_decisions_name_deliberation_owner_and_rollback_limit

OPPORTUNITY_COST_GATE := PASS IF
  next_best_alternative_is_named
  AND do_nothing_option_is_explicit
  AND scarce_resource_cost_includes(time OR people OR money OR attention)

MARGIN_GATE := PASS IF
  base_estimate_is_named
  AND uncertainty_range_or_failure_cost_is_named
  AND buffer_size_matches_cost_of_being_wrong
  AND measurable_unknowns_are_measured_before_padding

BOUNDED_RATIONALITY_GATE := PASS IF
  search_or_research_can_expand_unbounded
  AND good_enough_threshold_stop_condition_and_recovery_path_are_defined_before_execution

FERMI_GATE := PASS IF
  value_is_not_lookupable_in_current_context
  AND estimate_is_order_of_magnitude_only
  AND decomposition_assumptions_are_visible
```
