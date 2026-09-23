# Universalraum-Fundamental — opset- und GS-Repro-Sanity-Sonden

Datum: 15. September 2026. Endliche, nicht-arithmetische Forschungsfortsetzung
im Anschluss an `universalraum-v16-integrated-20260915`, `universalraum-minimal-followups-20260915`
und `universalraum-relational-hole-20260915`. NON-RH-Forschung.

## Firewall (bindend)

- **Search target, kein Claim.** Die beiden Sonden prüfen reproduzierbar
  numerische Strukturdaten der gepinnten nativen Quellen. Sie begründen keine
  neue Vermutung, kein T1–T8-Tor und keine Zustandsauswahl.
- **Verdict-Enums.** Jede Sonde endet mit `PASS` / `FAIL` / `STUB` /
  `INFEASIBLE`. Kein Status wird stillschweigend aufgewertet.
- **Kein `[E]`.** Kein Ergebnis wird als load-bearing markiert. Kein Eintrag
  in `status_ledger.csv`, keine `\veri{}`-Zitate, keine Promotion nach
  `verification/`.
- **Out of Scorecard.** Kein `evidence_scorecard.json`-Eintrag, kein
  `predictions.ts`-Sync, keine `experiments/evidence`-Zeile.
- **NON-RH.** Keine RH-Aussage, keine RH-Runde, kein `rh/`-Sync.
- **Keine Edits an** `verification/`, `papers/`, `website/`, Ledger,
  Changelog, Manifeste. Nur dieser Ordner wird angelegt.
- **Quellen schreibgeschützt.** `native_tensor.npz` (SHA-256
  `3f00a0892157a691e4ef26920c3702772c7bf76a250fad98ff04a079bb64b763`)
  wird nur gelesen. Keine Datei außerhalb dieses Ordners wird verändert.

## Sonden

1. **`opset_probe.py`** — Operator-Satz-Sonde auf dem kleinsten Sektor (N=3).
   Lädt W aus `native_tensor.npz`, falls verfügbar; sonst synthetischer
   `WW†=8I`-Stub mit explizitem `STUB`-Marker. Baut X, N_b als Sparse-Operatoren
   auf dem N=3-Sektor (dim aus `native_three.py`: 41664 + 3840 = 45504),
   berechnet dim A_3 (Kontrollalgebra) und die Kommutant-Dimension vs F(N),
   testet den modeweisen N_b/A-Split (E1) gegen die gepinnten W-Reihen.
2. **`gs_sanity_probe.py`** — Grundzustands-Repro-Sanity. Reproduziert die
   H_μ-Schranke (g=Δ/20, μ=Δ/50 ⇒ H_μ ≥ ΔN/800), das helle E_- bei μ=0,
   die Prüfloch-Bedingung E_- > 0 für 0 < g/Δ < 1/√8, das N=3-Gram-Spektrum
   {0,7,10,12} und dimensioniert den N=64-Singulett-Sektor (nur Count-/
   Memory-Schätzung, keine volle Diag bei >RAM).
3. **`t1_fixed.py`** (16/16 PASS) — T1-Algebra-Abschluss: so(10) aus
   Fermion-Bilinearen auf dem geraden Unterraum (Span 45, Lie-Abschluss mod
   Zentrum mit ganzzahligen CAR-c-Zahlen, 16-dim irreduzibel), su(4) Span 15
   irreduzibel (Index-Map I=4s+a ASSUMED), B(C^64) per Doppel-Kommutantensatz
   (analytisch, kein 16-GB-Kronecker), q-Verdikt YES (Wort in erweiterten
   Generatoren), N=3-Kommutantenschranke 8.732.673 ≫ F(N)=1.
4. **`stabilizer.py`** — Echter W-Stabilisator-Test (kanonische Zeilenform,
   60 distinkte Zeilen): innerer 4er-Zyklus ist exakter Automorphismus 60/60
   (Z4-Familiensymmetrie, bedingt auf Index-Map; Zirkularität möglich falls W
   mit dieser Symmetrie konstruiert wurde); Shifts/Slot-Swap keine (30/6/12/18
   von 60 Zeilen).
5. **`t5_twobank.py`** (6/6 PASS) — Zwei-Bank-H_A exakt: (H³)_{4,1}=8g²η,
   niedrigere Potenzen null, P_{1→4}-Maximum 0.9989 bei t≈2484 ħ/Δ
   (g/Δ=0.05, η/Δ=0.1), eig [-0.0217,-0.0179,0.9217,1.1179],
   Kegel-Lemma F'_+=F'_- ⟺ ε=0.
6. **`t5_varresp.py`** — Geladene Antwort auf N=64-Variationszustand
   |ψ⟩=0.9905|F⟩−0.1374|B⟩ (E=−0.0196Δ, ⟨Nb⟩=0.0189, exakte JW-Vorzeichen):
   G_rs diagonal, 16 Moden depletiert (min 0.9976), off-diagonal exakt 0,
   Spur=⟨Nf⟩=63.962. BEDINGT (Variation, kein GS).

## Reproduktion

```bash
python3 -B opset_probe.py
python3 -B gs_sanity_probe.py
```

NumPy, SciPy, SymPy werden benötigt. Output wird mit
`rg -n "FAIL|ERROR|dim|E_-|bound|OK|STUB|INFEASIBLE|PASS"` reduziert.

## Status

Siehe `STATE`-Block im Chat. Kein Commit, kein Push, kein PDF-Update.
