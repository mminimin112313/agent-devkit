---
name: implementation-frontend
description: "Use when an approved route, component, or client interaction needs building, fixing, or polishing: layout, typography, color and tokens, components and states, accessibility, motion and rendering performance, and rendered-UI proof. Also use for a UI cleanup pass that must not add interface the direction did not ask for."
---

# Implementation Frontend

## Procedure

```text
STEP_0 := DECLARE(support_files := exact assets/ + references/ set OR none)
STEP_0A := READ(required_assets_and_references_before_coding)
STEP_0B := RECORD(why_each_declared_file_was_loaded)
STEP_0C := SEARCH(existing_components, tests, docs, config, routes, design_tokens, data_adapters)
INPUT := { seam, user_facing_behavior, data_contract, required_states, token_handoff, proof_plan }

IF user_facing_behavior_is_implicit OR state_coverage_is_missing THEN STOP("define the frontend seam first")
IF behavior_change_or_bug_fix AND root_cause_or_failure_mode_is_implicit THEN STOP("name the failure mode before fixing")
IF runtime_state_or_data_contract_is_uncertain THEN STOP("verify the state before coding")
IF hardcoded_address_or_environment_value_is_needed THEN ROUTE -> config_or_adapter_first
IF proof_depends_on(dynamic_ui OR browser_automation OR hydrated_dom) THEN READ(references/rendered-ui-proof.md) BEFORE guessing_selectors_or_actions

STATE_SET := NAME(loading, empty, success, error, blocked_interaction)
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
SEPARATE(pure_state_and_view_model_decisions, humble_dom_storage_and_network_orchestration)
ELIMINATE(avoidable_special_case_branches_and_pass_through_prop_drilling)

IMPLEMENT minimum_change_that_satisfies(approved_behavior)
IF adding(toast OR confirm_dialog OR helper_text OR badge OR tooltip OR banner OR animation) not_in(approved_direction) THEN READ(references/ui-restraint-and-proof.md) AND REQUIRE(named_user_failure_it_prevents)

GUARDRAILS := KEEP(
  state_local_to_usage,
  semantic_structure_intact,
  sensitive_data_out_of_client_storage,
  readable_measure_and_asset_size_expectations_named,
  primary_emphasis_beats_decorative_treatment,
  no_unapproved_interface_additions
)

IF new_dependency OR caching_layer OR rendering_strategy materially_changes_the_seam THEN ROUTE -> planning-and-scoping

VERIFY FROM user_facing_seam USING(
  targeted_tests,
  interaction_proof,
  accessibility_checks,
  responsive_checks,
  token_handoff_checks,
  media_contrast_checks
)
VERIFY(preservation_evidence_and_expected_changed_behavior) AS applicable
IF regression_test_was_added_after_functional_change THEN
  CHECK(expected_failure_on_disposable_prechange_copy_or_isolated_fix_disabled)
  KEEP(existing_work_and_live_checkout_intact)
RUN(project_required_acceptance_checks)
AUDIT(line_counts_for_changed_files)
SPLIT_OR_JUSTIFY IF component_file_lines > local_limit OR component_file_lines > 200 OR source_file_lines > 300
; why: size is a review trigger for mixed responsibilities, not a split order. A cohesive component, generated file, or data table is justified in one line; never split into pass-through wrappers to meet a number

HANDOFF := RECORD(exact_behavior, exact_files, exact_proof)

CLAIM(visual_verification) ONLY IF surface_was_rendered_and_inspected ELSE REPORT("code inspected; not rendered")

STOP("frontend delivery note is ready")
```

## Overview

Ship the frontend seam without leaking into unrelated layers.

**Core principle:** if the user-facing behavior, accessibility impact, and verification path are not explicit, the frontend change is not ready.

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
Do not start implementation from vibes. Name the route or component seam, the states that matter, the data contract, and the proof that will verify the change.
</HARD-GATE>

<NON-NEGOTIABLE>
Every run must declare its exact local `assets/` and `references/` set before execution, read the required files before coding, and record why each declared file was loaded. Unnamed support files are out of contract and must not be relied on. If no support files are needed, say `none` explicitly. Final outputs must report the declared set, the files actually read, and the files actually used.
</NON-NEGOTIABLE>

<NON-NEGOTIABLE>
Keep state as close to usage as possible, preserve semantic structure, and avoid performance work that is not backed by a user-facing bottleneck or measurable interaction risk.
</NON-NEGOTIABLE>

<DISCIPLINE-GATE>
root_cause_or_failure_mode_is_named_before_fix. verification_distinguishes_preserved_behavior_from_requested_change.

Do not delete existing work solely because a test was written later. A reviewed behavior-preserving boundary edit that enables verification is preparation, not a workaround requiring a new approval round; follow the user's authorization and project gates.
</DISCIPLINE-GATE>

<DESIGN-AND-TESTING-DISCIPLINE-GATE>
Prefer deep component and state boundaries over shallow pass-through wrappers or prop-drilling chains that add interface cost without hiding complexity. Separate general-purpose UI mechanisms from feature-specific policy, and define normal-case state models so empty, boundary, or selection states work naturally without scattered special-case branches. Keep complex state transitions, selectors, and formatting calculations in pure units verified by output-based or state-based tests, while keeping DOM, storage, and network orchestration in humble boundary hooks or controllers verified through focused integration and rendered-UI checks without mocking internal collaborator calls.
</DESIGN-AND-TESTING-DISCIPLINE-GATE>

<ANTI-PATTERN>
Do not treat a pretty happy path as frontend completeness.
</ANTI-PATTERN>

<IMPLEMENTATION-HYGIENE-GATE>
Search before coding. Do not hardcode addresses, URLs, ports, filesystem roots, endpoints, credentials, or environment-specific values in frontend logic. Keep configuration, data adapters, state, components, views, and tests separated enough to prevent god component or god store growth. Audit line counts before handoff and split oversized changed files.
</IMPLEMENTATION-HYGIENE-GATE>

## Required Reads

- You MUST read `references/implementation-guardrails.md` before coding when this skill triggers.
- You MUST read `references/ui-restraint-and-proof.md` before adding interface elements the approved direction did not name, and before claiming visual completion.
- Read `../product-and-ux/references/restraint-and-rule-intent.md` when an addition or removal is a judgment call that `ui-restraint-and-proof.md` does not settle.
- You MUST start from `assets/frontend-implementation-brief.md` before implementation.
- IF state_coverage_is_the_main_risk THEN START -> `assets/component-state-checklist.md`

## When to Use

- IF approved_route_component_or_interaction_seam_needs_building THEN USE
- IF remaining_risk_is_state_coverage_accessibility_responsiveness_or_ui_wiring THEN USE
- IF design_exists_but_exact_state_and_proof_handling_are_still_missing THEN USE
- IF new_feature OR bug_fix OR refactor OR behavior_change THEN USE

## Do Not Use

- IF request_is_open_ended_product_discovery THEN ROUTE -> product-and-ux
- IF backend_contract_is_not_stable THEN ROUTE -> architecture-and-design OR implementation-backend
- IF work_is_review_or_release_gate THEN ROUTE -> quality-and-review

## Choose Roles

- `IF default_frontend_build THEN use agents/software-engineer-frontend.md`
- `IF state_flow_or_visual_intent_needs_implementation_alignment THEN use agents/ui-ux-designer.md`
- `IF interaction_proof_accessibility_or_regression_is_weak THEN use agents/qa.md`

## Choose Assets

- `IF default_delivery_note THEN START -> assets/frontend-handoff.md`
- `IF behavior_or_visual_acceptance_is_the_gate THEN START -> assets/ui-review-checklist.md`
- `IF state_coverage_is_the_highest_risk THEN START -> assets/component-state-checklist.md`
- `IF seam_is_known_but_behavior_and_proof_need_a_build_brief THEN START -> assets/frontend-implementation-brief.md`

## Choose References

- `IF coding_guardrail_needed THEN READ -> references/implementation-guardrails.md`
- `IF adding_unrequested_ui OR polishing OR claiming_visual_completion THEN READ -> references/ui-restraint-and-proof.md`
- `IF layout_grid_hierarchy_typography_or_component_visuals_are_the_seam THEN READ -> references/ui-composition.md`
- `IF palette_roles_contrast_or_semantic_color_are_the_seam THEN READ -> references/color-systems.md`
- `IF tokens_figma_library_governance_or_design_handoff_are_the_seam THEN READ -> references/design-systems-and-figma.md`
- `IF seam_should_inherit_shared_tokens_effects_or_variants THEN READ -> references/design-system-foundations.md`
- `IF translating_approved_ux_into_props_variants_and_stateful_behavior OR emphasis_rules_need_translation THEN READ -> references/component-implementation-playbook.md`
- `IF layout_navigation_media_or_breakpoint_behavior_matters OR readable_measure_asset_size_risk_is_high THEN READ -> references/responsive-layout-patterns.md`
- `IF proof_depends_on(dynamic_ui OR browser_automation OR hydrated_dom) THEN READ -> references/rendered-ui-proof.md`
- `IF custom_interaction_focus_or_announcements_are_part_of_the_seam THEN READ -> references/aria-and-keyboard-baseline.md`
- `IF missing_states_or_blocked_interactions_are_likely THEN READ -> references/ui-state-coverage.md`
- `IF animation_rendering_cost_or_bundle_behavior_could_regress_the_ux THEN READ -> references/frontend-performance-guardrails.md`

## Output Contract

Return a frontend delivery note with:

- declared support files
- files read before coding
- why each file was loaded
- seam implemented
- states and accessibility coverage
- proof run
- preservation baseline and expected changed behavior, as applicable
- preparatory boundary changes and limits of available verification
- search evidence and uncertainty checks
- hardcoded-address prevention and extension seam used
- line-count audit and split-or-justify result
- responsive or performance notes
- interface elements added beyond the approved direction, each with the failure it prevents, and elements removed
- rendered and inspected, or code-only
- next owner or next skill
- files actually used
