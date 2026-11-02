# Local Runtime Triage

Use this lens when a reported failure may come from the local runtime environment rather than the code seam itself.

```text
USE_THIS_LENS IF
  symptom_may_be_local(auth OR config OR workspace OR sandbox OR install_source)
  OR repro_changes_across_machines_or_sessions
  OR failure_happens_before_the_target_code_path_is_reached
  OR symptom_depends_on(interactive_worker_state OR one_shot_prompt_state OR missing_local_state_artifact)
  OR platform_specific_home_or_config_root_resolution_may_be_wrong

TRIAGE_ORDER := {
  auth,
  config,
  config_root,
  install_source,
  workspace,
  worker_state,
  sandbox,
  system_metadata
}

PASS IF
  local_runtime_inputs_checked_before_code_blame
  AND active_auth_method_or_missing_auth_is_named
  AND config_load_state_is_named
  AND home_directory_or_explicit_config_root_is_named_when_path_resolution_matters
  AND workspace_membership_or_repo_state_is_named
  AND worker_state_file_presence_or_absence_is_named_when_relevant
  AND sandbox_state_is_named_when_relevant

FAIL IF
  code_change_is_proposed_before_local_runtime_state_is_checked
  OR repro_environment_is_implicit
  OR path_resolution_depends_on_home_or_config_root_but_that_source_is_implicit
  OR worker_state_dependency_is_implicit_when_the_surface_requires_it
  OR workspace_or_sandbox_state_is_missing_when_they_matter

STOP("diagnose the local runtime surface before reviewing code changes") IF FAIL_IF_conditions_are_met
```
