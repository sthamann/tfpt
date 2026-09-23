# TFPT / Universalraum v1.4 — Detailbericht zu den sechs gelösten Follow-ups

**Datum:** 14. September 2026  
**Workspace:** `/Users/stefanhamann/Projekte/tfpt-theoryv4`  
**Ziel dieses Dokuments:** Vollständiger, ehrlicher Bericht über die sechs parallelen Theory-Contracts zu den Follow-up-Fragen F1–F6 (keine Promotion, keine T-Schließungen).

---

## 0. Ausgangslage und Methode

### Ausgangslage (v1.4)

Die Runde baut auf dem **Universalraum-Update v1.4**, dem **Hauptbuch**, dem **Quellenpaket** (N9–N13 / Fünf-Quellen-Prüfung), der Datei **`TFPT_Universalraum_Ergebnisse_2026-09-14_v1.4.md`** (Forschungsresultate, explizit *keine* T1–T8-/RH-Promotion) und **`TFPT_Followups_2026-09-14_v1.4.md`** (die sechs Entscheidungsfragen mit Verdict-Zuordnung) auf.

Kernbotschaft der Follow-ups: Die sechs Fragen sind jeweils mit einem **ausführbaren Vertrag** beantwortet — das ist **kein** Abschluss von T1–T8 und **keine** Promotion nach `verification/`, Ledger, Papers oder Website.

### Methode

- **Sechs parallele Theory-Contracts** unter `experiments/theory-contracts/` (NON-RH, **experiments-only Firewall**).
- Jeder Contract: deterministischer `checker.py`, `validation.json`, Unit-Tests (`test_checker.py`); Reproduktion normal und mit `python3 -B -OO` (bytegleiche JSON-/Testergebnisse laut README).
- **Keine** stillschweigende Upgrade-Stufe: Verdict-Enums (`consistent`, `F2_SOURCE_SELECTOR_EDGE_LOCAL`, `F3_QUARTET_CONDITIONAL`, …) sind Suchflächen-Diagnosen, keine load-bearing `[E]`-Claims.

### Gesamt-Checkzahlen (alle Contracts bestanden)

| Contract | Pfad (kurz) | Bedingungen (`validation.json`) |
|---|---|---:|
| F1 | `universalraum-v14-F1-primitives-20260914` | **399** |
| F2 | `universalraum-v14-F2-architektur-20260914` | **7024** |
| F3 | `universalraum-v14-F3-quartett-20260914` | **239** |
| F4 | `universalraum-v14-F4-fehler-skalierung-20260914` | **65** |
| F5 | `universalraum-v14-F5-gemeinsame-welt-20260914` | **115** |
| F6 | `universalraum-v14-F6-transfer-20260914` | **66** |
| **Summe** | | **7908** |

F1 meldet zusätzlich **`inherited_source_prefix_checks`: 1073** (Quellenpin-Erbe aus `compiler-origin-audit-20260913`); diese Zahl ist **nicht** in der Summe 7908 enthalten.

---

## 1. F1 — Wer bedient das Labor?

**Contract:** `experiments/theory-contracts/universalraum-v14-F1-primitives-20260914`  
**Fragestellung:** Kann jeder Bedienschritt des v1.4-Mikrolabors auf **eingefrorene Primitive** mit expliziter Umsetzung und Kosten reduziert werden — ohne versteckten Zielzustandsprojektor `P₀` oder `Ω` als Input-Ressource?

**Verdict:** **`consistent`** — F1 als **Laborvertrag geschlossen**, **nicht** als native Compiler-Herleitung aus P1/P2. `U` selbst kommt nicht aus P1+P2; kontrollierte Evolution, Resonanz, Belegung, Messung, Reset bleiben deklarierte Primitive.

### Verifizierte Zahlen (Quelle: `validation.json`, `README.md`)

| Größe | Wert | Quelle |
|---|---|---|
| Checks | 399 | `validation.json` → `checks` |
| Status | PASS | `validation.json` → `status` |
| Sternfilter-Dimension | 544 | `star_filter.dimension` |
| Sternfaktoren | 13 | `star_filter.n_factors` |
| `∏ A_j = P_{0,dressed}` | true | `star_filter.equals_P0_dressed` |
| Sechsfaktor = Projektor | false (max. Rest 0.15522820139741864) | `six_factor_equals_projector`, `six_factor_max_leftover` |
| `Σ τ_j` | 3172.8296339999974 ℏ/Δ (publ.: 3172.829634) | `error_budget.sum_tau`, `published.sum_tau_hbar_over_Delta` |
| Start+Ende kontrollierte H-Aufrufe | 26 | `protocol_costs.controlled_H_calls_start_plus_end` |
| Start+Ende Zeit | 6345.659267999995 ℏ/Δ (publ.: 6345.659268) | `protocol_costs.time_start_plus_end` |
| Präparation `w²/6` | 0.16191533129706945 (publ.: 0.16191533) | `preparation.preparation_probability` |
| Gesamt behalten `w⁴/6` | 0.15729944705423687 (publ.: 0.15729945) | `preparation.unconditional_kept` |
| Frisch `17w⁴/192` | 0.08356533124756335 (publ.: 0.08356533) | `preparation.unconditional_fresh` |
| Quotient frisch/behalten | 17/32 | `preparation.quotient_fresh_over_kept` |
| Reset-Versuche (Mittel) | 6.1760674050394835 (publ.: 6.1761) | `preparation.reset_attempts` |
| `w` | 0.9856429311786321 (publ.: 0.9856429312) | `preparation.w` |
| Infidelität ≤ 10⁻⁶ → `δH+δE₀` | 7.879401948374521e-08 Δ (publ.: 7.88e-08) | `error_budget.deltaH_plus_deltaE0_over_Delta` |
| Versteckter Zielprojektor als Ressource | false | `hidden_target_projector_used_as_resource` |
| Endliche Clifford+T-Synthese der Zeiten | nicht behauptet | `finite_gate_synthesis_claimed`: false |

**Eingefrorene Primitive (10):** `K_B7`, `Q_C`, `U_C`, `C`, `Ures`, `Q`, `c_exp`, `Hadamard`, `measure_reset`, `fresh_measured_bits` — Kosten in README-Tabelle und `validation.json` → `primitives`.

**Quellenpin:** `compiler-origin-audit-20260913/context_instrument.py` (SHA-256 Präfix `ba1da931…9e3995`, README).

### Contract-Dateien

- `README.md`
- `validation.json`
- `checker.py`
- `test_checker.py`

### Reproduktion

```sh
cd /Users/stefanhamann/Projekte/tfpt-theoryv4/experiments/theory-contracts/universalraum-v14-F1-primitives-20260914
python3 -B checker.py validation.json
python3 -B -m unittest test_checker
python3 -B -OO -m unittest test_checker
```

### Offen / entscheidender Kill- bzw. Schließungstest

- **Offen:** Dass die Primitive selbst aus der **ursprünglichen TFPT-Regel** (P1/P2) folgen; native Verfügbarkeit von Resonanz, isoliertem Stern, kontrolliertem `H`, Record, Clock, Reset ohne Zusatzressourcen.
- **Entscheidender Test (erfüllt im Vertrag):** Jeder Griff hat Kostenzeile; kein Schritt nutzt `P₀` oder `Ω` als Input — **Kill:** ein Laborgriff, der doch einen versteckten Zielprojektor braucht, oder fehlende Kostenangabe.

---

## 2. F2 — Welche Bauweise ist vorgeschrieben?

**Contract:** `experiments/theory-contracts/universalraum-v14-F2-architektur-20260914`  
**Fragestellung:** Wählt **Lokalität allein** die Vermittlerarchitektur — oder muss ein **quellenbasierter Selektor** (ohne Spektrumlesen) entscheiden?

**Verdict:** **`F2_SOURCE_SELECTOR_EDGE_LOCAL`** — **Kante quellenbasiert:** Bank **pro Kante** (iii), nicht durch angenehmeres Spektrum gewählt. Z4-Glue / uniformes `J` auf Clebsch-Kanten **wählt die Bank nicht** (`z4_glue.selects_bank`: false).

### Verifizierte Zahlen

| Größe | Wert | Quelle |
|---|---|---|
| Checks | 7024 | `validation.json` → `count` |
| C16 `L(m)` | (0,0,1,2,4,5,7,9,12,14,17,20,24,27,31,35,40) | `c16.L_m` |
| Band kantenlokal | **7/10 Δ** (0,7 Δ) | `c16.edge_local.certified_band_gap_over_Delta` |
| Band zellgeteilt | **2/5 Δ** (0,4 Δ) | `c16.cell_shared.certified_band_gap_over_Delta` |
| Negativkontrolle 0,8 Δ | scheitert Pivot 1, 2. Pivot −7/20 | `c16.negative_control_0.8_Delta` |
| Feshbach-Rest kantenlokal | 1.7160106225095237 J (13.152776924847569 J vorher) | `c16.edge_local.feshbach_remainder_over_J` |
| F4-Grund Zelle / Kante | 555.4885003638373 / 732.1203109419222 | `f4_witnesses` (Selektor liest diese **nicht**) |
| Gap-Koeff. Zelle / Kante | +13.901769… / −11.955494… | `architectures.extensive_countermodel` |
| E8 F2-Ränge | 45 (Site), 285 (Kante) | `e8_f2` |
| Geteilte Bank diagonal ±1 | obstruiert | `e8_f2.shared_diagonal_pm1_gauge_exists`: false |
| CAR/Tensor 940D | 1584 Übergänge, 144 nichttriviale Vorzeichen | `car` |
| Vorschrift Selektor | `edge_local` | `selector.prescribed` |

**Explizit nicht behauptet:** thermodynamischer Bandgap, innerer Singulettgap aus Feshbach oder 0,7 Δ, Ausschluss komplexer Adapter, native Clock-Lift, T1–T8 (`claims_not_made`).

### Contract-Dateien

- `README.md`, `validation.json`, `checker.py`, `test_checker.py`  
- Externer Zeuge: `experiments/theory-contracts/universalraum-five-source-frontier-20260914/spectrum_followup.json` (SHA-256 in `f4_witnesses.sha256`).

### Reproduktion

```sh
cd /Users/stefanhamann/Projekte/tfpt-theoryv4/experiments/theory-contracts/universalraum-v14-F2-architektur-20260914
python3 -B checker.py validation.json
python3 -B -m unittest test_checker
python3 -B -OO -m unittest test_checker
```

### Offen / Kill-Tests

- **Offen:** komplexe/nichtdiagonale Adapter; Clock-Transport des Gittercocycles in TFPT-Quellbasis; Vermittlerhopping, andere Ladungssektoren.
- **Kill des Selektors** (`selector.kill`): quellennative CAR/Tensor-Lösung für **geteilte** Zellmoden in der tatsächlichen Gaugeklasse; quellenerzwungenes Hopping; nativer Clock-Adapter, der geteilte Moden braucht; Quelle, die K4-Zellen oder Kette erzwingt.

---

## 3. F3 — Vierfachstruktur beweisen?

**Contract:** `experiments/theory-contracts/universalraum-v14-F3-quartett-20260914`  
**Fragestellung:** Ist die **4-Isotyp-Multiplizität** der ersten Anregung exakt / zertifiziert — oder nur numerisch und an gepinnte Daten gebunden?

**Verdict:** **`F3_QUARTET_CONDITIONAL`** — **bedingt, nicht zertifiziert** als vollständiger Spektralbeweis. Exakt: Rang-4-Projektor `[4,1]` in `ℚ[S5]`, Operatoridentitäten, `Aut`-Invarianz. **`fourfold_proved_with_certificate`: false**.

### Verifizierte Zahlen

| Größe | Wert | Quelle |
|---|---|---|
| Checks | 239 (213 exakt, 10 zertifiziert, 7 Negativ, 9 numerisch — README) | `count` |
| Singulett `E0`, `E1`, Gap | 11.960507412663516, 12.446984939669278, 0.4864775270057624 | `singlet` |
| Max. Residuum (8 Vektoren) | 4.7473366811147897e-14 | `singlet.max_residual` |
| Variationelle Viererraum-Obergrenze | 12.447023775951228 | `singlet.variational_quartet_upper` |
| Berichtetes nacktes Nichtsingulett | 12.133537149348086 (**nicht zertifiziert**) | `singlet.reported_bare_nonsinglet`, `bare_minimum_certified`: false |
| Bedingt: `f(H₀)` bei dieser Untergrenze | 12.96487952485328 | `singlet.f_of_reported_bare` |
| Schwelle `f` vs. Obergrenze | 11.579468146686272 | `singlet.threshold_to_beat_variational_upper` |
| `|Aut(Clebsch)|` | 1920 (16 Translationen) | `aut` |
| S5-Projektor Rang | 4, `[4,1]` standard | `s5_projector` |
| Kato-isoliertes trunkiertes Quartett | Residuum < 5·10⁻¹⁴ (Follow-up-Text; JSON: 4.75e-14) | README / `max_residual` |

**Teilresultat klar markiert:** Numerisches Cluster der ersten vier Moden ist **kein** exakter Multiplizitätsbeweis (`numerical_four_modes_are_not_an_exact_multiplicity_proof`: true). **`H6`-Rest:** nicht behauptet (`H6_remainder_claimed`: false).

### Contract-Dateien

- `README.md`, `validation.json`, `checker.py`, `test_checker.py`  
- Gepinnte Quellen in `pins` (u. a. `spectrum_followup.json`, `validation_singlet_dense.json`).

### Reproduktion

```sh
cd /Users/stefanhamann/Projekte/tfpt-theoryv4/experiments/theory-contracts/universalraum-v14-F3-quartett-20260914
python3 -B checker.py validation.json
python3 -B -m unittest test_checker
python3 -B -OO -m unittest test_checker
```

### Offen / Kill- bzw. Schließungstest

- **Offen:** Intervall/Inertia/Temple für **180180D** adjungiertes nacktes Minimum; Intervallhülle **24024D** trunkiertes `H₀ + 0.00125 F4`; kanonischer **H6**-Rest; Lean.
- **Schließungstest:** Zertifizierte nackte Untergrenze ≥ 12.133537149348086 → Sektorvergleich **bedingt → zertifiziert**. **Kill:** Intervallzertifikat, das Minimum **unter** 11.579… zeigt, oder Bruch der exakten `F4`-Identität.

---

## 4. F4 — Fehler und wachsende Größe

**Contract:** `experiments/theory-contracts/universalraum-v14-F4-fehler-skalierung-20260914`  
**Fragestellung:** Bleibt das Labor bei Fehlern und wachsender Größe brauchbar — **unabhängige** Zellen vs. **gekoppelte** Default-Kopplung?

**Verdict:** **`F4_INDEPENDENT_USABLE_COUPLED_DEFAULT_NOT_USABLE`** — **unabhängig: ja** (bewiesen); **gekoppelt mit Default `λ = J`: nein** (außerhalb 10⁻⁶-Fensters).

### Verifizierte Zahlen (unabhängig)

| Größe | Wert | Quelle |
|---|---|---|
| Checks | 65 | `checks`-Array-Länge |
| CPTP-Rate `r` | 0.975420710450023 | `independent.rate` |
| Fehlerboden-Multiplikator | 40.684658438426474 | `independent.floor_multiplier` |
| `ε` für 10⁻⁶ | 2.4579289549977014e-08 | `independent.epsilon_for_1e-6` |
| Zyklen 1 Zelle @ 10⁻⁶ | **556** | `independent.cycles_single_1e-6` |
| Zyklen 4096 Zellen (Union) @ 10⁻⁶ | **890** | `independent.cycles_independent_4096_global_1e-6` |
| Union bei verschränktem Start | true | `union_bound_holds_for_entangled_start` |
| Ungelesener unitaler Record kühlt nicht | Fixalgebra-Dim. **3876** | `negative_control.fix_algebra_dimension` |
| Reset Farbbits/Zelle | ≤ 8 | `budgets.reset_color_bits_per_cell_upper` |
| Austauschrecords/Zyklus | 3 | `budgets.exchange_records_per_cycle` |
| Mittlere Präparationsversuche | 6.176067405039554 | `budgets.mean_preparation_attempts` |

### Verifizierte Zahlen (gekoppelt, Default `λ = J`)

| Fenster | `usable_at_1e-6` | `λ/J` max für 10⁻⁶ (Indikativ) |
|---|---|---|
| 2 Zellen, 3 Records | false | 3.688189236899026e-08 |
| 2 Zellen, Spektralfilter | false | 7.746804078790014e-10 |
| Kette N=4096, 3 Records | false | 4.5021841270740064e-12 |
| Kette N=4096, Spektralfilter | false | 9.456547947741716e-14 |

- `default_coupling_in_1e_6_window`: **false**  
- `J/Δ` bei `t/Δ = 1/20`: 0.005  
- Grobe Eindeutigkeit stirbt bei **N=5**, `λ=J` (README); JSON: `crude uniqueness dies at N=5`  
- **Härteste Restressource:** Zwischenzellentkopplung oder Extra-Datum **`λ ≪ J`** auf deklarierten Record-/Filterzeitskalen.

### Contract-Dateien

- `README.md`, `validation.json`, `checker.py`, `test_checker.py`

### Reproduktion

```sh
cd /Users/stefanhamann/Projekte/tfpt-theoryv4/experiments/theory-contracts/universalraum-v14-F4-fehler-skalierung-20260914
python3 -B checker.py validation.json
python3 -B -m unittest test_checker
python3 -B -OO -m unittest test_checker
```

### Offen / Kill-Test

- **Offen:** Physische Reset-/Controller-Kopplung, wechselwirkende Zellen jenseits der Schranke, native Herleitung von Entkopplung — **kein T8-Abschluss**.
- **Kill:** Nachweis, dass Default-`λ=J` auf den deklarierten Zeitskalen doch 10⁻⁶-Fenster erfüllt **ohne** extra Datum; oder Widerlegung des unabhängigen CPTP-Attraktors.

---

## 5. F5 — Eine gemeinsame Welt?

**Contract:** `experiments/theory-contracts/universalraum-v14-F5-gemeinsame-welt-20260914`  
**Fragestellung:** Trägt **eine** skalierende Familie gleichzeitig Dimension/Lichtkegel, chirales Maß und masslosen Spin-2?

**Verdict:** **`NO_GO_MISSING_SELECTORS`** — **No-go: 5 fehlende Selektoren**. `common_world`: false. **T3, T4, T5, T7 bleiben offen** (`T1_T8_closed`: []).

### Familie

**`C16_Clebsch_x_(Z/LZ)^d`** — Clebsch SRG (16,5,0,2), E8-Superaustausch, Overlap auf 2D-Torus, Tensor auf Box-Laplace, Sinus-Weyl auf denselben Momenta.

### Verifizierte Zahlen (Teilresultate — **keine** Welt-Ableitung)

| ID | Ergebnis | Quelle |
|---|---|---|
| Checks | 115 | `checks` |
| T3 Wärme L=64, ds/d | 1.0167118262988828 | `heat.ds_over_d_L64` |
| T4 Fluss 3, L=8/10 | 3 Nullmoden, Index −3, GW < 1.2e-13 | `overlap`, README |
| T4 Fluss 0 | 2 Nullmoden, Index 0 | `overlap` flux 0 |
| T7 Tensor | TT Rang 2, kein Pol; Schwelle 2m; Ward `(g1-g2)(p3-p1)=0` | `tensor` |
| T7 Weyl d=3 | 8 Knoten, Gesamtchiralität 0 | `weyl.by_dimension.3` |
| T5 negativ | K4 nicht in Clebsch einbettbar (dreiecksfrei) | `graph.K4_subgraph`: false |
| Wärme ≠ Kausal | Heat-Kernel am Antipoden 4.4757253458982404e-13 | `causal` |
| Spectator-Faser ×16 | 48 Nullmoden bei Index −48 (nicht 3) | `fiber.spectator_fiber_copies` |

**Fünf fehlende Selektoren** (vollständig in `verdict.missing_selectors`): Familie+Kegel; Fluss/Geometrie-Herkunft; 3+1D+Spiegelgap; massloser Spin-2; T5-Zelle vs. nativer Graph.

### Contract-Dateien

- `README.md`, `validation.json`, `checker.py`, `test_checker.py`

### Reproduktion

```sh
cd /Users/stefanhamann/Projekte/tfpt-theoryv4/experiments/theory-contracts/universalraum-v14-F5-gemeinsame-welt-20260914
python3 -B checker.py validation.json
python3 -B -m unittest test_checker
python3 -B -OO -m unittest test_checker
```

### Offen / Kill-Test

- **Offen:** Native Selektoren, die **eine** Familie auf 3+1D, Kegel, chiral, Spin-2 zwingen — ohne Extra-Input.
- **Kill (positiv):** Konstruktion der fehlenden Selektoren aus TFPT-Quelle; **Kill (negativ bestätigt):** erneuter No-go mit derselben Familie und expliziten Selektor-Labels.

---

## 6. F6 — Dieselben Parameter für mehrere Beobachtungen?

**Contract:** `experiments/theory-contracts/universalraum-v14-F6-transfer-20260914`  
**Fragestellung:** Stimmen **fixierte** Inflations- und Overlap-Parameter gleichzeitig mit ACT und Flavour überein — ohne Retuning?

**Verdict:** **`tension`** (Kosmologie) + **`no_shared_flavour_transfer`** (Flavour). **Spannung ≈ 3,5σ** in `n_s` bei As-Kalibrierung; kein neuer Likelihood-Fit als Lösung.

### Kosmologie (ACT DR6 v2, Tabelle 5, Spalte P-ACT-LB2)

| Größe | Wert | Quelle |
|---|---|---|
| Checks | 66 | `count` |
| `c3` fix | 0.039788735772973836 (= 1/(8π)) | `cosmology.c3_fixed` |
| ACT `n_s` | 0.9752 ± 0.0030 | README |
| ACT `log(10¹⁰ A_s)` | 3.062^{+0.010}_{−0.012} | README |
| Kalibrierung auf zentrales **A_s** | N = 56.62390990009669, `n_s` = 0.9646792317321665, **Pull 3.5069227559444784 σ** | `as_calibration` |
| Kalibrierung auf zentrales **n_s** | N = 80.64516129032243, **A_s-Verhältnis 2.0284155031054754×** | `ns_calibration` |
| Joint √χ² (ρ=0, Minimum entlang Branche) | **3.499602298028172** (Scan ρ: ~3.39–3.70) | `joint_chi2_rho_scan` |
| Gemeinsame Zentralen ohne c3-Tuning | c3_req/c3_fix = **0.9039001112201315** (−9.61 %) | `forbidden_c3_retune` |
| Invariant C_inf | 0.4929956404242692 (Pull ln C_inf ≈ −2.92σ bei ρ=0) | `cosmology.C_inf`, `invariant_pull` |
| Tensor r (selbes N) | 0.00374267… / 0.00184512… | `tensor_same_N` |
| Tilt-Schließung bräuchte ~30 % Relationsänderung; führendes SR O(1/N) ~3.5 % | | `theory_error_budget` |

### Flavour

- Modell: deklarierter Zweitorus, `m0=1`, U(1)-Fluss.  
- Fluss 3: **3** Nullmoden (L=8,10); Fluss 0: **2** Nullmoden, Index 0.  
- **`Y_ab = y δ_ab`** — Einheitsmatrix, **keine Hierarchie** (`flavour.status`: `no_shared_flavour_transfer`).  
- Kosinus-Profil: **neuer Input**, keine abgeleitete SM-Textur.

### Contract-Dateien

- `README.md`, `validation.json`, `checker.py`, `test_checker.py`

### Reproduktion

```sh
cd /Users/stefanhamann/Projekte/tfpt-theoryv4/experiments/theory-contracts/universalraum-v14-F6-transfer-20260914
python3 -B checker.py validation.json
python3 -B -m unittest test_checker
python3 -B -OO -m unittest test_checker
```

### Offen / Kill-Test

- **Offen:** Sieben benannte `missing_transfer`-Stücke (normierte Wirkung, Higgsprofil, RG, Overlap-Theoriefehler, höhere SR, Reheating entlang Invariante, Tensor an N gekoppelt).  
- **Kill:** Per-Observable-Retuning von N oder Texturen als „Lösung“; **c3** als Kosmologie-Dial. **Schließungstest:** deklarierter Joint-Likelihood mit Tabellen-Kovarianz **und** abgeleitete Flavour ohne Extra-Texturen.

---

## 7. Gesamtbild

### T1–T8 (alle offen — warum)

Keiner der sechs Contracts schließt T1–T8 (`T1_T8_closed` überall leer). Kurz nach Ergebnisbericht §9 und Follow-ups:

| Tor | Stand dieser Runde | Warum nicht geschlossen |
|---|---|---|
| **T1** | Lazy-Walk, Entropie, drei Architekturen getrennt | Keine native Operations-/Zustandsauswahl aus der Regel allein |
| **T2** | Half-Charge-Obstruktion, Oszillatornormen | Kein natives analytisches Feld auf dichter Domäne aus der **tatsächlichen** Quelle |
| **T3** | Wärme C16×T^d gibt eingesetztes d zurück | Kein Familien-/Kegel-Selektor (F5 No-go) |
| **T4** | Overlap-Nullmoden bei gesetztem Fluss | Fluss/3+1D/Spiegelgap/chirale Ladung nicht abgeleitet (F5) |
| **T5** | CAR/F4/Bänder, bedingte Untergrenze | Zertifizierte nackte Sektoren, H6, Vielzellenlimes |
| **T6** | ACT-Diagnose, Y = y·1 | Kein gemeinsamer Transfer (F6) |
| **T7** | Tensor/Weyl-Kontrollen | Kein massloser Spin-2-Pol aus derselben Quelle (F5) |
| **T8** | Mikrolabor, Feedback, unabhängige Zellen | Gekoppelte Default-λ=J nicht brauchbar; Reset/Clock nicht nativ abgeleitet (F4) |

**Querschnitt:** **`U` nicht aus P1+P2** (F1); keine gemeinsame Welt-Familie (F5); empirische Spannung (F6).

### Fugen-Status (Konsolidierung / `TFPT_UNIVERSALRAUM_FUGEN_2026-09-14.md`)

| Fuge | Kurzstatus |
|---|---|
| **λ** | Uniform **J = 2t²/Δ** auf jeder Bindung unter E8-Superaustausch-Lesart; **λ ≠ J** braucht Zusatzdaten (F4 bestätigt Default außerhalb 10⁻⁶ bei Kopplung) |
| **Graph** | Clebsch-Graph unter genannter Lesart (stark regulär, Schur–Weyl 64 Irreps) |
| **Cross-Register** | **Negativ exakt:** Aufzeichnung ⊂ Sym²(4), nicht aus 248 ableitbar; Registerlesebasis = Zusatzdatum |
| **Präparation** | Ω Hülle, inert unter gleichkontextiger Aufzeichnung; frisches Register außerhalb — Start in Hülle **gesetzt**, Zahlen F1 (w²/6, …) im Vertrag |
| **Zeitskala** | Auf **t²/Δ** und M̄_Pl **lokalisiert**, nicht geschlossen |
| **240-Bijektion** | Äquivariante Identifikation **tot** (Bahnen 15+45+180 ≠ 60·ℤ) |
| **c = 8** | Kein Kondo-RG-Fixpunkt in dem Sinn; **konforme Einbettung durch Z4-Eichung** (E8)₁-Programm, Trägerzahl mod 4 ↔ Fermionsektor noch zu konstruieren |

### RH, Faktorisierung, P vs. NP, dunkle Sektoren

Explizit **offen** in allen sechs Contracts (`claims_not_made` / Firewall). Keine Pins in dieser Runde geändert; endliche physikalische Tests lösen diese Probleme **nicht**. Externe RH-/Faktorquellen teils lokal nicht verfügbar (Ergebnisbericht) — nicht als unabhängig verifizierter Fortschritt verbucht.

### Was die sechs Follow-ups gemeinsam leisten

Ein **berechenbares kleines Labor** (Filter, Aufzeichnung, Endprüfung, Rohstatistik) mit **eingefrorenen Griffen** (F1), **quellenbasierter Kantenarchitektur** (F2), **exakter Algebra + bedingter Spektrumskette** (F3), **skaliertem unabhängigen Fehlerkanal, aber gekoppeltem Default-No-go** (F4), **negativem Welt-No-go** (F5) und **empirischer Spannung ohne Retuning** (F6). Es fehlt weiter der Nachweis, dass die **ursprüngliche TFPT-Regel** dieses Labor und seine Bedienung **erzeugt**.

---

## 8. Vorschlag nächste Revision (Reihenfolge)

1. **F3-Zertifikat:** Intervall/Inertia für 180180D nacktes Minimum und 24024D trunkiertes Spektrum; ggf. A2 (Kommutante von `H_eff` auf hartem C16-Belegungssektor) aus Follow-ups.
2. **F4-Entkopplung:** `λ ≪ J` oder physische Entkopplung **nativ** begründen oder messen; gekoppelte 10⁻⁶-Fenster nachziehen.
3. **F5-Selektoren:** Explizite Konstruktion oder weiterer No-go pro Selektor — sonst bleiben T3/T4/T5/T7 getrennt.
4. **F6-Likelihood:** Deklarierter Joint-Likelihood (Kovarianz aus Tabelle 5, falls verfügbar) **ohne** Fit als Lösung; abgeleitetes Higgs/Flavour-RG, falls überhaupt anschlussfähig.

---

## 9. Anhang — Pfade, Checkzahlen, Repro-Kommandos

| # | Contract-Pfad | Checks | Status-String (`validation.json`) |
|---|---|---:|---|
| F1 | `experiments/theory-contracts/universalraum-v14-F1-primitives-20260914` | 399 | PASS / `consistent` |
| F2 | `experiments/theory-contracts/universalraum-v14-F2-architektur-20260914` | 7024 | `F2_SOURCE_SELECTOR_EDGE_LOCAL` |
| F3 | `experiments/theory-contracts/universalraum-v14-F3-quartett-20260914` | 239 | `F3_QUARTET_CONDITIONAL` |
| F4 | `experiments/theory-contracts/universalraum-v14-F4-fehler-skalierung-20260914` | 65 | `F4_INDEPENDENT_USABLE_COUPLED_DEFAULT_NOT_USABLE` |
| F5 | `experiments/theory-contracts/universalraum-v14-F5-gemeinsame-welt-20260914` | 115 | `NO_GO_MISSING_SELECTORS` |
| F6 | `experiments/theory-contracts/universalraum-v14-F6-transfer-20260914` | 66 | `tension` |

**Summe Bedingungen:** 7908.

### Reproduktion (jeweils im Contract-Verzeichnis)

```sh
REPO=/Users/stefanhamann/Projekte/tfpt-theoryv4/experiments/theory-contracts

for d in universalraum-v14-F1-primitives-20260914 \
         universalraum-v14-F2-architektur-20260914 \
         universalraum-v14-F3-quartett-20260914 \
         universalraum-v14-F4-fehler-skalierung-20260914 \
         universalraum-v14-F5-gemeinsame-welt-20260914 \
         universalraum-v14-F6-transfer-20260914; do
  cd "$REPO/$d"
  python3 -B checker.py validation.json
  python3 -B -m unittest test_checker
  python3 -B -OO -m unittest test_checker
done
```

### Referenz-Dokumente (Universalraum v1.4)

- `universal_room/TFPT_Followups_2026-09-14_v1.4.md`
- `universal_room/TFPT_Universalraum_Ergebnisse_2026-09-14_v1.4.md`
- `universal_room/TFPT_UNIVERSALRAUM_FUGEN_2026-09-14.md` (Fugen Tabelle, 240-Bijektion, Z4/c=8)

---

*Ende des Berichts. Nur diese Datei wurde erzeugt; keine Änderungen an verification/, Ledger, Papers oder Website.*
