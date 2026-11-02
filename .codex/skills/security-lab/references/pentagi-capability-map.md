# PentAGI Capability Map

This skill absorbs PentAGI execution ideas into SoloPilot packaging.

```text
FLOW_MAPPING := {
  pentagi_flow -> one_lab_run_directory,
  pentagi_task -> one_security_objective(inventory OR scan OR verification),
  pentagi_subtask -> one_tool_driven_check_or_exploit_attempt,
  pentagi_action -> one_docker_command_request_capture_or_artifact_write
}

ROLE_MAPPING := {
  pentagi_pentester -> agents/attacker.md,
  pentagi_reporter -> agents/reporter.md,
  pentagi_fix_and_guardrail_interpretation -> agents/defender.md
}

CAPABILITY_MAPPING := {
  docker_tool_execution -> scripts/*.sh,
  evidence_packaging -> collect-evidence.sh,
  iterative_rerun_after_remediation -> verify-fix.sh,
  structured_reporting -> assets/*.md
}

OUT_OF_SCOPE := {
  pentagi_web_ui,
  pentagi_database_and_memory_services,
  provider_orchestration,
  background_workers_or_subscriptions
}
```
