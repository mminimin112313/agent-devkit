# UX Interaction Reference

Use for flows, navigation, forms, interaction patterns, UX writing, onboarding, errors, and user effort.

Every rule here protects one user outcome. Apply a rule only when that outcome is at risk in the current context; read `restraint-and-rule-intent.md` before adding confirmations, success messages, helper text, badges, empty-state copy, onboarding, or notifications.

## Flow Rules

```text
GOAL_PATH := shortest_clear_path_to_user_goal
WAYFINDING := PASS IF user_knows(where_they_are, what_is_available, what_happens_next)
PROGRESSIVE_DISCLOSURE := reveal advanced detail only after the simpler decision is stable
PROGRESSIVE_DISCLOSURE := hide_detail_only_when_primary_decision_stays_clear AND reveal_path_is_descriptive
STATE_VISIBILITY := show loading, saving, validation, empty, error, success, and disabled states
RECOVERY := make destructive or high-risk actions reversible first; confirm only when the loss is irreversible and costly and undo is not feasible
WIZARD := use_for_novel_long_or_branched_tasks; avoid_for_experts_creative_work_or_tasks_that_can_be_simplified
ACTION_ORDER := arrange primary secondary cancel and destructive actions by consequence and platform expectation
LOCAL_ACTION := place control near the object it changes
INTERACTION_POLISH := allowed only after cause effect state and recovery are clear
PESSIMISTIC_STATES := design empty, error, overflow, missing_asset, long_content, and user_generated_content cases before calling a screen done
SAFE_EXPLORATION := support uncertain action with undo, cancel, preview, reversible paths, or sandboxed changes
MIDSTREAM_CHANGE := preserve state and context when users change goals during a task
MIDSTREAM_CHANGE_SUPPORT := preserve state, context, escape, and recovery paths when users change goals midstream
DEFERRED_CHOICE := let users continue when a decision can safely wait
USEFUL_FRICTION := add friction only when it prevents harm, confirms consequence, improves consent, or protects attention; remove it when it only delays user value
ETHICAL_FRICTION := friction can be good when it protects privacy, safety, consent, reflection, abuse prevention, or long-term wellbeing
INCREMENTAL_CONSTRUCTION := support partial completion and visible progress for build-up tasks
MICROBREAK_RECOVERY := make resume state obvious after interruptions
PROSPECTIVE_MEMORY := place reminders and future-action cues near the relevant object
SIMPLE_UNDER_PRESSURE := test flows under hurry, interruption, rare use, uncertainty, and emotional stakes
MAINSTREAM_FLOW := default flows should serve mainstream users who want enough control and quick progress, with expert power kept discoverable but quiet
PLEASURE_IN_USE := repeated interactions should feel competent, smooth, and rewarding after the first impression; polish must reinforce control, not only novelty
CORE_AND_CONTEXT := design the core user action plus the moments immediately before and after it
CONTROL_FLOOR := keep enough control, feedback, and override for users to feel safe
TIME_REDUCTION := reduce thinking, waiting, reading, deciding, error recovery, and repeated micro-delay
SPARE_CAPACITY := leave users attention to think about their own goal, not the interface
WAIT_STATE := waiting is an interaction state; show cause, progress or uncertainty, expected next event, alternative action, retry, or cancellation when trust or flow is affected
WAIT_EXPERIENCE := design waits as service moments: perceived fairness, social cues, explanation, occupied time, progress, and recovery matter as much as elapsed time
PERCEIVED_PERFORMANCE := quick feedback, skeletons, optimistic states, and truthful progress can preserve attention, but fake certainty destroys trust
AUTOMATION_HANDOFF := automated actions need visible intent, confidence, status, override, correction, and human recovery when consequence is meaningful
AUTOMATION_DIALOGUE := if a system initiates, recommends, blocks, or changes action, it must explain what it noticed, what it intends, what the user can do, and when control returns
MODE_SAFETY := dangerous or high-consequence modes need unmistakable state, entry reason, exit path, confirmation, and recovery
PERFORMANCE_LOAD_SPLIT := reduce cognitive load, movement load, waiting load, and recovery load separately before claiming a flow is simple
TARGET_ACQUISITION := frequent or urgent actions need enough size, spacing, and reachable placement for the input method and user dexterity
DECISION_COST := response time and error risk rise as choices become more numerous or complex; simplify the decision, not only the visuals
BEHAVIORAL_LEVER_GATE := peak-end, loss-aversion, commitment, defaults, scarcity, and social-proof levers PASS only IF they serve the user's own stated goal AND keep consent, exit, and review visible; FAIL IF the lever mainly raises conversion against user interest (see Anti-Patterns And Dark Patterns in interface-patterns.md)
PEAK_END_MEMORY := design emotionally intense moments and final moments because users remember them disproportionately
LOSS_AVERSION_FLOW := when users might feel they are losing value, privacy, security, time, status, or progress, explain the tradeoff plainly and preserve review, undo, or exit
COMMITMENT_LADDER := ask for commitments in earned steps; each step must return value, preserve reversibility where possible, and avoid making prior micro-actions feel like traps
```

## Navigation And Information Architecture

```text
IF users_return_often THEN optimize for recognition, shortcuts, and stable locations
IF users_are_new THEN optimize for scent, labels, and visible next steps
IF hierarchy_is_deep THEN provide breadcrumbs, local navigation, search, or scoped menus
IF nav_item_names_overlap THEN rename by user intent rather than organization chart
BREADCRUMBS := use when depth or backtracking matters, not as a substitute for clear labels
ROUTE_MEMORY := preserve current category, filter, or object context when users move between list and detail
MENU_LOCATION := stable placement beats novel placement for repeated navigation
NAV_MODEL := choose hub_spoke, fully_connected, tree, step_by_step, pyramid, or flat by destination count, task sequence, and user mental model
DEEP_LINK := preserve route state and object context when users arrive from outside the normal path
ESCAPE_HATCH := every modal, wizard, deep hierarchy, and drilldown needs a clear way out
ENTRY_POINT := first action should be visible for each major user goal
SELF_EVIDENT_FLOW := users should understand purpose, current location, available action, and next step at a glance
SELF_EVIDENCE_TEST := before explaining a screen, remove question marks by making object, action, consequence, and next step visible in the interface itself
QUESTION_MARK_AUDIT := remove ambiguous labels, hidden affordances, unclear regions, uncertain destinations, and mismatched page names
SATISFICING_PATH := make the first reasonable option safe, descriptive, reversible, and close to the user's goal
MUDDLING_SUPPORT := preserve back paths, visited state, current location, and recovery because users operate with partial mental models
FAMILIARITY_TRANSFER := users bring expectations from similar products; use familiar behavior unless the new model is visibly better and learnable
MINDLESS_CLICK := extra steps are acceptable when each step has strong information scent and low uncertainty
MINDLESS_CHOICE_GATE := reduce choice effort by making labels obvious, options visibly distinct, and wrong turns cheap to recover
JUST_IN_TIME_HELP := difficult choices need brief, timely, unavoidable guidance placed at the decision point
NAV_TRUNK_TEST := from any deep page users must identify site_id, page_name, main_sections, local_options, current_location, and search
PAGE_NAME_MATCH := page heading should match the link or button that led there closely enough to preserve confidence
CURRENT_LOCATION_CUE := current section and page cues must be visually strong enough for hurried scanning
SEARCH_BOX := large or content-rich sites need a familiar visible search box before advanced search options
HOME_ORIENTATION := for first visits or unfamiliar products, home and entry pages answer what_this_is, what_can_i_do, and where_to_start; add why_it_matters only when the value is not obvious from the first two
BREADCRUMB := use for large deep hierarchies as lightweight location and upward navigation, not as primary IA
ORGANIZE_BY_BEHAVIOR := group navigation and flow by what users do and the order they expect
DESIRE_PATHS := observe real user paths and adapt IA to the routes people already take
MULTIDEVICE_LAYERING := map user needs, tasks, features/content, and devices separately before assigning channels
EXPERIENCE_LAYER_AUDIT := sequence strategy, scope, structure, skeleton, and surface; do not repair surface symptoms before checking upstream intent and information architecture
SIDE_DOOR_NAVIGATION := support credible alternate entry paths from search, notifications, links, history, and support without losing object context
SCROLL_PROOF := important content below the fold needs scent, partial reveal, position feedback, or task evidence before relying on scrolling
```

## Forms

```text
INTERACTION_COST := reduce steps memory effort pointer_travel and unnecessary decisions
FIELD_ORDER := match user mental model and real-world data sequence
LABELS := persistent enough to survive typing, errors, and review
VALIDATION := inline when local, summary when cross-field, delayed only when unavoidable
ERROR_COPY := state problem + location + repair action
OPTIONALITY := mark optional fields when most fields are required; mark required when few are required
INPUT_HELP := show examples for format ambiguity, not for obvious fields
FIELD_CHOICE := match answer_shape, correction_cost, device_context, and option_count
CHECKOUT_FORM := optimize for trust, recognizable payment fields, grouping, progress, and recovery
LOGIN_FORM := minimize fields and make account recovery visible without competing with sign-in
FORM_GROUP := group by user mental model and completion sequence, not database schema
FORGIVING_FORMAT := accept reasonable input variants and normalize them when precision risk is low
FORGIVING_FORMAT_REPAIR := accept varied formats when user intent is clear, then normalize, confirm, or explain constraints according to error cost
STRUCTURED_FORMAT := constrain input when precision, error cost, or downstream machine interpretation is high
SMART_DEFAULT := prefill likely values only when they remain visible, reviewable, and easy to correct
FORM_AS_EXCHANGE := ask only when user value, product need, privacy risk, and effort cost are justified
FORM_PROJECT_DISCOVERY := before form design, name information need, data quality need, success metric, stakeholders, downstream owner, device constraint, and workflow position
FORM_DIMENSIONS := question_content + interaction_mechanics + visual_layout must be designed together
ANSWER_MODEL := each question must pass comprehension, retrieval, judgment, and response_mapping
QUESTION_SCOPE := each form question covers one concept unless users naturally treat the answer as one unit
QUESTION_ORDER := order by user mental model, dependency, difficulty, sensitivity, and review need
SENSITIVE_FIELD := ask late, explain purpose, reduce precision, or remove when trust risk exceeds value
QXQ_RECORD := complex forms need question_by_question purpose, answer_shape, control, validation, dependency, privacy, analytics, and owner notes
QXQ_REVIEW_GATE := use question_by_question records to catch unnecessary fields, ambiguous wording, wrong control choice, hidden privacy risk, weak validation, and orphan ownership before implementation
```

## Form Visual Rules

```text
QUESTION := ask one concept at a time with vocabulary users understand
FIELD_TYPE := choose by answer shape, error risk, device, and option count
LABEL_PLACEMENT := preserve context during typing, validation, review, and correction
VERTICAL_PATH := reduce zigzag scanning and keep completion direction obvious
BUTTONS := label by outcome; avoid reset; align primary action with completion path
HELP := keep question-level help visible when users need it to answer correctly
PLACEHOLDER := FAIL IF it replaces a persistent label
COLOR := do not rely on color alone for required, optional, validation, or error state
PAYMENT_FIELD := preserve familiar card, date, and security-code grouping unless a local reason improves completion
FIELD_FRICTION := remove fields, split questions, or change control type before adding explanatory copy
AUTOCOMPLETE := use when suggestions are relevant, fast, and correctable
LIST_BUILDER := use when users are composing, ordering, or selecting a set
OPEN_VS_CLOSED := open input supports unknown answers; closed input supports known sets, comparison, validation, and lower correction effort
DROPDOWN_CAUTION := use only for short known option sets where scanning cost is acceptable
LONG_OPTION_SET := prefer search, autosuggest, grouping, or progressive narrowing
DATE_INPUT := choose text, segmented field, calendar, or relative picker by recall mode, range, precision, and device
NUMBER_INPUT := use slider, stepper, or spinner only when bounds and increments match intent
TEXT_BOX_WIDTH := match expected answer shape when it improves comprehension and error detection
FLOAT_LABEL_CAUTION := use only with proven readability, contrast, animation clarity, and error-state behavior
REQUIRED_OPTIONAL_POLICY := mark the minority state consistently and never by color alone
```

## Validation And Error Flow

```text
VALIDATION_TIMING := match the cost of waiting, the confidence of detection, and user correction effort
FORM_VALIDATION_POLICY := validation timing, placement, copy, submit behavior, and duplicate-submission handling should reduce repair effort without interrupting answer formation
INLINE_ERROR := use when one field can be repaired locally
SUMMARY_ERROR := use when errors are spread across sections or steps
VALIDATION_FEEDBACK := preserve input + explain rule + locate problem + name repair action
DISABLED_PRIMARY_ACTION := use cautiously because it can hide the reason action is unavailable
DISABLED_ACTION := prefer enabled_with_repair_feedback OR remove_unavailable_action_with_reason
PROGRESS_INDICATOR := show meaningful progress in multi-step forms, not decorative step count
SUCCESS := confirm completion only when the result is not visible in place, happened elsewhere, took noticeable time, or has a next consequence the user must know; a visible in-place result is its own confirmation
DESTRUCTIVE_ACTION := visual danger treatment plus undo when feasible; confirmation only when the action is irreversible and costly
SEMANTIC_PRIORITY := danger, success, and neutral colors must not overpower the true primary task unless consequence demands it
PREVIEW := show outcome before destructive, expensive, or visual changes
CANCELABILITY := long, risky, or uncertain operations need a stop path
UNDO := prefer multilevel undo for exploratory editing and object manipulation
COMMAND_HISTORY := expose repeatability and audit trail for complex or expert workflows
VALIDATE_WHEN_READY := validate only after enough information exists and feedback will not disrupt answer formation
SERVER_VALIDATION := required for security, eligibility, identity, payment, persistence, and policy rules
ERROR_PLACEMENT := put field errors near fields and global summaries above affected groups with links when needed
WARNING_MESSAGE := allowed answer plus risk, unusual value, irreversible consequence, or likely mistake
SUCCESS_MESSAGE := use when reassurance changes confidence, next action, or completion certainty
SYSTEM_PROCESSING := show saving, submitting, retry, delay, and duplicate-submission protection when latency matters
LOADING_PATTERN := choose spinner, skeleton, optimistic update, progress bar, queued status, blocking overlay, or inline retry by wait length, layout stability, certainty, and reversibility
DISABLED_SUBMIT_CAUTION := avoid silent disabled primary actions; explain requirements or return actionable feedback
DOUBLE_ENTRY := require repeat entry only when hidden error risk is greater than copying burden
PASSWORD_VISIBILITY := provide show-hide when correction value outweighs privacy exposure
ERROR_OWNERSHIP := write errors as system repair guidance, not user blame; name what happened, why it matters, and what action restores progress
FAULT_TREE_REPAIR := for severe failure paths, identify root causes, prevention controls, detection signals, recovery path, and owner before finalizing copy or layout
SLIP_VS_MISTAKE := treat slips with feedback, constraints, placement, and interruption recovery; treat mistakes with clearer mental models, situational awareness, reduced noise, and decision support
ROOT_CAUSE_ERROR_DESIGN := repeated errors require design investigation across constraints, feedback, pressure, training, policy, incentives, and environment before blaming operator behavior
```

## Prototype And Testing Rules

```text
PROTOTYPE := testable_question, not only visual_mockup
TEST_SCOPE := define what_to_validate + fidelity_needed + non_goals before prototyping
PROTOTYPE_DECISION_GATE := prototype when uncertainty concerns information architecture, state transitions, device behavior, real content or data, stakeholder alignment, user testing, or costly implementation risk
FIDELITY_BY_RISK := choose prototype fidelity by decision risk, audience, artifact lifespan, interaction realism, and what failure will teach
PROTOTYPE_FIDELITY_MATRIX := choose paper, clickable, coded, or remote prototypes by learning goal, interaction realism, content and data need, audience, accessibility, time, and discard or reuse plan
PROTOTYPE_AS_CONTRACT := record learning goal, expected signal, constraints, reviewer role, and decision owner before presenting a prototype
PENCILS_BEFORE_PIXELS := explore divergent structure, story, and flow at low fidelity before visual precision makes weak ideas feel expensive
IA_PROTOTYPE := test navigation_structure through user tasks before sitemap approval
USABILITY_TEST := representative_users + independent_tasks + observation_criteria + note_owner + synthesis_time
PROTOTYPE_TEST_SESSION := plan tasks, participant role, facilitator script, observation criteria, reset state, capture method, and synthesis owner before running prototype research
REMOTE_TEST := use only when prototype can stand alone and recording is ready
REAL_DEVICE_PROTOTYPE := test browser and target-device behavior when viewport, touch, overlay, animation, performance, or hardware context changes the learning signal
PROTOTYPE_STATE_MAP := prototype proof needs triggers, transitions, overlays, component states, conditional paths, reset behavior, and fallback routes when they affect the task
FIDELITY_TRANSITION := each fidelity jump must name what can now be learned, what is still unresolved, and which artifact should be discarded or refined
PROTOTYPE_NOT_PROOF := prototypes cannot prove final conversion, full accessibility, production performance, or final visual impact unless the prototype environment measures those properties
STAKEHOLDER_FEEDBACK := separate domain_signal, decision_signal, taste_feedback, and out_of_scope_feedback
SEARCH_FILTERS := use when users know criteria but not exact item; show contextual filters that reduce result space
INFINITE_SCROLL := allow only when discovery dominates and footer recovery filtering are not harmed
RELATED_ACTIONS := place controls near the object they affect and size targets for repeated use
TABLE_ROWS := expose hover details or expandable rows only when local context speeds comparison
MICROINTERACTION := define trigger + rule + feedback + constraint
ANIMATION := orientation_or_feedback_before_style
BUTTON := visible affordance + adequate padding + state + outcome_label
ROW_DETAIL := hover or expansion is valid only when the hidden content is secondary and locally useful
CARD_OR_LIST_OR_TABLE := choose by user intent: browse, scan, or compare
COMPONENT_CHOICE_BY_SCAN := choose cards, lists, tables, forms, navigation, and microinteractions by the user scan mode and comparison need before surface style
PATTERN_REFERENCE := use references/interface-patterns.md when choosing screen type, navigation model, collection pattern, command surface, data exploration pattern, or form control family
PATTERN_SELECTION := choose UI patterns by context, user goal, constraints, accessibility, performance, and known tradeoffs
CONSISTENCY_EXPECTATION_TEST := consistency should reduce uncertainty, but variation is allowed when it signals state, risk, hierarchy, or context
PATTERN_COMPOSITION := combine patterns only when each pattern has a distinct job and duplicate content is removed
TEST_SMALL_OFTEN := prefer small frequent tests over delayed large formal studies
TINY_USABILITY_TEST := use small repeated sessions with real tasks, observers, and immediate synthesis when teams are arguing from opinion or waiting for a large study
FIRST_IMPRESSION_TEST := ask users what they think the screen is, what it offers, and where they would start before task execution
OBSERVED_PROBLEM_ONLY := prioritize behavior seen in sessions over opinions, predictions, or literal feature requests
FIX_SERIOUS_FIRST := rank observed problems by task harm, confidence loss, frequency, and repair cost
KAYAK_PROBLEM := ignore brief wrong turns when users notice quickly, recover unaided, and remain confident
ADD_LESS_RULE := when users miss meaning, remove obscuring noise before adding instructions or features
SINGLE_SENTENCE_VISION := describe the core experience in one short user-language sentence before prototyping
USER_STORY_VISION := use a brief credible story to encode context, user motive, core action, and success criteria
STORYBOARD_PROOF := storyboards, journey maps, service diagrams, and narrative flows must be visually inspected for sequence, actor, touchpoint, emotion, and handoff clarity
SCENE_STRUCTURE_FLOW := complex journeys should map scene goal, actor, context, trigger, action, system response, emotion, transition, and unresolved question before screen design
MODULAR_STORY_FLOW := multidevice or branching experiences need main plot, subplot, reusable scenes, entry points, and continuity rules so modules do not fragment the user story
EXTREME_TARGETS := use ideals such as instant, effortless, at_a_glance, and error_free as directional constraints
STAKEHOLDER_SEEING := let stakeholders watch users and own the problem before trying to win by argument
PERSUASION_TEST := test defaults, scarcity, rewards, social proof, and fear appeals for comprehension, consent, exit, and long-term trust
SOCIAL_PROOF_TEST := reviews, counts, testimonials, and popularity cues need source clarity, freshness, representativeness, abuse controls, and a non-social decision path
STORY_DECISION_SUPPORT := use pictures and stories to clarify sequence, consequence, identity, or memory; do not let narrative emotion replace evidence users need to decide
UX_FOUNDATION_SEQUENCE := beginner or remedial UX work should move through user evidence, problem definition, divergent ideas, rough structure, prototype, usability signal, and iteration before visual polish is treated as progress
USER_RESEARCH_METHOD_GATE := choose interviews, observation, card sorting, expert review, eye tracking, field studies, usability tests, remote tests, or personas by the learning question, context access, evidence strength, and synthesis owner
INTERACTION_ROLE_BOUNDARY := interaction design owns user goal translation into behavior, feedback, state, wireframes, and prototypes; do not collapse it into visual styling or broad product strategy without recording the missing owner
CONTENT_TESTING_GATE := UX writing and interface content should be tested for comprehension, task completion, trust, accessibility, localization fit, and repair behavior before being treated as final
MICROCOPY_STATE_MATRIX := applies to reusable content libraries and design systems, not to one-off screens; buttons, labels, errors, empty states, confirmations, onboarding, help, notifications, voice, and settings copy need purpose, state, risk, owner, voice rule, and test signal
USER_CENTERED_CONTENT_GATE := for content entering a reusable pattern only; content must name audience, task moment, channel, action consequence, accessibility, localization, measurement, and maintenance owner before it enters a reusable pattern
AI_ASSISTED_CONTENT_GATE := AI-generated UX content is draft material until a human verifies factual accuracy, audience fit, bias, ethics, accessibility, source traceability, and measurable task effect
```

## Motion And Microinteraction Rules

```text
MICROINTERACTION_CONTRACT := trigger + rule + feedback + loop_or_mode + constraint
TRIGGER := user_action OR system_event OR time_or_threshold
FEEDBACK := tell users that an action happened, is happening, failed, or changed state
PATTERN_FEEDBACK := when notifications, validation, filters, loading, or success feedback exist, decide their timing + channel + persistence + dismissal; whether success feedback exists at all follows SUCCESS
ANIMATION_PURPOSE := orientation + continuity + progress + attention + affordance
MOTION_PROTOTYPE_PROOF := motion examples need trigger, duration, easing, transformation purpose, scroll behavior, interruption behavior, and reduced-motion fallback
MOTION_LIMIT := avoid motion that delays repeated tasks, causes uncertainty, or hides state change
LOADING_ANIMATION := communicate waiting state and progress expectation where possible
TRANSITION_ANIMATION := preserve object continuity between states, especially list_to_detail or menu_open_close
DELIGHT := add only after usability, accessibility, and task speed remain intact
```

## Six Minds Research And Flow

```text
SIX_MINDS_FLOW := evaluate each flow through attention, wayfinding, language, memory, decision, and emotion
MICROQUESTION_FLOW := map every question users ask before commitment and answer it at the right moment
PROBLEM_SPACE := expose current_state, goal_state, operators, blockers, subgoals, and next_step in user terms
APPEAL_ENHANCE_AWAKEN_FLOW := attract with what users seek, retain by solving the real problem, and deepen value through proven goals or fears
VIRTUAL_WAYFINDING := digital spaces need deliberate cues for where_am_i, where_can_i_go, how_do_i_move, and what_happens_next
VOICE_WAYFINDING := voice flows need listening state, context retention, available commands, current topic, and repair cues
GESTURE_DISCOVERY := hidden gestures require proven audience expectations or visible teaching cues
EXPECTED_FLOW := identify what prior service, app, or physical process users are using as their navigation model
CONTEXTUAL_INTERVIEW := observe people in their real work or life context while asking open questions about what they are doing and why
SIX_MINDS_RESEARCH := tag observations by what users attend to, how they move, exact words, expectations, decisions, and emotions
WHY_NOT_ONLY_WHAT := survey and task metrics need contextual observation before root-cause design decisions
RAW_LANGUAGE_CAPTURE := record and transcribe sessions when wording, expertise, search terms, or AI commands matter
AFFINITY_BY_MIND := synthesize segments by recurring cognitive dimensions rather than demographics alone
PERSONA_EVIDENCE_GATE := personas are useful only when grounded in observed behavior, goals, constraints, and decision differences that change design choices
JOURNEY_MAP_CAUTION := journey maps are evidence only when stages, actors, channels, pain points, decisions, and ownership are legible and grounded in observed behavior
PROTOTYPE_WITH_MIND_LENSES := test prototypes for gaze, interaction metaphor, language fit, expectation fit, decision support, and hesitation or fear
LOW_FIDELITY_SIGNAL := keep prototypes visibly unfinished when the goal is concept and flow feedback
COMPARABLE_TESTING := compare prototypes with competitors or familiar alternatives to expose conventions and unmet needs
PROTOTYPE_WITH_COMPARABLES := test prototypes against familiar alternatives when conventions, metaphors, or user expectations are the main uncertainty
EXPERIENCE_LIFECYCLE := adapt help, language, evidence, and reassurance as users move from novice questions to specific implementation concerns
```

## UX Writing

```text
COPY := useful + specific + concise + timely
BUTTON_LABEL := verb + object when ambiguity exists
EMPTY_STATE := explain current state + useful next action when the user can act; transient filter or search empties need one plain line naming the filter and how to clear it; read-only empties need nothing beyond the absence itself or one plain line when absence is ambiguous; no illustration or call to action
CONFIRMATION := when a confirmation is justified, name consequence, scope, and reversibility in the action label itself, not in a generic are-you-sure question
ERROR_MESSAGE := avoid blame; name the fix
EMPTY_STATE_ACTION := include the smallest useful next action only when a valid action exists, especially when production data is absent
TONE_MATCH := copy tone should match visual personality and risk level
MANIPULATIVE_COPY := FAIL IF opt_out_or_secondary_action_copy pressures, shames, hides cost, or obscures consequence
COPY_REMOVAL := cut intros, redundant instructions, explanatory padding, click_here links, passive voice, slow starts, and repeated ideas
CONVERSATION_TUNING := tune detail by time_pressure, error_risk, consequences, and shared_knowledge
VOICE_CHART := define personality, relationship, language traits, and forbidden tones before scaling content across teams
CONTENT_FIRST_FLOW := model the exchange as what_user_says_or_needs + what_system_answers + what_user_does_next before polishing screens
UX_TEXT_PATTERN := each title, label, button, help, notification, empty state, error, and confirmation needs purpose, audience, moment, and consequence
CONTENT_MEASUREMENT := measure comprehension, task success, conversion, retention, support contacts, search refinement, error repair, and trust signals before declaring copy better
UX_REPAIR_METRICS := UX repair should pair behavioral evidence, analytics, support signals, task success, conversion, accessibility, and stakeholder goals before declaring a fix effective
AI_COPY_GUARD := generated UX text must be checked against voice, factuality, policy, localization, accessibility, and consequence before shipping
LLM_CONTENT_MEASUREMENT := LLM-based UX content needs intent success, factuality, safety, repair rate, user trust, escalation, and content-owner review before scale
CONTENT_LIFECYCLE := UX text needs source, owner, structured fields, reuse rules, localization, analytics, CMS constraints, and retirement path when it lives beyond one screen
REGULATED_CONTENT_TRACE := regulated or policy-sensitive UX content needs source of truth, approver, version, jurisdiction, expiration, and audit trail before release
OMNICHANNEL_COPY := content reused across app, email, notification, support, and service touchpoints must preserve meaning, timing, and consequence in each channel
INCLUSIVE_CONTENT := avoid wording that assumes ability, culture, device, identity, prior knowledge, or emotional state without evidence
LOCALIZATION_READY := design strings, placeholders, variables, examples, and tone so translation can preserve meaning and layout
LOCALIZED_PATTERN_CHECK := translated interface guidance needs local task vocabulary, example relevance, layout fit, and convention checks before reuse
LOCALIZED_UX_VISUAL_GATE := localized UX sources or examples with broken text extraction can inform layout, sequence, emphasis, and diagram structure only after visual inspection; do not infer precise prose rules from mojibake
PRACTICAL_FORM_STACK := forms need grouped fields, persistent labels, high-contrast borders, validation timing, optional/required handling, and multi-step split when length harms completion
FORM_BUTTON_ALIGNMENT := form and button choices should preserve scan order, target clarity, error repair, and expected submit/cancel hierarchy
IMPLEMENTATION_COPY_GATE := no UI is ready until every state that actually occurs has its copy decided; deciding means written OR deliberately absent with a reason, because helper text, confirmations, and success messages are added only when INPUT_HELP, SUCCESS, and DESTRUCTIVE_ACTION call for them
DISABLED_COPY_GATE := disabled or unavailable actions need nearby reason or repair path when users can reasonably want the action
FRONTEND_STATE_GATE := before polish approval, each of empty, loading, error, success, disabled, focus, selected, overflow, and long-content is either defined or marked n/a with a reason; success follows SUCCESS
PESSIMISTIC_STATE_DESIGN := design empty, error, overflow, long-content, missing-asset, and edge states early enough to shape the component
INTERACTION_COST_BUDGET := reduce steps, decisions, motor effort, waiting, and memory burden before adding new UI controls or visual polish
COGNITIVE_LOAD_BUDGET := minimize simultaneous choices, unfamiliar terms, decorative noise, and hidden dependencies when users are learning or deciding
DISABLED_ACTION_CAUTION := unavailable actions need a visible reason or repair path when users can reasonably expect to use them
DESTRUCTIVE_FRICTION := destructive actions need consequence naming and undo or recovery when feasible; add confirmation only where undo cannot exist
HANDOFF_CONVERSATION := handoff should describe what the user is trying to do, what the system says back, and what the next repair or progress step is
NOTIFICATION_VALUE := each notification must prove user value, urgency, actionability, frequency limit, dismissal path, and channel fit
RECIPROCITY_BOUNDARY := free trials, gifts, samples, favors, and concessions must be framed as optional value, not as pressure that obscures cost, consent, or cancellation
```

## Source Bands Absorbed

Provenance was kept in the original global design-corpus ledgers. This repo-local copy exposes only reusable flow, interaction, form, research, testing, and content rules and does not import host-specific corpus ledgers.

## Visual Pages Inspected

Visual evidence is intentionally kept in `docs/visual-review/` manifests and contact sheets. Use those artifacts before making figure-specific interaction, form, research, or content-design claims.
