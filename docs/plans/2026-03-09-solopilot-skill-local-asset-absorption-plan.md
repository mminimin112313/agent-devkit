# SoloPilot Skill-Local Asset Absorption Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Rebuild SoloPilot so each top-level skill absorbs its own prompts and assets, then remove the root `.codex/prompts` and `.codex/templates` directories.

**Architecture:** Keep the ten-skill catalog intact while moving role prompts, assets, and long-form guidance into each skill package. Make every `SKILL.md` point only to local package assets, then delete the root prompt/template directories after reference cleanup and verification.

**Tech Stack:** Markdown skill packages, YAML discovery metadata, repository documentation

---

### Task 1: Record the approved design in-repo

**Files:**
- Create: `docs/plans/2026-03-09-solopilot-skill-local-asset-absorption-design.md`
- Create: `docs/plans/2026-03-09-solopilot-skill-local-asset-absorption-plan.md`

**Step 1: Confirm both planning files exist**

Run: `test -f docs/plans/2026-03-09-solopilot-skill-local-asset-absorption-design.md && test -f docs/plans/2026-03-09-solopilot-skill-local-asset-absorption-plan.md`
Expected: command exits `0`

**Step 2: Verify filenames match the approved topic**

Run: `find docs/plans -maxdepth 1 -name '2026-03-09-solopilot-skill-local-asset-absorption-*.md' | sort`
Expected: both new files are listed

### Task 2: Create the target package skeleton under every skill

**Files:**
- Modify or create under: `.codex/skills/*/agents/`
- Modify or create under: `.codex/skills/*/assets/`
- Modify or create under: `.codex/skills/*/references/`
- Preserve: `.codex/skills/*/agents/openai.yaml`

**Step 1: Add local asset folders where missing**

Create these directories as needed:

- `.codex/skills/intake-and-routing/assets`
- `.codex/skills/planning-and-scoping/assets`
- `.codex/skills/architecture-and-design/assets`
- `.codex/skills/implementation-frontend/assets`
- `.codex/skills/implementation-backend/assets`
- `.codex/skills/product-and-ux/assets`
- `.codex/skills/quality-and-review/assets`
- `.codex/skills/release-and-operations/assets`
- `.codex/skills/multi-agent-orchestration/assets`
- `.codex/skills/skillsmith/assets`

**Step 2: Add `references/` folders only where the migrated material needs long-form support**

At minimum evaluate:

- `.codex/skills/quality-and-review/references`
- `.codex/skills/release-and-operations/references`
- `.codex/skills/multi-agent-orchestration/references`
- `.codex/skills/skillsmith/references`

**Step 3: Verify every skill now exposes a consistent package surface**

Run: `find .codex/skills -mindepth 1 -maxdepth 2 \\( -type d -name agents -o -type d -name assets -o -type d -name references \\) | sort`
Expected: every top-level skill shows `agents/`; asset-bearing skills show `assets/`

### Task 3: Move prompt ownership into skill-local `agents/`

**Files:**
- Delete after migration: `.codex/prompts/*.md`
- Modify or create under: `.codex/skills/*/agents/*.md`
- Modify: `.codex/skills/*/SKILL.md`

**Step 1: Absorb intake and planning roles**

Create or adapt:

- `.codex/skills/intake-and-routing/agents/cto.md`
- `.codex/skills/intake-and-routing/agents/po-pm.md`
- `.codex/skills/planning-and-scoping/agents/cto.md`
- `.codex/skills/planning-and-scoping/agents/tech-lead.md`
- `.codex/skills/planning-and-scoping/agents/worker.md`

**Step 2: Absorb design and implementation roles**

Create or adapt:

- `.codex/skills/architecture-and-design/agents/cto.md`
- `.codex/skills/architecture-and-design/agents/tech-lead.md`
- `.codex/skills/architecture-and-design/agents/ui-ux-designer.md`
- `.codex/skills/implementation-frontend/agents/software-engineer-frontend.md`
- `.codex/skills/implementation-frontend/agents/ui-ux-designer.md`
- `.codex/skills/implementation-frontend/agents/qa.md`
- `.codex/skills/implementation-backend/agents/software-engineer-backend.md`
- `.codex/skills/implementation-backend/agents/platform.md`
- `.codex/skills/implementation-backend/agents/qa.md`
- `.codex/skills/product-and-ux/agents/po-pm.md`
- `.codex/skills/product-and-ux/agents/ui-ux-designer.md`
- `.codex/skills/product-and-ux/agents/software-engineer-frontend.md`

**Step 3: Absorb review, release, orchestration, and skillsmith roles**

Create or adapt:

- `.codex/skills/quality-and-review/agents/spec-reviewer.md`
- `.codex/skills/quality-and-review/agents/reviewer.md`
- `.codex/skills/quality-and-review/agents/qa.md`
- `.codex/skills/release-and-operations/agents/release-manager.md`
- `.codex/skills/release-and-operations/agents/devops.md`
- `.codex/skills/release-and-operations/agents/security-privacy.md`
- `.codex/skills/release-and-operations/agents/qa.md`
- `.codex/skills/multi-agent-orchestration/agents/orchestrator.md`
- `.codex/skills/multi-agent-orchestration/agents/tech-lead.md`
- `.codex/skills/multi-agent-orchestration/agents/worker.md`
- `.codex/skills/skillsmith/agents/skill-author.md`
- `.codex/skills/skillsmith/agents/skill-reviewer.md`

**Step 4: Rewrite each `SKILL.md` to reference only local `agents/` paths**

Update:

- `.codex/skills/architecture-and-design/SKILL.md`
- `.codex/skills/implementation-backend/SKILL.md`
- `.codex/skills/implementation-frontend/SKILL.md`
- `.codex/skills/intake-and-routing/SKILL.md`
- `.codex/skills/multi-agent-orchestration/SKILL.md`
- `.codex/skills/planning-and-scoping/SKILL.md`
- `.codex/skills/product-and-ux/SKILL.md`
- `.codex/skills/quality-and-review/SKILL.md`
- `.codex/skills/release-and-operations/SKILL.md`
- `.codex/skills/skillsmith/SKILL.md`

**Step 5: Verify prompt references were localized**

Run: `rg -n "\\.codex/prompts/" .codex/skills`
Expected: no matches

### Task 4: Move asset ownership into skill-local `assets/`

**Files:**
- Delete after migration: `.codex/templates/*.md`
- Modify or create under: `.codex/skills/*/assets/*.md`
- Modify: `.codex/skills/*/SKILL.md`

**Step 1: Add intake, planning, and design assets**

Create or adapt:

- `.codex/skills/intake-and-routing/assets/intake-record.md`
- `.codex/skills/intake-and-routing/assets/routing-decision.md`
- `.codex/skills/planning-and-scoping/assets/plan-record.md`
- `.codex/skills/planning-and-scoping/assets/owned-slice.md`
- `.codex/skills/architecture-and-design/assets/design-note.md`
- `.codex/skills/architecture-and-design/assets/module-ownership.md`
- `.codex/skills/architecture-and-design/assets/package-scaffold.md`

**Step 2: Add implementation and product assets**

Create or adapt:

- `.codex/skills/implementation-frontend/assets/frontend-handoff.md`
- `.codex/skills/implementation-frontend/assets/ui-review-checklist.md`
- `.codex/skills/implementation-backend/assets/backend-handoff.md`
- `.codex/skills/implementation-backend/assets/contract-checklist.md`
- `.codex/skills/product-and-ux/assets/product-brief.md`
- `.codex/skills/product-and-ux/assets/ux-review.md`

**Step 3: Add review, release, orchestration, and skillsmith assets**

Create or adapt:

- `.codex/skills/quality-and-review/assets/spec-review.md`
- `.codex/skills/quality-and-review/assets/code-review.md`
- `.codex/skills/quality-and-review/assets/qa-verdict.md`
- `.codex/skills/quality-and-review/assets/review-checklist.md`
- `.codex/skills/quality-and-review/assets/integration-checklist.md`
- `.codex/skills/quality-and-review/assets/worker-handoff.md`
- `.codex/skills/release-and-operations/assets/release-gate.md`
- `.codex/skills/release-and-operations/assets/rollback-record.md`
- `.codex/skills/release-and-operations/assets/operational-readiness.md`
- `.codex/skills/release-and-operations/assets/release-review-checklist.md`
- `.codex/skills/multi-agent-orchestration/assets/slice-record.md`
- `.codex/skills/multi-agent-orchestration/assets/convergence-record.md`
- `.codex/skills/multi-agent-orchestration/assets/dispatch-handoff.md`
- `.codex/skills/multi-agent-orchestration/assets/active-slices.md`
- `.codex/skills/multi-agent-orchestration/assets/module-ownership.md`
- `.codex/skills/multi-agent-orchestration/assets/mail-handoff.md`
- `.codex/skills/skillsmith/assets/skill-authoring-record.md`
- `.codex/skills/skillsmith/assets/skill-audit.md`
- `.codex/skills/skillsmith/assets/asset-promotion-record.md`

**Step 4: Rewrite each `SKILL.md` to reference only local `assets/` paths**

Update the same ten `SKILL.md` files listed in Task 3 so all asset references are relative to the owning skill package.

**Step 5: Verify template references were localized**

Run: `rg -n "\\.codex/templates/" .codex/skills`
Expected: no matches

### Task 5: Add skill-local long-form references where the main skill would otherwise bloat

**Files:**
- Create under: `.codex/skills/*/references/*.md`
- Modify: `.codex/skills/*/SKILL.md`

**Step 1: Identify which skills need long-form guidance**

At minimum evaluate:

- `.codex/skills/quality-and-review/references/review-sequencing.md`
- `.codex/skills/release-and-operations/references/release-evidence.md`
- `.codex/skills/multi-agent-orchestration/references/convergence-rules.md`
- `.codex/skills/skillsmith/references/asset-promotion.md`

**Step 2: Keep `SKILL.md` procedural**

For each long-form addition, reduce the main `SKILL.md` to trigger, procedure, and output contract plus links to local support files.

**Step 3: Verify reference paths are local and valid**

Run: `find .codex/skills -path '*/references/*' -type f | sort`
Expected: only skill-local reference files are listed

### Task 6: Update discovery metadata and package READMEs

**Files:**
- Modify: `.codex/README.md`
- Modify: `.codex/skills/README.md`
- Modify: `.codex/skills/*/agents/openai.yaml`
- Delete: `.codex/prompts/README.md`
- Delete: `.codex/templates/README.md`

**Step 1: Rewrite shared `.codex` documentation**

Update `.codex/README.md` and `.codex/skills/README.md` so they describe:

- skill-local role prompts
- skill-local assets
- removal of root prompt/template catalogs
- the ten-skill public surface

**Step 2: Refresh discovery metadata**

Review every `agents/openai.yaml` so descriptions still match the richer local package contents.

**Step 3: Verify shared docs no longer advertise root prompt/template directories**

Run: `rg -n "\\.codex/prompts|\\.codex/templates" .codex/README.md .codex/skills/README.md .codex/skills/*/agents/openai.yaml`
Expected: no matches except deliberate legacy notes slated for removal

### Task 7: Remove root prompt and template directories

**Files:**
- Delete directory: `.codex/prompts/`
- Delete directory: `.codex/templates/`

**Step 1: Confirm no remaining active references**

Run: `rg -n "\\.codex/prompts|\\.codex/templates" .codex`
Expected: no matches outside historical docs that are intentionally left untouched

**Step 2: Delete the directories**

Remove:

- `.codex/prompts/`
- `.codex/templates/`

**Step 3: Verify deletion**

Run: `test ! -d .codex/prompts && test ! -d .codex/templates`
Expected: command exits `0`

### Task 8: Run final structural verification

**Files:**
- Verify: `.codex/skills/**`

**Step 1: Check the skill catalog is unchanged**

Run: `find .codex/skills -mindepth 1 -maxdepth 1 -type d | sort`
Expected: only the ten approved skill directories

**Step 2: Check every skill still has a `SKILL.md` and `agents/openai.yaml`**

Run: `for d in .codex/skills/*; do test -f "$d/SKILL.md" && test -f "$d/agents/openai.yaml" || exit 1; done`
Expected: command exits `0`

**Step 3: Check package-local prompts and assets now exist**

Run: `find .codex/skills -path '*/agents/*.md' -o -path '*/assets/*.md' | sort`
Expected: each skill shows its local execution assets

**Step 4: Check the old root path references are gone from active skills**

Run: `rg -n "\\.codex/prompts|\\.codex/templates" .codex/skills .codex/README.md`
Expected: no matches

**Step 5: Review the final diff**

Run: `git diff -- .codex docs/plans`
Expected: the diff shows local asset absorption, updated skill docs, and deletion of the root prompt/template directories
