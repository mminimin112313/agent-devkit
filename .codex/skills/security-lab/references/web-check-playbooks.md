# Web Check Playbooks

Use harmless proofs and bounded requests. The goal is confirmation and repair, not impact maximization.

```text
AUTHN_AUTHZ := {
  collect_at_least_two_roles_or_identities_when_possible,
  compare_same_object_access_with_low_privilege_and_high_privilege_accounts,
  test_direct_object_references_in(path_params, query_params, graphql_ids, json_body_fields),
  confirm_server_rejects_unauthorized_reads_and_writes_even_when_client_ui_hides_the_action,
  EVIDENCE_TO_KEEP := {
    object_id_used,
    request_and_response_pair,
    expected_authorization_result,
    observed_authorization_result
  }
}

XSS := {
  start_with_unique_marker_in_every_reflected_input,
  identify_reflection_context(html_text, attribute, script, style, url),
  use_harmless_proof_payloads_only_after_reflection_is_confirmed,
  verify_payload_survival_across(storage, rendering, later_views),
  EVIDENCE_TO_KEEP := {
    raw_payload,
    reflection_context,
    rendered_response_or_screenshot,
    whether_execution_required_user_interaction
  }
}

SQLI := {
  begin_with_low_noise_probes(quote_imbalance, numeric_boundary_changes, sort_or_filter_manipulation),
  record_deltas_in(errors, timing, status_codes, row_counts),
  use_ENABLE_SQLMAP_path_only_when_the_seam_is_promising_and_the_exact_input_is_known,
  STOP_IF := parameterization_failure_is_confirmed_without_needing_broader_extraction,
  EVIDENCE_TO_KEEP := {
    candidate_parameter,
    baseline_request_and_changed_request,
    observed_delta,
    sqlmap_output_path_if_used
  }
}

SSRF := {
  point_callbacks_to_lab_owned_service_or_attacker_container_alias_never_external_hosts,
  test(import, image_fetch, pdf_render, webhook, crawler, preview)_endpoints,
  compare_allowed_public_looking_destinations_with(blocked_docker_aliases, loopback_style_names, internal_callback_targets),
  confirm_redirects_alternate_schemes_or_dns_names_do_not_bypass_initial_validation,
  EVIDENCE_TO_KEEP := {
    destination_url_used,
    whether_server_fetched_it,
    headers_or_tokens_forwarded,
    callback_log_or_target_side_log
  }
}

FILE_UPLOAD_AND_PATH_TRAVERSAL := {
  test(size, extension, mime_mismatch, svg, double_extension)_handling_with_harmless_files,
  verify_where_uploaded_files_are_served_and_whether_content_is_transformed_or_sanitized,
  probe_download_and_file_view_endpoints_with_bounded_traversal_markers_before_sensitive_paths,
  confirm_archive_extraction_keeps_files_inside_intended_directory,
  EVIDENCE_TO_KEEP := {
    filename_and_content_type_used,
    upload_response,
    retrieval_path,
    server_behavior_after_retrieval
  }
}

COMMAND_EXECUTION_AND_DEBUG_EXPOSURE := {
  look_for(ping, conversion, archive, report, git, admin_tooling)_features,
  prefer_harmless_time_or_echo_markers_in_the_lab,
  compare_normal_input_and_shell_metacharacter_variants_only_when_the_seam_reaches_a_command_sink,
  check(debug_endpoints, stack_traces, config_dumps, health_pages)_for_secret_disclosure,
  EVIDENCE_TO_KEEP := {
    command_sink_or_debug_path,
    input_variant,
    observed_time_output_or_error_difference,
    logs_or_screenshots
  }
}
```
