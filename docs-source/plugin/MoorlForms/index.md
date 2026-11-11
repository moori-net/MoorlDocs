---
description: Der Formular Baukasten ermöglicht es Kinderleicht komplexe Formulare mit eigenständigen Aufgabenbereichen zu erstellen. Es ist modular aufgebaut und flexibel einsetzbar.
tags:
- Shopware 6 Plugin
- Formulare erstellen
- Datei-Upload
- B2B
- E-Mail senden
---

# Formular Baukasten 2 | Basis Version

Der Formular Baukasten ermöglicht es Kinderleicht komplexe Formulare mit eigenständigen Aufgabenbereichen zu erstellen. Es ist modular aufgebaut und flexibel einsetzbar.

![Vorschau](images/admin-form-general.png)

---

## Plugin erwerben

Dieses Plugin kann im offiziellen **Shopware Community Store** erworben werden.

- [Shopware Community Store](https://store.shopware.com/de/search?search=MoorlForms)


**Wichtiger Hinweis:** Du benötigst das kostenlose [moori Foundation Plugin](https://docs.moori.net/plugin/MoorlFoundation/).

---

## Eigene Formulare für Shopware 6

- Du möchtest eigene Formulare in Shopware erstellen?
- Du hast keine Shopware Professional Subscription, möchtest aber nicht auf dieses essenzielle Feature verzichten?
- Die Möglichkeiten des Formular Baukastens von Shopware Professional reichen nicht aus?
- Du baust komplexe Formulare und suchst nach einer guten Basis für deine individuellen Anpassungen?

Solltest du eine dieser Fragen mit "Ja" beantworten können, dann bist du hier jedenfalls nicht auf dem Holzweg!

## Beispiel Formulare zum Download

- [Einfaches Kontaktformular](examples/simple-contact-form.json)
- [Entity Mapping Formular](examples/entity-mapping-form.json)
- [Responsives Formular](examples/responsive-form.json)
- [Alle Features](examples/all-features.json)

Weitere Beispiele findest du in der jeweiligen Dokumentation der Add-Ons!

## Add-Ons

Dieses Plugin wurde in seiner Basis Version um einige Funktionen gekürzt, damit es zu einem
erschwinglichen Preis angeboten werden kann. Alle weiteren Funktionen können durch Add-Ons
erlangt werden.

Die vollständige [Feature-Übersicht](https://docs.moori.net/plugin/MoorlForms/all-features/) fasst die Basis und sämtliche Add-ons zusammen. Technische Erweiterungsverträge und Grenzen stehen in der jeweiligen `CODEX.md` im Pluginverzeichnis.

1. [Classic Add-On](https://docs.moori.net/plugin/MoorlFormsClassic/): Bedingungen, Repeater, zusätzliche Felder, Verlauf, Druckansicht und weitere Aktionen
2. [Exit-Intent-Popups Add-On](https://docs.moori.net/plugin/MoorlFormsPopup/): Nutze Formulare als Popup
3. [Slides Add-On](https://docs.moori.net/plugin/MoorlFormsSlides/): Nutze Slides
4. [Kunden-Formulare Add-On](https://docs.moori.net/plugin/MoorlFormsCustomer/): Kundenspezifische Formulare für Registrierung und Kundenbereich
5. [Produkt-Konfigurator Add-On](https://docs.moori.net/plugin/MoorlFormsCustomProducts/): Zusätzliche Angaben zu Produkten inkl. Preiskalkulation
6. [Bestellung Add-On](https://docs.moori.net/plugin/MoorlFormsOrder/): Zusätzliche Checkout-Angaben, optionale Bestellsperre und Speicherung an der Bestellung
7. [Produkt-Anfrage Add-On](https://docs.moori.net/plugin/MoorlFormsProduct/): Produktspezifische Anfrage-Formulare
8. [CSV Add-On](https://docs.moori.net/plugin/MoorlFormsCsv/): Formularwerte in CSV-Dateien schreiben
9. [Hubspot Add-On](https://docs.moori.net/plugin/MoorlFormsHubspot/): Übertragung an die konfigurierte HubSpot-Integration
10. [Mautic Add-On](https://docs.moori.net/plugin/MoorlFormsMautic/): Mautic-Formular-/Kontaktintegration
11. [Webhook Add-On](https://docs.moori.net/plugin/MoorlFormsWebhook/): Konfigurierbare HTTP-Anfragen mit Formularwerten
12. Kundenindividuelle Add-Ons auf Anfrage

(\* In Entwicklung, \*\* In Konzeptphase)

## Beispiel Add-On für Entwickler

[Beispiel Add-On](https://github.com/moorl/MoorlFormsExample). Der lokale Stand enthält veraltete Methodensignaturen und muss vor einer Aktivierung an die aktuellen Basis-Interfaces angepasst werden. Siehe dessen `CODEX.md` und die [Feature-Übersicht](https://docs.moori.net/plugin/MoorlForms/all-features/#example-und-eigene-erweiterungen).

## Wofür ist dieses Plugin gut?

Das Shopware 6 _Formular Baukasten 2_ Plugin ermöglicht es Kinderleicht komplexe Formulare mit eigenständigen
Aufgabenbereichen zu erstellen.

Es ist modular aufgebaut, so lassen sich Prozesse und einzelne Felder beliebig erweitern.

## Installation

!!! note

      Falls du Probleme mit dem Plugin hast, bitte beachte folgende [Hinweise](https://docs.moori.net/plugin/) im FAQ Bereich.

1. Installiere
   [Foundation](https://docs.moori.net/plugin/MoorlFoundation/)
2. Installiere Formular Baukasten 2 im Plugin Manager
3. Gehe zu: Inhalte | Formular Baukasten 2

Hier kannst du nun ein neues Formular erstellen oder importieren.

## Einstellungen

Die Screenshots dieser Anleitung zeigen die englische Administration in Full HD (1920 × 1080). Beide Dokumentationssprachen verwenden dieselben Bilder.

### Basiskonfiguration

![](images/admin-list.png)

![](images/admin-new-import.png)

1. Neues Formular erstellen
2. Import

![](images/admin-form-general.png)

1. Formular Einstellungen
2. Formular speichern
3. Export
4. Strukturbereich der Formularelemente
5. Einstellungsbereich (Formular/Element)

![](images/admin-element-text.png)

1. Kontextmenü zum Erstellen, Löschen oder Duplizieren von Elementen
2. Generelle Elementeinstellungen

### Einstellungen im Detail

#### Zuweisungen von Elementen und Formularen

Du kannst generell die Sichtbarkeit der Formulare und der Elemente hier konfigurieren.

Ein Formular/Element...

- nur in einem bestimmten Zeitraum anzeigen
- nur in einem bestimmten Verkaufskanal anzeigen
- nur für ein gewähltes Liefer-Land anzeigen
- nur für eine ausgewählte Versandart oder Zahlungsart anzeigen
- nur für eine bestimmte Kundengruppe anzeigen

Ein produktspezifisches Formular...

- kann einem Produkt-Stream zugewiesen werden

Ein Element der Gruppe Sektionen...

- kann hier einem Hintergrundbild zugewiesen werden

Einige dieser Zuweisungen sind nur in den Formular Baukasten 2 Add-Ons verfügbar!

![](images/admin-form-assignment.png)

![Sichtbarkeit und Entity-Mapping eines Elements](images/admin-element-assignment.png)

#### Layout und Stylesheet Einstellungen

Du kannst jedem Formular/Element Stylesheet Attribute zuweisen.

Die CSS Optionen variieren je nach Typ des Formulares/Elementes.

![](images/admin-form-layout.png)

### Einstellungen für Elemente

#### Feld Konfiguration

Alle Elemente aus der Gruppe Feld und Multi-Feld können weitere Eigenschaften in dieser Konfiguration erhalten.

![](images/admin-element-field-settings.png)

#### Auswahl Konfiguration

Alle Elemente aus der Gruppe Multi-Feld können Datenbankspezifische Werte erhalten. Durch Add-Ons werden hier mehr Möglichkeiten geboten.

![Auswahlelement](images/admin-element-selection.png)

![](images/admin-element-selection-settings.png)

Wähle `custom-entity`, um DAL-Quelle, Beschriftungen und Filter zu konfigurieren. Es werden höchstens 500 Optionen geladen. Die Aufnahme zeigt eine ungespeicherte Auswahl.

![Auswahl einer eigenen Entity (ungespeichertes Beispiel)](images/admin-element-custom-entity.png)

#### Responsives Verhalten

Sofern das Eltern-Element aus der Gruppe Zeilen/Rows ist, können alle darin enthaltenen Elemente responsive Eigenschaften erhalten.
Hierbei gilt die Regel "Mobile-First", es werden immer die Eigenschaften weiter vererbt.

Die Aufteilung ist wie folgt.

Viewport (xs bis xxl) | Vererbt (Ja/Nein) | Anzeigen (Ja/Nein) | Breite | Sortierung/Anordnung

![](images/admin-element-layout.png)

#### Konfiguration Upload Feld

![Upload-Element](images/admin-element-upload.png)

![](images/admin-element-upload-settings.png)

#### Datum, Uhrzeit und Zahlen

Datumsfelder bieten Kalendereinstellungen, Wochentagsauswahl und Datumsgrenzen. Uhrzeit- und Zahlenfelder besitzen eigene Eingabeeinstellungen. Diese Browsergrenzen sind nicht automatisch entsprechende serverseitige Fachprüfungen; beachte die Feature-Übersicht.

#### HTML und Card-Sektionen

HTML-Inhalte werden sprachbezogen gepflegt. Card-Sektionen fassen zusammengehörige Inhalte zusammen und lassen sich über die Layout-Einstellungen gestalten.

#### Validierung

Konfiguriere Pflichtfelder, Längen, Muster und Vergleichsfelder am Element.

![Validierungseinstellungen eines Elements](images/admin-element-validation.png)

#### Eingebettete CMS-Elemente

Füge ein CMS-Element in die Formularstruktur ein und konfiguriere dessen Inhalt.

![Eingebettetes CMS-Element](images/admin-element-cms.png)

![Einstellungen des eingebetteten CMS-Elements](images/admin-element-cms-settings.png)

### Einstellungen für Formulare

Wähle die Verarbeitungsschritte in den allgemeinen Formulareinstellungen. Die verfügbaren Aktionen hängen von den aktiven Add-ons ab.

![Verfügbare Formularaktionen](images/admin-form-actions.png)

#### Konfiguration E-Mail

Hier kann der E-Mail Empfänger konfiguriert werden. Ist kein Wert hinterlegt, wird die Standard E-Mail Adresse
des Shops genutzt.

Die Basis besitzt bereits die Aktion `receipt-confirmation` für eine Empfangsbestätigung und unterstützt Empfänger aus Formularkonfiguration, Übersetzung, geeigneten Auswahloptionen oder Entity-Kontext. Classic ergänzt die vollständige Mailkopie mit eigener Vorlage und optionalem Kundenschalter. Empfangsbestätigung und Mailkopie sind unterschiedliche Funktionen.

![](images/admin-form-mail.png)

Die folgende Aufnahme zeigt eine temporär ausgewählte Empfangsbestätigung im Editor; dieser Entwurf wurde nicht gespeichert.

![](images/admin-form-mail-receipt-draft.png)

## CMS Einstellungen

Das Formular hat keinen eigenen Block, sondern ist über das "Element Austauschen"-Symbol erreichbar!

Nachdem das CMS Element eingefügt wurde, kann man Formulare vom Typ CMS oder Test der CMS Seite zuweisen.

![Formular im Erlebniswelten-Editor](images/admin-cms-page.png)

![](images/admin-cms-element-settings.png)

![Formularauswahl für das CMS-Element](images/admin-cms-form-selection.png)

## Plugin-Einstellungen

Öffne **Erweiterungen → Meine Erweiterungen → Formular Baukasten 2 → Konfigurieren**. Zu den allgemeinen Einstellungen gehören Logging, Uploads und Anhänge, Trimming und Zeichenanzeigen. Die Modal-Einstellungen steuern Formulare im Dialog.

![Allgemeine Plugin-Einstellungen](images/admin-plugin-config-general.png)

![Modal-Einstellungen des Plugins](images/admin-plugin-config-modal.png)

## Ausgabe im Storefront

### Formularvalidierung

Die Feldvalidierung kann Browserprüfungen mit einer rekursiven serverseitigen Validierung kombinieren. Konfiguriere Pflichtfelder, Längen, Muster und Vergleichsfelder passend zum Eingabetyp. Für reine Browsergrenzen von Datum, Uhrzeit, Zahlen und URLs gelten die Einschränkungen der Feature-Übersicht.

### E-Mail-Versand

Aktiviere die Aktion `mail` und wähle Empfänger und Vorlagen in den E-Mail-Einstellungen des Formulars. Die E-Mail kann die formatierte Formularzusammenfassung und konfigurierte Anhänge enthalten. Empfangsbestätigung und Classic-Mailkopie sind eigenständige Aktionen.

## Sicherheit

- Die formatierte HTML-Zusammenfassung maskiert Eingaben. Eigene HTML-/Twig-Inhalte und Integrationen müssen entsprechend ihrem Einsatzzweck eingerichtet werden; nicht jede im Browser angebotene Eingrenzung ist ein serverseitiger Fachvalidator. Details stehen in der [Feature-Übersicht](https://docs.moori.net/plugin/MoorlForms/all-features/#grenzen-der-validierung).
