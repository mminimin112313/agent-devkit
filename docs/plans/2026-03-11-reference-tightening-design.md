# Reference Tightening Design

**Date:** 2026-03-11

**Scope:** Tighten repo-local `.codex` reference files without flattening asset forms or losing substantive guidance.

## Intent

The next cleanup pass should compress prose-heavy reference files, not erase detail or over-normalize every support file into the same shape.

## Approved Direction

- keep `assets/` form-shaped when they act as checklists, worksheets, or handoff records
- focus rewriting effort on `references/` where long-form guidance still reads more like notes than decision logic
- use symbols only when they expose structure more clearly than prose
- preserve enumerated content when the list itself is the guidance, rather than forcing every list into assignments

## Candidate Targets

- `product-and-ux/references/design-system-methodology.md`
- `product-and-ux/references/mobile-first-experience-principles.md`
- `product-and-ux/references/ux-research-methods.md`
- `product-and-ux/references/interaction-accessibility-principles.md`
- `security-lab/references/web-check-playbooks.md`
- `security-review/references/web-app-review-playbook.md`
- `quality-and-review/references/root-cause-and-prevention.md`

## Acceptance

- assets remain recognizable as reusable forms or checklists
- selected references become more scan-friendly and logic-shaped
- symbol usage clarifies decision structure without dropping edge cases or evidence expectations
- regression tests catch future drift in both the rulebook and the selected references
