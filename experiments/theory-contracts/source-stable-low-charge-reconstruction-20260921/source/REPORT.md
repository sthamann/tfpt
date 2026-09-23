# Primitive Quellenereignisse: stärkstes Originalgesetz, exakte Kurzzeitentscheidung und fehlendes Objekt

Datum: 21. September 2026  
Auftrag: Prüfen, ob der bestehende TFPT-Korpus bereits ein **ursprüngliches**, vom nativen Ziel-Hamiltonoperator unabhängiges Gesetz enthält, das zugleich

1. die elementare (W)-Paarumwandlung gegenüber einer direkten Doppelumwandlung auswählt und
2. die fermionische und bosonische Kinetikmatrix festlegt.

Es wurde nur gelesen. Weder Repository, Ledger noch Theoriegraph wurden verändert; keine Vollsuite wurde ausgeführt. Der Theoriegraph war aktuell: 5946 Knoten, 64014 Kanten, 256 Contracts. Die vier Ausgangsverträge `primitive-transfer-selection-20260912`, `source-operator-origin-20260920`, `common-source-gauge-grade-transfer-20260920` und `source-mixed-response-reconstruction-20260921` bleiben `UNKNOWN/PARTIAL/PARTIAL/PARTIAL` in ihrem jeweiligen Graphstatus.

## Entscheidung

Im gezielt geprüften Originalbestand und unter den stärksten im Theoriegraphen ausgewiesenen Kandidaten findet sich **kein einzelnes vorhandenes Originalgesetz**, das die verlangten Größen unabhängig gemeinsam festlegt. Das ist ein Befund über diesen geprüften Bestand, keine erschöpfende Aussage über jede Datei oder jede künftig mögliche Quelle.

Der stärkste vorhandene Bestand zerfällt in zwei nicht verbundene Hälften:

- Der rohe reflexionspositive Naht-/DtN-Zweig besitzt einen positiven Transfer und eine freie Einteilchenstruktur. Er kann auf seinem eigenen Raum einen quadratischen Generator beziehungsweise eine Kandidaten-Kinetik liefern. Die kanonische Operatoridentität vom rohen Nahtkern zum physisch geladenen Feldraum ist jedoch genau `QGEO.KERNEL.01 [O]`; selbst der Feld-Level der Markov-/OS-Einbettung bleibt offen.
- Der affine (E_8)-Vakuumzweig plus 3+2-Markierung fixiert einen echten geordneten kubischen Koeffizienten (d_{ABC}\epsilon_{ijk}), einschließlich relativer Vorzeichen und Austauschtyp. Er liefert aber ausdrücklich keinen Hamiltonoperator, keine gemeinsame physische Zeit und keine kanonische CAR/CCR-Feldabbildung.

Diese Hälften dürfen nicht nachträglich miteinander multipliziert werden. Das wäre genau der bereits ausgeschlossene Zieloperator-Transport: ein roher Operator wird aus dem gewünschten Ziel zurückdefiniert und kann es dann tautologisch reproduzieren (`TRANS.TARGETOP.RAWSELECT.01`, `verification/graph_v2/transitions.json`, Z. 245–259).

Das stärkste **unabhängige Auswahlgesetz, das reichen würde**, ist daher kein zusätzliches Symmetrieaxiom, sondern der **erste Kurzzeit-Jet eines einzigen rohen, graduierten Quellentransfers auf demselben Feldraum**. Dieses Objekt ist unter den geprüften Originalkandidaten noch nicht konstruiert.

## 1. Was die Originalquellen tatsächlich festlegen

### 1.1 Roher Nahttransfer: quadratisch und auf seinem eigenen Raum

Im Ursprungsdokument wird der OS/Euclidische Vielteilchen-Hamiltonoperator als

\[
H_{\rm seam}=d\Gamma(-\log T)
\]

aus dem Recovery-Transfer (T) gebildet (`origin_theory.tex`, Z. 1829–1841). Das ist eine **zweite Quantisierung eines Einteilchenoperators**. Es fixiert unter der gesetzten Identifikation einen freien quadratischen Generator; es erzeugt weder den nativen (W)-Kubikterm noch entscheidet es dessen elementare Ereignisordnung.

Noch grundlegender ist die Operatoridentität selbst offen. `QGEO.KERNEL.01` verlangt

\[
C_\Sigma=U^{-1}C_{\mu_4}U
\]

als Operatorgleichheit und nicht nur als Spektrumsübereinstimmung (`verification/status_ledger.csv`, Zeile 257). Der aktuelle Text lokalisiert die offene Herkunft in der Auswahl der rohen Dynamik und der vier Marken (`origin_theory.tex`, Z. 1843–1862).

Der finite Markovvertrag macht die Trennung ausdrücklich: Für den dreizuständigen Kernel ist (Q=\log T) ein exakter klassischer Markovgenerator, aber die Einbettung auf Feld-/quasilokaler Algebraebene bleibt offen (`tfpt_research_contracts.tex`, Z. 12738–12760; Ledger-ID `DYN.MARKOV.EMBED.01`). Der Übergang zur physikalischen unitären Dynamik verlangt zusätzlich eine quasilokale Hamilton-Dilatation, Größenkonsistenz, Lieb–Robinson-Schranke und OS-Fortsetzung (`tfpt_research_contracts.tex`, Z. 12762–12775). Derselbe klassische Transfer besitzt bereits mehrere inequivalente Quantenlifts (`tfpt_research_contracts.tex`, Z. 12777–12810).

Damit ist der Nahttransfer der stärkste vorhandene Kandidat für eine ursprüngliche Kinetik, aber noch **kein gemeinsamer geladener Quellentransfer**.

### 1.2 Affines (E_8)-Vakuum: kubischer Tensor, aber keine Zeitderivation

Der Originalvertrag `compiler-vacuum-current-cubic-20260918` fügt ausdrücklich „no action, oscillator or Hamiltonian“ hinzu (`PROOF.txt`, Z. 19–24). Er beweist

\[
[J_m^a,J_n^b]=J_{m+n}^{[a,b]}+mk\,\kappa(a,b)\delta_{m+n,0}I
\]

und

\[
\langle\Omega|J_1^aJ_0^bJ_{-1}^c|\Omega\rangle
=\kappa(a,[b,c]).
\]

Im ((27,3))-Zweig folgt exakt

\[
C_{(A,i)(B,j)(C,k)}=d_{ABC}\epsilon_{ijk},
\]

mit Wardmatrixrang (44) auf (45) neutralen Kubikmonomen; die relativen Koeffizienten sind eindeutig (`compiler-vacuum-current-cubic-20260918/PROOF.txt`, Z. 66–100).

Die 3+2-Markierung (S) repariert den Austauschtyp:

\[
\{S,d_H\}=0,
\qquad
Y_{\rm mark}(h)=(Sd_H)\otimes A(h),
\qquad
Y_{\rm mark}^{T}=Y_{\rm mark}.
\]

Der zugehörige Audit sagt jedoch ebenso klar: (S) liefert keinen current-to-CAR- oder boson-to-fermion-Intertwiner; die physische Quelle hat noch nicht gezeigt, dass die geordnete Stromantwort als lokaler Fermionvertex mit (S) auf dem bezeichneten Bein ausgeführt wird (`common-source-gauge-grade-transfer-20260920/flavor/PROOF.txt`, Z. 50–80 und 127–137). Stromnullmoden und deren Polynome liefern diese physische Operation ebenfalls nicht (ebenda, Z. 278–298).

Der stärkste positive Schluss bleibt daher

\[
\text{affines Kubik + Markierung}
\Longrightarrow \text{(W)-artiger Koeffizientenkandidat},
\]

nicht aber

\[
\Pi_{\Psi\Psi}[B_A,H_{\rm src}]
=g\sum_{i<j}W_{Aij}\Psi_j\Psi_i.
\]

### 1.3 Lokale Maxwell-/Randkandidaten schließen die Lücke nicht

Der jüngste Maxwell-Contract besitzt eine konkrete lokale Rechnung, setzt aber bereits eine kompakte (U(1))-Verbindung, ihre Kopplung, gleiche Geschwindigkeiten, einen bosonisierten Feldraum und eine Zustands-/Renormierungswahl (`source-maxwell-field-transfer-20260921/PROOF.txt`, Z. 15–18 und 33–43). Seine Kopplung (e) bleibt innerhalb der Kandidatenklasse frei, und der gemeinsame Operator-/Zustands-/Zeitanschluss aus der ursprünglichen Quelle ist weiterhin offen (ebenda, Z. 204–247). Er ist daher keine unabhängige P1/P2-Herleitung der Kinetik oder der (W)-Ereignisordnung.

Der tatsächlich ursprüngliche mikroskopische Quellenkandidat ist weiterhin ein quadratischer QWZ-Hamiltonoperator. Gaussianische Elimination bleibt quadratisch und erzeugt keinen elementaren Vier- oder Zwölffermionterm (`source-dynamics-selection-20260920/PROOF.txt`, Z. 6–28). Nichtverschwindende zusammengesetzte Stromkumulanten ändern diese Aussage nicht.

### 1.4 Die einzige vorhandene „primitive Ereignisregel“ ist ausdrücklich eine Zusatzhypothese

`FOUR_PRIMITIVE_PROCESS.md` nimmt an, dass genau vier geerbte Cliffordgeneratoren unabhängige elementare Poisson-Sprünge sind, während Produkte nur sequenziell auftreten. Der Text sagt ausdrücklich, dass weder diese Poisson-Lesart noch die Stützbeschränkung aus den ursprünglichen physikalischen Prämissen folgt (`primitive-transfer-selection-20260912/FOUR_PRIMITIVE_PROCESS.md`, Z. 6–14 und 84–88).

Der vollständige Ratenraum-Audit zeigt zudem, dass Symmetrie, positiver Transfer, eindeutiger stationärer Zustand, Markov-Komposition, detailliertes Gleichgewicht und maximale Lücke die gemeinsamen Ereignisraten nicht auswählen. Benötigt wird eine **source-derived coupling support or a primitive event measure** (`COUPLING_RATE_POLYTOPE.md`, Z. 66–121). Das ist genau die hier wieder auftretende fehlende Struktur; sie ist kein bereits vorhandenes Originalgesetz.

## 2. Exakte Entscheidung durch Kurzzeit-Jets

Angenommen, eine Quelle liefert auf **einem** Hilbertraum einen stark stetigen Transfer

\[
T_{\rm src}(t)=e^{-t\widetilde H_{\rm src}},
\qquad
\widetilde H_{\rm src}=H_{\rm src}-E_*I\ge0,
\]

und aus derselben Darstellung stammen kanonische Projektoren auf die Boson-/Fermionzahlsektoren. Definiere

\[
K_1(t)=P_{1b,0f}\,T_{\rm src}(t)\,P_{0b,2f},
\qquad
K_2(t)=P_{2b,0f}\,T_{\rm src}(t)\,P_{0b,4f}.
\]

Da die Sektoren bei (t=0) orthogonal sind,

\[
K_1'(0)=-P_{1b,0f}\widetilde H_{\rm src}P_{0b,2f}
=-P_{1b,0f}H_{\rm src}P_{0b,2f}=-C,
\]

\[
K_2'(0)=-P_{2b,0f}\widetilde H_{\rm src}P_{0b,4f}
=-P_{2b,0f}H_{\rm src}P_{0b,4f}=-D.
\]

Hier ist (C) der **direkte elementare** Zweifermion-zu-Einboson-Block und (D) der **direkte elementare** Vierfermion-zu-Zweiboson-Block. Damit ist die gesuchte Unterscheidung quellenintern und basisfrei formuliert:

\[
\boxed{C=gW\ne0,\qquad D=0.}
\]

Falls (D=0), aber (C=gW), erscheint dieselbe Zweibosonrichtung erst in zweiter Ordnung:

\[
K_2''(0)=P_{2b,0f}\widetilde H_{\rm src}^{2}P_{0b,4f}
=g^2P_{2b,0f}X^2P_{0b,4f},
\]

sofern die Quelle keine weiteren zweistufigen Pfade zwischen diesen Sektoren besitzt. Dann ist der Taylor-Koeffizient zweiter Ordnung

\[
K_2(t)=\frac{g^2t^2}{2}P_{2b,0f}X^2P_{0b,4f}+O(t^3).
\]

Das ist exakt „zweimal dasselbe elementare Ereignis“. Für

\[
H_\eta=H_W+\eta(X^2+X^{\dagger2})
\]

gilt dagegen bereits

\[
K_2'(0)=-\eta P_{2b,0f}X^2P_{0b,4f}\ne0.
\]

Der Unterschied liegt somit nicht im erreichbaren Endzustand, im Tensor (W), in der Symmetrie oder in einer endlichen Zeitwahrscheinlichkeit. Er liegt in der **ersten Transferableitung**.

### Kinetik aus demselben ersten Jet

Sei (F) der vollbesetzte Fermionprüfzustand und (|i^h\rangle=f_iF) die Einlochbasis. Für

\[
H_{\rm kin}=\sum_{ij}f_i^\dagger h_{ij}f_j
\]

gilt

\[
\langle i^h|(H-E_F)|j^h\rangle=-h_{ji}.
\]

Nach Abzug der Sektorenergie (E_F) und mit

\[
K_h(t)_{ij}=\langle i^h|e^{-t(H-E_F)}|j^h\rangle
\]

folgt daher

\[
\boxed{K_h'(0)_{ij}=h_{ji}.}
\]

Analog bestimmt der erste Jet auf dem Einbosonraum nach Abzug der kanonischen Vakuumenergie (c) die bosonische Matrix (Omega), äquivalent zur unteren Antwort

\[
[[b_A,H],b_B^\dagger]=\Omega_{AB}I.
\]

Damit könnte **ein und dasselbe Quellenobjekt** alle verlangten Daten liefern:

\[
T_{\rm src}'(0)
\longrightarrow
\{h,\Omega,C,D\}.
\]

Diese Jets bestimmen zunächst nur die angezeigten Generatorblöcke. Eine Rekonstruktion des **vollständigen** Generators verlangt zusätzlich einen gemeinsamen dichten invarianten Kern, Selbstadjungiertheit beziehungsweise eindeutigen Abschluss, vollständige Sektorprojektoren und ein Quellenprinzip, das versteckte orthogonale Blöcke ausschließt oder bestimmt. Ohne diese globalen Voraussetzungen wäre selbst ein erfolgreicher Vier-Jet-Test noch keine vollständige Herleitung von (H_{\rm src}).

Gerade diese gemeinsame Herkunft fehlt bisher. Ein vollbesetzter Zustand allein sieht (h) nur über (operatorname{tr}h). Der Einloch-Jet ist ein nützlicher kleiner Rekonstruktionskanal; er ist nicht eindeutig oder logisch minimal, denn auch ein kanonisch definierter Einfermionblock kann (h) rekonstruieren. Entscheidend ist, dass der gewählte niedrige Sektor aus derselben Quelle stammt und die vollständige Matrix statt nur ihrer Spur bestimmt.

## 3. Warum Semigroup, Reflexionspositivität, Jacobi und abstrakte Lokalität (D=0) nicht erzwingen

### 3.1 Semigroup und zeitliche Reflexionspositivität

Für jedes nach unten beschränkte (H_\eta) setze

\[
E_*(\eta)=\inf\operatorname{spec}H_\eta,
\qquad
T_\eta(t)=e^{-t(H_\eta-E_*(\eta))}.
\]

Dann ist (T_\eta(t)) eine positive selbstadjungierte Kontraktionshalbgruppe. Für beliebige (t_i\ge0) und Vektoren (psi_i) gilt

\[
\sum_{ij}\langle\psi_i,T_\eta(t_i+t_j)\psi_j\rangle
=\left\|\sum_iT_\eta(t_i)\psi_i\right\|^2\ge0.
\]

Dies ist die zeitliche Reflexions-Grampositivität. Sie gilt auch im bereits konstruierten stabilen Bereich (eta\ne0). Also können

\[
\text{untere Antworten + Stabilität + Semigroup + zeitliche RP}
\]

die direkte Doppelumwandlung nicht ausschließen.

Diese Aussage ist **kein** Gegenmodell zur vollständigen OS-Lokalität, zum rohen P1/P2-Nahtmaß oder zu allen TFPT-Bedingungen. Sie entscheidet nur die häufig versuchte Abkürzung über Semigroup und zeitliche RP. Der lokale symmetrische Semigroup-Befund des Korpus ist zudem an ein freies/quotientiertes endliches Modell gebunden; dessen Einzelschritt ist sogar nicht positiv, erst ein komprimierter Clockschritt ist positiv (`tfpt_research_contracts.tex`, Z. 12291–12322).

### 3.2 Graduierte Jacobiidentität

Die graduierte Jacobiidentität ordnet verschachtelte Kommutatoren. Sie setzt keinen zulässigen Koeffizienten auf null. Wird (X^2+X^{\dagger2}) in (H) eingesetzt, propagiert Jacobi dessen nichtverschwindenden (Q=4)-Block korrekt in die gemischte Antwort. Um daraus (D=0) zu folgern, müsste eine unabhängige Quellrelation bereits sagen, dass der entsprechende erste verbundene Jet verschwindet. Im Korpus existiert diese Relation nicht.

### 3.3 Lokalität

Strikte Lokalität könnte ein **globales** Quadrat (X^2=(\sum_xX_x)^2) wegen seiner weit getrennten Kreuzterme ausschließen. Sie verbietet aber nicht automatisch einen lokalen direkten Term

\[
\sum_x Y_x,
\qquad
Y_x:\;4f\rightarrow2b,
\]

oder einen endlichreichweitigen Nachbarterm. Deshalb folgt (D=0) erst aus dem konkreten lokalen Aktions-/Ereignisträger, nicht aus dem Wort „lokal“ allein. Der vorhandene Korpus warnt genau davor, Lokalität oder Unabhängigkeit nachträglich zur Auswahl eines günstigen Punktes zu benennen (`COUPLING_RATE_POLYTOPE.md`, Z. 117–126).

Die richtige scharfe Version lautet: **Der verbundene erste Quellenkumulant besitzt Stütze im (2f\leftrightarrow1b)-Kanal und keine Stütze im (4f\leftrightarrow2b)-Kanal.** Eine solche Aussage wäre ein echtes primitives Ereignisgesetz. Ein vollständiges quellenselektiertes (W[J]=\log Z[J]), aus dem diese verbundenen Jets folgen könnten, ist selbst als `FTRANSFER.GENERATING.01 [O]` registriert (`docs/OPEN_PROBLEMS.md`, Z. 173–190).

## 4. Das exakt fehlende Quellenobjekt

Benötigt wird nicht ein weiterer Ziel-Hamiltonoperator, sondern das Tupel

\[
\boxed{
(\mathcal H_{\rm src},\pi_{\rm src},\Omega_{\rm src},
T_{\rm src}(t),\{P_{n_b,n_f}\})
}
\]

mit folgenden unabhängig aus der Quelle gewonnenen Eigenschaften:

1. (pi_{\rm src}) ist eine gemeinsame graduierte Darstellung der kanonischen geraden (B_A) und ungeraden (Psi_i), mit einem Adjunkten, einer Ladungs-/Gradwirkung und ohne Zuschauerfaktor.
2. (T_{\rm src}(t)) ist der physische, stark stetige positive Transfer derselben Quelle; zunächst gilt (\widetilde H_{\rm src}=-T_{\rm src}'(0)) und damit (H_{\rm src}=-T_{\rm src}'(0)+E_*I). Weder Generator noch Energieursprung werden aus (H_W) zurückdefiniert.
3. Die Projektoren (P_{n_b,n_f}) stammen aus denselben Quellfeldern und sind mit Zustand, Domäne und Zeit verträglich.
4. Der erste Jet erfüllt

   \[
   K_1'(0)=-gW,
   \qquad K_2'(0)=0,
   \]

   mit einem einzigen quellenselektierten (g\ne0), während die zweite Ableitung (K_2''(0)=g^2P X^2P) und damit der quadratische Taylor-Koeffizient (g^2P X^2P/2) die sequenzielle Antwort reproduzieren.
5. Ein kanonischer niedriger Fermionsektor (zum Beispiel der Einloch- oder Einfermionsektor) und der Einboson-Jet liefern nach den jeweiligen skalaren Energiesubtraktionen die nichttrivialen Matrizen (h) und (Omega) auf demselben Raum.
6. Der Jet ist quasilokal beziehungsweise besitzt eine aus der ursprünglichen Aktion hergeleitete Stütze; dies muss geprüft und darf nicht als Auswahlaxiom eingesetzt werden.
7. Ein gemeinsamer dichter Kern, Abschluss-/Selbstadjungiertheitsbedingungen, vollständige Sektoren und eine Quellenregel für alle Restblöcke machen aus den gemessenen Jets einen vollständigen Generator. Andernfalls sind nur die vier angezeigten Blöcke hergeleitet.

Die genaue Lücke ist daher:

\[
\boxed{
\text{kein kanonischer gemeinsamer gradierter Rohtransfer mit berechenbarem ersten Jet}
}
\]

und nicht bloß „noch kein besseres Symmetrieargument“.

Die bestehenden Übergangsregister bestätigen dieselbe Stelle:

- `TRANS.D4RAW.BANK.01`: roher 256-Moden-Raum (	o) W-Bank nicht eindeutig; Hom-Raum 8192-dimensional (`verification/graph_v2/transitions.json`, Z. 10–33).
- `TRANS.RAWKERNEL.GDELTA.01`: rohe Kernelinvarianten bestimmen (g/\Delta) nicht (ebenda, Z. 166–189).
- `TRANS.GAUSSCAR.NATIVEMODEL.01`: freier gaußscher Naht-CAR-Adapter (	o) natives wechselwirkendes Modell ist in der geprüften gleichen Modenzahlklasse behindert (ebenda, Z. 192–214).
- `QGEO.KERNEL.01`: die rohe Operatoridentität selbst ist offen; ein Spektrum genügt nicht.

## 5. Einziger begründeter nächster Rechenschritt

Der nächste Test sollte kein weiteres Hilfsmodell optimieren und nicht erneut (H_\eta) diagonalieren. Er lautet:

> Nimm den ersten Quellenkandidaten, der **aus seinen eigenen Originaldaten** zugleich geladene gerade/ungerade Felder, Zustand und Zeit besitzt. Konstruiere auf einem gemeinsamen invarianten Kern die vier ersten Jets
>
> \[
> J_h=\left.\partial_t(P_hT_{\rm src}(t)P_h)\right|_0,
> \quad
> J_b=\left.\partial_t(P_bT_{\rm src}(t)P_b)\right|_0,
> \]
>
> \[
> J_1=\left.\partial_t(P_{1b,0f}T_{\rm src}(t)P_{0b,2f})\right|_0,
> \quad
> J_2=\left.\partial_t(P_{2b,0f}T_{\rm src}(t)P_{0b,4f})\right|_0.
> \]

**Erfolg:** Nach Abzug der kanonisch aus derselben Quelle bestimmten skalaren Sektorenergien gilt (J_h=h^T) für die hier gewählte Einlochkonvention und (J_b=-\Omega); beide sind nichttrivial und quellenselektiert. Ferner gilt (J_1=-gW) mit genau einem (g\ne0), (J_2=0), und die zweite Ableitung des (Q=4)-Blocks reproduziert (g^2X^2) mit der richtigen Zeitordnung; alle orthogonalen/operatorwertigen Restkanäle verschwinden.

**Abbruch:** Schon (P_h,P_b,P_{0b,2f},P_{0b,4f}) oder die gemeinsame Quellenzeit sind nicht kanonisch definiert; (J_1=0); (J_1) enthält nur einen zustandsabhängigen Erwartungswert; (J_2\ne0); oder (W,h,\Omega) werden aus dem Ziel zurücktransportiert. Dann ist das Ergebnis `SOURCE_FIRST_JET_NOT_AVAILABLE` beziehungsweise der konkrete Kandidat ausgeschlossen.

Nach dem aktuellen Originalaudit greift das Abbruchkriterium **vor der Rechnung**: Der DtN-/OS-Zweig besitzt keinen konstruierten gemeinsamen geladenen (W)-Feldraum, und der affine Kubikzweig besitzt keine unabhängig ausgewählte physische Zeitderivation. Das ist ein Nachweis der aktuellen Quellenlücke, kein Unmöglichkeitssatz gegen eine zukünftige gemeinsame nichtgaußsche Rohquelle.

## Belegkern

- `experiments/theory-contracts/source-mixed-response-reconstruction-20260921/source/REPORT.md`, Z. 20–70, 88–156, 158–184, 267–296: stärkster positiver Anschluss, fehlende Operatoridentität und Nulltest linearer Quellenzeiten.
- `experiments/theory-contracts/compiler-vacuum-current-cubic-20260918/PROOF.txt`, Z. 19–39, 66–100, 107–131: affiner Ursprung, eindeutiges Kubik und offene Rohquelle-/Feldabbildung.
- `experiments/theory-contracts/common-source-gauge-grade-transfer-20260920/flavor/PROOF.txt`, Z. 50–80, 127–137, 278–298: Markierungsreparatur und fehlender current-to-field-Abstieg.
- `origin_theory.tex`, Z. 1829–1862: freie OS-Zweitquantisierung, DtN-Kandidat und offene Auswahl der rohen Dynamik.
- `tfpt_research_contracts.tex`, Z. 12726–12810 und 12832–12857: drei verschiedene Dynamikbegriffe, field-level Offenheit und nicht eindeutige Quantenlifts.
- `experiments/theory-contracts/primitive-transfer-selection-20260912/FOUR_PRIMITIVE_PROCESS.md`, Z. 6–14, 84–88; `COUPLING_RATE_POLYTOPE.md`, Z. 66–126: primitive Ereignisstütze ist Zusatzhypothese; Semigroup/RP/Symmetrie selektieren sie nicht.
- `verification/status_ledger.csv`, Zeilen 257, 381 und 1140: `QGEO.KERNEL.01 [O]`, `SEAM.EQUIV.01 [E]/[O]`, finite `DYN.MARKOV.EMBED.01 [E]` plus field-level `[O]`.

## Verdict

\[
\boxed{\texttt{NO_COMMON_SOURCE_FIRST_JET_IN_CHECKED_SET}}
\]

Der stärkste im geprüften Bestand vorhandene Ursprung liefert entweder **freie Kinetik/Transfer** oder **den markierten kubischen Tensor**, aber nicht beides auf demselben Quellenraum. Stabilität, Semigroup, zeitliche Reflexionspositivität, graduierte Jacobiidentität und abstrakte Lokalität eliminieren die direkte Doppelumwandlung nicht. Das fehlende unabhängige Gesetz ist der quellenselektierte verbundene **erste Transfer-Jet** mit (J_1=-gW\ne0), (J_2=0) und gleichzeitigem niedrigen Fermion-/Einboson-Jet für (h,\Omega).
