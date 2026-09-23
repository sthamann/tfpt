# TFPT Universalraum — Gesamtstand mit allen Infos (2026-09-14)

Stand: 14.09.2026 ~14:20 UTC+2. Quellen: `universal_room/` (13× `.md`, 3× `.pdf`, 1× `.zip` mit `main.tex`), `docs/OPEN_PROBLEMS.md`, `experiments/theory-contracts/universalraum-paired-release-20260914/new-input-audit/`, heutige `/tmp`-Nachrechnungen. Status: Forschungsstand, **alle T1–T8 offen**, NON-RH, keine `verification/`-Promotion. Nur Chat-Ablage gewünscht; keine Ledger-/Paper-/Website-Änderung.

## 1. Inventar und Prüfer-Lage

| Schicht | Dateien |
|---|---|
| A. Fragmente | `Analyse_und_Rekonstruktion.md` (708 Z.), `TFPT_Fortsetzung.md` (521 Z.), `TFPT_Rekonstruktion_2026-09-14.md` (624 Z.), `TFPT_Omega_Praeparation_Mehrzeittest_2026-09-14.md` (319 Z.) |
| B. Fugen/Inversion | `TFPT_Sechs_Pruefpunkte_Analyse.md` (593 Z.), `TFPT_TOE_GEMEINSAMER_URSPRUNG_2026-09-14.md` (526 Z.), `TFPT_UNIVERSALRAUM_FUGEN_2026-09-14.md` (286 Z.), `GESAMTSYNTHESE` (350 Z.), `INVERSION` (246 Z.), `Q_AUDIT_UND_U_REGEL` (1163 Z.), `Universalraum_Rekonstruktion_2026-09-14.md` (421/963 Z.), `TFPT_Universalraum_Gesamtkonstrukt_2026-09-14.md` (407 Z.), `Konsolidierte_Fortsetzung.md` (709 Z.) |
| C. Gebunden | `tfpt_compiler_universalraum_2026-09-13.pdf` (21 S., v1.0), `tfpt_anschluss_zellen_seam_2026-09-14.pdf` (7 S.), `TFPT_Universalraum_Gesamtdarstellung_2026-09-14.pdf` (90 S., v1.1, 210+128 Checks), `TFPT_Universalraum_LaTeX_Quellen_2026-09-14.zip` (46 Dateien, Haupt `main.tex`) |

- `README.md` der Linie: T1–T8 offen, NON-RH, keine Promotion.
- `new-input-audit/` (13:53–13:58 fertig, **läuft nicht**): `check.py`, `singlet_f4.py/.json`, `verification.json` (~76 kB, `count=891`, `T1_T8_closed=[]`), `verification_optimized.json`, `sources/`.
- In-repo: `check.py` + `singlet_f4.py`. **Nicht** im Repo (nur in `Konsolidierte_Fortsetzung.md` referenziert): `microscopic_fourth.py`, `verify_clebsch_singlet.py`, `verify_independent.py` (89). Ältere Paket-Prüfer `pruefer.py`, `verify_reconstruction.py`, `omega_protocol.py` ebenfalls nur referenziert.
- `verification.json`: `F4_scope="hard tensor-product convention; CAR/native phase identification not established"`, `C16_singlet_F4_555_and_583="not independently reproduced: first attachment contains no accessible numerical code link"` (durch `singlet_f4.py` jetzt in-repo reproduziert, siehe §3).
- `CAR_native_phase_equivalence: false` — Top-Level in `singlet_f4.json`.
- Frühere Fugen/Inversion-Checker PASS: fugen `checker.py` 27288 + Tests 14/14; inversion 325 (`consistent_partial`) + `followup_checks.py` 147 + Tests 19/19. Clebsch-Graph `srg(16,5,0,2)`, Adj-Spektrum `5⁽¹⁾,1⁽¹⁰⁾,(−3)⁽⁵⁾`.

## 2. Gesicherter Kern

1. Universalraum = Träger + Operationen + Zusammensetzung + Zustand + Aufzeichnung + Auslesung; Compiler = Leseverfahren. Nur `PR(B) ≃ B`.
2. 60 Strahlen / 15 Kontexte, Rang 30: `T=1/28(CᵀBC+FᵀF)`, `K=B/7`, `CT=KC`, `D(ρ)=3/7ρ+1/7I·Trρ`; Spec `1⁽¹⁾,(3/7)⁽¹⁵⁾,(2/7)⁽⁹⁾,(−2/7)⁽⁵⁾,0⁽³⁰⁾`. Passiv 44/45 Dim; 240 CQ nur mit Register-Nachschub.
3. Zelle Ω: `|Ω⟩=1/√24 Σ sgn(π)|π⟩`, `ker H_Γ=Λ⁴ℂ⁴`, `H_tet=JΣP⁺_ij`; kein Stabilizer.
4. Vermittlung: `H_eff=−(t²/Δ)ΣK_e†K_e`, `J_eff=(√(Δ²+4g²)−Δ)/2=2t²/Δ>0`, `PK_e†K_fP=0 (e≠f)`.
5. E8: `248=(45,1)+(1,15)+(10,6)+(16,4)+(16̄,4̄)`, `c=8=5+3`, Z4-Glue. Kein Kondo, keine 240-Bijektion (Bahnen 15+45+180; 15,45 nicht 60-teilbar). `[g₁,g₁]→(10,6)` (960), `[g₁,g₃]→(45,1)+(1,15)`, nie (10,6).
6. Nur `a=1/7` gibt Rang 30 + obiges Spec; μ=0 wählt es allein (`K_alt` etc. → Rang 55–60). B-Spektrum {7¹,2⁹,(−2)⁵}.
7. Echo: `F_behalten=1`, `F_frisch=17/32`, `F(η)=(17+15η)/32`, Variante 1/2, Sternfilter `A₄=1/8ΣUᵏ`, `p_prep=3/32=9/16·1/6`. Uhren `R⁴=I`, `(U_C⊗U_S)|Ω⟩=|Ω⟩` exakt, PW ‖Δ‖∼1e−16.
8. α: `c₃=1/(8π)`, `α⁻¹=137.0359992168407`, **+1,897σ** über CODATA 2022 (mpmath). Konstante φ₀-Variante gäbe 137,03650146 — Zahl sitzt nur auf α-abhängiger Naht. Vierkörper `−8t⁴/Δ³=−5·10⁻⁵` vs. `+16t⁴/Δ³=+10⁻⁴` (Verhältnis −2, verschiedene Modelle).

## 3. Heute nachgerechnet

### 3.1 Zweizelle (J=1)

`E₀=(4+λ−R)/2`, `R=√(16−2λ+λ²)`, `E₁=3+λ/2−Q/2`, `Q=√(4+λ²)`, `Δ=J+(R−Q)/2`:

| λ | E₀ | E₁ | Gap |
|---:|---:|---:|---:|
| 0 | 0.0 | 2.0 | 2.0 |
| 0.5 | 0.2974375810 | 2.2192235936 | 1.9217860126 |
| 1 | 0.5635083269 | 2.3819660113 | 1.8184576844 |
| 2 | 1.0 | 2.5857864376 | 1.5857864376 |
| 4 | 1.5505102572 | 2.7639320225 | 1.2134217653 |
| 8 | 2.0 | 2.8768943744 | 0.8768943744 — keine Kreuzung |
| 20 | 2.3046402852 | 2.9501243789 | 0.6454840937 |

Dichtscan bis 10⁷: min Δ=0,5000002757, Limes J/2 von oben. Vermittler (Δ=1): `g≈0,866025403784 → J_eff=0,5`; `t/Δ=1/20 → J=0,005`.

### 3.2 A4-Repro (`new-input-audit`)

`check.py --output /tmp/...` → **891/891 PASS, 0 FAIL**. `singlet_f4.py` (/tmp-Kopie, ~10,9 s): **E₁=11,561762122802579**, **Δ_s=0,516363785734**, ε²-Koeff **13,901769** → bei ε=1/20 ≈0,5511182086 J. F4-555/583 Abw. ~7×10⁻¹², Residuen ~1e−14. Flags `full_non_singlet_comparison / exact_multiplicity_upper_bound / higher_order_bound` alle `false`. Zertifiziert nur `|t|/Δ=1/640`; 1/20 nur ε²-Korrektur.

### 3.3 A3-Entscheidung: lokale Moden (L)

G: `Konsolidierte_Fortsetzung.md:244-256` (60 globale Moden); L: ebd. `:692` + `TFPT_Rekonstruktion_2026-09-14.md:409` (∑H_tet,x). Minimalmodell: G bei N=4 E₀/E₀(1)≈6,01 (nicht-extensiv, Kreuz ~2t²/Δ), L exakt extensiv. Formel `E₀=(4J+λ−R)/2` formal unverändert; Gabel ändert λ_eff + N-Skalierung. T5-Kriterium: nur L hält Energie extensiv und Normen größenuniform. Offen: `b_A/b_B`-Mikrodefinition, L+Transport→Zweizellenblock, 4. Ordnung im Netz.

## 4. Fehlendes zur Raum-Rekonstruktion (A1–A8)

- **A1 (T1):** U-Regel (`U: H_matter⊗H_mediator⊗H_history`, `U†U=I`; Materie=Λ², Gedächtnis=Sym²) ist Kandidat, nicht aus P1+P2 abgeleitet. A/B/C unbestimmt.
- **A2:** `L†L=K†K`-Fix lokal; Audit aller Vertizes fehlt; non-Clifford-Record ohne E8-Herkunft.
- **A3:** entschieden (L), Mikrodefinition + Beweis offen (siehe §3.3).
- **A4:** F4 geschlossen, Singulett in-repo; offen: `t⁶`-Rest, 64 Sektoren, thermodynamische Uniformität, 1/20-Zertifizierung.
- **A5:** Grundzustand angekleidet (98,56 % bei 0,05); 8-Punkt-Filter kein exakter Mikrospektrum-Filter (inkommensurabel).
- **A6:** TFPT-Phasenadapter fehlt (`CAR_native_phase_equivalence: false`); 240 Wurzeln ≠ 240 CQ — Ebenen-Abbildung fehlt.
- **A7:** `V_E8` als VOA ja; native chirale Naht mit Phasen/Domänen/Skalierung nein; 2+1→1+1 kein 3+1.
- **A8:** 3 Prüfer nur extern; RH-Refresh `SOURCE_UNAVAILABLE` (Ordner MISSING); Faktorgraph-Behauptung ohne Pfad (`hylaean_boolean_factorgraph_result.json` r648 ≠ separater Faktorgraph; `rh/catalog/autodraft.py` ohne FAIL).

## 5. Echte Probleme (B1–B4)

- **B1 RH** (`Gesamtkonstrukt:286-301`, Audit-5 `:17`): `Q_ζ(g)=ΣG(ρ)Ḡ(1−ρ̄)` → `=‖Ag‖²` ∀g, unabhängiges A, gleiche Norm/Ränder/Mischterme. Beilage E: (1) Blöcke, (2) Nullraum-Kopplung + Bildraum, (3) Schur-Positivität, (4) dichte Fortsetzung, (5) alle Stufen + Kontinuität + arithmetische Identität. Cholesky aus positiver Q_ζ zirkulär. Code nur `v539/v540`, `check_rh_high_block.py`, RH-probes — kein Abschluss.
- **B2 Faktor** (`:307-355`): `S_N=N⁴gcd⁴`, M₄ kodiert pq, O(N) ggT = exponentiell in log N; Fourier bei teilerfremd gleichförmig. Shor nur Referenz. Gefrorenes kohärentes Protokoll in log N fehlt (Zufall ~N^{−1/2}, unstrukturiert nur N^{1/4}).
- **B3 lösbar heute:** Hamilton-Identifikation via Spektren; Echo-Diagnostik mit Negativkontrollen; Quartett algebraisch + Nichtsingulett-Ausschluss.
- **B4:** RH erst nach positiver Darstellung; P vs NP separat.

## 6. Tore T1–T8 + finale Fragen

| Tor | Fehlender Abschluss |
|---|---|
| T1 | Quell-Auswahl abgeleitet (Belegung, Parameter, Statistik, Zugriffe) |
| T2 | Phasentreue chirale Skalierung; zuerst half-charge inter-sector field |
| T3 | Skalierende 3+1-Geometrie + gemeinsamer Lorentzkegel an mehreren RG-Flüssen; 3+1D-Parent für T3–T8 |
| T4 | `D_int χ_a=0`, 3 Familien, Spiegelentkopplung, Maß; Spin(10)-Obstruktion (Clebsch ≠ Spin(10)) |
| T5 | Rest + alle Sektoren + lokaler Vielzellen-/Kontinuumslimes |
| T6 | Transfer mit Fehlern (α 1,897σ ohne Schema; μ/τ 2,2 %; Higgs 129–134 vs. 125; Inflation 1,76 vs. 2,10×10⁻⁹; Proton ×80/3,4/2,4 zu kurz) |
| T7 | Spin-2-Pol + Ward + universelle Kopplung |
| T8 | Reservoir/Anfang/kosmologisches Funktional (Born vorausgesetzt) |

Final: DM (stabiler Sektor + Produktion), DE (radiativ klein), Baryogenese (quantitativ), strong CP (Maß-Schutz), BH (braucht T7).

## 7. Reihenfolge

1. A4+A8 zu Ende (F4/Singulett-Repro getan mit §3.2; weiter: Restschranke, Nichtsinguletts).
2. A3-Mikrodefinition (L) für T5.
3. A1/A6 (U-Auswahl + Phasenadapter) — härteste Nuss, ohne sie bleibt es eine Klasse statt *der* Ursprung.
4. B1-Vertrag (5 Schritte, hängt an A6). T3/T4/T7/T8 danach.

---
*Erstellt 2026-09-14 auf Nutzerwunsch (`_spark`-Ablage in Documents). Keine Repo-Änderung.*
