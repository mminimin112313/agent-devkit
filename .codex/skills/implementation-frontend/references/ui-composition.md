# UI Composition Reference

Use for hierarchy, layout, spacing, typography, grids, density, polish, and responsive screen design.

## Layout Rules

```text
START_WITH(user_goal)
CHOOSE(layout_model := document_flow OR task_panel OR dashboard OR editor OR commerce OR form)
SCREEN_TYPE := choose_by_primary_user_intent(overview OR focus OR make OR do) BEFORE arranging_components
PATTERN_SCREEN_TYPES := overview + focus + make + do

IF layout_model = dashboard THEN prioritize scan, comparison, filters, and stable density
IF layout_model = dashboard THEN show status + next_actions_at_a_glance BEFORE decorative_charts
IF layout_model = editor THEN prioritize tool access, canvas stability, undoable actions, and selection feedback
IF layout_model = form THEN prioritize field order, validation, grouping, and error recovery
IF layout_model = commerce THEN prioritize product evidence, price clarity, trust, and checkout path
IF layout_model = task_panel THEN keep frequent controls visible and hide rare controls behind clear access paths

GRID := PASS IF margins + columns + gutters are consistent at each breakpoint
ALIGNMENT := PASS IF edges reveal grouping and hierarchy
SPACING := PASS IF spacing scale distinguishes containment, relation, and separation
DENSITY := PASS IF repeated-use workflows remain scannable without decorative filler
CANVAS := shrink or constrain content width when full-screen spread weakens focus
DENSE_UI := allowed for expert, data-heavy, or repeated workflows when group boundaries remain legible
REGIONS := assign global, local, object, workspace, utility, and feedback areas before styling
CENTER_STAGE := give the main object or task the dominant region
GLANCE_TEST := purpose, primary region, primary action, page name, and next step must survive a few-second scan
SCAN_REGIONS := users should be able to name page regions quickly and safely ignore irrelevant regions
NOISE_REDUCTION := remove elements that do not support user goal, trust, orientation, or decision
SIMPLE_GRID := use fewer alignment lines, lighter grouping, and whitespace before stronger visual containers
REMOVE_VISUAL_LOAD := remove heavy containers, duplicate emphasis, extra type levels, and arbitrary shape variation before adding hierarchy
CONCEPTUAL_FIELD := layout starts from message, audience, medium, and intended response before selecting a surface style
VISUAL_LANGUAGE := type, image, shape, spacing, color, and material should share an internal logic or an intentionally named contrast
FORM_SPACE_MEANING := empty space, figure-ground, density, openness, alignment, and edge relationships are meaning-bearing shapes
LAYOUT_PACING := vary density, openness, scale, value, and interruption to create rhythm only when the scan path remains legible
FORM_VERTICAL_PATH := align labels, fields, help, errors, and buttons to create one obvious completion direction
FORM_ONE_ROW := put one question concept per row unless comparison between sibling answers is the task
FORM_GROUPING := proximity and headings should reveal mental groups, dependencies, and step boundaries
FORM_BUTTON_ALIGNMENT := primary action belongs at the end of the completion path with outcome-specific copy
```

## Grid Rules

```text
GRID := structure_for_relationships_not_decoration
GRID_SYSTEM := define columns + gutters + baseline + breakpoints before screen-by-screen layout
GRID_ANATOMY := define margins, columns, gutters, flowlines, modules, spatial_zones, and baseline rhythm before treating a grid as complete
GRID_SCOPE := apply grids to top_level_frames and component_frames
GRID_PROGRAM := define the grid as an ordering program for content relationships, not as a decorative overlay after layout
GRID_INTERVALS := verify horizontal and vertical intervals, not only column count, because rhythm and proportion come from both axes
GRID_VARIANTS := create allowed grid variants for recurring content types before improvising page-by-page exceptions
BASELINE := align repeated text rhythm before adding visual complexity
COLUMNS := choose count by content measure, hierarchy, and breakpoint behavior
MODULES := use to coordinate text, image, captions, page numbers, and white space
SPATIAL_ZONES := use to preserve recurring relationships among navigation, content, actions, metadata, and feedback
GRID_VISUAL_PROOF := inspect real layouts for line measure, image crop, caption relation, type scale, and whitespace rhythm before accepting a grid rule
GRID_EXTENSION := grids may coordinate print, screen, signage, exhibition, and spatial surfaces only after scale, viewing distance, and reading path are named
BREAK_GRID := allowed only when the exception improves emphasis comprehension or personality
ASYMMETRIC_GRID := allowed IF visual_weight_relationships_remain_readable
STRUCTURAL_PATTERN := visible pattern, rhythm, branching, or repetition must clarify relationship, flow, or scale before it earns space
FIGMA_GRID := apply to frames and component containers so spacing relationships survive iteration
RESPONSIVE_GRID := preserve hierarchy and scan path before preserving exact desktop geometry
DESIGN_TOOL_GRID := grids in design tools must be verified against content measure, resize behavior, frame nesting, and component reuse, not just visual alignment
COLUMN_THINKING := use columns to reason about relationships, not to outsource every layout decision
FLUIDITY := not all elements should be fluid; preserve intended widths for controls, cards, media, and dense content when resize harms comprehension
RELATIONSHIP_SPACING := internal component spacing should scale differently from spacing between unrelated groups

IF content_has_long_reading THEN protect measure, line-height, and baseline consistency
IF content_mix_has_images_and_text THEN use modules to preserve caption and image relationships
IF grid_is_visible_to_user THEN it has failed unless the format intentionally teaches structure
```

## Hierarchy And Emphasis

```text
PRIMARY := one dominant target per region
CONTRAST := use size OR weight OR color OR position OR spacing; avoid using all at once
GROUPING := cards_only_for_repeated_items_modals_or_framed_tools
CARD_LAYOUT := use for browsing modular items; prefer list_or_table when order density or title scanning dominates
CARD_CONTENT := one idea + limited actions + clear hierarchy
CARD_DASHBOARD := use compact status_or_action_modules without hiding comparison or next action
FLOW := order content by task sequence, not by internal implementation order
EMPTY_SPACE := reserve whitespace for comprehension, not for making sparse content feel premium
WHITE_SPACE := tune by content_density + user_research + brand_message
OPTICAL_CORRECTION := trust perceived center weight and alignment over raw geometry when they conflict
CONSISTENCY := establish repeatable type spacing alignment component behavior before intentional variation
EFFECTS := shadows gradients and illustrations must serve depth feedback hierarchy or comprehension
VISUAL_WEIGHT := judge by size, darkness, saturation, complexity, density, and position together
ATTENTION_LEVERS := choose the smallest useful set from size, weight, color, position, spacing, shape, and motion
ASYMMETRY := use only with a clear counterweight and intentional scan path
GESTALT_GROUPING := proximity and similarity must reveal relationship before decorative styling
GESTALT_LAYOUT := use proximity, similarity, continuity, and closure as meaning-bearing layout rules
GESTALT_REPAIR := repair mistaken visual relationships by changing spacing, similarity, continuity, closure, figure-ground, and grouping before relying on explanatory text
FLOW_FORCE := diagonal, radial, branching, or organic visual movement should pull attention toward the user task, not away from the next action
PATTERN_USE := copy the problem-solution structure, not the surface style of an example
DE_EMPHASIS := make secondary elements quieter before making primary elements louder
DOCUMENT_VS_VISUAL_HIERARCHY := semantic order may differ from visual priority when the task demands it
LABEL_REDUCTION := remove or quiet labels when value, position, or surrounding context already explains meaning
WEIGHT_CONTRAST_BALANCE := compensate high weight with lower contrast or high contrast with lower weight when elements compete
PROGRESSIVE_DISCLOSURE_LAYOUT := hide secondary sections only when reveal path and primary decision remain clear
SCANNING_HIERARCHY := prominence, grouping, and nesting must mirror importance, similarity, and containment
WEB_SCAN_DESIGN := web screens should support scanning with obvious headings, trigger words, chunking, hierarchy, and action scent before expecting linear reading
SHOUTING := fail when too many elements compete for primary attention
CLUTTER := fail when low-value elements lower the signal-to-noise ratio of the task
SUBTLE_CUE_RISK := cues that feel obvious to designers may be invisible to hurried users
MARGINAL_GAINS := refine high-frequency details because small repeated improvements compound into felt simplicity
PERCEPTUAL_LAYERING := use restrained color, depth, and grouping so users can tune into one layer and ignore others
SIZE_LOCATION_PRIORITY := important items may be visually enlarged or centered beyond literal scale when task importance demands it
VISUAL_POPOUT := unique size, shape, orientation, value, contrast, or motion should be reserved for the element users need next
ATTENTION_NULL := content placed where users have learned to ignore it should be redesigned as absent until gaze or behavior proves otherwise
BLUR_SQUINT_ATTENTION := grayscale blur and squint review can reveal likely automatic attention before user testing
FOVEAL_DETAIL := small details outside direct attention need stronger cueing, larger treatment, or later just-in-time placement
VISUAL_STANDARD := icons and symbols must match user interpretation; novelty belongs elsewhere when meaning risk is high
CHANGE_NOTICE := important screen changes need motion, position, sound, state text, or local contrast because presence alone does not prove perception
EXPECTATION_SCAN := place high-value content where task and learned screen conventions lead attention, not merely where the designer wants attention
VISCERAL_POLISH_BOUNDARY := first-impression beauty can improve confidence and exploration, but visual treatment must still expose affordance, hierarchy, state, and recovery
UI_FOUNDATION_BALANCE := color, type, grid, spacing, imagery, cards, effects, and controls must share hierarchy instead of competing for attention
OPTICAL_CORRECTION_UI := adjust icon, button, card, and type alignment by perceived weight when mathematical centering looks wrong
VISUAL_CONSISTENCY_AREAS := typography, color, layout and format, interaction behavior, and pattern choice should stay consistent unless a user task benefits from explicit variation
BRAND_COLOR_RESTRAINT := use brand color for recognition, priority, and semantic emphasis; do not let it become the default treatment for every surface
```

## Typography

```text
TYPE_SCALE := choose roles before sizes
READABILITY := PASS IF line_length + line_height + contrast support the reading mode
LINE_HEIGHT := choose by reading mode, type size, measure, density, and script; crowded lines are a comprehension failure
CONTRAST_RATIO := verify small text, disabled text, colored type, and type over image against the named accessibility target
LABELS := compact, specific, and adjacent to the control or value they explain
DISPLAY_TYPE := use only for true heroes or brand moments
COMPACT_UI := use tighter headings and stable component dimensions
TYPE_ROLE := define title, section, label, body, metadata, value, and action roles before choosing sizes
CASE_AND_WEIGHT := convey role and priority; avoid random uppercase, bold, or italic emphasis
TABLE_TYPE := optimize for aligned scanning, not paragraph reading
CARD_TYPE := preserve item title, key attribute, and primary action hierarchy
OPTICAL_TYPE_ALIGNMENT := adjust perceived center and overshoot when text or icons look misaligned despite exact geometry
TYPE_SCALE_SYSTEM := define type sizes from product roles; avoid pure modular math when it creates missing or fractional practical sizes
FONT_CHOICE := choose legible families with enough useful weights before expressive novelty
TYPE_APPROPRIATENESS := type choice must match audience, message, medium, production constraints, and reading mode before personal taste or novelty
TYPE_HIERARCHY_RESTRAINT := create hierarchy with the smallest effective change in size, weight, color, case, spacing, or position before mixing more families
TYPE_AS_IMAGE := expressive type may act as image only when the intended visceral message survives readability, context, and accessibility checks
REFLECTIVE_VISUAL_MEANING := symbolic or premium visual treatment should support identity, memory, pride, or story only after the behavioral use case remains strong
LINE_LENGTH := keep paragraph measure readable; wider lines need larger line-height
BASELINE_ALIGNMENT := align mixed text sizes by baseline when centered alignment looks visually off
NUMERIC_ALIGNMENT := right-align numbers when users compare magnitude
LINK_TREATMENT := color is optional if position, underline, icon, or context already communicates interactivity
LETTER_SPACING := use for all-caps readability and tight headline correction, not as default styling
COLORED_TYPE := judge value, saturation, temperature, and textural weight together before approving colored text
SCAN_TEXT := headings, short paragraphs, lists, and key terms expose structure before full reading
HEADING_PROXIMITY := headings belong closer to the content they introduce than to the preceding block
COMPREHENSION_TEXT := readable text is not necessarily understood; titles, context, prior knowledge, examples, and vocabulary must fit the audience
MEMORY_TRANSFER_CAUTION := do not require users to remember codes, values, or instructions across locations when the interface can preserve or repeat them
READING_COST_CAUTION := reduce reading burden with scan structure, plain labels, local examples, and carried-forward context before adding longer instructions
NEEDLESS_WORDS := remove filler, self-congratulation, redundant instructions, and copy that does not change action or understanding
TEXT_AS_INTERFACE_LOAD := every heading, label, helper, tooltip, and paragraph should either change comprehension, confidence, repair, or action; otherwise remove or demote it
SENTENCE_SIMPLIFICATION := prefer active voice, direct verbs, short starts, no redundant prepositions, and no repeated meaning
FORM_LABEL := persistent, readable, and available during typing, validation, correction, and review
FORM_HINT := examples and format hints support ambiguous answers but must not replace labels
FORM_ERROR_TEXT := concise enough to scan, specific enough to repair, and close enough to the affected field
FORM_TEXTBOX_WIDTH := reflect expected answer length when it helps users notice wrong formats
TYPOGRAPHY_VISUAL_BASICS := beginner visual systems must prove readable hierarchy, line length, spacing, contrast, and responsive fit before expressive font pairing
```

## Components And Content Patterns

```text
BUTTON_ANATOMY := label + container + padding + state + affordance + outcome
BUTTON_PRIORITY := primary, secondary, destructive, and cancel actions must have distinct weight and safe order
BUTTON_PADDING := scale with label length and target size; do not let text crowd the edge
BUTTON_ACTION_PROOF := button text, order, size, alignment, and destructive styling must make the outcome clear before visual treatment is approved
ICON_TEXT_BALANCE := pair icon and text only when the icon speeds recognition and the label preserves meaning
ICON_RULE := universal icons may stand alone only when recognition is proven; unique icons need labels or onboarding
COLORED_ICON := use only when hue adds meaning or brand value without harming recognition
CARD_RULE := use for modular browsing, product summaries, status blocks, and lightweight grouped actions
LIST_RULE := use for fast title scanning, chronological items, or compact repeated actions
TABLE_RULE := use for comparison, sortable data, numeric alignment, and dense attributes
DASHBOARD_RULE := surface status, exception, comparison, and next action before decorative charts
SPLIT_VIEW_RULE := use when selection and detail must remain visible together
DRILLDOWN_RULE := use when small-screen focus matters more than comparison
THUMBNAIL_GRID_RULE := use when visual recognition dominates item selection
CAROUSEL_RULE := limit to small known sets or secondary discovery
PAGINATION_RULE := use for bounded sets needing position and chunking
INFINITE_SCROLL_RULE := use for discovery only when position, footer, and filter escape are handled
ILLUSTRATION_RULE := explain empty states, onboarding, or brand warmth only when it does not delay task completion
GRADIENT_RULE := use to support depth, emphasis, or material signal; avoid as default background polish
SHADOW_RULE := tune offset, blur, spread, opacity, and color by elevation purpose and surface contrast
DEPTH_RULE := emulate a consistent light source before adding elevation
ELEVATION_SYSTEM := define small, medium, large, overlay, and interactive shadow states as tokens
INSET_RAISED_RULE := raised and inset surfaces need opposite highlight/shadow logic
IMAGE_CONTRAST_RULE := text over imagery needs stable contrast through overlay, reduced image contrast, colorization, or text shadow
ASSET_SIZE_RULE := photos, icons, and screenshots have intended sizes; avoid scaling past their clarity range
USER_CONTENT_RULE := uploaded images need crop, aspect-ratio, background-bleed, and fallback controls
EMPTY_STATE_VISUAL := use illustration or shape only when it supports state explanation and next action
SEPARATION_RULE := prefer spacing, background shift, or shadow before adding more borders
BORDER_REDUCTION_RULE := when borders pile up, try spacing, background shift, or shadow before adding another line
WHITE_SPACE_ROLE := whitespace is a grouping and attention tool, not leftover emptiness
VISUAL_STYLE_STACK := gradients, shadows, icons, photos, illustrations, cards, and buttons must each have a role in hierarchy, state, or meaning
MEDIA_IN_TOOL := raster, vector, video, and exported assets need scale, crop, format, density, and fallback behavior before being accepted in UI compositions
IMAGE_MODE := choose literal, symbolic, abstract, photographic, illustrative, diagrammatic, or typographic image modes by message, audience expectation, and production reality
TYPE_IMAGE_RELATION := text and image may reinforce, contrast, repeat, or intentionally diverge, but the relationship must be named before approval
VISUAL_SYSTEM_VARIATION := a system can allow deliberate variation when the changing dimension is itself repeatable and useful for differentiation
UI_CRAFT_STACK := interface polish is a stack of purpose, perception, grid, spacing, type, color, components, states, and handoff; weak lower layers make surface polish fragile
LOW_DETAIL_FIRST := start with feature and rough structure before committing to layout shell, color, or decoration
SKETCH_BEFORE_SURFACE := sketch alternative stories, flows, and layouts before polished pixels because surface fidelity can hide weak product thinking
SYSTEMATIZE_EVERYTHING := repeated spacing, type, color, radius, shadow, and opacity decisions should become constrained scales
TRANSPARENT_BASICS := good UI basics make the interface feel obvious by aligning visibility, affordance, feedback, and expectation
PERCEPTION_GAP_FILL := ambiguous alignment, spacing, repetition, or contrast makes users invent false groups, so visual relationships must be tested by perceived grouping rather than raw geometry
BIG_SCREEN_BASELINE := design the largest meaningful content, viewport, and state before approving responsive compression
GRID_AS_SCAFFOLD := grids guide density and relationship, but content hierarchy and task sequence may justify breaking columns
DETAIL_REASON := every visible detail should earn its place through task clarity, comprehension, consistency, accessibility, brand signal, or production constraint
SIMPLICITY_TEST := simplicity removes irrelevant work; minimalism fails when it hides needed context, controls, state, or recovery
ELEGANT_SIMPLICITY_VISUAL := visual simplicity succeeds when the remaining elements reveal structure, priority, control, and character rather than merely reducing visible objects
FORM_COLOR_RULE := required, optional, validation, warning, success, and disabled states need non-color cues
FORM_TOUCH_RULE := mobile forms need larger targets, comfortable spacing, keyboard hints, visible labels, and nearby errors
FORM_FLOAT_LABEL_RULE := allow only when readability, contrast, animation, and error states are verified
CLICKABLE_VISIBILITY := links and buttons must be identifiable by shape, placement, color, underline, or component role without cursor probing
VISITED_LINK_RULE := preserve a visible distinction between visited and unvisited text links when navigation history matters
LOW_CONTRAST_TYPE := fail when text is both small and low contrast
HIDE_CUE := hidden controls need visible scent through labels, previews, layout, state, or local examples
HIDDEN_EXIT_CAUTION := close icons and concealed affordances are insufficient when users cannot predict where to find them
STYLE_TREND_CAUTION := neumorphism, glass, heavy blur, and low-contrast material effects are allowed only when affordance, contrast, focus, and state clarity survive
RULE_BREAK_PROOF := break layout, type, image, color, or spacing conventions only when the communication gain, audience fit, and lost affordance are explicit
REFERENCE_STYLE_CAUTION := historical, trendy, vernacular, or subcultural style should be sampled as communication context, not copied as surface fashion
PRODUCTION_AWARE_COMPOSITION := approve print, screen, export, or fabrication layouts only after scale, medium, reproduction, asset integrity, and final approval path are checked
DEVELOPER_UI_BASIC_STACK := implementation-ready UI needs color roles, type roles, spacing, grid, component anatomy, states, labels, and interaction feedback before code values are frozen
IMPLEMENTATION_VISUAL_CHECKLIST := before shipping a component, verify size, spacing, contrast, borders, icons, labels, state variants, responsive behavior, and accessibility instead of trusting defaults
COLOR_TYPE_COMPONENT_ALIGNMENT := palette, typography, and component styling must be reviewed together because changing one changes perceived hierarchy and affordance
```

## Responsive Checks

```text
PASS IF no text overlaps at mobile, tablet, desktop, and wide desktop
PASS IF fixed-format elements have stable dimensions or aspect ratios
PASS IF interaction targets remain reachable and distinguishable
FAIL IF hover states, labels, counters, or dynamic content resize the layout unexpectedly
```

## Source Bands Absorbed

Provenance was kept in the original global design-corpus ledgers. This repo-local copy exposes only reusable composition, layout, typography, and component-visual rules and does not import host-specific corpus ledgers.

## Visual Pages Inspected

Visual evidence is intentionally kept in `docs/visual-review/` manifests and contact sheets. Use those artifacts before making figure-specific layout, hierarchy, typography, or component claims.
