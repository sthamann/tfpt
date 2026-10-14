# Familienanteil des ursprünglichen Fold-Zeitgesetzes an der (10,6)-Gewichtskette

Anschluss: Die hergeleitete Gewichtskette (Codex §§12–14 von
`UR.SEAM.JOINT_WARD_STATE.01`; `native-vertex-marking-bridge-20261014`):
`q = 2λ`, λ eine der 60 gemischten (10,6)-Wurzeln, Familiengewicht = minimales β_F,
geometrischer Vektor h ∈ {±M^j e₁}.

## T1 [E] – Wo eine Relativwirkung zwischen den Beinen herkommen muss

Auf identischen CAR-Moden wirkt jeder Ein-Teilchen-Operator zweitquantisiert als
`X⊗1 + 1⊗X` auf Λ². Eine „Ein-Bein"-Wirkung `X⊗1` bildet Λ² nicht in sich ab. Für den
symmetrischen Ausdruck `Y_C(h) = CᵀA(h) − A(h)C` ist C daher kein zeitgleicher
Einteilchenoperator. Es muss der **relative Transport zwischen zwei Zeitpunkten** in
der bilokalen Austauschstruktur sein,
`S_int = (|g|²/2) Σ_a ∫dτ dσ D_Δ(τ−σ) 𝒥_a(τ,σ)²`
(`source-native-retarded-selection-20260922/PROOF.md` §3). Ist die Zeitentwicklung
familienblind, so ist C = 1 und `Y_1 = A − A = 0`.

## T2 [E] – Das ursprüngliche Fold-Zeitgesetz ist familienabhängig

Zeitgesetz: `K = L0 + δ·Q`, `δ_k = (k+α)/8 − ½` (Codex,
`UR.SEAM.QUOTIENT_LOCALITY_E8.01`). Sei δ_F die Projektion von δ auf den A3-Faktor der
ehrlich gekleideten Clock. Für **jede** der acht Kleidungen und beide α = ¼, ¾ gilt:

* δ_F ≠ 0;
* auf den sechs Familiengewichten der 60 (10,6)-Wurzeln nimmt δ_F die Werte
  `{±x, ±¼, ±¼}` an, mit `x ∈ {3/16, 1/16}`;
* auf den vier Marken entspricht das `d = (¼ + x/2, −¼ + x/2, −x/2, −x/2)`, also dem
  Entartungsmuster **1+1+2**.

Welcher Wert von x vorliegt, hängt von der Kleidung j ab. Die Auswahl der gekleideten
Clock bleibt eine offene Prämisse.

**Folge.** Das ursprüngliche Zeitgesetz liefert, ohne neue Annahme, einen
nichtskalaren Familien-Zeitgenerator δ_F. In der bilokalen Austauschstruktur ist der
relative Familientransport zwischen τ und σ dann `C(τ−σ) = exp(i(τ−σ)δ_F)`. Genau das
fehlte dem familienblinden Kern D_Δ.

Nur als Beobachtung, ohne Behauptung: Das Muster 1+1+2 auf den Marken hat dieselbe
Teilungsform wie der ursprüngliche Anker (1,1,2).

## T3 [E]
`K(λ) = 3/4 + α/2`, also 7/8 bzw. 9/8; das stimmt mit Codex überein.

## Grenzen

1. **Verschiedene Modelle.** δ stammt aus dem gefalteten Nahtfermion, D_Δ aus dem
   nativen W-Modell. Dessen f ∈ (16,4) sind fermionische CAR-Moden, keine
   E8-Stromfelder, und N_f + 2N_b ist nicht die Quellenladung H_q. Die Zeitwirkung
   von δ_F auf den nativen Austausch setzt eine Identifikation der beiden Modelle
   voraus, die nicht bewiesen ist.
2. **Austauschtyp.** Ein lokaler 3+1D-Weyl-Yukawa braucht den Lorentz-Spin-/internen
   Austausch-Intertwiner. δ_F liefert eine Zeit-/Familienstruktur, diesen Intertwiner
   aber nicht.
3. **Kein Massenansatz.** Hier wird kein Y_C ausgewertet und keine Unterdrückung
   eingesetzt; nur die Existenz und Form des quellseitigen Familiengenerators ist
   gezeigt.

## Nächste echte Quellenidentifikation

Gesucht ist die explizite Abbildung zwischen dem gefalteten Nahtfermion (mit δ) und
den nativen (16,4)-Moden des W-Modells, die die Paarstruktur P_A und den Zeitgenerator
gemeinsam transportiert. Erst damit wird `C(τ−σ) = exp(i(τ−σ)δ_F)` zum tatsächlichen
Relativtransport im nativen bilokalen Vertex.
