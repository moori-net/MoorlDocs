# Formular Baukasten 2 | Basis Version

Dieses Plugin basiert auf einer Grundlegenden Neuentwicklung des
[Formular Baukastens](../MoorlFormBuilder/index.md) und bietet maximale
Flexibilität und Integrität für Shopware 6.

## Hinweis für alle Kunden, die den Formular Baukasten bereits besitzen

Dieses Plugin ist grundlegend anders aufgebaut und bietet keine Möglichkeit, die bisherigen
Formulare zu migrieren.

Leider ist es nach Absprache mit Shopware auch nicht möglich die Subscriptions zu duplizieren/übertragen.

Da ich meinen bisherigen Kunden keinen Nachteil schaffen möchte, wird der Formular Baukasten
weiterhin mit Updates versorgt. Aber es werden keine neuen Funktionen mehr entwickelt.

Für alle Interessenten mit aktiven Subscriptions biete ich einen 50% Rabatt für Basis und Add-Ons. 
Die Migration der Formulare wird auf Wunsch ebenfalls übernommen.
Es kann jedoch zu Abweichungen im Aussehen kommen, diese werde ich nicht abgleichen.

## Add-Ons

Dieses Plugin wurde in seiner Basis Version um einige Funktionen gekürzt, damit es zu einem
erschwinglichen Preis angeboten werden kann. Alle weiteren Funktionen können durch Add-Ons
erlangt werden.

Es ist auch möglich eigene Add-Ons zu erstellen, dazu folgt demnächst eine Entwickler-Dokumentation.

1. [Classic Add-On](../MoorlFormsClassic/index.md): Beinhaltet alle Funktionen des [Formular Baukastens](../MoorlFormBuilder/index.md)
2. [Exit-Intent-Popups Add-On](../MoorlFormsPopup/index.md): Nutze Formulare als Popup
3. [Slides Add-On](../MoorlFormsSlides/index.md): Nutze Slides
4. [Kunden-Formulare Add-On](../MoorlFormsCustomer/index.md): Kundenspezifische Formulare für Registrierung und Kundenbereich
5. [Produkt-Konfigurator Add-On](../MoorlFormsCustomProducts/index.md): Zusätzliche Angaben zu Produkten inkl. Preiskalkulation
6. Order Add-On**: Zusätzliche Angaben zur Bestellung inkl. Preiskalkulation auf den Warenkorb
7. [Produkt-Anfrage Add-On](../MoorlFormsProduct/index.md): Produktspezifische Anfrage-Formulare
8. Kundenindividuelle Add-Ons auf Anfrage

(\* In Entwicklung, \*\* In Konzeptphase)

## Beispiel Add-On für Entwickler

[Beispiel Add-On](https://github.com/moorl/MoorlFormsExample)

## Wofür ist dieses Plugin gut?

Das Shopware 6 _Formular Baukasten 2_ Plugin ermöglicht es Kinderleicht komplexe Formulare mit eigenständigen
Aufgabenbereichen zu erstellen.

Es ist modular aufgebaut, so lassen sich Prozesse und einzelne Felder beliebig erweitern.

## Installation

_Hinweis: Falls du Probleme mit dem Plugin hast, bitte beachte 
folgende  [Hinweise](../faq.md) im FAQ Bereich._

1. Installiere
   [Foundation](../MoorlFoundation/index.md)
2. Installiere Formular Baukasten 2 im Plugin Manager
3. Gehe zu: Inhalte | Formular Baukasten 2
   
Hier kannst du nun ein neues Formular erstellen oder importieren.

## Beispiel Formulare zum Download

- [Einfaches Kontaktformular](examples/simple-contact-form.json)

## Einstellungen

### Basiskonfiguration

![](images/fb-01.jpg)

![](images/fb-02.jpg)

1. Neues Formular erstellen
2. Import

![](images/fb-03.jpg)

1. Formular Einstellungen
2. Formular speichern
3. Export
4. Strukturbereich der Formularelemente
5. Einstellungsbereich (Formular/Element)

![](images/fb-04.jpg)

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

![](images/fb-05.jpg)

#### Layout und Stylesheet Einstellungen

Du kannst jedem Formular/Element Stylesheet Attribute zuweisen.

Die CSS Optionen variieren je nach Typ des Formulares/Elementes.

![](images/fb-06.jpg)

### Einstellungen für Elemente

#### Feld Konfiguration

Alle Elemente aus der Gruppe Feld und Multi-Feld können weitere Eigenschaften in dieser Konfiguration erhalten.

![](images/fb-07.jpg)

#### Auswahl Konfiguration

Alle Elemente aus der Gruppe Multi-Feld können Datenbankspezifische Werte erhalten. Durch Add-Ons werden hier mehr Möglichkeiten geboten.

![](images/fb-08.jpg)

#### Responsives Verhalten

Sofern das Eltern-Element aus der Gruppe Zeilen/Rows ist, können alle darin enthaltenen Elemente responsive Eigenschaften erhalten.
Hierbei gilt die Regel "Mobile-First", es werden immer die Eigenschaften weiter vererbt.

Die Aufteilung ist wie folgt.

Viewport (xs bis xxl) | Vererbt (Ja/Nein) | Anzeigen (Ja/Nein) | Breite | Sortierung/Anordnung

![](images/fb-09.jpg)

#### Konfiguration Upload Feld

![](images/fb-10.jpg)

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

Die Funktion "Kopie senden" und "Empfänger nach Auswahlbedingung" gibt es im Classic Add-On!

![](images/fb-16.jpg)

![](images/fb-17.jpg)

## CMS Einstellungen

Das Formular hat keinen eigenen Block, sondern ist über das "Element Austauschen"-Symbol erreichbar!

Nachdem das CMS Element eingefügt wurde, kann man Formulare vom Typ CMS oder Test der CMS Seite zuweisen.

![](images/fb-22.jpg)

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

- Es werden HTML Tags maskiert um schädliche Scripts zu unterbinden.
