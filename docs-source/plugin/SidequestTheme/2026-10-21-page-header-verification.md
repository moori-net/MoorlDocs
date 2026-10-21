# Gemeinsamer Seitenkopf: Prüfung vom 21.10.2026

Die Prüfung verwendet Shopware 6.7.14.1 mit separaten Quellkopien von SidequestTheme und MoorlTicketVendor unter `var/testing/TvHeroTest` sowie der ausdrücklich benannten Datenbank `moorl_tv_volunteer_20261021_test`. Testdaten und Theme-Zuordnungen liegen in zurückgerollten Testtransaktionen. Die laufende Shopdatenbank und bestehende CMS-Inhalte wurden nicht verändert.

Vier Theme-Integrationstests prüfen die tatsächliche Shopware-Template-Vererbung: Startseite und Kategorie mit ihren eigenen übersetzten Feldern, Fallback bei fehlenden Metadaten, Login mit erhaltenen Core-Formularen sowie Eventdetails mit und ohne CMS-Detail-Element. Das CMS-Beispiel verwendet denselben Foundation-Block wie das ausgelieferte Ticket-Layout. Doppelte automatische Kategorienamen und gemappte Beschreibungen sind ausgeschlossen. Ergebnis: 4 Tests, 48 Assertions, keine Fehler.

Die vollständige Ticket-Vendor-Suite umfasst zusätzlich 308 Tests. Sie prüft auch die Darstellung ohne zugewiesenes Sidequest-Theme. Sie meldet sieben bestehende Core-/Foundation-Deprecations.

Die vollständigen Theme-Styles wurden mit Shopwares nativer SCSS-Kompilierung kompiliert, ohne Theme-Dateien des laufenden Verkaufskanals zu veröffentlichen. Kategorie, Event und Login wurden aus echten Testantworten mit diesen Styles als eigenständige HTML-Vorschauen gerendert. Für die Vorschauen wurden Schrift und Beispielbilder lokal eingebettet; JavaScript wurde dabei entfernt. Die Browserprüfung ist eine Darstellungsprüfung, keine erneute Funktionsprüfung aller Formulare.

Chrome bestätigt bei 375 und 1440 Pixeln jeweils einen gemeinsamen Header, geladene Space Mono, die Akzentfarbe `rgb(136, 255, 3)` und keinen horizontalen Überlauf. Die Titelgröße beträgt 40 beziehungsweise 68 Pixel, die maximale Headerbreite 832 Pixel. Lange Eventtitel und ein Datumsbereich über Mitternacht wurden berücksichtigt. Screenshots liegen im Entwicklungsprojekt unter `var/testing/sidequest-header-previews/`.

Der gemeinsame Header übernimmt keine frei gestalteten CMS-Heros und löscht keine statischen CMS-Texte. Solche Inhalte bleiben redaktionell pflegbar. Zur Übernahme im laufenden Shop sind das normale Leeren des Caches und die Theme-Kompilierung erforderlich.

## Nachtrag: Übernahme in die laufende Entwicklungsinstanz

Die neue Theme-Komponente war zunächst nur im Windows-Projekt und der isolierten Testkopie vorhanden. In der laufenden Docker-Instanz fehlten die neuen Theme-Dateien; ein Cache-Clear konnte sie deshalb nicht aktivieren. Die zehn betroffenen Theme-Dateien wurden anschließend gezielt nach `custom/plugins/SidequestTheme` übertragen und ihre Eigentümer auf `www-data:www-data` gesetzt. Die Ticket-Header-Blöcke waren dort bereits vorhanden.

Das Theme wurde für den vorhandenen Sidequest-Verkaufskanal synchron kompiliert und anschließend der Cache geleert. Startseite, Kategorie, Event und Login unter `http://localhost` liefern HTTP 200 und jeweils genau einen gemeinsamen Header. Die neue CSS-Datei wird mit aktualisiertem Theme-Pfad ausgeliefert. Acht Browserprüfungen am tatsächlichen Shop bei 375 und 1440 Pixeln bestätigen Schrift, Farbe, Headerbreite und fehlenden horizontalen Überlauf. Es wurden keine Migrationen ausgeführt oder CMS-/Eventinhalte geändert.

Nachbesserung der Breadcrumb-Position: Der Kategorienkopf steht vor dem geerbten Block `cms_breadcrumb`. Die native Breadcrumb wird genau einmal direkt darunter ausgegeben. Die Theme-Suite besteht mit 4 Tests und 50 Assertions; Home und Kategorie wurden anschließend auch im laufenden Shop mit HTTP 200 und korrekter Reihenfolge bestätigt. Die Template-Datei wurde in den Container übernommen und der Cache geleert; Styles waren unverändert.

Breadcrumb nach Kategorieebene: Auf Home und direkten Kindern des Navigationseinstiegs entfällt der gesamte Container. Unterkategorien behalten die Breadcrumb direkt unter dem Header. Die Prüfung berücksichtigt die Zuordnung des Verkaufskanals. Die Theme-Suite besteht mit 4 Tests und 62 Assertions; alle drei Fälle wurden anschließend auch im laufenden Shop mit HTTP 200 bestätigt. Template übertragen und Cache geleert; kein neuer Style-Build erforderlich.

Account-Schaltfläche: Der Accountlink steht als eigene Aktion außerhalb der Navigationsliste und übernimmt die grüne Fläche sowie das transparente Hover-/Fokusdesign des Tickets-Buttons der Referenz. Template und SCSS wurden in den laufenden Container übertragen, das Theme kompiliert und der Cache geleert. Chrome bestätigt bei 320, 375, 768, 991, 992 und 1440 Pixeln genau eine sichtbare Schaltfläche ohne horizontalen Überlauf, das Linkziel `/account` und die korrekten Grund- und Hoverfarben. Unter 992 Pixeln wurde dafür das Menü über seinen tatsächlichen Toggle geöffnet. Screenshots und Messwerte liegen unter `var/testing/sidequest-account-button-check/`.
