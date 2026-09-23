# Seam-Schließung: drei Restannahmen der Spiegelungsrunde — 15. September 2026

Endliche, nichtarithmetische Forschungsrechnung (NON-RH). **Firewall:** dies
ist ein Theory-Contract-Experiment — **keine** Claims in `verification/`,
`status_ledger.csv`, Papers oder Website, keine Beförderung.

Fortsetzung von `universalraum-seam-reflection-lift-20260915` (PASS, 331
Checks). Von dessen vier „nicht hergeleitet"-Punkten werden hier drei exakt
bearbeitet:

| Punkt | Ergebnis |
|---|---|
| Zweinachbar-Rahmen | Spiegelkovarianz ⇔ J U J = ±R^m U: nur spiegelsymmetrische Quellen (modulo Link-Eichung) überleben; link-lokal und link-überspannend bleibt exakt a = ±b. Rest der Annahme = Geometrie der Lücken. |
| Uhr 6 vs. Uhr 4 | Nicht gleich, aber exakt vereinigt: T = R ⊗ G_F hat Ordnung 24 mit **T¹² = −I** (binärer Lift einer C12); alle sechs gemeinsamen Spiegel invertieren T; ⟨T,S⟩ = binäre Diedergruppe, 48 Elemente; Boson-Uhr Ordnung 12 ohne −I. |
| Eine W-Bank pro Link | Uhr transitiv auf Links + Multiplizität eins der Bosondarstellung in Λ²(64) (Casimir-Annullator (C−56)(C−120)=0 exakt) ⇒ Bank nach Schur eindeutig; n Kopien = eine Bank mit g√n plus freie Zuschauerbänke (exakter Fock-Toytest) → Zuschauerverbot erzwingt n = 1. |

**Weiter offen (ehrlich):** physisches g/Δ (Ableitungsvertrag:
QGEO.KERNEL.01), gemeinsamer 3+1D-Ursprung (T3), chirales Maß (T4),
dynamischer Spin 2 (T7), rohe Seam → markierter Rand (QGEO.MARKS.01).
Kein T1–T8-Tor wird geschlossen.

## Dateien

- `seam_closure.py` — Checker (Teil A sympy-exakt, Teil B/C ganzzahlig/exakt;
  Fock-Toytest float64 mit 1e-9-Guard). 44 Bedingungen.
- `run_normal.json` / `run_optimized.json` — normale und `-OO`-Ausführung,
  byteidentisch. `status: PASS`.

## Reproduktion

```sh
cd experiments/theory-contracts/universalraum-seam-closure-20260915
/opt/homebrew/bin/python3 seam_closure.py
```

Benötigt NumPy, SciPy, SymPy sowie repo-lokal `native_common.py`
(v1.6.9-Quellpaket) und den gepinnten Tensor
`universalraum-v16-integrated-20260915/sources/native_tensor.npz`.
Kein Zugriff außerhalb des Repositorys.
