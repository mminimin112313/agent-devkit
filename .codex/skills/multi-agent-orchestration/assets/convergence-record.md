# Convergence Record

```text
PROGRAM := {
  objective,
  orchestrator,
  acceptance_owner,
  shutdown_owner,
  current_phase,
  shutdown_condition
}

SLICE_RETURN := {
  slice,
  owner,
  declared_identity,
  status,
  required_skills,
  fresh_dispatch_context,
  proof,
  blocker,
  return_summary,
  spec_review_status,
  code_quality_review_status,
  dispatched_support_paths,
  actual_support_paths_used,
  dispatch_deviations,
  next_action
}

INTEGRATION := {
  merge_strategy,
  convergence_order,
  integration_owner,
  convergence_owner,
  review_path,
  conflict_check,
  remaining_risks
}

PASS IF
  PROGRAM.acceptance_owner
  AND PROGRAM.shutdown_owner
  AND PROGRAM.shutdown_condition
  AND INTEGRATION.merge_strategy
  AND INTEGRATION.convergence_order
  AND INTEGRATION.integration_owner
  AND INTEGRATION.convergence_owner
  AND all_implementation_slices_have_spec_review_then_code_quality

FAIL IF
  INTEGRATION.merge_strategy IS implicit
  OR INTEGRATION.convergence_owner IS missing
  OR INTEGRATION.review_path IS missing
  OR PROGRAM.shutdown_condition IS implicit
  OR any(SLICE_RETURN.dispatch_deviations_hidden)
```
