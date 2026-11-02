# Go Rulebook

```text
SOURCE_STATUS := checked_primary_sources_http_200
ABSORPTION_DEPTH := starter_distillation
CATALOG_SEED := awesome-guidelines@e9eba9152e4c1d47522eddf5ae1a6bd482ee3e33
PRIMARY_SOURCES := {
  https://go.dev/doc/effective_go,
  https://google.github.io/styleguide/go,
  https://raw.githubusercontent.com/uber-go/guide/master/style.md
}
OWNER_SKILLS := { implementation-backend, architecture-and-design, quality-and-review }

ABSORBED_RULES := {
  small_interfaces_are_owned_by_consumers,
  errors_are_explicit_values_with_context,
  goroutine_channel_and_context_lifetimes_need_shutdown_evidence,
  package_boundaries_should_minimize_global_state,
  table_tests_are_preferred_for_behavior_matrix_edges
}

GENERALIZED_RULES := {
  gofmt_style -> local_tooling_when_go_module_exists,
  project_layout_opinion -> defer_until_repo_has_go_owner
}

DEFERRED_RULES := {
  go_standard_project_layout_import,
  linter_stack_without_go_toolchain
}

VERIFY := PASS IF
  context_cancellation_error_paths_and_package_contracts_are_tested_or_probed
```

