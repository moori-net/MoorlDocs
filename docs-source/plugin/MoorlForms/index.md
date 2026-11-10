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

![Vorschau](images/fb-20.jpg)

---

## Plugin erwerben

Dieses Plugin kann im offiziellen **Shopware Community Store** erworben werden.

- [Shopware Community Store](https://store.shopware.com/de/search?search=MoorlForms)


**Wichtiger Hinweis:** Sie benötigen das Foundation Plugin, welches Ihnen kostenlos zur Verfügung steht: [moori Foundation](../MoorlFoundation/index.md)


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

Die vollständige [Feature-Übersicht](all-features.md) fasst die Basis und sämtliche Add-ons zusammen. Der [Prüfbericht](plugin-audit.md) benennt den Abgleich mit dem Quellcode und den Stand der aktuellen Admin-Aufnahmen. Technische Erweiterungsverträge und Grenzen stehen in der jeweiligen `CODEX.md` im Pluginverzeichnis.

1. [Classic Add-On](../MoorlFormsClassic/index.md): Bedingungen, Repeater, zusätzliche Felder, Verlauf, Druckansicht und weitere Aktionen
2. [Exit-Intent-Popups Add-On](../MoorlFormsPopup/index.md): Nutze Formulare als Popup
3. [Slides Add-On](../MoorlFormsSlides/index.md): Nutze Slides
4. [Kunden-Formulare Add-On](../MoorlFormsCustomer/index.md): Kundenspezifische Formulare für Registrierung und Kundenbereich
5. [Produkt-Konfigurator Add-On](../MoorlFormsCustomProducts/index.md): Zusätzliche Angaben zu Produkten inkl. Preiskalkulation
6. [Bestellung Add-On](../MoorlFormsOrder/index.md): Zusätzliche Checkout-Angaben, optionale Bestellsperre und Speicherung an der Bestellung
7. [Produkt-Anfrage Add-On](../MoorlFormsProduct/index.md): Produktspezifische Anfrage-Formulare
8. [CSV Add-On](../MoorlFormsCsv/index.md): Formularwerte in CSV-Dateien schreiben
9. [Hubspot Add-On](../MoorlFormsHubspot/index.md): Übertragung an die konfigurierte HubSpot-Integration
10. [Mautic Add-On](../MoorlFormsMautic/index.md): Mautic-Formular-/Kontaktintegration
11. [Webhook Add-On](../MoorlFormsWebhook/index.md): Konfigurierbare HTTP-Anfragen mit Formularwerten
12. Kundenindividuelle Add-Ons auf Anfrage

(\* In Entwicklung, \*\* In Konzeptphase)

## Beispiel Add-On für Entwickler

[Beispiel Add-On](https://github.com/moorl/MoorlFormsExample). Der lokale Stand enthält veraltete Methodensignaturen und muss vor einer Aktivierung an die aktuellen Basis-Interfaces angepasst werden. Siehe dessen `CODEX.md` und die [Feature-Übersicht](all-features.md#example-und-eigene-erweiterungen).

## Wofür ist dieses Plugin gut?

Das Shopware 6 _Formular Baukasten 2_ Plugin ermöglicht es Kinderleicht komplexe Formulare mit eigenständigen
Aufgabenbereichen zu erstellen.

Es ist modular aufgebaut, so lassen sich Prozesse und einzelne Felder beliebig erweitern.

## Installation

!!! note

      Falls du Probleme mit dem Plugin hast, bitte beachte folgende [Hinweise](../) im FAQ Bereich.

1. Installiere
   [Foundation](../MoorlFoundation/index.md)
2. Installiere Formular Baukasten 2 im Plugin Manager
3. Gehe zu: Inhalte | Formular Baukasten 2
   
Hier kannst du nun ein neues Formular erstellen oder importieren.

## Einstellungen

Aktuelle [Admin-Aufnahmen in Full HD](admin-screenshots.md) wurden nach vollständigem Browser-Neuladen erneut auf Englisch erstellt. Die deutschen FHD-Varianten wurden entfernt. Verbleibende JPGs illustrieren ältere Versionen. Die Empfangsbestätigung wurde für die Aufnahme nur im Editor ausgewählt und nicht gespeichert; die Galerie erläutert die Aufnahmebedingungen.

### Basiskonfiguration

![](images/admin-fhd/en/admin-list.png)

![](images/admin-fhd/en/admin-new-import.png)

1. Neues Formular erstellen
2. Import

![](images/admin-fhd/en/admin-form-general.png)

1. Formular Einstellungen
2. Formular speichern
3. Export
4. Strukturbereich der Formularelemente
5. Einstellungsbereich (Formular/Element)

![](images/admin-fhd/en/admin-element-text.png)

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

![](images/admin-fhd/en/admin-form-assignment.png)

#### Layout und Stylesheet Einstellungen

Du kannst jedem Formular/Element Stylesheet Attribute zuweisen.

Die CSS Optionen variieren je nach Typ des Formulares/Elementes.

![](images/admin-fhd/en/admin-form-layout.png)

### Einstellungen für Elemente

#### Feld Konfiguration

Alle Elemente aus der Gruppe Feld und Multi-Feld können weitere Eigenschaften in dieser Konfiguration erhalten.

![](images/admin-fhd/en/admin-element-field-settings.png)

#### Auswahl Konfiguration

Alle Elemente aus der Gruppe Multi-Feld können Datenbankspezifische Werte erhalten. Durch Add-Ons werden hier mehr Möglichkeiten geboten.

![](images/admin-fhd/en/admin-element-selection-settings.png)

#### Responsives Verhalten

Sofern das Eltern-Element aus der Gruppe Zeilen/Rows ist, können alle darin enthaltenen Elemente responsive Eigenschaften erhalten.
Hierbei gilt die Regel "Mobile-First", es werden immer die Eigenschaften weiter vererbt.

Die Aufteilung ist wie folgt.

Viewport (xs bis xxl) | Vererbt (Ja/Nein) | Anzeigen (Ja/Nein) | Breite | Sortierung/Anordnung

![](images/admin-fhd/en/admin-element-layout.png)

#### Konfiguration Upload Feld

![](images/admin-fhd/en/admin-element-upload-settings.png)

#### Konfiguration Datum

![](images/fb-11.jpg)

#### Konfiguration Uhrzeit

![](images/fb-12.jpg)

#### Konfiguration Nummer

![](images/fb-13.jpg)

#### Konfiguration HTML (Sprachbezogen)

![](images/fb-14.jpg)

#### Konfiguration Card-Sektion

![](images/fb-15.jpg)

### Einstellungen für Formulare

#### Konfiguration E-Mail

Hier kann der E-Mail Empfänger konfiguriert werden. Ist kein Wert hinterlegt, wird die Standard E-Mail Adresse
des Shops genutzt.

Die Basis besitzt bereits die Aktion `receipt-confirmation` für eine Empfangsbestätigung und unterstützt Empfänger aus Formularkonfiguration, Übersetzung, geeigneten Auswahloptionen oder Entity-Kontext. Classic ergänzt die vollständige Mailkopie mit eigener Vorlage und optionalem Kundenschalter. Empfangsbestätigung und Mailkopie sind unterschiedliche Funktionen.

![](images/admin-fhd/en/admin-form-mail.png)

![](images/admin-fhd/en/admin-form-mail-receipt-draft.png)

## CMS Einstellungen

Das Formular hat keinen eigenen Block, sondern ist über das "Element Austauschen"-Symbol erreichbar!

Nachdem das CMS Element eingefügt wurde, kann man Formulare vom Typ CMS oder Test der CMS Seite zuweisen.

![](images/admin-fhd/en/admin-cms-element-settings.png)

## Ausgabe im Storefront

### Formularvalidierung

Das Beispielformular ist vom Typ "Test" die clientseitige Validierung ist deaktiviert. 
Der Formular Baukasten 2 unterstützt eine rekursive serverseitige Validierung der Eingabefelder!

![](images/fb-18.jpg)

Die clientseitige Valididierung ist wieder aktiv. Nun wird das Formular doppelt validiert.

![](images/fb-19.jpg)

### E-Mail Versand

In diesem Beispiel zeige ich dir, wie die E-Mail im Standard ausgegeben wird.

![](images/fb-20.jpg)

![](images/fb-21.jpg)

## Sicherheit

- Die formatierte HTML-Zusammenfassung maskiert Eingaben. Eigene HTML-/Twig-Inhalte und Integrationen müssen entsprechend ihrem Einsatzzweck eingerichtet werden; nicht jede im Browser angebotene Eingrenzung ist ein serverseitiger Fachvalidator. Details stehen in der [Feature-Übersicht](all-features.md#grenzen-der-validierung).
