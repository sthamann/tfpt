# Zusatzreview der revidierten Fable-Theoreme 2–4

10. September 2026. Zielstand: `PROOF.md`, SHA256 **a3036e97420699cc19e5076dbf038c5f6252d1a04168c1764d089576ea00d692**, 12.600 Bytes. Ein unveränderter lokaler Snapshot liegt separat unter `fable-zusatz-original/`. Dieser Zusatz ergänzt `REVIEW-FABLE-DYNAMIK.md`; er ersetzt oder ändert dessen ältere Quellenpins nicht. Gelesen wurden die neuen Theoreme 2–4 und ihre zugehörigen Schlussfolgerungen. Kein hoher Dressing-Lauf, keine Zertifizierung der neuen Iteration-2-Zahlen. Der zuvor identifizierte LL2-Fehler wird im neuen Text ausdrücklich korrigiert; die hier geprüften Scope-Fragen bestehen davon unabhängig.

**Urteil:** Die neue elektrische Cap-Breathing-Formel ist exakt. Die angeblich exakte 2×2-Reduktion und ihre physischen Prozentangaben sind nicht bewiesen und widersprechen dem bereits nachgewiesenen Austritt aus genau diesem ersten Block. Der Duhamel-Vertrag benötigt die ganze Residualmatrix oder eine Kontrolle der gesamten komprimierten Trajektorie; eine einzelne anfängliche Leakage-Diagonale genügt nicht.

## 1. Theorem 2: was Duhamel tatsächlich liefert

Sei V die nach Orthogonalisierung festgelegte Isometrie, \(h=V^*HV\) und \(R=HV-Vh\). Für den selbstadjungierten vollständigen H und den endlichen Code im Definitionsbereich gilt

\[
e^{-itH}V-Ve^{-ith}
=-i\int_0^t e^{-i(t-s)H}R e^{-ish}\,ds.
\]

Folglich, für einen normierten Codevektor v,

\[
\|(e^{-itH}V-Ve^{-ith})v\|
\le\int_0^{|t|}\|R e^{-i\operatorname{sgn}(t)s h}v\|\,ds
\le |t|\|R\|.
\]

Der sichere einheitliche Fehlerkoeffizient ist \(\|R\|=\sqrt{\lambda_{\max}(R^*R)}\). Ein Tabellenwert \((R^*R)_{aa}\) beschreibt ausschließlich die anfängliche Spalte. Die Formel \(|t|\sqrt{(R^*R)_{aa}}\) gilt beispielsweise bei einem h-Eigenvektor oder mit einem gesonderten entsprechenden Trajektorienbound; bei einem nichtdiagonalen h folgt sie nicht aus der einzelnen Anfangsleakage. Aus der vollständigen exakten Gram-Matrix ist etwa auch die sichere Schranke

\[
\|R\|^2\le\max_a\sum_b|(R^*R)_{ab}|
\]

verfügbar. Die neuen offdiagonalen Leakage-Einträge dürfen also nicht ignoriert werden. Auch die Matrix h nach derselben Orthogonalisierung muss feststehen.

**Kleiner exakter Gegenzeuge zur verwendeten allgemeinen Folgerung:**

\[
H=\begin{pmatrix}0&1&0\\1&0&1\\0&1&0\end{pmatrix},
\qquad V=(e_1,e_2),\qquad
h=\begin{pmatrix}0&1\\1&0\end{pmatrix},
\qquad R=(0,e_3).
\]

Für v=e₁ im Code ist Rv=0; der beanspruchte spaltenweise Bound wäre null. Aber \(Rhv=e_3\), sodass der tatsächliche Fehler schon mit \(-t^2e_3/2\) beginnt. Bei \(t=\pi/\sqrt2\) ist sogar \(e^{-itH}e_1=-e_3\), während die komprimierte Entwicklung im Code bleibt; ihr Abstand beträgt \(\sqrt2\). Der unabhängige Prüfer kontrolliert die entsprechenden Matrixidentitäten exakt.

Die neue zweite Iteration kann nach Reproduktion einen weiteren endlichen Restfehler liefern. Zwei beobachtete Reduktionsfaktoren beweisen aber keinen Konvergenzradius, keinen festen Expansionsparameter 1/400 und keinen Nichtabbruch sämtlicher höherer Ordnungen. Corollary 1.1 über feste Materiemuster ist auf bereits gedresste, mehrere Materiesektoren enthaltende Codes nicht anwendbar. Die Minimalitäts- und Allordnungsformulierungen bleiben deshalb unbelegt. Für eine eigenständige Definition der Rekursion muss zudem bezeichnet sein, welches \(E_v\) einem bereits über mehrere diagonale Energien verteilten Vektor zugeordnet wird und wie die mitgeführten Marken nach Orthogonalisierung definiert sind.

## 2. Theorem 3: ein exakter Kopplungsblock ist keine exakte 2×2-Reduktion

Für den ursprünglichen Zwei-Plaquetten-Code J sind \(g^2=N/96\) und \(\eta=\Gamma/g\) exakt. Mit \(V_1=(J,\eta)\) gilt die genaue **Kompression**

\[
V_1^*HV_1=
\begin{pmatrix}h_0&gI\\gI&h_1\end{pmatrix}.
\]

Dies ist ein 32-dimensionaler Block und kein bewiesener autonomer Zweiniveauraum. Im unveränderten Source-Parent liefert `tfpt/ERWEITERUNG.md`

\[
h_1=h_0+(4+\kappa/2-11c)I-\frac{2c}{3N}K,
\qquad
R_1=(I-V_1V_1^*)H\eta\ne0,
\]

\[
R_1^*R_1\ge\frac1{24}I+G_2>0,
\quad
G_2=b^2\left[(12N-22)I-\frac4{3N}K\right].
\]

Hier sind K der ausdrücklich definierte komprimierte offene Wilsonshift und c=1/576. Der neutrale Onsite-Austausch und der Zwei-High-Kanal sind tatsächliche Originaloperationen. Schon das vierte komprimierte Moment zeigt den fehlenden Beitrag:

\[
J^*H^4J-E_0^*(V_1^*HV_1)^4E_0=g^2R_1^*R_1>0.
\]

Die bekannte Formel \(\tfrac12(1-\Delta/\sqrt{\Delta^2+4g^2})\) ist exakt für den Eigenvektor einer **angenommenen isolierten** skalaren 2×2-Matrix. Um sie für den tatsächlichen Parent verwenden zu dürfen, müsste der Raum invariant sein, der diagonale Block passend skalieren und die restliche Selbstenergie kontrolliert werden. Gerade die Invarianz scheitert hier exakt. Daher sind 6,6%, 10,0%, 28,7% keine bewiesenen nativen Zustandsgewichte, und \(N\approx96\Delta^2\) ist keine bewiesene physische Abbruchschwelle oder Orthogonalitätskatastrophe.

Darüber hinaus vermischt „Überlappung mit der eigenen ersten Dressingversion“ zwei verschiedene Objekte schon im Hilfsmodell. Bei konstantem \(\Delta=9587/2400\) und \(g^2=125/96\) hat der **normierte Erstordnungsvektor**

\[
\frac{|L\rangle-(g/\Delta)|H\rangle}{\sqrt{1+g^2/\Delta^2}}
\]

High-Gewicht \(g^2/(\Delta^2+g^2)\approx7{,}5445\%\). Der exakte Eigenvektor derselben isolierten 2×2-Matrix hat dagegen ungefähr 6,5858%. Beide Zahlen sind ausdrücklich Modellwerte; keine davon ersetzt die ursprüngliche feldtheoretische Rechnung. Physische Gewichte, normierte Überlappungsquadrate und unnormierte Beimischungsnormen müssen getrennt angegeben werden.

Die belastbare Folgerung lautet daher: Die genaue erste Kopplung wächst bei dieser globalen All-Low-Präparation wie \(\sqrt N\). Wie sich daraus der Überlapp einer bestimmten vollständig gedressten Zustandsfamilie entwickelt, ist eine weitere Rechnung mit dem tatsächlichen Hamiltonoperator.

## 3. Theorem 4: exaktes Cap-Breathing und korrekte Stationaritätsgrenze

In der bezeichneten neutralen Cap-Basis \(a=0,1,2,3\) sind die elektrischen Energien relativ zum gemeinsamen Onsitewert

\[
E_a=\kappa(0,20,16,20),\qquad
T_{\rm bal}|a\rangle=|a+1\bmod4\rangle.
\]

Damit gilt für die tatsächliche rein elektrische Entwicklung des präparierten Caps exakt

\[
\langle\Psi(t),T_{\rm bal}\Psi(t)\rangle
=\frac14\sum_a e^{it(E_{a+1}-E_a)}
=\frac12[\cos(20\kappa t)+\cos(4\kappa t)].
\]

Der erste positive gemeinsame Revivalzeitpunkt ist \(t=\pi/(2\kappa)=50\pi\). Energiezunahme \(14\kappa\), elektrische Varianz \(68\kappa^2\), Balance-Kommutatornormquadrat \(208\kappa^2\) sowie auf den zwei deklarierten Ringen die volle Varianz \(68\kappa^2+16b^2=389/11250\) stimmen. Die Cosinusformel gilt für H_E; unter dem vollständigen H kommen die bewiesenen Materiekanäle hinzu.

Für den **gesondert vorgegebenen algebraischen Normfluss** \(\lambda_t(U)=U\), \(\lambda_t(S_m)=m^{it}S_m\) ist die stationäre endliche Restriktion ebenfalls präzise beweisbar:

\[
P_r=U^rS_4S_4^*U^{-r},\quad
L=U(I-P_3)+U^{-3}P_3,\quad
F_{ab}=L^{a-b}P_b
\]

sind alle \(\lambda_t\)-fest. Folglich ist die gesamte bezeichnete M₄-Algebra punktweise fest, ebenso die beiden entsprechenden Loop-Faktoren. **Jeder auf diese Algebra eingeschränkte Zustand**, einschließlich des Cap-Zustands, hat dort unveränderte Antworten. Daraus folgt weder ein unveränderter Cap-Vektor in der ursprünglichen Rotorrepräsentation noch Invarianz seines Zustands auf der ganzen Algebra. Dafür müssten Darstellung, Erweiterung des Zustands und Implementierung des Flusses eigens vorliegen.

Auch der Normfluss darf dabei nicht mit \(\operatorname{Ad}(e^{it\log\mathsf N})\) auf der positiven Ladungsbasis gleichgesetzt werden: Der Normfluss fixiert U, während \(e^{it\log\mathsf N}Ue^{-it\log\mathsf N}|1\rangle=2^{it}|2\rangle\). Die Übereinstimmung der Skalierungsphasen auf S_m identifiziert die beiden Flüsse nicht auf einer Algebra, die auch Addition enthält. Der getestete Kontrast ist daher: **elektrischer Fluss mit berechnetem Cap-Breathing versus ein gesondert definierter Normfluss mit fester markierter M₄-Algebra**. Eine gemeinsame physische Zeitauswahl ist damit weiterhin nicht hergeleitet.

## Kontrolle und Pins

`check_fable_zusatz.py` liefert zehn exakte kleine Kontrollen: Duhamel-Gegenzeuge, vierkomponentige Cap-Antwort und Revival, Momente, Zwei-Ring-Varianz sowie die Unterscheidung zweier 2×2-Modellgewichte. Ergebnis: `fable-zusatz-checks.json`. Keine neue Dressing-Iteration wurde ausgeführt. `fable-zusatz-pins.json` pinnt die unveränderten neuen Originalsnapshots und diese Zusatzartefakte separat; ältere Manifeste bleiben unangetastet.
