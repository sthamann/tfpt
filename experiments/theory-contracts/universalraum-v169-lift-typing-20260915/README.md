# v1.6.9 Lift-Typisierung — getypte Quell-Träger-Audit · 15. September 2026

Endliche Forschungsrechnung (NON-RH). **Firewall:** Theory-Contract-Experiment —
**keine** Claims in `verification/`, `status_ledger.csv`, Papers oder Website,
keine Commits, keine Promotion. Paket 1 des v1.6.9-Arbeitsauftrags: typisierte
Audit der Quell-Träger-Verbindung (Darstellung / Γ-Lift / dΓ / Instrument),
exakte Multiteilchen-Unterscheidungen, vollständiger aufgezeichneter kleiner
Versuch auf einem Träger, beide Stabilisatoren, Ausführbarkeitsklassifikation.

## Dateien

- `native_source.py` — byte-gepinnte In-Repo-Quelle (SHA-256 `380577f8…`,
  Kopie aus `universalraum-operations-groundstate-20260915`; rekonstruiertes
  W: `7a4a0b1c…`; der externe npz-Pin `3f00a089…` wurde in früheren Runden
  byte-exakt gegengeprüft und wird hier nicht gelesen).
- `check_source_side.py` — die sieben C³-Quellwörter (49 Produkte, 7-dim.
  Algebra, †-Vervollständigung M₃), die 60 C⁴-Gaußstrahlen (Überlappungen
  {0,1/4,1/2,1}), die Regressionen tr(Π₀Π₁Π₂) = (1−i)/4 und der
  Reflexionswort-Zeuge (Antworten 1 und 0).
- `check_multiparticle.py` — dΓ(AB) ≠ dΓ(A)dΓ(B) (ein Eintrag +1; nativer
  Lie-Zeuge 3968), Π²=Π ⇏ dΓ(Π) Projektor (Eigenwert 2 auf dem Saatpaar),
  Γ(UV) = Γ(U)Γ(V) (49 Paare + 6 Clockpotenzen, exakt).
- `check_recorded_experiment.py` — der vollständige v1.6.9-Versuch auf K₃:
  beide Arme, alle Ergebniswahrscheinlichkeiten, neutraler Zeiger mit
  explizitem Koppler, Paarkohärenz-Erhalt, exakter Halbeffekt, Δ/54 und
  Δ/108; unabhängiges numerisches Replay auf dem 9-dimensionalen nativen
  Stern.
- `check_process_symmetry.py` — Stabilisatoren von W allein (768 / 4608 /
  Lie 60) gegen den vollen markierten Prozess (4 / 8 / Lie 34);
  Clock-Intertwiner und Vereinigungsrang 60; Ausführbarkeitszeugen
  (n_r = dΓ(e_rr), Z_b = Γ_b(−I), [n₄,WᵀW] mit 210 Nichtnullen,
  Spin-1-Kommutant-Gegenzeuge).
- `replay.py` / `replay_manifest.json` — Status; normale und optimierte
  (`-OO`) Ausführung müssen bis auf Laufzeitfelder byteidentisch sein.
- `RESULTS.md` — vollständiger Bericht (deutsch; Label
  exakt/numerisch/bedingt/offen).

## Reproduktion

```sh
cd experiments/theory-contracts/universalraum-v169-lift-typing-20260915
/opt/homebrew/bin/python3 replay.py
```

Benötigt werden Python 3, NumPy, SciPy, SymPy. Laufzeit ≈ 25 s. Der
Clock-Konstruktor wird aus dem gepinnten In-Repo-Pfad
`experiments/theory-contracts/compiler-involution-types/checker.py`
(SHA-256 `9bf99de7…`) gelesen; abweichende Hashes brechen den Lauf.
Statusdateien starten mit RUNNING und werden bei Fehlern auf FAIL gesetzt.
