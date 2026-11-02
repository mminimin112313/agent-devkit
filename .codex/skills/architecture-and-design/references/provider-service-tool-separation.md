# Provider Service Tool Separation

Keep business and algorithmic decision-making inside pure or in-memory domain services while keeping out-of-process coordination inside humble controllers and consumer-owned tool adapters. When an orchestration sequence requires intermediate checks before loading or mutating additional external state, guard domain mutations with explicit `CanExecute` precondition checks on the domain object and record state transitions as immutable past-tense domain events rather than injecting out-of-process dependencies into the domain layer or scattering business rules across controllers.

Wrap third-party libraries that access unmanaged external dependencies behind a narrow adapter owned by the application so external API upgrades and interaction tests stay confined to the outermost boundary.

```text
PROVIDER_CONTROLLER := owns(ui_events, routing, coordination, transaction_or_unit_of_work_commit, domain_event_dispatch) AND NOT owns(deep_business_rules OR storage_formats)
SESSION_ORCHESTRATOR := owns(request_lifecycle, history_normalization, abort_control, stream_fan_out) AND NOT hide_inside(provider_just_because_it_talks_to_ui)
SERVICE := owns(domain_workflow, decision_logic, invariant_preconditions, domain_events, input_output_normalization) AND PASS IF testable_without_ui_shell_or_out_of_process_dependencies
TOOL_ADAPTER := owns(external_commands_apis_filesystems_platform_calls) AND isolates(side_effects, platform_specific_details, third_party_sdk_surface)
UI_SHELL := owns(rendering, user_input_collection) AND NOT source_of_truth_for(workflow_rules)

FAIL IF
  controller_carries_deep_business_rules
  OR domain_service_calls_out_of_process_dependencies_directly
  OR tool_adapter_decides_product_behavior
  OR third_party_unmanaged_client_types_leak_across_domain_or_controller_signatures
  OR ui_shell_becomes_workflow_source_of_truth
```
