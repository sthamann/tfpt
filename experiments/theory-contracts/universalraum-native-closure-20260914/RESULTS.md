# TFPT und Universalraum: ausführbare Quelle, Symmetriereduktion und kritische Dynamik

14. September 2026, Forschungsrevision 1.5. Fortsetzung des vollständigen Hauptbuchs v1.4.

## Gesamturteil in einfach

Wir haben mehrere Teile der kleinen mathematischen Maschine tatsächlich weiter gelöst.
Der Aufzeichnungsbaustein braucht weniger Spezialsteuerung; die große endliche
Spektralrechnung lässt sich stärker durch Symmetrie verkleinern; und für eine
ausdrücklich gewählte Kette kann man den Übergang zu beweglichen, masselosen
Anregungen vollständig ausrechnen. Auch ein unmittelbar auftauchendes Problem
dieser Kette, ihre exponentielle Farbentartung, lässt sich symmetrisch reparieren.

**Die vollständige vereinheitlichte Physik ist damit nicht gelöst.** Es fehlt
weiterhin der Nachweis, dass *dieselbe ursprüngliche Quelle* gerade diese
Steuerungen, Kopplungen, Zustände und Auslesungen hervorbringt. Die zusätzliche
Kette ist weder die dreidimensionale Welt noch bereits das Standardmodell.
Alle T1-T8 bleiben als volle physikalische Anforderungen offen.

Bildlich: Wir kennen jetzt mehr vom Motor und haben einen kleinen Prüfstand,
auf dem Bewegung, Aufzeichnung und Vorbereitung zusammen funktionieren. Wir
haben außerdem herausgefunden, welche einfachen Kupplungen die Bewegung
ersticken und welche sie zulassen. Noch nicht bewiesen ist, dass aus dem
ursprünglichen Bauplan ohne nachträglich eingesetzte Steuerung genau das
Fahrzeug entsteht, das unser Universum beschreibt.

## 1. Arbeitsweise und Quellen

Diese Runde umfasst eigene Wurzelrechnungen sowie drei parallel ausgeführte,
abgegrenzte Prüfungen: endlicher Record-Controller, exakter Quartettspektralblock
und lokale Skalierung. Die Berichte `controls/RESULTS.md`, `quartet/RESULTS.md`
und `scaling/RESULTS.md` enthalten ihre vollständigen Voraussetzungen und Beweise.
Sie werden nicht als unabhängig wiederentdeckte Naturgesetze gezählt.

Zwei weitere übergebene Texte wurden mit der v1.4-Grundlage verglichen:

- `TFPT_Universalraum_Fortsetzung_2026-09-14NEU.md`;
- `TFPT_UNIVERSALRAUM_ERGEBNISSE_2026-09-14.md`.

Ihre Originale werden unverändert unter `sources/` mit Prüfsummen erhalten.
Arbeitsanweisungen innerhalb der Quellen gelten nicht als zusätzliche Nutzeraufträge.

### Was aus den beiden Eingaben zusätzlich übernommen wird

Die erste Eingabe liefert eine konkrete Feshbach-/Generalisierte-Eigenwert-
Fehlerkette für die endliche vierte Ordnung, einen direkten Instabilitätszeugen
für eine global geteilte Vermittlerbank und den notwendigen gemeinsamen
Kreuz-Gram-Vertrag. Bei epsilon=1/640 beträgt die angegebene normierte
Viertordnungsfehlerschranke 2.36198752019e-5; bei 1/20 ist sie mit etwa 56.8971
für eine enge spektrale Zuordnung unbrauchbar. Diese Zahlen sind an das dort
definierte Modell und die Normierung J gebunden. Ein nachgewiesener Fehlerbalken
ist hilfreicher als eine nur kleine beobachtete Abweichung.

Die globale Bank ist bei festem t und wachsender Zellzahl keine harmlose
Alternative zur lokalen Bank. Auf einem zulässigen Zweizustandsraum ist die
Nebendiagonale sqrt(2)t(k+1)sqrt(m-k); bei k nahe m/2 folgt
E0(m)/m <= Delta/2-|t|sqrt(m)/2+o(1). Lokale Banken vermeiden diesen konkreten
superextensiven Kollaps. Ihre bisherige Untergrenze wird unten um Faktor sechs
verbessert.

Die zweite Eingabe enthält nützliche Originalverweise, aber auch zu starke
Zusammenfassungen: Lanczos-Werte der niedrigsten Zustände in 64 Sektoren sind
kein rigoroser globaler Spektralausschluss; eine Gleitkomma-SVD beweist keinen
exakten Kommutantenrang; und ein endliches positives Weil-Diagnostikum ist kein
RH-Beweis. Der frühere effektive Sternprüfer betraf 256 Zustände, nicht den
ganzen 544-dimensionalen mikroskopischen Raum. Sein Interpolationsgrad ist sechs,
nicht sieben. Die vorhandenen Originalresultate werden deshalb nicht pauschal
als exakte Schließung übernommen.

## 2. Der lokale Record braucht keine Resonanzumschaltung

Der gemeinsame Record ist

\[
R=P_+\otimes I+P_-\otimes X,\qquad P_\pm=(I\pm S)/2.
\]

Unter festem Delta>0, t/Delta=1/20, adressiertem t-an/aus und kohärentem
Belegungszugriff Q konstruiert `controls/RESULTS.md` einen exakten Volltransfer
aus zwölf positiven Hamiltonpulsen und elf diskreten Belegungs-Z-Kicks.
Ein wiederverwendbarer Pointer im Zustand |-> verwandelt Q in diese Z-Kicks.

Die positive Rückfolge ist nicht einfach das Inverse. Sie hinterlässt eine
berechnete Sektorphase gamma=12 pi(1-Delta/omega). Zwei Off-Warteintervalle
korrigieren diese Phase auf dem ganzen 44-dimensionalen Raum. Ergebnis:

\[
VAQUA=R\oplus I_{12}.
\]

Die geplante Evolutionszeit vereinfacht sich zu 24 pi hbar/Delta. Endliche
Q-Zeiten sind ebenfalls behandelbar, wenn ihr zusätzlich deklarierter Generator
die Vermittlerbelegung erhält: Jedes Q-Fenster wird bei t=0 auf eine volle
Detuningperiode ergänzt. Bei Q-Dauer hbar/Delta ergeben die 23 Q-Fenster
zusammen mit den Evolutionspulsen **70 pi hbar/Delta**. Das gesamte 88D-Modell
mit Helper ist numerisch geprüft, zusätzlich zum analytischen Phasenbeweis.

Es verschwinden somit zwei zuvor verlangte Ressourcen: Delta->0 und negative
Zeitentwicklung. Nicht verschwunden sind Q selbst, die nichtstabilisierende
Wedge-Kopplung, adressiertes Schalten, genaue Zeiten und physische Präparation.
Der endliche Q-Generator ist konstruiert, aber nicht aus TFPT abgeleitet.

### Dieselbe Ausführung liefert Präparation und Mehrzeitantwort

Das wiederholte Sternfilter K=P^-03 P^-02 P^-01 verwendet genau diese Records.
Es benötigt keinen kontrollierten Hamiltonoperator und keinen 13-Faktor-
Spektralfilter, wenn kontrollierte Näherungspräparation akzeptiert wird.
Bei zwanzig Runden beträgt die ideale Präparationsinfidelität
1.2233966909e-17. Der frische bedingte Rückkehrwert ist
0.5312499999780164, nahe 17/32. Die erhaltene Registervariante nähert sich 1.

Früher Abbruch bezahlt die tatsächliche Ausbeute: im Mittel rund 24 Versuche,
aber nur 102.7916667 Recordmakros bis zur erfolgreichen Vorbereitung. Mit Echo,
Schlussfilter und endlichen Q-Zeiten liegt die mittlere Zeitobergrenze bei
36239.58 hbar/Delta. Reset, Messung, Schaltflanken und übrige Steuerung kommen
hinzu. Das sind ideale Rechenergebnisse, keine Hardwarefidelitäten.

## 3. Der Record ist auch ein kohärenter Rechenbaustein

Diese eigene Rechnung verbindet Aufzeichnung und Logik ohne neue Interpretation
der Recordmatrix. Ein Hadamard H auf dem Pointer liefert exakt

\[
(I\otimes H)R(I\otimes H)
=I\otimes|0\rangle\langle0|+S\otimes|1\rangle\langle1|.
\]

Der Pointer kontrolliert also einen Ququart-Swap. Kodiert man ein Qubit in den
Farben 0 und 2, während das zweite Farbbit null bleibt, ist dies ein Fredkin-Gatter.
Mit sauberem Hilfsbit r=0 setze A=CNOT(r->b) Fredkin(a;b,r). Dann realisiert

\[
A^\dagger\,\mathrm{CNOT}(r\to c)\,A
\]

genau Toffoli(a,b->c) und gibt r=0 zurück. Die vollständige Wahrheitstabelle und
ein kohärenter Vierzweigzustand sind geprüft. Verbrauch: zwei Records, vier
Pointer-Hadamards, drei zusätzliche CNOT und ein sauberes Arbeitsbit.

**Grenze:** Hadamardzugriff, CNOT, Routing und saubere Hilfsbits sind zusätzliche
Zugriffe. Ein realisierbares Toffoli ist eine Verbindung zu bekannter universeller
Quantenrechnung, nicht bereits ein neuer Faktorisierungsalgorithmus oder ein
P-vs-NP-Beweis. Die allgemeine Universalität von Toffoli plus Hadamard ist bekannt.
[Primärquelle](https://arxiv.org/abs/quant-ph/0301040)

## 4. Autonome Zeit lässt sich konstruieren - ihr Spektrum wählt das Programm nicht

Für ein vorgegebenes endliches Programm U0,...,U(T-1) sei
V0=I, V(t+1)=Ut Vt und W=sum_t |t><t| tensor Vt. Der übliche Pfad-
History-Hamiltonoperator erfüllt exakt

\[
W^\dagger H_{\rm hist}(U)W=L_{\rm Pfad}\otimes I.
\]

Alle Programmwörter haben damit dasselbe Spektrum
2-2 cos(pi k/(T+1)), jeweils mit der Datendimension als Multiplizität.
Die Eigenvektoren und festgehaltene Zwischenzeit-Auslesungen unterscheiden sie;
das Spektrum allein tut es nicht. Auf einem Ring bleibt nur die Gesamtholonomie
als Eichinvariante. Zwei explizite Ringprogramme mit gleicher Holonomie und
unterschiedlichen Zwischenaufzeichnungen sind geprüft.

**Positive Konstruktion:** Setzt man statt des Laplaceoperators die statischen
gewichteten Hoppings sqrt((t+1)(T-t)) Ut, überträgt die Uhr bei Zeit pi hbar/2
den Anfangszustand exakt zum letzten Clockort und führt dabei das gesamte
Programm bis auf die bekannte Phase (-i)^T aus. Dies folgt aus der Darstellung
als 2Jx eines Spins T/2. Ganze Operatorblöcke sind für T=1,...,8 nachgerechnet.
Das ist eine konkrete autonome endliche Ausführung, nicht bloß ein Konzeptbild.

Die wachsenden Gewichte sind nicht kostenlos. Bei fester maximaler Kopplung J
ist die Zeit pi hbar max_t sqrt((t+1)(T-t))/(2J), mindestens pi hbar T/(4J).
Auch die datenabhängigen Clockkopplungen müssen tatsächlich implementiert werden.
Das Programm ist hier in H eingeschrieben, nicht aus einer primitiven Regel
ausgewählt. Ein schönes Clock-Spektrum kann diese fehlende Auswahl nicht ersetzen.
Allgemeine solche Clockkonstruktionen sind bekannt; der Beitrag hier ist ihr
konkreter Anschluss und ihre Grenze für den vorliegenden Quellenanspruch.
[Primärquelle](https://arxiv.org/abs/1712.07395)

## 5. Eine konkrete versteckte Symmetrie verkleinert die Rechnung

Die 24024-dimensionale C16-Singulettdarstellung reduziert sich unter
G=2^4:S5 auf 18 Multiplizitätsblöcke, der größte 262-dimensional. Der relevante
Standardblock ist explizit als 80x80-Operator konstruiert. Die rationale
Projektorform P_T(P_S4-P_S5) isoliert eine Kopie des vierdimensionalen
Standardfaktors je Multiplizität. Charakterrechnung, voller modularer
Intertwiner und rationaler Rekonstruktionsbeweis schließen hier zusammen.

Das ganzzahlige Grad-80-Polynom von X=sum_e S_e wurde mit 17 Primmoduli unter
bewiesener Koeffizientengrenze eindeutig rekonstruiert und mit einer weiteren
Primzahl geprüft. Seine 80 Nullstellen sind einfach. Rationale Wurzelzählung:

\[
11.561762122<E_{\min,\rm std}<11.561762123,
\]

die nächste Blockenergie liegt zwischen 13.2464863 und 13.2464864. Die vierfache
Standardmultiplizität ist innerhalb dieses Isotypieblocks jetzt exakt gesichert.
Ob dieser Block die globalen ersten Anregungen aller Sektoren liefert, ist damit
noch nicht bewiesen.

Eine zusätzliche Tableau-Transposition J erfüllt J^2=I und JXJ=-X. Alle 1920
Graphautomorphismen sind gerade und besitzen explizit einen ungeraden
zentralisierenden Permutationsoperator. Damit ist tr(J rho(g))=0 für alle g,
und alle G-Multiplizitätsblöcke zerfallen in gleich große J+- und J--Hälften.
Aus dem 80er Problem wird ein 40er Singularwertproblem; das größte entsprechende
quadrierte Singulettproblem hat nur **131x131** Dimensionen.

Das ist eine tatsächliche symmetrische Vereinfachung. Sie beweist keine physische
Chiralität: E->40-E gilt für den führenden H0, nicht unverändert für den
Viertordnungsterm F4. Auch die übrigen SU(4)-Sektoren und die mikroskopische
Restkontrolle werden dadurch nicht automatisch geschlossen.

## 6. Von Zellen zu Dynamik: hohe und niedrige Skala trennen

Die gemeinsame Farbkanalidentität sum_A K†e,A Ke,A=2P^-e verbessert für C16 die
Untergrenze von -1920 m t²/Delta auf **-320 m t²/Delta** bei zelllokalen Banken;
eigene Vermittler pro Kante erlauben -80 m t²/Delta. Mit Transportmatrix
h>=delta_b I gilt dieselbe Aussage mit delta_b statt Delta.

Für h=Delta I-eta A, maximalem Graphgrad D und q=|eta|D/Delta<1 ist der
statische inverse Vermittlerkern über Wege entwickelbar. Nach Weglänge R gilt

\[
\|W-W_R\|\le Cm\frac{t^2}{\Delta}\frac{q^{R+1}}{1-q}.
\]

Dies ist eine größenuniforme statische Kontrolle pro Zelle, kein bereits
bewiesener dynamischer Feshbach- oder Streusatz.

### Das einfachste positive Verkleben reicht nicht

Für identische Zellen mit eindeutigem Grundzustand und Gap g gilt für alle
Größen und kappa>=0 exakt

\[
\operatorname{gap}\left[\sum_c(h_c-e_0)+\kappa\sum_{cd}(I-S_{cd})\right]=g.
\]

Der untere Wert folgt aus Positivität, der obere aus einer gleichförmigen
Einanregung. Ganze positive Zell-Swaps liefern also Bewegung, schließen aber
die Masse aus dem Produktvakuum nicht. Diese Route zur masselosen Physik ist
unter ihren Voraussetzungen ausgeschlossen.

### Ein anderer, ausdrücklich gewählter Transfer wird auf der inneren Skala kritisch

Ein selektiver Transfer Tcd zwischen leerer und angeregter Zelle besitzt auf
einem D-regulären Graphen den exakten Vakuumgap g-kappa D, solange kappa D<g.
Für den tatsächlich exakt bekannten 544D-Viersite-Stern ist bei t/Delta=0.05
g=0.00243396875137 Delta. Das ist nicht der unbekannte globale C16-Gap.

Auf einer offenen einkomponentigen Kette ist die ganze Vielteilchenlösung durch
Jordan-Wigner gegeben: am Vakuumrand kappa=g/2 quadratische Dispersion, darüber
ein gefüllter Zustand mit linearen Ferminahzweigen. Bei kappa=g ist kF=pi/3 und
vF=sqrt(3)g. **Niedrige Anregungen können kritisch werden, während die hohen
Vermittler massiv bleiben.** Man muss die Skala Delta nicht künstlich schließen.

### Das neu auftauchende Entartungsproblem ist teilweise vollständig reparierbar

Mit allen 30 ersten Sternfarben hat eine offene Kette ohne Farbaustausch 30^N
gleiche Farbsektoren. Der positive besetzte Austausch
J sum_x Nx N(x+1)(I-S(x,x+1)) reduziert den Grundraum bei festem N und
J,kappa>0 exakt auf Sym^N(C^30), Dimension binomial(N+29,29).
Die extensive Restentropie verschwindet ohne willkürliche Farbwahl, und die
Ladungsgrundenergie bleibt unverändert.

Diese Reparatur ist nicht das Ende der Physikaufgabe. Ein orthogonaler
Farb-Spinwellen-Testzustand beweist gap_N<=2J(1-cos(pi/N))=O(N^-2).
Neben linearen Ladungsmoden bleibt also ein quadratischer oder weicherer
Farbsektor. Ein gemeinsamer Lorentzkegel oder drei Familien sind nicht abgeleitet.
Die genaue Zweizellenidentität in `scaling/RESULTS.md` zeigt, welche Transfer-,
Dichte-, chemischen und Austauschkoeffizienten der Compiler gemeinsam bestimmen muss.

## 7. Half-Charge: eine minimale bedingte Ergänzung mit Energiekontrolle

Eine separate einfache Referenzkonstruktion macht den fehlenden Zugriff genauer.
Auf l2(Z) tensor l2(Z) tragen die Zustände |k,l> die Ladungen k/2 und l/2.
Der Operator J|k,l>=|k+1,l-1> ist unitär, hat Norm eins und besitzt das explizite
Adjungierte mit umgekehrten Verschiebungen. Er erhält die Gesamtladung, kippt
aber die einzelne Systemparität (-1)^k.

Für H0=(k²+l²)/4 gilt punktweise

\[
2E(k,l)+1-E(k+1,l-1)=((k-1)^2+(l+1)^2)/4\ge0.
\]

Damit bildet J den Energiedomänenraum D(H0) in sich ab und erfüllt
||H0 J psi||<=||(2H0+I)psi||. Auch das Adjungierte ist kontrolliert.
Endliche abgeschnittene Prüfräume werden ausdrücklich nur als partielle
Verschiebungen geprüft, nicht fälschlich als endliche Unitaritäten.

**Entscheidende Grenze:** Eine Algebra, deren verfügbare Operationen getrennt
mit System- und Referenzparität kommutieren, kann J nicht erzeugen. Die
Konstruktion benötigt eine neue ungerade-System-mal-ungerade-Referenz-Kopplung.
Sie zeigt einen minimalen möglichen Ladungstransfer, konstruiert aber weder
das renormierte lokale Half-Charge-Feld der TFPT-Quelle noch seine E8-Netzgrenze.
Der Referenztrick darf die fehlende Ressource nicht unsichtbar auslagern.

## 8. Reset: die ausgeschiedene Information braucht einen Ort

Eine universelle unitäre Löschrealisierung, die d orthogonale Eingaben auf
denselben reinen Systemzustand zurücksetzt, muss d orthogonale Umweltzustände
erzeugen. Das folgt unmittelbar aus Skalarprodukterhaltung. Für m unabhängige
d-dimensionale Eingaben und finale Infidelität höchstens delta je System folgt

\[
\log_2\dim E\ge m[\log_2d-h_2(\delta)-\delta\log_2(d-1)].
\]

Beweis: Starte die Eingaben unabhängig maximal gemischt und die Umwelt rein.
Die Gesamtentropie bleibt m log2 d. Jeder nahezu reine Systemausgang hat
Entropie höchstens h2(delta)+delta log2(d-1); Subadditivität zwingt den Rest in
die Umwelt. Alle Speicher, Messgeräte und sonstigen Entropiesenken sind in E
einzuschließen. Für d=256, delta=1e-6 sind dies mindestens
7.99997063138 Bits pro unabhängiger Eingabe.

Das ist keine Behauptung über jede Wiederholung desselben bekannten Zustands,
keine Kostenformel für bloß bedingte erfolgreiche Versuche und keine Wärmegleichung.
Die unbedingte Wiederverwendung einschließlich Fehlversuchen braucht aber einen
expliziten Speicher-/Entropievertrag. Ein geschlossenes System vergisst nicht
durch bloße Umbenennung seiner Freiheitsgrade.
[Primärquelle zum thermodynamischen Kontext](https://arxiv.org/abs/1306.4352)

## 9. Kosmologie: eine vermeintlich kleine Korrektur kann das Matching nicht retten

Für die dokumentierte TFPT-Massenregel M²/Mp²=c3^7, c3=1/(8pi), und das vollständige
Starobinsky-Potential V=(3/4)M²(1-exp(-sqrt(2/3)phi))² setze y=exp(sqrt(2/3)phi)>1.
In erster Potential-Slow-Roll-Ordnung, aber **ohne** große-N-Abschneidung, gilt exakt

\[
A_s(1-n_s)^2=\frac{M^2}{6\pi^2}(1+1/y)^2
>\frac{M^2}{6\pi^2}.
\]

Die konkrete ACT-Tabellenspalte P-ACT-LB2 hat ln(10^10 As)=3.062 und ns=0.9752.
Ihre zentrale Kombination erreicht nur **0.4929956404** der strikten Untergrenze.
Das volle Potential korrigiert den großen-N-Ausdruck also in die falsche Richtung,
um die Abweichung zu reparieren.

| Festgehaltener Wert | Daraus errechneter anderer Wert |
|---|---|
| As=2.137025496e-9 | ns=0.9642233954; N_SR=53.8113746; r=0.0036466904 |
| ns=0.9752 | As=4.413594581e-9, etwa 2.0653 mal der betrachtete Zentralwert |

Das ist ein algebraischer Widerspruch für gleichzeitiges **Zentralwert-Matching
dieser festgelegten Näherungsbranche**. Es ist keine gemeinsame Likelihood,
keine berechnete Ausschlusssignifikanz und kein Ausschluss aller TFPT-Varianten.
Höhere Slow-Roll-Ordnungen, tatsächliche Modenentwicklung, Reheating und eine
physisch abgeleitete Änderung von Potential oder Matching müssen gesondert
untersucht werden. Eine nachträglich frei gewählte neue Massenkonstante wäre
kein parameterfreier Erfolg.
[ACT-Primärquelle, Version 2, Tabelle 5](https://arxiv.org/abs/2503.14452v2)

## 10. Gemeinsamer Stand T1-T8 und der anderen Fronten

| Front | Diese Runde tatsächlich erreicht | Vollständiger fehlender Nachweis |
|---|---|---|
| T1, tatsächliche Erzeugung/Algebra | Fester-Delta-Record, bezahlte endliche Q-Fenster, Anschluss an kohärente Logik | Wedge-, Q-, An/aus- und Controllerherkunft aus derselben primitiven Quelle |
| T2, geladene Seam | Expliziter norm- und energiekontrollierter relativer Half-Charge-Adapter; native Paritätsgrenze klar | Renormiertes lokales Half-Charge-Feld der wirklichen Quelle, Adjungiertenkontrolle und E8-/Clock-Zuordnung |
| T3, gemeinsamer Raumzeitträger | Ganze skalierende Referenzfamilien; exakte Gaps; linearer gefüllter Kettensektor | Native Geometrie und Zustandswahl, drei Raumdimensionen, gemeinsamer Lorentzgrenzwert |
| T4, chirale Materie | Alle Farbsektoren gerechnet, extensive Entartung symmetrisch entfernt; zusätzliche weiche Mode nachgewiesen | Chirales 3+1D-Maß, Spiegelentkopplung, Familien- und Eichdarstellungen derselben Quelle |
| T5, Dynamik/Skalierung | Stärkere lokale Untergrenze und statischer Reichweitenrest; vollständige Ketten-Vielteilchenlösung | Uniforme dynamische Reduktion der tatsächlichen Quelle, wechselwirkende 4D-Grenze und Streuung |
| T6, physikalisches Matching | Vollpotential-Slow-Roll-Identität, die einen vorgeschlagenen Reparaturweg ausschließt | Gemeinsames Quellenmatching aller Observablen mit Unsicherheiten und physischer Skalensetzung |
| T7, Gravitation | Gapped positive Swaproute ausgeschlossen; kritische innere Route konkretisiert | Dynamischer masseloser Spin-2-Pol und universelle Kopplung auf demselben 3+1D-Träger |
| T8, Zustand/Ausführung | Präparation, Record und Mehrzeitantwort gemeinsam; Controllerzeit und Resetkapazität explizit | Quellenseitige Auswahl von Zustand, Programm, Umwelt, Auslesung und kosmologischem Zustand |

RH bleibt ohne Identifikation des tatsächlichen signierten Weil-Objekts und
uniforme Positivität offen. Ein positives Clock-Spektrum identifiziert dieses
Objekt nicht; der neue Eichsatz zeigt die Unterbestimmtheit sogar konstruktiv.
Faktorisierung bleibt von einer nativen effizienten kohärenten Realisierung
mit Bitkosten und messbarer Ausbeute abhängig. Ein Quanten-Gatteranschluss
beweist weder klassische Polynomialzeit-Faktorisierung noch P=NP. Für Hylæan
ist keine neue End-to-End-Fähigkeit getestet; nur das gemeinsame Prozess- und
Reset-Prüfschema ist methodisch übertragbar.

## 11. Verifikation und Grenzen dieser Runde

Eigene Root-Prüfer: 72+32=104 Bedingungen, normal/-OO byteidentisch, sechs
absichtlich falsche Varianten erkannt. Kontrollfront: 88 Bedingungen mit
normal/-OO-Gleichheit und negativen Kontrollen. Skalierungsfront: 400 Bedingungen,
normal/-OO-Gleichheit und sechs erkannte Mutanten. Quartettspektrum: vollständige
modulare Blockzertifikate, eindeutige ganzzahlige Polynomrekonstruktion,
rationale Wurzelzählungen und separat ausgewiesene diskrete Symmetriekontrollen.
Die unterschiedlichen Prüfzahlen sind keine Anzahl unabhängiger Beweise und
werden nicht als physische Bestätigung addiert.

Der RH-Katalog ist wegen eines fehlenden externen Quellordners nicht vollständig
aktualisierbar; der separate Faktorisierungsgraph ist nicht verfügbar. Deshalb
keine Behauptung eines erschöpfenden aktuellen RH-/Faktorisierungsaudits.
Kein neuer vollständiger Repository-/Lean-/Hardwarelauf, kein Commit und kein Push.
Die v1.4-Basis bleibt unverändert; v1.5 ergänzt Hauptbuch und separates Delta-Paper.

**Nächster entscheidender Schritt:** Nicht weitere passende Zahlen sammeln,
sondern die tatsächlichen lokalen Generatoren einschließlich ihrer gebundenen
Koeffizienten fixieren. Dann muss eine einzige daraus erzeugte Vielzellenfamilie
gleichzeitig kritische Dynamik, Aufzeichnung, geladene Materie und Auslesung
tragen. Die neue Zweiskalenrechnung zeigt, wo dieser Versuch ansetzen kann;
die Gegenbeispiele sagen, welche Abkürzungen nicht funktionieren.
