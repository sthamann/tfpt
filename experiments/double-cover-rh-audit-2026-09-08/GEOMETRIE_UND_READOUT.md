# Geometrische Reflexion, Markierungen und der tatsächliche Boundary-Readout

**Fortsetzung:** [CLOCK_READOUT.md](CLOCK_READOUT.md) konstruiert einen
normierten kombinierten Carrier-/Seam-Readout, der alle vorhandenen Clock-
Sektoren erhält. Der unten bewiesene Verlust beim reinen Boundary-Zugriff
und die Markierungshindernisse bleiben bestehen.

8. September 2026. Fortsetzung von [SEAM_FORTSETZUNG.md](SEAM_FORTSETZUNG.md).
Eigene lokale Forschungsartefakte; keine Statuspromotion, keine Änderung der
untersuchten Quellmodelle. Keine Primzahlen oder Riemann-Nullstellen als Eingabe.

**Ergebnis:** Im vorhandenen 16D-Compiler gibt es eine explizite rationale
Clock-Umkehr, die die Boundary erhält. Eine gleichzeitige Erhaltung der
3+2-Carrier-Markierung ist dagegen exakt unmöglich. Der Boundary-Readout sieht
außerdem keine nichttrivialen C6-Moden. Im QWZ-Modell lässt sich eine räumliche
Clock-Umkehr durch Gegenüberstellung entgegengesetzter Holonomien realisieren;
deren physikalische gemeinsame Darstellung und Identifikation mit dem Compiler
sind dadurch noch nicht gegeben.

Die frühere nichtlokale Matrix war ein Existenzzeuge, kein Lokalitäts-No-go.
Ihre Carrier/Boundary-Mischung ist durch die neue Konstruktion vermeidbar.
Die verbleibende Mischung der beiden Carrier-Blöcke ist unter den folgenden
genauen Voraussetzungen hingegen unvermeidbar.

## 1. Welche Räume und Quellen gemeint sind

Untersucht wird wieder die unveränderte Quellfamilie aus
[`seam_state_derivation_probe.py`](../tfpt-discovery/seam_state_derivation_probe.py):

\[
A=I_8\otimes J,\quad J=\begin{pmatrix}0&1\\-1&0\end{pmatrix},\quad
B=A_{\rm int},\quad H(u,t)=-i(uA+tB).
\]

Die acht Paare zerfallen in drei Carrier-Paare, zwei weitere Carrier-Paare
und drei Boundary-Paare. Die Projektoren heißen hier \(P_3,P_2,P_B\) und
haben die Ränge 6, 4, 6. Die Quell-Clock \(O\) hat Ordnung sechs; sie
permutiert die ersten drei und nächsten zwei Paare und wirkt auf der Boundary
identisch. \(O^2\) stellt in dieser Konstruktion die Familienwirkung dar.

Diese 16 Majorana-Komponenten sind nicht automatisch der interne
Spin(10)-Halbspinor oder eine vollständige physikalische Seam. Insbesondere
wird die fünfteilige Formel \((12Y-I)/5\) nicht ohne Darstellungsabbildung
auf diesen Raum übertragen.

Die QWZ-Matrizen stammen aus
[`v998_seam_modular_closure.py`](../../verification/v998_seam_modular_closure.py).
Andere laufende Arbeiten, etwa
[carrier-module-conjugation](../theory-contracts/carrier-module-conjugation/README.md),
unterscheiden bereits Gitterkonjugation, mikroskopische Teilchen-Loch-Wirkung
und Holonomie. Ihre Resultate werden hier nicht als nachgewiesene Abbildung
auf unsere 16D-Matrizen vorausgesetzt.

## 2. Eine einfache rationale Reflexion ohne Polarzerlegung

Auf dem achtteiligen Paarraum definiere

\[
v=(1,1,1,1,1,0,0,0)^T,\qquad
w=(2,2,2,-3,-3,0,0,0)^T,
\]
\[
P_v=vv^T/5,\qquad P_w=ww^T/30.
\]

\(v\) ist die gleichförmige Carrier-Richtung, an die die gleichförmige
Boundary koppelt. \(w\) ist die dazu orthogonale Richtung im zweidimensionalen
Raum der auf den 3- bzw. 2-Kanal-Blöcken konstanten Vektoren.

Sei \(T\) die Paarpermutation, die das zweite und dritte Carrier-Paar tauscht
und alle anderen Paare fest lässt. Mit \(X=\sigma_x,Z=\sigma_z\) gilt für

\[
\boxed{U=(T-2P_v-P_w/13)\otimes X-(5P_w/13)\otimes Z}
\]

exakt

\[
U^T=U,\quad U^2=I,\quad UAU=-A,\quad UBU=-B,
\]
\[
UOU=O^{-1},\quad [U,P_B]=0,\quad U|_B=I_3\otimes X.
\]

Die Matrix hat ausschließlich rationale Einträge, mit gemeinsamem Nenner 78,
und eine 8+8-Signatur. Sie komplementiert daher für alle endlichen Parameter
und \(\beta>0\) die treue thermische Kovarianz
\(C_\beta=(I+e^{\beta H(u,t)})^{-1}\).

Die Koeffizienten sind aus der Kopplung berechnet, nicht angepasst: In den
normierten Richtungen \(v,w\) ist der verbindende Quellblock

\[
D=-\sqrt6(I+J/5).
\]

Nach Wahl des Boundary-Rahmens \(X\) erzwingt die Kopplung \(U_v=-X\) und

\[
U_w=D^{-1}XD=(12X-5Z)/13.
\]

Das ergibt die obige Formel zusammen mit einer Umkehr der gerichteten
Dreierkanal-Periode. Keine numerische Nullstellensuche oder Polarzerlegung
ist für diesen Zeugen erforderlich.

**Was nicht kanonisch geworden ist:** die Wahl des Boundary-Pauli-Rahmens
und einer der möglichen Dreierreflexionen. Die Lösung ist weder eine bloße
Permutation einzelner Blätter noch ein nachgewiesener physikalischer Deck-
Operator. Sie mischt die beiden unterschiedlich markierten Carrier-Blöcke.

## 3. Warum die gleichzeitige 3+2-Erhaltung ausgeschlossen ist

Die gerichtete Dreierkopplung der drei markierten Bereiche liefert exakt

\[
\operatorname{Tr}(P_3BP_2BP_BB)=-36,
\]
\[
\boxed{\operatorname{Tr}(P_3HP_2HP_BH)=-36it^3.}
\]

Angenommen, ein invertierbarer komplex-linearer Operator \(V\) erhält alle
drei Projektoren und erfüllt \(VHV^{-1}=-H\). Spurkonjugation würde den
angegebenen Ausdruck erhalten. Die drei Faktoren \(H\) würden ihn zugleich
ins Negative überführen. Für \(t\ne0\) ist das ein Widerspruch.

Der Ausschluss benötigt weder Orthogonalität noch eine bestimmte
Parametrisierung von \(V\), keine Clock-Bedingung und keine einzelne
Temperaturwahl. Er gilt sogar für einen nur für diesen festen gekoppelten
Hamiltonian gesuchten invertierbaren linearen Operator.

**Bedingte Konsequenz für TFPT:** Wenn der gesuchte Blattwechsel in dieser
Darstellung sowohl die Boundary als auch die beiden Carrier-Markierungen
einzeln erhalten soll, kann genau diese gekoppelte Quellfamilie ihn nicht
realisieren. Das ist kein Ausschluss anderer TFPT-Darstellungen oder
antiunitärer Wirkungen.

Zusätzlich gilt

\[
\operatorname{Tr}(O^2H)=-6it.
\]

Daher kann bei \(t\ne0\) auch kein linearer Vorzeichenwechsler mit der
konkreten Familienwirkung \(O^2\) kommutieren. Unsere Lösung kehrt diese
Wirkung um: \(UO^2U=O^{-2}\). Ein vorgeschlagener Intertwiner zu einer
anderen Konstruktion, deren Involution die Familienwirkung erhält, muss
diesen Unterschied ausdrücklich auflösen. Auf dem Familienfixraum kann
er verschwinden; auf der vollständigen Darstellung nicht.

Eine ergänzende lineare Zählung ergibt 14 reell symmetrische Lösungsrichtungen
bei Boundary-Erhaltung und nur 12 bei Erhaltung aller drei Markierungen.
Die zweite Zahl bedeutet nicht zwölf invertierbare Reflexionen: Der
Spurwiderspruch zeigt, dass dort jeder Lösungskandidat singulär sein muss.

Werden die drei verbindenden Kantenfamilien unabhängig gewichtet, gibt es
ebenfalls keinen gemeinsamen linearen Vorzeichenwechsler für alle Gewichte:
Die Spur des geordneten Produkts der drei einzelnen Kantenmatrizen ist −36.
Dieser Kontrollfall erhält C6 und CAR, ist aber nicht als unter sämtlichen
TFPT-Einheitsregeln erlaubte Variation ausgewiesen.

## 4. Der Boundary-Readout sieht die nichttriviale Clock nicht

Es gilt schon auf der Quelle

\[
OP_B=P_B,\qquad [O,H]=0.
\]

Mit \(\Pi_0=\frac16\sum_{k=0}^5O^k\) folgt deshalb für den gesamten von der
Boundary erreichbaren Raum

\[
\operatorname{span}\{H^n\operatorname{im}P_B:n\ge0\}
\subseteq\operatorname{im}\Pi_0.
\]

Für die Kopplungsmatrix \(B\) wird dieser Raum exakt erreicht: Die Matrix
aus den Boundary-Spalten von \(I,B,\ldots,B^4\) hat Rang 10, ebenso
\(\Pi_0\). Die verbleibenden **sechs nichttrivialen C6-Moden sind für diesen
Boundary-Zugriff unsichtbar**. Das gilt nicht nur für eine numerische
Temperatur: Resolventen und Funktionen von \(H\) bleiben in denselben
invarianten Sektoren.

Die zehn zugänglichen Dimensionen zerfallen weiter:

- Vier Boundary-Dimensionen sind orthogonal zur gleichförmigen Boundary-
  Richtung und erfüllen \(B\psi=0\); sie tragen nur den nackten \(uA\)-Anteil.
- Die beiden gleichförmigen Boundary-Komponenten erzeugen mit \(B\) einen
  sechsdimensionalen gekoppelten Raum. Auch dort ist \(O=I\).

In einer rationalen, nicht orthonormalen Gruppenbasis dieses aktiven Raums
lautet die Gram-Matrix \(\operatorname{diag}(3,2,3)\otimes I_2\). Seine
sechs Hamilton-Eigenwerte sind

\[
\pm(u+t\lambda_j),\qquad j=1,2,3,
\]

wobei die drei reellen \(\lambda_j\) die festen Wurzeln von

\[
\boxed{\lambda^3-\lambda^2-21\lambda+9=0}
\]

sind. Der separate Prüfer bestätigt das Polynom direkt auf den ursprünglichen
16D-Matrizen. Es handelt sich um eine feste endliche Spektralfamilie. Der
Logarithmus einer komprimierten Kovarianz kann dennoch nichtlinear von den
Parametern abhängen; die affine Formel gilt für das volle aktive \(H\).

**Bedeutung:** Die C6-Struktur wird durch diesen Zugriff nicht in den
Boundary-Readout übertragen. Sie ist außerdem nicht ohne weitere Herleitung
eine arithmetische Skalenwirkung. Ein Primzahl- oder RH-Mechanismus folgt aus
der erhaltenen Zweirand-Symmetrie nicht.

## 5. Gleiche Reflexion bedeutet noch nicht gleicher Zustand

Auf der aktiven zweidimensionalen Compiler-Boundary wirkt \(X\), auf dem
QWZ-Zweirand-Unterraum aus der vorigen Rechnung wirkt \(Y\). Ein expliziter
unitärer Symmetrie-Intertwiner existiert trivial:

\[
Q=\operatorname{diag}(1,i),\qquad YQ=QX.
\]

Dieser Gleichlauf identifiziert aber nicht die Kovarianzen. Bei
\(u=1,t=1/8,\beta=1\) hat die aktive Compiler-Boundary die Besetzungswerte

\[
(0.27926838698813855,\ 0.7207316130118613).
\]

Die QWZ-Randanker bei \(p=0,M=1\) sind exakte Nullmoden und besitzen bei
jeder endlichen Temperatur die Kovarianz \(I_2/2\). Ihre Besetzungswerte
sind also \((1/2,1/2)\). Keine unitäre Matrix kann diese beiden Zustände
am angegebenen Vergleichspunkt identifizieren. Das ist ein konkreter
Gegencheck gegen ein bloßes Zusammenlegen der Symmetriedaten, kein Ausschluss
aller möglichen Parameterabbildungen zwischen den Modellen.

## 6. Eine passende räumliche Clock-Umkehr auf der QWZ-Seite

Die frühere Querreflexion ließ die Längsclock unverändert. Wählt man
stattdessen

\[
V_x=R_x\otimes I_y\otimes\sigma_x,
\]

also eine Umkehr der Längspositionen, liefert der vorhandene Quellkonstruktor

\[
\boxed{V_xH_\alpha V_x^{-1}=-H_{-\alpha}.}
\]

Hier ist \(e^{2\pi i\alpha}\) die Seam-Holonomie. Die lokalen Beweise sind
\(XZX=-Z\), \(XT_x^\dagger X=-T_x\), \(XT_yX=-T_y\); die Ortsreflexion
kehrt die gerichtete Seam-Kante und damit ihre Phase um.

Bei \(\alpha=0\) oder \(1/2\) schließt diese konkrete Reflexion innerhalb
desselben Sektors. Bei \(\alpha=1/4\) oder \(3/4\) vertauscht sie dagegen
zwei unterschiedliche Quellsektoren. Der Nachweis ist allgemein lokal;
zusätzlich wurden zwölf vollständige endliche Zylinder geprüft.

Auf der **explizit hinzugefügten** direkten Summe

\[
\mathcal H_{\rm dbl}=\mathcal H_\alpha\oplus\mathcal H_{-\alpha},\qquad
H_{\rm dbl}=\operatorname{diag}(H_\alpha,H_{-\alpha})
\]

definiert

\[
U_{\rm dbl}=\begin{pmatrix}0&V_x\\V_x&0\end{pmatrix}
\]

eine unitäre Involution mit

\[
U_{\rm dbl}H_{\rm dbl}U_{\rm dbl}^{-1}=-H_{\rm dbl},\qquad
U_{\rm dbl}T_{\rm dbl}U_{\rm dbl}^{-1}=T_{\rm dbl}^{-1}.
\]

Das ist eine konkrete endliche Geometrie mit Sektorwechsel, modularer
Komplementierung und umgekehrter Translationsrichtung. Die gegenüberstehenden
Holonomien stammen aus der vorhandenen Quellfamilie; der gemeinsame
physikalische Zustandsraum, seine Auswahl und seine Identifikation mit dem
TFPT-Double-Cover wurden dadurch nicht hergeleitet.

Auch die Clock ist sorgfältig zu typisieren:
\(T_\alpha^{N_x}=e^{2\pi i\alpha}I\). Sie ist ohne weitere Abbildung nicht
die Compiler-Clock mit \(O^6=I\). Eine Sektorphase abzuziehen oder eine
andere Clock zu deklarieren wäre ein zusätzlicher Darstellungsentscheid.

## 7. Entscheidung für TFPT, RH und Faktorisierung

Die Untersuchung der bloßen Existenz endlicher Reflexionen ist jetzt deutlich
weiter: Ein rationaler Boundary-erhaltender Compiler-Zeuge und eine räumliche
QWZ-Clock-Umkehr sind explizit vorhanden. Weitere beliebige ähnliche Matrizen
würden den wesentlichen Übergang nicht schließen.

Der nächste belastbare Vertrag muss **eine gemeinsame Darstellung** angeben,
die gleichzeitig Markierungen, Familienwirkung/Clock, Kovarianz und
Holonomiesektoren transportiert. Für die naheliegende Forderung, die drei
Markierungen und die Familienwirkung unverändert zu erhalten, liegen bereits
exakte Gegenargumente vor. Diese Forderung unverändert erneut zu testen wäre
keine offene Forschungsaufgabe mehr.

Eine alternative Darstellung darf diese Hindernisse nur durch eine aus der
Quelle begründete andere Wirkung auf die Markierungen/Familie oder durch
eine sauber typisierte antiunitäre bzw. vergrößerte Konstruktion umgehen.
Ein nachträgliches Angleichen von Spektren oder Umbenennen von Clock-Moden
liefert diese Begründung nicht. Der Boundary-Fixraumverlust muss dabei
ebenfalls adressiert werden, falls nichttriviale Clock-Daten relevant sein sollen.

Für RH bleibt zusätzlich die gesamte arithmetische Identifikation offen:
kompatibler unendlicher Skalenraum, Maß, vollständige Spurformel einschließlich
aller Stellen und globale Positivität. Die neue Verdopplung liefert keinen
Euler-Produkt-Mechanismus und keine Primzahlpotenz-Gewichte.

Für Faktorisierung entsteht kein neuer Algorithmus. Die Zylindergröße
\(N_x\) ist hier ein geometrischer Regulator, kein nachgewiesener
Eingang einer zu faktorisierenden Zahl mit faktortragendem Readout. Die
Kosten- und Erfolgspflichten des bisherigen Faktorisierungszweigs werden
durch diese endlichen Symmetrien nicht verändert.

## 8. Reproduktion und unabhängige Gegenprüfung

```sh
experiments/tfpt-discovery/.venv/bin/python experiments/double-cover-rh-audit-2026-09-08/seam_geometry_probe.py
experiments/tfpt-discovery/.venv/bin/python experiments/double-cover-rh-audit-2026-09-08/check_geometry_certificate.py
```

- [Hauptprobe](seam_geometry_probe.py): **31/31 Prüfungen bestanden**;
  exakte rationale Reflexion, zwei Spurhindernisse, beobachtbarer Unterraum,
  festes kubisches Polynom, Zustandsvergleich und QWZ-Sektorwechsel.
  [Protokoll](seam_geometry.log), [Daten und Quellhashes](seam_geometry_results.json).
- [Separater Zertifikatsprüfer](check_geometry_certificate.py): prüft die
  gespeicherte Matrix ohne ihre Konstruktionsformel oder Nullraumsuche,
  das kubische Polynom auf den Rohmatrizen und einen unabhängig durch lokale
  Kanten zusammengesetzten symbolischen QWZ-Zylinder mit freier Seam-Phase.
  [Protokoll](geometry_certificate.log).
- Gemeinsame Abhängigkeit ist der Extraktor der unveränderten 16D-Quelle.
  Die Gegenprüfung ist keine zweite unabhängige Herleitung dieser Quelle.
- Ein struktureller SymPy-Vergleich im Zertifikatsprüfer benötigte zunächst
  algebraische Expansion komplexer Ausdrücke; danach verschwand der scheinbare
  Rest exakt. Keine Änderung der mathematischen Aussage oder der Quellmatrizen.

Die allgemeinen endlichen Aussagen folgen aus den angegebenen Identitäten.
Die Stichproben dienen der Überprüfung der tatsächlichen Quellimplementierung.
Ein physikalischer Kontinuumsgrenzwert, RH oder ein Faktorisierungsvorteil
wurden in dieser Untersuchung nicht bewiesen oder gemessen.
