#!/usr/bin/env python
# coding: utf-8

# # Relationale Algebra

# Die Relationale Algebra ist der wohl formalste Teil dieser  Vorlesung. <br>
# Zuvor wurde über die Modellierung von Daten gesprochen und wie man relationale Datenbanken entwirft. <br>
# Jetzt geht es darum, die zuvor modellierte relationale Datenbank  mit einer Sprache zu manipulieren bzw. neue Sichten darauf zu erstellen und an diese Anfragen zu stellen. 

# ## Einführung

# In den letzten Kapiteln wurde das Relationsschema mit Basisrelationen, die in der Datenbank gespeichert sind, behandelt. 
# <br>
# Jetzt geht es um „abgeleitete“ Relationenschemata mit virtuellen Relationen, die aus den Basisrelationen berechnet werden. 
# <br>
# Die „abgeleiteten“ Relationsschemata werden durch Anfragen definiert. 
# Daher benötigt man eine Anfragesprache. Eine Eigenschaft von ihr ist es, die Basis-Relationen nicht zu verändern, sondern neue Relationen für den Nutzer oder für die Applikation zu generieren.
# <br>
# ~~~~
# Eine Anfrage an eine Relation und deren Ergebnisse stellen wieder neue Relationen dar. 
# ~~~~
# 

# ### Kriterien für Anfragesprachen

# Für Anfragesprachen gibt es verschiedene Kritieren. Unter Anderem soll eine Ad-Hoc-Formulierung möglich sein. Der Benutzer soll eine Anfrage formulieren können, ohne ein vollständiges Programm schreiben zu müssen. Wenn man ein neues Programm in einer Sprache wie Python schreibt, muss man sich darum kümmern Bibliotheken zu importieren, usw. Dies ist bei einer Anfragensprache eben nicht der Fall. 
# <br>
# Zudem soll eine Anfragesprache eingeschränkt und keine komplette Programmiersprache sein. Sie soll aus einem Standard und nicht aus zu vielen verschiedenen Vokabularien bestehen. Dennoch besteht der SQL-Standard aus mehr als 1300 Seiten!
# <br>
# Eine weiteres Kriterium einer Anfragesprache ist die Deskriptivität bzw. die Deklarativität. 
# Der Benutzer soll formulieren was er haben möchte („Was will ich haben?“) und nicht wie er an das kommt, was er haben möchte („Wie komme ich an das, was ich haben will?“). Das System erstellt die darunterliegenden Programme automatisch zu der gegebenen Anfrage, ohne dass man schreiben muss, wie die Programme genau funktionieren. 
# <br><br>
# Zusätzlich muss eine Sprache optimierbar sein. Eine Sprache besteht aus wenigen Operationen.
# Für die Operatormenge gibt es Optimierungsregeln. Die Optimierung ist abhängig von der Nutzung bzw. von den Daten. Bestimmte Operatoren in bestimmten Situationen kosten unterschiedlich viel. 
# <br><br>
# Eine Anfragesprache muss effizient sein, insbesondere die einzelnen Operationen.
# Im relationalen Modell hat jede Operation eine Komplexität ≤ O(n²)
# Wobei n die Anzahl der Tupel einer Relation darstellt. 
# <br><br>
# Die Abgeschlossenheit ist eine weitere Eigenschaft einer Anfragesprache. Das Ergebnis von Anfragen auf Relationen ist wiederum eine Relation und kann als Eingabe für die nächste Anfrage verwendet werden.
# <br><br>
# Eine weitere, aber nicht sehr strenge, Eigenschaft ist die Mengenorientiertheit.
# Die Operationen sollen auf Mengen von Daten gelten. Dies gilt aber nicht in jedem Fall. 
# Letztendlich möchte man auf Elemente einer Tabelle zugreifen und nicht nur auf einzelne Elemente  („tuple-at-a-time“), die irgendwo herumliegen. 
# <br><br>
# Adäquatheit ist eine weitere Eigenschaft einer Anfragensprache. 
# Alle Konstrukte des zugrundeliegenden Datenmodells sollen unterstützt werden. 
# Dazu zählen Relationen, Attribute, Schlüssel, usw. 
# <br><br>
# Die Vollständigkeit einer Anfragesprache bedeutet, dass eine Sprache mindestens die Anfragen einer Standardsprache (z.B. relationale Algebra) ausdrücken kann. Die Relationale Algebra dient hierbei als Vorgabe. 
# <br><br>
# Zuletzt soll eine Anfragesprache sicher sein. Keine Anfrage, die syntaktisch korrekt ist, darf in eine Endlosschleife geraten oder ein unendliches Ergebnis liefern.

# ### Anfragealgebra

# In der Mathematik ist die Algebra definiert durch einen Wertebereich und auf diesem definierte Operatoren. <br>
# Ein Operand besteht aus Variablen oder aus Werten, aus denen neue Werte konstruiert werden können (x, 2, 3, ...).<br>
# Ein Operator besteht aus Symbolen, die Prozeduren repräsentieren, die aus gegebenen Werten neue Werte produzieren (+, -, * , /, ...).
# <br><br>
# Für Datenbankanfragen gibt es ebenfalls eine Algebra, die relationale Algebra (RA). Sie ist eine Anfragesprache für das relationale Modell. 
# Die Inhalte der Datenbank (Relationen) sind die Operanden.
# Die Operatoren definieren gewisse Funktionen zum Berechnen von Anfrageergebnissen.
# Es sind sehr grundlegenden Dinge, die wir mit Relationen tun wollen.
# 

# ### Mengen vs. Multimengen

# Bei der relationalen Algebra geht es hauptsächlich um Mengen. Bei normalen Mengen darf kein Tupel doppelt auftauchen. Bei Multimengen können identische Tupel mehrmals vorkommen. Es kann nämlich in einer Datenbanktabelle passieren, dass die Schlüssel nicht ordentlich definiert sind. Dann hat man sozusagen ein „Sack voll mit Tupeln“ (engl. „bag“).   
# <br>
# Die Operatoren der relationalen Algebra sind auf Mengen definiert, wohingegen die Operatoren auf einem DBMS (SQL-Anfragen) auf Multimengen definiert sind. Dies hat verschiedene Gründe. Zum Einem kann man hiermit die Effizienz beeinflussen bzw. steigern. Dazu kann man sich überlegen wie man eine Vereinigung als Multimenge und eine Vereinigung als Menge implementiert. 

# ## Basisoperatoren

# ## Klassifikation der Operatoren

# Die bereits bekannten Mengenoperatoren 
# <br>
# □ Vereinigung, Schnittmenge, Differenz 
# <br><br>
# Entfernende Operatoren werden auf einzelnen Elemente angewandt. 
# <br>
# □ Selektion, Projektion
# <br><br>
# Mit kombinierenden Operatoren kann man mehrere Relationen miteinander verbinden und neue Kombinationen von Tupeln bilden. Im Gegensatz zu den Mengenoperationen bei denen die Ergebnistupel immer gleich aussehen, kann es bei den kombinierenden Operatoren dazu kommen, dass die Ergebnistupel in ihren Attributen unterschiedlich aussehen. 
# <br>
# □ Kartesisches Produkt, Join, Joinvarianten 
# <br><br>
# Die Umbenennung ist die einzige Ooeration, die nicht die Tupel verändert, sondern das Schema. 
# <br><br>
# Ein Ausdruck in der Relationlen Algebra besteht aus einer Kombination von Operatoren und Operanden, auch Anfragen (queries) genannt. 

# ## Vereinigung (union, $\cup$)

# Die Vereinigung sammelt Elemente (Tupel) zweier Relationen unter einem gemeinsamen Schema auf.
# - R ∪ S := {t | t $\in$ R $\vee$ t $\in$ S}
# 
# Um eine Vereinigung anwenden zu können, müssen die Attributmengen beider Relationen identisch sein. Dazu gehören die Namen, Typen und die Reihenfolge. Wenn man beispielsweise die Attribute  in einer Tabelle in einem anderen Format hat als in der Anderen und die Werte vom gleichen Typ sind, kann mam diese Umbenennen und dennoch eine Vereinigung bilden. 
# <br>
# Ein Element ist nur einmal in der Vereinigung von R und S (R ∪ S) vertreten, auch wenn es jeweils einmal in R und S auftaucht. Es kommt zu einer Duplikatentfernung.

# ## Beispiel für Mengenoperatoren

# Das Beispiel zeigt zwei Tabellen R und S mit jeweils Name, Adresse, Geschlecht und Geburt. 
# Wenn man diese Relationen miteinander vereinigt, erhält man eine neue Relation, in der das Tupel mit "Carrie Fisher" nur ein Mal vorkommt. 

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

# Die Differenz in der Relationalen Algebra ist sehr ähnlich zu der aus der Mathematik. <br> 
# Die Differenz von R und S (R − S) eliminiert die Tupel aus der ersten Relation, die auch in der zweiten Relation vorkommen. Die Schemata beider Relationen müssen für eine Differenz gleich sein. 
# <br>
# - R − S := {t | t $\in$ R $\wedge$ t $\notin$ S}
# 
# Die Kommutativität gilt bei der Differenz nicht:
# - R − S ≠ S − R

# ## Beispiel für Mengenoperatoren

# Sowohl in der Relation R, als auch in der Relation S, gibt es das gleiche Tupel mit "Carrie Fisher". Bei der Differenz (R-S) wird das in beiden vorkommende Tupel eliminiert. 

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

# Die Schnittmenge R $\cap$ S ergibt die Tupel, die in beiden Relationen gemeinsam vorkommen.<br>
# - R $\cap$ S := {t | t $\in$ R $\wedge$ t $\in$ S}
# 
# Die Schnittmenge als Operator kann durch Verinigungen und Differenzen dargestellt werden, daher ist sie prinzipiell „überflüssig“. 
# - R $\cap$ S = R − (R − S) = S − (S − R)

# ![title](schnittmenge.jpg)

# ## Beispiel für Mengenoperatoren

# In Relation R sowie in Relation S gibt es ein identisches "Carrie Fisher" Tupel. Bildet man die Schnittmenge der beiden Relationen ($R\cap S$), sind in der Ergebnisrelation alle Tupel, die sowohl in R, als auch in S vorkommen. In diesem Fall wäre es nur das Tupel mit "Carrie Fisher". 

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

# Die Projektion ist ein unärer Operator. Sie erzeugt eine neue Relation mit einer Teilmenge der ursprünglichen Attribute.<br>
# Angenommen man projiziert auf eine Relation R mit den Attributen A1 bis Ak: $\pi_{A1,A2,…,Ak}$(R). Als Ergbnis erhält man eine neue Relation mit einer Teilmenge der ursprünglichen Attribute von R. Die Reihenfolge der Attribute entspricht üblicherweise der aufgelisteten Reihenfolge.<br><br>
# Durch das Weglassen von Attributen, kann es dazu kommen, dass die übrig gebliebenen Attribute  Duplikate enthalten. Diese werden implizit entfernt. <br>
# Ein Beispiel hierzu: Man bildet eine Projektion mit den Attributen A und B auf R. Das Ergebnis sind zwei identische Tupel. Das Duplikat wird eliminiert. 

# Relation R
# 
# |A|B|C|
# |-|-|-|
# |1|1|2|
# |1|1|3|

# $\pi_{A,B}$(R)
# 
# |A|B|
# |-|-|
# |1|1|

# ## Projektion – Beispiel

# Hier sind zwei weitere Beispiele zu Projektionen anhand einer Film-Tabelle dargestellt. <br>
# Im ersten Beispiel werden bei der Projektion nur die Spalten Titel, Jahr und Länge behalten. Die anderen Spalten werden weggeschnitten. <br>
# In zweitem Beispiel kommt 'True' doppelt vor und daher werden dessen Duplikate entfernt. 

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

# Die Relationale Algebra erlaubt es den Projektionsoperator mehr Fähigkeiten zu geben. Bei der einfachen Projektion zuvor ($\pi_{L}$(R)) war das L dabei 'nur' eine Attributliste. Die erweiterte Projektion kann neben der Attributliste auch andere Ausdrücke an der Stelle des L's stehen haben. <br>
# Ein anderer Ausdruck wäre A→B, wobei A ein Attribut in R und B ein neuer Name ist. Dies entspricht einer Umbenennung von Attributen. <br>
# Eine weitere Möglichkeit für einen neuen Ausdruck ist e→C. e ist ein Ausdruck mit Konstanten, arithmetischen Operatoren, Attributen von R, String-Operationen. C ist der neue Name für den Ausdruck e. Zwei Beispiele hierfür: 
# - A1 + A2 → Summe
# - Vorname || \` \` || Nachname → Name

# ## Selektion (selection, $\sigma$)

# Ein weiterer unärer Operator ist die Selektion. Sie erzeugt eine neue Relation mit gleichem Schema, aber einer Teilmenge der Tupel. Einfach ausgedrückt kann man sagen, dass eine Selektion die Anzahl der Tupel reduziert.  <br>
# Nur Tupel, die der Selektionsbedingung C (condition) entsprechen, werden in die neu erzeugte Relation übernommen. Für jedes Tupel wird somit einmal die Bedingung geprüft. Es handelt sich bei den Selektionsbedingungen um boolesche Selektionsbedingungen wie man sie aus Programmiersprachen kennt. <br>
# Die Operanden der Selektionsbedingung sind nur Konstanten oder Attribute von R. Diese können mittels Vergleichsoperatoren wie <, >, ≤, $\ge$, <> und = verglichen werden. const = const ist ein Beispiel dafür wie so etwas aussehen kann. Ist aber eigentlich unnötig, da es sich um Konstanten handelt. Eine typische Selektion ist ein Vergleich zwischen Attribut und Konstante (attr = const). Wenn man zwei Attribute miteinander vergleicht, (attr = attr) kann man mögliche Attribute finden, an denen die zwei Relationen gejoint werden können. Das würde einer Join Bedingung entsprechen. <br>
# Die einzelnen Selektionsbedingungen können zu einer gesamten Selektionsbedingung durch AND, OR und NOT kombiniert werden.<br>
# <br>
# Nicht zu verwechseln sind die Selektion aus der Relationalen Algebra mit dem SELECT aus SQL. Das SELECT entspricht in der Relationalen Algebra einer Projektion. Die Selektion wiederrum entspricht in SQL einer WHERE-Bedingung:
# - Selektion $\neq$ SELECT

# ## Selektion – Beispiel

# Die Beispiele zeigen verschiedene Selektionen auf einer gegebenen Film-Relation. <br>
# Im ersten Beispiel werden alle Filme selektiert, dessen Länge größer oder gleich 100 Minuten ist. <br>
# Im zweitem Beispiel kommt noch hinzu, dass diese Filem vom Fox-Studio produziert worden sein müssen. 

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

# Das Kartesische Produkt ist ein binärer Operator. Benannt worden ist es nach René Descartes. Ein französischer Naturwissenschaftler, Mathematiker und Philosoph. Das Kartesische Produkt ist auch unter anderen Namen wie Kreuzprodukt oder Produkt bekannt. Außerdem gibt es verschiedene Schreibweisen dafür: R * S statt R $\times$ S
# <br><br>
# Das Kreuzprodukt zweier Relationen R und S ist die Menge aller Tupel, die man erhält, wenn man jedes Tupel aus R mit jedem Tupel aus S kombiniert. Das Schema hat ein Attribut für jedes Attribut aus R und S. Bei Namensgleichheit von zwei oder mehreren Attributen wird kein Attribut ausgelassen, stattdessen werden sie eindeutig umbenannt. 

# ![title](descartes.jpg)

# ## Kartesisches Produkt – Beispiel

# Das Beispiel zum Kartesischen Produkt zeigt zwei Relationen R und S, die mittels Kreuzprodukt kombiniert werden. Dazu werden alle möglichen Kombinationen der Tupel gebildet. Die Relationen R und S haben ein Attribut mit dem selben Namen (B). In der neuen Ergbnisrelation wird das Attribut jeweils eindeutig umbenannt. Bei der Umbennenung wird als Präfix der Relationsname vor das Attribut geschrieben: R.B und S.B.

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
# 
# - Die hier verwendete Version des Multiple-Choice-Trainers von EILD.nrw wird nur in das JupyterBook eingebunden und nicht selbst gehostet. Der Multiple-Choice-Trainer wird durch GitHub-Pages gehostet. 
# - Alle Fragen und Kategorien befinden sich zurzeit in Überarbeitung und sind nicht final. 

# In[1]:


from IPython.display import IFrame

url = "https://lejuliennn.github.io/mct-trainer/#/quiz/categories/relationalealgebra"
IFrame(src=url, width='100%', height=800)


# In[ ]:




