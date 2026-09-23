# universalraum-fugen-20260914 — die fünf gesetzten Fugen, gerechnet

NON-RH. Exploration (`experiments/`), keine Promotion: kein Marker in `verification/`,
Ledger, Papers oder Website bewegt sich durch diesen Ordner. T1–T8 bleiben offen.

Anschluss an `universal_room/tfpt_compiler_universalraum_2026-09-13.pdf`,
`universal_room/tfpt_anschluss_zellen_seam_2026-09-14.pdf` und
`universal_room/TFPT_UNIVERSALRAUM_INVERSION_2026-09-14.md`. Ergebnisdokument:
`universal_room/TFPT_UNIVERSALRAUM_FUGEN_2026-09-14.md`.

Gegenstand sind die fünf im Manuskript als *gesetzt* markierten Fugen:
λ (Zwischenzellkopplung), Kopplungsgraph, Cross-Register-Kopplung der Vor-Messung,
Präparation (Ω / Register), Zeitskala.

## Dateien

| Datei | Inhalt |
|---|---|
| `checker.py` | Exakte Prüfungen (27 288 Bedingungen, ~6 s): E8-Sektoren und Klammerkanäle, Vorzeichen des Austauschs (10 ⊂ Sym²(16) via expliziten so(10)-Gammamatrizen), Trägerkern K⁺K = I − S, Spinor-Nachbarschaftsgraph = Clebsch (16,5,0,2), vollständiger Graph N = 4m (Gap exakt 2J), Sektortrennung Zelle/Aufzeichnung auf den 15 gepinnten Quellkontexten, Bahnen der 240 CQ-Koordinaten gegen 240 Wurzeln, Z4-Glue-Klassen und (E8)₁-Charakter. Schreibt `validation.json`. |
| `clebsch_su4.py` | Numerik: SU(4)-Austausch auf dem Clebsch-Graphen (16 Träger, Schur–Weyl, dünnbesetzte Young-Orthogonalform als `LinearOperator`, alle 64 Irreps λ ⊢ 16 mit ≤ 4 Zeilen) und N-alitätssektoren des uniformen Rings n = 5…13. Schreibt `clebsch_su4.json`; `--quick` beschränkt auf Irreps ≤ 30 000. |
| `test_checker.py` | 14 Tests (unittest, auch unter `python -OO`): Kernzahlen, zwei Negativkontrollen (symmetrischer Kern, verschobene Kopplung), K4-Spektrum, Dimensionssumme 4¹⁶, Ring-Sektor gegen Schur–Weyl. |
| `validation.json`, `clebsch_su4.json` | Maschinenlesbare Ergebnisse. |

## Quellpin

`compiler-origin-audit-20260913/context_instrument.py`, SHA-256 `ba1da931…9e3995` (wie in
`record_composition.py` und `universalraum-inversion-20260914`). Der Prüfer bricht bei
Quelländerung geschlossen ab.

## Reproduktion

```sh
python3 -B checker.py validation.json          # ~6 s
python3 -B -m unittest test_checker            # 14 Tests
python3 -B clebsch_su4.py                      # Minuten bis Stunden, s. Log
```

Abhängigkeiten: numpy, scipy. Keine Änderung an Ledger, Papieren, Katalogen oder Indizes.
