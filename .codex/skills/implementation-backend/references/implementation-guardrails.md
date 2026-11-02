# Backend Implementation Guardrails

Trace impact beyond direct callers: shared mutable state and aliases, inherited or dynamically dispatched behavior, and observable I/O or events can carry a change into other consumers. Use these paths to choose regression checks; a small diff or a static call graph alone does not establish safety.

When coupling prevents a useful check, separate a minimal reviewed behavior-preserving boundary edit from the requested functional change. Check the available build, type, source, and runtime observations, then capture baseline behavior before changing the function. Report unavailable observations honestly. A successful build supports the edit but does not establish behavioral equivalence.

Keep preparation, structural edits, and functional edits attributable by running fast relevant checks between them. Run the project's required acceptance checks for the final result. Preserve existing work rather than restarting solely to enforce a test-writing sequence.

Review a preparatory boundary edit through its diff and available observations; this does not require a separate user approval round. Preserve the default production wiring, initialization order, failure timing, and error propagation. If any of those contracts changes, separate it as an intended behavior change rather than claiming preservation. Name an actual unavailable environment or dependency and its unverified scope when blocked; inconvenient test setup alone does not make verification unavailable.

When a regression test for a fix or new behavior was added after implementation, confirm its expected failure against a disposable pre-change copy or with only the fix disabled in an isolated copy. Keep the live checkout and existing work intact. Do not require a preservation baseline to fail. If the comparison cannot run, report that evidence gap instead of treating the new passing test as proof that it detects the regression.

Choose checks by what can change, including generated behavior, schemas, executable documentation, and rendered layout. Use the relevant build, render, or runtime check for those effects; a pure wording edit does not need an unrelated new unit test.

Before restructuring an untested boundary, observe representative current outputs and effects. Separate behavior being preserved from the defect or requirement being changed, and investigate unexpected existing results instead of automatically treating them as correct or widening the task to fix them all.

Choose the smallest controllable boundary that exercises the affected decision without an unrelated live dependency. Preserve production behavior when making it testable. Use a real integration when persistence or an external interaction is itself the contract being changed; a mock that replaces that contract cannot establish its correctness.

When working in tightly coupled legacy code, trace effect propagation to locate narrow pinch points that cover the intended change cluster, and step inward if a pinch point widens into a brittle multi-dependency harness. When existing collaborators cannot be untangled safely in one step, isolate new behavior in a newly extracted sprout function or class, or wrap the boundary cleanly without tangling temporal pre- and post-steps into existing branches.

Keep code either deep in decision logic or wide in collaborators, never both. Extract domain rules and complex algorithms into in-memory units with few collaborators so they can be verified through output-based or state-based tests, and keep controllers and repositories as humble orchestrators that coordinate storage, transactions, and external dispatch. Eliminate special-case branches where possible by defining normal-case state and range semantics so boundary inputs work naturally, and document module and method interfaces with precision—units, inclusive or exclusive bounds, null semantics, resource ownership, invariants, side effects, and preconditions—without leaking implementation details into interface comments.

Distinguish managed out-of-process dependencies (such as an application-owned database) from unmanaged external dependencies (such as message buses, webhooks, or third-party APIs). Keep database schema and reference data in version-controlled migrations, commit business operations atomically through explicit transactions or units of work, use separate transaction or unit-of-work scopes for arrange, act, and assert in integration tests, and reset mutable test data at the start of each test. Mock or spy only consumer-owned adapters at the outermost edge of unmanaged dependencies, verifying both expected calls and the absence of unexpected calls, and pass time or request context explicitly rather than through ambient static state or production test-environment flags.

```text
GUARDRAILS := PASS IF
  contract_and_boundary_behavior_are_defined_before_implementation_detail
  AND side_effects_are_isolated_at_explicit_runtime_edges_or_adapters
  AND null_empty_timeout_duplicate_and_partial_failure_cases_are_treated_as_first_class_work
  AND deep_domain_or_algorithm_logic_is_separated_from_humble_controller_orchestration
  AND managed_dependencies_are_verified_via_final_state_with_isolated_arrange_act_assert_scopes
  AND unmanaged_dependencies_are_mocked_or_spied_only_at_consumer_owned_outermost_adapters
  AND interface_comments_state_abstraction_invariants_bounds_and_preconditions_without_implementation_leakage

FAIL IF
  delivery_logic_widens_into_architecture
  OR migration_strategy_is_required_but_missing
  OR cross_consumer_redesign_is_smuggled_into_implementation
  OR a_unit_combines_high_domain_complexity_with_many_out_of_process_collaborators
  OR tests_assert_interactions_on_stubs_or_mock_in_process_or_managed_dependencies
  OR production_code_is_polluted_with_test_environment_switches_or_ambient_time_singletons
```
