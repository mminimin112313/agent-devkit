# Agent Devkit

Reusable multi-agent orchestration rules, role configs, and operating skills for **Codex**, **Claude Code**, **Antigravity**, and **OpenCode**.

## What Lives Here

- `AGENTS.md`: workspace-level guide for repositories that adopt this operating layer.
- `.codex/AGENTS.md`: top-level runtime laws and routing rules.
- `.codex/config.toml`: multi-agent feature flags and registered sub-agent role definitions.
- `.codex/agents/`: dispatch-ready role configurations (`explorer`, `worker`, `frontend_engineer`, `backend_engineer`, `reviewer`, `tech_lead`, `engineering_manager`, `qa`, `devops`, `security_privacy`, `release_manager`, `platform`, `po_pm`, `ui_ux_designer`, `monitor`).
- `.codex/skills/`: active top-level skills.
- `.codex/rulebooks/`: language and runtime rulebooks carried forward by `intake-and-routing`.
- `scripts/`: cross-platform global installer scripts for Codex, Claude Code, Antigravity, and OpenCode.
- `docs/inventory.md`: living repository map, architecture logic, and verification notes.
- `tests/`: skill-contract and governance regression suite.

## Active Top-Level Skills

| Skill | Purpose |
|---|---|
| `intake-and-routing` | Classify raw requests, enforce workspace boundary safety, and route to the narrowest owning skill. |
| `product-and-ux` | Discover the real user job, shape flows, UX writing, and visual direction, and review or cut over-kind and over-displayed UI before build. |
| `planning-and-scoping` | Turn approved direction into an execution-ready plan with one active step, role separation, and exact proof. |
| `architecture-and-design` | Decide module seams, deep interfaces, Humble Object boundaries, and rollback shapes before coding. |
| `implementation-frontend` | Deliver routes, components, and client state seams with layout, color, accessibility, motion, responsive, and rendered-UI proof, without adding unrequested UI. |
| `implementation-backend` | Deliver APIs, jobs, adapters, and persistence seams with deep modules, isolated side effects, and contract-safe verification. |
| `quality-and-review` | Run ordered review (`spec_fit -> code_quality -> qa_evidence`), design red-flag audits, and four-pillar test evaluation. |
| `release-and-operations` | Govern release readiness, rollout/rollback plans, observability baselines, and runtime incident response. |
| `multi-agent-orchestration` | Coordinate bounded parallel worker lanes with non-overlapping file ownership and independent evaluation. |
| `security-review` | Review trust boundaries, auth/session controls, secrets handling, and exploitable risk paths. |
| `security-lab` | Run isolated Docker-based security checks and verification diffs against authorized local targets. |
| `skillsmith` | Author, audit, and refine reusable skills, references, and assets under strict disclosure and style contracts. |
| `starting_pac` | Bootstrap legal/professional analysis workflows when explicitly triggered. |

## Install Globally

The global installer provisions the skill catalog and operating guides across **Codex**, **Claude Code**, **Antigravity**, and **OpenCode** in one command. Existing user configuration files (`config.toml`, `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`) are preserved by default while reference templates are written alongside as `*.agent-devkit.*`.

### Windows PowerShell

Install across all supported global agent hosts (`codex`, `claude`, `antigravity`, `opencode`):

```powershell
.\scripts\install-global.ps1
```

Preview the actions without writing files, or install to specific targets only:

```powershell
.\scripts\install-global.ps1 -DryRun
.\scripts\install-global.ps1 -Targets "codex,claude,antigravity,opencode"
.\scripts\install-global.ps1 -WorkspaceGuidePath "$HOME\projects\AGENTS.md"
```

### macOS / Linux / POSIX Shell

```sh
sh ./scripts/install-global.sh
```

Preview the actions, select specific targets, or install the workspace guide:

```sh
DRY_RUN=1 sh ./scripts/install-global.sh
INSTALL_TARGETS="codex,claude,antigravity,opencode" sh ./scripts/install-global.sh
WORKSPACE_GUIDE_PATH="$HOME/projects/AGENTS.md" sh ./scripts/install-global.sh
```

### Default Global Target Paths & Environment Overrides

- **Codex**: `$HOME/.codex` (`skills/`, `agents/`, `AGENTS.md`, `config.toml`). Set `CODEX_HOME` to install somewhere other than `$HOME/.codex`.
- **Claude Code**: `$HOME/.claude` (`skills/`, `CLAUDE.md`, `AGENTS.md`). Override with `CLAUDE_HOME` or `-ClaudeHome`.
- **Antigravity**: `$HOME/.gemini/antigravity/skills`, `$HOME/.gemini/config/skills`, and `$HOME/.gemini/skills`. Override with `ANTIGRAVITY_HOME`, `GEMINI_CONFIG_HOME`, or `GEMINI_HOME`.
- **OpenCode**: `$HOME/.config/opencode` (`skills/`, `AGENTS.md`). Override with `OPENCODE_HOME` or `-OpenCodeHome`.
- Pass `-ForceConfig` (PowerShell) or `FORCE_CONFIG=1` (POSIX shell) to overwrite existing top-level `config.toml`, `AGENTS.md`, `CLAUDE.md`, or `GEMINI.md` files with the repository defaults.
- Pass `-NoBackup` (PowerShell) or `NO_BACKUP=1` (POSIX shell) to skip pre-install backups.

## Validate Changes

Install test dependencies and run the contract suite:

```sh
python -m pip install -r requirements-dev.txt
python -m pytest -q
```

## Security Lab Scope

`security-lab` is for local containers, images, or explicitly authorized staging targets only. Do not scan public or third-party targets with `security-lab`.
