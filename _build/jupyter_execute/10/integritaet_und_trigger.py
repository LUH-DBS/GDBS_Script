#!/usr/bin/env python
# coding: utf-8

# # Integrität und Trigger
# In diesem Kapitel beschäftigen wir uns mit Integritätsbedingungen und Triggern.
# ## Motivation – Aktive Datenbanken
# Die Daten, die wir in eine Datenbank einfügen wollen können fehlerhaft sein, es kann sich um typographische Fehler, logische Fehler oder auch Andere handeln. Um den Fehlern entgegenzuwirken wäre eine Möglichkeit , das Schreiben besserer Anwendungen, jedoch ist das Prüfen der Konsistenz und Korrektheit sehr schwer, da z.B komplexe Bedingungen, schon abhängig von vorhandenen Daten sein können. Eine andere Möglichkeit ist das Benutzen von aktiven Elementen im DBMS wie Integritätsbedingungen(integrity constraints, ICs), die einmal spezifiziert werden und wenn nötig dann ausgeführt werden. Integritätsbedingungen "bewachen", dass nur Daten die der spezifizierten Form entsprechen, zugelassen werden.

# ## Schlüssel und Fremdschlüssel
# In diesem Kapitel beschäftigen wir uns mit der am häufigsten genutzten Integritätsbedingung, Schlüssel. Zunächst werden wir die verschiedenen Arten von Schlüsseln(Primär-, Sekundärschlüssel, Fremdschlüssel) kennenlernen und anschließend wie diese Schlüsselbedingungen und referentielle Integrität erzwungen werden.
# 
# ### Schlüssel
# Die einfachtse und am häufigsten genutzte Bedingung sind Schlüssel. Schlüssel sollten aus den vorherigen Kapiteln bekannt sein, sie bilden sich aus ein oder mehreren Attributen und identifizieren eindeutig ein Tupel. Falls eine Schlüsselmenge S gegeben ist, müssen sich also zwei Tupel einer Relation in mindestens einem Attributwert der Schlüsselmenge unterscheiden.
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
# Eine schönere Lösung für dieses Problem wäre, erst den Manager, dann das Studio einzufügen.
# <br><br>
# Es kann der Fall auftreten, dass es zyklische referentielle Integritätsbedingungen gibt. Z.B könnten zusätzlich Manager\*Innen nur Vorsitzende von Studios sein, also ist ManagerinID ein Fremdschlüssel und referenziert auf VorsitzendeID. So gilt die Fremdschlüsselbedingung in beide Richtungen.Es kann nach wie vor kein Studio ohne vorhandenes Managertupel eingefügt werden. Es kann nun auch kein Manager\*In ohne vorhandenes Studio eingefügt werden. Die Lösung für dieses Problem ist das Zusammenfassen mehrerer Änderungsoperationen zu einer „Transaktion“ (mehr dazu im Kapitel 11 „Transaktionsmanagement“) und dann das Verschieben der Integritätschecks bis ans Ende der Transaktion.
# <br><br>
# Dieser Constraint kann mit dem Schlüsselwort DEFERRABLE deklariert werden. DEFERRABLE lässt sich einmal in INITIALLY DEFERRED und INITIALLY IMMEDIATE teilen. Bei INITIALLY DEFERRED wird der Integritätscheck an das Ende der Transaktion, die aus mehreren Statements bestehen kann, verschoben. Bei INITIALLY IMMEDIATE wird der Integritätscheck ans Ende des Statements verschoben. NOT DEFERRABLE, also dass die Bedingung bei jeder Änderung der Datenbank geprüft wird, ist default. Ein Beispiel für die Synatx zu DEFERRABLE finden Sie unten.
# 
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
# 
# ```
# CREATE TABLE Studios(
# Name CHAR(30) PRIMARY KEY,
# Adresse VARCHAR(255),
# VorsitzendeID INT UNIQUE REFERENCES ManagerIn(ManagerinID)
# DEFERRABLE INITIALLY DEFERRED
# );
# ```

# ## Bedingungen auf Attributen und Tupel
# In diesem Kapitel werden weitere Arten der Nebenbedingungen, wie die Annahme bestimmter Werte untersagt wird, betrachtet. Zuerst beschäftigen wir uns mit Bedingungen auf einzelnen Attributen(NOT NULL und CHECK) und anschließend mit Bedingungen für ganze Tupel, also auf das Schema(CHECK). 
# 
# ### NOT NULL
# Wird ein Attribut mit NOT NULL deklariert, so ist es nicht erlaubt für dieses Attribut den Wert NULL einzutragen.
# 
# ```
# CREATE TABLE Studios(
# Name CHAR(30) PRIMARY KEY,
# Adresse VARCHAR(255) NOT NULL,
# VorsitzendeID INT NOT NULL
# REFERENCES ManagerIn(ManagerinID)
# ON UPDATE CASCADE
# );
# ```
# Für das obige Beispiel gilt mit den NOT-NULL-Bedingungen, dass das Einfügen eines Studios ohne Manager\*In nicht mehr möglich ist und das jedes Studio eine Adresse haben muss. Somit ist die Null-Werte Strategie beim Löschen von Manager\*Innen nicht mehr möglich.
# 
# ### Attribut-basierte CHECK Bedingungen
# Die CHECK-Bedingung verfeinert die erlaubten Werte für ein Attribut durch die Spezifikation einer Bedingung. Die Bedingung wie jedes mal geprüft, falls ein Attribut einen neuen Wert erhält, also bei INSERT und UPDATE. Sie ist ähnlich zur WHERE-Klausel, kann beliebig komplex sein und auch aus einer SELECT…FROM…WHERE… Anfrage bestehen. I.d.R. werden CHECK-Bedingungen benutzt um eine einfache Einschränkung der Werte durchzuführen. Falls die Bedingung nicht erfüllt wird, so scheitert die Änderung.
# <br><br>
# In diesem Beispiel wird gecheckt, ob die VorsitztendeID >= 100000 ist, da kleinere Werte für die VorsitzendeID nicht erlaubt sind.
# 
# ```
# CREATE TABLE Studios(
# Name CHAR(30) PRIMARY KEY,
# Adresse VARCHAR(255) NOT NULL,
# VorsitzendeID INT REFERENCES ManagerIn(ManagerinID)
# CHECK (VorsitzendeID >= 100000)
# );
# ```
# In diesem Beispiel wird gecheckt, ob das Geschlecht entsprechend dem Format (‘W‘, ‘M‘, ‘D‘) definiert ist.
# 
# ```
# CREATE TABLE SchauspielerIn (
# Name CHAR(30),
# Adresse VARCHAR(255),
# Geschlecht CHAR(1) CHECK (Geschlecht IN (‘W‘, ‘M‘, ‘D‘)),
# Geburtstag DATE );
# ```
# Eine CHECK Bedingung darf sich auch auf andere Attribute beziehen, jedoch nur im Zusammenhang mit einer SQL Anfrage, wie im unteren Beispiel gezeigt.
# 
# ```
# CREATE TABLE Studios(
# Name CHAR(30) PRIMARY KEY,
# Adresse VARCHAR(255) NOT NULL,
# VorsitzendeID INT CHECK (
# VorsitzendeID IN
# (SELECT ManagerinID FROM ManagerIn))
# );
# ```
# Auf diese Weise wird indirekt referentielle Integrität simuliert. 
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
# Es ist auch möglich Bedingungen für ganze Tupel zu deklarieren. Eine CHECK-Bedingung kann wie Primär- und Fremdschlüsselbezeiehungen in der Liste der Attributen auftauchen und beliebige Bedingungen wie eine WHERE-Klausel haben. Die deklarierten CHECKs werden bei jedem INSERT und UPDATE eines Tupels geprüft.
# <br><br>
# Im unteren Beispiel wird geprüft, ob das Geschlecht 'W' ist oder ob die Anrede nicth mit 'Fr' beginnt.
# ```
# CREATE TABLE SchauspielerIn (
# Anrede CHAR(10),
# Name CHAR(30) PRIMARY KEY,
# Adresse VARCHAR(255),
# Geschlecht CHAR(1) CHECK (Geschlecht IN (‘W‘, ‘M‘, ‘D‘)),
# Geburtstag DATE,
# CHECK (Geschlecht = ‚W‘ OR Anrede NOT LIKE ‚Fr%‘ ));
# ```
# 
# Eine CHECK-Bedingung wird nicht geprüft, falls eine andere (oder sogar die gleiche) Relation in einer Subanfrage der CHECK Bedingung erwähnt wird und diese eine Änderung erfährt. D.h. andere Relationen kennen diese CHECK Bedingung nicht. Solche Probleme gibt es bei ASSERTIONS (siehe Kapitel ...) nicht. Deshalb sollten komplexe Bedingungen lieber als ASSERTION deklariert werden, oder (realistischer) in die Anwendungslogik gesteckt werden..
# 
# ### Bedingungen ändern
# Um Bedingungen nachträglich noch zu ändern, müssen diese einen Namen haben. Meistens vergeben DBMS sowieso interne, jedoch hässliche Namen. Beispiele hierfür finden Sie unten.
# 
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
# 
# ```
# SET CONSTRAINT MyConstraint DEFERRED;
# 
# SET CONSTRAINT MyConstraint IMMEDIATE;
# ```
# Das Entfernen von CONSTRAINTS ist nach dem Scheme ALTER TABLE Relation DROP CONSTRAINT Name; möglich.
# 
# ```
# ALTER TABLE Schauspieler DROP CONSTRAINT NamePrimaer;
# ALTER TABLE Schauspieler DROP CONSTRAINT NichtGeschlechtslos;
# ALTER TABLE Schauspieler DROP CONSTRAINT AnredeKorrekt;
# ```
# 
# Das Hinzufügen ist nach dem Schema ALTER TABLE Relation ADD CONSTRAINT Name ...;
# ```
# ALTER TABLE Schauspieler ADD CONSTRAINT NamePrimaer PRIMARY KEY (Name);
# ALTER TABLE Schauspieler ADD CONSTRAINT NichtGeschlechtslos CHECK (Geschlecht IN (‚W‘, ‚M‘));
# ALTER TABLE Schauspieler ADD CONSTRAINT AnredeKorrekt CHECK (Geschlecht = ‚W‘ OR name NOT LIKE ‚Frau%‘ );
# ```
# 
# Es können nur Tupel-basierte Bedingungen nachträglich hinzugefügt werden, attribut-basierte Bedingungen nicht.

# ## Zusicherungen(Assertions) und Trigger
# 
# Manchmal sollen sich Bedingungen nicht auf bestimmte Tupel beziehen, sondern auf der Schemaebene definiert werden (wie Relationen und Sichten). Solche Bedingungen nennen sich Assertions (Zusicherungen) und Trigger. Eine Assertion ist ein Boole‘scher SQL Ausdruck, der stets wahr sein muss. Die Handhabung von Assertions ist durch einen Admin sehr leicht, jedoch verlangsamen Assertions die Datenbank, da sie schwierig effizient zu implementieren sind.
# Trigger (Auslöser) sind Aktionen, die bei bestimmten Ereignissen (INSERTs, …) ausgelöst werden, im Vergleich zu Assertions sind Trigger leichter effizient zu implementieren.
# 
# ### Assertions
# Assertions werden nach dem folgenden Schema deklariert CREATE ASSERTION Name CHECK (Bedingung). Die Bedingung muss stets gelten, auch schon bei der Erzeugung der Assertion. Änderungen die die Assertion verletzen werden abgewiesen.
# CHECK Bedingungen innerhalb eines CREATE TABLE ... können hingegen falsch werden!
# <br><br>
# Zur Formulierung
# <br>
# Kein direkter Bezug zu Relationen, deshalb müssen Attribute und Relationen in einer SQL Anfrage eingeführt werden.
# <br><br>
# Um eine Assertion zu löschen wird folgendes Schema benutzt DROP ASSERTION Name.
# 
# #### Assertions – Beispiel
# Haben wir die Relationen ManagerIn(Name, Adresse, ManagerinID, Gehalt) und Studios(Name, Adresse, VorsitzendeID) gegeben.
# <br>
# In diesem Beispiel wurde eine Assertion deklariert die nur Vorsitzende von Studios annimmt, die mindestens 1.000.000 verdienen.
# ```
# CREATE ASSERTION ReicheVorsitzende CHECK
# (NOT EXISTS
# (SELECT *
# FROM Studios, ManagerIn
# WHERE ManagerinID = VorsitzendeID
# AND Gehalt < 1000000)
# );
# ```
# Eine Alternative zu dem Beispiel oben, wäre ein CHECK innerhalb eines CREATE TABLE ... .Der Unterschied zu der Assertion oben ist, dass nachträgliche Änderungen an der Relation ManagerIn nicht mehr abgefangen werden können
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
# 
# Haben wir nun die Relation Filme(Titel, Jahr, Länge, inFarbe, StudioName, ProduzentID) gegeben. Wir formulieren eine Assertion, die sicherstellt, dass die Gesamtlänge der von einem Studio produzierten Filme mind. 10000 Minuten beträgt.
# 
# ```
# CREATE ASSERTION NurGrosseStudios CHECK
# (10000 <= ALL
# (SELECT SUM(Länge) FROM Filme
# GROUP BY StudioName)
# );
# ```
# Alternativ wäre wieder ein CHECK beim Schema für die Relation Filme möglich.
# 
# ```
# CHECK (10000 <= ALL
# (SELECT SUM(Länge) FROM Filme
# GROUP BY StudioName)
# ```
# Der Unterschied im Vergleich zu der Assertion oben ist, dass beim Löschen eines Films die Bedingung nicht geprüft wird. Also ist es möglich, dass nachdem Filme aus der Relation Filme gelöscht wurden, es Studios gibt, die nicht mehr mind. 10000 Minuten Filmmaterial haben und dies nicht überprüft wird. Ebenso kann dies eim Studiowechsel eines Films nicht geprüft werden.
# 
# ### Unterschiede der CHECK Bedingungen
# 
# |Constraint-Art|Wo spezifiziert?|Wann geprüft?|Gilt immer?|
# |---|---|---|---|
# |**Attribut-basiertes**|CHECK Beim Attribut|Bei INSERT in Relation oder UPDATE des Attributs|Nein, falls Subanfragen verwendet werden.|
# |**Tupel-basiertes CHECK**|Teil des Relationenschemas|Bei INSERT oder UPDATE eines Tupels|Nein, falls Subanfragen verwendet werden.|
# |**Assertion**|Teil des Datenbankschemas|Beliebige Änderung auf einer erwähnten Relation|Ja|

# ### Trigger
# Trigger sind so genannte Event-Condition-Action Rules (ECA-Rules). Der Unterschied zu Zusicherungen ist, dass Trigger nicht immer gelten müssen, sondern sie werden nur bei bestimmten Ereignissen (INSERT, UPDATE, DELETE, Ende einer Transaktion) ausgeführt. Ein Ereignis wird zunächst nicht verhindert, sondern es wird lediglich eine bestimmte Bedingung geprüft. Falls die Triggerbedingung falsch ist passiert nichts weiter. Falls sie wahr ist, wird eine Aktion ausgeführt. Die Aktion könnte das Ereignis verhindern oder rückgängig machen oder auch etwas völlig anderes tun.
# 
# ### Trigger in SQL
# Die ausgelöste Aktion durch Trigger kann sowohl vor oder nach dem Ereignis ausgeführt werden. Die Aktion kann sich auf alte und/oder neue Werte von Tupeln beziehen, die beim Ereignis eingefügt, verändert oder gelöscht werden.Mit WHEN können neben dem Ereignis auch weitere Bedingungen angegeben werden, die gelten müssen um die Aktion durchzuführen. Die Aktion kann einmal für jedes veränderte Tupel oder einmalig für alle Tupel, die verändert wurden ausgeführt werden.
# 
# #### Trigger – Beispiel
# Hier finden Sie ein Beispiel für einen Trigger, welcher verhindert, dass Manager\*Innengehälter nicht gesenkt werden. Nach jedem Update von Gehalt der Manager\*In Relation, wird das alte Gehalt mit dem neuen verglichen und wenn das alte größer war, wird das Gehalt des betroffenen Tupels wieder auf das Alte gesetzt. Das Rekursionsverhalten ist DBMS-Hersteller-spezifisch.
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
# 
# 
# #### Trigger  –  Alternative
# Anstelle von AFTER kann in einem Trigger BEFORE benutzt werden, ebenso könne die auslösenden Ereignisse INSERT/DELETE auch ohne OF sein. Bei INSERT gibt es kein OLD ROW ... und bei DELETE kein NEW ROW ..., da es keine alten und neue Tupel gibt. Wenn FOR EACH ROW nicht explizit spezifizeirt ist, ist FOR EACH STATEMENT der Default, dann gilt OLD TABLE / NEW TABLE. Die WHEN-Klausel ist optional und es können mehrere SQL-Ausdrücke drin enthalten sein, die mit BEGIN … END umrahmt sind.
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
# In diesem Beispiel sind mehrere SQL-Ausdrücke in der WHEN-Klausel enthalten. Dieser Trigger bewirkt, dass das Durchschnittsgehalt von Manager\*Innen nicht unte 500.000 sinkt. Es sind je ein Trigger für UPDATE, INSERT und DELETE nötig.
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
# 
# ## Zusammenfassung
# In diesem Kapitel haben wir uns mit verschiedenen Schlüsseln, wie UNIQUE(Sekundärschlüssel) und PRIMARY KEY(Primärschlüssel) beschäftigt. Weiterhin haben wir gelernt wie referentielle Integrität erhalten bleibt, mithilfe von Fremdschlüsselbeziehungen, in SQL REFERENCES und FOREIGN KEY. Wir haben auch gesehen wie Attribut-basierte und Tupel-basierte Assertions mit CHECK deklariert werden können. Zuletzt haben wir Triggers kennengelernt, welche nur zu bestimmten Ereignissen wie INSERT,UPDATE usw. ausgeführt werden. 

# ## Multiple Choice

# In[1]:


from IPython.display import IFrame

url = "https://lejuliennn.github.io/mct-trainer/#/quiz/categories/integritaetundtrigger"
IFrame(src=url, width='100%', height=800)


# In[ ]:




