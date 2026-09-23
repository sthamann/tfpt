# RR→W: Wählt TFPT bereits den physischen Zeitgenerator?

**Entscheid:** **Nein.** Der neue RR→W-Anschluss liefert einen exakt durch den nativen Tensor getragenen **erhaltenen inneren Generator**. Die Originalquellen wählen ihn jedoch nicht als Hamiltonzeit des nativen \(W\)-Modells aus. Die erste fehlende Bedingung ist eine aus der rohen P1/P2-Quelle kommende, lokale und zustandserhaltende Feldabbildung, welche **dieselbe** Zeitentwicklung auf RR-, geladenen und \(W\)-Operatoren verschränkt.

Das ist kein allgemeines No-go gegen eine spätere physische RR-Zeit. Es entscheidet die gegenwärtige Auswahlfrage: Geometrische Clock, modulare Zeit, Viertelholonomie und der native wechselwirkende Hamiltonoperator sind noch verschiedene Verträge.

## 1. Was positiv und exakt vorliegt

Auf dem markierten RR-Raum

\[
E=H^0(\mathbb P^1,\mathcal O(\mu_4)),\qquad
R=\operatorname{diag}(1,i,-1,-i,1),\qquad Se_n=-e_{4-n}
\]

wählt \(R^2\) die \(3+2\)-Zerlegung. Der vorhandene Hyperladungsoperator und der Halbspinor \(\Lambda^{\rm even}E\) folgen. Der native Paar-Tensor erfüllt nach dem dokumentierten Hodge-Basiswechsel die endliche D4-Kovarianz. Das ist eine echte Strukturbrücke, nicht bloß eine Dimensionsgleichheit.

Mit der zusätzlich erklärten Hardy-Metrik wird

\[
Jf=(z^4-1)f,\qquad h=J^{-1}(-i\partial_\theta)J
\]

zu einem selbstadjungierten endlichen Generator mit Spektrum \(0,1,2,3,4\). Diese Metrik und dieser Logarithmus sind aber Bestandteile des Einbettungsvertrags. Die D4-Wirkung allein lässt vier positive Metrikgewichte offen; P1 wählt die Hardy-Metrik bisher nicht. Außerdem mischt \(h\) die als innere Farbe gelesenen drei Richtungen nicht stationär: bereits \([h,T_{02}]\ne0\).

## 2. Der RR-Generator hebt sich exakt durch \(W\), ist aber eine Ladung

In der Hardy-Fourierbasis ist der Generator diagonal,

\[
h_E=\operatorname{diag}(0,1,2,3,4),\qquad \operatorname{tr}h_E=10.
\]

In der normalisierten D4-angepassten RR-Basis hat derselbe Operator stattdessen den ersten Block \(\left(\begin{smallmatrix}2&2\\2&2\end{smallmatrix}\right)\) und die übrigen Einträge \(2,1,3\). Der Archivtensor und \(h_E\) müssen stets gemeinsam in dieselbe Basis transportiert werden. Die folgende Lie-Algebra-Identität gilt darstellungsbedingt für jedes \(h_E\), also auch für diesen tatsächlichen RR-Generator:

\[
h_F=d\Gamma_{\rm even}(h_E)\otimes I_4,
\]

\[
h_B=\Bigl(10I_{10}+\operatorname{diag}(h_E,-h_E^{\mathsf T})\Bigr)\otimes I_6.
\]

Der eigene exakte Gegencheck verwendet den diagonalen Repräsentanten in der dazugehörigen kanonischen Koordinatenbasis und ergibt

\[
W\,d\Gamma_2(h_F)=h_BW
\]

auf **allen 480 von 480** getragenen Paarkoeffizienten. Dabei hat \(h_F\) die Eigenwerte \(0,\ldots,10\), \(h_B\) die Eigenwerte \(6,\ldots,14\). Folglich kommutiert auf dem endlichen Teilchenkern

\[
K_{RR}=f^\dagger h_Ff+b^\dagger h_Bb
\]

mit dem nativen Hamiltonoperator

\[
H_W=\Delta N_b+g\sum_A(b_A^\dagger P_A+P_A^\dagger b_A).
\]

Das ist die positive Brücke: RR liefert eine exakte \(U(1)\)-Symmetrie des vorhandenen \(W\)-Modells.

Sie reicht durch die bereits vorhandene nichtlineare Antwortkette. Mit \(\mathcal L A=[A,H_W]\), \([K_{RR},H_W]=0\) und \([K_{RR},f]=-h_Ff\) folgt durch Jacobi und Induktion

\[
[K_{RR},\mathcal L^n f]=-h_F\,\mathcal L^n f\qquad(n\ge0).
\]

Die im Original bereits hergeleitete Jacobi-/Resolventenantwort einschließlich ihres nichtverschwindenden Rests \(\Sigma_2\) trägt damit dieselbe RR-Innenwirkung in jeder Stufe. Da dieselbe Kovarianz für die volle Spin(10)×SU(4)-Wirkung gilt, zerfällt bei invariantem \(\Omega_W\) der zu \(f\Omega_W\) zyklische Antwortmodul entsprechend als \(\mathbb C^{64}\otimes\mathcal M\), mit der Liouvillianwirkung auf dem Multiplizitätsfaktor. Das ist eine neue Kovarianzklassifikation der vorhandenen Antwort, keine neue Herleitung ihrer Dynamik.

Sie identifiziert keine Zeit. Schreibe die \(GL(5)\)-Wirkung als Spin(10)-Anteil plus Zentrum. Dann gilt exakt

\[
K_{RR}=J_{\mathrm{Spin}(10)}(h_E)+5Q,
\qquad Q=N_f+2N_b.
\]

Der später dokumentierte v1.6.4-Grundzustandsvertrag gibt für das festgelegte schwach gekoppelte Modell einen Spin(10)×SU(4)-invarianten Zustand \(\Omega_W\) mit \(Q=64\). Daher

\[
K_{RR}\Omega_W=320\,\Omega_W.
\]

Im selben \(Q=64\)-Sektor existiert aber der einfache Besetzungszeuge mit \(N_f=0,N_b=32\) in einer \(h_B=6\)-Mode; er hat \(K_{RR}=192\). Weder ein globaler Energieoffset noch \(\mu Q\) ändert diese Rangfolge innerhalb desselben Ladungssektors. Der native Grundzustand ist also nicht der Grundzustand von \(K_{RR}\).

Noch elementarer: Für \(g\ne0\) koppelt \(H_W\) verschiedene \((N_f,N_b)\)-Besetzungen durch \(b^\dagger P+P^\dagger b\); \(K_{RR}\) ist besetzungszahlkonservierend. Deshalb kann \(H_W=aK_{RR}+cI\) als Operator nicht gelten. Dieser Schluss benötigt die Grundzustandsaussage nicht.

Die ältere v1.6.3-Auswertung hatte die Eindeutigkeit bei \(g/\Delta=1/20\) noch nicht reproduziert; v1.6.4 behauptet eine frische Re-Zertifizierung. Für die vorliegende Entscheidung ist diese Versionsspannung nicht tragend, weil die Operatorstruktur bereits \(K_{RR}\ne H_W\) beweist.

## 3. Reflexion, chemische Verschiebung und Clock-Zweig

Für den gewählten minimalen Logarithmus gilt exakt

\[
Sh_ES=4I-h_E,
\qquad
S(h_E-2I)S=-(h_E-2I).
\]

Das macht \(S\) zu einer Spektralreflexion um Energie 2. Es macht \(h_E\) nicht D4-invariant. Die Zentrierung \(h_E-2I\) ist zudem indefinit und wird nach Exterior-/Bosonenlift nicht zu einem harmlosen skalaren Offset: Ein Einteilchen-Shift \(h_E\mapsto h_E+\lambda I\) hebt sich als gradabhängige chemische Ladung, nicht als \(cI\) auf dem Fockraum.

Auch der Clock-Zweig ist offen. Aus \(R=e^{i\pi h_E/2}\) folgen nur die Eigenwerte von \(h_E\) modulo 4. Andere Logarithmen \(n\mapsto n+4k_n\), das Vorzeichen der Zeit und ihre Einheit bleiben möglich. Die Relation mit \(S\) beschränkt paarweise Zweige, wählt aber ohne Positivitäts-, Zustands- und Lokalitätsvertrag keinen physischen Generator.

## 4. Warum die anderen vorhandenen Zeitverträge die Lücke nicht schließen

1. **Viertelholonomie.** Die tatsächliche Quelle besitzt \(H_{\rm source}=L_0-Q/4\). Auf dem bedingten E8-Ziel ergibt das \(H_\delta=L_0-\delta\cdot P\), zwei Grundzustände und eine Lücke \(1/2\). Neutrale Ströme sind für den linearen Ladungsterm blind; geladene Paar- und Spinorfelder sehen ihn. Die gepinnten \(C/J\)-Lifts kommutieren nicht mit \(H_\delta\).
2. **Zwei Clock-Symmetrien.** Innerhalb der benannten Klasse positiver homogener quadratischer Stromhamiltonoperatoren erzwingt gemeinsame Invarianz unter \(C\) und \(J\) zwar \(H=vL_0+c\). Dieser Satz ist bedingt: Die rohe Quelle muss beide Implementer erst als Symmetrien derselben physischen Zeit liefern.
3. **Modulare Zeit.** Bei einer lokalen normalen, zustandserhaltenden *-Isomorphie würde die Tomita-Takesaki-Dynamik automatisch mittransportiert. Die benötigte Rohnetz-/Zustandsabbildung fehlt. Der frühere endliche HSMI-Zeuge vermischte eine Phasendrehung mit reeller modularer Streckung und liefert diese Auswahl nicht.
4. **Lokaler QWZ-Grenzwert.** Für die erklärte Ein-Kopien-Quelle konvergieren geladene Kovarianz und Zeitantwort gemeinsam zu einem chiralen Fermion. Das ist eine positive Quellzeitbrücke für **einen** Kanal; sie erzeugt weder acht Quellenspezies noch den RR→W-Adapter.

## 5. Präziser Auswahlvertrag

Ein physischer RR→W-Zeitanschluss ist erst angenommen, wenn ein Vertrag RR_W.TIME.SELECT.01 folgende Punkte gleichzeitig erfüllt:

1. **Quellseitige Daten:** Aus dem rohen P1/P2-Rand kommen eine lokale Algebra \(\mathcal A_{raw}\), ein Zustand \(\omega_{raw}\) und eine stark stetige Zeitgruppe \(\tau_t^{raw}\). In ihrer physischen GNS-Darstellung muss die Zeit durch einen positiven beziehungsweise nach unten beschränkten Generator implementiert sein. Treue beziehungsweise zyklisch-separierende Vektoren sind zusätzlich nur dann erforderlich, wenn die modulare Rekonstruktionsroute benutzt wird. Diese Daten dürfen nicht nachträglich vom Ziel zurücktransportiert definiert werden.
2. **Ein gemeinsamer Feldadapter:** Eine lokale, adjungierten-, Ladungs- und Graduierungs-erhaltende Abbildung \(\Phi\) realisiert RR-Träger, geladene Felder und \(W\) im selben Zielraum und erfüllt \(\omega_{raw}=\omega_W\circ\Phi\). Sie leitet insbesondere die Hermitesche RR-Metrik her.
3. **Zeitintertwining auf einem gemeinsamen Kern:**
   \[
   \Phi(\tau_t^{raw}(A))=e^{itH_W}\Phi(A)e^{-itH_W}
   \]
   für neutrale **und** geladene Erzeuger, ihre Adjungierten und die \(W\)-Wechselwirkung. Eine dimensionslose positive Skala darf auftreten, muss aber aus demselben metrologischen Vertrag kommen.
4. **Clock-Rolle:** Für \(R,S,C,J\) wird quellenintern entschieden, ob sie mit \(H_W\) kommutieren, Zeit umkehren, einen Hintergrund mittransformieren oder nur als Heisenberg-entwickelte Operatoren vorliegen. Bloße Matrixordnungen reichen nicht.
5. **Zustandsprüfung:** Der Zustand wird wie in Punkt 2 erhalten. Falls \(\Phi\) durch eine GNS-Isometrie oder Unitäre \(U\) implementiert wird, gilt zusätzlich \(U\Omega_{raw}=\Omega_W\). Derselbe Generator muss die behauptete Stationarität beziehungsweise Grundzustandsrolle tragen. Ein Zusatz \(\mu Q+cI\) darf nur verwendet werden, wenn Quelle, Ensemble und Ladungssektor ihn auswählen.

**Erste fehlende Bedingung:** Punkt 2–3 in ihrer kleinsten Form: ein quellenabgeleiteter lokaler Adapter \(\Phi\), der Zustand und geladene Zeitentwicklung gleichzeitig erhält. Vor diesem Nachweis kann der Zieloperator seine eigene Herkunft nicht selektieren.

Der aktuelle Befund spricht für die saubere Klassifikation

\[
\boxed{K_{RR}\text{ = erhaltener innerer Generator},\qquad H_W\text{ = separate Modellzeit}.}
\]

Eine spätere gemeinsame Quelle könnte beide verknüpfen oder einen anderen Hamiltonoperator auswählen. Das ist offen; bereits ausgewählt ist es nicht.

## Originalquellen und geprüfte Stellen (11 Dateien)

1. outputs/TFPT_RR_Quellenbruecke_20260921.md, Z. 30–70, 87–169, 191–205 — RR-Split, \(W\)-Kovarianz, gewählte Metrik/Zeit und physischer Auswahlpunkt.
2. work/source_reconstruction_2/rr_source_certificate.py, Z. 19–64 — exakte D4-, \(3+2\)-, Hyperladungs-, Generator- und Reflexionsrechnung.
3. outputs/TFPT_RR_Quellenbruecke/RR_W_CHECK.py, Z. 155–270, 281–371 — gepinnter \(W\)-Tensor, beide D4-Wirkungen, Determinanten-/Hodge-Transport und Metrikgrenze.
4. experiments/theory-contracts/charged-source-time-audit-20260920/PROOF.txt, Z. 154–246, 248–297 — \(H_\delta\), geladene Frequenzen, C/J-Test und bedingte Auswahl \(vL_0+c\).
5. experiments/theory-contracts/charged-source-time-audit-20260920/contract_index.json, Z. 1–86 — Verdict PARTIAL, Kills und offene mikroskopische Quellzeit.
6. experiments/theory-contracts/source-rg-clock-bridge-20260920/PROOF.txt, Z. 161–210, 212–240 — positive Coxeter-kovariante Geschwindigkeitsfamilie und fehlende Clock-Implementer.
7. experiments/theory-contracts/modular-source-selection-audit-20260917/RESULTS.md, Z. 20–71, 136–169 — HSMI-Gegencheck und Bedingung gemeinsamer Algebra/Zustand.
8. experiments/theory-contracts/source-local-line-20260920/SOURCE_LINE_PROOF.txt, Z. 1–20, 63–150, 202–248 — positive Ein-Kanal-Quellzeit und offene Achtkanalherkunft.
9. experiments/theory-contracts/universalraum-clock-origin-20260915/RESULTS.md, Z. 180–250, 476–493 — Clock als Spin(10)-Element, aber nicht Hamiltonzeit; gemeinsamer \(H,\Omega\)-Antworttest.
10. experiments/theory-contracts/universalraum-native-operations-ground-response-20260915/RESULTS.md, Z. 35–50, 103–175, 282–310 — Definition von \(H_W\), nativer Grundzustands-/Operationsvertrag und offene Operationsherkunft.
11. experiments/theory-contracts/universalraum-native-ground-response-20260915/RESULTS.md, Z. 90–109, 128–380, 382–390, 538–566 — spätere Grundzustands-Re-Zertifizierung, vorhandene Jacobi-/Resolventenantwort, Symmetrie und Unterscheidung von Modellzeit, Clock und Kontrollen.
