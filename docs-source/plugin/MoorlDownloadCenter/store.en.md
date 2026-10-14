**Important note:** You need the Foundation Plugin, which is available free of charge: [Foundation](https://store.shopware.com/en/search?search=MoorlFoundation)


## Deliver digital content professionally

Use the Download Center to manage and sell digital content directly in Shopware. Provide manuals, product catalogues, software, updates, media, licence keys, or extensive download packages. For each item, you decide whether it is publicly visible, available only after purchase, or accessible only to selected customers and customer groups.

The plugin combines product sales, file management, and the customer account in one continuous process. Customers find all authorised content in their account under **My purchases**, where they can access files, external links, and codes in one place.

## Public downloads and protected ESD products

A Download Center can contain public and private content:

- **Public downloads** are suitable for manuals, data sheets, catalogues, and other information that should already be available on the product detail page.
- **Private downloads** are only visible to authorised customers. They are suitable for software, paid documents, member content, training materials, or individual files.
- **ESD products** link a product to a Download Center. A personal download subscription is automatically created after purchase.
- **Direct assignments** make content available to individual customers or customer groups without requiring an order.

You can combine public and private content in one product. For example, offer a freely available product manual together with an installation package protected until after purchase.

## Controlled activation and subscriptions

For private ESD products, the plugin creates an individual download subscription for every purchased item. Access depends on the product price and payment status:

- Free digital products can be activated immediately.
- Paid products become available once the order has been paid.
- Access can be activated or deactivated manually in the admin.
- A duration can limit access until a fixed end date.
- Customers can view the status, validity, and available content in their account.

This makes the Download Center suitable for one-off digital purchases, time-limited access, licence models, and supplementary content for physical products.

## Files, external links, and licence keys

A Download Center can combine different types of digital content:

- **Files** from a configured file system
- **External links**, for example to portals or downloads provided by third parties
- **Serial numbers and licence keys** for software products
- **Volume licence keys** that can be sold multiple times
- **Download codes** that customers can use to activate personal content

Files can be organised in nested directories. Use a `metadata.xml` file to hide individual files and add descriptions or custom icons. This keeps even extensive download areas easy to navigate.

## Flexible storage locations

Store content where it best fits your project. The Download Center supports, among others:

- local file system
- FTP and SSH
- Amazon S3
- WebDAV
- Nextcloud

File system clients allow you to manage files outside the Shopware server. This is particularly useful for large packages, existing infrastructure, or content used by multiple systems.

## Customer account, CMS, and product detail page

Customers receive a clear, central point of access to their content:

- A dedicated account module bundles all personal download subscriptions.
- Public downloads can be displayed on product detail pages.
- Download Centers can be embedded as CMS elements in Shopping Experiences.
- Authorised customers can download files, open external links, and view assigned codes.
- Guest customers receive a personal deeplink to their download subscriptions.

The deeplink is generated from the configured base URL and a personal token. This allows guest customers to access purchased content without a regular customer login.

## Automated notifications with Flow Builder

The plugin provides dedicated Flow Builder events for download subscriptions. Use them to trigger emails and further automated processes based on a subscription's status:

- **EsdCreated**: A download subscription has been created.
- **EsdActivated**: A subscription has been activated.
- **EsdDeactivated**: A subscription has been deactivated.

The supplied email template contains customer data, the Download Center name, and the personal deeplink. Use it in Flow Builder as a starting point for your own notifications, for example for new downloads, successful payments, or manual activations.

## Typical use cases

The Download Center is suitable for, among other things:

- software, extensions, and updates
- licence keys, serial numbers, and activation codes
- e-books, whitepapers, templates, and training materials
- product catalogues, data sheets, and manuals
- content for retailers, customers, or member groups
- downloads with time-limited access
- media libraries with public and protected areas

## Feature overview

- public and private Download Centers
- product assignments for digital products and ESD sales
- direct access for customers and customer groups
- automatic download subscriptions after purchase
- payment-status-based and manual activation
- time-limited access
- files, external links, codes, and licence keys
- nested directories and file metadata
- local and external file systems
- CMS element and product detail page integration
- customer account for personal downloads and subscriptions
- deeplinks for guest customers
- Flow Builder events and email templates for notifications
