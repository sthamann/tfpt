# TFPT: Ergebnis der exakten Suche an der gemeinsamen Quellzeit

22. September 2026 · Forschungsstand **PARTIAL**

**Die endgültige TFPT-Lösung ist in dieser Fortsetzung nicht gefunden.**
Neu sind ein stärkerer Ausschluss für die Zeitinterpretation des vorgelegten
Kanals und eine exakt bestimmte, bedingte Fortsetzung seiner ursprünglichen
markierten Antworten. Beides wurde an den ursprünglichen Compileroperatoren
berechnet und unabhängig auf mathematischer Ebene durch einen zweiten Agenten
geprüft.

## Was jetzt tatsächlich entschieden ist

Der vorgelegte Quellenkanal verteilt einen Schritt auf die Identität und
fünf Clifford-Operationen:

\[
\Phi(X)=\frac7{12}X+\frac1{12}\sum_{j=1}^{5}\Gamma_jX\Gamma_j.
\]

Er ist als einzelner diskreter Quantenkanal gültig. Sein positiver
GNS-Hamiltonoperator ist ebenfalls gültig. Die zusätzliche Vorstellung,
dass genau dieser Kanal auf derselben Algebra aus einem stetigen
zeitunabhängigen Markovprozess entsteht, ist dagegen ausgeschlossen.

Der neue Beweis erfasst **alle Logarithmuszweige und alle positiven
ganzzahligen Potenzen**, auch sechs zusammengefasste Schritte. Er setzt
keine symmetrische Bewegung zwischen den beobachteten Zeiten voraus.
Nach einer Mittelung über die tatsächlichen Quellsymmetrien müsste ein
solcher Generator eine negative Sprungrate enthalten:

\[
\frac1{16}\log(3/4)<0.
\]

Das ist mit einem solchen Markovgenerator unvereinbar. Der alte Test hatte
nur die symmetrischen Zwischenzeiten ausgeschlossen. Diese Ausweichmöglichkeit
ist jetzt vollständig mitbeurteilt. **Nicht ausgeschlossen** sind der
GNS-Prozess, zeitabhängige reduzierte Prozesse oder eine größere physisch
begründete Dynamik. Es folgt daraus kein Beweis diskreter physischer Zeit.

## Der ursprüngliche Nahttransfer bleibt verträglich

Der klassische TFPT-Transfer B ist weiterhin kontinuierlich Markov-
einbettbar. Seine Übertragung auf alle Quelloperatoren war die zusätzliche
Annahme. Um genau diesen Unterschied zu klären, wurde die ganze Klasse

\[
L=\sum_{j=1}^{5}\lambda_j(\Gamma_j\,\cdot\,\Gamma_j-\mathrm{id}),
\qquad\lambda_j\ge0
\]

mit den bereits vorhandenen fünf Operatoren untersucht. Es wurden keine
neuen Felder, kein Gamma-Randgitter, kein Vaux und kein gewünschter RR-
Energieblock eingesetzt. Die Wahl dieser Generatorenklasse selbst bleibt
eine ausdrücklich zusätzliche Annahme.

**B allein lässt einen dreidimensionalen Bereich mit sechs Ecken zu.**
Diese Menge wurde symbolisch vollständig gelöst. Das ist ein konkreter
Nachweis, warum ein guter Zahlenfit die Quelle noch nicht auswählen kann.

Berücksichtigt man zusätzlich sämtliche Transferantworten des vorhandenen
produktgeschlossenen markierten Operatorbereichs und eine Rotationssymmetrie
seines Dreierkomplements, bleibt in dieser Klasse genau die Fortsetzung

\[
L_{\rm mark}=
\frac{\log(3/2)}4\sum_{j=1}^{2}(\operatorname{Ad}\Gamma_j-\mathrm{id})+
\frac{\log6}{12}\sum_{j=3}^{5}(\operatorname{Ad}\Gamma_j-\mathrm{id}).
\]

Die beiden Raten sind positiv: ungefähr **0,1013663** und **0,1493133**.
Der stationäre Zustand ist eindeutig I4/4; die ursprüngliche kleinste
Recovery-Zerfallsrate bleibt erhalten. Innerhalb des bezeichneten
Operatorbereichs stimmen alle verschachtelten Spur-Transferkorrelatoren
für alle Zeitintervalle überein, nicht nur die ursprünglichen Eigenwerte.

Dieser Satz ist bedingt. Die verwendeten GNS-Produktantworten sind noch
keine unabhängig aus dem rohen P1-Nahtkern gewonnenen Messdaten. Die
Fortsetzung ist außerdem **ein anderer vollständiger Kanal**. Die beiden
Kandidaten lassen sich an einer einzigen zusätzlichen Quellantwort unterscheiden:

| Normierte zusätzliche Zweipunktantwort nach einer Schritteinheit | Wert |
|---|---:|
| Ursprünglicher vollständiger Φ-Kandidat | 1/3 ≈ 0,3333333 |
| Kontinuierliche markierte Fortsetzung | (2/9)^(2/3) ≈ 0,3668808 |

Diese Zahlen sind Entscheidungstests für die beiden Kandidaten, keine
vorgeschriebenen Messwerte einer beliebigen endgültigen TFPT-Lösung.
Die mathematische 2+3-Aufspaltung betrifft interne Clifford-Richtungen;
eine Identifikation mit den physischen Farb- und schwachen Richtungen ist
damit nicht hergeleitet.

## Warum hier kein genetischer Algorithmus eingesetzt wurde

Die entscheidenden Bedingungen ließen sich stärker lösen:

- Der Logarithmus-Ausschluss gilt analytisch für eine unendliche Klasse.
- Der positive Ratenbereich wurde vollständig durch lineare Gleichungen
  und die Aufzählung aller Ecken bestimmt.
- Die zusätzliche Vierpunktantwort bestimmt den sonst freien Parameter
  exakt. Eine stochastische Suche wäre hierfür unnötig.

Mit ausschließlich B als Gütemaß würden unendlich viele Modelle exakt
denselben Fehler null erreichen. Ein genetischer Algorithmus könnte eines
auswählen, aber nicht begründen, warum die ursprüngliche Quelle dieses
Modell auswählt. Erst ein unabhängig hergeleitetes zusätzliches Quellgesetz
würde dieses Problem verändern.

## Was für die vollständige Lösung noch fehlt

Die neue Rechnung schließt eine falsche Zeitidentifikation und liefert
eine verträgliche bedingte Alternative. **Sie liefert weiterhin nicht die
gesuchte gemeinsame Herkunft von Quelle, geladenen Materiefeldern und
physischer Zeit.**

Die nächste entscheidende Herleitung muss aus dem ursprünglichen Naht-/
Collar-Funktional die nichtkommutativen Quellantworten samt ihrer zulässigen
Einfügungen bestimmen. Besonders wichtig sind Antworten außerhalb des
bisher festgelegten markierten Teilbereichs: Sie entscheiden, welcher
vollständige Prozess überhaupt vorliegt. Diese Auswahl kann nicht durch
erneutes Minimieren eines frei gewählten Gütemaßes ersetzt werden.

Darüber hinaus bleibt der tatsächlich geladene Sektorwechsel erforderlich.
Der bereits bewiesene Spin(10)-Zentraltest gilt weiterhin: Mehr Operatorwörter
in demselben 32er-Zustandsraum erzeugen die fehlenden nativen Spinorfelder
nicht. Das ältere ungerade 64er-Randfeld reproduziert W bedingt, erhält aber
nicht die vollständige native CAR/CCR-Algebra und ursprüngliche Zeit.
Diese bekannte Konstruktion wurde deshalb nicht nochmals optimiert.

Der übrige TFPT-Bestand bleibt Teil der Aufgabe: E8-Compiler, bekannte
Flavor-Strukturen, Kopplungs-Fixpunkte und verzahnte Clocks. Keiner dieser
Bestände wird durch die vorliegende Quellenrechnung zurückgenommen. Ihre
gemeinsame physische Realisierung und die offenen T1–T8-Anforderungen,
einschließlich chiraler vierdimensionaler Feldtheorie und Gravitation,
sind aber durch diese Fortsetzung nicht geschlossen.

## Dokumentation und Prüfumfang

Forschungs-ID: **UR.SOURCE.CONTINUOUS_MARKED_TIME.01**.
Die exakten endlichen Prüfungen bestehen im normalen und optimierten Lauf
mit bytegleichen Ergebnissen. Der gesamte Logarithmus-Ausschluss und die
Gleichheit aller markierten Wörter beruhen auf den ausgeschriebenen Beweisen,
nicht auf einer endlichen Stichprobe. Ein separater Agent hat die beiden
Ausschlussargumente sowie die konstruktive Fortsetzung geprüft. Dies ist
keine externe Peer Review und keine Beweisassistenten-Formalisation.

Vollständige Beweise und Voraussetzungen:
[PROOF.md](/Users/stefanhamann/Projekte/tfpt-theoryv4/experiments/theory-contracts/source-continuous-marked-time-search-20260922/PROOF.md).
Die Arbeit ist als **PARTIAL** im Theoriegraphen erfasst; kein physisches
Tor und kein Paper-/Ledger-/Scorecard-Status wurde aufgewertet.

Wissenschaftlicher Rahmen zur Unterscheidung eines einzelnen Kanals von
seiner kontinuierlichen Markov-Einbettung:
[Wolf et al.](https://arxiv.org/abs/0711.3172),
[Wolf–Cirac](https://arxiv.org/abs/math-ph/0611057).
Die konkreten TFPT-Rechnungen stehen im verlinkten eigenen Beweis.
