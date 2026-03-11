---
description: Das E-Learning Management System für Videokurse. Flexible Kurs-Laufzeit, Lernmaterialien zum Download, Frage-/Antowortforum u.v.m. Auch interne Unternehmensschulungen sind möglich.
tags:
  - LMS
  - Videokurse
  - E-Learning
  - Medien
  - ESD
---

# Studygood | Dein Lernmanagement System

Das E-Learning Management System für Videokurse. Flexible Kurs-Laufzeit, Lernmaterialien zum Download, Frage-/Antowortforum u.v.m. Auch interne Unternehmensschulungen sind möglich.

![Vorschau](images/preview.png)

---

## Plugin Demo

Zu diesem Plugin steht eine Storefront-Demo zum Testen bereit. Unter folgenden Link kann das Plugin getestet werden:

- [https://demo-sw67.moori.net/AppflixStudygood](https://demo-sw67.moori.net/AppflixStudygood)


## Plugin erwerben

Dieses Plugin kann im offiziellen **Shopware Community Store** erworben werden.

- [Shopware Community Store](https://store.shopware.com/de/search?search=AppflixStudygood)


**Wichtiger Hinweis:** Sie benötigen das Foundation Plugin, welches Ihnen kostenlos zur Verfügung steht: [moori Foundation](../MoorlFoundation/index.md)


## Quickstart

Für dieses Plugin steht ein **Demo-Paket** zum Testen bereit.

Gehen Sie zu `Einstellungen` → [`Demo Assistent`](../MoorlFoundation/demo-assistant.md) und wählen Sie dort `AppflixStudygood` aus.

**Hinweis:** In einigen Fällen werden neue Kategorien und Seiten zu Ihrem Shop hinzugefügt. Bitte beachten Sie, dass die Demo-Daten ausschließlich zu Testzwecken dienen. Die darin enthaltenen Bilder können urheberrechtlich geschützt sein und dürfen nicht der Öffentlichkeit zugänglich gemacht werden.


---

## Planung

### Hosting festlegen

- **Streaming – Kopierschutz notwendig:** Videos über Vimeo hosten
- **Streaming – kein Kopierschutz nötig:** Videos über YouTube hosten
- **Videos selbst hosten:** Upload über den Medienmanager. Wichtig: Je nach Hoster gibt es Upload-Beschränkungen, sodass teilweise nur wenige MB möglich sind.

## Ersteinrichtung

### Videos und Medien einrichten

Die Verwaltung der Medien wird hier eingerichtet: [Eingebettete Medien](../MoorlFoundation/embedded-media.md)

### Kurs anlegen

Über die Hauptnavigation im Admin: `Inhalte` → `Studygood Kurse` → `Hinzufügen`

#### Stammdaten

- **Name:** Der Name des Kurses
- **Beschreibung:** Kurze Kursbeschreibung. Die Hauptbeschreibung wird über das Produkt bezogen.
- **Tutor (optional):** Der Ersteller des Kurses
- **Aktiv**
- **Produkte:** Produkte, die diesen Kurs beinhalten. Der Kurs kann mehreren Produkten zugewiesen werden.
- **Eingebettete Medien (optional):** Ein Video, z. B. eine kurze Übersicht über den Kursinhalt

#### Event

Relevant für Kurse, die z. B. live oder vor Ort stattfinden (via IFrame).

#### Inhalt

Eine Übersicht der Kapitel und Lektionen.

#### Metadaten

Allgemeine Informationen über den Kurs, z. B. Kursdauer oder Anzahl an Dokumenten bzw. Downloads.

### Kapitel anlegen

Ein strukturierter Kurs besteht aus mehreren Kapiteln, die wiederum die Lektionen enthalten.

Ein neues Kapitel wird über `Aktueller Kurs` → `Inhalt` → `Kapitel` → `Hinzufügen` angelegt.

- **Name:** Der Name des Kapitels
- **Beschreibung (optional):** Kurze Beschreibung
- **Position:** Die Anordnung innerhalb des Kurses
- **Medien (optional):** Ein Vorschaubild für das Kapitel

### Kapitel bearbeiten

Sobald ein Kapitel angelegt wurde, erscheint ein neuer Eintrag in der Liste. Klicken Sie auf den Namen des Kapitels, um mit der Bearbeitung fortzufahren.

### Lektion anlegen

In der Detailansicht des Kapitels können nun die Lektionen für dieses Kapitel angelegt werden.

Eine neue Lektion wird über `Aktuelles Kapitel` → `Lektionen` → `Hinzufügen` angelegt.

- **Name:** Der Name der Lektion
- **Beschreibung (optional):** Kurze Beschreibung
- **Position:** Die Anordnung innerhalb des Kapitels
- **Vorschau:** Diese Lektion kann kostenlos betrachtet werden.
- **Eingebettete Medien:** Der wesentliche Inhalt der Lektion
- **Medien (optional):** Ein Vorschaubild für die Lektion

### Lektion bearbeiten

Sobald eine Lektion angelegt wurde, erscheint ein neuer Eintrag in der Liste. Klicken Sie auf den Namen der Lektion, um mit der Bearbeitung fortzufahren.

- **Board:** Eine Übersicht für Kommentare und Fragen zur aktuellen Lektion
- **Dateien:** Zu der Lektion können Downloads und Dokumente zur Verfügung gestellt werden.
- **Länge:** Die Länge der Lektion wird in Sekunden eingetragen.
- **Bewertung:** Erstellung eines Multiple-Choice-Tests zur Selbsteinschätzung
- **Punkte:** Die Anzahl der Punkte, die zum Bestehen des Tests erforderlich sind

### Multiple-Choice-Test anlegen (optional)

#### Fragen

- **Inhalt:** Die Frage
- **Lösung:** Eine Erklärung bzw. der Lösungsweg nach Abschluss der Bewertung
- **Medien:** Ein Bild zur Frage
- **Punkte:** Die Anzahl der Punkte bei richtiger Antwort

#### Antworten

Sobald die Frage angelegt wurde, können die Antworten erstellt werden, ohne die Seite zu verlassen. Klicken Sie dazu auf das Kontextmenü (`...`) in der Liste, um die erstellte Frage in einem Modal-Fenster zu öffnen.

Dort erscheint eine weitere Liste, in der die Antworten für die Frage angelegt werden können.

- **Ist wahr:** Diese Antwort ist richtig.
- **Inhalt:** Die Antwort
- **Medien:** Ein Bild zur Antwort

### Kurs fertigstellen

Wiederholen Sie die Schritte, bis alle Kapitel und Lektionen vollständig angelegt sind. Im Titel ist ein Pfad hinterlegt, sodass Sie schnell wieder zur Lektion oder zum Kurs springen können.

### Produktzuordnung

Gehen Sie in das Produkt, dem der Kurs zugewiesen wurde. Wechseln Sie dort auf den Reiter `Studygood`. Hier können bzw. müssen folgende Angaben gemacht werden.

#### Stammdaten

- **Standardseite:** Die Produktseite bleibt wie im Standard vorgesehen. Die Kurse und Lektionen werden in einem Reiter auf der Produktdetailseite aufgeführt.
- **Kursdauer:** Die Gültigkeit eines Kurses in Tagen
- **Eventdatum (optional):** Zusätzliche Angabe für ein Live-Event
- **Eingebettete Medien (optional):** Ein Video, z. B. eine kurze Übersicht der Kursinhalte auf Produktebene

#### Metadaten (wichtig)

Klicken Sie bei den Metadaten auf den Button `Aktualisieren`. Dadurch werden die Daten aller Kurse für dieses Produkt zusammengefasst.

### Abschluss

Der Kurs ist nun erstellt.

## Alle Daten im Überblick

Über die Hauptnavigation im Admin unter `Einstellungen` → `Erweiterungen` sind alle Daten des Plugins zugänglich:

- `Studygood Boards`
- `Studygood Kapitel`
- `Studygood Lektionen`
- `Studygood Abos`
- `Studygood Test Fragen`
- `Studygood Test Antworten`
- `Studygood Tutoren`

## Erwerb eines Kurses

Der Kunde legt einen Kurs in den Warenkorb und bestellt ihn.

Im Kundenmenü `Meine Abos` sind alle Kurse inklusive Kursfortschritt aufgelistet. Dort ist auch ersichtlich, wann der Zugang zum Kurs abläuft.

Sobald der Zahlungseingang bestätigt ist, hat der Kunde Zugriff auf den Kursinhalt.

Abos können im Admin auch manuell angelegt werden:

1. Über das Produkt: `Aktuelles Produkt` → `Studygood` → `Abos`
2. Über den Kunden: `Aktueller Kunde` → `Abos`
3. Global: `Einstellungen` → `Erweiterungen` → `Studygood Abos`
