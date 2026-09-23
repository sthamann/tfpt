# Beobachter, Gedächtnis und Selbstmodell im gemeinsamen Prozessraum

10. September 2026. **Gedächtnis, Vorhersage und Handlung lassen sich in einer gemeinsamen Dynamik exakt beschreiben. Bewiesen wird hier, wann eine kleinere Zustandsbeschreibung sämtliche erlaubten zukünftigen Antworten erhält. Eine Ableitung subjektiven Erlebens ist damit nicht gegeben.**

## 1. Präzise Funktionen statt einer Gleichsetzung aller Begriffe

Ein Beobachter erhält Antworten, führt einen internen Zustand fort und wählt Eingriffe. Eine brauchbare gemeinsame Beschreibung lautet: äußerer Prozess, erlaubte Eingriffe, Antwortfunktionen, Gedächtnisaktualisierung, Entscheidungsregel und Ressourcenbudget. Der Begriff „Projektion“ bezeichnet dabei zunächst eine ausdrücklich angegebene Abbildung; nicht jede Abbildung ist eine dynamisch geschlossene Projektion.

| Begriff | Hier verwendete operative Bedeutung | Was zusätzlich festgelegt werden muss |
|---|---|---|
| Information | Verringerung der Unsicherheit über eine bestimmte Frage; statistisch etwa gegenseitige Information | Frage, Verteilung und zugängliche Messungen |
| Gedächtnis | Fortgeführte Zusammenfassung der Geschichte, die spätere Antworten oder Entscheidungen beeinflusst | Welche zukünftigen Eingriffe und Ziele erhalten bleiben sollen |
| Vorhersagemodell | Abbildung von Geschichte und gewählter zukünftiger Handlung auf Antworten beziehungsweise deren Verteilung | Fehlermaß und Prüfung an bislang nicht verwendeten Eingriffen |
| Selbstmodell | Internes Modell eigener Zustände, Operationen oder Grenzen, dessen Vorhersagen überprüfbar sind | Modellgegenstand, Genauigkeit und zulässige Störungen |
| Handlungsfähigkeit | Eine Regel verändert durch ausführbare Eingriffe den weiteren Prozess | Kontrolle über die Eingriffe, Zielkriterium und Kosten |
| Intelligenz als messbare Fähigkeit | Lernen und Übertragen wirksamer Vorhersage-/Handlungsregeln über eine ausgewiesene Aufgabenfamilie | Familienumfang, neuartige Aufgaben, Leistung und Ressourcen; keine universelle IQ-Definition |
| Subjektives Erleben | Dass es für ein System etwas bedeutet, in einem Zustand zu sein | Eine zusätzliche Theorie und empirisch unterscheidbare Zuordnung; die Funktionsdefinitionen enthalten sie nicht |

Zustände über zukünftige Antworten darzustellen ist ein etablierter Ansatz. Predictive State Representations modellieren kontrollierte Systeme mit handlungsbedingten Vorhersagen; die Originalarbeit zeigt für gegebene endliche POMDP-Modelle eine entsprechende lineare Darstellung. Sie beweist damit weder die leichte Entdeckung des Modells aus beliebigen Daten noch effiziente allgemeine Handlungsplanung. [Littman–Sutton–Singh, Theorem 1](https://proceedings.neurips.cc/paper/2001/file/1e4d36177d71bbb3558e43af9577d70e-Paper.pdf)

## 2. Der endliche Funktionssatz

Gegeben seien ein endlicher Zustandsraum S, dieselbe endliche erlaubte Aktionsmenge A in jedem Zustand, Übergänge δ(s,a) und Antworten λ(s,a). Antworten enthalten auch die für Entscheidungen relevanten Belohnungen. Ein Aktionswort w erzeugt eine vollständige Antwortfolge T_s(w).

Definiere

\[
s\sim t\quad\Longleftrightarrow\quad T_s(w)=T_t(w)\ \text{für jedes endliche }w\in A^*.
\]

**Satz.** Der Quotient S/∼ ist die gröbste deterministisch fortführbare Zustandsbeschreibung, die alle zukünftigen Antworten erhält. Allgemein besitzt eine surjektive Kompression q:S→Q exakte Übergänge und Antworten auf Q genau dann, wenn für jedes a gilt:

\[
q(s)=q(t)\Longrightarrow
\begin{cases}
\lambda(s,a)=\lambda(t,a),\\
q(\delta(s,a))=q(\delta(t,a)).
\end{cases}
\]

**Beweis.** Notwendigkeit folgt unmittelbar daraus, dass ein Q-Zustand unter derselben Aktion nur eine Antwort und einen Nachfolgezustand besitzt. Unter den beiden Bedingungen definiert man die Antwort und den Übergang mittels irgendeines Vertreters s; beide sind wohldefiniert. Induktion über die Wortlänge beweist alle zukünftigen Antwortgleichheiten. Für ∼ stimmen zunächst die Ein-Schritt-Antworten. Die Antworten nach Aktion a auf jedes weitere Wort v sind die Endstücke von T_s(av); deshalb sind die Nachfolger wiederum äquivalent. Jede andere zulässige Kompression darf nur ∼-äquivalente Zustände zusammenfassen und verfeinert daher S/∼. ∎

Die Aussage gilt auch unter adaptiven Entscheidungen: Gleiche bisherige Antworten veranlassen dieselbe beobachtungsbasierte Regel zu denselben Handlungen. Bei Zufallsregeln koppelt man dieselben Zufallsbits. Somit bleiben alle endlichen Antwort-/Belohnungsverteilungen unter solchen Regeln erhalten. Bei bekanntem funktionalem Anfangszustand stimmen auch optimale endliche Belohnungswerte; das folgt alternativ induktiv aus der Bellman-Rekursion.

Eine Nuance ist wesentlich: Ein redundanter Gedächtniscode kann genug Information für sämtliche Vorhersagen enthalten, während seine zusätzlichen Labels nicht eindeutig fortführbar sind. Für einen **geschlossenen Zustandsraum** wird deshalb auch die zweite Bedingung benötigt. Der kanonische Quotient erfüllt beides.

Der Quotient ist endlich konstruierbar: Beginne mit einer einzigen Klasse und trenne nach Ein-Schritt-Antworten und Nachfolgerklassen. Nach höchstens |S|−1 echten Verfeinerungen ist die Partition stabil. Ein verbleibender Unterschied hat einen Zeugen mit höchstens |S|−1 Aktionen. Das setzt die vollständig gegebene endliche Übergangstabelle voraus; es erlaubt keine allgemeine Vollständigkeitsbehauptung aus wenigen Messdaten eines unbekannten Systems.

## 3. Vollständig geprüftes Gedächtnisbeispiel

Das Programm verwendet vier Zustände (b,g) mit zwei Bits. b ist ein beschreibbares Gedächtnisbit; g schaltet bei jedem Schritt um, beeinflusst jedoch keine erlaubte Antwort. Die sechs Aktionen heißen warten, schreibe0, schreibe1, lesen, rate0, rate1. Schreiben setzt b, Lesen meldet b und kostet einen Belohnungspunkt, richtiges Raten liefert einen Punkt. Die übrigen Antworten sind leer.

Alle 15 Partitionen des Viererraums wurden untersucht. Ergebnis: Der minimale vollständige Quotient besitzt zwei Zustände, nämlich b=0 und b=1. Das Zusatzbit g darf entfallen. Bei ausschließlich erlaubtem Warten genügt dagegen **ein einziger** Zustand. Der minimale Raum hängt somit von den erlaubten Eingriffen ab.

„schreibe0, dann 100-mal warten“ und „schreibe1, dann 100-mal warten“ erzeugen identische Antwortfolgen. Ein einziges anschließendes Lesen unterscheidet sie. Die ausgeführten Schreibaktionen gehören jedoch zur Geschichte: Wer sie aus dem Gedächtnis entfernt, verliert eine entscheidungsrelevante Information. Auch bei unbekanntem Anfangsbit ist passives Warten beliebig lange uninformativ; ein Leseeingriff schafft Zugang.

63 exakte Kontrollen prüfen den Quotienten, sämtliche Ein-Schritt-Abschlüsse, 259 Aktionswörter bis Länge drei, die Gegenzeugen und Bellman-Werte bis Horizont acht. Die ausgeschriebene Induktion begründet die unbegrenzte Wortaussage; die Testanzahl allein tut dies nicht. Es liegt kein formales Beweisassistent-Zertifikat vor.

## 4. Modellieren muss Interventionen einschließen

Zwei einfache kausale Modelle verwenden ein faires Bit U:

\[
M_1:X=U,\ Y=X;\qquad M_2:X=U,\ Y=U.
\]

Beide zeigen ausschließlich die beobachteten Paare (0,0) und (1,1), jeweils mit Wahrscheinlichkeit 1/2. Erzwingt man jedoch X:=0, wird Y in M₁ sicher null; in M₂ bleibt Y fair verteilt. Eine noch so genaue Anpassung der gemeinsamen Beobachtungsverteilung trennt diese Modelle nicht. Der Unterschied liegt in der Strukturannahme, welche Gleichung beim Eingriff ersetzt wird. Diese Interventionssemantik ist in kausalen Strukturmodellen ausdrücklich definiert. [Pearl, §3.2.1](https://web.cs.ucla.edu/~kaoru/SS-2009-57-Sup.pdf)

Für eine gemeinsame Universalraum-Beschreibung genügt daher nicht, dass zwei „Schatten“ dieselben bisher beobachteten Korrelationen reproduzieren. Ihre Übersetzung muss die tatsächlich erlaubten Eingriffe samt Antworten erhalten.

## 5. Selbstmodell und Rückkopplung bestimmen Erleben nicht

Ein Ein-Bit-Regler speichert eine Kopie m=b seines eigenen Bits. Für das Ziel r berechnet er a=m XOR r, führt b′=b XOR a aus und sagt m′=m XOR a voraus. Für alle vier Kombinationen (b,r) gilt exakt b′=m′=r. Er besitzt ein zutreffendes Selbstmodell, eine Handlungswahl und eine geschlossene Rückkopplung. Die vier Fälle sind geprüft.

Dieses Gegenmodell zeigt die logische Lücke: Die genannten Funktionen sind schon durch eine winzige Wahrheitstabelle realisiert. Fügt man der Beschreibung ein bisher undefiniertes Prädikat „erlebt subjektiv“ hinzu, erzwingen die Funktionsgleichungen weder dessen Wahrheit noch dessen Falschheit. **Es ist kein Nachweis, dass der Regler tatsächlich nichts erlebt, und kein allgemeiner Beweis gegen Maschinenbewusstsein.** Es widerlegt die Behauptung, aus diesen Funktionsbedingungen allein sei Bewusstsein bereits hergeleitet. Eine Gleichsetzung wäre eine zusätzliche Hypothese.

Auch empirische Bewusstseinstheorien werden an spezifischen Vorhersagen geprüft. COGITATE verglich 2025 vorregistrierte Vorhersagen von IIT und GNWT bei 256 Teilnehmenden mit drei Messmodalitäten. Einige Vorhersagen passten, zentrale andere wurden herausgefordert. Untersucht wurden konkrete neuronale Vorhersagen über bewusste visuelle Inhalte; daraus folgt weder eine allgemeine Gleichsetzung von Selbstmodell und Erleben noch eine vollständige Widerlegung sämtlicher Varianten beider Theorien. [COGITATE, Originalabstract und Abbildungslegenden](https://pubmed.ncbi.nlm.nih.gov/40307561/)

## 6. Information, Gedächtnis und Rechenaufwand bleiben verschieden

Bei unabhängigen fairen Münzwürfen beträgt die Entropierate ein Bit pro Schritt, während zur optimalen Vorhersage kein vergangenes Bit benötigt wird. Eine deterministische alternierende Folge mit zufälliger Anfangsphase hat Entropierate null, benötigt aber ein Phasenbit für genaue Vorhersagen. Viel Zufälligkeit ist daher weder viel Gedächtnis noch Intelligenz. In der computational mechanics werden entsprechend Entropierate und statistische Komplexität des minimalen Vorhersagezustands unterschieden. [Shalizi–Crutchfield, Definitionen 4–5 und 12](https://arxiv.org/pdf/cond-mat/9907176)

Auch ein perfektes Modell beseitigt die Schwierigkeit der Handlungswahl nicht. Ein kompakt beschriebener Prozess kann n-mal eine Bitwahl erlauben und am Ende genau dann belohnen, wenn die gewählte Belegung eine eingegebene boolesche Formel erfüllt. Jeder Übergang und die Endprüfung sind leicht berechenbar. Eine allgemein schnelle optimale Handlungssuche würde trotzdem SAT lösen. Die ausgeschriebene Zustandstabelle kann exponentiell groß sein; Polynomialität in ihrer Größe wäre keine Polynomialität in der Formelgröße. Dies ist eine direkte Reduktion, kein Beweis von P≠NP.

Der tragfähige gemeinsame Nenner ist somit eine **Dynamik mit zugänglichen Eingriffen, fortführbarem Gedächtnis und überprüfbaren Antwortfunktionen**. Sie vereinheitlicht Funktionsbeschreibungen. Welche Eingriffe physisch existieren, wie günstig Modelle lernbar sind und ob subjektives Erleben entsteht, bleiben zusätzliche, getrennt zu begründende Fragen.

## Quellenscope und Reproduktion

PSR: Originaltext einschließlich Theorem und Abschlussargument gelesen. Pearl: Interventionsdefinition und ihre strukturellen Voraussetzungen gelesen. Shalizi–Crutchfield: Zustandsäquivalenz, Minimalität und Begriffsdefinitionen gezielt gelesen. COGITATE: Originalabstract und Abbildungslegenden über PubMed; Nature-Volltext/PMC/Oxford-Zugriff scheiterten, daher keine eigene Rohdaten- oder vollständige Methodenprüfung. Papadimitriou–Tsitsiklis (1987) wurde nur über den Verlagsabstract zur Komplexität kontrolliert; die SAT-Reduktion oben steht unabhängig davon.

`check_observer.py` läuft mit der Python-Standardbibliothek und schreibt `observer-checks.json` neu. `SOURCES.json` hält die gelesenen Quellen fest; `MANIFEST.json` bindet die eigenen Artefakte. Keine bisherigen Dateien oder Originalquellen verändert.
