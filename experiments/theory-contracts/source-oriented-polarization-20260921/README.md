# Gerichtete Quellenrekonstruktion

`UR.SOURCE.ORIENTED_POLARIZATION.01` — **PARTIAL**, 2026-09-21.

Der echte skalare DtN und die Randorientierung bestimmen ker(Λ+i∂s), also die holomorphe Randalgebra. Der originale positive additive v210-Ansatz besteht diesen skalaren Ursprungstest nicht. Für tatsächlich über die Scheibe fortsetzbare untwisted Spinorfelder folgt die NS-Polarisierung konstruktiv; die Identifikation der geladenen P1-Felder mit diesen Sektionen sowie der ursprünglichen Zeit fehlen.

Beweis, Voraussetzungen und genaue Originalstellen: [PROOF.md](PROOF.md).
Unabhängiger mathematischer Review: [independent_review.md](independent_review.md).
Mitwandernde Analyse des vorhandenen Kandidaten: [recentered_source.md](recentered_source.md).

Reproduktion vom Repository:

```sh
python3 -B experiments/theory-contracts/source-oriented-polarization-20260921/checker.py
python3 -B -OO experiments/theory-contracts/source-oriented-polarization-20260921/checker.py
```

Abhängigkeiten: numpy, sympy; der getrennte Rezentrierungsprüfer braucht außerdem mpmath. Quellen sind SHA256-gepinnt. Endliche Checks ersetzen keine unendlichdimensionalen Beweise. Research-Firewall: keine empirische Scorecard, keine Änderung an Originalprüfern/Papers/Ledger, keine physische Gate-Schließung oder vollständige TFPT-Lösung.
