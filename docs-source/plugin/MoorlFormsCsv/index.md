---
description: Speichert Daten aus dem Flow-Builder oder Formular Baukasten in einer vorhandenen CSV-Datei.
tags:
- Shopware 6 Plugin
- Flow-Builder
- CSV Schreiben
- Datenerfassung
---

# Flow Builder Aktion | CSV Schreiben

Diese Erweiterung ist mit [Formular Baukasten 2](https://docs.moori.net/plugin/MoorlForms/) kompatibel

## Installation

!!! note

      Falls du Probleme mit dem Plugin hast, bitte beachte folgende [Hinweise](https://docs.moori.net/plugin/) im FAQ Bereich.

1. Installiere [Foundation](https://docs.moori.net/plugin/MoorlFoundation/)
2. Installiere diese Erweiterung im Plugin Manager

## Einrichtung

### Freigabe der Dateierweiterung CSV

Prüfe bei einem abgelehnten Upload die Einstellung „Zusätzliche Upload Erweiterungen“ im Foundation Plugin. Dessen aktueller Konfigurationsdefault enthält bereits `zip,rar,psd,docx,csv`; vorhandene Installationen können abweichende Werte gespeichert haben. Ergänze `csv`, falls die Erweiterung dort fehlt.

### Erstelle eine CSV mit Kopfzeile

Bevor du eine CSV Datei verwenden kannst, musst du diese vorbereiten. Wichtig ist hierbei, dass du deine Kopfzeile und eine darauffolgende leere Zeile erstellst. Die Zeichenkodierung ist in UTF-8.

Ein Beispiel für das Kontaktformular:

```text
email;first_name;last_name;subject;comment;phone_number

```

### Datei in den Medien-Manager hochladen

Nachdem du die Datei erstellt hast, kannst du diese in den Shopware Medien-Manager hochladen.

### Eine neue Aktion im Flow-Builder erstellen

Gehe in einen Flow deiner Wahl und erstelle eine neue Aktion. Im folgenden Beispiel wird eine Aktion für das Kontaktformular erstellt.

Im Auswahlfeld "CSV Datei" kannst du nun alle CSV Dateien aus dem Medien-Manager sehen. Wähle die gewünschte Datei aus.

Wenn sich die CSV-Datei nicht einlesen lässt, prüfe nochmals [die Kopfzeile und Leerzeile](#erstelle-eine-csv-mit-kopfzeile).

Weise nun die verfügbaren Felder zu. Diese Felder sind Twig-Variablen, du kannst auch feste Werte oder [Twig Funktionen](https://twig.symfony.com/doc/3.x/functions/index.html) verwenden!

Du kannst die Flow-Builder Aktion nun speichern.

## Formular Baukasten anbinden

Öffne unter **Inhalte → Formular Baukasten** dein Formular und dessen Formulareinstellungen. Aktiviere **In CSV Datei speichern** (`csv-form`) und öffne den Reiter **CSV**. Wähle eine vorhandene CSV-Mediendatei und ordne die Formularwerte in der Mappingtabelle zu. Die angebotenen Platzhalter verwenden den technischen Feldnamen, beispielsweise `{{ email.value }}`. Speichere das Formular. Die Flow-Aktion heißt technisch `action.write.csv` und benötigt ein Ereignis mit `MailAware`.

## Format, Speicherung und Grenzen

- Administration-Defaults: Separator `;`, Enclosure `"`, Escape ein Backslash. Das Escape-Feld wird gespeichert, vom PHP-Service aber nicht ausgewertet; die CSV-Funktionen verwenden ihren PHP-Standard.
- Zuordnungen werden in ihrer Tabellenreihenfolge als Spalten geschrieben. Nicht belegte Zuordnungen erzeugen leere Zellen. Eine neue Kopfzeile wird nicht angelegt.
- Für das Einlesen der Spalten muss die letzte nach der Kopfzeile gelesene Zeile leer sein. Halte deshalb eine zusätzliche leere Abschlusszeile vor; ein einzelner abschließender Zeilenumbruch reicht beim geprüften PHP-Verhalten nicht aus. Beim erneuten Einlesen einer befüllten Datei kann diese Voraussetzung erneut relevant werden.
- Der Service hängt Zeilen direkt an `public/<Medienpfad>` an. Er benötigt eine lokal vorhandene, beschreibbare Datei. Eine entfernte Medien-URL bzw. Object Storage wird nicht heruntergeladen. Medienmetadaten werden nach dem Schreiben nicht aktualisiert.
- Die Vorschau lädt den vollständigen Dateiinhalt. Download und Medienmanagerlinks folgen der Shopware-Medienkonfiguration; verwende für Dokumentationsbeispiele keine echten Kundendaten.
- Keine eigene Dateisperre, Zeichensatzkonvertierung oder automatische Wiederholung. Datei- und Twig-Fehler werden im Plugin nicht abgefangen. Der zuerst initialisierte CSV-Pfad bleibt im Service gespeichert; unterschiedliche Dateien in einem Service-Lebenszyklus erfordern eine gesonderte Prüfung.

Die CSV-spezifische Administration wurde für diesen Dokumentationsabgleich nicht visuell verifiziert.

## Test

Zum Testen wird das Kontaktformular zweimal ausgefüllt und abgeschickt.

In der Konfiguration der Flow-Builder Aktion kannst du eine Vorschau der CSV Datei öffnen, um sicherzustellen, dass die Formulardaten gespeichert wurden.

Um die CSV Datei auszuwerten, kannst du diese im Medien-Manager oder direkt in der Flow-Builder Aktion herunterladen und mit z.B. Microsoft Office Excel oder OpenOffice Calc öffnen. Bitte denke daran die Datei in der UTF-8 Kodierung einzulesen!
