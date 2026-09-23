# Korrelierter IR-Glue nach der neutralen Refermionisierung

**Verdikt: PARTIAL.** Das ursprüngliche Gitter \(\Gamma\) fixiert exakt die UV-Restklassen seiner vier Glueklassen. In der zusätzlich angesetzten Produktkategorie \((D_8)_1\times\mathrm{Ising}_R\) ist ein fermionischer einfacher Strom algebraisch konsistent. Das motiviert einen sechsteiligen IR-Kandidaten, leitet ihn aber nicht aus \(\Gamma\) her: Nach Entfernung der massiven Ising-Kopie sind die kritischen \(1/\psi/\sigma\)-Sektoren nicht allein durch die UV-Paritäten festgelegt.

Die neue Quellenprüfung `UR.SOURCE.DYNAMICS_SELECTION.01` verschärft diese Grenze: Auf dem direkt deklarierten Weg von \(V_0\) nach \(V_{\rm aux}\) hat der Mittelpunkt \(\Delta(n)=\Delta(z)=2\). Die hier verwendete separate Diagnosemetrik \(V_c\) hat dagegen \(\Delta(n)=\Delta(z)=1\). Der folgende Sektortest ist deshalb keine von der Quelle ausgewählte kritische Dynamik.

## 1. Exakte Gewichte aus dem Gitter

Am gewählten \(V_c\) zerfällt jedes Feld eindeutig als

\[
x=T(p)+A u+B v,
\qquad
(h_R,h_L)=\left(\frac{p^2+A^2}{2},\frac{B^2}{2}\right).
\]

Für die vier Glueklassen ergibt das vor der Projektion des massiven Majoranas:

| Klasse | minimaler neutraler Anteil | \((h_R,h_L)\) im UV |
|---|---|---:|
| \(0\) | \(0\) | \((0,0)\) |
| \(f\), Projektion \(v\) | \((u-v)/2\) | \((5/8,1/8)\) |
| \(b\), Projektion \(s\) | \((u+v)/2\) | \((9/8,1/8)\) |
| \(f+b\), Projektion \(c\) | \(u\) oder \(v\) | roh \((5/2,0)\), minimal \((3/2,0)\) oder \((1,1/2)\) |

Der rohe Repräsentant \(f+b=T(e_1+s)+u\) hat \(p^2=4\), Lorentz-Norm \(5\), Spin \(5/2\) und daher \((5/2,0)\). Die Verschiebung um \(T(e_1+e_2)\) liefert \(p=s-e_2\) mit \(p^2=2\). Die beiden integralen minimalen Vertreter haben \((h_R,h_L)=(3/2,0)\) beziehungsweise \((1,1/2)\), also Lorentz-Normen \(3,1\) und Spins \(3/2,1/2\). Der Checker wertet jeweils den vollständigen zehndimensionalen Vektor aus.

Ein halbganzzahliger neutraler Vertex enthält im Zwei-Ising-Wörterbuch einen Twistfaktor beider Majoranas. Wird genau einer davon massiv und sein passender Ordnungs- oder Unordnungsfaktor besitzt einen Vakuumerwartungswert, entfallen auf jeder chiralen Seite \(1/16\). Bedingt darauf werden

\[
f\longmapsto (v,\sigma_R,\sigma_L): (9/16,1/16),
\]

\[
b\longmapsto (s,\sigma_R,\sigma_L): (17/16,1/16).
\]

Die beiden Klassen tragen komplementäre Ordnung/Unordnung-Daten. Die Virasoro-Gewichte allein entscheiden nicht, welche davon nach Wahl des massiven Vakuums als gewöhnliches lokales Feld verbleibt.

## 2. Der exakte einfache-Strom-Test

Für \((D_8)_1\) gelten

\[
h_0=0,\qquad h_v=\tfrac12,\qquad h_s=h_c=1,
\]

und für Ising

\[
h_1=0,\qquad h_\psi=\tfrac12,\qquad h_\sigma=\tfrac1{16}.
\]

Der rechte Kandidat

\[
J=(c,\psi_R),\qquad h_J=\tfrac32
\]

ist in der angesetzten Produktkategorie ein fermionischer einfacher Strom der Ordnung zwei. Die integralen Gitterfelder \(T(s-e_2)+u\) und ihre Konjugierten liefern exakt die passende \(c\)-Klasse mit chiralem \(u\)-Dressing. Erst die zusätzliche Refermionisierung und Wahl des massiven Vakuums identifiziert dessen masselose Projektion mit \(\psi_R\); das motiviert \(J\), leitet ihn aber nicht aus der Quelle her.

Die Monodromieladungen sind

\[
Q_c(0)=Q_c(c)=0,qquad Q_c(v)=Q_c(s)=\tfrac12,
\]

\[
Q_\psi(1)=Q_\psi(\psi)=0,qquad Q_\psi(\sigma)=\tfrac12.
\]

Damit ist die vollständige rechte monodromielokale Menge

\[
(0,1),(0,\psi),(c,1),(c,\psi),(v,\sigma),(s,\sigma).
\]

Sie ist unter Fusion geschlossen und zerfällt in drei \(J\)-Bahnen:

\[
(0,1)\leftrightarrow(c,\psi),
\quad
(0,\psi)\leftrightarrow(c,1),
\quad
(v,\sigma)\leftrightarrow(s,\sigma).
\]

Weil \(h_J\) halbzahlig ist, ist dies eine **fermionische** Erweiterung. Eine spinstrukturunabhängige bosonische Erweiterung folgt daraus nicht.

## 3. Der von \(\Gamma\) korrelierte UV-Glue und sein bedingter IR-Kandidat

Die vier Nebenklassen liefern zusätzlich zur rechten Monodromie die Links-Rechts-Korrelation:

\[
\begin{array}{c|c}
\text{Glueklasse}&(A,B)\text{ in }x=T(p)+Au+Bv\\ \hline
0&A,B\in\mathbb Z,\ A\equiv B\pmod2\\
c&A,B\in\mathbb Z,\ A\not\equiv B\pmod2\\
v,s&A,B\in\mathbb Z+1/2.
\end{array}
\]

Exakt aus \(\Gamma\) folgt bis hierher nur diese UV-Restklassenkorrelation. Unter der zusätzlichen Standard-Refermionisierungszuordnung und nach Wahl des massiven Ising-Vakuums, der Spinstruktur und der lokalen Defektlinien ergibt sich daraus der folgende korrelierte Sechs-Sektoren-**Kandidat**:

\[
\begin{array}{c|c}
T(D_8)\text{-Klasse}&(\text{Ising}_R,\text{Ising}_L)\\ \hline
0&(1,1)\oplus(\psi,\psi)\\
c&(\psi,1)\oplus(1,\psi)\\
v&(\sigma,\sigma)\\
s&(\sigma,\sigma).
\end{array}
\]

Der daraus folgende Sechs-Sektoren-Kandidat lautet

\[
\begin{aligned}
\mathcal H_{\rm cand}={}&[(0,1_R)\oplus(c,\psi_R)]\otimes 1_L\\
&\oplus[(0,\psi_R)\oplus(c,1_R)]\otimes\psi_L\\
&\oplus[(v,\sigma_R)\oplus(s,\sigma_R)]\otimes\sigma_L.
\end{aligned}
\]

Seine sechs Gewichte sind

\[
(0,0),\ (1/2,1/2),\ (3/2,0),\ (1,1/2),\
(9/16,1/16),\ (17/16,1/16).
\]

Diese Zuordnung ist ein mit den vier \(\Gamma/M\)-Klassen kompatibler IR-Kandidat. Die Bezeichnungen „diagonal“, „antidiagonal“ und „Ramond“ sind Teil der zusätzlichen Ising-Zuordnung und kein bereits von der Quelle ausgewählter Projektor. Der Kandidat respektiert die mikroskopische Bedingung, dass ein nichtintegrales \(u\)- oder \(v\)-Refermion nicht als nacktes lokales Feld eingeführt werden darf.

## 4. Was exakt ist und was noch fehlt

Exakt sind:

1. die vier Gitterklassen und ihre Parität;
2. ihre neutralen Restklassen und vollständigen \((h_R,h_L)\)-Gewichte an \(V_c\);
3. die Monodromietabelle von \(J=(c,\psi_R)\);
4. die sechs monodromielokalen rechten Objekte, ihre Fusionsgeschlossenheit und ihre drei \(J\)-Bahnen innerhalb der angesetzten Produktkategorie;
5. die durch \(\Gamma\) erzwungene UV-Korrelation der \(u,v\)-Restklassen.

Nicht exakt hergeleitet ist die Identifikation dieser UV-Reste mit unabhängig festgelegten kritischen \(1/\psi/\sigma\)-Sektoren beider Chiralitäten nach Entfernung der massiven Ising-Kopie.

Für den tatsächlichen massiven-Vakuum-Projektor fehlt weiterhin:

- welches Vorzeichen der massiven Majoranamasse realisiert wird;
- welche der komplementären \(f/b\)-Twists den nichtverschwindenden Ordnungs- beziehungsweise Unordnungs-Vakuumerwartungswert trägt;
- welche Spinstruktur und welche Defektlinien als lokale Operatoren zugelassen sind.

Ohne diese Daten darf die letzte \(J\)-Bahn \((v,\sigma)\leftrightarrow(s,\sigma)\) nicht automatisch als zwei gleichzeitig gewöhnliche lokale Felder interpretiert werden. Der Sechs-Sektoren-Ausdruck ist ein mit dem exakten UV-Glue kompatibler bedingter Kandidat, aber kein aus \(\Gamma\) oder der Quelle hergeleiteter physikalischer IR-Projektor. Insbesondere folgt weder eine \(N=1\)-Supersymmetrie noch eine vierdimensionale chirale Fermionauswahl.

## Reproduktion

```bash
python3 check_ir_glue.py
python3 -OO check_ir_glue.py
```
