# Color Systems Reference

Use for color roles, palette construction, contrast, semantic states, brand mood, and color accessibility.

## Palette Construction

```text
START_WITH(context := brand_mood + product_domain + content_type + accessibility_need)
BRIEF_COLOR := start palette decisions from brief, audience, brand constraints, technical limits, and desired user action
DEFINE(color_roles := background, surface, text, muted_text, border, primary, accent, success, warning, danger, focus)
ASSIGN(semantic_role) BEFORE choosing decorative variation
CHECK(contrast) BEFORE polishing hue relationships
BRAND_ROLES := main_brand + secondary_brand + neutral_support BEFORE additional_accents
COLOR_SOURCE := translate real_world_or_nature_inspiration into semantic_UI_roles before use
HSL_WORKFLOW := prefer hue_saturation_lightness style adjustment when building UI palettes because it maps better to human decisions than hex-only editing
SHADE_SYSTEM := define useful lightest darkest and middle steps before applying colors screen-by-screen
PALETTE_PROPORTION := define dominant, support, accent, and neutral surface_area before judging palette quality
IMAGE_PALETTE := derive UI colors from image dominance, support, accent, crop, and caption/overlay needs only after readability survives alternate crops
LOCAL_MEANING := treat cultural, seasonal, gendered, national, food, luxury, urban, and nature color meanings as hypotheses requiring audience context
PALETTE_REPAIR := compare before_after examples by changed_role, changed_area, changed_contrast, and changed_image_relationship instead of naming the new hue only
HUE_VALUE_CHROMA := separate hue, value, and chroma before critiquing or repairing a palette
COLOR_ATTRIBUTES := describe ambiguous colors by hue_family + value_range + chroma_level + temperature_relation instead of a color name alone
COLOR_LANGUAGE := establish shared color vocabulary with clients and engineers before approving subjective color direction
COLOR_NAME_TRANSLATION := translate named colors into hue_family, value, chroma, temperature, medium, and UI role before using them in a system
COLOR_CONTEXT_ROLE := decide whether a color is carrying context, identity, information, safety, motion, tradition, subject matter, or foundation before tuning hue
LIMITED_PALETTE := use fewer colors when learning, auditing, or repairing a palette so value, hue, saturation, and temperature relationships become visible
GAMUT_MASK := constrain experimental palettes with a deliberate hue/value/chroma range before judging whether they are coherent
PALETTE_RATIO := define flexible dominant, secondary, and accent proportions; ratio formulas are starting points, not approval rules
COLOR_AS_VISUAL_LANGUAGE := color should support message, hierarchy, image, typography, material, and medium as one system rather than a detached palette
COLOR_INTERPRETATION_CONTEXT := color meaning changes across philosophy, art, architecture, literature, music, psychology, material, and product context; translate meanings through audience and medium evidence before using them as UI rules

IF palette_feels_flat THEN vary value, chroma, and temperature before adding more hues
IF palette_feels_noisy THEN reduce accent count and strengthen neutral structure
IF brand_color_is_low_contrast THEN reserve it for large surfaces or accents, not small text
IF color_encodes_state THEN add shape, label, icon, or position as a second cue
IF brand_color_is_used_everywhere THEN demote it to moments_of_recognition_or_priority
IF named_color_suggests_emotion THEN verify audience_domain_evidence before assigning product meaning
IF named_color_is_approved THEN record its actual role, range, contrast behavior, and reproduction medium instead of relying on the name as a token contract
IF two_colors_share_hue THEN compare value and chroma before calling the relationship calm, loud, muddy, or accessible
IF color_preference_is_client_or_team_subjective THEN translate debate into role, audience, evidence, medium, and system constraints
IF palette_model_is_used THEN treat it as an exploration scaffold and still verify role, legibility, context, and audience fit
IF color_reference_comes_from_art_or_material_culture THEN inspect the image, surface, adjacency, medium, and historical context before turning it into product semantics
```

## Harmony And Contrast

```text
VALUE_CONTRAST := primary readability control
CHROMA_CONTRAST := emphasis and energy control
TEMPERATURE_CONTRAST := depth, mood, and figure-ground control
COMPLEMENTARY_CONTRAST := use sparingly for focal impact
ANALOGOUS_HARMONY := use for calm unity, then add value contrast for usability
NEUTRAL_SYSTEM := use warm/cool neutral decisions deliberately; gray is not automatically neutral in context
VALUE_FIRST := check value structure in grayscale before spending effort on hue nuance
CHROMA_REPAIR := lower saturation deliberately and verify the resulting value and hue shift
NEUTRALIZATION := record whether chroma was lowered by grey, complement, lower-chroma neighbor, opacity, or lighting because each method changes the result differently
SATURATED_COLOR := reserve for focus, action, alert, or brand recognition
EMOTIONAL_COLOR := pair with audience, domain, and surrounding neutrals; do not rely on generic color psychology
PSYCHOLOGICAL_TRIGGER := treat generic color-emotion associations as prompts for research, not as product evidence
PERCEIVED_BRIGHTNESS := adjust by hue perception, not numeric lightness alone
HUE_ROTATION := rotate hue when changing brightness or accessible contrast would otherwise make a color feel muddy
GREY_TEMPERATURE := warm_or_cool_greys should support the product mood and nearby primary color
ADJACENCY_EFFECT := compare colors in their real neighboring surfaces because proportion and edge contrast can change perceived hue, intensity, and warmth
ADAPTATION_CHECK := review long-lived or brand-critical colors after eye adaptation, not only in an isolated picker
AFTERIMAGE_RISK := avoid high-chroma fixation patterns in sustained workflows because adaptation can change perceived complements and fatigue
CONTRAST_COLOR := evaluate contrast as a perceptual response to surround and adaptation, not only as a pairwise numeric difference
WARM_COOL_DEPTH := use temperature contrast for spatial depth only after value and readability still hold
BOUNCE_LIGHT := account for nearby colored surfaces tinting shadows, illustrations, immersive scenes, and image-derived palettes
ATMOSPHERIC_DEPTH := represent distance with lower contrast, lower saturation, and background-color drift when imagery or spatial UI needs depth
```

## Product Color QA

```text
PASS IF text/background contrast meets the product's accessibility target
PASS IF dark_mode adjusts surfaces, elevation, and semantic states rather than only inverting colors
PASS IF charts or status chips remain distinguishable without hue perception
PASS IF disabled states look unavailable without becoming illegible
FAIL IF the UI relies on color names or emotional stereotypes without audience/context evidence
FAIL IF validation, payment trust, risk, or completion status is conveyed through hue alone
PASS IF colored_surfaces_keep_readable_text_by flipping_contrast_or_adjusting_hue_saturation_lightness
PASS IF state_color_has secondary cue such as label icon shape position or copy
PASS IF photo_overlay_text remains readable across expected crops, brightness shifts, and subject positions
PASS IF localized_color_meaning is recorded as evidence_or_risk rather than assumed universal emotion
PASS IF safety_or_medical_color improves identification, hierarchy, and error prevention with a non-color cue
PASS IF brand_palette documents where color must stay consistent and where flexible variation is allowed
PASS IF color_data_visualization encodes order, category, uncertainty, and density with value, pattern, label, and layout support
FAIL IF brand, news, event, city, or wayfinding color is approved from isolated swatches without system examples
PASS IF palette_choice_can_be_explained_by function, legibility, guidance, distraction_control, brand_fit, and brief_fit
PASS IF complex_illustration_or_scene keeps strongest contrast and color energy at the intended focus
```

## Visual Inspection Rules

```text
READABILITY := judge foreground + background + value + chroma together
TONE_GRID := inspect hue families across light, middle, dark, vivid, muted, and grayish tones before naming a palette
PALETTE_VARIATION := compare candidate palettes as systems, not isolated swatches
PALETTE_SEQUENCE := compare approved and rejected variants in realistic screen sequences before naming a palette final
RELATIVITY := check adjacent colors because perceived hue and intensity shift by context
MIXING_MODEL := distinguish additive_light, subtractive_pigment, and screen_UI_color before applying a rule
MEDIUM_MIXING_MODEL := never transfer a color rule across screen, print, paint, photography, and physical material without naming the medium and conversion risk
LIGHT_CONTEXT := evaluate color under the relevant light source, direction, intensity, surrounding surface, and display or material condition when appearance matters
ILLUMINANT_SPEC := name light source or standard illuminant before making color measurement, matching, or reproduction claims
COLOR_MEASUREMENT := separate human perception, device measurement, colorant mixture, and color-management transform
SWATCH_BOARD_LIMIT := swatches prove vocabulary and range only; product acceptance requires role, surface, content, and state examples
DESIGN_GALLERY_EVIDENCE := use galleries as comparative evidence for proportion, adjacency, image relation, and audience mood, not as copyable style
DICTIONARY_SWATCH_PROOF := palette dictionary spreads require visual inspection of swatch proportion, adjacency, neutral support, and applied examples before a durable palette rule is accepted
CONTROL_VARIABLES := reduce form, texture, size, layout, and content variation before judging a color relationship
GROUND_TEST := test color samples on multiple grounds because parent/background color can change the apparent result
REPETITION_TEST := inspect palette behavior at unit, repeated field, interrupted field, and sequence scales
TRANSPARENCY_MODEL := distinguish digital alpha, optical transparency, projected light, and pigment overlap before reusing an effect
COLOR_SYMBOL_TRANSFER := fail color-symbol claims that move from one medium or culture to another without naming what changed in surface, light, scale, audience, and use

IF text_sits_on_colored_background THEN test black, white, semantic, and accent text variants
IF two_palettes_share_a_hue THEN compare value/chroma distribution before calling them equivalent
IF color_is_brand_or_mood THEN inspect real examples, material, imagery, and surrounding neutrals
IF UI_action_uses_semantic_color THEN visual_weight_must_match_action_priority
IF background_color_changes THEN retest text, image, white_space, and accent hierarchy because the entire page mood shifts
IF palette_is_based_on_real_scene_or_photo THEN sample local_color, lit_color, shadow_color, and neighboring_color separately before deriving tokens
IF color_system_has_many_named_values THEN test whether users and makers can remember, choose, and reproduce them consistently
IF color_moves_or_animates THEN verify motion, transition, afterimage, and attention cost, not just static frame harmony
IF color_is_used_across_steps THEN review rhythm, transition, and attention reset across the full sequence
IF colored_type_is_used THEN test form, counterform, texture, rhythm, and readability, not just hue preference
```

## Advanced Color Controls

```text
COLOR_SPEC := include viewing_condition + background + medium WHEN color_match_or_brand_identity_matters
APPEARANCE_SPEC := include illuminant, observer, adaptation, background, medium, and tolerance when exact color appearance matters
METAMERISM := compare critical colors under relevant light sources or displays before claiming a match
COLORIMETRY_DIAGRAM := do not translate gamut, spectral, or chromaticity diagrams into UI color choices unless axes, observer model, illuminant, and medium are understood
COLOR_SPACE := choose_by_output(RGB_screen, CMYK_or_spot_print, LAB_or_ICC_translation)
TRICHROMATIC_LIMIT := remember that RGB-like channels are a model of capture or display, not a guarantee of equal human appearance
UNIFORM_COLOR_SPACE := use LAB/LUV-like spaces for approximate perceptual distance, while recording their limits and viewing assumptions
COLOR_CONSTANCY := test whether a color role still reads correctly when background, illuminant, surface, or surrounding variance changes
SURFACE_COLOR := distinguish emitted screen color from perceived object or surface color when translating physical-world references
BRAND_COLOR := record exact_match_path beyond hex WHEN reproduction_risk_is_high
INFO_COLOR := classify_or_measure_before_decorating
QUANT_STEPS := use value_or_pattern_before hue_only_steps
CONTRAST := check hue + value + saturation + warm_cool + proportion independently
SATURATION := reserve high_chroma for focus_or_alerts, not long_reading
ACCESSIBILITY := test state colors through color_vision_deficiency and aging_lens assumptions
PALETTE_MEMORY := keep navigation_or_wayfinding palettes small enough to remain mnemonic
PALETTE_SCALE := define greys, primary, accents, and semantic colors as reusable ranges, not isolated swatches
SATURATION_LIGHTNESS := preserve useful saturation when making colors lighter, especially for UI tints and colored backgrounds
DUOTONE_SPOT := preserve tonal separation, face/object readability, and print/display reproduction before judging the second color's mood
FIGMA_COLOR_EXPORT := verify browser, export, unmanaged display, and wide_gamut differences when color-critical assets move through Figma or code
CMYK_SAMPLE := treat numeric print mixes as reproduction evidence for a medium, not as direct screen token values
CALIBRATION_PATH := document the device, profile, display condition, print stock, or measuring instrument when color fidelity matters
SPECIALTY_COLOR := fluorescent, metallic, spot, and material-dependent colors need medium-specific samples or production proof before being treated as ordinary screen colors
```

## Source Bands Absorbed

Provenance was kept in the original global design-corpus ledgers. This repo-local copy exposes only reusable color decision rules and does not import host-specific corpus ledgers.

## Visual Pages Inspected

Visual evidence is intentionally kept in `docs/visual-review/` manifests and contact sheets. Use those artifacts before making figure-specific palette, colorimetry, or contrast claims.

## Remaining Visual Review Backlog

Inspect source pages or screenshots when evaluating swatches, palette examples, simultaneous contrast, color illusions, before/after redesigns, CIE/LAB/gamut diagrams, information color maps, dictionary palette spreads, duotone and spot-print examples, photo-with-type layouts, palette experiment sequences, and wayfinding color-coded signage.

## Excluded Color Source Notes

- Painting-only pigment behavior, drying, opacity, glazing, and underpainting advice remains excluded unless generalized into screen or product color verification.
- Tool-version-specific print or image-editing steps are excluded unless the durable rule is color separation, tonal readability, or reproduction risk.
