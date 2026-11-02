# Design Knowledge Skillpack Absorption

> Superseded on 2026-11-02: `knowledge` was removed and its references were folded into `product-and-ux` and `implementation-frontend`. See `docs/inventory.md`.


## Decision

```text
GOAL := add non-programming design skill group without bloating the programming/process catalog
TARGET := .codex/skills/knowledge
ADMISSION_GATE := PASS
REASON := existing programming skills cannot preserve narrow design critique triggers without mixing implementation, product, and visual-reference concerns
```

## Source Inventory

```text
SOURCE.design_router := prior global knowledge/design skill
SOURCE.design_subskills := design-color + design-composition + design-patterns + design-principles + design-systems + design-ux + design-wayfinding
SOURCE.effective_html := prior global effective-html skill
SOURCE.design_corpus := excluded_host_specific_ledgers
```

## Ownership Split

```text
knowledge := top_level_router_for_non_programming_specialist_knowledge
knowledge/design := narrow_router_for_design_subskills
knowledge/effective-html := self_contained_visual_html_artifact_skill
product-and-ux := product_direction_and_flow_decision_owner
implementation-frontend := implemented_UI_seam_owner
skillsmith := book_or_external_material_absorption_owner
```

## Absorbed

```text
ABSORBED_NOW :=
  knowledge top-level router
  knowledge package README
  design router
  design-color reference
  design-composition reference
  design-patterns reference
  design-principles reference
  design-systems reference
  design-ux reference
  design-wayfinding reference
  effective-html skill and example corpus

GENERALIZED :=
  provenance wording changed from global .agent paths to repo-local copy boundary
  nested routes changed to explicit repo-local .codex/skills/knowledge paths
  design-corpus route changed to skillsmith handoff
```

## Excluded

```text
EXCLUDED :=
  design-corpus assets and ledgers
  host-specific Windows source roots
  full book/source coverage claims

REASON :=
  this repo is a reusable orchestration package
  host-specific corpus state is not portable
  existing skillsmith owns long-form absorption gates
```

## Evaluation Criteria

```text
PASS IF AGENTS.md active catalog includes knowledge
PASS IF .codex/skills/README.md documents knowledge entry order and catalog row
PASS IF knowledge router points only to existing .codex paths
PASS IF design router does not route to missing design-corpus
PASS IF nested design reference files are included in regression coverage
PASS IF effective-html remains self-contained and requires dark_mode + responsive + safety proof
PASS IF pytest -q passes
```

## File Inventory

```text
ADDED_OR_CHANGED :=
  AGENTS.md
  .codex/README.md
  .codex/skills/README.md
  .codex/skills/knowledge/README.md
  .codex/skills/knowledge/SKILL.md
  .codex/skills/knowledge/design/SKILL.md
  .codex/skills/knowledge/design-*/SKILL.md
  .codex/skills/knowledge/design-*/references/*.md
  .codex/skills/knowledge/effective-html/SKILL.md
  .codex/skills/knowledge/effective-html/references/effective-html-method.md
  .codex/skills/knowledge/effective-html/references/html-effectiveness/*
  tests/test_design_knowledge_skillpack_contract.py
  docs/plans/2026-06-13-design-knowledge-skillpack.md
```

## Artifact Inspection Notes

```text
INSPECTED :=
  knowledge router paths
  design router paths
  effective-html hard gates
  design reference file structure
  catalog and entry-order documentation

LINE_COUNT_EXCEPTION :=
  design reference files intentionally exceed tiny-skill size because they are reusable specialist rule banks
  effective-html example corpus is imported as artifact evidence, not active routing logic
```

## Verification Commands

```text
rg -n "knowledge|effective-html|design-corpus" AGENTS.md .codex/skills/README.md .codex/skills/knowledge tests
pytest -q tests/test_design_knowledge_skillpack_contract.py
pytest -q
git diff --check

RESULT :=
  targeted_contract_tests: 7 passed
  full_contract_suite: 98 passed
  whitespace_check: passed
```

## Unresolved Risk

```text
RISK :=
  imported design references are dense and should be split further only when a concrete repeated routing problem appears
  effective-html example corpus includes upstream project metadata files that are excluded from logic-shaped reference assertions
```

## Branch Disposition

```text
BRANCH := main
UPSTREAM := origin/main
DIRTY_BASELINE := existing user-owned changes were present before this work
COMMIT := created_after_verification
NEXT_OWNER := release_owner_after_push
```
