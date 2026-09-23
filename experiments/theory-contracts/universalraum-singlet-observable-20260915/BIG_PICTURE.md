# Neue Vogelperspektive: derselbe Prozess in verschiedenen Ansichten

## B1. Was sich durch die drei weiteren Texte ändert

Die nachgereichten Texte werden als Vorschläge geprüft, nicht als bewiesene
Ergebnisse oder neue Arbeitsanweisungen übernommen. Die stärkste gemeinsame
Idee trägt: **Innere Identität, Zusammensetzung, Ort, Zeit und Auslese dürfen
nicht stillschweigend dasselbe Label erhalten.** Eine immer genauere Rechnung
innerhalb einer Bank ersetzt diese Verbindungen nicht. Die voranstehenden
lokalen Ergebnisse bleiben gültig; die fundamentale Priorität verschiebt
sich auf die gemeinsame Operations- und Kompositionsregel.

| Vorschlag | Prüfung und Konsequenz |
|---|---|
| Ort in Multiplizitäten statt in den 64 inneren Labels suchen | Sinnvolle Möglichkeit, aber Multiplizität beschreibt bereits chemische Umwandlung ohne Raum |
| Der große Kommutant könnte verborgenen Raum enthalten | Hamilton- und Symmetriekommutant sind verschieden; die Größe allein trägt diesen Schluss nicht |
| Den ganzen Z4-Ursprung statt nur den ladungserhaltenden Ausschnitt betrachten | Konkrete zusätzliche Terme existieren am selben W; ihre Verfügbarkeit ist noch nicht hergeleitet |
| Ladung +3 und Ladung -1 sind modulo vier gleich | Ein zusätzlicher Term kann sie dynamisch verbinden; die Operatoren sind nicht identisch |
| Zeitabhängige Kreuzantwort zeigt Transport | Im Allgemeinen falsch; unten steht ein exaktes Gegenbeispiel sogar bei Anfangskorrelation null |
| Mehrere Schatten könnten einen gemeinsamen Ursprung bestimmen | Möglich bei gemeinsamem Vertrag und ausreichender Unterscheidbarkeit; Übereinstimmung allein genügt nicht |
| Holografie könnte die fehlende Verbindung sein | Ein nativer isometrischer Kodierungsbaustein ist vorhanden; Raumgrenze, Schutz und gemeinsame Raumzeit fehlen |

Die zusätzlich eingefrorenen Texte heißen im Prüfpaket `multiplicity_z4.txt`,
`fundamental_reduction.txt` und `runtime_synthesis.txt`. Sie werden im
Hauptdokument vollständig angehängt. Die anschließende Schatten- und
Holografiefrage des Nutzers wurde durch eigene Rechnungen weiterverfolgt.

## B2. Noethers Frage: Welche Unterschiede kann die Dynamik überhaupt verändern?

Bei ungebrochener innerer Gruppe G zerfällt ein Zustandsraum als

\[
\mathcal H=\bigoplus_\lambda V_\lambda\otimes M_\lambda,
\qquad H=\bigoplus_\lambda I_{V_\lambda}\otimes h_\lambda,
\qquad \operatorname{End}_G(\mathcal H)
=\bigoplus_\lambda I_{V_\lambda}\otimes\operatorname{End}(M_\lambda).
\]

G-invariante Entwicklung darf die Kopien eines Typs verändern, nicht die
inneren Komponenten dieses Typs willkürlich auseinanderziehen. Das macht
Multiplizitäten zu einem möglichen Träger weiterer Dynamik. Es macht sie
noch nicht zu Orten. Schon die drei hellen N=3-Typen enthalten zwei Kopien:
einmal drei Fermionen, einmal einen Fermion plus einen Boson. Ihre jeweilige
Hamiltonmatrix lautet

\[
h_\lambda=\begin{pmatrix}0&g\sqrt\lambda\\g\sqrt\lambda&\Delta\end{pmatrix},
\qquad \lambda=7,10,12.
\]

Am Prüfpunkt g/Delta gleich 1/20 sind die maximalen Umwandlungswahrscheinlichkeiten
7/107, 1/11 und 3/28. Das ist echte symmetrieverträgliche Dynamik, zunächst
aber eine Veränderung der Zusammensetzung und kein Ortswechsel.

Wichtig ist die Richtung des Kommutanten: Im N=3-Sektor hat der Kommutant
der vollen inneren Gruppe die Dimension 16. Die viel größere Zahl
1444233216 betrifft den kleineren Kontrollsatz aus X und Bosonzahl.
Auf dem isolierten irreduziblen 64er-Pol ist der G-Kommutant sogar nur skalar,
während der Kommutant der dort skalaren Energie alle 64-mal-64-Matrizen
enthält. Die große Energiedegeneration ist kein Nachweis vieler Orte.

Für einen G-Singulett-Grundzustand und die ursprünglichen irreduziblen
Fermionoperatoren folgt aus Schurs Lemma

\[
C_{rs}(t)=\delta_{rs}\,c(t).
\]

Feste lineare Umbenennungen liefern lediglich einen Gramfaktor mal derselben
Zeitfunktion. Auch eine perfekte Kenntnis aller lokalen Spektrallinien würde
aus den 64 inneren Komponenten deshalb noch keine räumliche Anordnung machen.
Ein stationärer Grundzustand kann zeitabhängige Korrelationsfunktionen haben;
Nichtstationarität ist keine notwendige Voraussetzung dafür. Physische
Uhrenablesung und Zeitrichtung sind weitere Fragen.

## B3. Korrelation ist noch kein Eingriff: ein exakt gelöstes Gegenbeispiel

Zwei nicht miteinander wechselwirkende Qubits genügen:

\[
H=\tfrac12(Z_A+Z_B),\qquad
|\Omega\rangle=(|01\rangle+|10\rangle)/\sqrt2,
\qquad A=X_A,\quad B=Y_B.
\]

Der Zustand ist stationär. Trotzdem ist

\[
\langle\Omega|B e^{-itH}A|\Omega\rangle=\sin t.
\]

Die Kreuzkorrelation startet bei null und verändert sich mit der Zeit.
Es gibt dennoch keinerlei Signal von A nach B: Alle A-lokalen Operationen
kommutieren mit jedem zeitentwickelten B-lokalen Observablen. Für jedes
spurtreue lokale Quanteninstrument bleibt daher die unbedingte B-Statistik
unverändert. Eine Konditionierung auf ein Messergebnis in A wäre etwas anderes.

Der belastbare Übertragungstest ist stattdessen

\[
\delta_{A\to B}(t)=
\operatorname{tr}\!\left[B U_t\mathcal E_A(\rho)U_t^\dagger\right]
-\operatorname{tr}\!\left[B U_t\rho U_t^\dagger\right].
\]

A und B müssen zuerst als unabhängig adressierbare Teile definiert sein;
das Instrument muss verfügbar sein, ohne durch seine Definition schon B
anzusteuern. Erfolg bedeutet eine nichtverschwindende unbedingte Änderung
nach dem A-Eingriff. Die lineare Antwort misst entsprechend einen retardierten
Kommutator, nicht bloß eine Zweipunktkorrelation. Lieb-Robinson-Abschätzungen
können anschließend die Ausbreitung in einem bereits lokal gekoppelten
Modell begrenzen; sie erzeugen diese Lokalität oder drei Raumdimensionen
nicht von selbst. Siehe die Primärarbeit von
[Bravyi, Hastings und Verstraete](https://arxiv.org/abs/quant-ph/0603121).

Ein weiterer exakter Befund verhindert ein zu starkes Paritäts-No-go:
Der native Graph der 480 Fermionpaare verbindet alle 64 Moden. Eine
Vorzeichenumkehr auf einer Fermionteilmenge, bei unveränderten Bosonen,
erhält jede Kante genau dann, wenn sie trivial oder die globale Fermionparität
ist. Die binäre Inzidenzmatrix hat Rang 63. Zusätzliche unabhängige
Bankparitäten entstehen beim Kopieren von Banken; sie sind nicht als solche
ein Hindernis innerhalb der einen ursprünglichen Bank. Werden auch Bosonen
umgezeichnet, sind andere gemeinsame Gradierungen möglich.

## B4. Die einfachste fehlende Auswahl: Warum genau dieser Hamiltonoperator?

Die Z4-Idee besitzt einen präzisen Kern. Ein ganzzahliger, auf jedem Grad
konstanter Ladungslift mit neutralem Grad null müsste bei den entsprechenden
nichtverschwindenden Klammern erfüllen

\[
2q_1=q_2,\qquad q_1+q_3=0,\qquad 2q_3=q_2.
\]

Die Koeffizientenmatrix hat Determinante 4 und Rang drei. Über den ganzen
Zahlen bleibt nur q1=q2=q3=0; modulo vier gilt dagegen die gewohnte Belegung
1, 2, 3. Das verbietet nicht andere kontinuierliche Cartanladungen und beweist
nicht, dass der aktuelle Operator-Hamiltonian schon alle E8-Klammern realisiert.

Eine wörtliche Identifikation der Grad-eins-Labels mit primitiven CAR-
Vernichtern scheitert bereits an einem kleinen Beispiel: Die native
W-Spalte des Paares (0,1) ist null, aber
\([f_0,f_1]=2f_0f_1\ne0\). Die innere Lieklammer und die gewöhnliche
Operatoralgebra der Fermionfelder dürfen nicht gleichgesetzt werden.
Eine andere, zusammengesetzte E8-Realisierung wird dadurch nicht ausgeschlossen.

### B4.1 Zwei zusätzliche Terme am unveränderten Tensor

Der Bosonträger (10,6) besitzt eine symmetrische reelle invariante Paarung
eta. In der nativen Gewichtsbasis koppelt sie entgegengesetzte Spin-
Vektorgewichte und komplementäre Farbpaare. Es gilt eta Quadrat gleich eins.
Damit sind bereits

\[
B_+=\tfrac12\sum_{AB}b_A^\dagger\eta_{AB}b_B^\dagger,
\qquad
R_+=\sum_{AB}b_A^\dagger\eta_{AB}P_B^\dagger
\]

G-invariant. Bplus erzeugt zwei Bosonen, Rplus einen Boson und zwei Fermionen.
Beide ändern N um vier; beide erhalten N modulo vier. Die vollständige
Lie-Invarianz wurde an allen 45 plus 15 Generatoren überprüft, nicht nur
an den Cartanladungen. Rplus wirkt auf dem leeren Zustand nicht trivial:
Das Normquadrat beträgt exakt 480. Der quadratische Bosonpaarterm ist sogar
einfacher als der vorgeschlagene zusätzliche kubische Kanal.

Auf dem unveränderten Träger lautet die allgemeine G-invariante,
fermionparitätsgerade, normalgeordnete Hamiltonfamilie vom Grad höchstens drei

\[
H_{\rm ext}=c+\varepsilon N_f+\Delta N_b
+\kappa B_++\bar\kappa B_-
+g\sum_A b_A^\dagger P_A+\bar g\sum_A P_A^\dagger b_A
+\lambda R_++\bar\lambda R_-.
\]

Die Vollständigkeit gilt nur innerhalb dieser ausdrücklichen Polynomialklasse:
End(F) und End(B) haben jeweils einen Skalar, Sym hoch zwei von B einen
Skalar, und B tritt in Lambda hoch zwei von F genau einmal auf. Konkret
zerfällt letzterer Raum in (10,6), (126,6) und (120,10). Die SU(4)-Zentrumsregel
schließt die verbleibenden bosonisch-kubischen und gemischten
Besetzungs-Boson-Terme aus. Höhere Polynome, räumliche Kopien und neue
Feldträger sind damit nicht klassifiziert.

Für das native Modell hat das lineare System aller diagonalen Modenphasen
exakt neun unabhängige kontinuierliche Erhaltungen: die acht inneren Cartans
und N. Bei zusätzlichem nichtverschwindendem Rplus-Kanal oder Bosonpaar-Kanal
bleiben exakt acht. Die Ränge sind 115 beziehungsweise 116 auf 124 Moden;
explizite ganzzahlige Kerne und modulare Rangzertifikate beweisen sie.
Dies ist keine Behauptung, die volle nichtabelsche Gruppe schrumpfe auf acht
Dimensionen. Sie bleibt erhalten. Außerdem ist N modulo vier bereits die
Wirkung des SU(4)-Zentrums und keine neu hinzugewonnene unabhängige Symmetrie.

Für reelle Kopplungen und epsilon gleich null enthält die Fermiongleichung
nun zwei verschiedene Beiträge:

\[
[H_{\rm ext},f_r]=-gD_r-\lambda\widetilde\chi_r^\dagger,
\qquad D_r\sim bf^\dagger,\quad
\widetilde\chi_r^\dagger\sim b^\dagger\eta f^\dagger.
\]

Sie haben N-Ladungen -1 und +3. Eine Dynamik kann diese Kanäle bei bloßer
Z4-Erhaltung verbinden, ohne die Operatoren oder ihre Referenzzustände
fälschlich gleichzusetzen. **Zulässig ist aber noch nicht aus dem Compiler
abgeleitet.** Die Grundzustands- und Polschranken des unveränderten Modells
gelten für diese Erweiterung nicht ungeprüft weiter.

Auch ein mu-N-Term bleibt G- und Z4-invariant. Bereits der Zwei-Zustandsblock
aus leerem Zustand und einer normierten Quartetterzeugung im kleinen Modell
zeigt

\[
H+\mu N=\begin{pmatrix}0&\lambda\\\lambda&\Delta+4\mu\end{pmatrix}.
\]

Seine niedrigere Eigenenergie hängt von mu ab. Der Übergang zu Z4 allein
wählt also weder ein chemisches Potential noch einen eindeutigen physikalischen
Grundzustand aus. Für Delta größer als Betrag kappa ist die bosonische
Quadratik positiv; die linearen Bosonkopplungen an beschränkte Fermionoperatoren
lassen sich relativ dazu abschätzen. Das gibt eine untere Energieschranke,
aber noch keinen neuen eindeutigen Grundzustandssatz.

### B4.2 Eine weitere Vereinfachung: neue Dynamik oder andere Teilchenvariablen?

Manche scheinbaren Erweiterungen beschreiben nur andere Bosonvariablen.
Auf der reellen, phasengleichen Teilfamilie setze man

\[
b=c\cosh r+\eta c^\dagger\sinh r.
\]

Dies ist eine G-verträgliche kanonische Bogoliubov-Transformation. Sie ergibt

\[
\Delta'=\Delta\cosh2r+\kappa\sinh2r,\quad
\kappa'=\Delta\sinh2r+\kappa\cosh2r,
\]
\[
g'=g\cosh r+\lambda\sinh r,\quad
\lambda'=g\sinh r+\lambda\cosh r.
\]

Die additive Konstante ist 30 mal (Delta prime minus Delta). Bei g Quadrat
größer lambda Quadrat verschwinden kappa prime und lambda prime gemeinsam
genau dann, wenn

\[
\mathcal I=\kappa(g^2+\lambda^2)-2\Delta g\lambda=0.
\]

Beispiel: Delta=1, kappa=4/5, g=2, lambda=1 und tanh r=-1/2 ergeben
Delta prime=3/5, g prime=Wurzel 3, kappa prime=lambda prime=0.
Obwohl die alte Zahl N nicht erhalten ist, gibt es dann die verborgene
kontinuierliche Erhaltung Nf plus zweimal Nc. Daher wäre auch die Folgerung
„N ist gebrochen, also ist das Fundament nur Z4“ ohne Prüfung zu schnell.
Für I ungleich null ist nur diese uniforme kanonische Reduktion ausgeschlossen,
nicht jede denkbare nichtlineare verborgene Symmetrie.

Der sehr einfache reelle Quadraturansatz lambda=g bei kappa=0 ist dagegen
nicht durch eine endliche solche Transformation auf den nativen Ansatz
reduzierbar. Er ist ein prüfbarer Kandidat, kein hergeleitetes Naturgesetz.
Ein weiterer Herkunftstest ist besonders schlicht: Bei freiem
H0=epsilon Nf+Delta Nb haben die beiden kubischen Terme die Frequenzen
Delta minus 2 epsilon und Delta plus 2 epsilon. Am verwendeten epsilon=0
gibt es keine schnelle gegen langsame Frequenz, die das Weglassen des zweiten
Kanals durch eine Rotating-Wave-Näherung rechtfertigen würde. Ein exaktes
U(1)-Prinzip könnte das dennoch rechtfertigen; dieses Prinzip wäre dann
auszuweisen und abzuleiten.

## B5. Holografie und Schatten: die konkrete native Verbindung

### B5.1 Ein Kodierer ist bereits vorhanden

Der vorhandene, frisch geprüfte Tensor erfüllt WW dagger gleich 8 I60.
Daher ist

\[
V=W^\dagger/\sqrt8:\ \mathbb C^{60}\longrightarrow\Lambda^2\mathbb C^{64},
\qquad V^\dagger V=I_{60},\quad
\Pi=VV^\dagger=W^\dagger W/8
\]

eine exakte Isometrie mit einem Rang-60-Projektor Pi. Ein 60-dimensionaler
logischer Zustand kann verlustfrei als kohärente Überlagerung von
Fermionpaaren dargestellt werden. Die andere Richtung sieht aber nicht den
ganzen 2016-dimensionalen Paarraum: Ihr Kern hat Dimension 1956.
Diese „dunklen“ Richtungen sind nicht deshalb generell unphysikalisch;
sie sind für genau diese Abbildung unsichtbar.

Die beiden Ansichten sind durch W also bereits verbunden. Die native
N=2-Dynamik im hellen Paar-plus-Boson-Bereich ist sogar exakt

\[
H_{N=2,\mathrm{hell}}=
\begin{pmatrix}0&\sqrt8 g\\\sqrt8 g&\Delta\end{pmatrix}\otimes I_{60}.
\]

Sie wandelt die Kodierungsform um; am Prüfpunkt erreicht die entsprechende
Übergangswahrscheinlichkeit höchstens 2/27. Der nur in die Paarseite
eingebettete Code ist bei g ungleich null kein invarianter H-Unterraum.
Dieser kleine gemeinsame dynamische Träger ist ein positiver Befund. Er
ist N=2, nicht der native N=64-Grundzustand und nicht dessen geladener Pol.
Insbesondere ist er noch kein Transport durch physikalischen Raum.

### B5.2 Warum das noch kein holografischer Fehlerkorrekturcode ist

Für jeden der 64 Fermionmoden wurde die logische Kompression seiner
Besetzungsmessung berechnet:

\[
V^\dagger n_rV\quad\hbox{hat Spektrum}\quad
0\ (45\text{-fach}),\quad 1/8\ (15\text{-fach}).
\]

Das Resultat ist nicht skalar. Die Umgebung kann daher schon durch Ablesen
einer einzigen verlorenen Mode etwas über den logischen Zustand erfahren.
Die notwendige Fehlerkorrekturbedingung für die vollständige 60er-Codemenge
ist verletzt: Der Code korrigiert nicht die beliebige Löschung dieser einen
Mode. Fermionparität ändert dieses Besetzungsargument nicht, denn n_r ist gerade.
Kleinere geeignete Untercodes oder ein aus nativen Operationen erzeugtes
größeres Kodierungsnetz sind dadurch nicht ausgeschlossen, aber noch nicht
konstruiert. Bloßes Aneinanderhängen desselben Tensors garantiert keinen Code.

In etablierten holografischen Spielzeugmodellen sind isometrische Kodierung,
Rekonstruktion logischer Operationen aus verschiedenen Randteilen und
Fehlerkorrektur genau kontrollierte Eigenschaften. Das ist ein hilfreiches
Prüfschema, keine direkte Identifikation mit TFPT. Siehe
[Pastawski, Yoshida, Harlow und Preskill](https://arxiv.org/abs/1503.06237).
Die Rekonstruktion aus einem Teilrand ist auch in der AdS/CFT-Arbeit von
[Dong, Harlow und Wall](https://arxiv.org/abs/1601.05416) an konkrete
Quanteninformations- und geometrische Voraussetzungen gebunden.
Diese Voraussetzungen wurden für TFPT nicht nachgewiesen.

### B5.3 Was mehrere Schatten gemeinsam eindeutig machen können

Seien Ri festgelegte Mess- oder Reduktionsabbildungen eines gemeinsamen
Zustands rho. Für eine endliche, nicht eingeschränkte Zustandsklasse sind
alle Zustände aus den Schatten Ri(rho) genau dann unterscheidbar, wenn
auf den hermiteschen spurlosen Differenzen gilt

\[
\bigcap_i\ker R_i=\{0\}.
\]

Das ist das einfache gemeinsame-Kern-Kriterium. Anschaulich: Was eine
Ansicht nicht sieht, muss eine andere sehen. Zwei Qubitansichten auf (x,z)
und (y,z) genügen gemeinsam zur Bloch-Rekonstruktion, jede für sich nicht.
Zweimal dieselbe Ansicht auf (x,z) genügt weiterhin nicht. Das gilt ebenso
für zwei Theorieberichte, deren Übereinstimmung bereits aus denselben
eingesetzten Annahmen stammt: Sie liefern keine zweite unabhängige Messung.

Drei exakt nachgerechnete Grenzen sind wesentlich:

1. Die orthogonalen Zustände (000 plus 111)/Wurzel 2 und
   (000 minus 111)/Wurzel 2 haben dieselben reduzierten Zustände auf
   sämtlichen echten Teilmengen der drei Qubits. Eine gemeinsame
   phasensensitive XXX-Messung unterscheidet sie mit Erwartungswert +1 oder -1.
   Auch sehr viele lokale Schatten können also eine globale Phase übersehen.
2. Paarweise passende Überschneidungen garantieren nicht einmal einen
   gemeinsamen Ursprung. Drei binäre Variablen können nicht paarweise
   ausnahmslos verschieden sein. Jede einzelne perfekte Antikorrelation
   besitzt aber dieselben gleichverteilten Einzelmarginalen. Gemeint ist
   hier ein gemeinsames klassisches Tripel, nicht eine Behauptung gegen
   kontextuelle Quantenexperimente.
3. Selbst die vollständige Antwort einer Referenz bestimmt keinen völlig
   entkoppelten dunklen Zusatzsektor. H und H direkt plus K besitzen vom
   Startvektor (F,0) aus dieselben Energiemomente und dieselbe Zeitantwort.
   Ein exaktes kleines Matrixbeispiel prüft diesen Sachverhalt.

Das erreichbare Ziel ist daher zunächst der **kleinste gemeinsame
beobachtbare Prozess**, nicht ein aus endlichen Schatten bewiesener
einzigartiger ontologischer Innenraum. Zwei Historien gelten operational
als gleich, wenn alle verfügbaren künftigen Eingriffs- und Auslesefolgen
dieselben Wahrscheinlichkeiten liefern. Das ist eine eindeutige
Unterscheidungsregel für gegebenes Verhalten; sie garantiert weder eine
eindeutige Hilbertraumdarstellung noch von selbst eine einfache Geometrie.

### B5.4 Die drei Wände müssen unterschiedlich geprüft werden

| Gemeinte Wand | Was sie gegenwärtig bedeutet | Welcher Anschluss fehlt |
|---|---|---|
| Universalraum | Grenze zwischen gemeinsamem Operatorobjekt und seinen reduzierten Ansichten | Ein gemeinsamer verfügbarer Operationssatz, Zustand und Rekonstruktionsvertrag |
| TFPT | Grenze zwischen interner Compilerstruktur und physikalischer Realisierung | Herleitung der Ausführung, relativer Parameter und operationaler Teilung |
| Beobachtete Realität | Endlicher Zugang über Messungen, Präparationen und Korrelationen | Ein quantitatives, nicht nachträglich angepasstes Feld- und Messwörterbuch |

Diese Erkenntnisgrenzen sind nicht schon drei bewiesene physikalische
Holografieschirme. Ein kosmologischer Horizont, ein Code-Rand und eine offene
mathematische Beweispflicht sind verschiedene Dinge. Ebenso sind
Universalraum und TFPT Kandidatenbeschreibungen der Realität, nicht bereits
drei experimentell etablierte wechselwirkende Welten.

Eine stärkere holografische Deutung müsste eine einzige Kodierung mit
Zuständen, Operationen und Zeitentwicklung verbinden. Auf einem invarianten
Codesektor wäre etwa V dagger V=I und Hrand V=V Hin eine passende
Intertwining-Bedingung. Bei nichtinvarianten reduzierten Ansichten muss die
entstehende Erinnerung mitgeführt werden; autonome reduzierte Dynamik darf
nicht einfach vorausgesetzt werden. Zusätzlich braucht es eine Bedeutung
von Randteilen, kontrollierte Rekonstruktion und eine skalierende Geometrie.

## B6. Die einfachste neue Arbeitsrichtung und ihre Abnahmekriterien

Der plausible übersehene Punkt ist kein weiterer großer Tensor:
**Wir brauchen die gemeinsame Regel, die festlegt, welche Operationen,
Teilchenvariablen und Ansichten tatsächlich dieselbe Ausführung beschreiben.**
Noethers Symmetrieprüfung sagt, was erhalten bleibt. Die Schattenprüfung sagt,
was überhaupt unterscheidbar ist. Der Eingriffstest sagt, was etwas anderes
beeinflussen kann. Zusammen sind diese drei kleinen Fragen strenger und
informativer als weitere isolierte Zahlenübereinstimmungen.

1. **Den minimalen Ursprungsvertrag auswählen.** Den tatsächlichen Compiler
   auf den nativen kubischen Term, den zweiten kubischen Kanal und den
   quadratischen Paarterm prüfen. Die vollständige kleine Familie und der
   Bogoliubov-Test verhindern, dass derselbe Prozess mehrfach gezählt wird.
   Erfolg ist eine Ableitung oder ein präziser Ausschluss samt relativen
   Parametern, nicht nur die Feststellung erlaubter Symmetrie.
2. **Die Schattenkarte am vorhandenen W aufbauen.** Für denselben Vertrag
   Präparationen, Aufzeichnungen und kontrollierte Mehrzeitantworten in den
   verschiedenen Ansichten auflisten. Gemeinsam unsichtbare Richtungen und
   unverträgliche Überlappungen berechnen. Aus einem Teil der Daten eine
   Aussage bestimmen, die eine andere Ansicht ohne Nachjustierung testet.
   Der jetzt bewiesene Rang-60-Code und sein Einmoden-Leck sind Ausgangsdaten,
   kein Anlass, Raum oder perfekte Fehlerkorrektur bereits anzunehmen.
3. **Daraus einen gemeinsamen kausalen Teilträger gewinnen.** Eine verfügbare
   Operation muss die unbedingte Statistik eines anderen operational
   bestimmten Teils verändern. Derselbe Träger muss das relativistische
   Feldwörterbuch tragen. Erst dann sind Skalierung, chirales Maß und ein
   Spin-2-Sektor belastbare nächste Rechnungen.

Die lokale Lanczos-Fortsetzung bleibt als kontrolliertes Diagnoseinstrument
nützlich, steht aber nicht mehr an erster Stelle der fundamentalen Suche.
Die drei Schritte ersetzen keine einzelnen T1-T8-Nachweise. Auch eine
erfolgreiche endliche Kodierung würde RH, effiziente Faktorisierung oder
P-versus-NP nicht automatisch lösen.

Der RH-Absatz der Eingabe enthält keine neue vollständige arithmetische
Beweiskonstruktion. Das vorhandene Forschungsregister wurde begrenzt
abgeglichen; sein Aktualitätslauf scheitert derzeit an einer nicht verfügbaren
historischen Quelle beziehungsweise Quellen-/Review-Drift. Bestehende
endliche Determinantsonden sind ausdrücklich Diagnosemodelle. Es wurde
kein neuer RH-Beweis, kein umfassender RH-Neulauf und keine Erneuerung
der entsprechenden Vertrauensmarker behauptet.

**Bilanz:** Ein gemeinsamer Kodierungsbaustein ist schon da; außerdem sind
die minimalen symmetrieverträglichen Dynamiken und zwei wichtige
Verwechslungen jetzt wesentlich schärfer bestimmt. Die vollständige
universelle physikalische Lösung bleibt offen. Der nächste Schritt ist
kleiner und konkreter geworden: dieselbe Ausführung durch mehrere
kalibrierte, dynamisch konsistente Ansichten rekonstruieren und testen.

## B7. Abgleich des zuletzt eingesandten Berichts v1.6.3

Der sechste Text dieser Runde, „Operationssatz, nativer Grundzustand und
Feldwörterbuch“, enthält überwiegend bereits berücksichtigte Befunde:
die Kommutantenleiter, das Lochbild, die Normen der ersten Stufen, den
nichtverschwindenden Seitenzweig und den verschwindenden Weyl-Skalarkanal.
Seine zweite vorgeschlagene Folgeaufgabe wurde inzwischen wesentlich
weitergeführt: Alle vier Zwei-Boson-Singuletts sind konstruiert und der
richtige H-Lanczos-Anfang ist fünf Glieder weit bestimmt.

Vier Präzisierungen verhindern eine Übernahme veralteter Schlüsse:

1. **Sieben und sechzehn sind verschiedene Kommutanten.** Sieben gilt
   für volle innere Gruppe zusammen mit X und Nb; sechzehn für die Gruppe
   allein. Die drei hellen inneren Typen kommen auf beiden Seiten der
   Umwandlung vor. Einzelne Tabellenzeilen sind multiplizitätsfrei, der
   ganze N=3-Sektor aber nicht. Der Schluss vom nichtskalaren Clock auf
   eine äußere, nicht zusammenhängende Symmetrie ist weiterhin falsch.
2. **Eine kleine Zweignorm beweist keine globale Konvergenz.** Der
   genannte Defekt 2,90 mal 10 hoch -5 betrifft eine bestimmte Kontraktion.
   Die höhere Bosonstufe ist weiterhin gekoppelt. „Numerisch fast allein
   durch die Normen lösbar“ und „vernachlässigbar“ sind ohne Restschranke
   zu stark. Auch Zh plus Zadd gleich eins ist eine Summenregel, keine
   Bestimmung sämtlicher Spektrallinien. Ritz-Erwartungswerte bleiben
   Erwartungswerte des Ritz-Zustands, nicht automatisch von Omega.
3. **Der Feldschluss ist ansatzabhängig.** Der angegebene Fünfzyklus
   (16,45,0,30,37) wurde frisch am W überprüft. Damit ist eine einzige
   binäre Chiralitätsbelegung der primitiven Labels mit entgegengesetzter
   Händigkeit auf jeder Kante unmöglich. Das verbietet kein allgemeines
   Dirac-Wörterbuch mit erweiterten Trägern, Ableitungen oder zusammengesetzten
   Feldern. Der Tensorfeldkanal ist unter dem angegebenen engen Ansatz
   sinnvoll, nicht schon der universell einzige physikalische Feldtyp.
4. **Der gespeicherte Rechnerstand ist älter als der Text.** Die lokal
   zugehörige Datei `native_ground_state.json` hat einen anderen Checkerhash
   als das aktuelle Programm. Ihr gespeichertes w2-Normquadrat ist um
   229 Quadrat gegenüber der physikalischen Norm skaliert. Das aktuelle
   Programm enthält bereits die richtige Entskalierung; die alte Datei
   ist also kein aktueller Replaynachweis. Sie meldet außerdem
   `norms_by_traces_used=false` und Ritz-Tiefe drei. Die im Text erwähnte
   Datei `norms_by_traces.json` und das dortige Replaymanifest waren bei
   dieser Prüfung nicht vorhanden. Diese Beobachtung schließt ein
   Resultat an anderem Ort nicht aus, liefert hier aber keines.

Daher wird insbesondere die Behauptung, nu4 sei in dieser Quelle auf zwei
unabhängigen Wegen vollständig reproduziert, nicht übernommen. Der Text
selbst bezeichnet nu4 zugleich als „nur Spurnetzwerk“ und beschreibt den
Brute-Force-Abgleich nur bis nu3. Der frühere gepinnte exakte nu4-Eingang
unserer eigenen Rechnung bleibt davon getrennt und wurde nicht als neue
Enumeration ausgegeben. Ein fertig berechnetes nu5 wird aus dem vorhandenen
Programm mit `MAX_N=5` nicht abgeleitet; eine Einstellung ist kein Ergebnis.

**Die interessante verbleibende Richtung ist die Spurnetzwerk-Methode.**
Sie kann Normen durch Kontraktionen des vorhandenen Tensors berechnen,
statt alle Vielteilchenamplituden zu speichern. Zur fundamentalen
Vereinfachung wird sie erst dann, wenn sie auch gemischte H-Momente,
Seitenzweige und kontrollierte Mehrzeitantworten liefert. Der konkrete
nächste Test ist daher kein bloßer weiterer Normwert: Eine zweite kleine
Kontraktionsrechnung soll die schon exakt bekannten zehn H-Momente
reproduzieren und dann mindestens ein noch nicht bekanntes gemischtes
Matrixelement samt Fehlerkontrolle bestimmen. Diese Methode lässt sich
mit der Schattenkarte verbinden, ersetzt aber keine native Operation.

Das Prüfpaket bewahrt neben dem Text die beiden widersprechenden
Programmstempel und das vorhandene Spurnetzwerkprogramm. Diese fremden
Dateien wurden nicht verändert oder als vollständig neu ausgeführt ausgegeben.
