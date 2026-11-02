# Interface Pattern Coverage Map

This file records where the interface-pattern language lives inside the skillpack.

```text
PASS IF every_pattern_domain_maps_to_live_repo_local_files
FAIL IF a_domain_points_to_removed_or_implicit_coverage
```

| Domain | Core coverage | Lives in |
| --- | --- | --- |
| Human goals and cognition | audience, goals, research modes, cognition, memory, interruptions, repetition, keyboard-only, collaboration | `references/human-centered-interface-patterns.md`, `assets/product-brief.md`, `assets/ux-review.md`, `../../implementation-frontend/references/interface-pattern-translation.md` |
| Information architecture and screen families | information architecture, screen families, workflow structure, cards, dashboards, wizards, settings, workspaces, tags | `references/structure-navigation-and-wayfinding-patterns.md`, `SKILL.md`, `assets/product-brief.md`, `../../implementation-frontend/references/interface-pattern-translation.md` |
| Navigation and wayfinding | signposts, deep links, escape hatches, progress, breadcrumbs, navigation models | `references/structure-navigation-and-wayfinding-patterns.md`, `SKILL.md`, `assets/ux-review.md`, `../../implementation-frontend/assets/ui-review-checklist.md` |
| Layout and disclosure | hierarchy, gestalt, chunking, framework regions, progressive disclosure, tabs, accordions, collapsible panels | `references/screen-layout-visual-and-mobile-patterns.md`, `SKILL.md`, `assets/product-brief.md`, `../../implementation-frontend/references/interface-pattern-translation.md` |
| Visual language and aesthetics | clarity, actionability, affordance, composition, color, typography, imagery, accessibility | `references/screen-layout-visual-and-mobile-patterns.md`, `SKILL.md`, `assets/ux-review.md`, `../../implementation-frontend/assets/ui-review-checklist.md` |
| Mobile adaptation | essential-task framing, touch constraints, linearization, bottom navigation, infinite lists, generous borders | `references/screen-layout-visual-and-mobile-patterns.md`, `SKILL.md`, `assets/product-brief.md`, `../../implementation-frontend/assets/frontend-implementation-brief.md` |
| Collection browsing and drilldown | split view, drilldown, cards, thumbnail grids, pagination, jump to item, alpha scrollers | `references/structure-navigation-and-wayfinding-patterns.md`, `references/action-data-and-input-patterns.md`, `assets/product-brief.md`, `../../implementation-frontend/references/interface-pattern-translation.md` |
| Actions and commands | command surfaces, direct manipulation, preview, cancelability, undo, command history, macros | `references/action-data-and-input-patterns.md`, `SKILL.md`, `assets/ux-review.md`, `../../implementation-frontend/assets/component-state-checklist.md` |
| Complex data exploration | browsing, sorting, filtering, datatips, spotlight, brushing, small multiples | `references/action-data-and-input-patterns.md`, `assets/product-brief.md`, `../../implementation-frontend/references/interface-pattern-translation.md` |
| Input, forms, and validation | forgiving format, structured inputs, hints, prompts, strength meters, autocomplete, defaults, error messages | `references/action-data-and-input-patterns.md`, `assets/product-brief.md`, `../../implementation-frontend/assets/component-state-checklist.md`, `../../implementation-frontend/references/interface-pattern-translation.md` |
| Design systems and component hierarchy | systems, component hierarchy, framework fit, consistency, modularity | `references/interface-systems-and-smart-surfaces.md`, `SKILL.md`, `../../implementation-frontend/SKILL.md` |
| Adaptive and connected surfaces | connected, anticipatory, assistive, and natural interaction behavior | `references/interface-systems-and-smart-surfaces.md`, `SKILL.md`, `assets/ux-review.md`, `../../implementation-frontend/references/interface-pattern-translation.md` |

## Maintenance Rule

If any referenced file is renamed or removed, update this map in the same change. The map is the proof that the pattern language lives in active operating files instead of one-off notes.
