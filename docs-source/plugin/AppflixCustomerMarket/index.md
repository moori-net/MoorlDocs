---
description: Die Erweiterung ermöglicht es, Kunden eigene Anzeigen inserieren zu lassen. Erweitern Sie Ihren Shop durch User-Generated Content und profitieren Sie von einem besseren SEO-Ranking.
tags:
  - Kleinanzeigen
  - SEO
  - Marktplatz
---

# Appflix Kleinanzeigen

Die Erweiterung ermöglicht es, Kunden eigene Anzeigen inserieren zu lassen. Erweitern Sie Ihren Shop durch User-Generated Content und profitieren Sie von einem besseren SEO-Ranking.

![Vorschau](images/preview.png)

---

## Plugin Demo

Zu diesem Plugin steht eine Storefront-Demo zum Testen bereit. Unter folgenden Link kann das Plugin getestet werden:

- [https://demo-sw67.moori.net/AppflixCustomerMarket](https://demo-sw67.moori.net/AppflixCustomerMarket)


## Plugin erwerben

Dieses Plugin kann im offiziellen **Shopware Community Store** erworben werden.

- [Shopware Community Store](https://store.shopware.com/de/search?search=AppflixCustomerMarket)


**Wichtiger Hinweis:** Sie benötigen das Foundation Plugin, welches Ihnen kostenlos zur Verfügung steht: [moori Foundation](../MoorlFoundation/index.md)


## Quickstart

Für dieses Plugin steht ein **Demo-Paket** zum Testen bereit.

Gehen Sie zu `Einstellungen` → [`Demo Assistent`](../MoorlFoundation/demo-assistant.md) und wählen Sie dort `AppflixCustomerMarket` aus.

**Hinweis:** In einigen Fällen werden neue Kategorien und Seiten zu Ihrem Shop hinzugefügt. Bitte beachten Sie, dass die Demo-Daten ausschließlich zu Testzwecken dienen. Die darin enthaltenen Bilder können urheberrechtlich geschützt sein und dürfen nicht der Öffentlichkeit zugänglich gemacht werden.


---

## Planung

### Was kann man mit diesem Plugin machen?

1. Kunden können über den Kundenbereich eigene Kleinanzeigen schalten.
2. Die Veröffentlichung einer Anzeige kann optional kostenpflichtig sein.
3. Die Kontaktdaten des Verkäufers können versteckt oder kostenpflichtig freigeschaltet werden.
4. Ein eigener Kunden-Marktplatz und eine Community können das SEO-Ranking verbessern.
5. Kleinanzeigen können durch kostenpflichtige Boosts besser platziert werden, z. B. durch eine Platzierung in einem Slider auf der Startseite.

### Was kann man nicht mit diesem Plugin machen?

1. Kleinanzeigen können nicht über den Checkout erworben werden: Die Kleinanzeigen sind keine Produkte. Interessenten müssen den Verkäufer selbst kontaktieren.
2. Kleinanzeigen können weder im Produktlisting gelistet noch in derselben Kategoriestruktur abgebildet werden.

### Sonstige Hinweise

1. Die Kleinanzeigen benötigen eine eigene Hauptkategorie, die alle Unterkategorien für die Kleinanzeigen enthält.
2. Die Eingabefelder für die Kleinanzeigen können durch benutzerdefinierte Felder und Anpassungen am Template erweitert werden.
3. Kleinanzeigen können auch im Admin angelegt und verwaltet werden.

## Ersteinrichtung

### Kategorien erstellen

Erstellen Sie eine Hauptkategorie für alle Kleinanzeigen und zum Einstieg zwei bis drei Unterkategorien.

Über die Hauptnavigation im Admin: `Kataloge` → `Kategorien`

Weisen Sie jeder Kategorie die CMS-Seite des Plugins zu: `Alle Kleinanzeigen`

### Basis-Konfiguration

Über die Hauptnavigation im Admin: `Erweiterungen` → `Meine Erweiterungen` → `Appflix Kleinanzeigen` → `Konfigurieren`

- **Aktiv:** Das Plugin ist in diesem Verkaufskanal aktiv.
- **Privater Modus:** Die Kontaktdaten des Verkäufers sind erst sichtbar, wenn der Kunde mindestens eingeloggt ist.
- **Zeige mehr Anzeigen vom Verkäufer:** Auf der Detailseite der Kleinanzeige werden optional weitere Anzeigen desselben Anbieters gelistet.
- **Kategorieseite mit allen Kleinanzeigen:** Hauptkategorie für alle Kleinanzeigen (im ersten Schritt angelegt).
- **Detailformular für Kleinanzeigen:** Optionale Felder, die bei einer Kleinanzeige angegeben werden können.
- **Boost-Optionen:** Welche Boosts sind verfügbar? (Boost Top kann mit der Standard-CMS-Seite `Alle Kleinanzeigen` sofort verwendet werden.)
- **Unterkategorien im Listing anzeigen:** Möglichkeit, im Listing nach Unterkategorien zu filtern.
- **Globale Navigation im Listing anzeigen:** Im Kategoriebaum des Listings werden alle Hauptkategorien dargestellt (nicht empfohlen).
- **Button in der Sidebar anzeigen:** Ein Button zum Erstellen einer neuen Kleinanzeige.
- **Erweiterte Suche:** [Foundation | Erweiterte Suche](../MoorlFoundation/advanced-search.md)
- **Geo-Koordinaten automatisch ermitteln:** Anhand der Adresse wird die Position bestimmt. So kann auch nach Entfernung gesucht werden. (Achtung: Falsche Adressangaben verlangsamen die Erstellung einer Kleinanzeige.)
- **Alte Kleinanzeigen entfernen:** Sobald eine Kleinanzeige älter als X Tage ist und keinen aktiven Boost hat, wird sie automatisch entfernt.
- **Kleinanzeigen nach X Tagen entfernen**
- **Anzahl kostenpflichtiger Kleinanzeigen, die ein Nutzer kostenlos veröffentlichen kann**
- **Anzahl kostenpflichtiger Kontaktanfragen, die ein Nutzer kostenlos verwenden kann**
- **Kleinanzeigen automatisch prüfen:** Wenn diese Option aktiv ist, werden die Kleinanzeigen automatisch geprüft und freigegeben. Andernfalls muss der Shopbetreiber die Anzeigen manuell freigeben.
- **Freigabemethode**
- **Links entfernen:** Wenn diese Option aktiviert ist, werden URLs aus Beschreibungen entfernt. So verhindern Sie, dass Nutzer Eigenwerbung schalten können.
- **Keyword-Blacklist:** Diese Wörter können aus der Beschreibung entfernt werden. Wörter, die Teile der eingegebenen Begriffe enthalten, werden ebenfalls entfernt.

![](images/admin-config-1.png)
![](images/admin-config-2.png)
![](images/admin-config-3.png)
![](images/admin-config-4.png)

### Anzeigentypen erstellen

![](images/admin-ad-type-1.png)

Über die Hauptnavigation im Admin: `Einstellungen` → `Kleinanzeigen Typen` → `Hinzufügen`

![](images/admin-ad-type-2.png)
![](images/admin-ad-type-3.png)
![](images/admin-ad-type-4.png)
![](images/admin-ad-type-5.png)
![](images/admin-ad-type-6.png)

#### Stammdaten

- **Name:** Der Name des Typs
- **Alias:** Technischer Name / Kurzform
- **Ablaufzeit:** Zeitraum, nach dem eine Kleinanzeige gelöscht wird
- **Beschreibung:** Kurze Beschreibung des Typs
- **Aktiv:** Typ ist aktiv
- **Priorität:** Höhere Priorität = weiter oben gelistet
- **Farbe:** Farbliche Hervorhebung des Typs
- **Icon:** Symbol des Typs, z. B. `fa7s|search` (Font Awesome 7 Solid → Suche)

#### Preise

- **Boost Startseite:** Preis, um die Kleinanzeige auf der Startseite darzustellen (es wird ein CMS-Listing-Element auf der Startseite benötigt)
- **Boost Slot:** Alternative zu Boost Startseite
- **Boost Top:** Preis, um die Kleinanzeige im Listing ganz oben darzustellen (es wird ein CMS-Listing-Element auf der Listing-Seite benötigt)

Die Boosts können optional über die Pluginkonfiguration deaktiviert werden. In den Listing-CMS-Elementen, die z. B. auf der Startseite oder über dem Haupt-Listing platziert werden, gibt es für alle drei Boosts einen entsprechenden Filter, der aktiviert werden muss. Eine Einheit entspricht 24 Stunden.

- **Angebot:** Preis zum Freischalten der Kontaktdaten des Käufers (einmalig)
- **Veröffentlichung:** Preis zum Veröffentlichen einer Kleinanzeige (einmalig)

### Kleinanzeigen erstellen (Admin)

![](images/admin-ad-01.png)

Über die Hauptnavigation im Admin: `Kunden` → `Kleinanzeigen` → `Hinzufügen`

#### Stammdaten

- **Name:** Der Name der Kleinanzeige
- **Typ**
- **Auto increment:** Zähler (wenn im Storefront eine Kleinanzeige angelegt wird, werden die Medien im Ordner `Kleinanzeigen` → `Zählernummer` gespeichert)
- **Kurzbeschreibung**
- **Beschreibung**
- **Keywords**
- **Herstellernummer**
- **EAN**
- **Aktiv**
- **Freigegeben:** Die Kleinanzeige wurde freigegeben (automatisch oder manuell)
- **Verfügbar:** Die Kleinanzeige ist verfügbar
- **Veröffentlicht:** Die Kleinanzeige ist veröffentlicht
- **Boosting:** Ablaufdatum und Uhrzeit des jeweiligen Boostings
- **Kontaktinformationen zum Verkäufer**
- **Firmenname:** Wenn der Verkäufer gewerblich verkauft
- **Medien:** Bilder zur Kleinanzeige
- **Medienordner:** Medien-Uploads im Storefront werden in diesem Ordner gespeichert
- **Ist gewerblich:** Wenn der Verkäufer gewerblich verkauft
- **Impressum:** Pflichtangabe bei gewerblichen Verkäufern

#### Adresse

- **Adresse:** Vollständige Adresse des Verkäufers bzw. der Kleinanzeige
- **Geo-Koordinaten:** Werden automatisch ermittelt, wenn `Auto Location` aktiviert ist

#### Preis

- **Preis:** `0` steht für `kostenlos`

#### SEO

- **Metaangaben:** Titel, Beschreibung und Keywords
- **SEO-URLs:** SEO-URLs zur Kleinanzeige

![](images/admin-ad-02.png)
![](images/admin-ad-03.png)
![](images/admin-ad-04.png)
![](images/admin-ad-05.png)
![](images/admin-ad-06.png)
![](images/admin-ad-07.png)
![](images/admin-ad-08.png)
![](images/admin-ad-09.png)
![](images/admin-ad-10.png)
![](images/admin-ad-11.png)
