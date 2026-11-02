# Superpowers Absorption Program Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Compile the active `superpowers` skill set into the repo-local SoloPilot skillpack while keeping the repo-local catalog primary and only promoting truly necessary new top-level skills.

**Architecture:** Execute the absorption as staged repo-local passes. Each pass adds or tightens one owned behavior seam, then locks it with pytest so the imported force survives without keeping a duplicate `superpowers` hierarchy. Use compile-first rules from `docs/plans/2026-03-11-superpowers-absorption-design.md` and treat new top-level skills as exception-only outcomes.

**Tech Stack:** Markdown skill packages, repo-local operating docs, TOML runtime role configs, pytest contract tests

---

### Task 1: Lock the compile-first policy and top-level admission gate

**Files:**
- Modify: `AGENTS.md`
- Modify: `.codex/README.md`
- Modify: `.codex/AGENTS.md`
- Modify: `.codex/skills/README.md`
- Modify: `.codex/skills/skillsmith/SKILL.md`
- Modify: `.codex/skills/skillsmith/assets/skill-authoring-record.md`
- Create: `tests/test_superpowers_absorption_catalog_contract.py`

**Step 1: Write the failing test**

Add assertions that:
- repo-local docs require compile-first absorption
- new top-level skill creation is gated by explicit trigger and output-contract checks
- catalog docs do not describe `superpowers` as a parallel public namespace

**Step 2: Run test to verify it fails**

Run: `pytest -q tests/test_superpowers_absorption_catalog_contract.py`
Expected: FAIL before the catalog and skillsmith wording is tightened

**Step 3: Write minimal implementation**

Tighten the shared docs and `skillsmith` package so the compile-first rule, admission gate, and anti-duplication policy are explicit.

**Step 4: Run test to verify it passes**

Run: `pytest -q tests/test_superpowers_absorption_catalog_contract.py`
Expected: PASS

### Task 2: Absorb spawn-runtime and dispatch structure

**Files:**
- Modify: `.codex/config.toml`
- Modify: `.codex/agents/*.toml`
- Modify: `.codex/agents/AGENTS.md`
- Modify: `.codex/skills/multi-agent-orchestration/SKILL.md`
- Modify: `.codex/skills/multi-agent-orchestration/agents/*.md`
- Modify: `.codex/skills/multi-agent-orchestration/assets/*.md`
- Modify: `.codex/skills/multi-agent-orchestration/references/*.md`
- Modify: `.codex/README.md`
- Modify: `tests/test_agent_identity_contract.py`
- Modify: `tests/test_agent_skills_absorption_lane1.py`

**Step 1: Write the failing test**

Add assertions that:
- runtime descriptions and role prompts carry copyable spawn intent instead of generic labels
- dispatch templates preserve opening-line, lane, forbidden-authority, and rewrite-on-drift structure
- useful structure from `subagent-driven-development` is translated into repo-local orchestration language rather than copied as a parallel system

**Step 2: Run test to verify it fails**

Run: `pytest -q tests/test_agent_identity_contract.py tests/test_agent_skills_absorption_lane1.py`
Expected: FAIL before the spawn and dispatch wording is strengthened

**Step 3: Write minimal implementation**

Tighten runtime descriptions, role prompts, and orchestration assets so spawn behavior stays explicit and self-correcting without live feel checks.

**Step 4: Run test to verify it passes**

Run: `pytest -q tests/test_agent_identity_contract.py tests/test_agent_skills_absorption_lane1.py`
Expected: PASS

### Task 3: Absorb ideation and planning superpowers into existing owners

**Files:**
- Modify: `.codex/skills/intake-and-routing/SKILL.md`
- Modify: `.codex/skills/intake-and-routing/assets/*.md`
- Modify: `.codex/skills/planning-and-scoping/SKILL.md`
- Modify: `.codex/skills/planning-and-scoping/assets/*.md`
- Modify: `.codex/skills/planning-and-scoping/references/*.md`
- Modify: `.codex/skills/product-and-ux/SKILL.md`
- Modify: `.codex/skills/product-and-ux/assets/*.md`
- Modify: `.codex/skills/product-and-ux/references/*.md`
- Create: `tests/test_superpowers_process_absorption_contract.py`

**Step 1: Write the failing test**

Add assertions that:
- ideation requires explicit context gathering and design approval before implementation routing
- planning outputs execution-ready steps with proof paths and stop points
- repo-local planning does not depend on keeping `brainstorming` or `writing-plans` as separate top-level skills

**Step 2: Run test to verify it fails**

Run: `pytest -q tests/test_superpowers_process_absorption_contract.py`
Expected: FAIL before intake, product, and planning wording is tightened

**Step 3: Write minimal implementation**

Compile the useful `brainstorming`, `writing-plans`, and selected `executing-plans` rules into the repo-local process skills while preserving local trigger clarity.

**Step 4: Run test to verify it passes**

Run: `pytest -q tests/test_superpowers_process_absorption_contract.py`
Expected: PASS

### Task 4: Absorb execution-loop and parallelism rules

**Files:**
- Modify: `.codex/skills/multi-agent-orchestration/SKILL.md`
- Modify: `.codex/skills/multi-agent-orchestration/agents/*.md`
- Modify: `.codex/skills/multi-agent-orchestration/assets/*.md`
- Modify: `.codex/skills/quality-and-review/SKILL.md`
- Modify: `.codex/skills/quality-and-review/assets/*.md`
- Modify: `.codex/skills/quality-and-review/references/*.md`
- Create: `tests/test_superpowers_execution_absorption_contract.py`

**Step 1: Write the failing test**

Add assertions that:
- independent slices are dispatched only when ownership is actually disjoint
- execution loops use ordered spec review then quality review
- delegated execution is expressed through repo-local roles, assets, and evidence contracts rather than generic `superpowers` wording

**Step 2: Run test to verify it fails**

Run: `pytest -q tests/test_superpowers_execution_absorption_contract.py`
Expected: FAIL before orchestration and review-loop wording is tightened

**Step 3: Write minimal implementation**

Compile `dispatching-parallel-agents`, `subagent-driven-development`, and the useful parts of `executing-plans` into orchestration and review assets.

**Step 4: Run test to verify it passes**

Run: `pytest -q tests/test_superpowers_execution_absorption_contract.py`
Expected: PASS

### Task 5: Absorb debugging, TDD, verification, and review-discipline rules

**Files:**
- Modify: `.codex/skills/implementation-backend/SKILL.md`
- Modify: `.codex/skills/implementation-backend/assets/*.md`
- Modify: `.codex/skills/implementation-frontend/SKILL.md`
- Modify: `.codex/skills/implementation-frontend/assets/*.md`
- Modify: `.codex/skills/quality-and-review/SKILL.md`
- Modify: `.codex/skills/quality-and-review/assets/*.md`
- Modify: `.codex/skills/quality-and-review/references/*.md`
- Modify: `.codex/skills/failure-memory/SKILL.md`
- Modify: `.codex/skills/failure-memory/assets/*.md`
- Create: `tests/test_superpowers_quality_absorption_contract.py`

**Step 1: Write the failing test**

Add assertions that:
- bug work requires root-cause investigation before fixes
- implementation work requires test-first or explicit red-green discipline where appropriate
- completion claims require fresh evidence
- code review request and response rules stay technical and evidence-backed

**Step 2: Run test to verify it fails**

Run: `pytest -q tests/test_superpowers_quality_absorption_contract.py`
Expected: FAIL before implementation and review discipline is tightened

**Step 3: Write minimal implementation**

Compile `systematic-debugging`, `test-driven-development`, `verification-before-completion`, `requesting-code-review`, and `receiving-code-review` into the existing implementation, review, and failure-memory owners.

**Step 4: Run test to verify it passes**

Run: `pytest -q tests/test_superpowers_quality_absorption_contract.py`
Expected: PASS

### Task 6: Absorb worktree and branch-finish behavior into release ownership

**Files:**
- Modify: `.codex/skills/release-and-operations/SKILL.md`
- Modify: `.codex/skills/release-and-operations/assets/*.md`
- Modify: `.codex/skills/release-and-operations/references/*.md`
- Modify: `.codex/README.md`
- Modify: `.codex/AGENTS.md`
- Create: `tests/test_superpowers_release_absorption_contract.py`

**Step 1: Write the failing test**

Add assertions that:
- repo-local release guidance covers isolated workspace setup and branch-exit decision points
- branch-finish rules remain evidence-first and option-oriented
- no separate top-level skill is introduced if release ownership stays sharp

**Step 2: Run test to verify it fails**

Run: `pytest -q tests/test_superpowers_release_absorption_contract.py`
Expected: FAIL before release docs absorb the missing behavior

**Step 3: Write minimal implementation**

Compile `using-git-worktrees` and `finishing-a-development-branch` into repo-local release ownership and shared operating docs.

**Step 4: Run test to verify it passes**

Run: `pytest -q tests/test_superpowers_release_absorption_contract.py`
Expected: PASS

### Task 7: Converge catalog, revisit the admission gate, and verify the program

**Files:**
- Modify: `.codex/skills/README.md`
- Modify: `.codex/README.md`
- Modify: `.codex/skills/skillsmith/**`
- Modify: `tests/test_superpowers_absorption_catalog_contract.py`
- Verify: `tests/test_agent_identity_contract.py`
- Verify: `tests/test_agent_skills_absorption_lane1.py`
- Verify: `tests/test_superpowers_process_absorption_contract.py`
- Verify: `tests/test_superpowers_execution_absorption_contract.py`
- Verify: `tests/test_superpowers_quality_absorption_contract.py`
- Verify: `tests/test_superpowers_release_absorption_contract.py`

**Step 1: Run targeted verification**

Run:
- `pytest -q tests/test_superpowers_absorption_catalog_contract.py`
- `pytest -q tests/test_superpowers_process_absorption_contract.py`
- `pytest -q tests/test_superpowers_execution_absorption_contract.py`
- `pytest -q tests/test_superpowers_quality_absorption_contract.py`
- `pytest -q tests/test_superpowers_release_absorption_contract.py`

Expected: all targeted suites pass

**Step 2: Re-run the admission gate**

Check whether any source behavior still cannot be compiled into an existing repo-local owner without weakening trigger clarity or output-contract force.
Expected: create a new top-level skill only if the admission gate in `docs/plans/2026-03-11-superpowers-absorption-design.md` passes and the justification is recorded in `skillsmith`.

**Step 3: Run full verification**

Run:
- `git diff --check`
- `pytest -q`

Expected: both commands pass
