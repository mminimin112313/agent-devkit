# SoloPilot Security Skills Design

**Date:** 2026-03-11

## Goal

Add two repo-local security skills to the cloned SoloPilot skillpack so operators can review application changes for security risk and run reproducible local Docker-based security exercises against self-owned sites.

## Approved Constraints

- target the cloned `sources/codex-orchestrator/.codex` tree
- keep the security work limited to self-owned sites running inside a local Docker network
- include runnable scripts, not only prose
- absorb PentAGI execution concepts deeply, but do not re-implement PentAGI's full product runtime inside `.codex`
- keep the new skills compatible with the existing SoloPilot packaging model

## Chosen Structure

Add two top-level skills:

- `security-review`
- `security-lab`

Both skills own their own agents, assets, and references. `security-lab` also owns deterministic shell scripts for bootstrapping a lab, inventorying a target, running checks, collecting evidence, and verifying fixes.

```text
.codex/skills/
├─ security-review/
│  ├─ SKILL.md
│  ├─ agents/
│  ├─ assets/
│  └─ references/
└─ security-lab/
   ├─ SKILL.md
   ├─ agents/
   ├─ assets/
   ├─ references/
   └─ scripts/
```

## Why Two Skills

The work splits into two distinct operating concerns:

- `security-review` is a gate and decision skill. It reviews code, configs, Docker surfaces, and trust boundaries before or alongside remediation.
- `security-lab` is an execution skill. It runs reproducible checks inside a constrained Docker network and turns suspected weaknesses into concrete evidence and regression tests.

Keeping them separate preserves trigger clarity while still allowing a direct handoff from review to lab execution.

## PentAGI Absorption Strategy

PentAGI contributes the execution model, not the product shell.

Absorb:

- flow -> task -> subtask -> action progression
- role-specialized operating lanes
- Docker-isolated tool execution
- evidence-oriented reporting
- iterative retest after remediation

Do not absorb:

- PentAGI web UI
- GraphQL or REST runtime
- persistent databases
- knowledge graph services
- provider integration surface

The resulting skillpack supports the same practical security workflow inside SoloPilot without turning `.codex` into a second product.

## Capability Map

### `security-review`

Primary capabilities:

- name the trust boundary
- inspect authn, authz, validation, encoding, secret handling, logging, and outbound call seams
- inspect file upload, file read/write, template rendering, command execution, URL fetch, and proxy surfaces
- assess Docker-specific surfaces such as published ports, privileged mode, mounted secrets, and unsafe network exposure
- classify issues by exploitability and impact
- hand suspected issues to `security-lab` for repro

### `security-lab`

Primary capabilities:

- bootstrap a bounded Docker lab with attacker and target containers
- inventory endpoints and passive attack surface
- run passive and active web checks using Dockerized tools
- preserve requests, reports, logs, and run metadata under a standard artifact path
- rerun the same checks after a fix
- fail closed when the target is outside the approved Docker network

## Tooling Direction

`security-lab` uses external Docker images as disposable tool runners instead of embedding heavyweight binaries into the repo. The initial scripts are shaped around:

- `ghcr.io/zaproxy/zaproxy:stable` for spidering and baseline scans
- `projectdiscovery/nuclei:latest` for template-driven web findings
- an overrideable `SQLMAP_IMAGE` for optional SQL injection verification
- `curlimages/curl` for health checks and header capture
- `nicolaka/netshoot` as a reusable attacker utility container

These image names remain configurable through environment variables so operators can pin or replace them without editing the scripts.

## Safety Model

- only self-owned local targets are allowed
- targets must resolve on the declared Docker network
- public domains and off-lab addresses are rejected by default
- destructive exploit paths stay off unless explicitly enabled
- all outputs land under `artifacts/security-lab/<run-id>/`

## Output Contracts

### Review Output

- seam reviewed
- trust boundary
- findings with severity
- required repro or verification path
- remediation owner

### Lab Output

- lab metadata
- target inventory
- tool outputs and logs
- exploit attempts and observed results
- post-fix verification summary

## Verification Plan

- validate every shell script with `bash -n`
- verify help and missing-argument behavior for every script
- check the skills catalog still lists the new skills correctly
- confirm artifacts directories and skill-local file structure are created as designed

## Risks And Mitigations

- top-level skill count grows further beyond the preferred compact catalog
  mitigation: keep each new skill broad and execution-oriented rather than adding more narrow siblings
- external Docker images may vary over time
  mitigation: keep every image overrideable through environment variables
- review claims could drift into speculation
  mitigation: require explicit boundaries, exploit paths, or a lab repro handoff before recording a security finding
