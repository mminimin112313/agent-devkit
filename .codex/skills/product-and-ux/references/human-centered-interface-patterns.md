# Human-Centered Interface Patterns

Design the interface around human goals, memory, and interruption behavior before discussing surface polish.

```text
PASS IF user_goal_memory_and_interruption_model_are_named_before_surface_decisions
FAIL IF decorative_direction_arrives_before_behavioral_constraints
```

## Start Here

- name the user's real goal, not just the screen action
- identify audience skill range and domain confidence
- ask why the task exists before deciding how the screen should look
- match content depth and functionality to that audience instead of shipping one generic surface
- decide whether the seam should behave more like guided instruction, rapid expert tooling, or a mixed-mode experience
- treat the interaction as a conversation so the next question, current state, and likely consequence stay legible

## Research Inputs

Use the lightest evidence that can still answer the question:

- direct observation when environment and workarounds matter
- case studies when you need richer workflow examples
- surveys when preference or segmentation matters
- personas only after real evidence exists

Do not substitute marketing segmentation for interface research. Product desire and interface behavior are related but not the same.

## Behavioral Pattern Lenses

Apply these lenses when choosing patterns:

- safe exploration: provide low-risk trial, preview, undo, or escape routes when mistakes are costly
- instant gratification: show useful feedback or value early
- satisficing: make the likely good-enough choice obvious instead of forcing exhaustive comparison
- changes in midstream: support edits, reversals, and route changes without punishment
- deferred choices: let users continue when a decision can safely wait
- incremental construction: preserve work while the user builds a complex outcome step by step
- habituation: keep repeated actions stable so practiced users can operate quickly
- microbreaks: assume attention can break at any moment
- spatial memory: keep stable placement for important objects, actions, and signposts
- prospective memory: help users remember what they intended to do later
- streamlined repetition: shorten loops for repeated work
- keyboard only: preserve a full path without requiring pointer use
- social proof and collaboration: show other people, shared state, or team signals only when they reduce uncertainty

## Skill-Mix Rules

- for novice and expert users in the same seam, combine progressive disclosure with visible shortcuts instead of forcing one interaction mode on everyone
- when interruptions are common, prefer save-draft, stable breadcrumbs, recent items, and resumable progress over long fragile flows
- when the task is repetitive, keep object placement, labels, and action order stable enough for habit to form
- when users compare options quickly, prefer recognition aids such as previews, thumbnails, and smart defaults over recall-heavy configuration
- when users need reassurance before committing, show previews, examples, or reversible next steps before destructive state changes

## Avoid

- demanding setup choices that the user cannot yet evaluate
- changing the position or label of common actions between related screens without a strong reason
- treating collaboration indicators as decoration when they could reduce duplicate work or uncertainty
- requiring pointer-only interaction on seams that are repetitive, assistive-tech dependent, or interruption-prone

## Experience Modes

Check which mode dominates before picking patterns:

- first-use and unfamiliar
- intermittent and rusty
- expert and high-frequency
- collaborative and shared-state
- interrupted and resumable

The same surface rarely serves all five modes equally well. Call out the primary mode and the tolerated compromise.

## Guardrails

- do not force irreversible commitment when safe exploration would still support the goal
- do not make users remember previous choices, hidden state, or off-screen context unless the task truly requires expertise
- do not optimize only for expert throughput when the product still depends on discoverability
- do not add social proof, presence, or collaboration markers when they mainly create pressure or noise
- do not rely on hover, timing, or pointer precision when keyboard-only or touch use is plausible

## Design Prompts

- what is the smallest thing the interface can do to prove progress quickly
- where can the user safely back out, preview, or recover
- which decisions should be deferred instead of forced now
- which elements must stay spatially stable for recognition and habit
- what interruptions or context switches are normal for this workflow
- where should the interface remember for the user instead of making them remember
- which parts of the flow should stay stable to support habit and muscle memory
- where the interface should help the user resume after interruption
- what expert shortcut is justified only after the novice path is already legible

## Output

Record at least:

- user goal and skill range
- evidence path and its weakness
- behavioral lenses that matter most
- interruption and recovery expectations
- memory aids or repetition shortcuts required
- collaboration or keyboard-only constraints
- dominant experience mode
