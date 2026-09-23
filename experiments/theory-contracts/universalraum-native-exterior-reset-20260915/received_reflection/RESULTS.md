# Ergebnisse · Seam-Spiegelung

Lauf vom 15. September 2026. `status: PASS`, **331 exakte Bedingungen**, normaler
und optimierter Lauf byteidentisch.

Ausgangslage: Der bedingte Auswahlsatz in Abschnitt 15 von v1.6.10 zeigt, dass eine
gemeinsame Links-rechts-Spiegelung von Fermionorten und Paarbänken gleiche
Gewichtsbeträge erzwingt und danach nur der negative Lift übrig bleibt. Er führt
vier Punkte als nicht hergeleitet: die physische Verfügbarkeit der gespiegelten
Paaroperation, die Wirkung der rohen Seam auf Ecken und Kanten, den
Nächster-Nachbar-Ansatz und das physische g/Δ. Dieser Lauf schließt den zweiten
Punkt und liefert für den ersten die Operatoridentität.

## 1 · Rohe Seam — der antiperiodische μ4-Ring

Unveränderte v480-Geometrie: N = 256, Q = 64, vier Intervalle der Länge 48 ab
Position 8, antiperiodisch.

| Größe | Ergebnis |
|---|---|
| Clock | ρ⁴ = −I exakt, ρ⁸ = I |
| Regionerhaltende Spiegelungen | genau vier, Zentren 63, 127, 191, 255 |
| Lift-Quadrat | S² = +I für alle vier |
| Clock-Konjugation | S ρ S⁻¹ = ρ⁻¹ exakt, ohne Zusatzvorzeichen |
| Zustandsinvarianz | ‖S C S\* − C‖\_max ≤ 1.12·10⁻¹⁴, also ω∘σ = ω |
| Gruppe | S_k = ρ^k S, also ⟨ρ, S⟩ = Diedergruppe der Ordnung 16 |

Die Gruppe ist dieder, nicht dizyklisch. Trotz ρ⁴ = −I ist die Seam-Spiegelung
eine echte Involution. Das ist der Punkt, an dem die Konstruktion hätte scheitern
können und nicht gescheitert ist.

### Der Ecken-Kanten-Versatz ist Geometrie, keine Zusatzannahme

Die Spiegelung mit Zentrum 63 wirkt auf die vier Intervalle (Fermionstationen) als
Permutation `[0, 3, 2, 1]`: Station 0 und 2 fest, 1 und 3 vertauscht. Das ist genau
σ: z ↦ 1/z auf den Marken μ4 = {1, i, −1, −i}, die 1 und −1 festhält und i mit −i
vertauscht.

Dieselbe Spiegelung wirkt auf die vier Lücken (Paarübergänge) als `[3, 2, 1, 0]` —
**ohne feste Kante**. Das ist die um einen halben Schritt versetzte Kantenspiegelung.
Ein Operatoradapter wird nirgends gebraucht: Ecken und Kanten eines Quadrats liegen
um einen halben Schritt versetzt, deshalb erzeugt eine eckenfeste Spiegelung
zwangsläufig die kantenfreie. Die Translierte ρ·σ mit Zentrum 127 ist umgekehrt die
Kantenspiegelung auf den Stationen, `[1, 0, 3, 2]`.

### η ist die Randbedingung der Seam, keine Modellwahl

Die Stationsvorzeichen der Seam-Spiegelung sind `(1, −1, −1, −1)`. Die
Auswahlmatrix J des v1.6.10-Satzes hat die Einträge `(1, η, η, η)`. Beide stimmen
überein für η = −1, und die Vorzeichen entstehen ausschließlich aus der Zahl der
antiperiodischen Umläufe.

Kontrolle auf dem periodischen Ring: dieselben vier Spiegelungen existieren, ihre
Stationsvorzeichen sind `(1, 1, 1, 1)`, also η = +1. Das η in J ist damit die
Randbedingung des Rings. Die TFPT-Seam ist antiperiodisch, weil RP-Zulässigkeit die
Nullmode verbietet (v480) — η = −1 wird nicht gewählt, es wird geerbt.

### Kontrollen

Fünf Ring- und Platzierungsvarianten (N = 128, 256, 512; p0 = 0, 5, 8, 13, 17;
ℓ = 24, 30, 40, 48, 96) liefern durchweg vier Spiegelungen, Stationsbild
`[0, 3, 2, 1]`, Vorzeichen `(1, −1, −1, −1)` und kantenfreies Linkbild `[3, 2, 1, 0]`.
Das Ergebnis hängt nicht an einer Größe.

Negativkontrolle: Verschiebt man ein einziges Intervall um eine Stelle, existiert
**keine** regionerhaltende Spiegelung mehr. Die gemeinsame Wirkung gehört zur
μ4-symmetrischen Konfiguration.

## 2 · Native Quelle — die Spiegelung hebt auf W

Gepinnter Tensor W (60 × 2016, W Wᵀ = 8 I₆₀, Casimir-Identität erneut bestätigt).
Der Clock-Lift permutiert die fünf Spin(10)-Slots als (0 2 1)(3 4), Vorzeichen −1,
Periode sechs auf den 64 Fermionmoden.

Slot-Spiegelungen s mit s p s⁻¹ = p⁻¹: genau sechs. **Alle sechs** heben über
denselben äußeren Lift wie der Clock und erfüllen exakt:

- S_F² = +I auf den 64 Fermionmoden — echte Involution, kein quaternionischer Lift
- S_F G_F S_F⁻¹ = G_F⁻¹ — die Relation σρσ = ρ⁻¹ auf den Fermionressourcen
- **W Λ²(S_F) = S_B W**, exakt, mit ganzzahligem S_B und **unverändertem W**
- S_B² = +I und S_B G_B S_B⁻¹ = G_B⁻¹ auf den 60 Paarkanälen

Damit ist die native Quelle dieder-kovariant, nicht bloß clock-kovariant. Die
Spiegelung trägt Paarübergänge auf Paarübergänge, ohne den inneren Tensor zu ändern.
Genau diese Operatorrelation war in v1.6.10 als fehlend geführt.

## 3 · Auswahl

Mit den aus der Seam gewonnenen Stationsmatrizen statt gesetzten:

- J² = I, J R J = R⁻¹, L = R J mit L² = I
- U J = L (b I + a R), also vertauscht die Spiegelung Onsite- und Nachbargewicht
- Die einzige Obstruktion der Zeilen-Gram-Gleichheit ist exakt a² − b². Daraus
  folgt |a| = |b|.
- Danach: der balancierte Rahmen hat bei η = +1 den Rang 3, also **eine** freie
  Fermionrichtung; bei η = −1 den Rang 4, also **keine**.
- Das ungleiche Gegenmodell a = 3/5, b = 4/5 scheitert an der Spiegelungskovarianz
  mit a² − b² = −7/25.

Beide bislang gesetzten Modellentscheidungen — gleichstarke Mischung und negatives
Umlaufvorzeichen — folgen damit aus einer einzigen Spiegelung, die die Seam selbst
mitbringt.

## 4 · Was das nicht schließt

- Eine W-Paarbank pro Seam-Link bleibt eine Kompositionsannahme.
- Der Zweinachbar-Quellrahmen bleibt ein Ansatz.
- Der innere Perioden-sechs-Clock ist **nicht** mit dem Stations-Clock der
  Periode vier identifiziert. Die Spiegelung existiert auf beiden Ebenen, die
  Clocks sind nicht dieselben.
- Physisches g/Δ, 3+1D-Raumzeit, chirales Maß und dynamischer Spin 2 bleiben offen.
- Alle T1–T8-Gesamtpflichten bleiben offen. Dies ist ein Forschungsordner, keine
  Beförderung.
