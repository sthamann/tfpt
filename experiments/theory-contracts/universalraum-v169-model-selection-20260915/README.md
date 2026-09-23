# TFPT / Universalraum: v1.6.9 Modellselektion — 15. September 2026

Endliche, nichtarithmetische Forschungsrechnung. **Firewall:** dies ist ein
Theory-Contract-Experiment — **keine** Claims in `verification/`,
`status_ledger.csv`, Papern oder Website, keine Commits, keine Promotion,
kein RH-/Faktorisierungs-/P-vs-NP-Resultat. Kein T1–T8-Tor wird geschlossen.

## Fragestellung

Paket 2 des v1.6.9-Arbeitsauftrags: Entscheidung Selektion vs Unterbestimmtheit
für TFPT/Universalraum. Formulierung der zulässigen Modellklasse und Lieferung
EINES von drei Ergebnissen: (a) Eindeutigkeit modulo definierter
operationeller Äquivalenz, (b) ein explizites physikalisch unterscheidbares
Gegenmodellpaar mit dem exakten unterscheidenden Experiment, oder (c) eine
präzise lokalisierte offene Fortsetzungsbedingung.

## Dateien

- `model_selection.py` — Prüfer: Modellklassenspezifikation, beide inverse
  Tests (I₄ = 1+c⁴; Q = (1/960)Tr_intern(8I−G_C^(3))), Selektionsfrage,
  Äquivalenzcheck, Phasensensitivität. Exakte Arithmetik (Fraction/int64).
- `replay.py` — führt den Prüfer normal und unter `-OO` aus; verlangt
  Byteidentität (bis auf Laufzeitfelder).
- `RESULTS.md` — vollständiger Bericht (deutsch; Label
  exakt/numerisch/bedingt/offen).
- `replay_manifest.json` — Status und Hashes.

## Reproduktion

```sh
cd experiments/theory-contracts/universalraum-v169-model-selection-20260915
/opt/homebrew/bin/python3 replay.py
```

NumPy wird benötigt. Kein Zugriff auf Dateien außerhalb des Repositorys; der
native W-Tensor wird in-repo rekonstruiert und per SHA-256 gegen die
gepinnten `native_source.py`-Werte abgesichert. Kein Commit, kein Push.
