# MoorlTicketVendor — Store Review

## 1. Foundation dependency

**Developer note:** MoorlFoundation is required and is installed and updated through the Shopware Store. Composer automatically installs the separate libraries needed to generate PDF tickets and QR codes.

We intentionally omit Foundation from Composer's dependencies: in our experience, adding it switches the plugin to “managed by Composer” and causes problems with Store updates.
