---
description: Stores data from Flow Builder or Form Builder 2 in an existing CSV file.
tags:
- Shopware 6 Plugin
- Flow Builder
- CSV writing
- Data entry
---

# Flow Builder Action | Write CSV

This extension is compatible with [Form Builder 2](https://docs.moori.net/en/plugin/MoorlForms/)

## Installation

!!! note

      If you have problems with the plugin, please note the following [hints](https://docs.moori.net/en/plugin/) in the FAQ section.

1. install [Foundation](https://docs.moori.net/en/plugin/MoorlFoundation/)
2. install this extension in the Plugin Manager

## Setup

### Enable the CSV file extension

If an upload is rejected, check “Additional upload extensions” in the Foundation plugin settings. Its current configuration default already contains `zip,rar,psd,docx,csv`; existing installations may have saved different values. Add `csv` if it is missing.

### Create a CSV with header line

Before you can use a CSV file, you need to prepare it. It is important that you create your header line and a subsequent empty line. The character encoding is in UTF-8.

An example for the contact form:

```text
email;first_name;last_name;subject;comment;phone_number

```

### Upload the file to the media manager

Once you have created the file, you can upload it to the Shopware Media Manager.

### Create a new action in the flow builder

Go to a flow of your choice and create a new action. In the following example, an action is created for the contact form.

You can now see all CSV files from the Media Manager in the "CSV file" selection field. Select the desired file.

If the CSV file cannot be read, check [this step](#create-a-csv-with-header-line) again.

Now assign the available fields. These fields are Twig variables, you can also use fixed values or [Twig functions](https://twig.symfony.com/doc/3.x/functions/index.html)!

You can now save the Flow-Builder action.

## Connect Form Builder

Open your form under **Content → Form Builder** and open its form settings. Enable **Save to CSV file** (`csv-form`) and open the **CSV** tab. Select an existing CSV media file and map the form values in the mapping table. Suggested placeholders use the technical field name, for example `{{ email.value }}`. Save the form. The technical Flow action is `action.write.csv`; it requires an event implementing `MailAware`.

## Format, storage and limitations

- Administration defaults: separator `;`, enclosure `"`, and a backslash for escape. The escape field is saved but is not passed to the PHP CSV functions; they use their PHP default.
- Mapping rows are written in table order. Unassigned mappings produce empty cells. The plugin does not create a header.
- When reading columns, the last line read after the header must be empty. Keep an additional empty final line; a single final line break is insufficient in the PHP behavior checked here. This requirement can matter again when reloading columns from a populated file.
- Rows are appended directly to `public/<media path>`. The file must exist locally and be writable. The service does not download remote media URLs or object storage files and does not update media metadata after writing.
- Preview loads the entire file. Download and media manager links follow your Shopware media configuration; use no real customer data for documentation examples.
- No plugin-level file lock, encoding conversion or automatic retry. File and Twig errors are not caught by this plugin. The first initialized CSV path remains stored in the service; different files in one service lifetime require separate verification.

The CSV-specific administration was not visually verified for this documentation review.

## Test

For testing purposes, the contact form is filled out and sent twice.

In the configuration of the Flow Builder action, you can open a preview of the CSV file to ensure that the form data has been saved.

To analyse the CSV file, you can download it in the Media Manager or directly in the Flow Builder action and open it with e.g. Microsoft Office Excel or OpenOffice Calc. Please remember to read the file in UTF-8 encoding!
