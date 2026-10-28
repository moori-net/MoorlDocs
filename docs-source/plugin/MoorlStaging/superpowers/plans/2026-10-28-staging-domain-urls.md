# Staging domain URL correction

**Goal:** Rewrite every cloned sales-channel domain independently, preserving
its origin and language/pseudo path. For `staging`, the user's mappings are
localhost -> localhost/staging, localhost/xyz -> localhost/staging/xyz,
sidequest33.com.local -> sidequest33.com.local/staging, and
sidequest33.com.local/de -> sidequest33.com.local/staging/de (schemes preserved).

**Cause:** Global APP_URL replacement touches only matching origins; fallback
appends after language paths and only runs if no rows were updated.

**Approach:** Read domain IDs/URLs from the destination DB, compute each URL,
and update its ID with bound parameters. Use source-domain URLs by matching ID
as the authoritative original value, enabling reruns and repairing old bad
mappings. Move nested target paths before shorter ones to avoid unique URL
conflicts when the clone name is also an original language/path segment.
For target-only domains, retain prefix detection as a fallback.
A shared URL builder retains protocol,
authority, port, path, query and fragment, avoids double prefixing, and preserves
an actual installation base path from APP_URL when the domain shares that path.
Use it for APP_URL/dashboard links too; root APP_URL trailing slashes must not
produce doubled slashes. Keep maintenance and plugin updates unchanged.

**Validation:** Real process()/finish() behavior with DBAL boundary doubles,
all four user examples together, nonmatching APP_URL origins, encoded paths,
query/fragment, ports, reruns, installation subdirectories, no APP_URL when
APP_URL rewriting is disabled, and unchanged maintenance behavior. No live DB
or existing staging data will be changed by verification.

- [x] Write regression tests and observe failures.
- [x] Implement per-domain updates and shared URL mapping.
- [x] Run full PHP suite, PHP syntax/diff checks and focused review.

Verification: 88 PHP tests / 206 assertions pass; both changed/new PHP files
pass syntax checks and git diff --check passes. Independent review found an
overlapping-name uniqueness issue in the first prefix-only implementation.
Reproduced it with clone names de/staging and a uniqueness-enforcing DB double,
then fixed it using source URLs and longest-target-path-first updates. Added
regression coverage for repairing previously appended /de/staging mappings.
No live staging database or environment files were modified.
