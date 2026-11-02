# Agent Environment Contract

```text
AGENTS.md OWNS path-scoped agent behavior.
MEMORY.md OWNS current project state, decisions, blockers, next actions, and latest verification.
.codex/README.md OWNS local Codex folder orientation.
.codex/skills/README.md OWNS repo-local skill routing.
.codex/skills/<project-slug>-continuation/SKILL.md OWNS "continue work" behavior.
.codex/work-log/*.md OWNS detailed session evidence.
```

## Development Diagnostics

```text
IF project_is_non_trivial THEN REQUIRE(logging_and_error_code_decision)

FILE_BASED_LOGGING := RECOMMEND WHEN
  runtime_events_or_agent_decisions_must_survive_chat_context
  OR debugging_requires_replayable_local_evidence
  OR user_reports_need_timestamps_inputs_outputs_and_failures

ERROR_CODE_STANDARD := RECOMMEND WHEN
  failures_cross(UI OR CLI OR API OR background_job OR agent_handoff)
  OR operators_need_searchable_failure_categories
  OR support_docs_or_tests_need_stable_assertions

PASS IF MEMORY.md names logging/error-code decision OR explicitly defers it with reason.
FAIL IF errors_are_only_free_text AND repeated_debugging_is_expected.
```

## Line Cap

```text
APPLY_200_LINE_CAP_TO := {
  AGENTS.md,
  MEMORY.md,
  .codex/**/*.md,
  docs/*.md created_by_agent
}

EXCLUDE_FROM_LINE_CAP := {
  long source plans,
  imported specs,
  generated reports explicitly marked as source material
}
```

## Completion Test

```text
PASS IF a new agent can answer:
  what is this project
  what has been decided
  what should be done next
  what command or check was last run
  where detailed session evidence lives
```
