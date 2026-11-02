# Platform Contracts

Evaluate a boundary by what a caller must know to use it correctly, including initialization order, concurrency, failure outcomes, cancellation, and durability. A short signature does not make a contract simple if those conditions remain hidden. Keep changeable representation knowledge under a clear owner so that an encoding change does not require synchronized edits across otherwise independent read and write stages.

Compare viable alternatives when the structure is genuinely unsettled and use an actual change or failure scenario to judge them. Do not add a mandatory redesign exercise to a local change whose existing boundary is already adequate.

Design module contracts to be somewhat general-purpose so the interface exposes the core mechanism needed by callers while keeping caller-specific policy up in the consumer or provider-specific details down in the adapter. Define normal-case state and range semantics so boundary inputs work naturally without proliferating special-case branches or unnecessary exceptions. Pull complexity downwards by computing safe defaults internally rather than exporting uncalibrated configuration parameters, and reduce exception surfaces by masking transient low-level failures inside the owning layer or aggregating fine-grained errors at a boundary dispatcher while failing fast on corrupted invariants.

Reserve single-implementation interfaces for unmanaged external dependencies whose interactions are externally visible and must be replaced with test doubles at the system edge. Do not introduce single-implementation interfaces for in-process domain classes or managed dependencies owned exclusively by the application, and do not thread pass-through methods or pass-through variables across layers that add no new abstraction.

```text
MINIMUM_CONTRACT_RECORD := {
  owner,
  consumers,
  current_state_evidence,
  target_state_framing,
  allowed_dependency_direction,
  module_depth_and_hidden_decisions,
  general_purpose_mechanism_vs_special_purpose_policy,
  exception_reduction_and_aggregation_strategy,
  managed_vs_unmanaged_dependency_classification,
  compatibility_expectations,
  discoverability_expectations,
  structured_response_shape,
  filtering_or_pagination_behavior,
  observability_hooks,
  migration_path,
  rollback_notes,
  transport_choice_and_runtime_boundary,
  activation_events_and_host_entrypoints,
  command_view_or_config_ids,
  docs_seam_and_operator_facing_discoverability,
  tool_server_manifest_seam,
  session_lifecycle_state_model,
  agent_runtime_ui_state_boundary_vs_generic_pane_state,
  sender_receiver_ownership,
  artifact_storage_location,
  artifact_classes_readers_writers_and_lifecycle,
  failure_behavior,
  actionable_error_behavior,
  execution_model_compatibility_expectations
}

PASS IF every_field_in(MINIMUM_CONTRACT_RECORD) IS explicit_when_relevant
  AND public_operator_facing_interactive_seam_names(host_entrypoints, command_ids, docs_seam, tool_server_manifest_seam, session_lifecycle_state_model, agent_runtime_ui_state_boundary_vs_generic_pane_state) WHEN runtime_is_interactive OR agent_driven

FAIL IF
  prompt_policy_assets_mix_with_runtime_code
  OR ui_shell_reads_or_mutates_storage_without_contract
  OR provider_service_tool_dependencies_are_implicit
  OR discoverability_or_response_shape_is_implicit_for_a_public_operator_facing_seam
  OR operator_docs_seam_is_missing_for_public_interactive_contracts
  OR mcp_or_tool_server_manifest_boundary_is_implicit
  OR session_lifecycle_state_model_is_left_for_ui_code_to_invent
  OR agent_runtime_state_is_mixed_with_generic_pane_state
  OR path_normalization_and_workspace_fallback_are_implicit
  OR pass_through_methods_or_pass_through_variables_cross_layers_without_new_abstraction
  OR uncalibrated_configuration_parameters_punt_policy_complexity_to_callers
  OR single_implementation_interfaces_are_added_for_in_process_or_managed_dependencies_without_a_second_implementation
```
