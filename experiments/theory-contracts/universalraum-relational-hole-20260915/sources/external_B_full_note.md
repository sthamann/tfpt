# TFPT / Universalraum: Anregungen als Änderungen eines Hintergrunds

## Forschungsfortsetzung zum Stand v1.6 und v1.6.1

15. September 2026. Eigenständige Forschungsnotiz; keine Änderung der freigegebenen Quelldokumente. „Hier ausgearbeitet“ bezeichnet diese Untersuchung, keinen Prioritätsanspruch gegenüber sämtlichen früheren Rechnungen oder der Literatur.

## 1. Ergebnis und Einordnung

**Die stärkste einfache Fortsetzung ist eine genaue Beziehung zwischen einem zusammengesetzten Dreierzustand und einem Loch in einem Viererzustand.** Im unveränderten nativen Modell lässt sich ein normierter Zustand \(|Q_4\rangle\) konstruieren, für den in allen 64 Moden gilt:

\[
\boxed{\sqrt{32}\,f_r|Q_4\rangle=\chi_r^\dagger|0\rangle.}
\]

Links wird ein Fermion entfernt, rechts ein Komposit erzeugt. Beide Seiten sind derselbe normierte Dreierzustand. Die Ladungen stimmen vollständig: links \(4-1=3\), rechts \(0+3=3\). Eine Umbenennung nur modulo vier ist nicht nötig.

Dieser Anschluss unterstützt ein präzises Stück der Einfachheitsintuition: **Die Bedeutung einer Anregung hängt auch von dem Zustand ab, auf dem sie wirkt.** Ein anderes Bezugssystem im Zustandsraum kann eine vermeintliche Unvereinbarkeit lösen, ohne die Wechselwirkung zu erweitern.

Weitere Ergebnisse dieser Untersuchung:

- Der passende Viererkanal schließt unter dem ursprünglichen Hamiltonoperator auf einer exakt berechneten 2×2-Matrix. Auf seinem unteren Eigenzustand ist die Lochantwort vollständig bekannt.
- Die Abweichung der Kompositfelder von kanonischen Fermionregeln besitzt eine kurze exakte Formel. Auf einem symmetrischen Hintergrund hängt ihre gleichzeitige Norm nur von zwei mittleren Besetzungen ab.
- Die gesamte unital erzeugte Kontrollalgebra des N=3-Sektors hat unter den beiden dokumentierten Kontrollen Dimension 14, trotz 45.504 Zuständen.
- Die Zustandsauswahl lässt sich durch neutrale Abläufe grundsätzlich nicht vollständig bestimmen: Unter passenden Domänenannahmen bleibt sogar eine beliebige Verschiebung \(H\mapsto H+F(N)\) unsichtbar.

**Nicht gelöst sind die Auswahl des physischen Hintergrunds, die native räumliche Zusammensetzung und die vollständigen T1–T8-Ziele.** Insbesondere ist der hier konstruierte Viererzustand bei der dokumentierten schwachen Kopplung kein Grundzustand des vollständigen N=4-Sektors. Gerade diese Gegenprüfung verhindert, dass aus einem exakten Lochanschluss eine unbewiesene Vakuumtheorie wird.

## 2. Welche Quellen und Ergebnisse zugrunde liegen

Gelesen und miteinander abgeglichen wurden die sieben genannten Dateien: die beiden Forschungsnotizen v1.6.1, Hauptdokument und Update v1.6, beide erklärenden/resultierenden Markdown-Texte v1.6 sowie das Prüf- und Quellenpaket. Das Hauptdokument hat 168, das Update acht PDF-Seiten. Für die neue Entwicklung sind insbesondere die Kapitel 34–37 des Hauptdokuments und Abschnitte 2–7 der technischen Notiz v1.6.1 maßgeblich. Die älteren Kapitel liefern die weiteren offenen Physik- und Arithmetikfragen. Die aktuellen Quellen wurden mit SHA-256 erfasst; mathematische PDF-Seiten wurden zusätzlich visuell kontrolliert.

Der aktuelle Stand ersetzt einige frühere Engpässe:

| Thema | Maßgeblicher Stand |
|---|---|
| Matrixordnung und E8 | Die markierte Gitterisometrie ist vorhanden; v1.6 reproduziert einen bereits am 9. September vorhandenen Beweis. |
| Präparation der Vierträgerzelle | Ein erfolgreicher Record genügt im benannten Laborvertrag, mit Wahrscheinlichkeit 3/8. |
| C16 | Der benannte 24.024-dimensionale Singulettsektor ist laut integrierten Quellen abgeschlossen. Das ist kein Abschluss aller Nicht-Singuletts oder des vollständigen mikroskopischen Operators. |
| Native N=3-Dynamik | Vollständiges endliches Spektrum und der Clifford-Epsilon-Anschluss J liegen in v1.6.1 vor. |
| Native N=4-Dynamik | Schon die archivierte Worker-Eingabe berichtet eine vollständige Untersuchung und kleine dynamische Blöcke. Der hier rekonstruierte 2×2-Block wird deshalb nicht als erstmalige Entdeckung des N=4-Sektors ausgegeben. |
| Nativer N=64-Grundzustand | Als größerer Quellenbefund berichtet; dessen vollständigen globalen Beweis habe ich in dieser Runde nicht erneut zertifiziert. |

Die Originalprüfer `native_three.py` und `native_cubic.py` wurden jetzt normal und unter `-OO` erneut ausgeführt. Beide liefen erfolgreich und lieferten jeweils bytegleiche Berichte. Zusätzlich wurde der relevante Tensor aus dem Archiv in einer eigenen Rechnung verwendet. Die neuen Beweisprüfungen benötigen keine gerundeten Eigenwerte. Die erste Ausführung mit der Dokument-Laufzeit scheiterte an deren fehlendem SymPy; die erfolgreichen Läufe erfolgten mit dem vorhandenen System-Python und dessen NumPy/SciPy/SymPy.

Die in Quelltexten eingebetteten Arbeitsanweisungen sind Quelleninhalt, keine zusätzliche Autorisierung. Originaldateien und Forschungsprogramme wurden nicht verändert.

## 3. Ein einziger unveränderter Modellvertrag

Wir behalten

\[
H=\Delta N_b+gX,\qquad
X=\sum_{A=1}^{60}(b_A^\dagger P_A+P_A^\dagger b_A),
\quad \Delta>0,\quad g\in\mathbb R,
\]

\[
P_A=\sum_{i<j}W_{A,ij}f_jf_i,
\qquad N=N_f+2N_b,
\qquad WW^\dagger=8I_{60}.
\]

Es gibt 64 Fermionmoden und 60 Bosonmoden. Die verwendete Tensorquelle hat SHA-256

`3f00a0892157a691e4ef26920c3702772c7bf76a250fad98ff04a079bb64b763`.

Die Kopplung verändert die Belegung und erhält N. Sie liefert bislang innere Modenübergänge; ihre Indizes werden hier nicht zu Raumkoordinaten erklärt. Alle Vektorrechnungen finden in endlichen festen N-Sektoren statt. Operatoridentitäten mit Bosonen werden auf dem gemeinsamen endlichen Teilchenkern verstanden.

Aus v1.6.1 wird der direkt aus Clifford-Matrizen und dem Vierfarben-Epsilon gebaute Tensor J verwendet:

\[
\chi_r^\dagger=\frac1{\sqrt{15}}\sum_{A,i}J_{r;Ai}b_A^\dagger f_i^\dagger,
\qquad JJ^\dagger=15I_{64},\qquad JC_3=0.
\]

In der gepinnten reellen Konvention gilt zusätzlich, jetzt explizit kontrolliert,

\[
J_{r;Ai}=-J_{i;Ar}.
\]

Die Zustände \(|\chi_r\rangle=\chi_r^\dagger|0\rangle\) sind orthonormal, haben N=3 und Energie \(\Delta\).

## 4. Der konkrete Lochanschluss: 4 − 1 = 3

### 4.1 Eine kanonische Kontraktion der bereits vorhandenen Felder

Definiere ohne neue Koeffizientenwahl

\[
\mathcal Q^\dagger=\sum_{r=1}^{64}f_r^\dagger\chi_r^\dagger,
\qquad |Q_4\rangle=\frac{\mathcal Q^\dagger|0\rangle}{\sqrt{128}}.
\]

„Vierer“ bedeutet hier **N=4**. Dieser Zustand besteht aus einem Boson und zwei Fermionen; er ist kein Zustand aus vier freien Fermionen. Er ist auch nicht der frühere Vierträgerzustand \(\Omega\) des anderen Laborvertrags.

Die Antisymmetrie von J und die kanonischen Fermionregeln geben

\[
f_s\mathcal Q^\dagger|0\rangle=2\chi_s^\dagger|0\rangle.
\]

Weil der unnormierte Zustand genau zwei Fermionen enthält,

\[
2\|\mathcal Q^\dagger|0\rangle\|^2
=\sum_s\|f_s\mathcal Q^\dagger|0\rangle\|^2
=64\cdot4=256.
\]

Damit sind Normierung und Lochidentität bewiesen:

\[
\boxed{f_s|Q_4\rangle=\frac1{\sqrt{32}}|\chi_s\rangle.}
\]

Die Rechnung wurde für alle 64 Moden mit exakten Besetzungsoperationen kontrolliert. Der unnormierte ganzzahlige Vektor \(\sqrt{15}\mathcal Q^\dagger|0\rangle\) hat 480 nichtverschwindende Basisamplituden und Normquadrat 1920.

### 4.2 Was damit gelöst ist und was nicht

**Gelöst:** Der Dreierkomposit ist exakt als Ergebnis einer Fermionentfernung aus einem ausdrücklich konstruierten Viererhintergrund realisiert. Man muss die erhaltene Zahl nicht ändern, kein Kondensat voraussetzen und keine neue Kopplung hinzufügen.

**Nicht behauptet:** \(\chi_s^\dagger=f_s\) als Operatoridentität. Die rechte und linke Seite der Vektoridentität wirken auf verschiedene Hintergründe. N bleibt vollständig erhalten, wenn Ein- und Ausgang einschließlich der entfernten Anregung bilanziert werden. Ein physischer Zugriff, der tatsächlich \(f_s\) realisiert, muss weiterhin durch den Operationsvertrag gedeckt sein.

Ebenso folgt daraus weder eine relativistische Antiteilchenidentifikation noch die vollständige physische Half-Charge-/Clock-Abbildung. Ein inneres konjugiertes Gewicht und eine lokale Lochanregung reichen dafür nicht aus.

### 4.3 Weshalb das zur Einfachheitsintuition passt

Ein freier Platz in einer besetzten Struktur und ein zusätzliches Objekt über einem leeren Bezug können denselben verbleibenden Zustand beschreiben. Die Mathematik legt hier die exakten Faktoren fest. Die Vereinfachung besteht in einer besseren Wahl dessen, worauf ein Operator wirkt, nicht in einer Änderung der Ladungsrechnung.

## 5. Die Dynamik des Viererhintergrunds ist ebenfalls klein

### 5.1 Ein invarianter Zweizustandsraum

Setze

\[
|B_2\rangle=\frac14X|Q_4\rangle.
\]

Die volle Wirkung aller Originalvertizes ergibt exakt

\[
X|Q_4\rangle=4|B_2\rangle,
\qquad X|B_2\rangle=4|Q_4\rangle.
\]

\(|B_2\rangle\) ist normiert und besteht ausschließlich aus zwei Bosonen. Die Beiträge zu vier freien Fermionen verschwinden vollständig. Im ganzzahligen Nachweis besitzt \(X\sqrt{15}\mathcal Q^\dagger|0\rangle\) 30 nichtverschwindende Zweibosonamplituden und Normquadrat 30720. Die Rückwirkung ist genau das 16-Fache des Ausgangsvektors. Es wird kein Rest außerhalb des Zweizustandsraums abgeschnitten.

In der Basis \((|Q_4\rangle,|B_2\rangle)\) ist daher

\[
\boxed{H_4=\begin{pmatrix}\Delta&4g\\4g&2\Delta\end{pmatrix}.}
\]

Seine beiden Energien sind

\[
E_{4,\pm}=\frac{3\Delta\pm\sqrt{\Delta^2+64g^2}}2.
\]

Das ist ein exakter invarianter Teilraum des vollständigen Operators. Ein vollständiger N=4-Singulettzensus wird hier nicht zusätzlich behauptet.

### 5.2 Eine exakte Lochantwort mit kleinem Energieabstand

Für den unteren Eigenzustand

\[
|Q_-\rangle=u|Q_4\rangle+v|B_2\rangle,
\qquad
u^2=\frac12\left(1+\frac\Delta{\sqrt{\Delta^2+64g^2}}\right)
\]

kann u reell positiv gewählt werden; v erhält das passende relative Vorzeichen. Weil \(f_r|B_2\rangle=0\), gilt

\[
f_r|Q_-\rangle=\frac u{\sqrt{32}}|\chi_r\rangle.
\]

Die Energieänderung der Fermionentfernung ist

\[
\boxed{\varepsilon_h=\Delta-E_{4,-}
=\frac{\sqrt{\Delta^2+64g^2}-\Delta}{2}
=\frac{16g^2}{\Delta}+O(g^4/\Delta^3).}
\]

Die Zweizeitantwort folgt ohne weitere Näherung:

\[
\boxed{
\langle Q_-|f_r^\dagger(t)f_s(0)|Q_-\rangle
=\delta_{rs}\frac{u^2}{32}e^{-i\varepsilon_h t/\hbar}.}
\]

Für \(g/\Delta=1/20\):

| Größe | Wert |
|---|---:|
| Hintergrundenergie \(E_{4,-}/\Delta\) | 0,96148351928655 |
| Lochenergie \(\varepsilon_h/\Delta\) | 0,03851648071345 |
| Gewicht pro Modus \(u^2/32\) | 0,03013244829508 |

Die geschützte Dreieranregung hat über dem leeren Zustand Energie \(\Delta\), als Loch über diesem Vierereigenzustand jedoch nur den angegebenen kleinen Energieabstand. Das ist eine konkrete Realisierung von „Anregungen relativ zum Hintergrund“.

Es ist noch keine Teilchenmasse im Raum: Es fehlt eine hergeleitete Impulsabhängigkeit. Für festes \(g\ne0\) ist dieser lokale Energieabstand zudem positiv.

### 5.3 Die Gegenprüfung: dieser Hintergrund wird nicht zum Vakuum erklärt

Bei \(g/\Delta=1/20\) ist \(E_{4,-}>0\). Bereits der Vierfermionenbasiszustand mit besetzten Moden \(0,1,2,57\) liefert einen negativen Variationswert. Seine Konversionsnorm ist exakt \(\|X|0,1,2,57\rangle\|^2=2\). Die Kompression auf ihn und seinen normierten Konversionszustand hat Matrix

\[
\begin{pmatrix}0&\sqrt2g\\\sqrt2g&\Delta\end{pmatrix}.
\]

Ihr kleinster Eigenwert ist

\[
\frac{\Delta-\sqrt{\Delta^2+8g^2}}2<0.
\]

Die Variationskompression muss kein invarianter Raum sein, um diese obere Schranke an die Grundenergie zu liefern. Damit ist \(|Q_-\rangle\) bei der betrachteten schwachen Kopplung **nicht einmal Grundzustand des vollständigen N=4-Sektors**. Ein zusätzlich postulierter Symmetriesektor wäre ein gesonderter Auswahlvertrag.

Auch die bisherige Präparationsgrenze bleibt bestehen: H allein erzeugt die geschützten Dreierzustände weiterhin nicht aus drei freien Fermionen. Unser Lochprozess beginnt in N=4 und enthält eine ausdrücklich benannte Fermionentfernung.

## 6. Zusammengesetzte Fermionen: die richtige Norm auf dem Hintergrund

### 6.1 Die vollständige gleichzeitige Operatoridentität

Mit \(\{A,B\}=AB+BA\) folgt aus den ursprünglichen Boson- und Fermionregeln

\[
\begin{aligned}
\{\chi_r,\chi_s^\dagger\}={}&\delta_{rs}I\\
&+\frac1{15}\sum_{A,B,i}\overline{J_{r;Ai}}J_{s;Bi}\,b_B^\dagger b_A\\
&-\frac1{15}\sum_{A,i,j}\overline{J_{r;Ai}}J_{s;Aj}\,f_j^\dagger f_i.
\end{aligned}
\]

Die vermeintlich komplizierten gemischten Vieroperatorprodukte heben sich auf. Übrig bleiben ein konstanter Term und zwei Einteilchendichten. Dagegen gilt \(\{\chi_r^\dagger,\chi_s^\dagger\}=0\) schon aus den Fermionerzeugungsregeln.

Die Formel erklärt zugleich den alten Gegenfall: Im vollständig mit Fermionen besetzten Nullbosonzustand ist der gemischte Antikommutator null. Die Felder sind global keine freien kanonischen Fermionmoden. Das schließt eine nichttriviale Feldantwort auf anderen Zuständen nicht aus.

### 6.2 Auf einem symmetrischen Zustand genügen zwei Zahlen

Angenommen, der Zustand ist unter den angegebenen Spin(10)- und SU(4)-Wirkungen invariant. Die Einteilchenräume \((16,4)\) und \((10,6)\) sind irreduzibel. Dann sind ihre Einteilchendichten skalar:

\[
\langle f_j^\dagger f_i\rangle=\frac{\langle N_f\rangle}{64}\delta_{ij},
\quad
\langle b_B^\dagger b_A\rangle=\frac{\langle N_b\rangle}{60}\delta_{AB}.
\]

Deshalb

\[
\boxed{\langle\{\chi_r,\chi_s^\dagger\}\rangle
=\delta_{rs}Z_\omega,
\quad Z_\omega=1+\frac{\langle N_b\rangle}{60}-\frac{\langle N_f\rangle}{64}.}
\]

Für einen solchen Zustand im Sektor N=64 reduziert sich das weiter:

\[
\boxed{Z_\omega=\frac{23}{480}\langle N_b\rangle.}
\]

Falls der berichtete native N=64-Singulettgrundzustand gilt, ist seine Bosonbesetzung nicht null: Ein Nullbosonzustand hat Energieerwartung null, während das Modell negative Variationsenergien besitzt. Dann folgt \(Z_\omega>0\). Das ist ein bedingter positiver Anschluss an diesen Hintergrund; der größere Grundzustandssatz wurde hier nicht neu bewiesen.

Für einen isolierten differenzierbaren Eigenzustand liefert Hellmann–Feynman zusätzlich

\[
\langle N_b\rangle=\left.\frac{\partial E_0}{\partial\Delta}\right|_g.
\]

Die Ableitung muss bei festem g erfolgen, nicht entlang eines festen Verhältnisses g/Delta. Damit wäre die gesamte gleichzeitige Kompositnorm aus einer einzigen Energieableitung bestimmbar.

**Grenze:** \(Z_\omega\) ist eine gleichzeitige Norm beziehungsweise eine Spektralsummenregel. Es ist noch kein isoliertes Quasiteilchen-Polgewicht. Eine Normierung \(\chi/\sqrt{Z_\omega}\) erzwingt weder volle Operator-CAR noch Wick-Faktorisierung, räumliche Lokalität oder einen Kontinuumsgrenzwert.

## 7. Die große Zustandszahl verbirgt eine kleine Kontrollalgebra

Im N=3-Sektor haben wir

\[
X=\begin{pmatrix}0&C_3^\dagger\\C_3&0\end{pmatrix},
\quad B=N_b=\begin{pmatrix}0&0\\0&I\end{pmatrix}.
\]

Der unabhängig reproduzierte ganzzahlige Satz lautet

\[
S(S-7I)(S-10I)(S-12I)=0,\qquad S=C_3C_3^\dagger,
\]

mit Multiplizitäten 64, 2880, 576 und 320. Die Nullräume sind ein 37.888-dimensionaler reiner Fermionraum und ein 64-dimensionaler Boson-Fermionraum. Jeder positive Singulärwert liefert eine Zweizustandswirkung mit entsprechender Vielfachheit.

Für genau die beiden Kontrollen X und B folgt daher

\[
\boxed{
\operatorname{alg}^*(I,X,B)
\cong \mathbb C\oplus\mathbb C\oplus
\bigoplus_{\lambda=7,10,12}(M_2(\mathbb C)\otimes I_{m_\lambda}),
\quad \dim=14.}
\]

Beweis: \(X^2\) trennt die drei verschiedenen positiven Eigenwerte durch Spektralpolynome. Auf jedem Zweizustandsblock erzeugen X und B alle Matrixeinheiten. Auf dem Nullraum unterscheidet B die beiden dunklen Teilräume. Keine der beiden Kontrollen verändert die Multiplizitätsindizes. Eine exakte rationale Algebraabschlussrechnung auf einer treuen 8-dimensionalen Darstellung bestätigt die Dimension 14.

**Nutzen:** Mehrzeitwörter aus diesen Kontrollen lassen sich über diese kleine Algebra behandeln. Die schon belegten inneren Übergänge bleiben real; sie bedeuten keine unabhängige Kontrolle über alle 45.504 Zustände.

**Grenze:** Das ist kein Satz über zusätzliche modeweise Quelloperationen und auch kein allgemeiner Stillstandssatz für höhere N. Aus drei aktiven Schwingungstypen folgen insbesondere keine drei Raumdimensionen.

## 8. Zustandsauswahl: welche Information tatsächlich fehlt

Sei \(\mathcal A_0\) die Algebra der N-neutralen Observablen. Weil \([H,N]=0\), gilt für jedes reelle F, für das die Entwicklungen wohldefiniert sind,

\[
e^{it(H+F(N))/\hbar}Oe^{-it(H+F(N))/\hbar}
=e^{itH/\hbar}Oe^{-itH/\hbar},\qquad O\in\mathcal A_0.
\]

Auch vollständige Instrumentfolgen mit neutralen Krausoperatoren unterscheiden diese Entwicklungen bei identischem Eingang nicht. Alle Historien mit gleichem Endzeitpunkt erhalten denselben zusätzlichen sektorabhängigen Unitärfaktor, der in ihren Gramprodukten wegfällt.

**Exakte Schlussfolgerung:** Neutrale Ausführungsdaten allein bestimmen die relativen Energien verschiedener N-Sektoren nicht. Mehr solche Daten beheben dieses Identifikationsproblem nicht.

Die sparsame Lösung ist, die Zustandsfrage in zwei klar definierte Fälle zu zerlegen:

1. **Physisch fester N-Sektor:** F(N) ist dort ein Energienullpunkt. Dann ist die Auswahl von N als Anfangs- oder Randbedingung zu begründen.
2. **Physisch vergleichbare N-Sektoren:** Ein zulässiger Ladungswechsel oder eine Referenz, die Ladung austauscht, muss mitmodelliert werden. Erst damit sind die relativen Sektorenergien messbar.

Die neue Lochantwort zeigt den Unterschied explizit: Unter H+mu N wird \(\varepsilon_h\) zu \(\varepsilon_h-\mu\). Das ist eine geladene Antwort zwischen N=4 und N=3. Sie setzt einen entsprechenden Zugriff voraus.

Dies erklärt, welche fehlende Information T8 benötigt. Es wählt noch keinen physikalischen Wert für mu und keinen gewünschten Grundzustand. Auch maximale Entropie, eine positive Quadratsumme oder der formale Ausdruck \(H=-\log T\) ersetzen die Auswahl ihrer Eingaben nicht.

## 9. Raum: die nächste einfache Frage betrifft Teilalgebren

Die brauchbare Fortsetzung ist, räumliche Teile durch unabhängige Zugriffe und ihre Wechselwirkung zu charakterisieren. Das entspricht dem etablierten Gedanken, dass die operational zugängliche Algebra die relevante Teilsystemstruktur mitbestimmt; siehe [Zanardi, Virtual Quantum Subsystems](https://arxiv.org/abs/quant-ph/0103030). Eine daraus speziell für TFPT ausgewählte 3D-Struktur liegt noch nicht vor.

Für Kandidaten \(\mathcal A_x\) und \(\mathcal A_y\) kann man zunächst neutrale, gerade lokale Observablen verwenden und die Antwort

\[
\mathcal R_{xy}(t)=\sup_{\|A\|,\|B\|\le1}
\|[\alpha_t(A),B]\|,
\quad A\in\mathcal A_x,\ B\in\mathcal A_y
\]

untersuchen. Dies ist nur dann ein Herkunftstest, wenn die Teilalgebren bereits aus zulässigen Quellzugriffen bestimmt sind. Ihre freie Wahl würde den Raum vorwegnehmen. Für ungerade Fermionfelder sind die entsprechenden graduierten Lokalitätsrelationen zu beachten.

Die ersten nichtverschwindenden verschachtelten Kommutatoren können danach Erreichbarkeit zeigen; Skalierung muss eine geeignete lokale Familie, Volumenwachstum und gemeinsame Ausbreitung ergeben. Der vorhandene wachsende eindimensionale TFPT-Netzansatz ist ein möglicher Ausgangspunkt, aber kein bereits abgeleitetes A3/BCC-Raumgitter.

Die lokale Parität liefert weiterhin einen harten Test: Für getrennte Banken mit nur lokal geraden Paarvertizes und Vermittlerhopping kommutiert jede erlaubte Entwicklung mit \(\Pi_x=(-1)^{N_{f,x}}\). Ein Loch als ungerade Anregung umzuinterpretieren beseitigt diese Schranke nicht. Auch dessen Bankwechsel müsste zwei lokale Paritäten ändern. Der neue Lochanschluss ist deshalb noch kein räumlicher Fermiontransport.

Die Matrixordnung liefert ein E8-Längengitter in kleinen Matrizen. Sie realisiert nicht schon die gesamte 248-dimensionale E8-Liealgebra durch gewöhnliche 2×2-Matrixkommutatoren. Eine nichttriviale komplexe Liealgebrahomomorphie von der einfachen E8-Algebra nach gl(2,C) wäre injektiv und scheitert an der Dimension. Der Unterschied zwischen Gitter, Lieklammer, Fockoperator und Ortsoperation bleibt wesentlich.

## 10. Alle acht Hauptfragen: Lösungsertrag und verbleibende Aufgabe

| Tor | Sparsamster Ansatz nach dieser Untersuchung | Tatsächlicher Status |
|---|---|---|
| **T1: Quelle, Markierung, Dimension** | Den vorhandenen Matrix-/Cliffordkern samt *wirklich erlaubten* Operationen festhalten. Physische Äquivalenz über vollständige Antworten prüfen. Die maximale Ordnung und q brauchen einen Auswahl- beziehungsweise Ausführungsnachweis. | E8-Gitteranschluss vorhanden; eindeutige Quellen- und Dimensionsauswahl offen. |
| **T2: physisches Feld** | Die neue Lochidentität und die Besetzungsformel für die Kompositnorm als Ausgang verwenden. Auf dem ausgewählten Hintergrund Energie, Adjunktion, Mehrzeitantwort und Clock prüfen. | Exakter endlicher Lochanschluss erreicht; Half-Charge-Feld und Kontinuumsrenormierung offen. |
| **T3: räumliche 3+1D-Ausführung** | Quellzugängliche Teilalgebren und ihre gegenseitige Antwort bestimmen. Vorhandene Netzdynamik mit denselben Feldern verbinden. | Innere Rekopplung ist nachgewiesen; nativer 3D-Raum und gemeinsamer Kegel offen. |
| **T4: Chiralität** | Erst am gemeinsamen räumlichen Operator einen regulierten Index, zulässiges Maß und kontrollierte Spiegelentkopplung nachweisen. | Falten des vorhandenen Walks entfernt keine Spiegel. Kein neues chirales Maß bewiesen. |
| **T5: Kontinuum und Wechselwirkung** | Dieselbe lokale Regel und denselben Zustand mit kontrollierter Größenabhängigkeit verwenden; verbundene Korrelatoren, Clusterstruktur und Streuung prüfen. | Endliche kleine Blöcke und Stabilität helfen, liefern aber noch keinen wechselwirkenden Grenzwert. |
| **T6: Kopplungen, Familien, Neutrinos** | Einen gemeinsamen Transfer mit allen Eingaben einfrieren; erst dann normierte Spektren und Mischungen vergleichen. | Aus 64er-Multiplizitäten, E8-Zerlegungen oder drei Schwingungstypen folgt keine vollständige Familien-/Konstantenauswahl. |
| **T7: Gravitation** | Im selben Modell nach einem dynamischen Spin-2-Pol, zwei Helizitäten und universellen Ward-Identitäten suchen. | Kegelkinematik vorhanden; kein Graviton und keine universelle Kopplung hergeleitet. |
| **T8: Zustand und Ursprung** | Die N-neutrale Äquivalenz zuerst berücksichtigen. Einen Sektor begründen oder einen echten Ladungsvergleich samt Referenz liefern. | Die fehlende Information ist scharf bestimmt. Der neue Viererhintergrund wird vom vollständigen schwach gekoppelten Modell nicht als Grundzustand ausgewählt. |

Für T4 ist eine bekannte knappe Zielrelation

\[
\gamma_5D+D\gamma_5=aD\gamma_5D.
\]

Sie zeigt, wie Gitterchiralität präzise anders als naive Antikommutation realisiert werden kann. Ein geeigneter D, sein Maß und seine Herkunft müssten jedoch aus TFPT folgen. Die Relation einfach einzusetzen wäre ein zusätzlicher Modellbau. Primärquelle: [Lüscher, Exact chiral symmetry on the lattice](https://arxiv.org/abs/hep-lat/9802011).

Für T7 darf ein Spin-2-Kandidat nicht nur einen Namen erhalten. Unter den Voraussetzungen eines Lorentz-kovarianten erhaltenen Energie-Impuls-Tensors bestehen bekannte Beschränkungen für masselose Teilchen mit Spin größer als eins. Ein Emergenzansatz muss erklären, welche Voraussetzung gegebenenfalls nicht erfüllt ist. Das ist kein pauschales Verbot jeder emergenten Gravitation. Primärquelle: [Weinberg und Witten, Limits on massless particles](https://www.sciencedirect.com/science/article/pii/0370269380902129).

## 11. Die weiteren offenen Fragen aus dem Hauptbuch

Diese Fragen werden nicht stillschweigend ausgelassen. Für keine von ihnen ergibt der lokale Lochsatz schon einen vollständigen Abschluss.

| Problem | Konkrete einfache Fortsetzung | Was weiter fehlt |
|---|---|---|
| Aufzeichnung und Interferenz | Historien durch \(D(h,h')=\omega(K_{h'}^\dagger K_h)\) gemeinsam beschreiben. Gramoperatoren vergleichen; äquivalente kohärente Abbildungen besitzen auf ihren Bildern einen Isometrieadapter. | Native Instrumente, Hilfsregister, Reset und Zustand. Orthogonale Aufzeichnung interner Austauschwege kann ihre Interferenz zerstören. |
| Messproblem und Zeitpfeil | Vollständige Ein- und Ausgangszustände sowie zurückbehaltene Aufzeichnungen modellieren; thermodynamische Aussagen aus dem tatsächlich erlaubten Zugriff ableiten. | Eine dynamische Herkunft der Randbedingungen und irreversibler Makrostatistik. Ein endlicher Echovergleich allein erledigt diese Frage nicht. |
| C16-Gesamtspektrum | Den bereits abgeschlossenen benannten Singulettsektor als Baustein nutzen; die übrigen Darstellungen und den Transfer zum mikroskopischen H gesondert kontrollieren. | Die allgemeinen Nicht-Singulett- und Mikroskopieabschlüsse, soweit im aktuellen Vertrag gefordert. Kein erneuter Großlauf in dieser Untersuchung. |
| Gemeinsamer Lichtkegel | Pole verschiedener physischer Antworten aus demselben Zustand vergleichen; ein gemeinsames Zeitmaß legt deren Geschwindigkeitsverhältnis nicht fest. | Eine Symmetrie oder Dynamik, die wirklich universelle Geschwindigkeiten erzwingt. |
| Inflation und Parametertransfer | Die gemeinsame Vorhersagekurve beibehalten: ein Wert desselben Parameters muss Amplitude und Neigung zugleich tragen. Alle Änderungen bis zur elektromagnetischen Ausgabe weiterrechnen. | Die dokumentierte Spannung ist durch den Lochanschluss nicht behoben. Keine neue Daten-Likelihoodrechnung. |
| Dunkle Materie | Dunkle Sektoren nur dann als Kandidaten verwenden, wenn Kopplung, Stabilität, Entstehung und gravitative Wirkung berechnet sind. | „Dunkel gegenüber einem Operator“ ist keine Herleitung kosmologischer dunkler Materie. |
| Dunkle Energie | Einen erhaltenen effektiven Energie-Impuls-Tensor samt Zustandsgleichung aus derselben Quelle gewinnen. | Die \(\mu N\)-Freiheit oder eine verschobene Grundenergie bestimmt keine physische kosmologische Konstante. |
| Schwarze Löcher | Erst nach der gravitativen Dynamik die zugänglichen Algebren, Horizonte und Entropie bestimmen. | Ein endliches History-Register liefert weder Horizontdynamik noch den Flächenterm. |
| Materieüberschuss und starke CP-Frage | Symmetrieverletzung, Zustand und Nichtgleichgewicht im gemeinsamen Modell quantitativ untersuchen. | Innere Vorzeichen oder eine vierfache Ladung liefern noch keine Asymmetrieausbeute oder CP-Unterdrückung. |
| RH | Eine exakte Identifikation der vollständigen signierten Weil-Form mit einer positiven Darstellung auf dem erforderlichen Testraum suchen. | Gemischte Terme, Rand-/archimedische Beiträge, unendliche Kontrolle und der eigentliche Identifikationssatz. Ein positives Gramobjekt anderer Herkunft genügt nicht. |
| Faktorisierung | Den Aufwand der *Auslesung* einer identifizierten Kennzahl in der Eingabelänge \(\log N\) vollständig nachweisen. | Die bekannte E8-Gaußsumme \(N^4\gcd(t,N)^4\) enthält hier keinen nachgewiesenen neuen schnellen Zugriff. |
| P versus NP | Eine präzise uniforme Algorithmus- oder Untergrenzenbehauptung mit ihrem Ressourcenmodell formulieren. | Weder die E8-Struktur noch die Reduktion eines festen endlichen Sektors löst diese Komplexitätsfrage. |

Diese Einträge sind Lösungswege mit benannten fehlenden Beweisen, keine als Lösungen umetikettierten offenen Aufgaben. Eine vollständige Lösung aller mathematischen und physikalischen Fragen lässt sich aus den vorliegenden Daten nicht seriös behaupten.

## 12. Was Einfachheit hier sinnvoll bedeutet

Eine kurze Formel ist besonders wertvoll, wenn sie Voraussetzungen reduziert oder viele Folgen gleichzeitig erzwingt. Hier leisten das die Lochidentität, der 2×2-Viererblock, die Besetzungsformel und die kleine Kontrollalgebra.

Eine kompakte Sprache allein wählt dagegen weder Zustand noch Raum. Der bereits im Hauptbuch vorgeschlagene positive Historienkern ist ein guter gemeinsamer Rahmen; er ist keine neue Entdeckung dieser Runde und ersetzt keine Auswahl von \(\omega\) und den zulässigen Wörtern.

Als konkrete Arbeitshypothese bleibt:

> Teilchen sind zugängliche Änderungen eines gemeinsam belegten Systems. Räumliche Beziehungen sollen durch die gegenseitige Erreichbarkeit seiner physisch zugänglichen Teile bestimmt werden. Alle Antworten müssen aus derselben Zustands- und Operationswahl stammen.

Der erste Satz besitzt jetzt einen weiteren exakten lokalen Zeugen. Der zweite und die physische Eindeutigkeit des dritten sind Forschungsaufgaben.

## 13. Der nächste entscheidende Nachweis

**Der nächste Hauptschritt sollte die geladene Feldantwort auf dem tatsächlich ausgewählten nativen Hintergrund sein.** Der neue Viererblock liefert dafür einen vollständig lösbaren Referenzfall, an dem ein allgemeiner Ansatz seine Ladungen, Phasen und Normen richtig reproduzieren muss.

Die konkrete Reihenfolge ist:

1. Den behaupteten N=64-Grundzustandsvertrag einschließlich Energieterm und physischer Sektorauswahl festhalten. Seinen vorhandenen Beweis gezielt revalidieren, soweit er als Voraussetzung benutzt wird.
2. \(\langle N_b\rangle\), die daraus folgende Summe \(Z=23\langle N_b\rangle/480\) und die tatsächlichen Spektralanteile der Felder f und chi berechnen. Die Summenregel muss von der aufgelösten Spektralantwort erfüllt werden.
3. Eine durch die Quelle erlaubte Kopplung zweier Teilalgebren angeben und prüfen, ob diese *ungerade* Anregung wirklich übertragen wird. Bei ausschließlich lokal geraden Bankoperationen ist das Ergebnis bereits algebraisch null; eine andere zulässige Quelloperation muss daher ausdrücklich identifiziert werden.
4. Erst mit diesem gemeinsamen Vertrag räumliche Skalierung, Chiralität und universelle Ausbreitung untersuchen.

Erfolg wäre derselbe Hintergrund, dieselbe Felddefinition und dieselbe ursprüngliche Operationsquelle in allen drei ersten Schritten. Ein zusätzlicher Wunschzustand oder frei eingesetzter Fermionhop würde diesen Nachweis nicht erfüllen.

## 14. Evidenz und Reproduktion

Das begleitende ZIP enthält die beiden eigenen Prüfer, den gepinnten Tensor, Berichte, Quellenmanifest und einen Replay-Einstieg. Die kleine Algebra, die N=3-Polynomidentität, die J-Beziehungen und die neuen Vierervektoren werden aus dem Tensor berechnet. Die Paket-Ausführung benötigt Python mit NumPy, SciPy und SymPy; sie benötigt keine absoluten Pfade zu früheren Forschungsprogrammen.

- Eigener Basistest: 54 exakte Prüfbedingungen.
- Eigener Vierer-/Lochtest: 191 exakte Prüfbedingungen einschließlich der 54 wiederverwendeten Basisbedingungen. Diese Zahlen dürfen nicht zu 245 unabhängigen Bedingungen oder Entdeckungen addiert werden.
- Beide eigenen Programme: normal und unter `-OO`, jeweils bytegleiche Berichte.
- Zusätzlich erneut ausgeführte Originalprüfer: N=3 und kubischer E8-Anschluss, ebenfalls normal und unter `-OO` bytegleich. Ihre Berichte sind als gesonderte Evidenz beigelegt.
- Die allgemeinen Antikommutator-, Symmetrie- und Unbeobachtbarkeitssätze werden im Text analytisch hergeleitet. Endliche Gegenprüfungen ersetzen weder diese Beweise noch einen unendlichen Grenzwertsatz.
- Dezimalwerte für Energien sind Auswertungen der angegebenen exakten Wurzelausdrücke, keine Eigenwertbeweise aus numerischer Rundung.

Nicht durchgeführt: formale Lean-Verifikation dieser neuen Sätze, externe Begutachtung, vollständiger frischer C16-/N=64-Audit, Kontinuumsbeweis oder experimentelle Prüfung. Kein T1–T8-Tor wird als vollständig geschlossen markiert.

**Fazit:** Eine konkrete bisher offene Anschlussfrage lässt sich tatsächlich durch eine einfachere Sicht auf denselben Zustand lösen: Der Dreierkomposit ist ein Loch des Viererhintergrunds. Die verbleibende Hauptfrage ist nun, weshalb und wie das physische System den passenden gemeinsamen Hintergrund und seine räumlichen Zugriffe bereitstellt.
