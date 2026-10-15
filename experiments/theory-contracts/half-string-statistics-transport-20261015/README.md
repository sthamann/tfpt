# Statistiktransport durch den Halbstring der Quelle (15. Oktober 2026)

Status: **PARTIAL**, keine Promotion. `python3 checker.py`: 201 Prüfungen (144 + 57 Korrekturprüfungen)
(Struktur exakt, Zahlen mit Gleitkomma-Toleranz) am unveränderten
`v988_psi_lambda_reduction.py:75–96`.

Die erste vorhandene Quellformel ist der Halbstring `D = (Viertelphasen-String)²`
(`half-twist-grade-carry`, §4). Am Originaloperator:

* `D H_r D = H_{r+2} − RD`, R nur am fernen Bogenende, `‖R‖ = 2`, `rank R = 2N_y`.
  ~~Sektorwechsel r → r+2~~ — **zurückgenommen**, siehe Korrektur: Eichverlagerung, Holonomie bleibt i^r.
* Fock-Lift `Γ = (−1)^{N_Bogen}`: fermionischer Erzeuger `c_x → −c_x` auf dem Bogen;
  bosonischer Bilinear `c_x†c_y → χ(x)χ(y) c_x†c_y`; Zeit
  `Γ dΓ(H_r) Γ = dΓ(H_{r+2}) − dΓ(RD)`.
* ~~Monodromie −1 = `exp(2πi v·s)`~~ — **zurückgenommen**: nur Vorzeichen von Γ, keine geprüfte D8-Identität.

Nicht geliefert: das Feld endlicher Energie (Vakuumüberschuss des scharfen Strings,
bulkkorrigierter Halbstring mit Carry U_s offen) und eine Calderón-Formel. Details:
`PROOF.md`.

## Korrektur (15. Oktober 2026, Wilson-Holonomie; bestätigt durch unabhängige Review)

Die Lesart von H1 als Sektorwechsel und von H3 als Monodromieidentität wird
zurückgenommen. Was die Prüfungen W1–W3 und S1–S6 (`checker.py`, jetzt 201 Prüfungen) zeigen:

* **W1/W2 – Eichverlagerung.** `D H_r D` ist unitär äquivalent zu `H_r`. Jede
  Zeilenschleife hat weiterhin die Holonomie `i^r`: Die Naht trägt `i^{r+2}`, die Bindung
  a → a+1 trägt −1. `R` ist genau dieser Kompensator. Es gibt keinen Wechsel r → r+2 und
  keine Verbindung α = ¼ ↔ ¾. Eine onsite-skalare Materieeichung ändert die Holonomie
  nicht; das stand schon in `verification/v1033_charged_disorder.py` („matter-only onsite
  gauge preserves total QWZ holonomy“) und im Round-7-Absatz von
  `articles/2026-08-30/mmst_charged_scaling_limit_en.tex:1882–1885`.
* **W3.** Für gerades r unterscheiden sich die Spektren von `H_r` und `H_{r+2}`. `H_1` und
  `H_3` sind isospektral, dort trennt nur W1.
* **H3** prüfte nur das Vorzeichen von Γ auf Bogenfermionen und `exp(iπ) = −1`. Das ist
  keine geprüfte D8-Monodromieidentität. Der bekannte v/s-Befund `exp(2πi e1·s) = −1`
  steht bereits in `charged-source-time-audit-20260920/PROOF.txt` §2 und
  `source-graded-locality-20260920/PROOF.txt` (3). Er wird hier nicht als neu gezählt.
* **Vorgänger.** Die Viertelversion (scharfe Bogenphase i, Endpunktresiduum mit Rang 2N_y
  und Norm √2) samt Z4-Flussregister steht in `v1033` (`sharp_arc_phase`,
  `finite_qwz_checks`). H1 ist deren Quadrat.
* **S1–S6 – Viertelstring S = exp(iπ N_Bogen/2), D = S².** Geprüft sind:
  - `[Q_ges, S] = 0`, S ist gerade, und `S c S† = −i c` auf dem Bogen. Ad S erhält CAR und
    Bilineare exakt.
  - S ist deshalb **nicht** der ladungstragende E_λ-Erzeuger.
  - `[dΓ(H_r), S] = dΓ(H_r − S H_r S†) S` ist ein Einkörper-Schnittstromoperator auf
    beiden Bogenenden (Naht und a → a+1). Er ist kein skalares Vielfaches von S, also
    keine einzelne Zeitfrequenz.
  - Ein einzelner Endpunkt bzw. Grenzwert braucht eine andere Lokalisierung,
    Renormierung und einen Sektorintertwiner.

Bestehen bleibt: H2 (exakte Fock-Konjugation als Eichidentität) und H4 (Duhamel).
