---
description: This plugin offers seamless and independent integration with your bank's EBICS interface. Automatic reconciliation of SEPA direct debits and prepayments.
tags:
  - EBICS
  - Banking software
  - SEPA
  - Direct debit
  - Pay in advance
  - Invoice
---

# EBICS 3.0 BankConnect

This plugin offers seamless and independent integration with your bank's EBICS interface. Automatic reconciliation of SEPA direct debits and prepayments.

![Preview](images/preview.png)

---

## Purchase the Plugin

The plugin can be purchased from the following stores. If you already have a Shopware account, please **always use** the link to the **Shopware Community Store** first, as alternative stores may cause licensing issues. If a plugin is **not** available in the Shopware Community Store, it is offered exclusively in one of the alternative stores.

- [Shopware Community Store](https://store.shopware.com/en/search?search=MoorlEbics) *(recommended)*
- [moori Plugin Store](https://moori-plugin-store.com/MoorlEbics)
- [Shopelfen Store](https://www.shopelfen.de/) *(under construction)*


**Important note:** You need the Foundation Plugin, which is available free of charge: [moori Foundation](../MoorlFoundation/index.md)


---

## Initial Setup

### Bank Setup

1. **Open the Bank Settings**  
   Navigate to **Settings → EBICS Banks**.

2. **Set a Keyring Password**  
   Before you configure your bank, you must define a global password to encrypt your EBICS key files:
    - Click **Create or Change Keyring Password** in the top-right corner
    - Choose a **six-digit password**

3. **Add a Bank**
    - Click **Add** in the top-right corner
    - Fill in all required fields (Customer ID, User/Participant ID, EBICS server URL, etc.)

4. **Initialize the EBICS Connection**  
   The initialization process consists of several steps:

    1. **Create Keyring File**
        - A secure keyring file is generated and encrypted with your password.

    2. **Send INI & HIA Requests**
        - Your public keys are sent to the bank.
        - **If you receive an error here:** Check that your EBICS access has been activated by the bank and that your Customer ID & User ID are correct.

    3. **Generate INI Letter**
        - The plugin creates a PDF containing the key fingerprints.
        - This document must be signed by an authorized person and sent to the bank.
        - **Note:** For test accounts, this step is often not required.

    4. **Send HPB Request**
        - The bank’s public keys are retrieved and stored in the keyring file.
        - Once this succeeds, the connection to the bank is fully active.

> 💡 **Tip:** The plugin always displays the last error message returned by the bank.  
> When no error message is shown anymore, your connection has been successfully set up.

5. **Optional Fields**
    - Enter your **creditor identifier** if you intend to use SEPA direct debits
    - Assign all relevant payment methods (e.g. Prepayment, Invoice, SEPA Direct Debit)

---

### Plugin Settings

- Explicitly assign payment methods to their intended purpose.
- Make sure **no payment method is assigned twice**.

---

## Technical Notes

The plugin uses Shopware’s standard order statuses:

- `open`
- `authorized`
- `paid`
- `refunded`
- `chargeback`
- `failed`

> ❗ Custom statuses are **not supported**.

Additional notes:

- Available EBICS order types depend on your bank.  
  If an order type is not supported, you will receive an appropriate error message.
- **Direct release** for payouts (refunds) is only possible with a **single signature**.  
  Four-eyes approval requires an external EBICS client (e.g. SFirm).
- **SEPA direct debit mandates** can only be created if a valid creditor identifier is stored in the bank settings.  
  Otherwise, such orders will be aborted.
- **Logs:** All processes are logged under `var/logs/moorl_ebics_*.log`.