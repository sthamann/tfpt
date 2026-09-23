# TFPT / Universalraum: Operationssatz, Feldwörterbuch, Grundzustandssonde

**Forschungsvertrag, 15. September 2026.** Endliche, nichtarithmetische
Fortsetzung. Kein neuer Hamiltonterm, keine Zustandsauswahl, keine
Promotion, kein vollständiges T1–T8-Tor, kein RH-/Faktorisierungs-/
P-vs-NP-Resultat. Alle Prüfer laufen normal und unter `-OO` mit
byteidentischen Berichten (bis auf Laufzeitfelder); maßgeblich ist
`replay_manifest.json`.

Modellvertrag (unverändert):
\(H=\Delta N_b+g\sum_{A=1}^{60}(b_A^\dagger P_A+P_A^\dagger b_A)\),
\(P_A=\sum_{i<j}W_{A,ij}f_jf_i\), \(N=N_f+2N_b\), 64 Fermionmoden,
60 Bosonmoden, \(WW^\dagger=8I_{60}\), 480 Vertizes. Zahlen am
Prüfpunkt \(g/\Delta=1/20\), ohne \(\mu N\).

## 1. Ergebnis in einem Absatz

Der tatsächlich verfügbare Operationssatz ist jetzt als Entscheidungstabelle
fixiert: die zwei bekannten Kontrollen allein lassen einen Kommutanten der
Dimension 1 444 233 216 (N=3); der nativ vorhandene
Spin(10)×SU(4)-Symmetrierahmen senkt ihn auf exakt **7**, modenweise
Besetzungsmessungen auf **1** — die gesamte offene operative Freiheit ist
damit auf die binäre Frage „Symmetrie als Anweisung verfügbar ja/nein"
zusammengezogen. Das relativistische Feldwörterbuch ist am tatsächlichen
Tensor geprüft: der skalare gleichhändige Weyl-Kanal ist auf allen 60 Zeilen
**exakt null**, der Vertex ist rein (1,0)+h.c.; das Kompositfeld zerfällt in
(3/2,0)⊕(1/2,0). Für den nativen Grundzustand liefert die Sonde: die
Z4-Zentrumsregel (Singuletts nur bei \(N\equiv0\bmod4\)), exakte
Singulett-Multiplizitäten \(1,1,4\) auf den Niveaus k=0,1,2, die exakten
Lanczos-Koeffizienten \(\beta_1^2=480\), \(\beta_2^2=916\),
\(\beta_3^2=299520/229\) mit der rigorosen Krylov-Oberschranke
\(E_0\le-1{,}0942308\,\Delta\) — und den ehrlichen negativen Befund, dass
diese Schranken N=64 **nicht** von den Nachbarsektoren N=59…63 trennen.

## 2. Fundament: npz-freie Quelle (`native_source.py`, 17 Guards)

Alle Objekte (W, J, C3, Cartan-Gewichte FW/BW, Wurzel-Involution BAR/ETA,
die 7 diskreten Symmetriegeneratoren, 60 Lie-Erzeuger, CAR-Helfer) werden
aus der Clifford-/Außenalgebra-Konstruktion rekonstruiert — ohne die
externe Tensorquelldatei, die aus manchen Shells unlesbar ist. Die
Rekonstruktion war in früheren Runden byte-exakt gegen die gepinnte Quelle
geprüft. Zentrale Regression: die volle Zwei-Teilchen-Casimiridentität
\(8W^\dagger W+4C_{\mathrm{Spin}(10)}+4C_{\mathrm{SU}(4)}=120\,I\) auf allen
2016 Paarzuständen, in gaußganzzahliger Arithmetik.

## 3. WP-A: Der Operationssatz und sein Kommutant (`operations_commutant.py`, 307 Guards)

### 3.1 Die Leiter (N=3, 45 504 Dimensionen; N=2, 2 076)

| Satz | Inhalt | Algebra-Dim. | Kommutanten-Dim. (N=3) | (N=2) |
|---|---|---:|---:|---:|
| S0 | {X, N_b} | 14 | 1 444 233 216 | 3 829 536 |
| S1 | + Spin(10)×SU(4)-Erzeuger | 743 583 744 | **7** | **3** |
| S2 | + Clock-Lift | unverändert | 7 | 3 |
| S3 | + Modenbesetzungen {n_r, m_A} | M₄₅₅₀₄ | **1** | **1** |
| S4 | + geladene f-Instrumente | M₄₇₅₈₀ (Union) | 1 | — |

S0-Regression: Algebra-Dimensionen 5 (N=2) und 14 (N=3) wie berichtet.
**Erratum zur Zwischenrunde:** eine frühe Fassung dieses Prüfers rechnete
die S0-Kommutante fälschlich mit \(2m^2\) pro hellem Block; korrekt ist
\(m^2\) (Kommutant von \(M_2\otimes I_m\) ist \(I_2\otimes M_m\)). Der
korrigierte Wert 1 444 233 216 stimmt mit dem v1.6.2-Original
(`minimal_interfaces.py`) und der Parallelsession überein; ein
Regressionstest mit dem exakten Wert verhindert den Rückfall.

### 3.2 Isotypie-Zerlegung von N=3 (exakt)

45504 = 41664 (Λ³) ⊕ 3840 (Boson⊗Fermion). Schur-Funktor-Schälung:
Sym³(16) = 144⊕672, S₂₁(16) = 16′⊕144⊕1200, Λ³(16) = 560 (irreduzibel).

| Block | Dim | Mult | S-Eigenwert | (C_Spin10, C_SU4) | Rolle |
|---|---:|---:|---:|---|---|
| (144, 20) | 2 880 | 2 | 7 | (85, 39) | hell, X-gekoppelt |
| (144, 4̄) | 576 | 2 | 10 | (85, 15) | hell, X-gekoppelt |
| (16′, 20) | 320 | 2 | 12 | (45, 39) | hell, X-gekoppelt |
| (16′, 4̄) | 64 | 1 | 0 (ker S) | (45, 15) | χ-Kompositblock |
| (672, 4̄) | 2 688 | 1 | — | (165, 15) | dunkel |
| (1200, 20) | 24 000 | 1 | — | (141, 39) | dunkel |
| (560, 20′) | 11 200 | 1 | — | (117, 63) | dunkel |

In Λ³(16,4) ist die Zerlegung multiplizitätsfrei; die drei hellen Typen
treten je zweimal auf (eine Kopie pro Seite, von C3 verbunden). Die
Zuordnung erfolgt über Casimir-Eigenwerte auf exakten Spektralprojektoren
und Gewichtszählungen, nicht über Dimensionen. Auffällig und von beiden
Spuren unabhängig bestätigt: **alle drei dunklen Blöcke tragen denselben
Gesamtcasimir 45** (in der Normierung (C_S+C_U)/4); nur die getrennten
Casimire (141/117/165 bzw. 39/63/15, Viertel) trennen sie.

### 3.3 Einordnung

- Die Kommutanten der S1-/S3-Stufen folgen aus der Zerlegung exakt
  (Burnside: ein Skalar pro isotyper Komponente nach X-Verknüpfung).
- Der Clock induziert eine orthogonale Lie-Algebra-Automorphie, erhält
  jede isotype Komponente und ändert über der vollen Symmetrie nichts
  (S2 = S1). Er sitzt im Normalisator, nicht im Zentralisator; als
  eigenständiger Vertrag neben X, N_b (ohne volle Symmetrie) berichtet
  die Parallelsession Algebra-Dimension 84, Kommutant 240 742 144.
- S3: der Trägergraph (X-Kanten + Lie-Kanten + Clock-Kanten) ist in
  beiden Sektoren zusammenhängend ({45504: 1}, {2076: 1}); mit
  Modenbesetzungen bleiben nur Skalare unsichtbar.
- S4: geladene Instrumente verschmelzen die Sektoren zu einer Komponente
  (47 580). Ihre native Verfügbarkeit ist **nicht** hergeleitet
  (T1-offen); CAR+CCR-Irreduzibilität ist ein analytischer Satz, hier
  kein Guard.
- Verfügbarkeits-Theorem (Parallelsession, hier konsistent): Wörter aus
  X, N_b liegen in der 16-dimensionalen Verflechteralgebra
  (\(\sum m_i^2=4+4+4+1+1+1+1\)); die 60 Erzeuger sind nicht darin.
  Der verbleibende symmetrieverträgliche Spielraum ist exakt
  **zweidimensional**: die getrennte Lesbarkeit der beiden Casimire, also
  die Unterscheidung der drei dunklen Blöcke.

**Antwort auf die v1.6.2-§10.3-Frage:** die operative Mehrdeutigkeit ist
auf eine binäre Alternative kollabiert — ist die kontinuierliche Symmetrie
als Anweisung verfügbar (Kommutant 7) oder nicht (1 444 233 216).

## 4. WP-C: Relativistisches Feldwörterbuch (`field_dictionary.py`, 2161 Guards)

Am tatsächlichen Tensor, vor jeder Orts-/Kontinuumsrechnung:

| Kanal | Norm² pro Zeile (60 Zeilen) | Status |
|---|---:|---|
| Skalar, gleichhändig \(\varepsilon_{\alpha\beta}\psi_I^\alpha\psi_J^\beta\) | **0** (exakt, alle 60) | verboten |
| Skalar, gepunktet (0,0) | 0 (exakt) | verboten |
| (1,0), symmetrische Spinorbasis {I, σˣ, σᶻ} | je 64, Summe **192** | erlaubt |
| (0,1), konjugiert | je 64 | erlaubt |

(σʸ = −iε ist antisymmetrisch und gehört zum Skalarkanal; die
symmetrische Basis ist {I, σˣ, σᶻ}.) Dimensionsidentität
C(128,2) = 2080 + 3·2016 = 8128 exakt. **Der Vertex ist rein
(1,0)+h.c.:** der Vermittler trägt eine selbstduale
Tensor-/feldstärkeartige Lorentzstruktur mit drei Komponenten pro
internem Label; der skalare Wechselwirkungskanal ist auf dem tatsächlichen
Tensor exakt null und darf nicht erneut als Wechselwirkung eingesetzt
werden (Regression gesichert).

Kompositfeld: χ = Vermittler × Weyl zerfällt in (3/2,0)⊕(1/2,0);
die Clebsch-Projektoren auf dem 6-dimensionalen (αβ)γ-Raum sind exakt
rational, idempotent, Ränge 4 und 2; flacher Spin-1/2-Anteil 1/3 (als
Konvention deklariert, keine Dynamikaussage). Bilineare f†f: 4096 =
1 (Singulett) + 45 + 15 (Adjungierte, Invarianz exakt geprüft) + 4035
(Rest ehrlich unbestimmt). Schur-Folge: ein zulässiger kinetischer
Operator auf dem irreduziblen 64er-Multiplett ist I₆₄⊗d(p).

## 5. WP-B: Grundzustandssonde (`groundstate_probe.py`, 446 Guards)

### 5.1 Z4-Zentrumsregel (exakt)

Das SU(4)-Zentrum trägt pro Fermionmode Ladung 3 (mod 4), pro Boson 2;
jeder Basispunkt des Sektors N trägt dieselbe Phase \(i^{3N}\),
niveauunabhängig. **Singuletts existieren nur bei \(N\equiv0\bmod4\).**
Die Sektorwahl findet damit nur unter …, 56, 60, 64, 68, … statt; alle
anderen Sektoren haben einen Casimir-Floor.

### 5.2 Singulett-Multiplizitäten (exakt zertifiziert)

| Niveau k | Gewicht-0-Raum | Singuletts mult_k | Zertifizierung |
|---:|---:|---:|---|
| 0 | 1 | 1 | direkt |
| 1 | 480 (= Vertex-Träger) | 1 | modulare Nullität mod 1000000007 und 1000000009 (beide 1) + expliziter Kernvektor (der W-diagonale/R-Zustand) |
| 2 | 442 800 | **4** | doppelt: (a) Weyl-Steinberg-Charakterauswertung auf exakten Gewichtsmultimengen (an k=0,1 validiert, kammerunabhängig); (b) orbit-reduzierte 2785×2785-Casimir-Nullität ≤ 4 (GF(2³¹−1)-RREF) + 4 exakte ganzzahlige Kernvektoren |
| 3 | 257 326 240 (nur gezählt) | — | — |

**Strukturelle Konsequenz:** der Singulett-Raum pro Niveau ist ab k=2
mehrdimensional; die Krylov-Kette aus |F⟩ ist ab dort **nicht** der ganze
Singulett-Sektor. Die Eindeutigkeitsaussage des Worker-Theorems betrifft
den Grundzustand (Spektralaussage) und wird davon nicht berührt; die
Sektor-Aussage „der Singulett" ist dagegen unhaltbar (mindestens 6
Singuletts bis k=2).

### 5.3 Exakte Lanczos-Koeffizienten und Krylov-Schranke

Lochsprache (Niveau k = 2k Löcher + k Bosonen), Besetzungs-Diktat-Arithmetik,
ganzzahlig. Bipartit (α_j = 0, geprüft). Kettenschluss exakt:
T₋v₁ = 480·|F⟩, T₋v₂ = 916·v₁.

\[
\beta_1^2=480,\qquad \beta_2^2=916,\qquad
\beta_3^2=\frac{299520}{229}\approx1307{,}9476
\]

β₃²-Zerlegung: Paar-Casimir-Term 191 692 800 + Boson-Hopf-Streuterm
383 385 600 = 575 078 400 = ‖T₊³F‖² (übereinstimmend mit der
Normenumeration der Parallelsession), geteilt durch ‖v₂‖² = 439 680.
Trägergrößen: 1 → 480 → 108 240 → **15 254 080** (Niveau 3, exakt
gestreamt gezählt; eine frühe Explorationszahl 15 252 960 war um 1120
falsch und ist korrigiert).

Die 4×4-Jacobi-Matrix (diag 0, Δ, 2Δ, 3Δ; gβ-Nebendiagonale) liefert die
rigorose Variationsobergrenze und ihre Ritz-Näherung (numerisch
gekennzeichnet):

\[
E_0(N{=}64,\ \text{Singulett-Krylov})\ \le\ -1{,}0942308\,\Delta,
\qquad |\langle F|\psi_{\rm Ritz}\rangle|^2 = 0{,}3975\;>\tfrac14 .
\]

Der Überlapp ist mit der Worker-Behauptung (> 1/4) auf Krylov-Ritz-Niveau
konsistent; er ist keine exakte Grundzustandsaussage.

**Wand:** β₄² benötigt ⟨v₃|T₋T₊|v₃⟩ auf 15,25 Mio. Zuständen mit
~10¹⁰ Elementaroperationen — jenseits des Budgets. Die Fortsetzung der
Kette ist nur über Symmetriekompression (orbit-/isotypie-reduzierte
Singulettbasis; die Weyl-Steinberg-Maschine liefert mult_k pro Niveau
gratis) oder die Spur-Resummation der Normsequenz ‖Q₊ᵏF‖² gangbar.

### 5.4 Casimir-Floor und Präzisierung der Normierung

Aus der geprüften Paaridentität: das kleinste von null verschiedene
Casimir-Niveau auf Λ² ist 56 in der Erzeugendensummen-Normierung
(_CAS = 56 auf den hellen 60 = (10,6), 120 auf den 1956 dunklen). In der
Normierung der Floor-Formel \(A=\sum P_A^\dagger P_A=(15N_f-(C_S{+}C_C))/2\)
ist derselbe Wert **14** (= 56/4). **Erratum zur Zwischenrunde:** eine
frühe Fassung verwendete 56 in der Floor-Formel (4× zu groß) und
separierte damit fälschlich N=62; mit dem korrekten Wert entfällt diese
Trennung. Regression gesichert.

### 5.5 Sektorfloors und ehrliche Trennungsbilanz (g/Δ = 1/20)

Basis-Floor \(E_{\rm floor}(N)=\min_{N_f}[(N-N_f)/2-\tfrac{15}{800}N_f]\)
(exakt rational). Gegen die Krylov-Obergrenze −1,0942308 Δ:

| N | Floor (exakt) | getrennt? |
|---:|---:|:---|
| 59 | −177/160 | nein (−0,012) |
| 60 | −9/8 | nein (−0,031) |
| 61 | −183/160 | nein (−0,050) |
| 62 | −93/80 | nein (−0,068) |
| 63 | −189/160 | nein (−0,087) |
| 64 | −6/5 | (der Kandidat) |
| ≥ 65 | ≥ −29/160 | ja, weit |

**Befund: diese Schranken trennen N=64 nicht von N=59…63.** Das ist kein
Gegenbeweis zum Worker-Sektortheorem — die Parallelsession berichtet
schärfere rationale Sektorvergleiche —, sondern der exakte Vermerk, welche
Schranke fehlt: die Lücke liegt bei den **Nachbarfloors** (das wahre
sektorweise c_min über alle Λ^{N_f} ist nur nach oben mit 14 begrenzt),
nicht bei der N=64-Oberschranke. Eine längere Lanczos-Kette allein kann
die Sektortrennung daher nicht schließen.

### 5.6 Gruppenzensus

Die 7 geprüften Quellsymmetrie-Generatoren erzeugen eine Gruppe der
Ordnung **768** (nicht die volle Weylgruppe): transitiv auf den 64 Moden,
31 Orbits auf den 2016 Paaren, 5 Orbits auf den 60 Bosonen und auf den
480 Vertex-Trägern. Der Stabilisator einer Mode hat Ordnung 12 und
25 280 Orbits auf den 120 960 (2-Loch + 1-Boson)-Zuständen (Burnside-
gegengeprüft) — die Größenordnung für eine spätere geladene
Antwortrechnung im reduzierten Quotienten.

## 6. Verhältnis zur Parallelsession (v1.6.4)

Der Schwesterordner `universalraum-native-ground-response-20260915`
berichtet unabhängig: die Normenumeration ‖Q₊ᵏF‖² = 1, 480, 439 680,
575 078 400, 952 296 652 800 (k ≤ 4, vollständig enumeriert); den
modellinternen Grundzustandssatz (eindeutiger Spin(10)×SU(4)-Singulett-
Grundzustand bei N=64 für 0 < |g|/Δ ≤ 1/20; −1,158089 Δ < E₀ <
−1,129636 Δ; Lücke > 0,007737 Δ); die geladene Antwort auf dem
Grundzustand mit den exakten Momenten m₀ = 1, m₁ = 0, m₂ = g²S,
m₃ = g²(ΔS+7a), S = 15 − 7b̄/32, den Schranken 0,842846 < b̄ < 1,245656
und Z_low > 0,880076280689; den Polsatz (64-fach entartete isolierte
Entnahmelinie) und den Ausschluss der exakten Zwei-Linien-Antwort.

Übereinstimmungen, wo sich beide Spuren überschneiden: die
N=3-Zerlegung (7 Blöcke, Multiplizitäten 2,2,2,1,1,1,1), alle
Casimirwerte, der S1-Kommutant 7, der S0-Kommutant 1 444 233 216 (nach
unserer Korrektur), die Normen 480 / 439 680 / 575 078 400 (unsere
β-Zähler), der Skalarkanal-Ausschluss. Nichts in dieser Sonde
widerspricht v1.6.4; unsere Trennungsbilanz (§5.5) präzisiert, welche
Schranke für eine vollständig eigenständige Sektorwahl noch zu liefern
ist.

## 7. Was offen bleibt (Rangfolge)

1. **Volle 33-Niveau-Kette:** Normsequenz k = 5…32 über die
   Symmetriespur-Resummation oder die orbit-reduzierte Singulettbasis
   (mult_k gratis aus der Weyl-Steinberg-Maschine). Erst dann: exakte
   Grundenergie, Lücke, ⟨N_b⟩ per Hellmann–Feynman, Verschränkung.
2. **Sektortrennung N=64:** schärfere untere Schranken für N = 59…63
   (echtes sektorweises c_min oder Diagonalisierung in deren
   Singulett-Unterräumen). Voraussetzung für jede „der Grundzustand hat
   N=64"-Aussage aus eigener Rechnung.
3. **mult_k für k ≥ 3** und die vollständige Singulett-Kettenmatrix.
4. **Geladene Antwort auf dem Grundzustand aus eigener Hand** (bisher
   nur über v1.6.4): die Stabilisator-Orbit-Reduktion (25 280 Orbits)
   ist die vorbereitete Größe.
5. **Feldtyp an der Quelle entscheiden:** (1,0)-Vermittler mit Kinetik
   oder nachgewiesene zweite Komponente für einen skalaren Typ.
6. **Präparation:** zahlenerhaltende Kontrollen erreichen N=64 aus dem
   leeren Zustand nicht; e^{−τH}F konvergiert mathematisch, braucht aber
   eine Instrumentenherleitung.
7. **Räumliche Skalierung:** bewusst nicht begonnen — sie trägt erst
   nach Zustand, Antwort und Feldwörterbuch.

## 8. Grenzen

Kein T1–T8-Tor wird geschlossen. Die Krylov-Schranke ist eine
Obergrenze, keine Grundzustandsidentifikation; die Singulett-Zählung ist
exakt, aber die Eindeutigkeit des Grundzustands ist eine Spektralaussage
und hier ungetestet; die Sektorfloors sind notwendige, nicht hinreichende
Bedingungen. Die geladene Antwort auf dem Grundzustand ist in diesem
Ordner nicht neu berechnet, sondern über die Parallelsession referenziert.
Keine RH-, Faktorisierungs- oder P-vs-NP-Aussage. Numerische Guards sind
gekennzeichnet (3 von 446).

## 9. Reproduktion

```sh
cd experiments/theory-contracts/universalraum-operations-groundstate-20260915
/opt/homebrew/bin/python3 replay.py   # vier Prüfer, normal und -OO
```

Maßgeblich sind die PASS-Ergebnisse und die Byteidentität (bis auf
Laufzeitfelder) in `replay_manifest.json`. Guardzahlen zählen
Prüfbedingungen inklusive Komponentenwiederholungen, keine unabhängigen
Theoreme. Kein Commit oder Push in dieser Runde.
