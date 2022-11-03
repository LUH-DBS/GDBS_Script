#!/usr/bin/env python
# coding: utf-8

# # SQL

# In[1]:


import sqlite3
import pandas as pd
get_ipython().run_line_magic('load_ext', 'sql')
get_ipython().run_line_magic('sql', 'sqlite:///filme/filme.db')
get_ipython().run_line_magic('sql', 'sqlite:///abteilung/abteilung.db')
get_ipython().run_line_magic('sql', 'sqlite:///buecher/buecher.db')
get_ipython().run_line_magic('sql', 'sqlite:///lehre/lehre.db')
get_ipython().run_line_magic('sql', 'sqlite:///rst/rst.db')
get_ipython().run_line_magic('sql', 'sqlite:///salesDB/salesDB.db')


# ## Einführung
# 
# Aus den vorherigen Kapiteln haben wir gelernt wie wir eine Datenbank auf Papier entwerfen, nun schauen wir uns die in der Realität benutzten technischen Mitteln an, insbesondere die Datenbankanfragesprache SQL.
# 
# ### Motivation für SQL
# SQL ist die meist-verbreiteste Datenbankanfragesprache. Es handelt sich hierbei um eine Very-High-Level Language, die Ad-hoc, deklarativ und nicht prozedural / imperativ ist. SQL-Anfragen sich an die relationale Algebra angelehnt. Zusätzlich sind Data definition(DDL) und Data manipulation(DML) mit SQL möglich. Wichtig zu beachten ist noch, dass sowohl Syntax, als auch Funktionalität sich von System zu System leicht unterscheiden können.
# 
# ### SQL-Historie
# 
# SQL(1982, IBM) entstand durch die Ursprungssprache SEQUEL(1976, IBM Research Labs San Jose). Später entwickelte sich SEQUEL zu SEQUEL2(1976, IBM Research Labs San Jose), welche auf einer der Vorreitern von Datenbanksystemen "System R" benutzt wurde.
# 
# ![title](historie1.jpg)
# <br>
# ![title](historie2.jpg)
# <br>
# ![title](historie3.jpg)
# ### SQL – Standardisierung
# Im Laufe der Zeit durchlief SQL verschiedene Standardisierungen, die Sie aus der folgenden Auflistung entnehmen können. Trotz der Standardisierung sind Inkompatibilitäten zwischen Systemen der einzelnen Hersteller noch möglich.
# 
# 
# - SQL1 von ANSI als Standard verabschiedet (1986)
# <br><br>
# - SQL1 von der (ISO) als Standard verabschiedet (1987)
#  <br>
#  - 1989 nochmals überarbeitet.
#  <br> <br>
# - SQL2 oder SQL-92 von der ISO verabschiedet (1992)
#  <br> <br>
# - SQL3 oder SQL:1999 verabschiedet
#  <br> 
#  - Trigger, rekursive Anfragen
#  <br>
#  - Objektrelationale Erweiterungen
#  <br> <br>
# - SQL:2003 von der ISO verabschiedet
#  <br>
#  - XML-Support durch SQL/XML
#  <br> <br>
# - SQL/XML:2006
#  <br>
#  - XQuery eingebunden
#  <br> <br>
# - SQL:2008
#  <br>
#  - Updates auf Sichten, logisches Löschen (TRUNCATE), …
#  <br> <br>
# - SQL:2011
#  <br>
#  - Adds temporal data (PERIOD FOR)
#  <br> <br>
# - SQL:2016
#  <br>
#  - Adds row pattern matching, polymorphic table functions, JSON.
# 
# ### SQL:2008 Struktur
# ■ Part 1: Framework (SQL/Framework) – 82 Seiten
# <br>
# □ Überblick
# <br><br>
# ■ Part 2: Foundation (SQL/Foundation) – 1316 Seiten
# <br>
# □ Datenmodell, DDL, DML, Abfragen
# <br><br>
# ■ Part 3: Call-Level Interface (SQL/CLI) – 389 Seiten
# <br>
# □ Zugriff auf DBMS mittels Funktionsaufrufen aus anderen Programmiersprachen
# <br><br>
# ■ Part 4: Persistent Stored Modules (SQL/PSM) – 188 Seiten
# <br>
# □ Prozedurale Erweiterungen
# <br><br>
# ■ Part 9: Management of External Data (SQL/MED) – 484 Seiten
# <br>
# □ Neue Datentypen und Funktionen
# <br><br>
# ■ Part 10: Object Language Bindings (SQL/OLB) – 396 Seiten
# <br>
# □ Auch (SQLJ); zur Einbettung von SQL in Java
# <br><br>
# ■ Part 11: Information and Definition Schemas (SQL/Schemata) – 286 Seiten
# <br>
# □ DBMS werden selbst-beschreibend durch normierten Katalog
# <br><br>
# ■ Part 13: SQL Routines and Types (SQL/JRT) – 198 Seiten
# <br>
# □ Externe Java Routinen als „stored procedures“
# <br><br>
# ■ Part 14: XML-Related Specifications (SQL/XML) – 438 Seiten
# <br>
# □ XML Datentyp und Erweiterung von SQL um XQuery
# <br><br>
# => Zusammen: 3777 Seiten
# 

# ## Einfach Anfragen

# ### SELECT … FROM … WHERE …
# 
# SQL-Anfragen folgen meist einer Drei-Zeilen-Struktur aus SELECT, FROM, WHERE, wobei SELECT und FROM in jeder SQL-Anfrage enthalten sein müssen. Das Schlüsselwort SELECT entspricht dem Projektionsoperator $\pi$, den wir aus dem Kapitel Relationale Algebra schon kennengelernt haben. Die FROM-Zeile gibt an von welchen Tabellen die Daten stammen sollen. WHERE entspricht gewissermaßen dem Selektionsoperator $\sigma$, hier werden also Bedingungen an  die Tupel gestellt die diese erfüllen sollen.
# 
# Betrachten wir folgendes Beispielschema für Filme, welches aus den vorherigen Kapiteln bekannt sein sollte. Wir möchten nun eine Anfrage formulieren, die uns alle Filme ausgibt, welche von Disney produziert und im Jahre 1990 erschienen sind.

# ### Beispielschema
# ![title](beispielschema.jpg)

# In[4]:


#SELECT * 
#FROM Film 
#WHERE StudioName = "Disney" AND Jahr= 1990;

__SQL__ = "SELECT * FROM Film WHERE StudioName = 'Disney' AND Jahr= 1990"
conn = sqlite3.connect("filme/filme.db")
df = pd.read_sql_query(__SQL__, conn)
df


# Wir benutzen SELECT \*, wodurch uns alle Attribute der ausgewählten Tabelle ausgegeben werden, alternativ kann man auch SELECT Titel, Jahr, Laenge... machen. Da wir alle Filme ausgeben wollen, schreiben wir FROM Film, da wir Tupel aus der Tabelle Film wollen. Zuletzt selektieren wir die Tupel, die StudioName = "Disney" und Jahr = 1990 erfüllen.
# 

# In SQL wird Groß- und Kleinschreibung nicht beachtet, sowohl bei Schlüsselwörtern wie SELECT, FROM, WHERE usw., als auch bei Attribut- und Relationen.
# <br><br>
# D.h es gilt also:
# ```
# From = FROM = from = FrOm
# ```
# <br>
# Und die folgenden Anfragen sind äquivalent:
# 
# ```
# SELect vorNAMe fROm fiLM
# ```
# <br>
# 
# 
# ```
# SELECT vorname FROM film
# ```
# <br><br>
# Anders ist es natürlich bei Konstanten:
# 
# ```
# ‘FROM‘ ≠ ‘from‘ ≠ from = FROM
# ```
# <br><br>
# Trotzdem gilt als Konvention zur Lesbarkeit, dass Schlüsselwörter großgeschrieben werden und Schemaelemente klein.

# ### Projektion in SQL (SELECT, $\pi$)
# 
# Wir betrachten nun die einzelnen Schlüsselwörter etwas genauer und starten mit der Projektion. In der SELECT Klausel werden Attribute von Relationen aufgelistet, die herausprojeziert werden sollen.
# <br><br>
# Im folgenden Beipiel wollen wir alle Attribute bzw. Spalten aus der Filmrelation ausgeben, der Stern "\*" ist hier eine kürzere Schreibweise für alle Attribute.

# In[5]:


#SELECT * 
#FROM Film

__SQL__ = " SELECT * FROM Film"
conn = sqlite3.connect("filme/filme.db")
df = pd.read_sql_query(__SQL__, conn)
df


# Es ist auch möglich konkret die Attributsnamen aufzulisten, die ausgegeben sollen werden. Im unteren Beispiel, geben wir nur die Spalten Titel, Jahr und inFarbe von der Filmrelation aus.

# In[6]:


#SELECT Titel, Jahr, inFarbe 
#FROM Film

__SQL__ = "SELECT Titel, Jahr, inFarbe FROM Film"
conn = sqlite3.connect("filme/filme.db")
df = pd.read_sql_query(__SQL__, conn)
df


# In der SELECT Klausel ist es auch möglich die Attributsnamen in der Ausgabetabelle umzubenennen. Die Ausgabe einer SQL-Anfrage ist immer eine Tabelle. Im unteren Beispiel projezieren wir die Attribute Titel, Jahr aus der Filmrelation und benennen die Attribute in unserer Ausgabetabelle zu Name,Zeit um. 

# In[7]:


#SELECT Titel AS Name, Jahr AS Zeit 
#FROM Film

__SQL__ = "SELECT Titel AS Name, Jahr AS Zeit FROM Film"
conn = sqlite3.connect("filme/filme.db")
df = pd.read_sql_query(__SQL__, conn)
df


# In der SELECT-Klausel ist es auch möglich arithmetische Ausdrücke zu benutzen. Im folgenden Beispiel werden Titel und Laenge der Filme herausprojeziert, wobei die Laenge direkt mit einer Konstanten multipliziert wird. Daher wird in der Ausgabetabelle die Laenge in Stunden und nicht in Minuten angegeben. Dementsprechend haben wir auch das Attribut Laenge in Stunden mit dem Umbenennungsoperator AS umbenannt.

# In[8]:


#SELECT Titel, Laenge * 0.016667 AS Stunden 
#FROM Film

__SQL__ = "SELECT Titel, Laenge * 0.016667 AS Stunden FROM Film"
conn = sqlite3.connect("filme/filme.db")
df = pd.read_sql_query(__SQL__, conn)
df


# Zudem ist es auch möglich, sich spezielle Konstanten ausgeben zu lassen. Im unteren Beispiel fügen wir der Ausgabetabelle eine neue Spalte hinzu, mit dem Namen inStunden, in der der String 'std.' steht

# In[4]:


#SELECT Titel, Laenge * 0.016667 AS Stunden, ‘std.‘ AS inStunden 
#FROM Film

__SQL__ = "SELECT Titel, Laenge * 0.016667 AS Stunden, 'std.' AS inStunden FROM Film"
conn = sqlite3.connect("filme/filme.db")
df = pd.read_sql_query(__SQL__, conn)
df


# ### Selektion in SQL (WHERE, $\sigma$)
# Die Selektion die wir aus der relationalen Algebra kennen wird in SQL mit dem Schlüsselwort WHERE ausgedrückt, nicht mit dem Schlüsselwort SELECT. Wie aus anderen Programmiersprachen bekannt, kann man in der WHERE-Klausel Bedinungen aufstellen. 
# <br><br>
# Es gibt sechs Vergleichsoperatoren =, <>, <, >, <=, >=(gleich, ungleich, kleiner, größer, kleiner gleich, größer gleich), hier können Sie links und rechts der Vergleichsoperatoren Konstanten und Attribute einsetzen. Insbesondere ist es auch möglich Attribute in der WHERE-Klausel zu vergleichen, die nicht in der SELECT- Klausel herausprojeziert werden. Auch im WHERE kann man arithmetische Ausdrücke in die Bedinung einbauen wie in diesem Beispiel:
# ```
# (Jahr - 1930) * (Jahr - 1930) <= 100
# ```
# Und Konstanten und auch Variablen konkatenieren:
# ```
# ‘Star‘ || ‘Wars‘ 
# ```
# entspricht 
# ```
# ‘StarWars‘
# ```
# oder ein Beispiel mit Variablen:
# ```
# Vorname || ' ' || Nachname = 'Luke Skywalker'
# ```
# Hier werden die Variablen Vorname und Nachname mit einer Leerstelle konkateniert und verglichen, ob der String 'Luke Skywalker' entspricht.
# <br><br>
# Das Ergebnis der Vergleichsoperation in SQL ist dann ein Bool'escher Wert, als TRUE oder FALSE. Dementsprechend können mehrere Vergleichsoperatoren mit AND, OR und NOT verknüpft werden, wobei die Klammerungen auch den bekannten Regeln der Logik entsprechen. 
# <br><br> 
# Nur wenn die gesamte WHERE-Klausel zu TRUE evaluiert wird, werden die entsprechenden Tupel ausgegeben.

# Im unteren Beispiel wollen wir jene Titel aus der Relation Film ausgeben, die nach dem Jahr 1970 erschienen und schwarz-weiß sind

# In[10]:


#SELECT Titel 
#FROM Film 
#WHERE Jahr > 1970 AND NOT inFarbe;

__SQL__ = "SELECT Titel FROM Film WHERE Jahr > 1970 AND NOT inFarbe"
conn = sqlite3.connect("filme/filme.db")
df = pd.read_sql_query(__SQL__, conn)
df


# In diesem Beispiel möchten wir wieder alle Filmtitel ausgeben, hier aber alle Filme die von MGM produziert wurden sind und nach dem Jahr 1970 erschienen sind oder kürzer als 90 min sind. 

# In[12]:


#SELECT Titel 
#FROM Film 
#WHERE (Jahr > 1970 OR Laenge < 90) AND StudioName = "MGM";

__SQL__ = "SELECT Titel FROM Film WHERE (Jahr > 1970 OR Laenge < 90) AND StudioName = 'MGM';"
conn = sqlite3.connect("filme/filme.db")
df = pd.read_sql_query(__SQL__, conn)
df


# ### Stringvergleiche
# In SQL gibt es Datentypen unteranderem die Datentypen Array fester Länge, Buchstabenliste variabler Länge und Konstanten. Es sind viele Vergleiche über Datentypen hinweg erlaubt. In diesem Beispiel vergleichen wir eine Variable mit einer weiteren Variable und einer Stringkonstanten:
# ```
# foo _ _ _ _ _ = foo = ‘foo‘
# ```
# Ebenfalls sind lexikographische Vergleiche mit den schon bekannten Vergleichsoperatoren =, <, >, <=, >=, <> möglich. Je nach verwendeter DBMS werden Sortierreihenfolge mit upper-case/lower-case andere behandelt
# ```
# 'fodder' < 'foo'
# ```
# ```
# 'bar' < 'bargain'
# ```

# ### String-Mustervergleiche mit LIKE
# Mit dem LIKE Operator können Sie Stringteile miteinander vergleichen, also ob ein String einem gewissen Stringmuster folgt. Hierfür gibt es zwei spezielle Zeichen, einmal '%', welches eine beliebige Sequenz von 0 oder mehr Zeichen entspricht und '\_', welches ein einzelnes beliebiges Zeichen steht. Hierfür ein Beispiel: Wir suchen jene Titel aus der Filmrelation, wo der Titel mit 'Star' beginnt, ein Leerzeichen folgt und 4 beliebige Zeichen folgen.

# In[13]:


#SELECT Titel 
#FROM Film WHERE Titel LIKE "Star ____";

__SQL__ = "SELECT Titel FROM Film WHERE Titel LIKE 'Star ____'"
conn = sqlite3.connect("filme/filme.db")
df = pd.read_sql_query(__SQL__, conn)
df


# Hier suchen wir alle Titel, wo das Wort 'War' vorkommen muss. Sowohl vor dem 'War' als auch nachdem 'War' sind beliebige Zeichensequenzen erlaubt.

# In[14]:


#SELECT Titel 
#FROM Film 
#WHERE Titel LIKE "%War%";

__SQL__ = "SELECT Titel FROM Film WHERE Titel LIKE '%War%'"
conn = sqlite3.connect("filme/filme.db")
df = pd.read_sql_query(__SQL__, conn)
df


# ### Datum und Uhrzeit
# In SQL gibt es auch Datentypen um Daten und Zeiten darzustellen.Der Datentyp DATE stellt ein Datumskonstante dar:
# <br>
# – DATE ‘YYYY-MM-DD‘
# <br>
# – DATE ‘1948-05-14‘
# <br><br>
# Zeitkonstanten werden mit dem Datentyp TIME dargestellt:
# – TIME ‘HH:MM:SS.S‘
# <br>
# – TIME ‘15:00:02.5‘
# <br><br>
# Zeitstempel, also eine Kombination aus Datum und Zeit, werden mit dem Datentyp TIMESTAMP dargestellt:
# <br>
# – TIMESTAMP ‘1948-05-14 15:00:02.5‘
# <br><br>
# Auch dieses Datentypen können wieder miteinander ,in Form von Variablen und Konstanten, verglichen werden:
# <br>
# – TIME ‘15:00:02.5‘ < TIME ‘15:02:02.5‘ ergibt TRUE
# <br><br>
# – ERSCHEINUNGSTAG >= DATE ‘1949-11-12‘

# ### Nullwerte
# Nullwerte sind spezielle Datentypen, in SQL wird dieser als NULL dargestellt, auf Papier ist auch ⊥ geläufig. Es gibt mehrere Arten einen Nullwert zu interpretieren. Zum einen kann ein Nullwert bedeuten, dass ein Wert unbekannt ist, z.B kann es sein, dass der Geburtstag eines/r Schauspieler\*in unbekannt ist. Eine weitere Interpretationsart ist, dass ein Wert eingetragen wurde der unzulässig ist, wie z.B ein Ehegatte eine eines/r Schauspieler\*in. Zuletzt  können mit Nullwerten bestimmte Zellen oder Spalten maskiert werden, wie z.B bei einer unterdrückten Telefonnummer.
# <br><br>
# Bei dem Umgang mit Nullwerten gibt es verschiedene Regeln, die beachtet werden müssen. Wird NULL mit arithmetischen Operationen verknüpft, so ergibt sich aus der Verknüpfung wiederum NULL. Bei Vergleichen mit NULL ergibt der Wahrheitswert UNKNOWN und nicht NULL. Man muss auch beachten, dass NULL keine Konstante ist, sondern NULL erscheint als Attributwert, abhängig von dem DBMS gilt NULL = NULL oder NULL $\neq$ NULL.
# <br><br>
# Beispiele: Sei der Wert von einer Variablen x NULL. Der Ausdruck x+3 ergibt NULL, da x NULL ist. Der Ausdruck NULL+3 ist unzulässig und kann so auch nicht geschrieben werden. Der Vergleich x=3 ergibt UNKNOWN, auch da x NULL ist.
# <br>
# <br>
# Weiterhin kann in der WHERE-Klausel mit IS NULL und IS NOT NULL überprüft werden, ob ein Wert NULL its. Z.B:
# ```
# Geburtstag IS NULL 
# ```
# ```
# Geburtstag IS NOT NULL
# ```

# ### Wahrheitswerte
# 
# |AND|true|unknown|false|
# |---|---|---|---|
# |**true**|true|unknown|false|
# |**unknown**|unknown|unknown|false|
# |**false**|false|false|false|
# 
# |OR|true|unknown|false|
# |---|---|---|---|
# |**true**|true|true|true|
# |**unknown**|true|unknown|unknown|
# |**false**|false|unknown|false|
# 
# |NOT|
# |---|
# |**true**|false|
# |**unknown**|unknown|
# |**false**|true|
# 
# Nehmen wir an TRUE=1, FALSE=0 und UNKNOWN = ½. Dann ergeben sich folgende Rechenregeln: 
# <br>
# AND: Minimum der beiden Werte
# <br>
# OR: Maximum der beiden Werte
# <br>
# NOT: 1 – Wert
# <br><br>
# Beispiele:
# <br>
# TRUE AND (FALSE OR NOT(UNKNOWN))
# <br>
# = MIN(1, MAX(0, (1 - ½ )))
# <br>
# = MIN(1, MAX(0, ½ )
# <br>
# = MIN(1, ½ ) = ½.
# <br><br>
# Zu beachten bei der Ausführungspriorität: NOT vor AND vor OR

# In[15]:


#SELECT * 
#FROM Film 
#WHERE Laenge <= 90 
#OR Laenge > 90; --Laenge <= 90 == UNKNOWN und Länge > 90

__SQL__ = "SELECT * FROM Film WHERE Laenge <= 90 OR Laenge > 90; --Laenge <= 90 == UNKNOWN und Länge > 90"
conn = sqlite3.connect("filme/filme.db")
df = pd.read_sql_query(__SQL__, conn)
df


# ### Sortierung
# In SQL sind Sortierungen(ASC für aufsteigend bzw. DESC für absteigend) mit der ORDER BY Klausel möglich, welche an das Ende der Anfrage geschrieben wird. ASC wird als default gewählt: 
# <br><br>
# ORDER BY \<Attributliste\> DESC/ASC
# <br><br>
# Im folgenden Beispiel wollen wir alle Attribute der Filmrelation ausgeben, welche von Disney produziert wurden und 1990 erschienen sind. Zusätzlich, soll die Ausgabe zuerst nach dem Attribut Laenge und folgend nach dem Attribut Titel aufsteigend sortiert werden.

# In[4]:


#SELECT * 
#FROM Film 
#WHERE StudioName = "Disney" 
#AND Jahr = 1990 ORDER BY Laenge, Titel;

__SQL__ = "SELECT * FROM Film WHERE StudioName = 'Disney' AND Jahr = 1990 ORDER BY Laenge,Titel;"
conn = sqlite3.connect("filme/filme.db")
df = pd.read_sql_query(__SQL__, conn)
df


# Hier wird  zuerst nach Laenge aufsteigend sortiert und folgend nach Titel aber absteigend.

# In[6]:


#SELECT * 
#FROM Film 
#WHERE StudioName = "Disney" 
#AND Jahr = 1990 ORDER BY Laenge ASC, Titel DESC;

__SQL__ = "SELECT * FROM Film WHERE StudioName = 'Disney' AND Jahr = 1990 ORDER BY Laenge ASC, Titel DESC;"
conn = sqlite3.connect("filme/filme.db")
df = pd.read_sql_query(__SQL__, conn)
df


# ## Anfragen über mehrere Relationen
# 
# ### Motivation
# Die Hauptstärke der Relationalen Algebra ist die Kombination von Relationen. Erst durch die Kombination mehrerer Relationen sind viele interessante Anfragen möglich. In SQL ist das möglich, indem man die beteiligten Relationen in der FROM-Klausel nennt.
# 
# ### Kreuzprodukt und Join
# 
# Im folgenden Beispiel haben wir die Relationen Film(Titel, Jahr, Länge, inFarbe, StudioName, ProduzentinID) und
# ManagerIn(Name, Adresse, ManagerinID, Gehalt) gegeben. Wir möchten nun alle Namen der Manager\*Innen ausgeben, die einen Star Wars Film produziert haben. Hierfür müssen die Relationen Film und ManagerIn gejoint werden.Zuerst bilden wir das Kruezprodukt der beiden Relationen, indem wir in der FROM-Klausel die Relationen mit einem Komma getrennt nennen , so wird intern das Kreuzprodukt dieser beiden gebildet. Schließlich wenden  wir noch einmal die Selektionsbedingung an, also dass nur ManagerInnen die einen Star Wars Film produziert haben ausgegeben werden. Und zuletzt noch die Joinbedingung, undzwar dass ProduzentinID und ManagerinID im Kreuzprodukt übereinstimmen sollen. Falls die beiden Bedinungen erfüllt sind wird ein Ergebnistupel produziert. Hierbei ist noch zu beachten, dass die Reihenfolge der WHERE-Bedingungen irrelevant ist.

# In[18]:


#SELECT Name 
#FROM Film, ManagerIn 
#WHERE Titel = "Star Wars" 
#AND ProduzentinID = ManagerinID; 

__SQL__ = "SELECT Name FROM Film, ManagerIn WHERE Titel = 'Star Wars' AND ProduzentinID = ManagerinID"
conn = sqlite3.connect("filme/filme.db")
df = pd.read_sql_query(__SQL__, conn)
df


# In[ ]:


#SELECT Name 
#FROM Film, ManagerIn --Kreuzprodukt
#WHERE Titel = ‘Star Wars‘--Selektionsbedingung 
#AND ProduzentinID = ManagerinID; --Joinbedingung


# In[19]:


#SELECT Name 
#FROM Film, ManagerIn 
#WHERE Titel = "Star Wars" 
#AND ProduzentinID = ManagerinID; 

__SQL__ = "SELECT Name FROM Film, ManagerIn WHERE Titel = 'Star Wars' AND ProduzentinID = ManagerinID"
conn = sqlite3.connect("filme/filme.db")
cur = conn.cursor()
df = pd.read_sql_query(__SQL__, conn)
df


# ### Uneindeutige Attributnamen
# 
# In diesem Beispiel haben wir die Relationen SchauspielerIn(Name, Adresse, Geschlecht, Geburtstag) und ManagerIn(Name, Adresse, ManagerinID, Gehalt) gegeben. Beide Relationen haben ein Attribut namens "Name". Wir wollen nun die Namen der Schauspieler\*Innen und Manager\*Innen ausgeben, die die selbe Adresse haben. Wie im vorherigen Beispiel,bilden wir wieder das Kreuzprodukt beider. Da nur der Attributname der Relationen uneindeutig wäre, muss in der Anfrage immer ein Präfix vor das Attribut gesetzt werden. Auch bei keiner Uneindeutigkeit, kann man das Präfix schreiben, was manchmal as Lesen von SQL-Anfragen erleichtert.

# In[20]:


#SELECT SchauspielerIn.Name, ManagerIn.Name 
#FROM SchauspielerIn, ManagerIn 
#WHERE SchauspielerIn.Adresse = ManagerIn.Adresse;


__SQL__ = "SELECT SchauspielerIn.Name, ManagerIn.Name FROM SchauspielerIn, ManagerIn WHERE SchauspielerIn.Adresse = ManagerIn.Adresse;"
conn = sqlite3.connect("filme/filme.db")
df = pd.read_sql_query(__SQL__, conn)
df


# ### Tupelvariablen
# In SQL ist es möglich einen Alias für eine Relation innerhalb einer Anfrage festzulegen. Dies ist sinnvoll, um die Tupeln, der beteiligten Relationen eindeutig zu Kennzeichnen, insbesondere wenn eine Relation mehrfach innerhalb einer Anfrage vorkommt. Umbenennung kann ebenfalls sinnvoll sein, um lange Relationennamen abzukürzen, um bessere Lesbarkeit zu schaffen. Ein Beispiel hierfür ist, z.B der Selfjoin im unteren Beispiel ,wo wir Schauspieler suchen, die zusammenleben. Und das Beispiel danach, wo wir Umbennenung zur Verkürzung der Anfrage benutzen.
# ```
# SchauspielerIn Star2
# ```
# ist äquivalent zu
# ```
# SchauspielerIn AS Star2
# ```

# In[21]:


#SELECT Star1.Name, Star2.Name 
#FROM SchauspielerIn Star1, SchauspielerIn Star2 
#WHERE Star1.Adresse = Star2.Adresse

__SQL__ = "SELECT Star1.Name, Star2.Name FROM SchauspielerIn Star1, SchauspielerIn Star2 WHERE Star1.Adresse = Star2.Adresse"
conn = sqlite3.connect("filme/filme.db")
df = pd.read_sql_query(__SQL__, conn)
df


# In[22]:


#SELECT S.Name, M.Name
#FROM SchauspielerIn S, ManagerIn M
#WHERE S.Adresse = M.Adresse;


__SQL__ = "SELECT S.Name, M.Name FROM SchauspielerIn S, ManagerIn M WHERE S.Adresse = M.Adresse;"
conn = sqlite3.connect("filme/filme.db")
df = pd.read_sql_query(__SQL__, conn)
df


# ### Tupelvariablen-Selfjoin
# 

# In[23]:


#SELECT Star1.Name, Star2.Name
#FROM SchauspielerIn Star1, SchauspielerIn Star2
#WHERE Star1.Adresse = Star2.Adresse;

__SQL__ = "SELECT Star1.Name, Star2.Name FROM SchauspielerIn Star1, SchauspielerIn Star2 WHERE Star1.Adresse = Star2.Adresse;"
conn = sqlite3.connect("filme/filme.db")
df = pd.read_sql_query(__SQL__, conn)
df


# Damit wir wie in der Ausgabe der obigen Beispiels, keine redundanten Tupel haben, setzten wir zusätzlich noch die Bedingung, dass die Namen der Schauspieler\*Innen verschieden sein müssen.

# In[24]:


#SELECT Star1.Name, Star2.Name
#FROM SchauspielerIn Star1, SchauspielerIn Star2
#WHERE Star1.Adresse = Star2.Adresse
#AND Star1.Name <> Star2.Name;

__SQL__ = "SELECT Star1.Name, Star2.Name FROM SchauspielerIn Star1, SchauspielerIn Star2 WHERE Star1.Adresse = Star2.Adresse AND Star1.Name <> Star2.Name;"
conn = sqlite3.connect("filme/filme.db")
cur = conn.cursor()
df = pd.read_sql_query(__SQL__, conn)
df


# ### Interpretation von Anfragen
# Anfragen können auf unterschiedlich Arten und Weisen interpretiert werden. Es gibt drie Interpretationsvarianten für Anfragen mit mehreren Relationen. Mit der Nested Loops(geschachtelte Schleifen) gibt es bei mehreren Tupelvariablen, für jede Variable eine geschachtelte Schleife. Bei der parallelen Zuordnung werden alle Kombinationen parallel bzgl. der Bedingungen geprüft. In der Relationen Algebra wird zuerst das Kreuzprodukt gebildet und dann auf jedes Resulat-Tupel die Selektionsbedingungen angewendet.
# <br>
# <br>
# Im folgenden Beispiel sind die Relationen R(A), S(A) und T(A) mit dem selben Attribut A gegeben. Wir suchen die folgenden Tupel R  ∩  (S  ∪  T) (= (R  ∩  S)  ∪  (R  ∩  T) ). Nehmen wir an dass T leer sei, das vermeintliche Resultat ist R  ∩  S. Mit Nested Loops ist das Ergebnis jedoch leer. 

# In[25]:


#SELECT R.A
#FROM R, S, T
#WHERE R.A = S.A
#OR R.A = T.A;

__SQL__ = "SELECT R.A FROM R, S, T WHERE R.A = S.A OR R.A = T.A;"
conn = sqlite3.connect("rst/rst.db")
df = pd.read_sql_query(__SQL__, conn)
df


# Im folgenden Beispiel ist das Ergebnis mit Nested Loops nicht leer.

# In[5]:


#SELECT *
#FROM
#(
#    (SELECT A FROM R)
#     INTERSECT
#    (SELECT * FROM
#     (SELECT A FROM S)
#      UNION
#    (SELECT A FROM T)
#   )
#)

__SQL__ = "SELECT * FROM (SELECT A FROM R INTERSECT SELECT * FROM (SELECT A FROM S) UNION SELECT A FROM T)"
conn = sqlite3.connect("rst/rst.db")
df = pd.read_sql_query(__SQL__, conn)
df


# ### Joins
# ![title](joins.jpg)

# Bis hierhin haben wir Joins nur mit Komma zwischen den Relationennamen in der FROM-Klausel und der Joinbedingung in der WHERE-Klausel kennengelernt. Kreuzprodukte können auch mit CROSS JOIN ausgedrückt werden,z.B Film CROSS JOIN spielt_in, hier werden direkt doppelte Attributnamen mit Präfix der Relation schon aufgelöst. 
# <br><br>
# Ein Beispiel für ein Theta-Join finden wir unten. 

# In[27]:


#SELECT * 
#FROM Film JOIN spielt_in ON Titel = FilmTitel 
#AND Jahr = FilmJahr

__SQL__ = "SELECT * FROM Film JOIN spielt_in ON Titel = FilmTitel AND Jahr = FilmJahr"
conn = sqlite3.connect("filme/filme.db")
df = pd.read_sql_query(__SQL__, conn)
df


# Beim JOIN werden im Vergleich zum CROSS JOIN die redundanten Attribute eliminiert. Damit das geschieht muss natürlich ein Fremdschlüsselbeziehung vorhanden sein oder die Attributnamen müssen identisch sein. Hier wie im unteren Beispiel gezeigt, werden also FilmTitel und FilmJahr eliminiert.

# In[28]:


#SELECT Titel, Jahr, Laenge, inFarbe, StudioName, ProduzentinID, Name 
#FROM Film JOIN spielt_in ON Titel = FilmTitel 
#AND Jahr = FilmJahr;

__SQL__ = "SELECT Titel, Jahr, Laenge, inFarbe, StudioName, ProduzentinID, Name FROM Film JOIN spielt_in ON Titel = FilmTitel AND Jahr = FilmJahr;"
conn = sqlite3.connect("filme/filme.db")
df = pd.read_sql_query(__SQL__, conn)
df


# Es ist ebenfalls möglich mehrere Joins hintereinander durchzuführen, wie im Beispiel unten gezeigt. 

# In[29]:


#SELECT Titel, Jahr 
#FROM Film JOIN spielt_in ON Titel = FilmTitel 
#AND Jahr = FilmJahr JOIN SchauspielerIn ON spielt_in.Name = SchauspielerIn.Name 
#WHERE Geschlecht = "f";

__SQL__ = "SELECT Titel, Jahr FROM Film JOIN spielt_in ON Titel = FilmTitel AND Jahr = FilmJahr JOIN SchauspielerIn ON spielt_in.Name = SchauspielerIn.Name WHERE Geschlecht = 'f'"
conn = sqlite3.connect("filme/filme.db")
df = pd.read_sql_query(__SQL__, conn)
df


# ### The TPC-H Schema
# ![title](tpc-h_schema.jpg)
# 
# Das TPC-H ist ein Benchmark, dessen Datensätze zufällig generiert werden. Die Daten sind an Unternehmen und ihren Handelsketten orientiert. Datenbankentwickler*\Innen benutzen TPC-H ,um neu entwickelte Systeme zu testen.  
# <br><br>
# Eine Beispielanfrage für das TPC-H Schema finden Sie unten.
#  
# #### TPC Query - Minimum Cost Supplier 

# In[14]:


#%sql
#SELECT s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone,
#s_comment
#FROM part, supplier, partsupp, nation, region
#WHERE p_partkey = ps_partkey AND s_suppkey = ps_suppkey
#AND p_size = 2 AND p_type like 'PROMO PLATED TIN'
#AND s_nationkey = n_nationkey AND n_regionkey = r_regionkey
#AND r_name = 'EUROPE'
#AND ps_supplycost =
#(SELECT min(ps_supplycost)
#FROM partsupp, supplier, nation, region
#WHERE p_partkey = ps_partkey AND s_suppkey = ps_suppkey
#AND s_nationkey = n_nationkey AND n_regionkey = r_regionkey
#AND r_name = 'EUROPE' )
#ORDER BY s_acctbal desc, n_name, s_name, p_partkey;


# In[12]:


__SQL__ = "SELECT s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment FROM part, supplier, partsupp, nation, region WHERE p_partkey = ps_partkey AND s_suppkey = ps_suppkey AND p_size = 2 AND p_type like 'PROMO PLATED TIN' AND s_nationkey = n_nationkey AND n_regionkey = r_regionkey AND r_name = 'EUROPE' AND ps_supplycost = (SELECT min(ps_supplycost) FROM partsupp, supplier, nation, region WHERE p_partkey = ps_partkey AND s_suppkey = ps_suppkey AND s_nationkey = n_nationkey AND n_regionkey = r_regionkey AND r_name = 'EUROPE' ) ORDER BY s_acctbal desc, n_name, s_name, p_partkey;"
conn = sqlite3.connect("salesDB/salesDB")
df = pd.read_sql_query(__SQL__, conn)
df


# #### The TPC-H Universal Table

# In[16]:


#%sql
#SELECT l_linenumber, l_quantity, l_extendedprice, l_discount, l_tax, l_returnflag, l_linestatus, l_shipdate, l_commitdate, l_receiptdate, l_shipinstruct, l_shipmode, l_comment, o_orderkey, o_orderstatus, o_totalprice, o_orderdate, o_orderpriority, o_clerk, o_shippriority, o_comment, ps_availqty, ps_supplycost, ps_comment, p_partkey, p_name, p_mfgr, p_brand, p_type, p_size, p_container, p_retailprice, p_comment, c_custkey, c_name, c_address, c_phone, c_acctbal, c_mktsegment, c_comment, s_suppkey, s_name, s_address, s_phone, s_acctbal, s_comment, n_nationkey, n_name, n_comment, r_regionkey, r_name, r_comment
#FROM lineitem, orders, partsupp, part, customer, supplier, nation, region
#WHERE p_partkey = ps_partkey
#AND s_suppkey = ps_suppkey
#AND n_nationkey = s_nationkey
#AND r_regionkey = n_regionkey
#AND c_custkey = o_custkey
#AND ps_partkey = l_partkey
#AND ps_suppkey = l_suppkey
#AND o_orderkey = l_orderkey


# In[15]:


__SQL__ = "SELECT l_linenumber, l_quantity, l_extendedprice, l_discount, l_tax, l_returnflag, l_linestatus, l_shipdate, l_commitdate, l_receiptdate, l_shipinstruct, l_shipmode, l_comment, o_orderkey, o_orderstatus, o_totalprice, o_orderdate, o_orderpriority, o_clerk, o_shippriority, o_comment, ps_availqty, ps_supplycost, ps_comment, p_partkey, p_name, p_mfgr, p_brand, p_type, p_size, p_container, p_retailprice, p_comment, c_custkey, c_name, c_address, c_phone, c_acctbal, c_mktsegment, c_comment, s_suppkey, s_name, s_address, s_phone, s_acctbal, s_comment, n_nationkey, n_name, n_comment, r_regionkey, r_name, r_comment FROM lineitem, orders, partsupp, part, customer, supplier, nation, region WHERE p_partkey = ps_partkey AND s_suppkey = ps_suppkey AND n_nationkey = s_nationkey AND r_regionkey = n_regionkey AND c_custkey = o_custkey AND ps_partkey = l_partkey AND ps_suppkey = l_suppkey AND o_orderkey = l_orderkey"
df = pd.read_sql_query(__SQL__, conn)
df


# ### Outer Joins

# Haben wir erneut die Relationen SchauspielerIn(Name, Adresse, Geschlecht, Geburtstag) und ManagerIn(Name, Adresse, ManagerinID, Gehalt) gegeben. Wir suchen nun alle Schauspieler\*Innen, die zugleich auch Manger\*Innen sind. 

# In[31]:


#SELECT Name, Adresse, Geburtstag, Gehalt 
#FROM SchauspielerIn 
#NATURAL INNER JOIN ManagerIn

__SQL__ = "SELECT Name, Adresse, Geburtstag, Gehalt FROM SchauspielerIn NATURAL INNER JOIN ManagerIn"
conn = sqlite3.connect("filme/filme.db")
df = pd.read_sql_query(__SQL__, conn)
df


# Nun suchen wir alle Schauspieler\*Innen und ihre Manager\*Inneninfo, falls diese vorhanden ist.

# In[32]:


#…FROM SchauspielerIn NATURAL LEFT OUTER JOIN ManagerIn

__SQL__ = "SELECT Name, Adresse, Geburtstag, Gehalt FROM SchauspielerIn NATURAL LEFT OUTER JOIN ManagerIn"
conn = sqlite3.connect("filme/filme.db")
df = pd.read_sql_query(__SQL__, conn)
df


# Falls keine Manager\*Ininfo vorhanden ist bleibt Gehalt NULL.

# Im Folgenden suchen wir Manager\*Innen und gegebenenfalls ihre Schauspieler\*Inneninfo

# In[9]:


#…FROM SchauspielerIn NATURAL RIGHT OUTER JOIN ManagerIn

__SQL__ = "SELECT Name, Adresse, Geburtstag, Gehalt FROM ManagerIn NATURAL RIGHT OUTER JOIN SchauspielerIn"
conn = sqlite3.connect("filme/filme.db")
df = pd.read_sql_query(__SQL__, conn)
df


# Wir sehen, dass RIGHT OUTER JOINS in sqlite3 nicht direkt möglich sind, da dieser Operator in sqlite3 nicht unterstützt wird. Man kann aber dennoch durch Vertauschen der Reihenfolge der Tabellen, die gewünschte Ausgabe mit LEFT OUTER JOINS erzeugen.

# In[8]:


__SQL__ = "SELECT Name, Adresse, Geburtstag, Gehalt FROM ManagerIn NATURAL LEFT OUTER JOIN SchauspielerIn"
conn = sqlite3.connect("filme/filme.db")
df = pd.read_sql_query(__SQL__, conn)
df


# Falls die Schauspieler\*Inneninfo nicht vorhanden ist bleibt Geburtstag NULL.

# Nun suchen wir alle Schauspieler\*innen und Manager\*innen.

# In[10]:


#…FROM SchauspielerIn NATURAL RIGHT OUTER JOIN ManagerIn

__SQL__ = "SELECT Name, Adresse, Geburtstag, Gehalt FROM SchauspielerIn NATURAL FULL OUTER JOIN ManagerIn"
conn = sqlite3.connect("filme/filme.db")
df = pd.read_sql_query(__SQL__, conn)
df


# Ebenso werden FULL OUTER JOINS in sqlite3 nicht unterstützt. Eine alternative Anfrage mit äquivalenter Ausgabe, die nur LEFT OUTER JOINS verwendet ist möglich. Ein FULL OUTER JOIN ist die Vereinigung von dem LEFT und RIGHT OUTER JOIN zweier Tabellen. Wie im vorherigen Beispiel gezeigt, können wir RIGHT OUTER JOINS mithilfe von LEFT OUTER JOINS erzeugen.

# In[34]:


__SQL__ = "SELECT Name, Adresse, Geburtstag, Gehalt FROM SchauspielerIn NATURAL LEFT OUTER JOIN ManagerIn UNION SELECT Name, Adresse, Geburtstag, Gehalt FROM ManagerIn NATURAL LEFT OUTER JOIN SchauspielerIn"
conn = sqlite3.connect("filme/filme.db")
df = pd.read_sql_query(__SQL__, conn)
df


# Falls zu den Schauspieler\*Innen die Manager\*Inneninfo bzw. Manager\*Innen die Schauspieler\*Inneninfo fehlt, bleiben Geburtstag oder Gehalt gegebenenfalls leer.

# Der Unterschied von FULL OUTER JOINS zu UNION ist, dass nur eine Zeile pro Person ausgegeben wird.

# ### Kreuzprodukt
# Wie aus der Relationalen Algebra bekannt bildet das Kreuzprodukt lle Paare aus Tupeln den beteiligten Relationen. In SQL können Kreuzprodukte mit CROSS JOIN gebildet werden, wie unten gezeigt oder auch mit Komma zwischen den beteiligten Relationen in der FROM-Klausel, wie ein Beispielt weiter gezeigt wird. Kreuzprodukte werden in der Regel selten verwendet, sie sind aber der Grundbaustein für Joins.

# In[35]:


#SELECT * 
#FROM SchauspielerIn CROSS JOIN Film

__SQL__ = "SELECT * FROM SchauspielerIn CROSS JOIN Film"
conn = sqlite3.connect("filme/filme.db")
df = pd.read_sql_query(__SQL__, conn)
df


# In[36]:


#SELECT * 
#FROM SchauspielerIn, Film

__SQL__ = "SELECT * FROM SchauspielerIn, Film"
conn = sqlite3.connect("filme/filme.db")
df = pd.read_sql_query(__SQL__, conn)
df


# ### Mengenoperationen in SQL
# Die Mengenoperationen UNION(Vereinigung), INTERSECT(Schnittmenge) und EXCEPT/MINUS(Differenz) können nur zwischen geklammertern Anfrageergebnissen benutzt werden, die das selbe Schema besitzen. Sobald einer dieser Operationen verwendet wird, wird implizit Mengensemantik verwendet. Möchte man Multimengensemantik haben, so müssen die Operatoren UNION ALL, INTERSECT ALL und EXCEPT/MINUS ALL verwendet werden. Das bietet sich an, wenn die Semantik egal ist oder die Mengeneigenschaft von Input und Output bereits bekannt ist.

# #### Schnittmenge: INTERSECT
# INTERSECT entspricht dem logischen „und“. Im Folgenden suchen wir die Schnittmenge zwischen den Namen und Adressen der Schauspieler\*Innen und den Mangager\*Innen.

# In[37]:


#(SELECT Name, Adresse FROM SchauspielerIn) INTERSECT (SELECT Name, Adresse FROM ManagerIn);

__SQL__ = "SELECT Name, Adresse FROM SchauspielerIn INTERSECT SELECT Name, Adresse FROM ManagerIn"
conn = sqlite3.connect("filme/filme.db")
df = pd.read_sql_query(__SQL__, conn)
df


# In diesem Beispiel suchen wir die Schnittmenge zwischen den Namen und Adressen der  weiblichen Schauspieler\*Innen und den Mangager\*Innen, die ein Gehalt größer als 1000000 haben.

# In[38]:


#%sql (SELECT Name, Adresse FROM SchauspielerIn WHERE Geschlecht = "f") INTERSECT (SELECT Name, Adresse FROM ManagerIn WHERE Gehalt > 1000000)

__SQL__ = "SELECT Name, Adresse FROM SchauspielerIn WHERE Geschlecht = 'f' INTERSECT SELECT Name, Adresse FROM ManagerIn WHERE Gehalt > 1000000"
conn = sqlite3.connect("filme/filme.db")
df = pd.read_sql_query(__SQL__, conn)
df


# #### Vereinigung: UNION
# UNION entspricht dem logischen „oder“. Im unteren Beispiel geben wir alle Namen und Adressen der Schauspieler\*Innen und den Mangager\*Innen aus.

# In[39]:


#(SELECT Name, Adresse FROM SchauspielerIn) UNION (SELECT Name, Adresse FROM ManagerIn);

__SQL__ = "SELECT Name, Adresse FROM SchauspielerIn UNION SELECT Name, Adresse FROM ManagerIn"
conn = sqlite3.connect("filme/filme.db")
df = pd.read_sql_query(__SQL__, conn)
df


# #### Differenz: EXCEPT/MINUS
# Im unteren Beispiel suchen wir den Titel und das Jahr jener Filme die in der Film-Relation vorkommen, aber nicht in der spielt_in-Relation. Damit diese Anfrage funktioniert, muss Umbenennung benutzt werden, da die beiden Mengen sonst nicht das selbe Schema besitzten.

# In[40]:


#(SELECT Titel, Jahr FROM Film) EXCEPT (SELECT FilmTitel AS Titel, FilmJahr AS Jahr FROM spielt_in) 

__SQL__ = "SELECT Titel, Jahr FROM Film EXCEPT SELECT FilmTitel AS Titel, FilmJahr AS Jahr FROM spielt_in"
conn = sqlite3.connect("filme/filme.db")
df = pd.read_sql_query(__SQL__, conn)
df


# #### Klammerung

# In[6]:


#SELECT *
#FROM
#(
#    (SELECT A FROM R)
#     INTERSECT
#    (SELECT * FROM
#     (SELECT A FROM S)
#      UNION
#    (SELECT A FROM T)
#   )
#)

__SQL__ = "SELECT * FROM (SELECT A FROM R INTERSECT SELECT * FROM (SELECT A FROM S) UNION SELECT A FROM T)"
conn = sqlite3.connect("rst/rst.db")
df = pd.read_sql_query(__SQL__, conn)
df


# ### Zusammenfassung der Semantik
# 
# 
# |R1|R2|UNION ALL|UNION|EXCEPT ALL|EXCEPT|INTERSECT ALL|INTERSECT|
# |---|---|---|---|---|---|---|---|
# |1|1|1|1|1|2|1|1|
# |1|1|1|2|2|5|1|3|
# |1|3|1|3|2|&#xfeff;|3|4|
# |2|3|1|4|2|&#xfeff;|4|
# |2|3|1|5|4|
# |2|3|2|&#xfeff;|5| 
# |3|4|2| 
# |4|&#xfeff;|2| 
# |4|&#xfeff;|3| 
# |5|&#xfeff;|3| 
# |&#xfeff;|&#xfeff;|3| 
# |&#xfeff;|&#xfeff;|3| 
# |&#xfeff;|&#xfeff;|3| 
# |&#xfeff;|&#xfeff;|4| 
# |&#xfeff;|&#xfeff;|4| 
# |&#xfeff;|&#xfeff;|4| 
# |&#xfeff;|&#xfeff;|5| 

# ## Geschachtelte Anfragen
# ### Motivation
# In vorherigen Beispielen haben wir schon geschachtelte Anfragen gesehen, nun betrachten wir diese etwas genauer. Eine Anfrage kann Teil einer anderen theoretisch beliebig tief geschachtelten Anfrage sein. Hier gibt es drei verschiedene Varianten:
# <br>
# 1. Die Subanfrage erzeugt einen einzigen Wert, der in der WHERE-Klausel mit einem anderen Wert verglichen werden kann.
# 2. Die Subanfrage erzeugt eine Relation, die auf verschiedene Weise in der WHERE-Klausel verwendet werden kann.
# 3. Die Subanfrage erzeugt eine Relation, die in der FROM Klausel (sozusagen als weitere Datenquelle) verwendet werden kann. – Wie jede andere normale Relation
# 
# ### Skalare Subanfragen
# Bei der ersten der drei Varianten von geschachtelten Anfrage, handelt es sich um skalare Subanfragen. Allgemeine Anfragen produzieren Relationen, mit mehreren Attributen, wo Zugriff auf ein bestimmtes Attribut auch möglich ist. Bei skalaren Subanfragen wird (garantiert) maximal nur ein Tupel und Projektion auf nur ein Attribut ausgegeben. Das Ergbenis einer skalaren Anfrage ist entweder genau ein Wert, der dann wie eine Konstante verwendet werden kann, oder wenn keine Zeilen gefunden werden, ist das Ergebnis der skalaren Anfrage NULL.
# <br>
# ![title](skalare_subanfragen.jpg)
# <br>
# Wir haben im Folgenden Beispiel die Relationen ManagerIn(Name, Adresse, ManagerinID, Gehalt)und Film(Titel, Jahr, Länge, inFarbe, StudioName, ProduzentinID) gegeben. Wir suchen nun den Produzent von Star Wars auf zwei Wegen, wobei garantiert ist, dass es nur einen Produzenten gibt. Zuerst suchen wir ,mithilfe einer allgemeinen Anfrage, unter allen Filmen jene mit dem Titel = 'Star Wars' und Jahr = 1977, wo die ProduzentinID mit der MangaerinID gematcht werden kann. Zuletzt geben wir den Namen aus.

# In[41]:


#SELECT Name 
#FROM Film, ManagerIn 
#WHERE Titel = ‘Star Wars‘ 
#AND Jahr = ‘1977‘ 
#AND ProduzentinID = ManagerinID;

__SQL__ = "SELECT Name FROM Film, ManagerIn WHERE Titel = 'Star Wars' AND Jahr = 1977 AND ProduzentinID = ManagerinID"
conn = sqlite3.connect("filme/filme.db")
df = pd.read_sql_query(__SQL__, conn)
df


# In dieser Variante suchen wir wieder den Produzent von Star Wars, jedoch mithile einer skalaren Subanfrage. Wir suchen zuerst die ProduzentinID des Films, wo Titel = 'Star Wars' und Jahr = 1977 gilt und vergleichen diesen einen mit der ManagerinID. Wenn eine identische ManagerinID gefunden wurde, geben wir den dazugehörigen Namen aus.

# In[42]:


#SELECT Name FROM ManagerIn 
#WHERE ManagerinID = ( SELECT ProduzentinID FROM Film WHERE Titel = "Star Wars" AND Jahr = 1977 );

__SQL__ = "SELECT Name FROM ManagerIn WHERE ManagerinID = ( SELECT ProduzentinID FROM Film WHERE Titel = 'Star Wars' AND Jahr = 1977 );"
conn = sqlite3.connect("filme/filme.db")
df = pd.read_sql_query(__SQL__, conn)
df


# Das DBMS erwartet maximal ein Tupel als Ergebnis der Teilanfrage, falls kein Tupel in der Subanfrage gefunden wird, ist das Ergebnis NULL, falls mehr als ein Tupel gefunden werden, wird ein Laufzeitfehler ausgegeben.

# #### Skalare Subanfragen – Beispiel 
# 
# Im folgenden Beispiel suchen wir die Abteilungen, deren durchschnittliche Bonuszahlungen höher sind als deren durchschnittliches Gehalt. Wir verwenden zwei Subanfragen, die einmal die durchschnittliche Bonuszahlung pro Abteilung ausgibt und einmal das durchschnittliche Gehalt pro Abteilung. Zuletzt vergleichen wir diese Werte miteinander und geben nur die aus, wo die durchschnittliche Bonuszahlung höher ist als das jeweilige durchschnittliche Gehalt.

# In[43]:


#SELECT a.Name, a.Standort 
#FROM Abteilung a 
#WHERE (SELECT AVG(bonus) 
#           FROM personal p 
#           WHERE a.AbtID = p.AbtID)>
#      (SELECT AVG(gehalt)
#            FROM personal p
#               WHERE a.AbtID = p.AbtID)

__SQL__ = "SELECT a.Name, a.Standort FROM Abteilung a WHERE (SELECT AVG(bonus) FROM personal p WHERE a.AbtID = p.AbtID)>(SELECT AVG(gehalt) FROM personal p WHERE a.AbtID = p.AbtID)"
conn = sqlite3.connect("abteilung/abteilung.db")
df = pd.read_sql_query(__SQL__, conn)
df


# In diesem Beispiel suchen wir alle Potsdamer Abteilungen mit ihrem jeweiligen Maximalgehalt. Auch hier benutzen wir wieder eine skalare Subanfrage. Wir geben neben der AbteilungsID, dem Abteilungsnamen, zusätzlich noch das Maximum aller Gehälter der jeweiligen Abteilung als maxGehatlt aus, die sich in Potsdam befindet.

# In[3]:


#SELECT a.AbtID, a.Name,
#           (SELECT MAX(Gehalt)
#                FROM Personal p
#            WHERE a.AbtID = p.AbtID) AS maxGehalt
#FROM Abteilung a
#WHERE a.Ort = ‘Potsdam‘

__SQL__ = "SELECT a.AbtID, a.Name, (SELECT MAX(Gehalt) FROM Personal p WHERE a.AbtID = p.AbtID) AS maxGehalt FROM Abteilung a WHERE a.Standort = 'Potsdam'"
conn = sqlite3.connect("abteilung/abteilung.db")
df = pd.read_sql_query(__SQL__, conn)
df


# In dieser Beispielanfrage suchen wir erneut alle Potsdamer Abteilungen mit ihrem jeweiligen Maximalgehalt. Im Vergleich zu der vorherigen Anfrage, können im Ergebnis dieser Anfrage Abteilungen ohne Mitarbeiter nicht vorkommen.

# In[45]:


#SELECT a.AbtID, a.Name, MAX(p.Gehalt) AS maxGehalt
#FROM Abteilung a, Personal p
#WHERE a.Ort = ‘Potsdam‘
#AND a.AbtID = p.AbtID
#GROUP BY a.AbtID, a.Name

__SQL__ = "SELECT a.AbtID, a.Name, MAX(p.Gehalt) AS maxGehalt FROM Abteilung a, Personal p WHERE a.Standort = 'Potsdam' AND a.AbtID = p.AbtID GROUP BY a.AbtID, a.Name"
conn = sqlite3.connect("abteilung/abteilung.db")
cur = conn.cursor()
df = pd.read_sql_query(__SQL__, conn)
df


# ### Bedingungen mit Relationen
# Nun betrachten wir weitere SQL Operatoren auf Relationen die Boole‘sche Werte erzeugen:
# <br><br>
# Um zu überprüfen ob eine Relation leer oder nicht ist, kann der EXISTS-Operator benutzt werden: 
# <br>
# EXISTS R gibt TRUE zurück, falls R nicht leer ist
# <br><br>
# Um zu überprüfen ob ein Wert in einer Relation mind. einmal vorkommt, kann der IN-Operator benutzt werden:
# <br>
# x IN R gibt TRUE zurück, falls x gleich einem Wert in R ist (R hat nur ein Attribut)
# <br><br>
# Um zu überprüfen ob x nicht in R vorkommt, kann NOT IN benutzt werden:
# <br>
# x NOT IN R gibt TRUE zurück, falls x keinem Wert in R gleicht
# <br><br>
# Um, zu überprüfen ob ein Wert größer als alle Werte in R ist, kann der ALL-Operator benutzt werden:
# <br>
# x > ALL R gibt TRUE zurück, falls x größer als jeder Wert in R ist (R hat nur ein Attribut)
# <br>
# x <> ALL R entspricht x NOT IN R bzw. auch NOT(x in R)
# <br>
# Natürlich kann man alternativ auch die anderen Vergleichsoperatoren verwenden: <, >, <=, >=, <>, =
# <br><br>
# Um zu überprüfen, ob ein Wert größer als mind. ein Wert aus einer Relation ist, kann der ANY-Operator benutzt werden
# <br>
# x > ANY R gibt TRUE zurück, falls x größer als mindestens ein Wert in R ist (R hat nur ein Attribut)
# <br>
# Auch hier kann man natürlich auch alternativ die anderen Vergleichsoperatoren verwenden: <, >, <=, >=, <>, =
# <br>
# x = ANY R entspricht x IN R
# <br>
# Ein alternativer Befehl für ANY ist SOME
# <br><br>
# Die Negation mit NOT(…) ist immer möglich.
# ### EXISTS Beispiele
# Im folgenden Beispiel wollen wir die ISBNs aller ausgeliehenen Bücher ausgeben. Hierbei verwenden wir den EXISTS-Operator und geben jene ISBNs aus der Relation BuchExemplar aus, dessen Inventarnr in der Relation Ausleihe existiert.

# In[46]:


#SELECT ISBN
#FROM BuchExemplar
#WHERE EXISTS
#     (SELECT *
#      FROM Ausleihe
#      WHERE Ausleihe.Inventarnr = BuchExemplar.Inventarnr) 

__SQL__ = "SELECT ISBN FROM BuchExemplar WHERE EXISTS (SELECT * FROM Ausleihe WHERE Ausleihe.Inventarnr = BuchExemplar.Inventarnr) "
conn = sqlite3.connect("buecher/buecher.db")
cur = conn.cursor()
df = pd.read_sql_query(__SQL__, conn)
df


# Im folgenden Beispiel suchen wir die Lehrstuhlbezeichnungen der Professor\*innen, die alle von ihnen gelesenen Vorlesungen auch schon einmal geprüft haben bzw. Lehrstuhlbezeichnungen von Professor\*innen, wo keine von diesem/er gelesene Vorlesung existiert, die von ihm/ihr nicht geprüft wurde. 

# In[18]:


#SELECT Lehrstuhlbezeichnung
#FROM Prof
#WHERE NOT EXISTS
#      (SELECT *
#       FROM Liest
#       WHERE Liest.PANr = Prof.PANr
#       AND NOT EXISTS (SELECT *
#                   FROM Prueft
#                   WHERE Prueft.PANr = Prof.PANr
#                   AND Prüft.VL_NR = Liest.VL_NR)
#) 

__SQL__ = "SELECT Lehrstuhlbezeichnung FROM Prof WHERE NOT EXISTS (SELECT * FROM Liest WHERE Liest.PA_Nr = Prof.PA_Nr AND NOT EXISTS (SELECT * FROM Prueft WHERE Prueft.PA_Nr = Prof.PA_Nr AND Prueft.VL_NR = Liest.VL_NR)) "
conn = sqlite3.connect("lehre/lehre.db")
df = pd.read_sql_query(__SQL__, conn)
df


# ### IN Beispiele
# Im folgenden Beispiel suchen wir eine Auswahl an Büchern mit bestimmter ISBN.

# In[47]:


#SELECT Titel
#FROM Bücher
#WHERE ISBN IN (3898644006, 1608452204, 0130319953)

__SQL__ = "SELECT Titel FROM BuchExemplar WHERE ISBN IN (3898644006, 1608452204, 0130319953)"
conn = sqlite3.connect("buecher/buecher.db")
df = pd.read_sql_query(__SQL__, conn)
df


# Hier suchen wir die Matrikelnr. der Studierenden, die zumindest einen Prüfer/in gemeinsam mit dem Studierenden mit der Matrikelnr. ‚123456‘ haben. 

# In[20]:


#SELECT DISTINCT Matrikel
#FROM Prüft
#WHERE Prüfer IN ( SELECT Prüfer
#                  FROM Prüft
#                  WHERE Matrikel = 123456) 

__SQL__ = "SELECT DISTINCT Matrikel FROM Prueft WHERE Pruefer IN ( SELECT Pruefer FROM Prueft WHERE Matrikel = 123456) "
conn = sqlite3.connect("lehre/lehre.db")
df = pd.read_sql_query(__SQL__, conn)
df


# Eine Alternativanfrage, welche dieselbe Ausgabe erzeugt, aber nicht den IN-Operator benutzt:

# In[21]:


#SELECT DISTINCT P1.Matrikel
#FROM Prueft P1, Prueft P2
#WHERE P2.Matrikel = 123456
#AND P1.Pruefer = P2.Pruefer

__SQL__ = "SELECT DISTINCT P1.Matrikel FROM Prueft P1, Prueft P2 WHERE P2.Matrikel = 123456 AND P1.Pruefer = P2.Pruefer"
conn = sqlite3.connect("lehre/lehre.db")
df = pd.read_sql_query(__SQL__, conn)
df


# In diesem Beispiel geben wir alle Nachnamen aller Professor\*innen aus, die schon einmal eine 1,0 vergeben haben.

# In[25]:


#SELECT Nachname
#FROM Prof
#WHERE 1.0 IN ( SELECT Note
#FROM Prüft
#WHERE Prüfer = Prof.ID )

__SQL__ = "SELECT Nachname FROM Prof WHERE 1.0 IN ( SELECT Note FROM Prueft WHERE Pruefer = ProfID )"
conn = sqlite3.connect("lehre/lehre.db")
df = pd.read_sql_query(__SQL__, conn)
df


# Achtung: Korrelierte Subanfrage, die Subanfrag wird für jede ProfID ausgeführt.
# 
# ### ALL und ANY Beispiele
# 
# Im folgenden Beispiel suchen wir die schlechteste Note des Studierenden mit der Matrikelnr. 123456.

# In[3]:


#SELECT Note
#FROM Prüft
#WHERE Matrikel = ‘123456‘
#AND Note >= ALL (SELECT Note
#                 FROM Prüft
#                 WHERE Matrikel = ‘123456‘)

__SQL__ = "SELECT Note FROM Prueft WHERE Matrikel = ‘123456‘ AND Note >= ALL (SELECT Note FROM Prueft WHERE Matrikel = ‘123456‘)"
conn = sqlite3.connect("lehre/lehre.db")
df = pd.read_sql_query(__SQL__, conn)
df


# Wie man sehen kann wird der Operator ALL nicht von sqlite3 unterstützt. Stattdessen kann man eine äquivalente Anfrage mithilfe MAX() formulieren.

# In[27]:


__SQL__ = "SELECT Note FROM Prueft WHERE Matrikel = 123456 AND Note >= (SELECT MAX(Note) FROM Prueft WHERE Matrikel = 123456)"
conn = sqlite3.connect("lehre/lehre.db")
df = pd.read_sql_query(__SQL__, conn)
df


# Im folgenden Beispiel suchen wir alle Studierenden, die mindestens eine Prüfung absolviert haben.

# In[4]:


#SELECT Name, Matrikel
#FROM Student
#WHERE Matrikel = ANY (SELECT Matrikel
#                      FROM Prueft)

__SQL__ = "SELECT Name, Matrikel FROM Student WHERE Matrikel = ANY (SELECT Matrikel FROM Prueft)"
conn = sqlite3.connect("lehre/lehre.db")
df = pd.read_sql_query(__SQL__, conn)
df


# Wie man sehen kann wird der Operator ANY nicht von sqlite3 unterstützt. Stattdessen kann man eine äquivalente Anfrage mithilfe IN formulieren.

# In[5]:


__SQL__ = "SELECT Name, Matrikel FROM Student WHERE Matrikel IN (SELECT Matrikel FROM Prueft)"
conn = sqlite3.connect("lehre/lehre.db")
df = pd.read_sql_query(__SQL__, conn)
df


# ### Bedingungen mit Tupeln
# Verallgemeinerungen von IN, ALL und ANY auf Tupel sind auch möglich. 
# <br><br>
# t IN R gibt TRUE zurück, falls t ein Tupel in R ist (mehr als ein Attribut möglich). Hierbei ist vorausgesetzt, dass beide dasselbe Schemata haben und dieselbe Reihenfolge der Attribute.
# <br><br>
# t > ALL R gibt TRUE zurück, falls t größer als jedes Tupel in R ist. Die Vergleiche finden in Standardreihenfolge der Attribute statt.
# <br><br>
# t <> ANY R gibt TRUE zurück, falls R mindestens ein Tupel hat, das ungleich t ist.
# <br>
# <br>
# Im folgenden Beispiel wollen wir alle Namen von Produzenten von Filmen mit Harrison Ford ausgeben. Wir suchen erst Titel und Jahr aller Filme mit Harrison Ford mithilfe einer Subanfrage. Für jene Filme suchen wir dann die ProduzentinIDs und gleichen die mit den ManagerinIDs ab, zuletzt geben wir die Namen der passenden Manager\*Innen aus.

# In[58]:


#SELECT Name 
#FROM ManagerIn 
#WHERE ManagerinID IN( SELECT ProduzentinID FROM Film WHERE (Titel, Jahr) 
#IN( SELECT FilmTitel AS Titel, FilmJahr AS Jahr FROM spielt_in WHERE Name = "Harrison Ford"));

__SQL__ = "SELECT Name FROM ManagerIn WHERE ManagerinID IN( SELECT ProduzentinID FROM Film WHERE (Titel, Jahr) IN( SELECT FilmTitel AS Titel, FilmJahr AS Jahr FROM spielt_in WHERE Name = 'Harrison Ford'))"
conn = sqlite3.connect("filme/filme.db")
df = pd.read_sql_query(__SQL__, conn)
df


# Es gibt auch eine alternative Formulierung der Anfrage ohne IN. Wir joinen ManagerIn, Film und spielt_in und geben jene Manager\*Innamen aus, wo spielt_in.Name Harrison Ford entspricht.

# In[59]:


#SELECT ManagerIn.Name 
#FROM ManagerIn, Film, spielt_in 
#WHERE ManagerinID = ProduzentinID 
#AND Titel = FilmTitel 
#AND Jahr = FilmJahr 
#AND spielt_in.Name = "Harrison Ford";

__SQL__ = "SELECT ManagerIn.Name FROM ManagerIn, Film, spielt_in WHERE ManagerinID = ProduzentinID AND Titel = FilmTitel AND Jahr = FilmJahr AND spielt_in.Name = 'Harrison Ford'"
conn = sqlite3.connect("filme/filme.db")
df = pd.read_sql_query(__SQL__, conn)
df


# ### Subanfragen in FROM-Klausel
# Wir können anstelle einer einfachen Relation auch eine geklammerte Subanfrage in der FROM-Klausel schreiben. Der Subanfrage mussein Alias vergeben werden, um auf die Attribute zuzugreifen.
# <br><br>
# Im folgenden Beispiel wollen wir wieder alle Namen von Produzenten von Filmen mit Harrison Ford ausgeben. Wir stellen eine Subanfrage in der FROM-Klausel, die alle ProduzentinIDs zurückgibt, welche in Filmen mit Harrison Ford beteiligt waren. Zum Schluss werden die ProduzentinIDs wieder mit den ManagerinIDs abgeglichen.

# In[60]:


#SELECT M.Name 
#FROM ManagerIn M, (SELECT ProduzentinID AS ID FROM Film, spielt_in WHERE Titel = FilmTitel AND Jahr = FilmJahr AND Name = "Harrison Ford") ProduzentIn 
#WHERE M.ManagerinID = ProduzentIn.ID;

__SQL__ = "SELECT M.Name FROM ManagerIn M, (SELECT ProduzentinID AS ID FROM Film, spielt_in WHERE Titel = FilmTitel AND Jahr = FilmJahr AND Name = 'Harrison Ford') ProduzentIn WHERE M.ManagerinID = ProduzentIn.ID"
conn = sqlite3.connect("filme/filme.db")
df = pd.read_sql_query(__SQL__, conn)
df


# ### Korrelierte Subanfragen
# Wird eine Subanfragen einmalig ausgeführt, so handelt es sich um eine unkorrelierte Subanfrage. Korrelierte Subanfragen werden mehrfach ausgeführt, undzwar einmal pro Bindung der korrelierten Variable der äußeren Anfrage.
# <br><br>
# Im folgenden ein Beispiel für eine korrelierte Subanfrage. Wir suchen alle mehrfachen Filme mit Ausnahme der jeweils jüngsten Ausgabe. Die Subanfrage wird für jedes Tupel in Filme ausgeführt.

# In[63]:


#SELECT Titel, Jahr 
#FROM Film Alt 
#WHERE Jahr < ANY ( SELECT Jahr FROM Film WHERE Titel = Alt.Titel);


#ohne ANY
__SQL__ = "SELECT Titel, Jahr FROM Film Alt WHERE Jahr < (SELECT MIN(Jahr) FROM Film WHERE Titel = Alt.Titel)"
conn = sqlite3.connect("filme/filme.db")
df = pd.read_sql_query(__SQL__, conn)
df


# Nun suchen wir die Namen und Gehälter aller Mitarbeiter\*Innen in Potsdam, wir formulieren zunächst eine Anfrage mit einer unkorrelierten und dann eine mit einr korrelierte Subanfrage.
# <br><br>
# Unten wird die Subanfrage nur einmal ausgeführt, da wir sofort alle AbtIDs haben. Daher handelt es sich hierbei um eine unkorrelierte Subanfrage.

# In[64]:


#SELECT Name, Gehalt
#FROM Personal p
#WHERE AbtID IN
#    (SELECT AbtID
#    FROM Abteilung
#    WHERE Ort =
#‘Potsdam‘)

__SQL__ = "SELECT Name, Gehalt FROM Personal p WHERE AbtID IN (SELECT AbtID FROM Abteilung WHERE Standort = 'Potsdam')"
conn = sqlite3.connect("abteilung/abteilung.db")
df = pd.read_sql_query(__SQL__, conn)
df


# Hierbei handelt es sich um eine korrelierte Subanfrage, aufgrund des p.AbtID, da die Subanfrage für jedes Tupel aus Personal p ausgeführt werden muss.

# In[65]:


#SELECT Name, Gehalt
#FROM Personal p
#WHERE Gehalt >
#    (SELECT 0.1*Budget
#    FROM Abteilung a
#    WHERE a.AbtID =
#p.AbtID)

__SQL__ = "SELECT Name, Gehalt FROM Personal p WHERE Gehalt > (SELECT 0.1*Budget FROM Abteilung a WHERE a.AbtID = p.AbtID)"
conn = sqlite3.connect("abteilung/abteilung.db")
df = pd.read_sql_query(__SQL__, conn)
df


# ## Operationen auf einer Relation
# ### Duplikateliminierung
# Wie aus der Relationalen Algebra bekannt, ist die Duplikateliminierung auch in SQL möglich. Relationale DBMS verwenden i.d.R. Multimengensemantik und nicht Mengensemantik. Durch Operationen, wie das Enfügen von Duplikaten in Basisrelationen, die Veränderung von Tupeln in Basisrelationen, Projektion in Anfragen, Subanfragen mit z.B UNION ALL oder die Vermehrung von Duplikaten durch Kreuzprodukte, entstehen Duplikate.
# 
# Um Duplikate zu eliminieren kann man das DISTINCt-Schlüsselwort benutzen, nach folgendem Schema:
# ```
# SELECT DISTINCT Attributnamen
# ```
# So wird gewährleistet, dass jedes projezierte Element aus Attributnamen nur einmal in der Ausgabe vorkommt. Zu beachten ist noch, dass DISTINCT eine kostenaufwändige Operation ist, da die Ausgabe einmal auf Duplikate hin durchsucht werden muss, mithilfe Sortierung oder Hashing.
# <br><br>
# Im folgenden Beispiel suchen wir alle Filme, in denen mindestens ein Schauspieler mitspielt. In der Relation spielt_in sind pro Schauspieler Titel und Jahr vorhanden. 

# In[66]:


#SELECT DISTINCT FilmTitel, FilmJahr 
#FROM spielt_in

__SQL__ = "SELECT DISTINCT FilmTitel, FilmJahr FROM spielt_in"
conn = sqlite3.connect("filme/filme.db")
df = pd.read_sql_query(__SQL__, conn)
df


# ![title](duplikateliminierung.jpg)
# 

# Wir erinnern uns zurück an die Anfragen, wo wir die Produzent\*Innen von Filmen mit Harrison Ford gesucht haben. Einmal sind wir an das Ergebnis durch Subanfragen gelangt und auf einem anderen Wege mit einem Join. Nun sind beide Anfragen nicht äquivalent, da bei der Anfrage mit dem Join Duplikate möglich sind, welches sich aber mit dem DISTINCT-Schlüsselwort lösen lässt.

# ### Aggregation
# Die aus der Relationalen Algebra bekannte Aggregation ist auch in SQL möglich, die Standardaggregationsoperatoren SUM, AVG, MIN, MAX, COUNT können auf einzelne Attribute in der SELECT-Klausel angewendet werden. Zudem gibt es noch weitere Aggregationsoperatoren wir z.B VAR, STDDEV für die Varianz und Standardabweichung. Es wird auch COUNT(\*) häufig benutzt, welches die Anzahl der Tupel in der Relation, die durch die FROM und WHERE Klauseln definiert wird zählt. Auch die Kombination mit DISTINCT wird häufig benutzt wie z.B COUNT(DISTINCT Jahr) SUM(DISTINCT Gehalt)
# 
# #### Aggregation – Beispiele
# Im folgenden Beispiel möchten wir das Durchschnittsgehalt aller Manager*\Innen ausgeben.

# In[3]:


#SELECT AVG(Gehalt) 
#FROM ManagerIn;

__SQL__ = "SELECT AVG(Gehalt) FROM ManagerIn"
conn = sqlite3.connect("filme/filme.db")
df = pd.read_sql_query(__SQL__, conn)
df


# In diesem Beispiel möchten wir alle Einträger der Relation spielt_in zählen.

# In[69]:


#SELECT COUNT(*) 
#FROM spielt_in;

__SQL__ = "SELECT COUNT(*) FROM spielt_in;"
conn = sqlite3.connect("filme/filme.db")
df = pd.read_sql_query(__SQL__, conn)
df


# In diesem Beispiel zählen wir alle Schauspiel in der spielt_in Relation, jedoch wird doppelt gezählt.

# In[70]:


#SELECT COUNT(Name) 
#FROM spielt_in;

__SQL__ = "SELECT COUNT(Name) FROM spielt_in;"
conn = sqlite3.connect("filme/filme.db")
df = pd.read_sql_query(__SQL__, conn)
df


# Mit DISTINCT wird nicht mehr doppelt gezählt.

# In[71]:


#SELECT COUNT(DISTINCT Name) 
#FROM spielt_in 
#WHERE FilmJahr = 1990;

__SQL__ = "SELECT COUNT(DISTINCT Name) FROM spielt_in WHERE FilmJahr = 1990;"
conn = sqlite3.connect("filme/filme.db")
df = pd.read_sql_query(__SQL__, conn)
df


# ### Gruppierung, Aggregation und NULL
# NULL wird bei der Aggregation ignoriert und trägt somit nicht zu SUM, AVG oder COUNT bei und wird auch nicht als MIN oder MAX ausgegeben. Um die Anzahl der nicht-NULL Werte zuzählen, kann also folgende Anfrage benutzt werden:
# ```
# SELECT COUNT(Länge) FROM Film;
# ```
# 
# Bei der Gruppierung ist NULL ein eigener Gruppierungswert, also gibt es z.B die NULL-Gruppe. Um das zu veranschaulichen betrachten wir die folgende Relation R:
# 
# |A|B|
# |---|---|
# |NULL|NULL|
# 
# 
# SELECT A, COUNT(B) FROM R GROUP BY A;
# <br>
# Ergebnis: (NULL, 0)
# <br><br>
# SELECT A, SUM(B) FROM R GROUP BY A;
# <br>
# Ergebnis: (NULL, NULL)
# 
# 
# ### Gruppierung
# Auch die aus der Relationalen Algebra bekannte Gruppierung ist in SLQ möglich mittels GROUP BY nach der WHERE-Klausel. Bei der Gruppierung gibt es in der SELECT-Klausel zwei "Sorten" von Attributen, einmal Gruppierungsattribute und einmal aggregierte Attribute. Nicht-aggregierte Werte der SELECT-Klausel müssen in der GROUP BY-Klausel erscheinen, es müssen jedoch keiner der beiden Sorten erscheinen. Eine Gruppierung mit Aggregation können wir im unteren Beispiel sehen.

# In[72]:


#SELECT StudioName, SUM(Laenge) 
#FROM Film GROUP BY StudioName

__SQL__ = "SELECT StudioName, SUM(Laenge) FROM Film GROUP BY StudioName"
conn = sqlite3.connect("filme/filme.db")
df = pd.read_sql_query(__SQL__, conn)
df


# In diesem Beispiel lassen wir die Aggregation weg und suchen nur die Studionamen gruppiert bei StudioName.

# In[73]:


#SELECT StudioName 
#FROM Film 
#GROUP BY StudioName

__SQL__ = "SELECT StudioName FROM Film GROUP BY StudioName"
conn = sqlite3.connect("filme/filme.db")
df = pd.read_sql_query(__SQL__, conn)
df


# In diesem Beispiel suchen wir nur die Gesamtlänge der Studios.

# In[74]:


#SELECT SUM(Laenge) 
#FROM Film 
#GROUP BY StudioName

__SQL__ = "SELECT SUM(Laenge) FROM Film GROUP BY StudioName"
conn = sqlite3.connect("filme/filme.db")
df = pd.read_sql_query(__SQL__, conn)
df


# In[75]:


#SELECT Name, SUM(Laenge) 
#FROM ManagerIn, Film 
#WHERE ManagerinID = ProduzentinID 
#GROUP BY Name

__SQL__ = "SELECT Name, SUM(Laenge) FROM ManagerIn, Film WHERE ManagerinID = ProduzentinID GROUP BY Name"
conn = sqlite3.connect("filme/filme.db")
df = pd.read_sql_query(__SQL__, conn)
df


# Wenn mehrere Relationen verwendet werden, wie im obigen Beispiel wird die Gruppierung am Schluss durchgeführt. Sie können sich an die folgende Reihenfolge der Ausführung (und des Lesens) richten:
# <br>
# 1. FROM-Klausel
# <br>
# 2. WHERE-Klausel
# <br>
# 3. GROUP BY-Klausel
# <br>
# 4. SELECT-Klausel
# <br>
# <br>

# Möchte man nun die Ergebnismenge nach der Gruppierung einschränken, so geht das nicht durch eine zusätzliche Bedingung in der WHERE-Klausel, sondern es muss das Schlüsselwort HAVING benutzt werden.Benutzt man zusätzlich noch Aggregationen in der HAVING-Klausel, so beziehen sich diese nur auf die aktuelle Gruppe. Wie bei der SELECT-Klausel, dürfen bei der Gruppierung in der HAVING-Klausel nur un-aggregierte Gruppierungsattribute erscheinen.
# <br>
# <br>
# Wir möchten die Summe der Filmlänge von Manager\*Innen ausgeben, dessen Gehälter über 1000000 liegt. Das untere Beispiel erfüllt nicht die Anfrage.

# In[1]:


#SELECT Name, SUM(Laenge) 
#FROM ManagerIn, Film 
#WHERE ManagerinID = ProduzentinID 
#AND Gehalt > 1000000 GROUP BY Name

__SQL__ = "SELECT Name, SUM(Laenge) FROM ManagerIn, Film WHERE ManagerinID = ProduzentinID AND Gehalt > 1000000 GROUP BY Name"
conn = sqlite3.connect("filme/filme.db")
df = pd.read_sql_query(__SQL__, conn)
df


# Wie oben schon genannt muss HAVING benutzt werden, um die Ergebnismenge nach der Gruppierung einzuschränken, wie um unteren Beispiel dargestellt wird.

# In[77]:


#SELECT Name, SUM(Laenge) 
#FROM ManagerIn, Film 
#WHERE ManagerinID = ProduzentinID 
#GROUP BY Name HAVING SUM(Laenge) > 200

__SQL__ = "SELECT Name, SUM(Laenge) FROM ManagerIn, Film WHERE ManagerinID = ProduzentinID GROUP BY Name HAVING SUM(Laenge) > 200"
conn = sqlite3.connect("filme/filme.db")
df = pd.read_sql_query(__SQL__, conn)
df


# In diesem Beispiel geben wir nur die Namen der Manager\*Innen aus und benutzten Aggregation, um diese zu filtern.

# In[78]:


#SELECT Name 
#FROM ManagerIn, Film 
#WHERE ManagerinID = ProduzentinID 
#GROUP BY Name HAVING SUM(Laenge) > 200

__SQL__ = "SELECT Name FROM ManagerIn, Film WHERE ManagerinID = ProduzentinID GROUP BY Name HAVING SUM(Laenge) > 200"
conn = sqlite3.connect("filme/filme.db")
df = pd.read_sql_query(__SQL__, conn)
df


# ### Zusammenfassung SQL
# Hier werden nocheinmal die Grundbausteine einer SQL Anfrage (mit empfohlener Lesereihenfolge) aufgelistet.

# 6\. SELECT
# <br>
# 1\. FROM
# <br>
# 2\. WHERE
# <br>
# 3\. GROUP BY
# <br>
# 4\. HAVING
# <br>
# 5\. ORDER BY

# Bei einer Anfrage die auf eine Datenbank zugreift sins SELECT … FROM … Pflicht. Zuletzt darf HAVING nur in Kombination mit GROUP BY erscheinen.

# ## Datenbearbeitung(DML)
# Zuvor haben wir SQL nur als Anfragesprache betrachtet. In diesem Kapitel betrachten wir SQL nun als DMl(Data Manipulation Language), also das Bearbeiten von Daten. In SQL stehen folgende Funktione zur Verfügung um Daten zu bearbeiten Create, Read, Update und Delete(CRUD). Um einzelne Tupel einzufügen, zu löschen und zu ändern.
# 
# 
# ### Einfügen
# Als Grundbaustein für das Einfügen in einer Relation R, muss man folgendem Schema folgen INSERT INTO R($A_1$, …, $A_n$) VALUES ($v_1$,…,$v_n$), wobei $A_1$,...,$A_n$ die Attribute der Relation R sind und $v_1$ ,...,$v_n$ die zu einfügenden Werte. Hierbei muss die Reihenfolge der Werte und Attribute beachtet werden, die Reihenfolge sollte entsprechend der Spezifikation des Schemas (CREATE TABLE ...) erfolgen. Falls beim INSERT Attribute fehlen, wird der Default-Wert aus der Tabellendefinition eingesetzt bzw. NULL, falls nicht anders angegeben wurde. 
# <br><br>
# Ein Beispiel für das Einfügen eines Tupels in die spielt_in-Relation ist unten zu finden.

# In[ ]:


get_ipython().run_line_magic('sql', 'INSERT INTO spielt_in(FilmTitel, FilmJahr, Schauspieler) VALUES (‘Star Wars‘, 1977, ‘Alec Guinness‘);')


# Falls alle Attribute gesetzt werden, kann die Attributliste auch ausgelassen werden, wie unten zu sehen ist.

# In[ ]:


get_ipython().run_line_magic('sql', 'INSERT INTO spielt_in VALUES (‘Star Wars‘, 1977, ‘Alec Guinness‘);')


# #### Einfügen per Anfrage
# In SQL ist es auch möglich Einfügeoperationen mit Anfragen zu kombinieren.
# <br>
# <br>
# Haben wir die beiden Relationen Studio(Name, Adresse, VorsitzendeID) und Film(Titel, Jahr, Länge, inFarbe, StudioName, ProduzentinID). Nun kann es sein, dass Studios in der Film-Relation vorkommen, aber nicht in der Studio-Relation. Wir möchten also alle Studios der Film-Relation ind die Studio-Relation einfügen. In der unteren Anfrage fügen wir jene StudioNamen in die Studio-Relation ein, die nicht in der Studio-Relation vorkommen. Jedoch bleiben bei dieser Anfrage die Attribute Adresse und VorsitzendeID auf NULL, welches im Allgemeinen Redundanz erzeugt, was vermieden werden sollte.

# In[ ]:


get_ipython().run_line_magic('sql', '')
INSERT INTO Studio(Name)
SELECT DISTINCT StudioName
FROM Film
WHERE StudioName NOT IN
    (SELECT Name
    FROM Studio);


# ### Ausführungsreihenfolge beim Einfügen
# 
# Betrachten wir wieder das vorherige Beispiel, einmal mit DISTINCT und einmal ohne. Wir fragen uns, ob jedes mal wenn, ein StudioName gefunden wurde, der noch nicht in der Tabelle enthalten ist, dieser direkt schon in die Tabelle eingefügt wird oder ob zuerst die ganze Anfrage ausgeführt wird. Tatsächlich ist es in SQL Standard so, dass zuerst die gesamte Anfrage ausgeführt wird und dann erst in die Relation eingefügt wird.

# In[ ]:


get_ipython().run_line_magic('sql', '')
INSERT INTO Studio(Name)
SELECT DISTINCT StudioName
FROM Film
WHERE StudioName NOT IN
    (SELECT Name
    FROM Studio);


# In[ ]:


get_ipython().run_line_magic('sql', '')
INSERT INTO Studio(Name)
SELECT StudioName
FROM Film
WHERE StudioName NOT IN
    (SELECT Name
    FROM Studio);


# #### Bulk insert
# Beim INSERT werden die Daten zeilenbasiert aus SQL statements eingefügt. Es ist möglich, dass die Daten ,die in eine Datenbank eingefügt werden sollen schon in einer bestimmten Form vorliegen. Da bietet es sich an den Befehl IMPORT zu benutzten, mitdem Daten aus einer Datei Zeilenbasiert eingefügt werden. Hierbei bleiben die gesetzten Trigger und Nebenbedingungen weiterhin aktiv und auch die Indizes werden laufend aktualisiert.
# <br><br>
# Eine deutlich effizientere Weise Daten einzufügen ist mit LOAD, hier wird seitenbasiert aus einer Datei eingefügt, wobei Trigger und Nebenbedingungen nicht berücksichtigt werden und die Indizes am Ende neu generiert werden. Man muss beachten, dass die Syntax von IMPORT und LOAD jeweils DBMS-spezifisch ist, z.B gibt es in sqlite keinen LOAD-Befehl.
# 
# ### Löschen
# Der Grundbaustein zum Löschen von Tupeln ist DELETE FROM R WHERE …, wobei R wie beim Einfügen eine Relation ist. Beim Delete werden immer ganze Tupel gelöscht. Im Gegensatz zum Einfügen, können die zu löschenden Tupel nicht direkt angegeben werden, sondern müssen in der WHERE-Klausel umschrieben werden. Um ein konkretes Tupel zu löschen, müssen also alle Werte dieses Tupel oder wenn vorhanden eine ID bekannt sein. Es werden alle Tupel gelöscht für die TRUE in der WHERE-Kausel gilt. Es ist auch möglich die WHERE-Klausel wegzulassen, dann werden alle Tupel der Relation gelöscht. Unten finden Sie einige Beispiele.

# In[ ]:


get_ipython().run_line_magic('sql', '')
DELETE FROM spielt_in
WHERE FilmTitel = ‘The Maltese Falcon‘
AND FilmJahr = 1942
AND Schauspieler = ‘Sydney Greenstreet‘;


# In[ ]:


get_ipython().run_line_magic('sql', '')
DELETE FROM Manager
WHERE Gehalt < 10000000;


# In[ ]:


get_ipython().run_line_magic('sql', '')
DELETE FROM Manager;


# ### Verändern (update)
# Der Grundbaustein zum Verändern von Tupeln ist UPDATE R SET … WHERE …, wobei auch hier R eine Relation ist. In der SET-Klausel werden komma-separiert Werte zugewiesen. Im Beispiel unten wird in der Managerrelation vor dem Name jener Manager\*Innen eine 'Präs.' gesetzt, dessen Manager\*InID in den Präsident\*InnenIDs vorkommt.
# 

# In[ ]:


get_ipython().run_line_magic('sql', '')
UPDATE Manager
SET Name = ‘Präs. ‘ || Name
WHERE ManagerinID IN
(SELECT PräsidentID FROM Studios);


# ## Schemata(DDL)
# ### Überblick
# In diesem Kapitel betrachten wir SQL als Data Definition Language(DDL). Möchte man eine neue Tabelle anlegen, müssen die verschiedenen Datentypen, Default-Werte, Indizes und damit zusammenhängende Tabellen beachten, welche wir uns in diesem Kapitel genauer anschauen.
# 
# ### Datentypen
# 
# Die vorhandenen Datentypen hängen von dem benutzten DBMS ab, wir betrachten die Datentypen von DB2 von IBM. Jedes definierte Attribut muss einen Datentyp haben. Es gibt: 
# <br>
# - CHAR(n) – String fester Länge (n Zeichen) 
# <br>
# - VARCHAR(n) – String variabler Länge, maximal n Zeichen 
# <br>
# - BIT(n) bzw. BIT VARYING(n) – Wie CHAR, aber Bits 
# <br>
# - BOOLEAN – TRUE, FALSE oder UNKNOWN 
# <br>
# - INT / INTEGER bzw. SHORTINT – 8 bzw. 4 Byte 
# <br>
# - FLOAT / REAL bzw. DOUBLE PRECISION 
# <br>
# - DECIMAL (n,d) – Z.B. Gehalt DECIMAL(7,2) – 7 Stellen, davon 2 Nachkommastellen
# <br>
# - CLOB und BLOB
# <br><br>
# Unten finden Sie einen Überblick aller DB2 Datentypen.
# 
# ### Überblick DB2 Datentypen
# ![title](db2_datentypen.jpg)

# ### Tabellen
# Der Grundbaustein zum Erzeugenvon Tabellen ist CREATE TABLE R …, wobei R der Name der Tabelle ist. In runden Klammern werden kommasepariert die gewünschten Attribute mit den jeweiligen Datentypen genannt. 

# In[ ]:


get_ipython().run_line_magic('sql', '')
CREATE TABLE Schauspieler (
Name CHAR(30),
Adresse VARCHAR(255),
Geschlecht CHAR(1),
Geburtstag DATE );


# Um eine Tabelle zu löschen wird DROP TABLE R ... verwendet.
# <br><br>
# Auch das Verändern des Tabellenschemas ist möglich, undzwar mit ALTER TABLE R ... . Es können neue Attribute hinzugefügt werden, alte gelöscht oder auch Datentypen von bestehenden Attributen verändert werden. Zu beachten ist, dass bei dem Hinzufügen von neuen Attributen Nullwerte entstehen.
# <br>
# - ALTER TABLE Schauspieler ADD Telefon CHAR(6);
# <br>
# - ALTER TABLE Schauspieler DROP Geburtstag;
# <br>
# - ALTER TABLE Schauspieler MODIFY Telefon CHAR(10);

# ### Default-Werte
# Default-Werte können mit dem Schlüsselwort DEFAULT gesetzt werden. In dem Beispiel unten wird für das Attribut Geschlecht der Default-Wert '?' bestimmt und für den Geburtstag das Default-Datum '0000-00-00'.

# In[ ]:


get_ipython().run_line_magic('sql', '')
CREATE TABLE Schauspieler (
Name CHAR(30),
Adresse VARCHAR(255),
Geschlecht CHAR(1) DEFAULT ‚?‘,
Geburtstag DATE DEFAULT DATE ‚'0000-00-00');


# Ein Default-Wert kann auch nachträglich mit einem ALTER TABLE hinzugefügt werden.

# In[ ]:


get_ipython().run_line_magic('sql', '')
ALTER TABLE Schauspieler
ADD Telefon CHAR(16) DEFAULT ‚unbekannt‘;


# ### Indizes
# Ein Index auf einem Attribut ist eine Datenstruktur, die es dem DBMS erleichtert, Tupel mit einem bekannten Wert des Attributs zu finden. Indizes sind nicht SQL-Standard, aber sind in (fast) jedem DBMS verfügbar.
# <br><br>
# Möchten wir z.B alle Disney Filme aus 1990 ausgeben. Wir könnte mit Variante 1 alle Tupel der Filmerelation durchsuchen und die WHERE Bedingung prüfen. Mit Variante 2 erstellen wir einen Index CREATE INDEX JahrIndex ON Film(Jahr) und können direkt alle Filme aus 1990 betrachten und diese auf ‚Disney‘ prüfen, da der Optimizer des DBMS unsern erstellten Inddex sofort zur Filterung der Bedingung Jahr = 1990 benutzen kann. Zuletzt in einer dritten Variante erstellen wir einen multidimensionalen Index CREATE INDEX JahrStudioIndex ON Film(Jahr, Studioname) und holen uns direkt alle Filme aus 1990 von Disney. Welche der Varianten wir letzlich wählen, hängt von zu erwartenden Anfragen ab. Bei dem Anlegen von Indizes muss auch beachtet werden, dass diese Speicher belegen und aktualisiert werden müssen, wenn neue Daten hinzugefügt wurden.

# In[79]:


#%sql SELECT * 
#FROM Film 
#WHERE StudioName = "Disney" 
#AND Jahr = 1990;

__SQL__ = "SELECT * FROM Film WHERE StudioName = 'Disney' AND Jahr = 1990"
conn = sqlite3.connect("filme/filme.db")
df = pd.read_sql_query(__SQL__, conn)
df


# Indizes auf einzelnen Attributen:

# In[ ]:


get_ipython().run_line_magic('sql', '')
CREATE INDEX JahrIndex ON Film(Jahr);


# Indizes auf mehreren Attributen:

# In[ ]:


get_ipython().run_line_magic('sql', '')
CREATE INDEX JahrStudioIndex
ON Film(Jahr, Studioname);


# Die Reihenfolge der Relationen bei Indizes auf mehreren Attributen ist wichtig. Wenn der Index sort-basiert ist, wird nach Jahr sortiert und für jedes Jahr jeweils nach Studioname. Für unser Beispiel wird mplizit zuerst nach Jahr gefolgt von StudioName gesucht.
# <br><br>
# Um einen Index zu löschen kann DROP INDEX ... verwendet werden.

# In[ ]:


get_ipython().run_line_magic('sql', '')
DROP INDEX JahrIndex;


# #### Indexwahl
# Aufgrund der Kosten muss die Indexwahl abgewogen werden. Zum einen beschleunigen Indizes Punkt- (und Bereichs-) Anfragen und Join-Anfragen erheblich, aber das Einfügen, Löschen und Verändern von Tupeln der Relation wird verlangsamt, da der Index immer wieder aktualisiert werden muss. Zudem benötigen Indizes auch noch Speicherplatz.
# 
# Die Wahl der besten Indizes ist eine der schwierigsten Aufgaben des Datenbankdesigns, in welcher auch viel Forschung betrieben wird. Im Idealfall ist die Vorhersage der Query Workload und Update-Frequenz bekannt und es werden Attribute gewählt mit denen häufig Konstanten verglichen werden oder die häufig als Joinattribute fungieren.
# 
# #### Indexwahl – Vorüberlegungen
# 
# Bei Vorüberlegungen zur Indexwahl muss ebenso beachtet werden, wie Indizes implementiert sind. Typischerweise sind Relationen über mehrere Diskblöcke gespeichert, wobei sich die wichtigsten Datenbankkosten aus der Anzahl, der in den Hauptspeicher gelesenen Diskblöcke bildet. Anders müssen bei Punktanfragen mit einem Index nur ein Block, statt allen gelesen werden, aber der Index selbst muss auch gespeichert und gelesen werden. In der Regel sind viel mehr Tupel pro Block repräsentiert und es werden häufig nur Schlüsselwerte und Speicheradresse und keine Daten gespeichert. Beim Updaten sind die Kosten sogar doppelt, da die Blöcke für das Lesen und Schriben der Index-Blöcke geladen werden muss.
# 
# #### Indexwahl – Beispiel
# Nun schauen wir uns ein Beispiel an. Haben wir die Relation spielt_in(FilmTitel, FilmJahr, SchauspielerName) udn die Variablen s,t,j gegeben und möchten drei typische Anfragen ausführen. Wir suchen einma lden Titel und das Jahr eines bestimmten Filmes s, den Schauspieler der in einem bestimmten Film eines bestimmten Jahres mitgespielt hat und wollen zuletzt in die Relation spielt_in Tupel einfügen.

# In[7]:


get_ipython().run_line_magic('sql', '')
SELECT FilmTitel, FilmJahr FROM spielt_in WHERE Name = s;


# In[ ]:


get_ipython().run_line_magic('sql', '')
SELECT SchauspielerName FROM spielt_in
WHERE FilmTitel = t AND FilmJahr = j;


# In[ ]:


get_ipython().run_line_magic('sql', '')
INSERT INTO spielt_in VALUES(t, j, s);


# Wir nehmen an, dass spielt_in auf 10 Disk-Blöcke verteilt ist. Im Durchschnitt hat jeder Film 3 Schauspiel und jeder Schauspieler spielte in 3 Filmen mit. Im schlimmsten Fall sind 3 Tupel auf 3 Blöcke verteilt und eine Index ist auf einem Block gespeichert. Die Operationen Lesen und Schreiben kosten 1 und Update und Insert kosten jeweils 2.
# 
# #### Indexwahl – Beispiel
# Im fogenden sind die Kosten der drei Anfragen tabellarisch aufgeführt. Die Variable p1 bildet den Anteil der Anfrage 1, p2 den Anteil der Anfrage 2 und 1-p1-p2 den Anteil der Anfrage 3.
# 
# |Anfrage|Kein Index|SchauspielerIndex|FilmIndex|Beide Indizes|
# |---|---|---|---|---|
# |**Schauspieler = s**|10|4|10|4|
# |**FilmTitel = t AND FilmJahr = j**|10|10|4|4|
# |**INSERT INTO spielt_in**|2|4|4|6|
# |**Gesamtkosten**|2+8$p_1$8$p_2$|4+6$p_2$|4+6$p_1$|6-2$p_1$-2$p_2$|

# ### Verteilung in IMDB (Real-world Daten, Stand ca. 2010)
# Im folgenden betrachten wir eine größere Datenbank, die dem Sternenschema folgt. In der Mitte sehen wir die Relation Movie und daherum viele weitere Relationen die mit der Movie_ID in Verbindung stehen.
# 
# ![title](imdb.jpg)
# 
# Wir wollen nun die Durchschnittliche Anzahl an Schauspieler\*Innen pro Film und umgekehrt berechnen und benutzen das Schlüsselwort WITH, um bestimmte Anfragen mit einem Alias vorzudefinieren.

# In[ ]:


get_ipython().run_line_magic('sql', '')
WITH
m AS (SELECT count(*) AS ZahlMovies FROM imdb.movie),
actress AS (SELECT count(*) AS ZahlActress FROM imdb.actress),
actor AS (SELECT count(*) AS ZahlActor FROM imdb.actor),
actors AS (SELECT (ZahlActress + ZahlActor) AS GesamtActors FROM actress, actor)

SELECT DOUBLE(actors.GesamtActors) / DOUBLE(m.ZahlMovies)
FROM m, actors


# Schauspieler*in pro Spielfilm: 8,7

# In[ ]:


get_ipython().run_line_magic('sql', '')
WITH
actors AS (SELECT * FROM imdb.actor UNION SELECT * FROM imdb.actress),
counts AS (SELECT name, count(movie_id) AS m FROM actors GROUP BY name)

SELECT AVG(DOUBLE(m)) FROM counts


# Spielfilme pro Schauspieler: 4,2

# ## Sichten
# ### Virtuelle Relationen
# 
# Bisher kennen wir nur Relationen, die aus CREATE TABLE Ausdrücken existieren und tatsächlich (materialisiert, physisch) in der Datenbank vorhanden sind. Dieses sind persistent und auf ihnen können Updates ausgeführt werden. In diesem Kapitel beschäftigen wir uns mit Sichten. Sichten entsprechen Anfragen, denen man einen Namen gibt. Sie wirken wie physische Relationen, jedoch existieren die Daten aus Sichten nur virtuell und Updates darauf sind nur manchmal möglich. Views stellen Separation of Concern dar, können Effizienz verbessern und ermöglichen einfachere Anfragen.
# <br>
# <br>
# ![title](stonebraker1.jpg)
# <br>
# ![title](stonebraker2.jpg)
# <br>
# Michael Stonebraker: Implementation of Integrity Constraints and Views by Query Modification. SIGMOD Conference 1975: 65-78

# ### Sichten in SQL
# Der Grundbaustein zum erstellen von Sichten(Views) ist CREATE VIEW Name AS Anfrage. In der Anfrage dürfen Relationen auch gejoint sein.
# <br><br>
# Im folgenden erstellen wir eine View auf alle Filme von Paramount und nennen die View ParamountFilme.

# In[ ]:


get_ipython().run_line_magic('sql', '')
CREATE VIEW ParamountFilme AS
SELECT Titel, Jahr
FROM Film
WHERE StudioName = "Paramount";


# Bei einer Anfrage an eine Sicht, wird die Anfrage aus der Sichtdefinition ausgeführt und die ursprüngliche Anfrage verwendet das Ergebnis dann als Relation. Bei Änderungen der zugrundeliegenden Relationen ändern sich quch die Daten der Sicht.
# <br><br>
# Um eine Sicht zu löschen kann DROP VIEW Name, für unser Beispiel DROP VIEW ParamountFilme, benutzt werden, das Löschen der Sicht hat keinen Einfluss auf die Basisdaten
# 
# ### Anfragen an Sichten
# Wir suchen nun alle Filme von Paramount aus 1979 und tun dies indem wir eine Anfrage an unsere ParamountFilme-Sicht stellen. Ohne Sicht müssten wir die Anfrage in eine Anfrage an die Basisrelation umwandeln wie eine Codezelle weiter zu sehen ist.

# In[ ]:


get_ipython().run_line_magic('sql', '')
SELECT Titel
FROM ParamountFilme
WHERE Jahr = 1979;


# In[81]:


get_ipython().run_line_magic('sql', '')
SELECT Titel 
FROM Film 
WHERE StudioName = "Paramount" 
AND Jahr = 1979;


# Ebenso sind Anfrage zugleich an Sichten und Basisrelationen möglich, wie unten gezeigt.

# In[82]:


get_ipython().run_line_magic('sql', '')
SELECT DISTINCT SchauspielerIn
FROM ParamountFilme, spielt_in
WHERE Titel = FilmTitel AND Jahr = FilmJahr;


# Im Folgenden nochmal ein weiteres Beispiel. Haben wir die Relationen Film(Titel, Jahr, Länge, inFarbe, StudioName, ProduzentinID) und ManagerIn (Name, Adresse, ManagerinID, Gehalt) gegeben. Wir erstellen eine View von allen Filmproduzent\*Innen und suchen mit der Sicht den/die Profuzent\*In für den Film Gone with the Wind.

# In[ ]:


get_ipython().run_line_magic('sql', '')
CREATE VIEW FilmeProduzentenInnen AS
    SELECT Titel, Name
    FROM Film, ManagerIn
    WHERE ProduzentinID = ManagerinID;


# In[83]:


get_ipython().run_line_magic('sql', '')
SELECT Name 
FROM FilmeProduzenten 
WHERE Titel = ‘Gone with the Wind‘


# Dieselbe Anfrage an die Basisrelation

# In[84]:


get_ipython().run_line_magic('sql', '')
SELECT Name 
FROM Film, ManagerIn 
WHERE ProduzentinID = ManagerinID 
AND Titel = 'Gone with the Wind';


# Es ist auch möglich die Attribute der Basisrelation in der Sicht umzubennen. Im Beispiel unten wird aus Titel FilmTitel und ManagerIn zu Produzentenname in der Sicht.

# In[ ]:


get_ipython().run_line_magic('sql', '')
CREATE VIEW FilmeProduzenten(FilmTitel, Produzentenname) AS
SELECT Titel, Name
FROM Film, ManagerIn
WHERE ProduzentinID = ManagerinID;


# Sichten können auch nur zur Umbennenung dienen, wie unten gezeigt.

# In[ ]:


get_ipython().run_line_magic('sql', '')
CREATE VIEW Movie(title, year, length, inColor, studio, producerID) AS
SELECT *
FROM Film;


# ### Diskussion
# Die Vorteile von Sichten beinhalten die Vereinfachung von Anfragen, sowie die Strukturierung der Datenbank. Es wird ebenfalls eine logische Datenunabhängigkeit geschaffen. Der Zugriff auf die Daten kann beschränkt werden, z.B könnten wir für unser Beispiel nur Paramount-Mitarbeiter\*Innen den Zugriff auf die Sicht ParamountFilme erlauben.
# <br>
# 
# □ Logische Datenunabhängigkeit
# <br>
# – Sichten stabil bei Änderungen der Datenbankstruktur
# <br>
# – Sichtdefinitionen müssen gegebenenfalls angepasst werden
# <br>
# – Stabilität nicht bei jeder Änderung
# <br>
# □ Optimierung durch materialisierte Sichten
# <br><br>
# 
# Weiterhin bleibt die Änderung auf Sichten ein Problembereich, sowie die Updatepropagierung für materialisierte Sichten. Auch die automatische Anfragetransformation gestaltet sich mit Sichten schwieriger.
# 
# 
# ### Updates auf Sichten
# In einigen Fällen ist es möglich, Einfüge-, Lösch- oder Updateoperationen auf Sichten durchzuführen. Hier stellen sich die Fragen: Wo sind die Sichten gespeichert? Welche Relationen sind betroffen? Wie verläuft die Zuordnung der Änderung zur Sicht?
# <br><br>
# In den meisten Fällen wird die Update-Operation einer Sicht auf eine Update-Operation der zugrunde liegenden Basisrelationen übersetzt. Hierbei darf kein DISTINCT, sondern nur eine normales SELECT verwendet werden. Eine gute Kenntnis der Datenbank muss vorausgesetzt sein, da durch das Vergessen mancher Attribute Inkonsistenzen durch NULL-Werte entstehen können.
# <br><br>
# □ Nur bei einer Relation
# <br>
# – Keine Subanfragen mit Selbstbezug
# <br>
# □ Nur bei normalem SELECT
# <br>
# – Kein DISTINCT
# <br>
# □ Nur falls genug Attribute verwendet werden, so dass alle anderen Attribute mit NULL oder dem Default-Wert gefüllt werden können.
# 
# ### Einfügen auf Sichten – Beispiel
# 
# Haben wir die Relation Filme(Titel, Jahr, Länge, inFarbe, StudioName, ProduzentinID) gegeben. Wir wollen nun einen weiteren Film in unsere ParamountFilme-Sicht einfügen.

# In[ ]:


get_ipython().run_line_magic('sql', '')
CREATE VIEW ParamountFilme AS
    SELECT Titel, Jahr
    FROM Filme
    WHERE StudioName = ‚Paramount‘;


# In[ ]:


get_ipython().run_line_magic('sql', '')
INSERT INTO ParamountFilme
VALUES (‚Star Trek‘, 1979);


# Das Einfügen wie oben dargestellt ist nicht erlaubt, das kein Wert für Studioname vorhanden ist und nicht überprüft wern kann, ob es sich um ein Paramountfilm handelt. Unten sehen wir eine korrekte Weise des Einfügens in die Sicht. Es wurde eine neue Sicht erstellt die StudioName beinhaltet. Der StudioName bei der Einfügeoperation muss Paramount sein, da kein anderer StudioName der Sicht entspricht. Das Neue Tupel ist (‚Star Trek‘, 1979, 0, NULL, ‚Paramount‘, NULL).

# In[ ]:


get_ipython().run_line_magic('sql', '')
CREATE VIEW ParamountFilme AS
    SELECT Titel, Jahr, StudioName
    FROM Filme
    WHERE StudioName = ‚Paramount‘;


# In[ ]:


get_ipython().run_line_magic('sql', '')
INSERT INTO ParamountFilme
VALUES (‚Star Trek‘, 1979, ‚Paramount‘);


# ### Löschen und Updates auf Sichten
# Im Folgenden möchten wir alle Filme aus unserer Sicht entfernen die 'Trek' im Filmtitel enthalten.

# In[ ]:


get_ipython().run_line_magic('sql', '')
DELETE FROM ParamountFilme
WHERE Titel LIKE ‚%Trek%‘;


# Diese Anfrage wird umgeschrieben zu der unteren.

# In[ ]:


#Korrekte Anfrage
get_ipython().run_line_magic('sql', '')
DELETE FROM Filme
WHERE Titel LIKE ‚%Trek%‘ AND StudioName = ‚Paramount‘;


# Auch bei einem Update muss die Prüfbedingung der Sicht mit übernommen werden.

# In[ ]:


get_ipython().run_line_magic('sql', '')
UPDATE ParamountFilme
SET Jahr = 1979
WHERE Titel = ‚Star Trek the Movie‘;


# In[ ]:


#Korrekte Anfrage
get_ipython().run_line_magic('sql', '')
UPDATE Filme
SET Jahr = 1979
WHERE Titel = ‚Star Trek the Movie‘ AND StudioName = ‚Paramount‘;


# ### Tupelmigration
# Angenommen wir erstellen eine Sicht auf die Relation ManagerIn(Name, Adresse, ManagerinID, Gehalt), welche alle Manager\*Innen mit einem Gehalt größer als 2 Millionen beinhaltet. 

# In[ ]:


get_ipython().run_line_magic('sql', '')
CREATE VIEW Reiche AS
    SELECT Name, Gehalt, ManagerinID
    FROM ManagerIn
    WHERE Gehalt > 2000000;


# Nun updaten wir unsere View, sodass der Manager mit der MnagerinID=25 ein Gehalt von 1,5 Millionen haben muss. Das Tupel (‚Eisner\`, ‚Hollywood‘, 25, 3000000), welches vor dem Update noch in der Sicht enthalten war, wird danach aus der Sicht „herausbewegt“.

# In[ ]:


get_ipython().run_line_magic('sql', '')
UPDATE Reiche SET Gehalt = 1500000
WHERE ManagerinID = 25;


# Um Tupelmigration zu verhindern, können problematische Update durch WITH CHECK OPTION abgelehnt werden.

# In[1]:


get_ipython().run_line_magic('sql', '')
CREATE VIEW Reiche AS
SELECT Name, Gehalt
FROM ManagerIn
WHERE Gehalt > 2000000
WITH CHECK OPTION;


# ### Anfrageplanung mit Sichten
# Üblicherweise werden Anfragen in Form eines Baums dargestellt. Die Blätter repräsentieren Basisrelationen und Sichten. Die Sichten können auch durch die Sichtdefinitionen erstezt werden.
# <br>
# Ein Beispiel hierfür sehen wir in der unteren Abbildung. Die Dreiecke sind die Anfragen und die Kreise Sichten. Wir ersetzen die Sichten v und w durch ihre Sichtdefinitionen und sehen, das w eine weitere Sicht z in Anspruch nimmt.

# ![title](anfrageplanung1.jpg)
# 

# Betrachten wir wieder unsere Beispielsicht ParamountFilme. Wir möchten nun die unten stehende Anfrage ausführen. 

# In[ ]:


#Sicht
get_ipython().run_line_magic('sql', '')
CREATE VIEW ParamountFilme AS
SELECT Titel, Jahr
FROM Filme
WHERE StudioName = ‚Paramount‘;


# In[14]:


#Anfrage
SELECT Titel 
FROM ParamountFilme 
WHERE Jahr = 1979;


# ![title](anfrageplanung2.jpg)
# <br><br>
# Hier wird die Sichtendefinition der ParamountFilme dargestellt.
# <br><br>
# ![title](anfrageplanung3.jpg)
# <br><br>
# Im zweiten Schritt sehen wir die Ausführungsreihenfolge der Anfrage, die direkt auf der Sicht ParamountFilme ausgeführt wird
# <br><br>
# ![title](anfrageplanung4.jpg)
# <br><br>
# Zuletzt sehen wir, dass ParamountFilme durch die Sichtendefnition ersetzt wurde.

# ### Materialisierte Sichten
# In der realen Welt ist es möglich, dass viele Anfragen an eine Datenbank sich häufig wiederholen, wie z.B bei Business Reports, Bilanzen, Umsätze oder Bestellungsplanung, Produktionsplanung oder auch bei der Kennzahlenberechnung. Diese vielen Anfragen sind oft Variationen mit gemeinsamen Kern. Um Ressourcen zu sparen kann eine Anfrage als Sicht einmalig berechnet und dann materialisiert werden. So kann die Sicht automatisch und transparent in folgenden Anfragen wiederbenutzt werden.
# <br><br>
# Drei Folien nach Prof. Ulf Leser, HU Berlin
# 
# #### MV – Themen und Probleme
# Es stellt sich die Frage welche Views nun zur Materialisierung ausgewählt werden, hierbei müssen die Kosten(Platz und Aktualisierungsaufwand) von MV beachtete werden, als auch der Workload und die Menge von MVs, beeinflussen die optimale Wahl.
# <br><br>
# Ein anderes Problemengebiet ist die automatische Aktualisierung von MVs, wie also z.B mit einer Aktualisierung bei Änderungen der Basisrelationen umgegangen wird, v.A. bei Aggregaten, Joins, Outer-Joins usw. . Hierfür bieten sich
# Algorithmen zur inkrementellen Aktualisierung an.
# <br><br>
# Weiterhin stellt sich auch die Frage, wie die Verwendung von MVs bei der Ausführung von Anfragen automatisiert wird. Die Schwierigkeit dieser Aufgabe hängt von der Komplexität der Anfragen bzw. Views ab, da das Umschreiben der Anfrage notwendig ist. Demnach werden Algorithmen zur transparenten und kostenoptimalen Verwendung der materialisierten Sichten notwendig.
# 
# ### „Answering Queries using Views“
# Angenommen wir habene ine Anfrage Q und eine Menge V (materialisierten) von Sichten gegeben. Es stellen sich folgende Fragen:
# <br>
# - Kann man Q überhaupt unter Verwendung von V beantworten?
# <br>
# - Kann man Q nur mit V beantworten?
# <br>
# - Kann man Q mit V vollständig beantworten?
# <br>
# - Ist es günstig, Sichten aus V zur Beantwortung von Q zu verwenden? Welche?

# ## Zusammenfassung
# In diesem Kapitel haben wir uns mit der Anfragesprache SQL beschäftigt. Zuerst haben wir uns mit dem Grundgerüst aller SQL-Anfragen dem SFW(SELECT FROM WHERE) Block beschäftigt, gefolgt von Subanfragen in der FROM- und WHERE-Klausel und den Schlüsselwörtern EXISTS, IN, ALL, ANY ,die genutzt werden um Bedingungen an Relationen zu stellen. Weiterhin haben wir die Mengenoperationen UNION, INTERSECT, EXCEPT und diesbezüglich DISTINCT,ALL(bei Multimengensemantik) kennengelernt. Wir haben auch die verschiedenen Joins und Outerjoins betrachtet und den Einsatz von Nullwerten kennengelernt. Darüber hinaus haben wir gesehen wie Gruppierung und Aggregation in SQL in Kombination mit Schlüsselwörtern wie GROUP BY, HAVING und MIN, MAX, COUNT umgesetzt wird.
# <br>
# <br>
# Im Weiteren haben wir SQL als DML betrachtet ,um Datenbankveränderungen mit INSERT, UPDATE, DELETE zu schaffen. In Bezug auf SQL als DDL haben wir Schemata und Datentypen kennengelernt, die zur Erstellung und Veränderung von Relationen mit CREATE TABLE und ALTER TABLE nötig sind. Anschließend haben wir die Datenstruktur Index betrachtet, die die Suche nach Tupel erleichtert. Zuletzt haben wir uns mit Sichten und materalisierten Sichten, sowie Anfragen und Updates darauf beschäftigt.

# ## SQL-Trainer
# 
# - Mithilfe des SQL-Trainers können sie ihr erlangtes Wissen aus diesem Kapitel vertiefen und praktisch anwenden:
# - Die hier verwendete Version des SQL-Trainers von EILD.nrw wird nur in das JupyterBook eingebunden und nicht selbst gehostet. Der SQL-Trainer wird durch GitHub-Pages gehostet. 

# In[1]:


from IPython.display import IFrame

url = "https://lejuliennn.github.io/sql-trainer/"
IFrame(src=url, width='100%', height=800)


# ## Multiple Choice
# 
# - Die hier verwendete Version des Multiple-Choice-Trainers von EILD.nrw wird nur in das JupyterBook eingebunden und nicht selbst gehostet. Der Multiple-Choice-Trainer wird durch GitHub-Pages gehostet. 
# - Alle Fragen und Kategorien befinden sich zurzeit in Überarbeitung und sind nicht final. 

# In[2]:


from IPython.display import IFrame

url = "https://lejuliennn.github.io/mct-trainer/#/quiz/categories/sql"
IFrame(src=url, width='100%', height=800)


# In[ ]:




