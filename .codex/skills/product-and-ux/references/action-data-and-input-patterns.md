# Action, Data, And Input Patterns

Action surfaces, data displays, and input controls should match the user's mental model of the task.

```text
IF task_is_action_heavy THEN ROUTE -> action_surface_matched_to(task_risk, reversibility_expectation)
ELSE IF task_is_data_heavy THEN ROUTE -> display_pattern_matched_to(navigation_model, filtering_model)
ELSE ROUTE -> input_pattern_matched_to(validation_model, recovery_path)
```

## Actions And Commands

Start by naming the dominant action style:

- direct action on objects
- command from menus or toolbars
- keyboard-first command
- gesture-driven action
- typed command

Use the smallest surface that still keeps actions legible.

## Action-Risk Ladder

State the risk level of the action before choosing the control pattern:

- trivial and repeatable
- meaningful but recoverable
- costly but reversible
- destructive or hard to reverse

The higher the risk, the more the surface should bias toward preview, explanation, undo, or staged commitment.

## Action Patterns

- button groups
- hover or pop-up tools
- action panel
- prominent done button or assumed next step
- smart menu items
- preview
- spinners and loading indicators
- cancelability
- multilevel undo
- command history
- macros

Match the action surface to usage:

- hover or pop-up tools only as enhancement when pointer precision is available
- toolbars for repeated expert actions that benefit from spatial memory
- typed commands or shortcuts when speed and repeatability matter and discoverability is still addressed
- action panels when the user needs grouped secondary choices without leaving the object context

Reversibility matters more as task cost rises. If the user can make a meaningful mistake, prefer cancel, undo, preview, or history over confirmation-only safety.

## Complex Data Patterns

Before choosing a chart or dense display, decide:

- what organizational model the data follows
- which visual variables should express grouping or difference
- how the user will navigate and browse it
- how sorting, rearranging, search, and filtering should work
- when exact values versus trend recognition matter

Useful patterns include:

- datatips
- data spotlight
- dynamic queries
- data brushing
- multi-Y graph
- small multiples

Also decide:

- whether detail-on-demand appears inline, in a side panel, or in a separate focus view
- whether filters should be persistent, transient, or query-builder style
- whether empty-filter results should teach recovery or simply report absence
- whether rearranging data changes only view state or also saved user state

## Data Rules

- keep overview and exact-value needs separate; one surface rarely does both equally well
- filtering and sorting should reveal the current lens, not act as hidden global state
- when comparison matters, align scales and labels before adding more visual variety
- when exploration matters, keep query latency and loading state visible

## Forms And Controls

Prefer controls that reduce avoidable errors and typing burden:

- forgiving format
- structured format
- fill-in-the-blanks
- input hints
- input prompt
- password strength meter
- autocompletion
- drop-down chooser
- list builder
- good defaults and smart prefills
- error messages

Use field structure deliberately:

- explicit required versus optional markers when omission risk is real
- floating labels only when they remain legible and do not replace needed prompts or examples
- chooser or builder patterns when the user would otherwise need to remember rigid values
- list builders when the user is assembling multi-item selections with ordering or review needs

## Input Rules

- ask only for what the system truly needs now
- make required versus optional explicit
- use defaults and prefills when they lower effort without causing hidden risk
- validate in a way that teaches recovery
- keep helper text close enough that the user does not have to remember it
- define whether validation happens inline, on blur, on submit, or in a mixed model
- preserve partial progress when the user can reasonably recover instead of restarting
- distinguish between formatting help, semantic validation, and destructive confirmation

## Avoid

- exposing long action menus when one or two primary actions dominate
- forcing strict input syntax when the system could repair or normalize safely
- using spinners or indefinite loading indicators where progress or cancelability would better match the risk

## Guardrails

- do not overuse drop-downs when search, autocomplete, or direct selection would be faster
- do not use gesture-only or hidden command patterns for critical actions
- do not ask for data before the interface can explain why it needs it
- do not force strict formats when forgiving parsing would still keep the data clean
- do not bury errors in summaries when the user needs field-level recovery

## Output

Record:

- dominant action style
- action-risk ladder
- reversibility and recovery model
- data exploration model, if any
- form or control patterns selected
- validation, helper-text, and default strategy
