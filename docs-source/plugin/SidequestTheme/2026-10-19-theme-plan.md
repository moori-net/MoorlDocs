# Sidequest Theme Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking. Dieser Auftrag umfasst die Planung; die Umsetzung beginnt mit einem gesonderten Umsetzungsauftrag.

**Goal:** Ein minimalistisches Shopware-Theme in `custom/plugins/SidequestTheme`, das Farben, Logo, Typografie und Gestaltung von SIDEQUEST 33 übernimmt und eine einstufige Hauptnavigation ohne Suche, Account und Warenkorb im Header bietet.

**Architecture:** Eigenständiges Theme auf Basis von `@Storefront` mit gezielten Twig-Overrides und SCSS. Shopware liefert Navigation, Übersetzungen, Medien und Servicelinks; die mobile Navigation verwendet das bereits im Storefront vorhandene Bootstrap Collapse. Keine zusätzliche JavaScript-Bibliothek und keine Änderungen an Core oder anderen Plugins.

**Tech Stack:** Shopware Storefront 6.7, PHP, Twig, SCSS, Bootstrap Collapse, lokale SVG- und Schriftdateien.

**Spec:** Nutzeranforderungen und der nachfolgende Gestaltungsentwurf in diesem Dokument. Stand der Referenzanalyse: 19.10.2026.

## Ausgangslage und Grenzen

- Im Plugin liegt bisher ausschließlich `composer.json`; Plugin-Klasse, Theme-Registrierung und Storefront-Ressourcen fehlen.
- Vorhandener Namespace: `SidequestTheme\`; Plugin-Klasse laut Composer: `SidequestTheme\SidequestTheme`; Paket: `sidequest/theme`; Version: `0.7.0`.
- Das Plugin fordert `shopware/core: ~6.7.0`. Das Projekt und seine Lockdatei nennen aktuell `v6.7.0.0-rc2`. Vor einer Installation die tatsächlich laufende Version und Composer-Kompatibilität prüfen; der Plan beinhaltet kein Shopware-Upgrade und keine pauschale Lockerung der Versionsanforderungen.
- Die lokal vorhandenen Storefront-Templates verwenden Header-/Footer-Fragmente, `header.navigation.tree` und `layout/navbar/navbar.html.twig`. Diese vorhandenen Schnittstellen sind bei der Umsetzung maßgeblich; ältere Beispiele mit `page.header.navigation` nicht ungeprüft übernehmen.
- Die aktuelle `composer.json` ist bereits geändert und teilweise gestaged. Vorhandene Änderungen bei der späteren Umsetzung erhalten.
- Geplant werden das Theme und seine globale Gestaltung. Event-, Booking- und Community-Inhalte der Referenz werden nicht automatisch als neue Seiten oder CMS-Elemente angelegt.
- Das Entfernen der Header-Einstiege betrifft die Darstellung. Account-, Such- und Checkout-Routen sowie Produkt-Kaufaktionen werden dadurch nicht deaktiviert.

## Gestaltungsentwurf

### Farben und Typografie

Die folgenden Werte stammen aus dem [Stylesheet der Referenz](https://sidequest33.com/build/sidequest.css):

| Verwendung | Wert |
| --- | --- |
| Seitenhintergrund | `#100e13` |
| Headerhintergrund | `rgba(16, 14, 19, 0.94)` |
| Footerhintergrund | `#1a1620` |
| Text und Überschriften | `#f4eff7` |
| Akzent, Links und aktive Zustände | `#88ff03` |
| Sekundärtext | `rgba(244, 239, 247, 0.68)` |
| Trennlinien | `rgba(244, 239, 247, 0.2)` |
| Untere Headerlinie | `rgba(136, 255, 3, 0.2)` |

- Schriftfamilie: `"Space Mono", ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace` für Fließtext und Überschriften.
- Die Referenz bindet [SpaceMono-Regular.ttf](https://sidequest33.com/build/sidequest/fonts/SpaceMono-Regular.ttf) mit Gewicht `400` und `font-display: swap` ein. Lokale Einbindung samt passender Schriftlizenz; keine externen Font-Requests zur Laufzeit.
- Fließtext: `1rem`, Zeilenhöhe `1.7`. Überschriften: Gewicht `400`, Laufweite `-0.055em`, Zeilenhöhe `0.98`.
- H1: `clamp(2.5rem, 5vw, 4.25rem)`; H2: `clamp(1.75rem, 3.4vw, 2.75rem)`; H3: `clamp(1.25rem, 2vw, 1.5rem)`.
- Navigation: `0.75rem`, Großbuchstaben, Laufweite `0.12em`; aktiver Link und Hover mit grüner Unterstreichung.
- Gestaltung: großzügige Abstände, dünne Linien, eckige Buttons und Formularfelder, zurückhaltende Übergänge. Shopware-Produktkarten, Formulare und Dialoge auf dunkle Flächen und lesbare Zustände abstimmen.
- Das dekorative Raster und die besonders große Hero-Typografie bleiben Gestaltungsmöglichkeiten für CMS-Inhalte; sie werden nicht global auf Produkt- oder Checkout-Seiten angewendet.

### Logo und Header

- Das weiße [Original-SVG der Referenz](https://sidequest33.com/build/sidequest/images/logo-dark.svg) lokal als `logo-dark.svg` bereitstellen; trotz Dateiname enthält es weiße Pfade. Keine nachgebaute Textmarke.
- Logo über die Shopware-Theme-Medienfelder austauschbar machen, mit lokaler SVG als Standard bzw. Fallback. Seitenverhältnis erhalten, Alt-Text `SIDEQUEST 33`, Link zur Shopware-Startseite.
- Desktop ab `992px`: eine gemeinsame Zeile mit Logo links und Hauptnavigation rechts. Kein zusätzlicher Navigationsbalken und keine Topbar.
- Sticky Header wie auf der Referenz; Mindesthöhe `5.5rem` am Desktop, `4.75rem` mobil. Logobreite `clamp(9.25rem, 19vw, 12rem)`.
- Header enthält keine Suchfelder oder Suchschalter, Account-, Warenkorb- oder Wunschlisten-Aktionen. Entfernen beim Rendern über Twig, nicht nur per CSS.
- Mobil unter `992px`: Logo und beschrifteter Menübutton; darunter die ausklappbare Linkliste im Dokumentfluss. Eine gemeinsame Navigationsliste für Desktop und Mobil vermeidet doppelte Links und unterschiedliche Menüstände.
- Bootstrap Collapse übernimmt Öffnen, Schließen und `aria-expanded`. Kein paralleles Shopware-Offcanvas-Menü erzeugen. Bei deaktiviertem JavaScript bleibt die mobile Linkliste zugänglich.
- Sprachschalter und externer Ticketbutton der Referenz sind nicht Teil der genannten Anforderungen und werden zunächst nicht ergänzt.

### Einstufige Hauptnavigation

- Datenquelle ist `header.navigation.tree`: ausschließlich direkte Kinder der im Verkaufskanal gewählten Einstiegskategorie ausgeben. Unterkategorien werden nicht rekursiv ausgegeben und nicht als zusätzliche Hauptpunkte hochgezogen.
- Optionalen Startseitenlink entsprechend der Shopware-Verkaufskanaleinstellung übernehmen. Linktexte und Reihenfolge bleiben in Shopware pflegbar; Referenznamen wie „Events“ und „Booking“ nicht fest codieren.
- Keine Dropdowns, Flyouts, Untermenüpfeile oder mobile Vor-/Zurück-Navigation. Ein Hauptpunkt mit Unterkategorien verlinkt direkt auf seine eigene Zielseite.
- Ordnerkategorien ohne eigenes Linkziel nicht als funktionslose Links darstellen; gewünschte Hauptpunkte in Shopware als Seiten oder Links konfigurieren.
- SEO-URLs, externe Linkziele und „in neuem Tab öffnen“ erhalten. Aktuelle Seite mit `aria-current="page"`, übergeordneten Hauptpunkt bei Unterseiten optisch aktiv markieren.
- Bei langen Linktexten und vielen Hauptpunkten kontrollierten Zeilenumbruch erlauben; keine überlappenden Links oder horizontale Seitenüberläufe.

### Minimalistischer Footer

- Dunkle Footerfläche `#1a1620`, feine obere Linie, vertikaler Innenabstand `2rem`.
- Kompakte Zeile: links `© <aktuelles Jahr> SIDEQUEST 33`, rechts die im Verkaufskanal gepflegten Servicelinks. Auf schmalen Displays umbrechen.
- Keine mehrspaltigen Linkblöcke, Hotlineboxen sowie Zahlungs- und Versandlogo-Leisten.
- Impressum, Datenschutz und weitere für den konkreten Shop konfigurierte Serviceseiten bleiben erreichbar. Shopware-Steuer-/Versandhinweis kompakt darunter erhalten; vorhandene Consent-Einstellungen bleiben zugänglich.
- Labels über Snippets bzw. vorhandene Übersetzungen pflegen, keine fest codierten CMS-Seiten-IDs oder Domainpfade.

## Umsetzungsansatz

Empfohlen ist ein schlankes Theme mit Twig-Vererbung und eigenem SCSS. Es kontrolliert die tatsächlich gerenderte Headerstruktur und verwendet weiterhin Shopwares Daten und Seiten.

Eine reine CSS-Lösung lässt unerwünschte Aktionen und Untermenüs im Markup bestehen. Eine vollständige Kopie aller Storefront-Templates erhöht den Pflegeaufwand bei Shopware-Updates. Beide Varianten bieten hier keinen Vorteil gegenüber gezielten Overrides.

## Globale Vorgaben

- Alle Implementierungsdateien liegen unter `custom/plugins/SidequestTheme`.
- Theme basiert direkt auf `@Storefront`; keine neue Abhängigkeit von MoorlFoundation oder anderen Themes.
- Keine zusätzlichen Frontend-Abhängigkeiten und kein eigenes JavaScript-Bundle für das Menü.
- Globale Farben, Schriftfamilien und Desktop-/Mobil-Logo über die üblichen Shopware-Theme-Felder anbieten; projektspezifische Footerfarbe ergänzen.
- SCSS-Variablen vor `@Storefront`, Komponentenstyles danach laden. Die Theme-View-Reihenfolge folgt `@Storefront`, `@Plugins`, `@SidequestTheme`, sodass die Theme-Overrides wirksam sind.
- Nur tatsächlich benötigte Template-Blöcke überschreiben; keine Coredateien verändern.

## Geplante Dateien

Alle folgenden Pfade sind relativ zum Pluginverzeichnis:

| Datei | Verantwortung |
| --- | --- |
| `composer.json` | Metadaten vervollständigen; Storefront-Abhängigkeit passend zu `~6.7.0` deklarieren |
| `src/SidequestTheme.php` | Plugin-Klasse mit `ThemeInterface` |
| `src/Resources/theme.json` | Theme-Vererbung, Styles, Assets, Farben, Schrift- und Logofelder |
| `src/Resources/app/storefront/src/scss/overrides.scss` | Shopware-/Bootstrap-Variablen vor dem Storefront-SCSS |
| `src/Resources/app/storefront/src/scss/base.scss` | Einstieg für die folgenden SCSS-Komponenten |
| `src/Resources/app/storefront/src/scss/base/_typography.scss` | Lokale Schrift und Typografieregeln |
| `src/Resources/app/storefront/src/scss/layout/_header.scss` | Header und einstufige Navigation einschließlich Mobilzustand |
| `src/Resources/app/storefront/src/scss/layout/_footer.scss` | Kompakter Footer |
| `src/Resources/app/storefront/src/scss/component/_controls.scss` | Buttons, Eingaben, Fokus und dunkle Shopoberflächen |
| `src/Resources/app/storefront/src/assets/logo-dark.svg` | Original-Wortmarke |
| `src/Resources/app/storefront/src/assets/fonts/SpaceMono-Regular.ttf` | Lokale Schriftdatei |
| `src/Resources/app/storefront/src/assets/fonts/OFL.txt` | Passender Schriftlizenztext |
| `src/Resources/views/storefront/layout/header.html.twig` | Separate Standardnavigation und ungenutztes Offcanvas-Markup unterdrücken |
| `src/Resources/views/storefront/layout/header/header.html.twig` | Eine Headerzeile mit Logo, Menübutton und eingebundener Navigation |
| `src/Resources/views/storefront/layout/header/logo.html.twig` | Theme-Logomedien mit lokalem SVG-Fallback |
| `src/Resources/views/storefront/layout/navbar/navbar.html.twig` | Flache Linkliste aus Shopwares Hauptnavigation |
| `src/Resources/views/storefront/layout/footer/footer.html.twig` | Kompakter Footer mit Servicelinks und Shopware-Hinweisen |
| `src/Resources/snippet/de-DE/storefront.de-DE.json` | Deutsche zusätzliche Menü-/Footertexte |
| `src/Resources/snippet/en-GB/storefront.en-GB.json` | Englische zusätzliche Menü-/Footertexte |

## Besonders zu prüfen

1. Auf einer tiefen Kategorie- oder Produktseite zeigt das mobile Menü weiterhin die Hauptpunkte und keine Unterkategorien.
2. Auch bei aktivierter Wunschliste und angemeldetem Kunden bleibt der Header auf Logo und Navigation reduziert.
3. Fehlendes Theme-Logo, lange Navigationstitel und deaktiviertes JavaScript führen weiterhin zu nutzbarer Navigation.
4. Shopware-Formulare, Dropdowns, Fehlermeldungen und Dialoge bleiben im dunklen Design lesbar und bedienbar.
5. Konfigurierte Servicelinks, Steuer-/Versandhinweise und Consent-Bedienung bleiben trotz reduziertem Footer erreichbar.

## Umsetzungsschritte

### Aufgabe 1: Registrierbares Theme und Markenressourcen

**Dateien:** `composer.json`, `src/SidequestTheme.php`, `src/Resources/theme.json`, SCSS-Einstiegsdateien, Typografie und Assets aus der Dateiliste.

**Schnittstelle:** Shopware erkennt `SidequestTheme\SidequestTheme` als Plugin und Theme; konfigurierte Theme-Werte und veröffentlichte lokale Assets stehen den folgenden Aufgaben zur Verfügung.

- [ ] Tatsächlich laufende Shopware-/PHP-Version prüfen und Composer-Anforderungen damit abgleichen. Bestehende Änderungen in `composer.json` erhalten.
- [ ] Plugin-Klasse als `Plugin implements ThemeInterface` anlegen; Metadaten und Storefront-Abhängigkeit ergänzen.
- [ ] Original-SVG, Schrift und passenden Lizenztext lokal aufnehmen. Theme- und Schrift-Assetpfade mit Shopwares Asset-Veröffentlichung abstimmen.
- [ ] `theme.json`, Variablen und Basistypografie mit den oben festgelegten Werten anlegen. Body-/Headline-Schrift und Markenfarben auf die Standard-Theme-Felder abbilden.
- [ ] Aus dem Pluginverzeichnis `composer validate --no-check-publish` und `php -l src/SidequestTheme.php` ausführen. Erwartet: gültige Composer-Struktur und keine PHP-Syntaxfehler.
- [ ] In der Shopware-Laufzeit `php bin/console plugin:refresh` ausführen; anschließend `php bin/console plugin:install --activate SidequestTheme`, sofern es noch nicht installiert ist. Erwartet: Plugin wird ohne fehlende Klasse erkannt und aktiviert.

### Aufgabe 2: Minimalistischer Header und flache Navigation

**Dateien:** Die vier Header-/Navbar-Templates, `_header.scss` sowie die beiden Snippetdateien aus der Dateiliste.

**Schnittstelle:** Verwendet Theme-Logos und Farben aus Aufgabe 1 sowie `header.navigation.tree`; liefert einen Header mit einer Navigationsliste und Bootstrap-Collapse-Ziel.

- [ ] Äußeres `layout/header.html.twig` über `sw_extends` erweitern: `base_navigation` und `base_offcanvas_navigation` leeren. Staging-Hinweise und den vorhandenen Header-Fragmentkontext erhalten.
- [ ] Im inneren Header Logo, mobilen Button und Navbar-Include als eine Einheit ausgeben. Suche, Topbar, Account, Warenkorb und Wunschliste gar nicht rendern; dabei den Menübutton außerhalb der entfernten Standardaktionen platzieren.
- [ ] Im Navbar-Override ausschließlich die oben definierte Hauptnavigation rendern. Keine Dropdown-Attribute oder Offcanvas-Nachladeaktionen übernehmen; aktive Zustände serverseitig aus aktueller Kategorie und Navigationspfad ableiten.
- [ ] Desktop-/Mobilstyles, grüne Unterstreichung, Fokuszustände, Sticky-Verhalten und Wrap bei langen Menüs ergänzen. Mobile Links ohne JavaScript sichtbar halten.
- [ ] Manuell auf Startseite, Kategorie, Unterkategorie und Produktdetail prüfen: identische Hauptpunkte auf Desktop und Mobil, direkte Navigation zu Hauptpunkten, keine Untermenüs.
- [ ] Mit aktiviertem Wishlist-Feature und angemeldetem Kunden kontrollieren, dass keine unerwünschten Headeraktionen oder leeren Aktionsspalten vorhanden sind.
- [ ] Ohne gesetztes Theme-Logo den SVG-Fallback prüfen. Menü bei `375px`, `768px`, `991px`, `992px` und `1440px`, mit langen Titeln, Tastatur und deaktiviertem JavaScript bedienen.

### Aufgabe 3: Kompakter Footer und einheitliche Shopgestaltung

**Dateien:** Footer-Template, `_footer.scss`, `_controls.scss`, bei Bedarf bestehende Theme- und Snippetdateien.

**Schnittstelle:** Verwendet Shopwares Footer-Fragmentdaten einschließlich `footer.serviceMenu` und die Theme-Werte aus Aufgabe 1.

- [ ] Footer auf Copyright und konfigurierte Servicelinks reduzieren. Standardblöcke für Hotline, Spalten und Zahlungs-/Versandlogos entfernen; Steuer-/Versandhinweis wiederverwenden.
- [ ] Footerfläche, Trennlinie und responsive Anordnung umsetzen; Hover und Tastaturfokus im Referenzstil gestalten.
- [ ] Shopware-Buttons, Eingaben, Produktkarten und Dialogflächen anhand der gemeinsamen Farbwerte angleichen. Statusmeldungen behalten verständliche Zustände und ausreichenden Kontrast.
- [ ] Mit mehreren Servicelinks und langen Linktiteln bei `375px` prüfen: alle Links sichtbar, erreichbar und korrekt verlinkt; kein horizontaler Seitenüberlauf.
- [ ] Produktlisting, Produktdetail, Kontaktformular und Checkout stichprobenartig auf Kontraste, Fehlermeldungen, Auswahlfelder und Dialoge prüfen. Vorhandene Cookie-Einstellungen erneut öffnen.

### Aufgabe 4: Build und Abnahme

**Dateien:** Keine weiteren Produktdateien vorgesehen; nur notwendige Korrekturen aus der Abnahme.

**Schnittstelle:** Das vollständige Theme wird einem vorgesehenen Test-Verkaufskanal zugewiesen und über Shopwares vorhandene Build-Werkzeuge veröffentlicht.

- [ ] Theme im Administrationsbereich dem vorgesehenen Test-Verkaufskanal zuweisen. Haupt- und Servicenavigation dort konfigurieren; notwendige Hauptpunkte als navigierbare Seiten bzw. Links pflegen.
- [ ] In der Shopware-Laufzeit `php bin/console assets:install`, `php bin/console theme:refresh`, `php bin/console lint:twig custom/plugins/SidequestTheme/src/Resources/views`, `php bin/console theme:compile` und `php bin/console cache:clear` ausführen. Erwartet: keine Twig-/SCSS-/Themefehler. Befehle in der Umgebung ausführen, in der PHP und Datenbank des Shops verfügbar sind.
- [ ] Im Browser prüfen, dass SVG und Schrift lokal mit Status `200` laden und `Space Mono` tatsächlich verwendet wird. Keine externen Font-Requests und keine JavaScript-Fehler durch entfernte Headeraktionen.
- [ ] Startseite, Listing, Produktdetail und eine CMS-Seite bei `375px`, `768px`, `992px` und `1440px` mit der Referenz vergleichen. Zusätzlich Tastaturbedienung und `200%` Zoom prüfen.
- [ ] Abnahme dokumentieren: minimalistischer Header ohne Suche/Account/Warenkorb, eine Navigationsebene auf allen Geräten, minimalistischer Footer, Original-Logo, korrekte Farbwerte und Schrift.

Für diese visuelle Theme-Anpassung reichen gezielte Syntax-/Build-Prüfungen und die beschriebenen Browserprüfungen. Eine neue Testinfrastruktur oder Tests, die nur Twig-Quelltext vergleichen, sind nicht vorgesehen.

## Referenzen

- [Referenzseite SIDEQUEST 33](https://sidequest33.com/de/)
- [Stylesheet mit Farben, Typografie und Breakpoints](https://sidequest33.com/build/sidequest.css)
- [Original-Logo als SVG](https://sidequest33.com/build/sidequest/images/logo-dark.svg)
- [Original-Schriftdatei](https://sidequest33.com/build/sidequest/fonts/SpaceMono-Regular.ttf)
- Lokale Ausgangspunkte: `composer.json` im Plugin und Projekt sowie `vendor/shopware/storefront/Resources/views/storefront/layout/` und `vendor/shopware/storefront/Resources/app/storefront/src/main.js`.
