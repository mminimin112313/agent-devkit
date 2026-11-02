---
name: multi-agent-orchestration
description: "Use when disjoint role-owned slices can run in parallel only if dispatch, support paths, proof, and convergence are explicit."
---

# Multi-Agent Orchestration

## Procedure

```text
1. DECLARE(support_files := exact assets/ + references/ set OR none)
2. READ(required_assets_and_references_before_dispatch)
3. RECORD(why_each_declared_file_was_loaded)
4. DEFINE(reason_for_fan_out)
5. CHECK(independence := file_overlap, concern_overlap, shared_root_cause_risk)
6. CHOOSE(pattern := research_fan_out OR independent_implementation OR verification_parallel OR competing_proposals)
7. REQUIRE(one_slice_per_problem_domain_when_root_causes_are_independent)
8. RECORD(each_slice IN assets/slice-record.md)
9. DISPATCH(fresh_implementer_subagent_with_precisely_curated_context_per_slice)
9A. DISPATCH(fresh_evaluator_subagent_after_implementation) IF slice_is_implementation_work
10. REQUIRE(two_stage_review := spec_compliance_then_code_quality) IF slice_is_implementation_work
11. TRACK(live_status IN assets/active-slices.md) IF fan_out_is_live = TRUE
12. DEFINE(acceptance_owner, integration_owner, convergence_owner, shutdown_condition IN assets/convergence-record.md) IF convergence_risk > minimal OR shutdown_decision_is_not_trivial
13. ROUTE -> quality-and-review IF convergence_is_ready_for_acceptance
14. ROUTE -> release-and-operations IF runtime_or_ship_decision_dominates
15. STOP("collapse to smaller path") IF overlap_grows OR shared_state_edits_appear OR latency_benefit_disappears OR worker_role_drift_is_not_stopped OR shared_root_cause_risk = TRUE
```

## Overview

Parallelism is optional and must earn its cost.

**Core principle:** if ownership overlaps, convergence is vague, or one operator can finish cleanly, do not fan out.

Delegate tasks to specialized agents with isolated context. By precisely crafting their instructions and context, ensure they stay focused and succeed at their task. They should never inherit your full session context or history. Construct exactly what they need.

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
Do not dispatch parallel slices until ownership, proof, convergence order, and shutdown condition are explicit.
</HARD-GATE>

<NON-NEGOTIABLE>
Every run must declare its exact local `assets/` and `references/` set before execution, read the required files before dispatch, and record why each declared file was loaded. Unnamed support files are out of contract and must not be relied on. If no support files are needed, say `none` explicitly. Final outputs must report the declared set, the files actually read, and the files actually used.
</NON-NEGOTIABLE>

<NON-NEGOTIABLE>
The orchestrator keeps integration, acceptance routing, and shutdown authority. Slices may deliver evidence and bounded changes, but they do not redefine the program boundary mid-flight. Slice returns must preserve actual support files used and any deviation from dispatch.
</NON-NEGOTIABLE>

<IDENTITY-GATE>
Each dispatched sub-agent must declare its repo role identity explicitly. Do not let workers answer as the orchestrator or as an unnamed generic Codex. receiver_identity_contract := declared_identity + receiver_opening_line + receiver_owned_lane + receiver_forbidden_authority
</IDENTITY-GATE>

<PARALLELISM-GATE>
parallel_fan_out_requires_independent_owned_slices. Do not split the work until each slice maps to one problem domain or owned seam with no shared root-cause dependency.
</PARALLELISM-GATE>

<NON-NEGOTIABLE>
Fresh subagent per task or slice. Do not reuse stale worker context when a fresh dispatch can carry the bounded task cleanly.
</NON-NEGOTIABLE>

<EVALUATION-SEPARATION-GATE>
For non-trivial implementation, dispatch or name three distinct roles: planner, implementer, and evaluator. The evaluator must inspect the implementation artifacts after execution and must not be the same agent or role that planned or implemented the slice.
</EVALUATION-SEPARATION-GATE>

## Required Reads

- You MUST read `references/parallel-governance.md` before defining slices, dispatching work, or converging returns.
- You MUST start from `assets/slice-record.md` before issuing dispatch. If the fan-out is already live, also update `assets/active-slices.md`.

## Routing

```text
IF slice_count < 2:
  STOP("one owner can still carry the work")
ELSE IF shared_write_overlap = TRUE:
  STOP("parallel slices are unsafe")
ELSE IF merge_strategy IS null OR acceptance_owner IS null:
  STOP("convergence contract is incomplete")
ELSE IF planner_agent = implementer_agent OR implementer_agent = evaluator_agent OR planner_agent = evaluator_agent:
  STOP("planner, implementer, and evaluator must be distinct")
ELSE:
  ROUTE -> multi-agent-orchestration
```

## Runtime and Harness Routing

Before choosing seats, read `references/runtime-routing.md` when any of these hold: the repository ships its own harness (CLI entry, gates, brief builder, hooks), the work will run on a host other than the one that wrote the project adapters (Claude Code, Codex, Gemini CLI, OpenCode), or a model or host version changed since the project last recorded seat choices.

```text
IF repo_has_own_harness:
  ROUTE node_input_and_proof -> the harness (its next-step command, its generated brief, its check)
  TREAT misfiring gates as harness nodes, not as extra lanes
SEAT(node) := latest user choice > project rule > runtime default, checked against what the runtime exposes now
NEVER hard-code model ids in this package; dated seat observations live in project notes
```

## Parallel Dispatch Pattern

Dispatch one agent per independent problem domain. Let them work concurrently.

Use when:
- multiple failures have different root causes
- multiple subsystems are broken independently
- each problem can be understood without context from others
- no shared state exists between investigations or implementations

Do not use when:
- failures are related and fixing one may fix others
- agents would edit the same seam
- full system state must be understood before acting

Each agent gets:
- specific scope
- clear goal
- exact constraints
- expected output

## Implementation Slice Review Pattern

For implementation slices:

1. Dispatch implementer with full slice text and bounded context
2. If implementer needs context, answer and re-dispatch
3. Implementer completes work, tests, and self-reviews
4. Dispatch spec compliance review first
5. Fix spec gaps and re-review until approved
6. Dispatch code quality review second
7. Fix quality issues and re-review until approved
8. Only then mark slice complete

Do not start code quality review before spec compliance is approved.

## Asset Routing

```text
IF creating_or_refreshing_one_slice_contract:
  START -> assets/slice-record.md
ELSE IF convergence_order OR acceptance_order needs explicit tracking:
  START -> assets/convergence-record.md
ELSE IF dispatch_prompt must be explicit for another owner:
  START -> assets/dispatch-handoff.md
ELSE IF fan_out_is_live:
  START -> assets/active-slices.md
ELSE IF ownership_overlap_is_the_main_risk:
  START -> assets/module-ownership.md
ELSE IF dispatch_prompt must cross role boundaries without mixing execution:
  START -> assets/dispatch-handoff.md
```

## Reference Routing

```text
IF dispatch_is_about_to_begin OR convergence_is_under_review:
  READ -> references/parallel-governance.md
IF merge_strategy OR shutdown_decision is disputed:
  READ -> references/convergence-rules.md
IF repo_has_own_harness OR host_runtime_differs OR model_or_host_changed:
  READ -> references/runtime-routing.md
IF work_has_three_or_more_nodes OR lanes_could_run_in_parallel:
  READ -> references/lane-graph.md
IF the_same_friction_recurs OR skill_text_contradicts_what_works:
  READ -> references/self-evolution.md
```

## Output Contract

Return an orchestration record with:

- declared support files
- files read before dispatch
- why each file was loaded
- reason for fan-out
- slice list
- per-slice owner, required skills, and proof
- per-slice planner, implementer, and evaluator identities
- per-slice declared identity
- per-slice fresh dispatch context
- per-slice local support paths dispatched
- per-slice local support paths actually used
- per-slice deviations from dispatch
- per-slice review stage and approval status
- evaluator artifact inspection result
- merge strategy
- convergence order
- integration owner
- acceptance owner
- review path
- shutdown condition
- next skill after convergence
- files actually used
