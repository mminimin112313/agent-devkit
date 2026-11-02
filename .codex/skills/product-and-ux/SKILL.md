---
name: product-and-ux
description: "Use for UX and product direction: discovery of the real user job, flows, forms, navigation, UX writing, interaction and visual direction, and UX review or critique of an existing surface, including cutting over-kind or over-displayed UI. Use before implementation when the experience is not yet decided."
---

# Product And UX

## Procedure

```text
STEP_0 := classify(work := new_direction OR bounded_change_inside_approved_direction OR review_only)
STEP_1 := declare(support_files := exact assets/ + references/ set OR none)
STEP_2 := read(required_assets_and_references_before_direction)
STEP_3 := record(why_each_declared_file_was_loaded)
STEP_4 := restate(user, job, desired_outcome)
STEP_5 := assess(scope := single_project OR multi_subproject)
STEP_6 := decompose_into_subprojects IF project_is_too_large_for_one_direction_package
STEP_7 := ask(only_questions_whose_answer_changes_direction_and_cannot_be_inferred) ; otherwise state the assumption and continue
STEP_8 := name(decision_question, evidence_mode)
STEP_9 := define(segment_scope, evidence_strength, limitations, contradictory_signals)
STEP_10 := compare(2_to_3_approaches, recommended_direction, avoid_list)
STEP_11 := apply(job_or_exploration_lens) IF direction_needs(jtbd OR effectuation OR opportunity_cost)
STEP_11A := apply(restraint_and_rule_intent) TO every_proposed_element ; each element names the user failure it prevents
STEP_12 := name(aesthetic direction, memorable differentiator, anti-generic frontend constraints) IF ui_facing_direction = TRUE AND work = new_direction
STEP_13 := compare(theme_system_options := 2_to_3_contrasted_visual_directions, palette_and_typography_pairings, recommendation) IF ui_facing_direction = TRUE AND visual_identity_is_undecided
STEP_14 := present(design_sections_scaled_to_complexity)
STEP_15 := get_user_approval(direction_level) ; per-section approval only when sections are independently costly to reverse
STEP_16 := translate(signals -> tradeoffs, recommended_direction, avoid_list, remaining_uncertainty)
STEP_17 := record(direction_approval_status, approval_owner, approval_notes)
STEP_18 := package(minimum_guidance)

IF work = bounded_change_inside_approved_direction THEN direction_approval_status := inherited_from_approved_direction
IF work = review_only THEN ROUTE -> output(review findings) AND STOP
IF direction_approval_status IN {approved, inherited_from_approved_direction} THEN ROUTE -> planning-and-scoping
ELSE IF scope_or_handoff_is_next THEN ROUTE -> planning-and-scoping
ELSE STOP("product direction is still incomplete")
```

## Overview

Shape the experience before the interface calcifies.

**Core principle:** if the user problem, evidence quality, or decision criteria are weak, design talk will collapse into taste.

**Rules carry reasons.** Every rule in this skill and its references protects a named user outcome. Apply a rule only where that outcome is at risk. Agents that apply rules without their reasons produce over-kind and over-displayed interfaces: extra confirmations, redundant helper text, badges nobody acts on, and question rounds nobody needed. `references/restraint-and-rule-intent.md` holds the reasons and the stop conditions.

Help turn ideas into fully formed designs and specs through natural collaborative dialogue.

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

Start by understanding the current project context, then ask only the questions whose answers change the direction, batched when several are needed. Once you understand what you're building, present the design and get user approval.

<HARD-GATE>
Do not jump from a vague request to screens, feature lists, or implementation advice. First make the user, job, success condition, and evidence path explicit. Do NOT invoke any implementation skill, write any code, scaffold any project, or take any implementation action until a design has been presented and approved. Why: building on an unexamined direction wastes the most work. Scale: a new direction gets a direction package; a bounded change inside an already approved direction inherits that approval and needs only a one-line statement of what changes; a review needs no approval to report findings.
</HARD-GATE>

<NON-NEGOTIABLE>
Every run must declare its exact local `assets/` and `references/` set before execution, read the required files before shaping direction, and record why each declared file was loaded. Unnamed support files are out of contract and must not be relied on. If no support files are needed, say `none` explicitly. Final outputs must report the declared set, the files actually read, and the files actually used.
</NON-NEGOTIABLE>

<APPROVAL-GATE>
Do not route implementation guidance forward until the direction package has been reviewed and explicitly approved.
</APPROVAL-GATE>

<NON-NEGOTIABLE>
Questions come before methods. State the question, segment scope, evidence strength, and limitations before turning research, feedback, or content direction into product guidance.
</NON-NEGOTIABLE>

<ANTI-PATTERN>
Do not confuse trend narration, user quotes, brand adjectives, or "good UX instincts" with a usable product decision.
</ANTI-PATTERN>

## Anti-Pattern: "This Is Too Simple To Need A Design"

"Simple" projects are where unexamined assumptions cause the most wasted work, so a new direction is always stated, even in a few sentences. The opposite failure is equally real: running the full ceremony of questions, options, and per-section approvals for a bounded change inside an approved direction. Match the process to the cost of being wrong.

## Anti-Pattern: Rules Without Reasons

Do not add an element because a reference lists it. Confirmations, success messages, helper text, required markers, empty-state media, tours, badges, and notifications each exist for one failure. If that failure is already prevented by a visible result, undo, inline validation, a clear label, or convention, the element is noise. Accessibility, legally required disclosure, and safety warnings are floors, not noise.

## When to Use

- a request is still a user-problem, flow, messaging, or direction question
- research, feedback, support, trend, or brand signals exist but have not become product guidance
- frontend implementation is close but the experience direction is still unstable
- the next move is bounded direction, not coding or release review
- an existing surface needs a UX review or critique; audit it against its own design evidence (tokens, components, prior decisions), keep the product's identity, prefer no finding to an unsupported one, and keep accessibility findings
- a design feels cluttered, over-explained, or over-protective and needs cutting

## Do Not Use

- low-level implementation after the experience is already approved
- backend-only contract work
- release or runtime approval

## Required Reads

- You MUST read `references/signal-translation-rules.md` before reducing research, feedback, competitive, design-direction, or cross-team packaging signals into product direction.
- You MUST start from `assets/product-brief.md` before shaping direction. Switch to a narrower asset only when the evidence mode is already clear.
- Read `assets/ux-review.md` when the next move is section-by-section design approval, changes requested, or measurable approval criteria.
- Read `references/visual-direction-differentiation-rules.md` when the direction must set aesthetic direction, memorable differentiation, or anti-generic frontend constraints.
- Read `references/job-and-exploration-lenses.md` when deciding what to build, diagnosing adoption, or exploring a novel uncertain direction.
- You MUST read `references/restraint-and-rule-intent.md` before proposing, reviewing, or cutting interface elements.
- Read `references/discovery-interview.md` when the user, trigger, or success condition is not yet explicit.

## Checklist

Scale these steps to the work. A new direction runs all of them; a bounded change runs 1, 4 (one line), and 7; a review runs 1 and reports.

1. **Explore project context** check files, docs, recent commits
2. **Ask only decisive questions** whose answers change the direction; state assumptions for the rest
3. **Propose 2-3 approaches** with trade-offs and your recommendation when the direction is genuinely open
4. **Present design** in sections scaled to their complexity, get approval at the direction level; per-section approval only when sections are independently costly to reverse
5. **Write design direction record** save the validated direction in local assets and route it forward only after approval
6. **User reviews written direction** ask for approval before planning begins
7. **Transition to implementation planning** route to `planning-and-scoping`

## Key Principles

- **Few, decisive questions** Ask only what changes the direction and cannot be inferred; batch them when several are needed
- **Multiple choice preferred** Easier to answer than open-ended when possible
- **Rules with reasons** Apply a rule only where its protected outcome is at risk
- **Subtract first** Before adding an element, check whether removing one solves the problem
- **YAGNI ruthlessly** Remove unnecessary features from all designs
- **Explore alternatives** Always propose 2-3 approaches before settling
- **Proportional validation** Get approval where being wrong is costly; a bounded change inside an approved direction proceeds
- **Be flexible** Go back and clarify when something doesn't make sense

## Choose Roles

- use `agents/po-pm.md` when the main job is product framing, scope, and trade-off selection
- use `agents/ux-researcher.md` when evidence gathering or interpretation is the weak point
- use `agents/content-strategist.md` when messaging, comprehension, or launch language is the seam
- use `agents/ui-ux-designer.md` when the direction must become concrete interaction or visual guidance

## Choose Assets

```text
IF default_direction_package THEN START -> assets/product-brief.md
ELSE IF missing_input = research_design THEN SWITCH -> assets/ux-research-plan.md
ELSE IF evidence_mode = feedback OR evidence_mode = support THEN SWITCH -> assets/feedback-coding-sheet.md OR assets/support-insight-brief.md
ELSE IF evidence_mode = market OR evidence_mode = competitive THEN SWITCH -> assets/trend-brief.md
ELSE IF seam = positioning OR seam = message_architecture THEN SWITCH -> assets/brand-foundation-worksheet.md OR assets/message-house.md
ELSE IF seam = launch_messaging THEN SWITCH -> assets/launch-content-brief.md
ELSE IF direction_exists AND review_needed THEN SWITCH -> assets/ux-review.md
ELSE STOP("choose the asset that matches the actual evidence mode")
```

## Choose References

```text
IF proposing_reviewing_or_cutting_interface_elements THEN READ -> references/restraint-and-rule-intent.md
IF user_trigger_or_success_condition_is_unclear THEN READ -> references/discovery-interview.md
IF flow_form_validation_navigation_onboarding_or_ux_writing_is_the_seam THEN READ -> references/ux-interaction.md
IF choosing_screen_type_navigation_model_pattern_or_checking_dark_patterns THEN READ -> references/interface-patterns.md
IF decision_needs_cognitive_load_perception_or_design_ethics_judgment THEN READ -> references/design-principles.md
IF evidence_mode = research THEN READ -> references/ux-research-methods.md
ELSE IF evidence_mode = feedback OR evidence_mode = support THEN READ -> references/feedback-synthesis-framework.md OR references/support-signal-synthesis.md
ELSE IF evidence_mode = trend OR evidence_mode = competitive THEN READ -> references/trend-research-rubric.md
ELSE IF direction_must_resolve_into_ui_rules THEN READ -> references/design-system-methodology.md OR references/mobile-first-experience-principles.md OR references/interaction-accessibility-principles.md OR references/ui-ideation-prompt-patterns.md
ELSE IF direction_is_still_low_fidelity_or_flow_shaping OR hierarchy_or_state_clarity_is_unproven THEN READ -> references/wireframe-discipline.md
ELSE IF aesthetic_direction_or_visual_differentiation_is_part_of_the_decision THEN READ -> references/visual-direction-differentiation-rules.md
ELSE IF visual_inputs_must_be_distilled_into_reusable_rules THEN READ -> references/design-system-extraction.md
ELSE IF direction_needs_user_job_or_novel_exploration_lens THEN READ -> references/job-and-exploration-lenses.md
ELSE READ -> references/signal-translation-rules.md
```

## Output Contract

Return a product and UX brief with:

- declared support files
- files read before direction
- why each file was loaded
- user and job
- question answered
- evidence path and limitations
- trade-offs
- recommended direction
- aesthetic direction
- memorable differentiator
- theme system options compared
- palette and typography pairing
- anti-generic frontend constraints
- what to avoid
- elements removed or deliberately absent, with the reason for each kept element
- Known / Inferred / Unknown labels on findings
- remaining uncertainty
- design sections reviewed and approval status
- next skill
- files actually used
