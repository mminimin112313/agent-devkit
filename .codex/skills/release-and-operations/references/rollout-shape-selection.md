# Rollout Shape Selection

What changed should determine the rollout shape.

```text
CHOOSE_THE_CHEAPEST_SAFE_PATH :=
  code_only_or_config_only_change -> prefer_narrowest_rollout_path
  dependency_or_image_change -> prefer_rebuild_aware_rollout_and_stronger_rollback_notes
  environment_or_topology_change -> prefer_restart_readiness_and_recovery_planning
  stateful_workflow_or_data_contract_change -> consider(backfill, replay, queue_drain, stateful_cutover) AS first_class_rollout_shapes

RECORD_EXPLICITLY := {
  chosen_rollout_shape,
  rebuild_or_restart_trigger,
  stateful_cutover_replay_or_backfill_trigger,
  queue_or_serialization_risk,
  post_deploy_monitoring_owner,
  rollback_trigger_and_owner
}

PASS IF
  rollout_shape_follows_the_change_type
  AND every_field_in(RECORD_EXPLICITLY) IS explicit_when_relevant
  AND monitoring_owner_and_rollback_owner_are_named

FAIL IF
  rollout_shape_is_selected_by_habit_instead_of_change_shape
  OR stateful_transition_risk_is_implicit
  OR rollback_trigger_is_missing
```
