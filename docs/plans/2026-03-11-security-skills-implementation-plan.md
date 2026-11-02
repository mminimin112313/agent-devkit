# Security Skills Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Add runnable `security-review` and `security-lab` skill packages to the cloned SoloPilot `.codex` tree, including deterministic Docker-lab scripts and supporting references.

**Architecture:** Keep the feature split into a review skill and an execution skill. Both packages stay self-contained under `.codex/skills`, while `security-lab` owns the shell entrypoints that orchestrate a local Docker network, disposable scanning containers, evidence capture, and fix verification.

**Tech Stack:** Markdown skill packages, Bash scripts, Docker CLI, Dockerized OWASP ZAP, Nuclei, optional sqlmap, local docs under `docs/plans/`

---

### Task 1: Record The Approved Design And Catalog Changes

**Files:**
- Create: `docs/plans/2026-03-11-security-skills-design.md`
- Modify: `.codex/skills/README.md`

**Step 1: Write the failing test**

Check that the current catalog has no `security-review` or `security-lab` entries.

**Step 2: Run test to verify it fails**

Run: `rg -n "security-review|security-lab" .codex/skills/README.md docs/plans`
Expected: no approved 2026-03-11 design doc and no catalog rows for the new skills

**Step 3: Write minimal implementation**

- add the approved design doc
- extend the skills catalog with the two new entries

**Step 4: Run test to verify it passes**

Run: `rg -n "security-review|security-lab" .codex/skills/README.md docs/plans/2026-03-11-security-skills-design.md`
Expected: both skill names appear in the catalog and design doc

**Step 5: Commit**

```bash
git add docs/plans/2026-03-11-security-skills-design.md .codex/skills/README.md
git commit -m "docs: add security skills design"
```

### Task 2: Build The `security-review` Skill Package

**Files:**
- Create: `.codex/skills/security-review/SKILL.md`
- Create: `.codex/skills/security-review/agents/openai.yaml`
- Create: `.codex/skills/security-review/agents/security-reviewer.md`
- Create: `.codex/skills/security-review/agents/remediation-reviewer.md`
- Create: `.codex/skills/security-review/assets/review-record.md`
- Create: `.codex/skills/security-review/assets/threat-model.md`
- Create: `.codex/skills/security-review/assets/finding-record.md`
- Create: `.codex/skills/security-review/assets/remediation-handoff.md`
- Create: `.codex/skills/security-review/references/review-lenses.md`
- Create: `.codex/skills/security-review/references/docker-surface-checks.md`

**Step 1: Write the failing test**

Check that the package directory and required files do not exist.

**Step 2: Run test to verify it fails**

Run: `test -f .codex/skills/security-review/SKILL.md`
Expected: non-zero exit status

**Step 3: Write minimal implementation**

- add the skill frontmatter, procedure, output contract, and support file references
- add the role prompts, checklists, and references required to run a security review

**Step 4: Run test to verify it passes**

Run: `find .codex/skills/security-review -maxdepth 3 -type f | sort`
Expected: the full package exists with `SKILL.md`, `agents/`, `assets/`, and `references/`

**Step 5: Commit**

```bash
git add .codex/skills/security-review
git commit -m "feat: add security review skill"
```

### Task 3: Build The `security-lab` Skill Package And Docker Scripts

**Files:**
- Create: `.codex/skills/security-lab/SKILL.md`
- Create: `.codex/skills/security-lab/agents/openai.yaml`
- Create: `.codex/skills/security-lab/agents/attacker.md`
- Create: `.codex/skills/security-lab/agents/defender.md`
- Create: `.codex/skills/security-lab/agents/reporter.md`
- Create: `.codex/skills/security-lab/assets/lab-run-record.md`
- Create: `.codex/skills/security-lab/assets/endpoint-inventory.md`
- Create: `.codex/skills/security-lab/assets/exploit-attempt.md`
- Create: `.codex/skills/security-lab/assets/verification-record.md`
- Create: `.codex/skills/security-lab/references/pentagi-capability-map.md`
- Create: `.codex/skills/security-lab/references/docker-lab-safety.md`
- Create: `.codex/skills/security-lab/references/attack-flow.md`
- Create: `.codex/skills/security-lab/scripts/bootstrap-lab.sh`
- Create: `.codex/skills/security-lab/scripts/inventory-target.sh`
- Create: `.codex/skills/security-lab/scripts/run-web-checks.sh`
- Create: `.codex/skills/security-lab/scripts/verify-fix.sh`
- Create: `.codex/skills/security-lab/scripts/collect-evidence.sh`

**Step 1: Write the failing test**

Check that the package and entrypoint scripts do not exist.

**Step 2: Run test to verify it fails**

Run: `test -f .codex/skills/security-lab/scripts/bootstrap-lab.sh`
Expected: non-zero exit status

**Step 3: Write minimal implementation**

- add the skill package
- implement deterministic Bash entrypoints with help text, strict mode, standard artifacts path, and Docker-network safety checks

**Step 4: Run test to verify it passes**

Run: `find .codex/skills/security-lab -maxdepth 3 -type f | sort`
Expected: the full package and all scripts exist

**Step 5: Commit**

```bash
git add .codex/skills/security-lab
git commit -m "feat: add security lab skill"
```

### Task 4: Verify Script Syntax And Discoverability

**Files:**
- Verify: `.codex/skills/README.md`
- Verify: `.codex/skills/security-review/**`
- Verify: `.codex/skills/security-lab/**`

**Step 1: Write the failing test**

Run the validation commands before fixing permissions or syntax errors and capture any failures.

**Step 2: Run test to verify it fails**

Run: `bash -n .codex/skills/security-lab/scripts/*.sh`
Expected: fail until syntax is correct

**Step 3: Write minimal implementation**

- fix shell syntax issues
- add executable bits to the lab scripts
- ensure every script returns usage text on `--help`

**Step 4: Run test to verify it passes**

Run:
- `bash -n .codex/skills/security-lab/scripts/*.sh`
- `for f in .codex/skills/security-lab/scripts/*.sh; do "$f" --help >/dev/null; done`
- `rg -n "security-review|security-lab" .codex/skills/README.md`

Expected: syntax check passes, help exits cleanly, catalog contains both skills

**Step 5: Commit**

```bash
git add .codex/skills/README.md .codex/skills/security-lab .codex/skills/security-review
git commit -m "chore: verify security skill package"
```
