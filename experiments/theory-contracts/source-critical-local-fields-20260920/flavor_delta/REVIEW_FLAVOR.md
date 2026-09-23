# Flavorprüfung des bedingten lokalen `c`-Spinors

**Contract:** `UR.SOURCE.CRITICAL_C_FLAVOR_REVIEW.20260920`  
**Verdikt:** `BEDINGT: LOKALES UNGERADES FELDBEIN; FESTER EINTRIPLET-KANAL BLEIBT RANG 2; VOLLREELLE 6 IST EIN NICHT SELEKTIERTER RANGWEG`

## Entscheidung

Der neue minimale lokale `c`-Klassenvertreter beseitigt unter den bereits
gesetzten Voraussetzungen am Konkurrenzpunkt `V_c` den früheren engen
Statistik-/Feldbein-Einwand. Er liefert bedingt ein lokales ungerades Feld in

\[
(16,\bar 4)+(\overline{16},4).
\]

Er beseitigt den Massenrangdefekt noch nicht. Für einen festen neutralen
Spin(10)-Higgs-Kanal und genau eine Familien-Tripletkomponente bleibt die
erzwungene Dreifamilienmatrix schiefsymmetrisch, hat Rang zwei und vernichtet
ihren eigenen Hintergrundsvektor. Ein Vollrangweg existiert erst, wenn beide
entgegengesetzten `SU(3) x U(1)_F`-Komponenten der ganzen `SU(4)`-Sechs im
selben neutralen Kanal aktiviert werden. Die vorhandene Realstruktur erlaubt
das, wählt es aber nicht aus.

Damit ist die kritische Frage scharf beantwortet:

* **Ja:** Das neue Modul kann bedingt das fehlende lokale ungerade Feldbein
  liefern.
* **Nein:** Es erzeugt aus dem bisherigen einen Familienhintergrund keine
  dritte Masse.
* **Bedingte positive Route:** Eine ausgewählte volle reelle Familien-`6`
  kann eine vierdimensionale Familien-plus-Anker-Matrix invertierbar machen.
  Weder diese Hintergrundwahl noch die Abtrennung eines schweren Ankers auf
  drei leichte Familien ist aus der geprüften Quelle hergeleitet.

## 1. Tatsächliche Darstellung und erzwungener Tensor

Das gemeinsame `T(D8)`-Glue ordnet die ungerade `c`-Klasse als

\[
(16,\bar4)+(\overline{16},4)
\]

ein. Der minimale Vertreter ist `x_c=T(s-e2)+u` beziehungsweise sein
`v`-Partner, nicht der rohe, nichtminimale Vertreter `f+b=T(e1+s)+u`.
Am separat gewählten `V_c` besitzt der minimale Vertreter exakt
`Delta=3/2`; das ist eine bedingte 1+1-dimensionale Aussage und keine
4D-Weyl-Skalendimension.

Zuerst ist die Orientierung des bereits implementierten Operators zu
fixieren. `native_source.py` erzeugt seine 64 `FW`-Gewichte aus geraden
D5-Masken und den vier geraden D3-Masken

```text
(+++), (--+), (-+-), (+--).
```

Damit haben alle 64 Gewichte gerade D5- und gerade D3-Minusparität. In der
festen Konvention von `local_modules` ist dieser tatsächlich implementierte
alte `S+`-Summand

\[
(\overline{16},\bar4),
\]

nicht `(16,4)`. Die 64 global negierten Gewichte bilden den anderen alten
Summanden `(16,4)` und kommen im implementierten `FW64` nicht vor. Jede
Übertragung vom nativen `W` auf diesen Partner braucht daher die ausdrücklich
deklarierte globale Wurzelkonjugation.

Für zwei neue Materiefelder in `bar4` und den Mediator `(10,6)` ist die
Familienabbildung darstellungstheoretisch bis auf Normierung durch `SU(4)`
festgelegt:

\[
W_-:\Lambda^2\bar4\longrightarrow 6,
\qquad
(Y_H)_{ab}=\epsilon_{abcd}H_{cd}.
\]

Relativ zum global konjugierten alten linken Summanden `(16,4)` kann diese
Abbildung als `W_-` bezeichnet werden. Sie ist damit noch kein im gepinnten
`FW64` implementierter Operator auf den neuen `(16,bar4)`-Feldern.
Äquivalent formuliert: Der neue `c`-Summand `(16,bar4)` unterscheidet sich
vom tatsächlich implementierten `(bar16,bar4)` durch einen D5-Chiralitäts-
wechsel, vom global konjugierten `(16,4)` dagegen durch die Familiendualität.
Beides sind hier deklarierte algebraische Darstellungsabbildungen; ein
physikalischer Intertwiner, der zugleich Hyperladung, Energie und
Operatorwirkung transportiert, ist daraus nicht hergeleitet.

Im nativen `CW`-Order haben die vier Gewichte für die hier deklarierte
`SU(3) x U(1)_F`-Cartanrichtung die direkt abgelesenen Grade

\[
(+3,-1,-1,-1),
\]

also `bar4 = 1_(+3) + bar3_(-1)` mit dem Anker an Index 0. Für die folgenden
Formeln wird ausdrücklich mit `[1,2,3,0]` in die bequemere Reihenfolge
„Triplet, dann Anker“ permutiert. Erst in dieser deklarierten Basis gilt

\[
\bar4=\bar3_{-1}+1_{+3},\qquad
6=\bar3_{+2}+3_{-2}
\]

Bei einer Aufspaltung der sechs Higgs-Komponenten in zwei Triplets `h` und
`k` ergibt sich dann die folgende Matrix. Der Balken in `bar4` bezeichnet die konjugierte
**Darstellung**; er ist hier kein Balken auf dem Komponentenvektor `h`.

\[
Y_-(h,k)=
\begin{pmatrix}
A(h)&k\\
-k^T&0
\end{pmatrix},
\qquad
A(h)_{ij}=\epsilon_{ijk}h_k .
\]

Exakt gilt

\[
A(h)h=0,
\quad \operatorname{rank}A(h)=2\;(h\ne0),
\quad
\det Y_-=(h^T k)^2.
\]

Der alte Einhintergrund-Ausschluss bleibt deshalb für einen **festen
Tripletgrad** vollständig bestehen. Ein interner schwach-chiraler Markierer
wie `S d_H` korrigiert die kombinierte Austauschsymmetrie, füllt aber die
fehlende entgegengesetzte Tripletkomponente nicht und ändert den Rang nicht.

## 2. Was die Realität von `(10,6)` tatsächlich tut

Im gepinnten nativen Tensor lautet die Wurzelkonjugation auf allen 60
Bosonen exakt

\[
\mathrm{BAR}(k,\{a,b\})
=\bigl(k+5\bmod 10,\{a,b\}^{c}\bigr).
\]

Sie dreht also **beide** Faktoren gleichzeitig:

1. das Spin(10)-Vektorgewicht, damit beim neutralen Paar
   `H_d <-> H_u`, und
2. den relativen `U(1)_F`-Grad der Familien-`6` durch die komplementäre
   Zweiermenge.

Die tatsächlichen neutralen Gewichte im 45-Kubik bestätigen den ersten
Punkt: Index 12 hat `Y=-1/2` und ist die `H_d`-Komponente; Index 14 hat
`Y=+1/2` und ist die entgegengesetzte Spin(10)-Komponente `H_u`. Daher
erzwingt die native Realität eine Relation der Form

\[
H_d(\{a,b\})^* = \pm H_u(\{a,b\}^{c}),
\]

nicht `k=conj(h)` innerhalb eines festgehaltenen `H_d`- oder `H_u`-Kanals.

Das vermeidet eine zu starke Negativaussage: Nimmt man **zusätzlich** einen
separierbaren Hintergrund `v_10 tensor H_6` an und verlangt beide Faktoren
einzeln reell, dann ist innerhalb des Familienfaktors

\[
k=\overline h,
\qquad
\det Y_-(h,\overline h)=\|h\|^4.
\]

Das ist ein echtes algebraisches Gegenbeispiel gegen einen Rang-zwei-Satz
für eine vollständig aktivierte reelle `6`. Es folgt aber nicht aus der
simultanen `BAR`-Involution allein. Die zusätzliche Separierbarkeit und die
Auswahl genau dieses Hintergrunds sind neue Voraussetzungen.

## 3. Abgleich mit dem vorhandenen Originaloperator

Der native `W`-Tensor in `native_source.py` ist positiv und konkret, aber er
ist auf dem alten `S+`-Summanden `(bar16,bar4)` implementiert. Sein
global konjugierter Partner `(16,4)` ist nicht Bestandteil von `FW64`.
Der neue `W_-:Lambda2(bar4)->6`-Tensor ist relativ zu diesem konjugierten
alten linken Summanden darstellungstheoretisch festgelegt, im gepinnten
Operator aber nicht als Kopplung der neuen lokalen `c`-Felder realisiert.

Das tatsächliche 45-Kubik faktorisiert als

\[
C_{(A,i)(B,j)(C,k)}=d_{ABC}\epsilon_{ijk}.
\]

Es enthält die vier real geprüften neutralen Up- und vier Down-Slots, aber
sein Familienfaktor ist der alte `A2`-Epsilon-Tensor auf drei Familien. Es
wählt weder eine volle `SU(4)`-Sechs, noch einen vierten Familienanker, noch
den separierbaren reellen Hintergrund aus. Deshalb darf die bedingte
`det=||h||^4`-Konstruktion nicht rückwirkend als Ergebnis des 45-Kubiks
ausgegeben werden.

Auch der Ort, an dem das neue lokale Feld leicht sein soll, bleibt
quellenseitig bedingt. Der direkte, bereits geprüfte Weg von `V0` nach
`V_aux` trifft am Mittelpunkt `Delta_n=Delta_z=2`; er trifft nicht den
separat gewählten Punkt `V_c` mit beiden Dimensionen eins. Der Ursprung der
nötigen nichtgaußschen Kopplungen, ihre Koeffizienten und die Auswahl des
kritischen Zustands bleiben offen. Der Quartic-Term eines separaten
Rotormodells besitzt keinen bewiesenen Operator-, Ladungs-, Zustands- und
Zeittransport auf diese Randtheorie.

## 4. Verbleibende erste Lücke

Die erste fehlende Abbildung ist jetzt enger als zuvor. Benötigt wird ein
Originaloperator, der gleichzeitig

1. den bedingten lokalen `c`-Spinor in die Materiekopplung transportiert,
2. `W_-` mit einem nachgewiesenen Koeffizienten realisiert,
3. im selben neutralen Spin(10)-Kanal beide Familien-Triplets aktiviert oder
   die stärkere separierbare reelle Hintergrundbedingung herleitet, und
4. einen schweren vierten Anker sowie die effektive Dreifamilienreduktion
   bestimmt.

Selbst dann wären beobachtete Massenspaltungen und Mischungen noch nicht
automatisch erklärt: `det=||h||^4` beweist Vollrang für vier Komponenten,
nicht drei leichte Familien, deren Hierarchie oder CKM/PMNS-Struktur.

## Gepinnte Hauptquellen

* `local_modules/PROOF.md`: `5d458c5fe3ceabfd12b5f637cff1fcad3ea0f618ba0e23d898bcbf6f9ba0ba00`
* `local_modules/certificate.json`: `9d4f000ec16cfdc6e54e8226ac556192195c1a03b57c033081ec8815d058bd9e`
* `critical_review/REVIEW.md`: `6be13b4fcb16ac68c0b267bda02ebd993dcea1bea1d2951d7980c52e2d5ab817`
* `critical_review/field_table.json`: `32ae92fd4767db883de301d1b3f8fe6cee9420a5b906b4c5f1e33618354b0add`
* `critical_review/validation.json`: `3a17ddb7008347082f3213972e176a78379ec885dae0a688632d7c7acde270b2`
* `native_source.py`: `380577f85d2afa8b50f91a0991769eaf8267ee5c09f327d87f17e1b4c0af1672`
* `compiler-vacuum-current-cubic-20260918/certificate.json`: `150f27876e19fba789b497d53b1dc02b3d9f2f02704b991cc214cfc8e0ab51eb`
* `source-flavor-origin-20260920/certificate.optimized.json`: `3efa28973698464e873b0ae2bde82469a73e1f1bf3543c85a33e63bfe931a9ca`
* `source-graded-locality-20260920/PROOF.txt`: `669309ea7f240397b2eb49c61e02b5224d4b9d1c15d50aeca30668fa97fa41bb`
* `source-dynamics-selection-20260920/PROOF.txt`: `03c09468b07cc68abd31d7f8d6715dd474564728d053ccb063a67a1ca71c89d2`

Die exakten endlichen Identitäten und Pins prüft `check_critical_flavor.py`.
Es verändert keine Originalquelle, kein Paper, kein Ledger und keinen
Theoriegraphen.
