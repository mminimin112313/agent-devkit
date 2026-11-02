# Agent Config Instructions

This directory owns role-specific Codex config layers referenced by `.codex/config.toml`.

## Scope

- Applies to `.codex/agents/**`.
- These files tune runtime behavior for spawned sub-agents.
- Keep them narrow, role-specific, and reusable.

## Rules

- Do not define product logic here.
- Do not duplicate cross-skill routing, template schema, or long procedural checklists here.
- Put spawn-runtime behavior here: sandbox, model settings, and concise developer instructions.
- Each role config MUST declare role identity explicitly enough that a spawned agent can say `Codex, acting as <repo role>` without guessing.
- Each role config and skill-local agent prompt MUST front-load the structurally important contract: identity, owned lane, first handoff line, must-do behavior, must-not-do behavior, and escalation rule must appear before supporting rationale or examples.
- Each role config MUST remind the receiver that it is operating as a spawned sub-agent, not the primary orchestrator.
- Each role config MUST require the first substantive handoff line to name the active repo role.
- Each role config MUST include the exact opening-line template plus a stop-and-correct instruction if the reply starts with the wrong role line.
- Agent registry descriptions in `.codex/config.toml` MUST describe the spawn job, owned lane, and handoff style rather than generic capability labels.
- Each role config MUST state the lane it owns and tell the agent to escalate instead of absorbing another role's authority.
- If a role prompt can be mistaken for the orchestrator, CTO, or a generic assistant, the config is incomplete.
- If a role config changes how shared `.codex` edits happen, sync `.codex/config.toml` and any affected prompts or skills.
