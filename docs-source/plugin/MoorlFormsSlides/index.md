# Formular Baukasten 2 | Slides Add-On

Mit diesem Add-On für [Formular Baukasten 2](https://docs.moori.net/plugin/MoorlForms/) kannst du Formulare in mehrere Schritte und optisch ansprechend aufteilen. Dieses Plugin ist die optimale Ergänzung zum Popup Add-On!

!!! note "Hinweis für alle Kunden, die den Formular Baukasten bereits besitzen"

    Dieses Plugin ist grundlegend anders aufgebaut und bietet keine Möglichkeit, die bisherigen Formulare zu migrieren.

    Leider ist es nach Absprache mit Shopware auch nicht möglich die Subscriptions zu duplizieren/übertragen.

    Da ich meinen bisherigen Kunden keinen Nachteil schaffen möchte, wird der Formular Baukasten weiterhin mit Updates versorgt. Aber es werden keine neuen Funktionen mehr entwickelt.

    Für alle Interessenten mit aktiven Subscriptions biete ich einen 50% Gutschein für Basis und Add-Ons.

    Der Gutschein wird individuell ausgestellt und ist nicht mit Rabattaktionen kommulierbar.

## Beispiel Formulare zum Download

- [Slides Add-On](examples/slides-add-on.json)

## Neues Element von Typ "Slides"

Dieses Element ist in der Konfiguration sehr anspruchsvoll, aber auch mächtig in der Anwendung.

Füge einen Container vom Typ `slides` und darin Unterelemente vom Typ `slide` ein. Die eigentlichen Formularfelder liegen innerhalb der Slides. Das Add-on registriert diese beiden Elementtypen; es führt keinen neuen Formulartyp ein. Popup ist eine optionale Ergänzung und keine Pflichtabhängigkeit.

## Konfiguration

Benenne die vor- und zurück Buttons.

Zusätzlich kannst du die CSS-Klassen der Buttons festlegen, automatisches Scrollen zum Formular mit Offset aktivieren, deaktivierte Buttons ausblenden und einen Absenden-Button für den letzten Schritt einfügen. Dessen Text und Klasse sind ebenfalls einstellbar. Der Editor initialisiert Vor/Zurück mit `btn btn-light`, automatisches Scrollen mit aktiv und einen Offset von 60 Pixeln.

Die Stylesheet Einstellungen sind essenziell für das Element, hier kannst du folgende
Konfigurationen machen:

1. Animationen für die Übergänge
2. Die minimale Höhe (empfohlen)
3. Die Slides gleichen sich mit Bootstrap-Zeilen, hier empfehle ich die horizontale und
vertikale Ausrichtung auf "Mittig" zu stellen.

Hinweis: Die CSS Eigenschaften werden auf die Slide-Elemente innerhalb des Slides übertagen.
So sind die Eigenschaften stimmig und du kannst z.B. die Hintergrundfarbe pro Slide anpassen!

Die Ausgabe benötigt sowohl eine belegte CSS-Konfiguration als auch eine Übergangskonfiguration (`config.css` und `config.animateInOut`). Fehlt eine davon, erscheint ein Konfigurationshinweis. Kindwerte überschreiben geerbte Elternwerte. Der Slider arbeitet als Galerie ohne Loop, Touch-Wischen oder Mausziehen; Vor/Zurück steuern den Wechsel.

Das Element vom Typ "Slide" ist das Unterelement und kann beliebig oft verwendet werden.

Da die CSS Eigenschaften durch das Eltern-Element gesetzt werden, kannst du diese Einstellungen
optional anpassen.

Ein Hintergrundbild kannst du im Tab "Zuweisung" definieren.

Jedes Slide-Element unterstützt responsive Unter-Elemente, nutze diese Einstellung um die Felder
auszurichten.

Die wesentlichen Bestandteile des Formulars kannst du frei positionieren.

## Ausgabe im Storefront

In diesem Beispiel habe ich das Popup-Formular verwendet. Die Slides sind aber auch für
CMS Elemente tauglich!

## Navigation und Validierung

Beim Klick auf Weiter prüft das Storefront-JavaScript die erforderlichen Felder der aktiven Slide mit der Browservalidierung. Die vollständige Formular- und Servervalidierung des Basisplugins bleibt für das Absenden maßgeblich. Optionale Felder werden von dieser speziellen Schrittprüfung nicht geprüft.

Die Überschrift wird beim Schrittwechsel aus dem Namen der aktiven Slide übernommen. Der optionale Absenden-Button wird beim Wechsel auf die letzte Slide freigegeben. Für einen sinnvollen Ablauf sollten Pflichtfelder und Absendeelemente auf die Schritte abgestimmt werden.

Mit Classic können Bedingungen Slides ausblenden; das Slides-JavaScript überspringt beim Wechsel eine entsprechend ausgeblendete Slide. Slides selbst enthält keine eigene Bedingungskonfiguration. Prüfe die konkrete Kombination insbesondere bei ausgeblendeten ersten oder letzten Schritten im Browser.

## Speicherung und Einrichtung

Die Struktur und Einstellungen werden als normale Formularelemente im Basisplugin gespeichert. Es gibt keine eigene Zwischenspeicherung des aktuellen Schritts, keine serverseitigen Teilabgaben und keine automatische Wiederaufnahme derselben Slide nach einem Neuladen. Die Eingabespeicherung des Basisplugins ist davon getrennt.

Einstieg: Inhalte → Formular Baukasten → Formular → Struktur → Slides-Element; technische Adminrouten `moorl.fb.form.detail` und `moorl.fb.form.element`. Es gibt keinen eigenen Slides-Menüpunkt. Die Downloadvorlage ist ein aktives CMS-Formular mit der Aktion `mail`; vorhandene Popup-Konfigurationswerte machen sie noch nicht zu einem Popup-Formular.

Ein separater Elementtyp `animation` ist im aktuellen Plugin nicht registriert. Die Übergangsanimationen der Slides stehen über die dafür vorgesehenen Layoutoptionen zur Verfügung.

Diese Ergänzungen entsprechen der Quellcodeprüfung vom 10.11.2026; sie sind keine Bestätigung eines ausgeführten Browser- oder Assetbuild-Tests. Die historischen Migrations-/Gutscheinhinweise oben wurden nicht auf aktuelle geschäftliche Gültigkeit geprüft.
