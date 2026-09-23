# Eine korrigierte Ausführung: Aufzeichnung, Präparation und Mehrzeitantwort

14. September 2026 · NON-RH · endliche Konstruktion mit zusätzlichen
Operationen, keine T1–T8-Promotion. Dieser Bericht entstand **nach** dem Export
des konsolidierten Gesamtpapers v1.2. Er ist die anschließende Rechnung.

## Ergebnis

Dieselbe korrigierte Vermittlungsoperation erzeugt jetzt ein kohärentes
Austauschregister, ein kontrolliertes Präparationsfilter und unterscheidbare
Mehrzeitverläufe. Eingänge, Pauli-Tick und dreizyklische Uhr sind mit den
tatsächlichen Quelloperationen verbunden. Ein schon präpariertes Ω, ein neuer
Hamiltonoperator oder kontinuierliche Teil-Swap-Pulse werden nicht benötigt.

Der dabei präzisierte Herkunftsengpass ist wichtig: Das Austauschregister ist
mit der bislang identifizierten reinen Clifford-/Stabilizer-Operationsklasse
nicht ausführbar. Vermittlung und kohärenter Belegungszugriff bleiben zusätzliche
Ressourcen. Die gemeinsame **bedingte Konstruktion** ist damit weiter als drei
isolierte Modelle, aber noch keine vollständig native TFPT-Ausführung.

## 1. Eingefrorener Quellen- und Ressourcenvertrag

Quelle: unveränderter Präfix P0/P1 von verification/v783_two_qubit_clifford.py,
über compiler-origin-audit-20260913/context_instrument.py.

- Alle vier Eingangsprojektoren |a><a| und der uniforme Projektor gehören
  zu den tatsächlichen 60 Quellprojektoren.
- Z⊗I und die Uhr C: 0→1→2→0, 3→3 erhalten die tatsächlichen 240
  phasenmarkierten Quellwurzeln. C normalisiert alle Quell-Paulis.
- Der Austausch S erfüllt mit denselben 16 Quell-Paulis S=(1/4)ΣP⊗P.
- Eine Rechenkontext-Messung mit ausgangsabhängiger Pauli-Bitverschiebung
  realisiert einen vollständigen Reset auf jeden gewählten Zustand |a>.

Zusätzlich festgelegt sind vier gekoppelte Quellträger, kanonische Wedge-Kopplung,
ihre unitäre Fortsetzung U0, kohärentes Kopieren der Vermittlerbelegung,
Registerinitialisierung/-messung, Kantenadressierung, Versuchsreihenfolge und
Feedback nach Fehlschlägen. Die Quantenmessregel ist Operationsvoraussetzung,
nicht aus dem Compiler bewiesen. Quellseitige Matrixfaktoren allein leiten
diese Zusammensetzung nicht her.

## 2. Ein vollständiges Aufzeichnungsinstrument aus U0

Setze P±=(I±S)/2 und W=K/√2 mit K|ab>=|a∧b>,
K|ba>=-|a∧b>, K|aa>=0. Dann

\[
W^\dagger W=P_-,\quad WW^\dagger=I_6,\quad WP_+=0.
\]

Auf (C⁴⊗C⁴)⊕C⁶ wähle die selbstadjungierte Involution

\[
U_0=\begin{pmatrix}P_+&W^\dagger\\W&0\end{pmatrix},\qquad U_0^2=I_{22}.
\]

Dies setzt voraus, dass der Nicht-Ereigniszweig unverändert bleibt. Seine
physikalische Eindeutigkeit wird durch das folgende Experiment nicht bewiesen.

Q kopiert nur die Vermittlerbelegung in ein binäres Register, kein geordnetes
Farbwort. Die vollständige Makrooperation auf allen 44 Dimensionen ist

\[
Q=I_{16}\otimes I_2\oplus I_6\otimes X,\qquad
(U_0\otimes I)Q(U_0\otimes I)
=\bigl(P_+\otimes I+P_-\otimes X\bigr)\oplus I_{12}.
\]

Der Vermittler kehrt vollständig zurück, ohne die Farbinterferenz zu zerstören.
Auf dem Materieraum bleibt R=P+⊗I+P-⊗X mit R²=I. Insbesondere

\[
R(\psi\otimes|0\rangle)
=P_+\psi\otimes|0\rangle+P_-\psi\otimes|1\rangle.
\]

Die beiden Krausoperatoren sind P+ und P-. Ihre Effekte summieren sich zu I.
Das behandelt alle Eingänge und beide Ausgänge, nicht nur den Erfolgszweig.
Ein ungemessenes Register bleibt kohärent.

## 3. Ein gemeinsamer Träger statt wechselnder Modelle

Die vier Materieträger bilden Hmat=(C⁴)^⊗4, Dimension 256. Für das
sequenzielle Protokoll wird ein gemeinsamer Raum gewählt:

\[
\mathcal H_{\rm common}=\mathcal H_{\rm mat}\oplus
\bigoplus_{e=1}^{6}(\mathbb C^6_e\otimes\mathbb C^4\otimes\mathbb C^4),
\qquad \dim\mathcal H_{\rm common}=832.
\]

Es ist höchstens ein Vermittler aktiv. Ue wirkt auf Materie plus dem
zugehörigen 96-dimensionalen Vermittlersektor und auf den anderen
Vermittlersektoren als Identität. Der Prüfer rekonstruiert alle sechs We
auf dem vollen Materieraum: We†We=P-e, WeWe†=I96 und WeP+e=0.
Die verschiedenen Vermittler-Ausgangsräume sind orthogonal. Jede vollständige
Record-Makrooperation kehrt in denselben Materiesektor zurück, auch mit
verschränkten Zuschauerzuständen.

Dies ist eine vollständige **gewählte Protokollrealisierung**, kein allgemeines
Fockmodell mit beliebig vielen gleichzeitig erregten Vermittlern.

Mit der tatsächlichen Quell-Uhr C und e(0)=01, e(1)=02, e(2)=03,
R_e(3)=I lässt sich eine feste Schrittregel schreiben:

\[
\mathbb U=(C\otimes I)\sum_{k=0}^3|k\rangle\langle k|\otimes R_{e(k)}.
\]

Unitarität folgt aus den orthogonalen Steuerblöcken. Bei Uhrstart 0 durchläuft
sie den Stern und kehrt nach drei Schritten zu 0 zurück. Mit Träger,
vierdimensionaler Uhr und binärem Record hat sie 6656 Dimensionen.
Die Uhr→Kanten-Zuordnung und der Registerzugriff bleiben gesetzt.
Eine physikalische Zeiteinheit oder autonome kosmologische Uhr folgt nicht.

## 4. Präparation ohne vorausgesetztes Ω

Starte mit dem einfachen Quellprodukt v0=|0,1,2,3>. Akzeptiere in jeder
Sternrunde nur Recordfolge 111. Alle acht ersten Recordfolgen haben
Wahrscheinlichkeit 1/8. Für N erfolgreiche Runden gilt

\[
v_N=K_\star^Nv_0,\qquad K_\star=P^-_{03}P^-_{02}P^-_{01},\qquad p_N=\|v_N\|^2.
\]

Ω=(1/√24)Σπ∈S4 sgn(π)|π(0),π(1),π(2),π(3)> wird nur zur
nachträglichen Zielprüfung definiert, nicht als Eingabe verwendet.

### Allgemeiner Konvergenzbeweis

Die 24 verschiedenen Farbanordnungen tragen die reguläre S4-Darstellung.
Dort hat G=Kstar†Kstar exakt das charakteristische Polynom

\[
\det(xI-G)=
\frac{x^{12}(x-1)(16x-1)^5(16x^2-9x+1)^3}{2^{32}}.
\]

Spektrum: 1 [einfach], 1/16 [fünffach], (9±√17)/32 [je dreifach],
0 [zwölffach]. Der einzige Eigenvektor zu 1 ist der Signaturvektor von Ω.
Die reguläre Darstellung der Gruppenalgebra ist treu; die daraus gewonnenen
polynomialen Operatoridentitäten gelten deshalb auch in jeder unitären
S4-Darstellung. Auf dem vollen 256-dimensionalen Materieraum ist der
Eigenprojektor zu 1 der Antisymmetrisierer PΩ. Die Multiplizitäten der übrigen
Eigenwerte werden bei diesem Übergang nicht unverändert übernommen.

Kstar und sein Adjungiertes fixieren PΩ. Mit β=(9+√17)/32<5/12 folgt
für jedes N, nicht nur für Stichproben:

\[
\|K_\star^N-P_\Omega\|^2\le\beta^N,\quad
\frac1{24}\le p_N\le\frac1{24}+\frac{23}{24}\beta^N,\quad
F_N=\frac1{24p_N}\ge\frac1{1+23\beta^N}.
\]

| N | Erfolgswahrscheinlichkeit pN | Bedingte Zielfidelität FN |
|---|---|---|
| 1 | 1/8 | 1/3 |
| 2 | 51/1024 | 128/153 |
| 4 | 175341/4194304 | 524288/526023 ≈ 0,9967016651 |
| 8 | 2932033221441/70368744177664 | 8796093022208/8796099664323 ≈ 0,9999992449 |
| N→∞ | 1/24 | 1 |

Bei endlichem N ist dies kontrollierte Näherungspräparation, keine exakte
Ω-Präparation. Die rationale Schranke mit (5/12)^20 garantiert Infidelität
<10^-6 bei N=20; der explizite Eingang erreicht dies schon bei N=8.
Eine größenuniforme Konvergenz für beliebig große Zellnetze folgt nicht.

### Fehlschläge und Neustart gehören dazu

Für eine lokale Rechenkontext-Messung mit Ausgang x realisiert der
Quell-Pauli X_(a xor x) den Reset:

\[
M_x=X_{a\oplus x}|x\rangle\langle x|=|a\rangle\langle x|,
\quad \sum_x M_x^\dagger M_x=I,\quad
\sum_xM_x\rho M_x^\dagger=|a\rangle\langle a|\operatorname{Tr}\rho.
\]

Vier lokale Resets erzeugen v0 sogar aus einer verschränkten Eingabe.
Ein Fehlschlag kann daher einen neuen Versuch auslösen, ohne Ω-Reservoir.
Weil pN≥1/24, benötigt man höchstens 24 Versuche im Mittel. Die
Restfehlerwahrscheinlichkeit nach m Versuchen ist höchstens (23/24)^m,
bei m=500 unter 10^-9. Beendigung ist fast sicher, nicht in einer festen
Worst-Case-Zahl garantiert.

Damit liegt ein vollständiges **kontrolliertes probabilistisches**
Präparationsverfahren innerhalb des Ressourcenvertrags vor. Es benötigt
Messung, Feedback, Reset und Register; es ist kein autonomer Attraktor.

Die ältere Zahl 1/6 bleibt konsistent: Vorgelagerte P--Tests auf 01 und 23
erzeugen mit Wahrscheinlichkeit 1/4 den Zweisingulettzustand. Bedingt darauf
beträgt das Ω-Gewicht 1/6. Die Gesamtausbeute bleibt (1/4)(1/6)=1/24.

## 5. Mehrzeitantwort mit genau derselben Präparation und Ausführung

Nach erfolgreicher Präparation: tatsächlicher lokaler Quelltick A auf Träger 0,
zweimal R01, danach A† und dasselbe N-Runden-Filter als Schlussprüfung.
Die Schlussprüfung wird nicht durch eine kostenlose ideale Ω-Messung ersetzt.

Protokoll R verwendet zweimal dasselbe erhaltene Register. R01²=I macht
die Aufzeichnung rückgängig. Protokoll F verwendet beim zweiten Schritt
ein frisches Register und ignoriert beide Records am Ende. Dann bleiben
Geschichten 00 und 11, deren **Dichten**, nicht Amplituden, addiert werden.

Mit B±=A†P±01A lauten die unbedingten gemeinsamen Erfolgswahrscheinlichkeiten

\[
j_N^R=\|K_\star^{2N}v_0\|^2,\qquad
j_N^F=\sum_{\sigma=\pm}\|K_\star^NB_\sigma K_\star^Nv_0\|^2.
\]

Division durch pN gibt die Schluss-Erfolgswahrscheinlichkeit bedingt auf
die erste erfolgreiche Präparation. Alle übrigen Ausgänge bleiben Fehlschläge.

Die tatsächliche dreizyklische Quell-Uhr C hat Spur 1. Ihre ideale
Recordverteilung ist (5/8,3/8), daher sind die bedingten Grenzwerte
1 und (5/8)²+(3/8)²=17/32. Die unbedingten Grenzwerte sind
1/24 und 17/768.

| N | Rückkehr, erhaltenes Register | Rückkehr, frisches Register |
|---|---|---|
| 1 | 0,3984375 | 0,25 |
| 2 | 0,8393698300 | 0,4434886259 |
| 4 | 0,9967024178 | 0,5274997175 |
| 8 | 0,9999992449 | 0,5312581678 |
| 12 | 0,9999999998 | 0,5312504084 |
| N→∞ | 1 | 17/32 = 0,53125 |

Die endlichen Werte wurden als exakte Brüche berechnet. Die lokale C-Uhr
verlässt den 24-dimensionalen Präparationssektor und erzeugt wiederholte
Farben. Deshalb wurde dieser Versuch auf dem **vollen 256-dimensionalen
Raum** gerechnet. Solche Komponenten wurden nicht herausprojiziert.

Ein zweites deklariertermaßen anderes Quellen-Setting A=Z⊗I hat Spur 0
und liefert die Grenzwerte 1 und 5/9. Das ist kein Widerspruch:
gleiches Instrument, anderer zulässiger Tick. Allgemein gilt
p+=(16-|Tr A|²)/24 und ideale frische Rückkehr p+²+(1-p+)².
Das frühere 17/32 wird hier also im Grenzfall neu aus einem gemeinsamen
Protokoll gewonnen, nicht als Ergebnis jedes endlichen Versuchs übernommen.

## 6. Die enger gefasste native Lücke

### Das Austauschregister ist eine echte zusätzliche Ressource

Auf vier Materiequbits und einem Recordqubit gilt

\[
R(I_{16}\otimes Z)R^\dagger=S\otimes Z.
\]

S ist kein vierqubitiger Pauli: Tr S=4, während ein Pauli spurlos
oder ±I mit Spur ±16 ist. R ist in dieser Kodierung somit nicht Clifford.
Der vollständig quellseitige Eingang |0>⊗(1/2)Σ_b|b>⊗|0> hat nach
R sogar exakt **13** nichtverschwindende Rechenbasisamplituden. Er ist
kein reiner Stabilizerzustand, dessen Trägergröße eine Zweierpotenz ist.

Eine exakte Realisierung mit ausschließlich Cliffordoperationen,
Stabilizer-Hilfszuständen und Pauli-Messungen ist damit ausgeschlossen,
auch mit klassischem Feedback. Eine nichtstabilisierende Kodierung,
Belegungsmessung, Kopplung oder Hilfspräparation wäre eine zusätzliche
Ressource. Der Ausschluss betrifft diese Operationsklasse, nicht jede
denkbare TFPT-Erweiterung. Zur Klasse siehe
[Aaronson–Gottesman](https://arxiv.org/abs/quant-ph/0406196).

### Die zentrale Clockphase ist kein relativer Vermittlerpuls

iI4 wirkt auf zwei Eingängen als -I16 und auf Λ²C⁴ als -I6.
Auf beiden Ladung-zwei-Alternativen ist das dieselbe skalare Phase.
Die für einen Echo-Swap nützliche Operation D=I16⊕(-I6) unterscheidet
dagegen die Belegung: U0 D U0=S⊕I6.
D ist daher kein Umbenennen der zentralen Gradierung; Q muss ebenso
als eigener Zugriff begründet werden.

### Unbeobachteter Austausch ist keine Kühlung

Alle P±e kommutieren mit PΩ. Der ungelesene Kanal
ρ↦P+eρP+e+P-eρP-e erhält Tr(PΩρ) und kann das Zielgewicht nicht erhöhen.
Der Fixraum des zyklischen ungelesenen Sternkanals ist die Kommutante
der S4-Wirkung: Jeder Dephasierungsschritt ist eine orthogonale
Hilbert–Schmidt-Projektion. Ein Fixpunkt des Zyklus kann bei keinem
Schritt Norm verlieren und muss deshalb jeden Schritt einzeln erfüllen.

Die Dimension ergibt sich exakt als Spur des Gruppenmittel-Projektors,
mit c(π) als Anzahl der Permutationszyklen:

\[
\dim\mathrm{Fix}=\frac1{24}\sum_{\pi\in S_4}4^{2c(\pi)}=3876.
\]

Die tracelose Dimension 3875 ist keine konstruierte Identifikation
mit einer gleichnamigen E8-Darstellung. Der kontrollierte Reset
umgeht die Gewichtserhaltung durch eine deklarierte Mess-/Feedbackoperation;
er widerlegt sie nicht und liefert keinen intrinsischen kosmologischen Zustand.

## 7. Geschlossene Teilfrage und nächste entscheidende Tests

Geschlossen im gewählten endlichen Modell: gemeinsame Recordkonstruktion,
alle lokalen Zweige, gemeinsamer Träger, kontrollierte Präparation auf
beliebige gewünschte Genauigkeit, Neustart-/Fehlerschranken und Mehrzeitantwort.
Nicht geschlossen: native Herleitung der nicht-Cliffordschen Kopplung,
U0-Auswahl, globale Verklebung, physikalischer Zustand, Skala, chirales Maß
und Gravitation. Alle T1–T8-Abschlüsse bleiben offen.

1. In phasenmarkierten Klammer-/Half-Charge-Operationen einen tatsächlichen
   nicht-Cliffordschen Adapter suchen. Er muss W, W†, ker W und Belegung
   gemeinsam, mit der nötigen Norm-/Energiekontrolle, realisieren.
   Eine bilineare Pauli-Summe oder ein Klammerkoeffizient allein genügt nicht.
2. Den 13-Amplituden-Quellinput, beide Record-Krausoperatoren und die
   acht-Runden-Echowerte als feste Abnahmetests verwenden. Auch Fehlschläge
   und Hilfszustandskosten müssen aus derselben Realisierung stammen.
3. Messung/Feedback/Reset entweder offen als operationalen Zusatz belassen
   oder aus einer Umgebung samt Energie-, Entropie- und Zustandshaushalt
   herleiten. Ein dunkler Vektor genügt nach dem Fixraumbeweis nicht.
4. Erst danach eine erklärte skalierende Zellfamilie prüfen. Der
   832-dimensionale Laborträger ist kein gemeinsamer 3+1D-Ursprung,
   kein vollständiges chirales Maß und kein dynamischer Spin-2-Sektor.

## 8. Reproduktion

231 eigene exakte Prüfbedingungen; zusätzlich 1073 Quell-Präfixprüfungen.
Normal und -OO liefern bytegleiche Berichte. Fünf in-memory-Mutanten
scheitern an den vorgesehenen Prüfstufen. Diese Zahlen zählen keine
unabhängigen physikalischen Entdeckungen. Kein voller RH-/Lean-Neubau.

Aus dem Repo:

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 /opt/homebrew/bin/python3 experiments/theory-contracts/compiler-single-execution-20260914/run_checks.py

[Prüfbericht](/Users/stefanhamann/Projekte/tfpt-theoryv4/experiments/theory-contracts/compiler-single-execution-20260914/verification.json) · [Replay und Quellhash](/Users/stefanhamann/Projekte/tfpt-theoryv4/experiments/theory-contracts/compiler-single-execution-20260914/replay.json).
Alle tragenden Rechnungen sind rational/algebraisch; Dezimalwerte sind
Darstellungen exakter Brüche. Die allgemeine Konvergenz folgt aus dem
oben ausgeführten Spektralbeweis, nicht aus den endlich vielen Beispielen.

Die vorgelagerte PDF-Konsolidierung liegt im Paket
compiler-paper-v1_2-20260914 und enthält den davor abgeschlossenen
Sechs-Quellen-Audit. Diese anschließende Konstruktion ist ein eigener
datierter Forschungsbefund.
