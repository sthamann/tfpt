# Ergebnisse · μ₄-Pointing auf der Seam

Lauf vom 17. September 2026. Skript `status: PASS`, **41 exakte Bedingungen**
(ganzzahlig, keine Floats). **Contract-Verdict nach präregistriertem Enum:
PARTIAL** — die Seam trägt kanonisch die C4 samt Vorzeichen −1, aber
Orientierung und Basispunkt sind nachweislich NICHT geometrisch
ausgezeichnet; die Negativkontrolle (abstraktes ℤ₄) diskriminiert wie
gefordert.

Geprüfte Hypothese (Angriff, kein Claim): die Seam trage bereits eine
kanonische μ₄-Pointing-Struktur (Basispunkt 1, Orientierung i, Vorzeichen
−1), und das abstrakte ℤ₄ reiche dafür nicht.

## 1 · B1 — Die C4 ist eindeutig, normal, ihr Vorzeichen ist kanonisch

Vollständige Enumeration von ⟨T,S⟩ (48 Elemente, Replay bestätigt):

| Größe | Ergebnis |
|---|---|
| Ordnung-4-Elemente | **exakt T⁶ und T¹⁸** — alle 24 Elemente S T^k außerhalb ⟨T⟩ sind Involutionen |
| C4-Untergruppen | **genau eine**: {I, T⁶, T¹², T¹⁸} = ⟨T⁶⟩, mit T¹⁸ = (T⁶)³ |
| Normalität | jede der sechs Spiegelungen konjugiert T⁶ ↔ T¹⁸ — die C4 ist normal, also ohne Wahl ausgezeichnet |
| Vorzeichen | einziges Involutionselement der C4 ist (T⁶)² = T¹² = **−I** — die Vorzeichenschicht der Pointing ist kanonisch und IST das Fermionvorzeichen |

Damit trägt die Seam mehr als die Kardinalität 4: die Gruppe selbst und
ihr −1 sind geometrisch erzwungen, nicht gewählt.

## 2 · B2 — Orientierung: pointing-abhängige Graduierung, kein chirales Maß

- **T⁶ = −T¹⁸** exakt als Operatoren auf den 256 Fermionmoden: die zwei
  Pointings liefern **entgegengesetzte** chirale Graduierungen. Die
  Graduierung hängt also echt an der Pointing — ohne Erzeugerwahl ist sie
  unbestimmt (das ist der Diskriminator gegen „Pointing irrelevant").
- (T¹⁸)² = −I und tr(T¹⁸) = 0, ganzzahlig: Eigenwerte nur ±i, **je
  128-fach**. Jede Pointing liefert eine bestimmte, exakt **balancierte**
  Graduierung — **Netto-Chiralität 0**. Aus der μ₄-Orientierung entsteht
  auf dem vollen Modenraum kein chirales Maß, nur eine
  pointing-abhängige ℤ₂-Graduierung. **T4 bleibt offen.**
- Jede der sechs Seam-Spiegelungen vertauscht die Erzeuger (S T¹⁸ S = T⁶):
  die Orientierung ist spiegelungs-ungerade; die Seam-Geometrie, die ihre
  Spiegelungen enthält, zeichnet keinen Erzeuger aus.
- Bosonbank: **T_B⁶ = T_B¹⁸** (= P_link² ⊗ I, Strukturpin) — die
  Orientierung ist ein rein fermionisches Datum, die Paarbänke sehen sie
  nicht.

## 3 · B3 — Basispunkt: keine Station ist ausgezeichnet

- Modellseite: R wirkt als 4-Zyklus **transitiv** auf den Stationen, J
  fixiert genau {0,2}.
- Rohe Seam (v480-Ring, ganzzahlige Kombinatorik, Replay): exakt vier
  stationenerhaltende Spiegelungen, Zentren 63/127/191/255. Ihre
  Stationsbilder sind exakt die vier Spiegelachsen des Quadrats:
  [0,3,2,1] und [2,1,0,3] (Eckenachsen, Fixstationen {0,2} bzw. {1,3})
  sowie [1,0,3,2] und [3,2,1,0] (Kantenachsen, **keine** Fixstation).
- Schnittmenge der Fixmengen über alle vier Spiegelungen: **leer** —
  einen kanonischen Basispunkt gibt es bereits auf der rohen Seam nicht.

## 4 · B4 — Negativkontrolle diskriminiert wie gefordert

Abstraktes ℤ₄ ohne Pointing, realisiert im selben Modell auf der
Bosonseite:

| Test | abstraktes/bosonisches ℤ₄ | gepointete fermionische C4 |
|---|---|---|
| Existenz | ⟨T_B³⟩ hat Ordnung 4 — Kardinalität ist da | ⟨T⁶⟩ eindeutig und normal |
| Vorzeichenschicht | **fehlt**: Involution T_B⁶ = P_link² ⊗ I ≠ −I; −I liegt in **keinem** der 24 Elemente von ⟨T_B, S_B⟩ | T¹² = −I = Fermionvorzeichen |
| Orientierung | — | zwei Erzeuger, entgegengesetzte Graduierungen; Wahl nötig |
| Basispunkt | — | vier Stationen, symmetrisch; Wahl nötig |

Die Negativkontrolle scheitert an der Vorzeichenschicht, und die
Pointing-Tests hängen echt an der Pointing (T⁶ = −T¹⁸): die Kontrolle
**diskriminiert** — die Hypothese ist an dieser Stelle nicht widerlegt.

## 5 · B5 — Markierungsraum und Konsistenz

Markierungsraum M = {Basispunkt ∈ ℤ4} × {Orientierung ∈ ±1}, 8 Elemente.
Die Aktion ist aus den Operatoren verifiziert, nicht positiert: T
kommutiert mit T¹⁸ (Uhr fixiert die Orientierung) und wirkt als 4-Zyklus
auf den Stationen ⇒ t:(b,ε)↦(b+1,ε); jede Spiegelung sendet T¹⁸ zu
(T¹⁸)⁻¹ und wirkt als b↦−b ⇒ s:(b,ε)↦(−b,−ε); T¹² = −I wirkt trivial
(Quotientenaktion). Exakt bestimmt:

- Markierungsgruppe: **8 Elemente**, Relationen t⁴ = s² = 1, s t s = t⁻¹
  — die Diedergruppe **D4** des Stationsquadrats.
- Aktion auf M: **frei transitiv** (Orbit 8, jedes nichttriviale Element
  fixpunktfrei) — M ist ein **D4-Torsor**: exakt acht Markierungen, keine
  ausgezeichnet.

Konsistenz-Replay der pointing-relevanten Seam-Closure-Schnittstelle
(13 der 41 Checks): R⁴ = −I, R⁸ = I, G_F⁶ = I, J R J = R⁻¹, T¹² = −I,
Ordnung 24, sechs Spiegel als Involutionen mit S T S = T⁻¹, |⟨T,S⟩| = 48,
Casimir-Identität des gepinnten Tensors, W Λ²(S_F) = S_B W, S_B² = I,
S_B T_B S_B = T_B⁻¹. Die Markierungswahl ändert keinen Operator — nichts
an der Schnittstelle wird verletzt.

## 6 · Verdict und Konsequenz

**PARTIAL** (präregistriertes Enum). Die starke Form der Hypothese —
„die Seam trägt bereits die volle Pointing" — ist **nicht bestätigt**:
Vorzeichen ja (kanonisch), Orientierung und Basispunkt nein (nachweislich
unbestimmt). Die schwache Form — „abstraktes ℤ₄ reicht nicht" — ist
**bestätigt**: die Negativkontrolle scheitert wie gefordert.

Die ehrliche Schärfe für die offenen Gates:

1. **MARKS.01** bekommt einen exakten endlichen Inhalt: die rohe Seam
   liefert die unorientierte C4 samt −1; der markierte Rand ist die Wahl
   einer von **8 Markierungen** (4 Basispunkte × 2 Orientierungen), auf
   denen die Seam-Symmetrie frei transitiv wirkt. Keine Markierung ist
   ausgezeichnet — die Wahl ist genuin zusätzliches Datum, kein
   Rechenergebnis. MARKS.01 bleibt offen.
2. **T4**: die Pointing induziert höchstens eine pointing-abhängige
   ℤ₂-Graduierung mit Netto-Chiralität 0 — kein chirales Maß. T4 bleibt
   offen.
3. Kein Bezug zur Carrier-Hand-Einordnung (μ₄ als Galois-Getriebe, wahre
   Uhr 30) beansprucht; dieser Contract spricht nur über die Seam-Gruppe
   ⟨T,S⟩ selbst.

Firewall: Experiment, kein Claim; nichts davon geht in `verification/`,
Ledger, Papers, Website oder Scorecard.
