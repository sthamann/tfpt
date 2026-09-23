# TFPT Universalraum — Konsolidierung + TOE-Rechnungen (2026-09-14)

Stand: 14.09.2026, Quelle: `tfpt-theoryv4/universal_room/` (16 Dateien: 13× `.md`, 3× `.pdf`, 1× `.zip`).
Status: Forschungsstand, T1–T8 offen, NON-RH, keine `verification/`-Promotion (vgl. `universal_room/README.md`).
Dieses Dokument fasst Konsolidierung **und** heutige Nachrechnungen (`/tmp`, Repo nur gelesen) zusammen.

## 1. Inventar

| Schicht | Dateien |
|---|---|
| A. Fragmente | `Analyse_und_Rekonstruktion.md` (708 Z.), `TFPT_Fortsetzung.md` (521 Z.), `TFPT_Rekonstruktion_2026-09-14.md` (624 Z.), `TFPT_Omega_Praeparation_Mehrzeittest_2026-09-14.md` (319 Z.) |
| B. Fugen/Inversion | `TFPT_Sechs_Pruefpunkte_Analyse.md` (593 Z.), `TFPT_TOE_GEMEINSAMER_URSPRUNG_2026-09-14.md` (526 Z.), `TFPT_UNIVERSALRAUM_FUGEN_2026-09-14.md` (286 Z.), `GESAMTSYNTHESE` (350 Z.), `INVERSION` (246 Z.), `Q_AUDIT_UND_U_REGEL` (1163 Z.), `Universalraum_Rekonstruktion_2026-09-14.md` (421 Z.) |
| C. Gebunden | `tfpt_compiler_universalraum_2026-09-13.pdf` (21 S., v1.0), `tfpt_anschluss_zellen_seam_2026-09-14.pdf` (7 S.), `TFPT_Universalraum_Gesamtdarstellung_2026-09-14.pdf` (90 S., v1.1, 210+128 Checks), `TFPT_Universalraum_LaTeX_Quellen_2026-09-14.zip` (46 Dateien, Hauptdatei `main.tex`) |

Prüfer-Lage: `pruefer.py`, `verify_reconstruction.py`, `omega_protocol.py` fehlen im Repo (nur als Anhang in `.md` genannt).
Gelaufen PASS: `universalraum-fugen/checker.py` 27288 + Tests 14/14; `universalraum-inversion/checker.py` 325 (`consistent_partial`) + `followup_checks.py` 147 + Tests 19/19.

## 2. Gesicherter Kern (alle Dokumente einig)

1. **Universalraum ≠ TFPT.** Universalraum = Träger + Operationen + Zusammensetzung + Zustand + Aufzeichnung + Auslesung. Compiler = Leseverfahren. Nur `PR(B) ≃ B`, nicht `RP(U) ≃ U`.
2. **60 Strahlen / 15 Kontexte, Rang 30.** `T = 1/28(CᵀBC + FᵀF)`, `K = B/7`, `CT = KC`, `D(ρ) = 3/7ρ + 1/7I·Trρ`. Spektrum `1⁽¹⁾, (3/7)⁽¹⁵⁾, (2/7)⁽⁹⁾, (−2/7)⁽⁵⁾, 0⁽³⁰⁾`. Passiv reichen 44/45 Dimensionen; volle 240 CQ nur mit offenem Register-Nachschub.
3. **Zelle Ω.** `|Ω⟩ = 1/√24 Σ sgn(π)|π⟩`, Hülle `ker H_Γ = Λ⁴ℂ⁴`, `H_tet = JΣP⁺_ij`. Ω kein Stabilizer → Swap-Kühlung allein präpariert Ω nicht.
4. **Vermittlung 2. Ordnung.** `H_eff = −(t²/Δ)Σ K_e†K_e`, `J_eff = (√(Δ²+4g²)−Δ)/2 = 2t²/Δ > 0`, `K⁺K = I−S = 2P⁻`. Belegung `PK_e†K_fP = 0 (e≠f)` kills Kreuzterme in 2. Ordnung.
5. **E8-Naht konform.** `248 = (45,1)+(1,15)+(10,6)+(16,4)+(16̄,4̄)`, `c = 8 = 5+3` aus D5⊕A3, Z4-Glue. Kein Kondo-Fixpunkt, keine 240-Bijektion.
6. **Mehrzeit-Echo.** Behalten `F = 1` vs. frisch `F = 17/32`, Variante `1/2`, Sternfilter `1/6`, Ω-Protokoll `p_prep = 3/32 = 9/16·1/6`.

## 3. Heute nachgerechnet (Zahlen)

### 3.1 Zweizelle — Gap > J/2 für alle λ ≥ 0

`J = 1`, `E₀ = (4+λ−R)/2`, `R = √(16−2λ+λ²)`, `E₁ = 3+λ/2−Q/2`, `Q = √(4+λ²)`, `Δ_gap = J+(R−Q)/2`.

| λ/J | E₀ | E₁ | Gap |
|---:|---:|---:|---:|
| 0 | 0.0000000000 | 2.0000000000 | 2.0000000000 |
| 0.5 | 0.2974375810 | 2.2192235936 | 1.9217860126 |
| 1 | 0.5635083269 | 2.3819660113 | 1.8184576844 |
| 2 | 1.0000000000 | 2.5857864376 | 1.5857864376 |
| 4 | 1.5505102572 | 2.7639320225 | 1.2134217653 |
| 8 | 2.0000000000 | 2.8768943744 | 0.8768943744 — keine Kreuzung |
| 20 | 2.3046402852 | 2.9501243789 | 0.6454840937 |

Dichtscan λ ∈ [0,50] ∪ {10²…10⁷}: min Δ = 0.5000002757 bei λ = 10⁷, Limes Δ → J/2 von oben. λ = 8J war Beweisgrenze, keine Physik.

Vermittler (Δ = 1): `g = √3/2 ≈ 0.866025403784` → `J_eff = 0.5` exakt. `t/Δ = 1/20 → J = 2t²/Δ = 0.005`.

### 3.2 Clebsch-Streit entschieden

Singulett (4,4,4,4), dim 24024: **E₀ = 11.045398337068, erste Anregung 11.561762122803, Gap 0.516363785734, Multiplizität 4** (Residuen ≤ 5.6e−14). Magnetisch niedrigste 12.133537149348 > Singulett-Anregung.
→ **Q-Audit (Vierfach) bestätigt, FUGEN-Dublett verworfen** (altes `clebsch_su4.json` mit k = 4 hatte nur 2 von 4 erwischt).

### 3.3 E8 + 240-Kill + a = 1/7

- `45+15+60+64+64 = 248` (Wurzeln 40+12+60+64+64 + 8 Cartan). `[g₁,g₁] → (10,6)` (960 Kanäle); `[g₁,g₃] → (45,1)+(1,15)`, nie (10,6). `4⊗4̄ = 1⊕15` enthält keine 6.
- **240-Kill:** Bahnen 15+45+180 = 240, aber 15 = 60·0+15, 45 = 60·0+45 — jede Bahn müsste 60-teilbar sein. 240 = 60·4 täuscht.
- **Nur a = 1/7:** B-Spektrum {7¹, 2⁹, (−2)⁵}. Nur dort `spec(T) = {1, (3/7)¹⁵, (2/7)⁹, (−2/7)⁵, 0³⁰}`, Rang 30, μ = 0. `K_alt` und alle a ≠ 1/7 → Rang 55–60. **μ = 0 ist das fehlende Auswahlprinzip.**
- c = 8: `q_D5+q_A3 = 5k²/8+3k²/8 = k² ≡ 0 mod 1`, `det L = 4·4/4² = 1`.

### 3.4 Uhren + Echo + α + Vierkörper

- `R⁴ = I`, `eig(R) = {1, i, −1, −i}`, `(U_C⊗U_S)|Ω⟩ = |Ω⟩` exakt, PW-Uhr ‖Δ‖ ∼ 1e−16, `(h_C+H_S)|Ω⟩ = 0`.
- `F_behalten = 1`, `F_frisch = (5/8)²+(3/8)² = 17/32`, `F(η) = (17+15η)/32`, CNOT-Variante 1/2, `A₄ = 1/8ΣUᵏ = |Ω⟩⟨Ω|`, `|⟨Ω|χ₀⟩|² = 1/6`, `p_prep = 3/32`.
- **α⁻¹ = 137.0359992168407, +1.897σ über CODATA 2022** (mpmath, Residuum 0). Konstante φ₀-Variante gäbe 137.03650146 — die Zahl sitzt nur auf der α-abhängigen Naht `q(α) = 48c₃⁴e^{−2α}`.
- Vierkörper `−8t⁴/Δ³ = −5·10⁻⁵` vs. `+16t⁴/Δ³ = +10⁻⁴` (Verhältnis −2): verschiedene Modelle (S₆-Cluster vs. P₋-Labels), kein Widerspruch.

## 4. Allesumfassende Lösung (Dach)

Primitive **U-Regel** als einzige Formel über allem:

> `U: H_matter ⊗ H_mediator ⊗ H_history → …`, `U†U = I`

- **Materie = Λ²(4)** (Austausch, `K_e`), **Gedächtnis = Sym²(4)** (Register/History) — erklärt Sektortrennung, 248 ohne `(·,10)`, nicht-autonomen Schatten ohne History.
- **E8 = Vertexgrammatik** (`C^μ_{st;ab}` aus Strukturkonstanten) → `H_eff⁽²⁾`, `H⁽⁴⁾`, Zweizellen-Spektrum, `(A₃)₁`-Kette, Zustandsgate `T_LH = 1/24`, Hecke = Jones.
- **Zeit aus Ereignisordnung** (PW-Uhr + Zusatz-`H_S`), **3D als Auswahl** (Weyl-Kodimension-3 + RG-Lorentz-Fixpunkt + Bulk–Rand), **Familien = index D_eff**, **α** aus `c₃ = 1/(8π)`-Schließung (eingefroren, +1.9σ).

Fünf Fugen bedingt geschlossen: λ (All-λ-Beweis), Graph (Clebsch unter Lesart Ort = Spinorgewicht, K4 als Hülle), Cross-Register (History-Sektor gesetzt, Versorgung offen), Präparation (Filter + Gates explizit, Quelle offen), Zeitskala (`t²/Δ + M̄_Pl`, Sekunden offen).

## 5. Offen für die vollständige TOE (T1–T8)

1. Quellwahl (J, λ, Graph, t, Δ) aus U — kein Selektor außer μ = 0 / Rang 30.
2. Native `(D5)₁+Z4`-Naht analytisch (nächste Rechnung: Superaustausch-Koeffizient aus E8-Strukturkonstanten).
3. d = 3 als Beweis statt Auswahl.
4. Chirales SM-Maß (`index = 3`), 4D-Limes, Spin-2-Pol, thermodynamischer Gap.
5. α-Naht ohne α-Rückkopplung; Lepton/Higgs/Inflation/Proton-Spannungen.
6. Voller 64-Irrep-Sweep + algebraisches Multiplizitäts-Zertifikat; 3 Paket-Prüfer ins Repo holen.

## 6. Nächster Rechenschritt

A) Superaustausch-Klammer `(16,4)⊗(16,4̄) → (10,6)`-Koeffizient aus E8-Strukturkonstanten in `/tmp` — schließt T2. Danach B) thermodynamischer Limes, C) `index = 3` + Spin-2.

---
*Erstellt 2026-09-14 auf Wunsch des Nutzers. Quellen: `universal_room/*.md`, 3 PDFs, LaTeX-`main.tex`, heutige `/tmp`-Rechnungen. Keine Ledger-/Paper-/Website-Änderung.*
