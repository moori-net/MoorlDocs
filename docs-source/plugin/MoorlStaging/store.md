## Updates und Änderungen zuerst im Testshop prüfen

Mit MoorlStaging erstellen und verwalten Sie Testumgebungen direkt in der Shopware-Administration. Eine eigene Datenbank und ein eigenes Shopverzeichnis bilden die Grundlage, um Shopware-Updates, Erweiterungen und Konfigurationsänderungen vor dem Einsatz im Produktivshop zu prüfen.

Der Ablauf ist in drei Tabs gegliedert: Im Dashboard halten Sie den Testzweck fest, unter **System & Datenbank** prüfen Sie Server und Zielverbindung, und unter **Staging erstellen** konfigurieren und starten Sie die Kopie. Erst wenn beide Prüfungen erfolgreich sind, wird die Erstellung freigeschaltet.

## Fünf Schritte mit Kontrolle über Daten und Dateien

Die Erstellung läuft in fünf nachvollziehbaren Schritten: Datenbank sichern, in die Zieldatenbank importieren, Shopdateien kopieren, Symlinks setzen und Zielshop konfigurieren. Fortschritt und Status zeigen den laufenden Schritt; bei einem gemeldeten Schrittfehler stoppt der Gesamtlauf. Einzelne Schritte können gezielt erneut ausgeführt werden.

Warenkörbe, Logeinträge, Bestellungen, Kunden, SEO-URLs und Suchbegriffe lassen sich beim Datenbankexport ausschließen. Zusätzliche Tabellen können Sie zeilenweise angeben. Dateiausschlüsse mit Platzhaltern, Optionen für Cache und Versionskontrolle sowie anpassbare Dateirechte unterstützen die Einrichtung auf Ihrem Server.

## Zielshop passend zum Test vorbereiten

MoorlStaging setzt die Zieldatenbankverbindung, kann die App-URL anpassen und stellt Verkaufskanal-Domains auf den Staging-Pfad um. Bestehende Sprach- und Unterpfade bleiben dabei erhalten. Wartungsmodus, Entwicklungsmodus, Deaktivierung aller Plugins und eine eigene Liste zum Setzen oder Entfernen von Umgebungsvariablen lassen sich konfigurieren.

Nach einem erfolgreichen Gesamtlauf finden Sie die Links zu Storefront und Administration im Dashboard. Interne Notizen helfen bei der Zuordnung von Update-Tests, Fehleranalysen und Entwicklungsständen.

## Optionale Kundenanonymisierung

Wenn Kunden und Bestellungen für Tests übernommen werden sollen, kann Schritt 5 bestimmte personenbezogene Daten in Kundenkonten, Kundenadressen, Bestellkunden und Bestelladressen durch Testdaten ersetzen. Kunden- und Bestellverknüpfungen bleiben erhalten. Die Option ist standardmäßig ausgeschaltet und arbeitet ausschließlich in der Zieldatenbank.

Bestehende Kundenpasswörter, Legacy-Zugangsdaten und Wiederherstellungseinträge werden entfernt. Vorhandene Kundenzugänge funktionieren danach im Staging nicht mehr. Dokumente, Dateien, Logs, Bewertungen, Newsletterdaten und Daten anderer Plugins werden nicht anonymisiert; auch die vorher erzeugte SQL-Sicherung bleibt davon unberührt. Der Umfang ist auf die beschriebenen Kundentabellen begrenzt.

## Lokale Befehle oder Ausführung per SSH

Wählen Sie zwischen **PHP shell**, **PHP shell via SSH**, **Symfony Process** und **Symfony Process via SSH**. SSH verbindet sich mit demselben Server auf `localhost:22`. Zugangsdaten können aus der Plugin-Konfiguration oder serverseitigen Umgebungsvariablen kommen. Die Symfony-/OpenSSH-Variante unterstützt auch Schlüsselanmeldung und prüft den bekannten Hostschlüssel.

Hosting-Profile legen Binärpfade und Anfangswerte neuer Staging-Systeme fest. Eigene Einstellungen bestehender Systeme bleiben erhalten. Bei Bedarf können Sie Pfade zu `mysql` und `mysqldump` manuell setzen und den Umfang der Protokollierung wählen.

## Voraussetzungen und Hinweise zum Betrieb

Die Erweiterung ist für Shopware 6.7 vorgesehen und benötigt eine geeignete Serverumgebung mit ausführbaren Shell-Werkzeugen, darunter `rsync`, `mysql`, `mysqldump` und `sed`. Je nach Ausführungsart sind `exec`, `proc_open`, die PHP-Erweiterung `ssh2` beziehungsweise OpenSSH und bei Passwortanmeldung `sshpass` erforderlich. Eine separate Zieldatenbank, ausreichend Speicherplatz, passende Rechte und Webserver-Regeln für den Staging-Pfad müssen vorhanden sein. MoorlFoundation wird nicht benötigt.

Medien werden standardmäßig kopiert. Wenn Sie Medien ausschließen und mit dem Live-Shop verlinken, teilen sich beide Shops dieselben Dateien; Änderungen oder Löschungen im Testshop betreffen dann auch den Live-Shop. Prüfen Sie außerdem Mailtransport, Zahlungsanbieter, Webhooks und Hintergrunddienste vor dem Testbetrieb.

Die Erweiterung erstellt Testkopien; sie bietet keinen automatischen Rücktransfer von Änderungen in den Live-Shop. Import und Wiederholung können Zieldaten überschreiben. Die Löschfunktion versucht Zieldatenbanktabellen, Kopie, Sicherung und öffentlichen Symlink zu entfernen; kontrollieren Sie das Ergebnis. Vorhandene Testumgebungen werden bei Deinstallation nicht automatisch entfernt.

Verfügbare Hosting-Profile sind keine pauschale Zusage für bestimmte Tarife. Einrichtung und Dauer hängen von Server, Datenmenge und Webserver-Konfiguration ab.
