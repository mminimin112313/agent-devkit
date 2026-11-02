# Design Note

```text
SUPPORT := {
  declared_assets,
  declared_references,
  files_read_before_decision,
  why_each_file_was_loaded,
  files_actually_used
}

TARGET := {
  seam,
  decision_owner,
  affected_roles,
  constraints,
  current_state_evidence,
  current_risks_or_bottlenecks,
  target_state_framing,
  dependency_direction,
  workflow_graph_or_node_types,
  runtime_surface,
  host_entrypoints,
  command_or_config_ids,
  docs_seam,
  tool_server_manifest_seam,
  control_plane,
  execution_plane,
  prompt_policy_plane,
  session_lifecycle_state_model,
  agent_runtime_ui_state_boundary,
  request_or_session_owner,
  workspace_artifact_boundary
}

ALTERNATIVES := {
  option_a,
  option_b,
  option_c,
  recommended_choice,
  why_losing_options_lost_now
}

TRADE_OFFS := {
  replaceability,
  hidden_coupling_risk,
  module_depth_vs_interface_cost,
  information_hiding_vs_temporal_decomposition,
  exception_reduction_and_aggregation,
  domain_vs_controller_quadrant_split,
  managed_vs_unmanaged_dependency_boundaries,
  implementation_cost,
  verification_impact,
  bridge_vs_direct_call,
  provider_vs_controller_split,
  service_vs_tool_split
}

MIGRATION := {
  first_increment,
  coexistence_or_cutover_plan,
  rollback_trigger,
  rollback_plan,
  rollback_owner
}

OBSERVABILITY := {
  seam_signals,
  error_categories,
  alert_owner,
  acceptance_metrics
}

ACCEPTANCE := {
  chosen_structure,
  entrypoint_and_dependency_direction,
  migration_or_compatibility_assumptions,
  streaming_and_cancel_contract,
  acceptance_conditions,
  recommended_next_owner,
  next_skill
}

PASS IF
  SUPPORT.declared_assets IS named_or_none
  AND SUPPORT.declared_references IS named_or_none
  AND SUPPORT.files_read_before_decision
  AND SUPPORT.why_each_file_was_loaded
  AND TARGET.seam
  AND TARGET.current_state_evidence
  AND TARGET.dependency_direction
  AND TARGET.host_entrypoints IS explicit_when_relevant
  AND TARGET.command_or_config_ids IS explicit_when_relevant
  AND TARGET.docs_seam IS explicit_when_relevant
  AND TARGET.tool_server_manifest_seam IS explicit_when_relevant
  AND TARGET.session_lifecycle_state_model IS explicit_when_relevant
  AND TARGET.agent_runtime_ui_state_boundary IS explicit_when_relevant
  AND ALTERNATIVES.recommended_choice
  AND ALTERNATIVES.why_losing_options_lost_now
  AND MIGRATION.rollback_trigger
  AND MIGRATION.rollback_owner
  AND OBSERVABILITY.seam_signals
  AND OBSERVABILITY.alert_owner
  AND ACCEPTANCE.recommended_next_owner
  AND ACCEPTANCE.next_skill

FAIL IF
  SUPPORT.files_actually_used IS missing
  OR TARGET.current_state_evidence IS generic
  OR TARGET.dependency_direction IS implicit
  OR TARGET.tool_server_manifest_seam IS implicit_when_relevant
  OR TARGET.session_lifecycle_state_model IS implicit_when_relevant
  OR MIGRATION.rollback_plan IS generic
  OR OBSERVABILITY.acceptance_metrics IS missing
```
