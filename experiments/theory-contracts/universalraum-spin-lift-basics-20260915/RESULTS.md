# TFPT / Universalraum: den verlorenen Spin-Lift wieder einsetzen

## Forschungsfortsetzung v1.6.10 - 15. September 2026

**Ergebnis:** Ein bereits in TFPT vorhandenes Umlaufvorzeichen verbindet drei bisher getrennte Fragen: Welche Information verlieren Paarmessungen? Welche Fermionrichtungen sind wirklich gekoppelt? Welcher Grundzustand wird bevorzugt? Für einen ausdrücklich festgelegten Viererzyklus mit dem unveränderten inneren Tensor W wird diese Verbindung hier bis zu einem eindeutigen Grundzustand des vollständigen Hamiltonoperators und seiner isolierten geladenen Antwort verfolgt.

**Geltungsbereich:** Die Quellenanordnung und ihre Identifikation mit einer physischen TFPT-Seam sind nicht hergeleitet. Der neue Grundzustandssatz gilt bei $0<|g|/\Delta\le1/2000$, der präzisere Antwortsatz bei $0<|g|/\Delta\le1/10000$. Das ist **nicht** der bisherige Prüfpunkt $g/\Delta=1/20$. Es gibt keinen neuen $\mu N$-Term. Die Bosonbesetzung wird nicht abgeschnitten. Kein vollständiges T1-T8-Gate ist geschlossen.

Die Beweise sind analytische Forschungsresultate mit exakten endlichen Kontrollen und rationalen Fehlerschranken, kein Proof-Assistant-Zertifikat und kein unabhängiges Fachgutachten. Die alte lokale 64-Fermion-Bank und die neue globale Vier-Bank-Anordnung sind verschiedene Hamiltonverträge.

**Verschärfte Auswahlprüfung:** Abschnitt 15 zeigt, dass Clock und eindeutiger Grundzustand allein das Umlaufvorzeichen nicht wählen. Ein vorgegebener gemeinsamer Links-rechts-Reflexionsvertrag würde dagegen innerhalb der reellen Zweinachbar-Klasse die gleiche Gewichtung erzwingen; mit dem Ausschluss freier Fermionrichtungen bleibt dann der negative Lift. Der entsprechende ursprüngliche TFPT-Operatorvertrag ist noch nicht nachgewiesen.

## 1. Was die erneute Grundlagenlektüre verändert

Die erneute Lektüre umfasst die Grundkonstruktion in `README.md`, `docs/THEORY.md`, `origin_theory.tex`, die D5/A3- und Pascal-Konstruktion, die aktuelle Standardmodell-Masterformel und ihre Projektionsgrenzen, den Kaskadenvergleich im E8-Audit, die Frontier-Verträge sowie die einschlägigen Abschnitte der Archivfassung `paper_v1_06_01_09_2025.tex`. Nicht sämtliche mehr als 30.000 Zeilen der aktuellen Theorie samt allen eingeschobenen Forschungsboxen wurden erneut vollständig geprüft.

Die ursprüngliche Einfachheit ist real auf der Ebene der Konstruktion: Der Anker $(1,1,2)$ liefert über elementarsymmetrische Funktionen $(4,5,2)$; der gerade Fockraum von fünf Slots trägt den 16-dimensionalen Halbspinor; D5, A3 und die zyklische Verklebung organisieren den E8-Rahmen. Die aktuelle Theorie nennt E8 ausdrücklich eine algebraische Hülle, nicht automatisch die physische Eichgruppe. Die Quellenmassen und Mischungsgrößen werden über eine kleine Zahl von Compiler-Ausdrücken organisiert; der physische RG-, QCD- und kosmologische Transport bleibt davon getrennt.

Die für diese Runde wichtigste wiedergefundene Stelle ist `origin_theory.tex`, Abschnitt zum vierintervalligen freien Fermionmodell, mit dem Prüfer `v480_multilocal_four_interval.py`: Die geometrische Vierteldrehung hat auf Fermionen die Beziehung

$$\rho^4=-I,\qquad \rho^8=I.$$

Auf geraden Paargrößen verschwindet dieses zusätzliche Minus. Der Prüfer wurde erneut normal und optimiert ausgeführt. Er zeigt den Mechanismus in einem gewählten antiperiodischen freien Ring; er beweist ausdrücklich nicht, dass die ursprüngliche TFPT-Seam dieser Ring ist. Sein Literaturanschluss ist die zustandserhaltende multilokale Fermionisierung von Rehren und Tedesco: [Originalarbeit](https://arxiv.org/abs/1205.0324). Dort ist die Änderung der Lokalisierung wesentlich; die Identifikation beliebiger Kopienräume ist nicht frei gegeben.

Die neue Einsicht dieser Runde ist daher nicht, dass Doppelabdeckungen neu wären. Neu ist der explizite Anschluss dieser bereits bekannten Information an die überlappenden W-Quellen, den vollständigen Grundzustandsvergleich und die geladene Antwort.

## 2. Prüfung der zugeschickten Arbeit

Die Arbeit **TFPT / Universalraum: eine gemeinsame Quelle auf dem Prüfstand**, Fortsetzung 1.2, enthält 15 Seiten. Ihr Prüfpaket wurde in einer neuen temporären Kopie entpackt. Alle vier wissenschaftlichen Prüfer liefen normal und mit `-OO`; die Ausgaben stimmen bytegenau mit den gepinnten Ergebnissen überein: 614 Bedingungen, aufgeteilt in 402, 22, 176 und 14.

Tragende Ergebnisse sind die induzierte Paar-Gram-Matrix, der geschützte innere Faktor, ein bedingter Wirkungstest, die explizite Beschränkung der lokalen Kontrollen, Graph-Gegenmodelle, die verdoppelte Schleifenphase und ein N=2-Grenzwert auf einem vorgegebenen Netz. Die Reproduktion macht daraus weder 614 unabhängige Theoreme noch eine vollständige physische Quelle.

Besonders wichtig ist die Gleichheit der gesamten eingeschränkten bosonischen N=2-Antwort zweier Dreiecksquellen mit Phasen null und pi, obwohl ihre Fermionkerne verschieden sind. Das neue Paper benennt damit selbst einen Informationsverlust. Dieser Befund wird im Folgenden nicht nur wiederholt, sondern für den TFPT-Viererclock verallgemeinert und durch eine neue Beobachtung ergänzt.

## 3. Ein festgelegter minimaler Kandidat

Vier unabhängige Fermionbereiche besitzen je 64 kanonische Moden $f_{x,r}$; vier unabhängige Bosonbereiche besitzen je 60 Moden $b_{e,A}$. Die inneren Indizes tragen unverändert die ursprünglichen Darstellungen $(16,4)$ beziehungsweise den W-Bildraum. Die vier **zusätzlichen Bereiche** sind nicht die vier Komponenten der bereits vorhandenen inneren SU(4)-Darstellung.

Für $\eta=\pm1$ sei

$$R_\eta=\begin{pmatrix}0&1&0&0\\0&0&1&0\\0&0&0&1\\\eta&0&0&0\end{pmatrix},\qquad
U_\eta=\frac{I+R_\eta}{\sqrt2},\qquad q_{e,r}=\sum_x(U_\eta)_{ex}f_{x,r}.$$

Jede einzelne q-Quelle ist kanonisch normiert. Verschiedene q-Quellen überlappen und sind gerade keine unabhängigen Fermionbanken. Die gemeinsame Wechselwirkung lautet

$$H_\eta=\Delta N_b+g\sum_{e,A}\bigl(b_{e,A}^\dagger P_A(q_e)+P_A(q_e)^\dagger b_{e,A}\bigr),\qquad
N=N_f+2N_b.$$

Dabei werden die 480 ursprünglichen W-Koeffizienten benutzt, keine zusätzliche freie Sprungmatrix. Der Viereckgraph, die Zweipunkt-Mittelung, unabhängige Kopien und die Wahl von $g/\Delta$ sind zusätzliche, sichtbare Modellannahmen.

### 3.1 Der gemeinsame Clock ist eine wirkliche Symmetrie dieses Kandidaten

$U_\eta R_\eta=R_\eta U_\eta$. Deshalb transformieren die q-Quellen unter der Fermiondrehung genauso wie die f-Moden. Beim Paar verschwindet das Vorzeichen; die Bosonbereiche werden zyklisch ohne Vorzeichen vertauscht. Die kombinierte Transformation erhält H exakt. Ihre vierte Potenz ist bei $\eta=-1$ die gesamte Fermionparität, ihre achte Potenz die Identität.

Das ist ein expliziter Clock-zu-Quellen-Intertwiner. **Nicht gezeigt** ist seine Gleichsetzung mit dem vollständigen mikroskopischen Seam-Prozess. Insbesondere ist der geometrische C8-Lift nicht durch Umbenennung der vorhandene innere Clock mit Periode sechs und nicht automatisch der Coxeter-Clock 30.

### 3.2 Paarinformation verliert ein Vorzeichen

Schreibe $S=UU^\dagger$. Aus $WW^\dagger=8I_{60}$ folgt

$$B_{ef}=8S_{ef}^{\,2},\qquad B=8I+2A_{C_4}.$$

Es handelt sich um das komplexe Quadrat der Amplitude, nicht generell um ihr Betragsquadrat. Für die hier reellen Vorzeichen ist B bei beiden Lifts identisch, mit Eigenwerten $4,8,8,12$.

Dagegen gilt

$$\operatorname{spec}S_+=\{0,1,1,2\},\qquad
\operatorname{spec}S_-=\{1-1/\sqrt2,1-1/\sqrt2,1+1/\sqrt2,1+1/\sqrt2\}.$$

Die periodische Quelle lässt 64 Fermionmoden vollständig frei. H wirkt auf deren Fockfaktor als Identität; jede globale Energie hat mindestens die entsprechende $2^{64}$-fache Entartung. Das betrifft das gesamte Fockmodell, nicht nur N=2. Die antiperiodische Quelle hat keinen solchen linearen Zuschauerbereich.

Allgemeiner hat eine vorgegebene vorzeichenbehaftete Zyklusquelle genau dann einen eindimensionalen Kopienkern, wenn das Produkt ihrer Kantenvorzeichen $(-1)^L$ beträgt. Der Beweis ist die Rekursion $x_j=-\eta_jx_{j+1}$. Lokale Vorzeichenänderungen verschieben die Vorzeichen entlang des Zyklus, ändern aber dieses Produkt nicht. Die zwei Schleifenklassen sind daher keine bloßen verschiedenen Basisnamen. Exakte Kontrollen umfassen sämtliche Vorzeichenbelegungen der Zyklen mit drei bis sieben Knoten.

## 4. Die fehlende Information wird ladungsneutral sichtbar

Die neue Rechnung muss keinen odden Messoperator als frei verfügbaren Aktuator annehmen. Ein bosonischer Rückkehrzeiger genügt, wenn der Eingang zusätzlich ein Fermion enthält.

Seien $A_A$ die reellen antisymmetrischen 64-mal-64-Matrizen zu W. Die ursprüngliche Dreiladungs-Gram-Matrix gibt

$$K_{Ar,Bs}=(A_BA_A^\dagger)_{rs},\qquad
\operatorname{spec}K=\{8^{(64)},1^{(2880)},(-2)^{(576)},(-4)^{(320)}\}.$$

Diese Identität wurde hier erneut aus der vollständigen kanonischen Dreifermion-Konstruktion und unabhängig aus sämtlichen 3600 A-Matrixblöcken geprüft. Für die zusammengesetzte Quelle definiere

$$T_{(e,x),(f,y)}=S_{ef}\,\overline{U_{fx}}U_{ey}.$$

Direktes CAR-Normalordnen liefert auf dem Eingang mit einem Boson und einem Fermion, nach passender Tensorordnung,

$$\boxed{G_3=(B\otimes I_4)\otimes I_{3840}-T\otimes K.}$$

Der 61.440-dimensionale Eingang reduziert sich somit auf vier 16-mal-16-Matrizen $B\otimes I_4-kT$ mit bekannten Vielfachheiten. Die Formel wurde zusätzlich mit vollständig ausgeschriebenen kleinen CAR-Modellen sowie 640 Einträgen des echten 256-Fermion-Modells kontrolliert; diese Stichprobe wird nicht als vollständige große Matrixdiagonalisierung bezeichnet.

| Moment | Periodisch | Antiperiodisch |
|---|---:|---:|
| $\operatorname{tr}G_3$ | 487680 | 487680 |
| $\operatorname{tr}G_3^2$ | 4440960 | 4440960 |
| $\operatorname{tr}G_3^3$ | 44601120 | 44601120 |
| $\operatorname{tr}G_3^4$ | 481843440 | 481728240 |

Beginnt man im gleichmäßig gemischten Einboson-Einfermion-Eingang und misst später die gesamte Bosonzahl, folgt

$$\boxed{p_-(t)-p_+(t)=-\frac{g^8t^8}{168}+O(t^{10}).}$$

Herleitung: Für einen Eigenwert $\lambda$ von $G_3$ ist die Bosonüberlebenswahrscheinlichkeit

$$1-\frac{4g^2\lambda}{\Delta^2+4g^2\lambda}
\sin^2\!\left(\frac{t\sqrt{\Delta^2+4g^2\lambda}}2\right).$$

Der oberste $\lambda^4$-Term der achten Zeitordnung ist $g^8\lambda^4/315$. Die niedrigeren Momente stimmen überein; Division der Differenz $-115200$ durch $315\cdot61440$ ergibt $-1/168$. Dies ist eine exakte lokale Tayloraussage, keine numerisch zertifizierte Differenz bei beliebigen endlichen Zeiten.

**Wichtig:** Dieser N=3-Vergleich ist ein Quellen-Diagnoseexperiment auf einem gesetzten Eingang. Er ist nicht die Antwort auf dem folgenden N=256-Grundzustand. Diese beiden Aufgaben werden ausdrücklich getrennt.

## 5. Eine vollständige lokale Casimir-Identität ersetzt riesige Fockmatrizen

Für eine kanonische 64-Moden-Quelle sei

$$Q=\sum_A P_A^\dagger P_A.$$

Die 60 antihermiteschen Einteilchengeneratoren $X_a$ von Spin(10) mal SU(4) erfüllen $-\sum_aX_a^2=60I$. Auf dem gesamten Fockraum gilt

$$\boxed{8Q=60N_f-\mathcal C,\qquad
\mathcal C=\sum_a d\Gamma(X_a)^\dagger d\Gamma(X_a)\ge0.}$$

Warum die endliche Prüfung für diese Identität reicht: Nach CAR-Normalordnung haben beide Seiten höchstens Grad vier. Die Einteilchenkoeffizienten sind durch den vollständigen Einteilchencasimir festgelegt. Die quartischen Koeffizienten werden durch die vollständige Zweifermionmatrix bestimmt. Dort wurde exakt

$$8W^\dagger W+\mathcal C_{\Lambda^2}-120I_{2016}=0$$

nachgerechnet. Vakuum, Einteilchen- und Zweiteilchenteil bestimmen daher alle normalgeordneten Koeffizienten; der Satz gilt auf allen $2^{64}$ Fermionzuständen. Die Matrixrechnung verwendet exakte gaußsche Ganzzahlen ohne Toleranzvergleich. Dies ist eine erneute Verifikation der hier benötigten Casimir-Grundlage, nicht eine Übernahme des alten Grundzustandssatzes für die einzelne Bank.

Daraus folgt $Q\le(15/2)N_f\le480I$. Der voll besetzte Zustand ist ein Singulett und erreicht 480. Für vier überlappende Quellen gilt deshalb

$$Q_{\rm ges}=\sum_{e,A}P_A(q_e)^\dagger P_A(q_e)\le M I,\qquad M=1920.$$

Mit $s_0=1-1/\sqrt2$ und $\delta=(15/2)s_0>2$ erhält man für die antiperiodische Quelle die stärkere operatorielle Aussage

$$\boxed{M-Q_{\rm ges}\ge\delta N_h,\qquad N_h=256-N_f.}$$

Denn $480-Q_e\ge(15/2)(64-N_{q_e})$, und die Summe der lokalen Lochzahlen ist die zweite Quantisierung von $U^\dagger U$ im Lochraum; deren kleinster Eigenwert ist $s_0$. Der vollständig gefüllte globale Zustand $F$ erreicht M und ist der einzige Maximierer. Das ist bereits die eindeutige Zustandswahl der effektiven Wechselwirkung $-(g^2/\Delta)Q_{\rm ges}$.

## 6. Vollständiger Grundzustandssatz ohne Bosonabschneiden

**Satz.** Für die festgelegte antiperiodische Viererquelle, $\Delta>0$, $\mu=0$ und

$$0<|g|/\Delta\le1/2000$$

hat H auf dem vollständigen Fermion-Boson-Fockraum genau einen Grundzustand. Er liegt in der erhaltenen Gesamtladung $N=256$. Seine spektrale Lücke ist größer als $g^2/\Delta$.

### 6.1 Die drei einfachen Schranken

Quadratvervollständigung ergibt für beliebiges $0<\theta\le1$

$$H\ge(1-\theta)\Delta N_b-\frac{g^2}{\theta\Delta}Q_{\rm ges}.$$

**Kleinere Gesamtladungen.** Für $N\le255$ gilt $N_h\ge1$, also bei $\theta=1$

$$H|_{N\le255}\ge-(M-\delta)g^2/\Delta.$$

**Größere Gesamtladungen.** Für $N\ge257$ muss mindestens ein Boson vorhanden sein. Mit $\theta=1/2$ folgt

$$H|_{N\ge257}\ge\Delta/2-2Mg^2/\Delta>0.$$

**Gesamtladung 256.** Der bosonfreie Teil dieses Sektors ist eindimensional, nämlich F. Auf seinem orthogonalen Komplement gilt dieselbe positive Schranke wie oben. Auf dem Zweizustandsraum aus F und seiner normierten ersten Umwandlung ist H genau die Ritz-Matrix

$$\begin{pmatrix}0&g\sqrt M\\g\sqrt M&\Delta\end{pmatrix}.$$

Sie liefert die obere Grundzustandsschranke

$$E_{\rm Ritz}=\frac{\Delta-\sqrt{\Delta^2+4Mg^2}}2
\le-M\frac{g^2}{\Delta}+M^2\frac{g^4}{\Delta^3}<0.$$

Die Trennung von den kleineren Ladungen ist mindestens

$$\left(\delta-M^2\frac{g^2}{\Delta^2}\right)\frac{g^2}{\Delta}>
\frac{g^2}{\Delta},$$

weil $M^2/2000^2=0.9216$ und $\delta>2$. Innerhalb N=256 kann es höchstens einen negativen Eigenwert geben: Das Komplement der einen bosonfreien Richtung ist positiv. Das Min-Max-Prinzip liefert die Eindeutigkeit und die behauptete Lücke.

### 6.2 Warum dabei keine unendlichen Zustände unterschlagen werden

Es gibt endlich viele Fermion- und Bosonmoden, aber beliebige Bosonbesetzungen. Die Kopplung ist relativ zu $N_b$ infinitesimal beschränkt: Auf dem Übergang von k zu k+1 Bosonen hat $\sum b^\dagger P$ die Normschranke $\sqrt{M(k+1)}$. Daraus folgen Selbstadjungiertheit auf der Zahloperator-Domäne und kompakte Resolvente. Die oberen Ladungssektoren sind durch die explizite Schranke gleichzeitig ausgeschlossen, nicht durch eine endliche Stichprobe. Alle Aussagen betreffen den vollständigen H dieses Kandidaten.

Dieser Beweis ist wesentlich kleiner als eine Vollraumberechnung. Er benutzt die eigentliche TFPT-Stärke - Darstellung, Gradierung und Erhaltung - um die große Matrix gar nicht erst aufzustellen.

## 7. Derselbe Grundzustand besitzt eine kontrollierte geladene Antwort

Für die präzisen Energie- und Gewichtsschranken verwenden wir den engeren Bereich

$$0<|g|/\Delta\le1/10000.$$

### 7.1 Der gesamte Rest wird als konvergente Resolvente kontrolliert

P projiziere auf alle bosonfreien Zustände, $\Pi=I-P$, $D=\Delta N_b|_\Pi$, $X=\sum(b^\dagger P_A+P_A^\dagger b)$, und $C=\Pi X P$. Dann $C^\dagger C=Q_{\rm ges}|_P$. Für $-Mg^2/\Delta\le E\le0$ schreibe

$$\Pi(H-E)\Pi=D^{1/2}(I+Z)D^{1/2},\qquad
Z=gD^{-1/2}\Pi X\Pi D^{-1/2}-ED^{-1}.$$

Die Bosonzahlschichten geben

$$\|Z\|\le2\sqrt M\,|g|/\Delta+M g^2/\Delta^2<1/100.$$

Der Einbosonblock des linearen X-Terms ist null. Deshalb ist die Fehlergrenze des Feshbach-Operators gegenüber $-(g^2/\Delta)Q_{\rm ges}$ nicht nur erster Ordnung in $g/\Delta$, sondern

$$\left\|g^2C^\dagger[\Pi(H-E)\Pi]^{-1}C-\frac{g^2}{\Delta}Q_{\rm ges}\right\|
\le\frac{g^2}{\Delta}M\left[\frac{M}{10^8}+\frac{(1/100)^2}{1-1/100}\right]
=\frac{g^2}{\Delta}\frac{119008}{515625}<\frac{g^2}{4\Delta}.$$

Hier wurde der vollständige Neumannrest summiert. Der Schur-/Feshbach-Schritt ist elementare Operatorblockrechnung; ein allgemeiner Literaturrahmen ist [Dusson, Sigal und Stamm](https://arxiv.org/abs/2105.02058). Die konkreten Konstanten und Quellenoperatoren oben wurden hier abgeleitet.

Insbesondere

$$-1920\frac{g^2}{\Delta}\le E_0<-1919.75\frac{g^2}{\Delta},\qquad
\operatorname{gap}(H)>1.5\frac{g^2}{\Delta}.$$

Im N=256-Sektor ist der Schurraum eindimensional. Der exakte Grundzustandswert ist daher die eindeutige negative Lösung einer skalaren Gleichung,

$$\boxed{E_0=-g^2\langle F|C^\dagger[\Pi(H-E_0)\Pi]^{-1}C|F\rangle.}$$

Das ist ein Fixpunkt des **tatsächlichen** gewählten Hamiltonoperators. Es ist nicht die Umbenennung eines Compilerpolynoms in eine physische Bewegungsgleichung. Die Resolvente und die rekonstruierte Zustandskomponente besitzen konvergente Reihen; die genaue Dezimalenergie wird hier nicht als berechnet ausgegeben.

### 7.2 Zwei isolierte Entnahmelinien

Im bosonfreien N=255-Sektor gibt es genau ein Loch. Normalordnen beziehungsweise die lokale Casimir-Identität liefern dort exakt

$$Q_{\rm ges}|_{\text{ein Loch}}=MI-15(U^\dagger U)\otimes I_{64}.$$

Der geometrische Fermionclock hat vier verschiedene Eigenphasen $\exp(i(2j+1)\pi/4)$. Pro Phase trägt der Einlochraum genau eine irreduzible 64-dimensionale innere Darstellung. Weil H beide Symmetrien erhält, ist sein energieabhängiger Schuroperator in jedem dieser vier Blöcke skalar. Er hat jeweils eine negative Nullstelle: Seine Ableitung nach E ist strikt negativ, und der Einloch-Kopplungsoperator ist injektiv. Die Realität von H und des Clockoperators paart konjugierte Phasen. Damit ergeben sich **genau zwei verschiedene niedrige Energielinien**, jeweils mit Vielfachheit 128. Die getrennten Intervalle unten schließen eine Zusammenlegung der beiden Linien aus.

Setze

$$a_-=15(1-1/\sqrt2),\qquad a_+=15(1+1/\sqrt2).$$

Aus derselben uniformen Schurrestschranke und der Grundenergieeinschließung folgen die Entnahmeenergien

$$\boxed{(a_\pm-1/2)\frac{g^2}{\Delta}
<\epsilon_\pm<(a_\pm+1/4)\frac{g^2}{\Delta}.}$$

In Einheiten $g^2/\Delta$ ergeben sich die nach außen gerundeten Intervalle $(3.8933,4.6435)$ und $(25.1066,25.8567)$. Dies sind analytische Einschließungen, keine Polzentralwerte. Alle übrigen N=255-Zustände liegen im absoluten Spektrum mindestens bei $\Delta/2-2Mg^2/\Delta>0$; ihr Abstand zum negativen Grundwert ist entsprechend größer. Der Additionssektor N=257 erfüllt ebenfalls diese positive Untergrenze.

### 7.3 Ein ursprüngliches, clockaufgelöstes Fermion sieht die Linie

Für den Grundzustand und die vier niedrigen Einlochblöcke ergibt die Resolventenschranke dieselbe untere Überlappung mit dem jeweiligen bosonfreien Referenzzustand:

$$Z\ge Z_*=\frac{408375}{408383}>0.99998.$$

Ein normierter Clock-Eigenmodus $a_{\theta,r}$ ist eine unitäre Linearkombination der **ursprünglichen** f-Moden, kein neu eingeführtes Kompositfeld. Da $a_{\theta,r}$ die Bosonzahl nicht ändert und Operatornorm eins hat, ist sein Übergang auf die zugehörige niedrige Linie mindestens

$$\boxed{|\langle\Psi_{\theta,r},a_{\theta,r}\Omega\rangle|^2
\ge(2Z_*-1)^2=\frac{166763606689}{166776674689}>0.99992.}$$

Beweis: Der bosonfreie Anteil der Amplitude ist mindestens $\sqrt{Z_0Z_\theta}$, der Betrag der übrigen Kreuzung höchstens $\sqrt{(1-Z_0)(1-Z_\theta)}$. Ihre Differenz ist mindestens $2Z_*-1$. Da $\|a_{\theta,r}\Omega\|^2\le1$, gilt dieselbe Untergrenze auch für den Anteil am normierten Entnahmespektrum.

Somit trägt die zugehörige Linie **über 99.992 Prozent** für einen clockaufgelösten Modus. Ein ursprünglicher einzelner Orts-/Kopienmodus enthält hingegen beide Clock-Paare und sieht im Allgemeinen beide niedrigen Linien. Für ihn wird keine einzelne Linie mit diesem Gewicht behauptet.

Hier gehören Quelle, Grundzustand und geladene Antwort wirklich zu demselben H. Die native Herstellung eines Fermion-Eingriffs oder eines Messgeräts ist dadurch weiterhin nicht konstruiert.

## 8. Was wir bei der Einfachheit möglicherweise falsch verlangt haben

### 8.1 Quadratische Erzeugung ist nicht vollständige dynamische Steuerbarkeit

Der alte Prüfer `v111_quadratic_transport.py` zeigt korrekt, dass quadratische Cliffordwörter auf dem 16-dimensionalen geraden Fockraum eine volle **assoziative** Matrixalgebra aufspannen. Daraus folgt nicht, dass zeitabhängige quadratische Hamiltonoperatoren jede unitäre Operation erzeugen. Ihre dynamische Lie-Algebra hat Dimension 45, nicht 255.

Die Ergänzung muss dennoch keine riesige Maschine sein: Gewährt man alle quadratischen Generatoren und **einen** nichtverschwindenden reinen quartischen Majoranaterm, erzeugen die Kommutatoren sämtliche 210 quartischen Richtungen. Zusammen mit den 45 quadratischen Richtungen entsteht $\mathfrak{su}(16)$. Der Prüfer kontrolliert die 210 erreichbaren Vierermengen und die exakte Hilbert-Schmidt-Unabhängigkeit aller 255 Richtungen.

Das ist ein möglicher minimaler Operationsbaustein, keine Behauptung, dieser steuerbare Term liege bereits nativ vor. Die fünf inneren Cliffordslots sind außerdem nicht mit den 64 Teilchenmoden der W-Bank gleichzusetzen. Die gekoppelte W-Quelle erzeugt zwar quartische effektive Terme; deren Gleichsetzung mit einem frei steuerbaren Quartikgenerator des inneren 16er-Raums ist gerade noch nicht gezeigt. Die Unterscheidung zwischen assoziativer Erzeugung und dynamischer Lie-Algebra entspricht dem etablierten Kontrollrahmen, etwa [Wiersema et al., Klassifikation dynamischer Lie-Algebren](https://doi.org/10.1038/s41534-024-00900-2).

### 8.2 Ein eindeutiges mikroskopisches Netz ist nicht zwingend nötig

Die Petersen-/Prisma-Gegenmodelle beweisen eine endliche Unterbestimmtheit, aber keine Verschiedenheit aller denkbaren großskaligen Grenztheorien. Unterschiedliche Mikroregeln können derselben Universalitätsklasse angehören. Das ist ein wesentlicher Grund, nicht immer feinere Graph-Eindeutigkeit zu verlangen, bevor eine physische Grenzrechnung begonnen wird. Siehe den ursprünglichen RG-Rahmen von [Wilson und Kogut](https://theory.tifr.res.in/~tridib/ReferenceMaterial/WilsonKogut.pdf).

Diese Entlastung ist keine automatische Rettung: Auf der einfachen unendlichen Zyklus-/Kettenfortsetzung hat die N=2-Antwort

$$B(k)=8+4\cos k,\qquad
E_-(k)=\frac{\Delta-\sqrt{\Delta^2+4g^2B(k)}}2,$$

also $E_-(k)-E_-(0)=2g^2k^2/\sqrt{\Delta^2+48g^2}+O(k^4)$ und keinen linearen Dirackegel an dieser Bandkante. Dies ist nur die N=2-Bandrechnung, **nicht** die Anregung des vollständigen großen Grundzustands und kein universeller Ausschluss des Modells.

Auch ein antiperiodischer Zyklus mit immer mehr gerader Knotenzahl hat $s_{\min}=1-\cos(\pi/L)\to0$. Der neue endliche Grundzustandsbeweis ist deshalb kein bereits gleichmäßig gappender Thermodynamikbeweis. Für den Standardmodell-/Raumzeitanspruch müssen Zustand, Anregung, Skalierung und Lokalität gemeinsam geprüft werden.

## 9. Was die alte E8-Kaskade wirklich beisteuert

Die gewünschte Archivdatei ist ein LaTeX-Umschlag einer ausdrücklich als bestmögliche PDF-Textextraktion bezeichneten 81-seitigen Fassung. Einige Formeln und Figuren sind in dieser Darstellung beschädigt oder fehlen. Aus solchen Schäden werden hier keine mathematischen Gegenbeweise konstruiert.

Die lesbare Skalenregel ist

$$D_n=60-2n,\qquad
\varphi_n=\varphi_0e^{-\gamma_0}(D_n/58)^\lambda,\qquad
\lambda=\frac{\gamma_0}{\log(248/60)},\quad\gamma_0=0.834.$$

Sie liefert eine logarithmisch organisierte Skalenleiter, nicht allein eine Hamiltonentwicklung. In Verhältnissen fällt der gemeinsame Vorfaktor heraus, aber die Abhängigkeit von $\gamma_0$ bleibt über $\lambda$ erhalten:

$$\frac{\partial}{\partial\gamma_0}\log\frac{\varphi_m}{\varphi_n}
=\frac{\log(D_m/D_n)}{\log(248/60)}\ne0\quad(m\ne n).$$

Die aktuellen Kaskadenkapitel zitieren einen Krümmungs-/Glättungsselektor. Der dort angegebene Prüfer `v5_e8_cascade.py` kontrolliert Endpunkte, Dimensionen und Summen, aber **nicht** diese Auswahl von $\gamma_0$ oder $\lambda$. Eine lexikografisch eindeutige Kette unter erklärten Kriterien ist zudem nicht schon eine physische Erklärung dieser Kriterien.

Noch klarer ist die Grenze in der alten Callan-Symanzik-Passage: Die dort ausgeschriebene, bei den behaltenen Ordnungen positive Betafunktion

$$\beta(\alpha)=\frac{b_1}{2\pi}\alpha^2+A c_3^2\alpha^3+\cdots$$

besitzt bei $b_1,A,c_3>0$ in genau dieser Trunkierung keine positive nichttriviale Nullstelle. Das anschließend genannte Compilerkubikum kann daher nicht einfach als dieser RG-Fixpunkt ausgegeben werden. Das widerlegt nicht den algebraischen Wert des Compilerkubikums; es sperrt die Gleichsetzung zweier verschiedener Bedeutungen von Fixpunkt.

Die Archivabschnitte zur Chiralität setzen bereits $M_4$ mal eine innere Faser, einen Spinor-/Randprojektorvertrag und einen Fluss an. Sie enthalten also keine bislang übersehene vollständige Erzeugung von 3+1D-Raumzeit aus W. Der produktive alte Hinweis ist stattdessen: **Umlauf, Vorzeichen und Skalierung gehören zusammen**, dürfen aber nicht als derselbe Zeitbegriff behandelt werden.

## 10. Einstein, Noether und Dirac als Arbeitsprinzipien

**Noether:** Die erhaltene Ladung $N_f+2N_b$ ist hier kein dekoratives Etikett. Sie reduziert den globalen Grundzustandsvergleich auf untere, mittlere und obere Ladungssektoren und macht den kurzen Beweis möglich.

**Dirac:** Die Paarantwort ist nicht das vollständige fermionische Objekt. Die Hebung, ihr Vorzeichen und die Gradierung müssen vor der Quadratisierung bewahrt werden. Das ist eine konkrete Double-Cover-Aussage, nicht die Behauptung, eine beliebige Quadratwurzel liefere bereits den relativistischen Diracoperator.

**Einstein:** Der nächste physische Test betrifft gemeinsame Kovarianz, Kausalstruktur und Energie desselben Modells. Passende Konstanten und ein formal kovarianter Zielraum ersetzen diese gemeinsame Realisierung nicht.

**Die einfache Leitidee:** Nicht noch mehr Zahlen sammeln, sondern die kleine **gradierte Quelle vor dem Informationsverlust** festhalten; daraus Zustand und Antworten ableiten; erst dann prüfen, welche räumliche Grenztheorie sie tatsächlich trägt.

## 11. T1-T8 bleiben einzeln sichtbar

| Gate | Was diese Runde tatsächlich beiträgt | Was weiter fehlt |
|---|---|---|
| T1 Auswahl | Zwei Spin-Lifts, ein Clock-Intertwiner, ein bedingter Reflexionsselektor und Zustandsselektion in einer kleinen Klasse | Ursprüngliche gemeinsame Vertex-/Kantenreflexion, Kopienregel und Kopplungsvertrag |
| T2 markierte Seam | Die verlorene fermionische Hebungsinformation wird präzisiert | Renormiertes Half-Charge-Feld, Energie-/Adjungiertenkontrolle und tatsächliche E8-Seam-Identifikation |
| T3 gemeinsamer 3+1D-Ursprung | Ein konkret zusammengesetzter endlicher Parent | Raumdimension, lokale Algebren, Skalierung und derselbe physische Parent für alle Sektoren |
| T4 chirales Maß | Kein neuer vollständiger Feldadapter | Chirales Eich-/Weylmaß, Anomalien, Spiegelentkopplung |
| T5 Kontinuum | Vollständiger endlicher Fock-Grundsatz mit Bosonrestkontrolle | Gleichmäßiger wechselwirkender Grenzübergang und relativistische Anregungen |
| T6 Parameter | Zwei kontrollierte Modelllinien aus W und Clock | Herleitung von g/Delta und der Verbindung zu beobachteten Massen, Kopplungen und Neutrinos |
| T7 Gravitation | Kein neuer Spin-2-Nachweis | Quantisierter masseloser Spin 2 und universelle Kopplung aus demselben Parent |
| T8 Zustand/Instrumente | Eindeutiger globaler Modellgrundzustand und geladene Antwort auf ihm | Physische Herkunft der Quelle sowie native Präparation, autonome Kontrolle und beschreibbares Record |

## 12. Die nächsten entscheidenden Prüfungen

1. **Ursprüngliche Quelle statt weiterer freier Graphen:** Eine konkrete Abbildung von TFPTs Seam-/Cliffordoperationen auf das gewählte q-Feld angeben, die CAR, Clock, W-Vertex und Zustand gemeinsam erhält. Abschnitt 15 präzisiert den Angriffspunkt: die gemeinsame Vertex-/Kantenreflexion. Übereinstimmung der Clockordnung oder einer abstrakten dihedralen Relation allein reicht nicht. Scheitert die Zustandsverträglichkeit, ist das ein tatsächlicher Ausschluss dieses Adapters.
2. **Den bewiesenen Modellbereich erweitern:** Für denselben antiperiodischen Kandidaten den Kopplungsweg bis $g/\Delta=1/20$ kontrollieren. Dabei Ladungswechsel, zusätzliche niedrige Zustände und Polgewichte verfolgen. Der vorhandene Satz darf nicht über seinen kleinen Bereich hinaus zitiert werden.
3. **Physische Universalitätsklasse statt vollständiger UV-Eindeutigkeit:** Eine vorab festgelegte Verfeinerungsfolge nehmen und dieselbe geladene Antwort auf ihrem jeweiligen Grundzustand untersuchen. Entscheidend sind kleine Impulse, Skalierung, lokale Antwort und ein gemeinsamer relativistischer Feldtyp. Erst ein erfolgreicher solcher Test trägt die Arbeit an chiraler Materie und Gravitation.

Keine dieser drei Prüfungen wird hier als bereits bestanden bezeichnet. Der Gewinn ist, dass die erste Zustands-/Antwortkette für einen konkreten Lift nun ausgeführt ist und ihr Beweis nicht von einer astronomischen Matrix abhängt.

## 13. Reproduktion und Lesereihenfolge

`verify_spin_lift.py` prüft native Tensorpins, die vollständige benötigte Casimir-Grundlage, die N3-Reduktion, Vorzeichenklassen, unabhängige CAR-Kontrollen, exakte Momente, rationale Restkonstanten sowie die Operations- und Archivpräzisierungen. `replay.py` wiederholt diese Rechnung normal und optimiert und führt den historischen v480-Zeugen separat aus. Der vollständige analytische Grundzustands-/Antwortbeweis steht in den Abschnitten 5-7; bloßes Zählen grüner Bedingungen ersetzt ihn nicht.

Das Prüfprotokoll benennt ausdrücklich, welche Ergebnisse endliche Gleichheiten, welche analytische Implikationen und welche noch Herkunftshypothesen sind. Alte Dokumente und Originaleingaben werden nicht überschrieben. Die aktualisierte Hauptfassung enthält diese neue Ebene und die vollständige vorherige Hauptfassung v1.6.9 als gekennzeichneten historischen Bestand; das kurze Update ersetzt sie nicht.

## 14. Nachprüfung der beiden zuletzt zugeschickten Perspektiven

Die beiden Texte mit den Anfängen **„Ja. Nach dem erneuten Querschnitt ...“** und **„Ich sehe keine bereits versteckte Formel ...“** wurden vollständig gelesen. Ihre Vorschläge sind Prüfhypothesen, keine übernommenen Arbeitsanweisungen oder bereits bewiesene Resultate. Beide Originale liegen mit Hashes unverändert im Prüfpaket. Die folgende Prüfung ergänzt die Spin-Lift-Rechnung, ersetzt sie nicht.

### 14.1 Tragender gemeinsamer Kern, aber keine automatische Quellenauswahl

Der positive Prozesskern

$$\Gamma(u,v)=\omega(u^\dagger v)$$

ist eine gute gemeinsame Beschreibung der erreichbaren Vorgänge. Ist eine unital vorgegebene C*-Algebra mit ihrer Multiplikation und einem Zustand gegeben, bestimmt die GNS-Konstruktion die zyklische Darstellung bis auf eine zustands- und algebraerhaltende unitäre Äquivalenz. Bei vollständig zeit- und instrumentmarkierten Kernen werden die so markierten Prozesse mit rekonstruiert. Das ist die präzise Bedeutung von „gleicher vollständiger Prozess“.

**Zwei Einschränkungen sind entscheidend.** Erstens genügt die Positivität einer beliebigen Matrix über Wortnamen nicht: Ein Nullwort muss auch nach erlaubter Linksmultiplikation null bleiben. Die positive Gram-Matrix diag(1,0,1) über den Wörtern $(1,a,a^2)$ verletzt dies, denn $[a]=0$, aber $[a^2]\ne0$. Ohne Kompatibilität mit den Algebrarelationen bekommt man einen Vektorraum von Antworten, noch keine ausführbare Algebra.

Zweitens enthält ein statischer Kern keine bisher unmarkierte physische Zeit. Auf $\mathbb C^3$ besitzen

$$\Omega=(1,0,0)^T,\qquad H_1=\operatorname{diag}(0,1,2),\qquad H_2=\operatorname{diag}(0,1,3)$$

denselben eindeutigen Grundvektor und für sämtliche zeitunmarkierten Matrixwörter denselben Kern. Die Anregungsenergien und zeitabhängigen Antworten sind verschieden. Nimmt man Zeittranslationen schon in die Wortmarkierungen auf, wird diese fehlende Information **mit eingegeben**. Die Rekonstruktion ist dann korrekt, aber keine Auswahl dieser Zeittranslationen aus den statischen Daten.

Die vorgeschlagene Selbstabschlussbedingung ist deshalb ein Forschungsprogramm, noch keine definierte eindeutige Gleichung. Festzulegen sind die realisierbaren Controller, ihre Ressourcen und der Abschlussoperator; außerdem muss eine nichttriviale Lösung bewiesen werden. Reine Positivität oder „kleinste konsistente Lösung“ kann auch eine stationäre skalare Theorie zulassen. Ein Quotient nach interner Ununterscheidbarkeit spart redundante Darstellungen; er macht fehlende Eingriffe nicht ausführbar.

### 14.2 Die modulare Zeitidee ist relevant, aber noch nicht unser fehlender Hamiltonoperator

Die vorgeschlagene Verbindung zu Connes und Rovelli ist sachlich richtig: Ihre [Thermal-Time-Arbeit](https://arxiv.org/abs/gr-qc/9406019) postuliert eine physische Interpretation des vom Zustand bestimmten modularen Flusses. Das ist eine physische Hypothese auf Grundlage eines mathematischen Satzes, kein allgemeiner Beweis, dass jeder modulare Fluss eine physische Uhr ist.

Für eine volle endliche Matrixalgebra und einen treuen Zustand $\rho>0$ gilt

$$\sigma_t^\rho(A)=\rho^{it}A\rho^{-it}.
\qquad K=-\log\rho.$$

Mit der Konvention $\alpha_s^H(A)=e^{isH}Ae^{-isH}$ gilt

$$\boxed{\sigma_t^\rho=\alpha_{-\beta t}^H\ \text{für alle }t
\iff K=\beta H+cI
\iff \rho=Z^{-1}e^{-\beta H}.}$$

Beweis: Ableiten bei null ergibt $[K-\beta H,A]=0$ für jede Matrix A. Der Kommutant der vollen Matrixalgebra besteht aus Skalaren. Der Rückweg folgt direkt durch Exponentiation. Für eine direkte Summe von Matrixalgebren ersetzt ein zentrales Element die skalare Konstante.

Damit ist ein konkreter Prüfmaßstab vorhanden: Ein **unabhängig aus der Quelle gewonnener** Zustand müsste diese Beziehung erfüllen. Wird zunächst aus H ein Gibbszustand hergestellt und danach $-\log\rho$ berechnet, wurde H nicht hergeleitet. Selbst Stationarität genügt nicht: Für $H=\operatorname{diag}(0,1,2)$ ist $\rho=\operatorname{diag}(1/2,1/3,1/6)$ treu und kommutiert mit H; die modularen benachbarten Frequenzen sind jedoch $\log(3/2)$ und $\log 2$, während H gleiche Energieabstände hat. Keine gemeinsame Zeitskalierung macht beide Flüsse gleich.

**Auf dem hier bewiesenen nativen Modellgrundzustand scheitert die unmittelbar globale Variante bereits früher.** Ein reiner Grundzustand ist auf der vollen Matrixalgebra seines Ladungssektors nicht treu: Ein nichtnull Projektor orthogonal zu ihm hat Erwartungswert null. Komprimiert man auf seinen Träger, bleibt nur eine eindimensionale Algebra und trivialer modularer Fluss. Das ist keine Einschränkung der Vakuum-Modulartheorie lokaler unendlicher Algebren. Ein reiner Gesamtzustand kann auf einer echten Teilalgebra treu sein; das Beispiel

$$\Psi=\sqrt{2/3}|00\rangle+\sqrt{1/3}|11\rangle,
\qquad\rho_A=\operatorname{diag}(2/3,1/3)$$

zeigt genau diesen Unterschied. Die Wahl und physische Verfügbarkeit dieser Teilalgebra müssen aber aus der Quelle folgen. Für den algebraabhängigen Begriff von Verschränkung und zyklisch-separierenden Vektoren siehe [Wittens Darstellung](https://arxiv.org/abs/1803.04993).

Noch eine verbleibende Mehrdeutigkeit: Auf $\mathbb C\oplus M_2$ erzeugen die treuen Zustände

$$\rho_w=w\oplus(1-w)\rho_2,\qquad0<w<1$$

denselben modularen Fluss bei festem $\rho_2$. Die Blockgewichte verschwinden in der Konjugation. Der Fluss bewegt keine zentralen Superselektionsgewichte und bestimmt sie nicht. Der maximal gemischte Zustand ist zwar besonders symmetrisch und treu, liefert aber auf einer Matrixalgebra überhaupt keinen nichttrivialen modularen Zeitfluss. „Nimm den einfachsten Zustand“ allein löst daher unsere Quellen-/Uhrfrage nicht.

### 14.3 Neue Schranke für den vorgeschlagenen Kausalitätstest

Die Konstruktion von Raumzeit aus relativen modularen Flüssen ist eine ernsthafte Richtung. Sie verlangt zusätzliche Relationen der **Algebren**, nicht bloß einige ähnliche Eigenwerte. Ein relevanter mathematischer Rahmen sind halbseitige modulare Inklusionen; einen präzisierten Struktursatz geben [Araki und Zsido](https://arxiv.org/abs/math/0412061).

Für die endlichen Testalgebren gilt jedoch der einfache allgemeine Satz: Ist $\mathcal N$ endlichdimensional und

$$\sigma_t(\mathcal N)\subseteq\mathcal N\qquad(t\ge0),$$

dann ist diese Inklusion für jedes t eine **Gleichheit**. Denn eine Automorphie erhält die Vektorraumdimension. Inklusion plus gleiche endliche Dimension erzwingt Gleichheit; die inverse Automorphie gibt die Gleichheit auch für negative t. Eine echte einseitige Schrumpfung der Algebra ist so unmöglich.

Dieser Dimensionsbeweis ist nicht ein globaler Ausschluss modularer Raumzeitrekonstruktion. Er zeigt, warum ein einzelner endlicher Clockblock kein nichttriviales Beispiel der benötigten Halbseitigkeit liefern kann. Man braucht eine kontrollierte unendliche Algebra oder einen Grenzübergang, in dem die endliche Dimensionsschranke nicht mehr greift. Gerade diese Kontrolle darf nicht durch einen großen endlichen Fit ersetzt werden.

### 14.4 Phasen, Gesamtsymmetrie und Unsichtbarkeit kleiner Tests

Der zweite Text trägt in drei Punkten unmittelbar:

- **Die Schleifenphase ist entscheidende Information.** Die zwei Dreiecksmatrizen wurden erneut unabhängig exakt nachgerechnet: Fermionränge 3 und 2, Überlappungsprodukte $+1/8$ und $-1/8$, aber identische Paarmatrix mit Spektrum $(12,6,6)$. Abschnitte 3-7 gehen darüber hinaus: Für den Viererclock wird das verlorene Vorzeichen an höhere Antworten, einen Grundzustand und dessen geladene Linien angeschlossen. Eine bloße Übereinstimmung von Paarzahlen reicht tatsächlich nicht.
- **Volle Quelle statt isolierter Tensor.** Für tatsächlich gesetzte Strukturen gilt $\operatorname{Stab}(W,\text{Clock},\ldots)\subseteq\operatorname{Stab}(W)$. Eine reale Markierung kann die Gruppe einschränken; eine umbenannte Basis nicht. Der neue Viererclock wirkt nur im zusätzlichen Kopienraum und erhält gerade die volle innere Gruppe. Er löst daher keine unter innerer G-Invarianz bewiesene Kontrollsperre durch Symmetriebruch. Bei der ursprünglichen vollständigen Quelle bleibt das gemeinsame Stabilisatorproblem offen. Die bisherige Schur-Argumentation für unseren Kandidaten wird durch diese Prüfspur nicht entkräftet.
- **Endlich viele Ladungssektoren wählen kein unbegrenztes Gesetz aus.** Wenn alle Versuche $N\le N_{\max}$ erhalten, setze $m=\lfloor N_{\max}/2\rfloor+1$. Dann ist $F_m(N_b)=\prod_{j=0}^{m-1}(N_b-j)$ dort identisch null, auf ganzzahligen Bosonbesetzungen überall nichtnegativ und erstmals bei $N_b=m$ ungleich null. Folglich ist $H+\eta F_m(N_b)$ bei $\eta>0$ in sämtlichen getesteten Abläufen ununterscheidbar von H, solange die Instrumente diese Sektoren nicht verlassen. Die Deformation respektiert Gesamtladung und innere Symmetrie. Der allgemeine Beweis ist das Nullprodukt; die Reproduktion ergänzt exakte Beispiele bis $N_{\max}=12$. Ein begründeter Grad-/Operationsvertrag kann die Deformation ausschließen, kleine Tests allein nicht.

Die Universalitätsalternative aus beiden Texten bleibt sinnvoll: Für makroskopische Gesetze muss möglicherweise eine robuste Klasse und nicht genau ein Mikrograph ausgewählt werden. Das ersetzt die RG-/Kontinuumsprüfung nicht. Ein Code ist außerdem ein möglicher Kommunikationstest, kein universell vorgeschriebenes Naturgesetz.

### 14.5 Konsequenz für die weitere Arbeit

Die Priorität wird präziser, nicht breiter: **Quelle samt fermionischem Lift und realem Operationssatz bestimmen; auf ihr Zustand und Antworten gemeinsam berechnen; dann lokale Algebren und ihre Skalierung prüfen.** Ein unabhängig gewonnener treuer Teilzustand und eine nichttriviale modulare Vergleichsrelation wären ein echter zusätzlicher Anschluss. Ein aus H definierter Gibbszustand oder ein bereits zeitmarkierter vollständiger Prozesskern wäre dagegen eine konsistente Umformulierung, noch keine neue Herleitung der Dynamik.

Keiner der beiden Texte liefert bereits die fehlenden Voraussetzungen für eine vollständige TOE, RH, effiziente Faktorisierung oder P versus NP. Ihre tragenden Hinweise sind integriert, ihre offenen Auswahlfragen bleiben sichtbar. Die neuen kleinen Gegenrechnungen sind in `verify_new_aspects.py` von der großen Spin-Lift-/Fockrechnung getrennt; der gemeinsame Replay führt beide normal und optimiert aus.

## 15. Fortgesetzte Auswahlprüfung: fehlt eine Spiegelungsrelation?

Der Nutzer bat während der Konsolidierung um weitere Arbeit. Deshalb wurde nicht nur die neue Quelle beschrieben, sondern unmittelbar die wichtigste noch verdeckte Wahl angegriffen: **Warum gerade die gleichstarke Nachbarmischung?**

### 15.1 Ein Gegenmodell gegen eine zu starke Deutung des Grundzustandssatzes

Ersetze die festgelegte Quelle zunächst durch die einfache reelle Familie

$$U_\eta(a,b)=aI+bR_\eta,\qquad a^2+b^2=1.$$

Alle einzelnen Quellen bleiben CAR-normiert, und $[U_\eta,R_\eta]=0$ gilt für jedes a und b. Der gemeinsame Clock und die volle innere Symmetrie bleiben erhalten. Ihre Einteilchenspektren sind

$$\operatorname{spec}S_+=\{1-2ab,1,1,1+2ab\},$$

$$\operatorname{spec}S_-=\{1-\sqrt2ab,1-\sqrt2ab,1+\sqrt2ab,1+\sqrt2ab\}.$$

Für den periodischen Lift und $(a,b)=(3/5,4/5)$ ist der kleinste Eigenwert $1/25>0$. Es gibt keine freie Fermionrichtung, obwohl das Umlaufvorzeichen positiv ist. Der Grundzustandsbeweis aus Abschnitt 6 gilt unverändert mit $\delta=(15/2)/25=3/10$. Bei $0<|g|/\Delta\le1/10000$ ist seine Ladungstrennung mindestens

$$\left(\frac3{10}-\frac{1920^2}{10000^2}\right)\frac{g^2}{\Delta}
=\frac{8223}{31250}\frac{g^2}{\Delta}>0.$$

Damit hat **auch dieser unverdrehte, ungleich gewichtete Kandidat** einen eindeutigen vollen Grundzustand bei N=256. Die Paarmatrix ist hier $8I+8a^2b^2 A_{C_4}$ und nicht dieselbe wie bei der zuvor fixierten gleichstarken Quelle. Das ist also kein Gegenbeispiel gegen die Sätze der Abschnitte 3-7, aber eines gegen die weitergehende Behauptung „Clock plus eindeutiger Grundzustand erzwingen den negativen Lift“. Die Gewichtung muss mit ausgewählt werden.

### 15.2 Eine kleine Spiegelungsregel würde die Gewichtung bestimmen

Für beide Lifts wähle den reellen signierten Reflexionsoperator J durch

$$Jf_0=f_0,\qquad Jf_x=\eta f_{4-x}\quad(x=1,2,3).$$

Er erfüllt exakt $J^2=I$ und $JR_\eta J=R_\eta^{-1}$. Setze $L=R_\eta J$; auch $L^2=I$. Auf dem markierten Zyklus entspricht J einer Vertexreflexion, L der dazu verschobenen Kantenreflexion. Die zugehörigen Paar-/Bosonbänke werden mit der vorzeichenlosen Permutation von L reflektiert. Dies ist der ausdrücklich erklärte gemeinsame Reflexionsvertrag, nicht irgendeine frei austauschbare Basis.

Nun gilt die kurze Identität

$$\boxed{U(a,b)J=L\,U(b,a).}$$

Die Spiegelung vertauscht also genau die beiden Quellgewichte. Beim ursprünglichen Paarvertex sind die Kopienkoeffizienten die äußeren Produkte der Quellenzeilen mit sich selbst, ohne komplexe Konjugation. Die Gleichheit der reflektierten Paaroperatoren verlangt deshalb

$$a^2=b^2.$$

Notwendigkeit sieht man bereits an den Koeffizienten, die zwei interne Fermionen vom linken beziehungsweise rechten Kopienort entnehmen. Für Suffizienz gilt bei $a=b$ bereits $UJ=LU$, bei $a=-b$ entsprechend $UJ=-LU$; das gemeinsame Minus verschwindet im Paar. Zusammen mit der Normierung folgt $|a|=|b|=1/\sqrt2$. Die vier Zeilen und ihre Paarprodukte wurden exakt für beide Lifts geprüft.

**Bedingter Auswahlsatz:** Innerhalb der reellen, gleichförmigen Zweinachbar-Klasse wählen (i) die erklärte gemeinsame Vertex-/Kantenreflexion und (ii) keine exakt freie Fermionrichtung die balancierte antiperiodische Quelle aus, bis auf Quellenzeichen und entsprechende lokale Vorzeichenkonventionen. Denn die Reflexion erzwingt Balance; bei Balance hat nur der negative Viererlift vollen Rang. Für vier Knoten sind die beiden relativen Vorzeichen der balancierten Mischung durch alternierende lokale Fermionvorzeichen äquivalent. Die zugehörigen Bosonzeichen dürfen dabei unverändert bleiben, weil der Vertex gerade ist.

Das ist eine kleinere fehlende Bedingung als eine beliebige neue Dynamik: **Wende dieselbe Spiegelung auf Fermionorte und Paarübergänge konsistent an.** Sie ist dennoch eine Zusatzvoraussetzung, solange sie nicht aus der eigentlichen Quelle stammt. Das Fehlen freier Zuschauer ist ebenfalls ein hier erklärtes Auswahlkriterium, nicht ein allgemeines Naturgesetz.

### 15.3 Tatsächlicher Anschluss an ältere TFPT-Struktur

In `origin_theory.tex` ist die Relation $\sigma\rho\sigma=\rho^{-1}$ bereits Teil der geometrischen Normalform. `v177_seam_marking_kernel.py` verwendet explizit $\rho:z\mapsto iz$ und $\sigma:z\mapsto1/z$ auf den vier Marken. `v180_clock_is_mobius.py` trennt die Clock-Geometrie weiterhin von der ursprünglichen Realisierungsvoraussetzung. Diese beiden Dateien wurden für diesen Anschluss gelesen, nicht als vollständiger neuer Seam-Beweis ausgeführt.

Somit wird die Spiegelung nicht als neue Zahlenidee importiert. Es fehlt aber die entscheidende **Operatorzuordnung**: Die geometrische sigma muss auf den ursprünglichen fermionischen Ressourcen als das passende J wirken und zugleich die W-Paarbänke mit der verschobenen Kantenwirkung von L abbilden. Die abstrakte dihedrale Relation allein bestimmt diese relative Wirkung auf zwei verschiedenen Ressourcen nicht. Auch Reflexionspositivität ist nicht dasselbe wie diese unitäre Paarvertex-Symmetrie. Ein physischer Lorentz-/Pin-Adapter wird aus den reellen Vorzeichenmatrizen nicht behauptet.

Eine zusätzliche exakte Negativkontrolle macht diese Grenze sichtbar: Reflektiert man die Paarbänke stattdessen mit **derselben Vertexpermutation** wie die Fermionorte, verlangt die Paar-Kovarianz in diesem Ansatz $b=0$. Schon ein diagonaler Kopienkoeffizient des Differenzoperators ist $b^2$. Diese andere Zuordnung erlaubt also nur die entkoppelte Vor-Ort-Quelle statt der balancierten Nachbarquelle. Die Wahl zwischen Vertex- und Kantenwirkung ist physischer Inhalt, nicht durch das Wort „Spiegelung“ erledigt.

Der nächste besonders aussagekräftige Test lautet damit enger: **Liefert die ursprüngliche markierte TFPT-Seam genau dieses gemeinsame Paar von Spiegelungswirkungen, einschließlich Zustand und Vertex?** Ein positiver Nachweis würde in dieser Quellenklasse die Mischungswahl und das Umlaufvorzeichen zusammen ersetzen. Ein negativer Nachweis würde diesen konkreten Anschluss ausschließen. Der Kopplungswert, die Verfeinerungsregel und die T1-T8-Gesamtnachweise blieben davon getrennte Aufgaben.
