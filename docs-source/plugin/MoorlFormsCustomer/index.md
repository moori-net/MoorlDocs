# Formular Baukasten 2 | Kunden-Formulare Add-On

Mit diesem Add-On für [Formular Baukasten 2](https://docs.moori.net/plugin/MoorlForms/) kannst du zusätzliche Felder in die Kundenregistrierung einbinden und eigene Formularseiten im Kundenkonto bereitstellen. Eingaben lassen sich vorhandenen Kundenfeldern und Custom Fields zuordnen.

Die Beschreibung wurde am 10.11.2026 mit dem lokalen Quellcode der Version 2.7.0 abgeglichen. Die Add-on-spezifische Administration wurde in dieser Umgebung nicht visuell geprüft.

## Einrichtung und Verfügbarkeit

Voraussetzungen laut Plugin-Paket sind Shopware `~6.7.8`, MoorlFoundation `~1.7.29` und MoorlForms `~2.7.0`.

Erstelle das Formular unter **Inhalte → Formular Baukasten 2** im Formular Baukasten. Wähle „Erweiterung der Kundenregistrierung“ (`customer-register`) oder „Formular im Kundenbereich“ (`customer-account`). Beide Typen verwenden die zugeordnete Entität `customer`. Aktivierung, Verkaufskanal und weitere Verfügbarkeitsbedingungen des Basisformulars bestimmen, wo es angeboten wird.

Das Add-On besitzt keine eigene Admin-Navigation und keine eigenen Plugin-Konfigurationsschalter. Layout, Eingabefelder, Mappings und Aktionen werden im Basisformular gepflegt.

## Beispiel Formulare zum Download

- [Kunden-Account Formular Add-On](examples/customer-account-add-on.json)
- [Kunden-Registrierung Formular Add-On](examples/customer-registration-add-on.json)

Prüfe nach dem Import die benötigten Custom Fields und die Mail-Konfiguration. Die Beispiele verwenden shopbezogene Feldnamen; ein echter Import in der aktuellen Oberfläche wurde für diesen Dokumentationsabgleich nicht durchgeführt.

## Neue Formular-Typen

- Formulare für den Account-Bereich
- Formulare für die Registrierung

## Mapping

Ordne die Eingabefelder über das Mapping den unterstützten Feldern der Kunden-Entität zu. Dazu gehören beispielsweise `firstName`, `email` und vorhandene Felder unter `customFields.<name>`. Individuelle Custom Fields müssen passend eingerichtet sein.

So kann der Kunde z.B. eine Gewerbeanmeldung hochladen, die Zuweisung zu der Datei steht z.B. in einem
Custom-Feld. Beim Upload wird dort die Medien-ID gespeichert, nicht der Dateiinhalt.

### Kunden-Account

Die Formulare für den Kunden-Account werden automatisch in der Navigation eingebunden.

Das Formular übernimmt anhand der Mapping-Eigenschaften die passenden Datenbankfelder.

Auch beim Speichern werden die Daten wieder in den zugeordneten Datenbankfeldern gespeichert.

Optional kann der Shopbetreiber per E-Mail über eine Änderung informiert werden. Richte dafür die Mail-Aktion, Empfänger und Vorlage im Formular ein; das Add-On aktiviert keine Standardbenachrichtigung.

Anders als die eingebettete Registrierung ist das Account-Formular eine eigenständige Seite. Ergänze dort einen passenden Absende-Button und bei Bedarf ein Feedback-Element, wie im Account-Beispiel gezeigt. Die Formularseite und das Speichern verlangen einen angemeldeten Kunden.

### Kunden-Registrierung

Die zusätzlichen Eingabefelder werden in Shopwares bestehendes Registrierungsformular eingebettet. Eigene Formularrahmen- oder Absende-Bauteile sind deshalb nicht erforderlich. Pflichtfelder werden vor der Shopware-Registrierung geprüft; nach erfolgreicher Registrierung werden die Mappings und Uploads dem neuen Kunden zugeordnet.

Im Flow Builder steht das Ereignis **Registrierung (Formular Baukasten)** mit dem technischen Namen `checkout.customer.moorl_form_register` zur Verfügung. Es enthält den Kunden und ein Formular. Bei mehreren Registrierungsformularen wird hierfür nur das erste verwendet. Der mitgelieferte Flow hat keine voreingestellten Aktionen; Benachrichtigungen oder weitere Schritte müssen eingerichtet werden.

## Gespeicherte Zusammenfassungen

Neben den individuellen Mappings schreibt die Basis die Zusammenfassungen `_moorl_fb_html`, `_moorl_fb_plain`, `_moorl_fb_json`, `_moorl_fb_xml` und die Uploadreferenzen `_moorl_fb_media_ids` in die Custom Fields des Kunden. Account-Formulare werden aus den zugeordneten Kundenfeldern vorbelegt; sie sind keine eigene Kunden-Datenbank.
