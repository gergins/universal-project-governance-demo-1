# Framework release and adoption

The template is independently versioned. Existing derived projects do not auto-update when the template changes.

1. The master uses `template.status=master`, `framework_version`, and a change log.
2. New projects must replace placeholders, set `template.status=initialized`, and record `framework_source_commit` and source repository.
3. Governance checks permit placeholders in the master only. Initialized projects fail validation on unresolved critical placeholders.
4. Update derived projects by reviewed pull request, compare local deviations, run relevant tests and preserve project-specific approvals.
5. Don't overwrite independent project decisions or copy provider credentials between repositories.

CI configuration here is **not** proof that required checks or branch protection have been enabled in GitHub settings.