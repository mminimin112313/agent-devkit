# Interface Systems And Smart Surfaces

When the interface is becoming a reusable system or a behavior-rich environment, treat system structure as a product decision.

```text
PASS IF repeated_component_or_state_rules_trigger_system_thinking_only_when_multiple_flows_need_shared_rules
FAIL IF a_local_seam_problem_is_forced_into_a_system_layer_without_reuse_pressure
```

## UI Systems

A system is warranted when the product needs:

- repeatable decisions across many screens
- consistent state behavior across components
- explicit composition rules
- scalable documentation for future changes
- multiple teams or repeated seams that would otherwise drift in naming, state behavior, or hierarchy

## System Maturity Signals

Escalate from local pattern guidance to system thinking when:

- the same component decisions repeat across multiple flows
- state and accessibility behavior must stay aligned across teams
- product direction depends on reusable composition rules
- framework defaults are starting to override product intent

## Atomic Design Lens

Use atomic design as a decomposition aid, not as ideology:

- atoms: smallest reusable pieces
- molecules: small combinations with one clear job
- organisms: larger composite sections
- templates: structure without final content
- pages: fully instantiated experience

Move up or down the hierarchy only when it reduces ambiguity. Do not force every decision into every level.

## System Rules

- document consistency and modularity together
- preserve nesting and composition rules
- keep technology choices subordinate to interface contracts
- let the system explain when variation is allowed and when it is drift
- keep a style guide or component index close enough that future contributors can see the live rules
- separate system-level primitives from page-specific convenience wrappers

## Framework Pressure

Frameworks can speed delivery, but they also import assumptions about:

- density
- component APIs
- interaction states
- visual semantics
- responsive breakpoints

Audit them for:

- whether their default density matches the product's task pressure
- whether their state model covers draft, error, empty, and blocked states
- whether their navigation and overlay primitives fit the wayfinding model
- whether they encourage composition or one-off overrides

Adopt them only after checking that those assumptions fit the product direction.

## Guardrails

- do not introduce a system layer when a local seam decision would solve the problem cleanly
- do not let atomic-design vocabulary replace user-facing reasoning
- do not adopt a framework component just because it exists if its interaction model conflicts with the product need
- do not make connected or anticipatory behavior feel magical without clear fallback and explanation

## Beyond The Screen

When the experience includes connected or adaptive behavior, call out whether it is:

- connected device behavior
- anticipatory behavior
- assistive behavior
- natural or multimodal interaction

These surfaces raise stronger expectations around trust, predictability, and fallback behavior.

## Adaptive-Surface Guardrails

- the user should be able to understand why the system suggested or changed something
- the user should have a way to correct, override, or dismiss adaptive behavior
- connected or assistive logic needs a clear fallback when data, permission, or device context is missing
- anticipatory features should reduce work without creating hidden state transitions

## Output

Record:

- whether the work creates or extends a UI system
- atomic-design consequence, if useful
- framework or system constraints
- smart-surface behavior and fallback expectations
- trust and predictability risks
- system maturity signal
