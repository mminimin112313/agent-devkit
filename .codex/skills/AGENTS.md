# Skills Subtree Instructions

These instructions apply to every file under `.codex/skills/`.

## Purpose

- Keep skills reusable, imperative, and repo-local.
- Treat each skill as a routing asset, not as project memory or a run log.
- Make each skill self-sufficient after `.codex` is copied into another repository.
- Optimize for a small top-level catalog rather than many narrow subskills.

## Authoring Rules

- Keep one operating concern per skill directory.
- Prefer a single-level directory shape: `.codex/skills/<skill-name>/SKILL.md`.
- Keep the catalog discoverable and broad; new top-level skills must earn their slot instead of duplicating an existing concern.
- Keep each `description:` trigger-first so routing can distinguish the skill from adjacent phases quickly.
- Describe the concrete capability and activation conditions in `description:`. Avoid threats, claims of overriding authority, and activation based on faint relevance.
- Put the procedure where an operator can find it quickly. Preserve useful structure; clear prose is allowed, and pseudocode is useful only where it clarifies actual branches or ordering.
- Do not require a shared dependency registry or any cross-skill dependency as a normal prerequisite.
- Name the supporting local `agents/**`, `references/**`, `assets/**`, or `scripts/**` paths that the skill relies on.
- Use only local `agents/`, `references/`, `assets/`, or `scripts/` when they materially improve clarity.
- Select local support files for the current operation and read the selected resources before relying on their contents. Mentioning an optional reference does not require every task to load it.
- Make the output contract or asset record the difference between support files that were declared, actually read, and actually used.
- Keep `Choose Assets` and `Choose References` aligned with live files, current decision types, and freshness expectations rather than copied legacy wording.
- If a skill can dispatch or guide delegated work, make it name the exact local skill or skills the delegate should use.
- If a skill expects reports from delegated work, make the asset or output contract record what local support files were instructed and what was actually used.
- When a repo-local skill has absorbed behavior from a global or imported skill, keep the repo-local owner authoritative and remove duplicate trigger ambiguity where possible.
- Explain where recurring lessons should be promoted:
  - routing or decision rules -> skills
  - execution order or gates -> skills
  - role behavior -> local `agents/*.md`
  - reusable coordination fields or checklists -> local `assets/*.md`
- Keep the language imperative when the reader is expected to follow a sequence. Write ordinary prose as one physical Markdown line per paragraph; do not insert mid-sentence hard wraps.
- Do not turn a skill into a narrative about one past task.

Improve shared skills only when the user has requested that work. Keep source extracts, filled records, and private reading notes outside the publication repository. Preserve required licenses and notices for any redistributed third-party material.

## Scope Discipline

- Edit only files inside `.codex/skills/**`.
- Reference other `.codex` assets by path instead of copying their full contents.
- Preserve concurrent edits in this subtree unless they directly conflict with the owned change.
