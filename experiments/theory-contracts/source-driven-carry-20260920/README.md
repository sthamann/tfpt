# Zwei Vorwärtsschritte transportieren tatsächlich Ladung

20. September 2026 · **UR.SOURCE.DRIVEN_CARRY.01: PARTIAL**

In der ursprünglichen freien QWZ-Quelle lässt sich der bisher nur aus
Sektorvergleichen bekannte Halb-/Ganzladungsübertrag durch eine tatsächliche
unitäre Zeitentwicklung ausführen. Ein vorgegebener gleichförmiger
Flussdurchlauf führt von f=1/4 über 3/4 nach 5/4. Der vollständige gefüllte
Anfangszustand wird währenddessen weder neu besetzt noch zurückgesetzt.

Am oberen Rand entstehen im kontrollierten Grenzwert die Ladungsänderungen
**+1/2 nach der ersten Hälfte und +1 nach dem ganzen Umlauf**. Am unteren Rand
stehen die entgegengesetzten Änderungen. Nach der großen Eichidentifikation
hat das Hintergrundlabel wieder seinen Anfangswert; der Zustand enthält ein
oberes Teilchen und ein unteres Loch. Die zweite Vorwärtsfahrt ist somit
physisch von der Umkehrung der ersten Fahrt verschieden.

## Was gegenüber dem vorherigen Befund hinzukommt

Der alte Satz verglich zwei Grundzustände. Hier wird derselbe Anfangszustand
mit dem zeitabhängigen Quellenoperator entwickelt. Eine analytische
Abschätzung kontrolliert den gesamten gefüllten See einschließlich der
massiven Moden und der tatsächlichen Nullstelle im Spektrum.

Die geometrisch markierte Randlinie setzt sich durch diese Nullstelle fort.
Ihre Mischung mit dem anderen Rand verschwindet dort schnell genug, um einen
beschränkten Kommutatorlöser zu konstruieren. Deshalb bleibt eine
adiabatische Abschätzung möglich, obwohl die gewöhnliche Mindestlücke null
wird. Die genaue Argumentation steht in [PROOF.md](PROOF.md).

Mit Umfang N und Fahrzeit T gelten:

- Spurabstand der entwickelten Kovarianz vom transportierten Ziel: O(1/T).
- Hilbert--Schmidt-Abstand: O(1/(T sqrt(N))).
- Fehler in der skalierten Quellenenergie: O(sqrt(N)/T+1/T²).

Die ausdrückliche Wahl **T=N^(3/4)** lässt diese Fehler und die zusätzlichen
Phasen fester niedriger Randanregungen gleichzeitig verschwinden. Auch die
Varianz der bereits definierten gefilterten regionalen Ladung geht gegen
null. Die Behauptung betrifft deshalb mehr als einen passenden Mittelwert.

## Ausgeführte numerische Gegenkontrolle

Alle 8N besetzten und 8N unbesetzten Moden der Breite-8-Quelle sind enthalten.
Die Zeitintegration verwendet die direkt importierten ursprünglichen
Hoppingmatrizen. Die gefilterte Ladung bezieht sich stets auf dieselbe rohe
Anfangsdichte; am Halbpunkt wird der dortige Filter verwendet.

| N | T | Flussprofil | Ladung nach halbem Umlauf | Ladung nach ganzem Umlauf |
|---:|---:|---|---:|---:|
| 32 | 32 | linear | 0,4999988494 | 0,9999951620 |
| 64 | 64 | linear | 0,4999998539 | 0,9999996882 |
| 32 | 64 | glatte Enden | 0,4999999999 | 1,0000000000 |

Für die letzte Zeile liegt der Spurabstand der **gesamten** Endkovarianz vom
Teilchen-Loch-Ziel bei etwa 0,000487; ihre gefilterte Ladungsvarianz liegt bei
8,92·10^-11. Die Halbierung des Integrationsschritts von 0,1 auf 0,05 ändert
den vollständigen Ladungsübertrag um etwa 4,3·10^-13. Das ist eine numerische
Konvergenzkontrolle, keine Intervallzertifizierung. Die analytischen
Fehlerschranken werden durch diese Dezimalwerte nicht ersetzt.

Die linear gefahrenen Fälle erreichen bereits fast ganzzahlige gefilterte
Ladungen, besitzen aber größere Kovarianzfehler. Ein guter einzelner
Messwert allein wäre somit noch kein Nachweis des ganzen Zielzustands.

## Reichweite und Bezug zur neuen Randrekonstruktion

Der zusätzliche Flussfahrplan ist eine **äußere Probe**, nicht aus P1/P2
ausgewählt. Er wirkt am gesamten Umfang. Ein zeitabhängiger Wechsel zwischen
gleichförmiger und Seam-Eichung benötigt das zugehörige skalare Potential.
Die Existenz dieses Transportes beweist keinen lokalen Spinorstrom und
selektiert keine acht inneren Kanäle.

Der später eingereichte Randrekonstruktionsvorschlag verändert dagegen die
lokale Randphase: acht Kanäle, ein zusätzliches gegenläufiges Paar und eine
spezielle Wechselwirkung. Er kann dadurch einen anderen lokalen Feldraum
tragen. Der globale Transport hier und jener lokale Kontinuumkandidat sind
verschiedene Aussagen. Insbesondere widerspricht unser Transport nicht der
Mindestenergie des globalen NS->R-Wechsels beider Ränder: andere Anfangs-
und Endsektoren und ein äußerer zeitabhängiger Antrieb sind ausdrücklich
angegeben; eine Spektrallinie bei Energie eins wird hier nicht behauptet.

Der etablierte physikalische Rahmen ist der
[Flusstransport von Laughlin](https://doi.org/10.1103/PhysRevB.23.5632);
die verwendete Art der adiabatischen Kontrolle gehört zum Rahmen von
[Avron und Elgart](https://arxiv.org/abs/math-ph/9805022).
Der spezifische Beitrag ist der überprüfte Anschluss an unsere konkrete
Quelle samt vollem See, Energie, Halb-Ladung und zweitem Vorwärtsschritt.

## Reproduktion und Beleggrenze

`python3 -B flux_drive.py` erzeugt die sieben numerischen Kontrollen.
`python3 -B checker.py` prüft Quellenpins, exakte endliche Blockidentitäten,
Fockraum-Energieidentitäten und die numerische Ergebnisdatei.
`python3 -OO -B checker.py` prüft, dass die Kontrollen nicht von deaktivierbaren
Python-Assertions abhängen. Allgemeine analytische Sätze werden durch den
Checker nicht formal bewiesen.

Die getrennten Reviews `FLUX_PROOF_REVIEW.txt`, `FLUX_ENERGY_REVIEW.txt` und
`FLUX_INDEPENDENT_AUDIT.txt` wurden durch andere Agenten erstellt; dies ist
keine externe wissenschaftliche Begutachtung. Die im letzten Review
angefragte explizite gleichmäßige Chartabdeckung ist in Abschnitt 2 von
`PROOF.md` ergänzt. Keine Änderung von Paperclaims, Physikledger oder T1–T8.
