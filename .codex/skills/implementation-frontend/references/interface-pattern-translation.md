# Interface Pattern Translation

Turn approved interface direction into seam-level implementation choices without flattening every UI into the same generic component patterns.

```text
IF dominant_pattern_family IS implicit THEN STOP("name the pattern family before implementation")
IF current_location_or_recovery_contract_matters THEN KEEP(wayfinding, escape_hatch, persistence_rules)
ELSE translate_only_the_seam_local_pattern_requirements
```

## Before Building

Name the dominant pattern family for the seam:

- orientation and wayfinding
- collection browsing or drilldown
- layout and disclosure
- action and command surface
- data exploration
- input and validation
- system or smart-surface extension

Then decide what the component must preserve:

- current location or next step
- safe exploration, escape, cancel, preview, or undo
- interruption and resume behavior
- recognition over recall
- stable placement for repeated actions
- selection, expanded state, draft state, or scroll context
- keyboard and assistive-tech path

## Orientation And Wayfinding

If navigation or multistep flow matters, implement explicit cues:

- clear entry point
- current location
- progress state
- breadcrumb or back path
- escape hatch
- deep-link stability when sharing or return visits matter
- utility destinations stay distinct from task progression
- inline related-content jumps do not disorient the current task

Avoid hiding orientation inside decorative motion or relying on browser history alone.

## Collections And Drilldown

For list, grid, and object-browsing seams, choose deliberately:

- split view when browsing and detail must stay adjacent
- drilldown when detail should replace the prior level cleanly
- list inlay when inline expansion keeps comparison faster than full navigation
- cards or thumbnail grids when visuals drive recognition
- carousel only when a small, bounded set benefits from peeking and lateral browsing
- pagination, jump-to-item, or scrollers when length and retrieval speed matter

Check:

- how selection is shown
- where details appear
- how the user returns
- how location is preserved after refresh or navigation
- whether split-view becomes drilldown on narrow widths
- whether selection or scroll position should persist after mutations

## Layout And Disclosure

Translate the approved layout model into concrete rules:

- titled sections for scanability
- tabs when peer sections are mutually exclusive
- accordion or collapsible panels when density should stay optional
- center-stage or visual-framework layouts when one region must dominate

Use progressive disclosure when expertise, risk, or density differs across users. Do not hide required actions behind disclosure intended only for advanced detail.

For layered UI such as drawers, sheets, popovers, and inline expansion, define:

- what opens the layer
- where focus enters
- what dismisses it
- where focus returns
- whether its open state is deep-linkable or persistent

## Actions And Commands

Match the control surface to action density and risk:

- button groups for a small number of peer actions
- menus or toolbars for dense command sets
- action panels for grouped secondary actions
- prominent done or next-step affordances when completion matters
- preview, cancel, undo, or history when errors are expensive

If a user can make a meaningful mistake, build for recovery rather than relying only on confirmation.

When actions chain together, define whether the seam is:

- one-step completion
- staged completion with explicit progress
- editable after submit
- recoverable through history or replay

If keyboard shortcuts, macros, or typed commands exist, also define:

- discoverability
- conflict handling
- visible confirmation of what ran
- equivalent fallback path for users who never learn the shortcut layer

## Data Exploration

When the seam shows complex data, define:

- overview versus exact-value needs
- filter and sort controls
- query latency handling
- hover, focus, or tap detail behavior
- comparison mode, if any

Useful translations include datatips, spotlighted selections, dynamic filtering, and small-multiples layouts.

For dense tables and dashboards, also define:

- sticky headers or key columns, if needed
- inline versus side-panel detail
- empty-filter result handling
- export, compare, or inspect-next-step behavior
- whether multiple linked views brush or spotlight each other

## Input And Validation

Choose controls that minimize effort and repair cost:

- forgiving format when strict syntax would create avoidable friction
- structured format when the data model is rigid
- autocomplete, chooser, or builder when recall burden is high
- defaults and prefills when they truly save work
- helper text and errors close to the field that needs attention

Keep validation, focus movement, and recovery behavior consistent with the visual design.

For repair-heavy forms, define:

- whether validation is inline, on blur, on submit, or mixed
- where summary errors appear
- whether partial progress is retained after failure
- whether defaults can be reset or overridden safely
- whether required versus optional fields remain obvious after the user starts typing

## System And Smart-Surface Effects

If the seam extends a design system or adaptive surface, call out:

- token or variant reuse
- component level in the system
- framework constraints
- fallback behavior for connected, anticipatory, or assistive logic
- whether the smart behavior can be overridden, corrected, or explained by the user

## Output

Record:

- dominant pattern family
- orientation cues
- disclosure and layout model
- recovery and interruption handling
- collection, data, or input translation
- system constraints or adaptive behavior
