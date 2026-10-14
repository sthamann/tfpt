# Ward-Markierung → nativer W-Bosonmode → Familiengewicht → geometrischer Vektor h

Positiver Bestand, an den angeschlossen wird:
`source-native-clock-flavor-bridge-20260922/PROOF.md:20–129` (Operatorwörterbuch
Q/Σ/G/T/P ↔ M/U mit N-Metrik und S), `:136–169` (Kanäle von Sym²(16⊗4)),
`source-native-retarded-selection-20260922/PROOF.md` §1–3 (nativer W-Operator
`H = ΔN_b + Σ_A (g b_A† P_A + h.c.)`, `P_A = Σ W_{A,ij} f_j f_i`, 64 CAR-Moden in
(16,4), 60 Bosonen in (10,6), `WW† = 8 I₆₀`, Erhaltungsgröße `N_f + 2N_b`, exakte
Bosonenelimination mit Kern `D_Δ`).

## Satz V [E]

* **V1 – Clock = Viertelrotation der nativen Ladung.** Im TFPT-Rahmen (D5 ⊕ D3 ≅ A3)
  ist Grad 2 der Glue-Graduierung C genau die Menge der 60 (10,6)-Wurzeln (gleich der
  Anzahl nativer Bosonen), Grad 1 die 64 (16,4)-Wurzeln. C wirkt mit i auf (16,4),
  mit −1 auf (10,6) und mit 1 in Grad 0. Auf den nativen Moden ist das
  `C = i^{N_f + 2N_b}`, also die Viertelrotation der Größe, die der native
  Hamiltonoperator erhält. Insbesondere gilt C⁴ = 1 auf den Fermionen: Im nativen
  Modell ist die Clock automatisch die **echte** Z4.
* **V2 – Familiengewichte.** Die D3-Anteile der (10,6)-Wurzeln sind die sechs
  Vektorgewichte ±e_j der 6 = Λ²4. Tᵀ bildet sie bijektiv auf die sechs
  A3-Gewichte mit zweimal +½ und zweimal −½ ab. Das sind genau die sechs minimalen
  Familienlifts `β_F = m + ½`, m eine Permutation von (0,0,−1,−1).
* **V3 – Ward-Boson.** `λ_A = (e₃; 1,0,0)` ist eine (10,6)-Wurzel und
  `Q' = 2(e₃+e₆) = 2λ_A`. Die Ward-Markierung der Quellenladung ist also das Doppelte
  der Ladung **eines nativen Bosonmodes** b_A.
* **V4 – Codex' Wörterbuch exakt bestätigt.** `LᵀL = N = S†S`; die sechs β_F sind
  `±L a_i` mit `a = (e₁, e₃, e₂+2e₃)`; `h_i = S a_i` ist orthonormal; v117:
  `M: h₁ → h₃ → h₂ → h₁`, `U: h₁ → −h₃, h₂ → h₂, h₃ → h₁`.
* **V5 – Kanalbuchhaltung.** `Λ²(16⊗4) = (10,6) ⊕ (120,10) ⊕ (126,6)` (2016),
  `Sym²(16⊗4) = (10,10) ⊕ (120,6) ⊕ (126,10)` (2080). Der native Paarvertex liegt im
  **antisymmetrischen** (10,6), nicht in den symmetrischen Yukawa-Kanälen.

## Die positive Kette

    Quellenladung q  ──Ward──►  q = 2λ_A,  λ_A ∈ (10,6)  =  Ladung eines nativen b_A
                                   │ Familienanteil (6 = Λ²4)
                                   ▼
                          β_F = m_A + ½   (Minimalpaket, zwei ±½)
                                   │ Codex: β_F = ±L a_i
                                   ▼
                          h = S a_i ∈ {±h₁, ±h₂, ±h₃} = ±M^j e₁ (S-Bild)

Der geometrische Vektor h im Einsatz A(h) des Wörterbuchs ist damit der
Familienanteil genau des nativen Bosonmodes, den die Ward-Markierung auswählt. Die
sechs Wahlen sind unter der 24-elementigen Gruppe gleichwertig (Codex: gleiche
Spektralklasse (1,1,4)).

## Was der native Vertex **nicht** liefert

1. **Die relative Clock auf einem Bein.** Der native Vertex ist antisymmetrisch
   (Λ², (10,6)) und liefert die A(h)-Struktur. Der symmetrische Yukawa-Ausdruck
   `Y_C(h) = CᵀA(h) − A(h)C` braucht zusätzlich eine Clock C auf nur einem Bein
   (`source-native-clock-flavor-bridge` §3: eine gemeinsame Basisänderung erzeugt
   sie nicht).
2. **Eine nichtskalare Familienzeitantwort.** Der exakte Eliminationskern `D_Δ` ist
   SU(4)-gleichförmig (`WW† = 8 I`); die normierte lineare Familienantwort im
   symmetrischen Quellenzustand ist einheitlich (`source-native-retarded-selection`).
   Die Ward-Wahl von λ_A legt ein Gewicht fest, liefert aber keine
   familienabhängige Zeitkorrelation.
3. **Den Q-Compiler.** Q wird im Wörterbuch nur durch Ähnlichkeit mitgeführt; aus dem
   nativen Vertex folgt er nicht.

Herkunftsgrenze: Der native W-Operator ist ein vorhandener Kandidat. Seine Herleitung
aus dem P1-Kern und seine Identifikation mit dem gefalteten Nahtfermion sind offen.
V1 ist eine Aussage über den nativen Modellraum, nicht über die gefaltete CAR-Quelle.

## Nächste echte Quellenidentifikation

Ein Operator der Quelle, der auf **einem** Bein des nativen (10,6)-Paars eine
Familienclock einführt. Er müsste ein Element von su(4), U oder M sein, das nicht
mit `WW† = 8 I` vertauscht. In den geprüften Contracts ist er nicht vorhanden.
Kandidat im Bestand: die Deckwirkung U, die laut `source-three-route-closure` §3
von gewöhnlicher Schleifenholonomie getrennt bleibt. Zu prüfen ist, ob die
tatsächliche Kragenverklebung U auf genau ein Bein des Paars wirken lässt.
