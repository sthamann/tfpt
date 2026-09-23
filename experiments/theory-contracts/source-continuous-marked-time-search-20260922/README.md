# Exakte Suche an der markierten TFPT-Quellzeit

**UR.SOURCE.CONTINUOUS_MARKED_TIME.01 · PARTIAL · 2026-09-22**

Der vorhandene diskrete M4-Kanal Φ und jede positive ganzzahlige Potenz
besitzen keinen zeitunabhängigen GKSL-Logarithmus auf derselben Algebra,
auch ohne Kovarianzannahme für die Zwischenzeiten. Sein positiver
GNS-Hamiltonoperator bleibt gültig. Der klassische Nahttransfer B bleibt
ebenfalls kontinuierlich Markov-einbettbar.

Eine vollständige symbolische Suche in der ausdrücklich zusätzlichen
Klasse der fünf vorhandenen Clifford-Sprünge bestimmt alle B-kompatiblen
Raten: eine dreidimensionale Menge mit sechs Ecken. Die vorhandenen
Produktantworten im markierten M2-Faktor plus SO(3)-Komplementsymmetrie
ergeben dort eine eindeutige kontinuierliche Fortsetzung mit Raten
log(3/2)/4 und log(6)/12. Sie erhält alle kanaldefinierten Transferwörter
dieses Faktors, verändert aber weitere Quellantworten. Sie ist keine
Einbettung von Φ auf ganz M4 und keine hergeleitete physische Feldzeit.

Die analytische Symmetriemittelung erfasst alle Logarithmuszweige; das
Ratenproblem wird vollständig linear gelöst. Ein genetischer Algorithmus
wurde nicht benötigt und würde die fehlende Quellenauswahl nicht ersetzen.

- Beweise, Annahmen und Grenzen: [PROOF.md](PROOF.md)
- Unabhängige Agentenprüfung: [INDEPENDENT_REVIEW.md](INDEPENDENT_REVIEW.md)
- Exakte finite Prüfung: `python3 -B checker.py`
- Optimierter Kontrolllauf: `python3 -B -OO checker.py --out certificate_optimized.json`
- Ergebnisse: `certificate.json`, `validation.json`, `source_pins.json`

Keine nativen Spin(10)-Feldoperatoren oder gemeinsame physische Quelle
hergeleitet; keine T1–T8-Promotion, keine endgültige TFPT-Lösung.
