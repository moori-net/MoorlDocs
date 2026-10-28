# Optional Symfony Process execution

The user requested the working MoorlDevTools Symfony Process approach as an
optional MoorlStaging backend, including a second variant using SSH.

## Approach

The user refined the selector to exactly four choices: `php` (PHP shell),
`php-ssh` (PHP shell via SSH), `process` (Symfony Process), and `process-ssh`
(Symfony Process via SSH). Remove the separate `sshEnable` configuration field.
A migration converts missing or `legacy` execution modes from the previous
`sshEnable` value, preserving explicit choices. Runtime compatibility remains
for installations where migrations have not yet run. The selector has no XML
default so plugin configuration synchronization cannot overwrite old SSH mode
before migration runs; the migration initializes new installations to `php`.
After successful migration, remove the obsolete sshEnable key so a later clean
uninstall/reinstall cannot accidentally restore its former SSH selection.

Add `sshCredentialsSource` with `configuration` (default) and `environment`.
Both SSH backends resolve credentials through the same method. Environment
mode reads `MOORL_STAGING_SSH_USERNAME` and `MOORL_STAGING_SSH_PASSWORD` using
Shopware EnvironmentHelper with getenv fallback. It never reads admin username
or password settings, never falls back to them, and never copies ENV secrets
into system config. Missing usernames fail with an actionable message. Missing
or empty passwords permit key authentication only for Symfony SSH. Existing
admin credentials are not deleted automatically; document clearing them after
switching to ENV. Remove example credential defaults from configuration.

Local Symfony execution uses `Process::fromShellCommandline()` like DevTools.
SSH execution uses a Process argument array to invoke OpenSSH on localhost:22
with the configured SSH username. Password authentication uses `sshpass -e`
and passes the configured password only through `SSHPASS`. An empty password
selects noninteractive key authentication. SSH host key checking stays enabled;
the PHP user's known_hosts must already trust localhost. These runtime
requirements are documented in both languages and the settings help text.

## Execution contract

- No Symfony process timeout, matching DevTools and long staging jobs.
- Preserve shell expressions, pipes and redirects, and the current local cwd.
- Return the last command's output as an array of lines, including stderr.
- Normal execution accepts codes 0 and 23; other codes throw with diagnostics.
- System checks reject codes 126 and 127 but accept other exit codes, as before.
- SSH connection/authentication failures must fail even during system checks.
- Never retry failed Symfony commands to collect stderr.
- Leave existing executors and binary compatibility settings unchanged.

## Validation

Run real harmless PHP child processes for output, exit codes, ordering and
single execution. Check actual SSH Process arguments and environment without
connecting to an SSH server. Test legacy dispatch and validate config.xml
against the installed Shopware schema. Live SSH is an environment integration
check and cannot be claimed from unit tests.

## Hosting compatibility configuration refinement

Keep the hosting provider selector only in plugin config. Remove the duplicate
staging server-config selector/button and component. On create/detail loading,
await both step configuration and saved global compatibility before initializing
processConfig: general step defaults, then provider recommendations, then saved
per-staging values. Preserve explicit false and empty-string saved values.
Publish stepConfig only after initialization so child step components cannot
race the preset lookup. Unknown/default/null-preset providers use general
defaults. On lookup failure notify the user and block execution until loaded.
Reuse providers.json as the source of recommendations and retain backend binary
selection from the same global compatibility setting.
