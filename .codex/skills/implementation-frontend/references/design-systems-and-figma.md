# Design Systems And Figma Reference

Use for tokens, components, variants, documentation, Figma libraries, handoff, and system governance.

## System Structure

```text
TOKENS := color + type + spacing + radius + shadow + motion + z_index
COMPONENT := anatomy + states + variants + usage_rules + accessibility_notes + content_rules
PATTERN := component_combination + user_goal + decision_criteria + anti_patterns
LIBRARY := reusable_assets + naming + publishing + versioning + contribution_path
FOUNDATION_TOKENS := convert repeated visual decisions into color, grid, type, spacing, shadow, and motion tokens
FOUNDATION_PATTERN_ASSETS := treat recurring screen types, navigation models, command surfaces, forms, data views, content rules, and mobile adaptations as reusable pattern assets
FOUNDATION_SYSTEM_PRODUCT := design systems manage scale, debt, shared language, reusable decisions, governance, and delivery quality

PASS IF primitive_tokens_feed_semantic_tokens
PASS IF components expose required states before visual polish
PASS IF variants map to real product needs, not every imaginable knob
FAIL IF a component library has visuals but no usage rules
PASS IF spacing type color radius shadow and opacity choices come from limited scales
PASS IF component_system_preserves pattern_usage_criteria and not only component anatomy
PASS IF design_system_distinguishes pattern_library, component_library, style_guide, code_guide, brand_guide, and content_guide responsibilities
PASS IF system_scope_is_based_on stakeholder_interviews + interface_inventory + code_inventory + product_needs
FAIL IF design_system_is_started_as visual_inventory_without governance, adoption, or maintenance_model
```

## Discovery And Strategy

```text
SYSTEM_PURPOSE := reduce design_debt + code_debt + repeated_decisions + delivery_friction
SYSTEM_AUDIENCE := designers + engineers + product + content + QA + support + leadership + external_consumers
DISCOVERY := stakeholder_interviews + user_research + interface_inventory + code_inventory + support_pain + product_roadmap
PRINCIPLES := memorable decision rules that evaluate tradeoffs, not slogans
ROADMAP := foundations -> components -> patterns -> workflows -> governance -> platform_expansion
METRICS := adoption + reuse + contribution_health + defect_reduction + delivery_speed + accessibility_compliance + satisfaction
```

## Figma Workflow

```text
PAGE_STRUCTURE := cover + foundations + components + patterns + flows + archive
PATTERN_PAGE_STRUCTURE := purpose + context + audience + anatomy + behavior + states + accessibility + content + examples + variants + anti_patterns + implementation + version
AUTO_LAYOUT := use for responsive relationships, not only tidy alignment
COMPONENTS := define slots, constraints, variants, and interaction states
SLOTS := define where icons, labels, media, actions, metadata, validation, and custom content may appear before allowing arbitrary overrides
STYLES := centralize repeated color, text, effects, and grids
HANDOFF := include specs, tokens, states, breakpoints, and content behavior
LAYOUT_GRID := define columns, gutters, margins, and frame scope before arranging repeated screens
FRAME_GRID_SCOPE := page_frames + component_frames + responsive_examples
EFFECT_STYLES := centralize shadows, inner shadows, gradients, and blur only when the effect has a named role
LIMITED_CHOICES := fewer well-chosen options beat many ad hoc values
FOUNDATION_PAGE := principles + tokens + typography + color + spacing + iconography + motion + content + accessibility
COLOR_MANAGEMENT := verify sRGB, browser rendering, exports, unmanaged displays, and wide-gamut differences for color-critical handoff
PROTOTYPE_MAP := inspect actual node maps, frame states, and connection labels before claiming a prototype flow is understandable
FIGJAM_EVIDENCE := moodboards, personas, user flows, and workshop boards count as design evidence only when tied to explicit decisions, assumptions, owners, and next tests
FILE_EVIDENCE_MAP := design files should connect research, personas, journeys, flows, wireframes, prototype states, testing notes, and handoff artifacts instead of scattering them as isolated pages
FIGMA_LEARNING_PIPELINE := Figma practice should connect frames, grids, components, prototype links, responsive constraints, and design rationale rather than isolated tool gestures
FIGMA_MOBILE_PROOF := mobile app design files need frame constraints, component reuse, prototype transitions, device preview, feedback notes, and design-system cleanup before handoff claims
```

## Figma Library And Token Rules

```text
PROMOTE_TO_LIBRARY IF component_or_style_repeats_across_files_or_projects
KEEP_LOCAL IF need_is_one_screen_or_one_file_only
COMPONENT_DESCRIPTION := searchable_aliases + usage_hint + alternative_names
DETACHED_INSTANCE := system_smell_resolved_by_override_path_or_swappable_nested_component
INSTANCE_OVERRIDE_POLICY := allowed overrides, locked properties, swap rules, and missing-variant signals must be documented before instances scale across files
VARIANT_SET := real_product_properties + code_aligned_property_names
TOKEN_NAMES := primitive_what -> semantic_how -> component_where_state
VARIABLE_COLLECTIONS := primitives_separate_from_semantic_tokens
VARIABLE_MODES := use modes for themes, density, platform, or locale only when semantic roles stay stable across modes
LOCAL_VARIABLES := keep file-local variables for temporary exploration until reuse, ownership, and naming are proven
VARIABLE_PROTOTYPE := document variable names, state transitions, conditional rules, reset behavior, and fallback paths before prototype logic becomes handoff evidence
VARIABLE_STATE_TABLE := variable-driven prototypes need state tables, calculation assumptions, reset cases, and invalid-state handling before they become transactional evidence
AUTO_LAYOUT_COMPONENT := text_resizing + padding + child_resize_behavior_verified_with_long_labels
CONSTRAINTS := document responsive behavior and test resize_orientation_cases
LIBRARY_PUBLISH := manual_change_note + consumer_review_before_sync_claim
LIBRARY_PRIVATE_SCOPE := keep one-file components, styles, and experiments local until repeated use, ownership, naming, and consumer value justify publication
BUTTON_COMPONENT := anatomy + size + padding + icon_slot + loading_state + disabled_state + destructive_variant
FORM_COMPONENT := label + help + input + validation + error + success + disabled + required_optional_behavior
CARD_PATTERN := anatomy + content_density + primary_action + secondary_actions + image_or_icon_rules + list_table_alternative
MOTION_TOKEN := duration + easing + purpose + reduced_motion_behavior
SCREEN_PATTERN := overview + focus + make + do + navigation_model + empty_error_loading_states
PATTERN_LIBRARY_OPERATIONS := pattern libraries need ownership, versioning, serving path, content updates, code/design asset sync, and retirement criteria
DESIGN_SYSTEM_STUDY_LOOP := study mature systems by extracting naming, component anatomy, state coverage, token scales, and documentation habits
COMMAND_PATTERN := button_group + action_panel + menu + preview + undo + cancelability + command_history
DATA_PATTERN := table + chart + filter + sort + datatip + spotlight + linked_views + small_multiples
FORM_PATTERN := control_choice + format_tolerance + hints + defaults + validation + error_repair
NOTIFICATION_PATTERN := trigger + priority + container + timing + persistence + dismissal + action
SEARCH_PATTERN := query + autocomplete + autosuggest + filters + feedback + empty_result_repair
ONBOARDING_PATTERN := walkthrough + playthrough + coachmark + progressive_reduction + completion_state
DATA_TABLE_PATTERN := columns + sort + filter + selection + density + empty_loading_error + keyboard + responsive behavior
CALENDAR_PATTERN := date_range + recurrence + timezone + availability + keyboard + mobile behavior
TOOLBAR_PATTERN := grouped_commands + icon_label_rules + disabled_reasons + overflow + shortcuts
DRAWER_PATTERN := purpose + width + dismissal + focus_return + responsive_variant + state_persistence
BADGE_CHIP_AVATAR_PATTERN := scope + status_freshness + fallback + deletion_or_overflow + accessible_name
LOADING_PATTERN := skeleton_spinner_progress_optimistic_retry chosen by wait certainty, layout stability, and user control
SPACING_SCALE := non_linear values with small steps at the small end and larger jumps at the large end
TYPE_SCALE := practical role coverage over mathematically pure modular scales
COLOR_SCALE := greys + primary + accent + semantic ranges with useful edges and middle steps
RADIUS_SCALE := tone-bearing small set, not arbitrary per-component corners
SHADOW_SCALE := elevation and interaction states from consistent light-source logic
OPACITY_SCALE := reusable de-emphasis and overlay values
CONTENT_RULE := voice + terminology + labels + errors + help + empty_states + validation + inclusive_language
ACCESSIBILITY_CONTRACT := keyboard + focus + contrast + screen_reader + motion + target_size + error_recovery
REGION_PATTERN := reusable layout zone with ownership, responsive behavior, and allowed components
FLOW_PATTERN := multi-component sequence with state, validation, error, and recovery rules
```

## Governance

```text
SYSTEM_AS_PRODUCT := define owner_model + adoption_path + contribution_channel + maintenance_responsibility
UI_INVENTORY := inspect production components and visual variants before adding new system objects
IF component_is_one_off THEN keep local until repeated need is proven
IF pattern_has_conflicting_examples THEN document allowed variants and forbidden variants
IF design_system_change_breaks_existing_product THEN provide migration note
IF contribution_path_is_unclear THEN system quality will decay
PATTERN_VERSIONING := change_note + migration_guidance + deprecated_status + owner + consumer_review
ASSET_SERVING := stable_paths + permissions + ownership + update_process
SYSTEM_GROWTH := start from repeated real needs; avoid speculative inventory
ANTI_PATTERN_CAPTURE := record forbidden usage and design smells beside the approved pattern
DESIGN_SYSTEM_AUDIT := before building or expanding a system, inventory product surfaces, repeated components, tokens, ownership, debt, adoption blockers, and implementation constraints
SYSTEM_ADOPTION_PATH := adopt, adapt, or create system assets by product fit, team capacity, code constraints, documentation maturity, and maintenance owner
COMPONENT_DOCUMENTATION_STACK := document purpose, anatomy, variants, states, tokens, usage examples, accessibility, content, and implementation links before scaling a component
SYSTEM_MAINTENANCE_REALITY := design systems are products with roadmap, support, adoption, contribution, migration, and retirement work
GOVERNANCE := propose + triage + design_review + code_review + accessibility_review + release + deprecate + support
CONTRIBUTION_MODEL := contribution_types + acceptance_criteria + owners + review_sla + communication_channel
ADOPTION := onboarding + docs_search + examples + support + release_notes + office_hours + product_team_partnerships
SYSTEM_BACKLOG := gaps + bugs + requests + migrations + experiments + debt + platform_needs
DEPRECATION := announce + replacement + migration_window + compatibility + removal_date
DESIGNOPS_MODEL := define how design work is requested, prioritized, staffed, reviewed, shipped, measured, and archived
TEAM_COORDINATION := separate design production, research operations, content governance, system contribution, and stakeholder decision rights
DESIGNOPS_TOOLING_GOVERNANCE := design tools, repositories, templates, and libraries need ownership, access rules, naming, integration, versioning, onboarding, and offboarding
SYSTEM_MEASUREMENT := track adoption, reuse, defect reduction, delivery speed, accessibility pass rate, support load, and contribution health
CONTENT_GOVERNANCE := define UX copy owners, structured fields, localization, CMS constraints, analytics, AI-review policy, and retirement rules
CONTENT_DESIGN_OPERATIONS := content design needs intake, pattern library, voice chart, review workflow, regulated-content trace, measurement plan, and adoption roadmap
UX_METHOD_REPOSITORY := research findings, personas, journey maps, heuristic reviews, analytics notes, wireframes, prototypes, and decisions need a shared repository with owner and update status
UX_HANDOFF_FOR_NON_DESIGNERS := UX handoff should preserve user goal, context, constraint, rationale, evidence, state matrix, content rules, accessibility, localization, measurement, and implementation owner so non-UX roles can maintain intent
CONTENT_LIFECYCLE_REPOSITORY := UX content should move through research, definition, ideation, prototype, validation, deployment, analytics, iteration, localization, and retirement records instead of living as isolated strings
VISUAL_TO_UI_INVENTORY := create visual inventories for color, type, spacing, and imagery, then UI inventories for components, patterns, states, and usage before defining the library
SYSTEM_FEDERATION_MODEL := design systems scale through a clear contribution model and shared ownership, not through one central team becoming every product team's bottleneck
SYSTEM_SINGLE_SOURCE_OF_TRUTH := design assets, code, documentation, and release notes need one synchronized source of truth with owner, version, and migration path
SYSTEM_FOUNDATION_SEQUENCE := establish principles, metrics, visual language, tokens, components, documentation, adoption, and governance in sequence before expanding to intelligent or multi-platform systems
CODED_UI_SYSTEMATIZATION := developers should convert repeated visual values into shared tokens and components once reuse is observed, not after every screen becomes bespoke
TOOL_SCREENSHOT_CAUTION := tool screenshots are evidence for workflow shape only; rules must survive tool-version changes
FIGMA_VISUAL_PROOF := use screenshots to verify auto-layout behavior, component nesting, prototype wiring, export settings, and handoff affordances, not just menu instructions
COLLABORATION_GOVERNANCE := multiplayer editing, shared libraries, branching, version history, and comments need ownership, naming, review, and rollback conventions
DOCUMENTATION_LINK := put usage documentation where component consumers encounter the component, including examples, constraints, states, accessibility, and owner
PLUGIN_CHECK_LIMIT := plugin output can support contrast, export, content, or cleanup checks but cannot replace human review of accessibility, semantics, interaction, and implementation constraints
```

## Handoff Checks

```text
PASS IF engineer_can_identify token names, spacing rules, responsive behavior, and state coverage
PASS IF accessibility target is named
PASS IF screenshots or prototypes show important transitions and edge cases
PASS IF frames_match_user_flow AND triggers_timing_assets_fonts_tokens_are_explicit
FAIL IF handoff only includes a static happy-path frame
FAIL IF Figma_file_is_treated_as_truth_without_code_state_data_and_platform_contract
PASS IF system_docs_include live_examples OR screenshots_with_state_matrix when interaction cannot be inferred from static anatomy
PASS IF system_release_has changelog + affected_consumers + migration_guidance + rollback_or_compatibility_note
PASS IF handoff_includes token_diff + state_matrix + responsive_examples + content_constraints + accessibility_target
PASS IF visual_frames_are_mapped_to semantic_roles, component_names, variant_properties, and interaction_states
PASS IF raster_exports include density, format, color profile expectation, crop, background, and fallback asset rules
PASS IF handoff includes external assets, content ownership, localization pressure, analytics events, and AI-generated-copy review when relevant
FAIL IF implementation_uses raw_visual_values_without semantic token roles
FAIL IF component_variants_are_created_from every visual permutation instead of real product states
FAIL IF Dev_Mode_or_inspector_values_override user_goal, accessibility, or responsive behavior
PASS IF prototype_handoff includes interaction map, device/browser notes, variable states, transition intent, and known unimplemented behavior
PASS IF handoff_follows_testing_review rather than treating visual completion as development readiness
```

## Source Bands Absorbed

Provenance was kept in the original global design-corpus ledgers. This repo-local copy exposes only reusable design-system decision rules and does not import host-specific corpus ledgers.

## Visual Review Backlog

- Inspect token hierarchy, variable grouping, auto layout resize, component variant, Dev Mode, annotation, export, and handoff screens before adding figure-specific Figma rules.
