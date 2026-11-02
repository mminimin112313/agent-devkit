# Java and JVM Rulebook

```text
SOURCE_STATUS := checked_primary_sources_http_200
ABSORPTION_DEPTH := starter_distillation
CATALOG_SEED := awesome-guidelines@e9eba9152e4c1d47522eddf5ae1a6bd482ee3e33
PRIMARY_SOURCES := {
  https://google.github.io/styleguide/javaguide.html,
  https://kotlinlang.org/docs/coding-conventions.html,
  https://docs.scala-lang.org/style/
}
OWNER_SKILLS := { implementation-backend, architecture-and-design, quality-and-review }

ABSORBED_RULES := {
  package_and_visibility_boundaries_are_design_contracts,
  nullability_mutability_and_exceptions_need_consumer_evidence,
  concurrency_and_resource_lifecycle_require_named_ownership,
  generated_or_framework_code_should_not_leak_into_domain_style_rules,
  language_specific_style_yields_to_module_local_consistency
}

GENERALIZED_RULES := {
  java_kotlin_scala_formatting -> local_project_formatter_or_existing_pattern,
  jvm_api_guidance -> compatibility_and_migration_contract
}

DEFERRED_RULES := {
  checkstyle_or_scalafmt_policy_without_repo_command,
  enterprise_framework_rules_without_active_surface
}

VERIFY := PASS IF
  package_visibility_exception_nullability_and_lifecycle_changes_have_tests_or_migration_notes
```

