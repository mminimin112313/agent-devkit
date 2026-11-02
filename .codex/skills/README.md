# Skills

This exported SoloPilot pack keeps a small, standalone skill catalog under `.codex/skills/<skill-name>/`.

## Discovery Model

- keep the top-level catalog broad and curated rather than splintered into narrow duplicates
- keep every skill independently understandable
- keep each skill description trigger-first so nearby phases are easy to distinguish
- keep support material inside the same skill directory when it materially helps
- keep role prompts, reusable assets, and long-form references inside the owning skill package
- do not depend on removed root prompt or template directories
- when delegated work is involved, dispatch with explicit repo-local skills and support paths rather than generic role guesses
- compile useful `superpowers` behavior into existing repo-local skills first
- compile useful `cc-thinking-skills` behavior into existing repo-local skills first
- do not present imported `superpowers` as a second public catalog
- do not present imported `thinking-*` skills as a second public catalog
- keep skills portable across environments; shared behavior must not depend on top-level mailboxes, launch agents, or machine-local daemons
- keep a `ROOT-CAUSE-SOLUTION-HOOK` in every top-level skill so fallbacks, bypasses, temporary patches, and workaround-first fixes require explicit user approval and a root-cause plan
- branch exit, isolated workspace setup, and release completion stay inside repo-local planning or release owners

## Entry Order

1. Start with `intake-and-routing` when the request is new or ambiguous.
2. Move to `product-and-ux` when the request implies creative work, new behavior, flow shaping, messaging, or design direction even if the scope looks small.
3. Design and UX knowledge lives inside its owners: `product-and-ux` for discovery, flows, UX writing, critique, and restraint; `implementation-frontend` for layout, color, tokens, components, accessibility, motion, and rendered proof.
4. Move to `planning-and-scoping` only after the direction has been presented and approved.
5. Use `architecture-and-design` when seams, contracts, or trade-offs are still open.
6. Use `implementation-*` only after planning is execution-ready, with failing tests first and exact proof paths.
7. Use `security-review` when code, config, auth, Docker, dependency, secret, or request-boundary work crosses a trust boundary.
8. Use `security-lab` only when `security-review` classifies a self-owned Docker target issue as repro-required or regression-required.
9. Use `quality-and-review` for ordered review, fresh verification before completion claims, debugging discipline, review request/response handling, and acceptance gating.
10. Use `release-and-operations` for ship, hold, rollback, incident follow-up, and branch exit decisions after fresh verification.
11. Use `multi-agent-orchestration` only when decomposition clearly improves delivery and slices can carry fresh isolated context.
13. Use `skillsmith` when the task is to create or revise the skill system itself.
14. Use `starting_pac` when a new repository starts from a plan or PRD and needs a durable `AGENTS.md`, `MEMORY.md`, `.codex`, continuation skill, work-log, and validation contract before implementation begins.

## Catalog

| Skill | Primary Job | Typical Roles | Typical Phases |
| --- | --- | --- | --- |
| `intake-and-routing` | restate a new request and choose the single best next skill | CTO, PM, lead | intake, triage |
| `planning-and-scoping` | turn an approved direction into owned seams, non-goals, and proof | CTO, lead, implementer | planning, scoping |
| `architecture-and-design` | decide seams, contracts, and design trade-offs before implementation | CTO, lead, platform | architecture, design |
| `implementation-frontend` | implement an approved UI seam with explicit state and accessibility proof | frontend, design-minded engineer | implementation, verification |
| `implementation-backend` | implement a chosen backend seam with contract-safe verification | backend, platform engineer | implementation, verification |
| `product-and-ux` | turn evidence into product direction, UX trade-offs, and flow decisions | PM, UX, UI | discovery, design |
| `quality-and-review` | require fresh proof, ordered review, and acceptance before completion claims | reviewer, QA, lead | testing, review, acceptance |
| `security-review` | review trust-boundary changes and classify findings or lab follow-up | security reviewer, lead, implementer | review, remediation planning |
| `security-lab` | reproduce and regress security issues against self-owned Docker lab targets | attacker, defender, reporter | repro, verification, regression |
| `release-and-operations` | choose ship, hold, mitigate, rollback, or incident follow-up | release, DevOps, QA | release, operations |
| `multi-agent-orchestration` | dispatch disjoint slices with explicit skills, support paths, and convergence | CTO, lead | orchestration, integration |
| `skillsmith` | compile or revise repo-local skills with explicit triggers and support files | CTO, skill author | skill design, packaging |
| `starting_pac` | bootstrap a new repository's agent operating layer from a plan or PRD | CTO, project shepherd | project start, setup |

## Packaging Rules

- required: `SKILL.md`
- recommended: `agents/openai.yaml`
- recommended when the skill owns execution roles: `agents/*.md`
- recommended when the skill owns repeatable records: `assets/*.md`
- optional: `references/`, `scripts/`
- avoid local scripts unless a repeated workflow is deterministic enough to justify them AND portable enough to run in common repo environments
- when a skill owns a deterministic CLI workflow, keep the authoritative scripts inside that skill package

## Design Standard

High-quality SoloPilot skills should:

- have trigger-focused frontmatter
- describe the activation boundary in `description:` rather than a generic capability label
- own one broad but sharp operating concern
- stay procedural and concise
- make single-agent execution viable by default
- describe optional multi-agent use explicitly rather than implicitly
- name the supporting local roles and assets they can lean on
- keep asset and reference selection rules current with the live package contents
- refresh stale templates, records, and evidence-oriented references when the decision type or source inputs changed
- make delegated-work reporting traceable when a skill can dispatch or guide slices
- return a concrete output contract
- include the shared `ROOT-CAUSE-SOLUTION-HOOK` near the top of `SKILL.md`

## Promotion Rules

- routing or decision rules -> skills
- role behavior -> local `agents/*.md`
- reusable forms or checklists -> local `assets/*.md`
- one-off project notes -> outside the exported skillpack
- add a new top-level skill only when existing repo-local owners would lose trigger clarity or output-contract force
- domain references belong in the `references/` of the skill that applies them; do not reintroduce nested knowledge routers

## Convergence Status

- current absorbed `superpowers` convergence status: no remaining source currently requires a new top-level repo-local skill
- current absorbed `cc-thinking-skills` convergence status: no source behavior currently requires a new top-level repo-local `thinking-*` skill
- current absorbed `cc-thinking-skills` convergence status:
  - model routing, model selection, model combination, Cynefin, Socratic clarification, and competence-boundary behavior absorbed into `intake-and-routing`
  - Jobs-to-Be-Done, effectuation, and product opportunity-cost behavior absorbed into `product-and-ux`
  - pre-mortem, reversibility, opportunity cost, margin of safety, bounded rationality, Fermi estimation, and inversion behavior absorbed into `planning-and-scoping`
  - first principles, second-order, systems, feedback loops, archetypes, leverage points, Lindy, theory of constraints, thought experiments, TRIZ, and via negativa behavior absorbed into `architecture-and-design`
  - map-territory, hypothesis-differential debugging, Five Whys Plus, Kepner-Tregoe, Occam, base-rate and probabilistic evidence checks, debiasing, dual-process verification, and steel-manning behavior absorbed into `quality-and-review`
  - red-team behavior remains owned by `security-review` / `security-lab`
  - OODA behavior remains owned by `release-and-operations`
  - regret-minimization personal life/career behavior is excluded as a catalog non-fit
- current absorbed design knowledge status: `knowledge` was removed on 2026-11-02; UX, interaction, pattern, and principle references moved to `product-and-ux`, and color, composition, and design-system references moved to `implementation-frontend`; physical wayfinding and `effective-html` were dropped as out of scope; book absorption remains owned by `skillsmith`
- current absorbed `superpowers` convergence status:
  - intake and skill-routing behavior absorbed into `intake-and-routing`
  - brainstorming behavior distributed across `intake-and-routing`, `product-and-ux`, and `planning-and-scoping`
  - writing-plans behavior absorbed into `planning-and-scoping`
  - test-driven-development behavior absorbed into `implementation-backend` and `implementation-frontend`
  - verification-before-completion, requesting-code-review, receiving-code-review, and systematic-debugging behavior absorbed into `quality-and-review`
  - subagent-driven-development and dispatching-parallel-agents behavior absorbed into `multi-agent-orchestration`
  - using-git-worktrees and executing-plans behavior absorbed into `planning-and-scoping`
  - finishing-a-development-branch behavior absorbed into `release-and-operations`
- current imported `anthropics-skills` convergence status: no remaining source currently requires a new top-level repo-local skill
- current imported `anthropics-skills` disposition:
  - absorbed: `mcp-builder`
  - generalized-only: `skill-creator`, `frontend-design`, `webapp-testing`
  - rejected: `algorithmic-art`, `brand-guidelines`, `canvas-design`, `claude-api`, `doc-coauthoring`, `docx`, `internal-comms`, `pdf`, `pptx`, `slack-gif-creator`, `theme-factory`, `web-artifacts-builder`, `xlsx`
- reopen the admission gate only if a new source behavior cannot be compiled into an existing repo-local owner without weakening trigger clarity or output-contract force
