# Prüfung des zugesandten Ansatzes und neue Folgerungen

14. September 2026. NON-RH. Keine T1–T8-Promotion.

## Herkunft und Ergebnis

`USER_SUBMISSION.md` archiviert den vom Nutzer übermittelten Text. Die am
Ende enthaltenen ChatGPT-Anhangsverweise 7/8 liefern hier keine erreichbaren
Dateien; deren angebliche Prüfer wurden nicht eingesehen oder ausgeführt.
`check_extension.py` ist eine eigene Rekonstruktion. Die 60 Projektoren
stammen über den hash-gepinnten Adapter aus den tatsächlichen E8-Wurzeln in
`verification/v783_two_qubit_clifford.py`, Quellabschnitte P0/P1.

Bestätigt sind die Spektren, die Faktorisierung, die Präparationsabhängigkeit,
die allgemeine symmetrische Kontextfamilie und die ausdrücklich zusätzlich
gesetzte SU(4)-Vierträgerzelle. Es gibt keinen Beweis, dass die physikalische
TFPT-Quelle gerade ihre Kopplung, Stärke, Grundzustandspräparation oder
skalierbare Nachbarschaft auswählt.

## 1. Exakte Lösung der endlichen Strahlkette

C summiert die vier Ergebnisse pro Kontext. F liest die 15 hermiteschen
Pauli-Erwartungswerte der Strahlprojektoren. Direkt an den Quellmatrizen gilt

    C C^t = 4I, F F^t = 12I, C F^t = 0,
    T = (C^t B C + F^t F)/28.

Mit Pc=C^t C/4, Pf=F^t F/12, Ph=I-Pc-Pf sind die drei Sektoren orthogonal.
T hat auf Pc die zu K=B/7 äquivalente Wirkung, auf Pf den Wert 3/7 und
auf Ph den Wert null. B ist invertierbar. Deshalb

    ker T = ker(C,F), dim ker T = 30,
    T^n = C^t K^n C/4 + (3/7)^n Pf, n>=1.

Der Prüfer kontrolliert die exakten Projektoren, die Faktoren und die
ersten drei Potenzen; die Formel für alle n folgt durch Induktion aus
den orthogonalen Sektoren. Spektrum:
1[1], 3/7[15], 2/7[9], -2/7[5], 0[30].
Ein ganzzahliges annihilierendes Polynom von 14T plus ganzzahlige
Spurmomente bestimmt unabhängig alle Vielfachheiten. Symmetrie garantiert
Diagonalisierbarkeit. Kein numerischer Eigenwertfit wird benutzt.

Die 30 Nullrichtungen sind kein innerhalb T fortbestehendes Gedächtnis.
Die kohärenten Register der früheren Konstruktion sind ein anderer Raum.

## 2. Gesamte Kontextfamilie und Auswahlgrenze

Unter voller symplektischer Kontextsymmetrie gibt es drei Paarorbits:
identisch, ein gemeinsamer Pauli, disjunkt. Dies folgt durch Erweiterung
angepasster symplektischer Basen; Schnittdimensionen 2/1/0 klassifizieren
die Paare maximal isotroper Ebenen. Die jeweilige Ausgangsvalenz ist 1/6/8.
Gesamtmassen a,b,c>=0 mit a+b+c=1 ergeben

    Kabc = aI + b(B-I)/6 + c(J-B)/8,
    Tabc = C^t Kabc C/4 + (a+b/3) Pf + (a-b/6) Ph.

Die Formel wird exakt auf allen drei Extrempunkten geprüft und gilt durch
Linearität auf dem ganzen Simplex. Die fünf Spektralbänder sind

    1[1], (a+b/3)[15], (a+b/6-c/4)[9],
    (a-b/2+c/4)[5], (a-b/6)[30].

Bei Eigenwertgleichheiten addieren sich Vielfachheiten; die gemeinsamen
Sektorprojektoren bleiben gültig. Die Forderungen c=0 und a-b/6=0
wählen a=1/7,b=6/7. Maximierung der Shannon-Entropie der sieben einzelnen
zulässigen Übergänge wählt dieselbe Verteilung. Die Entropie der drei
Orbitmassen allein zu maximieren wäre ein anderes Auswahlproblem.
Keine dieser Forderungen wird hier aus der physikalischen Quelle abgeleitet.

## 3. Neue Mehrschritt-Präzisierung der CQ-Ausführung

Im gemeinsamen klassisch-quantenmechanischen Raum gelten

    sigma'_D = sum_C K_DC Delta_D(sigma_C).

In Pauli-Koordinaten zerfällt die 240-dimensionale lineare Abbildung M in
einen Block K für die Identität und 15 Blöcke D_v K. D_v projiziert auf
die drei Kontexte, welche v enthalten. Die drei sind paarweise benachbart.
Daher hat jeder solche Block Rang 3, sein Quadrat Rang 1 und

    (D_v K)^3 = (3/7)(D_v K)^2.

Damit sind die Ränge von I,M,M²,M³ genau 240,60,30,30.
Neu daraus bestimmt: Der Nullanteil hat 30 Jordanblöcke der Größe 2 und
150 der Größe 1. Die größere CQ-Ausführung hat also echte zweischrittige
Transiente; T selbst ist dagegen symmetrisch und hat keine Jordanblöcke
der Größe 2. Beide Nullräume sind nicht gleichzusetzen.

Bei unabhängiger Anfangspräparation sigma_C=rho/15 und anschließend
fortgeführtem Kontext lautet der beobachtete Kanal für n>=1

    rho_n = I4/4 + (1/5)(3/7)^(n-1) (rho-I4/4).

Wird der Kontext stattdessen VOR JEDEM Schritt neu unabhängig und
gleichverteilt gesetzt, ist der Faktor (1/5)^n. Im zweiten Schritt sind
das 3/35 beziehungsweise 1/25. Die im Strahlmodell bereits passende
Kontext/System-Präparation liefert dagegen (3/7)^n. Diese drei Experimente
werden im Paper getrennt beschrieben.

Eine positive affine Rechtsinverse E:Raysimplex->Stabilizerpolytop kann
nicht existieren: Jeder extreme reine Strahl müsste auf sein einziges
Delta-Maß zurückgeführt werden. Affinität würde dann I4/4 für jeden der
15 Kontexte auf dessen andere Vierer-Gleichverteilung zurückführen. Das
ist widersprüchlich. Die bloße Mehrdeutigkeit von Zerlegungen wäre allein
noch kein Beweis; der Extrempunkt-/Affinitätsschritt ist entscheidend.

## 4. Vierträgerzelle: bestätigte Konstruktion

Zusätzlicher Hamiltonoperator auf (C4)^tensor4:

    H = J sum_(i<j) (I+Sij)/2, J>0.

Jeder Summand ist positiv. Gemeinsame Nullenergie verlangt Antisymmetrie
unter allen Transpositionen. Der Nullraum ist Lambda4 C4, also eindimensional.
Omega ist die signierte Summe aller 24 Permutationen von (0,1,2,3)/sqrt24.
Exaktes Spektrum H/J: 0[1],2[45],3[40],4[135],6[35]. Gap 2J.
Die vollständigen Spektralprojektoren sind Lagrange-Polynome von H/J;
damit ist exp(-itH/hbar) für vorgegebene t,J vollständig bestimmt.

Alle Einträgermarginalen sind I4/4, alle Paarmarginalen (I-S)/12.
Schon die sechs Paar-Erwartungen der positiven Energieprojektoren
identifizieren den Zustand bei Nullenergie. Robust gilt für jeden Zustand

    1 - <Omega|rho|Omega> <= Tr(rho H)/(2J).

Das sind eine Zustandscharakterisierung und ein Test, kein automatisches
Präparationsverfahren. Die unitäre stationäre Operatoralgebra hat Dimension
1²+45²+40²+135²+35² = 23076, nicht 1. Energieeigenzustände außerhalb des
Grundzustands bleiben stationär; Unitarität erzeugt keinen Attraktor.

## 5. Neue konkrete Anschlüsse und ihre Grenzen

An den tatsächlichen 16 Pauli-Matrizen des Quellträgers ist geprüft:

    Sij = (1/4) sum_(v=0..15) P_v^(i) tensor P_v^(j).

Der neue Hamiltonoperator besitzt somit eine kurze bilineare Darstellung
in vorhandenen Einzeloperatoren. Die zusätzliche Annahme ist ihre gemeinsame
Hamiltonkopplung; ein Mittel von Quantengattern ist nicht dieser Generator.
Diese algebraische Darstellung legt J, dessen Vorzeichen oder eine physische
Zustandspräparation nicht fest.

Unter 0,1,2,3 <-> 00,01,10,11 und einer festen Modenordnung liegt Omega
im Vier-Teilchen-Sektor der acht komplexen Fermionenmoden. Der Prüfer
konstruiert die Jordan-Wigner-Operatoren, prüft beide CAR-Relationen und
erhält die Einteilchendichte I8/2. Omega ist kein Slaterzustand und hat
24 statt einer Zweierpotenz an nichtverschwindenden Qubit-Amplituden;
er ist kein reiner Stabilizerzustand in dieser Kodierung.

Neu geprüft: H erhält diese Gesamtteilchenzahl. Seine Restriktion auf den
70-dimensionalen Sektor hat das Spektrum

    H|N=4 / J: 0[1],2[15],3[12],4[33],6[9].

Dies definiert einen neuen H70, nicht eine Gleichsetzung mit einem früheren
TFPT-H70-Quelloperator. Dafür wäre ein markierungstreuer Intertwiner nötig.
Ein gewöhnlicher Qubit-Blocktausch ist außerdem nicht ohne Beachtung der
Jordan-Wigner-Vorzeichen ein fermionischer Modentausch.

Für jede kollektive Viereroperation A gilt A^tensor4 Omega=det(A)Omega.
Ein kollektiver unitärer Compiler-Clock-Lift verändert den Grundzustands-
Dichteoperator daher nicht. Der vorhandene globale Clock-Takt wird aus
diesem Singulett allein nicht als zeitabhängiges Signal ausgelesen.

## 6. Neue skalierbare Zwischenfrage: zwei Zellen

Zwei voneinander unabhängige Tetramerzellen haben H0=HA+HB, eindeutigen
Produktgrundzustand und Gap 2J. Verbinde genau ein Trägerpaar zwischen
ihnen mit V=lambda (I+S)/2, lambda>=0. Im Produktzustand ist die Zweiträger-
Dichte I16/16, daher

    <V> = 5 lambda/8, Var(V)=15 lambda²/64.

Für lambda>0 ist der Produktzustand deshalb kein Eigenzustand des gekoppelten
Systems. Seine Varianz bezüglich H0+V ist dieselbe, weil H0 ihn annihiliert.
Positivität und Min-Max-Prinzip geben E1(H0+V)>=2J, während der Produktzustand
als Variationszustand E0<=5 lambda/8 liefert. Also

    gap >= 2J - 5 lambda/8 > 0 für 0<=lambda<16J/5.

In diesem Intervall ist der gekoppelte Grundzustand eindeutig. Für lambda>0
ist seine Energie strikt positiv: Der zusammenhängende Achtträgergraph
würde für gemeinsame Nullenergie Lambda8 C4 verlangen, das null ist.
Das bestätigt die Nullenergie-Skalierungsschranke des Zusenders, beweist aber
zugleich, dass schwache Kopplung zweier Zellen die Eindeutigkeit nicht sofort
zerstört. Kein 65536-dimensionaler Diagonalisierungslauf wird behauptet;
dies ist eine analytische Operatorabschätzung mit exakt geprüften lokalen
Erwartungen. Für viele Zellen oder einen Kontinuumsgrenzwert ist die
Abschätzung noch kein uniformer thermodynamischer Satz.

## 7. Alpha-Eindeutigkeit und gemeinsamer Inflationstest

Für die feste Alpha-Gleichung sei F(alpha)=alpha³-2c3³ alpha²-Cg(alpha),
C=(4/5)41c3^6 und g=-log(phi_s). Betrachte F(alpha)/alpha². Seine Ableitung ist

    1 + C (2g-alpha g') / alpha³.

Für alpha>0: q=d exp(-2alpha), d=48c3^4<1/6000, phi_s=1/(6pi)+f(q),
f(q)=q(1-q)^(-5/4). Mit 3<pi<10/3 gilt 1/20<phi_s<1/16, daher g>log16>2.
Ferner f'(q)=(1+q/4)(1-q)^(-9/4)<4; folglich g'<160q und
alpha g'<80d<1/50, da alpha exp(-2alpha)<=1/(2e)<1/2.
Damit ist die Ableitung strikt positiv. Der Quotient geht bei alpha->0+
gegen -unendlich und bei alpha->unendlich gegen +unendlich. Genau eine
positive einfache Nullstelle folgt. Die rationalen groben Schranken werden
zusätzlich geprüft; dies bleibt ein Satz zur gesetzten Gleichung, nicht
deren physikalische Identifikation.

Aus ns=1-2/N, r=12/N², As=N²c3^7/(24pi²) folgen exakt

    r=3(1-ns)², As(1-ns)²=c3^7/(6pi²).

Eine Kalibrierung auf As=2.10e-9 ergibt N innerhalb 50..60, nicht einen
Widerspruch zum ganzen Intervall. Dieser As-Wert ist dann Input; ns und r
sind bedingte Ausgaben. Zahlen stehen in verification.json. Die frühere
Aussage über die zu kleine Amplitude bei genau N=51.4 bleibt richtig.

## Reproduktion

`/opt/homebrew/bin/python3 -B experiments/theory-contracts/compiler-extension-audit-20260914/run_checks.py`

Der Runner vergleicht normale und optimierte Ausgabe und führt sechs eng
begrenzte In-Memory-Mutationen aus. Quellcode wird weder für Mutanten noch
für das Quellpräfix verändert. Ergebnisse: verification.json und replay.json.

PDF-Version 1.1 wird mit `TFPT_PAPER_DATE=2026-09-14` vor den bestehenden
paper_checks.py-, build_paper.py- und paper_layout_check.py-Befehlen erzeugt.
Die alte PDF- und Markdown-Version bleibt erhalten.

Primärliteratur zum Hintergrund, nicht als Beleg für neue TFPT-Herkunft:

- Pollock et al., Operational Markov condition for quantum processes,
  https://arxiv.org/abs/1801.09811 .
- Miyazaki et al., Linear Flavor-Wave Analysis of SU(4)-Symmetric Tetramer
  Model with Population Imbalance, https://arxiv.org/abs/2205.11155 .
- Aaronson/Gottesman, Improved Simulation of Stabilizer Circuits,
  https://arxiv.org/abs/quant-ph/0406196 .
