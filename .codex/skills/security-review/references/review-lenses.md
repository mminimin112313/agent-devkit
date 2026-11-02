# Security Review Lenses

```text
READ ONLY the lenses relevant_to(named_seam)

IF seam_touches(identity OR auth OR tenant_scope OR object_ownership) THEN PASS IF
  ingress_source_is_named
  AND auth_path_is_named
  AND authz_checks_are_named
  AND tenant_or_user_scope_is_named
  AND object_ownership_check_is_named

IF seam_touches(validation OR rendering OR stored_content) THEN PASS IF
  canonicalization_happens_before_validation
  AND output_encoding_matches_actual_sink
  AND active_content_sinks_are_bounded
  AND sanitization_exists_before_rendering

IF seam_touches(uploads OR filesystems OR shell_execution) THEN PASS IF
  upload_validation_checks(size AND mime AND extension AND server_side_type)
  AND filenames_cannot_escape_intended_directory
  AND command_execution_uses_fixed_argument_arrays
  AND uploaded_files_cannot_become_executable_or_stored_payloads

IF seam_touches(outbound_fetch OR webhooks OR redirects) THEN PASS IF
  scheme_host_port_and_redirects_are_restricted
  AND private_and_metadata_targets_are_blocked
  AND redirects_cannot_enter_private_space
  AND outbound_destinations_do_not_leak_tokens

IF seam_touches(errors OR logs OR traces OR debug_paths) THEN PASS IF
  errors_do_not_expose(secrets OR stack_traces OR sql OR signed_urls)
  AND logs_do_not_expose(auth_headers OR session_ids OR reset_tokens OR document_bodies)
  AND debug_paths_do_not_expose_internal_state

IF seam_touches(docker_runtime OR ports OR mounts OR privilege) THEN PASS IF
  debug_ports_are_not_exposed_by_convenience
  AND writable_mounts_do_not_expose_host_files_or_shared_secrets
  AND service_is_not_overprivileged
  AND lateral_reach_is_segmented
```
