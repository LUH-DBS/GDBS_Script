#!/usr/bin/env python
# coding: utf-8

# # Bearbeitung
# 
# **Anfragebearbeitung – Grundproblem** <br>
# 
# Die Anfragen, die man an eine Datenbank stellt, sind deklarativ. Solche Anfragen kann man in SQL, aber auch in der Relationalen Algebra formulieren. 
# Mittels der Anfragen sagt man somit was man will, aber nicht wie man das bekommt, was man will. 
# Das Datenbanksystem findet von selbst heraus, wie es an das kommt, was man möchte. 
# Angenommen die Anfragen wären nicht deklarativ, dann müsste man ein Programm schreiben, dass beispielsweise erst eine CSV-Datei durchgeht. 
# Stattdessen "sagt" man (deklarativ): Gebe alle Filme aus, die im Jahr 1996 produziert werden. <br>
# <br>
# Dafür müssen die Anfragen in eine ausführbare (prozedurale) Form transformiert werden. Ein Ziel hierbei ist es, einen „QEP“ (prozeduraler Query Execution Plan) zu erhalten. Wichtig zu beachten ist die Effizienz des Programms. Es soll zum Einem schnell sein, aber zum Anderen auch wenige Ressourcen verbrauchen (CPU, I/O, RAM, Bandbreite), denn es wirkt sich stark auf den Energieverbrauch aus. <br>
# <br>
# <br>
# 
# **Ablauf der Anfragebearbeitung**<br><br>
# Zunächst hat man eine Anfrage der Form: <br>
# SELECT * FROM x WHERE ...;
# 1. Parsing:<br>
# Eine solche Anfrage wird zunächst mit Blick auf die Syntax geparst. Anschließend werden die Elemente auf korrekte Semantik überprüft und ein Parsebaum erstellt. Es wird herausgefunden auf welche Operationselemente die Anfrage abgebildet wird. <br>
# <br>
# 2. Wahl des logischen Anfrageplans:<br>
# Im zweitem Schritt wird ein logischer Anfrageplan ausgewählt. In der Regel ist es ein Baum mit logischen Operatoren.<br>
# Es gibt exponentiell viele Pläne, die man anhand der Elemente, die man in der Anfrage hat, erstellen kann. Natürlich lassen sich bestimme Kombinationen nicht darstellen. Das Grundproblem ist auch NP-Vollständig.<br>
# Unter den verschiedenen Plänen muss der optimale Plan ausgewählt werden. Dabei gibt es verschiedene Optimierungsverfahren, die angewandt werden können.<br>
# Mittels der logischen Optimierung können Operatoren im Plan hin- und hergeschoben werden.
# Weitere Optimierungen können auch mit regelbasierten und kostenbasierten Optimierern durchgeführt werden. Diese basieren auf den Kosten der jeweiligen Operationen der Anfragen.<br>
# <br>
# 3. Wahl des physischen Anfrageplans:<br>
# Für jede Operation, die momentan noch in deklarativer Form ist, muss nun eine Prozedur bzw. ein Programm mit physischen Operatoren ausgewählt werden. Dies sind unter anderem Algorithmen, Scan Operatoren oder auch JOIN-Implementierungen. <br> 
# Hierbei können physische Optimierungen angewandt werden.<br>
# <br>
# 
# Am Ende wird der ausgewählte Anfrageplan ausgeführt. 
# 
# ![title](ablauf_anfragebearbeitung.jpg)

# ## Parsen der Anfrage
# 
# ### Syntaxanalyse
# Die Aufgabe einer Syntaxanalyse ist die Umwandlung einer SQL Anfrage in einen Parsebaum.<br>
# In einem Parsebaum werden folgende Elemente als Atome (Blätter) dargestellt:
#    - Schlüsselworte
#    - Konstanten
#    - Namen (Relationen und Attribute)
#    - Syntaxzeichen
#    - Operatoren
#    
# Bei Syntaktischen Kategorien können Teilausdrücke einer Anfrage Namen gegeben werden. Die Teilausdrücke können also zu Kategorien zusammengefasst werden. Beispielsweise bei einer VIEW.  
# <br>
# ### Eine Grammatik für einen Teil von SQL
# Die Anfragen unterliegen einer Grammatik (wie man sie aus der theoretischen Informatik kennt). Sie bestehen aus einer Struktur der Form "SELECT FROM WHERE", kurz SFW. Es können keine Anfragen formuliert werden, die nicht der Grammatik entsprechen.<br>
# - Anfragen:
# 
#         - <Anfrage> :: = <SFW>
#         - <Anfrage> :: = (<SFW>)
#         - Mengenoperatoren fehlen
# 
# 
# - SFWs:<br>
#     Die SFWs werden wie folgt aufgebaut, es fehlen Gruppierungen, Sortierungen etc.:
# 
#         - <SFW> ::= SELECT <SelListe> FROM <FromListe> WHERE <Bedingung>
# 
# 
# - Listen:<br>
#     Dabei ergibt sich eine SelListe(SelectListe) aus einem Attribut und einer anderen SelListe bzw. nur aus einem Attribut.
#     
#         - <SelListe> ::= <Attribut>, <SelListe>
#         - <SelListe> ::= <Attribut>
#     
#     Die FromListe ergibt sich aus einer Relation oder aus einer Relation mit einer weiteren FromListe.
#         
#         - <FromListe> ::= <Relation>, <FromListe>
#         - <FromListe> ::= <Relation>
# 
# 
# - Bedingungen (Beispiele):<br>
#     Bedingungen können Verknüpfungen bzw. Kombinationen von anderen Bedingungen sein. Verknüpft werden können sie beispielsweise mit AND oder auch mit OR:
#     
#         - <Bedingung> ::= <Bedingung> AND <Bedingung>
#  
#      Eine Bedingung kann auch eine Anfrage sein, bei der man eine Überprüfung in einer anderen Anfrage anfordert:
# 
#         - <Bedingung> ::= <Tupel> IN <Anfrage>
#         - <Bedingung> ::= <Attribut> = <Attribut>
#         - <Bedingung> ::= <Attribut> LIKE <Muster>
#         
# 
# - Tupel, Attribute, Relationen und Muster:<br>
#     Die Inhalte von Tupeln, Attributen, Relationen und Mustern sind nicht durch grammatische Regeln definiert. Entweder sie existieren oder sie existieren nicht. <br>
#     Angenommen man wählt eine Relation aus, die nicht existiert. Die Anfrage kann nicht korrekt ausgeführt werden und die Datenbank gibt zurück, dass es diese Relation nicht gibt. 
# <br><br>
# Die vollständige Grammatik kann man z.B. unter http://docs.openlinksw.com/virtuoso/GRAMMAR.html finden.
# 
# ### Parse-Baum
# 
# ![](parsebaum.jpg)
#     
# In diesem Bild sieht man den Aufbau eines Parsebaums, der anhand der vorherigen SQL-Anfrage erstellt wurde. Dabei besteht die Anfrage aus einem SFW. Das SFW kann wiederrum unterteilt werden in SELECT, SelListe, ... <br>
# Alle Konstanten und Relationen lassen sich in den Blattstrukturen wiederfinden.
# 
# 
# ### Prüfung der Semantik
# Die Prüfung der Semantik auf Korrektheit erfolgt während der Übersetzung. Dabei werden auf verschiedene Punkte geachtet, unter Anderem:
# - Existieren die Relationen und Sichten der FROM Klausel?
# - Existieren die Attribute in den genannten Relationen?
# - Sind sie eindeutig?
# - Korrekte Typen für Vergleiche? (bsp.: Vergleicht man einen Integer mit einem String usw. 
# - Aggregation korrekt?
# - ...
# 
# ### Vom Parse-Baum zum Operatorbaum
#                                                                 
# ![](operatorbaum.jpg)
# 
# Am Ende vom vorherigen Schritt erhält man einen Parsebaum. Dieser wird jetzt in einen Operatorbaum umgewandelt. Dargestellt werden kann der Operatorbaum mittels Relationaler Algebra. Dabei entspricht das SELECT einer Projektion und das WHERE einer Selektion. Aus den Schlüsselwörtern hat man nun konkrete Operatoren bekommen, die nun deutlich besser sichtbar sind. Man weiß jetzt auch, dass spielt_in und Schauspieler durch ein Kreuzprodukt kombiniert werden. Diese beiden Relationen sind der Input des Kreuzprodukts. Auf dem Output findet dananch eine Selektion statt und auf dessen Output letztendlich eine Projektion. 

# ## Transformationsregeln der RA
# Zuvor haben wir gesehen, dass es für jede Anfrage verschiedene Pläne gibt. Das bedeutet also auch, dass es verschiedene Operatorenbäume gibt. Somit kann man also verschiedene Anfragen ineinander transformieren. Dies wird anhand der Transformationseregeln der Relationalen Algebra dargestellt. 
# ### Anfragebearbeitung – Transformationsregeln
# Die Transformation der internen Darstellung soll ohne eine Änderung der Semantik erfolgen. Damit ist gemeint, dass die Operatorenbäume nach der Transformation immernoch die gleiche Anfrage wie vor der Transformation beantworten können bzw. es kommt immernoch das gleiche Ergebnis heraus.<br>
# Das Ziel einer Transformation ist es eine effizientere Ausführung zu finden. Die Operatoren sollen möglichst kleine Zwischenergebnisse liefern. Der nächste Operator soll als Input möglichst kleine Mengen von Tupeln erhalten auf denen er arbeiten kann. 
# <br><br>
# Um diese Transformation zu vollführen, müssen zunächst äquivalente Ausdrücke identifiziert werden. 
# Zwei Ausdrücke der relationalen Algebra gelten als äquivalent, falls sie gleiche Operanden (= Relationen) besitzen und stets die gleiche Antwortrelation zurückgeben.
# 'Stets' bedeutet hierbei, dass nicht per Zufall die gleichen Ergebnisse bei mehreren Anfragen herauskommen. Für jede mögliche Instanz der Datenbank, muss man das selbe Ergebnis erhalten.
# <br>
# 
# 
# ### Anfragebearbeitung – Beispiel
# 
# In diesem Beispiel möchte man den Nachnamen projizieren. Dafür erstellt man das Kreuzprodukt zwischen den Relationen 'Mitarbeiter' und 'Projekte'. Darauf selektiert man alle Paare bei denen die Mitarbeiter-ID gleich der Projekt-ID ist. Die Projekte, die ein gleiches oder größeres Budget als 40000 haben, werden aussortiert.  
# 
# ![](anfragebearbeitung_bsp1.jpg)
# 
# Nun kann man sich überlegen, wo man noch früher Tupel herausfiltern kann. Eine Möglichkeit wäre es die Selektion mit dem Kreuzprodukt zu einem Join zu kombinieren. 
# Eine Andere wäre es, die übrig gebliebene Selektion früher durchzuführen. Noch bevor man das Kreuzprodukt der beiden Relationen bildet, kann man die Selektion 'p.Budget < 40000' auf der 'projekt'-Relation ausführen. Man erwartet, dass der nachfolgende Join auf einer kleineren Tupelmenge ausgeführt wird. 
# 
# ![](anfragebearbeitung_bsp2.jpg)
# 
# ### Kommutativität und Assoziativität
# 
# Die Kommutativität und Assoziativität gelten insbesondere für Mengenoperationen. <br>
# - $\cup$ ist kommutativ und assoziativ
#     <br>
#     R $\cup$ S = S $\cup$ R
#     <br>
#     (R $\cup$ S) $\cup$ T = R $\cup$ (S $\cup$ T)
# <br><br>
# - $\cap$ ist kommutativ und assoziativ
#     <br>
#     R $\cap$ S = S $\cap$ R
#     <br>
#     (R $\cap$ S) $\cap$ T = R $\cap$ (S $\cap$ T)
# <br><br>
# - ⋈ ist kommutativ und assoziativ
#     <br>
#     R ⋈ S = S ⋈ R
#     <br>
#     (R ⋈ S) ⋈ T = R ⋈ (S ⋈ T)
#     
#     <br>Bei einem Join kann es passieren, dass die Spaltenreihenfolge anders ist. Sie kann nachträglich noch geändert werden (bspw. mit einer Projektion). 
#     
# Alle diese Regeln gelten jeweils für Mengen und für Multimengen. Zudem können die Ausdrücke in beide Richtungen verwendet werden.
# 
# ### Weitere Regeln
# - Selektion<br>
#     - $\sigma_{c1 AND c2}(R ) = \sigma_{c1}(\sigma_{c2} (R))$
#     
#         Wenn man eine Selektion mit zwei Bedingungen hat, kann man das in zwei Selektionen, die aufeinander aufbauen, kaskadieren. 
#     
#     - $\sigma_{c1 OR c2}(R ) = \sigma_{c1}(R) \cup \sigma_{c2} (R)$
#     
#         Wenn man eine Selektion mit einem OR hat, kann man davon die Vereinigung bilden. 
#         Dabei kommt es aber zu einem Problem bei Multimengen: 
#         c1 or c2 bedeutet, gebe mir jedes Tupel egal ob Bedingung c1, c2 oder beide gelten. Man würde bei der Vereinigung eine andere Anzahl an Tupeln bekommen. Bei den Fällen bei denen beide Bedingungen gelten, würde es das Tupel doppelt geben. 
# 
#     - $\sigma_{c1}(\sigma_{c2}(R)) = \sigma_{c2}(\sigma_{c1}(R))$
#     
#         Die äußere Bedigung kann mit der inneren Bedingung vertauscht werden. Dabei kann man sich überlegen welche Bedingung günstiger ist und sie zuerst auszuführen. 
#      
#     - $\sigma_{c}(R \Phi S) \equiv (\sigma_{c} (R)) \Phi (\sigma_{c} (S))$
#         - $\Phi \in \{\cup, \cap , - , ⋈\}$
#     - $\sigma_{c}(R \Phi S) \equiv (\sigma_{c} (R)) \Phi S$
#         - $\Phi \in \{\cup, \cap , - , ⋈\}$
#         - Falls sich c nur auf Attribute in R bezieht, kann man es so umformen, sodass sich die Selektion nur auf die Relation R bezieht. 
# 
# - Projektion <br>
#     - $\pi_{L}(R ⋈ S) = \pi_{L}(\pi_{M}(R) ⋈ \pi_{N}(S))$<br>
#         Eine Projektion einer Spalte auf einem Join zweier Relationen kann einer Projektion einer Spalte auf einem Join zweier Projektionen auf jeweils einer Relation entsprechen. 
#     - $\pi_{L}(R ⋈_{C} S) = \pi{L}(\pi_{M}(R) ⋈_{C} \pi_{N}(S))$<br>
#         Genauso kann nun auch bei einem Join mit Bedingung und einem Kreuzprodukt vorgegangen werden.
#     - $\pi_{L}(R \times S) = \pi_{L}(\pi_{M}(R) \times \pi_{N}(S))$
#     
#     - $\pi_{L}(\sigma_{C}(R)) = \pi_{L}(\sigma_{C}(\pi_{M}(R)))$<br>
#         Hierbei kann eine Projektion noch vor die Selektion geschoben werden. Wichtig dabei ist, dass die neue Projektion ($\pi_{M}$) L enthält. Es können auch weitere Projektionen hinzugefügt werden. Solange sie L enthalten, verändert sich nichts. 
# 

# ## Optimierung
# 
# ### Anfragebearbeitung - Optimierung
# Bei der Anfragebearbearbeitung wird eine regelbasierte Optimierung durchgeführt. Dabei schreibt ein fester Regelsatz Transformationen vor. Die Transformationen sollen eine Anfrage schneller bearbeiten. <br>
# Die Prioritäten unter den Regeln werden durch Heuristiken bestimmt. Es ist nach Erfahrung der beste Weg, es muss aber nicht immer der Fall sein. Ein Beispiel einer solchen Optimierung ist das 'pushen' einer Selektion nach unten im Anfragebaum. 
# <br><br>
# Außerdem wird noch eine kostenbasierte Optimierung angewandt. Für jede Relation kann man ein Kostenmodell aufstellen. Das Kostenmodell basiert dabei auf Statistiken, die das Datenbankmodell gesammelt hat. Nach dem Aufstellen des Kostenmodells kann mit diesem ein optimaler Plan bestimmt werden, bei dem die Kosten minimal sind. Dazu kann auch die optimale Joinreihenfolge bestimmt werden. Transformationen helfen hierbei die Kosten zu verringern.
# <br><br>
# Im Allgemeinen wird nicht die optimale Auswertungsstrategie gesucht, sondern eine einigermaßen effiziente Variante. Sie soll uns dabei helfen den schlimmsten Fall zu verhindern -> Avoid the worst case!
# 
# 
# ### Logische und physische Optimierung
# 
# Logische Optimierung:<br>
# Bei der logischen Optimierung kann anhand der Transformationsregeln jeder Ausdruck im Anfragebaum in viele verschiedene, semantisch äquivalente Ausdrücke umgeschrieben werden. Dabei wählt man den (hoffentlich) besten Ausdruck (=Plan, =QEP (QueryExecutionPlan)) aus.
# <br><br>
# Physische Optimierung:<br>
# Für jede relationale Operation gibt es viele verschiedene Implementierungen: 
# Zum Beispiel für den Zugriff auf Tabellen kann es ein Scan, verschiedene Indizes, ein sortierter Zugriff, etc. sein. 
# Genauso bei Joins kann man auch verschiedene Implementierungen wie Nested loop, sort-merge, hash, etc. wählen. 
# Daraus wählt man für jede Operation wieder die (hoffentlich) beste Implementierung aus. 
# <br><br>
# Es kann nun sein, dass die logische von der physischen Optimierung abhängt.
# Beispielsweise kann man sagen, dass ein bestimmter Plan besser funktioniert, wenn man einen Nested-Loop-Join durchführt. Wenn man eine Schleife innerhalb einer anderen hat, kann man in der einen Schleifen bereits etwas Anderes mitprüfen. Das würde einem bestimmten logischen Plan besser entsprechen. 
# 
# 
# ### Logische Optimierung – regelbasiert
# Die Grundsätze der logischen Optimierung lauten wie folgt:
# - Selektionen sollen so weit wie möglich im Baum nach unten geschoben werden.
# - Selektionen mit AND können aufgeteilt und separat verschoben werden.
# - Projektionen sollen so weit wie möglich im Baum nach unten geschoben werden,
# - bzw. neue Projektionen können eingefügt werden.
#     <br>Bei dem nach unten Verschieben von Selektionen und Projektionen gibt es einen Unterschied: Bei dem Verschieben von Selektionen geht es darum die Menge an Tupeln zu verringern. Bei Projektionen versucht man die Anzahl der Spalten zu verringern. <br>
#     Beides ist sinnvoll, da man davon ausgehen muss, dass bei riesigen Datensätzen eine Spalte mehrere Gigabyte groß sein kann. Wenn man solche Spalten nicht unbedingt mehr mitschleppen muss, macht man das Programm effizienter. 
# - Duplikateliminierung kann manchmal entfernt oder verschoben werden.
# - Kreuzprodukte sollen mit geeigneten Selektionen zu einem Join zusammengefasst werden. Kreuzprodukte sollen möglichst vermieden werden, stattdessen können Joins mit effizienteren Implementierungen durchgeführt werden. 
# 
# 
# In dieser Vorlesung geht es nicht um die Suche nach der optimalen Joinreihenfolge. Diese Thematik wird erst in aufbauenden Veranstaltungen genauer betrachtet. 
# <br><br>
# 
# ### Anwendung der Transformationsregeln
# 
# Die folgende Anfrage ist von Prof. Alfons Kemper (TU München). 
# Bei der Anfrage sucht man eindeutig alle Semester in denen für Studenten, hören, Vorlesungen und Professoren folgenden Bedingungen gelten: 
# Der Professor heißt mit Namen 'Sokrates'. Dieser Professor soll Vorlesungen halten und diese sollen von Studierenden gehört werden. 
# Also man möchte wissen: In welchen Semestern sind die Studierenden, die Vorlesungen bei Sokrates hören?
# 
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
# 
# Zunächst hat man eine Darstellung bei der es ein Kreuzprodukt aller Relationen gibt. Dann kommen die aneinandergereihten Selektionsoperatoren. Man merkt sofort, es ist nicht die logisch effizienteste Variante. 
# 
# ![](transformationsregeln.jpg)
# 
# ### Aufspalten der Selektionsprädikate
# 
# Das Erste was man macht, ist das Aufspalten der Selektion. Dadurch erhält man alles als einzelne Operationen. Im nächsten Schritt wird sich eine effizientere Platzierung der Selektionen überlegt. 
# 
# ![](aufspalten_selektionspraedikate.jpg)
# 
# ### Verschieben der Selektionsprädikate „Pushing Selections“
# 
# Um die Anzahl der Tupel zu verringern, schiebt man die Selektionen weiter nach unten.
# Das ist der Fall bei den Studierenden, die eine Vorlesung hören. Um deren Anzahl zu verringern wird nach dem Kreuzprodukt zwischen den beiden Relationen 'studierende' und 'hören' die Selektion platziert.
# Die kleinere Menge an Tupeln als Output wird dann wie zuvor über das Kreuzprodukt mit 'Vorlesungen' kombiniert. Mit einer Selektion wird die Anzahl der Tupel reduziert, bevor man ein weiteres Kreuzprodukt bildet. 
# Ansonsten hat man direkt vor die Professorentabelle die Selektion mit der Bedingung, dass der Name des Professors Sokrates sein soll, geschoben. Somit erhält man als Ouptut nach der Selektion nur ein Tupel und muss nicht mehr alle Professorentupel mitführen. 
# 
# ![](verschieben_selektionspraedikate.jpg)
# 
# ### Zusammenfassung von Selektionen und Kreuzprodukten zu Joins
# 
# Die Selektionen werden mit den Kreuzprodukten zusammengefasst und durch effizienter implementierte Joins ausgetauscht. 
# 
# ![](zusammenfassen_selektionspraedikate.jpg)
# 
# ### Optimierung der Joinreihenfolge: Kommutativität und Assoziativität ausnutzen
# 
# Die Kommutativität und Assoziativität werden jetzt ausgenutzt, um die Joinreihenfolge zu optimieren. Das bedeutet, man möchte die Tupelmenge, die man erzeugt, möglichst gering halten. 
# Daher verschiebt man die Selektion des Professorennames nach ganz unten. Grund hierfür ist, dass man aus dieser Selektion nur ein Tupel erhält, mit dem man weiterarbeiten muss. Danach vergrößert sich die Tupelmenge nur minimal um die Vorlesungen, die der Professor hält, usw. 
# Ohne diese Optimierung startet man mit der gesamten Menge an Studierenden, die diese Vorlesung hören. Nun muss man diese große Tupelmenge als Input für die nächsten Operationen mitnehmen, was vermeidbare Kosten verursacht. 
# 
# ![](joinreihenfolge1.jpg)
# 
# ### Was hat´s gebracht?
# 
# Ohne die Optimierungen hat man ein Maximum von 13 Tupeln mit denen man arbeiten muss. Generell arbeitet man hierbei immer mit einer sehr hohen Anzahl von Tupeln im Gegensatz zu der Variante mit Optimierungen. Durch die Optimierungen arbeitet man auf maximal 4 Tupeln. 
# 
# Es handelt sich hier um ein ausgedachtes Beispiel. Die Zahlen sind nicht logisch herleitbar. Es soll nur darstellen, wie sich das Verschieben von günstigen Join-Varianten auf die Tupelmenge, verhält. 
# 
# ![](joinreihenfolge2.jpg)
# 
# ### Einfügen von Projektionen
# 
# Nun kann man noch darüber nachdenken, ob man Projektionen einfügt, wenn man bestimmte Spalten nicht mehr braucht. Das wäre bei der Matrikelnummer der Fall, denn man benötigt im Nachhinein nur noch diese aus den Attributen beim Join und der Projektion danach. Insbesondere hat man dort einen Left-Join ausgeführt. 
# 
# ![](einfuegen_projektion.jpg)
# 
# ### SQLite Explain
# 
# Anfragepläne kann man auch in SQLite ausprobieren. Dafür stellt man am Anfang mit '.eqp on' den Modus an. Dann wird für jede Anfrage der Plan direkt gezeigt. 
# Es kann auch explizit mit 'EXPLAIN QUERY PLAN' eingestellt werden. Danach gibt man wie gewohnt die SQL-Anfrage ein. 
# Nun kann die tatsächliche Implementierung angesehen werden. Zunächst wird die 'producer' Tabelle gescannt. Dann wird ein Autoindex für 'movie' verwendet, weil wir den Primärschlüssel 'mid' verwenden. Dieser Index wird für den IN-OPERATOR verwendet und es wird ein B-TREE verwendet, um die doppelten Werte zu vermeiden. 
# 
# ![](sqlite.jpg)

# ## Kostenmodelle
# 
# ### Kostenbasierte Optimierung
# Generell müsste man konzeptionell alle denkbaren Anfrageausführungspläne generieren, um den besten darunter auszuwählen. Dabei werden die Kosten der Pläne anhand eines Kostenmodells bewertet.  Hierzu werden Statistiken und Histogramme zur Hilfe genommen. 
# Die Statistiken können können vom verfügbaren Speicher oder vom System abhängig sein. Je nach verwendetem Rechner, kann eine Operation eventuell unterschiedlich viel Zeit benötigen. Daher benötigt es eine Kalibrierung gemäß dem verwendetn Rechner.
# Beim Aufwands-Kostenmodell probiert man meistens den Durchsatz zu maximieren und nicht die Antwortzeit zu minimieren. 
# <br>
# Da es hierbei um Kosten geht, möchte man selbstverständlich den billigsten Plan ausführen. Dennoch sollte man darauf achten nicht zu lange zu optimieren, denn das Optimieren selbst kostet auch wieder Zeit und macht die Anfrage langsamer. Irgendwie muss man einen Zwischenweg zwischen beidem finden. Dies kann beispielsweise mithilfe von Heuristiken geschehen.  
# 
# 
# 
# ### Problemgröße (Suchraum)
# Wenn man konzeptionell alle denkbaren Anfrageausführungspläne generiert, erhalten wir die Anzahl der Bushy-Pläne bei n Tabellen gemäß der folgenden Formel:
# 
# $\frac{(2(n-1))!}{(n-1)!}$
# 
# 
# 
# |n|$2^n$|(2(n-1))!/(n-1)!|
# |---|---|---|
# |2|4|2|
# |5|32|1680|
# |10|1024|1,76 $\times 10^{10}$|
# |20|1.048.576|$4,3\times10^{27}$|
# 
# Bei wachsender Anzahl von n Tabellen, wächst der Suchraum sehr stark an. Die Plankosten unterscheiden sich somit schnell um viele Größenordnungen.
# Das Optimierungsproblem, unabhängig von den Bushy-Plänen, ist NP-hart.
# 
# 
# 
# ### Kostenmodell
# 
# ![](kostenmodell.jpg)
# 
# Haben einen algebraischen Ausdruck. Dieser wird einem Kostenmodell übergeben und man erhält die Ausführungskosten ohne den Ausdruck ausgeführt zu haben. 
# Das Kostenmodell betrachtet dabei Indexinformationen, Ballungs-Informationen (Clustering on disk), DB-Kardinalitäten und Attributverteilungen. 
# 
# 
# 
# ### Statistiken
# Zu jeder Basisrelation kennt man die Anzahl der Tupel und deren Tupelgröße. 
# Zu (jedem) Attribut kennt man eventuell den größten und kleinsten Wert. Es kann ein Histogramm zur Werteverteilung geben und man kennt (hoffentlich) die Anzahl der 'distinct'-Werte (Kardinalität). 
# Zum System kennt man die Speichergröße, die Bandbreite, die I/O-, sowie die CPU-Zeiten. 
# <br><br>
# Problem: Die Statistiken gelten nur für einen Zustand der Datensätze. Theoretisch müsste man nach jeder Veränderung der Datenbank neue Statistiken erstellen oder die bestehenden Statistiken updaten. Das verursacht hohe Kosten und wird daher meistens nur nach einer bestimmten Zeit manuell/explizit durchgeführt mit einer Funktion wie runstats().
# <br><br>
# 
# ![](statistik.jpg)
# 
# 
# 
# ### Kosten von Operationen
# 
# Es gibt bestimmte Kosten für Operationen, die unabhängig vom Kostenmodell gelten:
# 
# - Projektion: 
#     - Wenn eine Projektion mit einem anderem Operator kombiniert wird, dann kostet diese nichts. 
#     
# - Selektion: 
#     - Bei einer Seletktion ohne Index wird die gesamte Relation von der Festplatte gelesen. Die gesamte Relation ist daher Teil der Kosten. 
#     - Bei einer Selektion mit Baum-Index (z.B. B-Baum) muss man einen Teil des Index (Baumtiefe) und die gesuchte Seite von der Festplatte lesen.
#     - Beim Pipelining hat man (fast) keine Kosten. Wenn die Selektion immer wieder an eine Datenpipeline herangehangen wird, verursacht es also (fast) keine Kosten.  
#     
# - Join: 
#     - Beim Join hängen die Kosten vom Joinalgorithmus (Nested Loops, Hash-Join, Sort-Merge Join, usw.) ab. 
#     
# - Sortierung: 
#     - Die Kosten von Sortierungen werden in einer aufbauenden Veranstaltung besprochen. Es wird sich dabei um Sortieralgorithmen wie Two-Phase-Merge-Sort usw. handeln. 
# 
# Generell sind die Kosten von Operationen die Anzahl der Tupel im Input. Dabei fragt man sich , ob die Relation in den Hauptspeicher passt. Je kleiner die Anzahl der Tupel im Input ist, desto wahrscheinlicher passt sie in den Hauptspeicher. <br>
# Bedacht werden muss auch, wie groß die Anzahl der Tupel im Output einer Operation ist. Der Output wird nämlich der Input des nächsten Operators sein. Deshalb schätzt ein Kostenmodel u.a. für jede Operation die Anzahl der Ausgabetupel.
# Das Schätzen der Ausgabetupel geschieht also unter Betrachtung des Selektivitätsfaktors (selectivity factor, sf). Der Selektivitätsfaktor beschreibt die „Selektivität“ in Bezug auf die Inputgröße. 
# 
# 
# 
# - #Ausgabetupel = #Eingabetupel x Selektivität
#  
# Beispiel: Eine Operation mit Selektivitätsfaktor 0.5 wird auf eine Relation angewandt (O(R)). Dann ist die Anzahl der Ausgabetupel wahrscheinlich |R| / 2.
# 
# 
# 
# ### Selektivität
# Die Selektivität schätzt die Anzahl der qualifizierenden Tupel relativ zur Gesamtanzahl der Tupel in der Input Relation. 
# <br>
# 
# Bei Projektionen ist die Selektivität genau 1. Die Operation erhält R Tupel als Input und gibt R viele Tupel als Output wieder heraus. 
# 
# - sf = |R|/|R| = 1
# 
# <br>
# Bei der Selektion ist der Selektivitätsfaktor die Anzahl der Tupel der selektierten Menge geteilt durch die gesamte Anzahl der Tupel.
# 
# - sf = |$\sigma_c$(R)| / |R|
# 
# <br>
# Bei Joins ergibt sich der Selektivitätsfaktor aus der Selektivität des Joins geteilt durch die Selektivität des Kreuzproduktes. Das Kreuzprodukt ergibt sich aus der Anzahl der Tupel einer Relation multipliziert mit der Anzahl der Tupel einer anderen Relation.  
# 
# - sf = |R ⋈ S| / |R x S| = |R ⋈ S| / (|R| · |S|)
# 
# 
# 
# #### Selektivität schätzen
# 
# - Selektion:
# Wenn man eine Selektion auf einem einzelnen Schlüssel durchführt, also auf einer Konstanten, kann man davon ausgehen, dass der Selektivitätsfaktor genau
# 
# - sf = 1 / |R|
# 
# ist, da ein Schlüssel immer nur einmal auftaucht.
# 
# Wenn man aber eine Selektion auf einem Attribut A mit m verschiedenen Werten ausführt, ist der Selektivitätsfaktor:
# 
# - sf = (|R| / m) / |R| = 1/m
# 
# Wenn man beispielsweise eine Spalte mit 10 unterschiedlichen Werten hat und eine Selektion auf einem Wert ausführt, kann man davon ausgehen, dass im Schnitt 1/m Werte herauskommen. Dies ist nur eine Schätzung!
# 
# <br>
# - Join:
# Beim Equijoin zwischen R und S über Fremdschlüssel in S ist der Selektivitätsfaktor:
# 
# - sf = 1 / |R|
# - „Beweis“: sf = |R ⋈ S| / (|R x S|) = |S| / (|R| · |S|)
#     Da man einen Equijoin über Fremdschlüssel durchführt, ist die Anzahl der Ausgabetupel gleich der Anzahl der Tupel in S. Somit kann man S aus |S| / (|R| · |S|) wegstreichen und es ergibt sich der Selektivitätsfaktor sf = 1 / |R|.
# 
# 
# 
# ### Selinger-style“ Optimization
# 
# Zum Vorherigen gibt es ein Paper aus den 70er Jahren IBM. Im folgenden kann man erkennen wie es vom Research Team dargestellt wird:
# 
# ![](selinger_style1.jpg)
# 
# ![](selinger_style2.jpg)
# 
# 
# 
# ### Join Selektivität (Selinger Style) 
# 
# ![](selinger_style3.jpg)
# 
# Wir interessieren uns jetzt besonders für die Join Selektivität. Dazu folgende Anfrage als Beispiel:
# 
# - SELECT * FROM cust, order WHERE cust.ID = order.custID
# 
# Die Kardinalität von customerID (cust.ID) ist die Anzahl von customer (|cust|), weil es ein Schlüssel ist. 
# 
# - DISTINCT cust.ID = |cust|
# 
# Die order-customer-ID (oder.custID) ist kleiner gleich der Anzahl der customer (cust), weil wir weniger Bestellungen (orders) als Kunden (cust) haben. 
# 
# - DISTINCT order.custID ≤ |cust|
# 
# Dann müssen wir nach der Formel aus dem Paper das Maximum der beiden Kardinalitäten nehmen. Es ergibt sich ein Selektivitätsfaktor von:
# 
# - sf = 1/|cust|
# 
# Der Join von customer (cust) und order gibt somit die gleiche Anzahl an Tupeln zurück wie die Anzahl an Tupeln in order. 
# 
# - |cust ⋈ order| = 1/|cust| * |cust| * |order| = |order|
# 
# 
# 
# ### Modelle zum besseren Schätzen der Selektivität
# 
# Man kann das Schätzen der Selektivität auf unterschiedliche Weisen verbessern. <br>
# Eine Möglichkeit das Schätzen zu verbessern, wäre es eine Gleichverteilung der Werte anzunehmen sodass man die Minimum und Maximumwerte kennt. Bei einer ungleichen Verteilung ("skew") ist die Abschätzung schwierig und eher schlecht. <br>
# Dann könnte man ein Histogramm zur Hilfe nehmen. Parametrisierte Größen vereinfachen das Schätzen. Die Güte der Abschätzung hängt von Histogrammtyp und der Histogrammgröße ab. Außerdem ist das Garantieren der Aktualität sehr aufwändig. <br>
# Eine weitere Möglichkeit ist das Sampling. Dabei schaut man sich eine repräsentative Teilmenge der Relation an und schließt daraus auf die Verteilung der Werte. Parametrisierte Größen sind hierbei schwierig zu finden. Die Güte hängt von der Samplingmethode und der Samplegröße ab. Außerdem ist die Aktualität wieder von Bedeutung.
# 
# 
# 
# ### Beispiel zu Histogrammen
# 
# ![](histogramm.jpg)
# 
# ```
# SELECT *
# FROM product p, sales S
# WHERE p.id=s.p_id and
# p.price > 100 
# ```
# 
# Gegeben ist ein Histogramm mit 3300 Produkten und einer Preisspanne von 0 bis 1000. Zu jedem Bucket in der Preisspanne wird angegeben wie viele Produkte darin enthalten sind. Zudem ist eine sales Relation mit einer Millionen Einträgen gegeben. <br>
# <br>
# Angenommen es findet eine Gleichverteilung statt. Dann ist der Preis gleichverteilt zwischen 0 und 1000. Aufgrund unserer Selektionsbedingung (p.price > 100) suchen wir nach allen Produkten, die mehr als 100 Kosten. Es bleiben genau 900 Produkte übrig. Also kommen 900 von 1000 Einträgen weiter und man erhält eine Selektivität von 900/1000 = 9/10. Am Ende werden somit 9/10 * 3300 ≈ 3000 Produkte erwartet, die man noch zusätzlich mit der sales Relation joint. <br>
# <br>
# Wenn man weiß wie das Histogramm tatsächlich aussieht, würde man wissen, dass es insgesamt nur 5 Produkte gibt, die über 100 kosten. Die Selektivität der Bedingung ist dann 5/3000 ≈ 0.0015. Somit deutlich geringer als zuvor.  
# 
# 

# ### Kosten – Weitere Komplikationen
# Es gibt weitere Komplikationen:<br>
# Was passiert mit den Kosten, wenn man bestimmte Operationen parallel ausführen kann? Die Kosten aller Operatoren können somit nicht addiert werden.<br>
# Oder der Hauptspeicher bietet Möglichkeiten wie Pufferung und Caching. Damit kann man die Kosten für bestimmte Operatoren noch weiter verringern. <br>
# Die I/O Kosten (Lesen einer Seite) könnten auch gegenüber den CPU Kosten einen ganz anderen Faktor spielen.<br>
# Vielleicht hat man mehrere Nutzer (Multiuser), die gleichzeitig arbeiten und man möchte so viele Nutzer wie möglich zu behandeln. Vielleicht möchte man auch die Antwortzeit der Nutzer verkleinern und müsste anders reagieren. <br>
# <br>
# Die Kostenmodelle sind also hochkomplex. In diesem Bereich wird immernoch sehr viel Forschung betrieben. Der beste Optimierer wurde bis heute noch nicht gefunden. 
# 
# 
# 
# 
# ### Ausblick auf DBS II
# In DBS II geht es mit folgenden Themen weiter: 
# - diverse Algorithmen für einzelne Operatoren, insbesondere bei Joins und Sortierungen. 
# - Kostenmodelle/Kostenschätzung
# - Optimale Joinreihenfolge: Dynamische Programmierung
# - Physische Anfragepläne und Pipelining
# 
# Hier sieht man Tabellen mit denen man schauen kann, welche Pläne für welche Kombinationen gut funktionieren. Alle Punkte in diesen Diagrammen sind Pläne, die infrage kommen, für bestimmte Konstellationen von diesen Tabellen. 
# ![](ausblick.jpg)

# ## Multiple Choice
# 
# - Die hier verwendete Version des Multiple-Choice-Trainers von EILD.nrw wird nur in das JupyterBook eingebunden und nicht selbst gehostet. Der Multiple-Choice-Trainer wird durch GitHub-Pages gehostet. 
# - Alle Fragen und Kategorien befinden sich zurzeit in Überarbeitung und sind nicht final. 

# In[1]:


from IPython.display import IFrame

url = "https://lejuliennn.github.io/mct-trainer/#/quiz/categories/bearbeitung"
IFrame(src=url, width='100%', height=800)


# In[ ]:




