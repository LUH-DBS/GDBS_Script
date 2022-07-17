#!/usr/bin/env python
# coding: utf-8

# # Relationaler Entwurf
# 
# Die meisten kommerziellen Datenbanken unterstützen das relationale Datenmodell. 
# In diesem Kapitel lernen wir das relationale Modell kennen und diskutieren Methoden zur Überführung von Datenspezifikationen aus dem ER-Modell ins relationale Modell.

# ## Das Relationale Modell
# 
# Im folgenden werden wir ähnlich zum ER-Modell die grundlegenden Bausteine des relationalen Modells kennen lernen. Zentrale Grundbegriffe des relationalen Modells sind Relationen und Tupel. 

# In der Mathematik ist eine Relation $R$ eine Teilmenge des Kreuzproduktes von $n$ Mengen: $R\subset A_1 \times A_2 \times \cdots \times A_n$. Ein Element der Relation ist ein n-Tupel: $\forall t \in R. t=(a_1,a_2,\cdots, a_n) \wedge a_i \in A_i$
# 
# 
# Für Datenbanken gelten die aus der Mathematik bekannten Beziehungen mit folgenden zusätzlichen semantischen Erweiterungen. 
# Die Mengen $A_i$ sind im Datenkontext Domänen bzw. Wertebereiche. Diese Wertebereiche können im allgemeinen Standarddatentypen wie Integer, String, Boolean, usw. sein oder konkrete Wertebereiche, die durch Attribute definiert werden, wie zum Beispiel ID, Name, Alter, Geschlecht. Prinzipiell entspricht eine solche Menge der Spalte einer Tabelle.
# 
# Analog bilden die Einträge der Tupel $(a_1,\cdots, a_n)$ die Datenwerten einer Tabelle, z.B. (4, Abedjan, 36, m). Ein Tupel entspricht eine Zeile einer Tabelle.

# ### Die Relation

# Konzeptuell ist eine Datenbank eine Menge von Tabellen. Jede Tabelle stellt die Daten einer Relation dar. Eine Tabelle besteht aus Spalten, die in Relation zu einander stehen. Damit beinhaltet jede Zeile Datenwerte aus den jeweiligen Domänen, die in Relation zu einander stehen. Wir werden oft Tabellen und Relationen alternierend nutzen, obwohl diese konzeptionell unterschiedliche Konzepte sind. Eie Relation ist ein mathematisches Konzept, welches aus Mengen und Tupeln zusammensetzt, während eine Tabelle ein zweidimensionales Feld bestehend aus Spalten und Zeilen ist. Es ist jedoch leicht einzusehen, dass jede Relation als Tabelle darstellbar ist. 
# 
# Rückführend auf den ersten Satz dieses Unterabschnitt stellen wir also fest, dass die Relation das einzige Konstrukt des relationalen Modells ist und folgende Vorteile sich dadurch ergeben:
# 
# - Leicht beschreibbar. Entspricht oft unserer Vorstellung der Daten.
# - Einfach in einer DB abzubilden (zwei-dimensionales Array, Liste von Arrays, usw. )
# - Relationen bilden sowohl Entitytypen als auch Relationshiptypen ab.
# - Ist das abstrakte Modell hinter SQL

# ### Elemente des Relationalen Modells

# Zentrale Elemente des relationalen Modells sind Attribute, Tupel und Schema. 
# 
# - Datenbankschema: Im groben beschreibt jedes relationale Modell ein Datenbankschema, welche aus einem oder mehreren Relationenschemata besteht. 
# - Relationenschema: Jede Relation wird durch ihr Schema identifiziert. Das Relationenschema besteht aus dem Namen der Relation und der Liste der Attribute und ihrer Domänen. In einer Tabelle entspricht die Kopfzeile dem Relationenschema. Alle weiteren (Daten-)Einträge in der Tabelle bilden die „Relation“
# - Die Relation besteht aus keinem oder mehr Tupeln. Im relationalen Modell bilden Tupel einer Relation immer eine Menge. Das heißt, dass kein Tupel in seiner gesamten Ausprägung doppelt auftauchen kann. Diese Annahme gilt in echten Datenbanksystemen nur dann, wenn ein Schlüssel vorhanden ist. 
# - Attribute entsprechen den Bezeichnern der zu einander in Relation stehenden Domänenmengen. In Tabellen entsprechen Attribute den Spaltenbezeichnern ( Überschriften). In einem Relationenschema kann ein Attribut nicht doppelt vorkommen. Das Relationenschema ist somit eine Menge.
# - Attributwert: Jeder Dateneintrag in einem Tupel entspricht dem Attributwert der jeweiligen Spalte. Attributwerte sind atomar und stammen aus einer elementaren Domäne. 
# - Ein Tupel entspricht aus einer vollständigen Kombination von Attributwerten.
# 
# In der Abbildung unten sind die jeweiligen Elemente nochmal visuell dargestellt. Wir haben Primärschlüssel und Fremdschlüssel auch bereits dargestellt. Diese sind wie bekannt aus dem ER-Modell, Attribute die referenzielle Integrität gewährleisten. Hierauf werden wir später in diesem Kapitel genauer eingehen. 

# ![title](elemente_rm.jpg)

# ### Formal

# ■ Domänen D1, …, Dn
# <br>
# <br>
# ■ Relation R $\subseteq$ D1 x … x Dn
# <br>
# <br>
# ■ Beispiel
# <br>
# □ Relationenschema: Film(Titel, Jahr, Länge, Typ)
# <br>
# □ Domänen: String, Integer, Integer, String
# <br>
# □ Tupel: (Star Wars, 1977, 124, farbig)

# ### Edgar F. Codd

# Promotion an der University of Michigan Ann Arbor
# <br>
# Entwicklung des Relationalen Modells bei IBM (Almaden)
# <br>
# „A Relational Model of Data for Large Shared Data Banks" (1970)
# <br>
# Artikelserie
# <br>
# Literaturhinweis:
# <br>
# The Database Relational Model: A Retrospective Review and Analysis:
# <br>
# A Historical Account and Assessment of E. F. Codd's Contribution to the Field of Database Technology
# <br>
# Chris J. Date
# <br>
# ISBN: 0-201-61294-1 (9.99 EUR)

# #### Beiträge von Codd

# ■ Transformation des Datenmanagement zu einer Wissenschaft
# <br>
# □ Entsprechende Klarheit und Strenge
# <br>
# <br>
# ■ Nicht nur das relationale Modell, sondern überhaupt das Konzept eines Datenmodells
# <br>
# □ Unterscheidung zwischen Modell und Implementierung
# <br><br>
# ■ Relationale Algebra und relationales Kalkül
# <br><br>
# ■ Informell: Anfragesprache Alpha
# <br>
# □ Angelehnt: SEQUEL von Chamberlin und Boyce
# <br>
# □ Vorgänger von SQL
# <br><br>
# ■ Funktionale Abhängigkeiten
# <br><br>
# ■ Normalformen
# <br>
# □ Erste bis dritte Normalform

# ![title](codd1.jpg)

# ![title](codd2.jpg)

# ![title](codd3.jpg)

# ![title](codd4.jpg)

# ## Von ER-Diagrammen zu Relationenschemata

# EINLEITUNGSTEXT:
# <br>
# Logischer Entwurf:
# <br>
# ■ Sprachmittel: Datenmodell des ausgewählten DBMS
# <br>
# □ z.B. DB2, Oracle, … => relationales Modell
# <br>
# □ Tamino => XML
# <br>
# <br>
# ■ Vorgehensweise
# <br>
# □ (Automatische) Transformation des konzeptionellen Schemas
# <br>
# – z.B. ER in relationales Modell
# <br>
# <br>
# □ Verbesserung des relationalen Schemas anhand von Gütekriterien
# <br>
# – Normalisierung, Redundanzvermeidung, …
# <br>
# ■ Ergebnis: logisches Schema, z.B. Sammlung von Relationenschemata

# Ziele der Abbildung ER -> relationales Modell
# <br>
# ■ Darstellung aller Informationen des ER-Diagramms
# <br>
# <br>
# ■ Exaktheit
# <br>
# □ Das Datenbankschema kann genauso viele Instanzen wie das ER-Diagramm darstellen.
# <br>
# □ Das Datenbankschema kann nicht mehr Instanzen als das ER-Diagramm darstellen.
# <br>
# – Integritätsbedingungen müssen weiterhin gelten
# <br>
# <br>
# ■ Erhaltung und Einhaltung der Informationskapazität!

# ### Kapazitätserhöhende Abbildung

# ![title](erhoehend.jpg)

# ### Kapazitätsvermindernde Abbildung

# ![title](vermindernd.jpg)

# ### Grundalgorithmus

# 1. Wandle jeden Entitytypen in eine Relation mit den gleichen Attributen um.
# <br>
# <br>
# 2. Wandle jeden Relationshiptypen in eine Relation um mit:
# <br>
# □ Zugehörige Attribute des Relationshiptypen
# <br>
# □ Schlüsselattribute der beteiligten Entitytypen
# <br>
# <br>
# 3. Verfeinere den Entwurf
# <br>
# <br>
# 1. Zusammenlegung von Relationen
# <br>
# <br>
# 2. Normalisierung
# <br>
# ■ Ausnahmen
# <br>
# □ Schwache Entitytypen
# <br>
# □ IST Relationships

# ### Entity -> Relation

# ■ Name des Entitytyps -> Name der Relation
# <br>
# ■ Attribute des Entitytyps -> Attribute der Relation
# <br>
# ■ Diese Relation bildet in keiner Weise Relationships ab.

# ![](entitytyp.jpg)

# ■ Film(Titel, Jahr, Länge, Typ)
# <br>
# ■ Schauspieler(Name, Adresse)
# <br>
# ■ Studio(Name, Adresse)

# ### Relationshiptyp -> Relation

# Attribute
# <br>
# □ Attribute des Relationshiptyps selbst
# <br>
# □ Für jeden beteiligten Entitytypen: Füge deren Schlüsselattribut(e) als Attribute hinzu
# <br>
# <br>
# ■ Doppelte Attributnamen
# <br>
# □ Umbenennungen sind nötig!
# <br>
# <br>
# ■ Falls ein Entitytyp in mehreren Rollen beteiligt ist
# <br>
# □ Entsprechend oft die Schlüsselattribute übernehmen
# <br>
# □ Geeignete Umbenennungen sind dann sogar nötig

# ![](entitytyp.jpg)

# ■ spielt_in(Titel, Jahr, SchauspielerInName, SchauspielerInAdresse, Rolle)
# <br>
# ■ besitzt(Titel, Jahr, StudioName)
# <br>
# ■ Umbenennungen hier nur zur Klarheit

# BILD

# ist_unter_Vertrag(Titel, Jahr, SchauspielerName, SchauspielerAdresse, StudioName)

# BILD

# ist_unter_Vertrag(Titel, Jahr, SchauspielerName, SchauspielerAdresse, Stammstudio, ProduzierendesStudio, Gehalt)

# ### Zusammenlegen von Relationen

# ■ Man kann folgende Relationen kombinieren:
# <br>
# □ Die Relation für einen Entitytypen E
# <br>
# □ mit der Relation eines 1:n Relationshiptypen R, falls E auf den n-Seite liegt.
# <br>
# <br>
# ■ Neue Relation enthält also
# <br>
# □ Alle Attribute von E
# <br>
# □ Alle Attribute von R
# <br>
# – inkl. Schlüssel des anderen Entitytypen

# ![title](relationshiptyp1.jpg)

# ![title](relationshiptyp2.jpg)

# ![title](zusammenlegen1.jpg)

# #### 1:n-Relationships

# ![title](zusammenlegen1n.jpg)

# #### 1:1-Relationships

# ![title](zusammenlegen11.jpg)

# #### Falschbeispiel: n-m-Relationships

# ![title](zusammenlegennm.jpg)

# ### Schwache Entitytypen

# ■ Drei Besonderheiten
# <br>
# □ Die Relation eines schwachen Entitytypen S muss nicht nur die eigenen Attribute, sondern auch die
# Schlüsselattribute aller Entitytypen, die über unterstützende Relationshiptypen erreicht werden, enthalten.
# <br>
# □ Alle Relationen für Relationshiptypen, die S in Beziehung mit anderen Entitytypen setzen, müssen ebenfalls alle diese Attribute enthalten.
# <br>
# □ Ein unterstützender Relationshiptyp muss hingegen gar nicht durch eine Relation abgebildet werden.
# <br>
# – Begründung wie eben: 1:n

# ![title](schwache_entitytypen.jpg)

# ■ Studios(Name, Adresse)
# <br>
# ■ Crews(Nummer, Name)

# ![title](schwache_entitytypen2.jpg)

# ■ Studio(Name, Adresse)
# <br>
# ■ Schauspieler*in(Name, Adresse)
# <br>
# ■ Film(Titel, Jahr, Typ, Länge)
# <br>
# ■ Vertrag(Schauspieler*inName, StudioName, Titel, Jahr, Gehalt)

# ![title](schwache_entitytypen3.jpg)

#  Studio(Name, Adresse)
#  <br>
# ■ Schauspieler*in(Name, Adresse)
# <br>
# ■ Film(Titel, Jahr, Typ, Länge)
# <br>
# ■ ist_unter_Vertrag(Schauspieler*inName, StudioName, Titel, Jahr, Gehalt)
# <br>
# ■ Was fällt auf?

# ### Schema Teilmengen

# Beispiel
# <br>
# □ Personen(Name, SSN)
# <br>
# □ Steuerzahler*in(Name, SSN, Betrag)
# <br>
# <br>
# ■ Schema von Personen ist Teilmenge des Schemas von Steuerzahler.
# <br>
# <br>
# ■ Aber: Instanzen können sich unterscheiden
# <br>
# □ Steuerzahler*in Í Personen (jeder Steuerzahler ist eine Person)
# <br><br>
# ■ Beispiel
# <br>
# □ Schauspieler*in(Name, Adresse)
# <br>
# □ Studios(Name, Adresse)
# <br><br>
# ■ Schemata sind sogar identisch, aber Instanzen grundverschieden.
# <br>
# ■ D.h.: Gleiche oder überlappende Schemas können/sollen nicht immer zusammengelegt werden.

# ## Konvertierung von Spezialisierung

# ![title](spezialisierung.jpg)

# ## ER-Still

# □ Für jeden Entitytypen E der Hierarchie erzeuge eine Relation mit den Schlüsselattributen des WurzelEntitytypen und den Attributen von E
# <br>
# <br>
# ■ Film(Titel, Jahr, Länge,Typ)
# <br>
# <br>
# ■ Krimi(Titel, Jahr, Waffen)
# <br>
# <br>
# ■ Zeichentrickfilm(Titel, Jahr)
# <br>
# <br>
# ■ Anmerkungen
# <br>
# □ Die IST-Relationship selbst erhält keine Relation.
# <br>
# □ Geerbte Schlüsselattribute werden für weitere Beziehungen benötigt.
# <br>
# □ Es gibt vier verschiedene Filmsorten.
# <br>
# □ Jeder Film hat ein Tupel in der Relation Filme.
# <br>
# □ Ein konkreter Film (z.B. Roger Rabbit) kann Tupel in allen drei Relationen haben.
# <br>
# <br>
# ■ Stimmen(Titel, Jahr, Name)
# <br>
# ■ Schema von Zeichentrickfilm ist Teilmenge des Schemas von Stimmen.
# <br>
# □ Kann man es weglassen?
# <br>
# □ Nein: Stumme Zeichentrickfilme!

# ## Objekt-orientierter Stil

# □ Ein Entity gehört zu genau einer Klasse.
# <br>
# □ Für jeden möglichen Teilbaum der Hierarchie, der auch die Wurzel enthält, erzeuge eine Relation mit allen
# Attributen der beteiligten Entitytypen.

# ■ Erzeuge Relation für jeden Teilbaum.
# <br>
# ■ Diese Relation repräsentiert die Entities, die genau diese Komponenten der Hierarchie besitzen.
# <br>
# □ Objekte gehören zu genau einer Klasse.
# <br><br>
# ■ Vier Teilbäume
# <br>
# □ Nur Filme
# <br>
# □ Filme und Zeichentrickfilme
# <br>
# □ Filme und Krimis
# <br>
# □ Filme und Zeichentrickfilme und Krimis
# <br><br>
# ■ Film(Titel, Jahr, Länge, Typ)
# <br>
# ■ FilmZ(Titel, Jahr, Länge, Typ)
# <br>
# ■ FilmK(Titel, Jahr, Länge, Typ, Waffen)
# <br>
# ■ FilmZK(Titel, Jahr, Länge, Typ, Waffen)
# <br>
# <br>
# ■ Kann man Film und FilmZ zusammenführen?
# <br>
# <br>
# ■ Kann man FilmK und FilmZK zusammenführen?
# <br>
# <br>
# ■ Wie viele Relationen für Stimmen benötigt man?
# <br>
# □ Nur eine: Stimmen(Titel, Jahr, Name)

# ## Null-Werte Stil

# □ Erzeuge eine einzige Relation für die gesamte Hierarchie. Ein Entity wird durch ein Tupel repräsentiert mit NullWerten für Attribute, die der Entity nicht besitzt.

# ■ Eine einzige Relation mit allen Attributen.
# <br>
# <br>
# ■ Film(Titel, Jahr, Länge, Typ, Waffen)
# <br>
# <br>
# ■ Nicht-Krimis haben NULL-Wert als Attributwert für Waffen.
# <br>
# <br>
# ■ Feinheiten
# <br>
# □ Stumme Zeichentrickfilme und Krimis ohne Waffen sehen aus wie „normale“ Filme.

# ## Vergleich der drei Stile

# ■ Anzahl an Relationen (bei n Entitytypen)
# <br>
# □ Null-Stil: Nur eine Relation
# <br>
# □ ER-Stil: n Relationen
# <br>
# □ OO-Stil: O(2n-1) Relationen
# <br>
# <br>
# ■ Speicherbedarf
# <br>
# □ OO-Stil: Minimaler Speicherbedarf
# <br>
# – Nur ein Tupel pro Entity
# <br>
# – Jeweils nur so viele Attribute wie nötig
# <br>
# □ Null-Stil: Auch nur ein Tupel pro Entity
# <br>
# – Aber: Lange Tupel mit möglicherweise vielen Null-Werten
# <br>
# □ ER-Stil: Viele Tupel pro Entity
# <br>
# – Aber nur Schlüsselattribute werden wiederholt

#  Anfragebearbeitung
#  <br>
# □ Joins über viele Relationen sind teuer.
#  <br>
# □ Þ Null-Werte im Vorteil
#  <br>
# □ Welche Filme aus 1999 sind länger als 150 Minuten?
#  <br>
# – ER-Stil: Antwort direkt möglich
#  <br>
# – OO-Stil: Anfrage an alle vier Relationen
#  <br>
# □ Welche Waffen wurden in Zeichentrickfilmen, die länger als 150 Minuten sind, verwendet?
#  <br>
# – ER-Stil: Alle drei Relationen sind relevant:
#  <br>
# 1. Filme für die Länge
#  <br>
# 2. Zeichentrickfilme für die Tatsache, dass es ein Zeichentrickfilm ist
#  <br>
# 3. Krimis für die Waffe
#  <br>
# – OO-Stil: Anfrage nur an FilmeZK()

# NICHT enthalten: S.35
