## Test updates and changes in a staging shop first

MoorlStaging creates and manages test environments directly in Shopware Administration. A separate database and shop directory provide a place to test Shopware updates, extensions and configuration changes before applying them to production.

Three tabs guide the workflow: record the test purpose on the Dashboard, check the server and destination connection under **System & database**, then configure and start the copy under **Create staging**. Creation is enabled only after both checks pass.

## Five steps with control over data and files

Creation runs through five clear steps: back up the database, import it into the destination database, copy shop files, create symlinks and configure the destination shop. Progress and status identify the current step; a reported step error stops the full run. Individual steps can be repeated when needed.

Exclude carts, log entries, orders, customers, SEO URLs and search keywords from the database export. Add further table names on separate lines. File exclusions with wildcards, cache and version-control options, and configurable permissions help adapt the copy to your server.

## Prepare the destination for your tests

MoorlStaging sets the destination database connection, can update the app URL and maps sales channel domains to the staging path while preserving existing language paths and subpaths. Configure maintenance mode, development mode, deactivation of all plugins and your own list of environment variables to set or remove.

A successful full run returns you to the Dashboard with Storefront and Administration links. Internal notes help identify update tests, investigations and development environments.

## Optional customer anonymization

When copying customers and orders for testing, step 5 can replace certain personal data in customer accounts, customer addresses, order customers and order addresses with test data. Customer/order relationships remain intact. The option is off by default and operates only on the destination database.

Existing customer passwords, legacy credentials and recovery records are cleared. Existing customer logins no longer work in staging afterwards. Documents, files, logs, reviews, newsletter data and other plugins' data are not anonymized; the SQL backup created beforehand is also unaffected. The scope is limited to the customer tables described.

## Local commands or execution through SSH

Choose **PHP shell**, **PHP shell via SSH**, **Symfony Process** or **Symfony Process via SSH**. SSH connects to the same server on `localhost:22`. Credentials can come from plugin settings or server-side environment variables. The Symfony/OpenSSH variant also supports key authentication and checks the known host key.

Hosting profiles set binary paths and initial settings for new environments. Existing environments retain their individual settings. You can supply paths to `mysql` and `mysqldump` manually and select the logging level.

## Requirements and operational notes

The extension targets Shopware 6.7 and requires a suitable server with executable shell tools including `rsync`, `mysql`, `mysqldump` and `sed`. Depending on the execution method, it requires `exec`, `proc_open`, the PHP `ssh2` extension, or OpenSSH with `sshpass` for password authentication. Provide a separate destination database, sufficient storage, appropriate permissions and web server rules for the staging path. MoorlFoundation is not required.

Media is copied by default. If you exclude media and link it to the live shop, both shops share those files; changes or deletions in staging then affect the live shop too. Review mail transport, payment providers, webhooks and background services before testing.

The extension creates test copies; it does not automatically transfer changes back to the live shop. Imports and repeated steps can overwrite destination data. The deletion action attempts to remove destination database tables, the copy, backup and public symlink; verify the result. Uninstallation does not automatically remove existing test environments.

Available hosting profiles are not a blanket guarantee for hosting packages. Setup and duration depend on your server, data volume and web server configuration.
