# Scope Control Rules

```text
PASS IF
  approved_inputs_are_the_starting_point
  AND audience_is_named
  AND target_seam_is_defined_before_tasks
  AND non_goals_are_explicit
  AND source_to_acceptance_to_proof_is_traceable
  AND acceptance_is_observable
  AND one_slice_maps_to_one_proof_path
  AND the_current_step_has_a_clean_stop_point

FAIL IF
  while_were_here_logic_appears
  OR future_proofing_replaces_scope_control
  OR hidden_refactors_have_no_acceptance_owner
  OR stale_plan_or_stale_approval_is_reused_without_refresh
  OR new_tasks_have_no_source_input_or_proof_path
  OR the_plan_expands_because_the_next_step_is_vague

ROUTE -> re_decomposition IF active_step_is_not_executable_without_guesswork
ROUTE -> re_decomposition IF one_step_hides_multiple_proof_paths
ROUTE -> re_decomposition IF a_blocker_forces_a_meaningful_route_change
```
