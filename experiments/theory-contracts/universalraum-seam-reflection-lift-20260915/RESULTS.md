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

## 4 · Die vier offenen Strukturpunkte

`open_points_closure.py`, `status: PASS`, **60 exakte Bedingungen**, normal und
optimiert byteidentisch. Die vier Punkte aus Abschnitt 3 werden einzeln geprüft,
nicht umformuliert.

### P1 · Eine W-Paarbank pro Seam-Link — hergeleitet

Vollständige Aufzählung der D4-äquivarianten Bankplatzierungen auf dem
Stationsquadrat. Kriterien: die induzierte Kopplung muss zusammenhängend sein,
und der induzierte Quellrahmen darf keine freie Fermionrichtung haben.

| Platzierung | Bänke | Komponenten | freie Richtungen η=+1 | η=−1 |
|---|---|---|---|---|
| Ecken | 4 | **4** | 0 | 0 |
| Diagonalen | 2 | **2** | 2 | 2 |
| Zentrum (kollektiv) | 1 | 1 | **3** | **3** |
| **Kanten (Links)** | 4 | 1 | 1 | **0** |

Ecken und Diagonalen zerfallen in mehrere Komponenten, die vier Stationen bilden
dann kein gemeinsames System. Die einzelne kollektive Bank hat Rang 1 und lässt
drei Zuschauerrichtungen. Übrig bleibt genau die Kantenplatzierung, und in ihr nur
der negative Lift. Die Bank pro Link war eine Annahme und ist jetzt eine Folge.

### P2 · Der Zweinachbar-Ansatz — durch vollständige Klassifikation ersetzt

Zuerst exakt bewiesen: für U = Σ c_k R^k ist Spiegelungskovarianz **äquivalent** zu
einem palindromischen Koeffizientenvektor. Der Beweis ist die Identität
R^m Ũ = s · U mit s = ±1, also Ũ = s R^(−m) U — die gespiegelten Quellmoden sind
die vorhandenen, mit Vorzeichen umbenannt. Es bleibt kein Spielraum.

Damit gibt es genau sieben kovariante Familien. Ergebnis über die **ganze** Klasse,
nicht nur über den Zweinachbar-Fall:

| Träger | Familie | η=+1 | η=−1 |
|---|---|---|---|
| 1 Station | (c₀) | frei ok | frei ok |
| 2 Stationen | (c₀, c₀) | **immer Zuschauer** | frei ok |
| 2 Stationen | (c₀, −c₀) | **immer Zuschauer** | frei ok |
| 3 Stationen | (c₀, c₁, c₀) | frei ok | frei ok |
| 3 Stationen | (c₀, 0, −c₀) | **immer Zuschauer** | frei ok |
| 4 Stationen | (c₀, c₁, c₁, c₀) | **immer Zuschauer** | frei ok |
| 4 Stationen | (c₀, c₁, −c₁, −c₀) | **immer Zuschauer** | frei ok |

Der negative Lift wird in **keiner** der sieben Familien ausgeschlossen, der
unverdrehte in **fünf von sieben**. Auf einem Seam-Link gilt das für die ganze
Familie, nicht nur am balancierten Punkt: (c₀, c₀) hat bei η=+1 für jedes c₀ eine
freie Richtung.

Die beiden unverdrehten Überlebenden sind der Einstationsrahmen — der nach P1
unzusammenhängend ist — und der symmetrische Dreistationsrahmen, den P4 ausschließt.

### P3 · Die zwei Clocks — **zurückgezogen und ersetzt**

Die Suche selbst steht: über die vorzeichenbehaftete Slotgruppe, 3840 Elemente auf
den fünf Spin(10)-Slots und 48 auf den drei Farbslots, erfüllt **kein einziges**
G⁴ = −I. Eine Gegenprobe ohne Faktorisierung hat alle 184320 Produkte einzeln
gebildet, ebenfalls 0 Treffer.

**Die daraus gezogene Folgerung war falsch.** Die Suche lief nur über *reelle*
Vorzeichenpermutationen. TFPTs Trägerclock ist aber komplex: v177/v180 geben
ρ: z ↦ iz auf (P¹, μ4) mit den H¹-Charakteren ρ\*w_k = i^k. Ein komplexer Clock kann
keine reelle Vorzeichenpermutation sein — die Suche konnte das gesuchte Objekt
gar nicht enthalten.

Im Cartan-Torus ist er da. `native_mu4_clock.py`, `status: PASS`, **25 exakte
Bedingungen**.

**Kovarianz geschenkt.** Jedes Torus-Element ist W-kovariant, denn Gewichtserhaltung
q_i + q_j = q_A *ist* die Aussage, dass es mit dem Paartensor vertauscht. Exakt
geprüft auf allen 480 getragenen Paaren.

**Die Regel.** Alle Fermiongewichte sind Vorzeichenvektoren, alle Bosongewichte
gerade. Daher gilt ⟨λ,q⟩ ≡ Σλ (mod 2), und

> G⁴ = −I **genau dann**, wenn die Gewichtssumme λ ungerade ist.

**Vollständiger Scan.** Nur λ mod 8 zählt, also sind 28 Spinor- und 19
Farbhistogramme ein Scan über *alle* ganzzahligen Cartan-Gewichte. Das
Sektormuster des Seam-Rings — vier gleich große Sektoren zu je 16 an den vier
primitiven achten Einheitswurzeln — ist erreichbar. **57** Histogrammklassen
erreichen es.

**Die kanonische Realisierung.** λ = (0,0,0,0,0 | 0,1,2), also **ohne jedes
Spin(10)-Gewicht** — der Clock sitzt rein im A3 = SU(4)-Faktor, genau dort, wo
TFPT μ4 hinlegt und wo die Charaktere i^k leben.

| Größe | Ergebnis |
|---|---|
| Fermionsektoren | 16 / 16 / 16 / 16 an ζ₈^1, ζ₈^3, ζ₈^5, ζ₈^7 |
| G_F | Ordnung 8, G_F⁴ = −I |
| Träger G_B | Ordnung 4, Eigenwerte **exakt** μ4 = {1, i, −1, −i} |
| Kovarianz | W Λ²(G_F) = G_B W exakt auf allen 480 Paaren |

Fermion Ordnung 8 über Träger Ordnung 4: das ist die binäre Überlagerung aus v480,
nativ in W.

**Die Spiegelung.** Erschöpfende Suche über die volle Weylgruppe von D5 × A3,
1920 × 24 = 46080 Elemente, alle reell: **70** kehren den Clock um mit S² = **+I**,
86 mit S² = −I. Die Gruppe ⟨G_F, S⟩ ist damit die **diedrische** Überlagerung der
Ordnung 16 — dieselbe Gruppe, die der rohe Seam-Ring liefert, nicht die
quaternionische.

**Und der Perioden-sechs-Clock?** Er vertauscht mit dem μ4-Clock und lebt im anderen
Faktor: Perioden-sechs permutiert Spin(10)-Slots, μ4 trägt nur A3-Gewicht.

#### Was hier **nicht** gezeigt ist

- **Keine Eindeutigkeit.** 57 Histogrammklassen erreichen das Sektormuster. Die
  A3-Platzierung passt zu TFPTs eigener Zuordnung, ist hier aber nicht erzwungen.
- **Keine Operatoridentität** mit dem Seam-Stations-Clock. Übereinstimmend sind
  Gruppe, Ordnung, Sektorstruktur und Trägerspektrum — das ist viel, aber es ist
  kein Nachweis, dass es dasselbe Objekt ist.
- Der Perioden-sechs-Clock bleibt ein zweiter, vertauschender Clock im anderen
  Faktor. Nichts hier verschmilzt die beiden.

### P4 · Seam-Lokalität — nachgerechnet

Jede der vier Lücken des Seam-Rings berührt **genau zwei** Intervalle, und die vier
Lücken realisieren exakt die vier Kanten des Stationsquadrats: (0,1), (1,2), (2,3),
(0,3). Eine Quelle, die zu einer Lücke gehört, kann auf zwei Stationen zugreifen.
Träger zwei ist Geometrie der Seam, kein Ansatz.

## 5 · Was ehrlich offen bleibt

**Physisches g/Δ.** Die bewiesenen Fenster 1/2000 und 1/10000 stammen aus einer
Zweizustands-Ritzschranke. Das ist ein Qualitätsproblem der Schranke, kein
Strukturproblem: die Schranke skaliert wie √δ / M mit M der Summe der
Operatornormen, und diese Summe ist der grobe Bestandteil. Eine Resolventen- oder
Schrieffer-Wolff-Behandlung statt der Zweizustandsschranke würde das Fenster
verbreitern. Ein *physischer* Wert für g/Δ folgt daraus trotzdem nicht; dafür fehlt
ein Auswahlprinzip, keine bessere Ungleichung.

**3+1D-Raumzeit, chirales Maß, dynamischer Spin 2.** Das sind Konstruktionen, keine
Prüfungen. Nichts in diesem Ordner berührt sie. Die nächsten minimalen Schritte
sind benannt und jeweils einzeln entscheidbar: ein nichtnulles, vertexkonsistentes
Matrixelement des Feldvertrags (v1.6.9 §4 zeigt, dass der freie Ansatz exakt
verschwindet); eine Größenfolge derselben geladenen Antwort; und erst danach die
Frage nach der Universalitätsklasse im Limes.

Alle T1–T8-Gesamtpflichten bleiben offen. Dies ist ein Forschungsordner, keine
Beförderung.
