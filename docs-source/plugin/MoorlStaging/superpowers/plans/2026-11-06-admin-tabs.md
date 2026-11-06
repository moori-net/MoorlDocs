# Admin tabs implementation plan

**Goal:** Three Shopware administration tabs: dashboard, system/database checks, staging creation.

**Architecture:** Keep the existing detail/create components and step cards. Store the selected tab on the page. Keep check components mounted when switching tabs so validated state survives. Save new records before opening checks; invalidate database validation whenever credentials change. Only execute after saving successfully, with one active step at a time.

**Tech stack:** Shopware 6.7 administration, Vue Options API, Core tabs/cards/loader, Node test runner.

## Tasks

- [x] Add behavior tests for save failure, locked creation, active-step tracking, database validation and tab navigation; verify failures before implementation.
- [x] Update detail/create lifecycle, tab navigation and sequential execution. Preserve existing hosting defaults and user edits to cards.
- [x] Split template into three tabs, add localized guidance and progress, replace running icons with Core loaders, disable editing during execution, improve responsive spacing.
- [x] Run all plugin Node tests, syntax/template checks and diff review. Report build/browser limitations.

## Review focus

- Failed saves must never start a destructive process.
- Edited credentials and pending checks must lock creation, including stale asynchronous responses.
- Navigating tabs must retain configuration and validated state.
- Only the current step is loading; later steps remain pending after a failure.
- A new record must retain its selected tab after the initial save.

## Verification

- `node --experimental-vm-modules --test tests/Administration/*.test.mjs tests/Workflows/*.test.mjs`: 61 passed.
- Vue compiler: all four changed templates compiled; Babel parser: changed JavaScript parsed; Sass: changed styles compiled.
- `git diff --check`: clean.
- Independent review found a missing method on the Core tab wrapper and nullable configuration during progress refresh. Both fixed with failing-then-passing regression tests.
- Use the Core sync repository writer to propagate transport failures, including responses without structured API errors.
- Full plugin production build passed using the existing Docker container and an isolated source copy at `/tmp/moorl-staging-redesign-20261106-verify`. Windows build dependencies contain Linux esbuild binaries; no dependency installation or live container source update was needed.
- Browser interaction/visual review remains unverified. Build artifacts were only generated in the isolated verification directory; deployment is separate.
