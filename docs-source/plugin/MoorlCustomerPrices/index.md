---
description: Dieses einfache und benutzerfreundliche Plugin ermöglicht es, Produktpreise gezielt für unterschiedliche Kunden anzupassen - So lassen sich flexible Preisgestaltungen realisieren.
tags:
  - Shopware 6.7
---

# Kundenspezifische Produktpreise

Dieses einfache und benutzerfreundliche Plugin ermöglicht es, Produktpreise gezielt für unterschiedliche Kunden anzupassen - So lassen sich flexible Preisgestaltungen realisieren.

![Vorschau](images/admin-4.png)

---

## Plugin erwerben

Dieses Plugin kann im offiziellen **Shopware Community Store** erworben werden.

- [Shopware Community Store](https://store.shopware.com/de/search?search=MoorlCustomerPrices)


**Wichtiger Hinweis:** Sie benötigen das Foundation Plugin, welches Ihnen kostenlos zur Verfügung steht: [moori Foundation](../MoorlFoundation/index.md)


---

## Ersteinrichtung

### Plugin Konfiguration

![Plugin Konfiguration](images/admin-8.png)

1. Berechnungspriorität: Sofern andere Plugins verwendet werden, die an der Preisberechnung beteiligt sind, kann man hier die Priorät einstellen - Je höher die Priorität, desto eher wird der Preis durch dieses Plugin berechnet.
2. Berechnung bei Treffer hier abbrechen: Sofern andere Plugins verwendet werden, die an der Preisberechnung beteiligt sind, wird hier festgelegt, ob die Berechnung fortgeführt wird. Zum Beispiel haben Festpreise oft eine höhere Priorität, danach sollen keine weiteren Berechnungen am Preis durchgeführt werden.

## Kundenspezifischen Preis festlegen

### Aus der Sicht des Produktes

Öffnen Sie ein Produkt im Admin und klicken Sie auf den Reiter `Kundenspezifische Produktpreise`. Dort kann ein neuer Eintrag angelegt werden, indem ein Kunde ausgewählt und ein Preis festgelegt wird.

![Aus der Sicht des Produktes](images/admin-2.png)

### Aus der Sicht des Kunden

Öffnen Sie einen Kunden im Admin und klicken Sie auf den Reiter `Kundenspezifische Produktpreise`. Dort kann ein neuer Eintrag angelegt werden, indem ein Produkt ausgewählt und ein Preis festgelegt wird.

![Aus der Sicht des Kunden](images/admin-1.png)

### Allgemeine Übersicht

Über die Hauptnavigation im Admin: `Marketing` → `Kundenspezifische Produktpreise` gibt es eine Übersicht für alle angelegten Einträge. Hier kann man neue Einträge anlegen, oder bestehende Einträge löschen.

![Allgemeine Übersicht](images/admin-5.png)

### Eingabemaske

Neben der Zuweisung zum Produkt, dem Kunden und dem Preis, kann man auch ein Zeitfenster bestimmen, an dem der festgelegte Preis gültig ist. Neben dem Zeitfenster kann man auch eine Regel verwenden.

![Eingabemaske: Allgemein](images/admin-3.png)

Bei den Preiseinstellungen wird eine Steuerrate benötigt, um den Preis richtig in Brutto und auch in Netto darzustellen. Außerdem kann man den alten Basispreis oder den alten Streichpreis als neuen Streichpreis verwenden.

![Eingabemaske: Preis](images/admin-4.png)