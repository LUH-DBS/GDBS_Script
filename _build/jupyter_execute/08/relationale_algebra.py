#!/usr/bin/env python
# coding: utf-8

# # Relationale Algebra

# ## Einführung

# ■ Bisher
# <br>
# □ Relationenschemata mit Basisrelationen, die in der Datenbank gespeichert sind
# <br><br>
# ■ Jetzt
# <br>
# □ „Abgeleitete“ Relationenschemata mit virtuellen Relationen, die aus den Basisrelationen berechnet werden
# <br>
# □ Definiert durch Anfragen
# <br>
# – Anfragesprache
# <br>
# □ Basisrelationen bleiben unverändert

# ### Kriterien für Anfragesprachen

# ■ Ad-Hoc-Formulierung
# <br>
# □ Benutzer soll eine Anfrage formulieren können, ohne ein vollständiges Programm schreiben zu müssen.
# <br><br>
# ■ Eingeschränktheit
# <br>
# □ Anfragesprache soll keine komplette Programmiersprache sein
# <br>
# – Aber: SQL Standard besteht aus >1300 Seiten…
# <br><br>
# ■ Deskriptivität / Deklarativität
# <br>
# □ Benutzer soll formulieren „Was will ich haben?“ und nicht „Wie komme ich an das, was ich haben will?“
# <br><br>
# ■ Optimierbarkeit
# <br>
# □ Sprache besteht aus wenigen Operationen
# <br>
# □ Optimierungsregeln für die Operatorenmenge
# <br><br>
# ■ Effizienz
# <br>
# □ Jede einzelne Operation ist effizient ausführbar.
# <br>
# □ Im relationalen Modell hat jede Operation eine Komplexität ≤ O(n²)
# <br>
# – n = Anzahl der Tupel einer Relation
# <br><br>
# ■ Abgeschlossenheit
# <br>
# □ Anfragen auf Relationen
# <br>
# □ Anfrageergebnis ist wiederum eine Relation und kann als Eingabe für die nächste Anfrage verwendet werden.
# <br><br>
# ■ Mengenorientiertheit
# <br>
# □ Operationen auf Mengen von Daten
# <br>
# □ Nicht navigierend nur auf einzelnen Elementen („tuple-at-a-time“)
# <br><br>
# ■ Adäquatheit
# <br>
# □ Alle Konstrukte des zugrundeliegenden Datenmodells werden unterstützt
# <br>
# □ Relationen, Attribute, Schlüssel, …
# <br><br>
# ■ Vollständigkeit
# <br>
# □ Sprache muss mindestens die Anfragen einer Standardsprache (z.B. relationale Algebra) ausdrücken können.
# <br>
# □ Relationale Algebra dient als Vorgabe.
# <br><br>
# ■ Sicherheit
# <br>
# □ Keine Anfrage, die syntaktisch korrekt ist, darf in eine Endlosschleife geraten oder ein unendliches Ergebnis
# liefern.

# ### Anfragealgebra

# ■ Mathematik
# <br>
# □ Algebra: Definiert durch Wertebereich und auf diesem definierte Operatoren
# <br>
# □ Operand: Variablen oder Werte aus denen neue Werte konstruiert werden können
# <br>
# □ Operator: Symbole, die Prozeduren repräsentieren, die aus gegebenen Werten neue Werte produzieren
# <br><br>
# ■ Für Datenbankanfragen
# <br>
# □ Inhalte der Datenbank (Relationen) sind Operanden
# <br>
# □ Operatoren definieren Funktionen zum Berechnen von Anfrageergebnissen
# <br>
# – Grundlegenden Dinge, die wir mit Relationen tun wollen.
# <br>
# □ Relationale Algebra (Relational Algebra, RA)
# <br>
# – Anfragesprache für das relationale Modell

# ### Mengen vs. Multimengen

#  Relation: Menge von Tupeln
# <br>
# ■ Datenbanktabelle: Multimenge von Tupeln
# <br>
# □ Engl: „bag“
# <br><br>
# ■ Operatoren der relationalen Algebra: Operatoren auf Mengen
# <br><br>
# ■ Operatoren auf DBMS: SQL Anfragen
# <br>
# □ Rel. DBMS speichern Multimengen
# <br><br>
# ■ Motivation: Effizienzsteigerung
# <br>
# □ Beispiel:
# <br>
# – Vereinigung als Multimenge
# <br>
# – Vereinigung als Menge

# ## Basisoperatoren

# ## Klassifikation der Operatoren

# ■ Mengenoperatoren 
# <br>
# □ Vereinigung, Schnittmenge, Differenz 
# <br><br>
# ■ Entfernende Operatoren
# <br>
# □ Selektion, Projektion
# <br><br>
# ■ Kombinierende Operatoren 
# <br>
# □ Kartesisches Produkt, Join, Joinvarianten 
# <br><br>
# ■ Umbenennung 
# <br>
# □ Verändert nicht Tupel, sondern Schema 
# <br><br>
# ■ Ausdrücke der relationalen Algebra 
# <br>
# □ Kombination von Operatoren und Operanden 
# <br>
# □ „Anfragen“ (queries)

# ## Vereinigung (union, $\cup$)

# ■ Sammelt Elemente (Tupel) zweier Relationen unter einem gemeinsamen Schema auf.
# <br>
# □ R ∪ S := {t | t $\in$ R $\vee$ t $\in$ S}
# <br><br>
# ■ Attributmengen beider Relationen müssen identisch sein.
# <br>
# □ Namen, Typen und Reihenfolge
# <br>
# □ Zur Not: Umbenennung
# <br><br>
# ■ Ein Element ist nur einmal in (R ∪ S) vertreten, auch wenn es jeweils einmal in R und S auftaucht.
# <br>
# □ Duplikatentfernung

# ## Beispiel für Mengenoperatoren

# $R$
# 
# |Name|Adresse|Geschlecht|Geburt|
# |----|-------|----------|------|
# |Carrie Fisher|123 Maple St., Hollywood|F|9/9/99|
# |Mark Hamill|456 Oak. Rd., Brentwood|M|8/8/88|

# $S$
# 
# |Name|Adresse|Geschlecht|Geburt|
# |----|-------|----------|------|
# |Carrie Fisher|123 Maple St., Hollywood|F|9/9/99|
# |Harrison Ford|789 Palm Dr., Beverly Hills|M|7/7/77|

# $R \cup S$
# 
# |Name|Adresse|Geschlecht|Geburt|
# |----|-------|----------|------|
# |Carrie Fisher|123 Maple St., Hollywood|F|9/9/99|
# |Mark Hamill|456 Oak. Rd., Brentwood|M|8/8/88|
# |Harrison Ford|789 Palm Dr., Beverly Hills|M|7/7/77|

# ## Differenz (difference, ―, \\)

# ■ Differenz R − S eliminiert die Tupel aus der ersten Relation, die auch in der zweiten Relation vorkommen.
# <br>
# □ R − S := {t | t $\in$ R $\wedge$ t $\notin$ S}
# <br><br>
# ■ Achtung: Schemata von R und S müssen gleich sein.
# <br><br>
# ■ Achtung: R − S ≠ S − R
# <br>
# □ D.h. Kommuntativität gilt nicht

# ## Beispiel für Mengenoperatoren

# $R$
# 
# |Name|Adresse|Geschlecht|Geburt|
# |----|-------|----------|------|
# |Carrie Fisher|123 Maple St., Hollywood|F|9/9/99|
# |Mark Hamill|456 Oak. Rd., Brentwood|M|8/8/88|

# $S$
# 
# |Name|Adresse|Geschlecht|Geburt|
# |----|-------|----------|------|
# |Carrie Fisher|123 Maple St., Hollywood|F|9/9/99|
# |Harrison Ford|789 Palm Dr., Beverly Hills|M|7/7/77|

# $R-S$
# 
# |Name|Adresse|Geschlecht|Geburt|
# |----|-------|----------|------|
# |Mark Hamill|456 Oak. Rd., Brentwood|M|8/8/88|

# ## Schnittmenge (intersection, $\cap$)

#  Schnittmenge R $\cap$ S ergibt die Tupel, die in beiden Relationen gemeinsam vorkommen.
#  <br> <br>
# ■ R $\cap$ S := {t | t $\in$ R $\wedge$ t $\in$ S}
#  <br> <br>
# ■ Anmerkung: Schnittmenge ist „überflüssig“. Warum?
#  <br>
# □ R $\cap$ S = R − (R − S)
#  <br>
# = S − (S − R)

# ![title](schnittmenge.jpg)

# ## Beispiel für Mengenoperatoren

# $R$
# 
# |Name|Adresse|Geschlecht|Geburt|
# |----|-------|----------|------|
# |Carrie Fisher|123 Maple St., Hollywood|F|9/9/99|
# |Mark Hamill|456 Oak. Rd., Brentwood|M|8/8/88|

# $S$
# 
# |Name|Adresse|Geschlecht|Geburt|
# |----|-------|----------|------|
# |Carrie Fisher|123 Maple St., Hollywood|F|9/9/99|
# |Harrison Ford|789 Palm Dr., Beverly Hills|M|7/7/77|

# $R\cap S$
# 
# |Name|Adresse|Geschlecht|Geburt|
# |----|-------|----------|------|
# |Carrie Fisher|123 Maple St., Hollywood|F|9/9/99|

# ## Projektion (projection, $\pi$)

# ■ Unärer Operator
# <br><br>
# ■ Erzeugt neue Relation mit einer Teilmenge der ursprünglichen Attribute
# <br><br>
# ■ $\pi_{A1,A2,…,Ak}$(R) ist eine Relation
# <br>
# □ mit den Attributen A1,A2,…,Ak
# <br>
# □ Üblicherweise in der aufgelisteten Reihenfolge
# <br><br>
# ■ Achtung: Es können Duplikate entstehen, die implizit entfernt werden.

# ## Projektion – Beispiel

# Film
# 
# |Titel|Jahr|Länge|inFarbe|Studio|ProduzentID|
# |-----|----|-----|-------|------|---------|
# |Total Recall|1990|113|True|Fox|12345|
# |Basic Instinct|1992|127|True|Disney|67890|
# |Dead Man|1995|121|False|Paramount|99999|

# $\pi_{Titel,Jahr,Länge}$(Film)
# 
# |Titel|Jahr|Länge|
# |-----|----|-----|
# |Total Recall|1990|113|
# |Basic Instinct|1992|127|
# |Dead Man|1995|121|False|

# $\pi_{inFarbe}$(Film)
# 
# |inFarbe|
# |-------|
# |True|
# |False|

# ## Erweiterte Projektion

# ■ Motivation: Dem Projektionsoperator mehr Fähigkeiten geben
# <br><br>
# ■ Vorher: $\pi_{L}$(R) wobei L eine Attributliste ist
# <br><br>
# ■ Nun: Ein Element von L ist eines dieser drei Ausdrücke
# <br><br>
# 1. Ein Attribut von R (wie zuvor)
# <br>
# 2. Ein Ausdruck A→B wobei A ein Attribut in R ist und B ein neuer Name ist (Umbennennung).
# <br>
# 3. Ein Ausdruck e→C, wobei e ein Ausdruck mit Konstanten, arithmetischen Operatoren, Attributen von R und
# String-Operationen ist, und C ein neuer Name ist.
# <br>
# 1. A1 + A2 → Summe
# <br>
# 2. Vorname || \` \` || Nachname → Name

# ## Selektion (selection, $\sigma$)

# ■ Unärer Operator
# <br><br>
# ■ Erzeugt neue Relation mit gleichem Schema aber einer Teilmenge der Tupel.
# <br><br>
# ■ Nur Tupel, die der Selektionsbedingung C (condition) entsprechen.
# <br>
# □ Selektionsbedingung wie aus Programmiersprachen
# <br>
# □ Operanden der Selektionsbedingung sind nur Konstanten oder Attribute von R.
# <br>
# – const = const (eigentlich unnötig)
# <br>
# – attr = const (typische Selektion)
# <br>
# – attr = attr (Join Bedingung)
# <br>
# □ Weitere Vergleiche: <, >, ≤, $\ge$, <>
# <br>
# □ Kombination durch AND, OR und NOT
# <br><br>
# ■ Prüfe Bedingung für jedes Tupel
# <br><br>
# Achtung Selektion $\neq$ SELECT

# ## Selektion – Beispiel

# Film
# 
# |Titel|Jahr|Länge|inFarbe|Studio|ProduzentID|
# |-----|----|-----|-------|------|---------|
# |Total Recall|1990|113|True|Fox|12345|
# |Basic Instinct|1992|127|True|Disney|67890|
# |Dead Man|1995|90|False|Paramount|99999|

# $\sigma_{Länge\geq100}$(Film)
# 
# |Titel|Jahr|Länge|inFarbe|Studio|ProduzentID|
# |-----|----|-----|-------|------|---------|
# |Total Recall|1990|113|True|Fox|12345|
# |Basic Instinct|1992|127|True|Disney|67890|

# $\sigma_{Länge\geq100 AND Studio='Fox'}$(Film)
# 
# |Titel|Jahr|Länge|inFarbe|Studio|ProduzentID|
# |-----|----|-----|-------|------|---------|
# |Total Recall|1990|113|True|Fox|12345|

# ## Kartesisches Produkt (Cartesian product, cross product $\times$)

# ■ Binärer Operator
# <br><br>
# ■ Auch: Kreuzprodukt oder Produkt
# <br><br>
# ■ Auch: R * S statt R $\times$ S
# <br><br>
# ■ Kreuzprodukt zweier Relationen R und S ist die Menge aller Tupel, die man erhält, wenn man jedes Tupel aus R
# mit jedem Tupel aus S „paart“.
# <br><br>
# ■ Schema hat ein Attribut für jedes Attribut aus R und S
# <br>
# □ Achtung: Bei Namensgleichheit wird kein Attribut ausgelassen
# <br>
# □ Stattdessen: Umbenennen

# ![title](descartes.jpg)

# ## Kartesisches Produkt – Beispiel

# $R$
# 
# |A|B|
# |-|-|
# |1|2|
# |3|4|

# $S$
# 
# |B|C|D|
# |-|-|-|
# |2|5|6|
# |4|7|8|
# |9|10|11|

# $R \times S$
# 
# |A|R.B|S.B|C|D|
# |-|--|--|-|-|
# |1|2|2|5|6|
# |1|2|4|7|8|
# |1|2|9|10|11|
# |3|4|2|5|6|
# |3|4|4|7|8|
# |3|4|9|10|11|

# ## Der Join – Operatorfamilie

# ■ Natürlicher Join (natural join)
# <br><br>
# ■ Theta-Join
# <br><br>
# ■ Equi-Join
# <br><br>
# ■ Semi-Join und Anti-Join
# <br><br>
# ■ Left-outer Join und Right-outer Join
# <br><br>
# ■ Full-outer Join

# ### Natürlicher Join (natural join, ⋈)

# ■ Binärer Operator
# <br><br>
# ■ Motivation: Statt im Kreuzprodukt alle Paare zu bilden, sollen nur die Tupelpaare gebildet werden, deren Tupel
# „irgendwie“ übereinstimmen.
# <br>
# □ Auch: „Verbund“
# <br>
# □ Beim natürlichen Join: Übereinstimmung in allen gemeinsamen Attributen.
# <br>
# □ Gegebenenfalls Umbenennung
# <br>
# □ Schema: Vereinigung der beiden Attributmengen

# ![title](njoin.jpg)

# ■ Notation: r[A] sei Projektion der Tupels r auf Attribut A
# <br><br>
# ■ Seien A1,…,Ak die gemeinsamen Attribute von R und S
# <br><br>
# ■ R ⋈ S = {r $\cup$ s | r$\in$R $\wedge$ s$\in$S $\wedge$ r[A1]=s[A1] $\wedge$ … $\wedge$ r[Ak]=s[Ak] }
# <br><br>
# ■ Alternative, üblichere Definition
# <br>
# □ R ⋈ S = s r[A1]=s[A1] $\wedge$ … $\wedge$ r[Ak]=s[Ak](R × S)
# <br>
# □ Achtung: Eigentlich noch ordentlich projizieren

# ### Natürlicher Join – Beispiel

# $R$
# 
# |A|B|
# |-|-|
# |1|2|
# |3|4|

# $S$
# 
# |B|C|D|
# |-|-|-|
# |2|5|6|
# |4|7|8|
# |9|10|11|

# $R ⋈ S$
# 
# |A|B|C|D|
# |-|-|-|-|
# |1|2|5|6|
# |3|4|7|8|

# $R \times S$
# 
# |A|R.B|S.B|C|D|
# |---|---|---|---|---|
# |1|2|2|5|6|
# |1|2|4|7|8|
# |1|2|9|10|11|
# |3|4|2|5|6|
# |3|4|4|7|8|
# |3|4|9|10|11|

# $R$
# 
# |A|B|C|
# |-|-|-|
# |1|2|3|
# |6|7|8|
# |9|7|8|

# $S$
# 
# |B|C|D|
# |-|-|-|
# |2|5|6|
# |2|3|5|
# |7|8|10|

# $R ⋈ S$
# 
# |A|B|C|D|
# |-|-|-|-|
# |1|2|3|5|
# |6|7|8|10|
# |9|7|8|10|

# ■ Anmerkungen
# <br>
# □ Mehr als ein gemeinsames Attribut
# <br>
# □ Tupel werden mit mehr als einem Partner verknüpft

# ### Theta-Join (theta-join, $⋈_\theta$)

# ■ Verallgemeinerung des natürlichen Joins
# <br><br>
# ■ Verknüpfungsbedingung kann selbst gestaltet werden
# <br><br>
# ■ Konstruktion des Ergebnisses:
# <br>
# □ Bilde Kreuzprodukt der beiden Relationen
# <br>
# □ Selektiere mittels der gegebenen Joinbedingung
# <br>
# □ Also: R ⋈$A_\theta$ B S = s $A_\theta$ B (R $\times$ S)
# <br>
# □ $\theta$ ∈ {=, <, >, ≤, ≥, ≠}
# <br>
# □ A ist Attribut in R; B ist Attribut in S
# <br><br>
# ■ Schema: Wie beim Kreuzprodukt
# <br><br>
# ■ Equi-Join ist ein Spezialfall des Theta-Joins mit Operator „=“
# <br><br>
# ■ Natural Join ist ein Spezialfall des Theta-Joins
# <br>
# □ Aber: Schema des Ergebnisses sieht anders aus.
# <br>
# □ R(A,B,C) ⋈ S(B,C,D) = $\rho_{T(A,B,C,D)}$($\pi_{A,R.B,R.C,D}$($\sigma_{(R.B=S.B AND R.C = S.C)}$ ($R \times S$)))
# <br>
# ->Umbenennung

# ### Theta-Join – Beispiel

# $R$
# 
# |A|B|C|
# |-|-|-|
# |1|2|3|
# |6|7|8|
# |9|7|8|

# $S$
# 
# |B|C|D|
# |-|-|-|
# |2|5|6|
# |2|3|5|
# |7|8|10|

# $R ⋈_{A<D}S$
# 
# |A|R.B|R.C|S.B|S.C|D|
# |-|--|--|--|--|-|
# |1|2|3|2|5|6|
# |1|2|3|2|3|5|
# |1|2|3|7|8|10|
# |6|7|8|7|8|10|
# |9|7|8|7|8|10|

# $R ⋈_{A<D \wedge R.B \neq S.B}S$
# 
# |A|R.B|R.C|S.B|S.C|D|
# |-|--|--|--|--|-|
# |1|2|3|7|8|10|

# ### Komplexe Ausdrücke

# ■ Idee: Kombination (Schachtelung) von Ausdrücken zur Formulierung komplexer Anfragen.
# <br>
# □ Abgeschlossenheit der relationalen Algebra
# <br>
# – Output eines Ausdrucks ist immer eine Relation.
# <br><br>
# □ Darstellung
# <br>
# – Als geschachtelter Ausdruck mittels Klammerung
# <br>
# – Als Baum

# Film
# 
# |Titel|Jahr|Länge|Typ|StudioName|
# |-----|----|-----|---|----------|
# |Total Recall|1990|113|Farbe|Fox|
# |Basic Instinct|1992|127|Farbe|Disney|
# |Dead Man|1995|90|s/w|Paramount|

# ■ Gesucht: Titel und Jahr von Filmen, die von Fox produziert wurden und mindestens 100
# Minuten lang sind.
# <br>
# □ Suche alle Filme von Fox
# <br>
# □ Suche alle Filme mit mindestens 100 Minuten
# <br>
# □ Bilde die Schnittmenge der beiden Zwischenergebnisse
# <br>
# □ Projiziere die Relation auf die Attribute Titel und Jahr.
# <br>
# □ $\rho_{Titel,Jahr}$($\sigma_{Länge≥100}$(Film) $\cap$ $\sigma_{StudioName=‚Fox‘}$(Film))
# <br>
# □ Alternative: $\pi_{Titel,Jahr}$($\sigma_{Länge≥100 AND StudioName=‚Fox‘}$(Film))
# <br>
# – U.v.a.m.

# ### Komplexe Ausdrücke – Beispiel

# ■$\rho_{Titel,Jahr}$($\sigma_{Länge≥100(Film)}$ $\cap$ $\sigma_{StudioName=‚Fox‘}$(Film))

# ![title](komplex_bsp1.jpg)

# ■ Alternative: $\rho_{Titel,Jahr}$($\sigma_{Länge≥100 AND StudioName=‚Fox‘}$(Film))

# ### Komplexe Ausdrücke – Beispiel

# Film
# 
# |Titel|Jahr|Länge|Typ|StudioName|
# |-----|----|-----|---|----------|
# |Total Recall|1990|113|Farbe|Fox|
# |Basic Instinct|1992|127|Farbe|Disney|
# |Dead Man|1995|90|s/w|Paramount|

# Rolle
# 
# |Titel|Jahr|SchauspName|
# |-----|----|-----------|
# |Total Recall|1990|Sharon Stone|
# |Basic Instinct|1992|Sharon Stone|
# |Total Recall|1990|Arnold|
# |Dead Man|1995|Johnny Depp|

# ■ Gesucht: Namen aller Schauspieler, die in Filmen spielten, die mindestens 100 Minuten lang
# sind.
# <br>
# □ Verjoine beide Relationen (natürlicher Join)
# <br>
# □ Selektiere Filme, die mindestens 100 Minuten lang sind.
# <br>
# □ $\rho_{SchauspName}$($\sigma_{Länge≥100}$(Film ⋈ Rolle))

# ■ Stud(Matrikel, Name, Semester)
# <br>
# ■ Prof(ProfName, Fachgebiet, GebJahr)
# <br>
# ■ VL(VL_ID, Titel, Saal)
# <br>
# ■ Lehrt(ProfName, VL_ID)
# <br>
# ■ Hört(Matrikel,VL_ID)
# <br>
# ■ Gesucht: Unterschiedliche Semester aller Studierenden, die eine Vorlesung eines Professors des Jahrgangs 1960
# in Hörsaal 1 hören.
# <br>
# ■ $\rho_{Sem}$((($\sigma_{Saal=1}$((($\sigma_{GebJahr = 1960}$(Professor))⋈Lehrt)⋈VL)⋈Hört)⋈Stud))

# ### Umbenennung (rename, $\rho$)

# ■ Unärer Operator
# <br>
# <br>
# ■ Motivation: Zur Kontrolle der Schemata und einfacheren Verknüpfungen
# <br>
# □ $\rho_{S(A1,…,An)}$(R)
# <br>
# – Benennt Relation R in S um
# <br>
# – Benennt die Attribute der neuen Relation A1,…,An
# <br>
# □ $\rho_{S(R)}$ benennt nur Relation um.
# <br>
# ■ Durch Umbenennung ermöglicht
# <br>
# □ Mengenoperationen
# <br>
# – Nur möglich bei gleichen Schemata
# <br>
# □ Joins, wo bisher kartesische Produkte ausgeführt wurde
# <br>
# – Unterschiedliche Attribute werden gleich benannt.
# <br>
# □ Kartesische Produkte, wo bisher Joins ausgeführt wurden
# <br>
# – Gleiche Attribute werden unterschiedlich genannt.

# ### Umbenennung – Beispiel

# $R$
# 
# |A|B|
# |-|-|
# |1|2|
# |3|4|

# $S$
# 
# |B|C|D|
# |-|-|-|
# |2|5|6|
# |4|7|8|
# |9|10|11

# $R \times \rho_{s(X,C,D)}(S)$
# 
# |A|B|X|C|D|
# |-|-|-|-|-|
# |1|2|2|5|6|
# |1|2|4|7|8|
# |1|2|9|10|11
# |3|4|2|5|6|
# |3|4|4|7|8|
# |3|4|9|10|11

# ■ Alternativer Ausdruck: $\rho_{S(A,B,X,C,D)}$(R $\times$ S)

# ### Unabhängigkeit und Vollständigkeit

#  Minimale Relationenalgebra:
#  <br>
# □ π, σ, $\times$ , −, ∪ (und r)
#  <br>
# ■ Unabhängig:
#  <br>
# □ Kein Operator kann weggelassen werden ohne Vollständigkeit zu verlieren.
#  <br> <br>
# ■ Natural Join, Join und Schnittmenge sind redundant
#  <br>
# □ R $\cap$ S = R − (R − S)
#  <br>
# □ R ⋈C S = $\sigma_C$(R $\times$ S) 
#  <br>
# □ R ⋈ S = $\pi_{L}$($\sigma_{R.A1=S.A1 AND … AND R.An=S.An}$(R $\times$ S))

# ## Vorschau zu Optimierung

# ■ Beispiele für algebraische Regeln zur Transformation
# <br>
# □ R ⋈ S = S ⋈ R
# <br>
# □ (R ⋈ S) ⋈ T = R ⋈ (S ⋈ T)
# <br>
# □ $\rho_{Y}(\rho_{X}(R)) = \rho_{Y}(R)$
# <br>
# – Falls Y ⊆ X
# <br>
# □ $\sigma_{A=a}(\sigma_{B=b}(R))= \sigma_{B=b}(\sigma_{A=a}(R)) [ = \sigma_{B=b\wedge A=a}(R) ]$
# <br>
# □ $\pi_{X}(\sigma_{A=a}(R)) = \sigma_{A=a}(\pi_{X}(R))$
# <br>
# – Falls A ⊆ X
# <br>
# □ $\sigma_{A=a}(R ∪ S) = \sigma_{A=a}(R) ∪ \sigma_{A=a}(S)$
# <br>
# ■ Jeweils: Welche Seite ist besser?

# ## Operatoren auf Multimengen

# ### Motivation

#  Mengen sind ein natürliches Konstrukt
#  <br>
# □ Keine Duplikate
#  <br> <br>
# ■ Kommerzielle DBMS basieren fast nie nur auf Mengen
#  <br>
# □ Sondern erlauben Multimengen
#  <br>
# □ D.h. Duplikate sind erlaubt
#  <br> <br>
# ■ Multimenge
#  <br>
# □ bag, multiset 

# |A|B|
# |-|-|
# |1|2|
# |3|4|
# |1|2|
# |1|2|
# 
# Multimenge
# <br>
# Reihenfolge ist weiter unwichtig

# ### Effizienz durch Multimengen

# ■ Bei Vereinigung
# <br>
# □ Direkt „aneinanderhängen“
# <br><br>
# ■ Bei Projektion
# <br>
# □ Einfach Attributwerte „abschneiden“
# <br><br>
# ■ Nach Duplikaten suchen
# <br>
# □ Jedes Tupel im Ergebnis mit jedem anderen vergleichen
# <br>
# □ O(n²)
# <br><br>
# ■ Effizienter nach Duplikaten suchen
# <br>
# □ Nach allen Attributen zugleich sortieren: O(n log n)
# <br><br>
# ■ Bei Aggregation
# <br>
# □ Duplikateliminierung sogar schädlich bzw. unintuitiv
# <br>
# □ AVG(A) = ?

# Projektion auf (A,B)
# 
# |A|B|C|
# |-|-|-|
# |1|2|5|
# |3|4|6|
# |1|2|7|
# |1|2|8|

# ### Vereinigung auf Multimengen

#  Sei R eine Multimenge
#  <br>
# □ Tupel t erscheine n-mal in R.
#  <br> <br>
# ■ Sei S eine Multimenge
#  <br>
# □ Tupel t erscheine m-mal in S.
#  <br>
# ■ Tupel t erscheint in R $\cup$ S
# <br>
# □ (n+m) mal.

# $R$
# 
# |A|B|
# |-|-|
# |1|2|
# |3|4|
# |1|2|
# |1|2|

# $S$
# 
# |A|B|
# |-|-|
# |1|2|
# |3|4|
# |3|4|
# |5|6|

# $R \cup S$
# 
# |A|B|
# |-|-|
# |1|2|
# |3|4|
# |1|2|
# |1|2|
# |1|2|
# |3|4|
# |3|4|
# |5|6|

# ### Schnittmenge auf Multimengen

# ■ Sei R eine Multimenge
# <br>
# □ Tupel t erscheine n-mal in R.
# <br><br>
# ■ Sei S eine Multimenge
# <br>
# □ Tupel t erscheine m-mal in S.
# <br><br>
# ■ Tupel t erscheint in R $\cap$ S
# <br>
# □ min(n,m) mal.

# $R$
# 
# |A|B|
# |-|-|
# |1|2|
# |3|4|
# |1|2|
# |3|4|
# |1|2|

# $S$
# 
# |A|B|
# |-|-|
# |1|2|
# |3|4|
# |3|4|
# |5|6|

# $R \cap S$
# 
# |A|B|
# |-|-|
# |1|2|
# |3|4|
# |3|4|
# 

# ## Differenz auf Multimengen

# ■ Sei R eine Multimenge
# <br>
# □ Tupel t erscheine n-mal in R.
# <br><br>
# ■ Sei S eine Multimenge
# <br>
# □ Tupel t erscheine m-mal in S.
# <br><br>
# ■ Tupel t erscheint in R − S
# <br>
# □ max(0, n−m) mal.
# <br>
# □ Falls t öfter in R als in S vorkommt, bleiben n−m t übrig.
# <br>
# □ Falls t öfter in S als in R vorkommt, bleibt kein t übrig.
# <br>
# □ Jedes Vorkommen von t in S eliminiert ein t in R.

# $R$
# 
# |A|B|
# |-|-|
# |1|2|
# |3|4|
# |1|2|
# |1|2|

# $S$
# 
# |A|B|
# |-|-|
# |1|2|
# |3|4|
# |3|4|
# |5|6|

# $R-S$
# 
# |A|B|
# |-|-|
# |1|2|
# |1|2|

# $S-R$
# 
# |A|B|
# |-|-|
# |3|4|
# |5|6|

# ### Projektion und Selektion auf Multimengen

# ■ Projektion
# <br>
# □ Bei der Projektion können neue Duplikate entstehen.
# <br>
# □ Diese werden nicht entfernt
# <br><br>
# ■ Selektion
# <br>
# □ Selektionsbedingung auf jedes Tupel einzeln und unabhängig anwenden
# <br>
# □ Schon vorhandene Duplikate bleiben erhalten
# <br>
# – Sofern sie beide selektiert bleiben

# $R$
# 
# |A|B|C|
# |-|-|-|
# |1|2|5|
# |3|4|6|
# |1|2|7|
# |1|2|7|

# $\pi_{A,B}(R)$
# 
# |A|B|
# |-|-|
# |1|2|
# |3|4|
# |1|2|
# |1|2|

# $\sigma_{C\geq6}(R)$
# 
# |A|B|C|
# |-|-|-|
# |1|2|5|
# |3|4|6|
# |1|2|7|
# |1|2|7|

# ### Kreuzprodukt auf Multimengen

#  Sei R eine Multimenge
#  <br>
# □ Tupel t erscheine n-mal in R.
#  <br>
# ■ Sei S eine Multimenge
#  <br>
# □ Tupel u erscheine m-mal in S.
# <br>
# ■ Das Tupel tu erscheint in R $\times$ S n·m-mal.

# $R$
# 
# |A|B|
# |-|-|
# |1|2|
# |1|2|

# $S$
# 
# |B|C|
# |-|-|
# |2|3|
# |4|5|
# |4|5|

# $R \times S$
# 
# |A|R.B|S.B|C|
# |-|---|---|-|
# |1|2|2|3|
# |1|2|2|3|
# |1|2|4|5|
# |1|2|4|5|
# |1|2|4|5|
# |1|2|4|5|

# ### Joins auf Multimengen

# ■ Keine Überraschungen

# $R$
# 
# |A|B|
# |-|-|
# |1|2|
# |1|2|

# $S$
# 
# |B|C|
# |-|-|
# |2|3|
# |4|5|
# |4|5|

# $R⋈S$
# 
# |A|B|C|
# |-|-|-|
# |1|2|3|
# |1|2|3|

# $R⋈_{R.B<S.B}S$
# 
# |A|R.B|S.B|C|
# |-|---|---|-|
# |1|2|4|5|
# |1|2|4|5|
# |1|2|4|5|
# |1|2|4|5|

# ## Erweiterte Operatoren

# ## Überblick über Erweiterungen

# Duplikateliminierung 
#  <br>
#  ■ Aggregation 
#   <br>
#  ■ Gruppierung 
#   <br>
#  ■ Sortierung
#   <br>
#  ■ Outer Join 
#   <br>
#  ■ Outer Union
#   <br>
#  ■ Semijoin 
#   <br>
#  ■ (Division)

# ### Duplikateliminierung (duplicate elimination, $\delta$)

# ■ Wandelt eine Multimenge in eine Menge um.
# <br>
# □ Durch Löschen aller Kopien von Tupeln
# <br>
# □ $\delta$(R)
# <br>
# – Strenggenommen unnötig: Mengensemantik der relationalen Algebra

# $R$
# 
# |A|B|C|
# |-|-|-|
# |1|2|a|
# |3|4|b|
# |1|2|c|
# |1|2|d|

# $\delta(\pi_{A,B}(R))$
# 
# |A|B|
# |-|-|
# |1|2|
# |3|4|

# ### Aggregation

# ■ Aggregation fasst Werte einer Spalte zusammen.
# <br>
# □ Operation auf einer Menge oder Multimenge atomarer Werte (nicht Tupel)
# <br>
# □ Null-Werte gehen idR nicht mit ein
# <br>
# □ Summe (SUM)
# <br>
# □ Durchschnitt (AVG)
# <br>
# – Auch: STDDEV und VARIANCE
# <br>
# □ Minimum (MIN) und Maximum (MAX)
# <br>
# – Lexikographisch für nicht-numerische Werte
# <br>
# □ Anzahl (COUNT)
# <br>
# – Doppelte Werte gehen auch doppelt ein.
# <br>
# – Angewandt auf ein beliebiges Attribut ergibt dies die Anzahl der Tupel in der Relation.
# <br>
# – Zeilen mit NULL-Werten werden idR mitgezählt.

# $R$
# 
# |A|B|
# |-|-|
# |1|2|
# |3|4|
# |1|2|
# |1|2|

# SUM(B) = 10
# <br>
# AVG(A) = 1,5
# <br>
# MIN(A) = 1
# <br>
# MAX(B) = 4
# <br>
# COUNT(A) = 4
# <br>
# COUNT(B) = 4

# ### Aggregation – Beispiele

# Film
# 
# |Titel|Jahr|Länge|Typ|StudioName|
# |-----|----|-----|---|----------|
# |Total Recall|1990|113|Farbe|Fox|
# |Basic Instinct|1992|127|Farbe|Disney|
# |Dead Man|1995|90|s/w|Paramount|

# ■ MAX(Jahr): Jüngster Film
# <br>
# ■ MIN(Länge): Kürzester Film
# <br>
# ■ SUM(Länge): Summe der Filmminuten
# <br>
# ■ AVG(Länge): Durchschnittliche Filmlänge
# <br>
# ■ MIN(Titel): Alphabetisch erster Film
# <br>
# ■ COUNT(Titel): Anzahl Filme
# <br>
# ■ COUNT(StudioName): Anzahl Filme
# <br>
# ■ AVG(SchauspName): syntax error

# ### Gruppierung

# ■ Partitionierung der Tupel einer Relation gemäß ihrer Werte in einem oder mehr Attributen.
# <br>
# □ Hauptzweck: Aggregation auf Teilen einer Relation (Gruppen)
# <br>
# □ Gegeben
# <br>
# – Film(Titel, Jahr, Länge, inFarbe, StudioName, ProduzentID)
# <br>
# □ Gesucht: Gesamtminuten pro Studio
# <br>
# – Gesamtminuten(StudioName, SummeMinuten)
# <br>
# □ Verfahren:
# <br>
# – Gruppiere nach StudioName
# <br>
# – Summiere in jeder Gruppe die Länge der Filme
# <br>
# – Gebe Paare (Studioname, Summe) aus.

# ### Gruppierung (group, $\gamma$)

# ■ $\gamma_L$(R) wobei L eine Menge von Attributen ist. Ein Element in L ist entweder
# <br>
# 1. Ein Gruppierungsattribut nach dem gruppiert wird
# <br>
# 2. Oder ein Aggregationsoperator auf ein Attribut von R (inkl. Neuen Namen für das aggregierte Attribut)
# <br>
# ■ Ergebnis wird wie folgt konstruiert:
# <br>
# □ Partitioniere R in Gruppen, wobei jede Gruppe gleiche Werte im Gruppierungsattribut hat
# <br>
# – Falls kein Gruppierungsattribut angegeben: Ganz R ist die Gruppe
# <br>
# □ Für jede Gruppe erzeuge ein Tupel mit
# <br>
# – Wert der Gruppierungsattribute
# <br>
# – Aggregierte Werte über alle Tupel der Gruppe

# ### Gruppierung – Beispiele

# Film
# 
# |Titel|Jahr|Länge|Typ|StudioName|
# |-----|----|-----|---|----------|
# |Total Recall|1990|113|Farbe|Fox|
# |Basic Instinct|1992|127|Farbe|Disney|
# |Dead Man|1995|90|s/w|Paramount|

# ■ Durchschnittliche Filmlänge pro Studio
# <br>
# □ $\gamma_{Studio, AVG(Länge)→Durchschnittslänge}$(Film)
# <br><br>
# ■ Anzahl der Filme pro Schauspieler
# <br>
# □ $\gamma_{SchauspName, Count(Titel)→Filmanzahl}$(Film)
# <br><br>
# ■ Durchschnittliche Anzahl der Filme pro Schauspieler
# <br>
# □ $\gamma_{AVG(Filmanzahl)}(\gamma_{SchauspName, Count(Titel)→Filmanzahl}$(Film))
# <br><br>
# ■ Zu Hause:
# <br>
# □ Anzahl Schauspieler pro Film
# <br>
# □ Durchschnittliche Anzahl der Schauspieler pro Film
# <br>
# □ Studiogründung: Kleinstes Jahr pro Studio
# <br>
# <br>
# <br>
# ■ Gegeben: SpieltIn(Titel, Jahr, SchauspName)
# <br>
# ■ Gesucht: Für jeden Schauspieler, der in mindestens 3 Filmen spielte, das Jahr des ersten Filmes.
# <br>
# ■ Idee
# <br>
# □ Gruppierung nach SchauspName
# <br>
# □ Bilde
# <br>
# – Minimum vom Jahr
# <br>
# – Count von Titeln
# <br>
# □ Selektion nach Anzahl der Filme
# <br>
# □ Projektion auf Schauspielername und Jahr
# <br>
# ■ $\pi_{SchauspName, MinJahr}(\sigma_{AnzahlTitel≥3}(\gamma_{SchauspName, MIN(Jahr)→MinJahr, COUNT(Titel)→AnzahlTitel}(SpieltIn)))$
# <br>
# <br>
# <br>
# ■ Gegeben: SpieltIn(Titel, Jahr, SchauspName)
# ■ Gesucht: Für jeden Schauspieler, der in mindestens 3 Filmen spielte, das Jahr des ersten Filmes und den Titel
# dieses Films.
# □ Genauer: Ein Titel des Schauspielers in dem Jahr
# ■ Idee
# □ Wie zuvor
# □ Anschließend Self-Join um Filmtitel zu bekommen.
# □ Anschließend Gruppierung nach SchauspName um Gruppe auf einen Film zu reduzieren.
# ■ $\gamma_{SchauspName, MIN(MinJahr)→MinJahr, MIN(Titel)→Titel}( (SpieltIn) ⋈_{SchauspName = SchauspName, MinJahr = Jahr}
# (\pi_{SchauspName, MinJahr}(\sigma_{AnzahlTitel≥3}(
# \gamma_{SchauspName, MIN(Jahr)→MinJahr, COUNT(Titel)→AnzahlTitel}(SpieltIn)
# ) ) )
# )$

# ### Komplexe Ausdrücke – Beispiele
# <br>
# <br>
# ■ Stud(Matrikel, Name, Semester)
# <br>
# ■ Prof(ProfName, Fachgebiet, GebJahr)
# <br>
# ■ VL(VL_ID, Titel, Saal)
# <br>
# ■ Lehrt(ProfName, VL_ID)
# <br>
# ■ Hört(Matrikel,VL_ID)
# <br>
# ■ Gesucht: Fachgebiete von Professoren, die VL geben, die weniger als drei Hörer haben.
# <br>
# ■ $\gamma_{Fachgebiet}$( (Prof ⋈ Lehrt) ⋈
# ($\sigma_{ COUNT < 3(gVL_ID,COUNT(Matrikel)-> COUNT}$(Hört))
# )
# <br>
# ■ $\pi_{Fachgebiet}$( (Prof ⋈ Lehrt) ⋈
# ($\sigma_{ COUNT < 3(gVL_ID,COUNT(Matrikel)-> COUNT}$(Hört))
# )

# ### Sortierung (sort, $\tau$)
# <br>
# <br>
# ■ $\tau_L$(R) wobei L eine Attributliste aus R ist.
# <br>
# □ Falls L = (A1,A2,…,An) wird zuerst nach A1, bei gleichen A1 nach A2 usw. sortiert.
# <br><br>
# ■ Wichtig: Ergebnis der Sortierung ist keine Menge, sondern eine Liste.
# <br>
# □ Deshalb: Sortierung ist letzter Operator eines Ausdrucks. Ansonsten würden wieder Mengen entstehen und
# die Sortierung wäre verloren.
# <br>
# □ Trotzdem: In DBMS macht es manchmal auch Sinn zwischendurch zu sortieren.

# ### Semi-Join (⋊)
# <br>
# <br>
# ■ Formal
# <br>
# □ R(A), S(B)
# <br>
# □ R ⋉ S : = $\pi_A$(R⋈S)
# <br>
# = $\pi_A$(R) ⋈$\pi_{A\cap B}$(S)
# <br>
# = R⋈$\pi_{A\cap B}$(S)
# <br>
# □ In Worten: Join über R und S, aber nur die Attribute von R sind interessant.
# <br>
# □ Definition analog für Theta-Join
# <br>
# ■ Nicht kommutativ: R ⋉ S ≠ S ⋉ R

# ### Semi-Join
# 

# ![title](semijoin1.jpg)

# ![title](semijoin2.jpg)

# ![title](semijoin3.jpg)

# ### Outer Joins (Äußere Verbünde, |⋈|)
# <br>
# <br>
# Übernahme von „dangling tuples“ in das Ergebnis und Auffüllen mit Nullwerten (padding)
# <br>
# Nullwert: $\perp$ bzw. null (≠ 0)
# <br><br>
# Full outer join
# <br>
# Übernimmt alle Tupel beider Operanden
# R |⋈| S
# <br><br>
# Left outer join (right outer join)
# <br>
# Übernimmt alle Tupel des linken (rechten) Operanden
# <br>
# R |⋈ S (bzw. R ⋈| S)
# <br><br>
# Herkömmlicher Join auch „Inner join“
# <br>
# <br>
# <br>
# R⋈S
# <br>
# R |⋈ S
# <br>
# R ⋈| S
# <br>
# R |⋈| S

# ![title](outerjoin1.jpg)

# ![title](outerjoin2.jpg)

# ### Outer Union (⊎)
# <br>
# <br>
# ■ Wie Vereinigung, aber auch mit inkompatiblen Schemata
# <br>
# □ Schema ist Vereinigung der Attributmengen
# <br>
# □ Fehlende Werte werden mit Nullwerten ergänzt

# $R$
# 
# |A|B|C|
# |-|-|-|
# |1|2|3|
# |6|7|8|
# |9|7|8|

# $S$
# 
# |B|C|D|
# |-|-|-|
# |2|5|6|
# |2|3|5|
# |7|8|10|

# $R⊎S$
# 
# |A|B|C|D|
# |-|-|-|-|
# |1|2|3|$\perp$|
# |6|7|8|$\perp$|
# |9|7|8|$\perp$|
# |$\perp$|2|5|6|
# |$\perp$|2|3|5|
# |$\perp$|7|8|10|

# ### Division (division, /)
# <br>
# <br>
# ■ Typischerweise nicht als primitiver Operator unterstützt.
# <br>
# ■ Finde alle Segler, die alle Segelboote reserviert haben.
# <br>
# ■ Relation R(x,y), Relation S(y)
# <br>
# □ R/S = { t $\in$ R(x) | $\forall$ y $\in$ S $\exists$ <x, y> $\in$ R}
# <br>
# □ R/S enthält alle x-Tupel (Segler), so dass es für jedes y-Tupel (Boot) in S ein xy-Tupel in R gibt.
# <br>
# □ Andersherum: Falls die Menge der y-Werte (Boote), die mit einem x-Wert (Segler) assoziiert sind, alle y-Werte
# in S enthält, so ist der x-Wert in R/S.
# <br>
# ■ Hole die Namen von Angestellten, die an allen Projekten arbeiten.
# <br>
# □ Sinnvoller: Hole die Namen von Angestellten, die an allen Projekten arbeiten, in denen auch „Thomas Müller“
# arbeitet.

# ### Division – Beispiel

# ![title](division1.jpg)

# ### Division ausdrücken
# <br>
# <br>
# ■ Division ist kein essentieller Operator, nur nützliche Abkürzung.
# <br>
# □ Ebenso wie Joins, aber Joins sind so üblich, dass Systeme sie speziell unterstützen.
# <br><br>
# ■ Idee: Um R/S zu berechnen, berechne alle x-Werte, die nicht durch einen y-Wert in S „disqualifiziert“ werden.
# <br>
# – x-Wert ist disqualifiziert, falls man durch Anfügen eines y-Wertes ein xy-Tupel erhält, das nicht in R ist.
# <br>
# □ Disqualifizierte x-Werte: $\pi_{x}$ (($\pi_{x}$(R) $\times$ S) − R)
# <br>
# □ R/S: $\pi_{x}$(R) − alle disqualifizierten Tupel

# ### Division

# ![title](division2.jpg)

# ## Multiple Choice

# In[1]:


from IPython.display import IFrame

url = "https://lejuliennn.github.io/mct-trainer/#/quiz/categories/relationalealgebra"
IFrame(src=url, width='100%', height=800)


# In[ ]:




