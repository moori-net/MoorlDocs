# Flow Builder Aktion | Webhook ausführen

Diese Erweiterung ist mit [Formular Baukasten 2](https://docs.moori.net/plugin/MoorlForms/) kompatibel

## Installation

!!! note

      Falls du Probleme mit dem Plugin hast, bitte beachte folgende [Hinweise](https://docs.moori.net/plugin/) im FAQ Bereich.

1. Installiere
   [Foundation](https://docs.moori.net/plugin/MoorlFoundation/)
2. Installiere Webhook Integration im Plugin Manager

## Einrichtung

### Webhook erstellen

Es gibt für Webhooks unzählige Anwendungsbereiche, du kannst [hier](https://webhook-test.com/) Webhooks testen.

### Beispiele

#### Benachrichtigungen auf dein Amazon Echo Gerät

https://zeropointdevelopment.com/sending-notifications-to-amazon-echo-using-webhooks/

#### Per Webhook Nachrichten in dein Discord Channel senden

https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks

### Webhook mit Flow-Builder einrichten

- Navigiere zum Flow-Builder und öffne z.B. "Kontaktformular wurde verschickt"
- Gehe in den Reiter "Flow"
- Füge die Aktion **Webhook** (`action.send.webhook`) hinzu; das Ereignis muss `MailAware` bereitstellen
- Trage die Daten deines Webhooks ein
- Tipp: Für längere Texte kannst du einen globalen Platzhalter als Template verwenden
- Der Reiter „Webhook testen“ führt einen echten Aufruf aus; verwende ihn nur für ein dafür vorgesehenes Ziel. Twig-Variablen werden dabei nicht ausgewertet

Im normalen Betrieb werden Twig-Fehler als Fehlermeldungstext in die Parameter übernommen. Fehler des HTTP-Aufrufs werden protokolliert und abgefangen; daraus entsteht keine eigene Fehlermeldung für den Endkunden. Prüfe deshalb Zuordnungen, Zielantworten und das Pluginlog. Andere Fehler beim Aufbau der Konfiguration sind davon nicht pauschal abgedeckt.

### Webhook mit Formular Baukasten 2 Formular einrichten

- Öffne dein Formular im Shopware Admin
- In den Formulareinstellungen wählst du bei „Formular Aktionen“ **Webhook aufrufen** (`webhook-form`) und öffnest den Reiter **Webhook**
- Trage die Daten deines Webhooks ein
- Tipp: Für längere Texte kannst du einen globalen Platzhalter als Template verwenden
- Verwende für Formularfelder Platzhalter mit technischem Namen und `.value`, z. B. `{{ email.value }}`
- Ein Testaufruf sendet die eingegebenen Werte ohne Twig-Auswertung an das Ziel
- Speichere das Formular

## Methoden, Body und Authentifizierung

Die Oberfläche bietet `GET` und `POST`. Standard ist `GET`, eine leere Ziel-URL, deaktivierte Authentifizierung, leere Query-/Headerlisten, Bodytyp `json` und leere Bodyparameter. Benutzername, Passwort, Rohbody und globale Vorlage beginnen mit `null`.

Nur bei `POST` wird ein Body aufgebaut:

| Bodytyp | Verarbeitung |
| --- | --- |
| `empty` | Kein eigener Body. |
| `plain` | Unveränderter Rohtext; **keine Twig-Auswertung**. |
| `json` | Gemappte Parameterwerte werden als JSON-Objekt kodiert. |
| `x-www-form-urlencoded` | Gemappte Parameterwerte werden als Formdaten gesendet. |

Query-, Header- und JSON-/Formparameterwerte werden im normalen Betrieb per Twig gerendert. Die globale Vorlage wird zuvor gerendert und kann in diesen Werten mit `{{ template }}` eingefügt werden. Die URL, Benutzername, Passwort und der Rohbody werden nicht gerendert. Leere Mappingwerte, einschließlich Text `0` nach PHPs Leerprüfung, werden ausgelassen. Es gibt keine Multipart-/Dateiübertragung.

Aktive Authentifizierung verwendet Guzzle Basic Auth mit Benutzername und Passwort. Verbindung und gesamter Aufruf haben jeweils einen festen Timeout von 10 Sekunden. Ohne Ziel-URL wird kein Request gesendet. Das Plugin implementiert keine automatische Wiederholung oder eigene Warteschlange.

## Testanzeige und Logging

Der Test ist ein echter HTTP-Aufruf ohne Template-Auswertung und bildet keine Formular-/Flow-Laufzeitdaten nach. Die Response wird bereits im Service für das Log ausgelesen; die Testanzeige kann deshalb „No content“ melden, obwohl das Ziel einen Body geliefert hat. Der Text allein ist kein zuverlässiger Erfolgsnachweis.

Plugin-Einstellung `MoorlFormsWebhook.config.loggerLevel`: Standard `400/ERROR`; verfügbar sind `100/DEBUG`, `200/INFO`, `250/NOTICE`, `300/WARNING`, `400/ERROR`, `1000/DISABLED`. Die Logdatei liegt unter `var/log/moorl_forms_webhook_<Umgebung>.log` mit rotierendem Handler.

INFO zeichnet Konfiguration, Requestoptionen und Antwort auf; Fehlerlogs können ebenfalls Konfiguration und Optionen enthalten. Zugangsdaten, Header und Nutzdaten werden nicht maskiert. Übernimm keine echten Secrets oder Kundendaten in Screenshots und Diagnoseausgaben.

Die externen Beispiele bestätigen keine aktuelle Oberfläche oder erfolgreiche Netzwerkprüfung.

## Test

Ein Beispiel für einen gesendeten Webhook.
