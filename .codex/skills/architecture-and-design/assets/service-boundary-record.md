# Service Boundary Record

```text
BOUNDARY := {
  seam,
  current_state_evidence,
  target_state_framing,
  entrypoint,
  activation_events,
  owner,
  consumers
}

CONTRACT := {
  allowed_dependencies,
  public_interface,
  compatibility_expectations,
  message_or_command_ids,
  workspace_artifact_rules
}

OPERATIONS := {
  observability,
  artifact_classes_readers_writers_and_lifecycle,
  path_normalization_or_workspace_fallback,
  migration_path,
  timeout_and_failure_handling,
  streaming_and_cancel_ownership,
  rollback_plan,
  rollback_owner,
  next_skill
}
```
