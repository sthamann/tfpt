# TFPT: kontinuierliche RR-Clock im unveränderten nativen Prozess

21. September 2026. Forschungsfortsetzung; endliche, bedingte algebraische Aussage. Keine Promotion eines physischen Theorie-Claims.

## Fragestellung

Der vorherige Anschluss identifiziert die konkrete D4-Wirkung des fünfdimensionalen Riemann–Roch-Raums mit einer kovarianten Wirkung auf dem nativen Tensor W. Die nächste Frage ist stärker: Gibt es auch einen kontinuierlichen Generator derselben geometrischen Rotation, der mit dem nativen Paarprozess und seinem wechselwirkenden Zustand verträglich ist?

Der positive Befund ist eine erhaltene innere Clock. Daraus folgt noch keine Gleichheit dieser Clock mit dem physikalischen Hamiltonoperator. Gerade diese Rollen lassen sich auf demselben wechselwirkenden Grundzustand exakt unterscheiden.

## 1. Geometrischer Generator und erklärte Norm

Die verwendete Norm ist weiterhin die ausdrücklich gewählte Hardy-/Divisor-Norm aus dem vorherigen Bericht. In der orthonormalisierten D4-angepassten Basis entsprechen die fünf geometrischen Richtungen den Randfunktionen

\[
q_0=(z^4-1)/\sqrt2,\quad q_1=(z^4+1)/\sqrt2,
\quad q_2=z^2,\quad q_3=z,\quad q_4=z^3.
\]

Der komprimierte Generator \(D=z\partial_z\) lautet

\[
h=\begin{pmatrix}2&2&0&0&0\\2&2&0&0&0\\0&0&2&0&0\\0&0&0&1&0\\0&0&0&0&3\end{pmatrix}.
\]

Er ist hermitesch, hat Spektrum \(0,1,2,3,4\), Spur 10 und erfüllt
\[
\exp(i\pi h/2)=R_E=\operatorname{diag}(1,1,-1,i,-i).
\]
Hier bezeichnet R_E die Trägerdrehung; die zusätzliche Familienpermutation ist ein weiterer Faktor der vollständigen markierten D4-Wirkung. Sie darf in einer Aussage über die vollständige Clock nicht stillschweigend weggelassen werden.

Die Zuordnung der normierten geometrischen Basis zur orthonormalen Archivbasis ist erklärt. Sie ist keine nachträgliche Behauptung, die unnormierten meromorphen Vertreter hätten Einheitsgram: Dort war die Hardy-Gram-Matrix diag(2,1/2,1,1,1). Die physische Auswahl dieser Metrik aus P1 bleibt offen.

### 1.1 Die restlichen Normgewichte sind im endlichen Vertrag keine verschiedenen Theorien

Hier lässt sich die vorherige Aussage über vier offene Metrikgewichte weiter präzisieren. In der unnormierten D4-angepassten Basis ist der geometrische Ableitungsoperator
\[
h_{\rm raw}=\begin{pmatrix}2&1&0&0&0\\4&2&0&0&0\\0&0&2&0&0\\0&0&0&1&0\\0&0&0&0&3\end{pmatrix}.
\]
Eine positive D4-invariante Hermitesche Form hat die Gestalt G=diag(a,b,c,d,d). Die Forderung, dass genau dieser geometrische Generator selbstadjungiert ist, ergibt
\[
G h_{\rm raw}=h_{\rm raw}^\dagger G
\quad\Longleftrightarrow\quad a=4b.
\]
Somit bleiben G=diag(4b,b,c,d,d), b,c,d>0. Für zwei solche Formen G₁,G₂ ist T=G₂⁻¹ᐟ²G₁¹ᐟ² eine Isometrie vom ersten zum zweiten Raum. Die ersten beiden Diagonaleinträge von T sind gleich; deshalb kommutiert T mit R, S und h_raw.

Transportiert man auch die induzierten Spinor- und Bosonenmetriken,
\[
G_F=\Gamma_{\rm even}(G)\otimes I_4,
\qquad G_B=\det(G)\operatorname{diag}(G,G^{-T})\otimes I_6,
\]
so hebt sich T aufgrund der GL(5)-Kovarianz des W-Tensors zu einer Isometrie des gesamten endlichen Diagramms einschließlich W und Clock. Deshalb liefern diese drei positiven Normgewichte in diesem funktoriellen Vertrag dieselbe unitäre Äquivalenzklasse.

Das entfernt eine künstliche Mehrdeutigkeit auf der endlichen Ebene. Es leitet keine Norm oder lokale Abbildung auf der ursprünglichen Quellalgebra her: Der finite Basiswechsel muss nicht die räumliche Lokalität einer noch zu konstruierenden Feldabbildung erhalten. Auch der geometrische Ableitungsoperator selbst ist hier vorausgesetzt, nicht allein aus der Ordnung R⁴=I ausgewählt.

## 2. Kontinuierlicher Transport durch den tatsächlichen Tensor

Für einen Generator h auf E definiere
\[
A_h=d\Gamma_{\rm even}(h)\otimes I_4,
\qquad
B_h=\left[\operatorname{tr}(h)I_{10}
+\operatorname{diag}(h,-h^T)\right]\otimes I_6.
\]
Dabei ist dΓ die infinitesimale äußere Wirkung, kein weiterer physischer Hamiltonterm. Der Spurterm ist die infinitesimale Wirkung derselben Determinantenlinie, die bereits im diskreten W-Anschluss benötigt wurde.

Die entscheidende Identität ist
\[
W\,d\Gamma_2(A_h)=B_h W.
\]
Sie ist eine lineare Matrixidentität in h. Eine vollständige Prüfung auf allen 25 Matrixeinheiten E_ij beweist sie für jedes komplexe h dieser Darstellung, insbesondere für alle hermiteschen Generatoren. Analog besitzt der Viermarken-/Familienraum die äußere Wirkung auf Λ²F₄.

Für den geometrischen Generator hat A_h die geraden Teilsummen der Energien 0,1,2,3,4, jede mit vierfacher Familienmultiplizität. B_h besitzt die Energien \(10+\epsilon_i\) und \(10-\epsilon_i\), jeweils sechsmal. Deshalb ist die Energie des Paars genau die Energie des dazu gekoppelten Bosonkanals. Ein pauschaler Vergleich aller fünf Trägerenergien mit einem einzigen Bosonoffset hätte diesen natürlichen Transport übersehen.

## 3. Eine erhaltene Clock des unveränderten Hamiltonoperators

Mit den ursprünglichen CAR-/CCR-Operatoren setze
\[
K_h=f^\dagger A_hf+b^\dagger B_hb.
\]
Der native Hamiltonoperator bleibt
\[
H_W=\Delta N_b+g\sum_A(b_A^\dagger P_A+P_A^\dagger b_A),
\qquad Q=N_f+2N_b.
\]
Die Tensoridentität liefert auf dem endlichen Teilchenkern
\[
[K_h,H_W]=0,\qquad [K_h,Q]=0.
\]
Der erste Kommutator folgt direkt aus CAR/CCR: Der Transformationsbeitrag des Fermionpaars wird durch den des Bosons aufgehoben. Der Zahlterm ΔN_b kommutiert ebenfalls mit K_h. Jeder feste Q-Sektor ist endlichdimensional; die sektorweise Identität liefert die gemeinsame unitäre Implementierung ohne eine unbegründete Gleichsetzung unbeschränkter Operatordomänen.

Dieser K_h ist ein bereits im Modell vorhandener Symmetriegenerator. Er wird nicht als zusätzlicher Term in H_W eingeführt. Die D4-Clock ist also mit der nativen Wechselwirkung verträglich, ohne dass H_W geändert werden muss.

## 4. Derselbe wechselwirkende Grundzustand

Der vorhandene modellinterne Grundzustandssatz besagt für \(0<|g|/\Delta\le1/20\): Ω ist eindeutig, liegt bei Q=64 und ist Spin(10)×SU(4)-invariant. Hier wird dieser bereits dokumentierte Satz verwendet, nicht erneut durch eine vollständige Fockraumdiagonalisierung bewiesen.

Der Spurteil des äußeren Spinorlifts lässt sich abspalten:
\[
K_h=J_h+\frac{\operatorname{tr}h}{2}Q.
\]
J_h ist der gewöhnliche Spin(10)-Generator mit Spinorwirkung dΓ_even(h)−tr(h)I₁₆/2 und Vektorwirkung diag(h,−hᵀ). Für tr(h)=10 folgt daher
\[
K_h\Omega=320\Omega.
\]
Die native Grundzustandslinie bleibt unter der geometrischen Clock invariant. Das ist ein positiver Anschluss an den wechselwirkenden Zustand, nicht nur an den leeren Referenzzustand.

Ω ist allerdings kein Grundzustand dieses K_h. Bereits im selben Q=64-Sektor besitzt der Zustand mit 32 Bosonen im niedrigsten B_h-Eigenkanal den K_h-Wert 32·6=192. Ein Energieoffset oder Zusatz μQ verschiebt beide Zustände gleich und kann diese Ordnung nicht ändern. Das schließt die direkte Identifikation von K_h mit einer positiven Skalierung des nativen Grundzustands-Hamiltonoperators aus; es schließt keine allgemeinere Quellenrekonstruktion aus.

## 5. Exakter Transport der geladenen Antwort

Weil K_h und H_W kommutieren und [K_h,f]=−A_hf gilt, erhält man für eine ausdrücklich als Rahmenvergleich verwendete Familie
\[
f_{H_W+\omega K_h}(t)=e^{-i\omega A_ht}f_{H_W}(t).
\]
Hierdurch wird keine neue physische Kopplung ω ausgewählt oder postuliert. Die Formel beschreibt, wie die gleiche native Bewegung in einem mitrotierenden inneren Rahmen erscheint. Ω ist für beide Entwicklungen stationär; daraus folgt für beliebiges ω nicht, dass Ω auch Grundzustand des verschobenen Generators bleibt.

Wegen der inneren Symmetrie ist die ursprüngliche CAR-Antikommutatorantwort auf Ω von der Form C_H(t)=c(t)I₆₄. Der transportierte Ausdruck lautet deshalb
\[
C_{H+\omega K}(t)=c(t)e^{-i\omega A_ht}.
\]
Alle Observablen, die mit K_h kommutieren, haben exakt dieselbe Entwicklung. Geladene Felder tragen die explizite zusätzliche Clockphase. Diese globale innere Rahmenwirkung ist noch keine hergeleitete lokale Eichverbindung oder Gauss-Dynamik.

## 6. Warum die reine RR-Clock die wechselwirkende Antwort nicht ersetzt

Die vorhandene native Antwortrechnung liefert auf demselben Ω
\[
m_0=I,\qquad m_1=0,\qquad
m_2=g^2\left(15-\frac7{32}\langle N_b\rangle\right)I.
\]
Bei g≠0 ist das zweite Moment positiv. Dafür ist nicht einmal die schärfere numerische Grundzustandsschranke nötig: Q=64 impliziert 0≤⟨N_b⟩≤32, also S≥8 und m₂≥8g²I. Bei der bereits zertifizierten Kopplung |g|/Δ=1/20 gilt zusätzlich 0.842846<⟨N_b⟩<1.245656.

Eine rein lineare CAR-Zeit mit hermiteschem Einteilchengenerator A besitzt dagegen m₁=A und m₂=A². Schon die ersten beiden nichttrivialen Momente verhindern daher eine Gleichsetzung: m₁=0 würde A=0 erzwingen, und damit m₂=0. Dieser Widerspruch gilt auch nach einem Einheitsbasiswechsel, einer Skalierung oder einem zunächst frei erlaubten skalaren Offset, sobald die gleichen geladenen Momente gefordert werden.

Das ist ein Vergleich der vollständigen kanonischen 64-Feld-Antikommutatorantwort mit einer geschlossenen linearen Entwicklung auf genau diesen Feldern. Er verbietet weder eine nichtlineare Feldabbildung noch eine größere lineare Darstellung mit zusätzlich nachgewiesenen Feldern und deren Projektion. Der native Operator [H_W,f]=−gD mit D∼bf† zeigt bereits, wo die reine lineare Schließung verlassen wird.

## 7. Die Clock trägt die ganze native Antwortkette mit

Die existierende Rechnung im Contract `universalraum-native-ground-response-20260915`, Abschnitt 7, ordnet dieselbe Antwort bereits durch f, D/√S und weitere native Kompositoperatoren:
\[
G(z)=\frac{1}{z-\dfrac{g^2S}{z-a_1-\Sigma_2(z)}},
\qquad a_1=\Delta+7a/S,
\quad a=(\Delta\langle N_b\rangle-E_0)/64.
\]
Diese Darstellung und der Beweis Σ₂≢0 sind vorhandene Ergebnisse. Sie werden hier nicht als neue Lösung ausgegeben. Insbesondere ist die unbekannte Restantwort nicht durch eine Zwei-Linien-Näherung zu ersetzen.

Der neue Clockanschluss transportiert diese nichtlineare Struktur vollständig. Setze \(\mathcal L A=[A,H_W]\). Aus [K_h,H_W]=0 und der Jacobi-Identität folgt für jedes n≥0
\[
[K_h,\mathcal L^n f]=-A_h\mathcal L^n f.
\]
Insbesondere tragen f und D dieselbe geometrische innere Wirkung. Die Wechselwirkung erzeugt neue Kompositoperatoren, während die innere Markierung erhalten bleibt.

Im positiven Antikommutator-Antwortraum mit
\[
(A,B)_\Omega=\langle\Omega|\{A^\dagger,B\}|\Omega\rangle
\]
und Quotientierung der Nullvektoren liefert die Spin(10)×SU(4)-Invarianz
\[
(\mathcal L^m f_r,\mathcal L^n f_s)_\Omega
=\delta_{rs}\,m_{m+n}.
\]
Der von diesen Vektoren erzeugte zyklische Raum ist deshalb isometrisch ein Tensorprodukt eines 64-dimensionalen inneren Raums mit einem gemeinsamen skalaren Antwortraum. Die physische Liouville-Entwicklung wirkt dort als I₆₄⊗J; die geometrische Clock wirkt auf dem inneren Faktor. Die skalare Jacobi-Matrix J und ihre Restantwort müssen weiterhin berechnet werden. Der Raum ist für diese einzelne native Bank endlich, weil nur die endlichen Q=63- und Q=65-Sektoren beteiligt sind.

Dies ist eine exakte Ordnung der bereits vorhandenen nativen Antwort, kein ergänztes Bad und keine neue Feldspezies. Es ist auch keine Identifikation dieses Antikommutator-Antwortraums mit einer vollständigen Raumzeit-GNS-Theorie. Die positive Aussage ist eng: Die RR-Markierung bleibt entlang der gesamten wechselwirkenden Antwortkette konsistent, obwohl die tatsächliche Dynamik nicht auf den 64 linearen Fermionoperatoren schließt.

## 8. Verbleibender Quellenvertrag

Die endliche geometrische Clock und W passen gemeinsam zum nativen wechselwirkenden Zustand. Die richtige Zuordnung lautet daher zunächst: geometrische innere Clock als erhaltene Symmetrie des nativen Prozesses. Der Zeitvergleich ist damit nicht mehr ein unaufgelöster Widerspruch zwischen fünf ungleichen Moden und einem Paartensor.

Der noch fehlende Satz muss die ursprüngliche Quelle mit der nichtlinearen geladenen Antwort desselben H_W und Ω verbinden. Dazu reichen ein diskreter Clocklift, eine endliche Gram-Matrix oder eine bloß gewählte Hardy-Norm nicht. Aus der Quelle müssen die Feldabbildung, ihr Zustandsfunktional, der kontinuierliche Generator und die W-Wechselwirkung gemeinsam folgen. Das bleibt die konkret bearbeitete physische Herkunftsfrage; Alpha, Flavor, räumliche Lokalität und die übrigen T1–T8-Tore werden durch den endlichen Clockanschluss nicht automatisch geschlossen.

## Quellen, Status und Reproduktion

- Vorangegangene Herleitung: `TFPT_RR_Quellenbruecke_20260921.md` und das dortige Reproduktionspaket. Voraussetzungen: vorhandener markierter Grad-4-Divisor, äußere Spinordarstellung und erklärter endlicher Normvertrag.
- Native Tensorquelle: `experiments/theory-contracts/universalraum-v16-integrated-20260915/sources/native_tensor.npz`, SHA-256 `3f00a0892157a691e4ef26920c3702772c7bf76a250fad98ff04a079bb64b763`.
- `universalraum-native-ground-response-20260915/RESULTS.md`, Zeilen 99–109: bestehender rezertifizierter Grundzustandssatz; Zeilen 128–207: Bewegungsgleichung und Momente; Zeilen 327–382: vorhandene Resolventenordnung und nichtverschwindende Restantwort. Der ältere Contract `universalraum-native-operations-ground-response-20260915` hatte die größere Kopplung noch nicht zertifiziert; die spätere Version dokumentiert die ergänzten Schranken und Replays. Der neue Clockbeweis benötigt keine erneute Behauptung einer vollständigen Grundzustandsdiagonalisierung.
- `charged-source-time-audit-20260920/PROOF.txt`, `source-rg-clock-bridge-20260920/PROOF.txt`, `modular-source-selection-audit-20260917/RESULTS.md` und `source-local-line-20260920/SOURCE_LINE_PROOF.txt`: tatsächliche andere Zeitverträge und ihre Auswahlgrenzen. Die separate Quellenprüfung dokumentiert die genauen Stellen.
- Neuer Checker: vollständige gl(5)- und gl(4)-Basisidentitäten mit ganzzahligen Einträgen, expliziter Hardy-Generator, Normtransport und kleinster Paar/Boson-Zeitzeuge. Die allgemeine Kommutator-, Zustands- und Antwortraumargumentation steht im Text; endliche Checks allein werden nicht als formale Beweise dieser analytischen Aussagen ausgegeben.

Forschungs-ID: `UR.RR.CLOCK.01`. Verdict: **PARTIAL** für die physische Quellenfrage, **exakter bedingter endlicher Clockanschluss** für die ausgeschriebene Algebra. Die zugeordneten Tore `QGEO.KERNEL.01` und `SEAM.EQUIV.01` bleiben offen. Kein physischer Ledgerstatus oder Publikationsclaim wird hier hochgestuft.
