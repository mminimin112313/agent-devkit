---
name: security-review
description: "Use when a code, config, Docker, or request-boundary change needs trust-boundary review, finding classification, or lab handoff."
---

# Security Review

## Procedure

```text
INPUT := { entry_point, trusted_actor, untrusted_actor, boundary_data, capability_at_risk }

STEP_0 := declare(support_files := exact assets/ + references/ set OR none)
STEP_0A := read(required_assets_and_references_before_classification)
STEP_0B := record(why_each_declared_file_was_loaded)
STEP_1 := name_boundary(INPUT)
IF INPUT.entry_point IS null OR INPUT.capability_at_risk IS null THEN STOP("boundary must be explicit")

STEP_2 := read_only(relevant_lenses) FROM references/review-lenses.md
STEP_2A := read_only(automation_evidence_rules) FROM references/automation-evidence.md IF ci_scan_artifacts_exist OR scanner_output_is_cited
STEP_3 := classify(finding OR repro_required OR cleared_with_rationale)

IF result = finding THEN
  RECORD(exact_seam, weakness, impact, severity, evidence, remediation_owner)
  ROUTE -> remediation_owner
ELSE IF result = repro_required THEN
  START -> assets/remediation-handoff.md
  RECORD(target_seam, payload_family, desired_evidence, stop_conditions)
  ROUTE -> security-lab
ELSE
  ROUTE -> next_owner
```

## Overview

Security review starts at the trust boundary.

**Core principle:** if the boundary, exploit path, or remediation owner is implicit, the review is not done.

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
Do not sign off on a security-sensitive seam without naming the boundary, the weakness, and the evidence or repro path.
</HARD-GATE>

<NON-NEGOTIABLE>
Every run must declare its exact local `assets/` and `references/` set before execution, read the required files before classification, and record why each declared file was loaded. Unnamed support files are out of contract and must not be relied on. If no support files are needed, say `none` explicitly. Final outputs must report the declared set, the files actually read, and the files actually used.
</NON-NEGOTIABLE>

<NON-NEGOTIABLE>
If exploitability is uncertain, downgrade the claim to `repro required` and route it to `security-lab`. Do not present guesses as findings.
</NON-NEGOTIABLE>

## When to Use

- a code or config seam crosses a trust boundary
- auth, validation, upload, SSRF, XSS, injection, secret, or container risk is in scope
- a security-sensitive seam needs classification, remediation ownership, or lab follow-up
- the next move is security review, not a generic code review

## Do Not Use

- running live attacks against non-local targets
- replacing normal code review when no security seam changed
- accepting a claim based only on tool output without reading the affected seam

## Required Reads

```text
MUST START -> assets/review-record.md BEFORE classifying_the_seam
IF weakness_is_concrete THEN SWITCH -> assets/finding-record.md
IF next_step = security-lab_repro OR fix_verification THEN SWITCH -> assets/remediation-handoff.md

MUST READ -> references/review-lenses.md BEFORE choosing_security_lenses
IF ci_scan_artifacts_exist OR scanner_output_is_cited THEN MUST READ -> references/automation-evidence.md
IF exploitability_is_uncertain OR runtime_proof_may_be_needed OR one_security_sensitive_seam_could_expand THEN MUST READ -> references/static-vs-dynamic-boundary.md
```

## Choose Roles

```text
IF patch_does_not_exist THEN ROUTE -> agents/security-reviewer.md
ELSE IF patch_exists AND exploit_path_must_be_rechecked THEN ROUTE -> agents/remediation-reviewer.md
ELSE STOP("classify first, then review remediation")
```

## Choose Assets

```text
IF default_review THEN START -> assets/review-record.md
IF feature_adds(new_actor OR trust_boundary OR admin_capability OR webhook OR upload_surface) THEN START -> assets/threat-model.md
IF weakness_is_concrete THEN START -> assets/finding-record.md
IF next_step = security-lab_repro OR fix_verification THEN START -> assets/remediation-handoff.md
```

## Choose References

```text
READ -> references/review-lenses.md
IF ci_scan_artifacts_exist OR scanner_output_is_cited THEN READ -> references/automation-evidence.md
IF deciding(review_only OR lab_repro) THEN READ -> references/static-vs-dynamic-boundary.md
IF docker_surface_changed THEN READ -> references/docker-surface-checks.md
IF seam_is(web_request OR response_path OR upload_flow OR auth_boundary OR url_fetch OR command_execution_path OR template_sink) THEN READ -> references/web-app-review-playbook.md
```

## Output Contract

Return:

- declared support files
- files read before classification
- why each file was loaded
- seam reviewed
- trust boundary
- findings or `repro required` items
- evidence checked
- remediation owner
- next owner or next skill
- files actually used
