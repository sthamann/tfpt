# TFPT / Universalraum: einfache lokale Schließung und geprüfte Schnittstellen

**Forschungsfortsetzung und Quellenkonsolidierung v1.6.2 · 15. September 2026**

Diese Ausgabe verbindet die eigene Fortsetzung von v1.6.1 mit drei während
der Untersuchung gelieferten externen Texten. Sie ist ein Forschungsnachtrag,
keine verkürzte Neuausgabe des Hauptdokuments. Haupt- und Update-PDF v1.6
wurden in dieser Runde nicht verändert. Kein vollständiges T1–T8-Tor
wird geschlossen.

## 1. Ergebnis in einem Absatz

Der kubische 64er-Sektor ist exakt als Lochraum der ursprünglichen Fermionen
auf einer bestimmten Ladung-vier-Referenz realisiert. Seine Entnahmeantwort
und die vollständige ursprüngliche Fermion-Additionsantwort schließen in
kleinen endlichen Räumen. Die extern vorgeschlagene 5×3-Blockstruktur,
die kleine Kontrollalgebra, die Dichteformel für Kompositnormen sowie mehrere
Matrix- und Präparationsvereinfachungen sind bestätigt. Zwei vorgeschlagene
Abkürzungen tragen dagegen nicht: Der nichtverschwindende reine
Vier-Fermion-Kandidat ist nicht SU(4)-invariant, und der vorhandene Paartensor
verschwindet unter der naiven skalaren Weylfeld-Zuordnung. Der untersuchte
Lochhintergrund ist außerdem im schwachen Bereich nicht einmal Grundzustand
des vollständigen N=4-Sektors.

**Die lokale Algebra wird einfacher. Die physische Wahl von Zustand,
zugänglichen Operationen und räumlicher Feldzuordnung bleibt die gemeinsame
offene Verbindung.**

## 2. Welche Eingaben geprüft wurden

| Quelle | Kennzeichnung und Behandlung |
|---|---|
| Eigene v1.6.1-Fortsetzung | Gepinnte N=3- und kubische Prüfer erneut als Grundlage ausgeführt. |
| Externer Text A, 5×3 / Hodge / Quartik | Anhang ce1caa25; vollständig gelesen, neue Behauptungen am ursprünglichen Tensor unabhängig geprüft. |
| Externer Text B, Lochanschluss | Anhang 8793637f; vollständig gelesen, verlinkte 437-zeilige Forschungsnotiz gelesen und fremdes Prüfpaket unverändert in einer separaten Kopie normal sowie optimiert wiederholt. |
| Externer Text C, kleine Schnittstellen | Anhang 74f60e7d; vollständig gelesen, konkrete Matrix-, Präparations-, Transport- und Feldtypformeln unabhängig geprüft. |

Die im dritten Text genannten ursprünglichen 279/947-Prüfer sind über seine
abschließenden Inhaltsreferenzen nicht unmittelbar als Dateien bezeichnet.
Ihr Original-Replay wird hier deshalb nicht behauptet. Die unten angegebenen
eigenen Prüfungen sind davon unabhängig.

Arbeitsaufforderungen innerhalb der Eingaben wurden als Quelleninhalt
behandelt, nicht als zusätzliche Autorisierung. Die Quellen wurden nicht
verändert. Ein vollständiger frischer N=64-/C16-Audit ist nicht Bestandteil
dieser Runde.

## 3. Ein unveränderter Hamiltonoperator

Die eigene Rechnung verwendet weiterhin

\[
H=\Delta N_b+g\sum_{A=1}^{60}(b_A^\dagger P_A+P_A^\dagger b_A),\qquad
P_A=\sum_{i<j}W_{A,ij}f_jf_i,\qquad N=N_f+2N_b,
\]

mit \(\Delta,g>0\), 64 ursprünglichen Fermionmodi, 60 Bosonmodi und
\(WW^\dagger=8I_{60}\). Die ursprünglichen Fermionen erfüllen die CAR.
Es wird kein neuer Hopping-, Kondensat- oder Quartikterm hinzugefügt.

Aus v1.6.1 stammen die exakten Relationen

\[
C_3:\Lambda^3\mathbb C^{64}\longrightarrow
\mathbb C^{60}\otimes\mathbb C^{64},\qquad
JC_3=0,\quad JJ^\dagger=15I_{64},
\]

\[
\chi_r^\dagger|0\rangle=
\frac1{\sqrt{15}}\sum_{A,s}J_{r;A,s}b_A^\dagger f_s^\dagger|0\rangle,
\qquad H\chi_r^\dagger|0\rangle=\Delta\chi_r^\dagger|0\rangle.
\]

Die \(\chi_r\) sind global **keine** freien kanonischen Fermionen.
Eine lokale Zustandsidentität darf diesen früheren Gegenbeweis nicht
überschreiben.

## 4. Der genaue Lochanschluss und seine unabhängige Bestätigung

Für den Bosonindex \(A=(k,ab)\) bezeichnet \(\bar A\) das entgegengesetzte
Vektorlabel mit komplementärem Farbpaar \(cd\). Setze
\(\eta_A=\varepsilon_{abcd}\). Es gilt
\(\bar{\bar A}=A\), \(\eta_{\bar A}=\eta_A\), \(\bar A\ne A\).

Definiere

\[
K^\dagger=\frac12\sum_A\eta_A b_A^\dagger b_{\bar A}^\dagger,\qquad
R^\dagger=\sum_A\eta_A b_A^\dagger P_{\bar A}^\dagger,
\]

\[
|B\rangle=K^\dagger|0\rangle/\sqrt{30},\qquad
|R\rangle=R^\dagger|0\rangle/\sqrt{480}.
\]

Die ursprüngliche Besetzungsrechnung ergibt

\[
H\big|_{\operatorname{span}(B,R)}
=\begin{pmatrix}2\Delta&4g\\4g&\Delta\end{pmatrix}.
\]

Alle möglichen Ausgänge in vier freie Fermionen heben sich exakt auf.
Ein solcher zweidimensionaler N=4-Singulettblock war bereits früher
berichtet; neu ist hier seine Verbindung zum kubischen Sektor, nicht
die erstmalige Existenz des Blocks.

Für alle 64 Modi wurde unabhängig nachgerechnet:

\[
\boxed{f_r|R\rangle=-\frac1{\sqrt{32}}\chi_r^\dagger|0\rangle.}
\]

Der externe Text B definiert stattdessen

\[
|Q_4\rangle=\frac1{\sqrt{128}}\sum_r f_r^\dagger\chi_r^\dagger|0\rangle.
\]

Die genaue Gegenüberstellung liefert \(|Q_4\rangle=-|R\rangle\).
Das externe Pluszeichen in der Lochidentität ist somit nur die globale
Referenzphase. Die beiden Untersuchungen stimmen überein.

Der Ladungsanschluss lautet vollständig \(4-1=3\), nicht bloß modulo vier.
Es gilt keine globale Operatorgleichung \(f_r=\chi_r^\dagger\).
Die beiden Operationen beginnen auf verschiedenen Hintergründen und
erzeugen denselben Ausgangszustand.

Die Referenzpaarung wurde zusätzlich gegen sämtliche 45 Spin(10)- und
15 SU(4)-Liealgebrageneratoren zusammen mit der Quelltensor-Kovarianz
geprüft: Sie ist ein Singulett, nicht lediglich ein Zustand mit Gewicht null.

## 5. Eigene neue Fortsetzung: die gesamte Einteilchen-Antwort

### 5.1 Entfernen: genau eine Linie

Setze

\[
\Omega_4=\sqrt{\Delta^2+64g^2},\qquad E_\pm=(3\Delta\pm\Omega_4)/2,
\]

\[
|E_-\rangle=v|B\rangle+u|R\rangle,\quad
u^2=(1+\Delta/\Omega_4)/2,\quad v=-\sqrt{1-u^2},\quad u>0.
\]

Dann gilt

\[
\langle E_-|f_r^\dagger(t)f_s|E_-\rangle
=\delta_{rs}\frac{u^2}{32}e^{-i\epsilon_h t/\hbar},\qquad
\epsilon_h=(\Omega_4-\Delta)/2.
\]

Bei \(g/\Delta=1/20\) sind
\(\epsilon_h/\Delta=(\sqrt{29}-5)/10\) und
\(Z_h=u^2/32=(1+5/\sqrt{29})/64\).
Dieser Testwert wird nicht durch die Rechnung ausgewählt.

### 5.2 Hinzufügen: ein exakt geschlossener Viererraum

Die vollständige Antwort von \(f_r^\dagger|E_-\rangle\) schließt im
N=5-Sektor auf

\[
H_5=
\begin{pmatrix}
2\Delta&g\sqrt{31/2}&0&0\\
g\sqrt{31/2}&\Delta&g\sqrt{45/62}&0\\
0&g\sqrt{45/62}&2\Delta&g\sqrt{148/31}\\
0&0&g\sqrt{148/31}&\Delta
\end{pmatrix},
\qquad a=(v,u\sqrt{31/32},0,0)^T.
\]

Die normierte Basis verwendet einen beliebigen Vorzeichenwechsel ihres
letzten Vektors. Die Einträge wurden nicht angepasst: Eine bruchfreie,
besetzungsaufgelöste Krylov-Konstruktion rekonstruiert jede vollständige
Hamiltonwirkung exakt, einschließlich Pauli-Ausschluss und Bosonfaktoren.
Die unnormierten Normquadrate sind \(30,465,1350,1548450\).

Mit \(q_z=(z-2\Delta)(z-\Delta)\) gilt

\[
\det(z-H_5)=q_z^2-21g^2q_z+74g^4.
\]

Damit lauten die vier Energien

\[
E_{5,\lambda,\pm}
=\frac{3\Delta\pm\sqrt{\Delta^2+4g^2\lambda}}2,\qquad
\lambda=(21\pm\sqrt{145})/2.
\]

Geprüfte Quellsymmetrien wirken transitiv auf alle 64 Fermionlabels;
zusammen mit der Cartangewichtserhaltung ist die Antwort diagonal und
für alle Modi gleich. Die Gesamtgewichte erfüllen exakt

\[
Z_{\rm add}=1-u^2/32,\qquad Z_{\rm add}+Z_h=1.
\]

Die vollständige lokale retardierte Einteilchen-Antwort der originalen
Fermionen auf dieser Referenz lässt sich deshalb schreiben als

\[
G_{rs}(z)=\delta_{rs}\left[
\frac{Z_h}{z+\epsilon_h}
a^\dagger(z+E_--H_5)^{-1}a\right],\quad \operatorname{Im}z>0.
\]

Das ist keine Berechnung sämtlicher N=5-Zustände und kein freies
relativistisches Diracfeld. Es ist die vollständige relevante endliche
Zweipunktantwort auf diesem genau angegebenen Zustand.

### 5.3 Zwei Entnahmen: derselbe Paartensor erscheint erneut

Für alle 2016 Paare ergibt sich aus der unnormierten Referenz
\(D_{A,rs}=\eta_AW_{\bar A,rs}\), somit
\(D^\dagger D=W^\dagger W\), \(DD^\dagger=8I_{60}\).
Auf \(|E_-\rangle\) ist der Zwei-Loch-Gramoperator
\(u^2W^\dagger W/480\), mit Rang 60.

Nach der ersten Entnahme ist die Zeitentwicklung ein Faktor zur Energie
\(\Delta\). Nach der zweiten ist der Ein-Boson-Teil des bekannten
N=2-Paarblocks erreicht. Diese konkreten Mehrzeitwege sind geschlossen;
beliebige höhere Interventionsfolgen werden nicht pauschal als gelöst erklärt.

## 6. Der Hintergrund ist kein physisches Vakuum

Der externe Gegenzeuge mit besetzten Fermionmodi \(0,1,2,57\) wurde
unabhängig bestätigt. Seine Konversionsnorm ist genau zwei. Die Kompression
auf diesen Zustand und seinen normierten Konversionszustand hat Matrix

\[
\begin{pmatrix}0&\sqrt2g\\\sqrt2g&\Delta\end{pmatrix}
\]

und liefert den negativen Variationswert
\((\Delta-\sqrt{\Delta^2+8g^2})/2\).
Invarianz dieser Kompression ist für die Variationsschranke nicht nötig.

Weil \(E_->0\) für \(0<g/\Delta<1/\sqrt8\), ist unsere Referenz in diesem
Bereich **nicht einmal Grundzustand des vollständigen N=4-Sektors**.
Eine zusätzliche Beschränkung auf physische Singuletts wäre ein anderer,
erst zu begründender Vertrag.

Die eigene Additionsrechnung verschärft auch die sektorübergreifende
Gegenprobe: \(\lambda_+=(21+\sqrt{145})/2>16\), also liegt eine exakt
konstruierte N=5-Energie unter \(E_-\). Für \(H+\mu N\) gewinnt bei
\(\mu\ge0\) der leere Zustand gegenüber der Referenz, bei \(\mu<0\)
der genannte N=5-Zustand. Im schwachen Bereich macht **kein** chemisches
Potential die Referenz zum globalen Grundzustand.

Die richtige Fortsetzung ist daher, die geladene Antwort auf dem
tatsächlich ausgewählten Quellenzustand zu berechnen, nicht diesen
Prüfhintergrund durch zusätzliche Annahmen zum Vakuum zu erklären.

## 7. Externe Vereinfachung bestätigt: 5×3 statt großer Spektralsuche

Die 3840 Boson-Fermion-Konfigurationen zerfallen nach dem erhaltenen
Gesamtgewicht genau wie folgt:

| Anzahl Blöcke | Blockgröße | Form nach diagonaler Vorzeichenanpassung | Eigenwerte je Block |
|---:|---:|---|---|
| 960 | 1 | \(7I_1\) | \(7\) |
| 320 | 3 | \(7I_3+\mathbf1_3\mathbf1_3^T\) | \(7^2,10\) |
| 192 | 5 | \(7I_5+\mathbf1_5\mathbf1_5^T\) | \(7^4,12\) |
| 64 | 15 | \(8I-A(K_5\otimes K_3)\) | \(0,7^8,10^4,12^2\) |

Jede Zeile umfasst 960 Zustände. Für jeden 15er-Block wurden die fünf
Vektorlabels und drei Farbpaarlabels direkt aus der nativen Basis gefunden.
Die Koeffizienten der entsprechenden J-Zeile geben gerade den benötigten
Vorzeichenadapter. Kanten ändern beide Labels.

So folgt das bekannte Gesamtspektrum
\(0^{64},7^{2880},10^{576},12^{320}\) aus kleinen Graphidentitäten.
Dies ist eine echte analytische Vereinfachung des vorhandenen Spektrums,
kein zusätzlicher Hamiltonterm. Die Drei im endlichen Faktor ist
kein Nachweis dreier Raumdimensionen.

## 8. Hodge-Vorschlag: mathematisch richtig, physikalisch noch nicht identifiziert

Für den Dreitermkomplex

\[
\mathbb C^{41664}\xrightarrow{C_3}\mathbb C^{3840}
\xrightarrow{J}\mathbb C^{64}
\]

gilt tatsächlich \(d^2=0\). Im mittleren Raum hat

\[
L_{\rm Mitte}=C_3C_3^\dagger+J^\dagger J
\]

das Spektrum \(7^{2880},10^{576},12^{320},15^{64}\), also keinen Kern.
Die Aussage des ersten Texts über die mittlere Laplace-Matrix ist bestätigt.

**Zwei notwendige Korrekturen der Interpretation:**

1. Der gesamte Dreitermkomplex besitzt weiterhin einen 37888-dimensionalen
   Kern am linken Ende. Für \(D=d+d^\dagger\) auf insgesamt 45568 Dimensionen
   ist dies auch sein Nullraum; der Gradindex ist 37888. Die lokale
   mittlere Exaktheit wählt deshalb keinen eindeutigen Gesamtzustand.
2. Weder D noch dieser L sind als der bisherige physische Hamiltonoperator
   identifiziert. Ein zusätzlicher mathematischer Endraum ist nicht schon
   eine neue native Operationsmöglichkeit. Die Nullmoden des bisherigen H
   sind durch diese Umbenennung nicht aus seiner Dynamik verschwunden.

Auch der \(2^{64}\)-Kern der anderen positiven-Quadrat-Konstruktion aus
v1.6.1 wird dadurch nicht aufgehoben. Das sind unterschiedliche Operatoren
und unterschiedliche Beweisaufgaben.

## 9. Der vorgeschlagene reine Quartikoperator besteht den Symmetrietest nicht

Der erste Text schlägt die ungewichtete Kontraktion
\(Q_{\rm un}=\sum_A P_A P_{\bar A}\) vor. Ihre angegebenen
640 nichtverschwindenden Vier-Fermion-Amplituden mit Betrag vier wurden
exakt reproduziert. Alle tragen Cartangewicht null und N-Ladung minus vier.
Sie sind im deklarierten nativen Clock-Lift sogar invariant.

Aber bereits der SU(4)-Generator \(I_{16}\otimes(E_{01}-E_{10})\)
erzeugt einen nichtverschwindenden Defekt: 960 Amplituden, Normquadrat 30720
in der unnormierten Besetzungsdarstellung. **Gewichtsneutralität und
Clock-Verträglichkeit implizieren hier keine volle innere Invarianz.**

Mit der invarianten Paarung lautet die Kontraktion

\[
Q_{\rm inv}=\sum_A\eta_A P_A P_{\bar A}=0
\]

identisch. Das ist dieselbe Fierz-Auslöschung, welche den N=4-Referenzblock
geschlossen hält.

Damit scheidet dieser konkrete reine Quartikvorschlag als nichttriviale,
voll symmetrische Zusatzverbindung aus. Dies verbietet nicht sämtliche
quartischen Operatoren unter veränderten Voraussetzungen; es beantwortet
genau den vorgeschlagenen Test. Eine native U(1)-Brechung zu Z4 wurde
nicht hergeleitet und ist für den bewiesenen relationalen Lochsatz auch
nicht erforderlich.

## 10. Feldnorm und Kontrollalgebra: hilfreiche Reduktionen mit einer neuen Grenze

### 10.1 Kompositnorm aus Besetzungen

Aus den ursprünglichen CAR/CCR folgt auf dem endlichen Teilchenkern

\[
\{\chi_r,\chi_s^\dagger\}=\delta_{rs}I
+\frac1{15}\sum_{A,B,i}\overline{J_{r;Ai}}J_{s;Bi}b_B^\dagger b_A
-\frac1{15}\sum_{A,i,j}\overline{J_{r;Ai}}J_{s;Aj}f_j^\dagger f_i.
\]

Die gemischten höheren Terme heben sich auf. Die Tensor-Kontraktionen
\(\sum_{r,i}\bar J_{r;Ai}J_{r;Bi}=16\delta_{AB}\) und
\(\sum_{r,A}\bar J_{r;Ai}J_{r;Aj}=15\delta_{ij}\) wurden unabhängig geprüft.
Für einen Spin(10)×SU(4)-invarianten Zustand ergibt sich

\[
\langle\{\chi_r,\chi_s^\dagger\}\rangle
=\delta_{rs}\left(1+\frac{\langle N_b\rangle}{60}
-\frac{\langle N_f\rangle}{64}\right).
\]

Im Sektor N=64 reduziert sich das auf
\(Z_\chi=23\langle N_b\rangle/480\).
Für einen differenzierbaren isolierten Eigenzustand kann
\(\langle N_b\rangle=\partial_\Delta E|_g\) verwendet werden.
Die Ableitung erfolgt bei festem g, nicht bei festem Verhältnis g/Delta.

Diese Summenregel ist kein isoliertes Teilchenpolgewicht, keine
Operator-CAR und kein neuer N=64-Grundzustandsbeweis.

### 10.2 Die zwei bekannten Kontrollen erzeugen nur 14 Algebraelemente

Für genau Konversion X und Besetzung \(B=N_b\) im N=3-Sektor gilt

\[
\mathcal A_3\simeq\mathbb C\oplus\mathbb C
\oplus(M_2\otimes I_{2880})
\oplus(M_2\otimes I_{576})
\oplus(M_2\otimes I_{320}),\qquad\dim\mathcal A_3=14.
\]

Die erste skalare Wirkung liegt auf 37888 dunklen Fermionzuständen,
die zweite auf 64 dunklen Boson-Fermion-Zuständen. Eine treue rationale
8×8-Darstellung bestätigt den vollständigen Algebraabschluss.

### 10.3 Neue Schlussfolgerung aus dem Abgleich der Texte

Für die **vollständige** neutrale Observablealgebra
\(\bigoplus_n B(\mathcal H_n)\) ist die unsichtbare Hamiltonfreiheit im
endlichen Vertrag genau \(F(N)\). Die Begründung ist der sektorweise
skalare Kommutant. Neutralen Instrumentfolgen entgeht derselbe Zusatz.

Die tatsächlich geprüften **zwei** Kontrollen erzeugen jedoch nicht
diese vollständige Algebra. Ihr Kommutant im festen N=3-Sektor ist

\[
\mathcal A_3'\simeq M_{37888}\oplus M_{64}
\oplus(I_2\otimes M_{2880})
\oplus(I_2\otimes M_{576})
\oplus(I_2\otimes M_{320}).
\]

Jeder selbstadjungierte Zusatz aus diesem Kommutanten ist gegenüber
diesen Kontrollen unsichtbar, weil er auch mit
\(H=\Delta B+gX\) kommutiert. **Die bekannte operative Mehrdeutigkeit
ist unter diesem engen Kontrollvertrag sogar innerhalb eines festen
Ladungssektors größer als F(N).**

Zusätzliche tatsächlich zulässige modeweise oder Symmetrieoperationen
können sie reduzieren. Es wäre aber falsch, deren Existenz aus der
kleinen Kontrollalgebra zu folgern. Das ist ein konkreter neuer
Akzeptanztest für die vollständige Compiler-Operationsquelle.

## 11. Der dritte Text: Matrixkern, Präparation und Transport

### 11.1 Zwei Erzeuger über den gaußschen ganzen Zahlen

Im bereits bewiesenen Ordnungsvertrag wurde unabhängig bestätigt

\[
\mathcal M=\mathbb Z[i]\operatorname{span}\{I,w,q,wq\}
=\mathbb Z[i][w,q],\qquad q=\operatorname{diag}(i,1).
\]

Der Basiswechsel zur ursprünglichen maximalen Matrixordnung hat
Determinante i und gaußganzzahlige Hin- und Rückkoordinaten.
Dies ist eine Integralbasis, nicht nur eine komplexe Vektorraumbasis.

Im tatsächlichen vierdimensionalen Cliffordrahmen gilt exakt
\(q_4=CZ\,V\,CZ\,V\), \(V=(ZH)\otimes I\), einschließlich der Phase
und der markierten Achsenwirkung. Das schließt die Synthese **im
angenommenen Laboralphabet**. Es leitet dieses Alphabet nicht aus
der primitiven Quelle her: Aus R allein bleibt jedes Produkt in R,
während q nicht in R liegt.

Die vollständige Enumeration der 240 Wurzeln ergibt zudem exakt:

- 96 unitäre Wurzeln: 24 projektive Ein-Qubit-Cliffordwirkungen,
  je vier zentrale Phasen.
- 144 Rang-eins-Wurzeln: sämtliche 36 Übergänge zwischen sechs
  Pauli-Eigenstrahlen, je vier Phasen.

Für eine Rang-eins-Wurzel A ist erst \(A/\sqrt2\) der normierte
ausgewählte Zweig, mit \(A^\dagger A/2=P_{\rm in}\) und
\(AA^\dagger/2=P_{\rm out}\). Ein Wurzelname liefert nicht von selbst
eine kohärente Kontroll- oder Recordressource.

### 11.2 Nichtgaußsche Paarzustände durch eine gemeinsame Zahlprojektion

Jede tatsächliche W-Zeile enthält acht disjunkte Paare auf 16 Modi.
Mit ihren ursprünglichen Vorzeichen gilt

\[
\Pi_{N_f=2}\prod_{r=1}^{8}
\left(\sqrt{1-p}+\sigma_r\sqrt p\,f_{i_r}^\dagger f_{j_r}^\dagger\right)|0\rangle
=\sqrt{8p(1-p)^7}\,|\psi_A\rangle.
\]

Alle 60 Zeilen erfüllen die nötige Disjunktheit und Vorzeichenidentität.
Die Erfolgswahrscheinlichkeit ist in dieser Familie maximal bei
\(p=1/8\), mit \((7/8)^7\), ungefähr 39,27 Prozent.

Das ist eine bedingte Darstellung der hellen Paarzustände, nicht der
Vierträgerzelle Omega. Ihr Vierpunktdefekt \(7/64\) bleibt erhalten.
Die gemeinsame Zahlprojektion darf nicht aufzeichnen, welches Paar
entstanden ist. Paarrotationen, Ladungsreferenz und diese Projektion
sind benannte Ressourcen, keine bereits hergeleiteten Primitive.

### 11.3 Zwei-Bank-Transport stimmt, ist aber bereits Spezialfall von v1.6.1

Mit vorgegebenem Vermittlerhopping eta zerfällt der gesamte N=2-Sektor
zweier nativer Banken mit 8248 Zuständen in 60 aktive Viererräume und
8008 dunkle Zustände. Pro Kanal:

\[
H_A=\begin{pmatrix}
0&\sqrt8g&0&0\\
\sqrt8g&\Delta&\eta&0\\
0&\eta&\Delta&\sqrt8g\\
0&0&\sqrt8g&0
\end{pmatrix}.
\]

Gerade und ungerade Bankkombinationen liefern zwei 2×2-Blöcke mit
Vermittlerenergien \(\Delta\pm\eta\). Der erste Paartransfer erfüllt
\((H_A^3)_{4,1}=8g^2\eta\), bei verschwindenden niedrigeren Potenzen.

Die allgemeinen Spektralfunktionen
\(E_\pm(h)=(h\pm\sqrt{h^2+32g^2I})/2\) und die bedingte extensive
Schranke \(-480Lg^2/\delta\) bei \(h\ge\delta I>0\) standen bereits
in der eigenen v1.6.1-Fortsetzung. Der neue Text stimmt damit überein;
das wird nicht als zusätzlicher Raumzeitdurchbruch doppelt gezählt.
Graph und h bleiben Eingaben. Lokal gerade Bankoperationen transportieren
weiterhin kein einzelnes Fermion oder Loch zwischen den Banken.

## 12. Ein wesentlicher Feldtyp-Test vor jeder Kontinuumsrechnung

Unter der zusätzlichen Zuordnung „64 innere Labels gleichhändiger
lokaler Weylfelder, Boson als Lorentzskalar“ ist

\[
B_{IJ}=\varepsilon_{\alpha\beta}\psi_I^\alpha\psi_J^\beta
=B_{JI}.
\]

Da W in den inneren Indizes antisymmetrisch ist, folgt

\[
\boxed{\sum_{I,J}W_{A,IJ}
\varepsilon_{\alpha\beta}\psi_I^\alpha\psi_J^\beta=0.}
\]

Dieser Nullsatz wurde unabhängig für alle 60 tatsächlichen Tensorzeilen
durch Grassmann-Basisrechnung geprüft. Er bestätigt den dritten Text.
Die Zweikomponentenkonventionen werden in der Primärdarstellung von
[Dreiner, Haber und Martin](https://arxiv.org/abs/0812.1594) erläutert;
der konkrete W-Nulltest ist die hier vorgenommene Rechnung.

Die Austauschzerlegung

\[
\Lambda^2(S\otimes R)=
(\Lambda^2S\otimes\mathrm{Sym}^2R)
\oplus(\mathrm{Sym}^2S\otimes\Lambda^2R)
\]

zeigt eine algebraisch nichtverschwindende Alternative: W koppelt
an symmetrische Lorentzspinorindizes, also den Typ (1,0), nicht an
den Skalar. Auch dieser Nichtnulltest wurde für alle 60 Zeilen ausgeführt.
Eine physisch konsistente Dynamik dieses nichtskalaren Vermittlers
wird damit nicht behauptet. Es ist insbesondere nicht schon der
dynamische Spin-2-Sektor.

Der endliche Fockvertex wird nicht widerlegt. Ausgeschlossen ist diese
konkrete unzulässige Übersetzung in ein lokales relativistisches Skalarmodell.

Schurs Lemma vereinfacht bei ungebrochener innerer Symmetrie zusätzlich
einen zulässigen kinetischen Operator auf einem einzigen irreduziblen
64er-Multiplett zu \(I_{64}\otimes d(p)\). Es erzwingt keine gleiche
Kinematik anderer irreduzibler Sektoren und liefert weder Raum noch
eine Familienauswahl 4→1+3.

## 13. Eigene Clock- und Record-Verbindung

Die echte endliche Quell-Clock wurde aus ihrer gepinnten Konstruktion
ausgelesen. Unter der ausdrücklich angegebenen Identifikation ihrer
Koordinaten mit den nativen E8-Gewichtskoordinaten liefert die
vorzeichenrichtige äußere Wirkung auf gerade Fünf-Slot-Wörter einen
Fermionlift \(G_F\). Der Bosonlift \(G_B\) enthält zusätzlich das
Minuszeichen der orientierungsumkehrenden Fünferpermutation.

Geprüft sind
\(W\Lambda^2G_F=G_BW\), \(J(G_B\otimes G_F)=G_FJ\),
beide adjungierten Identitäten, Periode sechs und Referenzinvarianz.
Weglassen des Bosonminus verletzt die Kovarianz.
Der Partner \((-G_F,G_B)\) bleibt möglich; die volle markierte
Hilbert-/Feldidentifikation ist weiterhin offen.

Clock-Kovarianz ist keine Identifikation mit Hamiltonzeit: Am Testwert
ist \(E_+/E_-\) irrational. Daher gibt es keinen nichttrivialen
Hamiltonzeitpunkt, der auf leerem Zustand und beiden Referenzeigenzuständen
gleichzeitig die dort triviale Clockwirkung reproduziert.

Für einen verfügbaren Eingang B ist ein bedingter Ausführungspfad dagegen
vollständig normalisiert:

\[
\tau=\pi\hbar/\Omega_4,\qquad
\langle R|e^{-iH\tau/\hbar}|B\rangle
=-i e^{-i3\Delta\tau/(2\hbar)}\,8g/\Omega_4.
\]

Die anschließende Auswahl \(N_b=1\) hat am Testwert Erfolg 4/29.
Ein festes Entnahmeinstrument \(\{f_r,I-n_r\}\) liefert einschließlich
Puls und Auswahl Erfolg 1/232. Eine andere, auf \(N_f=2\) isometrische
Extraktion

\[
V_{\rm ext}=\frac1{\sqrt2}\sum_r f_r\otimes|r\rangle_D
\]

erzeugt \(-\sum_r|\chi_r\rangle|r\rangle_D/8\), mit bedingtem Gewicht
1/64 je Record, insgesamt je 1/464 einschließlich Puls.
Die Ladung bleibt mit dem entnommenen Detektorfermion insgesamt vier.
Die interne 15-Komponenten-Kohärenz wird nicht aufgezeichnet.

Die zwei Erfolgszahlen gehören zu unterschiedlichen Instrumenten.
B-Präparation, Besetzungsmessung und Detektorkopplung fehlen als
native Ableitungen. Zudem sind der postselektierte R-Zustand und der
stationäre Eigenzustand E-minus nicht gleich.
Aus reinen Vier-Fermion-Eingängen ist der geschlossene B/R-Raum durch
H, diese Clock und Bosonzahlprojektion allein unerreichbar.

## 14. T1–T8 und die nun entscheidenden Prüfungen

| Tor | Konkreter Beitrag | Weiter offen |
|---|---|---|
| T1 | Kurze Integralbasis, bedingte q-Synthese, gemeinsamer Clock-Lift | Primitive Operationen, eindeutige Markierungen, Rahmen und Dimensionswahl |
| T2 | Exakter Lochanschluss, Kompositnorm, vollständige endliche f-Zweipunktantwort | Physischer Hintergrund, tatsächliches Half-Charge-Feld, Renormierung, Energie und Adjungierte im Grenzraum |
| T3 | Native innere Rekopplung, bedingter exakter Paartransport | Herkunft räumlicher Teile und ihrer ungeraden Verbindung, gemeinsamer 3+1D-Träger |
| T4 | Exakter Nulltest der falschen skalaren Weylzuordnung | Richtiges Feldwörterbuch, chirales Maß, Index, Anomalien und Spiegelkontrolle |
| T5 | Kleine geschlossene Antwortblöcke und bedingte Stabilität | Wechselwirkender gemeinsamer Kontinuumslimes, Clusterstruktur und Streuung |
| T6 | Engere Symmetrie- und Feldtypbedingungen | Gemeinsame Kopplungs-, Familien- und Neutrinodaten samt Transfer |
| T7 | Kein neuer Spin-2-Nachweis | Masseloser quantisierter Spin 2, zwei Helizitäten und universelle Kopplung |
| T8 | Hintergrund-Gegenbeweise und präziser unsichtbarer Kontrollkommutant | Physische Zustandswahl, Sektorgewichte, native Präparation und Records |

**Prioritäten für die nächste Rechnung:**

1. Den tatsächlich verfügbaren Operationssatz erweitern beziehungsweise
   exakt abgrenzen und seinen Kommutanten bestimmen. Mehrfachwiederholung
   derselben zwei Kontrollen beseitigt ihre unsichtbaren Freiheitsgrade nicht.
2. Den berichteten nativen Grundzustand mitsamt seinem ursprünglichen
   Hamilton- und Sektorvertrag gezielt reproduzieren. Danach dessen
   Bosonbesetzung und vollständige geladene Antwort bestimmen.
   Die Summenregel und der hier vollständig lösbare Lochfall liefern
   unmittelbare Norm- und Energieprüfungen.
3. Vor einer großen Orts- oder Kontinuumsrechnung das Lorentz-Feldwörterbuch
   am tatsächlichen Tensor festhalten. Der bewiesene skalare Nullkanal
   darf nicht erneut als Wechselwirkung eingesetzt werden.
4. Erst mit demselben Zustand und Feldtyp eine native Verbindung zweier
   operational bestimmter Teilalgebren zeigen. Akzeptanz ist ein echtes
   ungerades Transfermatrixelement unter zulässigen Operationen, keine
   frei eingesetzte Hoppingregel. Dann erst skalierende Geometrie prüfen.

Es ist nicht bewiesen, dass eine einzige zusätzliche Operation alle vier
Schritte erledigt. Die gemeinsame Frage ist aber jetzt deutlich enger:
**Welche ursprüngliche Verknüpfung ist zugleich zugänglich, symmetrierichtig,
feldtypgerecht und auf dem ausgewählten Zustand dynamisch wirksam?**

## 15. Verifikation und nicht übernommene Behauptungen

Der gemeinsame Einstieg (replay.py) führt vier eigene Prüfer jeweils normal
und optimiert aus. Maßgeblich sind die PASS-Ergebnisse, Exitcodes und
byteidentischen Ausgabehashes im replay_manifest.json:
verify_hole.py, addition_response.py, external_synthesis.py und
minimal_interfaces.py. Der abschließende gemeinsame Lauf besteht mit
27143 Prüfwachen: 27139 exakt, vier numerisch. Große Guardzahlen enthalten
Komponentenwiederholungen und sind keine Zählung unabhängiger Theoreme.

Die exakten Rechnungen verwenden ganzzahlige Besetzungsamplituden,
symbolisch vereinfachte gaußrationale Matrizen und rationale
Abschlussprüfungen. Vier numerische Kontrollen betreffen Puls und
Normierung. Die gaußganzzahligen Liegeneratorprüfungen sind in den
verwendeten kleinen Komponenten exakt darstellbar und verwenden keine
Toleranzschwelle.

Das fremde Prüfpaket des Texts B wurde zusätzlich in
/tmp/tfpt-external-audit-20260915.DR6AO1 unverändert ausgeführt:
beide Prüfer bestanden normal und optimiert, mit bytegleichen Berichten.
Die dortigen 191 Prüfbedingungen enthalten bereits die 54 Basisbedingungen;
sie werden nicht addiert oder als eigene Entdeckungen gezählt.

Während der eigenen Fortsetzung entdeckte die systematische Gegenprüfung
einen Faktor-zwei-Fehler in der zunächst ausgeschriebenen Pulsamplitude.
Korrekt ist 8g/Omega4, während die Wahrscheinlichkeit 4/29 bereits stimmte.
Ein bleibender Regressionstest prüft die genaue Pauli-Zerlegung des
Referenzblocks. Ein Variablenüberschreibungsfehler und ein rein syntaktischer
Symbolgleichheitsfehler wurden ebenfalls vor dem abschließenden Replay
behoben; mathematische Gleichheit wurde exakt vereinfacht, nicht durch
numerische Toleranzen ersetzt.

Nicht als neue gesicherte Ergebnisse übernommen werden:

- die bloße Behauptung, algebraische Schließung müsse automatisch
  Zustand, Hamiltonoperator, Raum und Gravitation auswählen;
- die ungeprüfte native Zulässigkeit einer Ladung-vier-Zusatzoperation;
- der im dritten Text ohne identifizierbare Primärreferenz erwähnte
  Spiegelmodenartikel vom 30. August 2026;
- historische Kosmologie-Likelihoods oder vollständige N=64-/C16-Abnahmen
  ohne erneuten einschlägigen Audit in dieser Runde.

RH, Faktorisierung, P versus NP, dunkle Materie/Energie, Baryogenese und
Gravitation erhalten durch diese lokale Konsolidierung keinen vollständigen
Abschluss. Eine positive endliche Laplace-Matrix ist insbesondere keine
Identifikation einer arithmetischen Zielform.

Die SHA-256-Bindungen der drei Eingaben und der tatsächlichen Quellprogramme
stehen in den maschinenlesbaren Berichten. Der native Tensor hat SHA-256
3f00a0892157a691e4ef26920c3702772c7bf76a250fad98ff04a079bb64b763.
Es handelt sich um reproduzierbare endliche Rechenverifikation mit
angegebenen analytischen Folgerungen, nicht um einen vollständigen
Lean-Neubau, externe Begutachtung oder experimentelle Bestätigung.

Die Vorversionen bleiben unverändert. Dieser neue Forschungsordner wurde
nicht committed oder gepusht.
