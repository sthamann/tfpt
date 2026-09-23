# Geladene Felder aus dem erhaltenen Vierphasenregister

**2026-09-20 · UR.SOURCE.CHARGED_REGISTER.01 · PARTIAL**

Es gibt eine exakte gemeinsame Abbildung von Fermionfeldern, Zuständen und Zeitentwicklung in der vorhandenen Vierphasenquelle. Dafür muss das Register mit der Teilchenzahl korreliert bleiben. Die tatsächliche Phasenlinie der Quelle lässt sich dabei einbeziehen; ein zusätzlicher Registerfaktor stellt die vollständigen Fermionregeln sicher.

Das ist ein konstruktiver Anschluss an den letzten Ausschluss. Die erhaltene Dynamik ist jedoch eine teilchenzahlabhängige Randphase. Bei jeder festen Teilchenzahl bleibt sie frei. Sie liefert deshalb noch keine lokale Paarwechselwirkung oder vollständige physische TFPT-Realisierung.

## Bild und entscheidende Änderung

Man kann sich das ursprüngliche Register als Rad mit vier Stellungen vorstellen. Die letzte Rechnung bereitete dieses Rad unabhängig von der Materie vor und blendete es anschließend aus. Die Materie sah dadurch eine Mischung verschiedener Entwicklungen.

Jetzt bleibt eine gemeinsame Regel erhalten: Entfernt ein geladenes Feld ein Teilchen, dreht es zugleich das Rad um eine Stellung weiter. Die Summe aus Radstellung und Teilchenzahl bleibt modulo vier gleich. So behalten die Felder die Information, die beim vorherigen Ausblenden verloren ging.

Die Rechnung setzt weiterhin den ausdrücklich bedingten Raum `C4 tensor Fock(V)` voraus. Das ursprüngliche Einteilchenskript wählt diesen Vielteilchenraum, seine Präparation und das physische Feldwörterbuch nicht selbst aus. Die Kodierung ist mathematisch konstruiert, nicht aus P1/P2 als Naturvorschrift abgeleitet.

## Was exakt zusammenpasst

Sei \(z=i\), \(Z|r\rangle=z^r|r\rangle\), \(S|r\rangle=|r+1\rangle\), und \(N\) die Teilchenzahl. Mit den unveränderten Quellblöcken

\[
h_r=b+z^r a+z^{-r}a^\dagger,
\qquad H_R=\sum_r\Pi_r\otimes d\Gamma(h_r)
\]

definieren wir

\[
F_j=S\otimes c_j,\qquad C=Z\otimes z^N,\qquad
J_s|\psi_N\rangle=|s-N\bmod4\rangle\otimes|\psi_N\rangle.
\]

Die Felder erfüllen die vollständigen CAR, sind fermionisch ungerade und senken \(N\) um eins. Die vier Bilder von \(J_s\) sind orthogonal und erschöpfen den vollständigen Quellraum. Es gilt sowohl für die Felder als auch für den Hamiltonoperator

\[
F_jJ_s=J_sc_j,\qquad H_RJ_s=J_sH_s.
\]

Damit wird dieselbe Zeitentwicklung für alle Zeiten übertragen, nicht nur ein einzelner Erwartungswert. Keine der vier Klassen \(s\) wird durch diesen Satz als physischer Zustand ausgewählt.

## Die Verbindung zur tatsächlichen Phasenlinie

Die ursprüngliche Quelle enthält \(D=S\otimes\Gamma(u)\), wobei \(u=\operatorname{diag}(i^{q_j})\) auf dem bezeichneten Bogen die Phase \(i\) und außerhalb die Phase eins setzt. Hier ist \(q_j\in\{0,1\}\) eine Bogenmarkierung, keine elektrische Ladung.

Der naheliegende Ausdruck \(Dc_j\) verletzt die Fermionregeln zwischen einem Ort innerhalb und einem Ort außerhalb dieses Bogens. Die korrekte gemeinsame Ergänzung lautet

\[
\boxed{F_j^u=D\,(Z^{-q_j}\otimes c_j).}
\]

Sie folgt aus einer einzigen unitären Konjugation aller Felder. Der Faktor \(Z^{-q_j}\) ist notwendig; er wurde nicht an ein Messergebnis angepasst. Mit der dazugehörigen Kodierung \(J_s^u\) gilt erneut exakt

\[
H_RJ_s^u=J_s^uH_s^u,\qquad
H_s^u\big|_N=d\Gamma\!\left(u^{-r}h_ru^r\right)\big|_N,
\quad r=s-N\bmod4.
\]

Diese Konjugation verlegt die ursprüngliche Randphase an das Ende des Bogens. Sie verändert keinen Kopplungsbetrag und fügt keinen Hamiltonterm hinzu.

Auch der ursprüngliche Phasenoperator bleibt exakt erhalten:

\[
D J_s^u=J_{s+1\bmod4}^u.
\]

Die konstruierten Fermionfelder wirken innerhalb einer Klasse; der ursprüngliche Operator \(D\) wechselt zwischen den vier Klassen. Seine Zeitantwort wird durch die Differenz \(H_{s+1}^u-H_s^u\) übertragen. Deshalb sind die vier Klassen keine Superselektionssektoren der gesamten ursprünglichen Observablealgebra. Nur eine Klasse zu behalten würde einen bereits vorhandenen Quelloperator verlieren.

## Warum höhere Fermionterme noch keine neue lokale Kraft beweisen

Im Materiewörterbuch hängt die Phase am markierten Übergang nun von der **gesamten** Teilchenzahl ab. Ein zusätzliches Teilchen kann deshalb seinen Koeffizienten ändern, selbst wenn es räumlich anderswo sitzt.

Im exakten Sechsmodenbeispiel der Originalquelle gilt für eine bestimmte gerichtete Verbindung:

\[
\langle2|H_0^u|0\rangle=\frac i2,
\qquad
\langle2,4|H_0^u|0,4\rangle=\frac12.
\]

Die Ziffern bezeichnen besetzte Orbitale; \(|0\rangle\) im ersten Ausdruck ist kein Vakuum. Dasselbe Hopping hat mit einem zusätzlichen Zuschauer eine andere Phase. Daher ist der Operator auf dem gesamten Fockraum kein einziger teilchenzahlunabhängiger quadratischer Hamiltonoperator.

Für jede **feste** Teilchenzahl ist die Phase jedoch eine feste Zahl. Die Entwicklung ist dort weiterhin die freie Vielteilchenhebung eines Einteilchenoperators. Ein Slaterdeterminant bleibt ein Slaterdeterminant. Die formal auftretenden Vierfermionterme und höheren Terme bilden eine globale teilchenzahlabhängige Randbedingung ab; eine durch lokale Kollision erzeugte Bindung folgt daraus nicht.

## Was die Lokalitätsprüfung trägt

- **Zahlneutrale lokale Messungen:** Ihr Antwortkommutator übernimmt die begrenzte Ausbreitung der ursprünglichen lokalen Quelle. Man muss nur das Maximum über ihre vier Phasenzweige nehmen. Das ist ein allgemeines Argument für diese Observablen, keine Extrapolation des kleinen Beispiels.
- **Geladene Felder:** Ihr Zeitkommutator enthält den markierten Randübergang auch für einen davon entfernten Modus. Die Kodierung erhält damit nicht die gewöhnliche Zuordnung eines geladenen CAR-Feldes zu genau einem Gitterort.
- **Reichweite des positiven Satzes:** Die Schranke für neutrale Antwortkommutatoren beweist noch keinen vollständigen thermodynamischen Aufbau einer lokalen Observablealgebra. In der gemeinsamen Darstellung können globale zentrale Faktoren \(i^N\) verbleiben.

Ausgedehnte geladene Felder sind nicht automatisch unphysikalisch: In Eichtheorien können geladene Operatoren Phasenlinien benötigen. Hier ist allerdings nur eine **globale** erhaltene Größe \(C\) konstruiert. Lokale Gauss-Bedingungen, Flüsse und deren physische Herkunft folgen daraus nicht.

Ein räumlicher Grenztest lässt sich darüber hinaus analytisch entscheiden. Vergrößern wir den vorhandenen Zylinder bei fester Breite und rücken die markierte Verbindung immer weiter von einer lokalen zahlneutralen Messung ab, nähert sich deren Zeitentwicklung für feste Beobachtungszeiten der freien Quelle an. Der Fehler ist höchstens von der Form

\[
\|O_X(t)-O_X^{\mathrm{frei}}(t)\|
\le C_X\bigl(e^{v|t|}-1\bigr)e^{-a\,\mathrm{Abstand}(X,\mathrm{Markierung})}.
\]

Die Konstanten können unabhängig von Umfang und Teilchenzahl gewählt werden. Das folgt aus dem exakten Sektorvergleich und einer integrierten lokalen Ausbreitungsschranke. Es ist kein Größentrend, der aus sechs Moden erraten wurde. **In diesem räumlichen Grenzfall entsteht aus der Randphase keine neue lokale Kraft im Inneren.** Bereits vorhandene Zustandskorrelationen und Versuche, die bis zum Rand laufen oder ihn umwinden, bleiben davon getrennt.

## Bedeutung für die Gesamtsuche

Der letzte Registerausschluss galt für Produktpräparation und anschließendes Ausspuren. Die hier konstruierte korrelierte Kodierung erfüllt diese Voraussetzungen nicht und erlaubt tatsächlich einen vollständigen geladenen Feld- und Zeittransport. Damit ist diese zuvor offengelassene Möglichkeit konkret ausgewertet.

Die erste offene Herkunftsfrage lautet jetzt genauer: Warum sollte die Originaltheorie diesen Vielteilchenraum, diese geladenen Felder und ihre Zustandsregel auswählen, und welche ihrer ursprünglichen Operatoren erzeugen eine physische Dynamik über die globale Randphase hinaus? Ein neu eingesetztes Eichfeld oder ein frei gewählter Vermittler würde diese Frage nicht beantworten.

Es gibt keine Übertragung auf die anders konstruierten 64 Spin10×SU4-Felder oder auf einen unabhängigen 60-Kanal-Vermittler. Deren Gruppenwirkung, Zustand und Zeit müssten gemeinsam abgebildet werden. Die Auswahl der Kopplungen, chirale 3+1-dimensionale Materie und Gravitation sind durch den vorliegenden Satz nicht hergeleitet.

## Belege und Wiederholung

- [Vollständige Herleitung und Grenzen](PROOF.txt).
- [Interner unabhängiger Algebra-Review](REVIEW.txt), einschließlich der neutralen Ausbreitungsschranke. Keine externe Begutachtung oder Beweisassistenten-Formalisierung.
- [Abgleich mit vorhandenen Ergebnissen](INVENTORY.txt). Er entstand vor der hier ausgeführten kanonischen Ergänzung des tatsächlichen Phasenoperators; seine damals offene algebraische Teilfrage wird in der Herleitung beantwortet. Begrenzte Suche, keine allgemeine Neuheitsbehauptung.
- [Exakte endliche Kontrollen](certificate.json), [Checker](checker.py) und [Quellpins](source_manifest.json).

Der Checker rekonstruiert die Originalmatrizen bei `nx=3, ny=1` mit exakter Arithmetik. Er prüft die Fermionregeln, Teilchenzahl, Parität, alle vier Kodierungen, die unveränderte Hamiltonwirkung, den verschobenen Phasenübergang und die genannten Gegenproben. Das kleine periodische System ist keine Messung beliebig großer räumlicher Abstände; die allgemeine Aussage dazu steht separat in der Herleitung.

Aus dem TFPT-Repository mit einer Python-Umgebung mit SymPy und NumPy:

```sh
python3 -B experiments/theory-contracts/source-charged-register-20260920/checker.py --output /tmp/charged-register.json
python3 -OO -B experiments/theory-contracts/source-charged-register-20260920/checker.py --output /tmp/charged-register-optimized.json
cmp /tmp/charged-register.json /tmp/charged-register-optimized.json
```

**Firewall:** experimenteller Theorievertrag; `PARTIAL` bezüglich der physikalischen Herkunft, exakte Algebra unter den angegebenen Voraussetzungen. Kein physisches T1–T8-Gate geschlossen, keine Scorecard-, Paper- oder Ledger-Promotion, keine Gesamtlösung behauptet. Die allgemeinen Methoden sind bekannt; die Aussage betrifft ihre konkrete Anwendung auf die unveränderte v1033-Quelle.
