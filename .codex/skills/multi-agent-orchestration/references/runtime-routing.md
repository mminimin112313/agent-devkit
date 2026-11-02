# Runtime, Model and Harness Routing

Route each node by what it needs, then pick the runtime and seat that can do it today. Hosts and models change every few months; the routing questions do not.

## 1. Project harness first

A repository that ships its own harness (a CLI entry point, gate checker, brief builder, hooks or a skill bundle) owns the procedure. The orchestrator does not rebuild that procedure in prompts.

```text
IF repo_has(harness_entry := AGENTS.md command list OR CLI "status|go|brief|next" command):
  READ(AGENTS.md OR CLAUDE.md OR GEMINI.md, then the harness skill it names)
  ASK_HARNESS(next_step)            # e.g. `node book.mjs go <book>`; do not infer stage from memory
  NODE.input  := harness-generated brief file (one file the receiver reads)
  NODE.output := the single path the brief names as owned output
  NODE.proof  := the harness check that judges that output, run by the coordinator after return
  NEVER(call harness internals directly, copy harness tools into work folders, or hand-paste a brief the harness can generate)
IF harness_step_is_judgment (design, critique, taste):
  route to a seat that did not produce the artifact being judged
IF harness_gate_is_ceremony (blocks on formatting of a judgment artifact, not on a fact or rule):
  report it as harness friction and fix the gate under self-evolution; do not perform the ceremony twice
```

Harness lanes stay the six in `lane-graph.md`. Harness work is not a seventh lane: a gate, brief template or hook that misfired is a `harness` node; the book, code or document it produces is a `build` node.

## 2. Capability, not model name

Write the need on the node, not a model id.

| Need on the node | Seat that fits |
| --- | --- |
| Long-form prose in the target language, voice-sensitive | The strongest writing seat the user allows; one writer per output file |
| Broad source gathering, fetching, summarising many pages | A fast, cheap seat; many in parallel; outputs are cards or ledgers, never prose for the reader |
| Fact check against named sources | A seat that did not write the claim; it reads the source file, not memory |
| Judgment of design or prose (critique) | A different seat or fresh context from the author; fixed rubric; capped findings |
| Mechanical edits, renames, harness scripts | Any coding seat; deterministic proof required |
| Final integration, acceptance, shutdown | The coordinator itself |

Resolve the seat at dispatch time:

```text
SEAT := FIRST_OF(
  latest explicit user choice for this node type,
  project instruction (AGENTS.md / NOTES / book rules) for this node type,
  runtime default)
CHECK(seat_exists_in_current_runtime)  # list models or agents the runtime exposes; do not assume last month's ids
IF requested seat is missing: STOP and say which seat was requested and what the runtime offers. Do not silently substitute.
```

Do not hard-code model ids, reasoning levels or prices into a shared skill. Put dated observations ("2026-11: seat X writes Korean prose better than seat Y on chapter 3") in the project's own notes, where they can be retired.

## 3. Host runtimes

Every host can run a repo harness through its shell. They differ in how sub-agents, skills and hooks are wired.

| Host | Project instructions | Skill discovery | Sub-agents | Hooks |
| --- | --- | --- | --- | --- |
| Claude Code | `CLAUDE.md` (may import `@AGENTS.md`) | `~/.claude/skills`, `.claude/skills` | Native agent definitions (`.claude/agents/*.md`) and background agents | Yes, `settings.json`; they run only in Claude Code |
| Codex | `AGENTS.md` | `~/.agents/skills` (plus legacy `~/.codex/skills` on some hosts) | Spawned agents per runtime support; else sequential fresh contexts | Runtime-specific; do not assume Claude hooks ran |
| Gemini CLI | `GEMINI.md` (supports `@file` imports) | `~/.gemini/skills`, `~/.agents/skills` alias, workspace `.gemini/skills` | Runtime sub-agents where enabled; else sequential fresh contexts | Do not assume Claude hooks ran |
| OpenCode | `AGENTS.md` | `~/.config/opencode/skills`, also `.claude/skills` and `.agents/skills` | Runtime agents | Do not assume Claude hooks ran |

Rules that follow from the table:

- A role adapter file (for example `.claude/agents/<role>.md`) is a convenience for one host. The contract the role follows lives in a host-neutral file that every host reads.
- When hooks did not run (any host other than the one that owns them), the coordinator runs the checks the hooks would have demanded before claiming done.
- When the host has no sub-agents, keep separation by fresh context: finish the writer node, start a new session or clean context for the critic node, and pass only the brief file.
- Cross-host delegation (one host calling another host's CLI as a worker) is a node with its own seat decision. Use it only when the user or project rules allow that host for that node type.

## 4. When the runtime or models change

```text
ON new_model OR new_host_version:
  KEEP the routing table above (needs, not names)
  RE-CHECK seat_exists for each node type the project names
  RE-RUN one small known node (one chapter brief, one critique) and compare against the last kept output
  RECORD the observation with a date in the project notes; do not edit shared skills for a single model's quirk
  PROMOTE to a shared rule only when the same quirk appears across two models or two projects
```
