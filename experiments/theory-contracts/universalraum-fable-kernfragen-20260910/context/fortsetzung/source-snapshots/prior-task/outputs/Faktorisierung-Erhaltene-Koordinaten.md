# Erhaltene Determinantenkoordinaten: ein exakter positiver Auslesesatz

10. September 2026. Begrenzte Fortsetzung des ursprünglichen Universalraum-Modells. Die getrennte Koordinatenauslese ist vorhandene Projektarbeit; der hier ausgeschriebene Verteilungssatz und sein Vergleich betreffen genau den uniformen Gaußmatrix-Sampler. Kein Anspruch auf weltweite Neuheit oder einen neuen schnellen allgemeinen Faktorisierungsalgorithmus.

## 1. Quelle, Markierung und ursprüngliche Grenze

Die Quelle vom 9. September zieht die acht reellen Einträge von

\[
A\in M_2((\mathbb Z/N\mathbb Z)[i]),\qquad i^2=-1,
\]

unabhängig und gleichverteilt. Sie berechnet \(Z=\det A=x+iy\) und übergibt bisher allein \(x^2+y^2\) an den ggT-Leser. Original: `/Users/stefanhamann/Documents/Codex/2026-09-09/un/outputs/primitive-prozesse/Untersuchung.md`, Zeilen 153–197. Die dortige exponentielle Probenschranke ist ausdrücklich auf Quelle **und Normsignatur** beschränkt.

Die Markierung ist Teil des vorher rekonstruierten gemeinsamen Objekts: ganzzahlige gaußsche Ordnung, ausgezeichnetes komplexes Zentrum und Adjungierung. Im Ankerkommutanten ist \(a=iI\); die maximal geordnete Darstellung \(\mathcal M=P M_2(\mathbb Z[i])P^{-1}\) ändert die Determinante nicht. Die reellen Koordinaten lassen sich daher schon aus derselben arithmetischen Probe lesen. Für ungerades N wäre auch \(x=(Z+Z^*)/2\), \(y=(Z-Z^*)/(2i)\) möglich; die Implementierung besitzt beide Koeffizienten ohnehin.

Der Leser prüft zusätzlich

\[
g_x=\gcd(N,x),\qquad g_y=\gcd(N,y).
\]

Jeder Wert strikt zwischen 1 und N ist ein Faktor. Das Verfahren benutzt zur Ausführung nur N und frische Zufallsbits. Die Primfaktoren p,q werden ausschließlich in Beweis und separater Testauswertung verwendet.

Vorarbeit: `/Users/stefanhamann/Documents/Codex/2026-09-05/unt/work/pfaffian_prime_selector_20260909x/MATHEMATIK.md`, Zeilen 74–99. Dort wurde genau diese Idee für Pfaffiankoordinaten nachträglich empirisch geprüft; die Gleichverteilung der tatsächlichen Gatewörter war ausdrücklich **nicht** bewiesen. Hier sind A-Einträge per Definition uniform, und die davon erzeugte Determinantenverteilung wird vollständig hergeleitet. Es wird keine Verteilungsaussage von Gatewörtern übernommen.

## 2. Lokaler Verteilungssatz

Sei p eine ungerade Primzahl mit \(p\equiv3\pmod4\). Dann ist \((\mathbb Z/p\mathbb Z)[i]=\mathbb F_{p^2}\). Setze

\[
a_p=p^{-2}+p^{-4}-p^{-6},\qquad
b_p=p^{-2}-p^{-6},\qquad c_p=(p-1)b_p.
\]

Für die uniforme Zweiermatrix über diesem Körper gilt

\[
\Pr(Z=0)=a_p,\qquad \Pr(Z=z)=b_p\quad(z\ne0).
\]

**Beweis.** Für einen Körper mit Q Elementen gibt es \((Q^2-1)(Q^2-Q)\) invertierbare Zweiermatrizen. Ihre Determinanten sind auf \(\mathbb F_Q^*\) gleichverteilt: Multiplikation mit \(\operatorname{diag}(t,1)\) vermittelt zwischen den Fasern. Jede nichtverschwindende Faser hat deshalb \(Q^3-Q\) Elemente. Division durch \(Q^4\) und Q=p² ergibt b_p. Die verbleibende Nullfaser hat \(Q^3+Q^2-Q\) Elemente und ergibt a_p. ∎

Insbesondere ist die Verteilung genau die Mischung

\[
\mathcal L(Z)=(1-p^{-4})\operatorname{Unif}(\mathbb F_{p^2})+p^{-4}\delta_0.
\]

Die vier Signaturen \((1_{x=0},1_{y=0})\) haben Wahrscheinlichkeiten

| Signatur | Wahrscheinlichkeit |
|---|---:|
| (1,1) | \(a_p\) |
| (1,0) | \(c_p\) |
| (0,1) | \(c_p\) |
| (0,0) | \(d_p=(p-1)c_p\) |

Damit beträgt die lokale Nullwahrscheinlichkeit eines einzelnen Koordinatenlesers

\[
u_p=a_p+c_p=p^{-1}+p^{-4}-p^{-5}.
\]

Der Normleser verlangt an dieser Stelle die gemeinsame Nullheit beider Koordinaten und sieht nur a_p.

## 3. Exakte Paartrennung und strikte Verbesserung

Sei nun \(N=pq\), mit verschiedenen ungeraden Primzahlen \(p,q\equiv3\pmod4\). Die gewählte öffentliche Gleichverteilung erzeugt durch CRT unabhängige lokale Matrizen und damit unabhängige lokale Signaturen. Der Normleser trennt die Faktoren mit

\[
\rho_{\rm Norm}=a_p+a_q-2a_pa_q.
\]

Mindestens ein Koordinaten-ggT ist genau dann echt, wenn sich die beiden **Zweibit-Signaturen** unterscheiden. Deshalb

\[
\rho_{\rm Koord}=1-a_pa_q-2c_pc_q-d_pd_q.
\]

Es folgt die positive exakte Identität

\[
\boxed{\rho_{\rm Koord}-\rho_{\rm Norm}
=2(p+q-1)c_pc_q>0.}
\]

**Beweis der Differenz.** Unter den vom Normleser nicht getrennten Fällen haben beide Signaturen entweder (1,1), oder beide liegen in der dreielementigen Menge {(1,0),(0,1),(0,0)}. Der erste Fall ist nicht weiter trennbar. Im zweiten Fall sind die zusätzlichen unterschiedlichen Paare von Gesamtwahrscheinlichkeit \(2c_pc_q+2d_pc_q+2c_pd_q\). Mit \(d_p=(p-1)c_p\) ergibt sich die Formel. ∎

Dies ist auch eine **punktweise Dominanz**: Hat die Norm an p die Signatur (1,1) und an q eine andere, ist mindestens ein Koordinaten-ggT echt. Entsprechendes gilt vertauscht. Die Aussage verallgemeinert sich punktweise auf quadratfreies N mit ausschließlich inerten Primteilern. Die ausgeschriebene Wahrscheinlichkeitsformel gilt für genau zwei verschiedene Primteiler.

Für beliebige N kann der alte Norm-ggT als dritter Leser erhalten bleiben. Das garantiert trivialerweise, dass kein alter Normerfolg verloren geht; die obige exakte Formel wird dadurch nicht auf gespaltene Primzahlen oder Primzahlpotenzen ausgedehnt.

Ein minimaler markierter Zeuge ist N=77 und \(Z=7+i\), realisierbar durch \(A=\operatorname{diag}(1,Z)\): \(\gcd(77,|Z|^2)=\gcd(77,50)=1\), aber \(\gcd(77,\Re Z)=7\). Dieser bewusst kleine Anschauungszeuge ist kein blind gewonnenes Faktorisierungsergebnis.

## 4. Vollständige Kosten und Reichweite

Ein Versuch benötigt dieselben acht uniformen reellen Reste und dieselbe Determinante. Mit der einfachen Schulformel sind das acht reelle modulare Produkte für die zwei komplexen Produkte; der bisherige Normwert benötigt zwei weitere Quadrate. Die Ergänzung kostet höchstens **zwei zusätzliche ggT**, keine zusätzliche modulare Multiplikation. Alle Operanden haben O(log N) Bits. Rejection Sampling der acht uniformen Reste hat konstante erwartete Wiederholungszahl je Rest; es wird kein gleichverteilter unbekannter Faktor vorausgesetzt.

Auf Eingaben mit p≤q≤2p gilt asymptotisch

\[
\rho_{\rm Norm}=\Theta(N^{-1}),\qquad
\rho_{\rm Koord}=\Theta(N^{-1/2}).
\]

Das folgt direkt aus \(a_p\sim p^{-2}\), \(c_p\sim p^{-1}\) und der positiven Differenzformel. Bei frischen unabhängigen Versuchen ist die Misserfolgswahrscheinlichkeit exakt \((1-\rho)^k\), also

\[
k=\left\lceil\frac{\log\varepsilon}{\log(1-\rho)}\right\rceil.
\]

Der neue Leser braucht daher \(\Theta(\sqrt N\log(1/\varepsilon))\) statt \(\Theta(N\log(1/\varepsilon))\) Versuche in dieser Klasse. **Beide Größen wachsen exponentiell in der Eingabebitlänge.** Dies ist ein bewiesener Gewinn gegenüber einem informationsärmeren Leser derselben Quelle, kein Vorteil gegenüber klassischen Faktorisierungsverfahren. Zwei gewöhnliche uniforme skalare Reste erzielen bereits dieselbe führende Größenordnung mit weniger Quellenaufwand. Die genaue lokale Mischung oben macht diese Grenze sichtbar.

## 5. Exakte endliche Prüfung

`coordinate_reader_check.py` enthält ausschließlich eigenen elementaren Ganzzahlcode. Er importiert keine fremden Versuchsskripte. Für p=3 werden sämtliche 9⁴=6561 Matrizen direkt enumeriert. Zusätzlich werden für p=3,7,11,19 die vollständigen Determinantenverteilungen aus den unabhängig ausgezählten Körperprodukten und ihrer gewichteten Differenzfaltung bestimmt. Diese Faltung zählt **alle** Matrizen mit exakten Vielfachheiten; sie ist keine Zufallsstichprobe und keine direkte Enumeration aller p⁸ Matrizen.

Die CRT-Prüfung läuft für alle Paare unter {3,7,11} sowie für (11,19). Sie enumeriert alle \(p^2q^2\) möglichen Determinantenpaare und vergleicht tatsächliche Ganzzahl-ggT mit den Signaturformeln, einschließlich punktweiser Dominanz und der exakten positiven Differenz. Die Faktoren gehören nur zum Prüfer, nicht zum Samplervertrag.

| N | Determinantenpaare vollständig geprüft | Normerfolg | Koordinatenerfolg |
|---:|---:|---:|---:|
| 21 | 441 | 0,1378185 | 0,6213661 |
| 33 | 1089 | 0,1283828 | 0,5999578 |
| 77 | 5929 | 0,0288015 | 0,3727062 |
| 209 | 43681 | 0,0110636 | 0,2500510 |

Alle Kontrollen bestanden. `coordinate-reader-result.json` und die vollständige Aufzeichnung `coordinate-reader-stdout.json` enthalten die rationalen Wahrscheinlichkeiten, Zählgewichte und zusätzlichen Leserzeugen. Die allgemeinen Aussagen beruhen auf den obigen Beweisen; die endlichen Kontrollen sichern Rechnung und Modellgrenze.


# Tatsächliche Ausführung des erhaltenen Koordinatenlesers

`public_reader.py` ist eine zusätzlich ausführbare Umsetzung des besprochenen öffentlichen Samplers. Eingaben sind ausschließlich N, Startwert und Probenbudget. Der Algorithmus erhält keine Primfaktoren, keine Teilerliste und keine vorbereiteten informativen Matrizen. Er zieht acht Reste, bildet die gaußsche Determinante und prüft Real-, Imaginär- und Norm-ggT. Der Normleser bleibt als Kontrolle und für allgemeine N erhalten.

Die Startwerte 1, 2 und 3 wurden durchgehend verwendet. Die überprüften echten Zerlegungen umfassen:

| Eingabe | gefundene Zerlegung | Proben bei Startwerten 1 / 2 / 3 |
|---:|---|---:|
| 77 | 7 × 11 | 2 / 2 / 15 |
| 209 | 11 × 19 | 4 / 4 / 1 |
| 16.088.057 | 4.003 × 4.019 | 938 / 165 / 1.463 |
| 4.294.049.741 | 65.519 × 65.539 | 18.935 / 879 / 22.892 |

In diesen zwölf Läufen lieferte jeweils ein Koordinaten-ggT den Faktor, während der Norm-ggT **derselben erfolgreichen Probe** keinen Faktor lieferte. Es wurde nicht gemessen, wann der Normleser bei Fortsetzung des Zufallsstroms erstmals erfolgreich wäre; eine solche Behauptung folgt aus diesen Daten nicht. Jede ausgegebene Zerlegung wurde durch Ganzzahlmultiplikation geprüft. Die Aussage über Primzahlen und Restklassen stammt aus separater Prüfarbeitslogik, die dem Leser nicht zugänglich ist.

Die erste Ausführungsdatei enthält außerdem unverändert drei Läufe für die versehentlich zusätzlich gewählte allgemeine Zahl 4.295.098.341. Sie besitzt einen kleinen Faktor 3; diese Läufe werden nicht als balancierte Semiprimzahltests ausgegeben. Der korrekte balancierte 32-Bit-Test liegt separat in `public-reader-32bit-runs.json`. Damit bleibt die vollständige Versuchsgeschichte erhalten.

Dies sind kleine Funktionsdemonstrationen, keine Leistungsvergleiche mit Pollard-Rho, ECM oder Siebverfahren. Pseudozufallsfolgen mit festen Startwerten dienen der Wiederholbarkeit; der allgemeine Verteilungssatz setzt unabhängige uniforme Reste voraus. Einschließlich Normkontrolle zählt der Ausführer zehn reelle modulare Produkte, drei ggT und acht Restziehungen je Versuch. Eine allgemeine polynomielle Laufzeit folgt daraus nicht.
