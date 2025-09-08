---
description: Dieses Plugin bietet eine nahtlose und unabhängige Integration zu der EBICS-Schnittstelle Ihrer Hausbank. Automatischer Abgleich von SEPA-Lastschriften und Zahlungen via Vorkasse.
tags:
  - EBICS
  - Banking Software
  - SEPA
  - Lastschrift
  - Vorkasse
  - Rechnung
---

# EBICS 3.0 BankConnect

Dieses Plugin bietet eine nahtlose und unabhängige Integration zu der EBICS-Schnittstelle Ihrer Hausbank. Automatischer Abgleich von SEPA-Lastschriften und Zahlungen via Vorkasse.

![Vorschau](images/preview.png)

---

## Plugin erwerben

Das Plugin kann in den folgenden Stores erworben werden. Wenn Sie bereits einen Shopware-Account besitzen, nutzen Sie bitte **immer zuerst** den Link zum **Shopware Community Store**, da es bei alternativen Stores zu Problemen mit der Lizenzierung kommen kann. Ist ein Plugin **nicht** im Shopware Community Store verfügbar, wird es exklusiv in einem der alternativen Stores angeboten.

- [Shopware Community Store](https://store.shopware.com/de/search?search=MoorlEbics) *(empfohlen)*
- [moori Plugin Store](https://moori-plugin-store.com/MoorlEbics)
- [Shopelfen Store](https://www.shopelfen.de/) *(im Aufbau)*


**Wichtiger Hinweis:** Sie benötigen das Foundation Plugin, welches Ihnen kostenlos zur Verfügung steht: [moori Foundation](../MoorlFoundation/index.md)


---

## Ersteinrichtung

### Einrichtung der Bank

1. **Öffne die Bankeinstellungen**  
   Gehe zu **Einstellungen → EBICS Banken**.

2. **Keyring-Passwort setzen**  
   Bevor du deine Bank einrichtest, benötigst du ein globales Passwort zur Verschlüsselung deiner EBICS-Dateien:
    - Klicke oben rechts auf **Keyring-Passwort erstellen oder ändern**
    - Vergib ein **sechsstelliges Passwort**

3. **Bank hinzufügen**
    - Klicke oben rechts auf **Hinzufügen**
    - Fülle alle Pflichtfelder aus (Kunden-ID, Teilnehmer-ID, URL des EBICS-Servers etc.)

4. **Verbindung initialisieren**  
   Die Initialisierung erfolgt in mehreren Schritten:

    1. **Keyring-Datei anlegen**
        - Es wird eine verschlüsselte Schlüsselbund-Datei erstellt.

    2. **INI- und HIA-Anfrage**
        - Deine öffentlichen Schlüssel werden an die Bank übertragen.
        - **Fehler an dieser Stelle:** Prüfe, ob dein EBICS-Zugang bereits freigeschaltet ist und ob Kunden-ID & Teilnehmer-ID korrekt sind.

    3. **INI-Brief erzeugen**
        - Das Plugin erstellt ein PDF mit den Schlüssel-Hashes.
        - Dieses Dokument muss von einem berechtigten Unterzeichner unterschrieben und an die Bank übermittelt werden.
        - **Hinweis:** Bei Testzugängen ist dieser Schritt häufig nicht erforderlich.

    4. **HPB-Anfrage**
        - Die öffentlichen Bankschlüssel werden abgerufen und in der Keyring-Datei gespeichert.
        - Nach erfolgreicher HPB-Anfrage ist die Verbindung zur Bank aktiv.

> 💡 **Tipp:** Es wird immer die letzte Fehlermeldung der Bank angezeigt.  
> Sobald keine Fehlermeldung mehr erscheint, ist der Zugang erfolgreich eingerichtet.

5. **Optionale Felder**
    - Gläubiger-Identifikationsnummer für SEPA-Lastschriften hinterlegen
    - Relevante Zahlungsarten zuweisen (z. B. Vorkasse, Rechnung, SEPA-Lastschrift)

---

### Plugin-Einstellungen

- Weisen Sie den Zahlungsarten explizit ihren Verwendungszweck zu.
- Achten Sie darauf, **keine Zahlungsart doppelt** zuzuweisen.

---

### Technischer Hinweis

Das Plugin nutzt die Standard-Status von Shopware:

- `open`
- `authorized`
- `paid`
- `refunded`
- `chargeback`
- `failed`

> ❗ Benutzerdefinierte Status werden **nicht unterstützt**.

Weitere Hinweise:

- Welche Geschäftsvorfälle verfügbar sind, hängt von deiner Bank ab.  
  Nicht unterstützte Aufträge führen zu einer Fehlermeldung.
- **Direktfreigaben** für Auszahlungen (Rückerstattung) sind nur mit **Einzelunterschrift** möglich.  
  Bei 4-Augen-Freigabe ist ein externer EBICS-Client (z. B. SFirm) erforderlich.
- **SEPA-Lastschriftmandate** können nur erstellt werden, wenn eine gültige Gläubiger-Identifikationsnummer in den Bankeinstellungen hinterlegt ist.  
  Andernfalls werden Bestellungen abgebrochen.
- **Logs:** Vorgänge werden unter `var/logs/moorl_ebics_*.log` protokolliert.
