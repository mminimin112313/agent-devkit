---
name: architecture-and-design
description: "Use when module seams, contracts, workflow topology, or runtime design trade-offs must be decided with explicit evidence, explicit references, and explicit rollback shape before implementation starts."
---

# Architecture And Design

## Procedure

```text
1. DECLARE(support_files := exact assets/ + references/ set OR none)
2. READ(required_assets_and_references_before_deciding)
3. RECORD(why_each_declared_file_was_loaded)
4. LOAD(seam, evidence, constraints, consumers, runtime_risks)
5. IF seam_is_not_stable OR contract_is_implicit THEN STOP("stabilize the architectural target first")
6. RECORD(current_state_evidence := seam_behavior + coupling_or_bottleneck_evidence + dependency_or_metric_evidence)
7. NAME(target_seam := module_boundary OR public_api OR data_contract OR page_flow OR release_gate)
8. COMPARE(at_least_two_shapes) AND RECORD(why_losing_options_lost_now)
8A. CHECK(module_depth := interface_cost_vs_hidden_capability, information_hiding_vs_backdoor_leakage, general_purpose_mechanism_vs_special_purpose_policy, adjacent_layer_abstraction_change, pull_complexity_downwards, exception_reduction_strategy)
8B. CHECK(code_quadrant_separation := deep_decision_core_has_few_collaborators AND wide_orchestration_controller_has_low_branching_complexity AND managed_vs_unmanaged_dependencies_are_classified)
9. APPLY(decision_lens_guardrails) IF tradeoff_needs(constraint_challenge OR downstream_coupling OR cross_component_behavior OR bottleneck OR contradiction OR dependency_longevity OR rollback_cost)
10. CHECK(contract_ownership, dependency_direction, observability_and_rollback, security_exposure, downstream_consumers, host_entrypoints, command_or_config_ids, docs_seam, tool_server_manifest_seam, execution_model_compatibility)
11. RECORD(contract_discoverability, structured_response_shape, filtering_or_pagination_behavior, actionable_failure_behavior) IF public_seam_is_tool_or_api_like
12. RECORD_INTERACTIVE(host_entrypoints, command_or_config_ids, docs_seam, tool_server_manifest_seam, session_lifecycle_state_model, agent_runtime_ui_state_boundary) IF runtime_is_interactive OR agent_driven
13. APPLY_GUARDRAILS(cost_cap, timeout, retry, fallback, shadow_mode, promotion_grading) IF autonomy_or_high_cost_runtime_path = TRUE
14. RECORD_PLANES(control_plane, execution_plane, prompt_policy_plane, permission_plane) IF runtime_is_interactive OR agent_driven
15. RECORD_BRIDGE(direct_call OR command_bridge OR message_bridge) IF runtime_is_interactive OR agent_driven
16. DEFINE(evaluation_shape := discoverability_checks + lifecycle_state_checks + failure_case_checks + schema_or_structure_checks + pagination_or_filtering_checks) IF seam_exposes_tools_or_remote_contracts
17. DEFINE(migration := first_increment + coexistence_or_cutover + rollback_trigger + rollback_owner)
18. ROUTE ->
  implementation-frontend IF seam_is_client_facing
  implementation-backend IF seam_is_backend_or_contract_facing
  planning-and-scoping IF execution_boundary_is_not_yet_operable
19. STOP("design note is ready for the next owner")
```

## Overview

Design the seam before the diff.

**Core principle:** if the seam, contract, current-state evidence, required support files, or trade-off is implicit, the design is not ready.

<PORTABILITY-MANDATE>
Behave like a conservative repo-local coding agent. Do not guess hidden state, host-only tools, or machine-local services. Prefer portable repo-local files and explicit evidence over unstated environment assumptions. If the path would vary by host, shell, or operating system, choose the narrower portable path or stop and name the missing fact.
</PORTABILITY-MANDATE>


<ROOT-CAUSE-SOLUTION-HOOK>
IF problem_solving_requires(fallback OR workaround OR bypass OR temporary_patch) THEN
  ASK_USER_APPROVAL(reason, scope, risk, rollback_plan) BEFORE applying_non_root_solution
  RECORD(root_cause_status := confirmed OR hypothesis_only OR blocked)
  PREFER(root_cause_fix) OVER(symptom_workaround)
  STOP("fallback or workaround requires explicit user approval and a root-cause plan") IF approval_is_missing
</ROOT-CAUSE-SOLUTION-HOOK>


<HARD-GATE>
Do not route to implementation while the public seam, replacement boundary, dependency direction, rollback shape, or verification shape are still implicit.
IF seam_is_not_stable OR contract_is_implicit THEN STOP("stabilize the architectural target first")

Do not let implementation discover contract edge cases. Do not leave observability or rollback generic. Do not claim the architecture is "obvious" to skip alternatives.
</HARD-GATE>

<NON-NEGOTIABLE>
Every run must declare its exact local `assets/` and `references/` set before execution, read the required files before making the decision, and record why each declared file was loaded. Unnamed support files are out of contract and must not be relied on. If no support files are needed, say `none` explicitly. Final outputs must report the declared set, the files actually read, and the files actually used.
</NON-NEGOTIABLE>

<NON-NEGOTIABLE>
Record current-state evidence, target-state framing, migration path, rollback plan, observability baseline, and the recommended next owner.
</NON-NEGOTIABLE>

<NON-NEGOTIABLE>
When the seam exposes tools, APIs, or service contracts to other operators, record discoverability, structured response shape, filtering or pagination behavior, and actionable failure behavior.
</NON-NEGOTIABLE>

<MODULE-DEPTH-AND-TESTABILITY-GATE>
Prefer deep modules whose formal and informal interface cost is small relative to the capability and changeable design decisions they hide. Reject shallow modules, pass-through methods, pass-through variables, temporal decomposition across stages that share representation knowledge, and single-implementation interfaces for in-process or managed dependencies when no genuine second implementation or unmanaged mock boundary exists. Pull complexity downwards instead of exporting uncalibrated tuning parameters to callers, reduce exception-handling surfaces by defining edge cases into normal semantics where safe or masking and aggregating low-level errors at owning boundaries, and separate high-complexity domain or algorithmic decisions from collaborator-heavy out-of-process orchestration so no unit is simultaneously deep in branching logic and wide in collaborators.
</MODULE-DEPTH-AND-TESTABILITY-GATE>

<ANTI-PATTERN>
Do not present architecture as stack preference, code proximity, or taste.
</ANTI-PATTERN>

## Red Flags

These thoughts mean STOP: you're rationalizing.

| Thought | Reality |
|---------|---------|
| "The architecture is obvious" | If the trade-off matters, alternatives must still be named and rejected. |
| "Implementation can discover the contract edges" | That is a design miss, not implementation work. |
| "Generic logging and rollback notes are enough" | Generic notes are not a baseline. Name boundary, owner, signal, and trigger. |
| "I declared the reference files, so that's enough" | Declared is not read. Read is not used. Record all three. |
| "Current-state evidence can just be intuition" | Evidence must be named, not implied. |
| "We can tighten dependency direction later" | Hidden dependency direction becomes hidden coupling. |
| "Rollback will be easy because the change is small" | Small changes can still have large blast radius. Write the rollback shape. |
| "I do not need a reference because I know this area" | Required references exist to prevent stale recall and shallow design. |
| "Splitting by execution order makes the design cleaner" | Temporal decomposition leaks shared format or representation knowledge across stages; group by hidden design decision instead. |
| "Adding an interface for every class decouples the system" | Single-implementation interfaces for in-process or managed dependencies add indirection without abstraction; reserve single-implementation interfaces for unmanaged external boundaries. |
| "We can expose a config parameter so callers decide" | Exporting uncalibrated tuning parameters pushes complexity upwards instead of solving it inside the module. |

## Required Reads

- You MUST start from `assets/design-note.md` before proceeding.
- You MUST read `assets/architecture-review-checklist.md` before finalizing the design note.
- You MUST read the relevant reference before proceeding:
  - `references/service-decomposition.md` when split versus merge is the main decision
  - `references/platform-contracts.md` when shared contract or host ownership changes
  - `references/interactive-design-agent-architecture.md` when the seam is interactive, operator-facing, or agent-driven
  - `references/ai-routing-guardrails.md` when autonomy, cost, retry, or fallback rules matter
  - `references/observability-and-reliability-baseline.md` when rollback or runtime evidence shapes the design
  - `references/decision-lens-guardrails.md` when a bounded reasoning lens is needed for a trade-off without creating a parallel thinking-skill route

## When to Use

- IF module_split OR contract_change OR adapter_choice IS unsettled THEN USE
- IF UX_structure AND technical_structure MUST align before build THEN USE
- IF reliability OR security OR rollback shape changes with the design THEN USE

## Do Not Use

- IF request_is_raw_intake THEN ROUTE -> intake-and-routing
- IF work_is_routine_implementation_with_no_structural_choice THEN ROUTE -> implementation-backend OR implementation-frontend
- IF work_is_release_or_runtime_triage THEN ROUTE -> release-and-operations

## Choose Roles

- `IF system_boundary OR replaceability dominates THEN use agents/cto.md`
- `IF design_must_become_execution_ready THEN use agents/tech-lead.md`
- `IF UX_structure_must_align_with_system_shape THEN use agents/ui-ux-designer.md`
- `IF comparing_technical_shapes THEN use agents/architect.md`
- `IF autonomy_or_runtime_cost_controls_matter THEN use agents/guardrail-reviewer.md`

## Choose Assets

- `IF default_design_record THEN START -> assets/design-note.md`
- `IF readiness_check THEN START -> assets/architecture-review-checklist.md`
- `IF new_package_or_module_root THEN START -> assets/package-scaffold.md`
- `IF multi_owner_boundary THEN START -> assets/module-ownership.md`
- `IF automation_or_routing_guardrails THEN START -> assets/ai-guardrail-scorecard.md`
- `IF service_or_api_boundary THEN START -> assets/service-boundary-record.md`

## Choose References

- `IF split_or_consolidate_decision THEN READ -> references/service-decomposition.md`
- `IF shared_contract_or_platform_boundary THEN READ -> references/platform-contracts.md`
- `IF public_seam_must_be_discoverable_or_machine-readable THEN READ -> references/platform-contracts.md`
- `IF IDE_webview_agent_or_design_runtime THEN READ -> references/interactive-design-agent-architecture.md`
- `IF controller_service_adapter_ui_responsibilities_are_leaking THEN READ -> references/provider-service-tool-separation.md`
- `IF graph_shaped_or_execution_model_change THEN READ -> references/workflow-graph-and-migration-architecture.md`
- `IF autonomy_cost_retry_or_fallback_matters THEN READ -> references/ai-routing-guardrails.md`
- `IF runtime_evidence_or_rollback_shape_matters THEN READ -> references/observability-and-reliability-baseline.md`
- `IF mental_model_lens_would_help_tradeoff THEN READ -> references/decision-lens-guardrails.md`

## Output Contract

Return a design note with:

- declared support files
- files read before the decision
- why each file was loaded
- current-state evidence
- target seam
- alternatives considered
- why losing options lost
- chosen structure
- explicit dependency direction
- discoverability and structured response expectations when relevant
- host entrypoints and command or config ids when relevant
- docs seam and tool-server manifest seam when relevant
- session lifecycle state model when runtime is interactive or agent-driven
- agent-runtime UI state boundary versus generic pane state when relevant
- explicit observability baseline
- evaluation shape for remote or tool-like seams when relevant
- migration path
- rollback trigger and rollback owner
- acceptance conditions
- recommended next owner
- next skill
- files actually used

## Supporting Assets

Local Roles:
- `agents/cto.md`
- `agents/tech-lead.md`
- `agents/ui-ux-designer.md`
- `agents/architect.md`
- `agents/guardrail-reviewer.md`

Local Assets:
- `assets/design-note.md`
- `assets/package-scaffold.md`
- `assets/module-ownership.md`
- `assets/architecture-review-checklist.md`
- `assets/ai-guardrail-scorecard.md`
- `assets/service-boundary-record.md`

Local References:
- `references/service-decomposition.md`
- `references/platform-contracts.md`
- `references/interactive-design-agent-architecture.md`
- `references/provider-service-tool-separation.md`
- `references/workflow-graph-and-migration-architecture.md`
- `references/ai-routing-guardrails.md`
- `references/observability-and-reliability-baseline.md`
- `references/decision-lens-guardrails.md`

## Promote Recurring Lessons

- design heuristics -> `SKILL.md`
- role-specific design behavior -> `agents/*.md`
- reusable decision assets -> `assets/*.md`
