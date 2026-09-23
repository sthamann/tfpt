# Paket 4: v1.6.9-Bosonimpuls als autonomer Prozess — Ergebnisse

**Theorievertrag, 15. September 2026.** Geschlossenes endliches Modell mit
einem zeitunabhängigen H_tot; kein externer Schalter, kein Instantan-Gate
ohne Ressource. Label: **exakt** = ganzzahlig/rational/symbolisch;
**numerisch** = float64 mit Toleranz-Guard; **bedingt** = gewährt, Herkunft
unerklärt; **offen** = fehlendes Primitiv. Prüfpunkt Δ = 1, g/Δ = 1/20.

## 0. Antworten zuerst

- **Welche freie Wahl ist eliminiert?** Der externe Experimentator zur
  Impulsmitte. Frei-Arm und Zb-Arm sind Zweige **eines** autonomen H_tot
  (numerisch: Operator-Gleichheit ≤ 8,9·10⁻¹⁶); die Wahl „Eingriff ja/nein"
  wird zur internen Controller-Präparation (|F⟩ vs |Z⟩) **vor** dem Lauf
  mit bilanzierten Kosten (Präparationsdifferenz +0,002359Δ). Während der
  gemeinsamen Dauer T greift niemand ein.
- **Welche Annahme bleibt?** **Bedingt:** Controller-Switch, neutraler
  Zeiger, Zweigkopplungen und die gemeinsame Auslesezeit T werden gewährt;
  ihre Herkunft aus dem nativen Alphabet ist nicht hergeleitet.
  **Offen:** genau ein konkretes Primitiv — ein geladenes
  Modeninstrument {f_r, f_r†} an einer Mode (N = 2-Präparation, denn
  2 ∉ 4ℤ, exakt).
- **Welches Experiment unterscheidet?** Die unbedingte n5-Statistik bei
  gleicher Quelle, gleicher Dauer, ohne Nachselektion: Kontrolle
  0,0002194998817 → Impuls 0,0005299169088 (Δ ≈ +3,104·10⁻⁴, numerisch,
  Fehler >10⁶ unter dem Effekt); Recorder mit ignoriertem Zeiger exakt
  die Hälfte (+1,552·10⁻⁴).

## 1. Das geschlossene Modell

Hilbertraum (exakt): K₃ (System: |p₀⟩, |R₇⟩, |b₀⟩) × C₃ (Controller:
|F⟩ frei, |Z⟩ Impuls, |R⟩ Recorder) × R₂ (Zeiger) — 18 Dimensionen.
Ein einziger zeitunabhängiger Operator (exakt blockdiagonal, numerisch
hermitesch):

H_tot = H_F (+) H_Z (+) H_R, T = 2τ ≈ 6,0459978808,

  H_F = h₃ ⊗ I (frei, wechselwirkungsfrei, exakt),
  H_Z = (i/T) Log W_Z mit W_Z = (U Z_b U) ⊗ I (Impuls),
  H_R = (i/T) Log W_R mit W_R = (U⊗I) C_R (U⊗I) (Recorder),

C_R = (I−B)⊗I + B⊗X (exakt: unitäre Involution, Determinante −1,
Permutationsmatrix). Gesamtladung N_tot = 2·I₁₈ auf jedem Arm vor/nach
(exakt). Die K₃-Reduktion (h₃, B, Z_b, E) ist exakt gegen den nativen
Stern A = 0 gegengeprüft (H-Invarianz, N_b-Restriktion, n₅-Kompression).

## 2. Unbedingte Statistiken (numerisch)

| Arm | n5 (autonom unter H_tot) | v1.6.9-Referenz |
|---|---:|---:|
| Frei | 0,00021949988171226674 | 0,0002194998817122665 |
| Impuls | 0,0005299169088385697 | 0,00052991690883857 |
| Recorder (Zeiger ignoriert) | 0,0003747083952754186 | (frei+Impuls)/2 exakt |

Effekt +0,00031041702712630295 (Referenz …035); Halbierung exakt per
D_B-Linearität (exakt auf allen 9 Matrixeinheiten) und numerisch auf
10⁻¹² bestätigt. End-Bosonen: frei 0 (exakt), Impuls 25/729 (exakt),
Recorder die Hälfte. Der Impulsarm endet **nicht** bosonfrei (v1.6.9).

## 3. Ressourcenbilanz (Δ = 1; numerisch, Toleranz 10⁻⁹)

| Arm | Ladung | System (init → final) | Wechselwirkung (init → final) | Gesamt |
|---|---:|---:|---:|---:|
| Frei | 2 → 2 | 0 → 0 | 0 → 0 | 0 → 0 |
| Impuls | 2 → 2 | 0 → **+1/54** (≈ 0,01851852) | +0,00235935 → −0,01615917 | erhalten |
| Recorder | 2 → 2 | 0 → **+1/108** (≈ 0,00925926) | −0,00004628 → −0,00930554 | erhalten |

Controller und Zeiger bare je 0 → 0 (exakt); der Controller kehrt
unverändert zurück (Überlapp 1 auf 10⁻¹², numerisch). Kein freies Werk:
die Gesamtenergie ist pro Arm erhalten, die Systemgewinne zahlt exakt die
Wechselwirkung (ΔE_int + ΔE_sys = 0). Die positive Arbeit wird **nicht**
mit unveränderter Rückkehr bei additiven Energien kombiniert — die
Endpunktenergien sind in den Z/R-Zweigen nachweislich nicht-additiv
(‖H_int‖ = 0,76 bzw. 1,17). Präparationskosten (gesamt, Z−F: +0,002359Δ;
R−F: −0,000046Δ) sind die investierte Schaltarbeit vor dem Lauf.

Kohärenzkonto: C_R erhält **alle** Paar–Paar-Kohärenzen (exakt, 4
Operatoridentitäten); die Paar–Boson-Kohärenz wird am Recorder-Schritt
entfernt (exakt, D_B-Identität D_B = (id + Z_b·Z_b)/2). Endzeiger: frei
und Impuls rein (P ≈ 1); Recorder gemischt (Gewichte 107/108, 1/108;
P ≈ 0,98165295; keine Kohärenz). Überlebende Paarkohärenz im
Recorder-Endzustand |ρ₀₁| ≈ 0,0444 ≫ 10⁻³ (numerisch).

## 4. Zeitkovarianz (exakt + numerisch)

[Z_b, H₃] ≠ 0 exakt ([Z_b,H₃]/g ausgeschrieben); U(t)Z_b ≠ Z_bU(t) mit
Zeugnorm 0,509… (numerisch). Urteil: die **Systemoperation ist nicht
zeitkovariant**; das Gesamtmodell ist autonom (H_tot fest). Verzehrte
Energie-/Zeitreferenz (in der Bilanz enthalten): Switch-Zweig +
Wechselwirkungsenergie + gemeinsame Auslesezeit T. Eine bloße Batterie
genügt nicht — ohne Switch/Uhr keine nichtkovariante Operation zu
definierter Zeit (bedingt: Uhrherkunft unerklärt).

## 5. Universell vs. zustandsspezifisch (numerisch)

**Universell:** exp(−iTH_c) = W_c als volle Operatoren (Abweichung ≤
8,9·10⁻¹⁶); zusätzlich auf |R₇⟩, |b₀⟩ (|b₀⟩|0⟩ im Recorder) exakt
nachgeprüft. Umfang exakt: ganz K₃ (Impuls) bzw. K₃⊗R₂ (Recorder) —
kein zustandsspezifischer Trick auf |p₀⟩. Kein universelles
Z_b-Standalone-Gate zu beliebigen Zeiten (nur der volle Arm UZ_bU).

## 6. Fehlendes Primitiv (exakt/offen)

Die Produktpräparation |p₀⟩ trägt N = 2 über Vakuum; 2 ∉ 4ℤ (exakt),
also mit Alphabet ∪ S3 ∪ Q unerreichbar (Schwesterbefund keyD, hier nur
die Ladungsarithmetik neu geprüft). **Einziges fehlendes Primitiv: ein
geladenes Modeninstrument {f_r, f_r†} an einer Mode** (schließt zugleich
n_r und Z_r). Controller, Zeiger, Koppler, Ausleseuhr: bedingt gewährt.

## 7. Verifikation und Grenzen

`replay.py`: beide Prüfer normal und unter `-OO`, Status PASS,
**119 Guards** (65 exakt, 54 numerisch), byteidentische JSON-Berichte
bis auf Laufzeitfelder. Kein T1–T8-Tor geschlossen; keine
RH-/Faktorisierungs-/P-vs-NP-Aussage. Der Controller ist eine
hinzugefügte Ressource (bedingt), kein abgeleiteter Compilerinhalt; die
räumliche Trennung von Sender/Empfänger ist nicht gezeigt.
