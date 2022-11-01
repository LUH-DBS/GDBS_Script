#!/usr/bin/env python
# coding: utf-8

# # Bearbeitung
# 
# **Anfragebearbeitung – Grundproblem**
# - Anfragen sind deklarativ.
# - SQL, Relationale Algebra
# <br><br>
# - Anfragen müssen in ausführbare (prozedurale) Form transformiert werden.
# - Ziele
# - „QEP“ – prozeduraler Query Execution Plan
# - Effizienz
# - Schnell
# - Wenig Ressourcenverbrauch (CPU, I/O, RAM, Bandbreite)
# - Energie
# 
# **Ablauf der Anfragebearbeitung**
# 1. Parsing
# <br><br>
# Parsen der Anfrage (Syntax) 
# <br>
# Überprüfen der Elemente („Semantik“) 
# <br>
# Parsebaum
# <br><br>
# 2. Wahl des logischen Anfrageplans 
# <br><br>
# Baum mit logischen Operatoren 
# <br>
# Potentiell exponentiell viele 
# <br>
# Wahl des optimalen Plans – Logische Optimierung – Regelbasierter Optimierer – Kostenbasierter Optimierer
# <br><br>
# 3. Wahl des physischen Anfrageplans 
# <br><br>
# Ausführbar 
# <br>
# Programm mit physischen Operatoren – Algorithmen – Scan Operatoren 
# <br>
# Wahl des optimalen Plans – physische Optimierung
# <br><br>
# 
# ![title](ablauf_anfragebearbeitung.jpg)

# ## Parsen der Anfrage
# 
# ### Syntaxanalyse
# - Aufgabe: Umwandlung einer SQL Anfrage in einen Parsebaum.
# - Atome (Blätter)
# - Schlüsselworte
# - Konstanten
# - Namen (Relationen und Attribute)
# - Syntaxzeichen
# - Operatoren
# <br><br>
# - Syntaktische Kategorien
# - Namen für Teilausdrücke einer Anfrage
# 
# ### Eine Grammatik für einen Teil von SQL
# - Anfragen
# - <Anfrage> :: = \<SFW\>
# - <Anfrage> :: = ( <SFW> )
# - Mengenoperatoren fehlen
# <br><br>
# - SFWs
# - <SFW> ::= SELECT <SelListe> FROM <FromListe> WHERE <Bedingung>
# - Gruppierung, Sortierung etc. fehlen
# <br><br>
# - Listen
# - <SelListe> ::= <Attribut>, <SelListe>
# □ <SelListe> ::= <Attribut>
# □ <FromListe> ::= <Relation>, <FromListe>
# □ <FromListe> ::= <Relation>
# <br><br>
# ■ Bedingungen (Beispiele)
# □ <Bedingung> ::= <Bedingung> AND <Bedingung>
# □ <Bedingung> ::= <Tupel> IN <Anfrage>
# □ <Bedingung> ::= <Attribut> = <Attribut>
# □ <Bedingung> ::= <Attribut> LIKE <Muster>
# <br><br>
# ■ <Tupel>, <Attribut>, <Relation>, <Muster> nicht durch grammatische Regel definiert
# <br><br>
# - Vollständig z.B. hier: http://docs.openlinksw.com/virtuoso/GRAMMAR.html
# 
# ### Parse-Baum
# 
# ![](parsebaum.jpg)
# 
# ```
# SELECT Titel
# FROM spielt_in, Schauspieler
# WHERE SchauspielerName = Name
# AND Geburtstag LIKE ‘%1960’;
# ```
# 
# ### Prüfung der Semantik
# - Während der Übersetzung semantische Korrektheit prüfen
# - Existieren die Relationen und Sichten der FROM Klausel?
# - Existieren die Attribute in den genannten Relationen?
# - Sind sie eindeutig?
# - Korrekte Typen für Vergleiche?
# - Aggregation korrekt?
# - ...
# 
# ### Vom Parse-Baum zum Operatorbaum
# 
# ![](operatorbaum.jpg)
# 
# ```
# SELECT Titel
# FROM spielt_in, Schauspieler
# WHERE SchauspielerName = Name
# AND Geburtstag LIKE ‘%1960’;
# ```

# ## Transformationsregeln der RA
# ### Anfragebearbeitung – Transformationsregeln
# - Transformation der internen Darstellung
# - Ohne Semantik zu verändern
# - Zur effizienteren Ausführung
# - Insbesondere: Kleine Zwischenergebnisse
# <br><br>
# - Äquivalente Ausdrücke
# - Zwei Ausdrücke der relationalen Algebra heißen äquivalent, falls
# - Gleiche Operanden (= Relationen)
# - Stets gleiche Antwortrelation
# - Stets?
# <br>
# Für jede mögliche Instanz derDatenbank 
# 
# ### Anfragebearbeitung – Beispiel
# 
# ![](anfragebearbeitung_bsp1.jpg)
# 
# ![](anfragebearbeitung_bsp2.jpg)
# 
# ### Kommutativität und Assoziativität
#  ist kommutativ und assoziativ
# <br>
# R  S = S  R
# <br>
# (R  S)  T = R  (S  T)
# <br><br>
# $\cup$ ist kommutativ und assoziativ
# <br>
# R $\cup$ S = S $\cup$ R
# <br>
# (R $\cup$ S) $\cup$ T = R $\cup$ (S $\cup$ T)
# <br><br>
# $\cap$ ist kommutativ und assoziativ
# <br>
# R $\cap$ S = S $\cap$ R
# <br>
# (R $\cap$ S) $\cap$ T = R $\cap$ (S $\cap$ T)
# <br><br>
# ⋈ ist kommutativ und assoziativ
# <br>
# R ⋈ S = S ⋈ R
# <br>
# (R ⋈ S) ⋈ T = R ⋈ (S ⋈ T)
# <br><br>
# Gilt jeweils für Mengen und Multimengen
# <br><br>
# Ausdrücke können in beide Richtungen verwendet 
# 
# ### Weitere Regeln
# Selektion
# - $\sigma_{c1 AND c2}(R ) = \sigma_{c1}(\sigma_{c2} (R))$
# - $\sigma_{c1 OR c2}(R ) = \sigma_{c1}(R) \cup \sigma_{c2} (R)$
# - Nicht bei Multimengen
# - $\sigma_{c1}(\sigma_{c2}(R)) = \sigma_{c2}(\sigma_{c1}(R))$
# - $\sigma_{c}(R \Phi S) \equiv (\sigma_{c} (R)) \Phi (\sigma_{c} (S))$
# - $\Phi \in \{\cup, \cap , - , ⋈\}$
# - $\sigma_{c}(R \Phi S) \equiv (\sigma_{c} (R)) \Phi S$
# - $\Phi \in \{\cup, \cap , - , ⋈\}$
# - Falls sich c nur auf Attribute in R bezieht
# <br><br>
# Projektion
# - $\pi_{L}(R ⋈ S) = \pi_{L}(\pi_{M}(R) ⋈ \pi_{N}(S))$
# - $\pi_{L}(R ⋈_{C} S) = \pi{L}(\pi_{M}(R) ⋈_{C} \pi_{N}(S))$
# - $\pi_{L}(R \times S) = \pi_{L}(\pi_{M}(R) \times \pi_{N}(S))$
# - $\pi_{L}(\sigma_{C}(R)) = \pi_{L}(\sigma_{C}(\pi_{M}(R)))$
# 

# ## Optimierung
# 
# ### Anfragebearbeitung - Optimierung
# - Regelbasierte Optimierung
# - Fester Regelsatz schreibt Transformationen gemäß der genannten Regeln vor.
# - Prioritäten unter den Regeln: Heuristiken
# <br><br>
# - Kostenbasierte Optimierung
# - Kostenmodell
# - Transformationen um Kosten zu verringern
# - Bestimmung des optimalen Plans
# - Bestimmung der optimalen Joinreihenfolge
# <br><br>
# - Im Allgemeinen wird nicht die optimale Auswertungsstrategie gesucht, sondern eine einigermaßen effiziente Variante.
# - Ziel: Avoid the worst case.
# 
# ### Logische und physische Optimierung
# - Logische Optimierung
# - Jeder Ausdruck kann in viele verschiedene, semantisch äquivalente Ausdrücke umgeschrieben werden.
# - Wähle den (hoffentlich) besten Ausdruck (=Plan, =QEP)
# <br><br>
# - Physische Optimierung
# - Für jede relationale Operation gibt es viele verschiedene Implementierungen.
# - Zugriff auf Tabellen
# - Scan, verschiedene Indizes, sortierter Zugriff, …
# - Joins
# - Nested loop, sort-merge, hash, …
# - Wähle für jede Operation die (hoffentlich) beste Implementierung
# <br><br>
# - Abhängigkeit beider Probleme!
# 
# ### Logische Optimierung – regelbasiert
# - Grundsätze der logischen Optimierung
# - Selektionen so weit wie möglich im Baum nach unten schieben.
# - Selektionen mit AND können aufgeteilt und separat verschoben werden.
# - Projektionen so weit wie möglich im Baum nach unten schieben,
# - bzw. neue Projektionen können eingefügt werden.
# - Duplikateliminierung kann manchmal entfernt werden oder verschoben werden.
# - Kreuzprodukte mit geeigneten Selektionen zu einem Join zusammenfassen.
# <br><br>
# - Noch nicht hier: Suche nach der optimalen Joinreihenfolge
# <br><br>
# Folie: Prof. Alfons Kemper, TU München
# 
# ### Anwendung der Transformationsregeln
# ```
# select distinct s.Semester
# from Studiernden s, hören h
# Vorlesungen v,
# Professorinnen p
# where p.Name = ´Sokrates´
# and v.gelesenVon = p.PersNr
# and v.VorlNr = h.VorlNr
# and h.MatrNr = s.MatrNr
# ```
# In welchen Semestern sind die Studierenden, die Vorlesungen bei Sokrates hören?
# 
# ![](transformationsregeln.jpg)
# 
# ### Aufspalten der Selektionsprädikate
# 
# ![](aufspalten_selektionspraedikate.jpg)
# 
# ### Verschieben der Selektionsprädikate „Pushing Selections“
# 
# ![](verschieben_selektionspraedikate.jpg)
# 
# ### Zusammenfassung von Selektionen und Kreuzprodukten zu Joins
# 
# ![](zusammenfassen_selektionspraedikate.jpg)
# 
# ### Optimierung der Joinreihenfolge: Kommutativität und Assoziativität ausnutzen
# 
# ![](joinreihenfolge1.jpg)
# 
# ### Was hat´s gebracht?
# 
# ![](joinreihenfolge2.jpg)
# 
# ### Einfügen von Projektionen
# 
# ![](einfuegen_projektion.jpg)
# 
# ### SQLite Explain
# 
# ![](sqlite.jpg)

# ## Kostenmodelle
# 
# ### Kostenbasierte Optimierung
# - Konzeptionell: Generiere alle denkbaren Anfrageausführungspläne.
# <br><br>
# - Bewerte deren Kosten anhand eines Kostenmodells
# - Statistiken und Histogramme
# - Kalibrierung gemäß verwendeter Rechner
# - Abhängig vom verfügbaren Speicher
# - Aufwands-Kostenmodell
# - Durchsatz-maximierend
# - Nicht Antwortzeit-minimierend
# <br>
# Achtung: Nicht zu lange optimieren!
# <br><br>
# - Führe billigsten Plan aus
# 
# ### Problemgröße (Suchraum)
# - Konzeptionell: Generiere alle denkbaren Anfrageausführungspläne
# - Anzahl Bushy-Pläne mit n Tabellen
# - $\frac{(2(n-1))!}{(n-1)!}$
# 
# 
# |n|$2^n$|(2(n-1))!/(n-1)!|
# |---|---|---|
# |2|4|2|
# |5|32|1680|
# |10|1024|1,76 $\times 10^{10}$|
# |20|1.048.576|$4,3\times10^{27}$|
# 
# 
# 
# - Plankosten unterscheiden sich um viele Größenordnungen.
# - Optimierungsproblem ist NP-hart
# 
# ### Kostenmodell
# 
# ![](kostenmodell.jpg)
# 
# 
# ### Statistiken
# - Zu jeder Basisrelation
# - Anzahl der Tupel
# - Tupelgröße
# <br><br>
# - Zu (jedem) Attribut
# - Min / Max
# - Werteverteilung (Histogramm)
# - Anzahl der distinct Werte
# - Oft: „Kardinalität“
# <br><br>
# - Zum System
# - Speichergröße
# - Bandbreite
# - I/O Zeiten
# - CPU Zeiten
# <br><br>
# - Problem: Erstellung und Update der Statistiken
# - Deshalb meist nur explizit/manuell zu initiieren
# - runstats()
# <br><br>
# ![](statistik.jpg)
# 
# ### Kosten von Operationen
# - Projektion:
# - Keine Kosten falls mit anderem Operator kombiniert
# <br><br>
# - Selektion
# - Ohne Index: Gesamte Relation von Festplatte lesen
# - Mit Baum-Index (z.B. B-Baum): Teil des Index von Platte lesen (Baumtiefe) und gesuchte Seite von Platte lesen
# - Bei Pipelining: (Fast) keine Kosten
# <br><br>
# - Join
# - Je nach Joinalgorithmus
# - Nested Loops, Hash-Join, Sort-Merge Join, usw.
# <br><br>
# - Sortierung: Nicht hier
# <br><br>
# - Wesentliches Kostenmerkmal: Anzahl der Tupel im Input
# - Insbesondere: Passt die Relation in den Hauptspeicher?
# - Selektion, Projektion, Sortierung, Join
# <br><br>
# - Output ist Input des nächsten Operators.
# <br><br>
# - Deshalb: Ein Kostenmodel schätzt u.a. für jede Operation die Anzahl der Ausgabetupel.
# - „Selektivität“ in Bezug auf Inputgröße
# - #Ausgabetupel = #Eingabetupel x Selektivität
# - Auch „Selektivitätsfaktor“ (selectivity factor, sf)
# 
# ### Selektivität
# - Selektivität schätzt Anzahl der qualifizierenden Tupel relativ zur Gesamtanzahl der Tupel in der Input Relation.
# <br><br>
# - Projektion:
# - sf = |R|/|R| = 1
# <br><br>
# - Selektion:
# - sf = |$\sigma_c$(R)| / |R|
# <br><br>
# - Join:
# - sf = |R ⋈ S| / |R x S| = |R ⋈ S| / (|R| · |S|)
# 
# #### Selektivität schätzen
# - Selektion:
# - Selektion auf einen Schlüssel:
# - sf = 1 / |R|
# - Selektion auf einen Attribut A mit m verschiedenen Werten:
# - sf = (|R| / m) / |R| = 1/m
# - Dies ist nur geschätzt!
# <br><br>
# - Join
# - Equijoin zwischen R und S über Fremdschlüssel in S
# - sf = 1 / |R|
# - „Beweis“: sf = |R ⋈ S| / (|R x S|) = |S| / (|R| · |S|)
# 
# ### Selinger-style“ Optimization
# 
# ![](selinger_style1.jpg)
# 
# ![](selinger_style2.jpg)
# 
# ### Join Selektivität (Selinger Style)
# ![](selinger_style3.jpg)
# <br>
# Beispiel
# - SELECT * FROM cust, order WHERE cust.ID = order.custID
# - DISTINCT cust.ID = |cust|
# - DISTINCT order.custID ≤ |cust|
# - sf = 1/|cust|
# - |cust ⋈ order| = 1/|cust| * |cust| * |order| = |order|
# 
# ### Modelle zum besseren Schätzen der Selektivität
# - Gleichverteilung der Werte
# - Platzsparend (count, max, min), einfach
# - Schlechte Abschätzung bei “skew” (ungleiche Verteilung)
# <br><br>
# - Histogramme (Beispiel gleich)
# - Parametrisierte Größe, einfach
# - Güte der Abschätzung hängt von Histogrammtyp und -größe ab.
# - Außerdem: Aktualität garantieren ist aufwändig.
# <br><br>
# - Sampling
# - Repräsentative Teilmenge der Relation
# - Parametrisierte Größe, schwierig zu finden
# - Güte hängt von Samplingmethode und Samplegröße ab
# - Außerdem: Aktualität
# 
# ### Beispiel zu Histogrammen
# ```
# SELECT *
# FROM product p, sales S
# WHERE p.id=s.p_id and
# p.price > 100 
# ```
# - Gegeben 3300 products, 1M sales
# - Gleichverteilung
# - Preisspanne ist 0-1000 => Selektivität der Bedingung ist 9/10
# - Erwartet: 9/10*3300 ≈ 3000 Produkte
# - Histogramm-basiert
# - Selektivität der Bedingung ist 5/3300 ≈ 0,0015 also 5 Produkte
# 
# ![](histogramm.jpg)

# ### Kosten – Weitere Komplikationen
# - Parallelität / Pipelining
# - Kosten aller Operatoren können nicht addiert werden.
# <br><br>
# - Hauptspeichergröße
# - Pufferung und Caching
# <br><br>
# - I/O Kosten (Lesen einer Seite) vs. CPU Kosten
# <br><br>
# - Multiuser: Durchsatz statt Antwortzeit
# <br><br>
# - => Kostenmodelle sind hochkomplex
# 
# ### Ausblick auf DBS II
# - Diverse Algorithmen für einzelne Operatoren
# - Insbesondere Join und Sortierung
# - Kostenmodelle/Kostenschätzung genauer
# - Optimale Joinreihenfolge: Dynamische Programmierung
# - Physische Anfragepläne / Pipelining
# 
# ![](ausblick.jpg)

# ## Multiple Choice

# In[1]:


from IPython.display import IFrame

url = "https://lejuliennn.github.io/mct-trainer/#/quiz/categories/bearbeitung"
IFrame(src=url, width='100%', height=800)


# In[ ]:




