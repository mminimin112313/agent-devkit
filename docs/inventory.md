# Repository Inventory

This document is the living map for the repository.

```text
UPDATE_TRIGGER := file_layout OR operating_logic OR workflow_contract OR verification_contract OR security_boundary
COMPLETION_RULE := IF docs_inventory_not_updated_for_meaningful_change THEN change_is_incomplete
```

## File Layout

```text
AGENTS.md                                  -> workspace entry contract and project-specific rules
README.md                                  -> operator-facing install, validation, and safety guide
requirements-dev.txt                       -> pinned Python test dependency surface
pytest.ini                                 -> pytest discovery roots
track_prompt_reflections.py                -> standalone CLI for external prompt reflection ledgers
scripts/install-global.ps1                 -> Windows global installer for Codex, Claude Code, Antigravity, and OpenCode
scripts/install-global.sh                  -> POSIX global installer for Codex, Claude Code, Antigravity, and OpenCode
.github/workflows/pytest.yml               -> CI test and shellcheck workflow
.codex/AGENTS.md                           -> top-level runtime laws, role separation, and routing table
.codex/README.md                           -> package boundary, role hierarchy, and artifact inspection contract
.codex/config.toml                         -> multi-agent runtime settings and role registrations
.codex/agents/*.toml                       -> role-level agent configs
.codex/skills/*/SKILL.md                   -> active top-level skills (13 total)
.codex/rulebooks/*.md                      -> language and runtime rulebooks routed by intake-and-routing/references/rulebook-routing-map.md
.codex/skills/security-lab/scripts/*.sh    -> local container security lab helpers
docs/inventory.md                          -> this living repository map
docs/plans/*.md                            -> historical design and implementation plans
tests/test_*.py                            -> regression suite for skill and governance contracts
```

## Operating Logic

```text
portable_global_install := {
  windows: "scripts/install-global.ps1",
  posix: "scripts/install-global.sh",
  default_targets: "codex + claude + antigravity + opencode",
  codex_target: "$CODEX_HOME or $HOME/.codex",
  claude_target: "$CLAUDE_HOME or $HOME/.claude",
  antigravity_target: "$ANTIGRAVITY_HOME ($HOME/.gemini/antigravity), $GEMINI_CONFIG_HOME ($HOME/.gemini/config), and $GEMINI_HOME ($HOME/.gemini)",
  opencode_target: "$OPENCODE_HOME or $HOME/.config/opencode",
  workspace_guide: "optional WORKSPACE_GUIDE_PATH / -WorkspaceGuidePath",
  config_preservation: "preserves existing config.toml, AGENTS.md, CLAUDE.md, and GEMINI.md unless -ForceConfig / FORCE_CONFIG=1 is set, while writing *.agent-devkit.* reference copies",
  safety: "backs up managed skill and guide surfaces before copy unless -NoBackup / NO_BACKUP=1 is set, and prunes removed legacy skill directories"
}

evaluation_separation_contract := {
  rule: "non-trivial work separates planner, implementer, and evaluator roles",
  criteria: "defined in planning-and-scoping before implementation begins",
  routing: "multi-agent-orchestration dispatches an independent evaluator after implementation",
  acceptance: "quality-and-review blocks self-approved non-trivial work and requires direct artifact inspection"
}

programming_hygiene_contract := {
  search_first: "search_code_tests_docs_config_before_editing",
  search_fallback: "record_search_command_failure_and_preserve_scope_and_ignore_intent_with_fallback",
  root_cause_rule: "every top-level SKILL.md carries a ROOT-CAUSE-SOLUTION-HOOK near the portability mandate; diagnose root cause, apply a fundamental fix, and require explicit user approval with reason, scope, risk, and rollback plan before any fallback, workaround, bypass, or temporary patch",
  uncertainty_rule: "verify uncertain state or technical facts before proceeding",
  config_discipline: "route addresses, ports, URLs, paths, and environment values through config or adapters",
  scaffold_discipline: "create separated extension seams and prevent god class growth",
  line_count_audit: "audit changed file line counts and split oversized files before handoff",
  stepwise_execution: "proceed_step_by_step_with_clean_stop_points",
  support_file_resolution: "SKILL.md support file mentions resolve to existing skill-local assets or references"
}

software_design_and_testing_contract := {
  module_depth: "prefer deep modules that hide changeable representations and protocols behind simple common-case interfaces; reject shallow modules, pass-through methods, pass-through variables, and temporal decomposition",
  exception_discipline: "pull complexity downwards instead of exporting uncalibrated config parameters; reduce exception surfaces by defining normal-case semantics for edge inputs where safe, masking transient low-level failures inside the owning layer, or aggregating errors at boundary dispatchers",
  code_quadrants_and_humble_object: "separate deep domain or algorithmic logic (few collaborators, output-based or state-based unit tests) from wide out-of-process controller orchestration (humble objects, focused integration tests); never leave code in the overcomplicated quadrant",
  legacy_change_tactics: "trace effect propagation to narrow pinch points, step inward when pinch points widen into brittle harnesses, and use sprout or wrap extraction when legacy dependencies cannot be untangled in one step",
  dependency_and_test_pillars: "evaluate tests across regression protection, refactoring resistance, fast feedback, and maintainability; treat coverage metrics as negative indicators only; verify managed dependencies against real state with separate arrange/act/assert units of work, and mock or spy only consumer-owned adapters at unmanaged external boundaries"
}

workflow_contract := {
  authority: ".codex/AGENTS.md",
  parallel_limit: "up_to_twelve_workers matching .codex/config.toml max_threads = 12",
  mail_surface: "removed from active skills; handoffs use repo-local markdown assets",
  security_lab: "requires TARGET_CONTAINER, TARGET_IMAGE, or ALLOW_SAMPLE_TARGET=1 and emits signature-level verification diffs"
}
```

## Verification Evidence

```text
verification_evidence := {
  command: "python -m pytest -q",
  ci_workflow: ".github/workflows/pytest.yml",
  artifact_checks: [
    "all 13 top-level SKILL.md files pass contract tests",
    "host drift sync (2026-11-02): multi-agent-orchestration runtime-routing/lane-graph/self-evolution, rulebooks, numerical-review, and external-guideline-source-absorption were imported from the installed Codex home and routed; installers no longer drop them",
    "UX and frontend consolidation (2026-11-02): knowledge removed; restraint-and-rule-intent, discovery-interview, and ui-restraint-and-proof references verified by tests/test_ux_frontend_consolidation_contract.py",
    "SKILL.md support file mentions resolve to existing skill-local assets or references",
    "software design depth, Humble Object separation, legacy pinch-point/sprout/wrap, and four-pillar testing contracts are verified across architecture, implementation, planning, and review skills",
    "multi-agent global install scripts (PowerShell and POSIX shell) verify cleanly across Codex, Claude Code, Antigravity, and OpenCode targets with no hardcoded user paths",
    "security-lab shell scripts are LF-normalized and shellcheck-clean"
  ],
  unresolved_risk: "Docker runtime checks in security-lab require a host with Docker and security scanner images installed."
}
```
