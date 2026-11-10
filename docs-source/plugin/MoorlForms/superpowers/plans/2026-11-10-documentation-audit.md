# MoorlForms Pluginfamilie: Dokumentationsabgleich

**Ziel:** Funktionen aller 13 lokalen `MoorlForms*`-Plugins anhand ihrer tatsächlichen Registrierung und Ausführung dokumentieren, Abweichungen korrigieren und echte Admin-Aufnahmen in 1920 × 1080 erstellen.

**Vorgehen:** Die Basis wird zusammen mit der zentralen Feature-Dokumentation geprüft. Drei unabhängig bearbeitete Add-on-Gruppen liefern Quellenprüfung, korrigierte Handbücher und je Plugin eine `CODEX.md`. Admin-Aufnahmen und abschließende Integration erfolgen zentral.

**Rahmen:** Shopware 6.7, PHP/Symfony/DAL, Vue-Administration, Twig und Storefront-JavaScript. Die Benutzeranweisung autorisiert Prüfung und Dokumentationsänderungen bereits. Keine Veröffentlichung oder Installation ist Teil dieses Auftrags.

## Anforderungen

- Bestehende Änderungen erhalten; jedes Plugin besitzt ein eigenes Repository.
- Registrierte Services, Routen, Admin-Komponenten, Templates und Laufzeitpfade zusammen prüfen.
- Alle Funktionen in `docs/all-features.md` und dessen englischer Fassung zusammenführen.
- Vorlagen `*.tpl.md` mit korrigieren, damit spätere Generierung Änderungen erhält.
- Je Plugin `CODEX.md` als technische Orientierung mit Quellen, Grenzen und Prüfstand erstellen/aktualisieren.
- Admin-Screenshots sind echte Browseraufnahmen mit 1920 × 1080 Pixeln; keine nachgebildeten Ansichten.
- Quellcodebefunde, sichtbare UI und getestete End-to-End-Funktionen unterscheiden.
- Keine Formulare absenden, externen Integrationen auslösen oder Produktivdaten ändern, um Dokumentation zu illustrieren.
- Dokumentationsabweichungen korrigieren; darüber hinaus entdeckte Implementierungsfehler mit Quelle und Auswirkung festhalten.

## Arbeitspakete

- [x] Pluginbestand und Ausgangsstatus aller Repositorys erfassen.
- [x] Basis: Registrierung, Validierung, Aktionen, Datenmodell, Admin, Storefront, Import/Export und Konfiguration abgleichen.
- [x] Classic, Popup und Slides: Quellen, Handbücher und `CODEX.md`.
- [x] Customer, CustomProducts, Order und Product: Quellen, Handbücher und `CODEX.md`.
- [x] Csv, Hubspot, Mautic, Webhook und Example: Quellen, Handbücher und `CODEX.md`.
- [ ] Admin-Zugang und geladene Pluginstände prüfen; relevante Seiten aufnehmen und mit Quellen abgleichen.
- [x] Zentrale deutsche und englische Feature-Dokumentation und Einstiegsvorlagen aktualisieren.
- [x] Nachweisbare Abweichungen, Screenshot-Metadaten und verbleibende Prüfgrenzen dokumentieren.
- [x] Links, Bilder, Bildabmessungen, Git-Diffs und geeignete vorhandene Tests prüfen.

## Prüfschwerpunkte

- Eine vorhandene Klasse ist ohne Registrierung kein verfügbares Feature.
- Add-on-Metadaten und Handbuchversprechen müssen zum tatsächlichen Verarbeitungspfad passen.
- Sichtbare Einstellungen garantieren keine vollständige Backend-Validierung.
- API-/CRM-Integration wird durch Quellcodeprüfung und Admin-Sichtbarkeit nicht als erfolgreich zugestellt getestet.
- Historische Bilder und nicht gebaute Admin-Erweiterungen dürfen nicht als aktueller UI-Nachweis gelten.

## Ergebnisse

Die konkreten Befunde stehen nach Abschluss in `docs/plugin-audit.md`, die Feature-Übersicht in `docs/all-features.md`, technische Einzelheiten in der jeweiligen `CODEX.md`.

Die Anmeldung ist erfolgreich. Die 30 Adminansichten wurden nach vollständigem Browser-Neuladen erneut ausschließlich auf Englisch aufgenommen. Deutsche FHD-Varianten und alte Diagnosebilder wurden auf Benutzerwunsch entfernt. Beide Handbuchsprachen und Galerien nutzen die neuen englischen Bilder. Die vollständige visuelle Add-on-Abnahme bleibt wegen deaktivierter/nicht registrierter Add-ons offen. Keine Plugins installiert/aktiviert, kein Demoimport oder Versand.
