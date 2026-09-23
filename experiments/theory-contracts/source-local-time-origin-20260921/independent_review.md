# Unabhängiger Kurzreview: gewichteter Kreiszeitvertrag

21. September 2026 · Review der Anlage und des v221-Tests

## Urteil

Der gewichtete Klassifikationssatz ist **im periodischen skalaren Vertrag
korrekt**. Die Fourierklassifikation und die Folgerung aus der geometrischen
Vierteldrehung tragen. Es gibt keinen algebraischen Gegenfehler.

Der Satz braucht jedoch folgende Hypothesen ausdrücklich, damit „genau dann“
nicht überdehnt wird:

1. ein zusammenhängender Kreis und glattes `q>0`, `rho=q^-1`;
2. ein **skalarer lokaler Differentialoperator** erster Ordnung, kein
   matrixwertiger Diracoperator und kein allgemeiner Pseudodifferentialoperator;
3. die periodische selbstadjungierte Domäne, die die konstante Funktion
   enthält;
4. `Lambda_rho=q|D|` als positiver selbstadjungierter Operator auf
   `L2(rho dtheta)`, formdefiniert beziehungsweise mit seiner elliptischen
   selbstadjungierten Schließung;
5. Operatorgleichheit `|h|=Lambda_rho`, einschließlich gleicher Domänen, nicht
   nur Gleichheit der Hauptsymbole oder einzelner Matrixelemente.

Mit diesen Präzisierungen ist der Beweis vollständig. Für eine NS-Domäne
fehlt die konstante Nullmode; die angegebene Herleitung von `h=±qD` darf nicht
unverändert auf diesen Fall übertragen werden.

## 1. Selbstadjungiertheit und Domänen

Auf

\[
\mathcal H_\rho=L^2(S^1,\rho(\theta)d\theta),
\qquad q=\rho^{-1},
\]

ist `qD`, `D=-i partial_theta`, auf der periodischen `H1`-Domäne symmetrisch,
weil `q rho=1`:

\[
\langle f,qDg\rangle_\rho
=\int_0^{2\pi}\bar f(-ig')d\theta
=\langle qDf,g\rangle_\rho.
\]

Mit der Bogenkoordinate

\[
s(\theta)=\int_0^\theta\rho(t)dt
\]

ist dieser Operator unitär äquivalent zu `-i partial_s` auf einem Kreis der
Länge `L=integral rho dtheta`. Damit ist `qD` selbstadjungiert; für `q` glatt
und strikt positiv entspricht seine Domäne der periodischen `H1`-Domäne in
der ursprünglichen Koordinate.

Der gewichtete DtN-Operator

\[
\Lambda_\rho=q|D|
\]

ist auf demselben gewichteten Raum positiv und symmetrisch. Unter der
unitären Abbildung `f -> sqrt(rho) f` nach `L2(dtheta)` wird er

\[
q^{1/2}|D|q^{1/2}.
\]

Am saubersten wird dieser Ausdruck zunächst über seine geschlossene positive
Form definiert. Für glattes strikt positives `q` ist die zugehörige
Operatorendomäne die erwartete elliptische `H1`-Domäne. Damit sind Betrag,
Quadrat und Kernel als Operatoraussagen wohldefiniert.

## 2. Warum ein allgemeines lokales `h` tatsächlich `±qD` wird

Ein formal selbstadjungierter skalarer Differentialoperator erster Ordnung
auf `H_rho` hat die Form

\[
h=-ia(\theta)\partial_\theta
  -\frac i2\left(a'+a\frac{\rho'}\rho\right)+V,
\]

mit reellen `a,V`. Aus `|h|=Lambda_rho` folgt auf Hauptsymbolebene
`|a|=q`. Da der Kreis zusammenhängend und `q>0` ist, hat `a` konstantes
Vorzeichen: `a=±q`. Dann verschwindet der Symmetrisierungsterm wegen
`q rho=1`, und

\[
h=\pm qD+V.
\]

Auf der periodischen Domäne gilt `Lambda_rho 1=0`. Aus
`|h|=Lambda_rho` folgt `1 in ker|h|=ker h`; somit `h1=V=0`. Es bleiben
genau

\[
h=\pm qD.
\]

Dieser Nullmodenschritt ist der Grund, warum die periodische Domäne eine
tragende Hypothese ist. Bei antiperiodischer Randbedingung liegt `1` nicht in
der Domäne; zusätzliche Holonomie-/Nullordnungsterme müssen dann separat
klassifiziert werden.

## 3. Äquivalenz mit der Fourierbedingung

Für selbstadjungiertes `h=±qD` und positives selbstadjungiertes
`Lambda_rho=q|D|` gilt

\[
|h|=\Lambda_\rho
\quad\Longleftrightarrow\quad
h^2=\Lambda_\rho^2.
\]

Die Rückrichtung benutzt die Eindeutigkeit der positiven Quadratwurzel. Auf
dem gemeinsamen glatten periodischen Kern wird die Quadratgleichheit nach
Linksdivision durch `q` zu

\[
DqD=|D|q|D|.
\tag{1}
\]

Für glattes positives `q` sind beide Seiten elliptische Operatoren zweiter
Ordnung mit `H2`-Schließungen. Daher hebt die Identität auf dem gemeinsamen
glatten Kern auf die selbstadjungierten Operatoren ab. Eine bloß formale
Symbolgleichheit ohne diese Domänenaussage würde nicht genügen.

In der Fourierbasis lautet (1) exakt

\[
\langle e_m,(|D|q|D|-DqD)e_n\rangle
=(|m||n|-mn)q_{m-n}.
\]

Für `k>=2`, `m=1`, `n=1-k` folgt `2(k-1)q_k=0`; für negative `k` folgt
das konjugierte Argument. Also

\[
q_k=0\quad(|k|\ge2).
\]

Umgekehrt kann bei entgegengesetzten Vorzeichen von `m,n` nur
`|m-n|>=2` auftreten, während bei gleichen Vorzeichen der Vorfaktor null
ist. Daher reichen genau die Moden `-1,0,1`:

\[
q(\theta)=q_0+a\cos\theta+b\sin\theta,
\qquad q_0>\sqrt{a^2+b^2}.
\]

Die zusätzliche Vierteldrehung lässt von diesen drei Moden nur `q_0` übrig.
Damit folgen im angegebenen Vertrag `rho=konstant` und `h=±kappa D`.

## 4. Reichweite des v221-Zeittests

Der vorherige Primfaktortest ist korrekt, aber ausdrücklich **bedingt**. v221
definiert einen dreidimensionalen symmetrischen Recovery-/Vergessenskanal;
v814 zeigt bitgenau `T_v221=B^6` mit Spektren

\[
\operatorname{spec}B=\{1,2/3,1/3\},
\qquad
\operatorname{spec}T=\{1,(2/3)^6,(1/3)^6\}.
\]

Die Anlage behauptet keine Identität dieses Recovery-Kanals mit
`exp(-tau|h|)`. Der Widerspruch entsteht erst unter der zusätzlichen Annahme
einer gemeinsamen Quellenisometrie

\[
e^{-\tau|h|}J=JT_{\rm v221}
\]

oder unter den beiden komprimierten Momentgleichungen, die diese
Intertwinerbeziehung erzwingen. Dann kollidieren die beiden v221-Faktoren
exakt mit dem rationalen Energiegitter der periodischen beziehungsweise
NS-Kreiszeit.

Das Ergebnis widerlegt daher weder den gewichteten Klassifikationssatz noch
den Recovery-Kanal. Es zeigt nur, dass der vorhandene Recovery-Schritt nicht
ohne zusätzlichen Herkunftsnachweis zugleich als direkter Ein-Schritt-
Feldtransfer derselben lokalen Kreisquelle verwendet werden kann.

## Abschluss

**PASS mit Domänenpräzisierung.** Der gewichtete Satz ist für skalare
periodische Kreisfunktionen korrekt. Seine Übertragung auf NS-Felder,
matrixwertige Fermionen oder den v221-Recovery-Kanal wäre eine zusätzliche
Behauptung und ist in der Anlage nicht bewiesen. Die bisherige
Zeitobstruktion hält genau als Test einer solchen zusätzlichen direkten
Identifikation; sie ist kein allgemeiner TFPT-No-go.
