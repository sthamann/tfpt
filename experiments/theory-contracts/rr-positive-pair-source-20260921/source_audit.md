# Quellen-Audit des positiven RR/W-Lifts

## Entscheid

Der neue Operator

\[
H_+=2\kappa\sum_{A=1}^{60}
\left(b_A+\frac{P_A}{\sqrt8}\right)^\dagger
\left(b_A+\frac{P_A}{\sqrt8}\right)
\]

ist ein mathematisch gültiger positiver Kandidat. Auf jedem hellen
Einpaar-/Einbosonraum reproduziert er exakt den aktiven RR-Block

\[
\kappa\begin{pmatrix}2&2\\2&2\end{pmatrix}.
\]

Eine Herleitung aus der bisher vorliegenden ursprünglichen RR-Quelle liegt in
den geprüften Quellen nicht vor.
Der belastbare Status lautet:

* **exakt bedingt:** aktive `Q=2`-Zustandsisometrie und zugehörige Zeit;
* **widerlegt:** Interpretation als kanonische unitäre Operatoridentifikation
  `b_A <-> P_A/sqrt(8)` auf dem vollen Fockraum;
* **widerlegt:** Interpretation als zeitgetreuer Lift der vollständigen
  fünfdimensionalen RR-Wirkung in den angegebenen `Q=2`-Raum;
* **offen:** eine schwächere, quellenabgeleitete Kompression, welche den
  aktiven RR-Block auswählt, 60 Kanäle erzeugt und Zustand, Ladung,
  Reflexion und Zeit gemeinsam transportiert.

Die aktive RR-Ebene selbst ist in der markierten D4-Darstellung algebraisch
kanonisch ausgewählt. Die erste zusätzlich gewählte **physische** Struktur ist
die Entscheidung, nur diese Kompression als Quellenfeld zu verwenden, sowie
die Abbildung

\[
(\text{konstante RR-Linie},\text{uniforme Residuenlinie})
\longmapsto
(P_A/\sqrt8,b_A)
\]

zusammen mit ihrer 60-fachen Replikation. Erst **innerhalb** dieser gewählten
Feldabbildung erzwingt die positive RR-Form den elastischen Term.

## 1. Was die ursprüngliche RR-Rechnung tatsächlich liefert

Der ursprüngliche RR-Raum ist

\[
E=H^0(\mathbb P^1,\mathcal O(\mu_4)),\qquad \dim E=5.
\]

Mit der erklärten Hardy-Metrik und dem erklärten kontinuierlichen Logarithmus
hat sein Generator das Spektrum

\[
\operatorname{spec}h_{\rm geom}=\{0,1,2,3,4\}.
\]

In der D4-angepassten orthonormalen Basis zerfällt er in

\[
h_{\rm geom}=
\begin{pmatrix}2&2\\2&2\end{pmatrix}
\oplus (1)\oplus(2)\oplus(3).
\]

Der erste Block wirkt auf der konstanten Quellenlinie und der uniformen
Residuenlinie. Die drei übrigen Richtungen sind das dunkle
Augmentationstripel. Sie sind kontinuierlich invariant und bleiben Teil der
ursprünglichen fünfdimensionalen Zeit.

Die D4-Wirkung enthält mehr als den hellen Block:

* auf der hellen Ebene ist `R=I`; die konstante Linie ist `S`-gerade und die
  uniforme Residuenlinie `S`-ungerade;
* auf dem dunklen Tripel liegen die Drehungscharaktere `i,-1,-i`;
* auf ganz `E` gilt die affine Reflexion

\[
S h_{\rm geom}S=4I-h_{\rm geom}.
\]

Die aktive Ebene ist dabei kein beliebig gewählter Zweiraum. Setze

\[
P_{\rm act}=\frac14(I+R+R^2+R^3).
\]

Da `R` bezüglich jeder D4-invarianten positiven Metrik unitär ist, ist dieses
Gruppenmittel der orthogonale Projektor auf den `R`-Fixraum. Für die
vorliegende Darstellung

\[
R=\operatorname{diag}(1,i,-1,-i,1)
\]

gilt daher

\[
\operatorname{Ran}P_{\rm act}=\operatorname{span}\{e_0,e_4\},
\]

also genau die von konstanter Linie und uniformer Residuenlinie aufgespannte
aktive Ebene. Ferner folgt aus `SRS=R^{-1}` die Identität
`SP_actS=P_act`; der Projektor ist somit D4-äquivariant. Für den tatsächlich
verwendeten Generator, der die `R`-Eigenräume erhält, gilt außerdem

\[
[P_{\rm act},h_{\rm geom}]=0.
\]

Damit ist die **algebraische Auswahl der aktiven Ebene** aus der markierten
D4-Wirkung kanonisch. Nicht hergeleitet ist die stärkere physische Aussage,
dass gerade die Quellenfelder dieses projizierten Zweiraums allein den
Zielprozess erzeugen und das dunkle Tripel nicht als physische Zeitmoden
mitgeführt wird.

Schon der RR-Contract markiert seine physische Reichweite: Die Hardy-Metrik
und dieser Logarithmus sind erklärte Einbettungsdaten. P1/P2 wählen sie bisher
nicht. Die Residuenrechnung liefert außerdem ausdrücklich noch keine lokale
CAR/CCR-Feldabbildung.

## 2. Der aktive Zweiraum wird korrekt realisiert

Aus

\[
WW^\dagger=8I_{60}
\]

folgen die orthonormalen hellen Paarzustände

\[
|p_A\rangle=\frac{P_A^\dagger|0\rangle}{\sqrt8},
\qquad
\langle p_A|p_B\rangle=\delta_{AB}.
\]

Zusammen mit `|b_A>=b_A^dagger|0>` bilden sie 60 orthogonale Zweiräume. Für
den vorgeschlagenen `H_+` gilt dort exakt

\[
H_+\big|_{\operatorname{span}\{|p_A\rangle,|b_A\rangle\}}
=\kappa\begin{pmatrix}2&2\\2&2\end{pmatrix}.
\]

Damit existiert eine Isometrie der **aktiven Zustandsräume** und ein exakter
Intertwiner ihrer eingeschränkten Zeitentwicklung. Der Austausch bei
`t=pi/(4 kappa)` ist in diesem Scope korrekt.

Auch die Fockladung

\[
Q=N_f+2N_b
\]

passt auf dieser Ebene: Ein Boson und zwei Fermionen besitzen beide `Q=2`,
und sowohl `b_A` als auch `P_A` senken `Q` um zwei. Dies beweist eine
Gradverträglichkeit des Kandidaten, nicht seine Herkunft aus der Quelle.

Wegen der Symmetrie des hellen `2 x 2`-Blocks entscheidet diese Rechnung
außerdem nicht, welche der beiden RR-Linien als `P_A` und welche als `b_A`
zu lesen ist. Diese Feldbedeutung wird zusätzlich eingesetzt.

## 3. Der Spektraltest begrenzt die Deutung als vollständige RR-Zeit

Im gesamten `Q=2`-Raum zerfällt der Zweifermionraum als

\[
\Lambda^2\mathbb C^{64}
=\operatorname{Ran}W^\dagger\oplus\ker W,
\]

mit Dimensionen `60` und `1956`. Auf jedem der 60 hellen Paar-/Bosonblöcke
hat `H_+` die Eigenwerte `0` und `4 kappa`; auf `ker W` verschwindet er.
Somit

\[
\boxed{
\operatorname{spec}(H_+|_{Q=2})
=0^{2016}\oplus(4\kappa)^{60}.
}
\]

Ein 60-fach replizierter vollständiger RR-Raum hätte dagegen

\[
\operatorname{spec}(\kappa h_{\rm geom}\otimes I_{60})
=0^{60}\oplus\kappa^{60}\oplus(2\kappa)^{60}
\oplus(3\kappa)^{60}\oplus(4\kappa)^{60}.
\]

Die Eigenwerte `kappa,2 kappa,3 kappa` fehlen im Zieloperator. Daher existiert
keine Isometrie

\[
J:E\otimes\mathbb C^{60}\longrightarrow\mathcal H_{Q=2}
\]

mit

\[
J(\kappa h_{\rm geom}\otimes I_{60})
=(H_+|_{Q=2})J.
\]

Dieser Spektraltest ist bereits entscheidend. Die drei dunklen RR-Richtungen
können nicht als weitere Zustände im vorhandenen `Q=2`-Nullraum etikettiert
werden: Ein Zustandsintertwiner muss ihre Energien `kappa,2kappa,3kappa`
erhalten, nicht nur genügend Vektordimension bereitstellen.

Als **physischer Zeitgenerator auf diesem `Q=2`-Zielraum** realisiert der
positive Kandidat damit nur die Kompression auf den aktiven RR-Block. Der
Test widerlegt weder eine Darstellung der vollständigen RR-Wirkung durch
einen separaten inneren Generator noch deren Kommutation mit `H_+`.

## 4. Die vorhandene funktorielle RR/W-Brücke ist ein anderer Operator

Die früher bewiesene vollständige RR/W-Abbildung transportiert den
fünfdimensionalen Generator über die tatsächlichen Darstellungen:

\[
h_F=d\Gamma_{\rm even}(h_E)\otimes I_4,
\]

\[
h_B=\left(10I_{10}+\operatorname{diag}(h_E,-h_E^T)\right)\otimes I_6,
\]

\[
W\,d\Gamma_2(h_F)=h_BW.
\]

Der daraus folgende Fockoperator

\[
K_{RR}=f^\dagger h_Ff+b^\dagger h_Bb
\]

ist ein erhaltener innerer Generator. Er ist besetzungszahlkonservierend und
kommutiert mit der nativen W-Wechselwirkung. Der frühere Quellen-Audit hat
ausdrücklich entschieden, dass `K_RR` nicht die Hamiltonzeit `H_W` ist.

Dieselbe Tensoridentität zeigt auch die Verträglichkeit mit dem neuen
positiven Kandidaten. Schreibe

\[
X=\sum_A b_A^\dagger P_A,
\qquad
D=\sum_A P_A^\dagger P_A.
\]

Aus

\[
W\,d\Gamma_2(h_F)=h_BW
\]

folgt, dass der Paarvektor `P` unter `K_RR` in derselben Darstellung wie der
Bosonvektor `b` transformiert. Daher sind seine Hermiteschen Kontraktionen
und die Paar-Boson-Kontraktion invariant:

\[
[K_{RR},N_b]=0,
\qquad [K_{RR},D]=0,
\qquad [K_{RR},X]=0.
\]

Mit

\[
H_+=2\kappa N_b+\frac{\kappa}{\sqrt2}(X+X^\dagger)
 +\frac\kappa4D
\]

ergibt sich auf dem gemeinsamen endlichen Teilchenkern

\[
\boxed{[K_{RR},H_+]=0.}
\]

`H_+` kann somit die vollständige RR-Wirkung als **innere Symmetrie** tragen,
obwohl sein eigenes `Q=2`-Spektrum nicht die vollständige RR-Zeit realisiert.
Diese beiden Rollen sind strikt zu unterscheiden.

Dies ist die gegenwärtig belegte funktorielle Fortsetzung der **vollen**
RR-Wirkung. Sie ist nicht gleichbedeutend mit 60 identischen Kopien des
hellen `2 x 2`-Blocks. Insbesondere besitzt `h_B` die dokumentierten
Einteilchenwerte `6,...,14`, nicht nur `0,4`.

Der neue `H_+` ergänzt diese Darstellung durch einen anderen dynamischen
Vertrag: `h_active tensor I_60` wird direkt auf zusammengesetzte Paar- und
Bosonoperatoren ausgewertet, während `K_RR` als kommutierende innere
RR-Wirkung bestehen bleibt. Dass beide Konstruktionen denselben hellen
Zweierblock berühren, identifiziert ihre vollständigen Generatoren nicht.

## 5. Warum kein kanonischer Operator-Swap vorliegt

Setze

\[
a_A=P_A/\sqrt8.
\]

Auf Zuständen des hellen `Q=2`-Raums verhält sich `a_A^dagger|0>` wie ein
normierter Einteilchenzustand. Als Operator erfüllt `a_A` jedoch keine CCR.
Für einen unterstützten Kanal gilt beispielsweise

\[
[a_A,a_A^\dagger]|0\rangle=|0\rangle,
\]

während auf dem vollständig besetzten Fermionzustand

\[
[a_A,a_A^\dagger]|F\rangle=-|F\rangle.
\]

Dagegen gilt global

\[
[b_A,b_A^\dagger]=I.
\]

Eine unitär implementierte *-Automorphie erhält Kommutatoren. Deshalb kann
kein globales unitäres `U` die kanonische Operatoridentifikation

\[
U b_AU^\dagger=a_A
\]

realisieren. Dass `H_+` die Zustände `|p_A>` und `|b_A>` zu einer bestimmten
Zeit austauscht, ist eine gültige Zweizustandsdynamik; es ist kein Austausch
der vollständigen Feldoperatoren.

Die zusammengesetzten Operatoren

\[
B_A=b_A+a_A
\]

sind aus demselben Grund keine freien Bosonen. Die Positivität
`H_+=2kappa sum B_A^dagger B_A` repariert diese Algebra nicht und muss sie
auch nicht reparieren, solange `H_+` nur als wechselwirkender Kandidat gelesen
wird.

## 6. Der elastische Term ist bedingt erzwungen, nicht ursprünglich abgeleitet

Innerhalb der zusätzlich gewählten Operatorabbildung

\[
y_A=\begin{pmatrix}P_A/\sqrt8\\b_A\end{pmatrix}
\]

ist die Auswertung derselben positiven RR-Form eindeutig:

\[
\kappa\sum_A y_A^\dagger
\begin{pmatrix}2&2\\2&2\end{pmatrix}y_A
=2\kappa N_b+\frac{\kappa}{\sqrt2}(X+X^\dagger)
+\frac{\kappa}{4}D.
\]

Deshalb sind

\[
C_1=\frac{\kappa}{\sqrt2}W,
\qquad
C_{\rm el}=\frac\kappa4W^\dagger W,
\qquad
\Omega=2\kappa I
\]

und

\[
C_{\rm el}=C_1^\dagger\Omega^{-1}C_1
\]

korrekte Konsequenzen **dieser Liftregel**. Die Schur-Sättigung beweist, dass
der elastische Term nach Wahl des Operatorvektors nicht beliebig ergänzt
wurde.

Umgekehrt selektiert die abstrakte positive `2 x 2`-Form den Operatorvektor
`y_A` nicht. Sie erzeugt weder die 60 Labels noch den W-Tensor noch die
lokale CAR/CCR-Darstellung. Daher ist die Schur-Sättigung kein rückwirkender
Herkunftsbeweis der Liftregel.

Insbesondere darf `C_el=0` nicht als Axiom für jede mögliche Quelle benutzt
werden. Der Vergleich muss `C_el` aus derselben unabhängig gewonnenen
Quellenabbildung messen. Der jetzige positive Kandidat zeigt eine konsistente
Alternative, nicht ihre Auswahl durch P1/P2.

## 7. Zeit, Reflexion und Skala

Der aktive Block erfüllt in seiner Zweierbasis die affine Reflexion

\[
s h_{\rm active}s=4I-h_{\rm active},
\qquad s=\operatorname{diag}(1,-1).
\]

Das genügt für die eingeschränkte aktive RR-Zeit. Auf dem gesamten
`Q=2`-Raum kann dieselbe skalare Relation mit `4kappa I` nicht gelten, weil
der 1956-dimensionale dunkle Paarraum bei Energie null liegt. Die linke Seite
bleibt dort null, die rechte wäre `4kappa I`.

Auf dem vollen Fockraum ist `H_+` positiv und nach oben unbeschränkt. Eine
globale unitäre Relation

\[
U H_+U^\dagger=aI-H_+
\]

mit endlichem Skalar `a` ist daher spektral unmöglich. Dies ist kein
allgemeiner Ausschluss einer zweitenquantisierten RR-Reflexion: Deren Zentrum
kann teilchenzahl- oder sektorenabhängig sein. Eine solche Relation müsste
jedoch ausdrücklich konstruiert werden; der aktive `2 x 2`-Block liefert sie
nicht automatisch.

Auch `kappa` wird nicht durch den endlichen Matrixvergleich gewonnen. Der
Originalcontract behandelt die kontinuierliche Einheit und sogar die Wahl
des Hardy-Logarithmus als Teil des noch offenen Quellen-/Metrologievertrags.

## 8. Welche schwächere Aussage konstruktiv offen bleibt

Der Spektral- und CCR-Ausschluss verbietet nicht den neuen Hamiltonoperator.
Er begrenzt seine Interpretation. Eine physisch brauchbare schwächere Brücke
könnte aus einer Kompression oder GNS-Isometrie bestehen, die nur den aktiven
RR-Unterraum auf die hellen `Q=2`-Zustände abbildet. Dafür muss eine
Quellenherleitung mindestens zeigen:

1. warum die physischen Quellenfelder gerade die kanonische aktive
   Kompression `P_act` verwenden und wie das dunkle RR-Tripel physisch
   behandelt oder in einen anderen nachgewiesenen Sektor transportiert wird;
2. warum genau 60 Kopien entstehen und warum ihre Basis der vorhandene
   W-Bosonenraum ist;
3. wie Adjunktion, `Q`-Grad, innere Ladungen und die tatsächlichen D4-/Hodge-
   Wirkungen gemeinsam erhalten werden;
4. wie der Quellenzustand auf den Zielzustand abgebildet wird;
5. warum die Quellzeit gerade `H_+` mit derselben Skala `kappa` ist;
6. welche vollständige `Q=4`- und Mehrzeitantwort daraus folgt.

Eine solche Kompression muss keine kanonische Operatorautomorphie sein. Ihre
aktive Ebene ist bereits D4-kanonisch; die noch fehlende Wahl betrifft ihre
physische Rolle und Feldrealisierung. Sie darf aber auch nicht allein aus dem
bereits gewünschten Zieloperator rückwärts definiert werden.

## 9. Gezielte Prüfung der Herkunftsauswahl

Die geprüften Originalstellen liefern eine engere Antwort als ein allgemeines
No-go. `origin_theory.tex`, Zeilen 87--105, gewinnt aus dem Vierpunktdivisor
den fünfdimensionalen Riemann--Roch-Raum und dessen gerade Cliffordalgebra,
markiert die **physische Identifikation** dieses Raums mit dem Träger aber
ausdrücklich als bedingt. `tfpt_1_architecture_e8.tex`, Zeilen 167--188,
definiert P1 als skalaren, reflexionspositiven Nahtkern und P2 als
fünfstellige Readout-Schnittstelle. Diese Axiome benennen dort keinen
CAR/CCR-Operatoradapter.

Der stärkste einschlägige positive Satz steht in derselben Architekturdatei,
Zeilen 1569--1590: Die codeerhaltende Transportalgebra hat minimalen
Cliffordgrad zwei; Paartransporte erzeugen die gerade Codealgebra. Das wählt
eine **Operatorgradklasse**, aber weder einen unabhängigen CCR-Bosonoperator
noch die Einsetzung einer RR-Fixraumrichtung als `P_A/sqrt(8)` und der anderen
als `b_A`. Der Bericht `primitive-transfer-selection-20260912/REPORT.md`
bezeichnet seine eigene Auswahlform `Q` ausdrücklich als neu deklarierte
Hypothese und fordert die primitive Maß-/Charaktervorschrift erst noch aus der
Quelle.

Damit ist in diesen gezielt geprüften Quellen die erste konkrete zusätzliche
Wahl genau die Liftregel

\[
\iota_A(c_+)=P_A/\sqrt8,
\qquad
\iota_A(c_-)=b_A,
\]

einschließlich der Feldarten, ihrer targetseitigen Spiegelzuordnung, der
Anwendung auf die 60 W-Kanäle und der Zeitnorm `kappa`. Der Projektor
`P_act`, die Grad-zwei-Paarstruktur und die kommutierende innere RR-Wirkung
`K_RR` sind davon unabhängig bereits vorhanden.

Die verbleibende Freiheit lässt sich im Scope der gelesenen Regeln explizit
sehen: Solange P1/P2 keine targetseitige Spiegel- und Clockwirkung auf dem
hellen Paar/Boson-Dublett festlegen, kann eine norm- und `Q`-erhaltende
Einsetzung mit jedem `U in U(2)` nachkomponiert werden; die targetseitigen
Operatoren werden dann entsprechend durch `U` konjugiert. Erst ein
**unabhängig** festgelegtes targetseitiges `S` und das exakte Intertwining von
`h_active` reduzieren diese Freiheit auf eine gemeinsame Phase. Sie erzeugen
aber auch dann nicht aus sich heraus die kategoriale Festlegung
„erste Linie = zusammengesetztes CAR-Paar, zweite Linie = elementares
CCR-Boson“. Dies beweist eine Freiheit innerhalb des genannten
P1/P2-Scopes; es behauptet keine Nichtableitbarkeit aus allen möglichen
TFPT-Erweiterungen.

## 10. Gepinnte Quellen dieses Audits

Der Bericht verwendet gezielt die folgenden fünf Originaltexte, Contracts
und Prüfberichte in ihrem am 21. September 2026 gelesenen Dateistand. Die
SHA-256-Werte pinnen genau diesen Inhalt; die Liste behauptet keine globale
Vollsuche aller TFPT-Unterlagen.

| Quelle | SHA-256 |
|---|---|
| `/Users/stefanhamann/Projekte/tfpt-theoryv4/origin_theory.tex` | `4a2ac752cf9beb65452d5c1aad3a9dc22b0d3fee24e8247c064ed654f910d95f` |
| `/Users/stefanhamann/Projekte/tfpt-theoryv4/tfpt_1_architecture_e8.tex` | `ca5460de7fe54d7362dcfbc9d650cc349811d6bada906317baadd7297d2e89eb` |
| `/Users/stefanhamann/Projekte/tfpt-theoryv4/experiments/theory-contracts/primitive-transfer-selection-20260912/REPORT.md` | `0f69b0cd7e8ae9f704c248d1b29dd7a43304cff704cfe8db583d0022450c19ba` |
| `/Users/stefanhamann/Projekte/tfpt-theoryv4/experiments/theory-contracts/rr-residue-memory-20260921/HERLEITUNG.md` | `b412632905aac145598c754054e5151b7f6631cb1f1196dfc24cc324138ba7b8` |
| `/Users/stefanhamann/Projekte/tfpt-theoryv4/experiments/theory-contracts/rr-continuous-clock-20260921/HERLEITUNG.md` | `8e133bd50713e7e16fc6808bdbb38f38efb878b9cc0b189d46c062dc1043bde8` |

## Schlussstatus

Die Originalbefunde `rr-residue-memory-20260921` und
`rr-continuous-clock-20260921` bleiben `PARTIAL`. Sie sagen bereits, dass der
lokale zustands-, ladungs-, graduierungs- und zeiterhaltende RR/W-Adapter
fehlt. Der neue positive Lift schließt diese Lücke nicht; er gibt ihr einen
konkreten möglichen Zieloperator.

Der präzise Fortschritt ist:

\[
\boxed{
\text{aktive RR-Form} + \text{gewählter W-Feldlift}
\Longrightarrow H_+\text{ samt }C_{\rm el}.
}
\]

Nicht bewiesen ist die umgekehrte Herkunftsaussage

\[
\boxed{
\text{P1/P2 beziehungsweise ursprüngliche RR-Quelle}
\Longrightarrow \text{dieser W-Feldlift}.
}
\]

Der nächste entscheidende Test ist deshalb nicht eine weitere
Grundzustandsdiagonalisierung von `H_+`, sondern der unabhängige Bau des
aktiven Quellenadapters einschließlich des Umgangs mit dem dunklen RR-Tripel.
