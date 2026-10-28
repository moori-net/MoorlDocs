# Symfony Process Implementation Plan

> **For agentic workers:** Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add optional local Symfony Process and Symfony Process with SSH execution.

**Architecture:** Dispatch new execution modes in BinariesTrait while retaining the legacy path. Create local shell processes or SSH argument-array processes and apply staging exit-code rules to captured output.

**Tech Stack:** PHP, Symfony Process, Shopware system config, PHPUnit, OpenSSH, optional sshpass.

**Spec:** ../specs/2026-10-28-symfony-process-design.md

## Global Constraints

- No dependency on MoorlDevTools or package installation.
- Four backend values: `php`, `php-ssh`, `process`, `process-ssh`.
- Remove sshEnable from the UI and migrate missing/legacy selections from it.
- Both SSH backends support configuration or ENV credentials without fallback.
- SSH remains localhost:22 and verifies host keys.
- Passwords never appear in SSH command arguments.

## Review Focus

- Local mode must override sshEnable and avoid the PHP exec path.
- Failed commands with side effects execute once and stop the stack.
- System checks distinguish remote program usage errors from SSH failures.
- Shell quoting, output streams and empty stacks retain useful behavior.
- Existing installations keep their backend until explicitly changed.

### Task 1: Optional executors, settings and documentation

**Files:**
- Modify: src/Core/System/BinariesTrait.php
- Modify: src/Resources/config/config.xml
- Modify: docs/index.md, docs/index.en.md
- Create: tests/Core/System/BinariesTraitTest.php, phpunit.xml.dist

**Interfaces:**
- Consumes: SystemConfigService::get(), LoggerInterface::debug().
- Produces: unchanged execCmdStack(array $cmdStack, bool $test = false): array.
- Internal: createSymfonyProcess(string $cmd, bool $sshEnable): Process.

- [x] Write tests for real process output, system-check exit codes 126/127,
  accepted code 23, other failures, no duplicate side effects, stack order,
  legacy fallback, explicit local mode over SSH, SSH arguments/password env,
  empty SSH username, and SSH transport failures during checks.
- [x] Run `php vendor/bin/phpunit -c custom/plugins/MoorlStaging/phpunit.xml.dist`;
  verify failures expose the absent new dispatch and process creation.
- [x] Implement optional dispatch and process construction in BinariesTrait.
- [x] Add selector/help texts and German/English operator documentation.
- [x] Run the full MoorlStaging suite, PHP lint, XML schema validation and
  `git diff --check`; all must pass. Request independent code review.

## Execution notes

Work in the user-provided plugin checkout to keep the edits available in the
shared Shopware installation. The user explicitly requested implementation;
no additional approval round or commit is needed for these reversible edits.

Final review found one exit-code ambiguity: remote programs and SSH transport
errors can share the same status. Reproduced with real POSIX shell probes and
transport fixtures, then fixed by normalizing remote probe codes to 0 except
126/127. Every other nonzero SSH process result now fails system checks.

Validation: 44 tests, 75 assertions passed (no skipped tests), PHP syntax and
Shopware config schema validation passed. OpenSSH option parsing was verified
using `ssh -G` without connecting. Live SSH/password authentication was not
tested because no configured SSH test account is available in this workspace.

### Task 2: Four explicit modes and private ENV credentials

**Files:** BinariesTrait.php, config.xml, existing tests and operator docs;
new src/Migration/Migration1793145600ExecutionMode.php and migration tests.

**Interfaces:** Keep execCmdStack/createSymfonyProcess unchanged; introduce
getSshCredentials(): array internally, shared by the two SSH executors.

- [x] Add failing tests for explicit PHP/SSH selection overriding the old flag,
  ENV credentials via server/env/getenv, missing username, no admin fallback,
  configuration source isolation, empty password key auth, and migration writes.
- [x] Run the suite and confirm the new behaviors fail before implementation.
- [x] Implement shared credential resolution and explicit mode dispatch;
  migrate existing mode selections without changing explicitly stored modes.
- [x] Expose exactly four options, remove sshEnable and example credentials,
  add credential source and document variable names/clearing existing secrets.
- [x] Run all tests, syntax/schema validation, diff checks and independent review.

Task 2 validation: 64 tests, 151 assertions passing; four changed/new PHP files
pass syntax checks. The actual Shopware ConfigReader parses exactly four
execution options, no sshEnable element, and the local schema validates.
Migration writes were verified through the DBAL boundary; no live database
migration, SSH connection, or plugin update was executed in this workspace.

Independent review found one lifecycle edge: obsolete sshEnable survived a clean
uninstall because Shopware deletes only configuration fields still declared in
config.xml. Added failing tests for cleanup and preservation after write failure,
then fixed migration cleanup after successful selection transfer. Full suite and
diff checks pass; no remaining review findings.

### Task 3: One hosting compatibility selector and reliable initial presets

**Files:** administration detail/create pages, module registration, provider
component, removal of server-config component, snippets, config.xml help and docs;
tests/Administration/hosting-compatibility.test.mjs.

- [x] Test real page methods with delayed configuration reads, provider defaults,
  stored overrides, no preset, new staging initialization, and config read errors.
- [x] Observe failures; load both API responses before applying defaults in
  getStepConfig(), and await this method from create and detail initialization.
- [x] Remove duplicate selector/button and unused recommendation events/snippets.
- [x] Validate JS behavior, Vue templates, configuration schema, PHP regressions,
  diff integrity and request a focused code review.

Use the built-in Node test runner with VM ESM modules to execute real Shopware
component definitions, stubbing only API and component registration boundaries.

Task 3 verification: 10 administration tests passed after observing RED;
64 PHP regression tests passed. Both affected Vue templates compile with the
installed Vue compiler. Snippet/provider JSON and Shopware XML schema/reader
validation pass; only one compatibility control remains. Independent review
found no material issues. Browser rendering and production administration build
were not run.
