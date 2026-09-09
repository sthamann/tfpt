# Der Readout als vollständiger Träger der Kopplungsantwort

8. September 2026. Fortsetzung von [CLOCK_READOUT.md](CLOCK_READOUT.md).
Exakte Untersuchung derselben endlichen Quellfamilie; keine Statuspromotion.

**Der zwölfdimensionale Raum ist exakt \(\operatorname{im}B\), der Träger
der vorhandenen Kopplungsmatrix. Sein Projektor lässt sich allein aus \(B\)
rekonstruieren. Bei endlicher positiver Temperatur ist er zugleich der
Träger der Zustandsänderung bei Variation der Kopplungsstärke.**

Damit ist die Auswahl dieses endlichen Interaktionssektors stärker begründet
als zuvor. Nicht geschlossen ist die Frage, ob die tatsächliche physikalische
Seam diese Kandidatenkopplung realisiert oder ob alle wechselwirkungsfreien
Komponenten für sämtliche physikalischen Fragen verworfen werden dürfen.

## 1. Quellenstatus

Die unveränderte Familie ist
\[
H(u,t)=-i(uA+tB),\qquad A=I_8\otimes J,\quad B=A_{\rm int}.
\]

Sie stammt aus
[seam_state_derivation_probe.py](../tfpt-discovery/seam_state_derivation_probe.py).
Die Ausgangsarbeit
[v898_kms_schur_mixing.py](../../verification/v898_kms_schur_mixing.py)
bezeichnet diese Zustände ausdrücklich als Kandidaten und die Realisierung
durch die tatsächliche Seam als offene Prämisse. Die Rechnungen hier ändern
diesen Quellenstatus nicht.

Gefragt war, ob der vorige Readout nur durch die zusätzliche Forderung
„alle Carrier-Komponenten beobachten“ ausgewählt war. Der neue Befund
liefert eine unmittelbar auf die Kopplung bezogene Charakterisierung.

## 2. Der Projektor wird von B bestimmt

Exakt gilt
\[
\operatorname{rank}B=12,\qquad \dim\ker B=4.
\]

Der Kern besteht ausschließlich aus Boundary-Vektoren, deren Summe über
die drei Boundary-Paare komponentenweise null ist. Er enthält keine
Carrier-Richtung. Da \(B\) reell antisymmetrisch ist, ist sein Bild das
orthogonale Komplement seines Kerns. Für den bereits konstruierten Readout gilt
\[
\boxed{P=\operatorname{proj}_{\operatorname{im}B}=WW^T.}
\]

Eine vollständige algebraische Formel benötigt weder Clock, Reflexion
noch einen vorgegebenen Carrier-Projektor. Mit
\[
p(x)=(x+1)(x+3)(x^3+43x^2+459x+81)
\]
lautet sie
\[
\boxed{P=I-\frac{p(B^2)}{243}}
=-\frac{B^{10}+47B^8+634B^6+2046B^4+1701B^2}{243}.
\]

Die Identitäten \(P^T=P\), \(P^2=P\), \(PB=BP=B\) und Rang zwölf sind
exakt geprüft. Der separate Verifier konstruiert denselben Projektor
unabhängig von dieser Formel aus dem rationalen Nullraum von \(B\).

Die Auswahl ist eindeutig unter folgender Vollständigkeitsforderung:
Gesucht ist ein orthogonaler Projektor \(Q\) mit \(B=QBQ\), und die
Einschränkung von \(B\) auf \(\operatorname{im}Q\) soll keinen Kern haben.
Die erste Bedingung enthält alle Kopplungsrichtungen, die zweite entfernt
alle kopplungsblinden Richtungen. Zusammen erzwingen sie \(Q=P\).

Jeder Operator, der \(B\) ins Negative überführt, erhält automatisch \(P\),
weil \(P\) ein Polynom in \(B^2\) ist. Der Readout wurde somit nicht auf den
zuvor gefundenen Reflexionszeugen zugeschnitten.

## 3. Operative Charakterisierung durch die Kopplungsantwort

Setze
\[
C_\beta(u,t)=(I+e^{\beta H(u,t)})^{-1},\qquad
\Delta C=C_\beta(u,t)-C_\beta(u,0).
\]

Für jedes endliche \(\beta>0\), jedes reelle \(u\) und jedes \(t\ne0\) gilt
\[
\boxed{\operatorname{supp}(\Delta C)=P.}
\]

Beweis: \(A\) und \(B\) kommutieren und sind normal. In einer gemeinsamen
Eigenbasis ändert die Kopplung die Energie genau dort, wo der Eigenwert
von \(B\) ungleich null ist. Die Fermi-Funktion ist bei endlichem positivem
\(\beta\) streng monoton. Die Kovarianzdifferenz verschwindet deshalb
genau auf \(\ker B\).

An der ungekoppelten Achse ist die Antwort besonders einfach:
\[
\boxed{\left.\frac{\partial C_\beta(u,t)}{\partial t}\right|_{t=0}
=\frac{i\beta}{4\cosh^2(\beta u/2)}B.}
\]

Damit kann der Träger aus der linearen Antwort auf eine Kopplungsvariation
bestimmt werden. Für \(u=1,\beta=1\) ist der Vorfaktor vor \(iB\) etwa
0,196612. Sechs endliche Zustandsvergleiche und zentrale Differenzen mit
halbierter Schrittweite bestätigen diese allgemeinen Identitäten numerisch.

„Operativ“ bezeichnet die Antwort des expliziten Quellmodells. Ein
physikalischer Eingriff zur Variation von \(t\), die Realisierung des
KMS-Zustands und eine Messgenauigkeit wurden nicht nachgewiesen. Bei sehr
niedriger Temperatur können nichtverschwindende Antworten beliebig klein werden.

## 4. Zwei unterschiedliche Carrier-Zugriffe reichen aus

Die folgende Tabelle beschreibt den exakten Abschluss verschiedener
Startports unter \(A,B,O,O^{-1}\). Jeder angegebene Startport enthält beide
Majorana-Komponenten des jeweiligen Paares.

| Startzugriff | Erzeugte Dimension | Davon Clock-Fixraum |
|---|---:|---:|
| Gleichförmiges Boundary-Paar | 6 | 6 |
| Ein Carrier-Paar aus dem Dreierumlauf | 10 | 6 |
| Ein Carrier-Paar aus dem Zweierumlauf | 8 | 6 |
| Ein Paar aus jedem der beiden Carrier-Umläufe | **12** | 6 |
| Alle fünf Carrier-Paare | **12** | 6 |
| Vollständige alte Boundary | 10 | 10 |

Für die zwei Paare aus verschiedenen Umläufen bestätigt der separate
Verifier sogar, dass bereits ihre Bilder unter \(I,B,\ldots,B^5\) den
gesamten Interaktionssektor erzeugen. Nicht jeder Carrier-Kanal muss also
als unabhängiger Eingang vorgegeben werden. Eine physikalische Operation,
die diesen Zugriff liefert, ist damit noch nicht bestimmt.

Clock und Reflexion allein reichen weiterhin nicht als Auswahlprinzip:
\[
P=P\Pi_0+P(I-\Pi_0),\qquad
\Pi_0=\tfrac16\sum_{k=0}^5O^k.
\]
Beide Summanden haben Rang sechs und erhalten die Reflexion. Der zweite
enthält die nichttrivialen Clock-Sektoren, liegt vollständig im Carrier und
trägt bereits eine Clock von Ordnung sechs. Clock-Treue allein erzwingt
deshalb nicht den vollständigen Interaktionsreadout.

## 5. Zwei Grenzen der Auswahl

**Der volle Hamiltonian hat mehr Träger als die Kopplung.** Am Punkt
\(u=1,t=1/8\) hat \(H\) Rang 16. Die vier verworfenen Komponenten tragen
den nackten \(uA\)-Anteil und können physikalische Energie besitzen.
\(P\) ist somit der vollständige Interaktionssektor, nicht der bewiesene
Träger aller relevanten Physik. Seine Auswahl muss zur Fragestellung passen.

**Im Grundzustand kann die Kopplungsantwort verschwinden.** Für \(u=1\)
liegt der erste positive Nulldurchgang eines Energieniveaus bei
\[
t_{\rm gap}\approx0.230948870833,\qquad
1+t_{\rm gap}-21t_{\rm gap}^2-9t_{\rm gap}^3=0.
\]
Die positive Nullstelle ist exakt im Intervall \((0.23,0.24)\) isoliert.
Für \(0<t<t_{\rm gap}\) stimmen alle Energievorzeichen mit dem
ungekoppelten Zustand überein; wegen der gemeinsamen Eigenbasis bleibt
sein Grundzustandsprojektor unverändert. Direkte Prüfungen bei \(t=1/8\)
und \(t=0.2\) bestätigen dies. Bei \(t=0.3\) ändert er sich.

Die Antwortaussage darf daher nicht auf den Nulltemperaturgrenzwert
übertragen werden. Bei \(\beta=0\) ist \(C=I/2\) ebenfalls konstant.
Sie gilt genau bei endlichem \(\beta>0\) und \(t\ne0\). An \(t=0\) selbst
ist die Richtung \(B\) nur über die Familie oder deren Ableitung gegeben.

## 6. Bedeutung für TFPT, RH und Faktorisierung

Die frühere zusätzliche Auswahl „alle Carrier-Komponenten behalten“ ist
für die Definition dieses Raums nicht mehr nötig. Derselbe Raum ist der
eindeutige vollständige Sektor ohne Kopplungsnullmoden und besitzt eine
Charakterisierung durch seine thermische Antwort. Das ist ein gemeinsamer
Satz über die vorhandenen Quellmatrizen.

Offen bleibt auf der physikalischen Seite die Realisierung der konkreten
Kandidatenfamilie \(B,C_\beta\) und des zugehörigen Zugriffs. Weitere
isolierte Forderungen nach Selbstadjungiertheit, Clock-Treue oder einer
Involution liefern diese Realisierung nicht. Die bereits bewiesenen
Markierungs- und Familienhindernisse gelten weiter.

Für RH entsteht dadurch weder eine unendliche arithmetische Darstellung
noch die Identifikation mit der Weil-Form oder ein Euler-Produkt. Der
Fortschritt betrifft die Auswahl und Beobachtbarkeit des endlichen
Interaktionssektors. Für Faktorisierung fehlt weiterhin ein effizienter
Mechanismus, der eine eingegebene Zahl in faktortragende Daten überführt.

## 7. Reproduktion

    experiments/tfpt-discovery/.venv/bin/python experiments/double-cover-rh-audit-2026-09-08/interaction_support_probe.py
    experiments/tfpt-discovery/.venv/bin/python experiments/double-cover-rh-audit-2026-09-08/check_support_certificate.py

- [Hauptprobe](interaction_support_probe.py): **24/24 Prüfungen bestanden**.
  [Protokoll](interaction_support.log), [Daten und Quellhashes](interaction_support_results.json).
- [Separater Verifier](check_support_certificate.py): Projektor aus dem
  Nullraum, Gleichheit mit dem vorigen Readout, algebraischer Vorfaktor der
  linearen Antwort, Zweikanal-Zugriff und exaktes Nullstellenintervall.
  [Protokoll](support_certificate.log).
- Beide Prüfer teilen den Extraktor der Originalquelle. Sie sind keine
  unabhängigen Herleitungen dieser Quelle; die allgemeinen endlichen
  Aussagen folgen aus den angegebenen algebraischen Argumenten.

