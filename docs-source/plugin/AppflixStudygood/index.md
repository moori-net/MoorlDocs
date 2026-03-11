---
description: {var:description_de_de}
tags:
  - LMS
  - Videokurse
  - E-Learning
  - 
---

# {var:label_de_de}

{var:description_de_de}

![Vorschau](images/preview.png)

---

{file:snippets/docs_demo_plugin.md}

{file:snippets/docs_buy_plugin.md}

{file:snippets/docs_foundation_note.md}

{file:snippets/docs_quickstart.md}

---

## Planung

### Hosting Festlegen

- Streaming - Kopierschutz notwendig: Videos über Vimeo hosten
- Streaming - Kein Kopierschutz nötig: Videos über YouTube
- Videos selbst hosten: Upload über den Medienmanager (Wichtig: Je nach Hoster gibt es Uploadbeschränkungen (teilweise nur wenige MB möglich).)

## Ersteinrichtung

### Videos und Medien einrichten

Die Verwaltung der Medien wird hier eingerichtet: [Eingebettete Medien](../MoorlFoundation/embedded-media.md)

### Kurs anlegen

Über die Hauptnavigation im Admin: `Inhalte` → `Studygood Kurse` → `Hinzufügen`

#### Stammdaten

- Name: Der Name des Kurses
- Beschreibung: Kurze Kursbeschreibung (Die Hauptbeschreibung wird über das Produkt bezogen)
- Tutor (optional): Der Ersteller des Kurses
- Aktiv
- Produkte: Produkte, welche diesen Kurs beinhalten (der Kurs kann in mehreren Produkten zugewiesen werden)
- Eingebettete Medien (optional): Ein Video z.B. kurze Übersicht des Kursinhalts

#### Event

Relevant für Kurse, die z.B. Live oder vor Ort abgehalten werden (via IFrame)

#### Inhalt

Eine Übersicht der Kapitel und Lektionen

#### Metadaten

Grobe Informationen über den Kurs, z.B. Kursdauer, Anzahl an Dokumenten/Downloads

### Kapitel anlegen

Ein strukturierter Kurs besteht aus mehreren Kapiteln, die wiederum die Lektionen beinhalten.

Ein neues Kapitel wird über `Aktueller Kurs` → `Inhalt` → `Kapitel` → `Hinzufügen` angelegt

- Name: Der Name des Kapitels
- Beschreibung (optional): Kurze Beschreibung
- Position: Die Anordnung innerhalb des Kurses
- Medien (optional): Ein Vorschaubild für das Kapitel

### Kapitel bearbeiten

Sobald ein Kapitel angelegt wurde, erscheint ein neuer Eintrag in der Liste. Klicken Sie auf den Namen des Kapitels, um mit der Bearbeitung fortzufahren.

### Lektion anlegen

In der Detailansicht des Kapitels können nun die Lektionen für dieses Kapitel angelegt werden.

Eine neue Lektion wird über `Aktuelles Kapitel` → `Lektionen` → `Hinzufügen` angelegt

- Name: Der Name der Lektion
- Beschreibung (optional): Kurze Beschreibung
- Position: Die Anordnung innerhalb des Kapitels
- Vorschau: Diese Lektion kann kostenlos betrachtet werden
- Eingebettete Medien: Wesentlicher Inhalt der Lektion
- Medien (optional): Ein Vorschaubild für die Lektion

### Lektion bearbeiten

Sobald eine Lektion angelegt wurde, erscheint ein neuer Eintrag in der Liste. Klicken Sie auf den Namen der Lektion, um mit der Bearbeitung fortzufahren.

- Board: Eine Übersicht für Kommentare und Fragen zu der aktuellen Lektion
- Dateien: Zu der Lektion können Downloads und Dokumente zur Verfügung gestellt werden
- Länge: Die Länge der Lektion wird in Sekunden eingetragen
- Bewertung: Erstellung eines Multiple-Choice-Tests zur Selbsteinschätzung
- Punkte: Die Anzahl der Punkte um den Test zu bestehen

### Multiple-Choice-Test anlegen (optional)

#### Fragen

- Inhalt: Die Frage
- Lösung: Eine Erklärung/Lösungsweg, bei Abschluss der Bewertung
- Medien: Ein Bild zur Frage
- Punkte: Die Anzahl der Punkte bei richtiger Antwort

#### Antworten

Sobald die Frage angelegt wurde, kann man die Antworten erstellen, ohne die Seite zu verlassen. Klicken Sie dazu auf das Kontextmenü (...) in der Liste um die erstellte Frage in einem Modal-Fenster zu öffnen.

Hier erscheint nun eine weitere Liste, wo die Antworten für die Frage angelegt werden können.

- Ist wahr: Diese Antwort ist richtig
- Inhalt: Die Antwort
- Medien: Ein Bild zur Antwort

### Kurs fertigstellen

Wiederholen Sie die Schritte, bis alle Kapitel und Lektionen vollständig sind. Im Titel ist ein Pfad hinterlegt, so springen Sie schnell wieder in die Lektion oder in den Kurs.

### Produktzuordnung

Gehen Sie in das Produkt, in dem der Kurs zugewiesen wurde. Dort auf den Reiter `Studygood`. Hier können/müssen folgende Angaben gemacht werden.

#### Stammdaten

- Standardseite: Die Produktseite bleibt wie im Standard vorgegeben, die Kurse und Lektionen werden in einem Reiter auf der Produktdetailseite aufgeführt.
- Kursdauer: Die Gültigkeit eines Kurses (in Tagen)
- Eventdatum (optional): Zusätzliche Angabe für ein Live-Event
- Eingebettete Medien (optional): Ein Video z.B. kurze Übersicht der Kursinhalte auf Produktebene

#### Metadaten (wichtig)

Klicken Sie bei den Metadaten auf den Button `Aktualisieren`, so werden die Daten aller Kurse für dieses Produkt zusammengefasst.

### Abschluss

Der Kurs ist nun erstellt.

## Alle Daten im Überblick

Über die Hauptnavigation im Admin: `Einstellungen` → `Erweiterungen` sind alle Daten des Plugins zugänglich:

- `Studygood Boards`
- `Studygood Kapitel`
- `Studygood Lektionen`
- `Studygood Abos`
- `Studygood Test Fragen`
- `Studygood Test Antworten`
- `Studygood Tutoren`

## Erwerb eines Kurses

Der Kunde legt einen Kurs in den Warenkorb und bestellt diesen

Im Kundenmenü `Meine Abos` sind alle Kurse inklusive Kursfortschritt gelistet. Dort steht auch, wann der Zugang zum Kurs abläuft.

Sobald der Zahlungseingang bestätigt ist, hat der Kunde Zugang zum Kursinhalt.

Es können im Admin auch manuell Abos angelegt werden.

1. Über das Produkt: `Aktuelles Produkt` → `Studygood` → `Abos`
2. Über den Kunden: `Aktueller Kunde` → `Abos`
3. Global: `Einstellungen` → `Erweiterungen` → `Studygood Abos`
