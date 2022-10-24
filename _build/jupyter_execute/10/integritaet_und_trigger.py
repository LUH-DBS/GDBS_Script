#!/usr/bin/env python
# coding: utf-8

# # Integrität und Trigger
# In diesem Kapitel beschäftigen wir uns mit Integritätsbedingungen und Triggern.
# ## Motivation – Aktive Datenbanken
# Die Daten, die wir in eine Datenbank einfügen wollen können fehlerhaft sein, es kann sich um typographische Fehler, logische Fehler oder auch Andere handeln. Um den Fehlern entgegenzuwirken wäre eine Möglichkeit , das Schreiben besserer Anwendungen, jedoch ist das Prüfen der Konsistenz und Korrektheit sehr schwer, da z.B komplexe Bedingungen, schon abhängig von vorhandenen Daten sein können. Eine andere Möglichkeit ist das Benutzen von aktiven Elementen im DBMS wie Integritätsbedingungen(integrity constraints, ICs), die einmal spezifiziert werden und wenn nötig dann ausgeführt werden. Integritätsbedingungen "bewachen", dass nur Daten die der spezifizierten Form entsprechen, zugelassen werden.

# ## Schlüssel und Fremdschlüssel
# 
# ### Schlüssel
# Die einfachtse und am häufigsten genutzte Bedingung sind Schlüssel. Schlüssel sollten aus den vorherigen Kapiteln bekannt sein, sie bilden sich auch ein oder mehreren Attributen und identifizieren eindeutig ein Tupel. Falls eine Schlüsselmenge S gegeben ist, müssen sich also zwei Tupel einer Relation in mindestens einem Attributwert der Schlüsselmenge unterscheiden.
# <br>
# <br>
# Schlüssel werden im CREATE TABLE Ausdruck spezifiziert. Der Primärschlüssel wird mit dem Schlüsselwort PRIMARY KEY gekennzeichnet und kann nie einen Nullwert enthalten. Es gibt pro Relation maximal einen PRIMARY KEY. Ein weiterer Schlüssel ist UNIQUE, hiervon ist es erlaubt mehrere pro Relation und auch Nullwerte zu haben. Falls UNIQUE ohne Nullwerte benutzt werden soll, ist dies mit UNIQUE NOT NULL möglich. 
# 
# #### Primärschlüssel
# Primaärschlüssel werden im CREATE TABLE Ausdruck spezifiziert. Im Folgenden finden Sie eine Deklaration eines Primärschlüssels bei genau einem Attribut, dort findet die Deklaration dirket in der Attributenliste statt. Es ist auch möglich bei nur einem Attribut die Deklaration nach den Attributen zu nennen.
# 
# ```
# CREATE TABLE SchauspielerIn(
# Name CHAR(30) PRIMARY KEY,
# Adresse VARCHAR(255),
# Geschlecht CHAR(1),
# Geburtstag DATE);
# ```
# Bei mehreren Attributen findet die Deklaration zwingend nach den Attributen statt, wie im Beispiel unten gezeigt.
# ```
# CREATE TABLE SchauspielerIn(
# Name CHAR(30),
# Adresse VARCHAR(255),
# Geschlecht CHAR(1),
# Geburtstag DATE,
# PRIMARY KEY (Name, Adresse) );
# ```
# 
# #### Sekundärschlüssel
# Sekundärschlüssel bzw. Schlüsselkandidaten werden mit dem Schlüsseltwort UNIQUE spezifiziert. Die Sytax ist genau wie bei der Deklaration von einem PRIMARY KEY, also direkt beim Attribut oder als separate Attributliste nach den Attributen.
# <br><br>
# Der große Unterschied zu PRIMARY KEY  ist, dass es mehrere UNIQUE Deklarationen geben darf. Standardmäßig erlaubt UNIQUE NULL-Werte, da von NULL ≠ NULL (bzw. UNKNOWN) ausgegangen wird. Bei NULL ist es also möglich, dass zwei Tupel in UNIQUE Attributen übereinstimmen. Um auch Nullwerte zu unterbinden, kann UNIQUE NOT NULL verwendet werden. Ein Beispiel für eine Deklaration eines Sekundärschlüssel befindet sich unten.
# ```
# CREATE TABLE SchauspielerIn(
# Name CHAR(30),
# Adresse VARCHAR(255),
# Geschlecht CHAR(1),
# Geburtstag DATE UNIQUE,
# UNIQUE (Name, Adresse));
# ```

# #### Schlüsselbedingungen erzwingen
# Die spezifizierten Schlüsselbedingungen müssen stets gelten. Diese sind nur relevant bei INSERT und UPDATE, da bei DELETE keine Verletzung der Bedingungen passieren kann, denn es wurden keine Tupel der Relation hinzugefügt, die nicht den Bedingungen entsprechen. Beim Einfügen oder Ändern wird geprüft der neue Schlüsselwert bereits vorhanden ist.
# 
# Meistens ist die effiziente Prüfung der Bedingungen mittels Index möglich, da DBMS in der Regel automatisch Indizes für Primärschlüsselattribute anlegen. Optional ist es auch möglich manuell für UNIQUE-Attribute Indizes zu erstellen, z.B CREATE UNIQUE INDEX JahrIndex ON Filme(Jahr). Das entspricht CREATE INDEX JahrIndex ON Filme(Jahr), aber mit einer neuen UNIQUE Bedingung auf Jahr.
# <br><br>
# Ohne Indizes ist die Überprüfung eher ineffizient, da die gesamte Spalte durchsucht werden muss. Sind die Dtaen sortiert, kann binäre Suche verwendet werden, andernfalls muss sequentielle Suche benutzt werden.
# 
# #### Fremdschlüssel
# Ein Attribut oder eine Attributmenge kann als FOREIGN KEY deklariert werden, wenn die Attributmenge eine entsprechende Attributmenge einer zweiten Relation referenziert. So müssen gemeinsame Werte der Fremdschlüsselattribute auch als gemeinsame Werte des referenzierten Schlüssels auftauchen. Die referenzierte Attributmenge muss UNIQUE oder PRIMARY KEY sein. Haben wir z.B die zwei Relationen ManagerIn(Name, Adresse, ManagerinID, Gehalt) und Studios(Name, Adresse, VorsitzendeID), dann wäre es sinnvoll, dass der Attributwert für VorsitzendeID auf einen bestimmten, vorhandenen Manager verweist. Im Vergleich zu normalen Schlüsseln, darf ein Fremdschlüssel den Wert NULL annehmen. Das verwiesende Schlüsselattribut muss jedoch nicht einen NULL-Wert besitzen (und darf es meist auch nicht), hier kann NOT NULL Abhilfe leisten. Bei Fremdschlüsseln muss referentielle Integrität beibehalten werden, da es sonst zu dangling tuples kommen kann. Folgend einige Beispiele für die Syntax von Fremdschlüsseln:
# <br><br>
# Auf einem Attribut:
# <br>
# ```
# REFERENCES Relation(Attribut)
# ```
# <br>
# Auf (einem oder) mehreren Attributen:
# <br>
# 
# ```
# FOREIGN KEY (Attribute) REFERENCES Relation(Attribute)
# ```
# Seien die Relationen ManagerIn(Name, Adresse, ManagerinID, Gehalt) und Studios(Name, Adresse, VorsitzendeID) gegeben. Wir legen eine Fremdschlüssel für VorsitzendeID an, der auf ManagerinID verweist.
# 
# ```
# CREATE TABLE Studios(
#     Name CHAR(30) PRIMARY KEY,
#     Adresse VARCHAR(255),
#     VorsitzendeID INT REFERENCES Manager(ManagerinID));
#     
# CREATE TABLE Studios(
#     Name CHAR(30) PRIMARY KEY,
#     Adresse VARCHAR(255),
#     VorsitzendeID INT,
#     FOREIGN KEY (VorsitzendeID) REFERENCES
# ManagerIn(ManagerinID));
# ```

# ### CREATE TABLE – Beispiel
# In diesem Beispiel haben wir eine Mitarbeiterrelation mit verschiedenen Attributen gegeben. Die Schlüsselattribute eines Miitarbeiters sind Vor- und Nachname. Jeder Mitarbeiter muss Teil einer Abteilung sein, weshalb DepID auf eine vorhandene ID aus der Departmentrelation verweisen muss. Genauso müssen ProjectName und ProjectYear auf ein vorhandenes Projekt verweisen.
# 
# ```
# CREATE TABLE Employee(
#     FirstName CHAR(30),
#     LastName CHAR(30),
#     City VARCHAR(255) NOT NULL,
#     ZIP INT,
#     Street VARCHAR(255),
#     ProjectName VARCHAR(50),
#     ProjectYear INT,
#     DepID INT NOT NULL,
#     PRIMARY KEY (FirstName,LastName),
#     FOREIGN KEY (DepID) REFERENCES Department(DepID),
#     FOREIGN KEY (ProjectName,ProjectYear)
#         REFERENCES Project(Name, Year) );
# ```

# ### Referentielle Integrität erzwingen
# Es gibt drei Varianten um referentielle Integrität zu erzwingen: Ablehnung verletzender Änderungen (SQL default) ,Kaskadierung und Null-Werte.
# <br><br>
# Haben wir wieder die Relationen ManagerIn(Name, Adresse, ManagerinID, Gehalt) und Studios(Name, Adresse, VorsitzenderID) gegeben, wobei VorsitzendeID auf ManagerinID verweist.
# 
# ```
# CREATE TABLE Studios(
# Name CHAR(30) PRIMARY KEY,
# Adresse VARCHAR(255),
# VorsitzendeID INT REFERENCES ManagerIn(ManagerinID));
# ```
# 
# #### Referentielle Integrität erzwingen: Änderungen Ablehnen
# 
# Durch den von uns festgelegten Fremdschlüssel muss  es für jede VorsitzendeID auch eine ManagerinID geben. SQL lehnt per default Änderungen ab, die Fremdschlüsselbeziehungen verletzen.
# <br>
# Wenn ein INSERT Studio ... mit einer neuen (nicht-NULL) VorsitzendeID angefragt wird, die nicht in ManagerIn gespeichert ist, so wird dies abgelehnt.
# <br><br>
# Wenn ein UPDATE eines Studios mit einer neuen VorsitzendeID, die nicht in Manager gespeichert ist, angefragt wird, so wird dies ebenfalls abgelehnt.
# <br><br>
# Wenn ein DELETE eines ManagerIn-Tupels, dessen ManagerinID auch eine (oder mehrere) VorsitzendeID ist, so wird dieses auch abgelehnt.
# <br><br>
# Wenn ein UPDATE der ManagerinID eines ManagerIn-Tupels angefragt wird, die auch eine (oder mehrere) VorsitzendeID ist, so wird dies auch abgelehnt.
# 
# 
# #### Referentielle Integrität erzwingen: Kaskadierung
# Bei der Kaskadierung ist die Idee, dass Änderungen im Schlüssel im Fremdschlüssel nachgezogen werden. Bei Veränderung in der Schlüsselrelation, verändern sich auch die Werte der Fremdrelation mit.
# <br><br>
# Ein INSERT Studio ... mit einer neuen (nicht-NULL) VorsitzendeID, die nicht in ManagerIn gespeichert ist wird weiterhin abgelehnt.
# <br><br>
# Ein UPDATE eines Studios mit einer neuen VorsitzendeID, die nicht in Manager gespeichert ist, word auch weiterhin abgelehnt.
# <br><br>
# Ein DELETE eines ManagerIn-Tupels, dessen ManagerinID auch auf eine (oder mehrere) VorsitzendeID ist, wird akzeptiert, aber alle abhängigen Studios werden ebenfalls gelöscht.
# <br><br>
# Ein UPDATE der ManagerinID eines ManagerIn-Tupels, die auch eine (oder mehrere) VorsitzendeID ist, wird akzeptiert, aber die VorsitzendeIDs in Studios werden ebenfalls geändert.
# 
# #### Referentielle Integrität erzwingen: Auf NULL setzen
# Bei der Behandlung mit NULL-Werten ist die Idee, dass bei Änderungen im Schlüssel der Wert des Fremdschlüssels auf NULL gesetzt wird.
# <br><br>
# Ein INSERT Studio mit einer neuen (nicht-NULL) VorsitzendeID, die nicht in Manager gespeichert ist wird abgelehnt.
# <br><br>
# Ein UPDATE eines Studios mit einer neuen VorsitzendeID, die nicht in Manager gespeichert ist, wird auch weiterhin abgelehnt.
# <br><br>
# Ein DELETE eines Manager-Tupels, dessen ManagerinID auch eine (oder mehrere) VorsitzendeID ist wird akzeptier, aber die VorsitzendeID aller abhängigen Studios werden auf NULL gesetzt.
# <br><br>
# Ein UPDATE der ManagerinID eines ManagerIn-Tupels, die auch eine (oder mehrere) VorsitzendeID ist, wird ebenfalls akzeptiert aber die VorsitzendeIDs in Studios werden auf NULL gesetzt.
# 
# #### Referentielle Integrität erzwingen
# In bestimmten DBMS kann die Vorgehensweise individuell spezifiziert werden. Im unteren Beispiel legen wir beim Löschen Behandlung mit NULL-Werten und beim Ändern Kaskadierung fest. Hier wird eine "vorsichtige" Strategie verfolgt, denn die Studios werden nicht gelöscht und behalten falls möglich ihre VorsitzendenID.
# 
# ```
# CREATE TABLE Studios(
# Name CHAR(30) PRIMARY KEY,
# Adresse VARCHAR(255),
# VorsitzendeID INT REFERENCES ManagerIn(ManagerinID)
# ON DELETE SET NULL
# ON UPDATE CASCADE
# );
# ```

# ### Integritätschecks verschieben
# Es ist nicht immer möglich, Tupel einzufügen, die der referentiellen Integrität gehorchen. Möchten wir beispielsweise ein neues Studio, namens Redlight mit Sitz in New York und mit ManagerinID 23456, in unsere Relation Studios einfügen. Jedoch wurde die ManagerIn mit der ID 23456 noch nicht angelegt.
# ```
# INSERT INTO Studios
# VALUES (‘Redlight‘, ‘New York‘, 23456);
# ```
# Wir könnten stattdessen die ManagerinID NULL lassen, welches auch erlaubt ist, da NULL-Werte nicht auf referentielle Integrität geprüft werden müssen.
# 
# ```
# INSERT INTO Studios(Name, Adresse)
# VALUES (‘Redlight‘, ‘New York‘);
# ```
# 
# Später nach dem Einfügen des Managertupels mit der ManagerinID 23456 können wir das Tupel aus der Studiosrelation updaten:
# 
# ```
# UPDATE Studios SET VorsitzendeID = 23456
# WHERE Name = ‘Redlight‘;
# ```
# Eine schnönere Lösung für dieses Problem wäre, erst den Manager, dann das Studio einzufügen.
# <br><br>
# Es kann zyklische referentielle Integritätsbedingungen geben.
# <br>
# Manager sind nur Vorsitzende von Studios
# <br>
# ManagerinID ist Fremdschlüssel und referenziert VorsitzendeID.
# <br>
# Es kann nach wie vor kein Studio ohne vorhandenes Managertupel eingefügt werden.
# <br>
# Es kann nun auch kein Manager ohne vorhandenes Studio eingefügt werden.
# <br>
# Catch 22!
# <br>
# Lösung
# <br>
# Mehrere Änderungsoperationen zu einer „Transaktion“ zusammenfassen (mehr später: „Transaktionsmanagement“)
# <br>
# Integritätschecks bis ans Ende der Transaktion verschieben
# <br><br>
# ■ Jeder Constraint kann als DEFERRABLE oder NOT DEFERRABLE deklariert werden.
# <br><br>
# ■ NOT DEFERRABLE ist default
# <br>
# □ Bei jeder Änderung der Datenbank wird die Bedingung geprüft.
# <br><br>
# ■ DEFERRABLE
# <br>
# □ INITIALLY DEFERRED:
# <br>
# – Verschieben ans Ende der Transaktion
# <br>
# – oder bis wir Verschiebung aufheben
# <br>
# □ INITIALLY IMMEDIATE
# <br>
# – Zunächst nichts verschieben, bis wir Verschiebung verlangen.
# ```
# CREATE TABLE Studios(
# Name CHAR(30) PRIMARY KEY,
# Adresse VARCHAR(255),
# VorsitzendeID INT UNIQUE REFERENCES ManagerIn(ManagerinID)
# DEFERRABLE INITIALLY DEFERRED
# );
# ```

# ## Bedingungen auf Attributen und Tupel
# 
# ### Weitere Arten der Nebenbedingungen
# ■ Verbieten Annahme bestimmter Werte
# <br><br>
# ■ Bedingungen auf einzelnen Attributen
# <br>
# □ NOT NULL
# <br>
# □ CHECK
# <br><br>
# ■ Bedingungen für ganze Tupel, also auf das Schema
# <br>
# □ CHECK
# 
# ### NOT NULL
# ```
# CREATE TABLE Studios(
# Name CHAR(30) PRIMARY KEY,
# Adresse VARCHAR(255) NOT NULL,
# VorsitzendeID INT NOT NULL
# REFERENCES ManagerIn(ManagerinID)
# ON UPDATE CASCADE
# );
# ```
# ■ Einfügen eines Studios ohne Manager ist nicht mehr möglich.
# <br><br>
# ■ Jedes Studio muss eine Adresse haben.
# <br><br>
# ■ Die Null-Werte Strategie beim Löschen von Managern ist nicht mehr möglich.
# 
# ### Attribut-basierte CHECK Bedingungen
# Verfeinerung der erlaubten Werte für ein Attribut durch Spezifikation einer Bedingung.
# <br><br>
# Bedingung beliebig komplex
# <br>
# Wie WHERE Klausel
# <br>
# Oder sogar als SELECT…FROM…WHERE… Anfrage
# <br><br>
# i.d.R. aber eine einfache Einschränkung der Werte
# <br><br>
# CHECK wird geprüft falls ein Attribut einen neuen Wert erhält
# <br>
# INSERT
# <br>
# UPDATE
# <br><br>
# Falls FALSE, scheitert die Änderung
# ```
# CREATE TABLE Studios(
# Name CHAR(30) PRIMARY KEY,
# Adresse VARCHAR(255) NOT NULL,
# VorsitzendeID INT REFERENCES ManagerIn(ManagerinID)
# CHECK (VorsitzendeID >= 100000)
# );
# 
# CREATE TABLE SchauspielerIn (
# Name CHAR(30),
# Adresse VARCHAR(255),
# Geschlecht CHAR(1) CHECK (Geschlecht IN (‘W‘, ‘M‘, ‘D‘)),
# Geburtstag DATE );
# ```
# CHECK Bedingung darf sich auch auf andere Attribute beziehen.
# <br>
# Nur im Zusammenhang mit einer SQL Anfrage
# ```
# CREATE TABLE Studios(
# Name CHAR(30) PRIMARY KEY,
# Adresse VARCHAR(255) NOT NULL,
# VorsitzendeID INT CHECK (
# VorsitzendeID IN
# (SELECT ManagerinID FROM ManagerIn))
# );
# ```
# Simuliert referentielle Integrität
# <br>
# Was kann schief gehen?
# <br>
# UPDATE und INSERT auf der Studios Relation
# <br>
# CHECK wird geprüft
# <br>
# DELETE auf der Manager Relation
# <br>
# CHECK wird nicht geprüft; CHECK Bedingung wird ungültig
# <br>
# D.h.: Andere Relationen kennen diese CHECK Bedingung nicht.
# 
# ### Tupel-basierte CHECK Bedingungen
# Bedingungen können auch für ganze Tupel deklariert werden.
# <br>
# Wie Primär- und Fremdschlüsselbedingungen kann auch einen CHECK Bedingung in der Liste der Attribute auftauchen.
# <br>
# Ebenso wie bei Attribut-basierten CHECKs: Beliebige Bedingungen wie eine WHERE Klausel.
# <br>
# Wird geprüft bei jedem INSERT und jedem UPDATE eines Tupels.
# ```
# CREATE TABLE SchauspielerIn (
# Anrede CHAR(10),
# Name CHAR(30) PRIMARY KEY,
# Adresse VARCHAR(255),
# Geschlecht CHAR(1) CHECK (Geschlecht IN (‘W‘, ‘M‘, ‘D‘)),
# Geburtstag DATE,
# CHECK (Geschlecht = ‚W‘ OR Anrede NOT LIKE ‚Fr%‘ ));
# ```
# Typischer Aufbau einer Bedingung wenn wir mehrere Eigenschaften gemeinsam verbieten wollen (Männlich und Name beginnt mit „Frau…“)
# <br><br>
# Wird nicht geprüft falls eine andere (oder sogar die gleiche) Relation in einer Subanfrage der CHECK
# Bedingung erwähnt wird und diese eine Änderung erfährt.
# <br>
# D.h.: Andere Relationen kennen diese CHECK Bedingung nicht.
# <br>
# Solche Probleme gibt es bei ASSERTIONS (siehe unten) nicht. Deshalb komplexe Bedingungen lieber als ASSERTION deklarieren,
# <br>
# oder (realistischer) in die Anwendungslogik stecken.
# 
# ### Bedingungen ändern
# Zur Änderung von Bedingungen müssen Namen vergeben werden.
# ```
# CREATE TABLE SchauspielerIn (
# Anrede CHAR(19),
# Name CHAR(30) CONSTRAINT NamePrimaer PRIMARY KEY,
# Adresse VARCHAR(255),
# Geschlecht CHAR(1) CONSTRAINT NichtGeschlechtslos
# CHECK (Geschlecht IN (‚W‘, ‚M‘)),
# Geburtstag DATE,
# CONSTRAINT AnredeKorrektConstraint
# CHECK (Geschlecht = ‚W‘ OR Anrede NOT LIKE ‚Frau%‘ );
# ```
# Meist vergeben DBMS sowieso interne (aber hässliche) Namen.
# 
# ```
# SET CONSTRAINT MyConstraint DEFERRED;
# 
# SET CONSTRAINT MyConstraint IMMEDIATE;
# ```
# ■ Entfernen
# ```
# ALTER TABLE Schauspieler DROP CONSTRAINT NamePrimaer;
# ALTER TABLE Schauspieler DROP CONSTRAINT NichtGeschlechtslos;
# ALTER TABLE Schauspieler DROP CONSTRAINT AnredeKorrekt;
# ```
# ■ Hinzufügen
# ```
# ALTER TABLE Schauspieler ADD CONSTRAINT NamePrimaer PRIMARY KEY (Name);
# ALTER TABLE Schauspieler ADD CONSTRAINT NichtGeschlechtslos CHECK (Geschlecht IN (‚W‘, ‚M‘));
# ALTER TABLE Schauspieler ADD CONSTRAINT AnredeKorrekt CHECK (Geschlecht = ‚W‘ OR name NOT LIKE ‚Frau%‘ );
# ```
# □ Diese Bedingungen sind nun alle Tupel-basiert.
# <br>
# □ Attribut-basierte Bedingungen können nicht nachträglich eingefügt werden.

# ## Zusicherungen und Trigger
# 
# ### Motivation
# Manche Bedingungen sollen sich nicht auf bestimmte Tupel beziehen, sondern auf Schemaebene definiert werden (wie Relationen und Sichten).
# <br><br>
# Assertion (Zusicherungen)
# <br>
# Boole‘scher SQL Ausdruck, der stets wahr sein muss
# <br>
# Einfache Handhabung für Admin
# <br>
# Schwierig, effizient zu implementieren
# <br><br>
# Trigger („Auslöser“)
# <br>
# Aktionen, die bei bestimmten Ereignissen (INSERTs, …) ausgelöst werden
# <br>
# Leichter, effizient zu implementieren
# 
# ### Assertions
# CREATE ASSERTION Name CHECK (Bedingung)
# <br><br>
# Bedingung muss bei Erzeugung der Assertion bereits gelten.
# <br>
# Bedingung muss stets gelten; Änderungen, die die Assertion falsch machen, werden abgewiesen.
# <br>
# CHECK Bedingung können hingegen falsch werden!
# <br><br>
# Zur Formulierung
# <br>
# Kein direkter Bezug zu Relationen, deshalb müssen Attribute und Relationen in einer SQL Anfrage eingeführt werden.
# <br><br>
# Löschen
# <br>
# DROP ASSERTION Name;
# 
# #### Assertions – Beispiel
# ■ ManagerIn(Name, Adresse, ManagerinID, Gehalt) Studios(Name, Adresse, VorsitzendeID)
# <br>
# ■ Vorsitzende von Studios müssen mindestens 1.000.000 verdienen.
# ```
# CREATE ASSERTION ReicheVorsitzende CHECK
# (NOT EXISTS
# (SELECT *
# FROM Studios, ManagerIn
# WHERE ManagerinID = VorsitzendeID
# AND Gehalt < 1000000)
# );
# ```
# ■ Alternative:
# ```
# CREATE TABLE Studios(
# Name CHAR(30) PRIMARY KEY,
# Adresse VARCHAR(255) NOT NULL,
# VorsitzendeID INT REFERENCES ManagerIn(ManagerinID),
# CHECK ( VorsitzendeID NOT IN
# (SELECT ManagerinID FROM ManagerIn
# WHERE Gehalt < 1000000))
# );
# ```
# ■ Was ist der Unterschied?
# <br>
# □ Änderungen der ManagerIn Relation (Gehalt sinkt) werden nicht erkannt.
# <br><br>
# ■ Filme(Titel, Jahr, Länge, inFarbe, StudioName, ProduzentID)
# ```
# CREATE ASSERTION NurGrosseStudios CHECK
# (10000 <= ALL
# (SELECT SUM(Länge) FROM Filme
# GROUP BY StudioName)
# );
# ```
# □ Ein Studio muss mindestens 10,000 Minuten Filmmaterial haben
# <br><br>
# ■ Alternative beim Schema für Filme
# ```
# □ CHECK (10000 <= ALL
# (SELECT SUM(Länge) FROM Filme
# GROUP BY StudioName)
# ```
# ■ Unterschied?
# <br>
# □ Beim Löschen eines Films wird die Bedingung nicht geprüft.
# <br>
# □ Beim Studiowechsel eines Films wird die Bedingung nicht geprüft.
# 
# ### Unterschiede der CHECK Bedingungen
# 
# |Constraint-Art|Wo spezifiziert?|Wann geprüft?|Gilt immer?|
# |---|---|---|---|
# |**Attribut-basiertes**|CHECK Beim Attribut|Bei INSERT in Relation oder UPDATE des Attributs|Nein, falls Subanfragen verwendet werden.|
# |**Tupel-basiertes CHECK**|Teil des Relationenschemas|Bei INSERT oder UPDATE eines Tupels|Nein, falls Subanfragen verwendet werden.|
# |**Assertion**|Teil des Datenbankschemas|Beliebige Änderung auf einer erwähnten Relation|Ja|
# 
# ### Trigger
# ■ Auch: Event-Condition-Action Rules (ECA-Rules)
# <br><br>
# ■ Unterschiede zu Zusicherungen
# <br>
# □ Gelten nicht immer, sondern werden bei bestimmten Ereignissen (INSERT, UPDATE, DELETE, Ende einer Transaktion) ausgeführt.
# <br>
# □ Ein Ereignis wird zunächst nicht verhindert, es wird lediglich ein bestimmte Bedingung geprüft.
# <br>
# – Falls falsch, passiert nichts weiter
# <br>
# □ Falls wahr, wird eine Aktion ausgeführt. Die Aktion könnte das Ereignis verhindern oder rückgängig machen.
# <br>
# Oder auch etwas völlig anderes tun.
# 
# ### Trigger in SQL
# Eigenschaften/Fähigkeiten
# <br>
# Ausführung der Aktion vor oder nach dem Ereignis
# <br>
# Die Aktion kann sich auf alte und/oder neue Werte von Tupeln beziehen, die beim Ereignis eingefügt, verändert oder gelöscht werden.
# <br>
# Mit WHEN können neben dem Ereignis auch weitere Bedingungen angegeben werden, die gelten müssen um die Aktion durchzuführen.
# <br>
# Aktion wird durchgeführt
# <br>
# Einmal für jedes veränderte Tupel oder
# <br>
# einmalig für alle Tupel, die verändert wurden
# 
# #### Trigger – Beispiel
# ```
# CREATE TRIGGER GehaltsTrigger --Name des Triggers
# AFTER UPDATE OF Gehalt ON ManagerIn --Ereignis
# REFERENCING
#     OLD ROW AS AltesTupel,
#     NEW ROW AS NeuesTupel
# FOR EACH ROW --Für jedes veränderte Tupel einmal durchführen
# WHEN (AltesTupel.Gehalt > NeuesTupel.Gehalt) --Bedingung (condition)
#     UPDATE ManagerIn --Aktion
#     SET Gehalt = AltesTupel.Gehalt
#     WHERE ManagerinID = NeuesTupel.ManagerinID; --Nur betroffenes Tupel
# ```
# ■ Was bewirkt der Trigger?
# <br>
# □ Managergehälter werden nicht gesenkt!
# <br>
# □ Rekursionsverhalten ist DBMS-Hersteller-spezifisch.
# 
# #### Trigger  –  Alternative
# ```
# CREATE TRIGGER GehaltsTrigger                   --BEFORE
# AFTER UPDATE OF Gehalt ON ManagerIn             --INSERT / DELETE (ohne OF…)
# REFERENCING
#     OLD ROW AS AltesTupel,                      --Bei INSERT nicht erlaubt
#     NEW ROW AS NeuesTupel                       --Bei DELETE nicht erlaubt
# FOR EACH ROW                                    --Default: FOR EACH STATEMENT Dann: OLD TABLE / NEW TABLE
# WHEN (AltesTupel.Gehalt > NeuesTupel.Gehalt)    --WHEN ist optional
#     UPDATE ManagerIn                            --Auch mehrere SQL Ausdrücke (BEGIN … END)
#     SET Gehalt = AltesTupel.Gehalt
#     WHERE ManagerinID = NeuesTupel.ManagerinID;
# ```
# 
# #### Trigger - Beispiel
# ```
# CREATE TRIGGER DurchschnittsgehaltTrigger
# AFTER UPDATE OF Gehalt ON ManagerIn
# REFERENCING
#     OLD TABLE AS AlteTupel --Enthält nur die alten bzw. neuen Tupel.
#     NEW TABLE AS NeueTupel
# FOR EACH STATEMENT  --Ausführung nur einmal, egal wie viele Tupel betroffen.
# WHEN (500000 > (SELECT AVG(Gehalt) FROM ManagerIn)) --Wird nach dem UPDATE geprüft.
# BEGIN
#     DELETE FROM ManagerIn
#         WHERE (Name, Adresse, ManagerID, Gehalt) IN NeueTupel; --Es werden nur veränderte Tupel entfernt und durch die alten Tupel ersetzt.
#     INSERT INTO ManagerIn
#         (SELECT * FROM AlteTupel)
# END;
# ```
# ■ Was bewirkt dieser Trigger?
# <br>
# □ Das Durchschnittsgehalt von Managern soll nicht unter 500,000 sinken!
# <br>
# □ Je ein Trigger für UPDATE, INSERT und DELETE nötig
# 
# ## Zusammenfassung
# ■ Schlüssel
#  <br>
# □ UNIQUE, PRIMARY KEY, NOT NULL 
#  <br> <br>
# ■ Referentielle Integrität
#  <br>
# □ REFERENCES, FOREIGN KEY
#  <br> <br>
# ■ Attribut-basiertes CHECK
#  <br> <br>
# ■ Tupel-basiertes CHECK
#  <br> <br>
# ■ Zusicherungen (Datenbank-basiertes CHECK)
#  <br>
# □ ASSERTION
#  <br> <br>
# ■ Trigger
# 
