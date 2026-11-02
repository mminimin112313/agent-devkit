# Contract Checklist

```text
CONTRACT := {
  seam,
  consumer_list,
  producer_list,
  failing_or_blocked_case_recorded_before_fix,
  verification_matches_preservation_or_requested_change,
  unexpected_results_are_explained_or_reported,
  preparatory_and_functional_changes_are_distinguished,
  domain_vs_orchestration_separation,
  managed_vs_unmanaged_dependency_verification,
  versioning_impact,
  compatibility_risk,
  validation_path,
  edge_handling,
  verification_after_fix
}

PASS IF
  public_contract_is_named
  AND hidden_dependency_is_avoided
  AND contract_is_parseable_or_inspectable
  AND verification_matches_preservation_or_requested_change
  AND unexpected_results_are_explained_or_reported
  AND preparatory_and_functional_changes_are_distinguished
  AND validation_path_is_covered
  AND failure_path_is_covered
  AND actionable_error_behavior_is_defined
  AND side_effect_boundary_is_isolated
  AND domain_decisions_are_testable_without_out_of_process_collaborators
  AND managed_dependencies_verify_final_state_and_unmanaged_dependencies_verify_edge_contracts
  AND consumer_impact_is_recorded
  AND idempotency_expectation_is_recorded_when_side_effects_require_it
  AND bounded_runtime_behavior_is_recorded_when_relevant
  AND runtime_proof_is_present_when_runtime_behavior_is_claimed
  AND edge_cases_are_covered
  AND performance_note_is_added_when_relevant

FAIL IF
  public_contract_is_implicit
  OR verification_matches_preservation_or_requested_change IS missing
  OR validation_path_is_missing
  OR failure_path_is_missing
  OR consumer_impact_is_missing
  OR runtime_proof_is_required_but_missing

DECISION := { approved, blockers, follow_up }
```
