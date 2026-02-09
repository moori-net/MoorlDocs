---
description: Dieses Plugin ermöglicht es, Hersteller und Marken stärker hervorzuheben. Dazu gibt es viele Möglichkeiten, z.B. die Erstellung eigener CMS-Seiten mit Produkten und SEO.
tags:
  - Hersteller
  - CMS
  - Shopware 6.7
---

# Erweiterte Hersteller

Dieses Plugin ermöglicht es, Hersteller und Marken stärker hervorzuheben. Dazu gibt es viele Möglichkeiten, z.B. die Erstellung eigener CMS-Seiten mit Produkten und SEO.

![Vorschau](images/storefront-manufacturer-detail.png)

---

## Plugin Demo

Zu diesem Plugin steht eine Storefront-Demo zum Testen bereit. Unter folgenden Link kann das Plugin getestet werden:

- [https://demo-sw67.moori.net/MoorlManufacturer](https://demo-sw67.moori.net/MoorlManufacturer)


## Plugin erwerben

Das Plugin kann in den folgenden Stores erworben werden. Wenn Sie bereits einen Shopware-Account besitzen, nutzen Sie bitte **immer zuerst** den Link zum **Shopware Community Store**, da es bei alternativen Stores zu Problemen mit der Lizenzierung kommen kann. Ist ein Plugin **nicht** im Shopware Community Store verfügbar, wird es exklusiv in einem der alternativen Stores angeboten.

- [Shopware Community Store](https://store.shopware.com/de/search?search=MoorlManufacturer) *(empfohlen)*
- [moori Plugin Store](https://moori-plugin-store.com/MoorlManufacturer)
- [Shopelfen Store](https://www.shopelfen.de/) *(im Aufbau)*


**Wichtiger Hinweis:** Sie benötigen das Foundation Plugin, welches Ihnen kostenlos zur Verfügung steht: [moori Foundation](../MoorlFoundation/index.md)


## Quickstart

Für dieses Plugin steht ein **Demo-Paket** zum Testen bereit.

Gehen Sie zu **„Einstellungen → [Demo Assistent](../MoorlFoundation/demo-assistant.md)“** und wählen Sie dort **„MoorlManufacturer“** aus.

**Hinweis:** In einigen Fällen werden neue Kategorien und Seiten zu Ihrem Shop hinzugefügt. Bitte beachten Sie, dass die Demo-Daten ausschließlich zu Testzwecken dienen. Die darin enthaltenen Bilder können urheberrechtlich geschützt sein und dürfen nicht der Öffentlichkeit zugänglich gemacht werden.


---

## Ersteinrichtung

### Plugin Konfiguration

![Plugin Konfiguration](images/admin-1.png)

1. Hauptseite mit Herstellerübersicht: Die Kategorie auf der alle Hersteller gelistet sind
2. Erweiterte Suche: [Foundation | Erweiterte Suche](../MoorlFoundation/advanced-search.md)

### Allgemeine Übersicht

Über die Hauptnavigation im Admin: `Kataloge` → `Erweiterte Hersteller` gibt es eine Übersicht für alle angelegten Einträge. Hier kann man neue Einträge anlegen, oder bestehende Einträge duplizieren oder löschen.

![Allgemeine Übersicht](images/admin-2.png)

## Neuen Hersteller hinzufügen

Dieses Plugin basiert auf die Hersteller, die es bereits in Shopware gibt, diese können optional erweitert werden. Um einen erweiterten Hersteller zu erstellen, muss mindestens ein Hersteller in Shopware angelegt sein.

Legen Sie zuerst einen Hersteller in Shopware an: `Kataloge` → `Hersteller` -> `Hersteller hinzufügen`.

Anschließend können Sie einen neuen erweiterten Hersteller erstellen: `Kataloge` → `Erweiterte Hersteller` -> `hinzufügen`.

### Eingabemaske

![Allgemeine und Sichtbarkeit](images/admin-3.png)

Allgemein:

- Produkt Hersteller: Der Hersteller, der durch das Plugin erweitert wird
- Name: Name des Herstellers
- Teaser/Kurzbeschreibung
- Beschreibung im HTML Format
- Schlüsselwörter

Sichtbarkeit:

- Aktiv
- Kategorien: Produktlisten im Storefront, in denen der Hersteller vertreten ist. Man kann durch einen Link von der Herstellerseite direkt in die Kategorie springen und der Hersteller ist bereits im Filter ausgewählt.
- Tags: Erscheinen im CMS-Metabereich der Herstellerseite. Hersteller können auch nach Tags gefiltert werden.

![Medien](images/admin-4.png)

Medien:

- Avatar: Das Herstellerlogo kann durch dieses Bild überschrieben werden
- Banner: Ein Banner für die Herstellerseite im Storefront

Kontakt: Allgemeine Kontaktmöglichkeiten

![Adresse](images/admin-7.png)

Adresse: Adresse und Geokoordinaten des Herstellers

SEO: Meta Angaben zum Hersteller

CMS Seite: Zuweisung und Konfiguration der CMS Seite des Herstellers

## CMS Seiten

![CMS Seiten](images/admin-8.png)

Mit der Installation des Plugins werden bereits zwei CMS Seiten erstellt. Eine Seite für die Übersicht aller Hersteller und eine für die Herstellerseite. Um die CMS Seiten anzupassen, können die bestehenden Seiten dupliziert und bearbeitet werden.

### Erweiterte Hersteller (Liste)

![Erweiterte Hersteller (Liste)](images/admin-6.png)

### Erweiterte Hersteller (Standard)

![Erweiterte Hersteller (Standard)](images/admin-5.png)
