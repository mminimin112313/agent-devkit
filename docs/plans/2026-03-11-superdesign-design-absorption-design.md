# Superdesign Design Absorption Design

**Date:** 2026-03-11

**Scope:** Absorb design-domain knowledge from `sources/superdesign` into `product-and-ux` and `implementation-frontend` without importing extension-specific mechanics.

## Intent

`superdesign` contains reusable design thinking rules, but they are mixed with VS Code extension behavior and product-specific workflow rules. This pass extracts only the design-domain knowledge and maps it into the existing broad SoloPilot skills.

## Approved Mapping

- `product-and-ux`
  - variation-first ideation and contrastive concept generation
  - wireframe discipline
  - design-system extraction from visual inputs
  - hierarchy, spacing, typography, and palette decision rules

- `implementation-frontend`
  - component-isolated presentation work
  - theme token handoff from design direction into implementation
  - preview-safe frontend delivery expectations
  - responsive and presentation-proof rules

## Non-Goals

- do not import `.superdesign` storage paths
- do not import VS Code extension UX or command palette flows
- do not import product branding or marketplace behavior
- do not force a fixed “always 3 agents” runtime rule into the generic skill layer

## Acceptance

- design-domain rules become readable through existing references
- no extension-specific mechanics leak into repo-local skills
- `product-and-ux` gains stronger ideation, wireframe, and design-system guidance
- `implementation-frontend` gains stronger theme handoff, component isolation, and preview-safe delivery rules
