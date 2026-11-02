# Design Principles Reference

Use for durable design judgment across product, UI, graphic, psychology, and ethics sources.

## Decision Rules

```text
CLARITY := PASS IF primary_action + current_state + next_step are visible without explanation
HIERARCHY := PASS IF first_attention_target matches user_goal
FEEDBACK := PASS IF every meaningful user action has a timely visible response
AFFORDANCE := PASS IF controls suggest how they can be used before trial-and-error
SIGNIFIER := PASS IF labels, icons, grouping, and states make interaction meaning explicit
CONSTRAINT := PASS IF invalid or dangerous actions are prevented, softened, or clearly recovered
MAPPING := PASS IF control_position_or_order matches the thing being controlled
CONSISTENCY := PASS IF repeated patterns behave and appear predictably across the product
ERROR_RECOVERY := PASS IF mistakes are reversible or recoverable with humane language
ETHICS := FAIL IF the design hides cost, risk, opt-out, consent, or consequence
PROBLEM_FIRST := PASS IF visual decisions trace back to user goal, context, and next action
GUESS_LESS_PRODUCT_DESIGN := product design decisions should replace opinion with research, observed behavior, existing data, and fast learning loops before major bets
COMMUNICATION_FIRST := PASS IF style choices can explain what message, audience, medium, and response they serve
PERCEIVED_ORDER := prefer what the user can perceive over raw geometry when judging balance or alignment
UTILITY_BEFORE_DELIGHT := motion, illustration, and effects must first clarify or reassure
FEATURE_FIRST := begin design from the thing users are trying to accomplish, not a blank layout container
DETAIL_TIMING := postpone color, borders, and decoration until structure and hierarchy are stable
PATTERN_LANGUAGE := reusable patterns encode context, forces, tradeoffs, and failure modes, not just UI shapes
INTERFACE_AS_MEANS := interface quality is measured by whether users reach their ends with confidence and control
ANTI_PATTERN_AWARENESS := recurring UI solutions must be rejected when they create hidden cost, confusion, exclusion, or trust loss
PREDICTABILITY_BEFORE_NOVELTY := break patterns only when a real contextual problem outweighs convention value
SYSTEM_AS_PRODUCT := design systems have users, adoption paths, quality metrics, support load, debt, and roadmap
SYSTEM_MAINTENANCE_REALITY := design systems are products with roadmap, support, adoption, contribution, migration, and retirement work
PRINCIPLES_AS_MEASUREMENT := design principles should evaluate decisions and outcomes, not decorate documentation
PSYCHOLOGY_AS_EVIDENCE := psychological heuristics should explain observed risk and guide tests, not become universal slogans
GUIDELINE_RATIONALE_CHECK := UI guidelines should be applied by the cognitive, perceptual, or operational reason they serve, not as context-free rules
USABILITY_CORE := average users should accomplish real goals without the interface becoming more trouble than the goal is worth
SELF_EVIDENCE := prefer screens that explain themselves through naming, layout, hierarchy, and affordance
COMMON_COURTESY_CHECK := usability is a form of respect; avoid spending user effort with unclear choices, hidden state, needless words, slow recovery, or avoidable uncertainty
COURTESY := do not spend user goodwill with unnecessary work, hidden information, avoidable errors, or careless recovery
SIMPLICITY_STRATEGY := simplicity is a durable strategy, not a surface style or absence of features
ELEGANT_SIMPLICITY := shallow simplicity ignores complexity; durable simplicity crosses through complexity to find the deeper pattern
USER_CONTROL := simple experiences give enough control over outcomes to reduce anxiety without forcing needless decisions
CONCEPTUAL_MODEL := complex systems must expose a usable model of objects, states, rules, and consequences before relying on controls alone
AUTOMATION_TRANSPARENCY := automated systems need visible intent, confidence, boundary, override, failure explanation, and handoff to human control
MACHINE_COMMUNICATION := smart systems should communicate with rich, natural, timely signals and understandable outcomes, not only machine-readable status or alarms
INFLUENCE_ETHICS := persuasion patterns are risk-bearing; scarcity, defaults, framing, rewards, reciprocity, commitment, fear, and social proof need consent, benefit, exit, and harm review
UNCONSCIOUS_INFLUENCE_CAUTION := automatic attention, emotion, belonging, loss aversion, and similarity effects may explain behavior but never justify hiding evidence, cost, consent, or exit
NATURE_PATTERN := use natural or organic forms only when their structural logic supports orientation, rhythm, hierarchy, resilience, or growth; decoration is not usability evidence
IDEA_BEFORE_VISUAL := visual form should support concept, context, and user consequence before style exploration starts
HARM_REVIEW := evaluate design outcomes for physical, emotional, social, exclusionary, agency, and justice harms before optimizing surface usability
USER_BLAME_CAUTION := repeated mistakes are design evidence until the system has proven clear labels, visible state, recoverable actions, and fair constraints
PUBLIC_CONSEQUENCE := design quality includes who is affected after launch, not only whether the client request was fulfilled
POWER_AUDIT := name who benefits, who is harmed, who decides, who is excluded, and who has recourse before optimizing persuasive or high-reach systems
RULES_AS_TOOLS := design rules are accumulated risk controls and shared critique language, not fixed law
INTENTIONAL_EXCEPTION := breaking a rule requires naming the expected gain, sacrificed clarity, audience context, and recovery path
AESTHETIC_ACCOUNTABILITY := beauty, delight, and expressive form are valid only when they strengthen meaning, emotion, trust, or usability instead of masking weak intent
BEAUTY_TEST_CAUTION := visual appeal can increase perceived usability and hide defects, so attractive prototypes still need task evidence
ATTRACTIVE_USEFULNESS_TEST := beauty and play can improve confidence, creativity, learning, or attachment only when they do not mask usability, safety, consent, or recovery defects
HUMANITY_CENTERED_SCOPE := broaden high-impact design decisions from individual user success to affected communities, ecosystems, maintenance burden, and long-term repair
MEASUREMENT_HUMILITY := precise metrics are artificial abstractions; pair them with lived experience, qualitative evidence, and named values before optimizing systems
SUSTAINABILITY_AS_SYSTEM := sustainability claims need circular material flow, repairability, resilience, regeneration, business model fit, and owner accountability instead of end-of-life gestures alone
COMMUNITY_AUTHORITY := design with affected people and local maintainers when outcomes shape shared life; outside experts should supply tools, constraints, and evidence rather than extractive control
```

## Cognitive Load

```text
IF a screen contains competing goals THEN split, sequence, or demote secondary work
IF labels require domain knowledge THEN add plain-language label or local explanation
IF the user must remember state across screens THEN preserve context visibly
IF choice_count_is_high THEN group by user intent, not by internal taxonomy
IF the interface asks for attention THEN justify it with user value or safety
IF visual_treatment_is_loud THEN verify it earns attention by priority, risk, or decision value
IF a familiar pattern is altered THEN provide a stronger affordance or explanation
IF secondary_information_competes THEN reduce its contrast, weight, or spacing before increasing the primary element
IF design_iteration_feels_slow THEN reduce choices and solve one decision layer at a time
IF product_direction_is_unclear THEN name the north-star outcome, user story, evidence, and smallest sketch or prototype that can test it
IF users_may_explore_uncertainly THEN provide reversible action, preview, or cancelability before encouraging experimentation
IF a pattern_is_chosen THEN verify user_goal data_shape device_context task_frequency and risk_match
IF a pattern_smells_wrong THEN inspect context, principle fit, accessibility, consent, and long-term trust before iterating visuals
IF a design_system_rule_exists THEN verify it reduces repeated decisions, improves consistency, or lowers maintenance cost
IF a_form_asks_a_question THEN verify comprehension retrieval judgment and response_mapping
IF a_field_has_no_named_use THEN remove it or record the unresolved business reason before design continues
IF a_question_is_sensitive THEN reduce precision explain purpose delay placement or remove it
IF validation_feedback_appears THEN verify it helps repair without interrupting answer formation
IF metrics_show_abandonment_errors_support_load_or_bad_data THEN treat the form as a design problem, not a user problem
IF a_screen_creates_question_marks THEN remove ambiguity before adding explanation
IF users_scan_instead_of_read THEN make trigger words, hierarchy, affordances, and regions carry the first layer of meaning
IF users_satisfice THEN make likely first choices safe, scented, and reversible
IF users_muddle_through THEN preserve recovery, location, and history instead of depending on perfect understanding
IF team_argues_about_usability THEN run a small observed task test and synthesize behavior before continuing preference debate
IF users_must_choose_quickly THEN reduce option count, recommend a safe default, chunk decisions, or defer secondary choices
IF users_must_remember_across_steps THEN keep the needed value visible, copied forward, or selectable instead of relying on working memory
IF users_miss_important_changes THEN inspect goal-filtered attention, expectation, placement, contrast, motion, and local state cues before adding more explanation
IF a_design_debate_is_preference_based THEN observe users before escalating opinion
IF simplicity_is_claimed_by_adding_help THEN inspect whether complexity was removed or merely explained
IF users_are_under_pressure THEN assume learned procedures will fail and simplify the path itself
IF an_expert_customer_requests_power THEN separate expert signal from mainstream default need
IF removing_features_removes_control THEN restore feedback, override, or visible responsibility
IF prioritizing_only_quick_wins THEN check strategic and infrastructure simplicity debt
IF waiting_affects_trust THEN show cause, expected duration or uncertainty, progress, alternatives, and reassurance
IF variable_reward_or_habit_loop_is_designed THEN verify user benefit, consent, exit path, and harm risk before optimizing engagement
IF personalization_shapes_attention THEN expose why content changed, how to correct it, and what data or fairness risk is involved
IF notification_or_alert_demands_attention THEN match signal channel and interruption level to urgency, reversibility, and user context
IF design_claims_universal_principle THEN test audience literacy, accessibility, convention, device, risk, and post_launch ownership before generalizing
IF metrics_hide_harm THEN add qualitative evidence from support, interviews, complaints, abuse reports, or field observation before declaring success
IF known_harmful_problem_remains THEN block release or record the accountable exception, mitigation, owner, and user-facing consequence
IF principle_is_selected THEN map it to the design question it answers: perception, learning, usability, appeal, or decision quality
IF a_psychological_rule_is_cited THEN connect it to local user behavior, design tradeoff, evidence, and failure mode before treating it as authority
```

## Design Operations Principles

```text
DESIGNOPS_TRIGGER := role_specialization OR team_scale OR feedback_chaos OR burnout_risk
DESIGNOPS_PURPOSE := protect_quality_and_making_time_through_process_ownership
DESIGNOPS_OPERATING_SURFACE := design operations owns the tools, infrastructure, workflow, people support, governance, and culture needed for high-quality design work at scale
DESIGNOPS_MODEL_SELECTION := choose operations support, project support, embedded chief-of-staff, or research operations models by team scale, interruption load, craft specialization, and decision bottlenecks
RESEARCHOPS := intake + prioritization + participant_database + engagement_tracking + repository + legal_procurement_security_liaison
RESEARCHOPS_PROGRAM := research operations needs participant management, repository, consent, legal/security review, scheduling, incentives, templates, and synthesis access
MEASUREMENT := choose user_metrics + business_metrics before_after_change
DESIGNOPS_METRICS := measure throughput, focus time, research access, reuse, onboarding, decision latency, burnout risk, stakeholder clarity, and design quality signals
RACI := separate responsible accountable consulted informed before stakeholder_review
FEEDBACK_RIGHTS := separate decision_authority from comment_access
```

## Perception And Gestalt

```text
PROXIMITY := related_things_are_closer_than_unrelated_things
SIMILARITY := same_role_looks_same AND different_role_looks_different
CONTINUITY := scan_path_should_follow_task_order
CLOSURE := partial_visual_groups_are_safe_only_when_completion_is_obvious
FIGURE_GROUND := interactive_or_primary_content_must_separate_from_background
GOAL_FILTERED_PERCEPTION := users notice what supports current goals and expectations; critical changes outside that filter need stronger local cues
GESTALT_REPAIR_CHECK := if users misread relationships, inspect proximity, similarity, continuity, closure, figure-ground, and grouping before adding copy
MEMORY_LOAD_REDUCTION := reduce short-term memory load with visible state, recognition choices, stable labels, carried-forward context, and local reminders
VISUAL_WEIGHT := size + value + saturation + detail + position + density
SYMMETRY := use for stability, ceremony, recognition, and simple comparison when the task benefits from calm order
ASYMMETRY := use for motion, priority, tension, or organic scanning only when optical counterweight and scan path remain legible
ORGANIC_GEOMETRY := use proportion, rhythm, branching, and nested scale to clarify relationships; avoid treating biomorphic shape as automatic warmth
BRANCHING_STRUCTURE := use branching when it clarifies hierarchy, distribution, dependencies, or progressive choice; reject it when it only adds visual ornament
SPIRAL_OR_RADIAL_FLOW := use spiral or radial structure for cycles, growth, return, or central focus only when the scan path and next action remain obvious
PATTERN_SCALE := test repeated visual patterns at component, section, page, and responsive breakpoints because small motifs can become noise at system scale
TESSELLATION_CAUTION := modular repetition must preserve content priority, whitespace, breakpoints, and interaction targets before being approved as a layout system
SHAPE_SEMANTICS := validate symbolic or geometric meanings with audience and culture instead of assuming circles, triangles, spirals, or organic shapes carry universal emotion
PROPORTION_HIDDEN_SYSTEM := hidden ratios and construction systems are useful only when they improve perceived order, not when they override usability or content fit
OPTICAL_CORRECTION := adjust icons, text, and shapes by perceived center and weight when exact geometry looks wrong
ATTENTION_ECONOMY := every added emphasis reduces the clarity of other emphasis
SYSTEMATIC_CHOICE := durable quality comes from constrained reusable choices, not isolated taste decisions
CRITIQUE_LANGUAGE := critique should describe message, audience, hierarchy, form, space, type, image, color, medium, and constraint rather than personal preference alone
CLIENT_BRIEF_CAUTION := a requested artifact may be the wrong solution; diagnose the communication problem before accepting the stated format
PRACTICE_LOOP := study interfaces by identifying decisions you would not have made and rebuilding the pattern
VISUAL_DECISION_PRACTICE := improve craft by naming interface decisions you would not have made and rebuilding them under constraints
UI_LEARNING_ROADMAP := UI learning should move from why and actual UI work, to principles, style guides, design systems, trends, tools, resources, practice, career path, and feedback loop
PRACTICE_RESOURCE_FILTER := learning resources should be selected by current gap, artifact to produce, and feedback path instead of accumulated as passive lists
CONVERSATIONAL_INTERACTION := every interface exchange should make available actions, system response, and next user move understandable
DESIGN_SMELL := repeated friction signal that the selected pattern may be mismatched, over-combined, manipulative, or under-documented
SYSTEM_DEBT := accumulated inconsistency across design assets, code, content, and documentation that slows future work
FORM_CONVERSATION := forms are conversations where each question must earn user effort and return visible value or necessary progress
ANSWERING_WORKLOAD := comprehension, memory retrieval, judgment, and response translation are separate cognitive costs
REPAIRABILITY := humane interaction exposes what went wrong, where it happened, why it matters, and how to fix it
ERROR_EXPECTATION := mistakes are inevitable; design should prevent likely errors, test with representative users, and provide repair before blame
GOODWILL_RESERVOIR := trust is accumulated by clarity, honesty, speed, recovery, and respect, then spent by friction
OBSERVED_USE := actual user behavior outranks stakeholder prediction and participant feature prescriptions
EFFECTIVE_UI_CASE := better UX needs motive, means, opportunity, stakeholder language, and visible product risk before teams will fund or protect it
FEEDBACK_CULTURE := product teams need critique rituals where evidence, user impact, decision owner, and next experiment are clearer than taste defense
ENGAGEMENT_EVIDENCE := engagement claims should connect task value, frequency, confidence, recovery, and business outcome instead of surface activity alone
PROJECT_AUTHORITY := UX work needs a named decision owner with enough authority to preserve user evidence through schedule and stakeholder pressure
NON_UX_ROLE_CONTRACT := managers, writers, designers, developers, testers, and subject experts doing UX work need shared vocabulary, decision rights, evidence standards, handoff expectations, and escalation paths before changing user-facing behavior
USER_JOURNEY_REALITY := users arrive with prior context, competing alternatives, and future intent; evaluate a design by where users came from, what else competes for attention, and what the interface prepares them to do next
NOT_THE_USER_GATE := creator empathy is not evidence; replace self-reference with research, observed behavior, user language, accessibility checks, and task outcomes before approving a decision
RELEASE_FEEDBACK_LOOP := release is a learning event; collect support issues, analytics, observations, and stakeholder feedback before calling the interface done
COLLABORATION_DECISION := design decisions should record who decides, what evidence counts, and how disagreement is resolved
UX_REPAIR_PROGRAM := fixing bad UX requires problem framing, stakeholder alignment, user evidence, analytics, prioritization, solution hypotheses, test plan, and post-change measurement
ETHICAL_USABILITY := usability skill must not be used to hide cost, trick consent, or manipulate desire
COMPLEXITY_CONSERVATION := complexity rarely disappears; good design moves it to the actor, moment, device, or layer best able to handle it
USER_ROLE := users are best at goals, judgment, meaning, estimating, imagining, and deciding when enough is enough
COMPUTER_ROLE := computers are best at storage, retrieval, calculation, monitoring, sorting, filtering, and cross-referencing
CULTURE_OF_SIMPLICITY := metrics, rituals, language, and support processes must reward simplicity or the organization will erode it
CALM_TECHNOLOGY := information may live in the periphery until urgency, risk, or commitment justifies foreground interruption
```

## Six Minds Experience

```text
SIX_MINDS := evaluate experience through vision_attention_automaticity, wayfinding, language, memory_semantics, decision_problem_solving, and emotion
SIX_MINDS_REQUIREMENTS := major product decisions should name how attention, wayfinding, language, memory, decision, and emotion are supported or intentionally left out
EXPERIENCE_IN_MIND := experience is a multidimensional mental activity over time, not a property of one screen
AUTOMATIC_ATTENTION := use fast visual processes only when salience directs users toward their actual need
MENTAL_MODEL_DISCOVERY := discover stored concepts, stereotypes, service expectations, and motor expectations before claiming an interface is intuitive
LANGUAGE_AS_COGNITION := user vocabulary reveals meanings, expertise, trust boundaries, and expected process
LOCALIZED_PSYCHOLOGY_RULE := translated or localized psychology guidance must be rechecked against local wording, examples, cultural expectations, and UI conventions before becoming an implementation rule
PROBLEM_SPACE_DESIGN := define current state, goal state, possible moves, blockers, and subgoals from the user's perspective
EMOTION_AS_LOAD := fear, stress, interruption, and aspiration change working memory and decision quality
APPEAL_ENHANCE_AWAKEN := design should address immediate attraction, medium-term utility, and durable goals or fears when evidence supports all three
EVIDENCE_DRIVEN_EXPERIENCE := every major experience decision should name the cognitive lens and observation that supports it
CONTEXTUAL_INTERVIEW_MICROQUESTIONS := observe task context and capture what users attend to, where they think they are, what words they use, what memories they rely on, what decisions block them, and what emotions change behavior
AI_COGNITIVE_SUPPORT := AI features should augment attention, wayfinding, language, memory, decision, or emotion while preserving agency and correction
VISCERAL_BEHAVIORAL_REFLECTIVE := evaluate immediate impression, use-in-action, and post-use meaning/status/memory separately
EMOTIONAL_LEVEL_FIT := visceral appeal, behavioral pleasure, and reflective identity can conflict; decide which level should lead for the user, moment, culture, and risk
STORY_AS_STRUCTURE := use narrative only when it clarifies user goal, sequence, consequence, or memory
PRODUCT_STORY_EVIDENCE := product stories should connect user motive, business goal, sequence, conflict, resolution, and proof instead of serving as persuasive theater
ETHICS_VISUAL_EVIDENCE := inspect examples, artifacts, screenshots, or public consequences before turning an ethical case into a reusable rule
PHYSICAL_CONTEXT_PHOTO := physical-product and service-design claims need photos or diagrams of body, object, environment, and sequence, not only written affordance labels

IF experience_claim_is_made THEN identify which of the six minds is being supported or harmed
IF users_miss_content THEN inspect attention path before adding more copy
IF users_expect_a_process THEN discover the source schema before changing the flow
IF user_language_differs_from_system_language THEN add synonyms, rename labels, or separate novice and expert modes
IF a_decision_has_unanswered_microquestions THEN place answers at the moment those questions arise
IF users_are_fearful_or_overloaded THEN reduce choices, surface reassurance, preserve control, and avoid pressure
IF a_psychology_rule_is_imported_across_language_or_market THEN compare examples, labels, screenshots, diagrams, and behavioral evidence before treating it as equivalent
IF scarcity_social_proof_or_loss_framing_is_used THEN show factual basis, user benefit, opt-out path, and post-commitment consequence before optimizing conversion
IF AI_feature_is_added THEN state which cognitive process it augments and how users can override or correct it
IF product_decision_is_made THEN connect user_goal, business_goal, risk, evidence, and measurement before committing
IF bad_design_is_found THEN diagnose incentive, process, language, interaction, and governance causes before polishing the symptom
IF ux_repair_is_requested THEN trace root cause through business_rule, content, IA, data, component, incentive, and operating process before visual correction
IF prototype_is_requested THEN name learning_goal, fidelity, audience, task, constraints, and decision_owner first
IF content_claims_value THEN prove it through behavior, comprehension, trust, retention, or support reduction
IF design_team_is_scaled THEN protect focus time, decision rights, research access, and system maintenance before adding more ceremonies
IF a_high_risk_outcome_is_possible THEN map contributing causes, prevention points, recovery paths, and accountable owners before treating the screen as safe
IF shipped_work_can_be_misused THEN design prevention, reporting, monitoring, mitigation, and escalation before launch
IF review_group_lacks_affected_perspectives THEN treat approval as incomplete for ethical, accessibility, safety, or social-impact decisions
IF design_tool_work_is_claimed_as_ux THEN verify it carries research question, user context, test signal, and decision owner, not only polished screens
IF a_sustainability_or_social_impact_claim_is_made THEN map system boundary, actors, incentives, externalities, repair loop, and measurement limits before calling it responsible
IF autonomous_or_agentic_behavior_is_designed THEN provide conceptual model, predictable signals, user override, error recovery, and accountable handoff before increasing autonomy
```

## Source Bands Absorbed

Provenance was kept in the original global design-corpus ledgers. This repo-local copy exposes only reusable cognitive, ethical, operational, and product-design principles and does not import host-specific corpus ledgers.

## Visual Review Backlog

Inspect images when a source example depends on spatial layout, nature-pattern diagrams, symmetry/asymmetry examples, before/after comparison, warning/control placement, icon semantics, physical product affordance, sustainability/system maps, automation display, ethical case evidence, or color-only meaning.
