---
name: starting_pac
description: "Use when a new project starts from a plan, PRD, product brief, design note, or Korean \\\"기획\\\" file and the user wants Codex to set up AGENTS.md, MEMORY.md, .codex workspace files, continuation skills, work logs, validation rules, and a repeatable agent environment before implementation begins."
---

# Starting PAC

## Procedure

```text
INPUT := { project_root, plan_file, existing_instruction_files, existing_runtime_files }

STEP_0 := declare(support_files := references/agent-environment-contract.md + assets/bootstrap-record-template.md OR none)
STEP_1 := ORIENT(project_root, plan_file, AGENTS.md, MEMORY.md, .codex, package_manifests, git_status)
STEP_2 := SUMMARIZE_PLAN(product_name, intent, target_users, stack_hints, MVP_scope, exclusions, risks, first_next_actions)
STEP_2A := DECIDE(logging_and_error_code_need) IF project_is_non_trivial
STEP_3 := BOOTSTRAP_FILES(AGENTS.md, MEMORY.md, .codex/README.md, .codex/skills/README.md, continuation_skill, work_log)
STEP_4 := RECORD(development_observability_expectations, assumptions, blockers, next_actions)
STEP_5 := VERIFY(file_inventory, line_count_check, continuation_skill_exists, plan_reference_exists)
STEP_6 := HANDOFF(changed_files, validation_result, next_concrete_action)
```

## Overview

PAC means Project Agent Context.

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

## Trigger

```text
USE_THIS_SKILL IF
  user_asks(project_start_setup OR agent_environment_bootstrap)
  OR user_provides(plan_file OR PRD OR "기획")
  OR user_says("처음 시작" OR "에이전트 환경설정" OR "이어서 작업해도 되게")
  OR repo_has_plan_but_missing(AGENTS.md OR MEMORY.md OR .codex/README.md)
```

## Non-Goals

```text
DO_NOT choose the product architecture before reading the plan
DO_NOT overwrite existing repo-local rules without inspecting them
DO_NOT claim app/runtime verification before runnable code exists
DO_NOT make the generated continuation skill product-specific without evidence
```

## Required Reads

```text
READ := {
  applicable AGENTS.md files,
  plan_file,
  existing MEMORY.md if present,
  existing .codex/README.md if present,
  existing .codex/skills/README.md if present
}

IF support_needed THEN READ("references/agent-environment-contract.md")
IF recording_authoring_decisions THEN START_FROM("assets/bootstrap-record-template.md")
IF deterministic_bootstrap_needed THEN RUN("scripts/bootstrap_agent_env.py")
```

## Process

```text
STEP_1 := ORIENT
  identify project_root
  find plan file: 기획.md, PRD.md, plan.md, README.md, docs/*plan*.md
  inspect existing AGENTS.md, MEMORY.md, .codex, package manifests, and git status

STEP_2 := SUMMARIZE_PLAN
  extract product_name, product_intent, target_users, stack hints, MVP scope, exclusions, risks, first next actions
  identify whether development needs file-based logging, error-code standardization, diagnostics, or audit trails
  IF extraction_is_uncertain THEN mark assumption in MEMORY.md

STEP_3 := BOOTSTRAP_FILES
  create or update:
    AGENTS.md
    MEMORY.md
    .codex/README.md
    .codex/skills/README.md
    .codex/skills/<project-slug>-continuation/SKILL.md
    .codex/work-log/YYYY-MM-DD-agent-environment-bootstrap.md
  record development observability expectations:
    file-based logs when runtime/debug history must survive chat sessions
    standardized error codes when failures cross modules, UI, CLI, API, or agent handoff boundaries

STEP_4 := VERIFY
  run file inventory
  run line-count check for agent-maintained operating docs
  verify continuation skill exists
  verify plan file remains referenced as canonical input
  verify logging/error-code recommendation is recorded when the project is non-trivial

STEP_5 := RECORD_AND_HANDOFF
  update MEMORY.md with current state, decisions, blockers, next actions, verification
  update work log with commands and results
  final response reports changed files, validation, and next concrete action
```

## Deterministic Helper

```text
DEFAULT_COMMAND :=
  python3 .codex/skills/starting_pac/scripts/bootstrap_agent_env.py --project-root . --plan 기획.md

IF installing_globally THEN
  use installed script path under ~/.codex/skills/starting_pac/scripts/bootstrap_agent_env.py
```

The script is conservative: it creates missing files and refuses to overwrite existing files unless `--force` is passed.

## Output Contract

```text
PASS IF
  AGENTS.md exists
  AND MEMORY.md exists
  AND .codex/README.md exists
  AND .codex/skills/README.md exists
  AND project continuation skill exists
  AND work-log bootstrap entry exists
  AND plan file is cited in MEMORY.md
  AND verification result is recorded

FAIL IF
  future agent cannot continue from files alone
  OR generated docs hide assumptions
  OR local instructions conflict with deeper AGENTS.md files
```
