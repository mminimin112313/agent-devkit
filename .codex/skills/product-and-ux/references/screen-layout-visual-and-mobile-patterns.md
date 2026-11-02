# Screen Layout, Visual, And Mobile Patterns

Layout and visual language should make the task clearer, not decorate it.

```text
PASS IF hierarchy_and_mobile_adaptation_make_the_task_clearer_before_surface_polish
FAIL IF disclosure_or_visual_treatment_hides_required_actions_or_breaks_scanability
```

## Hierarchy And Layout

Visual hierarchy usually comes from some combination of:

- size
- position
- density
- background contrast
- rhythm and repetition

Use gestalt deliberately:

- proximity to group what belongs together
- similarity to show equivalence
- continuity to guide scanning
- closure to imply bounded regions

Also check:

- alignment and grid consistency
- visual flow from primary task to secondary detail
- whether small but critical controls are emphasized enough to compete with larger decorative regions
- whether dynamic regions change hierarchy or reading order unexpectedly

## Layout Patterns

- chunking information
- visual framework
- center stage
- grid of equals
- titled sections
- module tabs
- accordion
- collapsible panels
- movable panels

Choose progressive disclosure when density or expertise gaps would otherwise overwhelm the user.

## Disclosure Rules

- disclose advanced options later when they are rare, risky, or distracting
- keep high-frequency actions and critical status visible without expansion
- let disclosure reduce noise, not hide responsibility
- prefer one stable disclosure model per seam instead of mixing tabs, accordions, drawers, and hidden toggles without hierarchy

## Visual Language Rules

Always test the visual direction against:

- clarity
- actionability
- affordance
- composition
- consistency
- alignment
- accessibility

When choosing color and typography:

- do not rely on color alone for meaning
- make contrast and readability explicit
- use spacing and type hierarchy to reduce explanation burden
- keep icons, photography, and motifs supportive of recognition, not novelty for its own sake
- choose dark or light backgrounds based on readability, focus, and context instead of trend alone
- use hue, saturation, and temperature consistently so status and affordance stay learnable
- treat font pairing, numeric legibility, and paragraph rhythm as comprehension decisions, not brand garnish

## Density And Scanability

- dense enterprise surfaces still need a visual rhythm that explains grouping and priority
- sparse surfaces still need clear affordances and next steps
- if a layout asks the user to compare, keep items aligned enough for scanning
- if a layout asks the user to read, keep line length, spacing, and emphasis readable first

## Visual Style Ranges

Style families can vary widely:

- skeuomorphic
- illustrated
- flat
- minimalistic
- adaptive or parametric

Pick the least surprising style that still supports product meaning, trust, and usability.

## Mobile Adaptation

Mobile constraints are not a desktop afterthought:

- tiny screens
- variable widths
- touch input
- difficult text entry
- noisy physical environments
- location awareness
- limited attention

## Mobile Working Rules

- strip the experience to its essential task
- linearize content when narrow width makes comparison hard
- exploit hardware only when it truly reduces work
- optimize the most common interaction sequences first
- keep one-handed or interrupted use plausible when the context suggests it
- let primary actions survive narrow width without becoming visually dominant noise
- decide explicitly when split view should collapse to drilldown
- treat loading and progress feedback as orientation tools on mobile, not just backend status

## Mobile Patterns

- vertical stack
- filmstrip
- touch tools
- bottom navigation
- collections and cards
- infinite list
- generous borders
- loading or progress indicators
- richly connected apps

## Guardrails

- do not use visual style to weaken contrast, actionability, or state legibility
- do not add motion that hides hierarchy or makes orientation harder
- do not depend on wide-screen symmetry when narrow screens are a primary surface
- do not let disclosure, density, and responsive behavior drift independently

## Output

Record:

- hierarchy strategy
- disclosure strategy
- layout pattern
- visual tone and accessibility guardrails
- mobile task priority
- navigation and density changes across widths
- density strategy
