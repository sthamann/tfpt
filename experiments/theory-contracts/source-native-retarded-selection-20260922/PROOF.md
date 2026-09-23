# Native Zeitwirkung und der genaue fehlende Familienanteil

22. September 2026 · `UR.SOURCE.NATIVE_RETARDED_SELECTION.01` · **PARTIAL**

## Ergebnis und Entscheidungsfrage

Die entscheidende Frage dieser Fortsetzung lautet: Was liefert der bereits
vorhandene native W-Hamiltonoperator tatsächlich für den Strom- und
Familienanschluss, bevor eine zusätzliche Gross–Neveu-Dynamik angenommen wird?

Die vorhandene Paarwechselwirkung liefert eine exakt eliminierbare bosonische
Vermittlung mit zeitlicher Erinnerung. Ihre Stromdarstellung lässt sich auf
den ursprünglichen 64 komplexen Fermionmoden formulieren. Gleichzeitig bleibt
die normalisierte lineare Familienantwort im symmetrischen Quellenzustand
einheitlich. Daher genügt es für den vollständigen Flavor-Anschluss nicht,
eine Kopplungsstärke, einen Basiswechsel oder drei Feldamplituden zu wählen.
Die Quelle muss einen tatsächlich nichtskalaren dynamischen Familienanteil
liefern. Ein parallel erhaltener Yukawa-Operator auf dem vorhandenen
irreduziblen Familienlokalsystem kann diesen Anteil ebenfalls nicht liefern.

Das ist ein präziserer notwendiger Anschluss an die bestehenden
Yukawa-Ergebnisse. Die vollständige Ursprungsauswahl wird hier nicht gelöst.
Der native W-Hamiltonoperator ist ein bereits vorhandener Kandidat; seine
Herleitung aus dem ursprünglichen P1-Kern bleibt eine eigene Pflicht.

**Vorab festgelegte Entscheidung:** Ein Erfolg wäre eine native Stromwirkung
mit richtigem Zeitkern und ein zulässiger Weg zu nichtgleichen normierten
Familienantworten. Ein exaktes Symmetriehindernis beendet die Suche durch
bloße Parameter-/Basisoptimierung innerhalb dieser Kandidatenklasse.
Es wird kein neuer Hamiltonoperator als Ersatz eingeführt.

## 1. Gegebener nativer Operator; alte Befunde werden weiterverwendet

Die gepinnte Originalkonvention lautet

\[
H=\Delta N_b+\sum_{A=1}^{60}
\bigl(g b_A^\dagger P_A+\bar g P_A^\dagger b_A\bigr),\qquad
P_A=\sum_{i<j}W_{A,ij}f_jf_i,\quad \Delta>0.
\]

Es gibt 64 komplexe CAR-Moden in `(16,4)`, 60 CCR-Moden in `(10,6)`,
480 nichtverschwindende ganzzahlige W-Einträge und `WW†=8 I60`.
Die erhaltene Ladung ist `N_f+2N_b`. Das ist keine Realisierung durch
16 Vektor-Majoranas; interne Spin(10)-Spinoren und Raumzeitspinoren bleiben
verschiedene Begriffe.

Bereits am 15. September wurde auf allen 2016 Zweifermionzuständen bewiesen
und auf den vollen Fockraum fortgesetzt:

\[
\boxed{\sum_A P_A^\dagger P_A
=\frac{15N_f-C_D-C_F}{2}.}\tag{1}
\]

Dabei sind `C_D=Σ_{a=1}^{45}J_a²` und
`C_F=Σ_{a=46}^{60}J_a²`, mit `J_a=f†T_a f` und hermiteschen
Einteilchengeneratoren `T_a=i X_a/2` in der Original-Cliffordnormierung.
Auf dem Einteilchenraum gilt `Σ_a T_a²=15 I64`.
Entsprechend ist `Σ_a :J_a²:=C_D+C_F−15N_f`.

**(1), die native Symmetrie und die skalare Zweipunktantwort sind alte
Resultate.** Sie werden hier erneut am gepinnten W kontrolliert und für
den aktuellen Quellen-/Familienanschluss verwendet, nicht als neue
Entdeckungen ausgegeben.

## 2. Exakte Eliminierung der vorhandenen Bosonen

Betrachte zunächst die thermische Spur bei endlichem `β`, ohne neuen
Zustandsansatz. Ein kohärenter, normalgeordnet zeitdiskretisierter
Pfadintegral-Regulator für genau dieses H hat im Kontinuumsnotation

\[
S=\int_0^\beta d\tau\,[\bar f\partial_\tau f+
\bar b(\partial_\tau+\Delta)b+g\bar bP+\bar g\bar P b].
\]

Fermionen sind antiperiodisch, ihre Paare und die Bosonen periodisch.
Die bosonische Integration ist gaußsch; die fermionische Theorie wird
dadurch nicht gaußsch. Quadratische Ergänzung mit
`K=∂τ+Δ` liefert, bis auf den feldunabhängigen Bosonendeterminanten,

\[
\boxed{S_{\rm eff}[\bar f,f]=\int\bar f\partial_\tau f
-|g|^2\sum_A\int d\tau d\sigma\,
\bar P_A(\tau)D_\Delta(\tau-\sigma)P_A(\sigma).}\tag{2}
\]

Hier ist der Kern unabhängig vom gewünschten RR- oder Flavor-Ergebnis
durch den vorhandenen Bosonenterm bestimmt:

\[
D_\Delta(i\omega_n)=\frac1{\Delta-i\omega_n},\quad
\omega_n=2\pi n/\beta,\qquad
D_\Delta(t)=\frac{e^{-\Delta t}}{1-e^{-\beta\Delta}} (0<t<\beta),
\tag{3}
\]

periodisch fortgesetzt; Fourierkonvention `exp(−iωτ)`. Dies ist zunächst
ein euklidischer Matsubara-Kern. Eine retardierte Echtzeitantwort verlangt
zusätzlich eine angegebene analytische Fortsetzung und i0-Konvention.
Die Identität folgt zuerst aus der endlichen gaußschen Integration im
Regulator. Die übliche Trotter-Grenznotation in (2) ist keine eigenständige
Konstruktion einer vierdimensionalen Feldtheorie. Der endliche native
Hamiltonoperator ist bereits wohldefiniert und nach unten beschränkt.

Dies ist eine exakte Reduktion des gegebenen Modells, keine Näherung
zweiter Ordnung in g. Wiederholte Fermionwechselwirkungen bleiben in
`exp(−S_eff)` vollständig enthalten. Alle Fermionkorrelatoren sind damit
noch nicht ausgerechnet. Auch die vollständig wechselwirkende bosonische
Zweipunktfunktion ist nicht mit dem freien Eliminationskern (3) identisch.

Die allgemeine Methode ist etabliert, etwa Weber–Assaad–Hohenadler,
*Directed-Loop Quantum Monte Carlo Method for Retarded Interactions*,
[arXiv:1704.07913](https://arxiv.org/abs/1704.07913). Die konkrete
W-/Clifford-Identifikation stammt aus den lokalen TFPT-Quellen.

## 3. Die vollständige Stromform ist bilokal in der Zeit

Die quartische Koeffizientenidentität aus (1) gilt auch, wenn die beiden
konjugierten Grassmannfelder bei τ und die beiden nichtkonjugierten bei σ
stehen. Setze

\[
\mathcal J_a(\tau,\sigma)=\bar f(\tau)T_a f(\sigma).
\]

Dann gilt als normalgeordnetes Grassmannpolynom exakt

\[
\sum_A\bar P_A(\tau)P_A(\sigma)
=-\frac12\sum_{a=1}^{60}\mathcal J_a(\tau,\sigma)^2,
\]

also

\[
S_{\rm int}=\frac{|g|^2}{2}\sum_a\int d\tau d\sigma\,
D_\Delta(\tau-\sigma)\mathcal J_a(\tau,\sigma)^2.\tag{4}
\]

Dies ist die Stromumschreibung des vorhandenen Spinor-Paarprodukts.
`J_a(τ,σ)²` ist ausdrücklich nicht `J_a(τ,τ)J_a(σ,σ)` und auch keine
schon hergeleitete links-/rechtschirale Gross–Neveu-Kopplung.
Bei gleichen Zeiten müssen Operatorprodukte mit der in (1) angegebenen
Normalordnung und ihrem Einteilchenterm gelesen werden. Die kohärente
Zeitverschiebung des Regulators bleibt beim lokalen Grenzübergang erhalten;
die einseitigen Werte `D(0+)` und `D(0−)` dürfen nicht vertauscht werden.

Für langsame Paarquellen ist der führende lokale Term

\[
H_{\rm eff}^{(0)}=-\frac{|g|^2}{\Delta}\sum_A P_A^\dagger P_A
=\frac{|g|^2}{2\Delta}(C_D+C_F-15N_f).
\tag{5}
\]

Das attraktive Vorzeichen im nativen Paarkanal ist damit fest. Es ist
kein Beweis des Vorzeichens in einem anderen, erst zu identifizierenden
GN-Vektorkanal. Auch (5) ist kein exakt zeitlokaler Ersatz für (2).

Die richtige Bandkontrolle folgt direkt aus (3):

\[
\left|\Delta D_\Delta(i\omega)-1\right|
=\frac{|\omega|}{\sqrt{\Delta^2+\omega^2}}
\le\frac{\Omega}{\Delta}\quad(|\omega|\le\Omega).
\tag{6}
\]

Der Realteil ist `Δ/(Δ²+ω²)`, aber der Imaginärteil
`ω/(Δ²+ω²)` verschwindet im Allgemeinen nicht. Ihn wegzulassen würde
ohne weitere Austauschvoraussetzung eine fälschlich rein quadratische
Fehlerordnung ergeben. (6) kontrolliert den Kern als Fouriermultiplikator
auf einem deklarierten Frequenzband, nicht automatisch den Fehler aller
wechselwirkenden Observablen oder ein vorhandenes niedriges Energieband.

## 4. Weshalb die bestehende Quelle noch keine Familienhierarchie liefert

Der vorhandene Grundzustandsbeweis gilt für `0<|g|/Δ≤1/20`:
Der globale Grundzustand ist eindeutig und Spin(10)×SU(4)-invariant.
Für die eigentlichen f-Felder war deshalb bereits bekannt

\[
C_{ij}(t)=c(t)\delta_{ij},\qquad G_{ij}(z)=g_0(z)\delta_{ij}.
\tag{7}
\]

Hier kann C beispielsweise die positive Entnahmeantwort
`<Ω|f_i† exp[−t(H−E0)] f_j|Ω>` sein; die Transformationskonvention
wird für alle Indizes gleich gewählt. Schurs Lemma benutzt die
Irreduzibilität von `(16,4)`, die Invarianz von H und denselben Zustand.
Weder (7) noch c(t) müssen ein einzelner Exponentialpol sein.

Für jedes zeitunabhängige vollrangige Einbettungs-/Filterpaket
`L:C³→C64` und die entsprechenden drei linearen Felder folgt

\[
C_L(t)=c(t)L^\dagger L,\qquad G_L=C_L(0)>0,
\]
\[
\boxed{G_L^{-1/2}C_L(t)G_L^{-1/2}
=\frac{c(t)}{c(0)}I_3.}\tag{8}
\]

Die Amplituden können vor Normierung stark verschieden sein. Die
verallgemeinerten Eigenwerte des Paares `(C_L(t),G_L)` sind trotzdem
alle gleich. Es entstehen keine drei verschiedenen Energieskalen durch
dieselbe lineare Auslese. Das gilt auch für eine Einbettung in den
48-dimensionalen `16×3`-Teilträger und für beliebige konstante
Clock-/Flavor-Basiswechsel.

Es wird nicht behauptet, jeder physische Yukawa-Vertex sei ein solcher
Filter. Verschiedene Operator-Multiplizitätssektoren, ein tatsächlich
nichtinvarianter Zustand, dynamische Vertizes oder eine aus dem Ursprung
hergeleitete Änderung von H fallen nicht unter (8). Für weitere g-Werte
folgt (7) weiterhin für den invarianten Gibbszustand und dessen
invarianten Nulltemperaturgrenzwert; eine beliebige ausgewählte reine
Grundzustandsbranche wird außerhalb des bewiesenen Bereichs nicht
als invariant vorausgesetzt.

## 5. Direkter Anschluss an die vorhandenen Yukawa-Ergebnisse

Die bestehende Leptonformel liefert bereits

\[
r_\mu=\widehat m_\mu/\widehat m_\tau=\tfrac87\varphi_0,
\qquad r_e=\widehat m_e/\widehat m_\tau=\tfrac{96}{49}\varphi_0^3,
\quad \varphi_0=\tfrac1{6\pi}+\tfrac3{256\pi^4}.
\tag{9}
\]

Diese Formel wird nicht neu gefittet oder verworfen. Sie dient als
bereits vorhandenes Ziel des Quellenanschlusses. Für die dimensionslose
Singularwertmatrix `A=diag(r_e²,r_mu²,1)` ist

\[
\eta(A)=\frac{3\operatorname{tr}(A^2)}{(\operatorname{tr}A)^2}-1>0.
\tag{10}
\]

Für (9) ergibt sich `η=1.9780057604250806…`; bei einem skalaren A ist η=0.
(10) ist ein basisunabhängiger
Hierarchietest, kein Fertigstellungsprozentsatz. Die drei normalen
Feldamplituden in (8) als Massen zu deuten, würde genau diese notwendige
Unterscheidung übergehen. (9) wird hier nicht als native Polmessung
ausgegeben; der fehlende Schritt ist ihre dynamische Realisierung.

Auch die bereits vorhandene flache Familienverbindung gibt einen
scharfen Test. Ihre echten Punktumlaufmatrizen `M_k=U^k M U^(−k)`
erzeugen die irreduzible A4-Darstellung; U ist die separate Deckwirkung.
Ein paralleler Endomorphismus Φ auf diesem Rang-3-Lokalsystem kommutiert
mit sämtlichen Holonomien und ist daher skalar.

Stärker: Sei Y ein paralleler Yukawa-Homomorphismus zwischen zwei
unitären Familienlokalsystemen mit irreduziblem Rang-3-Eingangsraum.
Dann ist `Y†Y` ein paralleler Endomorphismus des Eingangsraums.
Also gilt `Y†Y=a I3`; bei a>0 sind alle drei Singularwerte gleich.
Unterschiedliche linke und rechte Basisrahmen beseitigen dieses Hindernis
nicht. Die zusätzliche Voraussetzung ist hier die Parallelität von Y,
nicht allein die Flachheit der beiden Verbindungen.

Für die gegebenen A4-Matrizen liefert das exakte Gruppentwirl zusätzlich

\[
\frac1{12}\sum_{h\in A_4}hAh^\dagger=\frac{\operatorname{tr}A}{3}I_3,
\quad
\frac1{12}\sum_h\|[A,h]\|_{\rm HS}^2
=2\left(\operatorname{tr}A^2-\frac{(\operatorname{tr}A)^2}{3}\right).
\tag{11}
\]

Damit ist die Abweichung vom parallelen Anschluss für jedes nichtgleiche
Yukawa-Singularwertpaket positiv, unabhängig von einer gemeinsamen
unitären Basiswahl. Dies ist ein Holonomie-Kompatibilitätstest, keine
Berechnung einer lokalen Gradientenenergie.

**Konkrete notwendige Schnittstelle:** Für den direkten gemeinsamen
Familienanschluss muss die ursprüngliche Quelle einen nichtparallelen
Yukawa-/Massenterm oder eine entsprechend begründete andere
Operator-/Zustandszuordnung erzeugen. Eine flache Verbindung kann einen
nichtparallelen kovarianten Endomorphismus tragen. Neue Berry-Krümmung
ist dafür nicht erforderlich. Die zuvor gefundene parallele
Determinantenrichtung `diag(b I3,−3b)` trennt höchstens Triplet und
Singulett; allein spaltet sie die drei Familien nicht auf.

Als kleinster Vorwärtstest dient direkt

\[
\mathcal A_F(t)=\widehat C_F(t)
-\frac{\operatorname{tr}\widehat C_F(t)}3 I_3,
\qquad \widehat C_F(t)=G_F^{-1/2}C_F(t)G_F^{-1/2}.
\tag{12}
\]

Für die Klasse (8) ist dies exakt null für alle t. Eine nichtverschwindende
Antwort muss aus den tatsächlichen Quelloperatoren folgen. Ihr bloßes
Vorhandensein wäre notwendig, noch nicht hinreichend für richtige
Yukawa-Werte, chirale Kopplungen und eine vierdimensionale Physik.

## 6. Die Originalvariation wählt diesen Anteil noch nicht aus

Der gezielte Audit der archivierten v4.5-Quellen liefert einen zusätzlichen
präzisen Befund. `02_carrier_source.tex:3020–3145` definiert die modulare
freie Energie nur auf den benannten Koordinaten
`ξ=(α,χ_geo,δ_ph,ρ_vac)` eines bereits festgelegten Zweigs. Einige
Koordinaten können funktionale Größen sein; es wird nicht pauschal eine
vierdimensionale endliche Variationsdomäne behauptet.

Die allgemeine Bordismusvariable B geht dort ausschließlich über
die Barriere `0 für B≅B_min, sonst +∞` ein. Die Gleichungen nach ξ
liefern somit keine unabhängige Klassifikation oder Variation der
ganzen Kragenoperatorfaser. Eine vollständige zugelassene Variation
`B(s)` müsste erst konstruiert und dann mit
`d M(B(s),ξ*)/ds|0=0` geprüft werden. Positive zweite Variation auf
dem Quotienten durch unitäre Richtungen wäre unter passenden
Regularitäts-/Koerzivitätsbedingungen eine mögliche lokale
Eindeutigkeitsstrategie, keine notwendige Bedingung und kein globaler
Eindeutigkeitsbeweis für sich allein.

Außerdem fordert das Axiom der physischen Operationalität in
`01_boundary_kernel_source.tex:622–625` nur `S_phys∈Seed_op`.
Das Minimalitätskorollar davor ist ausdrücklich konditional.
Zu unterscheiden sind daher die Existenz eines minimalen Defektvektors,
die Eindeutigkeit seiner Faser und die physische Auswahl dieser Faser.
Diese Pflichten bilden ohne Zusatzannahmen keine Implikationskette.
Die Bemerkung in `04_qft_source.tex:2103–2107` bestätigt, dass die
archivierte Schlusskette von einem minimalen Seed ausgeht.

Eine zusätzliche Begründung vollständiger Kernwahl und ihrer
Generatoridentifikation bleibt nötig, soweit sie nicht bereits in einem
wirklichen vollständigen Seed-Auswahlsatz enthalten wäre. Der aktuelle
TFPT-Ledger wird dadurch nicht nachträglich als vollständig gelöst oder
generell widerlegt eingestuft. Der Audit betrifft genau den genannten
archivierten Abschlussbeweis.

## 7. Entscheidung für die weitere Arbeit

Die vorhandene native Wechselwirkung braucht für ihre Stromdarstellung
keinen zusätzlichen elementaren GN-Skalar. Der Zeitkern ist im bestehenden
Modell nun explizit (2)–(4). Ein Parameter- oder genetischer Suchlauf über
g, Δ und konstante Familienfilter kann die Identität (8) jedoch nicht
überwinden, solange Zustand und Symmetrieannahmen gelten.

Der nächste begründete Herkunftsschritt ist daher die aus P1/P2/Clocks
abgeleitete geladene Operator-Variation, die einen nichtskalaren Anteil
in (12) erzeugt und zugleich mit der bereits vorhandenen parabolischen
Yukawa-Struktur (9) verträglich ist. Eine frei eingesetzte Diagonalmatrix
mit den Zielmassen wäre keine Lösung dieser Aufgabe. Falls im ursprünglichen
Seed keine solche Variation oder Auswahlregel definiert ist, muss genau
diese Regel vervollständigt werden; die nachgelagerte Optimierung der
symmetrischen Quelle kann sie nicht ersetzen.

## Belege, Prüfung und Grenzen

- `universalraum-native-operations-ground-response-20260915/common.py`:
  gepinnte native Operatoren, 60 Intertwiner und volle Casimiridentität.
- `universalraum-native-ground-response-20260915/RESULTS.md`, Abschnitte
  3–5: bereits bewiesener Grundzustandsbereich und skalare native Antwort.
- `tfpt_2_standard_model.tex:140–152,313–326`: Masterformel und
  Leptonverhältnisse. Keine Verwendung der Sektorzeilen u/d/e als
  drei Komponenten einer fiktiven Familienendomorphismusmatrix.
- `source-three-route-closure-20260922/FAMILY.md` und `family_checker.py`:
  tatsächlich verwendete A4-Holonomien und separate Deckwirkung.
- Die drei oben genannten archivierten Quellpassagen: tatsächlicher
  Variationsbereich und Geltungsbereich der Minimalitätsaussage.
- `checker.py`, `certificate.json`, `certificate_optimized.json`:
  gepinnte algebraische Kontrollen. Das allgemeine Schur-, Homomorphismus-
  und Integrationsargument steht im Text; endliche Prüfwerte ersetzen es nicht.

Firewall: `experiments/`; keine Paper-, Ledger- oder Scorecard-Promotion,
kein neu geschlossenes physisches T1–T8-Gate, keine vollständige TFPT-Lösung.
