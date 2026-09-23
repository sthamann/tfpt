# Ergebnisse · Fixpunkt-Ward-Suche für m_p/m_e

Lauf vom 17. September 2026. `checks: 12/12 passed`, Exit 0, Laufzeit ~33 s.
**Verdict: `NO_CANDIDATE`.**

Ausgangslage: Das α⁻¹-Template (`verification/v3_em_alpha.py`, EM.FP.01 [E] —
α⁻¹ als eindeutige Wurzel der U(1)-Ward-Identität F_U(1) = 0, Intervall-
zertifiziert) wurde auf die Cross-Sector-Ratio m_p/m_e = 1836.15267343
(CODATA 2022) übertragen: eine endliche, vorab eingefrorene Familie
Ward-artiger Selbstkonsistenzgleichungen über den 26 deklarierten
Compiler-Objekten, mit Look-elsewhere-Nullbatterie. Der Template-Selbsttest
reproduziert α⁻¹ = 137.0359992168407 exakt — die Maschinerie ist dieselbe
wie in v3.

## 1 · Eingefrorener Suchraum (wie präregistriert)

Pool: 26 Atome → Paarprodukte/-quotienten → exakte Deduplikation:
**N_POOL = 794**. Klassen: W0 Baseline 794; W2/W3/W4 je 630 436; W1 kubisch
16 391 336. **N_TOTAL = 18 283 438 Gleichungen** (Ward-Klassen 18 282 644).
Toleranz rel. 1·10⁻⁶ (Halbfenster 0.00183615267343).

## 2 · Reale Familie: kein Treffer

| Klasse | Gleichungen | Flagged im Toleranzfenster | Zertifizierte Kandidaten |
|---|---|---|---|
| W0 Baseline | 794 | 0 | — |
| W2 quadratisch | 630 436 | 0 | 0 |
| W3 Log-Seam | 630 436 | 0 | 0 |
| W4 Seam-Log (v3-Lift) | 630 436 | 0 | 0 |
| W1 kubisch | 16 391 336 | 0 | 0 |

**Keine** der 18 283 438 Gleichungen hat eine Wurzel innerhalb rel. 10⁻⁶ von
1836.15267343. Es gab nichts zu zertifizieren.

## 3 · Near-Misses (Berichtfenster rel. 10⁻⁴, keine Treffer)

8 Gleichungen mit Wurzeln im Berichtfenster, die besten:

| Klasse | Gleichung | Wurzel | rel. Abweichung |
|---|---|---|---|
| W4 | x − (7/6/λ_Y) − (8·78)·ln(1/φ_seam(1/x)) = 0 | 1836.15684854 | 2.274·10⁻⁶ |
| W3 | x − (4·240) − (248·55/117)·ln x = 0 | 1836.15788786 | 2.840·10⁻⁶ |
| W4 | x − (40·41) − (78/(7/6))·ln(1/φ_seam(1/x)) = 0 | 1836.17399092 | 1.161·10⁻⁵ |

Der beste Near-Miss verfehlt die Toleranz um Faktor 2.3 — und hätte selbst
bei Erreichen die Nullbatterie nicht bestanden (siehe §4).

## 4 · Nullbatterie (200 Surrogate-Familien, Seed 20260917)

- Ward-Treffer: **55 / 3 596 217 790** Surrogate-Gleichungen
  → Rate **1.529·10⁻⁸ pro Gleichung** (quad 1, log 8, seam 20, cubic 26).
- W0-Baseline: 0 / 156 302.
- **21 von 200** Zufallsfamilien haben ≥ 1 Ward-Treffer im Toleranzfenster;
  eine Familie erzeugte sogar **28** Treffer (zufällig auf x* geclusterte
  Koeffizienten) — ein Lehrstück in Look-elsewhere.
- Look-elsewhere-Erwartung für die reale Familie: **λ = 0.2796**.

Konsequenz, vorab eingefroren: ein einzelner realer Treffer hätte
p = 1 − e^(−0.28) ≈ 0.244 ≫ 0.01 gehabt → `CANDIDATE_BUT_LOOK_ELSEWHERE`.
Die Batterie war also scharf genug, um jeden Einzeltreffer dieser Familie als
Numerologie zu entlarven — und die reale Familie liefert nicht einmal einen.

## 5 · Einordnung (ehrlich)

- Das α⁻¹-Template (Fixpunkt/Selbstkonsistenz statt Dynamik) trägt m_p/m_e
  **nicht**: in der eingefrorenen Komplexitätsklasse (≤ 5 Atome pro
  Gleichung, 5 Ward-Formen inkl. des wörtlichen v3-Seam-Lifts) existiert
  keine Selbstkonsistenzgleichung mit Wurzel bei 1836.15267343.
- Das stärkt von innen die deklarierte Grenze (FIRSTPRINCIPLES.BOUNDARY.01):
  die zwei Externals des F_QCD-Transfers (α_s(M_Z), Lattice-C_p,
  FR.QCD.BUDGET.01 [C], FR.MPME.02) sind nicht durch eine verborgene
  Ward-Identität dieser Form ersetzbar. m_p/m_e bleibt eine
  `F_transfer`-Brücke — kein Compiler-Fixpunkt.
- Kein Upgrade, kein [E]-Sprachgebrauch, keine Änderung an verification/,
  Ledger, Papers, Website oder Scorecard.

## Reproduktion

```sh
cd experiments/theory-contracts && python3 fixpoint-ward-mpratio-20260917/fixpoint_ward_mpratio.py
```

Erwartete Endzeilen: `checks: 12/12 passed`, `VERDICT: NO_CANDIDATE`.
