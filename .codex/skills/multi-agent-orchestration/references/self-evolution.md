# Self-Evolution

Fix the harness while doing the task when the user's standing or current instructions authorize harness fixes. Then do not collect complaints for later, and do not ask again for fixes inside the scope below. Without that authorization, report the friction and the proposed fix in the final report instead of editing shared files.

## Triggers

| Friction | Fix |
| --- | --- |
| The same mistake happens twice (by you or an agent) | Make a machine catch it: a lint rule, test, script check or hook. Adding a written rule is not enough. |
| The same search or exploration happens twice | Freeze it as a script, a CLI subcommand or a skill step. |
| Skill text contradicts what actually works | Correct the skill now. Stale instructions mislead the next run. |
| A folder has an implicit convention | Add one line to that folder's `AGENTS.md` or `CLAUDE.md`. |
| An agent misread its dispatch | Fix the dispatch template or the role text, not just this agent's prompt. |
| A tool is slow, noisy or hard to call correctly | Wrap or patch it so the correct call is the easy one. |

## Scope

- **Edit directly:** this package, other skills, project scripts, lints, tests and hooks, local instruction files.
- **Edit with a backup:** global or shared files, such as the host's global `AGENTS.md`, `config.toml`, `agents/*.toml`, global hooks, junction-linked or hard-linked shared tools. Before editing, copy the original to the backup directory the user's instructions name, or `<agent-home>/skill-backups/<name>-<YYYYMMDD>-<reason>/`, outside live skill discovery. Check where links point before you write through them. List every such change in the final report.
- **Out of scope:** disabling safety controls, approval gates, or user-owned authorization, and any acceptance gate a skill marks as non-negotiable.

Prefer the smallest change that removes the friction. Improve an existing owner before adding a new file or skill.

## Record

When the user's instructions name a change log, append one JSON line per harness change there (for example `<agent-home>/skills/.evolution/improvements.jsonl`):

```json
{"ts":"<ISO-8601>","skill":"<owner>","symptom":"<what went wrong>","layer":"engine|detector|skill|docs|config","systemic":true,"origin":"self-found","rootCause":"<why>","fix":"<what changed>","test":"<command that proves it>","resolved":true}
```

Save a lesson that should shape future work in the project's memory system when one exists. Verify harness changes in the task's final pass: run the new test or lint and confirm it catches the original failure.
