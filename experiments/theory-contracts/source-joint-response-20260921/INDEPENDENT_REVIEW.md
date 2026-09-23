# Unabhängige Prüfung der gemeinsamen Paar-/Mediator-Polarrekonstruktion

Stand: 21. September 2026  
Geprüfte Ausgangsverträge: `UR.SOURCE.PAIR_TRANSFER.01` und
`UR.SOURCE.DRESSED_NATIVE.01`  
Urteil: **PARTIAL — der bedingte endlichdimensionale Grenzsatz ist exakt; die
Interpretation als quelleninvariante Wechselwirkung oder voller
CAR/CCR-Hamiltonian ist nicht begründet.**

## 1. Präzise Entscheidung

Die gemeinsame Polarrekonstruktion der bereits vorhandenen bilokalen
Paarzustände und Mediatorzustände ist mathematisch korrekt. Für jede endliche
Separation `0 < rho < 1` hat sie vollen Rang `2076`. Im Kollisionsgrenzwert
liefert sie, beim ausdrücklich gewählten gleichgewichteten Eingabeprotokoll,

```text
60 helle Richtungen mit Energie 3,
60 helle Tangential-/Jet-Richtungen mit Energie 4,
1956 dunkle Richtungen mit Energie 5.
```

In der ursprünglichen helles-Paar/Mediator-Basis ist der helle Grenzgenerator

```text
H_b,0 = [[7/2,-1/2],[-1/2,7/2]] tensor I_60.
```

Nach Abzug des gemeinsamen Zweifeld-Baselines `3I` ergibt sich bedingt

```text
V_rel = 1/2 [[1,-1],[-1,1]] tensor I_60
        direct-sum 2 I_1956.
```

Diese Sätze sind exakte Folgerungen aus der bereits gewählten zehnkanaligen
Randquelle, `Vaux`, dem Gittervakuum, der Konformalzeit und dem
Standard-Direktsummenmetrik-Protokoll. Sie sind keine Herleitung dieser
Voraussetzungen aus P1/P2.

Der scheinbar perfekte Paar↔Mediator-Transfer und der Koeffizient `-1/2` sind
jedoch **nicht invariant unter einer Änderung der relativen
Eingabenormalisierung**. Sie sind daher kein von der Quelle allein bestimmter
Kopplungswert. Die gemeinsame Polarabbildung ändert außerdem die vorbereiteten
Operatorzustände: Sie ist eine Isometrie von Labelräumen in den Quellenraum,
aber kein Produkt-, Adjunkt- oder CAR/CCR-Homomorphismus.

## 2. Exakte gemeinsame Gram-Matrix

Sei

```text
A = W^dagger W = 8 P_b,
W_hat = W/sqrt(8),
P_d = I-P_b,
G(rho) = d(rho) I + o(rho) A,
g_b(rho) = d(rho)+8o(rho).
```

Aus dem Paarvertrag gilt

```text
d(rho) = rho^2(2-rho)/[2(1-rho)^3],
o(rho) = (2-rho)/[2(1-rho)^2],
U_r = J_r G(rho)^(-1/2).
```

Sei `M : B -> H_src` die isometrische Einbettung der 60 vorhandenen
Mediatorfelder. Aus `C_0=M W` und der Orthogonalität verschiedener
Konformalgrade folgt ohne weitere Annahme

```text
J_r^dagger M = C_0^dagger M = W^dagger,
U_r^dagger M = G(rho)^(-1/2) W^dagger
              = c(rho) W_hat^dagger,
c(rho) = sqrt(8/g_b(rho)).
```

Damit besitzt `S_r(x,y)=U_r x+M y` exakt die Gram-Matrix

```text
K_r = [[I, c W_hat^dagger],
       [c W_hat, I]].
```

Auf `P_d E` ist sie die Identität. Nach Identifikation von `P_b E` mit `B`
durch `W_hat` zerfällt sie in 60 Blöcke

```text
[[1,c],[c,1]],
```

mit Eigenwerten `1+c` und `1-c`. Für `0<rho<1` enthält die normierte helle
Paarantwort positive Gewichte oberhalb des Grundgrades, also `g_b(rho)>8`
und `0<c<1`. Deshalb ist `K_r` positiv definit und

```text
rank S_r = 1956+60+60 = 2076.
```

Die gemeinsame Polarabbildung

```text
V_r = S_r K_r^(-1/2)
```

ist somit für jede endliche Separation eine Isometrie auf dem gesamten
Labelraum.

## 3. Kollisionsgrenzwert und Energieblock

Für einen normierten hellen Paarlabelvektor `x_A=W_hat^dagger e_A` setze

```text
chi_A = U_r x_A,
phi_A = M e_A,
<phi_A,chi_A> = c,
eta_A = (chi_A-c phi_A)/sqrt(1-c^2).
```

Dann sind `phi_A` und `eta_A` orthonormal. In der symmetrischen/antisymmetrischen
Eingabebasis `e_+ = (x_A,e_A)/sqrt(2)`,
`e_- = (x_A,-e_A)/sqrt(2)` gilt exakt

```text
V_r e_+ = sqrt((1+c)/2) phi_A + sqrt((1-c)/2) eta_A,
V_r e_- =-sqrt((1-c)/2) phi_A + sqrt((1+c)/2) eta_A.
```

`phi_A` hat Energie 3. Nach Entfernung dieses Anteils ist das niedrigste
Gewicht von `eta_A` der normierte `C_1`-Anteil mit Energie 4. Sein exaktes
Gewicht ist

```text
q_1(rho) = 12 rho/[g_b(rho)-8]
         = 24(1-rho)^3/[(4-3rho)(6-5rho)].
```

Da `q_1 -> 1`, konvergiert `eta_A` zur normierten `C_1`-Richtung

```text
zeta_A = C_1 x_A/sqrt(12),    H_0 zeta_A=4 zeta_A.
```

Folglich

```text
V_0 e_+ = phi_A,   V_0 e_- = zeta_A.
```

Der helle Generator ist in der `+/-`-Basis `diag(3,4)`. Die Hadamard-
Rücktransformation ergibt

```text
H_b,0 = 1/2 [[3+4,3-4],[3-4,3+4]]
      = [[7/2,-1/2],[-1/2,7/2]].
```

Die dunkle Polargrenze ist die schon bewiesene normierte `C_2`-Richtung mit
Energie 5. Ein gemeinsamer Viertelladungsterm verschiebt jeden festen
Impuls-/Ladungsfaserblock um denselben Skalar `-Q_2/4`; er ändert weder die
Mischung noch die folgenden Fehlerabschätzungen.

## 4. Exakte All-Time-Antwort

Vor der gemeinsamen Polarnormalisierung lautet der helle Block für alle
`tau>=0`, beziehungsweise nach `tau=it` für alle reellen Zeiten,

```text
K_b(rho,tau) =
 [[T_b(rho,tau), c exp(-3tau)],
  [c exp(-3tau), exp(-3tau)]],

T_b(rho,tau)
 = exp(-3tau) g_b(rho exp(-tau))/g_b(rho).
```

Die tatsächliche gemeinsame Antwort ist

```text
R_b(rho,tau)
 = Gamma_b(rho)^(-1/2) K_b(rho,tau) Gamma_b(rho)^(-1/2),
Gamma_b(rho)=[[1,c],[c,1]].
```

Schreibt man

```text
cos(theta)=sqrt((1+c)/2),
sin(theta)=sqrt((1-c)/2),
```

und bezeichnet die normierte Zeitantwort von `eta_A` mit `R_eta`, dann ist
dies äquivalent zu

```text
R_b(rho,tau)
 = Rot(theta)^dagger diag(exp(-3tau),R_eta(rho,tau)) Rot(theta).
```

Diese Formel zeigt zugleich die Grenze: Bei endlichem `rho` besitzt
`R_eta` unendlich viele positive Spektralgewichte ab Energie 4. Der sichtbare
Block ist daher bei endlicher Separation keine geschlossene Zweiniveau-
Hamiltonentwicklung. Erst im Kollisionsgrenzwert wird er invariant und

```text
R_b(0,tau)=exp(-tau H_b,0).
```

## 5. Uniforme Echtzeitfehlerabschätzung

Die Restmasse oberhalb der Energie-4-Richtung erfüllt exakt

```text
2rho-(1-q_1)
 = rho(2-rho)(7-6rho)/[(4-3rho)(6-5rho)] >= 0,
```

also `1-q_1 <= 2rho`. Für alle `t in R` folgt daher

```text
|R_eta(rho,it)-exp(-4it)| <= 2(1-q_1) <= 4rho.
```

Aus dem alten hellen Grundgewichtsbound

```text
1-c <= 1-c^2 = 1-p_b <= 3rho/2
```

folgt

```text
2 sin(theta) = sqrt(2(1-c)) <= sqrt(3rho).
```

Für zwei Einheitsphasen `a,b` gilt exakt

```text
||Rot(theta)^dagger diag(a,b) Rot(theta)-diag(a,b)||
 <= |a-b| sin(theta) <= 2 sin(theta).
```

Mit der Dreiecksungleichung erhält man die uniforme helle Schranke

```text
sup_t ||R_b(rho,it)-exp(-it H_b,0)||
 <= 4rho + sqrt(3rho).
```

Für den dunklen Block bleibt die bereits bewiesene Schranke

```text
sup_t ||T_d(rho,it)-exp(-5it)|| <= 5rho.
```

Da `4rho+sqrt(3rho) >= 5rho` für `0<rho<1`, gilt für den gesamten gemeinsamen
Block

```text
sup_t ||R_r(it)-exp(-it H_joint,0)||
 <= 4rho+sqrt(3rho).
```

Zusätzlich darf man die triviale Schranke `2` nehmen, also rechts
`min(2,4rho+sqrt(3rho))`. Der nichttriviale Term geht gleichmäßig in der
gesamten Echtzeit gegen null.

## 6. Entscheidender Normalisierungstest: Sättigung ist protokollabhängig

Die Quelle bestimmt die zwei Rohpräparationen, aber nicht allein deren
relative Metrik als unabhängige Eingabelabel. Das wird sichtbar, wenn man vor
der gemeinsamen Polarnormalisierung nur die Paarseite reskaliert:

```text
S_(r,lambda) = (lambda U_r, M),    lambda>0.
```

Für jedes endliche `rho` bleibt die Gram-Matrix positiv. Im
Kollisionsgrenzwert wählt sie als Energie-3-Richtung

```text
v_lambda=(lambda,1)/sqrt(1+lambda^2)
```

und als Energie-4-Richtung deren Orthogonalkomplement. Der Grenzgenerator ist
daher

```text
H_lambda = 3 v_lambda v_lambda^dagger
           +4(I-v_lambda v_lambda^dagger)
         = 4I-v_lambda v_lambda^dagger

         = 1/(1+lambda^2)
           [[3lambda^2+4, -lambda],
            [-lambda, 4lambda^2+3]].
```

Der Offdiagonalterm ist `-lambda/(1+lambda^2)`. Die maximale
Paar↔Mediator-Transferwahrscheinlichkeit lautet

```text
P_max(lambda)=4lambda^2/(1+lambda^2)^2.
```

Nur bei `lambda=1` ist sie eins. Schon `lambda=2` ergibt exakt `16/25`.
Damit sind die vollständige Sättigung, der Austauschkoeffizient `-1/2` und
die nach Phasenwechsel angegebene RR-Normierung `kappa=1/4` Eigenschaften des
ausdrücklich gleichgewichteten Acquisition-Protokolls. Innerhalb dieses
Protokolls sind sie exakt; als quelleninvariante Kopplung sind sie nicht
hergeleitet.

Die Singularität des Protokolls ist ebenfalls sichtbar: Die kleine
Gram-Eigenzahl ist `1-c`, also wächst die Konditionszahl wie

```text
(1+c)/(1-c) -> infinity.
```

Die Energie-4-Richtung entsteht durch normiertes Subtrahieren zweier im
Grenzwert identischer Rohpräparationen. Der Zustandsgrenzwert und seine
Zeitantwort sind kontrolliert, aber eine gleichmäßig beschränkte oder
rauschrobuste physische Präparationsoperation ist damit nicht bewiesen.

## 7. Physische Reichweite und Vakuumfrage

Der Satz fügt keinen neuen Quellenmodus hinzu: Die Energie-4-Richtung ist der
schon vorhandene erste Paar-Jet. Er repariert den alten Rangverlust jedoch
durch **neue polarisierte Präparationen**. Insbesondere mischt
`K_r^(-1/2)` Paar- und Mediatorlabel. Deshalb gilt nach der Rekonstruktion
nicht mehr gleichzeitig

```text
Paarlabel -> ursprüngliches Produkt Psi_i Psi_j,
Mediatorlabel -> ursprüngliches Feld Phi_A.
```

Die alte Feststellung bleibt bestehen: Die lokalen `Psi_i` haben keine
kanonischen CAR, die `Phi_A` sind keine 60 unabhängigen CCR-Moden, und der
koinzidente Produktdefekt wird nicht als Operatoridentität behoben. Bewiesen
ist eine isometrische Zustands-/Antwortrekonstruktion auf einem ausgewählten
`Q=2`-Labelblock.

Auch die Vakuumfrage wird nicht gelöst. Absolut liegen die hellen Energien bei
3 und 4, sodass der positive Quellenoperator keine neue Nullrichtung erhält.
Der relative Block `H_b,0-3I` besitzt dagegen 60 Nullrichtungen. Diese beiden
Aussagen dürfen nicht vermischt werden:

- Als bloße verbundene Energie relativ zum Einteilchenbaseline widerspricht
  der Block keinem absoluten Vakuumsatz.
- Als globaler Shift `H_0-(3/2)Q` würde er bereits Einzelfelder und helle
  Kombinationen auf Energie null setzen und die Vakuumeindeutigkeit verlieren.
- Als nur im `Q=2`-Sektor vorgenommene Subtraktion wäre er eine neue
  besetzungsabhängige Dynamik.

Der relative positive Block liefert insbesondere nicht die negative helle
Bindungsenergie des nativen Hamiltonians

```text
[[0,sqrt(8)g],[sqrt(8)g,Delta]],    det=-8g^2<0.
```

Er darf deshalb nicht frei zu einem Fock-Hamiltonian zweitquantisiert werden.
Dafür fehlen Produkt-/Adjunkterhalt, höhere Ladungssektoren, Domains,
Lokalität und eine aus der Quelle bestimmte gemeinsame Zustandsauswahl.

## 8. Endurteil

**Bewiesen, unter den gewählten Randvoraussetzungen:**

1. voller Rang 2076 für jede endliche Separation;
2. exakte gemeinsame All-Time-Antwort;
3. Kollisionsspektrum `3^60,4^60,5^1956`;
4. der `[[7/2,-1/2],[-1/2,7/2]]`-Block für die gleichgewichtete
   Standard-Direktsummenmetrik;
5. uniforme Echtzeitkonvergenz mit Fehler höchstens
   `min(2,4rho+sqrt(3rho))`;
6. keine zusätzliche Quellenmode, sondern Nutzung des vorhandenen ersten Jets.

**Nicht bewiesen:**

1. eine quelleninvariante Austauschkopplung oder perfekte Sättigung;
2. eine primitive Auswahl der relativen Paar-/Mediator-Eingabemetrik;
3. Erhalt der ursprünglichen Feldprodukte oder volle CAR/CCR;
4. ein autonomer endlicher Block bei endlicher Separation;
5. ein absoluter positiver Fock-Hamiltonian mit eindeutigem physischem Vakuum;
6. Herkunft von `I_(9,1)`, `Vaux`, Vakuum und Konformalzeit aus P1/P2;
7. irgendeine T1–T8-Schließung oder eine volle TFPT-Lösung.

Der Satz ist damit ein echter neuer **bedingter Zustands-/Zeitrekonstruktionssatz**.
Seine stärkste physische Lesart ist eine kontrollierte zweikanalige
Acquisition-Antwort der vorhandenen Randfelder. Er ist keine hergeleitete
mikroskopische Wechselwirkung.

## 9. Belegstellen

- `source-pair-transfer-20260920/PROOF.md`, Zeilen 78–121: vollständige
  Gram-Antwort und Spektralgewichte.
- Ebenda, Zeilen 123–173: endliche komprimierte Zeitantwort und fehlende
  geschlossene Hamiltonentwicklung.
- Ebenda, Zeilen 175–231: Polargrenze, Energien 3/5 und uniforme alte
  Paarfehlergrenzen.
- Ebenda, Zeilen 233–285: nichtnegative verbundene Energie und Abgrenzung zur
  nativen attraktiven Bindung.
- `source-dressed-native-20260920/PROOF.md`, Zeilen 121–188: `C_0=M W`,
  `C_1`, `C_2`, Rang 2016 und dunkler Jet.
- Ebenda, Zeilen 190–221: exakter CAR/CCR- und Produkt-/Gram-Rangdefekt.
- Ebenda, Zeilen 240–271: gemeinsame Energie-/Ladungsgrenzen und
  zusätzliche Wahl von `Vaux`.

Das Urteil bleibt im Experimente-Firewall `PARTIAL`. Es rechtfertigt weder
Ledger-/Paper-Promotion noch eine Übertragung auf den vollen Fockraum.
