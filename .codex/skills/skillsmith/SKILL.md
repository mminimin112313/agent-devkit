---
name: skillsmith
description: "Use when creating or revising a repo-local skill package so its triggers, support files, and output contract are explicit and reusable."
---

# Skillsmith

## Procedure

```text
INPUT := { explicit_user_request, recurring_job, raw_materials, failure_modes, output_contract, coverage_proof }
SUPPORT := { declared_files, files_read_before_revision, why_each_file_was_loaded }
STYLE_RULES := LOAD(references/pseudocode-style-rules.md) IF instruction_style_is_under_revision
OVERLAP_RULES := LOAD(references/overlap-and-audit-guardrails.md) IF package_boundaries_or_overlap_are_under_revision
TRIGGER_RULES := LOAD(references/trigger-and-disclosure-rules.md) IF activation_or_resource_loading_is_under_revision
INSTRUCTION_SURFACE_RULES := LOAD(references/instruction-surface-contracts.md) IF instruction_surface_is_under_revision

IF INPUT.explicit_user_request_does_not_include_skill_improvement:
  STOP("perform the requested task without changing the skill system")
IF INPUT.recurring_job IS null OR INPUT.output_contract IS implicit:
  STOP("refine inputs before revising the package")
IF raw_materials_include(long_form_source) AND coverage_proof IS implicit:
  STOP("record source coverage before claiming absorption")
IF external_behavior_is_being_imported AND imported_behavior_map_is_incomplete THEN STOP("finish the convergence audit before changing catalog surface area")
IF new_top_level_skill_is_proposed AND admission_gate_justification IS implicit:
  STOP("justify the new top-level skill before revising the catalog")
IF imported_material_is(vendor_specific OR document_output_specific OR media_production_specific) AND active_repo_local_owner_is_missing:
  STOP("record the catalog non-fit and keep the imported skill out of the active surface")

CORE := {
  trigger,
  success_condition,
  non_goals,
  hard_gates,
  anti_patterns
}

SKILL_MD := KEEP({ routing, required_reads, hard_gates, process, output_contract })
DETAIL.reference := MOVE(long_form_rules AND stable decision logic)
DETAIL.asset := MOVE(repeatable worksheets OR dispatch stubs OR checklists)

IF instruction_surface_is_under_revision:
  APPLY(INSTRUCTION_SURFACE_RULES)
  REQUIRE(instruction_surface_decision)

IF raw_materials_include(long_form_source):
  REQUIRE(private_record_of_selected_scope, actually_inspected_sections, applied_decisions, unread_or_unresolved_scope)
IF claiming_whole_source_absorption:
  REQUIRE(source_wide_inventory_and_disposition_audit)
IF imported_material_is(vendor_specific OR document_output_specific OR media_production_specific):
  REQUIRE(active_repo_local_owner OR excluded_catalog_non_fit_record)

IF new_top_level_skill_is_proposed THEN REQUIRE(admission_gate_justification)
IF existing_repo_local_skill_can_absorb_behavior_without_losing(trigger_clarity OR output_contract_force):
  KEEP(absorption_inside_existing_owner)
ELSE:
  ALLOW(new_top_level_skill)

IF support_file DOES_NOT materially_reduce_guesswork:
  DROP(support_file)

AUDIT := PASS IF
  trigger_is_sharp
  AND trigger_and_disclosure_match(TRIGGER_RULES) WHEN trigger_or_loading_behavior_changed
  AND support_file_selection_is_explicit
  AND hidden_dependencies_are_removed
  AND style_matches(STYLE_RULES) WHEN instruction_style_changed
  AND overlap_risk_matches(OVERLAP_RULES) WHEN package_boundaries_or_overlap_changed
  AND coverage_proof_exists_before_completion_claims WHEN external_material_was_imported_or_source_absorption_is_claimed

IF AUDIT = FAIL:
  REVISE()

IF routing_surface_changed = TRUE:
  UPDATE(.codex/skills/README.md)
```

## Required Reads

Read the current package and the support files that govern the part being changed. Choose the relevant references below instead of loading every resource for a small wording edit. Existing templates are reusable aids; create a filled record only when its handoff or evidence value justifies it, and keep that record outside the publication tree.

For a bounded source-based revision, the imported behavior map covers the selected decisions actually being imported. It does not require classifying unrelated source sections or imply that they were read.

- Read `references/pseudocode-style-rules.md` when revising instruction style, procedure wording, or checklist clarity.
- Read `references/overlap-and-audit-guardrails.md` when widening a package or deciding whether to add a neighboring capability.
- Read `references/book-absorption-rules.md` when using long-form material and `references/external-material-distillation.md` when importing other external guidance.
- Read `references/trigger-and-disclosure-rules.md` when revising descriptions, loading boundaries, examples, or script promotion.
- Read `references/instruction-surface-contracts.md` when changing instruction names, scope, canonical paths, adapters, or region markers.
- Use `assets/skill-authoring-record.md` for a substantial package change and `assets/asset-promotion-record.md` when deciding where reusable detail belongs.
- Use `assets/absorption-decision-record.md` for source coverage when importing material and `assets/parallel-maintenance-dispatch.md` for an authorized handoff across disjoint owned packages.

## Overview

Build the skill package, not just the wording.

Improve skills only within an explicit user-requested maintenance task. A failed command, a repeated difficulty, or an interesting source does not authorize automatic changes to shared instructions. Preserve the existing package's useful decisions, resources, and scope while making the requested improvement concrete and reviewable.

**Core principle:** if the trigger, output contract, or failure defenses are implicit, the skill is still a draft.

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
Do not ship a new or revised skill while its local ownership, output contract, and anti-failure structure are still implicit.
</HARD-GATE>

Read selected supporting material before relying on it. For a substantial handoff, distinguish resources requested from resources actually inspected and used. A short direct edit does not need a separate declaration form or a report listing unused resources.

<COVERAGE-GATE>
Report the actual selected scope and uninspected or unresolved material in a private record. Require a source-wide inventory and disposition audit only when claiming whole-source absorption; a bounded improvement does not require classifying unrelated chapters.
</COVERAGE-GATE>

<ANTI-PATTERN>
Do not treat skill writing as prompt filing. Copying persona-heavy source text into a skill package without distilling procedure, assets, and guardrails is a failed compilation.
</ANTI-PATTERN>

<CATALOG-GATE>
Do not ship a parallel top-level namespace when an existing repo-local skill can absorb the behavior without losing trigger clarity.
</CATALOG-GATE>

<IMPORT-FIT-GATE>
Do not absorb imported skills that are vendor-specific, document-output-specific, or media-production-specific unless an active repo-local owner already exists for that concern. If no active repo-local owner exists, record the source as excluded catalog non-fit instead of promoting a new top-level namespace.
</IMPORT-FIT-GATE>

## When to Use

- the user explicitly requests a new skill or an improvement to an existing skill package
- adding or revising a repo-local skill package under `.codex/skills/**`
- reducing a prompt dump, note, or repeated workflow into a deterministic skill package
- moving detail out of `SKILL.md` into durable local assets or references
- tightening trigger boundaries, support-file selection, or output contract clarity

## Do Not Use

- executing the target task directly when no skill change is needed
- broad prompt refactors outside the skill package
- one-off task notes that do not deserve reusable packaging

## Choose Roles

- `IF compiling_or_distilling THEN use agents/skill-author.md`
- `IF auditing_trigger_or_package_shape THEN use agents/skill-reviewer.md`

## Choose Assets

- `IF default_revision THEN use assets/skill-authoring-record.md`
- `IF auditing_trigger OR auditing_bloat THEN use assets/skill-audit.md`
- `IF moving_detail_out_of_SKILL THEN use assets/asset-promotion-record.md`
- `IF routing_surface_changed THEN use assets/change-impact-record.md`
- `IF deciding_durability THEN use assets/skill-pattern-checklist.md`
- `IF absorbing_external_material THEN use assets/absorption-decision-record.md`
- `IF parallel_maintenance = TRUE THEN use assets/parallel-maintenance-dispatch.md`

## Choose References

- `IF deciding_what_leaves_SKILL THEN use references/asset-promotion.md`
- `IF package_shape OR support_scope IS disputed THEN use references/skill-packaging-rules.md`
- `IF importing_external_material THEN use references/external-material-distillation.md`
- `IF source_is_awesome_list OR curated_guideline_catalog OR style_guide_bundle THEN use references/external-guideline-source-absorption.md`
- `IF importing_mental_model_or_thinking_skill_pack THEN use references/thinking-skill-absorption.md`
- `IF instruction_artifact_naming OR path_scope OR long_operational_doc_markers_are_under_revision THEN use references/instruction-surface-contracts.md`
- `IF deciding_examples OR scripts THEN use references/example-and-best-code-usage.md`
- `IF revising_trigger_text OR SKILL_body_loading_boundaries OR script_promotion THEN use references/trigger-and-disclosure-rules.md`
- `IF revising_style THEN use references/pseudocode-style-rules.md`
- `IF source_is_pdf OR source_is_book OR source_is_long_form_document THEN use references/book-absorption-rules.md`
- `IF guarding_against_sprawl THEN use references/overlap-and-audit-guardrails.md`

## Output Contract

Return the changed package, the requested behavior it supports, checks actually performed, and remaining evidence gaps. For substantial work, the authoring record can retain the relevant fields below outside the publication tree; omit fields that do not apply.

- declared support files
- files read before revision
- why each file was loaded
- target skill path
- operating concern
- admission gate justification
- source behavior map
- instruction artifact naming or path decision
- catalog non-fit decision when applicable
- active repo-local owner or exclusion record
- import disposition summary
- pseudocode style changes applied
- support files added or removed
- failure modes addressed
- multi-agent dispatch or reporting contract changed
- traceability fields added or tightened
- coverage proof added or tightened
- shared docs updated
- files actually used

## Verification and Source Handling

Verify metadata, reachable local support paths, the behavior of changed executable helpers, and the affected project checks. For a substantive behavior change, exercise an intended request, a nearby request that should use another path, and a relevant failure case. Inspect the actual outputs; a structural check or a source's benchmark does not prove that this package improves agent behavior.

When independent evaluation is available and authorized, provide the evaluator with the request and raw inputs rather than the intended answer. Compare the same inputs before and after a revision when claiming an improvement. Report unrun model evaluations without converting a planned test into a passing result.

Use public guidance and user-provided material to understand decisions, not to copy protected wording, diagrams, or example code into a distribution. Check redistribution terms before importing third-party code or assets and retain required notices. Keep raw sources, extracts, page-level reading coverage, filled authoring records, personal paths, and private service links outside the publication repository. Source titles or private locators are not needed in reusable operating instructions. Keep source attribution where a license requires it; do not remove attribution to hide copied material.
