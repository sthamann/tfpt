# Audit: tatsächliche Quellen-Zeitantwort und erster freier Selektor

Stand: 21. September 2026  
Verdict: **PARTIAL, aber konstruktiv vollständig für den bezeichneten Quellenblock**

## Entscheidung

Die neue Forderung „Bestimme die vollständige Zeitantwort der tatsächlich erzeugten Felder“ ist **bereits erfüllt**, sofern die zusätzliche, schon vorhandene Randquelle als Voraussetzung akzeptiert wird:

- zehnkanaliger Rand `Gamma = I_(9,1)`,
- `F(E8)`-Einbettung mit zusätzlichem rechten/linken Paar,
- ausgewählte positive Randphase `V_aux`,
- Gittervakuum, Kokzyklus und Konformalzeit `H_0=L_0`,
- vorhandene 64 ungeraden Felder `Psi_i` und 60 vorhandenen Mediatorfelder `Phi_A`,
- für die unten ausgeschriebene symmetrische `1/4`-Mischungsmatrix das zusätzliche Acquisition-/Labelmetrik-Protokoll, in dem Paar- und Mediatorlabel vor dem gemeinsamen Gram-Whitening jeweils einzeln auf Norm eins gesetzt werden.

Kein neuer Oszillator, kein neues Bad und kein Wunsch-Hamiltonian `H_+` werden dafür benötigt. Die Antwort der Quelle ist nicht der native volle CAR/CCR-Hamiltonian. Sie ist eine exakt bestimmte bilokale Paar-/Mediatorantwort derselben vorhandenen Randfelder.

Der früheste noch freie Selektor liegt **vor** dieser Antwort: P1/P2 wählen weder den zehnkanaligen Rand noch seine physische Energie-/Vakuumphase. Innerhalb des zehnkanaligen Kandidaten wird der Nullvektor `n` nur nach zusätzlich erklärter Blocksymmetrie und orientiertem Glue eindeutig; anschließend bleibt die positive Energiematrix beziehungsweise der Boostparameter `eta` eine kontinuierliche Wahl. `V_aux` ist kompatibel und elegant, aber nicht aus P1/P2 erzwungen. Auch die relative Acquisition-Normierung von Paar- und Mediatorlabel ist eine Präparations-/Metrikannahme und kein quelleninvariantes Wechselwirkungsdatum.

## 1. Was die vorhandene Quelle exakt liefert

Setze

```text
A = W^dagger W,     A^2=8A,     rank(A)=60,
P_b=A/8,            P_d=I-P_b.
```

Für die wirklichen antisymmetrisierten bilokalen Feldzustände `J_r` gilt für `v=rs` exakt

```text
J_r^dagger J_s = G(v) = d(v) I + o(v) A,
d(v) = v^2(2-v) / [2(1-v)^3],
o(v) = (2-v) / [2(1-v)^2].
```

Die vollständigen hellen und dunklen Eigenantworten lauten

```text
g_b(v)=d(v)+8o(v)
      =(2-v)(v^2-8v+8)/[2(1-v)^3],
g_d(v)=d(v).
```

Mit `rho=r^2`, der polar normierten Isometrie `U_r=J_r G(rho)^(-1/2)` und der bereits vorhandenen Konformalzeit ist die gesamte euklidische Antwort

```text
T_r(tau)=U_r^dagger exp(-tau H_0) U_r
        =exp(-3tau) G(rho exp(-tau)) G(rho)^(-1).
```

Damit explizit

```text
T_d(tau)=exp(-5tau)
         * (2-rho exp(-tau))/(2-rho)
         * (1-rho)^3/(1-rho exp(-tau))^3,

T_b(tau)=exp(-3tau)
         * (2-rho exp(-tau))[(rho exp(-tau))^2-8rho exp(-tau)+8]
           /[(2-rho)(rho^2-8rho+8)]
         * (1-rho)^3/(1-rho exp(-tau))^3.
```

Für Realzeit setzt man `tau=it`; die Reihe konvergiert für `0<rho<1` absolut. Der vorhandene Viertelladungsterm multipliziert den jeweiligen Impulsfaserblock mit `exp(tau Q_2/4)` beziehungsweise `exp(it Q_2/4)`.

Die Spektralmaße sind ebenfalls vollständig. Die Energien sind `3+n`. Ihre unnormierten Gewichte sind

```text
hell:  w_0=8,
       w_n=(n+2)(n+15) rho^n/4,  n>=1;

dunkel: w_0=w_1=0,
        w_n=(n-1)(n+2) rho^n/4, n>=2.
```

Deshalb besitzt die endliche Separation unendlich viele positive Pole. Der erste Moment

```text
M_r=3I+rho G'(rho)G(rho)^(-1)
```

ist nicht die volle Zeitantwort; die positive zweite Varianz

```text
T_r''(0)-T_r'(0)^2
=U_r^dagger H_0(1-U_rU_r^dagger)H_0U_r >0
```

misst genau die Rückwirkung des ausgelassenen Quellenraums.

## 2. Gemeinsame Polarrekonstruktion mit den vorhandenen Mediatoren

Die 60 `Phi_A` sind keine hinzugefügten Moden. Sie sind die bereits vorhandenen Gewicht-3-Mediatorfelder der gleichen Randquelle. Sei `M` ihre normierte Einbettung. Im hellen Kanal gilt

```text
c_rho = <M,U_r> = sqrt(8/g_b(rho)),
Gamma_b(rho) = [[1,c_rho],[c_rho,1]].
```

Für jedes `0<rho<1` ist `g_b(rho)>8`, also `0<c_rho<1` und

```text
det Gamma_b = 1-c_rho^2 > 0.
```

Damit ist die gemeinsame Abbildung `(U_r,M)` auf allen

```text
1956 dunklen Paarzuständen
+ 60 hellen Paarzuständen
+ 60 Mediatorzuständen
= 2076 Richtungen
```

injektiv. Der alte Gram-Rangverlust betrifft nur das unskalierte Zusammenziehen am selben Punkt.

Die vollständige helle Zwei-Zeit-Matrix ist bereits durch die Paarantwort bestimmt:

```text
K_b(rho,tau)=
  [[T_b(tau),              c_rho exp(-3tau)],
   [c_rho exp(-3tau),      exp(-3tau)]].

R_b(rho,tau)=Gamma_b(rho)^(-1/2)
             K_b(rho,tau)
             Gamma_b(rho)^(-1/2).
```

Dies ist die gemeinsame polar normalisierte All-Time-Antwort. Zusammen mit `T_d(tau)` ist der gesamte 2076-dimensionale Paar-/Mediatorblock bestimmt.

Im kontrollierten Kollisionsgrenzwert `rho -> 0` bleibt nach Gram-Whitening ein echter zweidimensionaler heller Raum. Seine beiden Quellenrichtungen sind die Gewicht-3-Richtung und die aus dem ersten bilokalen Jet erhaltene Gewicht-4-Richtung. Für das Protokoll, in dem `U_r` und `M` vor dem Whitening jeweils einzeln auf Norm eins gesetzt werden, gilt in der symmetrischen polarisierten Basis

```text
H_b,0 = [[7/2,-1/2],[-1/2,7/2]],
spec(H_b,0)={3,4},

R_b(0,tau)=exp(-tau H_b,0)
 =1/2 [[exp(-3tau)+exp(-4tau), exp(-3tau)-exp(-4tau)],
       [exp(-3tau)-exp(-4tau), exp(-3tau)+exp(-4tau)]].
```

Die 1956 dunklen Richtungen haben Energie 5. Mit Viertelladung lautet der gemeinsame Grenzgenerator blockweise

```text
hell:  H_b,0 - Q_2/4,
dunkel: 5I - Q_2/4.
```

Die Abhängigkeit von der Acquisition-/Labelmetrik lässt sich vollständig kontrollieren. Für

```text
S_lambda=(lambda U_r,M),  lambda>0,
```

liefert das jeweilige Gram-Whitening im Kollisionsgrenzwert

```text
H_lambda=4I-v_lambda v_lambda^dagger,
v_lambda=(lambda,1)/sqrt(1+lambda^2),
spec(H_lambda)={3,4}.
```

Damit bleiben der rekonstruierte zweidimensionale Quellenraum und sein Spektrum invariant. Die maximale Austauschwahrscheinlichkeit in der bezeichneten Labelbasis ist dagegen

```text
p_swap,max(lambda)=4lambda^2/(1+lambda^2)^2.
```

Sie ist nur bei `lambda=1` gleich eins. Die konkrete `1/4`-Mischungsmatrix ist daher eine Aussage über das einzeln unit-normierte Acquisition-Protokoll, nicht über eine quelleninvariante Wechselwirkungsstärke.

## 3. Warum dies den Positivitätskonflikt löst, ohne `H_+` vorauszusetzen

Die beiden Einzelfeldenergien addieren sich im hellen Kanal zu 3. Als **sektorinterne verbundene Energiebuchhaltung** relativ zu diesem festgehaltenen Einteilchen-Baseline ergibt sich im einzeln unit-normierten Labelprotokoll

```text
H_b,0-3I = 1/2(I-sigma_x).
```

Nach einer bloßen Phasenumkehr eines der beiden Basisvektoren wird daraus

```text
1/2(I+sigma_x)
= (1/4) [[2,2],[2,2]].
```

Das ist im Protokoll `lambda=1` der Schur-gesättigte positive RR-Block mit `kappa=1/4` in der gewählten dimensionslosen Konformalnormierung. Seine Form wird durch die gemeinsame Polarrekonstruktion der vorhandenen bilokalen Paare und Mediatoren realisiert; `kappa=1/4` und vollständiger Austausch sind wegen der oben gezeigten `lambda`-Abhängigkeit **keine quelleninvarianten Wechselwirkungsdaten**.

Der bedingte Positivitätsausschluss aus dem Nutzertext wird dadurch nicht verletzt. Der RR-Block ist hier eine **sektorinterne verbundene Energie relativ zum festgehaltenen Einteilchen-Baseline**, nicht der absolute Quell-Hamiltonian und nicht das Ergebnis eines globalen Vakuumshifts. Absolut liegen die hellen Eigenenergien bei 3 und 4. Es entsteht daher keine zusätzliche Nullzustandslinie des positiven Quellenoperators. Dunkle Paare bleiben in derselben sektorinternen Buchhaltung bei `+2`.

Das Ergebnis ist zugleich enger als ein voller nativer Erfolg:

- keine kanonische 64-CAR/60-CCR-Algebra,
- kein vollständiger Fockraum,
- keine Herleitung des wechselwirkenden N=64-Vakuums,
- keine 3+1D-Lokalität oder T1-T8-Schließung.

Es ist aber mehr als ein Tensorvergleich: Zustand, Gram, volle Zwei-Zeit-Antwort, Realzeit und Kollisionsgenerator sind auf demselben vorhandenen Quellenblock konstruiert.

## 4. Was aus P1/P2 stammt und was gewählt bleibt

| Stufe | Status |
|---|---|
| P1: Nahtkern/Normierung; P2: 5=3+2-Träger | deklarierte Ursprungsdaten `AX.P1.01`, `AX.P2.01` |
| `D5+A3+mu4 -> E8`, markierte interne Gruppenwirkung, Tensorlinie `W` | algebraisch aus dem Compiler unter seinen Voraussetzungen |
| exakte W-Vorzeichen, 64 Felder, 60 Mediatoren, 1956 dunkle Jets | im bedingten `F(E8)+I(1,1)`-Rand exakt konstruiert |
| `Gamma=I_(9,1)`, acht rechte Kanäle plus lokales R/L-Hilfspaar | zusätzliche Quellenklasse; nicht aus P1/P2 oder dem einspurigen QWZ-Rand hergeleitet |
| Zahlfunktion, Glue-Charakter, mikroskopische Kanalidentifikation | zusätzliche Annahmen |
| `n=(+,+,+,-,-,-,-,-,-,3)` | konditional eindeutig nach Charakteristik, Neutralität, Minimalität, deklarierter Blocksymmetrie und orientiertem Glue; diese physische Selektionsregel ist nicht hergeleitet |
| `V_aux=K+2Kmm^TK`, Gittervakuum, Konformalzeit `L_0` | kompatible, positive, blockinvariante Wahl; kein P1/P2-Satz |
| `eta`-Deformation/positive Geschwindigkeiten | kontinuierlich frei; Relevanz von `n` bleibt für `|eta|<log(2)/2`, aber `eta` wird nicht gewählt |
| `rho=r^2` | Einfügungs-/Sondenkoordinate, keine gefittete Kopplung; der Kollisionsgrenzwert eliminiert sie |
| relative Acquisition-Normierung `lambda` von Paar- und Mediatorlabel | Präparations-/Labelmetrikannahme; Spektrum `{3,4}` invariant, Mixing und maximale Austauschwahrscheinlichkeit nicht invariant |
| gemeinsamer polarer RR-Block bei `lambda=1` | im einzeln unit-normierten Acquisition-Protokoll realisiert; `kappa=1/4` ist kein quelleninvariantes Kopplungsdatum |

Damit lautet der **erste freie Selektor in der gesamten Kette**: die physische Realisierung der zehnkanaligen `I_(9,1)`-Randquelle samt tatsächlicher Blocksymmetrie, die `n` und die Phase auswählt. Wenn diese Quellenklasse bereits als Zusatzprämisse gewährt wird, ist der **erste noch freie kontinuierliche Selektor** die Energie-/Clockphase `V_eta` (insbesondere `eta` und die positiven Geschwindigkeiten); `V_aux=V_0` ist nur ein ausgezeichneter Punkt. Für eine konkrete Austauschwahrscheinlichkeit kommt danach die Acquisition-/Labelmetrik `lambda` hinzu.

## 5. Kleinster entscheidender Rücktest zur primitiven Quelle

Der nächste Test soll keine weitere Zielmodelloptimierung sein. Er muss den ersten freien Pfeil prüfen:

```text
P1/P2-/Nahtquelle
  -> tatsächliche 9R+1L-Kanalquelle, n, V und Vakuum
  -> vorhandene Psi/Phi-Felder
  -> die oben bereits bestimmte Antwort.
```

Minimaler Fail-Fast-Test:

1. Benenne den unabhängig vorhandenen P1-Randtransfer beziehungsweise Modular-/Zeitgenerator `H_P1` und dessen Zustand `Omega_P1`.
2. Konstruiere aus ihm ohne Basisfit die vorgeschlagenen zehn lokalen Kanaloperatoren. Prüfe zuerst, ob ihre Statistik-, Zahl- und Glue-Form wirklich `I_(9,1)` und den markierten `n` erzeugt. Der bekannte einspurige QWZ-Rand besteht diesen Rangtest nicht; das ist ein alter, kein neuer Ausschluss.
3. Falls der Kanaltest besteht, bilde aus denselben Operatoren `J_r` und `M` und berechne

```text
C_P1(rho,tau)=S_r^dagger exp(-tau H_P1) S_r,
S_r=(U_r,M).
```

4. Vergleiche ohne Nachjustieren zuerst Gram und ersten Jet, danach den zweiten Jet:

```text
C_P1(rho,0) ?= Gamma_r,
-d/dtau R_P1(rho,tau)|_0 ?= H_visible(rho),
R_P1''(0)-R_P1'(0)^2 ?= Quelle-Leckage der exakten Antwort.
```

Für **diesen bedingten zehnkanaligen Randkandidaten** ist der Kollisions-Gate besonders klein: Soll die P1-Quelle gerade ihn realisieren, muss ihr Transfer auf dem gemeinsamen hellen Polarquotienten die Energien `{3,4}` und auf dem dunklen Quotienten `5` liefern, jeweils mit demselben `Q_2/4`-Shift. Scheitert diese ungefitte Drei-Energie-Struktur, ist die Rückverbindung zu diesem Kandidaten widerlegt. Sie ist kein notwendiges Ziel für jede denkbare TFPT-Dynamik. Besteht sie, folgt als starker kandidatenspezifischer Test die gesamte rationale All-Time-Funktion oben.

## 6. Frische Reproduktion und Belegpfade

Frisch ausgeführt wurde nur der gezielte Originalchecker, keine Vollsuite:

```text
source-pair-transfer/checker.py
verdict: PARTIAL
checks: 7478
kernel_types: 9
same_time_pair_limit: true
native_binding_derived: false
```

Normal- und `-OO`-Lauf erzeugten byteidentische Zertifikate. SHA-256:

```text
0c6e754c0cbdcb7f9085fd6c53da3b092ed0e470a76d8d035a29f0d13757985c
```

Die 7.478 Kontrollen bestätigen die Basisformeln `G`, `T_r`, den kontrollierten Kollisionsgrenzwert und die Abgrenzung zur nativen Bindung. Die gemeinsame `(U_r,M)`-Polarfolge ist eine analytische Konsequenz dieser Formeln zusammen mit der bereits bewiesenen Identifikation `C_0=sqrt(8)M`; sie ist noch kein eigener Ledger-/Verification-Claim.

Originale:

- `experiments/theory-contracts/source-pair-transfer-20260920/PROOF.md`, insbesondere Zeilen 13–32, 78–173, 175–239, 308–324.
- `experiments/theory-contracts/source-dressed-native-20260920/PROOF.md`, insbesondere Zeilen 13–26, 32–82, 121–180.
- `experiments/theory-contracts/source-current-operator-time-20260921/source_adapter.md`, Abschnitte 1.3, 3–7.
- `experiments/theory-contracts/source-boundary-selection-20260920/PROOF.md`, insbesondere Zeilen 10–30, 65–154, 218–269.
- `experiments/theory-contracts/common-source-gauge-grade-transfer-20260920/ERGEBNIS.md`, Abschnitte 1–5.
- `experiments/theory-contracts/primitive-transfer-selection-20260912/README.md` und die Berichte `MINIMAL_COVARIANT_PROCESS.md`, `SOURCE_EDGE_ACCESS.md`, `PROCESS_MOMENT_AUDIT.md`: lokale Schatten, Kovarianz und Markovität wählen die gemeinsame Dynamik nicht.

Contract-IDs:

- `UR.SOURCE.PAIR_TRANSFER.01` — `PARTIAL`
- `UR.SOURCE.DRESSED_NATIVE.01` — `PARTIAL`
- `UR.SOURCE.OPERATOR_TIME.01` — `PARTIAL`
- `UR.SOURCE.BOUNDARY_SELECTION.01` — `PARTIAL`
- `common-source-gauge-grade-transfer-20260920` — `PARTIAL`

Die alten Zahlen 4.339/7.478 bleiben als Contract-Umfang beziehungsweise archivierte Kontrollen getrennt. Neu ausgeführt wurden hier genau die 7.478 Paarantwortkontrollen in zwei byteidentischen Modi. Kein T1–T8-Gate und keine physische Gesamtherleitung wird dadurch geschlossen.
