---
description: Error Messages - Causes and Solutions
tags:
- Error Messages
- Composer
---

# Error Messages - Causes and Solutions

## 🤔 Unfortunately, something went wrong

To correctly interpret an error, I need an error message or a log file. The easiest way is with the `FroshTools` plugin, which provides you with a log viewer.

For seamless support, please install this plugin: [Frosh Tools](https://store.shopware.com/frosh12599847132f/tools.html).

![Log Viewer](images/frosh-tools-log-viewer.jpg)

Here you will also find the basic steps for debugging errors:

[https://docs.shopware.com/de/shopware-6-de/tutorials-und-faq/fehlermeldungen-debuggen](https://docs.shopware.com/de/shopware-6-de/tutorials-und-faq/fehlermeldungen-debuggen)

## 💀 Shop "broken"? Don’t panic!

If the shop stops working because of a plugin and you can’t access the administration, you can simply deactivate the plugin in the database. Using your database management tool (PHPMyAdmin, Adminer, etc.), go to the `plugin` table, find the plugin by its technical name, and set the `active` field to "0". The plugin will then be deactivated and will no longer cause any problems.

## 💡 Golden Rule: Clear cache, deactivate/activate plugin

Most problems can be resolved in a few steps. If possible, try clearing the cache and deactivating and reactivating the plugins. No data will be lost in the process.

## ❌ Absolute No-Gos: Manually deleting plugin and database tables

Unless you are a Shopware expert, you should never perform these actions:

- Delete a plugin via FTP
- Manually delete the plugin's database tables
- If you are entitled to support, always create a ticket immediately

## ⚠️ Busy shop? Test system!

If you cannot afford outages on your shop, always play it safe and create a test system. If you need to move quickly, you can purchase a plugin for creating test systems in the Shopware Community Store.

## Common Error Messages

### Required plugin/package "moorl/foundation" is missing...

Are you getting the following error message when trying to install the plugin?

```text
Required plugin/package "moorl/foundation 1.4.*" is missing or not installed and activated
Required plugin/package "moorl/foundation 1.5.*" is missing or not installed and activated
Required plugin/package "moorl/foundation 1.6.*" is missing or not installed and activated
```

Then you are missing the Foundation plugin. You can acquire the plugin for free here:

[https://store.shopware.com/moorl50852475974f/foundation-plugin.html](https://store.shopware.com/moorl50852475974f/foundation-plugin.html)

### Could not execute "composer require" for plugin...

Since Shopware 6.5, plugins can install packages via composer. Not all plugins use this feature, but many moori plugins do.

You can avoid this error by...

1. Deactivating all plugins during a Shopware major update
2. Updating the plugins while they are deactivated and only then reactivating them
3. Updating the plugin after each manual upload (ZIP archive)

However, if you encounter an error, you can resolve it as follows:

```text
Could not execute "composer require" for plugin "MoorlSignIn (moorl/sign-in:2.5.9). Output: ./composer.json has been updated Running composer update moorl/sign-in --with-dependencies Loading composer repositories with package information Dependency shopware/core is also a root requirement. Package has not been listed as an update argument, so keeping locked at old version. Use --with-all-dependencies (-W) to include root dependencies. Updating dependencies Your requirements could not be resolved to an installable set of packages. Problem 1 - Root composer.json requires moorl/foundation 1.5.28 (exact version match: 1.5.28 or 1.5.28.0), found moorl/foundation[1.5.29] but it does not match your constraint and is therefore not installable. Make sure you fix the constraint as packages installed from symlinked path repos are updated even in partial updates and the one from the lock file can thus not be used. Installation failed, reverting ./composer.json and ./composer.lock to their original content.
```

This error message logs the issues:

- Problem 1 - Root composer.json requires moorl/foundation 1.5.28

Solution:

1. note which composer packages are mentioned in the problems.
2. open the file `composer.json`, which is located in the main directory of the shop
3. secure variant (may have to be repeated with every Shopware update!): Change the version of the package to the one in the error message (in this example it is moorl/foundation 1.5.29)
4. alternative variant for shop operators: Change the version, use an asterisk for the last number (in this example it is moorl/foundation 1.5.*)
5. alternative variant for experienced shop operators: Delete the entire line to remove the ‘require’. If this variant works, nothing else needs to be corrected.
6. after you have saved the file, you should be able to update your plugins again

!!! note

      If the problem occurs with a plugin update, then you can carry out step 5. If there are problems with a Shopware update, then try step 3 or 4 to prevent possible negative consequences.

![](images/fix-composer-not-match-constraint.jpg)

### Environment variable COMPOSER_HOME is misconfigured

If you receive this or a similar error message, either the path to the composer home is incorrect, or composer does not have read/write permissions on your web server.

```text
Could not execute "composer require" for plugin "MoorlFoundation (moorl/foundation:1.6.2). Output: Composer could not detect the root package (shopware/production) version, defaulting to '1.0.0'. See https://getcomposer.org/root-version ./composer.json has been updated Composer could not detect the root package (shopware/production) version, defaulting to '1.0.0'. See https://getcomposer.org/root-version Running composer update moorl/foundation
```

Open the `.env` or `.env.local` file in the main directory of your shop and adjust the environment variable accordingly.

### Table: custom_field_set Entry already exists...

```text
Table: custom_field_set Entry already exists [{"id":"98caa393862baa83506fabb17618d81b","name":"moorl_video"...
```

Please note the name of the entry in the database. In this case, it is `moorl_video`. This error can only be fixed by a query directly in the database:

```sql
DELETE FROM `custom_field_set` WHERE `name` = 'moorl_video';
```

### Error during installation or update (including Shopware updates)

Shopware has a separate file for each database update, the so-called migration classes, where database commands are processed.

During installation or update, the process can occasionally be interrupted. This problem is often caused by actions like restoring a backup, replacing data via FTP, or manually removing plugins.

Error 1: `SQLSTATE[42S02]: Base table or view not found`

This indicates that the plugin was previously installed, manually deleted, and its tables in the database were also deleted. However, the entries in the `migration` table were not deleted. To reinstall the plugin normally, you need to delete the entries in the `migration` table as well.

If the error occurs with the `moori Foundation` plugin, you need the technical name of the plugin, which is `MoorlFoundation`. Create a database command to delete the data from the `migration` table:

```sql
DELETE FROM `migration` WHERE `class` REGEXP '^MoorlFoundation\.*$';
```

Error 2: `SQLSTATE[42S21]: Column already exists`

This error occurs as described above, but with the difference that the `migration` table was cleared while plugin tables still exist. Since the migration was interrupted and the data already exists, this step must be skipped. Execute the following command and repeat it as necessary after each update attempt:

```sql
UPDATE `migration`
SET `update` = now(), `message` = NULL
WHERE `class` REGEXP '^MoorlFoundation\.*$' AND `message` IS NOT NULL;
```

## Errors in Administration

### No CMS Block Displayed

I have decided that CMS blocks (cms_block) should not reference their content and should be used exclusively for the layout of experience worlds.

After you have dragged a block into your page, you can easily replace the elements within it.

![Experience Worlds Editor](images/faq-1-1.jpg)

![Experience Worlds Editor](images/faq-1-2.jpg)

## Errors in the Storefront

### General Display Errors

The plugins are developed in the Shopware standard theme. Display errors usually occur in conjunction with a third-party theme.

Themes from the Shopware Store generally follow the rules of template inheritance.

With themes from [Zenit Design](https://store.shopware.com/zenit-design.html), there can sometimes be issues with modal windows, such as on the product detail page. There are often settings in the theme to resolve these errors.

There have been no reported issues with themes from [RH-Webdesign](https://store.shopware.com/rh-webdesign.html) and [ThemeWare](https://store.shopware.com/tc-innovations-gmbh.html).

Custom themes are often very rudimentary; test the functions best with the Shopware standard theme!

### Functions Not Executing as Expected

This is a JavaScript error. You can see these errors in your browser's developer tools (F12). In the case of a JavaScript error, you should first clear all cookies and site data from your browser (hard reload). If the issue persists, deactivate all plugins and themes one by one, except for the moori plugins. If the error still occurs, send me an email or create a support ticket!

Problems with tracking plugins are often noted, so start there.

## Errors Related to ElasticSearch or OpenSearch

### No Products Displayed After Activating the Plugin

No products are displayed, or the shop is no longer accessible. The following error message appears in the ElasticSearch log:

```text
{"error":{"root_cause":[{"type":"query_shard_exception","reason":"failed to create query: [nested] failed to find nested object under path [creators]","index_uuid":"OFSjs3dPTnyefiinZNhH6g","index":"sw_product_2fbb5fe2e29a4d70aa5854ce7ce3e20b_1715904015"}],"type":"search_phase_execution_exception","reason":"all shards failed","phase":"query","grouped":true,"failed_shards":[{"shard":0,"index":"sw_product_2fbb5fe2e29a4d70aa5854ce7ce3e20b_1715904015","node":"FXYG3dBvTSmapxiPaHG5Tg","reason":{"type":"query_shard_exception","reason":"failed to create query: [nested] failed to find nested object under path [creators]","index_uuid":"OFSjs3dPTnyefiinZNhH6g","index":"sw_product_2fbb5fe2e29a4d70aa5854ce7ce3e20b_1715904015","caused_by":{"type":"illegal_state_exception","reason":"[nested] failed to find nested object under path [creators]"}}}]},"status":400} [] []
```

The issue is that the data structure (mapping) has been altered by the plugin, so you need to rebuild the index for ElasticSearch.

The [Frosh Tools](https://store.shopware.com/frosh12599847132f/tools.html) plugin is very useful for this. Click on `Reindex`, wait a while, and check if the error has been resolved.

![ES Reindex](images/frosh-tools-es-reindex.jpg)

If the error cannot be resolved this way, you can also disable the ElasticSearch mapping for all moori plugins in the Foundation settings. Then rebuild the ElasticSearch index again!

![ES Disable](images/disable-es-mapping.jpg)

## Server Configuration Errors

### File and Directory Permissions

Manual adjustments or uploads can distort the permissions. This error becomes noticeable when you get a blank page in the storefront or can't upload media. The cache can also be affected. You can correct the permissions with these two simple commands.

```text
// Set all files to 0755 and directories to 0644
chmod -R u+rwX,go+rX,go-w /path/to/shop/main/directory

// Certificate files need 0660
find /path/to/shop/main/directory -name "*.pem" -exec chmod 0660 {} \;
```

### NGINX Proxy Cache

Shopware's built-in cache is based on the sales channel context. The cache is used on category and product pages based on the current language, currency and customer group.

If there are problems with the cache - e.g. if you select a different customer group and the rendered web pages do not adapt, it is most likely due to the server's cache settings.

The NGINX Proxy Cache is a feature of NGINX that allows cached copies of web pages to be stored in order to serve requests faster and reduce the load on the originating web pages. When NGINX acts as a reverse proxy, it can cache content from the source web pages and deliver it directly from the cache for repeated requests. This improves the loading time and reduces the load on the source websites.

#### Deactivation of the proxy cache

There are various options for deactivating the proxy cache in the NGINX configuration, depending on the desired scope:

Global deactivation: In the server configuration (e.g. /etc/nginx/nginx.conf or in a specific server or location block file), you can simply deactivate the cache by removing the relevant instructions or explicitly setting the cache to “off”:

```nginx
proxy_cache off;
```

Disable cache for specific locations: To disable the cache for specific URL paths or web pages only, add the proxy_cache off; statement to the relevant location block:

```nginx
location /path {
    proxy_cache off;
}
```

With these settings, the proxy cache can be deactivated selectively or completely.
