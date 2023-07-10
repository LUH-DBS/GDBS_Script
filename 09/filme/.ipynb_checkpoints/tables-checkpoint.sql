DROP TABLE IF EXISTS Film;
Create Table Film(
	Titel varchar(127) NOT NULL PRIMARY KEY,
	Jahr integer,
	Laenge integer,
	inFarbe bit,
	StudioName varchar(127),
	ProduzentinID integer,
	FOREIGN KEY(StudioName) REFERENCES Studio(Name));


DROP TABLE IF EXISTS SchauspielerIn;
CREATE TABLE SchauspielerIn (
 Name varchar(127) NOT NULL PRIMARY KEY,
 Adresse varchar(127),
 Geschlecht varchar(127),
 Geburtstag DATE);

DROP TABLE IF EXISTS spielt_in;
CREATE TABLE spielt_in (
 FilmTitel varchar(127),
 FilmJahr integer,
 Name varchar(127),
 FOREIGN KEY (FilmTitel) REFERENCES Film (Titel),
 FOREIGN KEY (FilmJahr) REFERENCES Film (Jahr),
 FOREIGN KEY (Name) REFERENCES SchauspielerIn (Name));


DROP TABLE IF EXISTS Studio;
CREATE TABLE Studio (
 Name varchar(127) NOT NULL PRIMARY KEY,
 Adresse varchar(127),
 VorsitzendeID varchar(127));
 
DROP TABLE IF EXISTS ManagerIn;
CREATE TABLE ManagerIn (
 Name varchar(127) NOT NULL PRIMARY KEY,
 Adresse varchar(127),
 ManagerInID varchar(127),
 Gehalt FLOAT,
 FOREIGN KEY (ManagerInID) REFERENCES Studio (VorsitzendeID),
 FOREIGN KEY (ManagerInID) REFERENCES Film (ProduzentinID));

