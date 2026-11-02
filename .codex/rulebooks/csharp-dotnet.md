# C# and .NET Rulebook

```text
SOURCE_STATUS := checked_primary_sources_http_200
ABSORPTION_DEPTH := starter_distillation
CATALOG_SEED := awesome-guidelines@e9eba9152e4c1d47522eddf5ae1a6bd482ee3e33
PRIMARY_SOURCES := {
  https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/coding-style/coding-conventions,
  https://learn.microsoft.com/en-us/dotnet/standard/security/secure-coding-guidelines,
  https://learn.microsoft.com/en-us/dotnet/standard/design-guidelines/naming-guidelines
}
OWNER_SKILLS := { implementation-backend, architecture-and-design, security-review, quality-and-review }

ABSORBED_RULES := {
  public_member_names_and_async_contracts_are_api_surface,
  nullable_and_exception_behavior_need_consumer_visible_evidence,
  security_sensitive_input_output_and_serialization_edges_need_review,
  framework_conventions_are_subordinate_to_existing_repo_patterns
}

GENERALIZED_RULES := {
  naming_guidelines -> public_api_compatibility_contract,
  secure_coding_guidance -> trust_boundary_review_lens
}

DEFERRED_RULES := {
  analyzer_rule_set_without_dotnet_project,
  package_versioning_policy_without_release_surface
}

VERIFY := PASS IF
  public_api_or_config_shape_change_has_consumer_evidence
  AND security_boundary_checks_are_named_when_relevant
```

