---
name: intake-and-routing
description: "Use when a new request, mixed request, or ambiguous request must be restated, bounded, and routed to the single best next repo-local skill before planning or implementation begins."
---

# Intake And Routing

## Procedure

```text
1. DECLARE(support_files := exact assets/ + references/ set OR none)
2. READ(required_assets_and_references_before_routing)
3. RECORD(why_each_declared_file_was_loaded)
4. RESTATE(request := target_outcome + success_condition + constraints + explicit_non_goals)
5. CHECK(current_context, existing_constraints, approval_state, evidence_state, workspace_boundary)
6. IDENTIFY(dominant_track := product OR planning OR architecture OR implementation OR review OR release OR orchestration)
7. RECORD(missing_inputs := approval OR boundary OR proof_expectation OR design_decision OR stakeholder_owner OR severity)
8. STOP("narrow cwd or get explicit approval") IF workspace_boundary_is_too_broad_for_the_task
9. ROUTE -> product-and-ux IF request_implies_new_behavior OR new_feature_direction AND direction_or_approval_is_not_explicit
10. MAP(mental_model_request -> repo_local_owner) IF mental_model_router_or_thinking_namespace_is_requested
11. ASK(one_focused_question) IF material_ambiguity_remains = TRUE
12. CHOOSE(one_next_skill)
13. RECORD(why_alternatives_lost_now IN assets/intake-record.md OR assets/routing-decision.md)
14. STOP("intake complete") WHEN the next owner can proceed without guessing
```

## Overview

Turn an incoming request into a clear next move, then stop.

**Core principle:** if the objective, success condition, or next operating track is still fuzzy, do not pretend planning has started and do not let execution start by accident.

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
Before any planning, architecture, implementation, or review move, you MUST name the outcome, success condition, current boundary, and next owner.

Do not route work forward until the request has a named outcome, boundary, and owner for the next decision. Do not ask exploratory multi-question bundles. Do not start coding, planning, or architecture exploration "just to get context." Do not treat creative work as "too simple" to need design.
</HARD-GATE>

<NON-NEGOTIABLE>
Choose the minimum viable next route. If one direct skill fits cleanly, do not escalate to orchestration. If ambiguity remains material, ask one focused clarification question instead of guessing.
</NON-NEGOTIABLE>

<NON-NEGOTIABLE>
Every run must declare its exact local `assets/` and `references/` set before execution, read the required files before routing, and record why each declared file was loaded. Unnamed support files are out of contract and must not be relied on. If no support files are needed, say `none` explicitly. Final outputs must report the declared set, the files actually read, and the files actually used.
</NON-NEGOTIABLE>

## Red Flags

These thoughts mean STOP: you're rationalizing.

| Thought | Reality |
|---------|---------|
| "The user already said enough, I can just start" | Named work is not the same as a bounded request. |
| "I'll explore the repo first and route after" | Intake decides how exploration should happen. |
| "I can code one slice while the rest is unclear" | Partial execution is still execution. Route first. |
| "The ambiguity is minor" | If it can change the next skill, it is material. |
| "I already know the owner because it's probably me" | Self-assigning the next owner is not evidence. Name it explicitly. |
| "I can ask a few quick questions and then decide" | Ask one focused question, not a bundle. |
| "Implementation is the minimum viable next route" | Only after intake proves product, planning, architecture, and review do not own the next move. |
| "This feels like harmless context gathering" | Undisciplined context gathering turns into accidental planning. |
| "This is too simple to need design" | Simple projects still need design before implementation. |

## Required Reads

- You MUST start from `assets/intake-record.md` before routing. Switch to `assets/routing-decision.md` only when multiple next skills need explicit comparison.
- You MUST read `references/signal-driven-routing.md` before routing research, feedback, redesign, competitive-direction, or cross-team packaging signals.
- Read `references/intake-clarification-patterns.md` when the request is still fuzzy after restatement or when you are tempted to ask more than one question.
- Read `references/severity-and-escalation.md` when runtime impact, support severity, or escalation posture may change the route.
- Read `references/workspace-boundary-safety.md` when the working directory looks broader than the intended task boundary or when repo scope is ambiguous.
- Read `references/rulebook-routing-map.md` when the request names a language, runtime, file extension, or framework, and carry the matching `.codex/rulebooks/` path to the next owner.

## Routing

```text
IF outcome IS unclear OR boundary IS unclear OR owner IS unclear:
  ROUTE -> intake-and-routing
ELSE IF request_implies_new_behavior OR new_feature_direction:
  ROUTE -> product-and-ux BEFORE planning_or_architecture_or_implementation
ELSE IF creative_work_or_behavior_change_is_present_even_if_small:
  ROUTE -> product-and-ux BEFORE implementation
ELSE IF trust_boundary_or_security_surface_changes:
  ROUTE -> security-review
ELSE IF security_repro_or_regression_requires_self_owned_docker_lab:
  ROUTE -> security-lab
ELSE IF runtime_impact OR incident_coordination dominates:
  ROUTE -> release-and-operations
ELSE IF evidence_is_incomplete OR acceptance_risk dominates:
  ROUTE -> quality-and-review
ELSE IF mental_model_router_or_thinking_namespace_is_requested:
  ROUTE -> the_existing_repo_local_owner_named_by_problem_type
ELSE IF multiple_owned_outcomes_can_progress_in_parallel:
  ROUTE -> multi-agent-orchestration
ELSE:
  ROUTE -> the_single_best_direct_skill
```

## Asset Routing

```text
IF default_delivery_intake:
  START -> assets/intake-record.md
ELSE IF multiple_next_skills_need_explicit_comparison:
  START -> assets/routing-decision.md
ELSE IF approval_owner_or_communication_path_is_ambiguous:
  START -> assets/stakeholder-alignment-note.md
ELSE IF request_is_a_hypothesis_or_test_idea:
  START -> assets/experiment-intake.md
```

## Output Contract

Return an intake record with:

- support files declared before execution
- files read before routing
- why each file was loaded
- request restatement
- target outcome and success condition
- current constraints and explicit non-goals
- missing boundary or evidence
- considered next skills
- chosen next skill
- why nearby alternatives lost
- next owner or next action
- one focused clarification question, if needed
- support files actually used
