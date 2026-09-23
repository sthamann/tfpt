# Zustand und Zeit ohne Zirkularität — Ergebnis

## Antworten zuerst

**Welche freie Wahl wurde beseitigt? — exakt.** Im treuen
Zweigeneratoransatz
\(\rho_{a,b}\propto\exp(-aN_b-bX)\) erzwingen bereits Aufspaltung und
maximale Konversion des N=4-Blocks
\[
\frac{|b|}{|a|}=\frac1{20},\qquad
\frac{\Delta E}{|a|}=\frac{\sqrt{29}}5,\qquad
P_{\max}=\frac4{29}.
\]
Der Interventionsarm fixiert zusätzlich das native Vorzeichen. Damit ist
der einzige mehrfach treffende Punkt
\(\rho\propto\exp(-\beta H)\). Er wird nicht als Lösung gezählt, weil er
den abzuleitenden Hamiltonoperator bereits als Gibbsgewicht benutzt.

**Welche Annahme bleibt? — offen.** Es fehlt ein von \(H\), seinen
Eigenvektoren, Gibbsgewichten und gemessenen Zielfrequenzen unabhängiges
Prinzip, das einen treuen Zustand mit genau diesem Logarithmus auswählt.
Global fehlt außerdem weiterhin die Sektorwahl: Quelle, Randbedingung oder
ein ausdrückliches Prinzip.

**Was unterscheidet? — bedingt.** Ein positiver Kandidat muss vor jeder
Zielfrequenzmessung \(\rho\) aus Quelldaten konstruieren. Dann sind auf
demselben Zustand nacheinander zu prüfen: N=4-Konversion \(4/29\), die
höhere Antwort \(I_4=1+c^4\) und der \(Z_b\)-Quotient
2,414201341270956. Noch stärker wäre ein Beweis
\(\log\rho=-\beta H+cI\) aus unabhängigen Quell-/Randaxiomen; ohne ihn ist
eine Übereinstimmung nur Rekonstruktion des schon eingesetzten \(H\).

## 1. Kandidaten und Voraussetzungen

„Stationär“ bedeutet hier stationär unter der zu vergleichenden nativen
H-Dynamik. Jeder treue Zustand ist unter seinem eigenen modularen Fluss
automatisch invariant.

| Kandidat | positiv | normiert | treu auf voller Algebra | H-stationär | geprüfter Bereich |
|---|---|---|---|---|---|
| Sektortrace \(I/d\) | PASS | PASS | PASS | PASS | alle drei Blöcke |
| Quellenkontrolle \(I_4/4\) | PASS | PASS | PASS auf \(M_4\) | nicht unabhängig gesichert | Quellenfaktor |
| Quellenstrahl \(P_s\) | PASS | PASS | **FAIL** | **FAIL** | Rang-1-Träger |
| \(\rho_q\propto q^{N_b}\), \(q>0\) | PASS | PASS | PASS | nur \(q=1\) | alle drei Blöcke |
| \(\rho_X\propto e^{-\kappa X}\) | PASS | PASS | PASS | nur \(\kappa=0\) oder \(\Delta=0\) | quellverbundene Blöcke |
| leerer Randvakuumstrahl | PASS | PASS | **FAIL** auf voller Algebra | PASS | Vakuumträger |
| \(e^{-\beta H}\), Kontrolle | PASS | PASS | PASS | PASS | alle Blöcke; **zirkulär** |

**Exakt geprüft** wurden der native 9-dimensionale Achtblattstern, der
N=4-Singulettblock
\[
H_4/\Delta=\begin{pmatrix}2&1/5\\1/5&1\end{pmatrix}
\]
und der helle 120-Träger als 60 identische aktive Zweierblöcke mit
Kopplung \(\sqrt8/20\). Es wurde keine dichte Matrix über Dimension 120
aufgebaut.

## 2. Modularvoraussetzungen und endliche native Algebra

Nach der Thermal-Time-Hypothese von
[Connes und Rovelli](https://arxiv.org/abs/gr-qc/9406019) wird der
modulare Automorphismenfluss eines Zustands als physischer Zeitfluss
gelesen. Dafür braucht man eine von der gesuchten Dynamik unabhängig
gegebene Algebra und einen treuen Zustand; äquivalent einen zyklischen und
separierenden Vektor in der GNS-/Standarddarstellung.

Die getesteten nativen Algebren sind endliche Typ-I-Faktoren
\(M_d(\mathbb C)\). Auf dem physikalischen irreduziblen \(d\)-Raum gibt
es für \(d>1\) keinen separierenden Vektor. In der
Hilbert-Schmidt-Standardform ist \(\rho^{1/2}\) genau dann zyklisch und
separierend, wenn \(\rho>0\) treu ist. Dann gilt exakt
\[
\Delta_\rho=L_\rho R_\rho^{-1},\qquad
\sigma_t(A)=\rho^{it}A\rho^{-it}.
\]
Reine Quellen-/Randstrahlen erfüllen diese Voraussetzung auf der vollen
Algebra nicht; nach Einschränkung auf ihren Rang-1-Träger ist der Fluss
trivial.

## 3. Modulare Flüsse

| Zustand | Modularoperator/-generator | Ergebnis |
|---|---|---|
| \(I/d\), \(I_4/4\) | \(\Delta_\rho=I\), \(\sigma_t=\mathrm{id}\) | **FAIL**, trivial |
| \(q^{N_b}\) | \(\Delta_\rho(E_{ij})=q^{n_i-n_j}E_{ij}\) | nichttrivial, aber nur \(N_b\)-Phasen; **H-mismatched** |
| \(e^{-\kappa X}\) | Generator \(-\kappa\,\mathrm{ad}_X\) | nichttrivial; fehlende \(N_b\)-Detuningstruktur; **H-mismatched** |
| Quellen-/Randstrahl | auf \(M_d\) nicht definiert | Voraussetzung **FAIL** |
| \(e^{-\beta H}\) | Generator \(-\beta\,\mathrm{ad}_H\) | MATCH, aber **zirkulär** |

**Exakt.** Auf \(M_d\) erzwingt die Gleichheit zweier innerer Flüsse
\(\log\rho+\beta H=cI\), denn ihre Generatorendifferenz kommutiert mit
allen Matrixeinheiten und ist daher zentral. Der Matrixeinheitencheck
wurde auf jedem aktiven Zweierfaktor ausgeführt. Für den hellen
120-Träger gilt dieselbe Aussage auf \(M_2\otimes I_{60}\).

Modularspektren: beim N=2-Stern hat \(X\) die Eigenwerte
\(\{-\sqrt8,0^7,+\sqrt8\}\), beim N=4-Block \(\{-4,+4\}\), beim hellen
Träger \(\{-\sqrt8,+\sqrt8\}\) je 60-fach. Diese nichttrivialen Flüsse
sind nicht die native Kombination \(N_b+X/20\).

## 4. Vorgegebene dimensionslose Antworten

| Kandidat | N=4: \(\sqrt{29}/5,\ 4/29\) | \(I_4=1+c^4\) | \(Z_b\)-Quotient |
|---|---|---|---|
| Trace / \(I_4/4\) | FAIL: kein Fluss | undefiniert | kein Signal |
| Quellen-/Randstrahl | keine volle Modularzeit | undefiniert | undefiniert |
| \(q^{N_b}\) | FAIL: \(1,0\) | undefiniert | beide Antworten 0 |
| \(e^{-\kappa X}\) | FAIL: keine Detuningskala, \(P_{\max}=1\) | **PASS exakt** | FAIL: 0 |
| \(e^{-aN_b-bX}\) | PASS genau bei \(|b/a|=1/20\) | PASS für \(b\ne0\) | PASS beim nativen Vorzeichen |

Die letzte Zeile trifft mehrere Antworten nur am H-Gibbs-Punkt. Eine freie
Modularzeitskala kann Aufspaltungen umskalieren, aber weder \(4/29\),
\(1+c^4\) noch den Interventionsquotienten ersetzen.

**Numerisch.** Aus denselben vorgegebenen Wahrscheinlichkeiten folgen
\[
\frac{0{,}0005299169088385700}{0{,}0002194998817122665}
=2{,}414201341270956.
\]
Der Replay reproduziert beide Werte und den Quotienten. Die Formeln und
Kandidatenausschlüsse sind exakt; nur die Cosinus-Auswertung am Prüfpunkt
ist numerisch.

## 5. \(H+\mu N\): intern gegen global

**Exakt, sektorintern.** Auf \(N=n\) gilt
\[
(H+\mu N)|_{\mathcal H_n}=H|_{\mathcal H_n}+\mu nI.
\]
Eigenvektoren, Energiedifferenzen, Heisenbergfluss, Konversionsraten und
normierte feste-Sektor-Zustände bleiben unverändert. Der zusätzliche
Faktor ist nur eine globale Phase beziehungsweise ein skalarer
Boltzmannfaktor. Für einen konstanten Offset innerhalb eines festgelegten
Sektors ist daher keine experimentelle Zustandsauswahl nötig.

**Exakt, global.** Zwischen Sektoren ändern sich die Energien zu
\(E_n+\mu n\). Die Floors sind
\[
E_{56}=-21/20,\quad E_{60}=-9/8,\quad E_{64}=-6/5,
\]
also jeweils \(-3/160\) pro Ladung. Bei \(\mu=3/160\) liegen diese
Floor-Linien am Vakuum; bei \(\mu=1/50\) liegen sie exakt \(1/800\) pro
Ladung darüber. **Bedingt durch den vorgegebenen Formbound** gewinnt dort
das leere Vakuum. Der numerische Ritz5-Kreuzwert 0,01779 bleibt von der
Floor-Grenze 0,01875 getrennt.

## 6. Urteil und Ausschlussumfang

**Urteil: sauber begrenzter Ausschluss, keine Zustandsregel gefunden.**
Ausgeschlossen sind auf den drei endlichen nativen Testblöcken:

1. tracial/maximal gemischte Sektor- und gleichgewichtete Quellenregeln;
2. reine Quellen-/Randstrahlen als volle modulare Zustände;
3. alle treuen reinen \(N_b\)-Gewichtungen;
4. alle treuen reinen W-Quelloperator-Exponentialzustände;
5. der Zweigeneratoransatz als *unabhängige* Herleitung: sein einziger
   mehrfach treffender Punkt ist genau die verbotene H-Gibbs-Regel.

**Offen** bleiben Zustandsprinzipien außerhalb dieser Klasse, größere
Algebren vom Typ II/III, nichtmodulare Zeitregeln und eine unabhängige
Quelle-/Randherleitung von \(\rho\). Der endliche Typ-I-Befund widerlegt
nicht die Thermal-Time-Hypothese allgemein.

Replay: **PASS**, 100 exakte Guards + 4 numerische Kontrollen; alle drei
Checker normal/`-OO` byteidentisch.

---

## Nachtrag: Unteralgebra-Route

### N1. Korrigierter allgemeiner Satz

**Exakt.** Für
\[
\mathcal B\simeq\bigoplus_i M_{n_i}(\mathbb C)\otimes I_{m_i}
\subsetneq\mathcal A
\]
wird der eingeschränkte Zustand blockweise durch
\[
h_i=\operatorname{Tr}_{m_i}(P_i\rho P_i)
\]
vertreten. Er ist auf \(\mathcal B\) genau dann treu, wenn jedes \(h_i\)
strikt positiv ist und kein Zentralblock Gewicht null trägt. In der
Standardform gilt
\[
\sigma_t^{\mathcal B}(A)_i=h_i^{it}A_i h_i^{-it}.
\]
Da \(h_i\) eine partielle Spur ist, kann globales \(\rho\) rein und
insbesondere keine Funktion des globalen \(H\) sein. Ein exakter
Schmidt-Zeuge dieses Checkers hat global Rang eins, aber
\(h=\operatorname{diag}(1/3,2/3)\) und ist auf
\(M_2\otimes I_2\) treu.

**Kontrast zur vollen Algebra.** Für \(\mathcal B=\mathcal A=M_d\)
verschwindet die partielle Kommutanteninformation. Stimmen zwei innere
Ableitungen auf allen Matrixeinheiten überein, kommutiert ihre
Generatorendifferenz mit ganz \(M_d\), ist also skalar:
\(\log\rho=-\beta H+cI\). Genau dieser Zentralisatorschritt gilt auf einer
echten Unteralgebra nicht global. Für einen dynamischen Vergleich ist aber
zusätzlich \([H,\mathcal B]\subseteq\mathcal B\) nötig; bloßes
Komprimieren \(PHP\) ist keine eingeschränkte Automorphismengruppe, wenn
Amplitude aus \(\mathcal B\) herausleckt.

### N2. Kandidat 1 — Zwei-Chart-Verschränkung

**Bedingte Zustandsdefinition, danach exakt.** Für je zwei Fermionmoden
pro Chart wurde der natürliche symmetrische Quellpaarzustand
\[
|\Phi_c\rangle=
\frac{|P_L\rangle+|P_R\rangle}{\sqrt{2(1+c^2)}}
\]
aus \(f_i^L=a_i\) und
\(f_i^R=c\,a_i+\sqrt{1-c^2}\,d_i\) gebaut. Auf der linken
Fermion-CAR-Algebra \(M_4=\operatorname{CAR}(a_1,a_2)\) hat \(\rho_L\)
die folgenden exakten Spektren:

| \(c^2\) | Spektrum \(\rho_L\) | treu auf \(M_4\) | Spreizung von \(H_E=-\log\rho_L\) |
|---:|---|---|---|
| 0 | \(1/2,0,0,1/2\) | FAIL, Rang 2 | 0 auf dem Träger |
| \(1/4\) | \(9/40,3/40,3/40,5/8\) | **PASS** | \(\log(25/3)\approx2{,}120264\) |
| \(1/2\) | \(1/12,1/12,1/12,3/4\) | **PASS** | \(\log9\approx2{,}197225\) |
| 1 | \(0,0,0,1\) | FAIL, Rang 1 | 0 auf dem Träger |

Die beiden inneren Überlappungen retten also tatsächlich die
Faithfulness — der frühere Vollalgebra-Ausschluss war dafür zu grob.
Sie liefern aber **keine Dynamikauswahl**: Auf der reinen Fermionchart ist
\(PHP=0\), während \(H_E\) bei \(c^2=1/4,1/2\) nichtzentral ist.
Noch entscheidender ist \([H,M_4]\not\subset M_4\), weil das native
Vertexpaar in den L-Boson übergeht. Nach Erweiterung auf den kleinsten
H-invarianten Paar/Boson-Faktor \(M_2\) ist der Quellpaarzustand wieder
Rang eins und nicht treu.

**Vergleiche:** N=4-Aufspaltung/\(4/29\) FAIL; \(I_4=1+c^4\) wird nicht
als Modularantwort erzeugt (das \(c\) steckt nur schon im Zustand);
\(Z_b\)-Quotient FAIL. Bei \(c^2=0,1\) stimmt nur der triviale
Trägerfluss mit einer Nullkompression überein, nicht mit nativer Dynamik.

### N3. Kandidat 2 — W-Paar-Kondensat

**Exakt auf dem N=4-Singulettblock.** Die W-only-Trunkierung von
\[
|\Psi_\lambda\rangle\propto e^{\lambda T^\dagger}|F\rangle
\]
ist wegen des exakten W-Matrixelements 4
\((|0\rangle+4\lambda|1\rangle)/\sqrt{1+16\lambda^2}\).
Da beide Basisvektoren Singulette sind, ist ihre G-invariante
Observablenalgebra der volle Multiplizitätsfaktor \(M_2\). Die Dichtematrix
hat für jedes endliche \(\lambda\) Rang eins: **nicht treu**, also kein
voller modularer Fluss auf \(M_2\).

Auf der diagonalen Unteralgebra \(\mathbb C\oplus\mathbb C\) ist der
Zustand für \(\lambda>0\) treu, aber deren modularer Fluss ist exakt
trivial. Außerdem erhält \(H_4\) diese Diagonalalgebra wegen des
Offdiagonaleintrags \(1/5\) nicht. Auf dem hellen
120-Träger ist
\(\mathcal B_G=M_2\otimes I_{60}\); der W-kohärente
Multiplizitätszustand bleibt Rang eins. Eine Wahl von \(\lambda\) kann
daher weder \(\sqrt{29}/5\), \(4/29\), \(1+c^4\) noch den
\(Z_b\)-Quotienten modular fitten.

### N4. Kandidat 3 — gefüllter Zustand

**Exakt.** \(|F\rangle\langle F|\) ist auf dem N=4-Singulett-\(M_2\)
Rang eins und nicht treu. Allgemein gibt der Zustand auch allen anderen
direkten Summanden der G-Kommutante Gewicht null. Auf seinem
eindimensionalen Trägereck \(\mathbb C\) ist er zwar treu, der modulare
Fluss dort aber Identität. Alle drei dimensionslosen Dynamikvergleiche
sind damit FAIL beziehungsweise undefiniert.

### N5. Urteil des Nachtrags

**Die Unteralgebra-Route ist mathematisch real, liefert hier aber noch
keine nichtzirkuläre Zustandsregel.** Kein getesteter Kandidat ist auf
derselben Unteralgebra zugleich

1. treu,
2. unter der nativen H-Dynamik abgeschlossen,
3. modular nichttrivial und
4. bei mehreren vorgegebenen dimensionslosen Antworten passend.

Der neue Ausschluss ist weiterhin endlich und kandidatengebunden. Offen
bleibt insbesondere ein aus W erzeugter global verschränkter Zustand,
dessen partielle Spur auf dem H-invarianten
\(M_2\)-Multiplizitätsfaktor strikt positiv ist. Er müsste ohne
H-Spektraldaten konstruiert werden und anschließend \(4/29\),
\(1+c^4\) und den Interventionsquotienten gemeinsam bestehen.

Nachtrags-Replay: **PASS**, insgesamt 141 exakte Guards + 6 numerische
Kontrollen; alle vier Checker normal/`-OO` byteidentisch.
