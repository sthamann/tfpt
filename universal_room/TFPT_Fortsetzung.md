# TFPT und Universalraum: korrigierte Rekonstruktion und konkrete Fortsetzung

Stand: 14. September 2026. Unabhängige Untersuchung der vier bereitgestellten Dokumente.

## Ergebnis und Reichweite

Die Fortsetzung liefert eine exakte Faktorisierung des festen 60-Strahlen-Prozesses, eine geschlossene Zweizellen-Energieformel, ein auslesbares relatives Uhrprotokoll, eine explizite bedingte Vierlesarten-Uhr und einen genau lösbaren Vermittlungsmechanismus für antisymmetrischen Austausch. Sie korrigiert insbesondere die pauschale Minimalität von 240 Koordinaten und den Schluss von fehlenden adjungierten Darstellungen auf verbotene Mehrträgerzustände.

Es handelt sich weder um einen vollständigen physikalischen Rekonstruktionssatz noch um eine neue Lösung von RH, Faktorisierung oder P versus NP. Die in den Quellen formulierten Abschlussbedingungen T1 bis T8 werden durch diese Untersuchung nicht geschlossen. Diese Grenze folgt hier aus ausdrücklich identifizierten fehlenden Eingaben, nicht aus dem Alter oder Schwierigkeitsgrad der offenen Fragen.

Die beigefügte Datei `pruefer.py` konstruiert die relevanten endlichen Objekte unabhängig aus den in den Dokumenten angegebenen Formeln. Sie benutzt keine Dateien des ursprünglichen Repositoriums. Ihre 148 Prüfbedingungen bestehen: 108 als exakte Identitätsprüfungen beziehungsweise endliche ganzzahlige Prüfungen und 40 als numerische Kontrollen. Normale Ausführung und `python -OO` erzeugen bytegleiche Ergebnisdateien. Diese Anzahl ist kein Maß für unabhängige Entdeckungen oder empirische Bestätigung.

### Quellenkürzel

Q0: `Eingefügter Text.txt`, insbesondere die Abschnitte über vollständige Ableitung, 240 Koordinaten und Rechenkomplexität.

Q1: `tfpt_compiler_universalraum_2026-09-13.pdf`, vor allem Kapitel 8 bis 14, Seiten 12 bis 18.

Q2: `tfpt_anschluss_zellen_seam_2026-09-14.pdf`, insbesondere Abschnitte 3 bis 5, Tabelle 2 auf Seite 4 und Anschlussprogramm auf Seite 6.

Q3: `TFPT_UNIVERSALRAUM_INVERSION_2026-09-14.md`, insbesondere Abschnitte 4 bis 8 und 11.

Die SHA256 Werte der tatsächlich bereitgestellten Dateien stehen in `quellenmanifest.json`.

## 1. Zuerst müssen drei verschiedene Prozesse getrennt werden

Die Quellen behandeln mindestens drei miteinander verwandte, aber nicht identische Beschreibungen:

1. Einen fest gewählten klassischen Prozess T auf 60 Kontext-Ergebnis-Paaren. Hier wird jeweils scharf gemessen und die nächste Kontextwahl mit K=B/7 getroffen.
2. Eine allgemeinere klassische und quantenmechanische Blockbeschreibung X=(X_C), in der jeder Kontext einen beliebigen positiven 4 mal 4 Block tragen kann.
3. Einen kohärenten Gesamtprozess mit Aufzeichnungsregistern, in dem diese Register später erneut benutzt oder interferometrisch gelesen werden dürfen.

Ein Minimalitätssatz für die dritte Beschreibung darf nicht aus einer Koordinatenzählung der zweiten hergeleitet werden. Ein Gegenbeispiel für allgemeinere Blockzustände darf nicht ohne Prüfung auf die eingeschränkten Zustände direkt nach der scharfen Messung übertragen werden.

Q3 selbst enthält die richtige Einschränkung: Für immer frische Register ist eine autonome reduzierte Regel möglich. Das dortige kohärente Zeugenpaar beweist deshalb die Unvollständigkeit einer bestimmten Auslesung unter bestimmten erlaubten Fortsetzungen. Es beweist nicht, dass TFPT als gesamte Theorie ontologisch nur ein Schatten genau eines bereits identifizierten Universalraums ist.

### 1.1 Exakte Faktorisierung des 60-Strahlen-Prozesses

Seien P_a, a=1,...,15, die nichttrivialen hermiteschen Zwei-Qubit-Paulis mit Tr(P_a P_b)=4 delta_ab. C summiert die vier Strahlgewichte eines Kontextes. F liest die 15 nichttrivialen Pauli-Erwartungswerte aus:

\[
C_{D,(C,s)}=\delta_{DC},\qquad
F_{a,(C,s)}=\operatorname{Tr}(P_a\Pi_{C,s}).
\]

Dann gelten in der aus den Pauli-Kontexten rekonstruierten Darstellung exakt

\[
CC^T=4I_{15},\quad FF^T=12I_{15},\quad CF^T=0,
\]

und der Prozess besitzt die geschlossene Darstellung

\[
\boxed{T=\frac1{28}\left(C^TBC+F^TF\right).}
\]

**Beweis.** Im selben Kontext haben identische Strahlen F-Skalarprodukt 3, verschiedene Strahlen das Skalarprodukt -1. Zwei verschiedene inzidente Kontexte teilen genau eine Pauli-Richtung; ihre Strahlvektoren haben dort Skalarprodukt +1 oder -1. Nichtinzidente Kontexte haben F-Skalarprodukt 0. Zusammen mit B ergeben sich genau die Einträge 1/7, 1/14 und 0 der Born-Übergangsmatrix. Die drei Gramidentitäten folgen aus den vier Vorzeichenkombinationen in jedem Kontext und der Tatsache, dass jede Pauli-Richtung in drei Kontexten vorkommt.

Daraus folgt unmittelbar

\[
CT=(B/7)C,\qquad FT=(3/7)F.
\]

Für q=Cp und r=Fp lautet die gesamte folgende Strahlverteilung

\[
\boxed{p'=\frac1{28}(C^TBq+F^Tr).}
\]

**Konsequenz:** Im festen Messprotokoll bestimmen Kontextverteilung und Systemauslesung gemeinsam bereits die vollständige nächste Strahlverteilung. Gleiche q und r können dort nicht verschiedene nächste p erzeugen.

Da B invertierbar ist und die Zeilenräume von C und F orthogonal sind,

\[
\operatorname{rank}T=30,\qquad \dim\ker T=30,
\qquad \ker T=\ker C\cap\ker F.
\]

Das volle Spektrum lautet

\[
\operatorname{spec}T=
\{1^{[1]},(2/7)^{[9]},(-2/7)^{[5]},(3/7)^{[15]},0^{[30]}\}.
\]

Es gibt also 30 lineare Koordinaten der festen zukünftigen Verteilung, einschließlich ihrer Normierung; normierte Zustände liegen in einer affinen Menge mit höchstens 29 Dimensionen. Diese Aussage betrifft nicht die Wiedergewinnung einer bereits vergangenen Ergebnisverteilung und nicht beliebige zusätzliche Eingriffe.

### 1.2 Was aus den 240 CQ-Koordinaten wird

Für die natürliche Erweiterung des beschriebenen Messschritts

\[
\Phi(X)_D=\sum_C K_{DC}\,\Delta_D(X_C)
\]

ist jeder Ausgangsblock nach einem Schritt in seiner Kontextbasis diagonal. Deshalb ist die Bilddimension höchstens 60. Sie ist genau 60: Die invertierbare Kontextmischung wird von einer Projektion auf die 60 diagonalen Richtungen gefolgt.

In Pauli-Koordinaten zerfällt Phi in 16 Blöcke der Größe 15. Der Identitätsblock ist K. Jeder nichttriviale Pauli-Block besitzt nach dem ersten Schritt Rang 3 und nach dem zweiten Rang 1. Folglich

\[
\operatorname{rank}\Phi=60,\qquad
\operatorname{rank}\Phi^2=30.
\]

Diese Formeln werden im Prüfer über exakte rationale Ränge kontrolliert. Die Blockbeschreibung mit 240 reellen Koordinaten ist ein nützlicher allgemeiner Eingangsraum, aber für diese feste Ausführung kein minimaler dauerhaft autonomer Informationsraum.

Bei beliebigen Eingriffen vor einer Messung oder bei kohärenter Registerrückkopplung können zusätzliche Richtungen wieder relevant werden. Deshalb muss jeder weitere Minimalitätssatz seine zulässigen Eingriffe und Zustandsklasse zuerst einfrieren.

### 1.3 Warum 240 nicht automatisch E8 bedeutet

Die 240 E8-Wurzeln sind 240 besondere Vektoren in einem acht-dimensionalen reellen Raum, nicht 240 unabhängige Zustandskoordinaten. Auch ein allgemeiner CQ-Raum mit 240 reellen Koordinaten wird dadurch nicht zur E8-Lie-Algebra. Deren Dimension ist 248 und ihre Lie-Klammer, Metrik und Integraldaten sind zusätzliche Struktur.

Eine bloße Bijektion zweier Mengen mit 240 Elementen hat daher sehr wenig Aussagekraft. Ein belastbarer Anschluss müsste mindestens Paarungen, erlaubte Operationen, Klammerstruktur, Positivität und die konkrete Auslesung miteinander verflechten.

## 2. Der Hüllensatz ist richtig; seine physikalische Verwendung ist bedingt

Q2 beweist korrekt:

\[
\operatorname{supp}\rho_{ij}\subset\Lambda^2\mathbb C^4\quad\forall i<j
\quad\Longrightarrow\quad
\psi\in\Lambda^N\mathbb C^4.
\]

Für N=4 ist dieser Raum eindimensional, für N>=5 ist er null. Dieselbe Aussage gilt für gemischte Zustände mit entsprechender Trägerbedingung.

Die physikalische Zusatzannahme ist der linke Teil: Warum muss jeder reale Paarzustand vollständig im antisymmetrischen Raum liegen? Dass eine Darstellung nicht in der adjungierten 248 vorkommt, beantwortet diese Frage nicht. Ein Generatorraum und ein Mehrteilchen-Zustandsraum sind unterschiedliche mathematische Objekte. Insbesondere bleibt 4 tensor 4 = 6 plus 10 als Zustandszerlegung bestehen.

Auch N=4 folgt nicht allein aus der Ausschließung von N>=5. Für N=1,2,3 existieren ebenfalls antisymmetrische Zustände. Vier ist unter diesen Bedingungen die maximale Größe und die erste eindeutige SU(4)-Singulettgröße; eine allgemeine Auswahl der maximalen Zelle ist ein weiterer Schritt.

### 2.1 Stärkerer Graphsatz

Sei Gamma ein zusammenhängender Graph auf N Trägern und

\[
H_\Gamma=\sum_{(i,j)\in E(\Gamma)}J_{ij}\frac{I+S_{ij}}2,
\quad J_{ij}>0.
\]

Dann gilt

\[
\boxed{\ker H_\Gamma=\Lambda^N\mathbb C^4.}
\]

**Beweis.** Nullenergie in einer Summe positiver Operatoren verlangt S_ij psi=-psi an jeder Kante. Die Kantentranspositionen eines zusammenhängenden Graphen erzeugen S_N. Damit transformiert psi unter der Vorzeichendarstellung aller Permutationen und ist total antisymmetrisch. Die Umkehrung ist direkt.

Für vier Träger haben daher ein vollständiger Graph, ein Pfad und ein Stern mit beliebigen positiven Kantengewichten denselben singulären Grundzustand. Ihr Anregungsspektrum ist nicht gleich. Der Prüfer bestätigt dies zusätzlich an einem Pfad mit Gewichten 1,2,3, dessen Gap ungefähr 0,467911 beträgt, statt 2 im gleichgewichteten vollständigen Graphen.

**Wichtige Folge für Skalierung:** Ein aus mehr als vier Trägern zusammenhängend aufgebautes System kann nicht alle diese Paarbedingungen gleichzeitig mit Nullenergie erfüllen. Ein skalierbares Netz verlangt endliche Energie für symmetrische Anteile, zusätzliche Sektoren oder eine geänderte Kompositionsregel. Ein absoluter Ausschluss sämtlicher symmetrischer Paaranteile wäre mit dem vorgeschlagenen verbundenen Zellennetz unvereinbar.

## 3. Korrektur der Vermittlungsroute und exakte bedingte Austauschform

### 3.1 Die Z4-Grade müssen stimmen

In einer konsistenten komplexen Schreibweise ist

\[
\mathfrak e_8=
\mathfrak g_0\oplus\mathfrak g_1\oplus\mathfrak g_2\oplus\mathfrak g_3,
\]

\[
\mathfrak g_0=(45,1)\oplus(1,15),\quad
\mathfrak g_1=(16,4),\quad
\mathfrak g_2=(10,6),\quad
\mathfrak g_3=(\overline{16},\overline4),
\]

bis zur Vertauschung der beiden konjugierten Spinorkonventionen. Es gilt

\[
[\mathfrak g_a,\mathfrak g_b]\subset\mathfrak g_{a+b\bmod4}.
\]

Daher führt derselbe Spinorgrad mit sich selbst nach (10,6), aber Grad 1 mit Grad 3 nach (45,1) plus (1,15). Schon 4 tensor bar(4)=1 plus 15 schließt eine 6 im gemischten Tensorprodukt aus.

Die Anschlussformel in Q2, Abschnitt 10, darf deshalb nicht mit einem gemischten 4/bar(4)-Paar zugleich eine 6 als Ziel behaupten. Falls eine Folge mehrerer virtueller Vertizes gemeint ist, müssen deren einzelne Typen angegeben werden.

Der unabhängige Wurzelcheck liefert 960 geordnete Wurzelpaare für Grad 1 plus Grad 1 nach Grad 2 und 832 für Grad 1 plus Grad 3 nach Grad 0; null gemischte Paare landen in Grad 2. Die letzteren 832 zählen nur Summen, die wieder Wurzeln sind. Opposite Wurzeln mit Cartan-Ziel kommen gesondert hinzu.

### 3.2 Ein vollständig lösbarer Vermittler

Unter zusätzlicher Annahme eines ausschließlich antisymmetrischen Vermittlers sei

\[
W:\mathbb C^4\otimes\mathbb C^4\to\mathbb C^6,
\quad W^\dagger W=P_-=(I-S)/2,
\quad WW^\dagger=I_6.
\]

Mit positiver Vermittlerenergie Delta und Kopplung g wird der mikroskopische Block

\[
H=\begin{pmatrix}
0&gW^\dagger\\
gW&\Delta I_6
\end{pmatrix}
\]

angesetzt. Die symmetrischen zehn Zustände haben Energie null. Jeder der sechs antisymmetrischen Zustände koppelt an genau einen Vermittlerzustand. Die unteren sechs Eigenwerte sind

\[
E_-=(\Delta-\sqrt{\Delta^2+4g^2})/2.
\]

Unter Identifikation des angekleideten unteren Raums mit dem ursprünglichen Paarraum folgt

\[
H_{\rm eff}=E_-P_-=E_-I+J_{\rm eff}P_+,
\]

\[
\boxed{J_{\rm eff}=\frac{\sqrt{\Delta^2+4g^2}-\Delta}{2}>0.}
\]

Für kleine g/Delta ergibt sich J_eff=g²/Delta-g⁴/Delta³+.... Dieser Mechanismus erklärt exakt, wie energetisch teure antisymmetrische virtuelle Zustände einen positiven Austauschterm erzeugen können. Er ist ein konkretes Modell der im Projekt gesuchten Vermittlung, kein Nachweis, dass die Quelle diesen Vermittler auswählt.

Bei zusätzlichen symmetrischen Vermittlern kann der relative Koeffizient schematisch kappa_minus-kappa_plus werden. Ohne Quelle für g, Delta, Bare-Energien und Vermittlertyp ist das Vorzeichen nicht allgemein erzwungen. Auch aus Lie-Strukturkonstanten allein folgt kein räumlicher Kopplungsgraph.

Der methodische Hintergrund ist die kontrollierte Elimination hochenergetischer Sektoren, etwa in Bravyi, DiVincenzo und Loss, arXiv:1105.0675. Der hier angezeigte Spezialfall ist direkt diagonalisiert und benötigt für seine Eigenwerte keine Störungsnäherung.

## 4. Exakte Reduktion zweier vollständiger Zellen

Q2, Tabelle 2 auf Seite 4, behandelt zwei vollständige Tetramergraphen und eine Brücke. Dafür kann die dortige Energiereihe geschlossen rekonstruiert werden.

Setze

\[
H_0=H_{\rm tet,A}+H_{\rm tet,B},\qquad
V=P^+_{ab}=(I+S_{ab})/2,
\qquad H=H_0+\lambda V.
\]

Für den Produktzustand |0>=Omega_A tensor Omega_B gilt

\[
\langle0|V|0\rangle=5/8.
\]

Für jeden traceless lokalen Operator A folgt aus der Antisymmetrie

\[
H_{\rm tet}A_i\Omega=2J A_i\Omega.
\]

**Beweis:** Nur die drei Kanten an i tragen bei. Sie ergeben (3A_i-sum_{j!=i}A_j)Omega/2. Wegen sum_j A_j Omega=Tr(A)Omega=0 ist das 2A_i Omega.

Die Swap-Identität im Viererträger lautet

\[
S_{ab}=\frac14\sum_{\mu=0}^{15}P_{\mu,a}P_{\mu,b}.
\]

Daher koppelt V den Produktgrundzustand nur an die normierte Kombination

\[
|1\rangle=\frac1{\sqrt{15}}\sum_{\mu=1}^{15}
(P_{\mu,a}\Omega_A)\otimes(P_{\mu,b}\Omega_B),
\]

die H0-Energie 4J hat. Beide Vektoren sind orthonormal. Weil V ein Projektor ist, ist ihr Spann unter V invariant. In dieser Basis gilt exakt

\[
\boxed{H\big|_{\operatorname{span}\{0,1\}}=
\begin{pmatrix}
5\lambda/8&\sqrt{15}\lambda/8\\
\sqrt{15}\lambda/8&4J+3\lambda/8
\end{pmatrix}.}
\]

Die untere Eigenenergie ist

\[
\boxed{E_-(\lambda)=2J+\frac\lambda2
-\frac12\sqrt{16J^2-2J\lambda+\lambda^2}.}
\]

| lambda/J | E_minus/J aus der geschlossenen Formel | Q2, Tabelle 2 |
|---:|---:|---:|
| 0 | 0 | 0 |
| 0,5 | 0,2974375810 | 0,2974 |
| 1 | 0,5635083269 | 0,5635 |
| 2 | 1 | 1,0000 |
| 3,2 | 1,3728942549 | 1,3729 |
| 6 | 1,8377223398 | 1,8377 |

Die Niedrigkopplungsentwicklung lautet

\[
E_-(\lambda)=\frac{5\lambda}{8}
-\frac{15\lambda^2}{256J}
+O(\lambda^3/J^2).
\]

Der zweite Term ist die virtuelle Energieabsenkung durch ein Paar adjungierter Anregungen bei Energie 4J. Damit erhält die bisherige Variationsschranke einen konkreten kontrollierten Korrekturterm.

**Reichweite:** Die Reduktion beweist einen exakten Eigenzweig, der bei lambda=0 aus Omega tensor Omega hervorgeht. Sie rekonstruiert die in Q2 berichteten Grundenergien. Sie beweist allein noch nicht, dass bei beliebig großem lambda kein anderer Symmetriesektor tiefer liegt. Der Prüfer kontrolliert die Invarianz im vollständigen Raum der Dimension 65.536, nicht nur durch Einsetzen der Tabellenwerte.

### 4.1 Was die Zellen in einem Netz tragen können

Ein einzelner eindeutiger Singulettgrundzustand besitzt keine interne logische Zustandsvielfalt. Auch der reine Produktgrundraum vieler isolierter Zellen ist eindimensional. Eine Projektion nur auf diese Grundräume erzeugt lediglich eine skalare effektive Energie.

Nichttriviale effektive Dynamik muss daher angeregte Multiplets, Randfreiheitsgrade, mehrere Vakuumsektoren oder andere aktive Zustände behalten. Die obige Rechnung identifiziert unmittelbar den adjungierten Anregungssektor als natürliche erste Erweiterung. Diese Aussage ist mit den wandernden Anregungen in Q2 vereinbar; sie verhindert nur, den eindimensionalen Grundzustand selbst mit einem dynamischen Vielzustandsträger zu verwechseln.

## 5. Uhrwerk: eine starke Obstruktion und zwei präzise Auswege

### 5.1 Die Paarenergietests laufen unter Htet nicht

Der vollständige gleichgewichtete Tetramer-Hamiltonoperator ist eine zentrale Summe aller Transpositionen. Daher

\[
[H_{\rm tet},S_{ij}]=0,
\qquad [H_{\rm tet},P^+_{ij}]=0.
\]

Jeder Paarenergietest bleibt unter der freien Htet-Dynamik konstant. Die Tabelle der relativen 3/12-Ticks in Q2 beschreibt aufeinanderfolgende Anwendungen eines gewählten Operators c, nicht automatisch die freie Zeitentwicklung unter Htet.

### 5.2 Ein vorhandenes relatives Uhrprotokoll lässt sich exakt ausrechnen

Wähle einen lokalen traceless hermiteschen Pauli A mit A²=I und präpariere

\[
|\psi(0)\rangle=e^{-i\pi A_1/4}\Omega
=\frac1{\sqrt2}(\Omega-iA_1\Omega).
\]

Wegen Htet A1 Omega=2J A1 Omega folgt

\[
|\psi(t)\rangle=
\frac1{\sqrt2}(\Omega-i e^{-2iJt/\hbar}A_1\Omega).
\]

Für die lokalen Auslesungen gilt

\[
\boxed{\langle A_1\rangle_t=-\sin(2Jt/\hbar),}
\]

\[
\boxed{\langle A_j\rangle_t=\tfrac13\sin(2Jt/\hbar),\quad j\ne1.}
\]

Die Relation <Omega|Ai Aj|Omega>=-1/3 für i!=j folgt aus den Paarmarginalien. Die lokalen Signale oszillieren gegeneinander; ihre Summe bleibt null. Die Periode ist pi hbar/J.

Das ist eine auslesbare Dynamik innerhalb des vorhandenen gesetzten Hamiltonmodells. Die lokale Präparation, die Wahl der beobachteten Pauli-Richtung und die physikalische Kalibrierung von J sind noch zusätzliche Daten. Der Befund löst nicht das Herkunftsproblem der Zeit.

### 5.3 Eine stärkere Form der symmetrischen PW-Obstruktion

Die bedingten Systemzustände der Aufspaltung ein Träger gegen drei liegen in Lambda³ C⁴, also in einer einzigen irreduziblen SU(4)-Darstellung bar(4). Jeder vollständig SU(4)-invariante System-Hamiltonoperator wirkt auf diesem Unterraum nach Schurs Lemma skalar.

Damit kann nicht nur die konkret untersuchte gleichgewichtete Swap-Summe dort keine vier Energien aufspalten. Keine vollständig SU(4)-invariante Hamiltonstruktur erzeugt auf genau diesem einzelnen irreduziblen Sektor vier verschiedene Energien. Mehr invariant gebaute Terme allein lösen das Problem nicht. Es braucht eine relative Referenzrichtung, zusätzliche Multiplizitäten oder eine andere Aufteilung.

### 5.4 Bedingte explizite Vierlesarten-Uhr

Eine Lösung mit sichtbarer Zusatzannahme ist

\[
h=\frac{\hbar\omega}{2}\operatorname{diag}(-3,-1,1,3),
\quad H_C=h_0,\quad H_S=h_1+h_2+h_3.
\]

Da jedes Basiswort von Omega jedes lokale Energielabel einmal enthält,

\[
(H_C+H_S)\Omega=0.
\]

Seien

\[
|t\rangle_C=\frac12\sum_{r=0}^3e^{-i\epsilon_rt/\hbar}|r\rangle_C,
\qquad |\psi(t)\rangle_S=2\,{}_C\langle t|\Omega\rangle.
\]

Dann

\[
|\psi(t)\rangle=e^{-iH_St/\hbar}|\psi(0)\rangle.
\]

Die vier Zeiten t_k=k pi/(2 omega), k=0,...,3, ergeben orthogonale Uhrenzustände und orthogonale bedingte Systemzustände. Die Konstruktion wird numerisch geprüft.

Dies ist eine echte stationäre globale Konstruktion mit nichttrivialer relationaler Dynamik. Sie verwendet jedoch den zusätzlich gewählten Generator h, eine Frequenzskala und eine Fourier-Auslesung. Sie ist kein Resultat einer source-only Auswahl. Verwandte endliche Uhren werden in Favalli und Smerzi, arXiv:2003.09042, behandelt; die hier verwendete Realisierung ist direkt auf Omega zugeschnitten.

## 6. Der unendliche Grenzprozess ist konstruierbar, der Zeitpfeil dadurch noch nicht ausgewählt

Für den beobachteten depolarisierenden Schatten

\[
\mathcal D(\rho)=\frac37\rho+\frac47\frac{I_4}{4}\operatorname{Tr}\rho
\]

gilt die konkrete Pauli-Realisierung

\[
\mathcal D(\rho)=\frac{13}{28}\rho
+\frac1{28}\sum_{a=1}^{15}P_a\rho P_a.
\]

Eine Isometrie ist

\[
V|\psi\rangle=
\sqrt{13/28}|0\rangle\otimes|\psi\rangle
+\frac1{\sqrt{28}}\sum_{a=1}^{15}|a\rangle\otimes P_a|\psi\rangle.
\]

Sie lässt sich zu einer unitären Operation mit einem 16-dimensionalen Hilfsregister erweitern. Für n frische, unabhängige Hilfsregister ergibt sich exakt D^n und damit der Kontrast (3/7)^n. Ein unendliches Registerband macht alle endlichen n gleichzeitig realisierbar. Mit einem beidseitigen Band und Verschiebung kann die globale Ausführung reversibel formuliert werden.

Dies ist ein Existenzbeweis für einen offenen beziehungsweise unendlichen Ausbau des **Schattenkanals**. Es ist keine Identifikation mit der kohärenten Originalausführung des Compilers. Es werden ein eingehender unkorrelierter Registerzustand, die Wechselwirkungsreihenfolge und die Unzugänglichkeit vergangener Register vorausgesetzt.

Der thermodynamische Pfeil folgt nicht aus der Unendlichkeit allein. Ein unendlich großes System kann ebenfalls stationär oder rekurrent in relevanten Observablen sein. Die spezielle Zustands- und Korrelationsstruktur der einlaufenden Umgebung bleibt eine Herkunftsfrage.

## 7. Der Übergang zum E8-Seam muss Operatorinhalt und Chiralität schließen

Q2 enthält ausdrücklich einen Modellwechsel: Die Zweizellenrechnung benutzt vollständige Vierergraphen. Die Vielzellen-WZW-Rechnung verwendet Vierersegmente mit nächster Nachbarschaft. Bei lambda=J ist erst dieses zweite Modell eine uniforme Kette. Gleiche isolierte Singuletts sind keine Garantie gleicher Anregungsspektren oder identischer Skalierungsgrenzen.

### 7.1 Die Zahl c=8 ist notwendig, aber nicht hinreichend

Für die chiralen Faktoren gilt bereits vor einer Kopplung c(D5,1)=5 und c(A3,1)=3. Das Produkt hat also schon c=8. Eine spätere Messung von c=8 weist allein keine dynamische E8-Erweiterung nach.

Die algebraische Verklebung kann präziser beschrieben werden. In den vier Z4-Sektoren sind die niedrigsten konformen Gewichte

| Sektor q | D5,1 | A3,1 | Summe |
|---:|---:|---:|---:|
| 0 | 0 | 0 | 0 |
| 1 | 5/8 | 3/8 | 1 |
| 2 | 1/2 | 1/2 | 1 |
| 3 | 5/8 | 3/8 | 1 |

Die passend verklebten drei nichttrivialen Sektoren können daher Gewicht-1-Ströme mit Dimensionen 64,60,64 liefern. Zusammen mit den ursprünglichen 45+15 Strömen ergeben sich 248. Dies stimmt mit der Z4-graduierten Lie-Algebra überein.

Eine tatsächliche Erweiterung verlangt aber lokale Vertexoperatoren, passende Cocycle-Phasen, Energie- und Adjungiertenkontrolle und geschlossene Operatorprodukte. Gerade diese Schritte gehören zur in Q1 formulierten T2-Aufgabe. Der lokale Quelleninhalt muss sie auswählen; die Gewichtstabelle allein beweist die Auswahl nicht.

### 7.2 Die Chiralitätslücke

Eine gewöhnliche uniforme SU(4)-Spinkette besitzt im kritischen Kontinuum linke und rechte Ströme. Der aus der endlichen Energieauswertung gewonnene Wert c=3 ist nicht automatisch ein isolierter rein chiraler Rand mit c_L-c_R=3. Ein chiraler E8-Seam verlangt entsprechend mehr als ein nichtchirales Produkt zweier kritischer Ketten.

Ein kontrolliertes Vorbild sind gekoppelte Ketten in einem zweidimensionalen Bulk: Gegenläufige innere Moden werden gepaart und gegappt, während chirale Randmoden übrigbleiben. Solche E8-Konstruktionen existieren als konkrete Modelle, etwa Lim, Mulligan und Teo, arXiv:2212.14559, sowie verwandte gekoppelte-Draht-Konstruktionen. Das beweist die mathematische und physikalische Möglichkeit einer solchen Architektur, nicht ihre Ableitung aus TFPT und erst recht nicht einen 3+1-dimensionalen Ursprung.

Für die weitere Arbeit müssen deshalb c_L, c_R, Operatorinhalt, Randbedingungen und die Herkunft des Bulks getrennt kontrolliert werden. Ein Ringfit mit c ungefähr 3 schließt diese Fragen nicht.

## 8. Die Clifford-Aussage darf nicht auf die ganze Erweiterung übertragen werden

Q1 formuliert die klassische Simulierbarkeit korrekt für Clifford-Prozesse mit Stabilizer-Präparationen und den genannten Messungen. Q0 dehnt diese Grenze zu weit auf den gesamten erweiterten Raum aus.

Der reine Tetramerzustand besitzt in der angegebenen Acht-Qubit-Kodierung

\[
\Omega=\frac1{\sqrt{24}}\sum_{\pi\in S_4}\operatorname{sgn}(\pi)
|\pi(0),\pi(1),\pi(2),\pi(3)\rangle.
\]

Er hat 24 nichtverschwindende Basisamplituden. Ein reiner Qubit-Stabilizerzustand hat in der Rechenbasis eine Trägermenge von Zweierpotenzgröße. Zusätzlich ergibt die unabhängige exakte Pauli-Prüfung nur 16 bis auf Vorzeichen stabilisierende Pauli-Wörter, statt der für einen reinen Acht-Qubit-Stabilizerzustand nötigen 256. Omega ist in dieser Kodierung kein Stabilizerzustand.

Auch kontinuierliche Austauschzeitentwicklung ist im Allgemeinen nicht auf eine endliche Clifford-Gruppe beschränkt. Deshalb ist eine pauschale Gottesman-Knill-Schranke für beliebig skalierte Tetramer-Präparation und Austausch nicht begründet. Die korrekte Referenzgrenze ist Aaronson und Gottesman, arXiv:quant-ph/0406196.

Daraus folgt weder Rechenuniversalität noch Shor-Fähigkeit, schnelle Faktorisierung oder eine Aussage über P versus NP. Dafür müssten skalierbare Präparation, erlaubte Gatter, Fehlertoleranz, Auslese und deren Kosten nachgewiesen werden. Die Katalog-IDs zu RH und Faktorisierung aus Q0 wurden in dieser Untersuchung nicht gegen die ursprünglichen Dossiers reproduziert.

## 9. Wie eine belastbare Gesamtrekonstruktion aussehen sollte

Die beiden Richtungen sind nicht einfach zwei Schreibweisen derselben Inversion:

- Vorwärts: Ein vollständiger Prozess erzeugt bestimmte TFPT-Auslesungen.
- Rückwärts: Gegebene Auslesungen bestimmen im Allgemeinen nur eine Klasse möglicher Prozesse.

Ein sinnvoller Rekonstruktionsbegriff lautet

\[
X\sim Y\iff
\Pr(o\mid X,\mathcal I)=\Pr(o\mid Y,\mathcal I)
\quad\text{für alle erlaubten zukünftigen Eingriffsfolgen }\mathcal I.
\]

Der minimale operative Zustand ist die Klasse [X], nicht eine vorab gewünschte Koordinatenzahl. Wird das Eingriffsrepertoire um kohärente Registerrückkopplung erweitert, kann eine zuvor ausreichende Klasse zerfallen und mehr Information notwendig werden.

Der passende mathematische Anschluss sind Mehrzeit-Prozesse beziehungsweise Prozesstensoren, wie bei Pollock und Mitarbeitern, arXiv:1512.00589 und arXiv:1801.09811. Diese Theorie hilft, verschiedene experimentelle Ausführungen korrekt zu unterscheiden. Sie liefert selbst keine TFPT-Quelle und wählt weder P1/P2 noch ein kosmisches Anfangsdatum aus.

Ein konkreter größerer Kandidat müsste mindestens gemeinsam bestimmen:

\[
\mathcal U=(\text{lokale Observablen},\text{zulässige Zusammensetzung},
\text{Zustand},\text{Dynamik},\text{Auslesung}).
\]

Die fünf Einträge sind keine fünf gelösten Einzelgleichungen. Die eigentliche Aufgabe ist, dass dieselbe primitive Quelle ihre Beziehungen auswählt. Ein willkürlich gewählter Graph mit frei eingesetzten Kopplungen, einem separat präparierten Vakuum und nachträglich angepasster Auslesung wäre nur eine neue Modellfamilie.

Eine Lorentz-Kegel-Identität in hermiteschen 2 mal 2 Matrizen liefert dabei noch keine räumliche Dimension, lokale Felder oder universelle Gravitation. Ebenso ist die Rekonstruktion H→psi→H in einer zuvor eingeschränkten Operatorfamilie kein unabhängiger Beweis für die Auswahl dieser Familie. Q1 und Q2 markieren diese Grenzen bereits ausdrücklich.

## 10. Das nächstliegende gemeinsame Arbeitsprogramm

| Priorität | Rechnung | Vorab festgelegtes Erfolgskriterium |
|---:|---|---|
| 1 | Prozessklassen und Quellenvertrag einfrieren | Die 30-dimensionale feste Ausführung, allgemeinere CQ-Eingaben und kohärente Mehrzeitprozesse werden getrennt; kein Minimalitätssatz wechselt still die Eingriffsklasse. |
| 2 | Vermittler aus tatsächlichen Quelloperatoren bauen | Z4-Typen stimmen; g, Delta, Matrixelemente und Graph werden aus Quellenobjekten abgeleitet oder als verbleibende freie Eingaben ausgewiesen. |
| 3 | Ein unverändertes Vielzellenmodell untersuchen | Der gewählte Graph wird nicht zwischen Rechnungen ausgetauscht; adjungierte Anregungen, Transport und Gap werden mit kontrollierter Größenskalierung berechnet. |
| 4 | E8-Operatorerweiterung und Chiralität testen | Nicht nur c=8, sondern Gewicht-1-Felder, Cocycle-Transport, Operatorprodukte und linke/rechte Sektoren sind kontrolliert. |
| 5 | Eine unabhängige physikalische Auslesung ableiten | Zustandswahl, Einheitenschnittstelle und Transfer sind vor Vergleich mit dem Zielwert festgelegt. |

Die Kopplungsrechnung hat weiterhin den größten Hebel. Jetzt besitzt sie jedoch einen korrigierten Typvertrag, eine explizite bedingte mikroskopische Realisierung und eine geschlossene Zweizellenkontrolle. Das ist deutlich konkreter als die bloße Aufforderung, irgendwann einen Superaustausch auszurechnen.

## 11. Gesamturteil

Die tragfähige Fortsetzung ist ein phasentreuer, zusammensetzbarer Prozess mit sorgfältig abgegrenzten Auslesungen. Der Compiler beschreibt einen echten Teil seiner Struktur, aber ein vollständiger physikalischer Ursprung ist durch die bisherigen Schatten nicht eindeutig rekonstruiert.

Der positive Zuwachs dieser Runde besteht aus exakt prüfbaren Schritten: 30-dimensionaler fester Prozessquotient, stärkere graphabhängige Hüllenaussage, korrigierte E8-Vermittlungstypen, genaue Austauschform unter angegebenen Annahmen, analytische Zweizellenreduktion und funktionsfähige relative Uhrprotokolle. Die zentrale verbleibende Beweispflicht ist die gemeinsame Auswahl dieser Ausführung aus der Quelle, einschließlich der räumlichen und physikalischen Grenzbeschreibung.

## Reproduktion

```sh
python -m pip install numpy sympy
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python pruefer.py --output pruefergebnisse.json
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -OO pruefer.py --output pruefergebnisse_optimiert.json
cmp pruefergebnisse.json pruefergebnisse_optimiert.json
```

Die Resultate gelten für die im Bericht explizit angegebenen Modelle. Der Prüfer führt keine ursprünglichen TFPT-Verifikationsdateien aus, ändert keine Ledger und benutzt keine numerischen Messdaten als Anpassungsparameter.
