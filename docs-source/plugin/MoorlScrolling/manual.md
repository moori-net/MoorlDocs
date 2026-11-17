**Dokumentation:**
[https://docs.moori.net/plugin/MoorlScrolling/](https://docs.moori.net/plugin/MoorlScrolling/)


**Wichtiger Hinweis:** Sie benötigen das Foundation Plugin, welches Ihnen kostenlos zur Verfügung steht: [Foundation](https://store.shopware.com/de/search?search=MoorlFoundation)


## Voraussetzungen

MoorlScrolling benötigt Shopware 6.7 mit Storefront und MoorlFoundation aus der Versionsreihe 1.7. MoorlInterrupter ist optional.

## Installation und Aktivierung

1. Installiere und aktiviere zuerst MoorlFoundation, sofern es noch nicht verfügbar ist.
2. Installiere MoorlScrolling unter **Erweiterungen > Meine Erweiterungen** und aktiviere das Plugin.
3. Öffne im Menü des Plugins **Konfigurieren**.
4. Wähle einen Verkaufskanal oder **Alle Verkaufskanäle** für die allgemeinen Vorgaben.
5. Schalte **Unendliches Scrollen aktivieren** ein. Wähle mit **Kategorie-Listings** und **Suchergebnisse** die gewünschten Bereiche aus.
6. Speichere die Konfiguration und lade die betreffende Kategorie oder Suchseite im Storefront neu.

Die Plugin-Aktivierung und die Einstellung **Unendliches Scrollen aktivieren** sind beide erforderlich. Die Einstellungen werden in Shopwares vorhandener Systemkonfiguration gespeichert; zusätzliche Datenbanktabellen sind nicht nötig.

## Erster Funktionstest

Öffne ein Listing mit mindestens zwei Produktseiten. Standardmäßig lädt MoorlScrolling weitere Seiten unten automatisch und vorherige Seiten oben manuell nach. Die nächste Seite wird im Hintergrund vorbereitet. Der manuelle Nachladelink bleibt verfügbar.

Öffne anschließend eine spätere Seite direkt, zum Beispiel mit `?p=2`. Prüfe das Nachladen vorheriger Produkte, einen Filterwechsel und die normale Seitennavigation. Bei Verwendung von MoorlInterrupter sollten die Störer auf ihren vorgesehenen Seiten und Positionen bleiben.

## Verkaufskanäle und Ladegrenzen

Ein einzelner Verkaufskanal erbt zunächst die globalen Einstellungen. Löse die Vererbung am jeweiligen Feld, um einen eigenen Wert zu speichern.

Standardmäßig pausiert jede Richtung nach drei automatisch geladenen Seiten, bis der Kunde manuell fortsetzt. Ein Bereich umfasst höchstens 20 eingebundene Seiten; danach führt der Nachbarlink zur regulären Shopseite. Mit `0` lässt sich die jeweilige Grenze aufheben.

## Theme und andere Erweiterungen

Unterstützt wird ein primäres Kategorie- oder Suchlisting je Dokument. Prüfe die Darstellung mit deinem Theme und weiteren Listing-Erweiterungen vor dem produktiven Einsatz. Nach einer individuellen Installation aus Quellcode müssen die Storefront-Dateien und das Theme über den üblichen Shopware-Build bereitgestellt werden.
