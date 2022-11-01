#!/usr/bin/env python
# coding: utf-8

# # Transaktionsmanagement
# ![title](transaktionen_img/cartoon.jpg)
# 
# Motivation - Transaktionsmanagement
# <br><br>
# ■ Annahmen bisher
# <br>
# □ Isolation: Nur ein Nutzer greift auf die Datenbank zu
# <br>
# – Lesend
# <br>
# – Schreibend
# <br>
# □ In Wahrheit: Viele Nutzer und Anwendungen lesen und schreiben gleichzeitig.
# <br>
# □ Atomizität
# <br>
# – Anfragen und Updates bestehen aus einer einzigen, atomaren Aktion. DBMS können nicht mitten in dieser Aktion ausfallen.
# <br>
# – In Wahrheit: Auch einfache Anfragen bestehen oft aus mehreren Teilschritten.
# <br><br>
# Motivierendes Beispiel
# 
# |**Kontostand: 500**|&#xfeff;|
# |---|---|
# |**Philipp**|**Sarah**|
# |&#xfeff;|read(K,y)|
# |read(K,x)|&#xfeff;|
# |x:=x+200|&#xfeff;|
# |write(x,K)|&#xfeff;|
# |commit|&#xfeff;|
# |&#xfeff;|y:=y-100|
# |&#xfeff;|write(y,K)|
# |&#xfeff;|commit|
# |**Kontostand: 400**|&#xfeff;|
# 

# ## Transaktionen
# 
# ### Die Transaktion
# Eine Transaktion ist eine Folge von Operationen (Aktionen), die die Datenbank von einem konsistenten Zustand in einen konsistenten (eventuell veränderten) Zustand überführt, wobei das ACID-Prinzip eingehalten werden muss.
# 
# ### Transaktionen – Historie
# ■ In alten DBMS kein Formalismus über Transaktionen
# <br>
# □ Nur Tricks
# <br><br>
# ■ Erster Formalismus in den 80ern
# <br>
# □ System R mit Jim Gray
# <br>
# □ Erste (ineffiziente) Implementierung
# <br>
# □ ACM Turing Award
# <br>
# – For seminal contributions to database and transaction processing research and technical leadership in system implementation from research prototypes to commercial products.
# <br><br>
# ■ ARIES Project (IBM Research)
# <br>
# □ Algorithms for Recovery and Isolation Exploiting Semantics
# <br>
# □ Effiziente Implementierungen
# <br>
# □ C. Mohan
# <br><br>
# ■ Transaktionen auch in verteilten Anwendungen und Services
# <br>
# ![title](transaktionen_img/jim_gray.jpg)
# <br>
# ![title](transaktionen_img/c_mohan.jpg)
# 
# ### ACID
# ■ Atomicity (Atomarität)
# <br>
# □ Transaktion wird entweder ganz oder gar nicht ausgeführt.
# <br><br>
# ■ Consistency (Konsistenz oder auch Integritätserhaltung)
# <br>
# □ Datenbank ist vor Beginn und nach Beendigung einer Transaktion jeweils in einem konsistenten Zustand.
# <br><br>
# ■ Isolation (Isolation)
# <br>
# □ Transaktion, die auf einer Datenbank arbeitet, sollte den „Eindruck“ haben, dass sie allein auf dieser Datenbank arbeitet.
# <br><br>
# ■ Durability (Dauerhaftigkeit / Persistenz)
# <br>
# □ Nach erfolgreichem Abschluss einer Transaktion muss das Ergebnis dieser Transaktion „dauerhaft“ in der Datenbank gespeichert werden.
# 
# ### Beispielszenarien
# ■ Platzreservierung für Flüge gleichzeitig aus vielen Reisebüros
# <br>
# □ Platz könnte mehrfach verkauft werden, wenn mehrere Reisebüros den Platz als verfügbar identifizieren.
# <br><br>
# ■ Überschneidende Konto-Operationen einer Bank
# <br>
# □ Beispiele später
# <br><br>
# ■ Statistische Datenbankoperationen
# <br>
# □ Ergebnisse sind verfälscht, wenn während der Berechnung Daten geändert werden.
# 
# ### Beispiel – Serialisierbarkeit
# ■ Fluege(Flugnummer, Datum, Sitz, besetzt)
# <br>
# ■ chooseSeat() sucht nach freiem Platz und besetzt ihn gegebenenfalls
# ```
# EXEC SQL BEGIN DECLARE SECTION;
#     int flug;
#     char date[10];
#     char seat[3];
#     int occ;
# EXEC SQL END DECLARE SECTION;
# void chooseSeat() {
# /* Nutzer nach Flug, Datum und Sitz fragen */
#     EXEC SQL SELECT besetzt INTO :occ FROM Fluege
#         WHERE Flugnummer=:flug
#         AND Datum=:date AND Sitz=:seat;
# if(!occ) {
#         EXEC SQL UPDATE Fluege SET besetzt=TRUE
#     WHERE Flugnummer=:flight AND Datum=:date AND Sitz=:seat;
#         }
#     else …
# }
# ```
# ->Embedded SQL
# 
# ### Beispiel – Serialisierbarkeit
# ■ Problem: Funktion wird von mehreren Usern zugleich aufgerufen
# 
# |Schedule|&#xfeff;|
# |---|---|
# |User 1 findet leeren Platz|&#xfeff;|
# |&#xfeff;|User 2 findet leeren Platz|
# |User 1 besetzt Platz|&#xfeff;|
# |&#xfeff;|User 2 besetzt Platz|
# 
# ■ Beide User glauben den Platz reserviert zu haben.
# <br><br>
# ■ Lösung gleich
# <br>
# □ Serielle Schedules
# <br>
# □ Serialisierbare Schedules
# 
# ### Beispiel - Atomizität
# ■ Problem: Eine Transaktion kann Datenbank in inkonsistenten Zustand hinterlassen.
# <br>
# □ Softwarefehler / Hardwarefehler
# ```
# EXEC SQL BEGIN SECTION;
#     int konto1, konto2;
#     int kontostand;
#     int betrag;
# EXEC SQL END DECLARE SECTION;
# void transfer() {
# /* User nach Konto1, Konto2 und Betrag fragen */
#     EXEC SQL SELECT Stand INTO :kontostand FROM Konten
#         WHERE KontoNR=:konto1;
#         If (kontostand >= betrag) {
#     EXEC SQL UPDATE Konten
#         SET Stand=Stand+:betrag
#         WHERE KontoNR=:konto2;
#     EXEC SQL UPDATE Konten
#         SET Stand=Stand-:betrag
#         WHERE KontoNR=:konto1;
#     } else /* Fehlermeldung */
# }
# ```
# ->Problem: Systemabsturz hier
# <br>
# ->Lösung: Atomizität
# 
# ### Probleme im Mehrbenutzerbetrieb
# ■ Abhängigkeiten von nicht freigegebenen Daten: Dirty Read
# <br><br>
# ■ Inkonsistentes Lesen: Nonrepeatable Read
# <br><br>
# ■ Berechnungen auf unvollständigen Daten: Phantom-Problem
# <br><br>
# ■ Verlorengegangenes Ändern: Lost Update
# 
# ### Dirty Read
# 
# |T1|T2|
# |---|---|
# |read(A,x)|&#xfeff;|
# |x:=x+100|&#xfeff;|
# |write(x,A)|&#xfeff;|
# |&#xfeff;|read(A,x)|
# |&#xfeff;|read(B,y)|
# |&#xfeff;|y:=y+x|
# |&#xfeff;|write(y,B)|
# |&#xfeff;|commit|
# |abort|&#xfeff;|
# 
# Problem: T2 liest den veränderten A-Wert, diese Änderung ist aber nicht endgültig, sondern sogar ungültig.
# <br>
# Folie nach Kai-Uwe Sattler (TU Ilmenau)
# 
# ### Nonrepeatable Read
# ■ Nicht-wiederholbares Lesen
# <br><br>
# ■ Beispiel:
# <br>
# □ Zusicherung: x = A + B + C am Ende der Transaktion T1
# <br>
# □ x, y, z seien lokale Variablen
# 
# |T1|T2|
# |---|---|
# |read(A,x)|&#xfeff;|
# |&#xfeff;|read(A,y)|
# |&#xfeff;|y:=y/2|
# |&#xfeff;|write(y,A)|
# |&#xfeff;|read(C,z)|
# |&#xfeff;|z:=z+y|
# |&#xfeff;|write(z,C)|
# |&#xfeff;|commit|
# |read(B,y)|&#xfeff;|
# |x:=x+y|&#xfeff;|
# |read(C,z)|&#xfeff;|
# |x:=x+z|&#xfeff;|
# |commit|&#xfeff;|
# 
# Problem: A hat sich im Laufe der Transaktion geändert.
# <br>
# x = A + B + C gilt nicht mehr
# <br>
# Beispiel nach Kai-Uwe Sattler (TU Ilmenau)
# 
# ### Das Phantom-Problem
# 
# |T1|T2|
# |---|---|
# |SELECT COUNT(*)<br>INTO X<br>FROM Mitarbeiter|&#xfeff;|
# |&#xfeff;|INSERT INTO Mitarbeiter<br>VALUES (‚Meier‘, 50000, …)|
# |&#xfeff;|commit|
# |UPDATE Mitarbeiter<br>SET Gehalt = Gehalt +10000/X|&#xfeff;|
# |commit|&#xfeff;|
# 
# 
# UPDATE Mitarbeiter
# SET Gehalt = Gehalt +10000/X
# commit
# Problem: Meier geht nicht in die Gehaltsberechnung ein. Meier ist das Phantom.
# <br>
# ![title](transaktionen_img/phantom.jpg)
# <br>
# Beispiel nach Kai-Uwe Sattler (TU Ilmenau)
# 
# ### Lost Update
# 
# |T1|T2|A|
# |---|---|---|
# |read(A,x)|&#xfeff;|10|
# |&#xfeff;|read(A,x)|10|
# |x:=x+1|&#xfeff;|10|
# |&#xfeff;|x:=x+1|10|
# |write(x,A)|&#xfeff;|11|
# |&#xfeff;|write(x,A)|11|
# 
# Problem: Die Erhöhung von T1 wird nicht berücksichtigt.
# <br>
# Folie nach Kai-Uwe Sattler (TU Ilmenau)
# 
# ### Transaktionen in SQL
# ■ Idee: Gruppierung mehrerer Operationen / Anfragen in eine Transaktion
# <br>
# □ Ausführung atomar (per Definition)
# <br>
# □ Ausführung serialisierbar (per SQL Standard)
# <br>
# – Kann aufgeweicht werden (Isolationsstufen)
# <br><br>
# ■ Ein SQL Befehl entspricht einer Transaktion
# <br>
# □ Ausgelöste TRIGGER werden ebenfalls innerhalb der Transaktion ausgeführt.
# <br><br>
# ■ Beginn einer Transaktion: START TRANSACTION
# <br><br>
# ■ Ende einer Transaktion (falls mit START TRANSACTION gestartet)
# <br>
# □ COMMIT signalisiert erfolgreiches Ende der Transaktion
# <br>
# □ ROLLBACK oder ABORT signalisiert Scheitern der Transaktion
# <br>
# – Erfolgte Änderungen werden rückgängig gemacht.
# <br>
# – Kann auch durch das DBMS ausgelöst werden: Anwendung muss entsprechende Fehlermeldung erkennen.
# 
# ### Isolationsebenen
# 
#  Aufweichung von ACID in SQL-92: Isolationsebenen
# ```
# set transaction
# [ { read only | read write }, ]
# [isolation level {
#     read uncommitted |
#     read committed |
#     repeatable read |
#     serializable }, ]
# [ diagnostics size ...]
# ```
# ■ Kann pro Transaktion angegeben werden
# <br><br>
# ■ Standardeinstellung:
# ```
# set transaction read write,
# isolation level serializable
# ```
# ■ Andere Ebenen als Hilfestellung für das DBMS zur Effizienzsteigerung
# 
# ### Bedeutung der Isolationsebenen
# ```
# read uncommitted
# ```
# □ Schwächste Stufe: Zugriff auf nicht geschriebene Daten
# <br>
# □ Falls man schreiben will: read write angeben (default ist hier ausnahmsweise read only)
# <br>
# □ Statistische und ähnliche Transaktionen (ungefährer Überblick, nicht korrekte Werte)
# <br>
# □ Keine Sperren: Effizient ausführbar, keine anderen Transaktionen werden behindert
# ```
# read committed
# ```
# □ Nur Lesen endgültig geschriebener Werte, aber nonrepeatable read möglich
# ```
# repeatable read
# ```
# □ Kein nonrepeatable read, aber Phantomproblem kann auftreten
# ```
# serializable
# ```
# □ Garantierte Serialisierbarkeit (default)
# <br>
# □ Transaktion sieht nur Änderungen, die zu Beginn der Transaktion committed waren (und eigene Änderungen).
# 
# ### Isolationsebenen – Übersicht
# 
# |Isolationsebene|Dirty Read|Nonrepeatable Read|Phantom Read|Lost Update|
# |---------------|----------|------------------|------------|-----------|
# |Read Uncommited|+|+|+|+|
# |Read Committed|-|+|+|-|
# |Repeatable Read|-|-|+|-|
# |Serializable|-|-|-|-|

# ## Serialisierbarkeit
# 
# ### Seriell vs. Parallel
# ■ Grundannahme: Korrektheit
# <br>
# □ Jede Transaktion, isoliert ausgeführt auf einem konsistenten Zustand der Datenbank, hinterlässt die Datenbank
# wiederum in einem konsistenten Zustand.
# <br><br>
# ■ Einfache Lösung aller obigen Probleme:
# <br>
# □ Alle Transaktionen seriell ausführen.
# <br><br>
# ■ Aber: Parallele Ausführung bietet Effizienzvorteile
# <br>
# □ „Long-Transactions“ über mehrere Stunden hinweg
# <br>
# □ Cache ausnutzen
# <br><br>
# ■ Deshalb: Korrekte parallele Pläne (Schedules) finden
# <br>
# □ Korrekt = Serialisierbar
# 
# 
# ### Schedules
# 
# |Schritt|T1|T3|
# |-------|---|---|
# |1.|Begin TA|Begin TA|
# |2.|read(A,a1)|read(A,a2)|
# |3.|a1 := a1 – 50|a2 := a2 – 100|
# |4.|write(A,a1)|write(A,a2)|
# |5.|read(B,b1)|read(B,b2)|
# |6.|b1 := b1 + 50|b2 := b2 + 100|
# |7.|write(B,b1)|write(B,b2)|
# |8.|commit|commit|
# 
# ■ Ein Schedule ist eine geordnete Abfolge wichtiger Aktionen, die von einer oder mehreren Transaktionen durchgeführt werden.
# <br>
# □ Wichtige Aktionen: READ und WRITE eines Elements
# <br>
# □ „Ablaufplan“ für Transaktion, bestehend aus Abfolge von Transaktionsoperationen
# 
# #### Serialisierbarkeit
# ■ Schedule
# <br>
# □ „Ablaufplan“ für Transaktionen, bestehend aus Abfolge von Transaktionsoperationen
# <br><br>
# ■ Serieller Schedule
# <br>
# □ Schedule in dem Transaktionen hintereinander ausgeführt werden
# <br><br>
# ■ Serialisierbarer Schedule
# <br>
# □ Es existiert ein serieller Schedule mit identischem Effekt.
# 
# #### Beispiel 1
# 
# |Serieller Schedule|&#xfeff;|&#xfeff;| 
# |------------------|--------|--------|
# |**Schritt**|**T1**|**T2**|
# |1.|BOT|&#xfeff;|
# |2.|read(A)|&#xfeff;|
# |3.|write(A)|&#xfeff;|
# |4.|read(B)|&#xfeff;|
# |5.|write(B)|&#xfeff;|
# |6.|commit|&#xfeff;|
# |7.|&#xfeff;|BOT|
# |8.|&#xfeff;|read(C)|
# |9.|&#xfeff;|write(C)|
# |10.|&#xfeff;|read(A)|
# |11.|&#xfeff;|write(A)|
# |12.|&#xfeff;|commit|
# 
# 
# 
# |Serialisierbarer Schedule|&#xfeff;|&#xfeff;|
# |---|---|---|
# |**Schritt**|**T1**|**T2**|
# |1.|BOT|&#xfeff;|
# |2.|read(A)|&#xfeff;|
# |3.|&#xfeff;|BOT|
# |4.|&#xfeff;|read(C)|
# |5.|write(A)|&#xfeff;|
# |6.|&#xfeff;|write(C)|
# |7.|read(B)|&#xfeff;|
# |8.|write(B)|&#xfeff;|
# |9.|commit|&#xfeff;|
# |10.|&#xfeff;|read(A)|
# |11.|&#xfeff;|write(A)|
# |12.|&#xfeff;|commit|
# 
# 
# #### Beispiel 2
# 
# |Serialisierbar?|&#xfeff;|&#xfeff;|
# |---------------|--------|--------|
# |**Schritt**|**T1**|**T3**|
# |1.|BOT|&#xfeff;|
# |2.|read(A)|&#xfeff;|
# |3.|write(A)|&#xfeff;|
# |4.|&#xfeff;|BOT|
# |5.|&#xfeff;|read(A)|
# |6.|&#xfeff;|write(A)|
# |7.|&#xfeff;|read(B)|
# |8.|&#xfeff;|write(B)|
# |9.|&#xfeff;|commit|
# |10.|read(B)|&#xfeff;|
# |11.|write(B)|&#xfeff;|
# |12.|commit|&#xfeff;|
# 
# #### Beispiel 3
# Aufgabe: Suche äquivalenten seriellen Schedule.
# 
# |Schritt|T1|T3|
# |-------|---|---|
# |1.|BOT|&#xfeff;|
# |2.|read(A,a1)|&#xfeff;|
# |3.|a1 := a1 – 50|&#xfeff;|
# |4.|write(A,a1)|&#xfeff;|
# |5.|&#xfeff;|BOT|
# |6.|&#xfeff;|read(A,a2)|
# |7.|&#xfeff;|a2 := a2 – 100|
# |8.|&#xfeff;|write(A,a2)|
# |9.|&#xfeff;|read(B,b2)|
# |10.|&#xfeff;|b2 := b2 + 100|
# |11.|&#xfeff;|write(B,b2)|
# |12.|&#xfeff;|commit|
# |13.|read(B,b1)|&#xfeff;|
# |14.|b1 := b1 + 50|&#xfeff;|
# |15.|write(B,b1)|&#xfeff;|
# |16.|commit|&#xfeff;|
# 
# Effekt: A = A − 150, B = B + 150
# 
# |Schritt|T1|T3|
# |-------|---|---|
# |1.|BOT|&#xfeff;|
# |2.|read(A,a1)|&#xfeff;|
# |3.|a1 := a1 – 50|&#xfeff;|
# |4.|write(A,a1)|&#xfeff;|
# |5.|read(B,b1)|&#xfeff;|
# |6.|b1 := b1 + 50|&#xfeff;|
# |7.|write(B,b1)|&#xfeff;|
# |8.|commit|&#xfeff;|
# |9.|&#xfeff;|BOT|
# |10.|&#xfeff;|read(A,a2)|
# |11.|&#xfeff;|a2 := a2 – 100|
# |12.|&#xfeff;|write(A,a2)|
# |13.|&#xfeff;|read(B,b2)|
# |14.|&#xfeff;|b2 := b2 + 100|
# |15.|&#xfeff;|write(B,b2)|
# |16.|&#xfeff;|commit|
# 
# Effekt: A = A − 150, B = B + 150
# 
# #### Beispiel 4
# 
# |Schritt|T1|T3|A|B|
# |-------|---|---|---|---|
# |1.|BOT|&#xfeff;|100|100|
# |2.|read(A,a1)|&#xfeff;|&#xfeff;|&#xfeff;|
# |3.|a1 := a1 – 50|&#xfeff;|50|&#xfeff;|
# |4.|write(A,a1)|&#xfeff;|&#xfeff;|&#xfeff;|
# |5.|&#xfeff;|BOT|&#xfeff;|&#xfeff;|
# |6.|&#xfeff;|read(A,a2)|&#xfeff;|&#xfeff;|
# |7.|&#xfeff;|a2 := a2 * 1.03|51,5|&#xfeff;|
# |8.|&#xfeff;|write(A,a2)|&#xfeff;|&#xfeff;|
# |9.|&#xfeff;|read(B,b2)|&#xfeff;|&#xfeff;|
# |10.|&#xfeff;|b2 := b2 * 1.03|&#xfeff;|103|
# |11.|&#xfeff;|write(B,b2)|&#xfeff;|&#xfeff;|
# |12.|&#xfeff;|commit|&#xfeff;|&#xfeff;|
# |13.|read(B,b1)|&#xfeff;|&#xfeff;|&#xfeff;|
# |14.|b1 := b1 + 50|&#xfeff;|&#xfeff;|153|
# |15.|write(B,b1)|&#xfeff;|&#xfeff;|&#xfeff;|
# |16.|commit|&#xfeff;|&#xfeff;|&#xfeff;|
# 
# 1. Effekt: A = (A − 50) * 1.03
# <br>
# B = B * 1.03 + 50
# 
# |Schritt|T1|T3|A|B|
# |-------|---|---|---|---|
# |1.|BOT|&#xfeff;|100|100|
# |2.|read(A,a1)|&#xfeff;|&#xfeff;|&#xfeff;|
# |3.|a1 := a1 – 50|&#xfeff;|50|&#xfeff;|
# |4.|write(A,a1)|&#xfeff;|&#xfeff;|&#xfeff;|
# |5.|read(B,b1)|&#xfeff;|&#xfeff;|&#xfeff;|
# |6.|b1 := b1 + 50|&#xfeff;|&#xfeff;|150|
# |7.|write(B,b1)|&#xfeff;|&#xfeff;|&#xfeff;|
# |8.|Commit|&#xfeff;|&#xfeff;|&#xfeff;|
# |9.|&#xfeff;|BOT|&#xfeff;|&#xfeff;|
# |10.|&#xfeff;|read(A,a2)|&#xfeff;|&#xfeff;|
# |11.|&#xfeff;|a2 := a2 * 1.03|51,5|&#xfeff;|
# |12.|&#xfeff;|write(A,a2)|&#xfeff;|&#xfeff;|
# |13.|&#xfeff;|read(B,b2)|&#xfeff;|&#xfeff;|
# |14.|&#xfeff;|b2 := b2 * 1.03|&#xfeff;|154,5|
# |15.|&#xfeff;|write(B,b2)|&#xfeff;|&#xfeff;|
# |16.|&#xfeff;|commit|&#xfeff;|&#xfeff;|
# 
# 
# 2. Effekt: A = (A − 50) * 1.03
# <br>
# B = (B + 50) * 1.03
# 
# #### Beispiel 5
# |Schritt|T1|T3|A|B|
# |-------|---|---|---|---|
# |1.|BOT|&#xfeff;|100|100|
# |2.|read(A,a1)|&#xfeff;|&#xfeff;|&#xfeff;|
# |3.|a1 := a1 – 50|&#xfeff;|50|&#xfeff;|
# |4.|write(A,a1)|&#xfeff;|&#xfeff;|&#xfeff;|
# |5.|&#xfeff;|BOT|&#xfeff;|&#xfeff;|
# |6.|&#xfeff;|read(A,a2)|&#xfeff;|&#xfeff;|
# |7.|&#xfeff;|a2 := a2 * 1.03|51,5|&#xfeff;|
# |8.|&#xfeff;|write(A,a2)|&#xfeff;|&#xfeff;|
# |9.|&#xfeff;|read(B,b2)|&#xfeff;|&#xfeff;|
# |10.|&#xfeff;|b2 := b2 * 1.03|&#xfeff;|103|
# |11.|&#xfeff;|write(B,b2)|&#xfeff;|&#xfeff;|
# |12.|&#xfeff;|commit|&#xfeff;|&#xfeff;|
# |13.|read(B,b1)|&#xfeff;|&#xfeff;|&#xfeff;|
# |14.|b1 := b1 + 50|&#xfeff;|&#xfeff;|153|
# |15.|write(B,b1)|&#xfeff;|&#xfeff;|&#xfeff;|
# |16.|commit|&#xfeff;|&#xfeff;|&#xfeff;|
# 
# Effekt: A = (A − 50) * 1.03
# <br>
# B = B * 1.03 + 50
# 
# 
# |Schritt|T1|T3|A|B|
# |-------|---|---|---|---|
# |1.|&#xfeff;|BOT|100|100|
# |2.|&#xfeff;|read(A,a2)|&#xfeff;|&#xfeff;|
# |3.|&#xfeff;|a2 := a2 * 1.03|103|&#xfeff;|
# |4.|&#xfeff;|write(A,a2)|&#xfeff;|&#xfeff;|
# |5.|&#xfeff;|read(B,b2)|&#xfeff;|&#xfeff;|
# |6.|&#xfeff;|b2 := b2 * 1.03|&#xfeff;|103|
# |7.|&#xfeff;|write(B,b2)|&#xfeff;|&#xfeff;|
# |8.|&#xfeff;|commit|&#xfeff;|&#xfeff;|
# |9.|BOT|&#xfeff;|&#xfeff;|&#xfeff;|
# |10.|read(A,a1)|&#xfeff;|&#xfeff;|&#xfeff;|&#xfeff;|
# |11.|a1 := a1 – 50|&#xfeff;|53|&#xfeff;|
# |12.|write(A,a1)|&#xfeff;|&#xfeff;|&#xfeff;|
# |13.|read(B,b1)|&#xfeff;|&#xfeff;|&#xfeff;|
# |14.|b1 := b1 + 50|&#xfeff;|&#xfeff;|153|
# |15.|write(B,b1)|&#xfeff;|&#xfeff;|&#xfeff;|
# 
# 
# Effekt: A = A * 1.03 − 50
# <br>
# B = B * 1.03 + 50
# 
# #### Schedules
# 
# |Schritt|T1|T3|
# |-------|---|---|
# |1.|BOT||
# |2.|read(A)|&#xfeff;|
# |3.|write(A)|&#xfeff;|
# |4.|&#xfeff;|BOT|
# |5.|&#xfeff;|read(A)|
# |6.|&#xfeff;|write(A)|
# |7.|&#xfeff;|read(B)|
# |8.|&#xfeff;|write(B)|
# |9.|&#xfeff;|commit|
# |10.|read(B)|&#xfeff;|
# |11.|write(B)|&#xfeff;|
# |12.|commit|&#xfeff;|
# 
# Serialisierbar? Nein,denn Effekt entspricht weder dem seriellen Schedule T1T3 noch dem seriellen Schedule T3T1
# <br><br>
# Serialisierbar? Nein, obwohl es konkrete Beispiele solcher Transaktionen gibt, für die es einen äquivalenten seriellen Schedule gibt. Man nimmt immer das Schlimmste an.
# 
# #### Beispiel 9
# Nochmal die beiden seriellen Schedules. Ist Ihnen etwas aufgefallen?
# 
# |Schritt|T1|T3|A|B|
# |-------|---|---|---|---|
# |1.|BOT|&#xfeff;|100|100|
# |2.|read(A,a1)|&#xfeff;|&#xfeff;|&#xfeff;|
# |3.|a1 := a1 – 50|&#xfeff;|50|&#xfeff;|
# |4.|write(A,a1)|&#xfeff;|&#xfeff;|&#xfeff;|
# |5.|&#xfeff;|BOT|&#xfeff;|&#xfeff;|
# |6.|&#xfeff;|read(A,a2)|&#xfeff;|&#xfeff;|
# |7.|&#xfeff;|a2 := a2 * 1.03|51,5|&#xfeff;|
# |8.|&#xfeff;|write(A,a2)|&#xfeff;|&#xfeff;|
# |9.|&#xfeff;|read(B,b2)|&#xfeff;|&#xfeff;|
# |10.|&#xfeff;|b2 := b2 * 1.03|&#xfeff;|103|
# |11.|&#xfeff;|write(B,b2)|&#xfeff;|&#xfeff;|
# |12.|&#xfeff;|commit|&#xfeff;|&#xfeff;|
# |13.|read(B,b1)|&#xfeff;|&#xfeff;|&#xfeff;|
# |14.|b1 := b1 + 50|&#xfeff;|&#xfeff;|153|
# |15.|write(B,b1)|&#xfeff;|&#xfeff;|&#xfeff;|
# |16.|commit|&#xfeff;|&#xfeff;|&#xfeff;|
# 
# |Schritt|T1|T3|A|B|
# |-------|---|---|---|---|
# |1.|BOT|&#xfeff;|100|100|
# |2.|read(A,a1)|&#xfeff;|&#xfeff;|&#xfeff;|
# |3.|a1 := a1 – 50|&#xfeff;|50|&#xfeff;|
# |4.|write(A,a1)|&#xfeff;|&#xfeff;|&#xfeff;|
# |5.|read(B,b1)|&#xfeff;|&#xfeff;|&#xfeff;|
# |6.|b1 := b1 + 50|&#xfeff;|&#xfeff;|150|
# |7.|write(B,b1)|&#xfeff;|&#xfeff;|&#xfeff;|
# |8.|Commit|&#xfeff;|&#xfeff;|&#xfeff;|
# |9.|&#xfeff;|BOT|&#xfeff;|&#xfeff;|
# |10.|&#xfeff;|read(A,a2)|&#xfeff;|&#xfeff;|
# |11.|&#xfeff;|a2 := a2 * 1.03|51,5|&#xfeff;|
# |12.|&#xfeff;|write(A,a2)|&#xfeff;|&#xfeff;|
# |13.|&#xfeff;|read(B,b2)|&#xfeff;|&#xfeff;|
# |14.|&#xfeff;|b2 := b2 * 1.03|&#xfeff;|154,5|
# |15.|&#xfeff;|write(B,b2)|&#xfeff;|&#xfeff;|
# |16.|&#xfeff;|commit|&#xfeff;|&#xfeff;|
# 
# T1T3 ≠ T3T1 
# <br>
# Ist das schlimm?

# ## Konfliktserialisierbarkeit
# 
# ### Konflikte
# ■ Bedingung für Serialisierbarkeit: „Konfliktserialisierbarkeit“
# <br><br>
# ■ Konfliktserialisierbarkeit wird von den meisten DBMS verlangt (und hergestellt)
# <br><br>
# ■ Konflikt herrscht zwischen zwei Aktionen eines Schedules falls die Änderung ihrer Reihenfolge das Ergebnis verändern kann.
# <br>
# □ „Kann“ - nicht muss.
# <br><br>
# ■ Neue Notation: Aktion ri(X) bzw. wi(X)
# <br>
# □ read bzw. write
# <br>
# □ TransaktionsID i
# <br>
# □ Datenbankelement X
# <br><br>
# ■ Transaktion ist eine Sequenz solcher Aktionen
# <br>
# □ r1(A)w1(A)r1(B)w1(B)
# <br><br>
# ■ Schedule einer Menge von Transaktionen ist eine Sequenz von Aktionen
# <br>
# □ Alle Aktionen aller Transaktionen müssen enthalten sein
# <br>
# □ Aktionen einer Transaktion erscheinen in gleicher Reihenfolge im Schedule
# <br><br>
# ■ Gegeben Transaktionen Ti und Tk
# <br>
# □ ri(X) und rk(X) stehen nicht in Konflikt
# <br>
# □ ri(X) und wk(Y) stehen nicht in Konflikt (falls X ≠ Y)
# <br>
# □ wi(X) und rk(Y) stehen nicht in Konflikt (falls X ≠ Y)
# <br>
# □ wi(X) und wk(Y) stehen nicht in Konflikt (falls X ≠ Y)
# <br>
# □ ri(X) und wk(X) stehen in Konflikt
# <br>
# □ wi(X) und rk(X) stehen in Konflikt
# <br>
# □ wi(X) und wk(X) stehen in Konflikt
# <br>
# – „No coincidences“: Man nimmt immer das schlimmste an. Die konkrete Ausprägung der write-Operationen ist egal.
# <br><br>
# ■ Zusammengefasst: Konflikt herrscht falls zwei Aktionen
# <br>
# □ das gleiche Datenbankelement betreffen,
# <br>
# □ und mindestens eine der beiden Aktionen ein write ist.
# 
# ### Konfliktserialisierbarkeit
# ■ Idee: So lange nicht-konfligierende Aktionen tauschen bis aus einem Schedule ein serieller Schedule wird.
# <br>
# □ Falls das klappt, ist der Schedule serialisierbar.
# <br><br>
# ■ Zwei Schedules S und S‘ heißen konfliktäquivalent, wenn die Reihenfolge aller Paare von konfligierenden Aktionen in beiden Schedules gleich ist.
# <br><br>
# ■ Ein Schedule S ist genau dann konfliktserialisierbar, wenn S konfliktäquivalent zu einem seriellen Schedule ist.<br><br>
# ■ Schedule:
# <br>
# r1(A) w1(A) r2(A) w2(A) r2(B) w2(B) r1(B) w1(B)
# <br><br>
# ■ Serieller Schedule T1T2:
# <br>
# r1(A) w1(A) r1(B) w1(B) r2(A) w2(A) r2(B) w2(B)
# <br><br>
# ■ Serieller Schedule T2T1:
# <br>
# r2(A) w2(A) r2(B) w2(B) r1(A) w1(A) r1(B) w1(B)
# 
# #### Konflikt – konfligieren
# ![title](konfliktserialisierbarkeit_img/def_konfligieren.jpg)
# 
# #### Konfliktserialisierbarkeit vs. Serialisierbarkeit
# ■ Konfliktserialisierbarkeit => Serialisierbarkeit
# <br>
# □ Beispiel zuvor: Serialisierbarkeit war „zufällig“ aufgrund spezieller Ausprägungen der Aktionen möglich.
# <br>
# □ S1: w1(Y) w1(X) w2(Y) w2(X) w3(X)
# <br>
# – Ist seriell
# <br>
# □ S2: w1(Y) w2(Y) w2(X) w1(X) w3(X)
# <br>
# – Hat (zufällig) gleichen Effekt wie S1, ist also serialisierbar.
# <br>
# – Aber: Es müssten konfligierende Aktionen getauscht werden. Welche?
# <br>
# – S2 ist also nicht konfliktserialisierbar
# <br><br>
# ■ Was fällt auf?
# <br>
# □ T3 überschreibt X sowieso -> Sichtserialisierbarkeit (nicht hier)
# 
# #### Graphbasierter Test
# ■ Konfliktgraph G(S) = (V,E) von Schedule S:
# <br>
# □ Knotenmenge V enthält alle in S vorkommende Transaktionen.
# <br>
# □ Kantenmenge E enthält alle gerichteten Kanten zwischen zwei konfligierenden Transaktionen.
# <br>
# – Kantenrichtung entspricht zeitlichem Ablauf im Schedule.
# <br><br>
# ■ Eigenschaften
# <br>
# □ S ist ein konfliktserialisierbarer Schedule gdw. der vorliegende Konfliktgraph ein azyklischer Graph ist.
# <br>
# □ Für jeden azyklischen Graphen G(S) lässt sich ein serieller Schedule S‘ konstruieren, so dass S konfliktäquivalent zu S‘ ist.
# <br>
# – D.h. S ist konfliktserialisierbar
# <br>
# – Z.B. topologisches Sortieren
# <br>
# □ Enthält der Graph Zyklen, ist der zugehörige Schedule nicht konfliktserialisierbar.
# 
# ####  Schedules
# 
# ##### Beispiel 1
# Konfliktserialisierbar ?
# 
# |Schritt|T1|T3|
# |-------|---|---|
# |1.|BOT||
# |2.|read(A)|&#xfeff;|
# |3.|write(A)|&#xfeff;|
# |4.|&#xfeff;|BOT|
# |5.|&#xfeff;|read(A)|
# |6.|&#xfeff;|write(A)|
# |7.|&#xfeff;|read(B)|
# |8.|&#xfeff;|write(B)|
# |9.|&#xfeff;|commit|
# |10.|read(B)|&#xfeff;|
# |11.|write(B)|&#xfeff;|
# |12.|commit|&#xfeff;|
# 
# ![title](konfliktserialisierbarkeit_img/graph1.jpg)
# 
# ##### Beispiel 2
# ![title](konfliktserialisierbarkeit_img/graph2.jpg)
# 
# |Schritt|T1|T2|T3|
# |-------|---|---|---|
# |1.|r(y)|&#xfeff;|&#xfeff;|
# |2.|&#xfeff;|&#xfeff;|r(u)|
# |3.|&#xfeff;|r(y)|&#xfeff;|
# |4.|w(y)|&#xfeff;|&#xfeff;|
# |5.|w(x)|&#xfeff;|&#xfeff;|
# |6.|&#xfeff;|w(x)|&#xfeff;|
# |7.|&#xfeff;|w(z)|&#xfeff;|
# |8.|&#xfeff;|&#xfeff;|w(x)|
# 
# S = r1(y) r3(u) r2(y) w1(y) w1(x) w2(x) w2(z) w3(x)
# 
# ##### Beispiel 3
# Serialisierbarer Schedule
# 
# |Schritt|T1|T2|
# |-------|---|---|
# |1.|BOT|&#xfeff;|
# |2.|read(A)|&#xfeff;|
# |3.|&#xfeff;|BOT|
# |4.|&#xfeff;|read(C)|
# |5.|write(A)|&#xfeff;|
# |6.|&#xfeff;|write(C)|
# |7.|read(B)|&#xfeff;|
# |8.|write(B)|&#xfeff;|
# |9.|commit|&#xfeff;|
# |10.|&#xfeff;|read(A)|
# |11.|&#xfeff;|write(A)|
# |12.|&#xfeff;|commit|
# 
# 
# ![title](konfliktserialisierbarkeit_img/graph3.jpg)
# 
# #### Beweis
# Konfliktgraph ist zykelfrei <=> Schedule ist konfliktserialisierbar
# <br>
# Konfliktgraph ist zykelfrei <=> Schedule ist konfliktserialisierbar
# <br>
# Leicht: Konfliktgraph hat Zykel => Schedule ist nicht konfliktserialisierbar
# <br>
# Bzw. Gegenbeispiel: T1 -> T2 -> … -> Tn -> T1
# <br>
# Konfliktgraph ist zykelfrei Þ Schedule ist konfliktserialisierbar
# <br>
# Induktion über Anzahl der Transaktionen n
# <br>
# n = 1: Graph und Schedule haben nur eine Transaktion.
# <br>
# n = n + 1:
# <br>
# Graph ist zykelfrei
# <br>
# => ∃ mindestens ein Knoten Ti ohne eingehende Kante.
# <br>
# => ∄ Aktion einer anderen Transaktion, die vor einer Aktion in Ti ausgeführt wird und mit dieser Aktion in Konflikt steht.
# <br>
# Alle Aktionen aus Ti können an den Anfang bewegt werden (Reihenfolge innerhalb Ti bleibt erhalten).
# <br>
# Restgraph ist wieder azyklisch (Entfernung von Kanten aus einem azyklischen Graph kann ihn nicht zyklisch machen).
# <br>
# Restgraph hat n-1 Transaktionen

# ## Sperrkontrolle
# 
# ### Scheduler
# ■ Der Scheduler in einem DBMS garantiert konfliktserialisierbare (also auch serialisierbare) Schedules bei gleichzeitig laufenden Transaktionen.
# <br>
# □ Komplizierte Variante: Graphbasierter Test
# <br>
# – Inkrementell?
# <br>
# □ Einfachere Variante: Sperren und Sperrprotokolle
# <br>
# – In fast allen DBMS realisiert
# <br>
# □ Idee: Transaktion sperrt Objekte der Datenbank für die Dauer der Bearbeitung
# <br>
# – Andere Transaktionen können nicht auf gesperrte Objekte zugreifen.
# <br>
# BILD
# 
# ### Sperren
# Idee: Transaktionen müssen zusätzlich zu den Aktionen auch Sperren anfordern und freigeben.
# <br>
# Bedingungen
# <br>
# Konsistenz einer Transaktion
# <br>
# Lesen oder Schreiben eines Objektes nur nachdem Sperre angefordert wurde und bevor die Sperre wieder freigegeben wurde.
# <br>
# Nach dem Sperren eines Objektes muss später dessen Freigabe erfolgen.
# <br>
# Legalität des Schedules
# <br>
# Zwei Transaktionen dürfen nicht gleichzeitig das gleiche Objekt sperren.
# <br>
# Zwei neue Aktionen
# <br>
# li(X): Transaktion i fordert Sperre für X an (lock).
# <br>
# ui(X): Transaktion i gibt Sperre auf X frei (unlock).
# <br>
# Konsistenz: Vor jedem ri(X) oder wi(X) kommt ein li(X) (mit keinem ui(X) dazwischen) und ein ui(X) danach.
# <br>
# Legalität: Zwischen li(X) und lk(X) kommt immer ein ui(X)
# 
# ### Schedules mit Sperren
# ■ Zwei Transaktionen
# <br>
# □ r1(A)w1(A)r1(B)w1(B)
# <br>
# □ r2(A)w2(A)r2(B)w2(B)
# <br><br>
# ■ Zwei Transaktionen mit Sperren
# <br>
# □ l1(A)r1(A)w1(A)u1(A)l1(B)r1(B)w1(B)u1(B)
# <br>
# □ l2(A)r2(A)w2(A)
# <br><br>
# ■ Schedule
# 
# |T1|T2|
# |---|---|
# |l1(A)r1(A)w1(A)u1(A)|&#xfeff;|
# |&#xfeff;|l2(A)r2(A)w2(A)u2(A)|
# |&#xfeff;|l2(B)r2(B)w2(B)u2(B)|
# |l1(B)r1(B)w1(B)u1(B)|&#xfeff;|
# 
# □ Legal?
# <br>
# □ Konfliktserialisierbar?
# 
# |T1|T3|A|B|
# |---|---|---|---|
# |&#xfeff;|&#xfeff;|25|25|
# |l(A); read(A,a1)|&#xfeff;|&#xfeff;|&#xfeff;|
# |a1 := a1 + 100|&#xfeff;|125|&#xfeff;|
# |write(A,a1); u(A)|&#xfeff;|&#xfeff;|
# |&#xfeff;|l(A); read(A,a2)|&#xfeff;|&#xfeff;|
# |&#xfeff;|a2 := a2 * 2|250|&#xfeff;|
# |&#xfeff;|write(A,a2); u(A)|&#xfeff;|&#xfeff;|
# |&#xfeff;|l(B); read(B,b2)|&#xfeff;|&#xfeff;|
# |&#xfeff;|b2 := b2 * 2|&#xfeff;|50|
# |&#xfeff;|write(B,b2); u(B)|&#xfeff;|&#xfeff;|
# |l(B); read(B,b1)|&#xfeff;|&#xfeff;|
# |b1 := b1 + 100|&#xfeff;|150|
# |write(B,b1); u(B)|&#xfeff;|&#xfeff;|
# 
# <br>
# Legal? Serialisierbar? Konfliktserialisierbar?
# 
# ### Freigabe durch Scheduler
# ■ Scheduler speichert Sperrinformation in Sperrtabelle
# <br>
# □ Sperren(Element, Transaktion)
# <br>
# □ Anfragen, INSERT, DELETE
# <br>
# □ Vergabe von Sperren nur wenn keine andere Sperre existiert
# <br>
# □ Alte Transaktionen
# <br>
# – l1(A)r1(A)w1(A)u1(A)l1(B)r1(B)w1(B)u1(B)
# <br>
# – l2(A)r2(A)w2(A)u2(A)l2(B)r2(B)w2(B)u2(B)
# <br>
# □ Neue Transaktionen
# <br>
# – l1(A)r1(A)w1(A)l1(B)u1(A)r1(B)w1(B)u1(B)
# <br>
# – l2(A)r2(A)w2(A)l2(B)u2(A)r2(B)w2(B)u2(B)
# <br>
# – Konsistent?
# 
# ### Schedules mit Sperren
# 
# |T1|T3|A|B|
# |---|---|---|---|
# |&#xfeff;|&#xfeff;|25|25|
# |l(A); read(A,a1)|&#xfeff;|&#xfeff;|&#xfeff;|
# |a1 := a1 + 100|&#xfeff;|125|&#xfeff;|
# |write(A,a1); l(B); u(A)|&#xfeff;|&#xfeff;|&#xfeff;|
# |&#xfeff;|l(A); read(A,a2)|&#xfeff;|&#xfeff;|
# |&#xfeff;|a2 := a2 * 2|250|&#xfeff;|
# |&#xfeff;|write(A,a2);|&#xfeff;|&#xfeff;|
# |&#xfeff;|l(B); abgelehnt!|&#xfeff;|&#xfeff;|
# |read(B,b1)|&#xfeff;|&#xfeff;|&#xfeff;|
# |b1 := b1 + 100|&#xfeff;|&#xfeff;|125|
# |write(B,b1); u(B)|&#xfeff;|&#xfeff;|&#xfeff;|
# |&#xfeff;|l(B); u(A); read(B,b2)|&#xfeff;|&#xfeff;|
# |&#xfeff;|b2 := b2 * 2|&#xfeff;|250|
# |&#xfeff;|write(B,b2); u(B)|&#xfeff;|&#xfeff;|
# 
# Legal? Serialisierbar? Konfliktserialisierbar? Zufall?
# 
# ### 2-Phasen Sperrprotokoll
# ■ 2-Phase-Locking (2PL): Einfache Bedingung an Transaktionen garantiert Konfliktserialisierbarkeit.
# <br>
# □ Alle Sperranforderungen geschehen vor allen Sperrfreigaben
# <br>
# □ Die Phasen
# <br>
# – Phase 1: Sperrphase
# <br>
# – Phase 2: Freigabephase
# <br>
# □ Wichtig: Bedingung an Transaktionen, nicht an Schedule
# 
# #### 2-Phasen Sperrprotokoll – Beispiel
# |T1|T3|A|B|
# |---|---|---|---|
# |&#xfeff;|&#xfeff;|25|25|
# |l(A); read(A,a1)|&#xfeff;|&#xfeff;|&#xfeff;|
# |a1 := a1 + 100|&#xfeff;|125|&#xfeff;|
# |write(A,a1); u(A)|&#xfeff;|&#xfeff;|
# |&#xfeff;|l(A); read(A,a2)|&#xfeff;|&#xfeff;|
# |&#xfeff;|a2 := a2 * 2|250|&#xfeff;|
# |&#xfeff;|write(A,a2); u(A)|&#xfeff;|&#xfeff;|
# |&#xfeff;|l(B); read(B,b2)|&#xfeff;|&#xfeff;|
# |&#xfeff;|b2 := b2 * 2|&#xfeff;|50|
# |&#xfeff;|write(B,b2); u(B)|&#xfeff;|&#xfeff;|
# |l(B); read(B,b1)|&#xfeff;|&#xfeff;|
# |b1 := b1 + 100|&#xfeff;|150|
# |write(B,b1); u(B)|&#xfeff;|&#xfeff;|
# 
# |T1|T3|A|B|
# |---|---|---|---|
# |&#xfeff;|&#xfeff;|25|25|
# |l(A); read(A,a1)|&#xfeff;|&#xfeff;|&#xfeff;|
# |a1 := a1 + 100|&#xfeff;|125|&#xfeff;|
# |write(A,a1); l(B); u(A)|&#xfeff;|&#xfeff;|&#xfeff;|
# |&#xfeff;|l(A); read(A,a2)|&#xfeff;|&#xfeff;|
# |&#xfeff;|a2 := a2 * 2|250|&#xfeff;|
# |&#xfeff;|write(A,a2);|&#xfeff;|&#xfeff;|
# |&#xfeff;|l(B); abgelehnt!|&#xfeff;|&#xfeff;|
# |read(B,b1)|&#xfeff;|&#xfeff;|&#xfeff;|
# |b1 := b1 + 100|&#xfeff;|&#xfeff;|125|
# |write(B,b1); u(B)|&#xfeff;|&#xfeff;|&#xfeff;|
# |&#xfeff;|l(B); u(A); read(B,b2)|&#xfeff;|&#xfeff;|
# |&#xfeff;|b2 := b2 * 2|&#xfeff;|250|
# |&#xfeff;|write(B,b2); u(B)|&#xfeff;|&#xfeff;|
# 
# 
# #### Deadlocks unter 2PL möglich
# ■ T1: l(A); r(A); A:=A+100; w(A); l(B); u(A); r(B); B:=B-100; w(B); u(B)
# <br>
# ■ T4: l(B); r(B); B:=B*2; w(B); l(A); u(B); r(A); A:=A*2; w(A); u(A)
# 
# |T1|T4|A|B|
# |---|---|---|---|
# |&#xfeff;|&#xfeff;|25|25|
# |l(A); read(A,a1)|&#xfeff;|&#xfeff;|&#xfeff;|
# |&#xfeff;|l(B); read(B,b2)|&#xfeff;|&#xfeff;|
# |a1 := a1 + 100|&#xfeff;|&#xfeff;|&#xfeff;|
# |&#xfeff;|b2 := b2 * 2|&#xfeff;|&#xfeff;|
# |write(A,a1)|&#xfeff;|125|&#xfeff;|
# |&#xfeff;|write(B,b2)|&#xfeff;|50|
# |l(B) – abgelehnt|&#xfeff;|&#xfeff;|&#xfeff;|
# |&#xfeff;|l(A) – abgelehnt|&#xfeff;|&#xfeff;|
# 
# 
# ■ Lösung 1: Timeouts
# <br>
# ■ Lösung 2: „Waits-for“-Graph zur Vermeidung von deadlocks
# 
# #### 2PL – Intuition
# ■ Jede Transaktion führt sämtliche Aktionen in dem Augenblick aus, zu dem das erste Objekt freigegeben wird.
# <br>
# ■ Reihenfolge der Transaktionen des äquivalenten seriellen Schedules: Reihenfolge der ersten Freigaben von
# Sperren
# <br>
# ![title](sperrprotokolle_img/2pl_intuition.jpg)
# 
# #### 2PL – Beweis
# ■ Idee: Verfahren zur Konvertierung eines beliebigen, legalen Schedule S aus konsistenten, 2PL Transaktionen in einen konfliktäquivalenten seriellen Schedule
# <br><br>
# ■ Induktion über Anzahl der Transaktionen n
# <br><br>
# ■ n = 1: Schedule S ist bereits seriell
# <br><br>
# ■ n = n + 1:
# <br>
# □ S enthalte Transaktionen T1, T2, …, Tn.
# <br>
# □ Sei Ti die Transaktion mit der ersten Freigabe ui(X).
# <br>
# □ Behauptung: Es ist möglich, alle Aktionen der Transaktion an den Anfang des Schedules zu bewegen, ohne konfligierende Aktionen zu passieren.
# <br>
# □ Angenommen es gibt eine Schreibaktion wi(Y), die man nicht verschieben kann:
# <br>
# – … wk(Y) … uk(Y) … li(Y) … wi(Y) …
# <br>
# □ Da Ti erste freigebenden Transaktion ist, gibt es ein ui(X) vor uk(Y):
# <br>
# – … wk(Y) … ui(X) … uk(Y) … li(Y) … wi(Y) …
# <br>
# □ Analog für eine Leseaktion ri(Y)
# <br>
# □ Ti ist nicht 2PL

# ## Sperren
# 
# ### Mehrere Sperrmodi
# ■ Idee: Mehrere Arten von Sperren erhöhen die Flexibilität und verringern die Menge der abgewiesenen Sperren.
# <br>
# □ Sperren obwohl nur gelesen wird, ist übertrieben
# <br>
# – Gewisse Sperre ist dennoch nötig
# <br>
# – Aber: Mehrere Transaktionen sollen gleichzeitig lesen können.
# <br>
# □ Schreibsperre
# <br>
# – Exclusive lock: xli(X)
# <br>
# – Erlaubt das Lesen und Schreiben durch Transaktion Ti
# <br>
# – Sperrt Zugriff aller anderen Transaktionen
# <br>
# □ Lesesperre
# <br>
# – Shared lock: sli(X)
# <br>
# – Erlaubt das Lesen für Transaktion Ti
# <br>
# – Sperrt Schreibzugriff für alle anderen Transaktionen
# <br>
# □ Kompatibilität
# <br>
# – Für ein Objekt darf es nur eine Schreibsperre oder mehrere Lesesperren geben.
# <br>
# □ Freigabe
# <br>
# – Unlock: ui(X) gibt alle Arten von Sperren frei
# 
# ### Bedingungen
# ■ Konsistenz von Transaktionen
# <br>
# □ Schreiben ohne Schreibsperre ist nicht erlaubt.
# <br>
# □ Lesen ohne irgendeine Sperre ist nicht erlaubt.
# <br>
# □ Jede Sperre muss irgendwann freigegeben werden.
# <br><br>
# ■ 2PL von Transaktionen
# <br>
# □ Wie zuvor: Nach der ersten Freigabe dürfen keine Sperren mehr angefordert werden.
# <br><br>
# ■ Legalität von Schedules
# <br>
# □ Auf ein Objekt mit einer Schreibsperre darf es keine andere Sperre einer anderen Transaktion geben.
# <br>
# □ Auf ein Objekt kann es mehrere Lesesperren geben.
# <br>
# ![title](sperren_img/bedingungen.jpg)
# 
# #### Beispiel
# ■ T1: sl1(A)r1(A)xl1(B)r1(B)w1(B)u1(A)u1(B)
# <br>
# ■ T2: sl2(A)r2(A)sl2(B)r2(B)u2(A)u2(B)
# <br>
# □ Konsistent?
# <br>
# □ 2PL?
# 
# |T1|T2|
# |---|---|
# |sl(A); r(A)|&#xfeff;|
# |&#xfeff;|sl(A)r(A)|
# |&#xfeff;|sl(B)r(B)|
# |xl(B) – abgelehnt!|&#xfeff;|
# |&#xfeff;|u(A)u(B)|
# |xl(B)r(B)w(B)|&#xfeff;|
# |u(A)u(B)|&#xfeff;|
# 
# Legal? Konfliktserialisierbar? 2PL funktioniert auch hier!
# 
# ### Weitere Sperrarten
# ■ Idee: Upgraden einer Sperre
# <br>
# □ Von Lesesperre zu Schreibsperre
# <br>
# □ Anstatt gleich strenge Schreibsperre zu setzen
# <br><br>
# ■ Updatesperren
# <br>
# □ Erlaubt nur lesenden Zugriff
# <br>
# □ Kann aber Upgrade erfahren
# <br>
# □ Lesesperre kann dann keinen Upgrade erfahren
# <br><br>
# ■ Inkrementsperre
# <br>
# □ Erlaubt lesenden Zugriff
# <br>
# □ Erlaubt schreibenden Zugriff falls Wert nur inkrementiert (oder dekrementiert) wird.
# <br>
# □ Inkremente sind kommutativ: Vertauschung ist erlaubt

# ## Multiple Choice

# In[1]:


from IPython.display import IFrame

url = "https://lejuliennn.github.io/mct-trainer/#/quiz/categories/transaktionsmanagement"
IFrame(src=url, width='100%', height=800)


# In[ ]:




