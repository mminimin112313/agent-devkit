# Structure, Navigation, And Wayfinding Patterns

Information architecture should be chosen before the visual shell.

```text
IF screen_family_or_navigation_model_is_implicit THEN STOP("name the structure before layout")
ELSE keep_wayfinding_exit_paths_and_deep_link_rules_explicit
```

## Structure First

- separate information structure from presentation choices
- prefer categories that are mutually exclusive and collectively exhaustive when the domain allows it
- organize by the user's question:
  - alphabetical when recall by name is common
  - number when identifiers dominate
  - time when sequence matters
  - location when place matters
  - hierarchy when parent-child relationships matter
  - category or facet when comparison and filtering matter

## Screen Families

Most application surfaces are one of these families:

- overview: show a list, feed, grid, or dashboard
- focus: show one thing in detail
- make: create or edit an object
- do: complete one task or step

Name the screen family before discussing layout. Mixed-purpose surfaces usually become harder to navigate.

## Screen-Family Checks

- overview surfaces should answer what exists, what matters now, and where to go next
- focus surfaces should keep identity, status, and key actions obvious
- make surfaces should preserve drafts, recovery, and unfinished work
- do surfaces should reduce branching and keep progress legible

## Structural Patterns

Choose the smallest pattern that matches the job:

- feature, search, and browse for large information spaces
- direct-access landing when one destination dominates return or mobile use
- streams and feeds for recency-driven surfaces
- media browser for highly visual collections
- dashboard for quick orientation across multiple signals
- canvas plus palette when creation and manipulation dominate
- wizard when the user benefits from guided sequencing
- settings editor for low-frequency configuration
- alternative views when the same objects need multiple lenses
- many workspaces when users switch among distinct contexts
- help systems when explanatory material must stay near the work
- tags when flexible cross-cutting retrieval matters

Choose the primary framing deliberately:

- content-centric when discovery and reading dominate
- commerce-centric when comparison and conversion dominate
- task-centric when completion speed and operational accuracy dominate

## Navigation And Wayfinding Rules

- keep distances short between common destinations
- place high-frequency destinations directly in global navigation
- bring consecutive task steps close together
- use signposts that explain current location, possible next moves, and exit paths
- preserve deep links when collaboration, sharing, or return visits matter
- keep utility destinations distinct from primary task navigation
- use associative or inline navigation only when it deepens the current context instead of scattering attention

## Navigation Surfaces

- global navigation for major product areas
- utility navigation for account, settings, support, or low-frequency tools
- associative and inline navigation for related content, contextual jumps, or next-best exploration
- related-content blocks when they lower dead ends instead of becoming recommendation noise
- sign-in tools where account state changes the next best action
- make back, home, and cancel semantics unambiguous
- keep labels stable enough that users can build orientation over time

## Navigation Models

- hub and spoke for central launch plus easy return
- fully connected for dense expert spaces with many lateral moves
- multilevel or tree for nested taxonomies
- step by step for guided progression
- pyramid for broad browse into deeper detail
- flat navigation for small spaces with frequent switching

## Wayfinding Patterns

- clear entry points
- menu page
- modal panel
- deep links
- escape hatch
- fat menus
- sitemap footer
- sign-in tools
- progress indicator
- breadcrumbs
- annotated scroll bar
- animated transition

Use animated transition only when it teaches spatial relationship instead of adding motion noise.

## Collection And Drilldown Patterns

- two-panel selector or split view
- one-window drilldown
- list inlay
- cards
- thumbnail grid
- carousel
- pagination
- jump to item
- alpha or numeric scroller
- new-item row

Choose based on object density, comparison needs, and whether details should stay adjacent or replace the prior view.

## Help And Orientation Support

- inline labels and hints for just-in-time clarity
- tooltips for compact explanation, not primary instruction
- guided tours for first-run orientation only
- searchable help or knowledge base when the domain is broad
- community or collaboration links when peer examples reduce ambiguity

## Avoid

- mixing unrelated screen families on one surface without a clearly dominant task
- using tags as the only retrieval model when the domain still needs stable hierarchy
- hiding the path back from detail, modal, or nested views
- adding animated transitions that do not teach continuity or relationship

## Guardrails

- do not collapse distinct screen families into one overloaded page just to reduce route count
- do not bury high-frequency destinations under generic menu buckets
- do not choose infinite drilldown without a clear resume, breadcrumb, or escape path
- do not mix taxonomy, workflow, and utility navigation without naming the hierarchy between them
- do not force carousels, deep nesting, or modal stacks when retrieval speed is the real user goal

## Output

Record:

- information architecture model
- screen family
- navigation model
- wayfinding cues
- collection or drilldown pattern
- deep-link, progress, or escape requirements
- screen-family rationale
