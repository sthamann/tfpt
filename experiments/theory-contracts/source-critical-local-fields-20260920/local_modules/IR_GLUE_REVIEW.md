# Kurzaudit zu `IR_GLUE.md`

**Verdikt:** `NEEDS_SCOPE_EDIT`

Die exakten UV-Gitteraussagen und der abstrakte einfache-Strom-Test sind
konsistent. Abschnitt 3 und die Exaktheitsliste in Abschnitt 4 gehen jedoch
an einer Stelle zu weit: Der Checker leitet den ausgeschriebenen
sechsteiligen **physischen IR-Sektorprojektor** nicht aus \(\Gamma\) her.
Er prüft eine UV-Restklassenkorrelation und testet anschließend einen
zusätzlich angesetzten Ising-Sektorkandidaten.

## Was exakt gezeigt ist

1. Aus \(\Gamma/(T(D_8)\oplus\mathbb Zn\oplus\mathbb Zz)\) folgen exakt
   die vier Glueklassen und für die neutralen \(u,v\)-Koeffizienten:

   \[
   0:\ A,B\in\mathbb Z,\ A\equiv B\pmod2,
   \]

   \[
   c:\ A,B\in\mathbb Z,\ A\not\equiv B\pmod2,
   \]

   \[
   v,s:\ A,B\in\mathbb Z+\tfrac12.
   \]

   Dies ist eine exakte **UV-Coset- und Links-Rechts-Restklassenkorrelation**.

2. In der gewählten Produktkategorie \((D_8)_1\times\mathrm{Ising}_R\)
   ist \(J=(c,\psi_R)\) ein fermionischer einfacher Strom der Ordnung zwei.
   Seine sechs monodromielokalen rechten Objekte, ihre Fusion und die drei
   \(J\)-Bahnen sind als algebraischer Kandidat exakt berechnet.

3. Die UV-Gewichte an \(V_c\), einschließlich der Korrektur vom rohen zum
   minimalen Cospinorvertreter, sind exakt.

## Nicht exakt aus dem Gitter abgeleiteter Schritt

Die Zuordnung

\[
(A\bmod2,B\bmod2)
\longmapsto
(1_R,\psi_R;1_L,\psi_L)
\]

nach Integration der massiven Ising-Kopie ist nicht allein durch die
UV-Restklassen bewiesen. Vor der Projektion beschreiben die ganzzahligen
chiral-bosonischen Paritäten den aus **zwei** Majoranas aufgebauten
Dirac-Sektor. Nach der Aufspaltung in eine kritische und eine massive
Majorana-Kopie sind die Paritäten der kritischen rechten und linken
Majorana-Komponenten nicht automatisch unabhängig erhaltene Quantenzahlen.
Massenvorzeichen, Spinstruktur, massive Vakuumwahl und Defektlinienregel
entscheiden, welche Kombinationen als gewöhnliche lokale IR-Operatoren
überleben.

Im Checker wird dieser Schritt nicht hergeleitet. `class_projector` und
`full` werden als feste Mengen eingetragen; der Test
`Gamma_class_projector_six_terms` prüft nur ihre gegenseitige Konsistenz.
`Gamma_neutral_residue_projector` prüft separat die UV-Paritätsreste. Es
gibt keinen Test, der aus den Resten ohne zusätzliche Ising-/Vakuumannahme
die sechs nichtchiralen IR-Terme erzeugt.

## Erforderliche Textkorrekturen

### Abschnitt 3

Die Überschrift sollte etwa lauten:

> **Der von \(\Gamma\) korrelierte UV-Glue und sein bedingter IR-Kandidat**

Den Satz

> „Damit entsteht ohne Kurzvektorzählung der Sektorprojektor …“

durch folgende Aussage ersetzen:

> „Unter der zusätzlichen Standard-Refermionisierungszuordnung und nach
> Wahl des massiven Ising-Vakuums, der Spinstruktur und der lokalen
> Defektlinien ergibt sich daraus der folgende korrelierte
> Sechs-Sektoren-**Kandidat**. Exakt aus \(\Gamma\) folgt bis hierher nur die
> UV-Restklassenkorrelation.“

Den späteren Satz

> „Diese Korrelation ist … der IR-Schatten der tatsächlichen vier
> \(\Gamma/M\)-Klassen“

zu

> „Diese Korrelation ist ein mit den vier \(\Gamma/M\)-Klassen kompatibler
> IR-Kandidat“

abschwächen. `NS diagonal`, `NS antidiagonal` und die beiden
Ramond-Zuordnungen sind nicht als bereits quellenseitig ausgewählter
Projektor zu bezeichnen.

### Abschnitt 4

In der Liste „Exakt sind“ sollten die Punkte 4 und 5 ersetzt werden durch:

4. „die sechs monodromielokalen rechten Objekte und drei \(J\)-Bahnen
   **innerhalb der angesetzten Produktkategorie**“;
5. „die durch \(\Gamma\) erzwungene UV-Korrelation der \(u,v\)-Restklassen.“

Danach sollte ausdrücklich stehen:

> „Nicht exakt hergeleitet ist die Identifikation dieser UV-Reste mit
> unabhängig festgelegten kritischen \(1/\psi/\sigma\)-Sektoren beider
> Chiralitäten nach Entfernung der massiven Ising-Kopie.“

## Unverändertes Gesamtverdikt

Nach diesen Scope-Korrekturen bleibt das substanzielle Resultat bestehen:
\(\Gamma\) liefert mehr als eine Dimensionskoinzidenz, nämlich eine exakte
UV-Gluekorrelation und einen dadurch motivierten, fusionstauglichen
sechsteiligen IR-Kandidaten. Ein vollständiger physikalischer
IR-Spinstrukturprojektor ist weiterhin offen und darf erst nach Auswahl des
massiven Vakuums und der Defekt-/Spinstrukturregeln behauptet werden.
