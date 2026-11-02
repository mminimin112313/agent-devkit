# Refactoring UI Book Absorption Design

**Date:** 2026-03-11

**Scope:** Absorb design-domain knowledge from `Refactoring UI` into repo-local skills, using extracted text first and page images only when the text is ambiguous or figure-dependent.

## Intent

This source is a long-form book, not a small repo prompt dump. The absorption path should preserve chapter structure, avoid overfitting to book wording, and keep image review targeted to the pages where text alone loses design meaning.

## Operating Rules

- extract the PDF to text before distillation
- use page images only when text is incomplete, layout-dependent, or figure-heavy
- distill by chapter or topic bands, not by arbitrary page counts
- fan out across six non-overlapping chapter slices with the orchestrator owning synthesis
- map guidance into existing broad skills rather than creating a book-specific skill

## Expected Targets

- `product-and-ux`
  - direction setting
  - hierarchy
  - spacing
  - typography
  - color
  - empty-state and polish heuristics

- `implementation-frontend`
  - translating those rules into component and layout implementation references

## Non-Goals

- do not preserve chapter prose verbatim
- do not import Tailwind-specific code examples as generic rules unless the rule survives framework changes
- do not flatten the whole book into one giant reference file

## Acceptance

- `skillsmith` can now explain how to absorb a book or PDF source
- extracted text artifacts are recorded
- chapter/topic slices can be distributed safely to workers
- distilled guidance lands in existing skills with tests and no extension-specific baggage
