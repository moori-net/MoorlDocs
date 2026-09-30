---
description: Hier findest du viele nützliche Tipps und Tricks für die Einrichtung deiner individuellen Formulare in Shopware 6.
tags:
- Formulare erstellen
- Anleitung
---

# Formular Baukasten 2 | Anleitungen

## Formular in Twig Template einbauen

**Basis Version**

Für Theme-Entwickler und Programmierer gibt es ein spezielles Twig-Snippet, um selbst erstellte Formulare direkt in ein Template einzubinden.

Nutze dazu das einfach das Snippet ``{% fb_form 'new_form' %}``.

Du kannst den technischen Namen oder die exakte ID des Formulars als Parameter übergeben.

## In Eingabefeldern SVG Icons nutzen

**Basis Version**

Du kannst SVG Icons innerhalb der Eingabefelder nutzen. Dazu liefert das moori Foundation Plugin bereits passende SVG Icons aus dem FontAwesome 5 Paket.

![](images/how-to-01.jpg)

Gib dazu `icon|<pack>|<name>` ein.

- pack: Name des Icon-Pakets, z.B. far, fas, fab (FontAwesome 5), fa6r, fa6s, fa6b (FontAwesome 6) oder default (Shopware)
- name: Name des Icons

Um den passenden Namen zu ermitteln, gehe dazu auf folgende Seiten:

- FontAwesome 5: [https://fontawesome.com/v5/search](https://fontawesome.com/v5/search)
- FontAwesome 6: [https://fontawesome.com/v6/search](https://fontawesome.com/v6/search)
- FontAwesome 7: [https://fontawesome.com/v7/search](https://fontawesome.com/v7/search)
- Shopware: [https://developer.shopware.com/resources/meteor-icon-kit/](https://developer.shopware.com/resources/meteor-icon-kit/)

![](images/how-to-02.jpg)

## Datenbank mit Formularen befüllen

**Basis Version**

Du kannst mithilfe des Formular Baukasten 2 selbst Datenbank-Einträge in Shopware 6 schreiben.

Dazu stehen dir nützliche Features zur Verfügung. Gehe dazu in den Formular-Einstellungen in den Reiter "Zuweisung" und wähle eine Tabelle aus.

![](images/how-to-10.jpg)

Anschließend kannst du ein Eingabefeld zu einer Tabellenspalte zuweisen.

![](images/how-to-11.jpg)

Bitte achte darauf, dass du Pflichtfelder entsprechend kennzeichnest.

Du findest hier ein Beispiel-Formular: [Entity Mapping Formular](examples/entity-mapping-form.json)

## Absende-Button individualisieren

**Basis Version**

Du kannst dem Absende-Button eigene Stylesheet-Klassen geben.

Gehe dazu in den Reiter "Stylesheet" und füge entsprechend die gewünschten Klassen ein.

![](images/how-to-09.jpg)

## Twig und Kontext Variablen als Standardwert verwenden

**Basis Version**

Wenn der Kunde zum Beispiel eine Produktanfrage stellen möchte, erleichtert es ein wenig Arbeit, wenn die Produktnummer im Formular bereits ausgefüllt ist. Viel besser ist es, wenn ein bereits eingeloggter Kunde seine persönlichen Daten nicht erneut im Formular ausfüllen muss.

Dazu kannst du im Feld "Standardwert" einfach eine Twig-Variable einfügen.

Folgende Beispiel Variablen könntest du verwenden
```html
{{ context.customer.email }}
{{ page.product.productNumber }}
```

![](images/form-builder-use-twig-variable-as-default-value.jpg)

!!! note

    Alle Variablen die den Begriff "context" enthalten, sind meistens persönliche Kundendaten. Das Plugin lädt diese Variablen asynchron nach, alle anderen Variablen werden im HTTP-Cache gespeichert.

## Produkt Anfragen nur für Produkte, die nicht lagernd sind

**Produkt-Anfrage Add-On**

Mit dem Produkt-Anfrage Add-On kannst du mithilfe der dynamischen Produktgruppe passende Formulare zuweisen.

![](images/how-to-03.jpg)

Lege eine neue dynamische Produktgruppe mit der Regel `Lagerbestand ist kleiner als 1` an.

![](images/how-to-04.jpg)

Deaktiviere den "In den Warenkorb" Button, dein Kunde kann nun Alternativ das Produkt anfragen.

![](images/how-to-05.jpg)

In den Formular-Einstellungen machst du eine Zuweisung für die dynamische Produktgruppe.

## Custom-Felder für Newsletter-Anmeldungen schreiben

**Classic Add-On**

Mit dem Element "Verschachtelte Felder" lassen sich strukturierte Eingabefelder nutzen. Damit kannst du unter anderem auch Custom-Felder für die Newsletter-Anmeldung schreiben.

In Shopware selbst kommen strukturierte Eingabefelder unter anderem auch in den Adressen der Kunden-Registrierung vor.

![](images/how-to-06.jpg)

Verwende das Element "Verschachtelte Felder" und nutze den technischen Namen `customFields`. Darin erstellst du weitere Eingabe-Elemente.

![](images/how-to-07.jpg)

In der HTML Ansicht des Formulars sehen wir nun wie das Eingabe-Element benannt ist.

![](images/how-to-08.jpg)

Sofern die Daten valide eingegeben wurden, ist die Spalte `custom_fields` mit den richtigen Daten befüllt.

!!! note

    Diese Funktion unterstüzt ausschließlich Eingaben vom typ `string` und `boolean`.