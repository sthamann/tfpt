# Ergebnisse · Seam-Schließung

Lauf vom 15. September 2026. `status: PASS`, **44 exakte Bedingungen**,
normaler und optimierter Lauf byteidentisch.

Ausgangslage: Die Spiegelungsrunde (`universalraum-seam-reflection-lift-20260915`)
hatte gezeigt, dass die Seam den gemeinsamen Spiegel mit η = −1 selbst
mitbringt, und vier Punkte offen gelassen. Drei davon sind hier exakt
geschlossen oder auf ein bereits benanntes Prinzip reduziert.

## 1 · Der Zweinachbar-Rahmen ist kein Ansatz mehr

In der vollen reellen zirkulanten Quellklasse U = aI + bR + cR² + dR³
(vier Stationen, η = −1) gilt exakt:

**Paarbank-Kovarianz unter dem Seam-Spiegel ⇔ J U J = ±R^m U.**

Das heißt: Die Quelle muss spiegelsymmetrisch sein — modulo der
Link-Umbenennungs-Eichung R^m und eines globalen Vorzeichens. Gerades m:
Symmetrie um eine Stationsachse; ungerades m: um eine Kantenachse. Die
Enumeration über alle 384 Zeilenzuordnungen liefert **genau acht kovariante
Familien, jede zweidimensional** (zwei pro Seam-Achse). Die chiral
unbalancierte Kontrollquelle (1, 2, 0, 5) fällt durch beide Tests.

In der link-lokalen Klasse (Träger = die zwei an den Link grenzenden
Stationen — das ist Geometrie: eine Lücke grenzt an genau zwei Intervalle)
überleben genau vier Lösungen: a = b, a = −b sowie die zwei entarteten
Ein-Stations-Quellen (a, 0) und (0, b), die keinen Paarübergang zwischen
Stationen erzeugen. Verlangt man, dass die Quelle ihren Link überspannt,
bleibt **exakt a = ±b**. Der frühere „Zweinachbar-Ansatz" besteht damit nur
noch aus dem geometrischen Faktum der Lücken, nicht aus einer Modellwahl.

## 2 · Die zwei Uhren verschmelzen zu einer

Die Stationsuhr R (Ordnung 8, R⁴ = −I) und die native innere Uhr G_F
(Ordnung 6, Slot-Permutation (0 2 1)(3 4)) sind **nicht** dieselbe Uhr —
aber sie sind Teile einer einzigen:

| Größe | Ergebnis |
|---|---|
| Kombinierte Uhr T = R ⊗ G_F | Ordnung exakt 24 auf den 4·64 = 256 Fermionmoden |
| Doppeldeckung | **T¹² = −I** exakt — T ist der binäre Lift EINER geometrischen C12 = lcm(4, 6) |
| Spiegel | alle sechs gemeinsamen Lifts S = J ⊗ S_F erfüllen S² = I und S T S⁻¹ = T⁻¹ |
| Gruppe | ⟨T, S⟩ hat exakt 48 Elemente (binäre Diedergruppe) |
| Bosonseite | T_B = P_link ⊗ G_B hat Ordnung 12 **ohne** −I; derselbe Spiegel invertiert sie |

Das Fermionvorzeichen ist also ein einziges gemeinsames −I der vereinigten
Uhr, nicht zwei getrennte Anomalien; die Doppeldeckung ist rein fermionisch.
Die Identifikationsfrage aus der Vorrunde ist damit beantwortet: **nicht
identisch, aber gemeinsam dieder-kovariant unter demselben Spiegel, als eine
binäre C12.** Eine physische Gleichsetzung der C12 mit einer Beobachtungsuhr
wird nicht behauptet.

## 3 · Eine W-Bank pro Link ist keine Kompositionsannahme mehr

Drei exakte Schritte:

1. **Uniformität:** Die Uhr wirkt transitiv auf den vier Links, der Spiegel
   erhält die Linkmenge — Kovarianz erzwingt dieselbe Bank auf jedem Link.
2. **Eindeutigkeit:** WᵀW erfüllt exakt (WᵀW)² = 8·WᵀW mit Spur 480, also ist
   WᵀW/8 ein Projektor vom Rang 60. Der Λ²-Casimir C = 120I − 8WᵀW wird von
   (C − 56)(C − 120) exakt annulliert: Er hat **nur** die Eigenwerte 56
   (Vielfachheit 60) und 120 (Vielfachheit 1956). Die Bosondarstellung kommt
   in Λ²(64) also mit **Multiplizität eins** vor — nach Schur ist die
   G-kovariante Paarbank bis auf Skala eindeutig. W ist nicht eine Wahl,
   sondern die einzige Möglichkeit.
3. **Kopien:** n identische Bänke sind unitär äquivalent zu EINER Bank mit
   Kopplung g√n plus (n−1) völlig entkoppelten freien Bosonbänken. Der
   Fock-Toytest (zwei Bänke, Gesamtbosonzahl-Cutoff 3) bestätigt das
   spektral exakt (alle 20 Eigenwerte, Abweichung < 10⁻⁹). Freie
   Zuschauerbänke verletzen dasselbe Zuschauerverbot, das schon η = −1
   ausgewählt hat — **derselbe Auswahlgrundsatz schließt n ≥ 2**. Der
   verbleibende Skalenfaktor g√n ist ununterscheidbar von g und wandert in
   die ohnehin offene g/Δ-Frage.

## 4 · Was danach noch offen ist

Die Liste ist jetzt kürzer und schärfer:

1. **Physisches g/Δ** — einzige verbliebene Kompositionsgröße. Ableitungsvertrag:
   beide Skalen müssen aus dem Seam-Kernel kommen (QGEO.KERNEL.01, offen).
2. **Rohe Seam → markierter Rand** (QGEO.MARKS.01, konstruktive Geometrie,
   keine endliche Rechnung).
3. **T3 gemeinsamer 3+1D-Ursprung, T4 chirales Maß, T7 dynamischer Spin 2,
   T8 native Präparation** — die großen Tore; kein Tor wird hier geschlossen.

Damit hängen alle verbliebenen Modellfreiheiten der Vier-Bank-Konstruktion an
genau zwei benannten geometrischen Obligationen (MARKS.01, KERNEL.01) plus
den physischen T-Toren — nicht mehr an Ansatz-Entscheidungen im Modell.
