# Sechs-Quellen-Audit: von der U-Idee zu einem geprüften lokalen Vertrag

Stand: 14. September 2026. NON-RH. Forschungsnachtrag, keine physikalische Promotion.
Alle T1–T8 bleiben offen. Die sechs eingesandten Texte sind Quellen, keine Anweisungen.
Die zusammenhängende Einordnung steht in [der Konsolidierung](../../../docs/TFPT_UNIVERSALRAUM_SECHS_QUELLEN_KONSOLIDIERUNG_2026-09-14.md).

## 1. Provenienz und Prüfklassen

`sources/` enthält die sechs Originaltexte bytegleich. `source_manifest.json` hält
Originalpfade und SHA256 fest. Widersprechende Quellen werden nicht still umgeschrieben.
`check.py` importiert drei hashgebundene lokale Hilfsdateien; der ältere Adapter prüft
seinerseits die tatsächlichen Gauß-E8-Quellprojektoren. Die neuen Registerrechnungen
verwenden den in den Texten behaupteten kanonischen lokalen Keilkanal. Sie ersetzen
keinen vollständigen phasentreuen E8-Focklift.

`verification.json` trennt exakte endliche Bedingungen von numerischen Spektraltests.
Die Kategorie `exact` umfasst auch Integritätsprüfungen, nicht nur mathematische Sätze.
Die allgemeinen Aussagen unten beruhen auf ausgeschriebenen Beweisen, nicht auf der
Anzahl grüner Checks. Importierte Helper-Prüfungen werden separat gezählt.

## 2. Neuer Hauptbefund: Eine zu genaue History ändert die Wechselwirkung

### 2.1 Der angegebene Kanal

Für a<b sei der lokale Kanal K durch

\[
K|ab\rangle=|a\wedge b\rangle,\quad
K|ba\rangle=-|a\wedge b\rangle,\quad K|aa\rangle=0
\]

festgelegt. Auf C4 ⊗ C4 gilt exakt

\[
K^\dagger K=I-S=2P_-,\quad KK^\dagger=2I_6.
\]

Der Q-Audit Teil II §2 und Fable §5.2 ergänzen jedoch den Ausgang um ein
orthogonales History-Label `(s,t,a,b,mu)`. Bei wörtlicher geordneter Speicherung
unterscheiden sich damit die History-Zustände zu ab und ba. Der neue Kanal ist

\[
\widetilde K|ab\rangle=|a\wedge b\rangle|ab\rangle_h,
\quad
\widetilde K|ba\rangle=-|a\wedge b\rangle|ba\rangle_h.
\]

Mit D = Σ_a |aa><aa| folgt stattdessen

\[
\widetilde K^\dagger\widetilde K=I-D,\qquad
\operatorname{rank}\widetilde K=12\ne6.
\]

Der Vektor |ab>+|ba> ist unter K dunkel, unter dem neuen Kanal nicht.
Außerdem kommutiert I-D nicht mit der kollektiven SU(4)-Wirkung. Die Speicherung
einer bevorzugten geordneten Farbbasis verändert also nicht nur eine Erzählung,
sondern den Operator und seine Symmetrie.

Bei gemeinsamer Zwischenenergie Δ liefert die zweite Ordnung jetzt
-t²(I-D)/Δ. Bis auf eine Konstante ist dies eine Bestrafung gleicher Farben,
nicht der SU(4)-Austausch. Auf dem vollständigen Vierergraphen besitzt Σ D_ij
genau 4! = 24 Nullzustände: jede Anordnung aller vier verschiedenen Farben.
Ω liegt darin, ist aber nicht mehr ausgezeichnet. Auch P_ker(Ktilde)=D gibt
diesen anderen Elternoperator.

**Reichweite:** Das widerlegt diese konkrete geordnete History-Ausführung mit
der behaupteten unveränderten Elimination. Es ist kein Verbot unitärer
History-Modelle. Eine kohärente spätere History-Manipulation, andere
Zwischenenergien oder ein nichtorthogonales Label wären andere Verträge.

### 2.2 Notwendige und hinreichende lokale Reparatur

Für normierte Records h_ab gilt allgemein

\[
\langle ab|K_h^\dagger K_h|ba\rangle
=-\langle h_{ab}|h_{ba}\rangle.
\]

Der ursprüngliche Gramoperator bleibt in der gewählten Phasenkonvention genau
dann erhalten, wenn h_ab=h_ba für jedes a≠b. Verschiedene Kanten können dagegen
durch orthogonale Lochmuster oder Kantenrecords unterschieden bleiben:

\[
\langle h_{e,ab}|h_{f,cd}\rangle=0\ (e\ne f),\qquad
h_{e,ab}=h_{e,ba}.
\]

Damit verschwinden die unerwünschten Kreuzterme **zwischen Kanten**, während
die gewünschte Interferenz **innerhalb einer Kante** bestehen bleibt.
Das ist ein präziser lokaler Kompatibilitätsvertrag, keine hergeleitete
kosmologische Auswahl. Auch die in K bereits gleichen-Farben-Nullrichtungen
brauchen für eine unitäre Gesamtausführung einen erhaltenen Ausgang.

### 2.3 Eine berechenbare Kontinuität zwischen beiden Fällen

Setze für vertauschte Farben den reellen Record-Überlapp 0≤η≤1; andere
ungeordnete Farbpaare besitzen schon orthogonale Vermittlerlabels. Dann

\[
G_\eta=I-\eta S-(1-\eta)D.
\]

Dies ist ein positiver Gramoperator: jeder nichttriviale Zweierblock hat
Eigenwerte 1±η. Für vier Träger kann die verschobene effektive Energie als

\[
\overline H_\eta=2\eta H_{\rm tet}/J+(1-\eta)D_{\rm coll},
\quad D_{\rm coll}=\sum_{i<j}D_{ij}
\]

geschrieben werden. Zur Elimination gilt
-Σ G_eta,ij = Hbar_eta - 6(1+η)I.
Für 0<η≤1 ist Ω der eindeutige Grundzustand und die Lücke von Hbar beträgt
**exakt 4η**. In physikalischen Eliminationseinheiten ist das 4ηt²/Δ.

Beweis: M=2Htet/J hat Kernel CΩ und M≥4(I-PΩ). D_coll ist positiv und
annihiliert Ω. Also Hbar_eta≥4η(I-PΩ). Die Schranke wird von v=A_0Ω erreicht,
etwa A=diag(1,-1,1,-1). v ist orthogonal zu Ω und enthält nur vier verschiedene
Farben, also D_coll v=0. Aus S_ij Ω=-Ω und Σ_i A_i Ω=Tr(A)Ω=0 folgt
Mv=Σ_{j≠0}(A_0-A_j)Ω=4v. Bei η=0 wird der Kernel 24-dimensional; die positive
Lücke oberhalb dieses ganzen degenerierten Grundraums ist dann 1, während die
Aufspaltung zwischen den niedrigsten beiden Zuständen null ist.

Damit wird die Kohärenz der Aufzeichnung selbst zu einer exakt prüfbaren
Voraussetzung der Zellselektion. Für η≠1 ist die volle kollektive SU(4)-Symmetrie
dieses Farbrecord-Modells im Allgemeinen gebrochen.

Diese Interpolation benutzt ausdrücklich die effektive Gramenergie -K†K.
Die andere Regel P_ker(K_eta) liefert bei jedem η<1 im Paarraum D, weil der
Rang bereits dann 12 ist. Sie darf nicht mit dieser kontinuierlichen
Energieinterpolation verwechselt werden.

## 3. Eine vollständig unitäre lokale Reparatur — aber weiterhin nicht eindeutig

Setze W=K/√2 und P=P_+=(I+S)/2. Auf dem 22-dimensionalen Ladungs-zwei-Raum
(C4⊗C4) ⊕ C6 definiere

\[
U_\theta=\begin{pmatrix}e^{i\theta}P&W^\dagger\\W&0\end{pmatrix}.
\]

W†W=I-P, WW†=I und WP=0 beweisen Uθ†Uθ=I für **jedes** θ.
Diese Ausführung erhält auch den ursprünglichen Kernel, statt ihn bei der
Paarannihilation zu verlieren. Sie ist mit der kollektiven SU(4)-Wirkung
verträglich. Die 22 Dimensionen sind minimal für eine unitäre Erweiterung
auf dem beibehaltenen 16-dimensionalen Paarraum plus sechs orthogonalen
Vermittlerzuständen; dies ist keine absolute Universalraum-Minimalität.

Die Freiheit ist beobachtbar. Mit einem anfänglichen |01> ohne Vermittler
liefern θ=0 und θ=π/2 dieselbe erste **blockdephasierte** Ausgabe, also dieselbe
Auslesung von Paar- und Vermittlersektor ohne deren relative Kohärenz.
Bei kohärentem Behalten und erneutem Anwenden derselben jeweiligen Regel gilt:

\[
U_0^2|01\rangle=|01\rangle,\qquad
U_{\pi/2}^2|01\rangle=-|10\rangle.
\]

Die Rückkehrzustände sind orthogonal. Gleiche lokale Klammer, gleiche
Raumdimension, Unitarität, SU(4)-Kovarianz und gleicher Ein-Schritt-Schatten
genügen somit nicht zur eindeutigen Mehrzeitphysik. Eine zusätzliche Bedingung
wie eine konkret begründete Involution, Generatorwahl oder Kernelphase wäre
nötig. Dieser Gegenbeleg behauptet nicht, dass jeder bereits vollständig
definierte alte TFPT-U-Schritt diese Freiheit besitzt.

Ein sparsamer zusätzlicher Auswahlvertrag ist „ohne Ereignis bleibt der
Zustand unverändert“: U|ker K=I. Bei festgehaltenen Blöcken W und W† erzwingt
Unitarität für einen allgemeinen Block [[A,W†],[W,D]] zunächst D=0 und
A†A=AA†=P. A ist damit eine unitäre Wirkung allein auf ker K. Unter
kollektiver SU(4)-Kovarianz ist Sym²(C4) irreduzibel; Schurs Lemma ergibt
A=e^{iθ}P. Die zusätzliche Identitätsforderung wählt θ=0. Das schließt
diese klar begrenzte lokale Auswahl, nicht die Herkunft des Zusatzprinzips,
die globale Ereignisreihenfolge oder das physikalische Zustandsfunktional.

## 4. Unique-dark ist kein Relaxationsbeweis

Eine weitere implizite Lücke betrifft Q-Audit Teil II §7. Wähle
L=I-PΩ als einzigen Lindblad-Sprungoperator und H=0. L besitzt genau einen
dunklen Vektorraum, CΩ. Trotzdem ist jeder Zustand im orthogonalen Komplement
stationär: für Lρ=ρL=ρ ist

\[
L\rho L^\dagger-\tfrac12\{L^\dagger L,\rho\}=0.
\]

|0000><0000| ist ein expliziter solcher Zustand. Er relaxiert nicht nach Ω.
Benötigt wird ein Satz über das **gesamte** stationäre Funktional und die
fehlenden invarianten Unterräume, nicht nur ein einzigartiger Nullvektor der
Sprungoperatoren. Ein ausgewiesenes Reservoir ist weiterhin nötig.

## 5. Zweizellenmodell: der allkopplige Satz trägt

Vorausgesetzt sind zwei vollständige gleichgewichtete K4-Tetramer und eine
einzige Brücke: H=H_A+H_B+λP^+_ab, J>0, λ≥0. Dies ist nicht C16.

Mit R²=16J²-2Jλ+λ² und Q²=4J²+λ² gelten

\[
E_0=(4J+\lambda-R)/2,\quad
E_1=3J+\lambda/2-Q/2,\quad E_1-E_0>J/2.
\]

Unabhängig geprüft wurden ganzzahlige Tensoridentitäten auf 65.536
Komponenten, die beiden invarianten Zweierblöcke und die rationale
adjungierte Kompression. Hinzu kommen vollständige numerische Spektren aller
15 zulässigen Youngformen an zehn Kopplungswerten; ihre mit SU(4)-Dimensionen
gewichtete Summe ist 4^8. Es wurde keine dichte 65.536²-Matrix gebaut.

Beweisprüfung des eingesandten Satzes:

1. Die lokalen Zellenergien sind 0,2J,3J,4J,6J. Unter 4J stehen global nur
   das Produktsingulett, Adjungierte bei 2J und die 20 bei 3J zur Verfügung.
2. Mit |0>=Ω_AΩ_B und |1>=(4S_ab-I)|0>/√15 ist der Singulettblock
   `[[5λ/8, √15λ/8],[√15λ/8,4J+3λ/8]]`. Sein niedrigster Wert ist E0;
   das orthogonale Singulettkomplement beginnt bei mindestens 4J.
3. Im adjungierten Sektor sei P die H0-Energie-2J-Projektion. H0≥4JI-2JP.
   Die Kompression PVP besitzt pro adjungierter Komponente die Werte
   1/2, fünf Achtel vierfach und 3/4. Sie ist exakt aus sechs
   A_iΩ-Richtungen einschließlich ihrer nichttrivialen Grammatrix berechnet.
4. Der Zwei-Projektionen-Block zum Eigenwert p von PVP hat unteren Wert
   `3J+λ/2 - sqrt(4J²+4Jλ(1-2p)+λ²)/2`. Da p≥1/2, liegt er ≥E1.
   Die Schranke wird auf den Zuständen (A_a-A_b)|0> und deren Swap erreicht;
   ihr tatsächlicher Block ist `[[2J+λ/2,λ/2],[λ/2,4J+λ/2]]`.
5. Alle anderen Darstellungen beginnen bei mindestens 3J, während E1<3J.
   Schließlich R²-(Q-J)²=11J²+2J(Q-λ)>0 und Q-J>0. Also R>Q-J und
   E1-E0>J/2. Positivität der Brücke und die invariant erreichte Untergrenze
   schließen weitere Grundzustandskonkurrenten aus.

Die frühere 8J-Grenze und unsere noch konservativere 16J/5-Grenze waren
Beweisgrenzen, keine Übergänge. Kein Schluss auf beliebig viele Zellen folgt.

## 6. Welche Einfachheit? Entropie hängt von der Auslesung ab

In der angegebenen inzidenzerhaltenden Familie Ka=aI+(1-a)(B-I)/6 besitzt
ein Eingang sieben mögliche **Kontexte** mit Gewichten a und sechsmal
(1-a)/6. Deren Entropie ist

\[
H_C(a)=-a\log a-(1-a)\log((1-a)/6).
\]

Sie ist strikt konkav und maximal bei a=1/7. Der tatsächliche Strahlenprozess
besitzt aber einen Selbstnachfolger und zwölf weitere Strahlen mit Gewichten
a und zwölfmal (1-a)/12. Seine Entropie

\[
H_R(a)=-a\log a-(1-a)\log((1-a)/12)
\]

ist maximal bei a=1/13. Der zugehörige Prozess hat Rang 60, nicht 30.
Beide Aussagen sind auf den tatsächlichen Quellprojektoren geprüft.

Auch minimale Ein-Schritt-Rangzahl wählt 1/7 nur **innerhalb dieser Familie**.
Lässt man symmetrieverträglich die acht nichtinzidenten Kontextnachfolger zu,
hat der ausschließlich nichtinzidente Prozess Rang 15. Uniformität über alle
15 Kontexte liefert Rang 16. Die bisherigen Annahmen des inzidenten Trägers
dürfen bei einer vermeintlich universellen Kompressionsauswahl nicht verschwinden.

Der passive Marginalquotient 45 linear / 44 normiert wurde separat bestätigt:
pro Pauli hat die Folge der Auslesezeilen den Rang zwei und schließt nach
einem zusätzlichen Zeitschritt. 15 Kontextspuren plus 30 Pauli-Zukunftsgrößen
ergeben 45. Das ist keine Minimalität für beliebige selektive Eingriffe.

## 7. Weitere verifizierte Anschlüsse und Korrekturen

- **Sternfilter:** Ganzzahliges Projektorpolynom, vollständiges 256-dimensionales
  Spektrum und alle acht Kontrollausgänge bestätigt. Der Erfolg am genannten
  χ0 beträgt 1/6. Gesteuerte Pulse und Register werden vorausgesetzt.
- **Clebsch:** Zwei neue Lanczos-Läufe im gesamten 24.024-dimensionalen
  Singulett-Multiplizitätsraum, k=14, ncv=64/128 und unterschiedliche Starts,
  finden vier orthogonale Zustände bei 11.561762122803J über
  11.045398337068J. Residuen und Orthogonalitätsfehler <10^-8. Dies widerlegt
  das Dublett, zertifiziert aber noch keine exakte maximale Multiplizität vier
  und ersetzt keinen neuen Lauf aller 64 C16-Darstellungen.
- **Vierte Ordnung:** Symmetrischer und antisymmetrischer 6⊗6-Zweig wurden
  symbolisch geprüft. Der gesamte Zweibondterm auf diesem Sektor ist in
  vierter Ordnung 4g^4 P_-/Δ³; nach Abzug der beiden Einzelbondkorrekturen
  bleibt -2g^4 S6/Δ³. Mit g=√2t ist das -8t^4 S6/Δ³. Das sind kompatible
  Subtraktionskonventionen desselben ausgewiesenen harmonischen Modells,
  nicht allein wegen verschiedener Schreibweise zwei verschiedene Modelle.
  Außerhalb des aktiven 6⊗6-Sektors ist eine Konstante dort nicht automatisch
  eine globale Konstante. Der volle C16-Clusteroperator bleibt ungeprüft.
- **Exakt versus führend:** j=(√(Δ²+4g²)-Δ)/2 ist im isolierten Kanal exakt;
  j=g²/Δ+O(g^4/Δ³)=2t²/Δ+O(t^4/Δ³), nicht exakt 2t²/Δ bei endlichem t.
  Das Verhältnis des verbundenen S6-Koeffizienten zu führendem J ist
  4(t/Δ)²: vier Prozent bei 0,1, ein Prozent bei 0,05.
- **E8-Typen:** 960 gleichgradige Wurzelsummen nach (10,6), dagegen
  640+192 gemischte Summen nach g0 plus 64 Cartanfälle erneut enumeriert.
  Der vorgeschlagene gemischte Kanal zum (10,6) am Ende der kurzen
  Konsolidierung ist ausgeschlossen. Eine korrigierte Koeffizientenrechnung
  würde außerdem den nativen T2-Halbladungsfeldvertrag noch nicht schließen.
- **Dimension:** Vier exakte periodische Überlagerungsverträge d=1,2,3,4
  besitzen dieselbe lokale Clebsch-Inzidenz. Die positive quadratische
  akustische Form folgt aus der Zyklusprojektion
  B^T[I-D(D^TD)^-1D^T]B/16 und ist rational geprüft. Dies ist ein
  Dimensions-Gegenmodell, kein Weyl- oder Raumzeitnachweis.
- **Spin(10):** Eine explizite CAR-Rechnung bestätigt [HU,T]P=U TP≠0 bei
  Gewichtsplatzmischung. Die Rolle „Gewicht = Ort“ kann nicht unverändert
  zugleich die Rolle einer ungebrochenen inneren Spin(10)-Symmetrie spielen.
- **Kommutante:** Die volle Kommutante eines einzelnen H enthält alle
  Spektralprojektoren und sämtliche Operationen innerhalb seiner entarteten
  Energieräume. Bereits beim Tetramer hat sie Dimension 23.076. Der Vorschlag,
  die volle C16-Kommutante als genau „SU(4)×W(D5)“ zu identifizieren, ist so
  nicht typgerecht. Sinnvoll sind lokalitäts- und quelltreue Automorphismen
  der gesamten Operatorfamilie oder gezielt dargestellte Lie-Generatoren.
- **Weylformel:** Für Σ_i v_i q_i σ_i ist det(ωI-Σ_i v_iq_iσ_i)
  =ω²-Σ_i v_i²q_i². Die in Q Teil II §9 geschriebene voll summierte Form
  v_i v_j q_i q_j enthält falsche Kreuzterme. Allgemein lautet der räumliche
  Ausdruck q^T V^T V q; dies allein wählt noch keinen gemeinsamen Kegel.
- **Alpha/Inflation:** Historischer Alpha-Wert hochpräzise erneut berechnet;
  die offizielle NIST-Tabelle bezeichnet sich weiter als CODATA 2022.
  Die As-Abweichung bei N=51,4 ist kein Ausschluss des ganzen N-Bereichs:
  N≈56,13124 trifft As=2,10·10^-9. Dann ist As Kalibrierung, keine unabhängige
  zusätzliche Vorhersage. Neue Massen- oder Protontransferrechnungen fehlen.

## 8. Reproduktion und ausdrücklich nicht geleistete Prüfungen

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 /opt/homebrew/bin/python3 -B experiments/theory-contracts/universalraum-six-source-audit-20260914/run_checks.py
```

Der Runner vergleicht Normal- und `-OO`-Ausgabe bytegenau, prüft unveränderten
Prüfercode während des Laufs und verlangt das Anschlagen fünf gezielt
veränderter Negativkontrollen. Nur eigene Ergebnisdateien werden geschrieben.
Die anfängliche allgemeine SymPy-Rangroutine war wegen großer
Zwischenzahlen zu langsam; sie wurde durch exakte DomainMatrix-Rangberechnung
über rationalen Zahlen ersetzt. Keine numerische Rangtoleranz wurde eingeführt.

Nicht erneut ausgeführt: die extern genannten vollständigen 2.511.496
Jacobi-Tripel, komplette Originalpakete der 20-Qubit-Präparation, sämtliche
57.600 Cocycle-Paare, das 90-seitige Buch als unabhängiger PDF-/Code-Neubau,
ein voller C16-Vierkörperoperator, alle C16-Irreps, eine native chirale
Grenzwertkonstruktion, 3+1D-Feldtheorie, neue Massen-/Protonläufe, Hardware,
RH-, Faktorisierungs- oder P-vs-NP-Beweise. Die genannten externen Ergebnisse
werden deshalb nicht pauschal als unabhängig verifiziert ausgegeben.

## 9. Primärliteratur: Methoden, keine externe TFPT-Bestätigung

- [Bravyi, DiVincenzo, Loss: Schrieffer-Wolff](https://arxiv.org/abs/1105.0675):
  effektive Hamiltonoperatoren, verbundene Cluster und kontrollierte Näherung.
- [Yarotsky: perturbierte klassische Gittersysteme](https://arxiv.org/abs/math-ph/0412040):
  Stabilität unter Voraussetzungen an kleine lokale Störungen. Keine hier
  ausgewertete universelle Schwelle für den gesamten TFPT-Kandidaten.
- [Dong, Lin: unitäre Vertexalgebren](https://arxiv.org/abs/1308.2361):
  Hintergrund der abstrakten Gittertheorie, nicht ihres nativen TFPT-Limes.
- [Pollock et al.: Mehrzeitprozesse](https://arxiv.org/abs/1801.09811):
  operationelle Unterscheidung von Gedächtnis und Ein-Schritt-Zuständen.
- [NIST: CODATA-2022-Tabelle](https://physics.nist.gov/cuu/Constants/Table/allascii.txt):
  datierte Messreferenz; keine Theorieunsicherheit für die TFPT-Formel.
