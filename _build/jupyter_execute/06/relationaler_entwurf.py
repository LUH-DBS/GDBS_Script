#!/usr/bin/env python
# coding: utf-8

# # Relationaler Entwurf
# 
# Die meisten kommerziellen Datenbanken unterstützen das relationale Datenmodell. 
# In diesem Kapitel lernen wir das relationale Modell kennen und diskutieren Methoden zur Überführung von Datenspezifikationen aus dem ER-Modell ins relationale Modell.

# ## Das Relationale Modell
# 
# Im Folgenden werden wir ähnlich zum ER-Modell die grundlegenden Bausteine des relationalen Modells kennen lernen. Zentrale Grundbegriffe des relationalen Modells sind Relationen und Tupel. 

# In der Mathematik ist eine Relation $R$ eine Teilmenge des Kreuzproduktes von $n$ Mengen: $R\subset A_1 \times A_2 \times \cdots \times A_n$. Ein Element der Relation ist ein n-Tupel: $\forall t \in R. t=(a_1,a_2,\cdots, a_n) \wedge a_i \in A_i$
# 
# 
# Für Datenbanken gelten die aus der Mathematik bekannten Beziehungen mit folgenden zusätzlichen semantischen Erweiterungen. 
# Die Mengen $A_i$ sind im Datenkontext Domänen bzw. Wertebereiche. Diese Wertebereiche können im allgemeinen Standarddatentypen wie Integer, String, Boolean, usw. sein oder konkrete Wertebereiche, die durch Attribute definiert werden, wie zum Beispiel ID, Name, Alter, Geschlecht. Prinzipiell entspricht eine solche Menge der Spalte einer Tabelle.
# 
# Analog bilden die Einträge der Tupel $(a_1,\cdots, a_n)$ die Datenwerten einer Tabelle, z.B. (4, Abedjan, 36, m). Ein Tupel entspricht einer Zeile einer Tabelle.

# ### Die Relation

# Konzeptuell ist eine Datenbank eine Menge von Tabellen. Jede Tabelle stellt die Daten einer Relation dar. Eine Tabelle besteht aus Spalten, die in Relation zu einander stehen. Damit beinhaltet jede Zeile Datenwerte aus den jeweiligen Domänen, die in Relation zu einander stehen. Wir werden oft Tabellen und Relationen alternierend nutzen, obwohl diese konzeptionell unterschiedliche Konzepte sind. Eine Relation ist ein mathematisches Konzept, welches aus Mengen und Tupeln zusammensetzt ist, während eine Tabelle ein zweidimensionales Feld bestehend aus Spalten und Zeilen ist. Es ist jedoch leicht einzusehen, dass jede Relation als Tabelle darstellbar ist. 
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
# - Datenbankschema: Im Groben beschreibt jedes relationale Modell ein Datenbankschema, welche aus einem oder mehreren Relationenschemata besteht. 
# - Relationenschema: Jede Relation wird durch ihr Schema identifiziert. Das Relationenschema besteht aus dem Namen der Relation und der Liste der Attribute und ihrer Domänen. In einer Tabelle entspricht die Kopfzeile dem Relationenschema. Alle weiteren (Daten-)Einträge in der Tabelle bilden die „Relation“
# - Die Relation besteht aus keinem oder mehr Tupeln. Im relationalen Modell bilden Tupel einer Relation immer eine Menge. Das heißt, dass kein Tupel in seiner gesamten Ausprägung doppelt auftauchen kann. Diese Annahme gilt in echten Datenbanksystemen nur dann, wenn ein Schlüssel vorhanden ist. 
# - Attribute entsprechen den Bezeichnern der zu einander in Relation stehenden Domänenmengen. In Tabellen entsprechen Attribute den Spaltenbezeichnern (Überschriften). In einem Relationenschema kann ein Attribut nicht doppelt vorkommen. Das Relationenschema ist somit eine Menge.
# - Attributwert: Jeder Dateneintrag in einem Tupel entspricht dem Attributwert der jeweiligen Spalte. Attributwerte sind atomar und stammen aus einer elementaren Domäne. 
# - Ein Tupel entspricht aus einer vollständigen Kombination von Attributwerten.
# 
# In der Abbildung unten sind die jeweiligen Elemente nochmal visuell dargestellt. Wir haben Primärschlüssel und Fremdschlüssel auch bereits dargestellt. Diese sind wie bekannt aus dem ER-Modell, Attribute die referenzielle Integrität gewährleisten. Hierauf werden wir später in diesem Kapitel genauer eingehen. 

# ![title](elemente_rm.jpg)

# ### Formal

# Formal betrachtet können wir die mathematische Definition von Relationen etwas spezieller auf Relationen in Datenbanken anwenden. Ausgangspunkt sind $n$ Domänen $D_1, D_2, \dots, D_n$. Jede Domäne entspricht einer endlichen oder unendlichen Menge von gleichartigen Ausdrücken. Domänen können auch ganz allgemein als Datentypen wie String oder Integer aufgefasst werden. 
# Eine Relation im Sinne des relationalen Modells ist die Teilmenge des Kreuzproduktes von $n$ Domänen: $R \subseteq D_1 \times D_2 \times \dots \times D_n $. Daraus Ergibt sich, dass es für jede Domäne $D_n$ eine Menge $A_n \subset D_n$ gibt die alle Werte, die in der Zieltabelle vorkommen abbilden. Zum Beispiel könnte $A_n$ die Menge aller Adressen eines Unternehmens sein. Im folgenden Beispiel wird das Nochmal verdeutlicht. Formal gibt es für jede Attributwertmenge $A_n$ auch ein Label $a_n$ welches die Menge bezeichnet. Hier: $a_n=$ "Adressen". Oft wird $A_n$ auch Synonym (unsauber) als Bezeichner verwendet.
# 
# - Beispiel
#     - Relationenschema: $R(a_1,a_2,a_3,a_4)$ $\equiv$ Film(Titel, Jahr, Länge, Typ)
#     - Domänen: String, Integer, Integer, String
#     - Tupel: (Star Wars, 1977, 124, farbig)

# ### Edgar F. Codd

# Die Relationale-Datenbanktheorie geht auf den Turing Award Gewinner Edgar F. Codd zurück, welcher an der University of Michigan Ann Arbor promoviert hat. Bei IBM (Almaden) hat Codd das Relationalen Modell entwickelt und das Paper „A Relational Model of Data for Large Shared Data Banks" 1970 veröffentlichz.
# <br><br>
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

# Edgar F. Codd hat nicht nut das relationale Modell entwickelt, sondern überhaupt das Konzept eines Datenmodells. Dazu gehört auch die Unterschiedung zwischen Modell und Implementierung, sowie ein mathematisches Regelwerk für Anfragen, die relationale Algebra und das relationale Kalkül. Auf diesem Regelwerk basiert informell die Anfragesprache Alpha und daran angelehnt SEQUEL(SQL Vorgänger) von Chamberlin und Boyce. Ebenso von Codd sind Integritätsbedingungen und Qualitätsformen, wie funktionale Abhängigkeiten und Normalformen(erste bis dritte). Durch seine Beiträge hat Codd das Datenmanagement zu einer Wissenschaft, mit entsprechender Klarheit und Strenge, transformiert.
# 

# ## Von ER-Diagrammen zu Relationenschemata

# In diesem Kapitel möchten wir lernen, wie wir von einem ER-Diagramm zu einem Relationenschema gelangen. Wir befinden uns im Phasenmodell im logischen Entwurf. Als Sprachmittel haben wir das Datenmodell des ausgewählten DBMS gegeben z.B. DB2, Oracle, … => relationales Modell. Am idealsten wäre eine automatische Transformation des konzeptionellen Schemas, z.B ER in relationales Modell erwüscht. Danach ist es noch möglich das entstandende relationale Schema anhand von Gütekriterien, mit Normalisierung und Redundanzvermeidung zu verbessern. Zuletzt soll das Hauptergebnis ein logisches Schema sein, wie z.B. eine Sammlung von Relationenschemata.

# ### Ziele der Abbildung ER -> relationales Modell
# Bei der Umformung eines ER-Diagramms in ein relationales Modell, soll das relationalle Modell **alle** Informationen des ER-Diagramms darstellen. Dabei spielt einmal die Exaktheit eine große Rolle. D.h. dass das Datenbankschema genauso viele und nicht mehr Instanzen als das ER-Diagramm darstellen kann, wobei Integritätsbedingungen weiterhin gelten müssen. Ziel ist also eine Erhaltung und Einhaltung der Informationskapazität!

# #### Kapazitätserhöhende Abbildung
# 
# In diesem Kontext betrachten wir ein Beispiel. Angenommen wir haben ein 1:1-Beziehung zwsichen Studios und Vorsitzende. Studios hat einen Schlüssel SName und Vorsitzende einen Schlüssel VName. Entsprechend könnten wir das Relationenschema: R = {SName, VName} wählen. Für unser gewähltes Relationenschema könnten wir die Schlüsselmenge: {{SName}} wählen. Jedoch wäre es so möglich, dass ein Vorsitzende\*r mehrere Studios leitet und die 1:1-Beziehung verletzt. Das wäre dann eine kapazitätserhöhende Abbildung. Würden wir als Schlüsselmenge beide Schlüssel {{SName},{VName}} wählen, dann hätten wir eine kapazitätserhaltende Abbildung die eine 1:1-Beziehung abbildet.

# ![title](erhoehend.jpg)

# ### Kapazitätsvermindernde Abbildung
# Betrachten wir nun folgendes Beispiel, in dem ein\*e Schauspieler\*in in einem Film mitspielt. Es herrscht eine n:m-Beziehung zwischen Schuspieler\*in und Film. Schauspieler\*in wird durch Name und Film durch Titel eindeutig identifiziert. Wir wählen nun als Relationenschema: R = {Name, Titel}. Wenn wir nun als Schlüsselmenge {{Name}} wählen, dann kann ein\*e Schauspieler\*in nur jeweils einmal in unserer Relation vorkommen, welches unsere eigentlich Kapazitäts verminderd. Wählt man stattdessen als Schlüsselmenge {{Name, Titel}}, so kommt die Kombination aus Name und Titel jeweils nur einmal in unserer Relation vor, welches kapazitätserhaltend ist.

# ![title](vermindernd.jpg)

# ### Grundalgorithmus

# Der Grundalgorithmus für eine kapazitätserhaltende und -einhaltende Abbildung sieht wie folgt aus:
# <br>
# 1. Wandle jeden Entitytypen in eine Relation mit den gleichen Attributen um.
# <br>
# <br>
# 2. Wandle jeden Relationshiptypen in eine Relation um mit:
#     - Zugehörige Attribute des Relationshiptypen
#     - Schlüsselattribute der beteiligten Entitytypen
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
# Ausnahmen gibt es bei dem Umgang mit schwachen Entitytypen und IST Relationships. Diese werden wir uns noch genauer in folgenden Kapiteln betrachten.

# ### Entity -> Relation

# Wir haben folgendes ER-Diagramm gegeben. Bei der Umwandlung eines Entitytyps in eine Relation wird der Name des Entitytyps zu dem Namen der Relation. Die Attribute des Entitytyps werden zu den Attribute der Relation. Die daraus entstehende Relation bildet in keiner Weise Relationships ab.

# Für die drei Entitytyps aus dem Diagramm, ergeben sich folgende Relationen:
# - Film(Titel, Jahr, Länge, Typ)
# <br>
# - Schauspieler(Name, Adresse)
# <br>
# - Studio(Name, Adresse)

# ![](entitytyp.jpg)

# ### Relationshiptyp -> Relation

# Bei der Umwandlung eines Relationshiptyps in eine Relation, müssen die Attribute des Relationshiptyps selbst und die Schlüsselattribute der beiteiligten Entitytypen mitgenommen werden. Sind doppelte Attributnamen vorhanden, sind
# Umbenennungen nötig!
# <br>
# Falls ein Entitytyp in mehreren Rollen beteiligt ist, müssen die Schlüsselattribute entsprechend oft übernommen werden. Geeignete Umbenennungen sind dann sogar nötig.

# Es ergebem sich folgende Relationen:
# - spielt_in(Titel, Jahr, SchauspielerInName, SchauspielerInAdresse, Rolle)
#     - spielt_in enthält alle Schlüsselattribute von Film und Schauspieler\*in und die eigenen Attribute
# - besitzt(Titel, Jahr, StudioName)
#     - besitzt enthält alle Schlüsselattribute von Film und Studio
# <br>
# Umbenennungen dienen hier nur zur Klarheit.

# ![](entitytyp.jpg)

# Bei ternären Beziehungen bleibt das Prinzip gleich. Für die unten dargestellte Beziehung, werden alle Schlüsselattribute der beteiligten Entitytypen, Film, Studio und Schauspieler\*in mitgenommen. Und ebenso die Attribute der Beziehung selbst. So ergibt sich das Relationsschema:
# - ist_unter_Vertrag(Titel, Jahr, SchauspielerName, SchauspielerAdresse, StudioName)

# ![title](schwache_entitytypen3.jpg)

# Zultzt betrachten wir ein Beziehung mit mehreren Rollen. Das ER-Diagramm ist ähnlich zudem vorherigen, bis darauf, dass ist_unter Vetrag einaml die Rolle Stammstudio und einmal die Rolle porduzierendes Studio besitzt. Dementsprechend muss das Schlüsselattribut des Entitytyps Studio, jeweils einmal für jede Rolle vorkommen. Es ergibt sich demnach folgendes Relationsschema:
# - ist_unter_Vertrag(Titel, Jahr, SchauspielerName, SchauspielerAdresse, Stammstudio, ProduzierendesStudio, Gehalt)

# ![title](relationshiptyp2.jpg)

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
# 
# In diesem Kapitel betrachten wir drei Strategien wie Spezialisierungen in Relationen dargestellt werden können.

# ### Spezialisierung
# 
# Angenommen wir haben einen Wurzel-Entitytyp der IST-Hierarchie gegeben. Dieser Wurzel-Entitytyp hat einen Schlüssel der alle Entitys der gesamten Hierarchie identifiziert. Eine Entity kann aus mehreren Komponenten der Hierarchie bestehen.
# 

# ![title](spezialisierung.jpg)

# ### ER-Still

# Beim ER-Stil wird für jeden Entitytypen E der Hierarchie eine Relation mit den Schlüsselattributen des Wurzel-Entitytypen und den Attributen von E erzeugt. Für das obige Beispiel würden sich folgende Relationen ergeben:
# - Film(Titel, Jahr, Länge,Typ)
# - Krimi(Titel, Jahr, Waffen)
# - Zeichentrickfilm(Titel, Jahr)
# 
# <br>
# <br>
# Die IST-Relationship selbst erhält keine Relation und die geerbten Schlüsselattribute können für weitere Beziehungen weiterbenutzt werden. In unserem Beipsiel gibt es vier verschiedene Filmsorten. Jeder Film hat ein Tupel in der Relation Filme. Ein konkreter Film (z.B. Roger Rabbit) kann auch Tupel in allen drei Relationen haben.
# <br>
# <br>
# Zusätzlich können wir noch die Beziehung Stimmen definieren: Stimmen(Titel, Jahr, Name). Wir sehen, dass das Schema von Zeichentrickfilm eine Teilmenge des Schemas von Stimmen ist. Kann man es dann nicht einfach weglassen? Nein, denn es gibt auch stumme Zeichentrickfilme!

# ### Objekt-orientierter Stil

# Beim Objekt-orientierten Stil gehört eine Entity zu genau einer Klasse. Für jeden möglichen Teilbaum der Hierarchie, der auch die Wurzel enthält, wird eine Relation mit allen Attributen der beteiligten Entitytypen erzeugt. Diese Relation repräsentiert die Entities, die genau diese Komponenten der Hierarchie besitzen. Unser Beispiel oben hat vier Teilbäume: Nur Filme, Filme und Zeichentrickfilme, Filme und Krimis, Filme und Zeichentrickfilme und Krimis. Demnach ergeben sich vier Relationen:
# - Film(Titel, Jahr, Länge, Typ)
# - FilmZ(Titel, Jahr, Länge, Typ)
# - FilmK(Titel, Jahr, Länge, Typ, Waffen)
# - FilmZK(Titel, Jahr, Länge, Typ, Waffen)

# Kann man Film und FilmZ zusammenführen?
# <br>
# Kann man FilmK und FilmZK zusammenführen?
# <br>
# <br>
# Nein, da jede Relation eine bestimmte Typkombination darstellt.
# <br><br>
# Wie viele Relationen für Stimmen benötigt man?
# <br>
# Es wird nur eine benötigt: Stimmen(Titel, Jahr, Name)

# ### Null-Werte Stil

# Beim Null-Werte-Stil wird eine einzige Relation für die gesamte Hierarchie erzeugt. Eine Entity wird durch ein Tupel repräsentiert,welches für fehlende Attribute Null-Werte hat. Für unser Beispiel, wird im Null-Werte-Stil also eine einzige Relation mit allen Attributen erstellt:
# - Film(Titel, Jahr, Länge, Typ, Waffen)
# <br><br>
# Filme die keine Krimis sind haben alls Attributwert NULL stehen. Zu beachten ist noch, dass mit der Null-Werte-Darstellung stumme Zeichentrickfilme und Krimis ohne Waffen von „normalen“ Filme nicht mehr zu unterscheiden sind.

# ### Vergleich der drei Stile
# 
# Alle drei Strategien haben ihre Vor- und Nachteile. Wir vergleichen zunächst die Anzahl der benötigten Relationen bei n Entitytypen:
# -  Null-Stil: Nur eine Relation
# - ER-Stil: n Relationen
# -  OO-Stil: O(2n-1) Relationen
# <br>
# <br>

# Nun vergleichen wir den Speicherbedarf:
# <br>
# - OO-Stil: Minimaler Speicherbedarf, da nur ein Tupel pro Entity benötigt wird und jeweil nur so viele Attribute wie nötig dargestellt werden.
# - Null-Stil: Auch nur ein Tupel pro Entity, möglicherweise jedoch mit vielen Null-Werten, welches das Tupel länger macht.
# -  ER-Stil: Viele Tupel pro Entity, es werden jedoch nur Schlüsselattribute wiederholt

# Bei der Anfragebearbeitung müssen wir annehmen, das Joins über viele Relationen teuer sind. Daher wäre eine Anfrage mit so wenig Joins wie möglich am günstigten. Das wäre hier der Null-Werte-Stil, da nur eine Tabelle für die Darstellung nötig ist.
#  <br><br>
# Möchten wir nun die folgende Anfrage ausführen: Welche Filme aus 1999 sind länger als 150 Minuten?
#  <br>
# - ER-Stil: Antwort direkt möglich, da Anfrage direkt an die "normale" Filmrelation gestellt werden kann.
#  <br>
# - OO-Stil: Anfrage an alle vier Relationen, da die Attribute Länge und Typ in allen vier Relationen vertreten sind.
#  <br>
#  <br>
#  
# Welche Waffen wurden in Zeichentrickfilmen, die länger als 150 Minuten sind, verwendet?
#  <br>
# - ER-Stil: Alle drei Relationen sind relevant, daher müssen drei Joins durchgeführt werden
#  <br>
# 1. Filme für die Länge
#  <br>
# 2. Zeichentrickfilme für die Tatsache, dass es ein Zeichentrickfilm ist
#  <br>
# 3. Krimis für die Waffe
#  <br>
# - OO-Stil: Anfrage nur an FilmeZK()

# ## Multiple Choice
# 
# - Die hier verwendete Version des Multiple-Choice-Trainers von EILD.nrw wird nur in das JupyterBook eingebunden und nicht selbst gehostet. Der Multiple-Choice-Trainer wird durch GitHub-Pages gehostet. 
# - Alle Fragen und Kategorien befinden sich zurzeit in Überarbeitung und sind nicht final. 

# In[1]:


from IPython.display import IFrame

url = "https://lejuliennn.github.io/mct-trainer/#/quiz/categories/relationalerentwurf"
IFrame(src=url, width='100%', height=800)


# In[ ]:




