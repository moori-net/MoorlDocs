# Formular Baukasten 2 | Produkt-Konfigurator Add-On

Mit diesem Add-On für [Formular Baukasten 2](https://docs.moori.net/plugin/MoorlForms/) kannst du Produkte individuell konfigurierbar machen und den Preis beeinflussen! Eingabefelder lassen sich Datenbankfeldern zuweisen!

Die Beschreibung wurde am 10.11.2026 mit dem lokalen Quellcode der Version 2.7.1 abgeglichen. Die Add-on-spezifische Administration wurde in dieser Umgebung nicht visuell geprüft. Das Plugin-Paket setzt Shopware `~6.7.8`, MoorlFoundation `~1.7.29` und MoorlForms `~2.7.0` voraus.

## Beispiel Formulare zum Download

- [Produkt-Konfigurator Add-On](examples/custom-products-add-on.json)
- [Produkt-Konfigurator Add-On (Flächenberechnung)](examples/custom-products-add-on-ac.json)

Prüfe nach dem Import Produktgruppe, Zielentität `order_line_item`, Steuer-/Währungsdaten und individuelle Custom Fields. Das Flächenbeispiel enthält keine Produktgruppenzuweisung. Die Beispiele verwenden ältere Exportdaten; ein echter Import in der aktuellen Oberfläche wurde für diesen Dokumentationsabgleich nicht durchgeführt.

## Neues Formular vom Typ "Produkt-Konfigurator"

Mit diesem Formular kannst du einerseits die Produktpreise über die Optionen beeinflussen und andererseits kannst du das Mapping nutzen, um die Konfiguration in Custom-Feldern zu speichern, z.B. für weitere technische Verarbeitung der Daten.

Lege das Formular unter **Inhalte → Formular Baukasten 2** mit dem Typ „Produkt-Konfigurator“ (`custom-product`) an. Das Add-On verwendet den Basiseditor und ergänzt dort die Einstellung zur Preisreihenfolge. Es besitzt keine eigene Admin-Navigation. Die Konfiguration wird in das bestehende Kauf-Formular eingebettet; ein zusätzlicher Absende-Button ist dort nicht nötig.

Die zugeordnete Entität ist `order_line_item`, also die Bestellposition. Die Konfiguration liegt zunächst als Payload an der Warenkorbposition. Nach Bestellabschluss werden die Mappings und Zusammenfassungen an die Bestellposition geschrieben.

Weise das Formular einer dynamischen Produktgruppe zu. Diese bestimmt, für welche Produkte es angeboten wird. Produkte ohne Produktstream-IDs werden in der aktuellen Zuordnung übersprungen.

Prüfe außerdem die Preis- und Währungseinstellungen. Die aktuelle Warenkorbberechnung verwendet für Optionspreise die Steuerregeln der Produkt-Preisdefinition; eine eigene Formularsteuerrate ist dafür nicht pauschal erforderlich.

Es ist auch möglich mehrere Formulare für die Produkte zu kombinieren! Achte jedoch darauf, dass du immer individuelle technische Namen für deine Eingabefelder nutzt!

## Preisdefinitionen

Du kannst für die Optionen Preisdefinitionen festlegen.

Für Optionen gibt es absolute Zuschläge und absolute Abschläge. Wähle für einen festen Rabatt die Preisart „Absoluter Preisnachlass“ (`absolute-discount`); der konfigurierte Betrag wird vom Preis abgezogen. Die frühere Einschränkung auf positive absolute Zuschläge gilt damit nicht mehr.

Prozentuale Preise sind relativ zum Preis des Produktes. Du kannst auch negative prozentuale Preise definieren.

## Längen- und Flächenberechnungen

Mit Feldern vom Typ „Nummer“ oder „Nummernbereich“ und deren Preismultiplikator kannst du den Produktpreis mit dem Eingabewert multiplizieren. Mehrere Multiplikatoren werden miteinander multipliziert, etwa Länge × Breite bei einer Flächenberechnung.

Die Einstellung `priceCalculationPriority` in der Produkt-Konfigurator-Karte bestimmt, ob Optionsbeträge ebenfalls multipliziert werden. Mit `B` als Basisstückpreis, `S` als Summe der gewählten Optionsbeträge und `M` als Produkt aller Multiplikatoren gilt:

| Einstellung | Stückpreis |
| --- | --- |
| Aus oder nicht gesetzt | `B × M + S` |
| An | `(B + S) × M` |

Bei mehreren kombinierten Formularen ist die Einstellung des ersten Formulars nach Formularpriorität maßgeblich. Die Produktmenge wird zusätzlich berücksichtigt. Ein numerischer Nullwert wird serverseitig derzeit als Multiplikator übersprungen; gleiche die Vorschau und den Warenkorb für solche Grenzwerte gesondert ab.

## Mapping

Ordne Eingabefelder den unterstützten Feldern der Bestellposition oder vorhandenen Custom Fields zu. Diese Mappings werden nach Bestellabschluss geschrieben; Uploads werden dabei als Medienreferenzen übernommen.

## Storefront

Kunden geben auf der Produktseite Texte ein, laden Dateien hoch und wählen Optionen aus. Die Preisanzeige berücksichtigt Auswahl und Menge. Die Konfiguration wird in den Warenkorb übernommen und kann vor dem Bestellabschluss angepasst werden. Die Bestellübersicht zeigt eine Textzusammenfassung.

Beim erneuten Bestellen aus der Bestellhistorie wird der gespeicherte Konfigurationspayload wieder mitgeschickt. Die Verarbeitung und Preisberechnung richten sich dabei nach den aktuell verfügbaren Formularen und Produkten.

## Admin

Solltest du das Mapping nicht nutzen, hast du trotzdem jederzeit Zugriff auf die Konfiguration.

Öffne **Bestellungen → Bestellung → Allgemein** und wähle im Kontextmenü der Position „Zeige Konfiguration“. Die Zusammenfassung bleibt auch ohne individuelle Feldmappings verfügbar.

Für E-Mail- und eigene Dokumentvorlagen kannst du `{{ orderLineItem.customFields._moorl_fb_html }}` oder `{{ orderLineItem.customFields._moorl_fb_plain }}` verwenden. `orderLineItem` muss dabei die aktuelle Bestellposition in deiner Vorlage bezeichnen; passe den Variablennamen an die jeweilige Schleife an. Zusätzlich werden `_moorl_fb_json`, `_moorl_fb_xml` und `_moorl_fb_media_ids` gespeichert. Das Add-On passt nicht automatisch sämtliche Mail- und Dokumentvorlagen an.

Die gespeicherten Zusammenfassungen stehen in den Custom Fields der Bestellposition zur Verfügung.

## Plugin-Einstellungen

Öffne **Erweiterungen → Meine Erweiterungen → Produkt-Konfigurator Add-On → Konfigurieren**.

| Einstellung | Standard | Wirkung |
| --- | --- | --- |
| Checkout sperren, wenn erforderliche Angaben fehlen | Aus | Blockiert den Bestellabschluss bei erkannten Konfigurationsfehlern |
| Badge in der Produktbox anzeigen | An | Kennzeichnet konfigurierbare Produkte |
| Button in der Produktbox anzeigen | An | Führt zur Konfiguration auf der Detailseite |
| Formulare nur für die Produktdetailseite laden | Aus | Beschränkt die Produktanreicherung auf Detailseiten |
| Formulare nur für Produktlisten laden | Aus | Beschränkt die Produktanreicherung auf Listings |

Sind beide Ladebeschränkungen aus, werden Produkte global angereichert. Sind beide an, laufen beide gezielten Ladepfade. Die Anzeige im Listing hängt davon ab, ob die Produktdaten dort angereichert werden.

Die Browseranzeige ist eine Vorschau; maßgeblich ist der berechnete Warenkorb. Prüfe Preisreihenfolge, Menge, Währung und Steuerstatus sowie die Pflichtfeldsperre mit deiner eingesetzten Formular- und Theme-Konfiguration. Eine allgemeine Kompatibilität mit Rabatt-/Promotion-Erweiterungen ist durch dieses Add-On allein nicht nachgewiesen.
