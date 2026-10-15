# Statistiktransport durch den ursprünglichen Halbstring

Auftrag (Codex): An den Originaldefinitionen prüfen, ob die Quelle eine Sektorerweiterung,
Defektfusion oder Calderón-Wirkung vorgibt, die den Statistiktransport
`exp(2πi v·s) = −1` (v = e₁, s = (½)⁸, v·s = ½) realisiert, und die erste Quellformel
mit ihrer Wirkung auf einen fermionischen und einen bosonischen Erzeuger samt Zeit
angeben.

## Die erste vorhandene Quellformel

**Quelle:** `verification/v988_psi_lambda_reduction.py:75–96`, unverändert:
QWZ-Zylinder `H_r` mit `T_X = σ_x/(2i) − σ_z/2`, `T_Y = σ_y/(2i) − σ_z/2` und
Nahtbindung `i^r T_X` (Z. 82, 87). r ist der Holonomiesektor, α = r/4.

**Halbstring:** `half-twist-grade-carry/README.md:137–176`, §4:

    D = −1 auf dem Bogen 0 ≤ x ≤ a (alle Zeilen), +1 sonst,
    D = (Viertelphasen-String der Quelle)²,
    R = H_{r+2} D − D H_r.

Dazu der Ladungs-Carry aus §3 (Z. 99–135):
`U_α|q⟩ = ε(α,q)|q+α⟩`, `C U_s C⁻¹ = i U_s`, `[H_0, U_s] = U_s(P_s + 1)`.

## Satz H (am Originaloperator geprüft)

* **H1 – Einteilchen.** `D² = 1` und `D H_r D = H_{r+2} − R D`. R hat Träger nur auf
  den Bindungen a → a+1, `‖R‖ = 2`, `rank R = 2N_y`. Geprüft für
  (N_x, N_y) ∈ {(6,2), (8,4), (10,8)} und alle vier Sektoren r. Der String wechselt
  den Holonomiesektor `r → r+2`, also **α = ¼ ↔ ¾**: Er verbindet genau die beiden
  realen Viertelphasen.
* **H2 – Fock-Lift.** `Γ = (−1)^{N_Bogen}` (Jordan-Wigner, kleiner Zylinder) erfüllt:
  - **fermionischer Erzeuger:** `Γ c_x Γ = −c_x` auf dem Bogen, `+c_x` außerhalb;
  - **bosonischer Erzeuger:** `Γ c_x† c_y Γ = χ(x)χ(y) c_x† c_y` (Vorzeichen nur für
    Bilineare, die das Bogenende überqueren);
  - **Zeit:** `Γ dΓ(H_r) Γ = dΓ(H_{r+2}) − dΓ(RD)`, exakt auf dem vollen Fockraum.
* **H3 – Monodromie.** Ein Quellfermion, das das Stringende umläuft, erhält den Faktor
  −1 = `exp(2πi·½)`. Das ist genau der für einen gemeinsamen lokalen
  Quellfermion-/Spinorsektor verlangte Wert `exp(2πi v·s)`.
* **H4 – Zeitabweichung.** `‖exp(−it DH_rD) − exp(−itH_{r+2})‖ ≤ t‖R‖ = 2t` (Duhamel).

## Was das bedeutet

Die Quelle selbst gibt mit dem Halbstring einen **Defekt/Sektorwechsel** vor: einen
geraden (bosonischen) Operator Γ, der (i) die Holonomiesektoren r ↔ r+2 verbindet,
(ii) mit den Quellfermionen genau die Monodromie −1 hat und (iii) die Zeitentwicklung bis
auf einen Endpunktdefekt mit Norm 2 verschränkt. Das ist die Ising-artige
Unordnungsstruktur, die ein Spinor-/Ramondfeld an das Fermion ankoppelt. Er wird
nicht hinzugefügt, sondern ist das Quadrat des vorhandenen Viertelphasen-Strings.

Ein Spinorfeld der Ladung s verlangt zusätzlich den Carry U_s; nur so ist
`C U_s C⁻¹ = i U_s` (Grad 1) erreicht. D allein hat Grad 2.

## Warum das noch nicht das geladene Feld ist (Originalgrenzen)

`half-twist-grade-carry/README.md:248–277`, §6:
1. **Vakuumüberschuss.** Der scharfe String regt UV- und massive besetzte Moden an. Die
   endlichen Diagnosen dort (N = 8, 16, 32) zeigen einen nicht kleinen
   Energieüberschuss. Das sind Gleitkomma-Messungen, keine asymptotische Schranke.
2. **Ein-Rand-Einschränkung.** Auf die oberen w Zeilen beschränkt entstehen vertikale
   Grenzflächenterme `rank V = 2(a+1)`, `‖V‖ = 2`. Auf niedrigen Randmoden
   verschwinden sie wie O(N^{1−2w}), also O(N⁻³) bei w = 2 (§5, Z. 178–246); das ist eine
   Einteilchenaussage.
3. **Fehlend:** ein bulkkorrigierter Halbstring aus derselben QWZ-Kovarianz mit Carry
   und Kokzyklus, mit einem nichtverschwindenden verschmierten Feld und seinem
   Adjungierten auf dem Vielteilchen-Kern endlicher Energie, gleichmäßigen
   Energieschranken und trägererhaltender lokaler Algebraidentifikation.

## Antwort auf die Arbeitsfrage

* **Sektor/Defekt:** Ja, das Original gibt einen vor, nämlich den Halbstring Γ
  (Sektorwechsel r → r+2, Monodromie −1). Das ist die erste tatsächliche Quellformel
  für den Statistiktransport.
* **Defektfusion:** Zwei Halbstrings fusionieren zu D² = 1 auf dem Bogen; mit dem
  Viertelphasen-String `S` gilt `D = S²`. Die Viertel- und Halbstrings bilden in den
  Holonomiesektoren also die Gruppe Z4 (r → r+1, r → r+2).
* **Calderón-Wirkung:** Eine explizite Calderón-Operatorformel für Γ habe ich in den
  geprüften Stellen nicht gefunden. B_Σ wird laut
  `_archive/tfpt-45/source_extracts/01_boundary_kernel_source.tex:499–521` aus dem
  gegebenen D_coll induziert, ohne Formel für einen Sektorwechsel.
* **Offen:** der bulkkorrigierte Halbstring mit Carry (siehe oben). Ohne ihn ist Γ ein
  Sektorwechsel mit richtiger Statistik, aber kein Feld endlicher Energie.

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
