# Quellenfrage: Konformalklasse, DtN und Zustandsauswahl

**PARTIAL**, 21. September 2026. Forschungscontract
`UR.SOURCE.CONFORMAL_KERNEL_SELECTION.01`, ohne Ledger-Promotion.

`PROOF.md` enthält die exakten Beweise und ihre Domänen. `checker.py`
prüft die algebraischen Zeugen und ruft die ursprünglichen v210/v290-
Operatoren unverändert auf. `source_pins.json` fixiert die gelesenen
Originalstände; `results.json` enthält den geprüften Lauf.

```sh
python3 -B experiments/theory-contracts/source-conformal-kernel-selection-20260921/checker.py
```

Die neue positive Reduktion: Im skalaren potentialfreien 2D-Fall ist die
Randenergie in der Konformalklasse bereits eindeutig, ohne eine flache
Innenmetrik physisch auszuwählen. Ein selbstadjungierter DtN-Operator
braucht zusätzlich die Randdichte. Die vorliegende v210-Medianwahl
rekonstruiert auf fest identifizierten Fouriermoden keinen gerichteten
chiralen Zustand; auch beim tatsächlichen positiven Viermarkenprofil
konvergiert ihre Kovarianz stark gegen null.

Erfolgskriterium der Prüfung war eine zielunabhängige Quellenauswahl auf
derselben ursprünglichen Algebra, Domäne und Zeit. Abbruchkriterium für
einen vermeintlichen Selektor war eine unzulässige DtN-Identifikation
oder ein falscher Grenzwert unter der bestehenden Modenidentifikation.
Die ursprünglichen endlichen Symmetriechecks bleiben gültig.

**Firewall:** Experimentelle Theorieprüfung, keine neue physische Quelle,
keine Identifikation neutraler und geladener Korrelatoren, keine
T1–T8-Schließung und kein E8-Zielimport. Die fehlende geladene Feldalgebra,
Polarisation und Zeitwirkung dürfen nicht nachträglich eingesetzt werden.
