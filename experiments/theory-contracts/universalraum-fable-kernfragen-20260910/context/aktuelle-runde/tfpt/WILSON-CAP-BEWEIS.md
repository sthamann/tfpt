# Ein Z₄-Cap in den tatsächlichen TFPT-Feldoperatoren

10. September 2026. Exakte Konstruktion im deklarierten kompakten U(1)-Rotor/CAR-Parent; anschließend ein exakter Widerspruch gegen dessen autonome endliche Dynamikreduktion. Keine neuen Materiearten, kein elektrischer Cutoff, kein angehängter Hilbertraum, keine Änderung des Parents.

**Ergebnis:** Der native Frobenius-Cap lässt sich einschließlich Produkt, Einheit, Adjunktion, positiver Paarung und Balancierung konkret mit zwei vorhandenen gaugeinvarianten Wilsonschleifen realisieren. Eine vorgegebene native Anfangspräparation trägt dabei exakt den kanonischen Z₄-Zustand. Die vollständige physische Dynamik erhält diese endliche Darstellung jedoch nicht: Das ursprüngliche Low–High-Hopping besitzt einen streng positiven, exakt berechneten Austrittsoperator. Die Konstruktion ist deshalb ein tatsächlicher algebraischer Anschluss mit einem präzisen dynamischen Fortsetzungsbedarf.

## 1. Native Daten und gemeinsame Domäne

Wir verwenden exakt den Parent aus `observable-dynamics/README.md`, `neutral-ground-state/README.md` und `ground-state-loop-response/README.md` auf einem kubischen Torus mit \(L\ge5\), \(N=L^3\):
\[
H=\frac\kappa2\sum_eE_e^2
+l^*(aA_U+\beta a^2A_U^2)l
+4d^*d+b(d^*A_Ul+l^*A_Ud),
\]
\[
a=1/12,\quad\beta=1/4,\quad b=1/24,\quad\kappa=1/100.
\]
Die Rückwege in \(A_U^2\) erzeugen das vollständige ursprüngliche \(\epsilon_L=1/96\). Auf einem Link gilt \(E|n\rangle=n|n\rangle\), \(U|n\rangle=|n+1\rangle\). Die lokale Rotoralgebra enthält laut Original alle beschränkten Operatoren auf dem endlichen Link-Hilbertraum, insbesondere beschränkte Funktionen von E. Die Feldalgebra enthält die beiden originalen CAR-Arten l,d.

Der gemeinsame Kern \(\mathcal D_{\rm fin}\) besteht aus endlichen Linearkombinationen ganzzahliger Fluxbasiszustände und Fockzustände. Alle unten verwendeten endlichen Verschiebungen, Projektionen und H erhalten diesen Kern. H ist eine beschränkte Störung des selbstadjungierten elektrischen/onsite-Operators. Es wird keine endliche Flux-Hamiltonmatrix als Ersatz verwendet.

Die native Gaussbedingung lautet
\[
G_x=n_{L,x}+n_{H,x}-1+\operatorname{div}_xE=0.
\]
Die vorhandene Präparation \(\Omega_0\) hat einen Low-Fermion pro Ort, keine High-Fermionen und sämtliche Fluxwerte null. Sie ist physisch neutral, aber laut Original weder stationär noch ein Grundzustand. Diese Unterscheidung bleibt erhalten.

## 2. Gaugeinvariante endliche Clock aus einem echten Wilsonloop

Wähle eine elementare Plaquette mit orientiertem ganzzahligem Schleifenstrom p. Es gilt \(\operatorname{div}p=0\), \(\|p\|^2=4\). Der tatsächliche Wilsonoperator
\[
W=U^p=\prod_eU_e^{p_e}
\]
kommutiert mit sämtlichen Gaussgeneratoren und mit allen CAR-Operatoren. Wähle einen seiner Links e mit \(p_e=1\), und setze
\[
Z=e^{i\pi E_e/2},\qquad
P_r=\frac14\sum_{j=0}^3i^{-rj}Z^j,\qquad
S=W(I-P_3)+W^{-3}P_3.
\]
Jeder Faktor gehört zur bestehenden lokalen physikalischen Algebra. P_r projiziert auf \(E_e\equiv r\pmod4\). S addiert den ganzen Schleifenstrom, außer beim Rest drei: Dort subtrahiert S dreimal den Schleifenstrom. Es folgt auf jeder ganzzahligen Fluxbasis exakt
\[
S^4=I,\qquad S^*S=SS^*=I,\qquad ZS=iSZ.
\]
Vier Schritte enthalten drei Inkremente und einen Rücksprung −3. Dadurch werden auch sämtliche anderen Schleifenlinks wiederhergestellt. Jeder einzelne Schritt bleibt Gauss-neutral. Anders als bei einem Einzel-Link-Shift braucht man keine nur mod vier geltende Ersatz-Gaussbedingung.

\(\mathcal B=C^*(Z,S)\cong M_4(\mathbb C)\) ist damit eine konkret dargestellte endliche Algebra innerhalb der tatsächlichen Feldalgebra. Ihre Matrixeinheiten sind
\[
F_{ab}=S^{a-b}P_b,
\quad F_{ab}F_{cd}=\delta_{bc}F_{ad},
\quad F_{ab}^*=F_{ba}.
\]
Der verbliebene unbegrenzte Fluxinhalt wird nicht gelöscht. Diese Algebra wirkt auf den Restklassen, mit dem durch S definierten Rücksprung. Sie ist nicht schon die gesamte Rotoralgebra oder deren Dynamik.

## 3. Expliziter zustandstreuer Frobenius-Intertwiner

Für einen Loop definiere
\[
J_1e_a=S_1^a\Omega_0,\qquad a=0,1,2,3.
\]
Die vier Zustände besitzen unterschiedliche tatsächliche Fluxwerte und sind orthonormal. Die Darstellung \(\pi(e_a)=S_1^a\) erhält Produkte, Involution \(e_a^*=e_{-a}\) und Einheit der nativen Gruppenalgebra. Zudem gilt
\[
\langle\Omega_0,\pi(x)^*\pi(y)\Omega_0\rangle
=\tau(x^*y),\qquad\tau(e_a)=\delta_{a0}.
\]
J_1 ist somit genau die isometrische GNS-Identifikation für diesen positiven Zustand, nicht bloß ein Dimensionsvergleich. Auch die Grade werden erhalten: \(Z_1J_1e_a=i^aJ_1e_a\).

Nun benutze zwei disjunkte vorhandene Plaquetten, zum Beispiel in den Ebenen z=0 und z=2. Ihre Operatoren kommutieren. Die Abbildung
\[
J_{12}(e_a\otimes e_b)=S_1^aS_2^b\Omega_0
\]
ist eine Isometrie des 16-dimensionalen Tensorraums in den **ursprünglichen** neutralen physikalischen Hilbertraum. Es werden keine zusätzlichen Moden eingeführt.

Die native Multiplikation \(m(e_a\otimes e_b)=e_{a+b}\) erhält sogar eine konkrete Feldoperatorrealisierung:
\[
\mathsf M=\sum_{a,b=0}^3
F^{(1)}_{a+b,a}F^{(2)}_{0,b}.
\]
Alle Indizes sind mod vier. Mit J_1 jetzt als Ein-Loop-Code und zweitem Loop in Rest null gilt
\[
\mathsf M J_{12}=J_1m,\qquad
\mathsf M^*J_1=J_{12}m^*,\qquad
J_1\eta=\Omega_0.
\]
Die Adjunktidentität benutzt dieselbe positive Paarung; \(mm^*=4I\) wird daher mittransportiert. Global ist \(\mathsf M\mathsf M^*=4P_0^{(2)}\). \(K=\mathsf M/2\) ist eine physische Kontraktion mit \(K^*K\) als Projektion. Wer K als Messzweig verwendet, muss auch den zweiten Zweig \(I-K^*K\) behalten; beide erfüllen die Vollständigkeitsrelation. Multiplikation wird dadurch nicht fälschlich zu einer verlustfreien unitären Operation erklärt.

Der native Cap erhält das konkrete Bild
\[
\Psi_{\rm cap}=J_{12}\frac{m^*\eta}{2}
=\frac12\sum_{a=0}^3S_1^aS_2^{-a}\Omega_0
=K^*\Omega_0.
\]
Er ist normiert, mit Einheitsamplitude 1/2, und erfüllt
\[
(Z_1Z_2)\Psi_{\rm cap}=\Psi_{\rm cap},\qquad
(S_1S_2^{-1})\Psi_{\rm cap}=\Psi_{\rm cap}.
\]
Der unnormierte Cap besitzt weiterhin Normquadrat \(4=1+3\). Alle gemischten Antworten in den bezeichneten endlichen markierten Algebren werden durch J erhalten.

Es gibt sogar eine explizite unitäre Präparation innerhalb derselben lokalen Feldalgebra: Der Fourieroperator
\[
\mathsf F_1=\frac12\sum_{a,b}i^{ab}F^{(1)}_{ab}
\]
und \(\mathsf C=\sum_aP_a^{(1)}S_2^{-a}\) sind gaugeinvariant und unitär; \(\mathsf C\mathsf F_1\Omega_0=\Psi_{\rm cap}\). Das ist eine erlaubte Feldoperation. Dass der unveränderte Hamiltonoperator sie zu einer ausgewählten Zeit erzeugt oder TFPT genau diese Präparation auswählt, wurde damit nicht bewiesen.

## 4. Exakte tatsächliche Hamiltonwirkung: der endliche Code ist nicht abgeschlossen

Sei \(P_J=J_{12}J_{12}^*\). In jedem Codezustand sind weiterhin alle Low-Moden besetzt und alle High-Moden leer. Der elektrische Anteil ist diagonal und erhält den Code. Alle nichtdiagonalen Low–Low-Hops sind Pauli-blockiert; die Rückwege ergeben genau \(\epsilon_LNI\). Damit ist die Kompression
\[
J_{12}^*HJ_{12}
=\epsilon_LNI_{16}
+2\kappa\,\mathrm{diag}_{a,b}(a^2+b^2).
\]
**Kompression ist jedoch keine dynamische Einschränkung.** Jeder der \(6N\) originalen gerichteten Low–High-Hops
\[
b\,d_x^*\,U_{xy}\,l_y
\]
erzeugt ein High-Fermion bei x und ein Low-Loch bei y. Die verschiedenen geordneten Paare \((x,y)\) liefern orthogonale Fockmuster. Für jedes Paar ist \(U_{xy}\) unitär; deshalb erhält sein Rotoranteil alle Skalarprodukte. Kein solcher Zustand liegt im Code. Es folgt für den tatsächlichen Austrittsoperator
\[
\Gamma=(I-P_J)HJ_{12}
\quad\boxed{\Gamma^*\Gamma=6Nb^2I_{16}=\frac N{96}I_{16}.}
\]
Alle Austrittszustände erfüllen weiterhin Gauss. Ihre Fluxänderung kompensiert genau den erzeugten Loch-/Teilchenladungsunterschied.

Das ist ein **harter Widerspruch für diesen festen Code**: Kein nichtverschwindender Codevektor, auch keine spezielle Cap-Linearkombination, kann den Austritt aufheben. Für kein beliebiges 16-dimensionales \(h_{\rm src}\) gilt \(HJ_{12}=J_{12}h_{\rm src}\), weil die Projektion dieser Gleichung auf das orthogonale Komplement \(\Gamma=0\) verlangen würde. Auf einem einzelnen bezeichneten ursprünglichen Hop ist bereits eine Austrittsnormquadratskomponente \(b^2=1/576\) sichtbar. Die gesamte Zahl N/96 gilt für die deklarierte globale All-Low-Präparation; sie wird nicht als universelle Vakuumuntergrenze ausgegeben.

Auch die endliche **rotor-only Algebra** bleibt unter H nicht autonom: Für einen Hop T mit elektrischem Shift \(p_e=\sigma=\pm1\) gilt auf \(\mathcal D_{\rm fin}\)
\[
[T,Z]=(1-i^\sigma)TZ.
\]
Der passende Materie-Offdiagonaleintrag von \([H,Z]\) hat Betragquadrat \(2b^2=1/288\). Jedes Element von \(\mathcal B\) wirkt als Identität auf CAR und hat dort Eintrag null. Wäre \(\alpha_t(Z)\in\mathcal B\), wäre dieser Matrixeintrag für alle t null; seine tatsächlich existierende Ableitung auf dem angegebenen Kern ist aber ungleich null. Dieser Nachweis benötigt keine unbewiesene Operatornorm-Differenzierbarkeit der großen Rotoralgebra.

## 5. Cap-Zustand, thermische Zeit und verbleibende Möglichkeit

Die vier elektrischen Cap-Energien relativ zu \(\epsilon_LN\) lauten
\[
(0,20\kappa,16\kappa,20\kappa).
\]
Daher sind Energiezunahme \(14\kappa=7/50\) und elektrische Varianz \(68\kappa^2\). Für \(T_{\rm bal}=S_1S_2^{-1}\) gilt
\[
\|P_{\rm AllLow}[H,T_{\rm bal}]\Psi_{\rm cap}\|^2
=208\kappa^2=13/625.
\]
Zusammen mit dem Austritt beträgt die volle Energievarianz exakt \(68\kappa^2+N/96>0\). Der konstruierte reine Cap-Zustand ist somit nicht stationär, kein Vakuum und kein KMS-Zustand für die tatsächliche H-Dynamik. Die kanonische Z₄-Zustandspaarung im vorigen Abschnitt ist dadurch nicht falsch; sie wurde für die ausdrücklich bezeichnete Präparation bewiesen. Die bereits vorhandenen physikalischen Grundzustands-GNS-Darstellungen bleiben andere, nicht eindeutig ausgewählte Zustandskonstruktionen. Ihre Restriktion auf die Loop-Clock ist hier nicht berechnet.

Das Brechen einer **festen** Cap-Balancierung widerlegt keinen zeitabhängig mitbewegten Cap. Man kann \(J(t)=e^{-itH}J_{12}\) und sämtliche Operationen gemeinsam transportieren; dann bleiben ihre algebraischen Beziehungen exakt. Damit wurde jedoch die bereits gegebene physische Dynamik eingesetzt, nicht aus dem endlichen Cap erzeugt. Für einen konstruktiven autonomen Ausbau muss der dynamische Abschluss mindestens die tatsächlich auftretenden neutralen Loch-/High-Teilchen- und Wilsonwörter enthalten. Die bewiesene Leakage verhindert das Weglassen dieser Richtungen.

## 6. Präzise Reichweite und Kontrolle

Die Konstruktion nutzt ausschließlich vorhandene U(1)-Rotoroperationen und unveränderte CAR; sie ersetzt weder den SM-Gauge-Anschluss durch SU(3) noch die physische Raumzeit-/Gravitationsherleitung. Die Wahl der beiden Plaquetten, eines markierten Links und des Flux-Restfensters sowie der Präparation bleibt ausdrücklich Input. Insbesondere ist noch nicht bewiesen, dass die elektrische Vierteldrehung Z genau die ursprüngliche physische Seam-/Calderón-Clock realisiert. Bewiesen ist eine konkrete Darstellung des gleichen markierten Frobeniusobjekts in vorhandenen Feldoperatoren; dessen intrinsische Auswahl ist ein zusätzlicher Herkunftsschritt. Dass neutrale Loop-Operatoren verfügbar sind, identifiziert sie auch nicht mit den geladenen High-CAR-Erzeugern; sie können höchstens eine noch herzuleitende Koeffizientenstruktur begleiten.

`check_wilson_cap.py` führt **18 exakte Kontrollen** aus. Auf dem echten \(L=5\)-Torus werden sämtliche 750 gerichteten LH-Terme mit exakten CAR-Vorzeichen und ganzzahligen Fluxänderungen auf allen 16 Codezuständen berechnet: 12.000 orthogonale physische Ausgangsbasiszustände und \(\Gamma^*\Gamma=(125/96)I_{16}\). Kein Flux-Hamiltonian wird abgeschnitten. Die allgemeinen Identitäten und das Volumenargument stehen oben. Native Module wurden per Codegraph gelesen, nicht importiert oder als Suite ausgeführt. Quellen und Artefakte sind in `quellenmanifest.json` gehasht.
