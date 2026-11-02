# Mobile Languages Rulebook

```text
SOURCE_STATUS := checked_primary_sources_http_200
ABSORPTION_DEPTH := starter_distillation
CATALOG_SEED := awesome-guidelines@e9eba9152e4c1d47522eddf5ae1a6bd482ee3e33
PRIMARY_SOURCES := {
  https://www.swift.org/documentation/api-design-guidelines/,
  https://github.com/github/swift-style-guide,
  https://kotlinlang.org/docs/coding-conventions.html,
  https://github.com/ribot/android-guidelines
}
OWNER_SKILLS := { implementation-frontend, implementation-backend, product-and-ux, quality-and-review }

ABSORBED_RULES := {
  platform_lifecycle_state_and_permission_edges_are_first_class_contracts,
  public_api_names_should_read_at_call_site,
  ui_thread_async_and_cancellation_paths_need_device_or_runtime_evidence,
  accessibility_and_localization_impacts_need_review_when_user_visible
}

GENERALIZED_RULES := {
  swift_kotlin_formatting -> local_project_style,
  android_architecture_guidance -> lifecycle_and_boundary_contract
}

DEFERRED_RULES := {
  ios_android_scaffold_policy_without_mobile_project,
  device_matrix_policy_without_release_owner
}

VERIFY := PASS IF
  lifecycle_permissions_accessibility_and_async_paths_have fresh_evidence
```

