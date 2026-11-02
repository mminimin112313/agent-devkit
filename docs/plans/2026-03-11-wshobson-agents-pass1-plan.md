# Wshobson Agents Pass 1 Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Absorb the reusable planning, decomposition, and AI-guardrail operating knowledge from selected `sources/wshobson-agents` skills into the existing broad SoloPilot skillpack without importing plugin or marketplace surface.

**Architecture:** Keep the pass inside four existing broad skills. Use `planning-and-scoping` and `multi-agent-orchestration` for the primary operating changes, add only minimal repo-neutral guardrail wording to `architecture-and-design`, and tighten `intake-and-routing` so missing context routes back to planning instead of leaking into implementation.

**Tech Stack:** Markdown skill packages, repo-local assets and references, git diff verification, pytest

---

### Task 1: Record the approved pass-1 boundary in repo docs

**Files:**
- Create: `docs/plans/2026-03-11-wshobson-agents-pass1-design.md`
- Create: `docs/plans/2026-03-11-wshobson-agents-pass1-plan.md`

**Step 1: Verify planning docs do not already exist**

Run: `find docs/plans -maxdepth 1 -name '2026-03-11-wshobson-agents-pass1-*.md'`
Expected: no output before creation

**Step 2: Write minimal implementation**

- add the approved design summary
- add this implementation plan with bounded target skills and verification

**Step 3: Run test to verify it passes**

Run: `find docs/plans -maxdepth 1 -name '2026-03-11-wshobson-agents-pass1-*.md' | sort`
Expected: both new files are listed

### Task 2: Update `planning-and-scoping` with context-first work-unit discipline

**Files:**
- Modify: `.codex/skills/planning-and-scoping/SKILL.md`
- Modify: `.codex/skills/planning-and-scoping/assets/plan-record.md`
- Modify: `.codex/skills/planning-and-scoping/assets/owned-slice.md`
- Modify: `.codex/skills/planning-and-scoping/assets/task-breakdown-stub.md`
- Modify: `.codex/skills/planning-and-scoping/references/workflow-delivery-lifecycle.md`

**Step 1: Write the failing test**

Check that these files do not yet clearly require context freshness, current-state checks, and explicit work-unit packaging before implementation.

**Step 2: Run test to verify it fails**

Run: `rg -n "context freshness|current state|desired state|work unit|context before implementation" .codex/skills/planning-and-scoping`
Expected: missing or partial coverage before edits

**Step 3: Write minimal implementation**

- require plans to state current state and desired state when relevant
- require explicit context-freshness checks before build-ready claims
- tighten owned slices so acceptance, dependencies, non-goals, and proof travel together

**Step 4: Run test to verify it passes**

Run: `rg -n "context freshness|current state|desired state|work unit|context before implementation" .codex/skills/planning-and-scoping`
Expected: the planning package now carries the pass-1 operating language

### Task 3: Update `multi-agent-orchestration` with ownership and interface-contract dispatch rules

**Files:**
- Modify: `.codex/skills/multi-agent-orchestration/SKILL.md`
- Modify: `.codex/skills/multi-agent-orchestration/assets/dispatch-handoff.md`
- Modify: `.codex/skills/multi-agent-orchestration/assets/slice-record.md`
- Modify: `.codex/skills/multi-agent-orchestration/assets/convergence-record.md`
- Modify: `.codex/skills/multi-agent-orchestration/references/convergence-rules.md`

**Step 1: Write the failing test**

Check that dispatch and convergence assets do not yet fully require interface contracts, shallow dependency graphs, or low-noise integration signaling.

**Step 2: Run test to verify it fails**

Run: `rg -n "interface contract|dependency graph|integration point|broadcast|shallow" .codex/skills/multi-agent-orchestration`
Expected: missing or partial coverage before edits

**Step 3: Write minimal implementation**

- require decomposition by ownership or seam before staffing by count
- require dispatch handoffs to name interface contracts and allowed integration points
- tighten convergence rules so overlap growth forces re-scope instead of chatter

**Step 4: Run test to verify it passes**

Run: `rg -n "interface contract|dependency graph|integration point|broadcast|shallow" .codex/skills/multi-agent-orchestration`
Expected: the orchestration package now documents the new dispatch discipline

### Task 4: Update `architecture-and-design` with repo-neutral AI guardrail heuristics

**Files:**
- Modify: `.codex/skills/architecture-and-design/SKILL.md`
- Modify: `.codex/skills/architecture-and-design/assets/ai-guardrail-scorecard.md`
- Modify: `.codex/skills/architecture-and-design/references/ai-routing-guardrails.md`

**Step 1: Write the failing test**

Check that the architecture package does not yet explicitly cover progressive disclosure, structured-output selection, and failure-mode review as guardrails.

**Step 2: Run test to verify it fails**

Run: `rg -n "progressive disclosure|structured output|failure mode|iterative refinement" .codex/skills/architecture-and-design`
Expected: missing or partial coverage before edits

**Step 3: Write minimal implementation**

- add repo-neutral guardrail wording only
- keep examples conceptual, not SDK-specific
- make the scorecard review whether the chosen AI interaction shape is proportionate and failure-aware

**Step 4: Run test to verify it passes**

Run: `rg -n "progressive disclosure|structured output|failure mode|iterative refinement" .codex/skills/architecture-and-design`
Expected: the architecture package now carries the new AI guardrail language

### Task 5: Update `intake-and-routing` so stale or missing context routes back to planning

**Files:**
- Modify: `.codex/skills/intake-and-routing/SKILL.md`
- Modify: `.codex/skills/intake-and-routing/assets/intake-record.md`
- Modify: `.codex/skills/intake-and-routing/references/intake-clarification-patterns.md`

**Step 1: Write the failing test**

Check that intake does not yet clearly distinguish missing context from approved implementation readiness.

**Step 2: Run test to verify it fails**

Run: `rg -n "missing context|stale context|implementation readiness|route back to planning" .codex/skills/intake-and-routing`
Expected: missing or partial coverage before edits

**Step 3: Write minimal implementation**

- make stale or incomplete context an explicit routing reason
- require intake records to note whether planning refresh is needed
- keep the route minimal instead of smuggling implementation forward

**Step 4: Run test to verify it passes**

Run: `rg -n "missing context|stale context|implementation readiness|route back to planning" .codex/skills/intake-and-routing`
Expected: the intake package now carries the freshness-routing rule

### Task 6: Integrate and verify the combined pass

**Files:**
- Verify: `.codex/skills/planning-and-scoping/**`
- Verify: `.codex/skills/multi-agent-orchestration/**`
- Verify: `.codex/skills/architecture-and-design/**`
- Verify: `.codex/skills/intake-and-routing/**`

**Step 1: Run syntax and drift checks**

Run:
- `git diff --check`
- `pytest -q`

Expected: no whitespace errors and repository tests pass

**Step 2: Review for forbidden imports**

Run: `rg -n "claude plugin|/conductor:|~/.claude|LangChain|Pydantic|Anthropic SDK" .codex/skills`
Expected: no new source-specific imports introduced by this pass
