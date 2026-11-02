# Service Decomposition

Judge decomposition by module depth and information hiding rather than file count or execution order. A split improves the system when each resulting module hides a changeable representation, protocol, or policy behind an interface that is much simpler than its implementation. Splitting by execution sequence alone creates temporal decomposition and back-door leakage when separate read, transform, and write stages still share unstated format assumptions.

Separate code that is deep in decision complexity or domain significance from code that is wide in mutable or out-of-process collaborators. Keep domain models and algorithms free of out-of-process dependencies so they can be verified through direct outputs or in-memory state, and keep controllers and orchestrators thin so they coordinate storage and external transports without owning deep branching rules. Break circular dependencies between services by returning plain value objects or recording immutable past-tense domain events rather than passing caller callbacks across boundaries.

```text
PASS IF split_reduces_hidden_coupling
  AND contract_is_clear_between_producer_and_consumer
  AND lifecycle_failure_mode_or_scaling_needs_are_meaningfully_different
  AND current_state_evidence_shows_the_split_improves_replaceability
  AND each_module_hides_a_distinct_changeable_design_decision
  AND deep_domain_or_algorithm_logic_is_separated_from_wide_collaborator_orchestration
  AND dependency_graph_remains_acyclic_with_minimal_indirection_layers

FAIL IF split_only_renames_layers
  OR shared_state_chatter_remains_constant
  OR ownership_boundary_is_not_meaningful
  OR complexity_is_added_only_for_style
  OR split_follows_temporal_execution_order_while_sharing_representation_knowledge
  OR resulting_methods_or_classes_are_conjoined_and_cannot_be_understood_independently
  OR a_single_unit_combines_high_branching_complexity_with_many_out_of_process_collaborators
  OR callback_cycles_couple_producer_and_consumer_lifecycles

IF runtime_is_interactive THEN CHECK(
  workspace_event_entrypoint,
  provider_or_controller,
  session_orchestration_service,
  domain_service,
  tool_adapter_wrappers,
  webview_or_client_shell,
  workspace_local_artifact_storage,
  workflow_nodes_and_typed_edges
)
```
