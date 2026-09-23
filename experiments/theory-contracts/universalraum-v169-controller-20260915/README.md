# v1.6.9-Controller: autonomer Zb-Eingriff im selben System — 15. September 2026

Endliche, nichtarithmetische Forschungsrechnung (NON-RH). **Firewall:** dies
ist ein Theory-Contract-Experiment — **keine** Claims in `verification/`,
`status_ledger.csv`, Papers oder Website, keine Commits, keine Promotion.
Der hinzugefügte Controller ist **bedingte** Machbarkeit (Herkunft
unerklärt); das einzige fehlende Primitiv wird explizit benannt.

## Fragestellung

Arbeitspaket 4 der v1.6.9-Bestellung: den Bosonimpuls Z_b = e^{iπN_b} und
einen neutralen Recorder als **einen** zeitunabhängigen Gesamt-Hamilton
H_tot auf System × Controller × Zeiger realisieren — ohne externen
Schalter, mit vollständiger Ressourcenbilanz.

## Dateien

- `native_source.py` — byteidentische Kopie der npz-freien Quelle
  (SHA-256 `380577f8…`); Fremdordner werden nie verändert.
- `model_core.py` — deterministische float64-Konstruktion: K3-Operatoren,
  die drei Arm-Unitaren, H_tot (18 Dim., blockdiagonal über dem
  Controller-Switch), partielle Spuren. Keine Guards, nur Builder.
- `check_closed_model.py` — Prüfer 1: exakte Stern→K3-Reduktion,
  Zb-Algebrazugehörigkeit, Recorder-Identitäten, H_tot-Struktur,
  Operator-Gleichheit der Zweige (universeller Umfang).
- `check_evolution_resources.py` — Prüfer 2: autonome Evolution aller
  Arme unter dem einen H_tot, v1.6.9-Statistiken, Energiebilanz,
  Zeiger-/Kohärenzkonten, Zeitkovarianz-Zeuge, Präparationsladung.
- `RESULTS.md` — vollständiger Bericht (deutsch; Label
  exakt/numerisch/bedingt/offen).
- `replay_manifest.json` — Status beider Prüfer; normale und optimierte
  (`-OO`) Ausführung müssen bis auf Laufzeitfelder byteidentisch sein.

## Reproduktion

```sh
cd experiments/theory-contracts/universalraum-v169-controller-20260915
/opt/homebrew/bin/python3 replay.py
```

NumPy, SciPy, SymPy werden benötigt. Maßgeblich sind die PASS-Ergebnisse
und die Byteidentität in `replay_manifest.json`.
