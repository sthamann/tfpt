# Ergebnisse · Fixpunkt-Ward-Suche auf drei Frontier-Ziele

Lauf vom 17. September 2026. `checks: 37/37 passed`, Exit 0, Laufzeit ~46 s.
Verdicts: **KOIDE-Q `TRIVIAL_FROM_EXISTING_E` · HIGGS-QUARTIC `NO_CANDIDATE` ·
MPME-CROSS `NO_CANDIDATE`.**

Ausgangslage: Das α⁻¹-Template (`verification/v3_em_alpha.py`, EM.FP.01 [E] —
Template-Selbsttest reproduziert α⁻¹ = 137.0359992168407 exakt) wurde mit
derselben eingefrorenen Methodik wie im Vorgänger-Contract
`fixpoint-ward-mpratio-20260917` auf drei Frontier-Ziele angewendet (Pool 794
aus 26 deklarierten Atomen, Toleranz rel. 10⁻⁶, je 200 Surrogate-Familien,
Seed 20260917, Schwelle p < 0.01).

## Ziel 1 · KOIDE-Q (x* = 2/3 = |ℤ₂|/N_fam) — `TRIVIAL_FROM_EXISTING_E`

**Reale Familie (N = 18 283 438, Ward 18 282 644):**

| Klasse | Flagged im Toleranzfenster | Davon exakte Identitäten (trivial) | Nichttriviale Kandidaten |
|---|---|---|---|
| W0 Baseline | 1 | 1 (x = 4/3·1/2 = 2/3 — die |ℤ₂|/N_fam-Lesart) | — |
| W2 quadratisch | 16 | 16 | 0 |
| W3 Log-Seam | 0 | 0 | 0 |
| W4 Seam-Log | 0 | 0 | 0 |
| W1 kubisch | 2 | 2 | 0 |

Alle 18 Ward-Treffer verschwinden **exakt** an x* = 2/3 (|F(2/3)| < 10⁻⁸⁰ in
dps-100-Arithmetik) — sie sind Restatements der Atom-Arithmetik des Targets,
z. B. `x² − (16/240) x − (2/5) = 0` oder `x² − (8/48) x − (1/3) = 0`. Es gab
**null** nichttriviale Gleichungen im Toleranzfenster; nichts zu zertifizieren.

**Near-Misses (Berichtfenster 10⁻⁴, keine Treffer):** 118, die besten:

| Klasse | Gleichung | Wurzel | rel. Abweichung |
|---|---|---|---|
| W1 | x³ − (3/26·4/3) x² − (φ₀/10) x − λ_Y = 0 | 0.6666673843 | 1.076·10⁻⁶ |
| W1 | x³ − (34/47·3/26) x² − (55/117/9) x − λ_Y = 0 | 0.6666655901 | 1.615·10⁻⁶ |
| W1 | x³ − (2/248) x² − (41/10/40) x − λ_Y = 0 | 0.6666646203 | 3.070·10⁻⁶ |
| W3 | x − (7/6/34/47) − (2·7/6) ln x = 0 | 0.6666693950 | 4.093·10⁻⁶ |

(Zum Kontext: der PDG-Polwert Q_pole = 0.6666644634 liegt 3,305·10⁻⁶ relativ
neben 2/3 — außerhalb der Toleranz, mitten im Near-Miss-Bereich.)

**Nullbatterie (200 Familien):** Ward-Treffer **1792 / 3 596 217 790**
Surrogate-Gleichungen → Rate **4,983·10⁻⁷ pro Gleichung** (quad 1072, log 15,
seam 7, cubic 698); Baseline 158/156 302; **198 von 200** Zufallsfamilien mit
≥ 1 Treffer (max 33). Die Rate liegt 33× über der des m_p/m_e-Vorgängers —
ein einfach-rationales Target wie 2/3 zieht Zufallstreffer an (inkl.
exakt-rationaler Koinzidenzen; die Rate ist damit eine obere Schranke an die
nichttriviale Rate, der Test konservativ). **λ = 9,11027** — ein Einzeltreffer
hätte p ≈ 0,9999 gehabt; selbst ein nichttrivialer Fund wäre
`CANDIDATE_BUT_LOOK_ELSEWHERE` gewesen (erst k ≥ 17 Treffer wären scharf).

**Einordnung:** Q = 2/3 ist **kein neuer Fixpunkt**, sondern exakt die
deklarierte Compiler-Lesart |ℤ₂|/N_fam — die einzigen "Ward-Wurzeln" bei 2/3
sind atom-arithmetische Identitäten. Die [E]-Leptonmassen geben
Q_source = 0.6644638161; der Abstand zum Target bleibt der bekannte
source→pole-Transfer (FR.POLE.SOLVE.01), keine Selbstkonsistenzgleichung
dieser Komplexitätsklasse.

## Ziel 2 · HIGGS-QUARTIC (x* = |λ(M̄_Pl)| = 0.0024287567882036172, v166 2-loop) — `NO_CANDIDATE`

**Reale Familie (N = 18 283 438; eingefrorene Magnituden-Schranken im Probe
gecheckt: x² < min Pool ⇒ W2 vakuum, x³ < min Atom ⇒ W1 vakuum; effektiver
Ward-Raum Log + Seam, N_eff = 1 260 872):** **null** Treffer im
Toleranzfenster — keine Baseline, keine Ward-Gleichung, keine exakte
Identität. Nichts zu zertifizieren.

**Near-Misses (Berichtfenster 10⁻⁴, keine Treffer):** 2, die besten:

| Klasse | Gleichung | Wurzel | rel. Abweichung |
|---|---|---|---|
| W3 | x − (48/λ_Y) − (41/10/3/26) ln x = 0 | 0.002428760219 | 1.413·10⁻⁶ |
| W3 | x − (41/10/7/6) − (7/6·1/2) ln x = 0 | 0.002428877638 | 4.976·10⁻⁵ |

**Nullbatterie (200 Familien):** Ward-Treffer **4 / 253 147 370** → Rate
**1,58·10⁻⁸ pro Gleichung** (alle in der Log-Klasse); Baseline 1/157 909;
3 Familien mit ≥ 1 Treffer (max 2). **λ = 0,0199231** — die Batterie wäre
scharf genug gewesen: zwei zertifizierte Treffer hätten p < 0.01 erreicht
(einzelner: p ≈ 0,0197 → `CANDIDATE_BUT_LOOK_ELSEWHERE`).

**Einordnung:** Die 2-loop-Near-Kritikalitäts-Residualgröße |λ(M̄_Pl)| ist in
dieser Komplexitätsklasse **keine** Ward-Wurzel aus Compiler-Atomen. Die
freie-Seam-Doppelbedingung λ(M_seam) = β_λ(M_seam) = 0 (v166, [E]-Signatur)
bleibt die strukturelle Aussage; der numerische Residualwert (ein
Transfer-Output mit gemessenen (m_H, m_t)-Inputs) trägt keine verborgene
Fixpunktform.

## Ziel 3 · MPME-CROSS (x* = 1836.15267343, CODATA 2022) — `NO_CANDIDATE`

Neue Gleichungsklasse mit der Residuenmatrix R als Matrix (p_R(x) =
det(xI − R) = x³ − 9x² + 10x − 8; R-Selbsttests im Probe: det 8, tr 9,
Minoren {2,3,5}, SNF (1,1,8) via gcd, ρ_R = 7,8568175371…, komplexes Paar,
E(x) streng wachsend auf dem Zweig). **Reale Familie (N = 1 892 102, Ward
1 891 308):** **null** Treffer im Toleranzfenster (Baseline 0, X1 0, X2 0,
X3 0). Nichts zu zertifizieren.

**Near-Misses (Berichtfenster 10⁻⁴, keine Treffer):** 2, die besten:

| Klasse | Gleichung | Wurzel | rel. Abweichung |
|---|---|---|---|
| X3 | (x − 10/φ₀)·p_R(x)/x³ − (40·41) = 0 | 1836.142356 | 5.619·10⁻⁶ |
| X3 | (x − 8·78)·p_R(x)/x³ − (48/c₃) = 0 | 1836.309678 | 8.551·10⁻⁵ |

**Nullbatterie (200 Familien):** Ward-Treffer **17 / 377 416 977** → Rate
**4,504·10⁻⁸ pro Gleichung** (x1 0, x2 5, x3 12); Baseline 0/157 261;
10 Familien mit ≥ 1 Treffer (max 4). **λ = 0,0851902** — scharf genug, dass
ein Einzeltreffer ohnehin Look-elsewhere geblieben wäre (p ≈ 0,082 ≫ 0,01),
zwei Treffer wären grenzwertig; es gibt keinen einzigen.

**Einordnung:** Auch die cross-sector Klasse mit expliziter Residuenmatrix —
Resolventen-Kubik, resolventen-gedressierter Transmutations-Logarithmus,
faktorisierte Produktform (EW-Seite × QCD-Resolvente), alle mit analytischer
Eindeutigkeit auf dem reellen Zweig x > ρ_R — trägt m_p/m_e **nicht**.
Zusammen mit dem Vorgänger (18,3M Gleichungen, 0 Treffer) ist das die zweite
eingefrorene Negativität: die F_QCD-Externals (α_s(M_Z), Lattice-C_p,
FR.QCD.BUDGET.01 [C]/[N]/[X]) sind auch durch R-matrix-gekoppelte
Ward-Identitäten dieser Form nicht ersetzbar. m_p/m_e bleibt eine
`F_transfer`-Brücke — kein Compiler-Fixpunkt.

## Gesamt

Kein Upgrade, kein [E]-Sprachgebrauch, keine Änderung an verification/,
Ledger, Papers, Website oder Scorecard. Ehrliche Nullen auf Higgs und
Cross-Sector; die Koide-Antwort präzisiert die bekannte Lesart (Target =
|ℤ₂|/N_fam trivial, Transfer bleibt die offene [C]-Frage).

## Reproduktion

```sh
cd experiments/theory-contracts && python3 fixpoint-ward-frontier-20260917/fixpoint_ward_frontier.py
```

Erwartete Endzeilen: `checks: 37/37 passed`, dann die drei Verdicts wie oben.
