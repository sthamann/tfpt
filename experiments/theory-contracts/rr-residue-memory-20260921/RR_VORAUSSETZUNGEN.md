# TFPT: Die 3+2-Markierung aus derselben Vierpunktgeometrie

**21. September 2026 — Forschungsfortsetzung.**

Unter der bereits vorhandenen Voraussetzung der markierten Vierpunktgeometrie lässt sich ein konkreter bisher nicht ausgeschriebener Schritt liefern: Die Halbwendung ihrer Vierteldrehung wählt im Riemann–Roch-Träger die 3+2-Zerlegung. Eine neue, frei gewählte innere Involution ist dafür nicht nötig. Die zugehörigen Hyperladungsräume und der Halbspinor lassen sich explizit ausrechnen. Auch die geometrische D4-Wirkung lässt sich mit dem unveränderten nativen W-Tensor exakt verbinden; ein Familien-Hodge-Basiswechsel absorbiert ihren Determinantencharakter.

Eine vollständige physische TFPT-Lösung ist damit nicht bewiesen. Der anschließende Versuch, diese fünf geometrischen Moden mit Moden der ursprünglichen Quantenquelle zu identifizieren, muss Norm, Zeitentwicklung, Lokalität und innere Symmetriewirkung gleichzeitig erhalten. Hier liefert die Rechnung einen präzisen Unterschied zwischen einer gültigen endlichen Modeneinbettung und der weiterhin fehlenden physischen Feldherleitung.

## 1. Ausgangspunkt aus den Originalquellen

Die Quelle verwendet bereits
\[
D=\mu_4=\{1,i,-1,-i\}\subset\mathbb P^1,
\qquad E=H^0(\mathbb P^1,\mathcal O(D)).
\]
Riemann–Roch ergibt dim E=5. Das ist in `ARCH.RRCAR.01`/v189 dokumentiert. Die anschließende Konstruktion
\[
S^+=\Lambda^{\rm even}E,\qquad\dim S^+=1+10+5=16,
\]
steht in `ARCH.RRCAR.02`/v197. Beide Originaleinträge unterscheiden ausdrücklich die geometrische Konstruktion von ihrer physischen Identifikation mit dem Carrier.

Auch der Bündeltyp passt bereits zum vorhandenen Anker: Für
\[
\mathcal A=\mathcal O(-2)\oplus\mathcal O(-1)^2
\]
ist \(\det(\mathcal A)^*\cong\mathcal O(4)\). Das gibt dieselbe holomorphe Bündelklasse wie \(\mathcal O(D)\). Die Bündelklasse allein liefert noch keine physische Hermitesche Metrik, Verbindung oder Einbettung in den Raw-RP-Zustand. Außerdem sind diese geometrische Determinantenlinie und die endliche Linie det E verschiedene Objekte.

Die nachfolgende Rechnung setzt diese markierte Geometrie voraus. Sie leitet nicht die Vierpunktgeometrie aus einer voraussetzungslosen Quelle ab und umgeht nicht `QGEO.KERNEL.01` oder `SEAM.EQUIV.01`.

## 2. Die innere 3+2-Involution ist jetzt explizit

Setze P(z)=z⁴−1. Eine Basis von E ist
\[
e_n(z)=\frac{z^n}{P(z)},\qquad n=0,1,2,3,4.
\]
Die Funktionen haben höchstens einfache Pole an D und sind bei Unendlich regulär. Die konstante Funktion ist e₄−e₀.

Für die geometrischen Pullbacks
\[
(Rf)(z)=f(iz),\qquad(Sf)(z)=f(1/z)
\]
folgt unmittelbar
\[
R=\operatorname{diag}(1,i,-1,-i,1),
\qquad Se_n=-e_{4-n}.
\]
Damit gelten R⁴=I, S²=I und SRS=R⁻¹. Insbesondere liegt R² im Zentrum dieser Diederwirkung.

Die Operatoren
\[
P_c=\frac{I+R^2}{2},\qquad P_w=\frac{I-R^2}{2}
\]
sind komplementäre Projektoren mit
\[
\operatorname{rank}P_c=3,\qquad\operatorname{rank}P_w=2.
\]
Konkret liegen e₀,e₂,e₄ im Dreierraum, e₁,e₃ im Zweierraum. Beide Räume werden von R und S erhalten.

**Der präzise positive Satz:** Auf dem vorhandenen markierten RR-Träger ist die Zerlegung 3+2 durch die zentrale Halbwendung ausgewählt. Dieser Operator ist weder die Einschränkung einer bereits positiv projizierten Zustandsinvolution noch die reine CAR-Polarisation. Die früheren Ausschlüsse dieser beiden Gleichsetzungen treffen diese Konstruktion deshalb nicht.

Mit der bisherigen TFPT-Vorzeichenkonvention lautet die innere Involution εint=−R². Die Zahl 3 allein wird dabei nicht mit dem Familienraum gleichgesetzt: Der Dreierraum E_c trägt unter R die Eigenwerte (1,−1,1); die drei nichttrivialen Familiencharaktere tragen (i,−1,−i). Ihre Gruppenwirkungen unterscheiden sich.

## 3. Der vorhandene Hyperladungsoperator folgt auf diesem Träger

Die traceless Ladungsverteilung auf beiden Blöcken erfüllt 3y_c+2y_w=0. Mit der üblichen, bereits im Compiler benutzten Normierung y_w=1/2 folgt
\[
Y=-\frac13P_c+\frac12P_w
=\frac{I+5\varepsilon_{\rm int}}{12}.
\]
Die Normierung und die Ladungskonjugationskonvention werden also benannt; sie werden nicht durch einen bloßen Projektorrang physisch bestimmt.

Auf Λeven E addieren sich die Ladungen der besetzten Plätze:

| Typ | Multiplizität | Y |
|---|---:|---:|
| νᶜ | 1 | 0 |
| Q | 6 | 1/6 |
| uᶜ | 3 | −2/3 |
| eᶜ | 1 | 1 |
| dᶜ | 3 | 1/3 |
| L | 2 | −1/2 |

Außerdem gelten tr_E(Y)=0, tr_E(Y²)=5/6 und, für den üblich normierten schwachen T₃, tr_E(T₃²)=1/2. Daraus folgt kY=5/3.

Diese Ladungstabelle war im TFPT-Compiler bereits vorhanden. Der zusätzliche Zusammenhang ist ihre explizite Anbindung an die wirkliche Halbwendung des RR-Raums. Aus den endlichen inneren Transformationen folgen noch keine lokalen Eichfelder oder ihre Wechselwirkung. Auch die kontinuierliche Gruppe SU(3)×SU(2) ist nicht schon aus einer endlichen D4-Wirkung als physische Eichgruppe hergeleitet.

### 3.1 Der Anschluss an alle 480 nativen W-Kopplungen

Verwende den vorhandenen Viermarkenraum F₄ und seine tatsächliche Permutationswirkung P₄. Dann trägt der Fermionraum die Wirkung
\[
U_{64}(g)=\Gamma_{\mathrm{even}}(g_E)\otimes P_4(g).
\]
Für beide Erzeuger R und S erfüllt der gepinnte Archivtensor exakt
\[
W\Lambda^2U_{64}(g)=
\left[\det(g_E)\operatorname{diag}(g_E,g_E^{-T})
\otimes\Lambda^2P_4(g)\right]W.
\]
Die Determinantenlinie ist durch die Spinorpaarung vorgegeben. Im unveränderten Archiv darf ihr Charakter nicht weggelassen werden: Mit ihm stimmen alle 480 getragenen Koeffizienten überein; ohne ihn haben alle 480 das falsche Vorzeichen. Verglichen wurden je Erzeuger sämtliche 120.960 Matrixeinträge. Alle 480 Kopplungen erhalten außerdem die angegebene Hyperladung.

Es gibt jedoch eine konkrete Beseitigung des Twists durch einen Basiswechsel. Auf Λ²F₄ sei K die signierte Komplementabbildung, beispielsweise K(01)=23, K(02)=−13, K(03)=12 und entsprechend rückwärts. Dann gelten K²=I und
\[
K\Lambda^2P_4=\det(P_4)\Lambda^2P_4K.
\]
Für die tatsächlichen Drehungs- und Spiegelungspermutationen ist det(P₄)=det(g_E)=−1. Daher erfüllt
\[
W^\sharp=(I_{10}\otimes K)W
\]
die unverdrehte Kovarianz
\[
W^\sharp\Lambda^2U_{64}(g)=
\left[\operatorname{diag}(g_E,g_E^{-T})\otimes\Lambda^2P_4(g)\right]W^\sharp.
\]
Auch diese Gleichheit wurde an sämtlichen Einträgen exakt geprüft. Es werden keine Moden oder Wechselwirkungsparameter ergänzt; der Bosonenraum erhält eine andere orthonormale Basis. Die Normierung WW†=8I bleibt erhalten.

**Dabei müssen die Ladungsoperatoren mittransformiert werden.** K lässt die fünf Träger-Cartanmarkierungen und Y unverändert, kehrt aber die drei SU(4)-Cartanmarkierungen im Sechserraum um. Unter vollständig komplexem SU(4) entspricht die transportierte Wirkung der kontragradienten Wirkung. Mittransportiert stimmen alle 480 Ladungsbedingungen; bei unveränderten Familienladungen scheitern alle 480. Die Hodge-Abbildung vertauscht also keine Ladungen heimlich.

Damit ist der endliche D4-kovariante Anschluss RR → Spinor/Familie → W konstruiert. Der frühere engere Gedanke, den Charakter nur durch eine skalare Familienphase zu entfernen, scheitert zwar an D4ᵃᵇ=C₂×C₂. Daraus folgt aber kein Verbot des hier ausgeschriebenen nichtskalaren Basiswechsels und keine Notwendigkeit einer neuen projektiven Erweiterung.

## 4. Der erste analytische Test: Sind das zulässige Quellenmoden?

### 4.1 Wörtliche Einbettung als ungewichtete Randfunktionen

In einem skalaren Rand-CAR-Modell mit Einteilchennorm L²(S¹,dθ) ist eine einfache Polfunktion an a∈D nicht normierbar:
\[
f(e^{i\theta})\sim\frac{c}{\theta-\theta_a}
\quad\Rightarrow\quad
\int|f|^2d\theta=\infty.
\]
Verschiedene Pole können diese lokale Divergenz nicht gegeneinander aufheben. Werden alle Pole entfernbar, bleibt eine global holomorphe Funktion auf der Sphäre, also eine Konstante. Folglich
\[
E\cap L^2(S^1)=\mathbb C\cdot1.
\]
**Die wörtliche Zuordnung „dieselben fünf meromorphen Funktionen sind fünf ungewichtete CAR-Schmierfunktionen“ scheitert.** Das ist ein Test dieses bestimmten, skalaren Normvertrags. Er schließt andere Bündelmetriken oder eine aus der vollständigen Quelle hergeleitete Feldabbildung nicht aus.

Der vorhandene lokale Quellen-Grenzwert benutzt ausdrücklich normierte L²-Schmierfunktionen, nicht unnormierbare Polfunktionen. Er betrifft eine erklärte Ein-Kopien-Quelle und behauptet seinerseits keine Herleitung dieser Quelle aus dem abstrakten P1-Datum. Diese Beweisgrenzen werden hier beibehalten.

### 4.2 Eine explizite, konsistente Einbettung existiert mit erklärter Bündelmetrik

Definiert man die Randmetrik
\[
\langle f,g\rangle_D=
\int_{S^1}|P(z)|^2\overline{f(z)}g(z)\frac{d\theta}{2\pi},
\]
dann ist
\[
J:E\longrightarrow H^2(S^1),\qquad Jf=P f
\]
eine Isometrie auf den Raum der fünf orthonormalen Fouriermoden 1,z,z²,z³,z⁴. Diese Metrik ist unter den angegebenen R- und S-Wirkungen invariant. Als Metrik einer Divisorlinie ist sie konsistent; sie ist hier ausdrücklich Bestandteil des Einbettungsvertrags. Der vollständige P1-Kernel wurde dadurch nicht rekonstruiert.

Auch die Zeit wird dabei vollständig mittransportiert. Für den chiralen Generator Dθ=−i∂θ=z∂z gilt
\[
J^{-1}D_\theta J
=z\partial_z+\frac{zP'(z)}{P(z)}
=z\partial_z+\frac{4z^4}{z^4-1}.
\]
Der Verbindungsterm darf nicht weggelassen werden. Auf e_n hat der transportierte Generator Eigenwert n.

Die Normkonventionen müssen dabei auseinandergehalten werden. Der W-Test verwendet die D4-angepasste Basis [1,e₀+1/2,e₂,e₁,e₃] mit deklarierter Einheitsmetrik. Die oben gewählte Hardy-Norm besitzt in genau dieser unnormalisierten Basis dagegen die Gram-Matrix diag(2,1/2,1,1,1). Durch Normalisieren erhält man die orthonormalen Bildfunktionen (z⁴−1)/√2, (z⁴+1)/√2, z², z, z³. Dieser Basisabgleich ist explizit möglich, wählt aber keine physische Norm aus P1 aus. Der Generator hat dann im ersten Zweierblock die Matrix [[2,2],[2,2]] und ansonsten die Einträge 2,1,3; sein Spektrum bleibt 0,1,2,3,4. Allgemein lässt die D4-Wirkung allein vier unabhängige positive Metrikgewichte offen.

**Damit ist ein echter endlicher Modenanschluss konstruiert. Er besitzt aber die Energien 0,1,2,3,4.** Diese fünf Fouriermoden einer Spezies sind noch keine fünf inneren Komponenten bei derselben Raumzeitkoordinate.

Der kleinste Symmetrietest ist ein Generator T₀₂, der die beiden als Farbe markierten Moden e₀ und e₂ mischt. Mit H_E=diag(0,1,2,3,4) gilt
\[
[H_E,T_{02}]\ne0.
\]
Der feste skalare Quellen-Hamiltonoperator hat also nicht die volle als innere stationäre Symmetrie verlangte SU(3)-Wirkung auf diesem Dreierraum. Ein gemeinsamer Energieoffset ändert daran nichts. Das ist kein Verbot einer dynamischen Eichverbindung oder eines mittransformierten Hintergrunds; eine solche zusätzliche Struktur muss jedoch wirklich aus der Quelle vorliegen.

Auf Λeven E sind auch die induzierten Energien nicht konstant: Ihre Werte reichen von 0 bis 10. Derselbe Operatortransport ergibt deshalb nicht automatisch den nativen W-Hamiltonoperator. Dessen ursprünglicher Q=1-Sektor über dem leeren Referenzzustand ist dagegen vollständig stationär. Diese Gegenüberstellung betrifft eine direkte zustands- und zeiterhaltende Modenidentifikation; sie entscheidet keine nichtlineare Rekonstruktion über dem wechselwirkenden Grundzustand.

### 4.3 Warum Pole nur abzurunden den fehlenden Grenzwert nicht beweist

Für a∈μ₄ und 0<r<1 betrachte als präzise Diagnose die normierten Hardy-Kerne
\[
\kappa_{a,r}(z)=\frac{\sqrt{1-r^2}}{1-r\bar a z}.
\]
Mit q=r² ist ihre Gram-Matrix
\[
K_{ab}(q)=\frac{1-q}{1-q a\bar b},
\]
mit den vier positiven Eigenwerten
\[
\lambda_k=\frac{4q^k}{1+q+q^2+q^3},\qquad k=0,1,2,3.
\]
Die Gram-Matrix tendiert zwar zu I₄. Jeder einzelne normierte Vektor konvergiert aber nur schwach gegen null und hat keinen starken Grenzvektor der Norm eins. Sein Energieerwartungswert ist
\[
\langle D_\theta\rangle=\frac{q}{1-q}\longrightarrow\infty.
\]
Eine schöne endliche Grenz-Gram-Matrix beweist daher noch keinen endlichenergetischen Quellenraum. Diese Familie dient nur dem entscheidenden Grenzwerttest; sie wird nicht als neues physisches Modell verwendet. Insbesondere wird ihre endliche Regularisierung nicht stillschweigend als voll D4-kovariantes Quellensystem ausgegeben.

## 5. Was dadurch am Gesamtweg präziser wird

Der nun ausgeschriebene positive Teil lautet
\[
(\mathbb P^1,\mu_4)
\longrightarrow(E,R,S)
\longrightarrow\varepsilon_{\rm int},\ 3+2,\ Y
\longrightarrow\Lambda^{\rm even}E\otimes F_4
\overset{W}{\longrightarrow}B_{60}.
\]
Er verbindet tatsächliche Gruppenwirkungen, nicht nur Dimensionen. Die reine CAR-Polarisation muss die innere 3+2-Involution dafür nicht mehr liefern.

Der erste physische Auswahlpunkt liegt anschließend in der **gemeinsamen Feldabbildung einschließlich Metrik, Verbindung, Zustand und Zeit**. Der explizite gewichtete Anschluss zeigt sowohl eine konsistente mathematische Möglichkeit als auch ihren tatsächlichen Operatorinhalt. Er ersetzt diese Auswahl nicht durch ein frei angepasstes Ergebnis.

Der endliche Paaroperator W ist in dieser Kette jetzt wirklich mit der geometrischen Wirkung verbunden. Eine vollständige Lösung müsste denselben Anschluss als lokale Feldabbildung einschließlich des wechselwirkenden Zustands und derselben Zeit realisieren und mit dem geladenen Sektor, den Compiler-Clocks, der Detline-/Wardantwort sowie Alpha und Flavor verbinden. Zusätzlich bleiben die räumliche lokale Komposition, der chirale vierdimensionale Anschluss, der Kontinuumsgrenzwert, Quantengravitation und der kosmologische Zustand zu beweisen. Der endliche kovariante Satz ist dafür eine relevante strukturelle Brücke, kein Abschluss dieser physischen Tore.

## 6. Begrenzter Gegencheck gegen eine falsche Feldidentifikation

Die früher dokumentierte Grenze bleibt bestehen: Im markierten E8-Level-1-Netz haben die (16,4)-Komponenten Gewicht 5/8+3/8=1 und sind bosonische Ströme. Sie sind nicht 64 freie komplexe chirale CAR-Felder. Solche freien Felder hätten c=64 und induzierten auf den angegebenen inneren Faktoren Level 16 statt 1. Eine gemeinsame freie lokale Feldidentität mit demselben Stress kann deshalb nicht angenommen werden.

Das ist eine Schärfung einer bereits im `modular-source-selection-audit-20260917` dokumentierten Grenze, keine neue Widerlegung der nativen endlichen Fockalgebra. Für den CFT-Rahmen siehe die [Klassifikation chiraler fermionischer Theorien](https://arxiv.org/html/2303.16917v2#S5.SS1). Die neue RR-Konstruktion umgeht diesen Unterschied nicht und behauptet das auch nicht.

## Quellen und Reproduktion

- `origin_theory.tex`, Zeilen 89–104: gemeinsamer Divisor, RR-Träger, Cliffordkette und physische Identifikationsgrenze.
- `tfpt_research_contracts.tex`, ab Zeile 208: Ankerbündel, Vierpunktwirkung und logarithmische Formen; ab Zeile 1648: Quellen-/Geometrieidentifikation.
- `verification/v189_riemann_roch_carrier.py`, `verification/v197_rr_carrier_clifford_d5.py`: bereits vorhandene Dimensions-/Cliffordresultate und ausdrücklich bedingte physische Lesart.
- `experiments/theory-contracts/raw-carrier-origin-gate-20260920/PROOF.txt`: frühere Polarisationstests, hier mit anderer innerer Involution respektiert.
- `experiments/theory-contracts/source-local-line-20260920/SOURCE_LINE_PROOF.txt`: tatsächlicher L²-Schmier- und Zeitvertrag der erklärten Ein-Kopien-Quelle.
- `rr_source_certificate.py`: exakte D4-Matrizen, Projektoren, Ladungen, mittransportierter Generator und rationaler Hardy-Gram-Test. Normaler und optimierter Lauf liefern bytegleiche Ergebnisse. Die unendlichen Norm-/Grenzwertaussagen folgen aus den angegebenen analytischen Beweisen, nicht aus einer endlichen Stichprobe.
- `RR_W_CHECK.py`: gepinnter Tensor, beide D4-Erzeuger, volle W-Kovarianz, Hodge-Transport und sämtliche getragenen Hyperladungs-/Cartanbedingungen. Enthalten im begleitenden Reproduktionspaket.

Kein physischer Ledgerstatus wurde hochgestuft. Es wurde weder die vollständige Theorie bewiesen noch ihre Unmöglichkeit gezeigt.
