# Source operator origin

Theory contract `UR.SOURCE.OPERATOR_ORIGIN.01`, 2026-09-20.

**PARTIAL.** [Ergebnis und Beweisgrenzen](ERGEBNIS.md).

Der unveränderte native 64CAR/60CCR-Quellraum hat eine triviale diagonale Spin10×SU4-Zentrumwirkung. Das gemeinsame T(D8)-Randwörterbuch identifiziert dieselbe Wirkung mit Fermionparität. Daher kann kein equivarianter Transfer ein ungerades lokales Randfeld nichttrivial in diese native Operatoralgebra abbilden. Der ursprüngliche Clifford-Übergang mit zusätzlichem6-Bein existiert vor der Familienkompression, verschwindet jedoch nach der tatsächlich verwendeten geraden Projektion. Rotor- und Half-Deck-Alternativen liefern den fehlenden Feld-/Zeittransfer ebenfalls nicht in ihrer derzeitigen Form.

Firewall: ausschließlich Theorieexperiment. Keine empirische Evidenz, kein vN-/Ledger- oder Paper-Upgrade, keine Behauptung einer vollständigen Lösung. Der Ausschluss gilt für das festgehaltene Quellen- und Gruppenwörterbuch.

Reproduktion: `python3 -B checker.py`, danach `python3 -B -OO checker.py`. Benötigt die gepinnten lokalen TFPT-Originalquellen, SymPy, NumPy und SciPy. Der Checker verifiziert Pins und führt die drei gezielten Rechenpakete aus; er vergleicht jeweils normale und optimierte Ergebnisse.
