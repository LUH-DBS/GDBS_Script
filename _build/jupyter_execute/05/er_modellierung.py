#!/usr/bin/env python
# coding: utf-8

# # ER-Modellierung
# 
# Beim konzeptionellen Entwurf möchten wir aus einer informellen Beschreibung einer Datenbank eine formelle Beschreibung erstellen, in der Mehrdeutigkeiten und jegliche Namen- und Typkonflikte behoben sowie Einschränkungen und Bedingungen sinnvoll ausgedrückt werden können. 
# 
# Eine Modellierungssprache für eine solche Modellierung ist das Entity-Relationship-Modell (ER-Modell). 
# 

# ## Einführung: Das Entity-Relationship-Modell
# 
# Die ER-Modellierung wurde 1976 von Peter Chen vorgestellt und wird seitdem als das Standardmodell für die frühe Entwurfsphase des Datenbankentwurfes verwendet.

# Original Publikation von 1976         |  Peter Chen
# :-------------------------:|:-------------------------:
# <img src="peter_chen_paper.jpg" width="400" /> | <img src="peter_chen.jpg" width="400" />
# 
# 

# Das Ergebnis einer ER-Modellierung sind ER-Diagramme, die Datenbanken beschreiben, die eine Instanz haben werden. Wir werden jetzt die zentralen Komponenten dieser Modellierungssprache und die Möglichkeiten damit Datenbedingungen und -beziehungen auszudrücken kennenlernen. 

# ## Begriffe

# ### Komponenten
# Die zentralen Komponenten der ER-Modellierung sind Entities, Entitytypen, Relationships und Relationshiptypen.
# 
# 
# 
# 
# **Entity:** Ein Ding / Objekt der realen oder der Vorstellungswelt
# 
# **Relationship:** Beschreibt Beziehungen zwischen zwei („konkreten“) Entities
# - Entities und Relationships sind nicht direkt darstellbar und werden nicht explizit im Diagramm sichtbar, sondern sind nur über Eigenschaften ihrer Klassen beobachtbar
# 
# **Entitytyp (entity set):** Eine Klasse für gleichartige Objekte
# 
# **Relationshiptyp:** Eine Klasse für gleichartige Beziehungen
# 
# Komponente| Darstellung| Visuell|
# ----------|------------|--------|
# Entitytyp |Rechteck|<img src="rechteck.jpg" />|
# Relationshiptyp |Raute|<img src="Raute.jpg" />|
# Attribut | Oval | <img src="Oval.jpg" />|
# 
# **Attribut:** repräsentiert eine Eigenschaft von Entities oder von Relationships
# - Es gibt Attribute die nur aus primitiven Datenwerten (String, Integer, …) und Operationen darauf bestehen und auch komplexere zusammengesetzte Attribute, die wir in dieser Vorlesung jedoch nicht detailliert behandeln werden. Komplexe Attribute werden dem erweiterten ER-Modell zugeordnet. 
# 
# Attribute an Entitytypen: 
# <img src="entitytypattribut.jpg" />
# 
# Attribute an Relationshiptypen:
# <img src="relationshiptypattribut.jpg" />

# **Beispiel:** Im folgenden Diagramm wollen wir Informationen über Filme, Schauspieler*innen und Studios modellieren. 
# - Ein Film enthält Daten über Titel, Jahr, Länge und Typ. 
#     - Dargestellt über einen Entitytypen und vier Attribute
# - Über Schauspieler*innen sollen Name und Adresse gespeichert werden
#     - Dargestellt über einen Entitytypen und zwei Attribute
# - Über Studios sollen Name und Adressen gespeichert werden.
#     - Dargestellt über einen Entitytypen und zwei Attribute
# - Es soll abgebildet werden dass Schauspieler*innen in Filmen mitspielen.
#     - Dargestellt über einen Relatioshiptypen der Filme und Schauspieler*innen verbindet
# - Es soll dargestellt werden, dass Studios die Rechte an Filmen besitzen. Insbesondere soll ein Film genau einem Studio gehören. 
#     - Dargestellt über einen Relatioshiptypen der Filme und Studios verbindet. Den letzten Punkt über "genau einem Studio" werden wir später im Kontext von Kardinalitäten genauer betrachten. 
# 
# <img src="er_diagramm_bsp.jpg" width ="700" />

# ### Instanz eines ER-Diagramms

# Wie bereits gesagt beschreiben ER-Diagramme Datenbanken, die eine Instanz haben (werden).
# Dabei gilt, dass der „Wert“ eines Entitytypen die (endliche) Menge der zugehörigen Entities ist. Jede Entity hat bestimmte Werte für seine Attribute, z.B., Basic Instinct = {Titel=Basic Instinct, Jahr = 1992, Länge = 127, Typ = Farbe}. Die Instanz eines n-ären Relationshiptypen ist eine Menge von n-Tupel, z.B spielt_in_instanz_1= (Basic Instinct, Sharon Stone).
# Dies alles ist an dieser Stelle nur eine abstrakte Denkhilfe. Die Modellierung im relationalen Modell wird sich nochmal unterscheiden, sodass sich die Abspeicherung durch ein DBMS auch unterscheiden wird. 
# 
# **Beispiel:** Die folgenden Tabellen stellen die Instanzen eines Teils unseres Modells in der finalen Datenbank im **relationalen Modell** (als Tabellen) dar. 
# 
# 
# <table>
# <tr><th>Filme</th><th></th><th>Schauspieler*in</th><th></th><th>spielt_in</th></tr>
# <tr><td>
# 
# 
# |Titel|Jahr |Länge|Typ|
# |------|----|------|----|
# |Basic Instinct |1992|127|Farbe|
# |Schindler's List |1993|187| S/W|
# |Django Unchained| 2012|165| Farbe|
# 
# </td><td>
# </td><td> 
# 
# |Name|Adresse|
# |----|-------|
# |Sharon Stone|Hollywood|
# |Johnny Depp |Paris|
# |Jaimie Foxx| Hidden Valley|
#     
# </td><td> 
# </td><td> 
#     
# |Name|Titel|
# |----|-------|
# |Sharon Stone|Baisc Instinct|
# |Johnny Depp |Dead Men|
# |Jaimie Foxx| Django Unchained|
#     
# </td></tr> </table>

# ## Kardinalitäten von Relationshiptypen

# Allgemein: Ein binärer Relationshiptyp kann beliebig viele Entities des einen Typen mit beliebig vielen des anderen Typen verbinden. Betrachten wir zum Beispiel unsere Beispieldatenbank über Filme. Hier kann eine Schauspieler\*in in mehreren Filmen mitspielen und gleichzeitig mehrere Schauspieler\*innen in einem einzigen Film. Hierbei nutzen wir bewusst "kann", da nicht jede Entity mit einer anderen Entity des jeweiligen Typen verbunden sein muss. Beispielsweise spielen in Animationsfilme keine Schauspieler\*innen mit. Anders ist es bei Relationshiptypen, bei denen eine Verbindung erzwungen werden muss. Beispielsweise muss jeder Film von einem Studio produziert werden - in diesem Fall sogar von genau einem Studio.
# 
# Man kann diese Kardinalitäten im ER-Modell genau spezifizieren. Es gibt im Allgemeinen drei häufige Kardinalitäten:
# 
# ### m:n Beziehungen
# - **m:n Beziehungen** sagen aus, dass jede Entity des einen Typen mit keinem oder mehreren Entities des anderen Typen verbunden sein kann.
# 
# <img src="mn_kardinalitaet.jpg" width="100" />
# 
# - Beispiele: Filme und Schauspieler\*innen, Produkte und Kund\*innen, Studierenden und Vorlesungen
# 
# 
# 
# ### 1:n Beziehungen
# 
# - **1:n Beziehungen** sagen aus, dass jede Entity des einen Typen mit maximal einem Entity des anderen Typen verbunden sein **kann**. Diese Beziehung gilt aber nur in eine Richtung. 
# 
# <img src="1n_kardinalitaet.jpg" width="100" />
# 
# - Beispiele: Ein Studio kann die Rechte an mehreren Filmen besitzen. Ein Film kann nur von einem Studio besessen werden.
# 
# - Darstellung mittels eines Pfeils zur „1er“ Seite.
# 
# 
# ### 1:1 Beziehungen
# 
# - **1:1 Beziehung** sagen aus, dass jede Entity des einen Typen mit maximal einem Entity des anderen Typen verbunden sein **kann und umgekehrt**.
# 
# <img src="11_kardinalitaet.jpg" width="100" />
# 
# - Beispiel: Ein Studio kann nur von einer Vorsitzenden geleitet werden. Eine Vorsitzende kann nur ein Studio leiten. Auch hier gilt immernoch "kann". Wir werden eine Notation für eine totale Abbildung, d.h., wo die Beziehung stattfinden muss, noch kennenlernen. In unserem Beispiel kann ein Studio theoretisch (vorübergehend) keinen Vorsitzenden haben.
# - Darstellung mittels eines Pfeils zu beiden Seiten.
# 

# ## Weitere Notationen für Kardinalitäten
# 
# Sie werden in der Literatur verschiedene Notationen für die Darstellung von Kardinalitäten finden. Diese sind unterschiedlich mächtig. Bisher haben wir lediglich die grafische Notation kennengerlernt, die über Pfeiltypen ausgedrückt wird. Eine Verbindung ohne eine Pfeilspitze, die eine beliebige Anzahl von Verbindungen, also "n", suggeriert und eine Verbindung mit einer Pfeilspitze, die maximal eine Verbindung, also "1", darstellt. Diese Notation lässt noch keine Nebenbedingungen hinsichtlich konkreter "n"-Werte zu.
# Im Folgenden werden wir noch die Min-Max-Notation und die numerische Notation kennenlernen. 
# 
# 
# ### Min-Max-Notation (Look-Up-Semantik)
# 
# Die Min-Max-Notation schränkt die möglichen Teilnahmen von Instanzen der beteiligten Entitytypen an der Beziehung ein. Insbesondere drückt sie aus, wie häufig eine Instanz minimal bzw. maximal an einer Beziehung teilnimmt. Die Notation ist (Min,Max) an der Seite des Entitytypen. 
# 
# Im folgenden Beispiel sagt (0,1) an der Seite des Produktes aus, dass ein Produkt entweder in einem oder keinem Regal gelagert wird. Andersherum sagt (0,3) auf der Seite des Regals aus, dass in einem Regal 0 bis 3 unterschiedliche Produkte gelagert werden können. 
# 
# <img src="minmax-beispiel.jpg" width="500" />
# 
# 
# ### Numerische Notation (Partizipationssemantik)
# 
# Die numerische Notation ist eine vereinfachende Form, in der man ausdrückt mit wie vielen Instanzen des gegenüberliegenden Typen eine Verbindung maximal aufgebaut wird. 
# 
# Im Folgenden Beispiel besagt die Angabe von "n" auf der Seite der Filme, dass bis zu n Filme mit einem Studio verbunden sein können. Die "1" auf der Seite von Studio besagt, dass jeder Film mit maximal einem Studio verbunden sein kann.
# 
# 
# <img src="numerisch-beispiel.jpg" width="500" />

# In der folgenden Tabelle sind nochmal alle drei Möglichkeiten Kardinalitäten anzugeben gegenübergestellt.
# 
# 
# |Beziehungsart|(min,max) links|(min, max) rechts| Numerisch links|Numerisch rechts|Grafische Notation|
# |-------------|---------------|-----------------|----------------|----------------|------------------|
# |many-to-many |     (0,* )    | (0,* )          |        n       |        n       |<img src="nn_notation.jpg" width="300"/>|
# |one-to-many  |     (0,* )    | (0,1 )          |        1       |        n       |<img src="1n_notation.jpg" width="300"/>|
# |many-to-one  |     (0,1 )    | (0,* )          |        n       |        1       |<img src="n1_notation.jpg" width="300"/>|
# |one-to-one   |     (0,1 )    | (0,1 )          |        1       |        1       |<img src="11_notation.jpg" width="300"/>|

# ### Totale Beziehung
# 
# Bisher haben wir hauptsächlich Beziehungstypen kennengelernt, die auf "kann" basieren. Lediglich mit der Min-Max-Notation können wir bisher sicherstellen, dass jede Entity eines Typs an einer Beziehung teilnehmen muss, indem wir den Minimalwert auf eine Zahl größer als 0 setzen: (1,* ) bedeutet, dass jede Entity mindestens einmal an einer Beziehung teilnehmen muss. Entsprechend bedeutet (1,1), dass jede Entity genau einmal an einer Beziehung teilnehmen muss.
# 
# Die totale Abbildung stellt man grafisch entweder durch einen offenen Pfeil auf der Seite der totalen Abbildung dar oder anhand eines Doppelstriches:
# 
# |Offener Pfeil|Doppelstrich|
# |-------------|------------|
# |<img src="1n_total_notation1.jpg" width="300"/>|<img src="1n_total_notation2.jpg" width="300"/>|
# 
# Analog kann man eine totale 1:1 Beziehung folgendermaßen darstellen:
# 
# <img src="11_total_notation.jpg" width="300"/>
# 
# 

# ### Entitytypen und Rollen

# Entitytypen können mehr als einmal in einer Relationship auftauchen, beziehungsweise kann ein Entitytyp durch einen Relationshiptyp mit sich selbst verbunden sein. Dabei tauchen sie jeweils in unterschiedlichen **Rollen** auf. Die ER-Modellierung ermöglicht die explizite Modellierung von Rollen durch Annotation an den Kanten der Relationships. 
# 
# **Beispiel (Rolle 1):** Im folgenden Beispiel wird modelliert, dass Filme Fortsetzungen voneinander sein können. Dabei taucht der Entitytyp Film einmal in der Rolle des Originals und einmal in der Rolle der Fortsetzung mit dem Relationshiptypen "ist_Fortsetzung" auf.
# 
# <img src="rolle_relationship.jpg" />

# **Beispiel (Rolle 2):** Im folgenden Beispiel taucht Studio in zwei Rollen auf: als Stammstudio und als Vertragsstudio. 
# <img src="rolle_relationship2.jpg" />
# 
# Diese Modellierung impliziert, dass das Stammstudio eines Schauspielers einem anderen Studio erlaubt den/die Schauspieler*in für einen bestimmten Film
# auszuleihen. 
# 
# 
# Mithilfe von Rollen vermeidet man unnötig redundante Entitytypen zu modellieren. Theoretisch könnte man jede Rolle als einen Entitytypen modellieren. Dies würde bedeuten, dass wir zwei Entitytypen mit den gleichen Attributen und höchstwahrscheinlich einer großen Überlappung von Entities haben würden. 
# 
# 

# ### n-äre Relationships

# Relationshiptypen können auch zwischen mehreren bis zu "n" Entitytypen existieren. Beispielsweise könnte man die Beziehung, dass  ein/e Schauspieler*in  bei einem Studio für eine bestimmten Film unter Vertrag steht, als einen ternären Relationshiptypen wie folgt dargestellt modellieren. 
# 
# <img src="n-aer_relationships.jpg" width="500"/>
# 
# Die Instanz eines solchen Relationshiptypen kann man dann als Tripel darstellen.
# 
# 
# Normalerweise versucht man n-äre Relationshiptypen zu vermeiden, da diese schwer nachzuvollziehen sind. Insbesondere sind Kardinalitäten nicht sofort ersichtlich. In unserem Beispiel muss man genau überlegen, wie der Pfeil am Studio zu interpretieren ist. Eine mögliche Interpretation des Pfeiles ist, dass jede Kombination von Schauspieler\*in und Film mit nur einem Studio in Beziehung steht. Man könnte aber auch rauslesen, dass jede/r Schauspieler\*in mit beliebig vielen Filmen, aber nur einem Studio in einer Beziehung steht. Analog kann jeder Film nur mit einem Studio aber beliebig vielen Schauspieler\*innen in Verbindung stehen. Um solche Mehrdeutigkeiten zu verhindern, sollte man sich bei der Modellierung auf binäre Relationshiptypen einschränken.

# ### Konvertierung in binäre Relationships

# Manchmal bietet sich im Modellierungsprozess an zunächst komplexe Relationshiptypen als n-äre Relationshiptypen zu modellieren und diese erst dann in binäre Relationshiptypen umzuwandeln. Bei dieser Konvertierung entsteht ein neuer Entitytyp, welcher durch binäre N:1 Relationshiptypen alle anderen Entitytypen verbindet. 
# 
# Falls ein Entitytyp mehrere Rollen spielt, entsteht pro Rolle ein Relationshiptyp.
# Attribute des Relationshiptyps werden an den neuen Entitytyp angehängt.
# 
# **Beispiel (Konvertierung in binäre Relationshiptypen):** Im folgenden haben wir unser Modell mit dem 4-ären Relationshiptypen ist_unter_Vertrag von **Beispiel (Rolle 2)** in ein Modell mit nur binären Relationshiptypen umgewandelt.
# 
# | n-äre Relationshiptypen | konvertiert zu binären Relationshiptypen |
# |-------------------------|------------------------------------------|
# <img src="rolle_relationship2.jpg" width="500" /> | <img src="n-aer_relationships_konvertiert.jpg" width="500" />
# 
# Wir haben einen neuen Entitypen "Vertrag" definiert ,welcher in N:1 Beziehung die ursprünglichen Beziehungen darstellt. Die Modellierung ist nicht vollständig äquivalent. Theoretisch könnte es nun mehrere Verträge mit der gleichen Kombination von  Studios, Schauspiler\*innen und Filmen existieren, das wären dann Vertragsduplikate. In der ursprünglichen Modellierung könnte das nicht passieren, da der Vertrag als Relationshiptyp mit entsprechenden Kardinalitäten eingeschränkt ist. 

# ### Attribute an Relationships

# In manchen Fällen ist es hilfreich, Relationships Attribute zuzuordnen. Damit stellt man sicher, dass das Attribut nur gesetzt ist, wenn eine Beziehung zwischen zwei Entitytypen existiert. 
# 
# **Beispiel:** Im folgenden Modell wird modelliert, dass in einem Vetrag ein Gehalt festgestellt wird. Eine Zuordnuung an Schauspieler\*in, Film oder Studio ist hier nicht sinnvoll
# Eine Schauspieler\*in könnte für verschiedene Filme unterschiedliche Gehälter bekommen. Verschiedene Schauspieler\*innen könnten für den selben Film unterschiedliche Gehälter bekommen. Ein Studio könnte verschiedenen Schauspieler\*innen unterschiedliche Gehälter zahlen.
# 
# <img src="attribute_relationship.jpg"  width="500"/>
# 
# 

# ## Spezielle Relationshiptypen: IST-Beziehung

# Das ER-Modell erlaubt spezielle Beziehungen, wie Subklassenbeziehungen explizit zu modellieren. Dabei wird modelliert, dass ein Entitytyp in einer Subklassenbeziehung zu einem anderen Entitytypen steht. Dabei ist die Subklasse jeweils eine Spezialisierung der oberen Klasse. Somit könnte es weniger Entitäten in der Subklasse geben, die jedoch mehr spezialisiere Attribute haben und in weiteren speziellen Relationshiptypen auftauchen. 
# Im ER-Modell gibt es hierzu den Relationshiptypen IST oder is-a. Zudem wird der Relationshiptyp als Dreieck dargestellt wobei die Spitze des Dreiecks zur Superklasse zeigt. IST-Relationshiptypen haben immer eine 1:1 Kardinalität: Ein Entity der Subklasse ist auch immer Entity der Superklasse. Pfeile sind bei dieser Darstellung nicht notwendig. 
# Das ist anders als bei objekt-orientierten (OO) Modellen
# In OO sind Objekte immer einer Klasse zugehörig und Subklassen erben von der Superklasse.
# In ER sind Entities in allen Subklassen repräsentiert in die sie gehören, und der jeweiligen Superklasse.
# 
# **Beispiel (ist-relationship):** Im folgenden Beispiel wurde modelliert, dass jede Filmentität entweder der Subklasse Krimi oder Zeichentrickfilm oder beiden oder keinem angehören kann. Die Entität muss dann entsprechend in den jeweiligen Entitytypen auftauchen.
# 
# <img src="ist_relationship.jpg" WIDTH="500" />

# Beispielfilme:
# - „Krieg der Sterne“ ist weder ein Zeichentrickfilm noch ein Krimi und hat somit vier Attribute.
# - „Prinzessin Mononoke“ ist ein Zeichentrickfilm und hat somit vier Attribute und „Stimmen“-Relationships.
# - „Prisoner“ hat vier Attribute und zusätzlich das Attribut „Waffen“.
# - „Roger Rabbit“ ist sowohl ein Krimi als auch ein Zeichentrickfilm und hat somit die vier Filmattribute, zusätzlich das Attribut „Waffen“ und „Stimmen“-Relationships.

# ## Nebenbedingungen(Constraints)

# Daten unterliegen häufig bestimmten Einschränkungen und Nebenbedingungen. Nebenbedingungen dienen oft dazu Entitytypen und Relatioshiptypen eindeutig identifizieren oder einschränken zu können. 
# Zu den gebräuchlichen Nebenbedingungen gehören unter anderem Schlüssel und Fremdschlüssel. Schlüssel sind Attributkombinationen die Entities eindeutig identifizierbar machen. Fremdschlüssel andererseits stellen referenzielle Integrität her. Damit wird die Existenz von bestimmten Entitytypen von anderen abhängig. Andere Einschränkungen betreffen Wertebereiche von Attributen und Kardinalitäten. Wir werden im Folgenden die wichtigsten Nebenbedingungen, die man im Rahmen der ER-Modellierung verwendet genauer betrachten. Wichtig ist bei der Bewertung von Nebenbedingungen, dass diese als Teil des konzeptionellen Entwurfes allgemeingültig definiert werden. Zufällig existierende Beziehungen in konkreten Daten können nicht automatisch zur Nebenbedingung qualifiziert werden.

# ### Schlüssel

# Ein Schlüssel ist eine (minimale) Menge von Attributen eines Entitytyps, für die gilt, dass keine zwei Entities gleiche Werte in allen Schlüsselattributen haben. Beispielsweise könnte für unseren Entitytypen Filme die Kombination aus Film und Jahr als Schlüssel fungieren. Die Wahl eines solchen Schlüssels muss mit Bedacht geschehen. Die Unterscheidbarkeit von Entities in der realen Welt muss durch die Schlüsseleigenschaften gewährleistet sein. Anderenfalls wird man ähnliche Entities nicht zeitgleich im Modell aufnehmen und von einander unterscheiden können. Würde man beispielsweise, nur den Titel eines Films als den Schlüssel auswählen, könnte man nicht mehr unterschiedliche Filme mit dem gleichen Titel von einander unterscheiden. Dabei gibt es oft Wiederverfilmungen der gleichen Geschichte mit dem gleichen Titel, wie z.B. "Hamlet", "King Kong". Die Kombination {Titel, Jahr} ist hier wahrscheinlich sinnvoller. 
# 
# Generell muss bei der ER-Modellierung für jeden Entitytypen ein Schlüssel angegeben werden. Manchmal gibt es mehrere Möglichkeiten einen Schlüssel zu definieren. Beispielsweise wird in Deutschland jede Person durch die Personalausweisnummer sowie der Steuernummer eindeutig identifiziert. Bei der Modellierung von Entitytypen ist es jedoch üblich einen Primärschlüssel auszuwählen. Bei IST-Beziehungen muss die Wurzel-Superklasse sämtliche Schlüsselattribute enthalten.
# 
# 
# Schlüsselattribute werden im ER-Modell durch Unterstreichen der Attributnamen dargestellt. 
# 
# **Beispiel:** Im folgenden Beispiel haben wir für jeden Entitytypen Schlüsselattribute angegeben. Filme werden durch {Titel, Jahr} , Schauspieler\*innen durch {Name, Adresse} und Studios durch {Name} jeweils eindeutig identifziert. 
# 
# <img src="schluesselbeispiel_film.jpg" width="500" />
# 

# ### Referentielle Integrität

# Referentielle Integrität erzwingt die Zuordnung von Entities zu einem Entity eines anderen Entitytypen. Bisher haben wir N:1-Relationshiptypen betrachtet, bei denen gilt, dass eine Beziehung zwischen einem Entity der n-Seite mit höchstens einem Entitytypen der 1-Seite existiert. Aber in dieser Modellierung kann ein Entity der n-Seite auch mit keinem Entity der 1-Seite in Verbingung stehen. Beispiesweise kann in unserem Film-Beispiel ein Film zu höchstens einem Studio gehören. Ein Film kann auch ohne ein Studio existieren. 
# Referentielle Integrität erzwingt die Existenz und Repräsentation des Studios. Damit stellt man sicher, dass nur Filme in der Datenbank aufgenommen werden, die auch wirklich einem Studio zugehören. 
# Das heißt, dass das Datenbanksystem beim Einfügen/Ändern eines Films prüfen muss, dass ein entsprechendes Studio vorhanden ist. Weiterhin wird sicher gestellt, dass ein Studio nicht gelöscht werden darf, solange es noch Filme besitzt.
# 
# Die Darstellung von referenzieller Integrität erfolgt im ER-Modell anhand eines offenen Pfeiles. Diese Darstellung haben wir für die Modellierung von totalen Beziehungen kennengelernt. Eine referenzielle Integrität beschreibt tatsächlich eine totale Abbildung eines Entitytypen auf einen anderen Entitytypen.

# **Beispiel:** Im Folgenden Beispiel wird an zwei Stellen referenzielle Integrität erzwungen. Zunächst wird erzwungen, dass jeder Film genau einem Studio zugeordnet werden muss. Weiterhin leitet jede/r Vorsitzend/e genau ein Studio. Vorsitzende können nicht ohne Studios existieren. Ein Studio kann jedoch ohne Vorsitzende existieren. 
# 
# <img src="referentielle_integritaet.jpg" width="500"/>

# ### Weitere Nebenbedingungen

# Es gibt weitere Nebenbedingungen, die man informell mitmodellieren kann. Beispielsweise könnte man Datentypen und Wertebereiche von Attributen modellieren. Grundsätzlich ist an dieser Stelle, dieser Detailgrad vermutlich nicht sinnvoll, da Datentypen oft datenbankabhängig sind. 
# Was man jedoch möglicherweise bereits modellieren möchte, sind alle Einschränkungen hinsichtlich Kardinalitäten. Hierzu haben wir die min/max und die numerische Notation kennen gelernt, die uns erlauben die Anzahl der Beziehungen, die eine Entity eingehen kann genauer zu spezifizieren und zu erzwingen. 

# ## Schwache Entitytypen

# In bestimmten Situationen können Entities nicht allein anhand ihrer Attribute identifiziert werden:
# <br>
# 1. Falls sie in eine Teil-Von-Hierarchie fallen. Zum Beispiel sind Geschäftszweige Untergruppen eines Unternehmens und benötigen zur weiteren Identifizierung auch die Bezeichnung des Unternehmens. Dies ist anders in der IST-Hierarchie, in der Subklassen Spezialisierungen aber nicht Bausteine der generalisierenden Entitytypen sind.  
# <br>
# 2. Entities, die zur Eliminierung n-ärer Relationships erschaffen wurden.
# <br>
# 
# Solche Entitytypen werden als schwache Entitytypen bezeichnet. 
# Ein Entitytyp ist schwach, wenn es zur eindeutigen Identifizierung dessen Entities, n:1 Relationshiptypen zu anderen Entities hinzugezogen werden müssen, um Schlüssel der verwandten Entities hinzuzunehmen. Die Darstellung eines schwachen Entitytyps erfolgt durch eine doppelte Umrandung des Entitytypen. Zudem werden alle unterstützenden N:1 Relationshiptypen doppelt umrandet. Man kann hier zur besseren Verdeutlichung auch den Pfeil der totalen Beziehung nutzen. 
# 
# 
# Falls E ein schwacher Entitytyp ist, besteht sein Schlüssel aus…
# - … null oder mehr eigenen Attributen
# - … und den Schlüsselattributen von Entitytypen, die über „unterstützenden Relationshiptypen“ n:1 erreicht werden können.
# <br>
# 
# Unterstützende Relationshiptypen bilden n:1 vom schwachen Entitytypen zu einem anderen Entitytypen ab.
# Es muss hierbei referentielle Integrität gelten, das heißt, dass die Abbildung total sein muss.
# Falls der referenzierte Entitytyp wiederum schwach ist, werden (rekursiv) weitere Schlüsselattribute übernommen. 

# **Beispiel(Nicht-IST-Hierarchie 1):**
# Im folgenden Beispiel sieht man die Modellierung von Crews und Studios. Es ist davon auszugehen, dass jedes Studio mehrere Crews hat. Das heißt, dass hier eine strukturelle Hierarchie herrscht. Jede Crew hat zwar eine Nummer als Schlüssel, es ist jedoch unwahrscheinlich, dass Crews verschiedener Studios immer unterschiedliche Nummern haben. Vermutlich fängt die Nummerierung in jedem Studio bei 1 an. Deshalb ist zu der Idenzifizierung einer Crew, in einer Datenbank auch der Schlüssel des jeweiligen Studios notwendig. Damit ist Crew ein schwacher Entitytyp.
# 
# <img src="schwache_ent_bsp1.jpg" width="500" />
# 

# **Beispiel (Auflösung n-ärer Relationshiptypen):** Der Entitytyp Vetrag wurde als Verbindungsentitytyp eingeführt um den 3-ären Relationshiptypen ist\_unter\_Vertrag durch mehrere binäre Relationshiptypen zu ersetzen. Beachten Sie, dass all jene Relationshiptypen N:1 sind. Es sollte nicht möglich sein, dass ein Vetrag ohne Zuordnung zu allen Parteien, wie Schauspieler\*in und Studio sowie dem eigentlichen Film als Gegenstand des Vertrages existiert. Damit ist Vetrag ein schwacher Entitytyp und kann nur durch die Aufzählung der Schlüssel aller anderen in Beziehung stehenden Entitytypen eindeutig identifiziert werden.
# 
# <img src="schwache_ent_bsp3.jpg" width="500" />

# ### Kann man schwache Entitytypen vermeiden?

# Eine der Ursachen für die Entstehung von schwachen Entitytypen ist, dass es nicht möglich ist einen allgemeingültigen Schlüssel zu deklarieren.
# In der Realität werden sehr oft künstliche IDs verwendet.
# - ISBN, SNN, VIN, etc.
# 
# Für unser Vertragsbeispiel hätten wir theoretisch auch eine Vertragsnummer definieren können. Zwar hätten wir immernoch die totale Beziehung zu den Vertragsgegenständen und Parteien, jedoch wäre jeder Vertrag als solches eindeutig identifizierbar. 
# 
# Um solch einen künstlichen Schlüssel zu definieren bedarf es einer anerkannten Autorität. 
# 

# ## Erweitertes ER-Modell (EER)
# 
# Bisher haben wir die Kernkonzepte der ER-Modellierung kennen gelernt. Die ER-Modellierungssprache beinhaltet auch weitere Erweiterungen, die es ermöglichen, Konzepte konkreter zu modellieren. In dieser Vorlesung stellen wir lediglich einige dieser Möglichkeiten vor.

# ### Weitere Attributarten
# 
# Die erste Erweiterung im EER sind weiter Spezifikationen von Attributen. Wie in den dargestellten Beispielen zu sehen ist ist es möglich verschiedene Nebenbedingungen zu modellieren. 

# <img src="weitere_attributnamen.jpg" />

# **Optionales Attribut**  ist ein Attribut, bei dem der Attributwert nicht für jede Entität vorhanden sein muss. Dies wird durch ein O auf der Verbindungskante gezeigt. Beispielsweise, handelt es sich bei Telefon um ein Optionales Attribut.
# 
# **Abgeleitetes Attribut** ist ein Attribut, dessen Wert von anderen Attributen hergeleitet werden kann. Beispielsweise kann der Bruttopreis aus dem Nettopreis und dem Steuersatz berechnet werden. 
# 
# **Mengenwertiges Attribut** enthält eine Menge von Werten. Beispielsweise kann ein Kunde mehrere Vornamen haben. 
# 
# **Strukturiertes Attribut** ist ein Attribut, welches sich aus anderen Attributen zusammensetzt. Beispielsweise setzt sich eine Adresse aus drei unterschiedlichen Komponenten zusammen: Straßenname, Postleitzahl und Ort. 

# ### Aggregation

# Wir haben bereits die IST-Beziehung kennen gelernt. Wir haben auch über Teil-von-Beziehungen im Rahmen von schwachen Entitytypen gesprochen. Im EER werden letztere als Aggregationen dargestellt und ermöglichen eine entsprechende Visualisierung, die man durch hierarchische Darstellung der Zusammensetzung, wie unten im Fahrradbeispiel zu sehen ist, modellieren kann.  
# Ohne EER-Semantik müsste man die Kardinalitäten zusätzlich modellieren. In der Darstellung unten, erwartet man, dass diese Kardinalitäten implizit vorhanden sind. 

# <img src="aggregation.jpg" />

# ## Designprinzipien

# Jetzt wo wir die wichtigsten Modellierungselemente der ER-Sprache kennen, wären wir in der Lage beliebige Informationen zu modellieren. Wir haben jedoch noch nicht darüber gesprochen, mit welchem Ansatz man jeweils diese Modellierungselemente wählen sollte. Es ist häufig so, dass man den selben Sachverhalt auf unterschiedlicher Weise modellieren kann. Jedoch ist nicht jede Modellierung sinnvoll. Im Folgenden wollen wir drei Grundprinzipien kennenlernen, die uns helfen eine sinnvolle Darstellung für eine informelle Beschreibung auszuwählen:

# - Treue zur Anwendung
# - Vermeidung von Redundanz
# - Einfachheit
#     - Sparsamer Einsatz von Relationships
#     - Sparsamer Einsatz von Attributen
#     - Sparsamer Einsatz von schwachen Entitytypen

# ### Anwendungstreue

# Die Anwendungstreue ist zunächst die offensichtlichste Anforderung. 
# Entitytypen und Attribute sollten natürlich die Realität widerspiegeln. Entitytypen sollten Attribute führen, die spezifiziert werden können. Relationshiptypen sollen Verhältnisse der Realität widerspiegeln. Dazu gehören reelle Kardinalitätsbeziehungen und Abbildungen. 
# 
# **Beispiel:** Schauspieler\*in und Filme stehen in einer m:n Beziehung. n:1, 1:n oder 1:1 wären inkorrekte Wiedergaben der Realität

# ### Redundanz

# Redundanz tritt auf, wenn der gleiche Sachverhalt auf mehr als eine Weise ausgedrückt wird. Dies kann durch ungeschickte Modellierung passieren. In der Datenbankwelt möchte man nach Möglichkeit **unbeabsichtigte** Redundanz verhindern, da Redundanz nicht nur Platz verschwendet ,sondern auch Situationen hervorrufen kann, dass Daten nicht mehr konsistent vorliegen. Man muss bei der Änderung von Daten an allen redundanten Stellen die Daten ändern. 

# **Beispiel (Redundanz):** Im Folgenden Beispiel sehen wir drei Möglichkeiten um Studios zu modellieren. Alle drei Varianten sind anwendungstreu. Die Modellierung in der oberen Zeile ist eine sinnvolle Modellierung. In der mittleren Zeile, haben wir für jeden Film den Studionamen zusätzlich als Attribut modelliert. Damit taucht der Name redundant auf. Dies ist ein offensichtliches Beispiel für redundante Modellierung, da zu jedem Film der Studioname zweimal gespeichert wird. Die Modellierung in der unteren Zeile modelliert Studio nur als Attribute von Film. Hier gibt es zwar keine Doppelung pro Film, jedoch besteht weiterhin Redundanz. Wenn wir davon ausgehen, dass ein Studio mehrere Filme besitzt, speichern wir den Namen und die Adresse jedes Studios mehrmals, nämlich ein mal pro Film. Bei unserer Modellierung in der obersten Zeile speichern wir jedes Studio nur einmal und Film sind durch die besitzt Beziehung jeweils mit der gleichen Studioentity verbunden. 

# <img src="redundanz1.jpg" />

# ### Einfachheit

# Eine Anforderung an der Informationsmodellierung ist, dass Konzepte möglichst einfach modelliert werden sollen. Einfachfachheit bezieht sich hierbei darauf, dass man versucht die gleiche Information mit wenigen Strukturelementen zu modellieren. Insbesondere geht es darum unnötige Entitytypen und Relationshiptypen zu vermeiden. Dies gilt insbesondere für ableitbare Relationshiptypen. 

# **Beispiel:** Das folgende Beispiel zeigt eine semantisch korrekte Modellierung der Informationen zu Filmen, Holdings und Studios. Man hätte jedoch die 1:1 Beziehung zwischen Holding und Studio wesentlich einfacher durch Attributbeziehungen modellieren können. 
# 
# <img src="einfachheit.jpg" width="700"/>

# #### Relationships

# Nicht jede mögliche Beziehung sollte abgebildet werden. Die Darstellung von ableitbaren Bezieheungen führt zu Redundanz und unnötiger Komplexität. Dies erschwert nachträgliche Änderungen in einer Datenbank. 
# Änderungen auf der Datenbank werden komplex, was Aufwand und Fehleranfälligkeit erhöht. 
# 
# **Beispiel:** Im Folgenden Beispiel werden zusätzlich zu der ternären Beziehung *ist\_unter\_Vertrag* auch zwei weitere Beziehungen *spielt\_in* und *besitzt* modelliert. Beide Beziehungen gelten jedoch immer nur dann, wenn eine Schauspieler\*in mit einem Studio zu einem Film im Vertrag steht. Damit sind beide Beziehungen ableitbar. Jede Änderung oder Löschung der *ist\_unter\_Vertrag* Beziehung muss dazuführen, dass auch entsprechende Relationships in *spielt\_in* und *besitzt* geändert bzw. gelöscht werden müssen. 

# <img src="relationships1.jpg" width="700" />
# 

# #### Attribut vs. Element

# Eine weitere Möglichkeit Modelle zu vereinfachen besteht, darin wenn möglich Attribute statt Entitytypen und Relationshiptypen zu nutzen. Diese sind auch einfacher zu implementieren. 
# 
# Grundsätzlich ist ein Entitytyp gerechtfertigt falls…
# - er mehr als nur den Namen eines Objekts darstellt,
# - oder er der n-Teil einer 1:n Relationship ist.
# 
# **Beispiel:** Im folgenden Beispiel sind beide Entitytypen *Filme* und *Studios* gerechtfertigt. *Filme* ist der n-Teil des *besitzt* Relationshiptyps und *Studios* hat mehr als ein Attribut. 

# <img src="attributvselement1.jpg" />
# 

# Beim folgenden Beispiel könnte man argumentieren, dass Studios einfach als Attributname von Filme modelliert werden könnte. 

# <img src="attributvselement2.jpg" />

# Tatsächlich ist das folgende Modell deutlich einfacher und modelliert den selben Sachverhalt. Jedoch aus der Diskussion zur Redundanz wissen wir, dass die folgende Modellierung zur redundanten Speicherung des gleichen *Studios* für unterschiedliche *Filme* führen kann. Tatsächlich können die Anforderungen Einfachheit und Redundanzfreiheit manchmal im Widerspruch stehen. 

# <img src="attributvselement3.jpg" />

# ## Zusammenfassung ER-Modellierung
# 
# In diesem Kapitel haben wir die ER-Modellierungssprache kennen gelernt, die uns erlaubt aus informellen Informationsbeschreibungen visuelle und formalisierte Informationen anhand von Entitytypen, Relationshiptypen und Attributen zu modellieren. In der ER-Modellierung können wir auch bereits Nebenbedingungen wie Kardinalitäten und Schlüsselbeziehungen modellieren. Schließlich haben wir Anforderungen für eine sinnvolle Modellierung diskutiert. Im nächsten Kapitel werden wir den nächsten Schritt im Datenbankentwurf besprechen. Es soll nun darum gehen, wie man aus einem ER-Modell ein relationales Modell herleiten kann, welches dann direkt in Datenbankmanagementsystemen abgebildet werden kann. 
