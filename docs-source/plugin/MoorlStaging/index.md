---
description: Ein Staging System für Shopware 6 mit nur einem Klick erstellen und wieder löschen? Dieses Plugin macht es möglich!
tags:
- Shopware 6 Plugin
- Staging
- Testsystem
---

# Staging und Testumgebungen

Ein Staging System für Shopware 6 mit nur einem Klick erstellen und wieder löschen? Dieses Plugin macht es möglich!

Dank performanter Prozesse auf Shell-Ebene, ist dieses Plugin bis zu fünfmal schneller als andere Staging Plugins!

Ein Shop mit 10.000 Produkten (inkl. Varianten) kann mit den empfohlenen Einstellungen bereits innerhalb einer Minute als Testumgebung bereitstehen. 

Du glaubst nicht? Überzeug dich selbst.

## Wofür ist dieses Plugin gut?

Shopware 6 basiert auf dem PHP Framework "Symfony" jedoch läuft das Zusammenspiel aus Shopware Core und vielen Plugins leider nicht so harmonisch ab, wie man es eigentlich erwarten sollte.

Das kann verschiedenste Ursachen haben, kleinere Fehler sind nicht weiter tragisch. Aber was passiert, wenn plötzlich der ganze Shop lahm liegt und es auch nicht so einfach ist ein Backup einzuspielen? Um dieses Szenario zu vermeiden, sollte man neue Updates auf einer Testumgebung unter die Lupe nehmen. Wenn alles läuft, kann man ohne Bedenken diese Updates auch im Live Shop installieren.

Eine Testumgebung einzurichten dauert meist bis zu einem halben Tag. Es ist nicht nur sehr Zeitintensiv, der kleinste Fehler kann zu einem enormen Datenverlust führen.

Mit diesem Plugin ist eine voll funktionstüchtige Testumgebung in unter zehn Minuten einsatzbereit und jegliche Risiken sind auf einem Minimum beschränkt.

## Installation

!!! note

      Falls du Probleme mit dem Plugin hast, bitte beachte folgende [Hinweise](../) im FAQ Bereich.

!!! note

      Die Staging Systeme werden bei Deinstallation des Plugins NICHT gelöscht.

## Einstellungen

### Systemanforderungen

- min. PHP v7.4
- php.ini: max_execution_time > 120 (größer als 2 Minuten)
- Server muss das Ausführen von Befehlen durch PHP unterstützen (Eine Liste an Anbietern
  befindet sich am Ende dieser Seite)
- Die APP_URL in der .env-Datei des Live-Systems muss richtig konfiguriert sein!

### Basiskonfiguration

In der Basiskonfiguration kannst du den Logger des Plugins aktivieren. So werden weitere Informationen zu den Prozessen in einer Logdatei gespeichert.

Du kannst diese Logdatei mit dem "Frosh Tools" Plugin einsehen.

Zudem gibt es einen Kompatibilitätsmodus für diverse Hosting Anbieter. Weitere Informationen findest du am Ende dieser Dokumentation.

### Testumgebung erstellen

Das Plugin befindet sich unter "Einstellungen" - "Erweiterungen" - "Staging".

![](images/ms-01.jpg)

Hier findest du eine Liste mit deinen Staging Systemen. Klicke oben rechts auf "Neues Staging System".

![](images/ms-02.jpg)

Nun wird ein kurzer Systemcheck ausgeführt um zu prüfen, ob das Plugin mit deinem Webserver kompatibel ist. Sollte es hier einen Fehler geben, kannst du das Plugin leider nicht nutzen und musst entweder einen anderen Webserver nehmen oder dich für ein alternatives Staging Plugin entscheiden.

Der Name deines Staging-Systems ist auch zugleich das Unterverzeichnis wo du dein Staging System erreichst. Du kannst den Namen auch leer lassen, dann wird automatisch ein Name generiert.

![](images/ms-03.jpg)

![](images/ms-04.jpg)

Im nächsten Schritt gibst du die Zugangsdaten zu der Datenbank deines Staging Systems ein. Zur Sicherheit überprüft das Plugin, ob du nicht versehentlich die Daten deiner Live Datenbank eingibst.

![](images/ms-05.jpg)

![](images/ms-06.jpg)

Wurde die Verbindung zur Datenbank erfolgreich hergestellt, kannst du nun eigene Einstellungen für Vorgänge vornehmen. Die Voreinstellungen entsprechen Empfehlungen bezüglich Performance und Datenschutz.

**Achtung**

Solltest du die Medien Verzeichnisse ausschließen, wird automatisch eine Verlinkung zu den Medien deines Live-Shops gesetzt. Das heißt, wenn du im Medien-Manager im Staging System Dateien entfernst, werden diese auch im Live-System entfernt.

![](images/ms-07.jpg)

![](images/ms-08.jpg)

![](images/ms-09.jpg)

Nun kannst du das Staging System erstellen. Die Vorgänge werden Schritt für Schritt durchlaufen.

Falls es einen Fehler gibt, kann das möglicherweise daran liegen, dass deine php.ini falsch konfiguriert ist. Hinweise dazu findest du am Anfang dieser Seite.

![](images/ms-10.jpg)

Sobald das Staging System erstellt wurde, kannst du über die Links auf Admin oder Storefront zugreifen.

![](images/ms-11.jpg)


## Hinweise zu Hosting Anbietern

Sofern der Server generell einen SSH Zugang anbietet und auf Apache basiert, sollte das Plugin problemlos funktionieren.

Server auf NGINX-Basis benötigen eine zusätzliche Konfiguration damit das Testsystem erreichbar ist.

### Allgemeine Hinweise zu Hostern mit NGINX-Webserver Konfiguration (z.B. TimmeHosting)

Aufbau der Verzeichnisse:

1. Das Hauptverzeichnis des Staging-Systems befindet sich in  
   ```<shopware_root>/_moorl_staging/<staging_name>/```

2. Die Datenbanksicherung des Staging-Systems befindet sich in  
   ```<shopware_root>/_moorl_staging/<staging_name>/backup/backup.sql```

3. Das Shopware-Verzeichnis des Staging-Systems befindet sich in  
   ```<shopware_root>/_moorl_staging/<staging_name>/shop```

4. Der Webroot des Staging-Systems befindet sich in  
   ```<shopware_root>/_moorl_staging/<staging_name>/shop/public```

5. Im Webroot des Produktivsystems wird ein Symlink zum Webroot des Staging-Systems angelegt:  
   ```<shopware_root>/_public/<staging_name>``` zeigt auf  
   ```<shopware_root>/_moorl_staging/<staging_name>/shop/public```.  
   Dieser Symlink (oder eine alternative Domain) muss in der NGINX-Konfiguration freigegeben werden.

!!! note

      Wenn eine alternative Domain im NGINX Webserver konfiguriert wird, muss die Umgebungsvariable APP_URL in ```<shopware_root>/_moorl_staging/<staging_name>/shop/.env.local``` ebenfalls angepasst werden.

### ALL-INKL.COM

Sofern keine Verbindung zu der Datenbank möglich ist, bitte die Erreichbarkeit von überall erlauben!

| Paket | Unterstützt | Hinweise |
| ----------- | ----------- | ----------- |
| ALL-INKL.COM - Privat | NEIN | |
| ALL-INKL.COM - PrivatPlus | JA | |
| ALL-INKL.COM - Premium | JA | |
| ALL-INKL.COM - Business | JA | |

### enerSpace

| Paket                      | Unterstützt | Hinweise |
|----------------------------|-------------| ----------- |
| Shopware 6 SSD Hosting     | JA | |
| Managed-SSD - Basic        | JA | |
| Managed-SSD - Medium       | JA | |
| Managed-SSD - Professional | JA | |
| Managed-SSD - Premium      | JA | |

### Profihost

In den Plugin Einstellungen Hosting Kompatibilitätsmodus auf Profihost (MariaDB) oder Profihost (MySQL) stellen. Wichtig dabei ist, dass die Staging Umgebung dieselbe Datenbank-Art (MySQL oder MariaDB) wie der Live-Shop nutzt!

| Paket | Unterstützt | Hinweise |
| ----------- | ----------- | ----------- |
| Managed Hosting | Ja | Apache Server muss neu gestartet werden |
| Managed Shop-Hosting | Ja | Apache Server muss neu gestartet werden |
| Managed Server (FlexServer) | JA | Apache Server muss neu gestartet werden |

### Hosteurope

Es wurde eine schlechte Performance beim Klonen der Datenbank beobachtet. Trotzdem ließen sich auf Hosteurope problemlos Staging Systeme erstellen.

| Paket | Unterstützt | Hinweise |
| ----------- | ----------- | ----------- |
| WebHosting - Basic | JA | |
| WebHosting - Medium | JA | |
| WebHosting - Premium | JA | |
| WebHosting - Supreme | JA | |
| WebServer - Basic SSD | JA | |
| WebServer - Medium SSD | JA | |
| WebServer - Premium SSD | JA | |
| WebServer - Supreme SSD | JA | |

### Mittwald

Dieser Provider bietet leider nicht die technische Basis, es fehlen diverse Optionen.

- Binary "rsync" ist nicht aktiviert
- PHP shell_exec() hat keine Berechtigung zum Ausführen von Binaries, welche in das Dateisystem schreiben, z.B. mysqldump
- PHP SSH Extension muss aktiviert werden, aber man kann nur den SSH root user nutzen, um Binaries auszuführen
- SSH Operationen werden nicht synchron ausgeführt, es wird nicht gewartet bis eine Operation ausgeführt wurde, stattdessen startet die nächste und verursacht Fehler
