# Seam-Reflexionsoperator — Ergebnisse

**TFPT / Universalraum · Theory-Contract · 15. September 2026**

Checker: `seam_reflection_operator.py` — **PASS, 5347 exakte Checks**,
normal und `-OO` byteidentisch (nach Entfernen der Laufzeitfelder).
Label: **[exakt]** maschinengeprüft endlich-exakt · **[bedingt]** gilt unter
ausdrücklich genannter Voraussetzung · **[offen]** nicht endlich prüfbar,
ehrlich benannt.

## Die Frage

Abschnitt 15.3 des Spinlift-Hauptdokuments (v1.6.10): *Liefert die
ursprüngliche markierte TFPT-Seam genau dieses gemeinsame Paar von
Spiegelungswirkungen, einschließlich Zustand und Vertex?* Ein positiver
Nachweis würde in dieser Quellenklasse die Mischungswahl und das
Umlaufvorzeichen zusammen ersetzen; ein negativer würde diesen konkreten
Anschluss ausschließen.

## Kurzantwort

**Das Skelett: ja, exakt. Die Auswahl im Modell: erzwungen, exakt. Die
Operatorzuordnung auf dem nativen Modell: konstruiert und termgenau
geprüft, exakt. Die Herleitung dieses Operators aus der rohen Seam:
weiterhin offen (zwei benannte Obligationen).** Das spinoriale Vorzeichen
wird durch die Bedingung „kein freies Zimmer" ausgewählt, nicht aus der
klassischen Seam-Geometrie abgelesen — deren H¹-Wirkung ist unsigniert.

## S1 — Das Seam-Skelett [exakt]

Aus der v177/v180-Normalform (ρ: z↦iz, σ: z↦1/z auf μ4 = {1, i, −1, −i}):

- σρσ = ρ⁻¹ symbolisch verifiziert; die vier Marken sind **ein** Clock-Orbit.
- σ auf den Marken: Permutation `(1 3)` — fixiert 1 und −1, tauscht i ↔ −i
  (Vertex-Typ).
- Induzierte Wirkung auf die vier Kanten des Markenquadrats: `(0 3)(1 2)` —
  der Kantentyp, also genau die **verschobene** Wirkung, die das Modell auf
  den Paarbänken verlangt (L = R·J als Permutation).
- Die beiden Vertex-Reflexionen des Quadrats sind Clock-konjugiert: die Seam
  trägt genau **eine** Reflexionsklasse.
- σ auf H¹(P¹∖μ4): w₁ ↔ w₃, w₂ fest — **alle Vorzeichen +1**. Die
  klassische Geometrie liefert die Permutation, aber keine fermionischen
  Minuszeichen.
- Wache gegen Verwechslung: die dokumentierte ursprüngliche innere Uhr
  (Duad-Konstruktion, Permutation (0 2 1)(3 4)) hat Ordnung **6**, ist also
  nicht die Seam-Clock der Ordnung 4 und nicht der C8-Lift.

## S2 — Erschöpfende Enumeration der Rahmenklasse [exakt]

Alle reellen Zwei-Nachbar-Rahmen auf dem Viererzyklus: 16 signierte Clocks
× 4 Quadratreflexionstypen × 16 Vorzeichenmuster = **1024 Kandidaten**,
Filter: Involution (J² = I), signierte Diederrelation (J R J = R⁻¹),
Paarkovarianz bei Balance (Zeilen-Outer-Products von UJ und LU stimmen bei
a = ±b überein), kein dunkler Mode (Rang(I+R) = 4).

- **64 Survivors, ausnahmslos mit antiperiodischer Holonomie h = −1.**
  Die Bedingungen „gemeinsame Reflexion + Paarkovarianz + kein freies
  Zimmer" erzwingen also das Umlaufvorzeichen und die balancierte Mischung
  (|a| = |b|) — die zwei bisherigen Modellwahlen sind in dieser Klasse
  **keine Wahlen mehr**.
- 16 Survivors pro Reflexionstyp; die Filter unterscheiden die
  Verankerungsklasse (Vertex- vs. Kantentyp auf den Stationen) **nicht** —
  die Seam wählt mit ihrem Vertex-Typ einen Vertreter der zugelassenen
  Menge; beide Klassen tragen dieselbe relative Verschiebungsstruktur.
- 8 Eichorbits unter Stationsvorzeichen-Konjugation (die Wirkung bleibt
  exakt in der Survivor-Menge, geprüft).
- Negativkontrolle [exakt]: dieselbe Vertexpermutation auf den Paarbänken
  erzwingt b = 0 (Mismatch-Eintrag b², nicht a²−b²) — nur die verschobene
  Kantenwirkung trägt die balancierte Nachbarquelle.
- Die dokumentierte Spin-Lift-Konfiguration (Clock (1,1,1,−1), Reflexion
  (1,−1,−1,−1)) ist Survivor.

## S3 — Native Operatorzuordnung [exakt, im arrangierten Modell]

Auf dem 256-Fermion-Vierbankmodell mit dem gepinnten nativen W (In-Repo-
Rekonstruktion, SHA-256 gepinnt):

- **Expliziter Operator:** Σ = signierte Vertexreflexion J auf den
  Stationen ⊗ Identität auf den 64 internen Moden, plus **unsignierte**
  Bankpermutation `(0 3)(1 2)` auf den Bosonenbänken.
- **Term-Level-CAR-Kovarianz:** für alle 16 Survivor-Konfigurationen des
  Seam-Typs `(1 3)` und alle 4 Bänke × 60 Kanäle: die reflektierten
  Paarterme (mit allen CAR-Vorzeichen und Umsortierungen) stimmen exakt mit
  den Zielbanktermen überein — **3840 geprüfte Paare, exakt**. Die
  Paaroperatoren bilden sich als P_e ↦ P_{L(e)} mit Koeffizient +1 ab;
  darum ist die bosonische Reflexion unsigniert (die Rahmenvorzeichen ℓ_e
  heben sich durch V J = L V bankweise weg, ℓ_e² = 1).
- **Zustandsverträglichkeit auf Gram-Niveau:** die Paarantwort B, die
  Transfermatrix T und jeder reduzierte Operator D − kT (k = 8, 1, −2, −4)
  kommutieren exakt mit Σ — **jeder Eigenraum, also auch der Grundraum,
  ist reflexionsinvariant.**
- Striktere Unterklasse [exakt]: 8 der 16 Konfigurationen haben uniforme
  Bankvorzeichen; nur für sie kommutiert auch der *signierte* L mit B.
  Physikalisch ist die Bankseite bosonisch-unsigniert; die Unterklasse ist
  als exaktes Nebenresultat vermerkt.
- Negative Strukturfeststellung [exakt]: auf den 64 nativen Fermionmoden
  existiert **keine** interne Ladungskonjugation als signierte Permutation
  (64/64 Cartan-Gewichte ohne Negatives in der Menge). Die Seam-σ wirkt auf
  H¹ ladungsnegierend (w₁ ↔ w₃ tauscht entgegengesetzte μ4-Charaktere);
  diese interne Realisierung steht im nativen Modell **nicht** zur
  Verfügung — die gefundene Zuordnung wirkt auf den Stationen, nicht
  intern.

## S4 — Toy-Voll-Fock-Zustandsverträglichkeit [exakt, Toy]

8-Moden-Toy (4 Stationen × 2 interne Moden), voller 256-dimensionaler
Fockraum, ganzzahlig:

- [U_Σ, Q] = 0 exakt auf dem gesamten Fockraum (Q = Σ_e P_e†P_e).
- U_Σ² = I (Involution), U_Σ orthogonal.
- Der Füllzustand ist Eigenzustand mit Eigenwert **+1**.
- Der Ein-Loch-Sektor (8×8, exakt) kommutiert mit der Reflexion.
- [bedingt] Die Eindeutigkeit des Grundzustands stammt aus dem
  analytischen Schwachkopplungstheorem des Spinlift-Pakets (zitiert, nicht
  neu bewiesen); ein eindeutiger Grundzustand eines symmetrischen H ist
  automatisch invariant.

## S5 — Wachstumsprobe [exakt, mit offener physikalischer Interpretation]

- **Dunkelmoden-Regel:** det(I + R) = 1 − (−1)ⁿ·h symbolisch für
  n = 3..8, exakt abgetastet für n = 10, 12, 16 (je 40 Stichproben,
  ganzzahlig). Also: **kein dunkler Mode ⟺ h = −(−1)ⁿ** — antiperiodisch
  genau für gerade Zyklen. Im defizienten Fall ist die Nullität exakt 1
  (erschöpfend n ≤ 8). Konsequenz für jede Verfeinerungsfolge: die
  Twist-Bedingung ist größenabhängig alternierend — eine konkrete,
  prüfbare Vorhersage.
- Die antiperiodische Impulsverschiebung k_m = 2π(m + ½)/n besteht auf
  jeder Größe — das fermionische Vorzeichen bleibt sichtbar, während die
  Paarseite blind bleibt.
- **Geladene Band (N2-Kette, als Proxy gelabelt — nicht die zertifizierte
  Dispersion über dem vollen Grundzustand):** ε(k) mit
  e₂ = 2g²/√(Δ² + 48g²) (dokumentierten Wert reproduziert),
  e₄ = −g²(Δ² + 24g²) / (6(Δ² + 48g²)^{3/2}),
  e₆ exakt. Relativistische Form √(m² + c²k²) − m sagt e₆* = 2e₄²/e₂
  voraus. **Residuum R₆ = −g²(Δ² + 18g²) / (45(Δ² + 48g²)^{3/2}) ≠ 0**,
  führend −g²/(45Δ). [offen] Die Band ist bis O(k⁴) mit einer massiven
  relativistischen Form verträglich (automatisch) und weicht bei O(k⁶)
  exakt ab — der relativistische Vergrößerungstest ist damit **nicht
  bestanden und quantifiziert**, nicht entschieden.

## Was damit beantwortet ist — und was nicht

Beantwortet [exakt, in dieser Quellenklasse]:

1. Die Seam trägt genau eine Reflexionsklasse, und ihr Vertex/Kanten-Paar
   ist strukturell genau das vom Modell geforderte (S1).
2. Die gemeinsame Reflexionsforderung plus „kein freies Zimmer" erzwingt
   Umlaufvorzeichen und balancierte Mischung vollständig (S2) — die zwei
   Modellwahlen sind ersetzbar, **sobald** der Operator aus der Seam
   kommt.
3. Der Operator existiert auf dem nativen Vierbankmodell explizit und ist
   zustandsverträglich (S3, S4).

Nicht beantwortet [offen]:

1. **QGEO.MARKS.01 / QGEO.KERNEL.01:** dass die *rohe* Seam die markierte
   Randfläche und den Calderón-Kern als Operatoren produziert — keine
   endliche Rechnung, weiterhin die zwei benannten Obligationen.
2. Das spinoriale Vorzeichen aus roher Seam-Geometrie: hier durch
   „kein freies Zimmer" selektiert, nicht aus der Seam abgelesen (deren
   H¹-Wirkung ist unsigniert).
3. Physikalischer Kopplungswert g/Δ, gemeinsamer 3+1D-Ursprung, chirales
   Maß, dynamischer Spin-2-Sektor: unberührt. **Kein T1–T8-Gate
   geschlossen.**

## Verdict

`conditional_structural_match` — bedingte strukturelle Übereinstimmung:
Skelett exakt, Auswahl erzwungen, Operator konstruiert und termgenau
geprüft; die rohe Seam-Herleitung des Operators bleibt der benannte Rest.
Ein künftiger Beweis von MARKS+KERNEL mit spinorialem Vorzeichen würde
diesen Contract zu einem Abschluss heben; ein Widerspruch dort würde den
Adapter ausschließen — beides sind echte Ausgänge, keine Schleife.
