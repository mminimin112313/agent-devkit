---
name: security-lab
description: "Use when a self-owned site must be reproduced or regression-tested for security issues inside a local Docker-only attacker and target lab."
---

# Security Lab

## Procedure

```text
STEP_0 := DECLARE(support_files := exact assets/ + references/ set OR none)
STEP_0A := READ(required_assets_and_references_before_lab_execution)
STEP_0B := RECORD(why_each_declared_file_was_loaded)
STEP_1 := READ(references/docker-lab-safety.md)
IF target_is_not_self_owned OR target_is_outside_declared_docker_network THEN STOP("security-lab is Docker-only and self-owned only")

STEP_2 := bootstrap_lab USING scripts/bootstrap-lab.sh
STEP_3 := inventory_target USING scripts/inventory-target.sh
STEP_4 := run_web_checks USING scripts/run-web-checks.sh
STEP_5 := collect_evidence USING scripts/collect-evidence.sh

IF remediation_has_been_applied THEN
  STEP_6 := verify_fix USING scripts/verify-fix.sh
  ROUTE -> assets/verification-record.md
ELSE
  ROUTE -> assets/exploit-attempt.md
```

## Overview

Run the attack in a box you own.

**Core principle:** if the target is not your site on the approved Docker network, stop.

<PORTABILITY-MANDATE>
Behave like a conservative repo-local coding agent. Do not guess hidden state, host-only tools, or machine-local services. Prefer portable repo-local files and explicit evidence over unstated environment assumptions. If the path would vary by host, shell, or operating system, choose the narrower portable path or stop and name the missing fact.
</PORTABILITY-MANDATE>


<ROOT-CAUSE-SOLUTION-HOOK>
IF problem_solving_requires(fallback OR workaround OR bypass OR temporary_patch) THEN
  ASK_USER_APPROVAL(reason, scope, risk, rollback_plan) BEFORE applying_non_root_solution
  RECORD(root_cause_status := confirmed OR hypothesis_only OR blocked)
  PREFER(root_cause_fix) OVER(symptom_workaround)
  STOP("fallback or workaround requires explicit user approval and a root-cause plan") IF approval_is_missing
</ROOT-CAUSE-SOLUTION-HOOK>

<HARD-GATE>
`security-lab` is only for self-owned targets running inside a local Docker network. Reject public domains, production hosts, and anything outside the declared lab network.
</HARD-GATE>

<NON-NEGOTIABLE>
Every run must declare its exact local `assets/` and `references/` set before execution, read the required files before touching the lab, and record why each declared file was loaded. Unnamed support files are out of contract and must not be relied on. If no support files are needed, say `none` explicitly. Final outputs must report the declared set, the files actually read, and the files actually used.
</NON-NEGOTIABLE>

<NON-NEGOTIABLE>
Evidence beats narration. Every run must leave artifacts, logs, and a verification record under a standard run directory.
</NON-NEGOTIABLE>

## Required Reads

```text
MUST START -> assets/lab-run-record.md BEFORE bootstrap
IF weakness_class_and_endpoint_are_concrete THEN START -> assets/exploit-attempt.md
IF rerunning_after_fix THEN START -> assets/verification-record.md

MUST READ -> references/docker-lab-safety.md BEFORE touching_the_target
MUST READ -> references/attack-flow.md BEFORE choosing_execution_order
IF escalating_a_lead_to_a_confirmed_finding THEN MUST READ -> references/finding-validation-rules.md
```

## When to Use

- reproducing a suspected weakness from `security-review`
- building a Docker-only attacker vs target lab for a self-owned site
- collecting endpoint inventory and passive findings before a fix
- rerunning the same checks after remediation
- generating reproducible evidence for a local security defect

Trigger this skill immediately when:

- a `security-review` handoff says `repro required`
- you need proof that an authz, XSS, SQLi, SSRF, upload, command-exec, or path-traversal weakness is real
- you need a before-and-after record that a fix removed the defect
- the target can be run or mirrored inside Docker and the work can stay entirely inside that lab

## Do Not Use

- scanning external or third-party systems
- broad brute force or destructive payloads unless explicitly enabled
- replacing normal code review when no repro is needed

## Choose Roles

```text
IF next_step = inventory OR payload_selection OR bounded_exploit_execution THEN ROUTE -> agents/attacker.md
ELSE IF findings_must_become(code_fix OR config_fix OR proxy_fix OR container_fix) THEN ROUTE -> agents/defender.md
ELSE IF artifacts_exist AND run_must_be_summarized THEN ROUTE -> agents/reporter.md
ELSE STOP("lab role must be explicit")
```

## Choose Assets

```text
IF starting_lab_run THEN START -> assets/lab-run-record.md
IF route_discovery_completed THEN START -> assets/endpoint-inventory.md
IF weakness_class_and_endpoint_are_concrete THEN START -> assets/exploit-attempt.md
IF patch_rerun_completed THEN START -> assets/verification-record.md
```

## Choose References

```text
READ -> references/docker-lab-safety.md
READ -> references/attack-flow.md
IF selecting_weakness_specific_checks THEN READ -> references/web-check-playbooks.md
IF calling_a_scanner_or_runtime_signal_confirmed THEN READ -> references/finding-validation-rules.md
```

## Operating Rules

```text
PASS IF
  NETWORK_NAME_is_explicit
  AND TARGET_URL_is_explicit
  AND target_is_reachable_by_docker_network_alias
  AND destructive_modes_are_disabled_by_default
  AND every_suspected_exploit_is_recorded

FAIL IF
  public_dns_is_used
  OR verification_record_is_missing_after_fix_rerun
  OR auth_context_is_required AND repro_context_is_missing
  OR scanner_output_is_treated_as_confirmed_without_request_response_evidence
```

## Output Contract

Return:

- declared support files
- files read before lab execution
- why each file was loaded
- lab metadata
- inventory location
- tool outputs
- exploit attempts and observed results
- verification verdict
- next remediation owner
- files actually used

## Supporting Assets

Local Roles:
- `agents/attacker.md`
- `agents/defender.md`
- `agents/reporter.md`
- `agents/openai.yaml`

Local Assets:
- `assets/lab-run-record.md`
- `assets/endpoint-inventory.md`
- `assets/exploit-attempt.md`
- `assets/verification-record.md`

Local References:
- `references/pentagi-capability-map.md`
- `references/docker-lab-safety.md`
- `references/attack-flow.md`
- `references/web-check-playbooks.md`
- `references/finding-validation-rules.md`

Local Scripts:
- `scripts/bootstrap-lab.sh`
- `scripts/inventory-target.sh`
- `scripts/run-web-checks.sh`
- `scripts/verify-fix.sh`
- `scripts/collect-evidence.sh`

## Promote Recurring Lessons

- reusable lab safety rules -> `references/*.md`
- operator roles -> `agents/*.md`
- repeatable records -> `assets/*.md`
- deterministic shell workflows -> `scripts/*.sh`
