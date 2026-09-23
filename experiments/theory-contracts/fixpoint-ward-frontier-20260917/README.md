# Fixpunkt-Ward-Suche auf drei Frontier-Ziele — 17. September 2026

Präregistrierte, endliche Suchrechnung (NON-RH), dieselbe eingefrorene Methodik
wie der Vorgänger-Contract `fixpoint-ward-mpratio-20260917`. **Firewall:** dies
ist ein Theory-Contract-Experiment — **keine** Claims in `verification/`,
`status_ledger.csv`, Papers oder Website, keine Beförderung, **niemals** eine
Scorecard-Zeile. Alle drei Ziele sind **`F_transfer`-Brücken, niemals primitive
Compiler-Outputs** (Frontier-Firewall, `tfpt_4_frontier.tex`; Guard
`FR.TRANSFER.01`). Selbst ein bestandener Kandidat wäre ein Contract-Ergebnis,
kein `[E]`. Ehrliche Nullen sind gültige Ergebnisse.

## Fragen (Hypothesen — zu prüfen, nicht zu behaupten)

1. **KOIDE-Q:** Ist die Koide-Relation Q eine Ward-artige
   Selbstkonsistenz-Wurzel über dem Leptonsektor (Lepton-c, φ₀-Leiter)?
2. **HIGGS-QUARTIC:** Hat die Near-Kritikalitäts-Residualgröße |λ(M̄_Pl)| eine
   Ward-artige Fixpunktform aus Compiler-Atomen?
3. **MPME-CROSS:** Existiert für m_p/m_e eine Ward-Identität in einer
   **qualitativ neuen Gleichungsklasse**, die die Residuenmatrix R explizit
   (als Matrix, über ihr charakteristisches Polynom) verwendet — cross-sector
   gekoppelte Formen statt reiner Pool-Skalare?

## Zielwerte und Quellen (vor der ersten Auswertung dokumentiert)

| Ziel | Zielwert x* | Quelle |
|---|---|---|
| KOIDE-Q | **2/3 exakt** — demokratisches Target Q⋆ = \|ℤ₂\|/N_fam | `tfpt_4_frontier.tex`, Sek. "The Koide relation — near 2/3, computed exactly" |
| (Kontext) | Q_source = 0.664463816123053897935385038368 aus der [E]-Leiter (16/7·φ₀⁵, 4/3·φ₀³, 7/6·φ₀²) | ebenda; v25/v93; im Probe nachgerechnet |
| (Kontext) | Q_pole = 0.666664463402636702938278624889 | PDG 2024 Polmassen (m_e = 0.51099895069, m_μ = 105.6583755, m_τ = 1776.93 MeV); im Probe nachgerechnet |
| HIGGS | \|λ(M̄_Pl)\| = 0.0024287567882036172 (vorzeichenbehaftet −0.0024…, β_λ = 1.7·10⁻⁴) | `verification/v166_higgs_free_seam.py`, 2-loop, Stand 2026-09-17; Fixpunktbedingung λ(M_seam) = β_λ(M_seam) = 0 (freie Seam, Frontier-Sek. "The Higgs quartic") |
| MPME-CROSS | m_p/m_e = 1836.15267343 | CODATA 2022 (±1.1·10⁻⁷ abs); Frontier-Sek. "Proton/electron ratio" |

Wichtige Kontext-Notizen (eingefroren):

- **Koide:** Das Target 2/3 ist selbst eine Compiler-Zahl (|ℤ₂|/N_fam). Der
  gemessene Polwert Q_pole liegt 3,3·10⁻⁶ (relativ) neben 2/3 — **außerhalb**
  der 10⁻⁶-Toleranz (im Probe gecheckt); ein Treffer bei 2/3 ist eine Aussage
  über das Compiler-Target, nicht über den Polwert. Die [E]-Leptonmassen
  liefern Q_source = 0.6644638 ≠ 2/3 — darum unterscheidet das Verdict
  "trivial aus bereits [E]-Objekten" von "eigenständige Fixpunktbedingung"
  (Regel unten).
- **Higgs:** Der Zielwert ist selbst ein Transfer-Output (gemessene
  (m_H = 125.25 GeV, y_t(M_Z) = 0.95) als Inputs der 2-loop-RGE) und trägt
  dessen Band; die Suche fragt, ob der Residualwert eine Compiler-Ward-Wurzel
  ist. Die Fixpunktform λ = 0 ist für die Wurzelsuche entartet (relative
  Toleranz an 0 sinnlos) — gesucht wird nach der **Residualgröße**.

## Gemeinsame eingefrorene Methodik (identisch zum Vorgänger)

**Atome (26, nur deklarierte Compiler-Objekte):** ganzzahlig 1, 2, 3, 4, 5, 8,
9, 10, 16, 40, 41, 48, 78, 240, 248; rational 41/10, 55/117, 34/47, 3/26,
16/7, 4/3, 7/6, 1/2; transzendent c₃ = 1/(8π), φ₀ = 1/(6π) + 3/(256π⁴),
λ_Y = √(φ₀(1−φ₀)). **Pool:** Atome ∪ Paarprodukte ∪ Paarquotienten, exakt
dedupliziert ⇒ **N_POOL = 794** (Komplexität ≤ 2 Atome pro Koeffizient).
**Toleranz:** relativ 1·10⁻⁶ (Halbfenster x*·10⁻⁶); Near-Miss-Fenster rel.
10⁻⁴ nur zum Bericht. **Nullbatterie:** M = 200 Surrogate-Familien gleicher
Konstruktion und Komplexität (Seed 20260917, **ein** rng-Strom, Batterien in
der Reihenfolge KOIDE → HIGGS → CROSS); Trefferrate pro Gleichung → λ =
Rate·N_eff; **Signifikanzschwelle p < 0.01** (Poisson). **Zertifikate:**
mpmath-`iv`-Bracket um die 50-stellig verfeinerte Wurzel plus
Intervall-Bandscan der Eindeutigkeit (v3-Stil).

**λ-Budget-Disziplin (Lehre des Vorgängers, eingefroren):** ein Einzeltreffer
ist nur signifikant, wenn λ < −ln(0.99) ≈ 0.01005. Die Suchräume sind durch
die Methodik festgelegt; wo λ darüber liegt, ist vorab festgelegt, dass der
Einzeltreffer als `CANDIDATE_BUT_LOOK_ELSEWHERE` fällt — die Schwelle wird
nicht nachträglich weichgeklopft.

## Präregistrierung Ziel 1 — KOIDE-Q

**Familie:** identisch zum Vorgänger (W0 Baseline x − A = 0; W2 quadratisch;
W3 Log-Seam; W4 Seam-Log (v3-Lift); W1 kubisch), N_TOTAL = 18 283 438,
N_Ward = 18 282 644. A, B ∈ Pool, C ∈ Atome.

**Trivialitätsregel (vor Auswertung eingefroren, zielspezifisch):** Da das
Target 2/3 selbst Atom-Arithmetik ist, wird ein Treffer **vor** dem
Poisson-Test klassifiziert:

- Baseline-Treffer x = A mit A = 2/3 exakt ⇒ die bekannte Lesart
  \|ℤ₂\|/N_fam — kein Ward-Kandidat.
- Ward-Treffer, deren Gleichung **an** x* exakt verschwindet
  (|F(x*)| < 10⁻⁸⁰ in dps-100-Arithmetik) ⇒ exakte Identität unter Atomen —
  die Gleichung *kodiert* das Target statt es zu *predicten*; kein Kandidat.
- Nur Ward-Treffer mit 0 < |F(x*)| und Wurzel in Toleranz sind Kandidaten.
- Verdict `TRIVIAL_FROM_EXISTING_E`: ≥ 1 exakter Treffer (Baseline oder Ward),
  aber **null** nichttriviale zertifizierte Kandidaten — d.h. die einzigen
  "Fixpunkte" sind Restatements der Compiler-Lesart; keine eigenständige
  Fixpunktbedingung.

**Surrogate-Note:** Zufallsfamilien mit rationalen Atomen erzeugen bei einem
einfach-rationalen Target wie 2/3 ebenfalls (exakte und fast-exakte) Treffer —
die gemessene Surrogate-Rate ist damit eine **obere Schranke** an die
nichttriviale Rate; der Poisson-Test ist konservativ. λ-Budget: bei
Vorgänger-Rate 1,5·10⁻⁸ wäre λ ≈ 0,28; die gemessene Rate entscheidet.

## Präregistrierung Ziel 2 — HIGGS-QUARTIC

**Familie:** identisch (W0–W4), N_TOTAL = 18 283 438. **Eingefrorene
Magnituden-Schranken (im Probe gecheckt, nicht angenommen):** für x* ≈ 0,0024
gilt x² < min Pool (5,9·10⁻⁶ < 1,6·10⁻⁴) ⇒ W2 hat keinen Vorzeichenwechsel im
Fenster; x³ < min Atom (1,4·10⁻⁸ < 0,0398) ⇒ W1 ebenso. Beide Klassen sind an
diesem Target **konstruktiv vakuum**; der effektive Ward-Raum ist Log + Seam:
**N_eff = 1 260 872**. (Die Klassen bleiben Teil der eingefrorenen Familie und
werden mit 0 Treffern berichtet; die Schranken werden pro Surrogate-Familie
erneut geprüft.) λ-Budget: λ ≈ 0,02 erwartet ⇒ ein Einzeltreffer wäre hier
prinzipiell scharf testbar.

## Präregistrierung Ziel 3 — MPME-CROSS (neue Gleichungsklasse)

**Warum strukturell neu und cross-sector:** Der Vorgänger koppelte x nur an
Pool-Skalare und die v3-Seam-Funktion; die Residuenmatrix R kam höchstens über
vorextrahierte Integer-Atome (8, 9, 10, 78) vor. Hier geht R **als Matrix**
ein, über ihr charakteristisches Polynom p_R(x) = det(xI − R) = x³ − 9x² +
10x − 8 und die Resolventen-Skala E(x) = p_R(x)/x² — die drei Invarianten
(tr R = 9, Σ-Minoren = 10, det R = 8) wirken als *Koeffizientenstruktur in x*,
nicht als Pool-Einträge. Das entspricht dem cross-sector Charakter der Ratio:
die EW-/Lepton-Seite (geschlossenes m_e) stellt die lineare/Budget-Struktur,
die QCD-/Flavour-Seite die Residuen-Resolvente (v4: R ist die
Compiler-Signatur des Flavoursektors; det R = 8 = h(D5)).

**Klassen (A, B ∈ Pool; N = 794 + 3·630 436 = 1 892 102, Ward 1 891 308):**

| Klasse | Form | Eindeutigkeit (analytisch, maschinell bestätigt) |
|---|---|---|
| C0 Baseline | x − A = 0 | — (Kontrolle) |
| X1 Resolventen-Kubik | det(xI − R) − A·x² − B = 0 | g/x² = E(x) − A − B/x² streng wachsend auf dem Zweig x > ρ_R (E′ > 0 dort, im Probe gecheckt), g < 0 auf (0, ρ_R] ⇒ genau eine positive Wurzel |
| X2 Resolventen-gedressierter Log | x − A − B·ln(x²/p_R(x)) = 0 | L = −ln E streng fallend auf dem Zweig ⇒ g′ = 1 − B·L′ > 1 ⇒ genau eine Wurzel (Zweig x > ρ_R = 7,8568175371…; darunter ist der Log undefiniert, p_R ≤ 0) |
| X3 Cross-Sektor-Produkt | (x − A)·p_R(x)/x³ − B = 0 | g/x³ = (1 − A/x)·E(x) − B; für A > ρ_R beide Faktoren wachsend und positiv für x > A, Produkt ≤ 0 auf (ρ_R, A] ⇒ genau eine Wurzel auf dem Zweig |

ρ_R ist die größte reelle Wurzel von p_R; die anderen zwei Eigenwerte von R
sind komplex (im Probe gecheckt) — der reelle Zweig x > ρ_R ist der physikalische
(Resolvente positiv). Zertifikate wie im Vorgänger: iv-Bracket + Bandscan;
die analytischen Eindeutigkeitssätze sind das Rückgrat (wie W4 im Vorgänger).
λ-Budget: N_eff = 1 891 308, erwartet λ ≈ 0,03–0,09 ⇒ Einzeltreffer wäre
scharf testbar.

## Verdict-Enum (eingefroren, pro Ziel)

- `NO_CANDIDATE` — kein nichttrivialer zertifizierter Kandidat in Toleranz
  und keine exakte Restatement-Lage (gültiges Ergebnis).
- `TRIVIAL_FROM_EXISTING_E` — nur exakte Restatements des Targets aus
  deklarierter Atom-Arithmetik; kein neuer Fixpunkt (Konsistenz-Notiz).
- `CANDIDATE_PASSES_NULLS` — ≥ 1 nichttrivialer zertifizierter Kandidat und
  p < 0.01.
- `CANDIDATE_BUT_LOOK_ELSEWHERE` — ≥ 1 Kandidat, aber p ≥ 0.01.
- `KERNEL_VIOLATION` — Selbsttest schlägt fehl.

## Abgrenzung zu gekillten/angrenzenden Ledger-Zeilen (claim-Felder gelesen)

- **FR.QCD.BUDGET.01** ([C]/[N]/[X]): m_p/m_e als Uncertainty-Budget ±7,5 % mit
  den zwei Externals α_s(M_Z), Lattice-C_p; Kill durch schärferes Lattice-Band.
  Dieser Contract stellt die disjunkte Frage nach einer Externals-freien
  Ward-Identität — jetzt zusätzlich in der R-Matrix-Klasse; das Budget und
  FR.MPME.02 [C] (Transfer-Reproduktion ≈ 1824) bleiben unberührt.
- **FR.POLE.SOLVE.01** ([E]/[C]): der Koide source→pole-Transfer ist der
  nicht-QED 53/54-Operator/Möbius-Generator (Standard-QED excluded, wrong
  sign). Dieser Contract sucht **keinen** Transfermechanismus, sondern prüft
  den Fixpunkt-Status des Targets 2/3 selbst — disjunkte Frage; ein
  TRIVIAL-Verdict bestätigt genau die dortige Lesart (Target = |ℤ₂|/N_fam).
- **FR.MUONG2.01** ([X], Kill 2026-08-04): die aufgelöste μ−2-Bridge ist das
  Disziplin-Vorbild — datierte Kill-Tests werden ernst genommen; nichts hier
  berührt den Vertex.
- **FR.CLOCK.PROBE.01** ([E]/[C]): von den "externalen" Frontier-Schemazahlen
  ist nur das Proton-C_p genuin extern — konsistent mit einem negativen
  Cross-Sektor-Fixpunkt-Ergebnis.
- **PS.RGTEST.01** ([X]/[O]): Pati-Salam/SO(10)-Unifikations-Kill-Test — das
  Higgs-Ziel hier ist die freie-Seam-Kritikalitäts-Residualgröße, kein
  Unifikations-Output; disjunkt.
- **PS.KAPPA.01** ([E]/[C]/[X]/[O]): κ = M_PS/M_s gepinnt O(1) — die
  Skalaron-Skalen-Variante der Higgs-Randbedingung wurde bereits in v166
  verworfen (Skalenselektion); das Target dieses Contracts lebt bei M̄_Pl.
- **ARCH.REVIEW.01 / v79-Firewall** (1920 − 84 + 3λ_C² = 1836.151, verworfen):
  wie im Vorgänger — Pool nur aus deklarierten Atomen, Familie vor Auswertung
  eingefroren, Nullbatterie entscheidet über Numerologie.

## Dateien & Reproduktion

- `fixpoint_ward_frontier.py` — standalone Probe (nur numpy + mpmath), druckt
  Checks + Verdicts pro Ziel.
- `RESULTS.md` — exakte Zahlen nach dem Lauf.

```sh
cd experiments/theory-contracts && python3 fixpoint-ward-frontier-20260917/fixpoint_ward_frontier.py
```

Erwartete Endzeilen: `checks: 37/37 passed`, Verdicts pro Ziel (siehe
RESULTS.md), Exit 0, Laufzeit ~46 s.
