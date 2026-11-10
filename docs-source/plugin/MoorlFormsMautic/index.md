# Flow Builder Aktion | Mautic Formular

Mit diesem Add-On für [Formular Baukasten 2](../MoorlForms/index.md) kannst du zugeordnete Formular- oder Flow-Daten an ein vorhandenes Mautic-Formular senden. Voraussetzung sind Foundation und für die Formularintegration das Basisplugin MoorlForms.

## Was ist Mautic?

Mautic ist eine Open-Source-Software für die Marketing-Automation. Mit Mautic lassen sich Website-Besucher tracken und mithilfe von Formularen in identifizierte Kontakte wandeln.

## Einrichtung

Die externen Menüangaben und Bilder dieser Anleitung stammen aus Mautic Version 4. Sie sind historische Beispiele und wurden nicht gegen eine aktuelle Mautic-Oberfläche geprüft. Eine vorhandene Mautic-Installation wird vorausgesetzt.

### Mautic API aktivieren

- Klicke oben rechts auf das Zahnrad
- Es öffnet sich auf der rechten Seite eine Navigation, klicke auf "Configuration"
- Klicke in der linken Navigation auf "API Settings"
- Aktivere die API und "HTTP basic auth"

Mit dieser methode kannst du dich mit deinem Benutzernamen und deinem Passwort mit der API verbinden. Ich empfehle für diesen Fall einen weiteren Admin anzulegen, der nur für die API bestimmt ist.

![](images/mautic-001.jpg)

### Einen Mautic client in Shopware anlegen

- Navigiere zu "Einstellungen" -> "Erweiterungen" -> "moori Clients"
- Erstelle einen neuen Client vom Typ „Mautic“ (technisch `api-mautic`)
- Gebe die URL, Benutzernamen und Passwort ein, hinter der URL darf kein "/" stehen
- Teste den Client

![](images/mautic-002.jpg)

### Erstelle ein Formular in Mautic

- Navigiere vom Hauptmenü in Mautic zu "Components" -> "Forms"
- Erstelle ein neues Formular vom Typ "Campaign Form"
- Gebe die Basisdaten ein und erstelle die Eingabefelder
- z.B. E-Mail, Vorname und Nachname
- Bei den Eingabefeldern kannst du im Reiter "Contact Field" eine Zuweisung machen z.B. "Email"

Die Kontaktfeldzuordnungen und Aktionen dieses Mautic-Formulars bestimmen, wie eingehende Daten Kontakten zugeordnet werden und welche weiteren Abläufe entstehen.

![](images/mautic-003.jpg)

### Mautic Formular mit Formular Baukasten 2 Formular verbinden

- Öffne dein Formular im Shopware Admin
- In den Formulareinstellungen wählst du bei „Formular Aktionen“ **An Mautic-Formular senden** aus
- Öffne den Reiter **Mautic** in den Formulareinstellungen
- Wähle deinen Mautic Client aus
- Wähle dein in Mautic erstelltes Formular aus
- Ordne die verfügbaren Zielfelder direkt in der zentralen Mappingtabelle zu
- Verwende technische Formularfeldnamen mit `.value`, beispielsweise `{{ email.value }}`
- Ordne weitere Felder zu und speichere das Formular

Die aktuelle Implementierung verwendet keine Mautic-Einzelzuordnung in den Elementeinstellungen. Die älteren Bilder unten dienen als Beispiele.

![](images/mautic-004.jpg)

![](images/mautic-005.jpg)

![](images/mautic-006.jpg)

## Verbindung mit dem Flow Builder

Öffne einen Flow mit einem `MailAware`-Ereignis und füge die Aktion **An Mautic-Formular senden** (`action.send.mautic`) hinzu. Wähle Client und Mautic-Formular aus und ordne die Zielfelder in der Mappingtabelle zu. Verwende die Daten des gewählten Ereignisses, z. B. `{{ contactFormData.email }}` beim passenden Kontaktformularereignis, und speichere die Aktion.

## Authentifizierung, Mapping und Grenzen

Die Formularaktion heißt `mautic-form`. In `config.mautic` liegen `clientId`, `formId`, `mapping`; neue Einstellungen beginnen mit `null`, `null`, `[]`. Der Foundation-Client enthält `baseUrl`, `userName` und `password`.

Die Formularliste wird mit **HTTP Basic Auth** über `{baseUrl}/api/` gelesen. Der Verbindungstest des Foundation-Clients liest Kontakte. Die eigentliche Formularübermittlung verwendet dagegen `escopecz/mautic-form-submit` mit Basis-URL, Formular-ID und gemappten Daten; die REST-Zugangsdaten werden an diesen Submission-Aufruf vom Plugin nicht weitergegeben.

Zielfeldnamen stammen aus den Aliasnamen des Mautic-Formulars. Mappingwerte werden per Twig gerendert. Leere Zuordnungen werden ausgelassen, auch reiner Text `0` nach PHPs Leerprüfung. Ohne Client-ID, Formular-ID oder Mapping wird nicht gesendet. Twig-/Submission-Fehler werden von der Integration nicht abgefangen; eine pauschal fehlerlose oder stille Verarbeitung ist nicht zugesagt.

Es gibt keine eigene Dateiübertragung, Kampagnenverwaltung oder automatische Seitennachladung. Die zahlreichen Klassen unter `src/Api` sind API-Helfer und keine separat registrierten Shopware-Features. Der erste erfolgreich initialisierte Client bleibt im Service erhalten; mehrere unterschiedliche Clients in einem Service-Lebenszyklus erfordern eine gesonderte Prüfung.

## Test

Prüfe nach einer bewusst durchgeführten Übermittlung im vorgesehenen Testsystem die Formularergebnisse und Feldwerte in Mautic. Kontaktanlage oder -aktualisierung sowie E-Mails hängen von dessen Formularaktionen und Kontaktfeldzuordnungen ab; eine E-Mail nach jeder Übermittlung ist keine Plugin-Garantie.

![](images/mautic-007.jpg)
