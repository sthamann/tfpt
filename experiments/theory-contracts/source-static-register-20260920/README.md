# Was das vorhandene Phasenregister tatsächlich erzeugt

20. September 2026 · **UR.SOURCE.STATIC_REGISTER.01 — PARTIAL**

Die unveränderte Vierphasenquelle kann nach dem Ausblenden ihres Registers
echte zusätzliche Vierpunktkorrelationen erzeugen. Diese sind jedoch kein
Beleg dafür, dass sie einen neuen geschlossenen Wechselwirkungsoperator der
Materie hervorbringt. Die beiden Aussagen lassen sich an derselben Quelle
auseinanderhalten.

Bildlich speichert das Register, welcher von vier Filmen abgespielt wird.
Jeder Film besitzt die bereits vorgegebene freie Fermionbewegung. Wenn wir
das Register nicht mehr betrachten, überlagern sich in unserer Beschreibung
die unterschiedlichen Ergebnisse. Das kann neue statistische Beziehungen
erzeugen. Daraus folgt noch kein neues Drehbuch für eine einzige reversible
Materiebewegung.

## Die genaue Aussage

Der ursprüngliche Operator in `verification/v1033_charged_disorder.py` ist
in den vier Registerzuständen diagonal. Für einen anfangs unabhängigen
Registerzustand, auch einen kohärenten, lautet der reduzierte Kanal deshalb

\[
\Phi_t(\rho)=\sum_{r=0}^3p_r U_r(t)\rho U_r(t)^\dagger.
\]

**Dieser Kanal ist auf dem vollständigen Materieraum genau dann unitär,
wenn alle besetzten Entwicklungen bis auf eine Gesamtphase übereinstimmen.**
Das folgt aus der Positivität seiner Choi-Matrix; der kurze Beweis steht
vollständig im [Rechenbericht](PROOF.txt). Es ist eine Anwendung bekannter
Quantenkanal-Mathematik, kein neues allgemeines Naturgesetz.

Bei der ausdrücklich bedingten Hebung auf denselben Fermion-Fockraum ist
jede dieser Entwicklungen gaußsch, also durch einen quadratischen
Fermionoperator erzeugt. Ein deterministisches unitäres Gesamtergebnis aus
dieser Vorschrift bleibt deshalb ebenfalls gaußsch. Ein späterer
unbedingter Reset oder eine reine Registerrotation ändert daran nichts.

## Ein ausdrücklicher Zeuge aus den Originalmatrizen

Als Diagnose verwenden wir die originale Quelle mit drei Gitterstellen in
Umfangsrichtung und einer in Querrichtung, ein gleichgewichtet besetztes
Register und einen Einteilchenzustand am abgehenden Randübergang. Die Größe
und die Präparation sind gewählte Tests, kein hergeleitetes Vakuum.

Die reduzierte Materiereinheit hat für kleine Zeiten die Entwicklung

\[
\operatorname{Tr}\rho(t)^2=1-t^2+O(t^3).
\]

Sie wird also gemischt. Der Koeffizient ist aus den Originalmatrizen exakt
berechnet und verwendet deren eigene Zeiteinheit.

Zugleich bleibt die Teilchenzahl genau eins. Daraus folgt für die Summe der
Abweichungen von der gaußschen Vierpunktzerlegung

\[
D_4=-\frac{1-\operatorname{Tr}\rho(t)^2}{2}
   =-\frac{t^2}{2}+O(t^3).
\]

**Die Vierpunktabweichung ist wirklich vorhanden. Sie stammt hier aus der
Mischung der Phasenzweige.** Sie darf deshalb nicht als Nachweis eines neu
erzeugten kohärenten Vierfermion-Hamiltonoperators ausgegeben werden.

## Was das für den Weg zur Gesamtlösung ändert

Die offene Frage wird enger: Gesucht ist eine aus der Quelle begründete
Dynamik, welche die erforderlichen Wechselwirkungen und geladenen Felder
gemeinsam realisiert. Ein vollständiger Determinantenfaktor oder ein
zusätzliches nichtgaußsches Readout reicht als Herkunftsnachweis nicht aus.

Eine Möglichkeit, die hier geprüfte Klasse zu verlassen, wäre eine aus dem
Ursprung hergeleitete Bewegung zwischen den Registersektoren. Solche
nichtkommutierende Quelldynamik kommt im separaten Rotorparent und in der
zusätzlich konstruierten relativen Quellenkopplung bereits vor. Deren
Operator-, Ladungs-, Zustands- und Zeitabbildung auf die Randquelle bleibt
aber eine eigene, weiterhin offene Aufgabe. Ihre bloße Existenz identifiziert
die verschiedenen Systeme nicht.

Der Registershift kann schon im unveränderten Modell eine zeitabhängige
Antwort besitzen. Das wurde nicht ausgeschlossen: Er wird durch die
unterschiedlichen Zweigentwicklungen transportiert. Ein solcher geladener
Probeoperator und ein tatsächlich im Hamiltonoperator wirkender Übergang
sind unterschiedliche Bestandteile der Theorie.

Kodierte Niederenergieräume, anfangs korrelierte Zustände, Postselektion und
zusätzliche Kontrollen sind ebenfalls nicht ausgeschlossen. Sie benötigen
ihre eigene Herleitung einschließlich der Fehler und der geladenen
Antworten. Dieser Vertrag beweist weder ein allgemeines Verbot emergenter
Wechselwirkung noch die Unmöglichkeit einer TFPT-Gesamtlösung.

Der vorgeschaltete [Quellenabgleich](SOURCE_INTERACTION_INVENTORY.txt) und
die [Casimir-Gegenprüfung](NATIVE_PAIR_REVIEW.txt) verhindern außerdem eine
Doppelzählung: Die Paar-Casimir-Identität der 64-Fermionen-/60-Bosonenbank
war bereits dokumentiert und gehört zu einem deklarierten Hilfsmodell.
Sie wird hier nicht als neue Ursprungsherleitung verbucht.

Die inzwischen dokumentierte
[vollständige Paarantwort](../source-pair-transfer-20260920/ERGEBNIS.md)
ergänzt diesen Befund: Dort stimmt der Kopplungstensor bereits mit den
zusammengesetzten Randfeldern überein, und ihre bedingte Zeitantwort ist
kontrolliert. Der helle Kanal besitzt aber noch keine negative
Bindungsenergie gegenüber denselben Einzelfeldern. Die heutige Prüfung
betrifft eine mögliche Quelle der noch fehlenden Dynamik. Sie zeigt, warum
das bloße Ausblenden des unveränderten statischen Registers dafür kein
deterministischer Wechselwirkungsmechanismus ist. Die andere Paarrechnung
wurde hier gelesen, nicht erneut ausgeführt.

## Belegstatus

- [Analytischer Beweis und genaue Voraussetzungen](PROOF.txt).
- [Interne unabhängige mathematische Gegenprüfung](REVIEW.txt).
- `checker.py`: exakte endliche Kontrollen der Originalquelle und des
  Reinheits-/Vierpunktzeugen; `certificate.json` dokumentiert die Ausführung.
- `source_manifest.json`: Prüfsummen der verwendeten Quellen und Artefakte.

Reproduktion aus dem Repository: `python3 -B
experiments/theory-contracts/source-static-register-20260920/checker.py`.
Die normale und die mit `-OO` ausgeführte Rechnung werden getrennt
zertifiziert. Der Prüfer führt neben der rationalen Rekonstruktion nur die
acht benötigten Definitionen des gepinnten Originalcodes aus und vergleicht
deren dyadisch exakte Matrizen ohne Rundungstoleranz. Die volle historische
Verifikationssuite wird dadurch nicht als erneut ausgeführt ausgegeben.

Die Kanaltheorie und fermionische Gaußstruktur sind etablierte Grundlagen:
[Bravyi, fermionic linear optics](https://arxiv.org/abs/quant-ph/0404180) und
[Girard et al., mixed-unitary channels](https://arxiv.org/abs/2003.14405).
Der Beitrag ist ihre ausdrückliche Anwendung auf diese offene
TFPT-Quellenfrage. Eine externe Begutachtung, eine physische Vorhersage
oder die Schließung eines T1–T8-Gates wird nicht behauptet.
