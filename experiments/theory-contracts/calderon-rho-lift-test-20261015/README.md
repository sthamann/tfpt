# Calderón-Lift von ρ? (15. Oktober 2026)

Status: **PARTIAL** (negativer Typisierungsbefund), keine Promotion. `python3 checker.py`:
799 Prüfungen.

* Die erste Quellformel ist P_C = (1+R_τ)/2, ι_C = R_τ
  (`01_boundary_kernel_source.tex:105–135, 159–170`). Ihr Fock-Lift Γ in der *bedingten* Cauchy-CAR-Realisierung (nicht automatisch A_loc) erfüllt:
  a†(f) ↦ a†(R_τ f), Bilineare kovariant, [Γ, Q] = 0, P_C-Vakuum fest,
  Γ dΓ(D) Γ† = dΓ(D_ref − D_rel). Das ist eine Konjugationsidentität für das euklidische/APS-D,
  kein Zeitintertwiner für τ_t.
* ρ ist kein solcher Operator. ρ(0) = r0 ist ein halbgeladener Ls-Grundzustand,
  ρ(Z⁸) ∩ Z⁸ = ∅, und K auf Z⁸ hat einen eindeutigen Grundzustand. Es gibt also keinen
  Lift auf der Z⁸-CAR des Faltungsmodells. Außerdem verbietet das Korollar Z. 172–180 Identifikationen ohne
  Transportabbildung.
* Im Quellkern steht kein Orbifold bzw. verdrillter Sektor. U_Σ ist eine Parameterfamilie
  mit SF = 1, C_Σ ist antiunitär mit Q ↦ −Q.
* Positiv: ρ ist ein Element der affinen E8-Weylgruppe, das −δ fixiert. Ein Tits-Lift im
  gesetzten E8 ist mathematisch nicht ausgeschlossen; er ist aber keine P1/P2-Herleitung des
  Sektors.
* Fehlend: die bosonische Erweiterung D8 → D8 ∪ (D8+s) aus der Quelle. Die ungeraden
  CAR-Felder brauchen dann Defekt- oder Spinsektoren; Z⁸ ∪ (Z⁸+s) ist nicht lokal.

Details: `PROOF.md`.
