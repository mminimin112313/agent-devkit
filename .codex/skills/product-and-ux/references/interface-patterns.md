# Interface Patterns Reference

Use for choosing UI patterns, screen types, navigation models, list/detail structures, command surfaces, data exploration, forms, mobile adaptations, and system-level pattern reuse.

## Pattern Selection

```text
START_WITH := user_context + user_goal + object_model + task_frequency + risk + device_context
PATTERN := reusable_problem_solution_tradeoff, not visual_template
CHOOSE_PATTERN IF it reduces user effort, preserves orientation, exposes the right object, or lowers action risk
REJECT_PATTERN IF it only matches surface style while task model, data shape, or device context differs
COMBINE_PATTERNS ONLY IF each pattern owns a distinct user question
PATTERN_RECORD := problem + context + forces + solution + behavior + accessibility + content + examples + variants + anti_patterns + evidence
LOCAL_VALIDATION := borrowed patterns still need validation against local audience, device, performance, and risk
PATTERN_SEARCH := search by user problem and interaction force, not only by component name
PATTERN_EVOLUTION_AUDIT := when a pattern catalog or design system changes, record added, renamed, narrowed, removed, and platform-specific patterns so reuse follows current user behavior instead of old names
PATTERN_CONTEXT_FIT := patterns are suggestions that must be adapted to user goal, device constraints, local conventions, content, accessibility, and risk; never paste an example as proof of fit
COMPETITIVE_SCAN := extract conventions and decision criteria, not surface styling
CONVENTION_DEFAULT := prefer familiar placement, naming, and behavior unless the replacement is self-evident or creates enough value to justify learning
CONVENTION_BREAK_TEST := break a convention only after proving the replacement improves comprehension, speed, safety, or accessibility for the local audience
MENTAL_MODEL_MIGRATION := when changing a familiar pattern, provide continuity, transition time, or side-by-side explanation for users with learned expectations
CLARITY_OVER_CONSISTENCY := break a local consistency rule only when the current user decision becomes significantly clearer
ACCESSIBILITY_PATTERN_PROOF := every pattern needs keyboard path, focus order, screen-reader name, target size, contrast, motion, and error recovery checks
LOCALIZATION_PATTERN_PROOF := long labels, RTL layout, translated tone, number/date formats, and variable content must fit before a pattern is accepted
EXPECTATION_BEFORE_PATTERN := discover user expectations and familiar conventions before choosing or changing an interface pattern
PATTERN_SELECTION_PROOF := pattern choice needs evidence for task fit, navigation model, data volume, state complexity, accessibility, and local consistency
VISIBILITY_BALANCE := expose status, available actions, and consequences without turning every possible control into simultaneous clutter
ELEMENT_PURPOSE := every UI element needs role, user expectation, state model, failure mode, and removal criteria before it becomes a reusable pattern
FOUR_SIMPLICITY_STRATEGIES := remove + organize + hide + displace
COMPLEXITY_TRANSFER := irreducible complexity must be assigned deliberately to user, system, support, documentation, or workflow owner
REMOVE_STRATEGY := cut non-core features, options, decisions, distractions, words, and time costs before styling alternatives
ORGANIZE_STRATEGY := group by behavior, hard-edged categories, relevant indexes, familiar patterns, grid, size, location, layers, and desire paths
HIDE_STRATEGY := hide infrequent but necessary detail only behind findable cues and recoverable reveal paths
DISPLACE_STRATEGY := move complexity to a better device, moment, actor, layer, computer, or user
SIMPLICITY_CONTROL_GATE := simplification must preserve enough user control, feedback, and recovery to avoid turning hidden complexity into anxiety
```

## Learning And Applying Patterns

```text
PATTERN_LIBRARY_USE := use collections, galleries, platform guidelines, frameworks, and design systems as inputs to judgment
PATTERN_TAILORING := adapt structure, labels, timing, states, and accessibility to local context
PATTERN_COMMUNICATION := pattern names should help design, code, content, QA, and product discuss the same decision
EVIDENCE_BASED_PATTERN := pattern popularity is not enough; name the usability problem it solves
DESIGN_EFFICIENCY := reuse patterns to reduce repeated invention, then spend effort on context-specific decisions
CONTENT_CONTRIBUTOR_SUPPORT := patterns need plain guidance when non-designers create or maintain content
```

## User Behavior

```text
SAFE_EXPLORATION := provide undo, cancel, preview, reversible paths, or sandboxed changes for uncertain actions
INSTANT_GRATIFICATION := let users get value before full setup when confidence or motivation is fragile
SATISFICING := make good-enough paths visible before expert optimization paths
SCANNING_BEHAVIOR := assume users scan for trigger words and visible affordances before reading explanatory copy
MUDDLING_THROUGH := support partial understanding with reversible paths, location cues, and forgiving recovery
MIDSTREAM_CHANGE := preserve input, state, and navigation context when users change direction
DEFERRED_CHOICE := allow progress without premature commitment when missing information is not blocking
INCREMENTAL_CONSTRUCTION := support building outputs piece by piece with visible partial progress
HABITUATION := keep repeated controls stable and support shortcuts
MICROBREAKS := make resume state obvious after interruptions
SPATIAL_MEMORY := keep object and control locations stable when users return often
PROSPECTIVE_MEMORY := put reminders, status, and future-action cues near the relevant object
KEYBOARD_ONLY := required for speed, accessibility, and expert use
INTERFACE_BEHAVIOR_LENSES := check safe exploration, instant gratification, satisficing, midstream change, deferred choice, incremental construction, habituation, spatial memory, and prospective memory before accepting a pattern
```

## Information Architecture

```text
IA_MODEL := separate information relationships from presentation before choosing screens
MECE := use mutually_exclusive_collectively_exhaustive categories when users must trust coverage
ORGANIZE_BY := alphabetical OR number OR time OR location OR hierarchy OR category OR facet
CHOOSE_ORGANIZATION_BY := how_users_remember_or_retrieve_the_item
VISIBLE_FREQUENCY := keep frequent items visible when speed, learning, or confidence matters
SEQUENCE := chunk jobs into steps when dependency, risk, or cognitive load is high
CARD_INFORMATION := use cards when independent identity, mixed attributes, or visual summary matter
SCREEN_SYSTEM := define overview, focus, make, and do screens before designing individual routes
SCREEN_TYPE_DECISION := choose overview, focus, make, do, dashboard, media browser, wizard, settings, stream, list/detail, or workspace patterns by user intent, information shape, and action consequence
BEGINNER_PIPELINE_PATTERN := beginner UX/UI work should move from problem, audience, research, persona, flow, wireframe, visual system, prototype, test, and handoff instead of starting with polished screens
FIVE_PLANES_TRACE := product experience decisions should trace strategy, scope, structure, skeleton, and surface; do not repair a surface symptom until upstream objective, requirement, IA, and interaction causes are checked
SCOPE_BOUNDARY := functional requirements and content requirements should name what is built, what is not, priority, owner, evidence, and acceptance signal before structure or screen pattern selection begins
SKELETON_ROLE_SPLIT := interface design, navigation design, information design, and wireframing have different jobs; record which one a pattern is proving before using a wireframe as a universal answer
HARD_EDGES := categories must have boundaries users can sort into consistently
INDEX_RELEVANCE := alphabetical, popularity, format, time, and space organization are valid only when they match retrieval strategy
PATTERN_ANCHORING := use familiar patterns, labels, images, or sequence anchors to make structure recognizable
SEARCH_AFTER_STRUCTURE := design browse structure before search except for large known-item retrieval
```

## Screen Types

```text
OVERVIEW := lists, grids, dashboards, maps, or option sets for choosing where to go next
FOCUS := one object plus local context and object-specific actions
MAKE := creation workspace with canvas, tools, palettes, inspector, and preview
DO := one task path with minimal branching and clear completion
FEATURE_SEARCH_BROWSE := use when catalogs need entry points, search, browsing, and featured shortcuts
STREAM_FEED := use when recency, social signal, or continuous updates dominate
MEDIA_BROWSER := use when visual recognition and collection management dominate
DASHBOARD := use for monitoring, exceptions, comparison, and next action
CANVAS_PALETTE := use for creation and direct manipulation with stable tool access
WIZARD := use for unfamiliar, risky, dependent, or long tasks
SETTINGS_EDITOR := group options, provide defaults, search, reset, and recovery
ALTERNATIVE_VIEWS := allow when users need genuinely different retrieval or analysis modes
MANY_WORKSPACES := support expert parallel work only with naming, persistence, and recovery
HELP_SYSTEM := contextual support surface, not a substitute for clear interaction
WALKTHROUGH := use when first success needs guided sequence
CONCEPT_WALKTHROUGH := use when users need a mental model before action
WORKFLOW_WALKTHROUGH := use when users need ordered steps
SETUP_PLAYTHROUGH := use when required setup blocks product value
SANDBOX_PLAYTHROUGH := use when safe practice builds confidence before real commitment
COACHMARK := use for contextual feature discovery; avoid as generic help overlay
MAINSTREAM_FIRST := default flows should serve users who want good_enough_quickly; expert power should not dominate the default surface
EXPERT_REQUEST_FILTER := expert requests should be separated into mainstream default, advanced option, support workflow, or removable edge case before adding visible complexity
OPEN_EXPERIENCE := combine similar specialized features into one general tool when user-defined use is more valuable than tailoring
```

## Navigation

```text
NAV_STRUCTURE := design separately from visual skin
DISTANCE := keep frequent paths short
GLOBAL_NAV := product scope and primary destinations
UTILITY_NAV := account, help, settings, sign-in, notifications, and meta tasks
ASSOCIATIVE_NAV := related objects or concepts without disrupting current hierarchy
HUB_SPOKE := central launcher for repeated returns
FULLY_CONNECTED := free exploration when information scent stays strong
TREE := hierarchical navigation with breadcrumbs, search, or escape support
STEP_BY_STEP := sequenced tasks with recovery and expert exits
PYRAMID := progressively narrowed hierarchy with clear upward and lateral paths
FLAT_NAV := small peer destination sets with low conceptual overlap
CLEAR_ENTRY_POINTS := reduce first-action uncertainty
MODAL_PANEL := bounded interruption with clear exit and state return
DEEP_LINK := URL or state restoration must preserve context
ESCAPE_HATCH := prevent dead ends
FAT_MENU := breadth plus preview when users need to choose among many destinations
BREADCRUMBS := location and backtracking support, not primary discovery
ANNOTATED_SCROLLBAR := useful when scroll position needs landmarks
ANIMATED_TRANSITION := preserve orientation between places
SITE_ID := persistent identity and home return affordance
PAGE_NAME := every page needs a prominent name that frames unique content
YOU_ARE_HERE := location cue must be strong enough to notice during quick scanning
TRUNK_TEST := validate deep pages by checking site_id, page_name, sections, local_navigation, current_location, and search
SEARCH_ENTRY := search box should use familiar search language, minimal default options, and scoped refinement after results when needed
HOME_ENTRY_POINTS := search, browse, sign_in, register, and start_process must look like entry points
TAGLINE := concise purpose plus differentiating value, not an abstract motto
TABS := active tab must visually connect to its panel and pop ahead of inactive tabs
```

## Layout Patterns

```text
VISUAL_HIERARCHY := match task priority and information relationship
GESTALT := proximity + similarity + continuity + closure reveal meaning
VISUAL_FLOW := follow the expected task sequence
PROGRESSIVE_DISCLOSURE := hide complexity only when the next decision stays clear
REGIONS := assign global, local, object, workspace, utility, and feedback ownership
CENTER_STAGE := dominant area belongs to the main object or task
GRID_OF_EQUALS := use when items have equal weight and comparable shape
TITLED_SECTIONS := use when scan labels are needed for groups
MODULE_TABS := use for related sections competing for one region
ACCORDION := use for compact mutually related sections where only some details are needed at once
COLLAPSIBLE_PANEL := hide supporting controls only when reveal path is obvious
MOVABLE_PANEL := expert workspace pattern requiring persistence and reset
```

## Mobile Patterns

```text
MOBILE_ESSENCE := start with what mobile users need in context, not desktop feature parity
DEVICE_HARDWARE := use camera, GPS, sensors, contacts, or biometrics only when it reduces effort or improves accuracy
LINEARIZE := prefer clear vertical sequences when screen size and attention are limited
COMMON_SEQUENCE := optimize the most common interaction before rare capabilities
VERTICAL_STACK := default mobile composition for scan and thumb flow
FILMSTRIP := use for visual sequences with quick lateral browsing
TOUCH_TOOLS := visible touch targets with gesture fallback and state feedback
BOTTOM_NAV := frequent peer destinations within thumb reach
INFINITE_LIST := discovery pattern requiring loading feedback, position memory, and filter escape
GENEROUS_BORDERS := reduce accidental touch in dense contexts
LOADING_INDICATOR := show truthful status when wait is noticeable
RICH_CONNECTION := offline, sync, and cross-device continuity must be explicit
NO_HOVER_DEPENDENCY := mobile patterns must not require hover, cursor probing, or subtle affordance discovery
MOBILE_DEEP_LINK := preserve requested content when users arrive from email, search, social, or notifications
FULL_SITE_ESCAPE := provide access to full capability when mobile subset cannot cover expected tasks
MOBILE_PERFORMANCE := avoid oversized assets and code that delay the task on unreliable networks
DEVICE_STRENGTH := assign tasks to desktop, mobile, wearable, physical environment, or service touchpoint by each device's strengths and weaknesses
DISPLACE_TO_USER := leave ambiguity, goal-setting, and personal organization to users when users are better suited than the system
THUMB_ZONE := frequent mobile actions should sit within comfortable reach unless risk, convention, or comparison demands another location
TOUCH_FEEDBACK := touch targets need pressed, loading, selected, disabled, and error feedback because hover cannot carry state
MOBILE_INTERRUPTION := design for resume after lock screen, call, notification, app switch, network loss, and partial input
MOBILE_APP_DESIGN_PIPELINE := define app concept, wireframe core screens, choose navigation, build reusable components, add data states, tune type and color, prototype flows, test on device, and only then systematize visual language
WIREFRAME_PURPOSE_GATE := wireframes should prove structure, content priority, navigation, and interaction states before typography, color, imagery, or brand polish dominates critique
MOBILE_SCREEN_SYSTEM := treat list, detail, login, feedback, recommendation, and settings screens as connected stateful surfaces rather than isolated mockups
```

## Lists And Collections

```text
SPLIT_VIEW := selection and detail remain visible together
DRILLDOWN := focus and small-screen clarity over side-by-side comparison
LIST_INLAY := quick detail expansion without losing list position
CARDS := independent items with mixed attributes, media, or summary actions
THUMBNAIL_GRID := visual recognition first, metadata and selection feedback second
CAROUSEL := small known sets or secondary discovery only
PAGINATION := position and chunking for bounded sets
INFINITE_SCROLL := discovery-first flow with footer, filter, and position tradeoffs handled
JUMP_TO_ITEM := long known lists with predictable lookup
ALPHA_NUMERIC_SCROLLER := alphabetic or numeric long-list navigation
NEW_ITEM_ROW := create in context when list itself is the creation surface
PAGINATION_VS_INFINITE := choose pagination for position, footer access, bounded search, and accessibility; choose infinite scroll for open-ended discovery with loading and position safeguards
FAVORITE := lightweight personal marker for recall
WISH_LIST := future intent collection with persistence, sharing, purchase, or planning semantics
ACTIVITY_FEED := recency stream where user identity, timestamps, and object links matter
FOLLOW := subscription to updates; define privacy, notification, and unfollow behavior
FRIEND_LIST := reciprocal social relationship; define request, acceptance, visibility, and removal behavior
SOCIAL_SIGNAL_PATTERN := visible participation, popularity, recommendations, and peer traces must identify source, scope, freshness, and user control because social cues can steer decisions before reflection
```

## Actions And Commands

```text
ACTION_LOCATION := controls belong near the object or region they affect
BUTTON_GROUP := related actions with clear priority and boundaries
ACTION_PANEL := object or task actions collected where menus/toolbars are too distant
HOVER_TOOLS := secondary discoverability only; provide non-hover path
PROMINENT_DONE := use when completion needs explicit commitment
ASSUMED_NEXT_STEP := use when completion is obvious and low risk
CTA_DIAGNOSTIC := calls to action need clear value, outcome verb, placement in the decision path, visual priority, state coverage, and measurement of task effect
SMART_MENU_ITEM := disable, hide, or explain invalid actions according to recoverability and discoverability
PREVIEW := reduce risk before destructive, expensive, or visual changes
PROGRESS := truthful wait state and expected completion where possible
CANCELABILITY := stop long or risky operations
MULTILEVEL_UNDO := safe exploration for reversible editing
COMMAND_HISTORY := audit and repeatability for complex work
MACROS := expert repetition when command sequences stabilize
DRAG_DROP := visible targets, feedback, reversibility, and keyboard alternative
DIRECT_MANIPULATION := object behavior should be visible before, during, and after manipulation
TRIGGER_ACTION_FEEDBACK := every interaction pattern needs trigger, action rule, and state consequence; feedback may be the visible state change itself
NOTIFICATION := message pattern with trigger, priority, channel, persistence, dismissal, and action
NOTIFICATION_CONTAINER := choose inline, toast, banner, badge, inbox, modal, or feed by urgency and scope
NOTIFICATION_ETIQUETTE := monitoring may be automatic, but interruption timing must respect user context and humility
NOTIFICATION_VALUE_PATTERN := reject notification patterns that lack user value, timing restraint, dismissal, accessible name, and clear owner
TOOLTIP := optional clarification for discoverable controls; never hide required instructions, errors, or primary labels inside it
POPOVER := use for local transient detail or lightweight action when state return, dismissal, focus, and mobile behavior are explicit
DRAWER := use for secondary navigation or task-adjacent panels only when orientation, width, close path, and state persistence are clear
CONTEXT_MENU := expert or object-local shortcut with visible alternative path and keyboard access
TOOLBAR := cluster frequent commands by object or mode; icons need recognition, state, disabled reasons, and tooltips or labels when ambiguous
```

## Complex Data

```text
DATA_QUESTION := choose visualization by user question before chart type
ORGANIZATIONAL_MODEL := reveal how data is grouped, related, ordered, and scoped
PREATTENTIVE_VARIABLES := position, size, color, shape, orientation, and motion encode relationships
BROWSE_EXPLORE := provide overview, zoom, filter, sort, and details according to exploration need
DATATIP := reveal exact value without destroying context
DATA_SPOTLIGHT := highlight focus while preserving surrounding structure
DYNAMIC_QUERY := immediate feedback for filtering and exploration
DATA_BRUSHING := linked highlighting across views
SORTABLE_TABLE := comparison and reordering for shared attributes
SMALL_MULTIPLES := repeated comparable views for pattern comparison
MULTI_AXIS_GRAPH := avoid unless users understand scale tradeoffs
```

## Forms

```text
FORGIVING_FORMAT := accept reasonable variants and normalize them
STRUCTURED_FORMAT := use when precision, error cost, or machine readability is high
FILL_BLANKS := use when sentence structure matches the user's mental model
INPUT_HINT := reduce ambiguity without replacing labels
INPUT_PROMPT := useful only when it does not disappear as required context
PASSWORD_STRENGTH := teach requirements while preserving repair path
AUTOCOMPLETION := relevant, fast, correctable suggestions
DROPDOWN := small known sets; search or autocomplete for large or unfamiliar sets
LIST_BUILDER := selecting, ordering, or composing a set
CHIP := compact selected item, filter, token, or attribute; deletion and overflow behavior must be explicit
BADGE := small status/count cue that needs scope, freshness, and accessible text
AVATAR := identity cue, not proof of personhood or permission; include fallback initials/image states and privacy rules
GOOD_DEFAULTS := reduce effort but remain reviewable
ERROR_MESSAGE := same-page, specific, repairable, and near the field
NEWSLETTER_SIGNUP := value proposition + minimal input + validation + confirmation + expectation or unsubscribe clarity
SOCIAL_SIGNUP := reduce effort with privacy, fallback login, and account-linking clarity
LAZY_SIGNUP := defer account creation until users experience value or need persistence
ECOMMERCE_STATE_PATH := cart, checkout, and product flows need price, quantity, inventory, validation, trust, confirmation, recovery, and cancellation states
VALIDATION_FEEDBACK_PATTERN := timing + field location + rule explanation + repair action
FORM_QUESTION_MODEL := comprehension + retrieval + judgment + response_mapping
FIELD_AUDIT := every field needs purpose, user-language label, answer shape, validation, privacy note, and owner
QUESTION_BY_QUESTION_PATTERN := form patterns are not ready until each question records purpose, wording, source, control, dependency, validation, privacy, analytics, and owner
SENSITIVE_QUESTION := delay, explain, reduce precision, or remove when trust risk is high
RADIO_BUTTON := one visible choice among mutually exclusive options
CHECKBOX := independent yes/no or multiple selections
SWITCH := immediate or clearly persistent setting change, not ordinary deferred submission
DROPDOWN_ALTERNATIVE := use autocomplete, search, grouped list, segmented controls, or progressive narrowing when option count or familiarity makes dropdown scanning expensive
DATE_CONTROL := choose by whether users recall exact date, compare a range, select near today, or enter administrative data
CALENDAR_PATTERN := use when spatial comparison of days, ranges, availability, or recurrence matters; otherwise prefer simpler date input
NUMERIC_CONTROL := text for exact arbitrary numbers; stepper for small bounded increments; slider for approximate value
CONDITIONAL_QUESTION := reveal when the controlling answer is stable and the dependency remains visible
GATEWAY_QUESTION := ask early when eligibility or routing prevents wasted effort
REVIEW_CONFIRMATION := use review screens when legal, payment, identity, or multi-step memory risk is high
QXQ_DOCUMENTATION := document each question's purpose, wording, source, control, validation, dependencies, privacy, analytics, and ownership
QXQ_PATTERN_REVIEW := use question-by-question documentation to decide which fields to remove, combine, split, defer, prefill, validate, or move to another channel
```

## Search And Filters

```text
AUTOCOMPLETE := complete known input when users have a target
AUTOSUGGEST := suggest possible queries, categories, or destinations when users are exploring
SEARCH_FILTER := apply criteria users understand through the product information architecture
MULTIPLE_FILTERS := show active criteria, interaction between criteria, and result count
LIVE_FILTER := update results immediately when latency is low and mistakes are recoverable
BATCH_FILTER := collect criteria before applying when latency, complexity, or expensive queries matter
FILTER_FEEDBACK := show active filters, empty-result repair, clear controls, and count changes
SCOPED_SEARCH := narrow search by category or context only when scope is visible and reversible
```

## Anti-Patterns And Dark Patterns

```text
ANTI_PATTERN := recurring solution that creates more harm than it solves
DARK_PATTERN := design that hides cost, risk, consent, consequence, or opt-out
INFLUENCE_PATTERN_RISK := persuasive patterns must disclose consequence, preserve opt-out, and avoid exploiting fear, shame, scarcity, or commitment pressure
COERCIVE_FRICTION := fail flows that make cancellation, privacy, refunds, support, or opt-out harder than acceptance without a user-protective reason
HIDDEN_COST_TRAP := fail patterns that reveal price, contract, risk, data use, or consequence only after commitment pressure rises
ABUSE_RESPONSE_PATTERN := social and communication features need reporting, muting, blocking, escalation, evidence capture, and policy feedback paths
MISUSE_RESPONSE_PATTERN := high-reach tools need prevention, detection, user reporting, operator escalation, and rollback when misuse is plausible
HAMBURGER_BASEMENT := important navigation hidden in a low-scent menu
MANIPULINK := link copy that manipulates instead of informing
CONFIRMSHAMER := opt-out copy that pressures through shame
TMI := too much information before users need it
MODAL_SMELL := interruption without clear scope, exit, state return, or proportional importance
POPUP_SMELL := attention capture without user value or timing justification
PATTERN_DEBT := bad patterns persist when short-term conversion hides trust and usability costs
```

## Pattern Composition

```text
COMPOSE_IF := each pattern owns a distinct job and total effort decreases
REUSE_ELEMENTS := reuse shared controls or data across patterns when roles remain distinct
CUT_DUPLICATE_CONTENT := remove repeated labels, categories, and actions created by combining patterns
INTERSTITIAL_PATTERN := bridge workflows only when transition meaning is clear
DATA_PERSISTENCE := preserve or clear repeated pattern data according to user expectation and error cost
CLARIFY_REPEATED_PATTERNS := distinguish similar patterns with labels, state, and visual role
TRADEOFF_REVIEW := after combining patterns, check whether complexity moved to another step
BREAK_PATTERN := allowed only after design-smell diagnosis, principle review, context review, predictability plan, accessibility check, and fallback
```

## Systems And Future Interfaces

```text
UI_SYSTEM := repeated patterns become system assets with usage criteria
ATOMIC_DESIGN := parts compose upward, but usage context must remain attached
FRAMEWORK := accelerates consistency but cannot replace product-specific pattern choice
DESIGN_SYSTEM_PATTERN := document context, audience, purpose, anatomy, behavior, states, accessibility, content, examples, variants, anti-patterns, and implementation links
PATTERN_ENTRY_CONTRACT := reusable pattern entries need problem, context, anatomy, behavior, variants, accessibility, examples, anti-patterns, and implementation notes
PATTERN_COMBINATION_AUDIT := combined patterns need duplicate-removal, data-persistence, state, accessibility, and total-effort checks
PATTERN_BREAK_GATE := break a familiar pattern only after diagnosing the design smell, naming predictability loss, and providing fallback
SYSTEM_REGION := reusable layout or product area that coordinates components, ownership, responsive behavior, and local rules
SYSTEM_FLOW := repeated sequence of patterns and components with validation, states, recovery, and success criteria
SYSTEM_SOURCE_OF_TRUTH := design assets, code, docs, and content must have named ownership and synchronization rules
CONNECTED_DEVICE := needs state sync, failure visibility, and ownership clarity
ANTICIPATORY_SYSTEM := must expose prediction, confidence, override, and correction paths
ASSISTIVE_SYSTEM := must preserve agency and explain support boundaries
NATURAL_INTERFACE := speech, gesture, and sensor input still need feedback, recovery, and alternatives
AUTONOMOUS_SYSTEM_BOUNDARY := machines that sense, decide, or act need visible goals, operating limits, escalation rules, override, audit trail, and graceful fallback before they enter everyday use
SMART_MACHINE_PATTERN := intelligent products need predictable behavior, legible signals, calm interruption, safe defaults, and negotiated control instead of surprising users with hidden agency
SOCIOTECHNICAL_PATTERN := large-system interfaces must reveal actor roles, incentives, externalities, maintenance paths, and community feedback instead of pretending the screen owns the whole outcome
CIRCULAR_SYSTEM_PATTERN := product and service patterns that claim reuse, repair, return, or recycling need status, handoff, logistics, responsibility, and failure recovery states
SIX_MINDS_PATTERN_CHECK := every major pattern should support attention, wayfinding, language, memory, decision, or emotion with named evidence
WAYFINDING_PATTERN := expose location, available movement, action metaphor, response timing, and next-state expectation
VOICE_PATTERN := include listening feedback, topic memory, follow-up scope, available commands, failure repair, and exit
AI_ASSISTANT_PATTERN := define cognitive support target, system boundary, confidence, explanation, override, correction, and fallback
MACHINE_PERSONALITY_PATTERN := anthropomorphic or emotional behavior is acceptable only when role, capability, dependency risk, and user expectation are honest and recoverable
NOVICE_EXPERT_LANGUAGE_PATTERN := support both plain user terms and expert vocabulary when audience expertise varies
DECISION_JOURNEY_PATTERN := order modules around user microdecisions instead of internal implementation sequence
PERSONALIZATION_PATTERN := expose what is personalized, why it changed, how to correct it, and what privacy or fairness risk it creates
VOICE_ASSISTANT_PATTERN := voice and agentic interfaces need listening state, confirmation, scope memory, interruption handling, correction, and non-voice fallback
IMPLEMENTATION_PATTERN_CHECK := every chosen pattern needs visible states, local actions, keyboard path, responsive behavior, and recovery route
SCAFFOLD_PATTERN := first usable product surface beats decorative shell; scaffold overview, focus, make, or do screen according to user goal
STATE_MATRIX := include empty, loading, partial, error, success, disabled, selected, focus, overflow, permission_denied, and long_content states when applicable
COMPONENT_API_PATTERN := component props should expose user-meaningful states and actions, not only visual knobs
VISUAL_QA_PATTERN := pattern acceptance needs artifact evidence for the viewport and state being claimed
PRIORITY_BY_COST := prioritize patterns and polish by frequency, user cost, risk, and confusion before rare visual details
PORTFOLIO_PROOF := visual design examples should show problem, constraint, before-after reasoning, state coverage, and production consequence instead of only final screens
SERVICE_COMPLEXITY_PATTERN := complex services need visible frontstage and backstage ownership, handoff status, escalation, and user-facing recovery rather than isolated screen optimization
DECISION_JOURNEY_MICROQUESTIONS := order interface modules around the questions users ask before commitment, not around internal feature categories
```
