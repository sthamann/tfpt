# Liefert der originale Naht-/Calderónoperator einen Lift von ρ?

Auftrag (Codex, 15.10.): Gibt der originale Naht- bzw. Calderónoperator einen echten Lift von
ρ(p) = Pp + r0 oder eine kanonische Sektorerweiterung, sodass W4 auf Feldgeneratoren zerlegt
werden kann? Ein formales R = U_s^{−1} W4 im bereits gesetzten E8 zählt nicht, und es wird
kein freier Hamiltonoperator hinzugefügt.

Status **PARTIAL** (negativer Typisierungsbefund), keine Promotion. `python3 checker.py`:
799 Prüfungen; normal und mit `-OO` gleich.

## Erste gültige Quellformel

`_archive/tfpt-45/source_extracts/01_boundary_kernel_source.tex`:

* Z. 105–135 und Beweis Z. 159–170: P_C = (1 + R_τ)/2 und ι_C = 2P_C − 1 = R_τ auf dem
  Cauchy-Daten-Hilbertraum H_∂ der gegebenen APS-Realisierung. Es gilt Seam = Fix(τ_dbl)
  (Z. 115–118).
* Z. 120–124: D_ref = ½(D + τ*Dτ*) und D_rel = ½(D − τ*Dτ*).
* Z. 172–180 (Korollar): τ_dbl, ι_C und ε_car dürfen nicht wörtlich identifiziert werden, nur
  über die angegebenen Restriktions- und Transportabbildungen.
* Z. 480–521: Das operative Seed S = (A_loc, τ_t, Θ, ω, [u_Σ], D_coll) setzt Algebra, Zeit,
  Zustand und D_coll voraus. B_Σ wird aus D_coll induziert. Die Kragennormalform lautet
  D_+ = γ_n(∂_n + B_Σ) (Z. 676–678).
* Die Calderón-Hochstufung bleibt in derselben elliptischen Klasse
  (`02_carrier_source.tex:2168–2200`).

**Wirkung in einer bedingten CAR-Realisierung** (Γ = Fock-Lift von R_τ; Prüfungen C0–C7 am
endlichen Cauchy-Raum). Die endliche Second Quantization der Cauchy-Daten ist eine
*bedingte* CAR-Realisierung. Das operative Originalnetz A_loc (Seed, Z. 480–495) ist damit nicht
automatisch diese CAR-Algebra:

* Fermionischer Erzeuger: Γ a†(f) Γ† = a†(R_τ f).
* Bosonischer Bilinear: Γ a†(f) a(g) Γ† = a†(R_τ f) a(R_τ g).
* [Γ, Q] = 0. Das P_C-Vakuum bleibt bis auf Vorzeichen fest. Dasselbe gilt für jeden Lift
  eines mit P_C kommutierenden Unitärs.
* Konjugationsidentität für D: Γ dΓ(D) Γ† = dΓ(D_ref − D_rel); Γ erhält dΓ(D) genau dann,
  wenn D_rel = 0. D ist hier der euklidische/APS-Dirac-Operator, nicht die gegebene physische
  Zeit τ_t des Seeds. Das ist eine korrekte Konjugationsidentität, **kein Zeitintertwiner**
  für τ_t.

## Typisierung R_τ gegen ρ

| | R_τ (Quelle) | ρ (Codex, auf dem gesetzten L_s) |
|---|---|---|
| Ort | Einteilcheninvolution auf H_∂ der APS-Realisierung | affine Abbildung der E8-Nullmoden, p ↦ Pp + r0 |
| Fock | Bogoliubov-Unitär der bedingten Cauchy-CAR | kein CAR-Operator: ρ(Z⁸) ∩ Z⁸ = ∅ (N2) |
| Vakuum | P_C-Vakuum fest (C1, C7) | ρ(0) = r0, also Wechsel zum Ls-Grundzustand mit Ladung ±½ je Kanal |
| Sektor | sektorerhaltend, Ladung ganzzahlig | vertauscht D8 und D8+s (R10) |
| D-Konjugation | D ↦ D_ref − D_rel (nicht τ_t) | Kρ = K, Qρ = Q, ρ(−δ) = −δ (R3–R5) |

ρ tauscht also das Vakuum mit einem halbgeladenen Grundzustand. Es tauscht nicht bloß
Blattdaten. Gemeinsam sind nur Involutivität und, je nach Wahl, die Dimension; laut Korollar
Z. 172–180 und nach Auftrag ist das kein Identifikationsgrund.

**Kein Lift auf der Z⁸-CAR des Faltungsmodells (N1/N2):** K auf Z⁸ hat die eindeutige Nullstelle p = 0, weil
|δ_k| < ½ für α ∈ {¼, ¾}. ρ bildet jeden ganzzahligen Ladungsvektor auf einen
halbzahligen ab. Deshalb gibt es auf diesem Z⁸-CAR-Fockraum keinen Operator, der ρ hebt; ein Lift
setzt die Sektorerweiterung schon voraus. Ob A_loc diese CAR ist, ist damit nicht entschieden.

**Kanonische Sektorerweiterung?** Weder in `01_boundary_kernel_source.tex` noch im Seed steht
ein Orbifold, ein verdrillter Sektor oder ein Ramond-Sektor (S11). Die Doppelung
M̃ = M_+ ∪ M_+^op liefert die τ-gerade/ungerade Zerlegung desselben Einteilchenraums, aber
keine halbzahligen Ladungen. Eine Eichung von Γ(R_τ) wäre ein zusätzlicher Schritt; die Quelle
schreibt ihn nicht vor.

**Weitere Originaloperatoren:**

* U_Σ ist eine Parameterfamilie U_Σ(λ_Σ√ρ) mit L_Σ = −log det_adm(1 − U_Σ) und SF = 1
  (`tfpt-42.tex:2323, 2327, 5137–5140`). Es gibt keine Modenform und keinen Fock-Lift.
* Die Blattoperation C_Σ ist antiunitär mit C_Σ Q C_Σ^{−1} = −Q (`tfpt-42.tex:7244–7246`).
  Sie ist schon vom Typ her nicht ρ, denn Qρ = Q.

## Was positiv bleibt

Die affine Struktur von ρ ist exakt (R1–R10):

* ρ² = id; ρ fixiert den K-Mittelpunkt −δ.
* Der lineare Teil ist P = Π_{k<4} s_{e_k − e_{k+4}} ∈ W(D8).
* r0 ist eine E8-Wurzel mit K(r0) = 0.
* T = τ_s ρ = ρ τ_s und T² = τ_q.

ρ ist damit ein Element der affinen Weylgruppe von E8, das −δ fixiert. Zwei getrennte
Aussagen:

1. **Mathematisch** ist ein affiner E8/Tits-Lift von ρ im gesetzten E8-Modul **nicht
   ausgeschlossen**. Er erhielte K; Kokzyklus und R² werden hier nicht bestimmt.
2. **Herleitung:** Ein solcher Lift setzt E8, also den Spinorsektor, schon voraus. Er ist
   daher keine Herleitung des fehlenden Sektors aus P1/P2.

**Erste nicht gegebene Quellformel:** eine aus der Quelle (Algebra, D_coll/B_Σ, Doppelung)
kanonisch folgende **bosonische** Erweiterung D8 → D8 ∪ (D8+s) mit einem Intertwiner zum
halbgeladenen K-Grundzustand r0. Die ursprünglichen ungeraden CAR-Felder brauchen dann
ausdrücklich Defekt- bzw. Spinsektoren oder den vollständigen Komplementtransport. Z⁸ ∪ (Z⁸+s)
ist **keine** gewöhnlich lokale gemeinsame Feldalgebra, weil sie v = e1 und s mit der vollen
Monodromie exp(2πi v·s) = −1 enthält. In den geprüften Originalen steht die Erweiterung nicht.
