# Positiver RR/W-Anschluss: erweiterte Rekonstruktion und präzise Herkunftsgrenze

**Stand: 21. September 2026. Forschungs-ID `UR.RR.POSITIVE_SOURCE.01`. Gesamtverdict: PARTIAL.**

Der eingereichte positive Kandidat ist mathematisch konsistent. Seine elastische Paarantwort muss in den Quellenvergleich aufgenommen werden. Der bisherige Rekonstruktionssatz lässt sich dafür erweitern, ohne seine Eindeutigkeit innerhalb der erklärten globalen Klasse aufzugeben. Die vollständige TFPT-Lösung folgt daraus nicht: Die Abbildung von der ursprünglichen Quelle auf die zusammengesetzten Felder, die physische Zeit und die Zustandsauswahl sind noch nicht hergeleitet.

Die zentrale neue Verbindung lautet: **Die elastische Ergänzung sättigt die Positivitätsgrenze, hebt die statische virtuelle Paaranziehung exakt auf und erzeugt dadurch einen großen, analytisch bestimmbaren Nullraum.** Diese drei Eigenschaften gehören zu derselben Struktur. Sie sind keine drei unabhängigen Indizien für eine bereits ausgewählte physische Quelle.

## 1. Bestätigter Kandidat und erste zusätzliche Wahl

Auf dem vorgegebenen CAR/CCR-Fockraum mit 64 Fermion- und 60 Bosonmoden sei

\[
P_A=\sum_{i<j}W_{A,ij}f_jf_i,\quad WW^\dagger=8I_{60},\quad Q=N_f+2N_b.
\]

Die zusätzliche Feldliftregel setzt die aktive RR-Form auf die Operatoren \((P_A/\sqrt8,b_A)\) ein. Für \(\kappa>0\) ergibt sie

\[
H_+=2\kappa\sum_A(b_A+P_A/\sqrt8)^\dagger(b_A+P_A/\sqrt8)
=2\kappa N_b+\frac{\kappa}{\sqrt2}(X+X^\dagger)+\frac\kappa4D,
\]

\[
X=\sum_A b_A^\dagger P_A,\qquad D=\sum_A P_A^\dagger P_A.
\]

Der gemeinsame Spaltenoperator \(B=(b_A+P_A/\sqrt8)_A\) ist auf \(\operatorname{Dom}N_b^{1/2}\) geschlossen; seine positive Quadratform liefert die selbstadjungierte Realisierung. Alle festen Q-Sektoren sind endlichdimensional. Der Operator erhält Q und erzeugt sowohl unitäre Zeitentwicklung als auch einen positiven euklidischen Transfer.

Für \(|p_A\rangle=P_A^\dagger|0\rangle/\sqrt8\) und \(|b_A\rangle=b_A^\dagger|0\rangle\) ist der jeweilige Zweiraum invariant und

\[
H_+|_A=\kappa\begin{pmatrix}2&2\\2&2\end{pmatrix}.
\]

Der Austausch bei \(t=\pi/(4\kappa)\) und die Rückkehr bei \(t=\pi/(2\kappa)\) stimmen exakt. Der Faktor \(\kappa\) ist dabei eine erklärte Zeitskala, kein hergeleiteter physischer Messwert.

Die natürliche 60-dimensionale Zielrepräsentation und W sind vorhandene TFPT-Daten. Ihre Verknüpfung mit den zwei aktiven Quellenrichtungen durch genau diese Operatorauswertung ist die noch zusätzlich gewählte Brücke.

## 2. Die Rekonstruktion bleibt mit elastischer Antwort erhalten

Schreibe \(a_{ij}=f_jf_i\) und \(D(V)=a^\dagger Va\), wobei V auf \(\Lambda^2\mathbb C^{64}\) wirkt. Ersetze die alte zahlenmatrixwertige fermionische Antwort durch

\[
\{[f_i,H],f_j^\dagger\}=h_{ij}I+\{[f_i,D(V)],f_j^\dagger\}.
\]

Die bosonische untere Antwort bleibe global

\[
[[b_A,H],b_B^\dagger]=\Omega_{AB}I.
\]

Vorausgesetzt bleiben die volle irreduzible Fockdarstellung, starke Q-Erhaltung, ein gemeinsamer invarianten Endlichteilchenkern und eine einzige globale untere Energieschranke. Dies sind Operatoridentitäten auf dem gesamten Kern, keine Schlussfolgerungen aus einzelnen Messzuständen.

Da \(D(V)\) auf dem endlichen Fermionraum beschränkt ist, fällt \(H-D(V)\) in die frühere Klasse. Der Stabilitätsbeweis entfernt weiterhin alle reinen Umwandlungen vom Grad \(m\ge3\). Folglich

\[
H=cI+d\Gamma_f(h)+d\Gamma_b(\Omega)+D(V)+T_1+T_1^\dagger+T_2+T_2^\dagger.
\]

Die vollständige Kompression auf \(Q\le4\) bestimmt eindeutig

\[
\boxed{(c,h,\Omega,V,C_1,C_2).}
\]

Dabei werden c aus dem Vakuum, h aus einem Fermion, Ω aus einem Boson, V aus dem verbleibenden Zweifermionblock, C₁ aus Paar→Boson und C₂ aus Vierfermion→Zweiboson abgelesen. V muss nicht vorab passend eingesetzt werden: Es wird aus der Q=2-Antwort bestimmt. Zusätzlich ist unabhängig zu beweisen, dass seine globale Antwort die ganze nichtskalare Fermionantwort erfasst.

Für den positiven Kandidaten sind diese Daten

\[
(c,h,\Omega,V,C_1,C_2)
=\left(0,0,2\kappa I,\frac\kappa4W^\dagger W,\frac\kappa{\sqrt2}W,0\right).
\]

Die Forderung V=0 ist also keine allgemeine physische Notwendigkeit. Umgekehrt bleiben globale Antwortannahmen notwendig: Beliebige positive Operatoren sind nicht allein aus Q≤4 rekonstruierbar.

## 3. Elastische Antwort, statische Aufhebung und dynamische Pole

Im Q=2-Sektor ist

\[
H_2=\begin{pmatrix}V&C^\dagger\\C&\Omega\end{pmatrix},\qquad
V=C^\dagger\Omega^{-1}C.
\]

Für \(z\ne2\kappa\) liefert die exakte Eliminierung des Bosonblocks

\[
H_{\rm eff}(z)=V+C^\dagger(z-\Omega)^{-1}C
=\frac{\kappa z}{4(z-2\kappa)}W^\dagger W
=\frac{2\kappa z}{z-2\kappa}\Pi_W,
\quad \Pi_W=W^\dagger W/8.
\]

Damit verschwindet die effektive Paarantwort bei z=0 exakt. Der positive elastische Term hebt die virtuelle statische Bosonantwort auf. Der auf die Paarrichtungen komprimierte Resolvent ist, außerhalb des Spektrums,

\[
P_{2F}(z-H_2)^{-1}P_{2F}
=\frac{I-\Pi_W}{z}+\frac{z-2\kappa}{z(z-4\kappa)}\Pi_W.
\]

In jedem hellen Paarzustand liegen die spektralen Gewichte je zur Hälfte bei 0 und 4κ. Der scheinbare Pol bei 2κ in der eliminierten Beschreibung ist kein Eigenwert des hellen vollen Blocks; im vollen Paarresolvent liegt dort eine Nullstelle.

Dies ist eine endliche Q=2-Operatoraussage, keine hergeleitete räumliche Streumatrix oder Aussage über reale Teilchenmassen. Das verwendete allgemeine Verfahren ist die bekannte [Feshbach–Schur-Abbildung von Dusson, Sigal und Stamm](https://arxiv.org/abs/2105.02058); die konkrete Formel hier folgt direkt aus den angegebenen Matrizen.

## 4. Aktive Kompression und vollständige RR-Wirkung sauber verbinden

Der vorliegende fünfteilige RR-Träger besitzt im erklärten Hardy-Vertrag

\[
\operatorname{spec}h_{RR}=\{0,1,2,3,4\},\qquad
Re_n=i^ne_n,\qquad Sh_{RR}S=4I-h_{RR}.
\]

Die aktive Ebene ist keineswegs irgendeine willkürliche Zweiebene. Sie ist der Fixraum von R:

\[
P_{\rm act}=\frac14(I+R+R^2+R^3),\qquad
\operatorname{Ran}P_{\rm act}=\operatorname{span}(e_0,e_4).
\]

Dieser Projektor ist unter einer D4-invarianten Metrik orthogonal, D4-äquivariant und kommutiert mit dem erklärten hRR. Die verbleibende Herkunftsfrage lautet daher genauer: Warum verwendet die physische Quellenantwort genau diese Kompression, und wie übersetzt sie deren zwei Richtungen in die zusammengesetzten Felder?

Ein vollständiger zeitgetreuer Einbettungslift aller fünf RR-Richtungen in denselben Q=2-Sektor von H+ ist dagegen ausgeschlossen:

\[
\operatorname{spec}(H_+|_{Q=2})=0^{2016}\oplus(4\kappa)^{60}.
\]

Die Energien κ, 2κ und 3κ fehlen. Die 1956 dunklen Paarzustände bei Nullenergie können diese drei Frequenzen nicht ersetzen. Der Ausschluss betrifft genau einen injektiven Zeitintertwiner in diesen Sektor bei gleicher Zeitnormierung; er ist kein allgemeines Verbot anderer Quellenabbildungen.

Zugleich ist die bereits vorhandene vollständige RR/W-Darstellung weiterhin nutzbar. Ihr funktorieller innerer Generator KRR erfüllt aufgrund der W-Intertwineridentität

\[
[K_{RR},X]=0,\quad [K_{RR},N_b]=0,\quad [K_{RR},D]=0,
\quad\Rightarrow\quad [K_{RR},H_+]=0.
\]

Die ganze innere RR-Wirkung kann somit mit H+ verträglich sein. **Innerer RR-Generator und physischer Hamiltonoperator sind dabei verschiedene Operatoren.** Diese Unterscheidung erhält den vollständigen Clockbestand, ohne die fehlenden drei Frequenzen zu übergehen.

Ein globaler kanonischer Feldtausch \(b_A\leftrightarrow P_A/\sqrt8\) ist ebenfalls ausgeschlossen: Der Paar-Kommutator hat auf leerem Fermionraum den Wert +1, auf dem vollbesetzten Raum −1, während \([b_A,b_A^\dagger]=I\). Der aktive Zustandsaustausch bleibt davon unberührt. Die allgemeine Nichtkanonizität von Fermionpaaren ist auch Gegenstand der Primärarbeit [How bosonic is a pair of fermions?](https://arxiv.org/abs/1310.8488); hier ist die Abweichung direkt am nativen W geprüft.

## 5. Vollständiger Nullraum und robuste Grenze der Zustandsauswahl

Die kommutierenden reinen Paarvernichter liefern

\[
\ker H_+=\operatorname{Ran}S,\qquad
S\psi=e^{-X/\sqrt8}(|0_b\rangle\otimes\psi),
\]

\[
\dim\ker H_+=2^{64},\qquad
\dim(\ker H_+\cap\mathcal H_q)=\binom{64}{q},\quad0\le q\le64.
\]

Die Exponentialreihe endet nach höchstens 32 Schritten. Die Umkehrung folgt aus der eindeutigen Rekursion aller Bosonkomponenten aus der bosonleeren Komponente. S ist injektiv, aber nicht unitär. Der Satz wird analytisch bewiesen, nicht durch eine vermeintliche Gesamt-Fockdiagonalisierung.

Diese Struktur ist allgemein: Für Ω>0 und reine Paarvernichter Kₐ hat \((b+K)^\dagger\Omega(b+K)\) denselben durch die Bedingungen \((b_A+K_A)\Psi=0\) bestimmten Grundraum. Änderung der positiven Metrik Ω bei festem K wählt keinen einzelnen Zustand aus. Schur-Sättigung im Q=2-Block allein beweist die globale Quadratdarstellung allerdings nicht; die höheren Antwortdaten müssen ebenfalls passen.

Noch robuster ist folgende Aussage. Sei \(\widetilde H\ge0\) eine beliebige selbstadjungierte Erweiterung mit unveränderter Formkompression auf Q≤3. Für jeden dortigen Nullvektor x gilt

\[
0=\langle x,\widetilde Hx\rangle=\|\widetilde H^{1/2}x\|^2,
\]

in der Forminterpretation. Somit liegt x auch im globalen Kern. Daher

\[
\boxed{\dim\ker\widetilde H\ge1+64+2016+41664=43745.}
\]

Dazu muss die Erweiterung Q nicht einmal erhalten. Kopplungen an höhere Sektoren können die Positivitätsfolgerung nicht umgehen.

Die Schlussfolgerung ist begrenzt und konkret: Ein unsichtbarer positiver Zusatzterm kann unter diesen Voraussetzungen kein eindeutiges globales Vakuum auswählen. Eine physische Sektorauswahl, ein zusätzlicher Zustandsvertrag oder eine Änderung bereits bestimmter niedriger Antworten wäre nötig. Ein eindeutiges Weltvakuum wird nicht als allgemeines notwendiges Axiom jeder physikalischen Theorie behauptet.

## 6. Native unabhängige Kontrolle

Der gepinnte Tensor hat SHA-256 `3f00a0892157a691e4ef26920c3702772c7bf76a250fad98ff04a079bb64b763`, 480 signierte Einträge und WW†=8I. Der Checker bestätigt die aktive Matrix, den elastischen Projektor und die besetzungsabhängige Antwort

\[
R_{44}|0\rangle=0,\qquad
R_{44}f_{57}^\dagger|0\rangle=\frac\kappa4f_{57}^\dagger|0\rangle.
\]

Für die Q=3-Abbildung C₃ wird ganzzahlig das Gram-Polynom

\[
G(G-7I)(G-10I)(G-12I)=0,\qquad G=C_3C_3^\dagger
\]

geprüft. Exakte Projektorspuren liefern alle Multiplizitäten und damit

| Energie / κ | Multiplizität |
|---:|---:|
| 0 | 41664 |
| 2 | 64 |
| 15/4 | 2880 |
| 9/2 | 576 |
| 5 | 320 |

Dies erfasst alle 45504 Zustände. Der Nachweis braucht keine dichte Gesamtmatrix. Analytische allgemeine Sätze, native exakte Kontrollen und Quellenprüfung sind im Paket getrennt dokumentiert.

## 7. Was zur vollständigen Lösung fehlt und welcher Ansatz jetzt begründet ist

Die Quelle muss nicht rückwirkend an den alten Hamiltonoperator ohne elastischen Term angepasst werden. Der beste Anschluss verwendet die geometrisch ausgezeichnete aktive Kompression und prüft ihren unabhängigen Feldadapter gegen **alle** sechs rekonstruierten Daten (c,h,Ω,V,C₁,C₂). Dabei bleibt die vollständige RR-Darstellung als innere Symmetrie sichtbar.

Ein prüfbarer Quellenvertrag braucht ein positives, graduiertes Quellenfunktional beziehungsweise einen Transfer samt Einsetzungsabbildung der Felder, aus dem auf einem gemeinsamen Hilbertraum entstehen:

1. die CAR/CCR-Struktur, Ladungen, Adjunktionen und der W-Kanal;
2. die gemeinsame erste Zeitantwort einschließlich V und C₁ sowie der direkte Q=4-Block C₂;
3. die globalen Antwortidentitäten der erweiterten Rekonstruktionsklasse;
4. Zeitnormierung und Zustands- beziehungsweise Sektorauswahl.

Der vorhandene RR-Träger, sein innerer Clocklift und W bestimmen diesen Quellenvertrag bislang nicht. Die positive Formauswertung konstruiert einen Kandidaten für dessen Ergebnis. Sie ist nicht bereits die unabhängige Herleitung des Funktionals. Eine Quelle aus dem gewünschten H+ rückwärts zu definieren würde diese Lücke lediglich in eine Definition verschieben.

Darüber hinaus bleiben lokale chirale 3+1D-Materie und Eichfelder, das wechselwirkende Kontinuum, gemeinsame physische Kopplungs-/Skalennormierungen, Quantengravitation und kosmologischer Zustand eigenständige Aufgaben. Die vorhandenen E8-, Standardmodell-, Flavor-, Alpha- und Clockresultate bleiben dabei erhalten; sie werden durch diesen endlichen Quellenkandidaten weder ersetzt noch zu einem Abschluss hochgestuft.

**Die physischen T1–T8-Gates bleiben offen.** Das ist keine Widerlegung von TFPT. Es ist die genaue Grenze der hier bewiesenen Fortsetzung: positiver Kandidat und erweiterte Rekonstruktion stehen; der ursprüngliche gemeinsame Feld-, Zustands- und Zeitvertrag steht noch aus.

## 8. Fortschrittsurteil nach erneuter Prüfung der Ursprungsregeln

Die aktuelle Rechnung schließt keinen der acht physischen Gesamtverträge. Sie verbessert die zulässige Rekonstruktionsklasse und beendet zwei konkrete Fehlidentifikationen. Daraus lässt sich kein Abstand in Prozent zur vollständigen Lösung ableiten.

Die Originalfassung von `tfpt_1_architecture_e8.tex`, Zeilen 167–187, führt P1 als primitiven Randkern und P2 als Trägerschnittstelle. Die Trägerschnittstelle ist dort ausdrücklich von ihren algebraischen Folgerungen getrennt. Die Wick-Funktor-Passage, Zeilen 1317–1448, trennt vorhandene Compilerrollen, berechnete Zustandskandidaten und die weiterhin fehlende physische Realisierung. Der jüngere Contract `compiler-vacuum-current-cubic-20260918` bestätigt bereits einen nichtverschwindenden ursprünglichen affinen Kubikterm, kennzeichnet aber den Raumzeit-/Feldanschluss als unhergeleitet. Diese Befunde dürfen weder zu „alles fehlt“ noch zu „der gemeinsame Hamiltonoperator ist damit ausgewählt“ verkürzt werden.

Der Vergleich ist gezielt, keine behauptete vollständige Nichtableitbarkeit aus sämtlichen TFPT-Bedingungen. Aus den untersuchten Originalregeln ergibt sich derzeit keine nachgewiesene Einsetzungsregel, welche die aktive RR-Kompression in genau den gemeinsamen CAR/CCR-Transfer überführt. Weitere Spektren des nach dieser Regel definierten H+ wären daher kein Fortschritt an dieser Herkunftsfrage. Dieser bedingte Modellzweig ist für die hier gestellte Herkunftsfrage ausgeschöpft, bis ein unabhängiger Quellenadapter oder eine neue tatsächlich begründete Auswahlbedingung vorliegt.
