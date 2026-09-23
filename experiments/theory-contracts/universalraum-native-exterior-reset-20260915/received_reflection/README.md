# Seam-Spiegelung: gemeinsame Wirkung auf Fermionorte und Paarübergänge

Abgetrennter Forschungsordner. Keine neuen Hamiltonterme, keine Änderung fremder
Quellen, keine Beförderung nach `verification/`, kein T1–T8-Abschluss.

Beantwortet die in v1.6.10 als Priorität benannte Frage: liefert die ursprüngliche
TFPT-Seam genau die gemeinsame Spiegelungswirkung, die Fermionorte, Paarübergänge
und Zustand verbindet? Der Auswahlsatz von v1.6.10 hatte diese Wirkung als Prämisse
gesetzt und `raw-seam to vertex/edge action` ausdrücklich als nicht hergeleitet
geführt.

- `seam_reflection_lift.py`: der vollständige Test, vier Teile.
- `RESULTS.md`: technischer Bericht mit den exakten Größen.
- `seam_reflection_normal.json` / `seam_reflection_optimized.json`: byteidentische Läufe.

## Reproduktion

```sh
python3 experiments/theory-contracts/universalraum-seam-reflection-lift-20260915/seam_reflection_lift.py
```

Benötigt Python, NumPy, SciPy, SymPy. Gepinnte Abhängigkeiten, beide über ihre
SHA-256 geprüft:

- nativer Tensor `experiments/theory-contracts/universalraum-v16-integrated-20260915/sources/native_tensor.npz`
- Clock-Konstruktor `experiments/theory-contracts/compiler-involution-types/checker.py`
- Hilfsmodul `universal_room/new-3/universalraum-v1.6.9/agents/source/inputs/native_common.py`

Die Seam-Ring-Geometrie ist unverändert die von `v480_multilocal_four_interval.py`
(N=256, vier μ4-symmetrische Intervalle, antiperiodisch).

Der Lauf endet mit `status: PASS` und der Zahl der bestandenen exakten Bedingungen.
Jede einzelne Bedingung bricht bei Verletzung sofort ab; es gibt keine weichen
Toleranzen außer den ausgewiesenen Maschinengenauigkeiten des freien Fermionrings.
