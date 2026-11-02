# Guideline Rulebook Library

This directory turns checked external guideline catalogs into durable, source-backed rulebooks.

```text
LIBRARY_PURPOSE := compile_catalogs_into_rulebooks

PASS IF
  each_entry_is_backed_by_primary_sources
  AND each_entry_names_owner_skill
  AND each_entry_separates(absorbed_rules, generalized_rules, deferred_rules)
  AND uninspected_catalog_links_remain_outside_active_rules

FAIL IF
  catalog_summary_becomes_rule
  OR rulebook_entry_duplicates_SKILL_routing_surface
  OR rulebook_entry_lacks_source_revision_or_access_date
```

## Entries

- [JavaScript and TypeScript](javascript-typescript.md)
- [Python](python.md)
- [Shell and PowerShell](shell-powershell.md)
- [Node Runtime and Data](node-runtime-data.md)
- [Frontend and Remotion](frontend-remotion.md)
- [Release, Docs, and Project Structure](release-docs-project.md)
- [C and C++](c-cpp.md)
- [C# and .NET](csharp-dotnet.md)
- [Go](go.md)
- [Java and JVM](java-jvm.md)
- [Rust](rust.md)
- [Ruby and PHP](ruby-php.md)
- [Mobile Languages](mobile-languages.md)
- [Scientific Languages](scientific-languages.md)
- [Functional and Dynamic Languages](functional-dynamic-languages.md)
- [Markup, Data, and Query Languages](markup-data-query.md)
