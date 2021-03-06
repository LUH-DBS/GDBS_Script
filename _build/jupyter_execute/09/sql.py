#!/usr/bin/env python
# coding: utf-8

# # SQL

# In[1]:


import sqlite3
get_ipython().run_line_magic('load_ext', 'sql')
get_ipython().run_line_magic('sql', 'sqlite:///filme/filme.db')
get_ipython().run_line_magic('sql', 'sqlite:///salesDB/salesDB')


# In[2]:


__SQL__ = " SELECT * FROM Film"
conn = sqlite3.connect("filme/filme.db")
cur = conn.cursor()
cur.execute(__SQL__)
rows = cur.fetchall()

for row in rows:
    for col in row:
        print(col,end=' ')
    print()


# ## Einführung
# ### SQL-Historie
# ■ SEQUEL (1974, IBM Research Labs San Jose)
# <br><br>
# ■ SEQUEL2 (1976, IBM Research Labs San Jose)
# <br>
# □ System R
# <br><br>
# ■ SQL (1982, IBM)
# <br><br>
# ![title](historie1.jpg)
# <br>
# ![title](historie2.jpg)
# <br>
# ![title](historie3.jpg)
# ### SQL – Standardisierung
# ■ SQL1 von ANSI als Standard verabschiedet (1986)
#  <br>
#  <br>
# ■ SQL1 von der (ISO) als Standard verabschiedet (1987)
#  <br>
# □ 1989 nochmals überarbeitet.
#  <br> <br>
# ■ SQL2 oder SQL-92 von der ISO verabschiedet (1992)
#  <br> <br>
# ■ SQL3 oder SQL:1999 verabschiedet
#  <br> 
# □ Trigger, rekursive Anfragen
#  <br>
# □ Objektrelationale Erweiterungen
#  <br> <br>
# ■ SQL:2003 von der ISO verabschiedet
#  <br>
# □ XML-Support durch SQL/XML
#  <br> <br>
# ■ SQL/XML:2006
#  <br>
# □ XQuery eingebunden
#  <br> <br>
# ■ SQL:2008
#  <br>
# □ Updates auf Sichten, logisches Löschen (TRUNCATE), …
#  <br> <br>
# ■ SQL:2011
#  <br>
# □ Adds temporal data (PERIOD FOR)
#  <br> <br>
# ■ SQL:2016
#  <br>
# □ Adds row pattern matching, polymorphic table functions, JSON.
# <br><br>
# Trotz Standardisierung: Inkompatibilitäten zwischen Systemen der einzelnen Hersteller
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
# ### Motivation für SQL
# ■ Meist-verbreitete Datenbankanfragesprache
# <br><br>
# ■ Ad-hoc und einfach
# <br><br>
# ■ Deklarativ
# <br>
# □ Nicht prozedural / imperativ
# <br>
# □ Optimierbar
# <br><br>
# ■ Very-High-Level Language
# <br><br>
# ■ Anfragen an relationale Algebra angelehnt
# <br>
# □ Hinzu kommt DDL: Data definition language
# <br>
# □ Hinzu kommt DML: Data manipulation language
# <br><br>
# ■ Achtung: Syntax kann sich von System zu System leicht unterscheiden.
# <br><br>
# ■ Achtung: Funktionalität kann sich von System zu System leicht unterscheiden.

# ## Einfach Anfragen

# ### Beispielschema
# ![title](beispielschema.jpg)
# ### SELECT … FROM … WHERE …

# In[3]:


#SELECT * 
#FROM Film 
#WHERE StudioName = "Disney" AND Jahr= 1990;

__SQL__ = "SELECT * FROM Film WHERE StudioName = 'Disney' AND Jahr= 1990"
conn = sqlite3.connect("filme/filme.db")
cur = conn.cursor()
cur.execute(__SQL__)
rows = cur.fetchall()

for row in rows:
    for col in row:
        print(col,end=' ')
    print()


# ■ Lesereihenfolge (und Schreibreihenfolge):
# <br>
# 1. FROM: Relation(en) aus denen die Daten stammen
# <br>
# 2. WHERE: Bedingung(en) an die Daten
# <br>
# 3. SELECT: Schema der Ergebnisrelation
# <br>
# – *: Alle Attribute der Inputrelationen
# <br><br>
# ■ Ausführung
# <br>
# □ Für jedes Tupel aus „Film“ prüfe die Bedingungen und gebe gültige Tupel aus
# ### Groß- und Kleinschreibung
# ■ In SQL wird Groß- und Kleinschreibung nicht beachtet
# <br>
# 
# ```
# From = FROM = from = FrOm
# ```
# 
# <br><br>
# ■ Auch bei Attribut- und Relationennamen
# <br>
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
# ■ Natürlich nicht bei Konstanten:
# <br>
# 
# ```
# ‘FROM‘ ≠ ‘from‘ ≠ from = FROM
# ```
# <br><br>
# ■ Konvention zur Lesbarkeit
# <br>
# □ Schlüsselworte großschreiben
# <br>
# □ Schemaelemente kleinschreiben
# ### Projektion in SQL (SELECT, $\pi$)
# ■ Spezifikation in der SELECT Klausel

# In[4]:


#SELECT * 
#FROM Film

__SQL__ = " SELECT * FROM Film"
conn = sqlite3.connect("filme/filme.db")
cur = conn.cursor()
cur.execute(__SQL__)
rows = cur.fetchall()

for row in rows:
    for col in row:
        print(col,end=' ')
    print()


# – Alle Attribute

# In[5]:


#SELECT Titel, Jahr, inFarbe 
#FROM Film

__SQL__ = "SELECT Titel, Jahr, inFarbe FROM Film"
conn = sqlite3.connect("filme/filme.db")
cur = conn.cursor()
cur.execute(__SQL__)
rows = cur.fetchall()

for row in rows:
    for col in row:
        print(col,end=' ')
    print()


# – Projektion auf die drei Attribute
# <br><br>
# ■ Erweiterte Projektion
# <br>
# □ Umbenennung:

# In[6]:


#SELECT Titel AS Name, Jahr AS Zeit 
#FROM Film

__SQL__ = "SELECT Titel AS Name, Jahr AS Zeit FROM Film"
conn = sqlite3.connect("filme/filme.db")
cur = conn.cursor()
cur.execute(__SQL__)
rows = cur.fetchall()

for row in rows:
    for col in row:
        print(col,end=' ')
    print()


# □ Arithmetischer Ausdruck:

# In[7]:


#SELECT Titel, Laenge * 0.016667 AS Stunden 
#FROM Film

__SQL__ = "SELECT Titel, Laenge * 0.016667 AS Stunden FROM Film"
conn = sqlite3.connect("filme/filme.db")
cur = conn.cursor()
cur.execute(__SQL__)
rows = cur.fetchall()

for row in rows:
    for col in row:
        print(col,end=' ')
    print()


# □ Konstanten:

# In[8]:


#SELECT Titel, Laenge * 0.016667 AS Stunden, ‘std.‘ AS inStunden FROM Film

__SQL__ = "SELECT Titel, Laenge * 0.016667 AS Stunden, ‘std.‘ AS inStunden FROM Film"
conn = sqlite3.connect("filme/filme.db")
cur = conn.cursor()
cur.execute(__SQL__)
rows = cur.fetchall()

for row in rows:
    for col in row:
        print(col,end=' ')
    print()


# ### Selektion in SQL (WHERE, $\sigma$)
# ■ Spezifikation in der WHERE Klausel
# <br>
# □ Bedingungen wie in einer Programmiersprache
# <br>
# □ Sechs Vergleichsoperatoren
# <br>
# – =, <>, <, >, <=, >=
# <br>
# – <>, <=, >= entspricht ≠, $\geq, \leq$
# <br>
# □ Operanden
# <br>
# – Konstanten und Attributnamen
# <br>
# – Auch Attribute, die nicht in der SELECT Klausel genannt werden.
# <br>
# □ Arithmetische Ausdrücke für numerische Attribute
# <br>
# – Z.B.: 
# ```
# (Jahr - 1930) * (Jahr - 1930) <= 100
# ```
# □ Konkatenation für Strings
# ```
# ‘Star‘ || ‘Wars‘ 
# ```
# entspricht 
# ```
# ‘StarWars‘
# ```
# – Vorname || \` \` || Nachname = \`Luke Skywalker\`
# 
# ### Selektion in SQL
# 
# ■ Ergebnis ist stets Boole‘scher Wert
# <br>
# □ TRUE oder FALSE
# <br>
# □ Können mit AND, OR und NOT verknüpft werden.
# <br>
# – Klammerungen sind erlaubt.
# <br>
# □ Nur wenn insgesamt auf TRUE evaluiert wird, erscheint das entsprechende Tupel im Ergebnis.
# <br>
# <br>
# ■ Beispiele

# In[18]:


#SELECT Titel 
#FROM Film 
#WHERE Jahr > 1970 AND NOT inFarbe;

__SQL__ = "SELECT Titel FROM Film WHERE Jahr > 1970 AND NOT inFarbe"
conn = sqlite3.connect("filme/filme.db")
cur = conn.cursor()
cur.execute(__SQL__)
rows = cur.fetchall()

for row in rows:
    for col in row:
        print(col,end=' ')
    print()


# In[4]:


#SELECT Titel 
#FROM Film 
#WHERE (Jahr > 1970 OR Laenge < 90) AND StudioName = "MGM";

__SQL__ = "SELECT Titel FROM Film WHERE (Jahr > 1970 OR Laenge < 90) AND StudioName = 'MGM';"
conn = sqlite3.connect("filme/filme.db")
cur = conn.cursor()
cur.execute(__SQL__)
rows = cur.fetchall()

for row in rows:
    for col in row:
        print(col,end=' ')
    print()


# ### Stringvergleiche
# ■ Datentypen
# <br>
# □ Array fester Länge, Buchstabenliste variabler Länge, Konstanten
# <br>
# □ SQL erlaubt viele Vergleiche über Datentypen hinweg
# <br><br>
# ■ foo _ _ _ _ _ = foo = ‘foo‘
# <br><br>
# ■ Vergleiche mit =, <, >, <=, >=, <>
# <br>
# □ Lexikographischer Vergleich
# <br>
# □ ‘fodder‘ < ‘foo‘; ‘bar‘ < ‘bargain‘;
# <br>
# □ Sortierreihenfolge upper-case/lower-case usw. je nach DBMS
# <br>
# □ Achtung: Auch nicht immer identisch zur Reihenfolge in Programmiersprachen
# 
# ### String-Mustervergleiche mit LIKE
# ■ string LIKE pattern
# <br>
# □ bzw. string NOT LIKE pattern
# <br><br>
# ■ Pattern hat spezielle Zeichen
# <br>
# □ ‘%‘: Beliebige Sequenz von 0 oder mehr Zeichen
# <br>
# □ ‘_‘: Ein beliebiges Zeichen
# <br><br>

# In[21]:


#SELECT Titel 
#FROM Film WHERE Titel LIKE "Star ____";

__SQL__ = "SELECT Titel FROM Film WHERE Titel LIKE 'Star ____'"
conn = sqlite3.connect("filme/filme.db")
cur = conn.cursor()
cur.execute(__SQL__)
rows = cur.fetchall()

for row in rows:
    for col in row:
        print(col,end=' ')
    print()


# □ Star Wars und Star Trek

# In[22]:


#SELECT Titel 
#FROM Film 
#WHERE Titel LIKE "%War%";

__SQL__ = "SELECT Titel FROM Film WHERE Titel LIKE '%War%'"
conn = sqlite3.connect("filme/filme.db")
cur = conn.cursor()
cur.execute(__SQL__)
rows = cur.fetchall()

for row in rows:
    for col in row:
        print(col,end=' ')
    print()


# ### Datum und Uhrzeit
# ■ Spezielle Datentypen und Repräsentationen
# <br>
# □ Datumskonstante:
# <br>
# – DATE ‘YYYY-MM-DD‘
# <br>
# – DATE ‘1948-05-14‘
# <br><br>
# □ Zeitkonstante
# <br>
# – TIME ‘HH:MM:SS.S‘
# <br>
# – TIME ‘15:00:02.5‘
# <br><br>
# □ Zeitstempel
# <br>
# – TIMESTAMP ‘1948-05-14 15:00:02.5‘
# <br><br>
# □ Zeitvergleiche
# <br>
# – TIME ‘15:00:02.5‘ < TIME ‘15:02:02.5‘ ergibt TRUE
# <br>
# – Selektion: ERSCHEINUNGSTAG >= DATE ‘1949-11-12‘
# ### Nullwerte
# Darstellung: NULL bzw. ⊥
# <br>
# <br>
# Mögliche Interpretationen
# <br>
# Unbekannter Wert
# <br>
# -> Geburtstag einer/s Schauspieler*in
# <br>
# Wert unzulässig
# <br>
# -> Ehegatte eines unverheirateten Schauspielers
# <br>
# Wert unterdrückt
# <br>
# -> Geheime Telefonnummer
# <br>
# <br>
# Regeln für Umgang mit Nullwerten
# <br>
# Arithmetische Operationen mit NULL ergeben NULL
# <br>
# Vergleich mit NULL ergibt Wahrheitswert UNKNOWN
# <br>
# NULL ist keine Konstante, sondern erscheint nur als Attributwert
# <br><br>
# Beispiel (sei der Wert von x NULL):
# <br>
# x+3 ergibt NULL.
# <br>
# NULL+3 ist kein zulässiger Ausdruck.
# <br>
# x = 3 ergibt UNKNOWN.
# <br><br>
# Prüfen von Nullwerten in WHERE Klausel
# <br>
# Geburtstag IS NULL bzw. Geburtstag IS NOT NULL
# ### Wahrheitswerte
# 
# |AND|true|unknown|false|
# |---|---|---|---|
# |**true**|true|unknown|false|
# |**unknown**|unknown|unknown|false|
# |**false**|false|false|false|
# 
# 
# ■ Rechenregeln
# <br>
# □ TRUE = 1
# <br>
# FALSE = 0
# <br>
# UNKNOWN = ½
# <br>
# □ AND: Minimum der beiden Werte
# <br>
# □ OR: Maximum der beiden Werte
# <br>
# □ NOT: 1 – Wert
# <br><br>
# □ Beispiel
# <br>
# – TRUE AND (FALSE OR NOT(UNKNOWN))
# <br>
# = MIN(1, MAX(0, (1 - ½ )))
# <br>
# = MIN(1, MAX(0, ½ )
# <br>
# = MIN(1, ½ ) = ½.
# 
# 
# |Titel|Jahr|Länge|inFarbe|Studio|ProduzentinID|
# |---|---|---|---|---|---|
# |Total|Recall|1990|NULL|True|Fox|12345|
# 
#  Überraschendes Verhalten

# In[23]:


#SELECT * 
#FROM Film 
#WHERE Laenge <= 90 
#OR Laenge > 90; --Laenge <= 90 == UNKNOWN und Länge > 90

__SQL__ = "SELECT * FROM Film WHERE Laenge <= 90 OR Laenge > 90; --Laenge <= 90 == UNKNOWN und Länge > 90"
conn = sqlite3.connect("filme/filme.db")
cur = conn.cursor()
cur.execute(__SQL__)
rows = cur.fetchall()

for row in rows:
    for col in row:
        print(col,end=' ')
    print()


# □ Tupel erscheint nicht im Ergebnis.
# <br><br>
# ■ Ausführungspriorität: NOT vor AND vor OR
# 
# ### Sortierung
# 
# ■ ORDER BY Klausel ans Ende der Anfrage
# <br>
# □ ORDER BY \<Attributliste\> DESC/ASC
# <br>
# □ ASC (aufsteigend) ist default
# <br>

# In[25]:


#SELECT * 
#FROM Film 
#WHERE StudioName = "Disney" 
#AND Jahr = 1990 ORDER BY Laenge, Titel;

__SQL__ = "SELECT * FROM Film WHERE StudioName = 'Disney' AND Jahr = 1990 ORDER BY Laenge, Titel;"
conn = sqlite3.connect("filme/filme.db")
cur = conn.cursor()
cur.execute(__SQL__)
rows = cur.fetchall()

for row in rows:
    for col in row:
        print(col,end=' ')
    print()


# In[27]:


#SELECT * 
#FROM Film 
#WHERE StudioName = "Disney" 
#AND Jahr = 1990 ORDER BY Laenge ASC, Titel DESC;

__SQL__ = "SELECT * FROM Film WHERE StudioName = 'Disney' AND Jahr = 1990 ORDER BY Laenge ASC, Titel DESC;"
conn = sqlite3.connect("filme/filme.db")
cur = conn.cursor()
cur.execute(__SQL__)
rows = cur.fetchall()

for row in rows:
    for col in row:
        print(col,end=' ')
    print()


# ## Anfragen über mehrere Relationen
# 
# ### Motivation
# ■ Hauptstärke der Relationalen Algebra ist die Kombination von Relationen
# <br><br>
# ■ Erst mit mehreren Relationen sind viele interessante Anfragen möglich.
# <br><br>
# ■ Nennung der beteiligten Relationen in der FROM Klausel
# 
# ### Kreuzprodukt und Join
# ■ Film(Titel, Jahr, Länge, inFarbe, StudioName, ProduzentinID)
# <br>
# ■ Manager*in(Name, Adresse, ManagerinID, Gehalt)

# In[29]:


#SELECT Name 
#FROM Film, ManagerIn 
#WHERE Titel = "Star Wars" 
#AND ProduzentinID = ManagerinID; 

__SQL__ = "SELECT Name FROM Film, ManagerIn WHERE Titel = 'Star Wars' AND ProduzentinID = ManagerinID"
conn = sqlite3.connect("filme/filme.db")
cur = conn.cursor()
cur.execute(__SQL__)
rows = cur.fetchall()

for row in rows:
    for col in row:
        print(col,end=' ')
    print()


# In[ ]:


#SELECT Name 
#FROM Film, ManagerIn --Kreuzprodukt
#WHERE Titel = ‘Star Wars‘--Selektionsbedingung 
#AND ProduzentinID = ManagerinID; --Joinbedingung


# ■ Semantik
# <br>
# □ Betrachte jedes Tupelpaar der Relationen Film und Manager.
# □ Wende Bedingung der WHERE Klausel auf jedes Tupelpaar an
# <br>
# □ Falls Bedingung erfüllt, produziere ein Ergebnistupel.
# <br><br>
# ■ Kreuzprodukt gefolgt von Selektion: Join
# <br><br>
# ■ Reihenfolge der WHERE Bedingungen egal

# In[30]:


#SELECT Name 
#FROM Film, ManagerIn 
#WHERE Titel = "Star Wars" 
#AND ProduzentinID = ManagerinID; 

__SQL__ = "SELECT Name FROM Film, ManagerIn WHERE Titel = 'Star Wars' AND ProduzentinID = ManagerinID"
conn = sqlite3.connect("filme/filme.db")
cur = conn.cursor()
cur.execute(__SQL__)
rows = cur.fetchall()

for row in rows:
    for col in row:
        print(col,end=' ')
    print()


# ### Uneindeutige Attributnamen
# ■ SchauspielerIn(Name, Adresse, Geschlecht, Geburtstag)
# <br><br>
# ■ ManagerIn(Name, Adresse, ManagerinID, Gehalt)
# <br><br>
# ■ Bei gleichen Attributnamen aus mehreren beteiligten Relationen:
# <br>
# □ Relationenname als Präfix:

# In[33]:


#SELECT SchauspielerIn.Name, ManagerIn.Name 
#FROM SchauspielerIn, ManagerIn 
#WHERE SchauspielerIn.Adresse = ManagerIn.Adresse;


__SQL__ = "SELECT SchauspielerIn.Name, ManagerIn.Name FROM SchauspielerIn, ManagerIn WHERE SchauspielerIn.Adresse = ManagerIn.Adresse;"
conn = sqlite3.connect("filme/filme.db")
cur = conn.cursor()
cur.execute(__SQL__)
rows = cur.fetchall()

for row in rows:
    for col in row:
        print(col,end=' ')
    print()


# □ Präfix ist auch erlaubt wenn Attributname eindeutig ist.
# <br>
# – Erleichtert das Lesen von SQL Anfragen
# 
# ### Tupelvariablen
# ■ Zur eindeutigen Kennzeichnung von Tupeln beteiligter Relationen
# <br>
# □ „Alias“ einer Relation
# <br>
# □ Insbesondere: Bei der mehrfachen Verwendung einer Relation in einer Anfrage
# <br><br>
# ■ Gesucht: Schauspieler, die zusammen leben

# In[35]:


#SELECT Star1.Name, Star2.Name 
#FROM SchauspielerIn Star1, SchauspielerIn Star2 
#WHERE Star1.Adresse = Star2.Adresse

__SQL__ = "SELECT Star1.Name, Star2.Name FROM SchauspielerIn Star1, SchauspielerIn Star2 WHERE Star1.Adresse = Star2.Adresse"
conn = sqlite3.connect("filme/filme.db")
cur = conn.cursor()
cur.execute(__SQL__)
rows = cur.fetchall()

for row in rows:
    for col in row:
        print(col,end=' ')
    print()


# □ Äquivalent zu Schauspieler AS Star2
# <br><br>
# ■ Auch sinnvoll als abkürzenden Schreibweise

# In[ ]:


#SELECT S.Name, M.Name
#FROM SchauspielerIn S, ManagerIn M
#WHERE S.Adresse = M.Adresse;


__SQL__ = "SELECT S.Name, M.Name FROM SchauspielerIn S, ManagerIn M WHERE S.Adresse = M.Adresse;"
conn = sqlite3.connect("filme/filme.db")
cur = conn.cursor()
cur.execute(__SQL__)
rows = cur.fetchall()

for row in rows:
    for col in row:
        print(col,end=' ')
    print()


# ■ Ohne explizites Angeben einer Tupelvariablen wird der Relationenname als Tupelvariable verwendet.
#  
# ### Tupelvariablen-Selfjoin
# 
# 
# |Name|Adresse|Geschlecht|Geburt|
# |---|---|---|---|
# |Carrie Fisher|123 Maple St., Hollywood|F|9/9/99|
# |Mark Hamill|456 Oak Rd., Brentwood|M|8/8/88|
# |Brad Pitt|123 Maple St., Hollywood|M|7/7/77|

# In[36]:


#SELECT Star1.Name, Star2.Name
#FROM SchauspielerIn Star1, SchauspielerIn Star2
#WHERE Star1.Adresse = Star2.Adresse;

__SQL__ = "SELECT Star1.Name, Star2.Name FROM SchauspielerIn Star1, SchauspielerIn Star2 WHERE Star1.Adresse = Star2.Adresse;"
conn = sqlite3.connect("filme/filme.db")
cur = conn.cursor()
cur.execute(__SQL__)
rows = cur.fetchall()

for row in rows:
    for col in row:
        print(col,end=' ')
    print()


# |Star1.Name|Star2.Name|
# |---|---|
# |Carrie Fisher|Carrie Fisher|
# |Carrie Fisher|Brad Pitt|
# |Brad Pitt|Carrie Fisher|
# |Brad Pitt|Brad Pitt|
# |Mark Hamill|Mark Hamill|

# In[37]:


#SELECT Star1.Name, Star2.Name
#FROM SchauspielerIn Star1, SchauspielerIn Star2
#WHERE Star1.Adresse = Star2.Adresse
#AND Star1.Name <> Star2.Name;

__SQL__ = "SELECT Star1.Name, Star2.Name FROM SchauspielerIn Star1, SchauspielerIn Star2 WHERE Star1.Adresse = Star2.Adresse AND Star1.Name <> Star2.Name;"
conn = sqlite3.connect("filme/filme.db")
cur = conn.cursor()
cur.execute(__SQL__)
rows = cur.fetchall()

for row in rows:
    for col in row:
        print(col,end=' ')
    print()


# |Star1.Name|Star2.Name|
# |---|---|
# |Carrie Fisher|Brad Pitt|
# |Brad Pitt|Carrie Fisher|

# |Star1.Name|Star2.Name|
# |---|---|
# |Brad Pitt|Carrie Fisher|
# 
# ### Interpretation von Anfragen
# 
# ■ Drei Interpretationsvarianten für Anfragen mit mehreren Relationen
# <br>
# □ Nested Loops (geschachtelte Schleifen)
# <br>
# – Bei mehreren Tupelvariablen: Eine geschachtelte Schleife für jede Variable
# <br>
# □ Parallele Zuordnung
# <br>
# – Alle Kombinationen werden parallel bezüglich der Bedingungen geprüft.
# <br>
# □ Relationale Algebra
# <br>
# – Bilde Kreuzprodukt
# <br>
# – Wende Selektionsbedingungen auf jedes Resultat-Tupel an
# <br><br>
# 
# ■ Gegeben drei Relationen: R(A), S(A) und T(A)
# <br><br>
# ■ Gesucht: R $\cap$ (S $\cup$ T) (= (R $\cap$ S) $\cup$ (R $\cap$ T) )

# In[ ]:


get_ipython().run_line_magic('sql', '')
SELECT R.A
FROM R, S, T
WHERE R.A = S.A
OR R.A = T.A;


# In[ ]:


get_ipython().run_line_magic('sql', '')
SELECT *
FROM
(
    (SELECT A FROM R)
     INTERSECT
    (SELECT * FROM
     (SELECT A FROM S)
      UNION
    (SELECT A FROM T)
    )
)


# ■ Problemfall: T ist leer, hat also kein Tupel
# <br><br>
# ■ Vermeintliches Resultat: R $\cap$ S
# <br><br>
# ■ Tatsächliches Resultat: leere Menge
# <br>
# □ Ausführung als drei geschachtelte Schleifen
# 
# ### Joins
# ![title](joins.jpg)
# 
#  Man kann Joins auch auf andere Weise ausdrücken.
#  <br>
# □ Geschmacksfrage
#  <br>
# □ Film CROSS JOIN spielt_in
#  <br>
# – Kreuzprodukt
#  <br>
# – Doppelte Attributnamen werden mit Präfix der Relation aufgelöst

# In[38]:


#Film JOIN spielt_in ON Titel = FilmTitel AND Jahr = FilmJahr

__SQL__ = "Film JOIN spielt_in ON Titel = FilmTitel AND Jahr = FilmJahr"
conn = sqlite3.connect("filme/filme.db")
cur = conn.cursor()
cur.execute(__SQL__)
rows = cur.fetchall()

for row in rows:
    for col in row:
        print(col,end=' ')
    print()


# – Theta-Join

# In[40]:


#SELECT Titel, Jahr, Laenge, inFarbe, StudioName, ProduzentinID, Name 
#FROM Film JOIN spielt_in ON Titel = FilmTitel 
#AND Jahr = FilmJahr;

__SQL__ = "SELECT Titel, Jahr, Laenge, inFarbe, StudioName, ProduzentinID, Name FROM Film JOIN spielt_in ON Titel = FilmTitel AND Jahr = FilmJahr;"
conn = sqlite3.connect("filme/filme.db")
cur = conn.cursor()
cur.execute(__SQL__)
rows = cur.fetchall()

for row in rows:
    for col in row:
        print(col,end=' ')
    print()


# – Eliminiert redundante Attribute FilmTitel und FilmJahr

# In[43]:


#SELECT Titel, Jahr 
#FROM Film JOIN spielt_in ON Titel = FilmTitel 
#AND Jahr = FilmJahr JOIN SchauspielerIn ON spielt_in.Name = SchauspielerIn.Name 
#WHERE Geschlecht = "f";

__SQL__ = "SELECT Titel, Jahr FROM Film JOIN spielt_in ON Titel = FilmTitel AND Jahr = FilmJahr JOIN SchauspielerIn ON spielt_in.Name = SchauspielerIn.Name WHERE Geschlecht = 'f'"
conn = sqlite3.connect("filme/filme.db")
cur = conn.cursor()
cur.execute(__SQL__)
rows = cur.fetchall()

for row in rows:
    for col in row:
        print(col,end=' ')
    print()


# □ Schauspieler NATURAL JOIN Manager
# <br>
# – Natural Join; Eliminiert redundante Attribute
# 
# ### The TPC-H Schema
# ![title](tpc-h_schema.jpg)
#  
# #### TPC Query 2 - Minimum Cost Supplier

# In[28]:


get_ipython().run_line_magic('sql', '')
SELECT s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone,
s_comment
FROM part, supplier, partsupp, nation, region
WHERE p_partkey = ps_partkey AND s_suppkey = ps_suppkey
AND p_size = [SIZE] AND p_type like '%[TYPE]'
AND s_nationkey = n_nationkey AND n_regionkey = r_regionkey
AND r_name = '[REGION]'
AND ps_supplycost =
(SELECT min(ps_supplycost)
FROM partsupp, supplier, nation, region
WHERE p_partkey = ps_partkey AND s_suppkey = ps_suppkey
AND s_nationkey = n_nationkey AND n_regionkey = r_regionkey
AND r_name = '[REGION]' )
ORDER BY s_acctbal desc, n_name, s_name, p_partkey;


# In[ ]:


SELECT s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment FROM part, supplier, partsupp, nation, region WHERE p_partkey = ps_partkey AND s_suppkey = ps_suppkey AND p_size = [SIZE] AND p_type like '%[TYPE]' AND s_nationkey = n_nationkey AND n_regionkey = r_regionkey AND r_name = '[REGION]' AND ps_supplycost = (SELECT min(ps_supplycost) FROM partsupp, supplier, nation, region WHERE p_partkey = ps_partkey AND s_suppkey = ps_suppkey AND s_nationkey = n_nationkey AND n_regionkey = r_regionkey AND r_name = '[REGION]' ) ORDER BY s_acctbal desc, n_name, s_name, p_partkey;


# In[8]:


__SQL__ = "SELECT s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment FROM part, supplier, partsupp, nation, region WHERE p_partkey = ps_partkey AND s_suppkey = ps_suppkey AND p_size = [SIZE] AND p_type like '%[TYPE]' AND s_nationkey = n_nationkey AND n_regionkey = r_regionkey AND r_name = '[REGION]' AND ps_supplycost = (SELECT min(ps_supplycost) FROM partsupp, supplier, nation, region WHERE p_partkey = ps_partkey AND s_suppkey = ps_suppkey AND s_nationkey = n_nationkey AND n_regionkey = r_regionkey AND r_name = '[REGION]' ) ORDER BY s_acctbal desc, n_name, s_name, p_partkey;"
conn = sqlite3.connect("salesDB/salesDB")
cur = conn.cursor()
cur.execute(__SQL__)
rows = cur.fetchall()

for row in rows:
    for col in row:
        print(col,end=' ')
    print()


# SIZE is randomly selected within [1. 50];
# <br>
# TYPE is randomly selected within the list Syllable 3 defined for Types
# <br>
# REGION is randomly selected within the list of values defined for R_NAME
# 
# #### The TPC-H Universal Table

# In[ ]:


get_ipython().run_line_magic('sql', '')
SELECT l_linenumber, l_quantity, l_extendedprice, l_discount, l_tax, l_returnflag, l_linestatus, l_shipdate, l_commitdate, l_receiptdate, l_shipinstruct, l_shipmode, l_comment, o_orderkey, o_orderstatus, o_totalprice, o_orderdate, o_orderpriority, o_clerk, o_shippriority, o_comment, ps_availqty, ps_supplycost, ps_comment, p_partkey, p_name, p_mfgr, p_brand, p_type, p_size, p_container, p_retailprice, p_comment, c_custkey, c_name, c_address, c_phone, c_acctbal, c_mktsegment, c_comment, s_suppkey, s_name, s_address, s_phone, s_acctbal, s_comment, n_nationkey, n_name, n_comment, r_regionkey, r_name, r_comment

FROM lineitem, orders, partsupp, part, customer, supplier, nation, region

WHERE p_partkey = ps_partkey

AND s_suppkey = ps_suppkey

AND n_nationkey = s_nationkey

AND r_regionkey = n_regionkey

AND c_custkey = o_custkey

AND ps_partkey = l_partkey

AND ps_suppkey = l_suppkey

AND o_orderkey = l_orderkey


# ### Outer Joins
# ■ SchauspielerIn(Name, Adresse, Geschlecht, Geburtstag)
# <br><br>
# ■ ManagerIn(Name, Adresse, ManagerinID, Gehalt)
# <br><br>
# ■ Schauspieler*innen, die zugleich Manager*in sind

# In[44]:


#SELECT Name, Adresse, Geburtstag, Gehalt 
#FROM SchauspielerIn 
#NATURAL INNER JOIN ManagerIn

__SQL__ = "SELECT Name, Adresse, Geburtstag, Gehalt FROM SchauspielerIn NATURAL INNER JOIN ManagerIn"
conn = sqlite3.connect("filme/filme.db")
cur = conn.cursor()
cur.execute(__SQL__)
rows = cur.fetchall()

for row in rows:
    for col in row:
        print(col,end=' ')
    print()


# ■ SchauspielerIn und gegebenenfalls ihre ManagerIninfo

# In[ ]:


#…FROM SchauspielerIn NATURAL LEFT OUTER JOIN ManagerIn


# □ Gehalt bleibt gegebenenfalls NULL
# 
# ■ ManagerIn und gegebenenfalls ihre Schauspielerinfo

# In[ ]:


#…FROM SchauspielerIn NATURAL RIGHT OUTER JOIN ManagerIn


# □ Geburtstag bleibt gegebenenfalls NULL
# 
# ■ Alle Schauspieler*innen und Manager*innen

# In[ ]:


#…FROM SchauspielerIn NATURAL FULL OUTER JOIN ManagerIn


# □ Geburtstag oder Gehalt bleiben gegebenenfalls leer
# 
# □ Unterschied zu UNION: Nur eine Zeile pro Person
# 
# ![](outerjoins.jpg)
# 
# |Geburtstag|Name|Adresse|Gehalt|
# |---|---|---|---|
# |1.2.1960|Mark Hamill|LA|NULL|
# |27.5.1969|Carrie Fischer|New York|NULL|
# |11.12.1940|Alec Guinness|London|NULL|
# |22.3.1981|Ben Affleck|Boston|5Mio|
# |23.8.1973|Quentin Tarantino|Berlin|10Mio|
# |NULL|George Lukas |San Jose|100Mio|
# |NULL|Steven Spielberg|LA|500Mio|
# 
# ->geschweifte Klammern fehlen in md Tabelle
# 
# ### Kreuzprodukt
# ■ Alle Paare aus Tupeln der beteiligten Relationen

# In[46]:


#SELECT * 
#FROM SchauspielerIn CROSS JOIN Film

__SQL__ = "SELECT * FROM SchauspielerIn CROSS JOIN Film"
conn = sqlite3.connect("filme/filme.db")
cur = conn.cursor()
cur.execute(__SQL__)
rows = cur.fetchall()

for row in rows:
    for col in row:
        print(col,end=' ')
    print()


# In[48]:


#SELECT * 
#FROM SchauspielerIn, Film

__SQL__ = "SELECT * FROM SchauspielerIn, Film"
conn = sqlite3.connect("filme/filme.db")
cur = conn.cursor()
cur.execute(__SQL__)
rows = cur.fetchall()

for row in rows:
    for col in row:
        print(col,end=' ')
    print()


# ■ Selten verwendet
# <br>
# ■ Grundbaustein für Joins
# 
# ### Mengenoperationen in SQL
#  Vereinigung: UNION
# <br><br>
# ■ Schnittmenge: INTERSECT
# <br><br>
# ■ Differenz: EXCEPT / MINUS
# <br><br>
# ■ Mengenoperationen nur zwischen geklammerten Anfrageergebnissen
# <br><br>
# ■ Mengenoperationen haben implizit eine Mengensemantik
# <br>
# □ Wandeln Input-Relationen in Mengen um
# <br>
# □ Wandeln Output in Menge um
# <br><br>
# ■ Input-Relationen müssen gleiche Schemata haben
# <br>
# □ Gleiche Attributnamen
# <br>
# □ Gleiche Datentypen
# <br>
# ■ SchauspielerIn(Name, Adresse, Geschlecht, Geburtstag)
# <br><br>
# ■ ManagerIn(Name, Adresse, ManagerinID, Gehalt)
# 
# #### Schnittmenge: INTERSECT
# ■ Entspricht dem logischen „und“

# In[49]:


#(SELECT Name, Adresse FROM SchauspielerIn) INTERSECT (SELECT Name, Adresse FROM ManagerIn);

__SQL__ = "(SELECT Name, Adresse FROM SchauspielerIn) INTERSECT (SELECT Name, Adresse FROM ManagerIn)"
conn = sqlite3.connect("filme/filme.db")
cur = conn.cursor()
cur.execute(__SQL__)
rows = cur.fetchall()

for row in rows:
    for col in row:
        print(col,end=' ')
    print()


# In[51]:


#%sql (SELECT Name, Adresse FROM SchauspielerIn WHERE Geschlecht = "f") INTERSECT (SELECT Name, Adresse FROM ManagerIn WHERE Gehalt > 1000000)

__SQL__ = "(SELECT Name, Adresse FROM SchauspielerIn WHERE Geschlecht = "f") INTERSECT (SELECT Name, Adresse FROM ManagerIn WHERE Gehalt > 1000000)"
conn = sqlite3.connect("filme/filme.db")
cur = conn.cursor()
cur.execute(__SQL__)
rows = cur.fetchall()

for row in rows:
    for col in row:
        print(col,end=' ')
    print()


# ■ Multimengen-Semantik: INTERSECT ALL
# 
# #### Vereinigung: UNION
# ■ Entspricht dem logischen „oder“

# In[52]:


#(SELECT Name, Adresse FROM SchauspielerIn) UNION (SELECT Name, Adresse FROM ManagerIn);

__SQL__ = "(SELECT Name, Adresse FROM SchauspielerIn) UNION (SELECT Name, Adresse FROM ManagerIn)"
conn = sqlite3.connect("filme/filme.db")
cur = conn.cursor()
cur.execute(__SQL__)
rows = cur.fetchall()

for row in rows:
    for col in row:
        print(col,end=' ')
    print()


# ■ Multimenge: UNION ALL
# <br>
# □ Beliebt, da schnell
# <br>
# □ Verwenden falls
# <br>
# – Semantik egal
# <br>
# – Multimengensemantik erwünscht
# <br>
# – Mengeneigenschaft von Input und Output bereits bekannt
# 
# #### Differenz: EXCEPT
# 
# ■ Auch MINUS

# In[53]:


#%sql (SELECT Titel, Jahr FROM Film) EXCEPT (SELECT FilmTitel AS Titel, FilmJahr AS Jahr FROM spielt_in) 

__SQL__ = "(SELECT Titel, Jahr FROM Film) EXCEPT (SELECT FilmTitel AS Titel, FilmJahr AS Jahr FROM spielt_in)"
conn = sqlite3.connect("filme/filme.db")
cur = conn.cursor()
cur.execute(__SQL__)
rows = cur.fetchall()

for row in rows:
    for col in row:
        print(col,end=' ')
    print()


# ■ Multimenge: EXCEPT ALL
# 
# #### Klammerung

# In[ ]:


get_ipython().run_line_magic('sql', 'SELECT * FROM ((SELECT A FROM R)INTERSECT(SELECT * FROM (SELECT A FROM S) UNION (SELECT A FROM T)))')


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
# ■ Eine Anfrage kann Teil einer anderen Anfrage sein.
# <br>
# □ Theoretisch beliebig tiefe Schachtelung
# <br><br>
# ■ Drei Varianten
# <br>
# 1. Subanfrage erzeugt einen einzigen Wert, der in der WHERE-Klausel mit einem anderen Wert verglichen
# werden kann.
# <br>
# 2. Subanfrage erzeugt eine Relation, die auf verschiedene Weise in WHERE-Klausel verwendet werden kann.
# <br>
# 3. Subanfrage erzeugt eine Relation, die in der FROM Klausel verwendet werden kann.
# <br>
# – Wie jede normale Relation
# 
# ### Skalare Subanfragen
# 
# ■ Allgemeine Anfragen produzieren Relationen.
# <br>
# □ Mit mehreren Attributen
# <br>
# – Zugriff auf ein bestimmtes Attribut ist möglich
# <br>
# □ i.A. mit mehreren Tupeln
# <br>
# □ Manchmal (garantiert) nur maximal ein Tupel und Projektion auf nur ein Attribut
# <br>
# – „Skalare Anfrage“
# <br>
# – Verwendung wie eine Konstante möglich
# <br>
# – Falls keine Zeile: null
# <br>
# ![title](skalare_subanfragen.jpg)
# <br>
# ■ ManagerIn(Name, Adresse, ManagerinID, Gehalt)
# <br>
# ■ Film(Titel, Jahr, Länge, inFarbe, StudioName, ProduzentinID)
# <br>
# ■ Gesucht: Produzent von Star Wars

# In[55]:


#SELECT Name 
#FROM Film, ManagerIn 
#WHERE Titel = ‘Star Wars‘ 
#AND Jahr = ‘1977‘ 
#AND ProduzentinID = ManagerinID;

__SQL__ = "SELECT Name FROM Film, ManagerIn WHERE Titel = 'Star Wars' AND Jahr = 1977 AND ProduzentinID = ManagerinID"
conn = sqlite3.connect("filme/filme.db")
cur = conn.cursor()
cur.execute(__SQL__)
rows = cur.fetchall()

for row in rows:
    for col in row:
        print(col,end=' ')
    print()


# ■ Oder aber

# In[57]:


#SELECT Name FROM ManagerIn 
#WHERE ManagerinID = ( SELECT ProduzentinID FROM Film WHERE Titel = "Star Wars" AND Jahr = 1977 );

__SQL__ = "SELECT Name FROM ManagerIn WHERE ManagerinID = ( SELECT ProduzentinID FROM Film WHERE Titel = 'Star Wars' AND Jahr = 1977 );"
conn = sqlite3.connect("filme/filme.db")
cur = conn.cursor()
cur.execute(__SQL__)
rows = cur.fetchall()

for row in rows:
    for col in row:
        print(col,end=' ')
    print()


# ■ DBMS erwartet maximal ein Tupel als Ergebnis der Teilanfrage
# <br>
# □ Falls kein Tupel: null
# <br>
# □ Falls mehr als ein Tupel: Laufzeitfehler
# 
# #### Skalare Subanfragen – Beispiel 
# ■ Abteilungen, deren durchschnittliche Bonuszahlungen höher sind als deren durchschnittliches Gehalt.

# In[ ]:


get_ipython().run_line_magic('sql', '')
SELECT a.Name, a.Standort FROM Abteilung a WHERE (SELECT AVG(bonus) FROM personal p WHERE a.AbtID = p.AbtID)>(SELECT AVG(gehalt)FROM personal pWHERE a.AbtID = p.AbtID)


# ■ Alle Potsdamer Abteilungen mit ihrem Maximalgehalt.

# In[ ]:


get_ipython().run_line_magic('sql', '')
SELECT a.AbtID, a.Name,
           (SELECT MAX(Gehalt)
                FROM Personal p
            WHERE a.AbtID = p.AbtID) AS maxGehalt
FROM Abteilung a
WHERE a.Ort = ‘Potsdam‘


# ■ Anmerkung: Auch Abteilungen ohne Mitarbeiter erscheinen im Ergebnis.
# <br><br>
# ■ Nicht so in der folgenden Anfrage:

# In[ ]:


get_ipython().run_line_magic('sql', '')
SELECT a.AbtID, a.Name, MAX(p.Gehalt) AS maxGehalt
FROM Abteilung a, Personal p
WHERE a.Ort = ‘Potsdam‘
AND a.AbtID = p.AbtID
GROUP BY a.AbtID, a.Name


# ### Bedingungen mit Relationen
# ■ Bestimmte SQL Operatoren auf Relationen erzeugen Boole‘sche Werte
# <br>
# □ EXISTS R
# <br>
# – TRUE, falls R nicht leer
# <br>
# □ x IN R
# <br>
# – TRUE falls x gleich einem Wert in R ist (R hat nur ein Attribut)
# <br>
# – Verallgemeinerung auf Tupel später
# <br>
# – x NOT IN R: TRUE falls x keinem Wert in R gleicht
# <br>
# □ x > ALL R
# <br>
# – TRUE falls x größer als jeder Wert in R ist (R hat nur ein Attribut)
# <br>
# – Alternativ: <, >, <=, >=, <>, =
# <br>
# – x <> ALL R: Entspricht x NOT IN R bzw. auch NOT(x in R)
# <br>
# □ x > ANY R
# <br>
# – TRUE falls x größer als mindestens ein Wert in R ist (R hat nur ein Attribut)
# <br>
# – Alternativ: <, >, <=, >=, <>, =
# <br>
# – x = ANY R: Entspricht x IN R
# <br>
# – Alternativer Befehl: SOME
# <br>
# □ Negation mit NOT(…) ist immer möglich.
# ### EXISTS Beispiele
# ■ ISBNs aller ausgeliehenen Bücher

# In[ ]:


get_ipython().run_line_magic('sql', '')
SELECT ISBN
FROM BuchExemplar
WHERE EXISTS
     (SELECT *
      FROM Ausleihe
      WHERE Ausleihe.Inventarnr = BuchExemplar.Inventarnr) 


# ■ Lehrstuhlbezeichnungen der Professor*innen, die alle von ihnen gelesenen Vorlesungen auch schon einmal
# geprüft haben.
# <br><br>
# ■ bzw. Lehrstuhlbezeichnungen von Professor*innen, so dass keine von diesem gelesene Vorlesung existiert, die von
# ihm nicht geprüft wurde.

# In[ ]:


get_ipython().run_line_magic('sql', '')
SELECT Lehrstuhlbezeichnung
FROM Prof
WHERE NOT EXISTS
      (SELECT *
       FROM Liest
       WHERE Liest.PANr = Prof.PANr
       AND NOT EXISTS (SELECT *
                   FROM Prüft
                   WHERE Prüft.PANr = Prof.PANr
                   AND Prüft.VL_NR = Liest.VL_NR)
) 


# ### IN Beispiele
# ■ Eine Auswahl an Büchern

# In[ ]:


get_ipython().run_line_magic('sql', '')
SELECT Titel
FROM Bücher
WHERE ISBN IN (‘3898644006‘, ‘1608452204‘, ‘0130319953‘)


# ■ Matrikel der Studenten, die zumindest einen Prüfer gemeinsam mit dem Studenten der Matrikel ‚123456‘ haben

# In[ ]:


get_ipython().run_line_magic('sql', '')
SELECT DISTINCT Matrikel
FROM Prüft
WHERE Prüfer IN ( SELECT Prüfer
                  FROM Prüft
                  WHERE Matrikel = ‘123456‘)``` 


# In[ ]:


get_ipython().run_line_magic('sql', '')
SELECT DISTINCT P1.Matrikel
FROM Prüft P1, Prüft P2
WHERE P2.Matrikel = `123456`
AND P1.Prüfer = P2.Prüfer


# ■ Nachnamen aller Professor*innen, die schon einmal eine 1,0 vergeben haben.

# In[ ]:


get_ipython().run_line_magic('sql', '')
SELECT Nachname
FROM Prof
WHERE 1.0 IN ( SELECT Note
FROM Prüft
WHERE Prüfer = Prof.ID )


# ■ Achtung: Korrelierte Subanfrage
# 
# ### ALL und ANY Beispiele
# 
# ■ Die schlechteste Note des Studenten mit Matrikel 123456

# In[ ]:


get_ipython().run_line_magic('sql', '')
SELECT Note
FROM Prüft
WHERE Matrikel = ‘123456‘
AND Note >= ALL (SELECT Note
                 FROM Prüft
                 WHERE Matrikel = ‘123456‘)


# ■ Alle Studenten, die mindestens eine Prüfung absolvierten

# In[ ]:


get_ipython().run_line_magic('sql', '')
SELECT Name, Matrikel
FROM Student
WHERE Matrikel = ANY (SELECT Matrikel
                      FROM Prüft)


# ### Bedingungen mit Tupeln
# ■ Verallgemeinerung von IN, ALL und ANY auf Tupel
# <br>
# □ t IN R
# <br>
# – TRUE falls t ein Tupel in R ist (mehr als ein Attribut möglich)
# <br>
# – Setzt gleiche Schemata voraus
# <br>
# – Setzt gleiche Reihenfolge der Attribute voraus
# <br>
# □ t > ALL R
# <br>
# – TRUE falls t größer als jedes Tupel in R ist
# <br>
# – Vergleiche in Standardreihenfolge der Attribute
# <br>
# □ t <> ANY R
# <br>
# – TRUE falls R mindestens ein Tupel hat, das ungleich t ist
# <br>
# <br>
# ■ Namen von Produzenten von Filmen mit Harrison Ford

# In[59]:


#SELECT Name 
#FROM ManagerIn 
#WHERE ManagerinID IN( SELECT ProduzentinID FROM Film WHERE (Titel, Jahr) 
#IN( SELECT FilmTitel AS Titel, FilmJahr AS Jahr FROM spielt_in WHERE Name = "Harrison Ford"));

__SQL__ = "SELECT Name FROM ManagerIn WHERE ManagerinID IN( SELECT ProduzentinID FROM Film WHERE (Titel, Jahr) IN( SELECT FilmTitel AS Titel, FilmJahr AS Jahr FROM spielt_in WHERE Name = 'Harrison Ford'))"
conn = sqlite3.connect("filme/filme.db")
cur = conn.cursor()
cur.execute(__SQL__)
rows = cur.fetchall()

for row in rows:
    for col in row:
        print(col,end=' ')
    print()


# ■ Analyse am besten von innen nach außen
# <br><br>
# ■ Alternative Formulierung

# In[61]:


#SELECT Name 
#FROM ManagerIn, Film, spielt_in 
#WHERE ManagerinID = ProduzentinID 
#AND Titel = FilmTitel 
#AND Jahr = FilmJahr 
#AND SchauspielerIn.Name = "Harrison Ford";

__SQL__ = "SELECT Name FROM ManagerIn, Film, spielt_in WHERE ManagerinID = ProduzentinID AND Titel = FilmTitel AND Jahr = FilmJahr AND SchauspielerIn.Name = 'Harrison Ford'"
conn = sqlite3.connect("filme/filme.db")
cur = conn.cursor()
cur.execute(__SQL__)
rows = cur.fetchall()

for row in rows:
    for col in row:
        print(col,end=' ')
    print()


# ### Subanfragen in FROM-Klausel
# ■ Bisher: Nur Subanfragen in WHERE-Klausel
# <br>
# □ Anstelle einfacher Relation steht eine geklammerte Subanfrage
# <br>
# □ Es muss ein Alias vergeben werden.
# <br>

# In[64]:


#SELECT M.Name 
#FROM ManagerIn M, (SELECT ProduzentinID AS ID FROM Film, spielt_in WHERE Titel = FilmTitel AND Jahr = FilmJahr AND Name = "Harrison Ford") ProduzentIn 
#WHERE M.ManagerinID = ProduzentIn.ID;

__SQL__ = "SELECT M.Name FROM ManagerIn M, (SELECT ProduzentinID AS ID FROM Film, spielt_in WHERE Titel = FilmTitel AND Jahr = FilmJahr AND Name = 'Harrison Ford') ProduzentIn WHERE M.ManagerinID = ProduzentIn.ID"
conn = sqlite3.connect("filme/filme.db")
cur = conn.cursor()
cur.execute(__SQL__)
rows = cur.fetchall()

for row in rows:
    for col in row:
        print(col,end=' ')
    print()


# ### Korrelierte Subanfragen
# ■ Unkorreliert: Subanfragen einmalig ausführen und das Ergebnis weiterverwenden
# <br><br>
# ■ Korrelierte Subanfragen werden mehrfach ausgeführt, einmal pro Bindung der korrelierten Variable der äußeren
# Anfrage
# <br><br>
# ■ Alle mehrfachen Filme mit Ausnahme der jeweils jüngsten Ausgabe

# In[65]:


#%sql SELECT Titel, Jahr 
#FROM Film Alt 
#WHERE Jahr < ANY ( SELECT Jahr FROM Film WHERE Titel = Alt.Titel);

__SQL__ = "SELECT Titel, Jahr FROM Film Alt WHERE Jahr < ANY ( SELECT Jahr FROM Film WHERE Titel = Alt.Titel)"
conn = sqlite3.connect("filme/filme.db")
cur = conn.cursor()
cur.execute(__SQL__)
rows = cur.fetchall()

for row in rows:
    for col in row:
        print(col,end=' ')
    print()


# □ Ausführung der Subanfrage für jedes Tupel in Filme
# 
# Scope: Attributnamen gehören zunächst zur Tupelvariablen der aktuellen Anfrage. Sonst: Suche von innen nach außen.
# 
# Unkorreliert:
# <br>
# Name und Gehalt aller Mitarbeiter in Potsdam

# In[ ]:


get_ipython().run_line_magic('sql', '')
SELECT Name, Gehalt
FROM Personal p
WHERE AbtID IN
    (SELECT AbtID
    FROM Abteilung
    WHERE Ort =
‘Potsdam‘)


# Korreliert:
# <br>
# Name und Gehalt aller Mitarbeiter, deren Gehalt höher als 10% des Abteilungsbudgets ist.

# In[ ]:


get_ipython().run_line_magic('sql', '')
SELECT Name, Gehalt
FROM Personal p
WHERE Gehalt >
    (SELECT 0.1*Budget
    FROM Abteilung a
    WHERE a.AbtID =
p.AbtID)


# ## Operationen auf einer Relation
# ### Duplikateliminierung
#  Relationale DBMS verwenden i.d.R. Multimengensemantik, nicht Mengensemantik.
#  <br>
# □ Duplikate entstehen durch
#  <br>
# – Einfügen von Duplikaten in Basisrelation
#  <br>
# – Veränderung von Tupeln in Basisrelation
#  <br>
# – Projektion in Anfragen
#  <br>
# – Durch Subanfragen (UNION ALL)
#  <br>
# – Vermehrung von Duplikaten durch Kreuzprodukt
#  <br> <br>
# ■ Duplikateliminierung
#  <br>
# □ SELECT DISTINCT Attributnamen
#  <br>
# □ Kosten sind hoch: Sortierung oder hashing
#  <br>
# ■ Alle Filme, in denen mindestens ein Schauspieler mitspielt

# In[66]:


#SELECT DISTINCT FilmTitel, FilmJahr 
#FROM spielt_in

__SQL__ = "SELECT DISTINCT FilmTitel, FilmJahr FROM spielt_in"
conn = sqlite3.connect("filme/filme.db")
cur = conn.cursor()
cur.execute(__SQL__)
rows = cur.fetchall()

for row in rows:
    for col in row:
        print(col,end=' ')
    print()


# ![title](duplikateliminierung.jpg)
# #### Wdh.: Duplikateliminierung bei Mengenoperationen
# ■ Mengenoperationen in SQL entfernen Duplikate
# <br>
# □ UNION, INTERSECT, EXCEPT
# <br>
# □ wandeln Multimengen in Mengen um und verwenden Mengensemantik
# <br>
# □ Solche Duplikateliminierung verhindern durch ALL
# <br>

# In[69]:


#(SELECT Titel, Jahr, FROM Film) UNION ALL (SELECT FilmTitel AS Titel, FilmJahr AS Jahr FROM spielt_in);

__SQL__ = "(SELECT Titel, Jahr, FROM Film) UNION ALL (SELECT FilmTitel AS Titel, FilmJahr AS Jahr FROM spielt_in)"
conn = sqlite3.connect("filme/filme.db")
cur = conn.cursor()
cur.execute(__SQL__)
rows = cur.fetchall()

for row in rows:
    for col in row:
        print(col,end=' ')
    print()


# – Film mit drei Schauspielern erscheint also 4 Mal im Ergebnis
# <br>
# □ R INTERSECT ALL S
# <br>
# □ R EXCEPT ALL S
# 
# ### Aggregation
# ■ Standardaggregationsoperatoren
# <br>
# □ SUM, AVG, MIN, MAX, COUNT
# <br>
# □ Angewendet auf einzelne Attribute in der SELECT-Klausel
# <br><br>
# ■ Typische weitere Aggregationsoperatoren
# <br>
# □ VAR, STDDEV
# <br><br>
# ■ COUNT(*) zählt Anzahl der Tupel
# <br>
# □ in der Relation, die durch die FROM und WHERE Klauseln definiert wird.
# <br><br>
# ■ Kombination mit DISTINCT
# <br>
# □ COUNT(DISTINCT Jahr)
# <br>
# □ SUM(DISTINCT Gehalt)
# 
# #### Aggregation – Beispiele

# In[70]:


#SELECT AVG(Gehalt) 
#FROM ManagerIn;

__SQL__ = "SELECT AVG(Gehalt) FROM ManagerIn"
conn = sqlite3.connect("filme/filme.db")
cur = conn.cursor()
cur.execute(__SQL__)
rows = cur.fetchall()

for row in rows:
    for col in row:
        print(col,end=' ')
    print()


# In[71]:


#SELECT COUNT(*) 
#FROM spielt_in;

__SQL__ = "SELECT COUNT(*) FROM spielt_in;"
conn = sqlite3.connect("filme/filme.db")
cur = conn.cursor()
cur.execute(__SQL__)
rows = cur.fetchall()

for row in rows:
    for col in row:
        print(col,end=' ')
    print()


# In[72]:


#SELECT COUNT(Name) 
#FROM spielt_in;

__SQL__ = "SELECT COUNT(Name) FROM spielt_in;"
conn = sqlite3.connect("filme/filme.db")
cur = conn.cursor()
cur.execute(__SQL__)
rows = cur.fetchall()

for row in rows:
    for col in row:
        print(col,end=' ')
    print()


# In[74]:


#SELECT COUNT(DISTINCT Name) 
#FROM spielt_in 
#WHERE FilmJahr = 1990;

__SQL__ = "SELECT COUNT(DISTINCT Name) FROM spielt_in WHERE FilmJahr = 1990;"
conn = sqlite3.connect("filme/filme.db")
cur = conn.cursor()
cur.execute(__SQL__)
rows = cur.fetchall()

for row in rows:
    for col in row:
        print(col,end=' ')
    print()


# ### Gruppierung, Aggregation und NULL
# ■ NULL wird bei Aggregation ignoriert.
# <br>
# □ Trägt also nicht zu SUM, AVG oder COUNT bei.
# <br>
# □ Ist nicht MIN oder MAX
# <br>
# □ Anzahl Tupel: SELECT COUNT(*) FROM spielt_in;
# <br>
# □ Anzahl nicht-NULL Werte: SELECT COUNT(Länge) FROM Film;
# <br><br>
# ■ NULL ist ein eigener Gruppierungswert
# <br>
# □ Es gibt also z.B. die NULL-Gruppe
# <br>
# □ SELECT A, COUNT(B) FROM R GROUP BY A;
# <br>
# – Ergebnis: (NULL, 0)
# <br>
# □ SELECT A, SUM(B) FROM R GROUP BY A;
# <br>
# – Ergebnis: (NULL, NULL)
# <br>
# 
# |A|B|
# |---|---|
# |NULL|NULL|
# 
# ### Gruppierung
# ■ Gruppierung mittels GROUP BY nach der WHERE-Klausel

# In[75]:


#SELECT StudioName, SUM(Laenge) 
#FROM Film GROUP BY StudioName

__SQL__ = "SELECT StudioName, SUM(Laenge) FROM Film GROUP BY StudioName"
conn = sqlite3.connect("filme/filme.db")
cur = conn.cursor()
cur.execute(__SQL__)
rows = cur.fetchall()

for row in rows:
    for col in row:
        print(col,end=' ')
    print()


# ■ In SELECT-Klausel zwei „Sorten“ von Attributen
# <br>
# 1. Gruppierungsattribute
# <br>
# 2. Aggregierte Attribute
# <br>
# □ Nicht-aggregierte Werte der SELECT-Klausel müssen in der GROUP BY-Klausel erscheinen.
# <br>
# □ Keine der beiden Sorten muss erscheinen.

# In[76]:


#SELECT StudioName 
#FROM Film 
#GROUP BY StudioName

__SQL__ = "SELECT StudioName FROM Film GROUP BY StudioName"
conn = sqlite3.connect("filme/filme.db")
cur = conn.cursor()
cur.execute(__SQL__)
rows = cur.fetchall()

for row in rows:
    for col in row:
        print(col,end=' ')
    print()


# In[77]:


#SELECT SUM(Laenge) 
#FROM Film 
#GROUP BY StudioName

__SQL__ = "SELECT SUM(Laenge) FROM Film GROUP BY StudioName"
conn = sqlite3.connect("filme/filme.db")
cur = conn.cursor()
cur.execute(__SQL__)
rows = cur.fetchall()

for row in rows:
    for col in row:
        print(col,end=' ')
    print()


# ■ Gruppierung bei Verwendung mehrerer Relationen wird am Schluss durchgeführt.

# In[79]:


#SELECT Name, SUM(Laenge) 
#FROM ManagerIn, Film 
#WHERE ManagerinID = ProduzentinID 
#GROUP BY Name

__SQL__ = "SELECT Name, SUM(Laenge) FROM ManagerIn, Film WHERE ManagerinID = ProduzentinID GROUP BY Name"
conn = sqlite3.connect("filme/filme.db")
cur = conn.cursor()
cur.execute(__SQL__)
rows = cur.fetchall()

for row in rows:
    for col in row:
        print(col,end=' ')
    print()


# ■ Reihenfolge der Ausführung (und des Lesens)
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
# ■ Einschränkung der Ergebnismenge nach der Gruppierung durch HAVING

# In[81]:


#SELECT Name, SUM(Laenge) 
#FROM ManagerIn, Film 
#WHERE ManagerinID = ProduzentinID 
#AND Gehalt > 1000000 GROUP BY Name

__SQL__ = "SELECT Name, SUM(Laenge) FROM ManagerIn, Film WHERE ManagerinID = ProduzentinID AND Gehalt > 1000000 GROUP BY Name"
conn = sqlite3.connect("filme/filme.db")
cur = conn.cursor()
cur.execute(__SQL__)
rows = cur.fetchall()

for row in rows:
    for col in row:
        print(col,end=' ')
    print()


# In[85]:


#SELECT Name, SUM(Laenge) 
#FROM ManagerIn, Film 
#WHERE ManagerinID = ProduzentinID 
#GROUP BY Name HAVING SUM(Laenge) > 1000

__SQL__ = "SELECT Name, SUM(Laenge) FROM ManagerIn, Film WHERE ManagerinID = ProduzentinID GROUP BY Name HAVING SUM(Laenge) > 1000"
conn = sqlite3.connect("filme/filme.db")
cur = conn.cursor()
cur.execute(__SQL__)
rows = cur.fetchall()

for row in rows:
    for col in row:
        print(col,end=' ')
    print()


# In[86]:


#SELECT Name 
#FROM ManagerIn, Film 
#WHERE ManagerinID = ProduzentinID 
#GROUP BY Name HAVING SUM(Laenge) > 1000

__SQL__ = "SELECT Name FROM ManagerIn, Film WHERE ManagerinID = ProduzentinID GROUP BY Name HAVING SUM(Laenge) > 1000"
conn = sqlite3.connect("filme/filme.db")
cur = conn.cursor()
cur.execute(__SQL__)
rows = cur.fetchall()

for row in rows:
    for col in row:
        print(col,end=' ')
    print()


# ■ Aggregationen in HAVING-Klausel beziehen sich nur auf aktuelle Gruppe.
# <br>
# ■ Nur Gruppierungsattribute dürfen un-aggregiert in HAVING Klausel erscheinen (wie bei
# SELECT-Klausel).
# ### Zusammenfassung SQL
#  Grundbausteine einer SQL Anfrage (mit empfohlener Lesereihenfolge)
#  <br>
# □ 6. SELECT
# <br>
# □ 1. FROM
# <br>
# □ 2. WHERE
# <br>
# □ 3. GROUP BY
# <br>
# □ 4. HAVING
# <br>
# □ 5. ORDER BY
# <br><br>
# ■ SELECT … FROM … sind Pflicht.
# <br>
# □ Ausnahme: z.B. SELECT 7 + 3
# <br><br>
# ■ HAVING darf nur in Kombination mit GROUP BY erscheinen.

# ## Datenbearbeitung(DML)
# ### Überblick
# ■  CRUD: Create, Read, Update, Delete
# <br><br>
# ■ Einfügen
# <br>
# □ INSERT INTO … VALUES…
# <br><br>
# ■ Löschen
# <br>
# □ DELETE FROM … WHERE …
# <br><br>
# ■ Ändern
# <br>
# □ UPDATE … SET … WHERE …
# ### Einfügen
# ■ Grundbaustein
# <br>
# □ INSERT INTO R(A1, …, An) VALUES (v1,…,vn);
# <br>
# □ Bei fehlenden Attributen
# <br>
# – Default-Wert aus Tabellendefinition (NULL, falls nicht anders angegeben)
# <br>
# □ Beispiel

# In[ ]:


get_ipython().run_line_magic('sql', 'INSERT INTO spielt_in(FilmTitel, FilmJahr, Schauspieler) VALUES (‘Star Wars‘, 1977, ‘Alec Guinness‘);')


# – Reihenfolge der Werte und Attribute wird beachtet.
# 
# □ Falls alle Attribute gesetzt werden, kann Attributliste fehlen:

# In[ ]:


get_ipython().run_line_magic('sql', 'INSERT INTO spielt_in VALUES (‘Star Wars‘, 1977, ‘Alec Guinness‘);')


# – Reihenfolge entsprechend der Spezifikation des Schemas
# (CREATE TABLE …)
# #### Einfügen per Anfrage
#  Füge in Studio-Tabelle alle Studios der Filme-Relation ein
#  <br>
# □ Film(Titel, Jahr, Länge, inFarbe, StudioName, ProduzentinID)
#  <br>
# □ Studio(Name, Adresse, VorsitzendeID)

# In[ ]:


get_ipython().run_line_magic('sql', '')
INSERT INTO Studio(Name)
SELECT DISTINCT StudioName
FROM Film
WHERE StudioName NOT IN
    (SELECT Name
    FROM Studio);


# Adresse und VorsitzendeIDbleiben NULL.
#  <br>
# □ Erzeugt im Allgemeinen Redundanz und sollte vermieden werden.
# ### Ausführungsreihenfolge beim Einfügen
# Wann wird eingefügt?
# <br>
# Nach vollständiger Ausführung der SELECT FROM WHERE Anfrage?
# <br>
# Sofort?
# <br>
# Schnellere Implementation
# <br>
# Was passiert jeweils bei Anfrage 1?
# <br>
# Was passiert jeweils bei Anfrage 2?
# <br>
# SQL Standard: Erst gesamte Anfrage ausführen

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
# 
# ■ INSERT
# <br>
# □ Zeilenbasiertes Einfügen aus SQL statements
# <br><br>
# ■ IMPORT
# <br>
# □ Zeilen-basiertes Einfügen aus Datei
# <br>
# □ Trigger und Nebenbedingungen bleiben aktiv
# <br>
# □ Indizes werden laufend aktualisiert
# <br><br>
# ■ LOAD
# <br>
# □ Seiten-basiertes Einfügen aus Datei
# <br>
# □ Trigger und Nebenbedingungen werden deaktiviert
# <br>
# □ Deutlich effizienter
# <br>
# □ Indizes werden am Ende neu generiert
# <br><br>
# ■ Syntax ist jeweils DBMS-spezifisch.
# <br>
# □ Viele Parameter
# 
# ### Löschen
# ■ Grundbaustein
# <br>
# □ DELETE FROM R WHERE …
# <br>
# □ Lösche alle Tupel in R, für die die Bedingung wahr ist.

# In[ ]:


get_ipython().run_line_magic('sql', '')
DELETE FROM spielt_in
WHERE FilmTitel = ‘The Maltese Falcon‘
AND FilmJahr = 1942
AND Schauspieler = ‘Sydney Greenstreet‘;


# ■ Tupel können im Gegensatz zum Einfügen nicht direkt angegeben werden, sondern müssen umschrieben werden.
# <br>

# In[ ]:


get_ipython().run_line_magic('sql', '')
DELETE FROM Manager
WHERE Gehalt < 10000000;


# ■ Alle Manager-Tupel löschen: DELETE FROM Manager;
# 
# ### Verändern (update)
# ■ Grundbaustein
# <br>
# □ UPDATE R SET … WHERE …
# <br>
# □ SET Klausel
# <br>
# – Wertzuweisungen
# <br>
# – Komma-separiert
# <br>

# In[ ]:


get_ipython().run_line_magic('sql', '')
UPDATE Manager
SET Name = ‘Präs. ‘ || Name
WHERE ManagerinID IN
(SELECT PräsidentID FROM Studios);


# ## Schemata(DDL)
# ### Überblick
# ■ Datentypen 
# <br>
# ■ Tabellen
# <br>
# ■ Default-Werte 
# <br>
# ■ Indizes
# 
# ### Datentypen
# ■ Jedes Attribut muss einen Datentyp haben. 
# <br>
# □ CHAR(n) – String fester Länge (n Zeichen) 
# <br>
# □ VARCHAR(n) – String variabler Länge, maximal n Zeichen 
# <br>
# □ BIT(n) bzw. BIT VARYING(n) – Wie CHAR, aber Bits 
# <br>
# □ BOOLEAN – TRUE, FALSE oder UNKNOWN 
# <br>
# □ INT / INTEGER bzw. SHORTINT – 8 bzw. 4 Byte 
# <br>
# □ FLOAT / REAL bzw. DOUBLE PRECISION 
# <br>
# □ DECIMAL (n,d) – Z.B. Gehalt DECIMAL(7,2) – 7 Stellen, davon 2 Nachkommastellen
# <br>
# □ CLOB und BLOB
# 
# ### Überblick DB2 Datentypen
# ![title](db2_datentypen.jpg)
# 
# ### Tabellen
# ■ Grundbaustein zum Erzeugen

# In[ ]:


get_ipython().run_line_magic('sql', '')
CREATE TABLE R …
CREATE TABLE Schauspieler (
Name CHAR(30),
Adresse VARCHAR(255),
Geschlecht CHAR(1),
Geburtstag DATE );


# ■ Löschen
# <br>
# □ DROP TABLE Schauspieler;
# <br><br>
# ■ Verändern
# <br>
# □ ALTER TABLE Schauspieler ADD Telefon CHAR(6);
# <br>
# – Nullwerte entstehen
# <br>
# □ ALTER TABLE Schauspieler DROP Geburtstag;
# <br>
# □ ALTER TABLE Schauspieler MODIFY Telefon CHAR(10);
# 
# ### Default-Werte

# In[ ]:


get_ipython().run_line_magic('sql', '')
CREATE TABLE Schauspieler (
Name CHAR(30),
Adresse VARCHAR(255),
Geschlecht CHAR(1) DEFAULT ‚?‘,
Geburtstag DATE DEFAULT DATE ‚0000-00-00‘);

ALTER TABLE Schauspieler
ADD Telefon CHAR(16) DEFAULT ‚unbekannt‘;


# ### Constraints und Trigger
#  Weitere Optionen für Tabellen
#  <br>
# □ PRIMARY KEY
#  <br>
# □ UNIQUE
#  <br>
# □ FOREIGN KEY … REFERENCES …
#  <br>
# □ NOT NULL
#  <br>
# □ CHECK
#  <br>
# □ CREATE ASSERTION
#  <br>
# □ CREATE TRIGGER
#  <br>
# ■ Siehe separater Foliensatz
# 
# ### Indizes
# ■ Ein Index auf einem Attribut ist eine Datenstruktur, die es dem DBMS erleichtert, Tupel mit einem bekannten Wert des Attributs zu finden.
# <br>
# □ Nicht SQL-Standard, aber in (fast) jedem DBMS verfügbar.
# <br><br>
# ■ Motivation

# In[87]:


#%sql SELECT * 
#FROM Film 
#WHERE StudioName = "Disney" 
#AND Jahr = 1990;

__SQL__ = "SELECT * FROM Film WHERE StudioName = 'Disney' AND Jahr = 1990"
conn = sqlite3.connect("filme/filme.db")
cur = conn.cursor()
cur.execute(__SQL__)
rows = cur.fetchall()

for row in rows:
    for col in row:
        print(col,end=' ')
    print()


# □ Variante 1: Alle 100.000 Tupel durchsuchen und WHERE Bedingung prüfen
# <br>
# □ Variante 2: Direkt alle 2000 Filme aus 1990 betrachten und auf ‚Disney‘ prüfen.
# <br>
# – CREATE INDEX JahrIndex ON Film(Jahr);
# <br>
# □ Variante 3: Direkt alle 100 Filme aus 1990 von ‘Disney‘ holen.

# In[ ]:


get_ipython().run_line_magic('sql', '')
CREATE INDEX JahrStudioIndex
ON Film(Jahr, Studioname);


# ■ Indizes auf einzelnen Attributen
# <br>
# □ CREATE INDEX JahrIndex ON Film(Jahr);
# <br><br>
# ■ Indizes auf mehreren Attributen

# In[ ]:


get_ipython().run_line_magic('sql', '')
CREATE INDEX JahrStudioIndex
ON Film(Jahr, Studioname);


# □ Reihenfolge wichtig! Warum?
# <br><br>
# ■ Löschen
# <br>
# □ DROP INDEX JahrIndex;
# 
# #### Indexwahl
# ■ Abwägung
# <br>
# □ Index beschleunigt Punkt- (und Bereichs-) Anfragen und Join-Anfragen erheblich.
# <br>
# □ Index verlangsamt das Einfügen, Löschen und Verändern von Tupeln der Relation.
# <br>
# – Index muss jeweils zusätzlich aktualisiert werden.
# <br>
# □ Indizes benötigen Speicherplatz.
# <br><br>
# ■ Wahl der besten Indizes ist eine der schwierigsten Aufgaben des Datenbankdesigns.
# <br>
# □ Vorhersage der query workload und update-Frequenz
# <br>
# □ Wahl der Attribute
# <br>
# – Häufiger Vergleich mit Konstanten
# <br>
# – Häufiges Joinattribut
# 
# #### Indexwahl – Vorüberlegungen
# ■ Relationen sind typischerweise über mehrere Diskblöcke gespeichert.
# <br>
# □ Wichtigste Datenbankkosten sind die Anzahl der Diskblöcke, die in den Hauptspeicher gelesen werden müssen.
# <br>
# □ Bei Punktanfragen mit Index müssen statt aller Blöcke nur ein Block gelesen werden.
# <br>
# □ Aber Index selbst muss ebenfalls gespeichert und gelesen werden.
# <br>
# – IdR viel mehr Tupel pro Block repräsentiert: Nur Schlüsselwert und Speicheradresse, keine Daten
# <br>
# □ Updates kosten sogar doppelt: Lesen und Schreiben auch der Index-Blöcke
# 
# #### Indexwahl – Beispiel
# ■ spielt_in(FilmTitel, FilmJahr, Schauspieler)
# <br><br>
# ■ Drei typische Anfragen

# In[88]:


#%sql SELECT FilmTitel, FilmJahr 
#FROM spielt_in WHERE Name = s;

__SQL__ = "SELECT FilmTitel, FilmJahr FROM spielt_in WHERE Name = s"
conn = sqlite3.connect("filme/filme.db")
cur = conn.cursor()
cur.execute(__SQL__)
rows = cur.fetchall()

for row in rows:
    for col in row:
        print(col,end=' ')
    print()


# In[ ]:


get_ipython().run_line_magic('sql', '')
SELECT Schauspieler FROM spielt_in
WHERE FilmTitel = t AND FilmJahr = j;
INSERT INTO spielt_in VALUES(t, j, s);


# ■ Annahmen
# <br>
# □ spielt_in ist auf 10 Disk-Blöcke verteilt.
# <br>
# □ Durchschnittlich habe jeder Film 3 Schauspieler.
# <br>
# □ Durchschnittlich spiele jeder Schauspieler in 3 Filmen.
# <br>
# □ Annahme des Schlimmsten: 3 Tupel sind auf 3 Blöcke verteilt
# <br>
# □ Index ist auf 1 Block gespeichert.
# <br>
# □ Lesen und Schreiben kostet 1.
# <br>
# □ Update und Insert kosten jeweils 2.
# 
# #### Indexwahl – Beispiel
# 
# |Anfrage|Kein Index|SchauspielerIndex|FilmIndex|Beide Indizes|
# |---|---|---|---|---|
# |**Schauspieler = s**|10|4|10|4|
# |**FilmTitel = t AND FilmJahr = j**|10|10|4|4|
# |**INSERT INTO spielt_in**|2|4|4|6|
# |**Gesamtkosten**|2+8$p_1$8$p_2$|4+6$p_2$|4+6$p_1$|6-2$p_1$-2$p_2$|
# 
# 
# ■ p1: Anteil Anfrage 1
# <br>
# ■ p2: Anteil Anfrage 2
# <br>
# ■ 1‒p1‒p2: Anteil Anfrage 3
# <br>
# 
# 
# ### Verteilung in IMDB (Real-world Daten, Stand ca. 2010)
# ![title](imdb.jpg)

# In[ ]:


get_ipython().run_line_magic('sql', '')
WITH
m AS (SELECT count(*) AS ZahlMovies FROM imdb.movie),
actress AS (SELECT count(*) AS ZahlActress FROM imdb.actress),
actor AS (SELECT count(*) AS ZahlActor FROM imdb.actor),
actors AS (SELECT (ZahlActress + ZahlActor) AS GesamtActors
FROM actress, actor)
SELECT DOUBLE(actors.GesamtActors) / DOUBLE(m.ZahlMovies)
FROM m, actors


# Schauspieler*in pro Spielfilm: 8,7

# In[ ]:


get_ipython().run_line_magic('sql', '')
WITH
actors AS (SELECT * FROM imdb.actor UNION
SELECT * FROM imdb.actress),
counts AS (SELECT name, count(movie_id) AS m
FROM actors GROUP BY name)
SELECT AVG(DOUBLE(m)) FROM counts


# Spielfilme pro Schauspieler: 4,2

# ## Sichten
# ### Virtuelle Relationen
# 
# ■ Relationen aus CREATE TABLE Ausdrücken existieren tatsächlich (materialisiert, physisch) in der Datenbank.
# <br>
# □ Persistenz
# <br>
# □ Updates sind möglich
# <br><br>
# ■ Die Daten aus Sichten (views) existieren nur virtuell.
# <br>
# □ Sichten entsprechen Anfragen, denen man einen Namen gibt. Sie wirken wie physische Relationen.
# <br>
# □ Updates sind nur manchmal möglich.
# <br>
# <br>
# ![title](stonebraker1.jpg)
# <br>
# ![title](stonebraker2.jpg)
# <br>
# Michael Stonebraker: Implementation of Integrity Constraints and Views by Query Modification. SIGMOD Conference 1975: 65-78
# 
# ### Sichten in SQL
# ■ CREATE VIEW Name AS Anfrage

# In[ ]:


get_ipython().run_line_magic('sql', '')
CREATE VIEW ParamountFilme AS
SELECT Titel, Jahr
FROM Film
WHERE StudioName = "Paramount";


# □ Auch mehr als eine Relation möglich!
# <br><br>
# ■ Bedeutung einer Anfrage an die Sicht
# <br>
# 1. Ausführung der Anfrage aus der Sichdefinition
# <br>
# 2. Die ursprüngliche Anfrage verwendet dann das Ergebnis als Relation.
# <br><br>
# ■ Daten der Sicht ändern sich mit der Änderung der zugrundeliegenden Relationen.
# <br>
# ■ Entfernen der Sicht: DROP VIEW ParamountFilme
# <br>
# □ Basisdaten bleiben unverändert.
# 
# ### Anfragen an Sichten

# In[ ]:


get_ipython().run_line_magic('sql', '')
CREATE VIEW ParamountFilme AS
SELECT Titel, Jahr
FROM Film
WHERE StudioName = "Paramount";


# In[ ]:


get_ipython().run_line_magic('sql', '')
SELECT Titel
FROM ParamountFilme
WHERE Jahr = 1979;


# ■ Umwandlung der ursprünglichen Anfrage in eine Anfrage an Basisrelationen

# In[10]:


#SELECT Titel 
#FROM Film 
#WHERE StudioName = "Paramount" 
#AND Jahr = 1979;

__SQL__ = "SELECT Titel FROM Film WHERE StudioName = 'Paramount' AND Jahr = 1979;"
conn = sqlite3.connect("filme/filme.db")
cur = conn.cursor()
cur.execute(__SQL__)
rows = cur.fetchall()

for row in rows:
    for col in row:
        print(col,end=' ')
    print()


# □ Übersetzung durch DBMS
# <br>
# ■ Anfrage zugleich an Sichten und Basisrelationen möglich

# In[13]:


#Anfrage aus VL Folien
#SELECT DISTINCT SchauspielerIn
#FROM ParamountFilme, spielt_in
#WHERE Titel = FilmTitel AND Jahr = FilmJahr;

#Anfrage für filme.db
__SQL__ = "SELECT DISTINCT Name FROM Film, spielt_in WHERE Titel = FilmTitel AND Jahr = FilmJahr;"
conn = sqlite3.connect("filme/filme.db")
cur = conn.cursor()
cur.execute(__SQL__)
rows = cur.fetchall()

for row in rows:
    for col in row:
        print(col,end=' ')
    print()


# ■ Film(Titel, Jahr, Länge, inFarbe, StudioName, ProduzentinID)
# ■ Manager(Name, Adresse, ManagerinID, Gehalt)

# In[ ]:


get_ipython().run_line_magic('sql', '')
CREATE VIEW FilmeProduzenten AS
    SELECT Titel, Name
    FROM Film, Manager
    WHERE ProduzentinID = ManagerinID;


# ■ Anfrage

# In[93]:


#%sql SELECT Name FROM FilmeProduzenten WHERE Titel = ‘Gone with the Wind‘

__SQL__ = "SELECT Name FROM FilmeProduzenten WHERE Titel = 'Gone with the Wind'"
conn = sqlite3.connect("filme/filme.db")
cur = conn.cursor()
cur.execute(__SQL__)
rows = cur.fetchall()

for row in rows:
    for col in row:
        print(col,end=' ')
    print()


# ■ Bedeutung

# In[94]:


#%sql SELECT Name FROM Film, ManagerIn WHERE ProduzentinID = ManagerinID AND Titel = 'Gone with the Wind';

__SQL__ = "SELECT Name FROM Film, ManagerIn WHERE ProduzentinID = ManagerinID AND Titel = 'Gone with the Wind';"
conn = sqlite3.connect("filme/filme.db")
cur = conn.cursor()
cur.execute(__SQL__)
rows = cur.fetchall()

for row in rows:
    for col in row:
        print(col,end=' ')
    print()


# ■ Nebenbei: Umbenennung von Attributen

# In[ ]:


get_ipython().run_line_magic('sql', '')
CREATE VIEW FilmeProduzenten(FilmTitel, Produzentenname) AS
SELECT Titel, Name
FROM Film, ManagerIn
WHERE ProduzentinID = ManagerinID;


# ■ Oder auch: Sicht einfach nur zur Umbenennung

# In[ ]:


get_ipython().run_line_magic('sql', '')
CREATE VIEW Movie(title, year, length, inColor, studio, producerID) AS
SELECT *
FROM Film;


# ### Diskussion
# ■ Vorteile
# <br>
# □ Vereinfachung von Anfragen
# <br>
# □ Strukturierung der Datenbank
# <br>
# □ Logische Datenunabhängigkeit
# <br>
# – Sichten stabil bei Änderungen der Datenbankstruktur
# <br>
# – Sichtdefinitionen müssen gegebenenfalls angepasst werden
# <br>
# – Stabilität nicht bei jeder Änderung
# <br>
# □ Beschränkung von Zugriffen (Datenschutz)
# <br>
# □ Optimierung durch materialisierte Sichten
# <br><br>
# ■ Probleme
# <br>
# □ Automatische Anfragetransformation schwierig
# <br>
# □ Änderungen auf Sichten
# <br>
# □ Updatepropagierung für materialisierte Sichten
# 
# ### Updates auf Sichten
# ■ In einigen Fällen ist es möglich, Einfüge-, Lösch- oder Updateoperationen auf Sichten durchzuführen.
# <br>
# □ Wo speichern?
# <br>
# □ Welche Relation?
# <br>
# □ Zuordnung der Änderung zur Sicht?
# <br><br>
# ■ Übersetzung der Update-Operation auf eine Update-Operation der zugrunde liegenden Basisrelationen
# <br>
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
# ■ Filme(Titel, Jahr, Länge, inFarbe, StudioName, ProduzentinID)

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


# □ Wert für Studioname?
# □ Einfügen also nicht erlaubt.

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


# Dies muss Paramount sein. Ein anderes Studio entspricht nicht der View.
# <br><br>
# ■ Neues Tupel (‚Star Trek‘, 1979, 0, NULL, ‚Paramount‘, NULL)
# 
# ### Löschen und Updates auf Sichten
# ■ Löschen

# In[ ]:


get_ipython().run_line_magic('sql', '')
DELETE FROM ParamountFilme
WHERE Titel LIKE ‚%Trek%‘;


# ■ Wird umgeschrieben zu

# In[ ]:


get_ipython().run_line_magic('sql', '')
DELETE FROM Filme
WHERE Titel LIKE ‚%Trek%‘ AND StudioName = ‚Paramount‘;


# ■ Update

# In[ ]:


get_ipython().run_line_magic('sql', '')
UPDATE ParamountFilme
SET Jahr = 1979
WHERE Titel = ‚Star Trek the Movie‘;


# ■ Wird zu

# In[ ]:


get_ipython().run_line_magic('sql', '')
UPDATE Filme
SET Jahr = 1979
WHERE Titel = ‚Star Trek the Movie‘ AND StudioName = ‚Paramount‘;


# ### Tupelmigration
# ■ Manager(Name, Adresse, ManagerinID, Gehalt)

# In[ ]:


get_ipython().run_line_magic('sql', '')
CREATE VIEW Reiche AS
    SELECT Name, Gehalt, ManagerinID
    FROM ManagerIn
    WHERE Gehalt > 2000000;


# ■ Tupelmigration:
# <br>
# □ Ein Tupel (‚Eisner\`, ‚Hollywood‘, 25, 3000000) wird aus der Sicht „herausbewegt“.

# In[ ]:


get_ipython().run_line_magic('sql', '')
UPDATE Reiche SET Gehalt = 1500000
WHERE ManagerinID = 25;


# ■ Vorsicht bei der Implementierung, oder explizite Verhinderung:

# In[ ]:


get_ipython().run_line_magic('sql', '')
CREATE VIEW Reiche AS
SELECT Name, Gehalt
FROM ManagerIn
WHERE Gehalt > 2000000
WITH CHECK OPTION;


# □ Verhindert Tupelmigration durch Ablehnung problematischer Updates.
# 
# ### Anfrageplanung mit Sichten
# ■ Baumdarstellung von Anfragen
# <br>
# □ Blätter repräsentieren Relationen
# <br>
# – Basisrelationen
# <br>
# – Sichten
# <br>
# □ Ersetzung der Sichten durch die Sichtdefinition
# <br>
# – Als Subanfrage
# <br>
# ![title](anfrageplanung1.jpg)
# <br><br>
# ■ Sicht

# In[ ]:


get_ipython().run_line_magic('sql', '')
CREATE VIEW ParamountFilme AS
SELECT Titel, Jahr
FROM Filme
WHERE StudioName = ‚Paramount‘;


# ■ Anfrage

# In[14]:


#Anfrage aus VL Folien
#SELECT Titel 
#FROM ParamountFilme 
#WHERE Jahr = 1979;

#Neue Anfrage für filme.db
__SQL__ = "SELECT Titel FROM Film WHERE Jahr = 1979"
conn = sqlite3.connect("filme/filme.db")
cur = conn.cursor()
cur.execute(__SQL__)
rows = cur.fetchall()

for row in rows:
    for col in row:
        print(col,end=' ')
    print()


# ![title](anfrageplanung2.jpg)
# <br>
# ![title](anfrageplanung3.jpg)
# <br>
# ![title](anfrageplanung4.jpg)
# 
# ### Materialisierte Sichten
# ■ Viele Anfragen an eine Datenbank wiederholen sich häufig
# <br>
# □ Business Reports, Bilanzen, Umsätze
# <br>
# □ Bestellungsplanung, Produktionsplanung
# <br>
# □ Kennzahlenberechnung
# <br><br>
# ■ Viele Anfragen sind Variationen mit gemeinsamem Kern
# <br><br>
# ■ Idee: Einmaliges Berechnen der Anfrage als Sicht
# <br>
# □ Automatische, transparente Verwendung in folgenden Anfragen
# <br>
# □ Materialisierte Sicht (materialized view, MV)
# <br>
# Drei Folien nach Prof. Ulf Leser, HU Berlin
# 
# #### MV – Themen und Probleme
# ■ Wahl von Views zur Materialisierung
# <br>
# □ MVs kosten: Platz und Aktualisierungsaufwand
# <br>
# □ Wahl der optimalen MVs hängt von Workload ab
# <br>
# □ Auswahl der „optimalen“ Menge von MVs
# <br><br>
# ■ Automatische Aktualisierung von MVs
# <br>
# □ Aktualisierung bei Änderungen der Basisrelationen
# <br>
# □ U.U. schwierig: Aggregate, Joins, Outer-Joins, ...
# <br>
# □ Algorithmen zur inkrementellen Aktualisierung
# <br><br>
# ■ Automatische Verwendung von MV
# <br>
# □ „Answering Queries using Views“
# <br>
# □ Umschreiben der Anfrage notwendig
# <br>
# □ Schwierigkeit hängt von Komplexität der Anfrage / Views ab
# <br>
# □ Algorithmen zur transparenten und kostenoptimalen Verwendung der materialisierten Sichten
# 
# ### „Answering Queries using Views“
# ■ Gegeben
# <br>
# □ Eine Anfrage Q
# <br>
# □ Eine Menge V (materialisierten) von Sichten
# <br><br>
# ■ Fragen
# <br>
# □ Kann man Q überhaupt unter Verwendung von V beantworten?
# <br>
# □ Kann man Q nur mit V beantworten?
# <br>
# □ Kann man Q mit V vollständig beantworten?
# <br>
# □ Ist es günstig, Sichten aus V zur Beantwortung von Q zu verwenden? Welche?
# 
# ## Zusammenfassung
# Die Anfragesprache SQL
# <br>
# Der SFW Block
# <br>
# Subanfragen
# <br>
# In FROM und WHERE
# <br>
# EXISTS, IN, ALL, ANY
# <br>
# Mengenoperationen
# <br>
# UNION, INTERSECT, EXCEPT
# <br>
# Joins und Outerjoins
# <br>
# Nullwerte
# <br>
# Mengen vs. Multimengen
# <br>
# DISTINCT, ALL
# <br>
# Gruppierung und Aggregation
# <br>
# MIN, MAX, COUNT
# <br>
# GROUP BY, HAVING
# <br>
# Datenbankveränderungen
# <br>
# INSERT, UPDATE, DELETE
# <br>
# Schemata und Datentypen
# <br>
# CREATE TABLE
# <br>
# ALTER TABLE
# <br>
# Indizes
# <br>
# Sichten
# <br>
# Anfragen (und updates)
# <br>
# Materialisierte Sichten
