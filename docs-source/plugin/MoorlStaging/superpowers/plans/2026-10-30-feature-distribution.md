# Feature Distribution Implementation Plan

**Goal:** Replace version-branch synchronization with distribution of completed feature PRs to `main` and all other `6.*` branches.

**Architecture:** A closed, merged PR from a same-repository `feature/**` branch triggers a Node.js script. Replay only feature commits, push clean results directly, and publish conflicts on draft PR branches for manual resolution. A rejected direct push also falls back to a PR. Process targets independently and report failures in the job summary.

**Tech stack:** GitHub Actions, Git, GitHub CLI, Node.js built-in modules and test runner.

**Agreed approach:** User approved distribution after feature PR merge, with PRs for conflicts instead of silently skipping targets. The old `LATEST_BRANCH` merge is removed.

**Single-branch features:** Add the PR label `no-backport` before merging a feature PR into its intended destination. The distribution job is skipped; the version-protection check still applies. Since distribution is skipped, its dependent cleanup does not automatically delete this feature branch. Without the label, the normal distribution and cleanup behavior applies. Adding the label after merging does not undo completed transfers.

## Constraints and review focus

- Preserve version-specific history; do not merge the entire source branch.
- Support merge, squash and rebase PRs, including multiple feature commits.
- Never push conflict markers directly to a target branch.
- Respect branch protection, concurrent updates, and existing backport PRs.
- Make retries safe and continue processing other targets after a failure.
- Require repository permission for Actions to create PRs. Bot pushes do not start the release workflow.

## Implementation and verification

- [x] Add `.github/workflows/distribute-features.yml` with the merged-feature trigger and explicit write permissions, replacing the old version-branch synchronization workflow.
- [x] Add `.github/scripts/distribute-feature.mjs` for discovery, cherry-picks, PR fallback, retry markers, and summaries.
- [x] Add Git integration tests in `tests/Workflows/distribute-feature.test.mjs` using disposable local repositories.
- [x] Verify clean backports, version isolation, merge/squash/rebase, text and modify/delete conflicts, and already-applied commits.
- [x] Validate workflow YAML and run all Node tests.
- [x] Complete a read-only review and resolve material findings: exact PR-marker matching and rejection of incomplete API commit lists.
- [x] Add feature-branch cleanup after successful distribution and after backport PR merges. Retain branches for missing targets, open/closed-unmerged PRs, or new feature commits; use an atomic Git lease for deletion. Verify with local bare remotes, including a concurrent push.

**Operational limit:** Actual GitHub pushes, API requests, and repository permissions are not exercised by local tests. Conflict drafts deliberately contain conflict markers and require full review, including binary and modify/delete conflicts.

## Composer version protection

- `.github/workflows/protect-composer-version.yml` checks feature/backport PRs against their merge base. It uses `pull_request_target`, a checkout of the exact base SHA, and read-only contents permissions; PR code is fetched only as Git data and never executed.
- Other Composer metadata and dependencies remain editable. Release version commits outside feature/backport PRs remain permitted.
- Distribution applies linear feature commits as one net change, retaining their original SHA references in the commit message. This allows complete draft PRs even when multiple Composer edits conflict.
- During distribution, every target retains its original root `version`. Version-only conflicts are resolved automatically; other Composer conflicts still require a draft PR.
- Activation: install the workflow/checker on each destination branch, then mark **Protect composer version** as required in GitHub branch protection or rulesets for `main` and `6.*`. The check cannot block merges until that repository setting is enabled. Direct automated distribution remains subject to existing branch rules and can fall back to PRs.
- Verified using disposable Git repositories: version edits/removals rejected, dependency edits accepted, unrelated base release accepted, formatting/nested versions preserved, and Composer conflicts handled across multiple feature commits.

## Automatic releases after adoption

Successful direct adoptions explicitly dispatch `release-feature.yml`; original feature merges and later backport PR merges trigger that workflow directly. For branches listed in `RELEASE_BRANCHES`, it creates a separate minor-version commit after adoption, preserving the rule that feature PRs themselves cannot change the version. See `2026-10-30-automatic-feature-releases.md` for snapshot, collision and retry behavior. The existing central release builder remains in use.
