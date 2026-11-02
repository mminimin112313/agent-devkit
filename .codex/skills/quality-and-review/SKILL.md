---
name: quality-and-review
description: "Use when a seam needs fresh proof, ordered review, acceptance, or handoff before anyone can call it done."
---

# Quality And Review

## Procedure

```text
INPUT := { seam, changed_files, fresh_proof, source_type, acceptance_source }

STEP_0 := declare(support_files := exact assets/ + references/ set OR none)
STEP_0A := read(required_assets_and_references_before_review)
STEP_0B := record(why_each_declared_file_was_loaded)
STEP_1 := gather(INPUT.seam, INPUT.changed_files, INPUT.fresh_proof, INPUT.acceptance_source)
STEP_1A := gather(evaluation_criteria, planner_identity, implementer_identity, evaluator_identity)
IF evaluator_identity = implementer_identity OR evaluator_identity = planner_identity THEN STOP("independent evaluator required")
STEP_1B := gather(search_evidence, uncertainty_checks, hardcoded_address_scan, line_count_audit)
IF INPUT.source_type = support_report THEN
  CAPTURE(symptom, impact, environment, repro_status, workaround)
  REPRODUCE(consistently_or_gather_more_data)
IF symptom_may_be_local_runtime_or_workspace_state THEN
  READ(references/local-runtime-triage.md) BEFORE attributing_the_issue_to_code

STEP_2 := review_in_fixed_order(spec_fit -> code_quality -> qa_evidence)
STEP_2A := reject(implementation_report_as_acceptance_evidence) IF code_or_artifact_check_is_missing
IF specialist_lens_is_needed THEN ROUTE -> bounded_specialist_lane

STEP_3 := investigate_root_cause(read_errors, reproduce, check_recent_changes, trace_data_flow) IF defect_or_unexplained_result_exists
STEP_3A := apply(evidence_ladder OR hypothesis_differential OR map_territory OR is_is_not_boundary OR root_cause_chain) IF reasoning_lens_is_needed
STEP_4 := compare_against_working_examples_or_references IF defect_or_unexplained_result_exists
STEP_5 := compare_falsifiable_hypotheses WHEN defect_or_unexplained_result_exists AND cause_is_uncertain
STEP_5A := test_localized_cause_directly WHEN defect_or_unexplained_result_exists AND evidence_already_identifies_it
STEP_6 := prefer(behavior_level_evidence) OVER(implementation_detail_proof) WHEN both_are_possible
STEP_6A := audit_design_red_flags(shallow_modules, information_leakage, temporal_decomposition, pass_through_methods_or_variables, special_general_mixture, conjoined_methods, overcomplicated_quadrant_units, comment_repeats_code_or_contaminates_interface)
STEP_6B := audit_test_quality(four_pillars_regression_refactoring_speed_maintainability, coverage_as_negative_indicator_only, no_assertions_on_stubs, no_mocks_of_intra_system_or_managed_dependencies, no_private_exposure_or_production_code_pollution, no_tautology_or_multi_act_unit_tests)
STEP_7 := verify(review_feedback_against_codebase_reality) IF incoming_change_request = review_feedback
STEP_8 := identify(checks_required_for_claim_and_project_acceptance)
STEP_9 := run_and_read(required_checks) IF existing_evidence_does_not_cover_current_changed_state_claim_scope_and_environment
STEP_10 := inspect_artifacts(changed_files, generated_outputs, docs, logs, screenshots_or_renders_when_relevant)
STEP_10A := record(proof_freshness, evidence_gaps, unresolved_risks, blocked_reproduction, root_cause_status, KPI_or_quality_threshold_result)
STEP_10B := block_if(hardcoded_address_in_logic OR god_class_risk_unresolved OR oversized_file_without_split_or_justification OR uncertain_state_assumed)
STEP_12 := decide(approve OR approve_with_follow_up OR revise OR block)

IF decision = revise THEN ROUTE -> implementation_owner
ELSE ROUTE -> next_owner
```

## Overview

Completion is an evidence decision.

**Core principle:** if proof, review scope, or handoff fidelity is weak, the work is not done.

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

Investigate a defect before claiming its cause or fix. Ordinary review does not require inventing a debugging investigation.

<HARD-GATE>
Review order is fixed unless a narrower local rule says otherwise: spec fit first, code quality second, QA evidence third. Do not skip forward because the code "looks right."
</HARD-GATE>

<NON-NEGOTIABLE>
Every run must declare its exact local `assets/` and `references/` set before execution, read the required files before choosing review order, and record why each declared file was loaded. Unnamed support files are out of contract and must not be relied on. If no support files are needed, say `none` explicitly. Final outputs must report the declared set, the files actually read, and the files actually used.
</NON-NEGOTIABLE>

<NON-NEGOTIABLE>
Evidence beats narration. Fresh verification is required for completion claims, release confidence, and security claims.
</NON-NEGOTIABLE>

<LOOP-GATE>
review_loop := spec_fit THEN code_quality THEN qa_evidence. implementation_report_is_not_acceptance_evidence.
</LOOP-GATE>

<VERIFICATION-GATE>
fresh_verification_before_completion_claims. review_feedback_requires_technical_verification_before_implementation.
</VERIFICATION-GATE>

<EVALUATOR-INDEPENDENCE-GATE>
The evaluator must be independent from the planner and implementer for non-trivial work. Evaluation must inspect artifacts directly: changed files, generated outputs, docs, command results, and acceptance evidence. Implementation self-review is useful but never final approval.
</EVALUATOR-INDEPENDENCE-GATE>

<CODE-HYGIENE-REVIEW-GATE>
Final review must check search evidence, hardcoded address prevention, extension seam shape, god class risk, line-count audit results, and uncertainty verification. Do not approve oversized changed files without a split or documented exception.
</CODE-HYGIENE-REVIEW-GATE>

<DESIGN-AND-TEST-QUALITY-GATE>
Evaluate tests across all four pillars—protection against regressions, resistance to refactoring, fast feedback, and maintainability—and treat coverage numbers as a negative indicator only. Reject tests that assert interactions on stubs, mock intra-system collaborations or managed dependencies, widen private visibility or pollute production code with test switches, duplicate production algorithms in expectations, or chain multiple Act sections in a unit test. Reject design red flags in changed code: shallow modules, back-door information leakage, temporal decomposition, pass-through methods or variables, conjoined methods, overcomplicated units that combine deep domain branching with many collaborators, and comments that repeat code or contaminate interfaces with implementation details.
</DESIGN-AND-TEST-QUALITY-GATE>

## Verification Standard

```text
NO COMPLETION CLAIMS WITHOUT FRESH VERIFICATION EVIDENCE
```

Use evidence that applies to the current changed state, claim scope, and environment. Re-run checks when those conditions changed or proof is missing, unexplained, or stale; a new message alone does not invalidate an observed result. Run project-required acceptance checks and report failures or unrun checks accurately.

## When to Use

- someone claims work is done, fixed, accepted, or ready to ship
- proof exists but review order or evidence sufficiency is still unclear
- a handoff must become approve, revise, or block
- support evidence should be checked before engineering work widens

## Do Not Use

- intake or planning before implementation exists
- architecture work that still lacks a concrete design
- release approval once the work is already in the shipping lane

## Required Reads

```text
IF default_review THEN START -> assets/review-checklist.md
ELSE IF requirement_fit_is_primary_question THEN START -> assets/spec-review.md
ELSE IF another_owner_needs_the_result THEN START -> assets/review-handoff.md

MUST READ -> references/review-sequencing.md BEFORE choosing_review_order
IF seam_has(explicit_acceptance_criteria OR approved_plan_steps OR spec_language) THEN MUST READ -> references/criterion-discipline.md
IF debugging_or_evidence_reasoning_lens_is_needed THEN MUST READ -> references/evidence-ladder-and-root-cause-lenses.md
```

## Evidence and Debugging

```text
BEFORE making_a_completion_claim:
  NAME(claim_scope, changed_state, environment)
  INSPECT(actual_artifacts_and_relevant_check_results)
  RUN(missing_or_invalidated_checks_and_project_required_acceptance)
  REPORT(observed_result, failures, unrun_checks, limitations)

IF defect_or_unexplained_result_exists:
  READ(errors_and_recent_changes)
  REPRODUCE_OR_RECORD(blocked_reproduction)
  TRACE(observable_effects_including_shared_state_dynamic_dispatch_and_IO)
  IF cause_is_uncertain:
    COMPARE(plausible_hypotheses_with_cheap_falsifying_observations)
  ELSE:
    TEST(localized_cause_directly)
  VERIFY(preservation_baseline_and_requested_fix_as_distinct_claims)
  REVISIT(cause_or_boundary) IF evidence_contradicts_the_fix
```

A passing initial preservation test can establish useful current behavior. For changed requirements, check that the evidence distinguishes the prior result from the requested result. A build-only check cannot prove behavior, and a mock that replaces the external contract cannot verify that integration.

## Review Request Contract

Review early, review often.

Mandatory:
- After each bounded task in multi-agent or chunked execution
- After completing a major feature
- Before merge to main or any equivalent completion lane

When dispatching review, provide precisely crafted context for evaluation, never your full session history. The reviewer should get:
- what was implemented
- what it should do
- the bounded diff or changed files
- the acceptance source or plan source
- the verification evidence already run

Act on feedback:
- Fix critical issues immediately
- Fix important issues before proceeding
- Push back if feedback is wrong, but only with technical reasoning and fresh verification

## Review Reception Contract

Code review requires technical evaluation, not emotional performance.

When receiving code review feedback:

1. Read complete feedback without reacting
2. Restate the technical requirement in your own words or ask
3. Verify against codebase reality
4. Evaluate whether it is technically sound for this codebase
5. Respond with technical acknowledgment or reasoned pushback
6. Implement one item at a time and test each

Never:
- blindly agree
- implement before verification
- batch unclear items and hope they are independent

Hold an unclear feedback item and changes that depend on it until the requirement is resolved. Continue independently verified items whose scope and dependencies are clear.

If external review feedback conflicts with the actual codebase, existing tests, or human-approved direction, push back with technical reasoning.

## Choose Roles

```text
IF question = requirement_fit OR scope_drift THEN ROUTE -> agents/spec-reviewer.md
ELSE IF question = code_level_correctness OR regression_risk THEN ROUTE -> agents/reviewer.md
ELSE IF question = fresh_verification_evidence OR artifact_quality THEN ROUTE -> agents/qa.md
ELSE IF docs_or_examples_are_part_of_acceptance_claim THEN ROUTE -> agents/docs-reviewer.md
ELSE IF incoming_evidence = bug_report OR support_case OR user_facing_defect_handoff THEN ROUTE -> agents/support-triager.md
ELSE STOP("review lane must be explicit")
```

## Choose Assets

```text
IF default_ordered_review THEN START -> assets/review-checklist.md
IF requirement_fit_is_weak_point THEN START -> assets/spec-review.md
IF correctness_OR_maintainability_OR_regression_risk_dominate THEN START -> assets/code-review.md
IF verification_evidence_is_decision_gate THEN START -> assets/qa-verdict.md
IF another_owner_must_receive_result THEN START -> assets/review-handoff.md
IF delegated_review_needs_exact_contract THEN START -> assets/code-review-dispatch.md OR assets/worker-handoff.md
IF main_risk = seam_interaction THEN START -> assets/integration-checklist.md
IF reasoning_lens_is_needed THEN READ -> references/evidence-ladder-and-root-cause-lenses.md
IF support_evidence_needs_cleanup THEN START -> assets/repro-intake.md OR assets/support-case-review.md
IF seam_needs_bounded_security_lens THEN START -> assets/security-review-checklist.md
```

## Choose References

```text
IF review_order_is_disputed THEN READ -> references/review-sequencing.md
IF acceptance_check_is_criterion_by_criterion THEN READ -> references/criterion-discipline.md
IF bug_fix_claim_lacks(failure_classification OR prevention_logic) THEN READ -> references/root-cause-and-prevention.md
IF seam_starts_as(support_report OR bug_handoff) THEN READ -> references/support-triage-and-evidence.md
IF symptom_may_be_local(auth OR config OR workspace OR sandbox OR install_source) THEN READ -> references/local-runtime-triage.md
IF symptom_depends_on(interactive_worker_state OR one_shot_prompt_state OR missing_local_state_artifact) THEN READ -> references/local-runtime-triage.md
IF platform_specific_home_or_config_root_resolution_may_be_wrong THEN READ -> references/local-runtime-triage.md
IF docs_or_examples_changed_materially THEN READ -> references/docs-as-code-review.md
IF visual_regression_or_accessibility_sensitive_presentation_matters THEN READ -> references/inclusive-visual-qa.md
IF seam_affects(workflows OR jobs OR lineage_sensitive_data_movement) THEN READ -> references/data-workflow-review-lens.md
IF trust_boundaries_changed THEN READ -> references/application-security-lenses.md OR references/web-auth-security-baseline.md
IF reasoning_lens_is_needed THEN READ -> references/evidence-ladder-and-root-cause-lenses.md
IF floating_point_comparison_fails OR numerical_threshold_is_disputed THEN READ -> references/numerical-review.md
```

## Output Contract

Return a review record with:

- declared support files
- files read before review
- why each file was loaded
- seam reviewed
- review order used
- proof checked and proof freshness
- evaluation criteria and independent evaluator identity
- verification commands, supported claim scope, and evidence validity for the current state
- artifacts inspected directly and KPI or quality threshold result
- search evidence, hardcoded-address scan, god-class risk, uncertainty checks, and line-count audit
- findings, evidence gaps, and remaining risk
- decision
- next owner or next skill
- files actually used
