# Workflow Graph And Migration Architecture

```text
ARCHITECTURE_CHECK := PASS IF
  execution_nodes_and_typed_inputs_outputs_are_named
  AND control_plane_metadata_access_is_separate_from_task_execution
  AND deferrable_human_gated_or_approval_steps_are_explicit
  AND retry_schedule_and_ownership_interactions_are_named

MIGRATION_CHECK := PASS IF
  old_execution_model_is_named
  AND new_execution_model_is_named
  AND broken_assumptions_are_listed
  AND compatibility_checks_exist_before_rollout
  AND rollback_and_observability_implications_are_recorded

FAIL IF ARCHITECTURE_CHECK = FALSE OR MIGRATION_CHECK = FALSE
```
