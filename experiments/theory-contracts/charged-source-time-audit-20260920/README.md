# Geladener Anschluss, Quellzeit und Clocks

20. September 2026 · **UR.SOURCE.CHARGED_TIME.01 · PARTIAL**

Der vorgeschlagene Übergang von Fermionströmen zur E8-Sektorerweiterung
wurde gegen die Originalquellen und mit unabhängigen Rechnungen geprüft.
Der maßgebliche Befund: Zahlenerhaltende Ströme sehen den tatsächlichen
Quellterm `-Qtotal/4` nicht. Paarströme und Halbspinorfelder sehen ihn.
Ihre geladenen Frequenzen und die tatsächlichen C/J-Wirkungen müssen deshalb
im selben Quellenprozess geprüft werden.

Die Klebeisometrie, Halbverdrehung und das verschobene E8-Zielspektrum sind
bereits in älteren Contracts vorhanden. Hier werden sie reproduziert und
mit dem aktuellen Vorschlag verbunden, nicht als neue Entdeckungen ausgegeben.

- [Vollständige Herleitung und Einordnung](PROOF.txt)
- [Unabhängige CAR-Stromprüfung](CAR_PROOF.txt)
- [Unabhängige Prüfung der Holonomie und Clockinterpretation](HOLONOMY_REVIEW.txt)
- [Exaktes Zertifikat](certificate.json) und [CAR-Ergebnisse](car_results.json)
- [Quellenbindungen](source_manifest.json)

Die rationalen C/J-Matrizen wurden auf demselben E8-Gitter mit dem vererbten
Ladungskokzyklus geliftet. Die gewählten Lifts erhalten ihre Ordnungen 30
und 4. Unter der verschobenen Zeit sind ihre zusätzlichen Transportphasen
explizit. Dieser Heisenbergtransport ist keine neue erhaltene Symmetrie.

Ein exakter Gegenzeuge trennt außerdem ausgelassene geladene Klammerpfade
von dynamischem Gedächtnis: Selbst bei identischem Projektor Q kann
`PAQBP-PBQAP` ungleich null sein, während `PHQ=0` und damit Selbstenergie
und Gedächtniskern verschwinden. Die gemeinsame-Q-Hypothese braucht daher
die tatsächlich gemeinsamen Kopplungsoperatoren.

## Reproduktion

Im Contract-Ordner:

```sh
python3 checker.py --output certificate.json
python3 -OO checker.py --output certificate_optimized.json
python3 car_audit.py
python3 -OO car_audit.py --output car_results_optimized.json
```

Abhängigkeiten: Python 3 und SymPy. Die beiden Ausführungsarten erzeugen
identische Ergebnisse. Die endlichen algebraischen Prüfungen verwenden
exakte Zahlen; die zusätzlich gespeicherten Sinusdispersion-Stichproben
sind numerische Illustrationen unabhängig bewiesener Schranken.

## Forschungsgrenze

Dieser Contract bleibt eine Theorieuntersuchung unter `experiments/`.
Er leitet weder acht Quellkanäle noch das mikroskopische Halbspinorfeld aus
P1/P2 her. Der Dreiquellenblock wird bestätigt, sein vollständiger globaler
Komplementboden hier nicht neu bewiesen. Keine Änderung an Ledger,
Verifikationssuite, Publikationspapieren oder T1–T8; keine empirische
Scorecard und kein TOE-Abschluss.
