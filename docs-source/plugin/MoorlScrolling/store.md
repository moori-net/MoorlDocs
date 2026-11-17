**Wichtiger Hinweis:** Sie benötigen das Foundation Plugin, welches Ihnen kostenlos zur Verfügung steht: [Foundation](https://store.shopware.com/de/search?search=MoorlFoundation)


## Produktlisten in beide Richtungen durchstöbern

Mit MoorlScrolling laden deine Kunden weitere Produkte direkt in einer Kategorie oder in den Suchergebnissen. Entscheide getrennt für vorherige und nachfolgende Seiten, ob das Nachladen manuell oder automatisch erfolgen soll. Optional werden benachbarte Seiten bereits im Hintergrund vorbereitet.

Die Erweiterung nutzt die vorhandenen Shopware-Produktlisten. Filter, Sortierung und klassische Seitennavigation bleiben Teil des Einkaufsablaufs. Für die Konfiguration werden keine zusätzlichen Datenbanktabellen benötigt.

## Manuelles Nachladen oder Infinite Scroll

Ein Nachladelink gibt deinen Kunden die Kontrolle, wann weitere Produkte erscheinen. Im automatischen Modus wird beim Scrollen in Richtung der Listengrenze nachgeladen; der manuelle Link bleibt ebenfalls verfügbar. Beide Richtungen lassen sich unabhängig einstellen.

Bei einem direkten Einstieg auf Seite 5 erscheinen zunächst die Produkte dieser Seite. Seite 4 kann oben, Seite 6 unten ergänzt werden. Beim Einfügen vorheriger Produkte bleibt das betrachtete Produkt an derselben Bildschirmposition.

## Vorbereitet für MoorlInterrupter

Jede nachgeladene Produktseite behält ihren eigenen Listing-Bereich. Dadurch bleiben die Seitenregeln, Positionen und responsiven Breiten von MoorlInterrupter erhalten. Störer verschiedener Seiten werden nicht zu einer gemeinsamen Produktzeile vermischt.

MoorlInterrupter ist optional. MoorlScrolling funktioniert ebenso mit Produktlisten ohne Störer.

## Vorladen und sichtbarer Fortschritt

Bereite die nächste Seite oder beide Nachbarseiten im Hintergrund vor. Sichtbar wird eine vorbereitete Seite erst beim tatsächlichen Nachladen. Vorladen lässt sich auch mit einem manuellen Nachladelink kombinieren.

Ein kompakter Fortschrittsbalken zeigt beispielsweise „24 von 120 Produkten“. Bei einem direkten Einstieg werden vorherige Seiten mitgezählt. Am Listenende bleibt der Balken mit 100 Prozent sichtbar.

## Passende Einstellungen je Verkaufskanal

Nutze globale Vorgaben und überschreibe sie bei Bedarf je Verkaufskanal. Kategorie-Listings und Suchergebnisse können getrennt aktiviert werden. Ebenso lassen sich das Ladeverhalten, die Vorladung, die Seitennavigation und die Aktualisierung der Seitenadresse beim Scrollen konfigurieren.

Konfigurierbare Grenzen steuern, wie viele Seiten automatisch und insgesamt in einem Bereich eingefügt werden. Standardmäßig pausiert die Automatik nach drei Seiten je Richtung und ein Bereich umfasst höchstens 20 Seiten. Mit dem Wert 0 lässt sich die jeweilige Grenze aufheben. Weitere Produkte bleiben über reguläre Seitenlinks erreichbar.

## Navigation und Fehlerbehandlung

Bereits eingebundene Seiten werden direkt angesprungen. Ein Sprung zu einer anderen Seite beginnt dort einen neuen Bereich. Filter-, Sortierungs- und Seitenlimitänderungen starten die Liste auf Seite 1 neu. Bei Ladefehlern bleiben angezeigte Produkte nutzbar; Kunden können die Anfrage wiederholen oder die reguläre Shopseite öffnen.

MoorlScrolling unterstützt ein primäres Kategorie- oder Suchlisting je Dokument in Shopware 6.7 mit Storefront. Wishlist, Produktslider, Cross-Selling und mehrere unabhängige Listings gehören nicht zum Funktionsumfang. Eigene Themes und Erweiterungen mit Listing-Overrides benötigen einen gemeinsamen Funktionstest.
