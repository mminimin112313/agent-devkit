---
name: implementation-backend
description: "Use when a chosen backend seam such as an API, job, adapter, or data contract needs implementation and contract-safe verification."
---

# Implementation Backend

## Procedure

```text
STEP_0 := DECLARE(support_files := exact assets/ + references/ set OR none)
STEP_0A := READ(required_assets_and_references_before_coding)
STEP_0B := RECORD(why_each_declared_file_was_loaded)
STEP_0C := SEARCH(existing_implementations, tests, docs, config, adapters, environment_patterns)
INPUT := { seam, dependencies, consumers, rollback_sensitivity, runtime_expectations }

IF seam_is_not_explicit OR verification_path_is_missing THEN STOP("clarify the backend seam first")
IF behavior_change_or_bug_fix AND root_cause_or_failure_mode_is_implicit THEN STOP("name the failure mode before fixing")
IF runtime_state_or_dependency_behavior_is_uncertain THEN STOP("verify the state before coding")
IF hardcoded_address_or_environment_value_is_needed THEN ROUTE -> config_or_adapter_first

BOUNDARY := DEFINE(
  validation,
  error_shape,
  structured_response_shape,
  discoverability,
  filtering_or_pagination_behavior,
  side_effects,
  data_assumptions,
  compatibility_risk
)

IF runtime_behavior_matters THEN
  RECORD(latency, retries, batching, duplicates, idempotency, baseline_evidence)

IF existing_behavior_must_be_preserved THEN
  CAPTURE(current_observable_behavior_with_checks_that_may_pass_initially)
IF requested_behavior_differs_from_current_behavior THEN
  RECORD(expected_change_and_current_failure_or_missing_behavior)
  PREFER(failing_regression_test_before_functional_change) WHEN meaningful_and_feasible
IF dependency_coupling_blocks_verification THEN
  MAKE(smallest_reviewed_behavior_preserving_boundary_change)
  CHECK(build_types_source_and_available_observations)
  CAPTURE(behavior_baseline_before_functional_change)
  IF behavior_baseline_is_unavailable THEN REPORT(blocked_behavior_verification) AND STOP_BEFORE_FUNCTIONAL_CHANGE()
TRACE(affected_callers, shared_mutable_state_and_aliases, inheritance_and_dynamic_dispatch, IO_and_events)
SEPARATE(test_enablement, structural_change, functional_change) WITH focused_checks_between_them
SEPARATE(deep_domain_or_algorithm_decisions, humble_out_of_process_orchestration)
CLASSIFY(dependencies := in_process OR managed_out_of_process OR unmanaged_external)
ELIMINATE(avoidable_special_case_branches_and_pass_through_plumbing)

IMPLEMENT minimum_change_that_satisfies(seam)

IF change_widens_into_architecture OR cross_consumer_redesign THEN ROUTE -> planning-and-scoping

VERIFY FROM owned_seam USING(targeted_tests, contract_checks, runtime_or_compatibility_proof)
VERIFY(preservation_evidence_and_expected_changed_behavior) AS applicable
IF regression_test_was_added_after_functional_change THEN
  CHECK(expected_failure_on_disposable_prechange_copy_or_isolated_fix_disabled)
  KEEP(existing_work_and_live_checkout_intact)
RUN(project_required_acceptance_checks)
AUDIT(line_counts_for_changed_files)
SPLIT_OR_JUSTIFY IF source_file_lines > local_limit OR source_file_lines > 300

HANDOFF := RECORD(changed_contract, changed_files, consumers, remaining_risk)

STOP("backend delivery note is ready")
```

## Overview

Ship the backend seam without smuggling in architectural drift.

**Core principle:** if the contract, dependency boundary, edge handling, or verification seam is vague, the backend change is not ready.

Choose verification that can expose a meaningful regression at the affected boundary. A preservation check may pass from its first run; a check for a requested change should distinguish the old result from the intended result.

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
Do not implement a backend change until the public seam, allowed dependencies, data assumptions, and verification path are explicit.
</HARD-GATE>

<NON-NEGOTIABLE>
Every run must declare its exact local `assets/` and `references/` set before execution, read the required files before coding, and record why each declared file was loaded. Unnamed support files are out of contract and must not be relied on. If no support files are needed, say `none` explicitly. Final outputs must report the declared set, the files actually read, and the files actually used.
</NON-NEGOTIABLE>

<NON-NEGOTIABLE>
If runtime behavior matters, record baseline evidence, consumer impact, idempotency expectations, and bounded runtime behavior before calling the seam complete.
</NON-NEGOTIABLE>

<NON-NEGOTIABLE>
If the seam is operator-facing or integration-facing, record discoverability, structured response or schema expectations, filtering or pagination behavior, and actionable error shape before calling it complete.
</NON-NEGOTIABLE>

<DISCIPLINE-GATE>
root_cause_or_failure_mode_is_named_before_fix. verification_distinguishes_preserved_behavior_from_requested_change.

Do not delete existing work solely because a test was written later. A reviewed behavior-preserving boundary edit that enables verification is preparation, not a workaround requiring a new approval round; follow the user's authorization and project gates.
</DISCIPLINE-GATE>

<DESIGN-AND-TESTING-DISCIPLINE-GATE>
Keep modules deep and interfaces simple for the common case. Separate complex domain or algorithmic decisions from out-of-process orchestration so no class or function is both high in branching complexity and wide in collaborators. Eliminate special cases by defining normal-case state and range semantics cleanly rather than piling on conditional branches. When modifying tightly coupled legacy code, locate narrow pinch points or isolate new behavior in extracted sprout or wrap units rather than building brittle wide-harry test setups. Verify domain and algorithmic code with output-based or state-based tests, verify managed dependencies such as application databases against real state using separate transaction or unit-of-work scopes across arrange, act, and assert, and use mocks or spies only on consumer-owned adapters at unmanaged external boundaries. Inject time and execution context explicitly as values or services rather than reading ambient static state.
</DESIGN-AND-TESTING-DISCIPLINE-GATE>

<ANTI-PATTERN>
Do not hide schema drift, null handling, compatibility risk, or undocumented contract changes behind passing tests.
</ANTI-PATTERN>

<IMPLEMENTATION-HYGIENE-GATE>
Search before coding. Do not hardcode addresses, URLs, IPs, ports, filesystem roots, credentials, endpoints, or environment-specific values in backend logic. Prevent god class growth by keeping configuration, adapters, domain logic, orchestration, persistence, and tests in separate seams when those concerns exist. Audit line counts before handoff and split oversized changed files.
</IMPLEMENTATION-HYGIENE-GATE>

## Required Reads

- You MUST read `references/implementation-guardrails.md` before coding when this skill triggers.
- You MUST start from `assets/contract-checklist.md` before implementation.
- IF data_movement_or_lineage_risk_dominates THEN SWITCH -> `assets/pipeline-review-checklist.md`

## When to Use

- IF public_api OR job OR adapter OR persistence_seam IS chosen AND needs_building THEN USE
- IF data_shape OR compatibility OR null_handling IS now implementation_work THEN USE
- IF architecture_is_settled AND remaining_risk_is_contract_safe_delivery THEN USE
- IF new_feature OR bug_fix OR refactor OR behavior_change THEN USE

## Do Not Use

- IF seam_is_not_chosen THEN ROUTE -> architecture-and-design OR planning-and-scoping
- IF work_is_frontend_behavior THEN ROUTE -> implementation-frontend
- IF work_is_release_approval THEN ROUTE -> quality-and-review OR release-and-operations

## Choose Roles

- `IF default_backend_build THEN use agents/software-engineer-backend.md`
- `IF shared_infrastructure_or_cross_service_contract THEN use agents/platform.md`
- `IF contract_proof_is_the_weak_point THEN use agents/qa.md`
- `IF ETL_lineage_ingestion_or_schema_drift_sensitive THEN use agents/data-pipeline-reviewer.md`

## Choose Assets

- `IF default_delivery_note THEN START -> assets/backend-handoff.md`
- `IF contract_safe_completion_gate THEN START -> assets/contract-checklist.md`
- `IF data_movement_or_pipeline_behavior_dominates THEN START -> assets/pipeline-review-checklist.md`
- `IF endpoint_or_public_interface_changed THEN START -> assets/api-change-note.md`

## Choose References

- `IF coding_guardrail_needed THEN READ -> references/implementation-guardrails.md`
- `IF dependency_direction_or_seam_shape_needs_contract_check THEN READ -> references/backend-architecture-review.md`
- `IF seam_is_operator_facing_or_query_shaped THEN READ -> references/backend-architecture-review.md`
- `IF seam_is_job_workflow_or_producer_consumer_chain THEN READ -> references/workflow-job-delivery.md`
- `IF reliability_idempotency_or_data_freshness_matter THEN READ -> references/data-pipeline-reliability.md`
- `IF fields_provenance_or_schema_evolution_changed THEN READ -> references/schema-and-lineage-rules.md`
- `IF docs_or_handoff_are_vague_after_code THEN READ -> references/backend-docs-gates.md`

## Output Contract

Return a backend delivery note with:

- declared support files
- files read before coding
- why each file was loaded
- seam implemented
- contracts and edge cases covered
- discoverability, structured response, and error behavior when relevant
- proof run
- preservation baseline and expected changed behavior, as applicable
- preparatory boundary changes and limits of available verification
- search evidence and uncertainty checks
- hardcoded-address prevention and extension seam used
- line-count audit and split-or-justify result
- compatibility or consumer risk
- docs or release implications
- next owner or next skill
- files actually used
