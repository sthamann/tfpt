# Fixpunkt-Ward-Suche für m_p/m_e — 17. September 2026

Präregistrierte, endliche Suchrechnung (NON-RH). **Firewall:** dies ist ein
Theory-Contract-Experiment — **keine** Claims in `verification/`,
`status_ledger.csv`, Papers oder Website, keine Beförderung, **niemals** eine
Scorecard-Zeile. m_p/m_e ist eine **`F_transfer`-Brücke, niemals ein primitiver
Compiler-Output** (Frontier-Firewall, `tfpt_4_frontier.tex`; Guard
`FR.TRANSFER.01`). Dieser Contract ändert daran nichts — selbst ein
bestandener Kandidat wäre ein Contract-Ergebnis, kein `[E]`.

## Frage (Hypothese — zu prüfen, nicht zu behaupten)

Gibt es eine Ward-artige Selbstkonsistenzgleichung F(x) = 0, gebaut **nur** aus
Compiler-Objekten, deren **eindeutige positive Wurzel** bei
m_p/m_e = 1836.15267343 (CODATA 2022) liegt — analog zu α⁻¹ als eindeutiger
Wurzel der U(1)-Ward-Identität F_U(1) = 0?

## Das α⁻¹-Template (aus `verification/v3_em_alpha.py`, Ledger EM.FP.01 [E])

Vier Elemente machen das Template aus, alle vier werden hier übernommen:

1. **Ward-Form:** Polynom-Budgetteil in der Unbekannten plus ganzzahliges
   Budget mal transzendenter Selbstkonsistenzterm
   (`a³ − 2c₃³a² − (4/5)c₃⁶·M·log(1/φ_seam(a))`, M = 41) — die Unbekannte
   steht auch im Seam-Argument (Fixpunkt-Charakter).
2. **Eindeutigkeit:** genau ein Vorzeichenwechsel auf dem deklarierten Zweig
   (v3: (0, 0.05)).
3. **Intervallzertifikat:** mpmath-`iv`-Bracket um die Wurzel mit definitem
   Vorzeichenwechsel plus Intervall-Partition mit genau einem
   unbestimmten (Wurzel-)Band.
4. **Inverse Test / Ablation:** gemessener Wert rekonstruiert das ganzzahlige
   Budget; Nachbarbudgets verfehlen das Ziel.

## Eingefrorener Suchraum (vor der ersten Auswertung, keine Erweiterung danach)

**Atome (26, nur deklarierte Compiler-Objekte):**

| Typ | Werte | Provenienz |
|---|---|---|
| ganzzahlig (15) | 1, 2, 3, 4, 5, 8, 9, 10, 16, 40, 41, 48, 78, 240, 248 | 1,2 = Anker a=(1,1,2); 3 = N_fam; 4 = Ankersumme; 5 = g_car (P2); 8 = det R; 9 = tr R; 10 = Σ 2×2-Hauptminoren (A_Λ); 16, 40, 41, 48, 240, 248 = Integer-Skelett (40 = ΣL, 48 = Ω_adm); 78 = ‖R‖²_F = dim E6 |
| rational (8) | 41/10, 55/117, 34/47, 3/26, 16/7, 4/3, 7/6, 1/2 | b₁; Quark-Koeffizienten; Lepton-c; δ |
| transzendent (3) | c₃ = 1/(8π), φ₀ = 1/(6π) + 3/(256π⁴), λ_Y = √(φ₀(1−φ₀)) | P1; Seam-Seed; Yukawa-λ |

**Pool:** Atome ∪ alle Paarprodukte ∪ alle Paarquotienten, exakt
dedupliziert (100-stellig) ⇒ **N_POOL = 794** Budgetkoeffizienten
(Komplexität ≤ 2 Atome pro Koeffizient).

**Gleichungsfamilie (5 Klassen, A, B ∈ Pool, C ∈ Atome; ≤ 5 Atome pro Gleichung):**

| Klasse | Form | Eindeutigkeit | N |
|---|---|---|---|
| W0 Baseline (Kontrolle, kein Ward-Kandidat) | x − A = 0 | — (Wert, keine Wurzel) | 794 |
| W2 quadratische Ward | x² − A x − B = 0 | Descartes: genau eine positive Wurzel | 630 436 |
| W3 Log-Seam-Ward (Lückenform) | x − A − B·ln x = 0 | eindeutig auf Zweig x > B bzw. x < B (g′ vorzeichendefinit) | 630 436 |
| W4 Seam-Log-Ward (v3-Lift) | x − A − B·ln(1/φ_seam(1/x)) = 0 | streng monoton: F′ = 1 − B·L′(x) > 1, da L fallend | 630 436 |
| W1 kubische Ward | x³ − A x² − B x − C = 0 | Descartes: genau eine positive Wurzel | 16 391 336 |

φ_seam ist die v3-Seam-Funktion (pb = 1/(6π), Q = 48c₃⁴·e^(−2a),
φ_seam = pb + Q(1−Q)^(−5/4)) mit Seam-Argument a = 1/x.

**N_TOTAL = 18 283 438 Gleichungen** (davon Ward-Klassen W1–W4:
18 282 644). Eingefroren als Konstanten im Code; der Probe bricht bei
Abweichung ab (KERNEL_VIOLATION).

**Toleranz (eingefroren):** relativ 1·10⁻⁶, Halbfenster
w = 0.00183615267343. Begründung: die verworfene v79-Näherungsformel
(1920 − 84 + 3λ_C² = 1836.151) matchte auf ~10⁻⁶ — ein Kandidat muss
mindestens dieses Niveau erreichen **und** zusätzlich die Nullbatterie
bestehen. (CODATA-Unsicherheit 1.1·10⁻⁷ absolut ist ~16000× enger und wird
nicht als Toleranz benutzt.) Near-Miss-Fenster rel. 10⁻⁴ dient nur dem
Bericht, kein Treffer.

## Nullbatterie / Look-elsewhere (eingefroren)

**M = 200 Surrogate-Familien** (Seed 20260917, `numpy.default_rng`),
gleiche Konstruktion und Komplexität: 15 ganzzahlige Atome log-uniform
gerundet aus [1, 248]; 8 rationale Atome p/q mit p ∈ [1, 60], q ∈ [2, 120];
3 transzendente Atome log-uniform aus [0.039, 0.24] (Wertebereich von
c₃, φ₀, λ_Y). Gleicher Poolbau, gleiche Klassen, gleiches 9-Punkt-Fenster.

Gemessen wird die Trefferrate pro Gleichung in den Ward-Klassen. Erwartungswert
unter Null: λ = Rate · 18 282 644. **Signifikanzschwelle (eingefroren):**
ein Poisson-p-Wert P(X ≥ k | λ) < 0.01 für die beobachtete Kandidatenzahl k.
Damit ist vorab festgelegt: ein einzelner Treffer kann bei λ = O(1)
**nicht** signifikant sein — genau das ist die Look-elsewhere-Disziplin, die
die v79-Formel nicht überstanden hätte.

## Eindeutigkeitszertifikate (wie v3, Intervallarithmetik)

Jeder Fenster-Treffer wird einzeln zertifiziert: mpmath-`iv`-Bracket um die
mit 50 Stellen verfeinerte Wurzel (definiter Vorzeichenwechsel) plus
Intervall-Partition des Zweigs mit genau einem unbestimmten Band. W1/W2:
zusätzlich Descartes (analytisch genau eine positive Wurzel bei positiven
Koeffizienten). W3: Zweigdisziplin x ≷ B, Existenz einer zweiten Wurzel auf
dem anderen Zweig wird protokolliert. W4: F′ > 1 analytisch (L fallend in x),
maschinell per Intervall-Scan bestätigt. **Zertifizierter Kandidat** =
Bracket ok + Eindeutigkeit ok + Wurzel in Toleranz.

## Verdict-Enum (eingefroren)

- `NO_CANDIDATE` — kein zertifizierter Kandidat in Toleranz (gültiges,
  gut dokumentiertes Ergebnis).
- `CANDIDATE_PASSES_NULLS` — ≥ 1 zertifizierter Kandidat **und** p < 0.01.
- `CANDIDATE_BUT_LOOK_ELSEWHERE` — ≥ 1 zertifizierter Kandidat, aber p ≥ 0.01.
- `KERNEL_VIOLATION` — Selbsttest schlägt fehl (Poolgröße ≠ 794, Klassengrößen
  ≠ eingefroren, Template-Selbsttest an v3 fehlgeschlagen, Zertifikatslauf
  bricht ab).

## Abgrenzung zu den gekillten Vorläufern (Ledger, [X]-Felder)

- **FR.QCD.BUDGET.01** ([C], m_p/m_e ≈ 1824 ± 7.5 % als typisiertes
  Uncertainty-Budget über den F_QCD-Transfer; zwei deklarierte Externals
  α_s(M_Z), Lattice-C_p; [X]-Kill: schärferes Lattice-Band könnte 1836.15
  ausschließen): jene Route ist ein Transfer **mit** externen Inputs. Dieser
  Contract stellt die disjunkte Frage, ob eine Ward-Identität **ganz ohne**
  Externals existiert. `NO_CANDIDATE` schärft die ehrliche Grenze aus
  FIRSTPRINCIPLES.BOUNDARY.01 (Externals sind nötig); FR.MPME.02 [C] bleibt
  unberührt.
- **FR.BOLTZMANN.SOLVE.01 / FR.RELIC.SOLVE.01** (integrierte ODE-Löser mit
  eingefrorenen Inputs und Band-Kill-Kriterien; ersetzten die v326-Toys, von
  denen eines 1836.15 **hardcodierte**): deren Sackgasse war das getunte Toy.
  Hier gibt es keine Dynamik, keine Anfangsbedingungen, keine externen Inputs,
  und die Familie ist **vor** der Auswertung eingefroren — Tuning ist
  konstruktiv ausgeschlossen, weil kein Parameter nachträglich bewegt werden
  kann.
- **ARCH.REVIEW.01 / v79-Firewall** (1920 − 84 + 3λ_C² = 1836.151, verworfen):
  die zwei Todesursachen — der SU(9)-Block 84 kommt im Träger D5⊕A3 nicht vor,
  und es gab keinen Mechanismus — werden hier adressiert: (1) der Pool enthält
  nur die 26 deklarierten Compiler-Objekte; (2) das Mechanismus-Problem wird
  nicht durch Behaupten gelöst, sondern statistisch: ein Treffer zählt nur,
  wenn gleichkomplexe Zufallsfamilien ihn nicht ebenfalls erzeugen. Die
  verworfene Formel ist genau der Typ, den die W0-Baseline als Kontrolle
  mitführt — und die Nullbatterie misst, wie oft so etwas zufällig vorkommt.

## Dateien & Reproduktion

- `fixpoint_ward_mpratio.py` — standalone Probe (nur numpy + mpmath),
  druckt Check-Zähler + Verdict.
- `RESULTS.md` — exakte Zahlen nach dem Lauf.

```sh
cd experiments/theory-contracts && python3 fixpoint-ward-mpratio-20260917/fixpoint_ward_mpratio.py
```
