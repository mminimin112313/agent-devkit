# Rulebook Routing Map

Use this reference when a request names a language, runtime, file extension, framework, or code-style concern. Route by the work owner, but carry the matching `.codex/rulebooks/` path forward as a required support file for implementation or review.

```text
RULEBOOK_ROUTING := PASS IF
  language_or_runtime_signal_is_named
  AND matching_codex_rulebook_path_is_selected
  AND next_owner_skill_is_named
  AND rulebook_is_carried_into_next_owner_support_files

FAIL IF
  language_specific_work_routes_without_rulebook_path
  OR rulebook_path_replaces_owner_skill_selection
  OR catalog_source_is_used_instead_of_compiled_rulebook
```

## Language And Runtime Map

```text
IF signal IN {js, javascript, mjs, cjs, ts, typescript, jsx, tsx} THEN
  RULEBOOK -> .codex/rulebooks/javascript-typescript.md
  OWNER -> implementation-frontend OR implementation-backend

IF signal IN {node, npm, package_json, child_process, fs, path, sqlite, json} THEN
  RULEBOOK -> .codex/rulebooks/node-runtime-data.md
  OWNER -> implementation-backend

IF signal IN {react, browser, dom, fetch, sse, localstorage, remotion, composition, video_render} THEN
  RULEBOOK -> .codex/rulebooks/frontend-remotion.md
  OWNER -> implementation-frontend

IF signal IN {py, python} THEN
  RULEBOOK -> .codex/rulebooks/python.md
  OWNER -> implementation-backend OR quality-and-review

IF signal IN {sh, bash, zsh, ps1, powershell, shell} THEN
  RULEBOOK -> .codex/rulebooks/shell-powershell.md
  OWNER -> release-and-operations OR quality-and-review

IF signal IN {c, h, cc, cpp, cxx, hpp, c++} THEN
  RULEBOOK -> .codex/rulebooks/c-cpp.md
  OWNER -> implementation-backend OR architecture-and-design

IF signal IN {cs, csharp, dotnet, .net} THEN
  RULEBOOK -> .codex/rulebooks/csharp-dotnet.md
  OWNER -> implementation-backend OR security-review

IF signal IN {go, golang} THEN
  RULEBOOK -> .codex/rulebooks/go.md
  OWNER -> implementation-backend

IF signal IN {java, kt, kotlin, scala, jvm} THEN
  RULEBOOK -> .codex/rulebooks/java-jvm.md
  OWNER -> implementation-backend

IF signal IN {rs, rust, cargo, crate} THEN
  RULEBOOK -> .codex/rulebooks/rust.md
  OWNER -> implementation-backend OR security-review

IF signal IN {rb, ruby, php} THEN
  RULEBOOK -> .codex/rulebooks/ruby-php.md
  OWNER -> implementation-backend OR security-review

IF signal IN {swift, ios, android, mobile} THEN
  RULEBOOK -> .codex/rulebooks/mobile-languages.md
  OWNER -> implementation-frontend OR implementation-backend

IF signal IN {r, julia, jl, fortran, numerical, scientific} THEN
  RULEBOOK -> .codex/rulebooks/scientific-languages.md
  OWNER -> implementation-backend OR quality-and-review

IF signal IN {clojure, erlang, dart, dlang, d, actor, functional} THEN
  RULEBOOK -> .codex/rulebooks/functional-dynamic-languages.md
  OWNER -> implementation-backend OR architecture-and-design

IF signal IN {xml, sql, markdown, md, query, schema, data_file} THEN
  RULEBOOK -> .codex/rulebooks/markup-data-query.md
  OWNER -> implementation-backend OR quality-and-review

IF signal IN {release_notes, changelog, semver, gitignore, gitattributes, env, license, vendor} THEN
  RULEBOOK -> .codex/rulebooks/release-docs-project.md
  OWNER -> release-and-operations OR skillsmith
```

## Handoff Rule

```text
PASS IF
  intake_record_names(rulebook_path, owner_skill, reason_for_selection)
  AND next_owner_reads_the_rulebook_before_decision_or_code

FAIL IF
  route_names_only_the_skill_without_the_rulebook_path_when_language_signal_was_present
```
