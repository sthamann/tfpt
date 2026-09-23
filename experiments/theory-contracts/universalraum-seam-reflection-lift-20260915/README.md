# Seam-Spiegelung: gemeinsame Wirkung auf Fermionorte und Paarübergänge

Abgetrennter Forschungsordner. Keine neuen Hamiltonterme, keine Änderung fremder
Quellen, keine Beförderung nach `verification/`, kein T1–T8-Abschluss.

Beantwortet die in v1.6.10 als Priorität benannte Frage: liefert die ursprüngliche
TFPT-Seam genau die gemeinsame Spiegelungswirkung, die Fermionorte, Paarübergänge
und Zustand verbindet? Der Auswahlsatz von v1.6.10 hatte diese Wirkung als Prämisse
gesetzt und `raw-seam to vertex/edge action` ausdrücklich als nicht hergeleitet
geführt.

- `seam_reflection_lift.py`: die Hauptfrage, vier Teile. 331 exakte Bedingungen.
- `open_points_closure.py`: die vier Strukturpunkte, die der erste Lauf offen ließ —
  Bankplatzierung, vollständige Quellklasse, die beiden Clocks und die Seam-Lokalität.
  60 exakte Bedingungen. **Punkt P3 darin ist zurückgezogen** (die Suche stimmt, die
  Folgerung nicht) und wird ersetzt durch:
- `native_mu4_clock.py`: der μ4-Clock mit negativem Lift im Cartan-Torus von W.
  25 exakte Bedingungen. Reihenfolge beim Lesen: Hauptlauf, Strukturpunkte, dann
  diese Korrektur.
- `RESULTS.md`: technischer Bericht mit den exakten Größen.
- `*_normal.json` / `*_optimized.json`: byteidentische Läufe.

## Reproduktion

```sh
python3 experiments/theory-contracts/universalraum-seam-reflection-lift-20260915/seam_reflection_lift.py
python3 experiments/theory-contracts/universalraum-seam-reflection-lift-20260915/open_points_closure.py
python3 experiments/theory-contracts/universalraum-seam-reflection-lift-20260915/native_mu4_clock.py
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
