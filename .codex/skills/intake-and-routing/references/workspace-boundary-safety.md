# Workspace Boundary Safety

Use this lens when the current working directory may be broader than the task boundary or when repository scope is unclear.

```text
USE_THIS_LENS IF
  cwd_scope_is_unclear
  OR current_directory_is_broader_than_the_target_repo
  OR read_search_authority_would_expand_materially_if_work_continues

BOUNDARY_INPUTS := {
  cwd,
  target_repo_or_project_root,
  task_owned_surface,
  broad_cwd_signal,
  explicit_user_approval
}

PASS IF
  target_repo_or_project_root_is_named
  AND task_owned_surface_is_named
  AND (
    cwd_is_inside_the_target_repo_or_project_root
    OR explicit_user_approval_exists_for_broad_scope
  )

FAIL IF
  target_repo_or_project_root_is_missing
  OR task_owned_surface_is_implicit
  OR broad_cwd_signal_exists_and_explicit_user_approval_is_missing

STOP("narrow the working boundary before routing") IF FAIL_IF_conditions_are_met
```
