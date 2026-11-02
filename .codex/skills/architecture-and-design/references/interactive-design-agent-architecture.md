# Interactive Design Agent Architecture

```text
PLANES := {
  control_config_plane,
  execution_plane,
  prompt_policy_plane,
  permission_tool_plane
}

PUBLIC_OPERATOR_FACING_INTERACTIVE_SEAM := {
  host_entrypoints,
  command_or_config_ids,
  docs_seam,
  tool_server_manifest_seam,
  session_lifecycle_state_model,
  agent_runtime_ui_state_boundary_vs_generic_pane_state
}

LAYERS := {
  entrypoint,
  provider_or_controller,
  session_or_orchestration_service,
  service_layer,
  tool_or_adapter_layer,
  ui_shell,
  workspace_artifact_storage
}

PASS IF
  each_plane_is_named
  AND each_layer_has_one_owner
  AND dependency_direction_is_explicit
  AND each_field_in(PUBLIC_OPERATOR_FACING_INTERACTIVE_SEAM) IS explicit_when_relevant
  AND request_start_delta_progress_finish_error_cancel_behaviors_are_named
  AND session_lifecycle_state_model_covers(create_to_finish_or_cancel)
  AND artifact_location_and_lifecycle_are_named
  AND streaming_partial_updates_errors_and_cancel_ownership_are_explicit

FAIL IF
  host_entrypoints_or_command_or_config_ids_are_hidden_in_product_code
  OR docs_seam_is_missing_for_a_public_operator_facing_runtime
  OR tool_server_manifest_seam_is_implicit
  OR agent_runtime_state_is_mixed_with_generic_pane_state
  OR business_logic_is_hidden_in_ui_handlers
  OR adapters_define_product_behavior
  OR prompt_policy_assets_are_mixed_with_runtime_logic
  OR workspace_artifacts_live_in_application_code_paths
```
