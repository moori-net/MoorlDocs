# Prüfung des Sidequest Themes

Stand: 19.10.2026. Geprüft auf der lokalen Shopware-Instanz 6.7.14.1 im Container `shopware_6.7.14.1` unter `http://localhost`. Das Theme ist installiert, aktiviert und dem lokalen Verkaufskanal „Storefront“ zugewiesen.

## Ergebnisse

| Prüfung | Ergebnis |
| --- | --- |
| Composer-Metadaten | Gültig; Composer empfiehlt lediglich, das vorhandene Versionsfeld bei Packagist-Veröffentlichungen wegzulassen |
| PHP-Syntax der Plugin-Klasse | Fehlerfrei |
| Twig-Lint | Alle sechs Templates gültig |
| Synchrone Theme-Kompilierung | Erfolgreich, ohne eigenen JavaScript-Build |
| Original-Logo und lokale Space Mono | Im Browser geladen, HTTP 200 |
| Hintergrund und Schrift | `rgb(16, 14, 19)` und geladene Space Mono bestätigt |
| Header | Ein Header mit schlichtem Account-Link; keine Suche, Warenkorb- oder Wunschlistenaktionen |
| Navigation bei 320, 375, 768, 991, 992 und 1440 Pixel | Keine verschachtelten Hauptmenüs, keine Überlappung von Logo und Menübutton, kein horizontaler Seitenüberlauf |
| Mobiles Menü | Bootstrap öffnet/schließt die Liste und aktualisiert `aria-expanded` |
| JavaScript deaktiviert | Navigationslinks sichtbar, nicht funktionsfähiger Menübutton ausgeblendet |
| Kategorie und Produktdetail | Identische Hauptpunkte, aktive Kategorie trotz ESI-Headercache korrekt markiert |
| Produkt kaufen | Demoartikel lässt sich hinzufügen; der Warenkorb öffnet sich mit Artikel |
| Warenkorbseite | Erreichbar, mit minimalistischem Header |
| Cookie-Einstellungen | Aus dem Footer erneut geöffnet, ohne die Warenkorbseite zu verlassen |
| Footer mit konfigurierten Testdaten | Service- und Footerlinks einschließlich Impressum und aktiviertem Widerrufslink erscheinen; doppelte Kategorien werden nur einmal ausgegeben |
| Addressdialog-Tabs | Dunkler Hintergrund `#1a1620` mit hellem Text `#f4eff7` am tatsächlichen Core-Markup bestätigt |
| Checkbox, Radio und Switch | Dunkle Markierung `#100e13` auf neongrünem aktivem Hintergrund bestätigt |
| JavaScript-Laufzeit | Keine unbehandelten Fehler während der Browserprüfung |

Die Browserprüfungen liefen mit einem separaten temporären Chrome-Profil. Es wurde keine Bestellung aufgegeben. Renderprüfungen für zusätzliche Footer-Konfigurationen verwendeten das Theme-Template mit Testdaten, ohne Verkaufskanal-Kategorien zu verändern.

## Technische Entscheidungen

Globales Content-Raster am 19.10.2026: Das Pseudoelement des gemeinsamen `.content-main`-Containers verwendet den vorgegebenen doppelten Linienverlauf mit 4,5 % Deckkraft, `3rem` Rasterweite und einer bis 75 % auslaufenden Maske. Die Farbe stammt aus der Theme-Akzentfarbe. Nach erfolgreicher synchroner Kompilierung wurde das Raster auf Startseite, Kategorie, Produktdetail, Ticketdetail, Login und Warenkorb geprüft; Screenshots bei 1440 und 375 Pixeln bestätigen die Darstellung. Das Loginfeld bleibt per Mausklick fokussierbar. Ein innerhalb des Contents geöffneter Bootstrap-Dialog bleibt vor seinem Backdrop sichtbar; die Content-Ebenen erzeugen keinen zusätzlichen Stacking-Kontext. Header und Footer erhalten kein Raster.

Erweiterung des Headers und Footers am 19.10.2026: Der Account-Link steht als letzter Eintrag in der Headernavigation und führt über die Standardroute `/account` zum Accountbereich bzw. für Gäste zur Anmeldung. Im lokalen Verkaufskanal „Storefront“ wurde die neue Kategorie „Footer“ als nativer Footer-Einstiegspunkt gesetzt. Ihre Unterkategorien Impressum, AGB und Datenschutz verweisen auf die bereits vorhandenen CMS-Seiten; die Seiteninhalte wurden nicht verändert. Geprüft wurden alle drei Linkziele (HTTP 200), der Account-Login für Gäste und die Darstellung bei 320, 375, 768, 992 und 1440 Pixeln einschließlich Navigation ohne JavaScript. Alle sechs Twig-Templates sind gültig.

Nachbesserung der Ticketansicht am 19.10.2026: Die Hauptnavigation hat auch bei Hover und Fokus keine Textunterstreichung; der grüne Indikator bleibt sichtbar. Eventkopf, Veranstaltungsort und Ticket-Cards des Ticket-Plugins verwenden die Bootstrap-/Theme-Variablen für Flächen, Text und Rahmen. Nach synchroner Kompilierung wurden die verlinkte Eventseite bei 1440 und 375 Pixeln, der ausverkaufte Card-Zustand und die Anpassung an helle Theme-Variablen im Browser geprüft. Keine JavaScript-Fehler oder horizontalen mobilen Überläufe.

- Änderungen liegen direkt im angefragten Pluginverzeichnis. Das Repository hat noch keinen initialen Commit; es wurde kein Worktree oder Commit erzeugt. Bereits vorhandene Änderungen an `composer.json` wurden erhalten.
- Für die Integration ist die laufende Shopware-Version 6.7.14.1 maßgeblich. Die Lockdatei des lokalen Projektkopfes nennt noch eine ältere Release-Candidate-Version; sie wurde nicht geändert.
- Das bestehende Core-Navbar-Plugin markiert aktive Links anhand der aktuellen Hauptseite. Dadurch bleiben aktive Zustände bei gemeinsam gecachten Header-Fragmenten korrekt. Ohne JavaScript bleiben die Links bedienbar; die dynamische Markierung entfällt.
- Ein zusätzliches lokales Stylesheet erhält die Navigation ohne JavaScript. Der Such-Sprunglink wurde entfernt, da sein Ziel im Theme nicht existiert.
- Der Core-Warenkorbcontroller bleibt als unsichtbares Element außerhalb des Headers erhalten. Ohne diesen Controller verhindert Shopwares normales AddToCart-Plugin das Hinzufügen trotz sichtbarem Kaufbutton. Dieses Verhalten wurde zunächst reproduziert und anschließend erfolgreich geprüft.
- Die Anpassung wurde durch Syntax-, Build-, Render- und Browserprüfungen verifiziert. Eine zusätzliche Testbibliothek wurde nicht installiert.

## Umfang der Prüfung

Eine unabhängige Codeprüfung fand drei relevante Punkte an Footerlinks und Bedienkontrasten; alle wurden korrigiert und durch Render-/Browserprüfungen bestätigt. Authentifizierte Kundenabläufe wurden nicht vollständig durchlaufen; die Addressdialog-Kontraste wurden anhand des vorhandenen Core-Markups im Browser geprüft. Eine Integration mit einem zusätzlichen Consent-Anbieter ist nicht Bestandteil des Themes.

`plugin:refresh` meldet zusätzlich vorhandene, unvollständige andere Pluginverzeichnisse ohne lesbare `composer.json`. Das Sidequest Theme wurde dennoch erkannt und erfolgreich installiert. Diese anderen Plugins wurden nicht repariert.
