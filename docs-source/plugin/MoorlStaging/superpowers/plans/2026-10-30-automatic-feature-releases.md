# Automatic Feature Releases Implementation Plan

**Goal:** After each successful feature/backport adoption, increment the destination's patch version once and explicitly run the existing release pipeline on that version commit.

**Architecture:** A queued, repository-wide workflow handles merged feature/backport PR events and dispatches from successful direct backports. A script validates adoption, creates a Composer version commit and immutable `release-source/<branch>/pr-<original PR>` tag atomically, then dispatches `release.yml` on that tag. The existing central reusable builder is preserved; its `github.sha` is now the exact version commit. The immutable tag makes retries reuse the original version instead of incrementing again.

**Constraints:** Honor `RELEASE_BRANCHES`; do not release unresolved/closed-unmerged backports. Preserve normal manual releases and Composer push releases. Use GitHub token `actions: write` explicitly for dispatch. Serialize and queue version operations. Respect protected branches; rejected pushes fail without publishing. Choose the next unused patch version, considering repository tags and branch versions, to avoid cross-branch version collisions. Preserve major and minor numbers. Do not modify the central github-actions repository.

## Steps

- [x] Add tests for patch selection, atomic version publication, immutable retry snapshots, failure recovery, and dispatch/adoption decisions.
- [x] Implement `.github/scripts/release-feature.mjs` and `.github/workflows/release-feature.yml`.
- [x] Dispatch the version workflow after successful direct distribution, including retries.
- [x] Extend `release.yml` to accept validated automatic source tags, preserving the existing builder and branch allowlist.
- [x] Run local Git integration tests and workflow YAML checks; review the final change.

## Reviewed edge cases and operations

- Include all immutable snapshot versions in version reservations, even after a source branch advances to another version. Queue both preparation and central publishing, so duplicate dispatches see completed tags rather than racing builds.
- Composer push releases now require an actual root-version change. Dependency-only feature merges do not publish the unchanged old version.
- A published release is a completed retry. A draft release or numeric version tag without a published release is an explicit failure requiring recovery of the existing build/artifact; simply dispatching the central builder again would skip publishing because its preflight detects the existing numeric tag. The original version snapshot is retained and never incremented again.
- Example: `1.7.5` becomes `1.7.6`. If `1.7.6` is already used or reserved anywhere in the repository, choose the next unused patch version instead. A version in another minor series does not block a patch increment.
- `no-backport` still prevents distribution, while the original merged destination can receive its patch release. Conflicted/unmerged targets get no bump; a later successful backport merge triggers their release.
- The original minor-increment requirement was corrected to patch increments. Existing release snapshots retain their stored version on retries; this change does not rewrite already prepared/published releases.
- Retry a failed preparation/dispatch using **Prepare automatic feature release**, choose the destination branch, and enter the original feature PR number. For a failure inside the existing central build, inspect that build run; if its numeric tag already exists, recover the published release using its artifact instead of creating another version.

**Validation limit:** No live GitHub dispatch, release publishing, Store upload or repository settings are changed locally. Install these workflows on the default branch and target branches before using the automation. Branch rules must permit the bot's version commit; the workflow does not bypass protection.
