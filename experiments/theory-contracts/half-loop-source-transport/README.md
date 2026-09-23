# Halb-Schritt im vorhandenen Quellraum und eine präzisere Energieprüfung

9. September 2026. Anschluss an
[common-engine-threeway](../common-engine-threeway/README.md), gepinnter
Repo-Stand `66b91e40e245569f06ab440ead80f446c9be0ee5`.

**Ergebnis:** Ein energieverträglicher Halb-Schritt des ursprünglichen
Wilson-Flusses lässt sich auf den bereits vorhandenen Zuständen des
kleinen Rotor-Parents konstruieren — ohne zusätzliche Sektoren. Die
eigentliche Halb-Ladungsprüfung besteht er noch nicht. Gleichzeitig wird
die E₈-Energieprüfung auf die volle symmetrieverträgliche quadratische
Klasse erweitert und gegen die vorhandene Hintergrundverschiebung abgesichert.

Dies sind lokale Forschungsresultate, kein mikroskopisches E₈-Feld und
keine Lösung von T1–T8. Insbesondere ist der Operator bewusst konstruiert,
nicht durch die TFPT-Dynamik eindeutig ausgewählt.

## 1. Ein positiver Operator-Kandidat ohne neue Hilfszustände

Der bisherige physikalische Quadrat-Raum besitzt 70 Materiebelegungen,
jeweils mit beliebigem ganzzahligem umlaufendem Fluss. Diese vorhandenen
Belegungen lassen sich in 35 Paare aufteilen: Eine Belegung wird ihrer
komplementären Belegung zugeordnet. Die Gesamtzahl vier bleibt erhalten.

Der neue Operator wechselt zwischen diesen Partnern. Dabei werden die
elektrischen Flüsse so mitgeführt, dass das Gauss-Gesetz gültig bleibt.
Beim zweiten Wechsel kommt genau ein voller umlaufender Flussschritt hinzu.

Nachgewiesen sind:

- `S²=W`, mit W dem ursprünglichen Wilson-Flussschritt.
- S ist unitär; beide inversen Richtungen sind explizit vorhanden.
- Kein Rotor mit halbzahligen Eigenwerten, zusätzlicher Fockraum oder
  externes Zwei-Zustands-Register wurde eingeführt.
- S und S* erhalten den vollständigen Definitionsbereich des unveränderten
  Hamiltonoperators. Eine explizite Energie-Graphnormschranke gilt für
  alle ganzzahligen Flüsse, nicht nur für einen numerischen Ausschnitt.
- Der Operator lässt sich aus den vorhandenen Fermionoperatoren und
  ganzzahligen Link-Transporten bilden. Er ist kein ergänzter Hamiltonian-Term.

Die Folge **entwickeln → S anwenden → weiterentwickeln** wurde zusätzlich
auf dem gleichen 1.412-dimensionalen Cutoff-Raum ausgeführt. Norm und die
anschließende Energieerhaltung stimmen. S selbst darf die Energie verändern.

**Nicht abgeleitet:** Warum genau diese Paarung, dieses Belegungsbit und
diese Phasen physikalisch gewählt werden sollen. Schon acht verschiedene
Bitwahlen liefern unterschiedliche zulässige Wurzeln. Die Konstruktion
liefert einen quellengetragenen Kandidaten, keine eindeutige Ursprungsgeschichte.

## 2. Warum dies noch kein erhaltenes Halb-Ladungsfeld ist

Für diesen Kandidaten existiert eine einfache halbzahlige Markierung P,
die bei jedem S-Schritt um 1/2 wächst. Aber der originale Hamiltonoperator
erhält P **nicht**. Ein unveränderter Transportterm mit Amplitude `1/12`
ändert P bereits um eine ganze Einheit.

Die Grenze ist in dieser kleinen Quelle genauer bestimmbar: Der echte
Transport verbindet alle 70 Materiebelegungen und sämtliche ganzzahligen
Flussstufen. Deshalb ist keine nichtkonstante Ladung erhalten, die nur
als Funktion dieser Belegungs- und Flusszahlen wirkt. Das betrifft diese
diagonale Klasse im endlichen räumlichen Quadrat, nicht sämtliche
quantenmechanischen Ladungsoperatoren oder mögliche Skalierungsgrenzen.

Damit ist die weitere Aufgabe klarer: Ein tatsächlicher Ladungsoperator
müsste über diese einfache Zählregel hinausgehen und aus der Quelle
hergeleitet werden. Eine bloße neue Nummerierung des vorhandenen Flusses
schließt die Lücke nicht.

Zum Vergleich wurde auch die skalare Quadratwurzel des Wilson-Operators
untersucht. Sie ist zwar unitär, erzeugt auf dem Referenzzustand aber
unendliche erwartete elektrische Energie. Die materiegestützte Konstruktion
vermeidet genau dieses Problem. Eine allgemeine Unmöglichkeit von Halb-
Twists oder zeitlich geglätteten Feldern wird daraus nicht behauptet.

## 3. Präzisierung der letzten Runde: Rohenergien dürfen verschieden sein

Der frühere Gleichenergie-Test betraf den quadratischen Zielanteil. Bei
seiner Anwendung auf die tatsächliche Quelle muss deren bereits vorhandene
lineare Hintergrundverschiebung erhalten bleiben. Gleiche **Rohenergien**
aller geladenen Zustände wären deshalb eine zu starke Forderung.

Für `E(q)=qᵀGq/2+ell·q+c` gilt stattdessen exakt

```
[E(q0+alpha)+E(q0-alpha)-2E(q0)]/2 = alphaᵀG alpha/2.
```

So wird die Hintergrundverschiebung durch einen Vergleich beider
Ladungsrichtungen getrennt, ohne H umzudefinieren oder einen Koeffizienten
nachzustellen. Gemeint sind Ladungssektor-Nullmodenenergien bei derselben
Referenz, nicht beliebige Energieerwartungen verschmierter Feldzustände.

Im vorhandenen bedingten Achtkanal-Energiemodell hat der Halb-Twist bei
einheitlichen Hintergrundzeichen die Rohenergien **0 und 2**. Der
Paarvergleich ergibt **1**, genau seinen quadratischen Zielwert. Auch
die vorhandene 5+3-Zeichenwahl mit **3/4 und 5/4** ergibt 1. Alle 240
Wurzelpaare wurden in beiden vorhandenen Varianten geprüft. Dies leitet
die acht mikroskopischen Kanäle weiterhin nicht her.

## 4. Der Energietest berücksichtigt nun auch Mischungen

Die vorige Runde behandelte nur diagonale Energien mit zwei Geschwindigkeiten.
Jetzt wird jede reelle symmetrische quadratische Energie zugelassen, die
die tatsächlichen Zieloperationen J und sigma respektiert. Diese Klasse
hat **sechs** Parameter, nicht zwei.

Ein kleiner exakter Test genügt dennoch: Vergleiche die zentrierten
Gegenladungs-Paarenergien von fünf festgelegten ganzzahligen Wurzeln und
dem Halb-Twist. Fünf unabhängige Gleichheiten erzwingen dann `G=vI` —
also eine gemeinsame Skala ohne zusätzliche Mischungen. Für jede
weggelassene Gleichheit wurde eine positive Gegenkonstruktion gefunden,
die alle anderen Prüfungen besteht.

Das ist ein schärferes Annahmekriterium für ein künftiges Quellfeld,
kein Beweis, dass die Quelle diese Gleichheiten bereits erfüllt. Die
Symmetrieannahme betrifft G; der physikalische Hintergrundterm darf
dabei weiterhin vorhanden sein.

## Was als Nächstes den Unterschied machen würde

Ein Kandidat muss nun gleichzeitig vorweisen: quellenbegründete Ladung,
einen Halb-Übertrag samt seiner adjungierten Gegenrichtung, kontrollierte Energie und
den hintergrundbereinigten Energievergleich. Der hier gebaute S erfüllt
Umkehrbarkeit, Flussübertrag und Energieverträglichkeit, scheitert aber
noch an der erhaltenen Ladung und ist nicht als E₈-Halb-Twist identifiziert.
Ein neues Gegenstück darf nicht allein durch Diagonalisieren von H und
frei gewählte Ladungsnummern definiert werden; Lokalität, Quellmarkierung
und Ladungsalgebra müssen mitgeprüft werden.

## Reproduktion und Umfang

- [PROOF.md](PROOF.md): Ableitungen, vollständige Geltungsbereiche und Gegenkontrollen.
- [validation.json](validation.json), [validation_optimized.json](validation_optimized.json): vollständige Läufe.
- [TEST_RESULTS.md](TEST_RESULTS.md): ausgeführte neue und bestehende Prüfungen.

Aus dem Repo-Root:

```sh
experiments/tfpt-discovery/.venv/bin/python -B experiments/theory-contracts/half-loop-source-transport/run.py --output /tmp/tfpt-half-loop.json
experiments/tfpt-discovery/.venv/bin/python -B -m unittest discover -s experiments/theory-contracts/half-loop-source-transport -p test_checker.py -v
experiments/tfpt-discovery/.venv/bin/python -B -OO -m unittest discover -s experiments/theory-contracts/half-loop-source-transport -p test_checker.py -v
```

Keine Änderungen an alten Quellen, Paper, Webseite, globalen Statusmarkern
oder fremden Arbeiten. Kein Commit/Push in dieser Forschungsrunde.
