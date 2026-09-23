# TFPT / Universalraum: v1.6.9 Lift-Typisierung — getypte Quell-Träger-Audit

**Theorievertrag, 15. September 2026.** Abgetrennter Forschungsordner. Keine
neuen Hamiltonterme, keine Änderung fremder Quellen, keine Promotion nach
`verification/`, kein Ledger-/Paper-/Website-Eintrag, kein T1–T8-Torabschluss.
Paket 1 des v1.6.9-Arbeitsauftrags: jede Abbildung zwischen den ursprünglichen
Quellräumen und dem nativen Träger erhält ihren **Typ** — Darstellung der
Quellalgebra, unitärer Focklift Γ, additive Second Quantization dΓ oder
reelles Messinstrument — und die Multiteilchen-Unterscheidungen werden exakt
bewiesen.

## 0. Antworten zuerst

**Welche bisher freie Wahl wurde eliminiert?** Zwei Schichten. Erstens auf
Operatorebene (v1.6.9, hier typisiert und geguardet): der Einzelmodenimpuls
Z₄ als unabhängig gewährter Operatortyp — ersetzt durch Z_b = e^{iπN_b}, das
auf dem gemeinsamen Dreizustandsraum in der dokumentierten Algebra aus X und
N_b liegt (Dimension fünf, Multiplikationsschließung geprüft); der extra
Modenselektor entfällt. Zweitens auf Typebene (neu in diesem Paket): die
freie Wahl, Quellwörter ungetypt „als Operatoren auf dem Träger" zu lesen.
dΓ ist **nicht** multiplikativ (dΓ(AB) ≠ dΓ(A)dΓ(B), exaktes Gegenbeispiel
mit einem einzigen Nichtnulleintrag +1), und Π² = Π überträgt sich **nicht**
auf dΓ(Π) (Eigenwert 2 auf dem Saatpaar, dΓ(Π)² ≠ dΓ(Π)); nur Γ ist
funktoriell (Γ(UV) = Γ(U)Γ(V), exakt für alle 49 Erzeugerpaare und alle
sechs Clockpotenzen). Wer die Typen verwechselt, wird von diesen drei
Prüfungen falsifiziert.

**Welche zusätzliche Annahme bleibt?** Die typisierte Zuordnung der 60
ursprünglichen C4-Gaußstrahlen — deren Überlappungsquadrate exakt
{0, 1/4, 1/2, 1} sind — zu globalen CAR-Charts fehlt weiterhin (kein
Fit, keine Auswahl). Ebenso bleiben Zusatzressourcen: unabhängige
Schaltbarkeit von X und N_b (aus dem fixen H folgt sie nicht,
[Z_b, H] ≠ 0), Zeigerpräparation und bedingte Zeigerkopplung, ursprüngliche
Präparation von p₀ und kalibrierte terminale n₅-Auslese.

**Welches Experiment / welcher Beweis unterscheidet dies von früheren
Modellen?** Der vollständig bilanzierte kleine Versuch auf **einem** Träger
(K₃ aus dem nativen Kanal-0-Stern des gepinnten W): zwei Operationsfolgen
(U·I·U gegen U·Z_b·U) vom selben Anfangszustand p₀ = |4,57⟩, zulässige
Auslese n₅, **alle** Ergebniswahrscheinlichkeiten, Aufzeichnung auf
demselben Träger mit neutralem Zweizustandszeiger (Isometrie mit explizitem
unitärem Koppler), Erhalt aller Paarkohärenzen, exakt **halber** Folgeeffekt
bei ignoriertem Zeiger, und die Arbeitsdeponien **Δ/54** (Impuls) und
**Δ/108** (Recorder), bei d² = 25/27 exakt. Dazu die drei exakten
Multiteilchen-Urteile und die beiden Stabilisatoren (unten).

## 1. Typisiertes Inventar

Typen: **Darst.** = Darstellung der Quellalgebra · **Γ** = unitärer Focklift
(Gruppenhomomorphismus) · **dΓ** = additive Second Quantization
(Lie-Darstellung) · **Instr.** = reelles Messinstrument. Sektor-Spalte:
Einteilchen / Gruppenoperation / Observable auf dem vollem relevanten
Fockraum. Letzte Spalte: physikalische Referenz (**phys.**) oder blöder
Basisname (**Basis**).

### Erzeuger

| Objekt | Träger | Typ | Sektor | Referenz |
|---|---|---|---|---|
| U = Q·diag(1,0,0), V = Q·diag(0,1,1) | C³ (Quelle) | Darst. der 7-dim. Wortalgebra | Einteilchen (Quellsektor) | Basis (parabolischer Anker) |
| 60 Reflexionen r_v = 1 − vv†/2 | C⁴ (Quelle) | Γ-Kandidaten | Einteilchen (Quellsektor); CAR-Chart-Zuordnung **offen** | Basis (Gaußstrahlen) |
| 7 diskrete Quellsymmetrie-Erzeuger | C⁶⁴ | Γ (Λ² ⊕ G_B) | Gruppenoperation auf Fock | phys. (deklarierte Symmetrie) |
| Clock L (Ordnung 6) | C⁶⁴ | Γ | Gruppenoperation; Intertwiner L^k Wᵀ = WᵀG_B^k | phys. |
| 60 Lie-Generatoren so(10)⊕su(4) | C⁶⁴ | dΓ (exterior_square) | Einteilchen → Observable auf Fock | phys. (innere Symmetrie) |
| X = T₊ + T₋, N_b | voller Fockraum | weder Γ noch dΓ eines Einteilchenoperators | Observable (Wechselwirkung/Kontrolle) | phys. |

### Produkte

| Produkt | Befund | Typ |
|---|---|---|
| 49 Produkte der 7 Wörter | abgeschlossen in der 7-dim. Algebra (Koordinatendeterminante −81) | Darst. (Quellsektor C³) |
| Γ(UV) = Γ(U)Γ(V) | **exakt bewiesen** auf Λ² und G_B (49 Paare + 6 Clockpotenzen; Induktion über Wortlänge) | Γ |
| dΓ(AB) = dΓ(A)dΓ(B) | **falsch im Allgemeinen** — Gegenbeispiel unten | dΓ |
| [dΓ(A), dΓ(B)] = dΓ([A,B]) | **exakt bewiesen** (die erhaltene Relation) | dΓ |

### Adjunktionen

| Adjunktion | Befund |
|---|---|
| † auf der 7-Wort-Algebra | **nicht abgeschlossen**: minimale †-Vervollständigung ist ganz M₃ (Dimension 9 ≠ 7, exakt) |
| r_v = 1 − vv†/2 | benutzt † wesentlich; alle 60 Reflexionen unitär (exakt) |
| BAR/ETA (Wurzel-Gegenpaarung) | BW[BAR[A]] = −BW[A], symmetrisch, nichtentartet (aus der gepinnten Quelle geguardet) |
| f_i ↔ f_i†, b_A ↔ b_A† | CAR/CCR-Adjunktion auf dem Fockraum (Trägerseite) |

### Relationen

| Relation | Status |
|---|---|
| WWᵀ = 8 I₆₀ | exakt (geguardet) |
| (WᵀW)² = 8 WᵀW (Hellprojektor) | exakt (geguardet) |
| L^k Wᵀ = Wᵀ G_B^k, k = 0..5 | exakt (geguardet); Vereinigungsrang der sechs Clockbilder **60, nicht 360** (Intertwinerbeweis + direktes modulares Rangzertifikat mod 2³¹−1) |
| 8WᵀW + C_S + C_C = 120 I | exakt (in der gepinnten Quelle geguardet) |
| CAR {f_i, f_j†} = δ_ij | Trägerseite |

### Markierungen

| Markierung | Typ | Befund |
|---|---|---|
| Saatpaar (4,57), Empfängermode 5 | Prozessmarkierungen | brechen die Symmetrie: 768 → 4 (s. §4) |
| Z_b = e^{iπN_b} | Γ_boson(−I₆₀) auf dem bosonischen Fockraum; auf K₃ Element von ⟨X, N_b⟩ | exakt (Matrixidentität auf N=2 geguardet) |
| Z₄ (alt) | Γ(u₄) (passiver Lift des Modenvorzeichens) | außerhalb der K₃-Kontrollalgebra ([Z₄, P_dunkel] ≠ 0, exakt) |
| n_r = dΓ(e_rr) | dΓ / S3-Instrument | exakt auf N=2 für die vier Sternmoden geguardet |
| Recorder V_rec | **Instr.** (Isometrie mit Zeiger) | V†V = I, expliziter Koppler C_R = e^{−iπB⊗(I−X_R)/2} |
| n₅-Auslese | **Instr.** (Lüders-Effekt E) | auf K₃ komprimierbar; Rückwirkung verlässt K₃ (diag(0,6/49,0), exakt) |

## 2. Multiteilchen-Prüfungen (alle exakt, nativer Träger)

**(M1) dΓ(AB) ≠ dΓ(A)dΓ(B).** Matrixeinheiten A = e₀₁, B = e₁₀ auf C⁶⁴:
die Differenz hat **genau einen** Nichtnulleintrag,
[dΓ(AB) − dΓ(A)dΓ(B)]_{(0∧1),(0∧1)} = **+1**. Allgemeine Identität exakt
geguardet: dΓ(A)dΓ(B) − dΓ(AB) = cross(A,B) mit
cross(A,B)(v∧w) = Av∧Bw + Bv∧Aw. Nativer Zeuge mit zwei dokumentierten
Spin(10)-Generatoren L₀, L₁: **3968** gaußganzzahlige Nichtnulleinträge.
Die **erhaltene** Relation ist die Lie-Homomorphie
[dΓ(L₀), dΓ(L₁)] = dΓ([L₀,L₁]) (exakt, null Residuum).

**(M2) Π² = Π ⇏ dΓ(Π)² = dΓ(Π).** Mit dem Saatpaar-Modenprojektor
Π = e₄₄ + e₅₇₅₇ des markierten Prozesses: dΓ(Π)|4∧57⟩ = **2**|4∧57⟩,
aber dΓ(Π)²|4∧57⟩ = **4**|4∧57⟩; die Differenz hat genau einen Eintrag
(+2). Negativkontrolle: ein Rang-**1**-Projektor diskriminiert auf Λ²
**nicht** (Eigenwerte in {0,1}, dΓ(e₄₄)² = dΓ(e₄₄), null Residuum) — die
Unterscheidung braucht Rang ≥ 2.

**(M3) Γ(UV) = Γ(U)Γ(V).** Positivbeweis auf dem Träger: alle **49**
Erzeugerpaare der deklarierten diskreten Gruppe auf Λ² (2016 Dimensionen)
**und** auf dem Bosonlift G_B (60 Dimensionen), ganzzahlig exakt; zusätzlich
Γ(L^k) = Γ(L)^k für alle sechs Clockpotenzen. Jedes Gruppenelement ist ein
Wort in den Erzeugern — paarweise Funktorialität auf den Erzeugern impliziert
Funktorialität auf der ganzen erzeugten Gruppe per Wortlängeninduktion
(benutzt, nicht gesampelt).

**Sektor-Einordnung je erhaltenem Quellwort:** die sieben C³-Wörter gelten
nur im Einteilchen-**Quellsektor** (kein dokumentierter Trägerlift); die 60
C⁴-Reflexionen sind unitäre Quelloperationen (Γ-Kandidaten, Zuordnung offen);
die deklarierten 7 Erzeuger + Clock gelten als **Gruppenoperationen** (Γ) auf
dem Fockraum; die 60 Lie-Generatoren als **Einteilchen**-Operatoren mit
dΓ-Lift; X, N_b, Z_b, n_r als **Observablen** auf dem vollen relevanten
Fockraum.

## 3. Regressionen (geguardet, nicht neu entdeckt)

- **Geordnete Tripelspur:** mit der dokumentierten Ordnung
  (Π₀, Π₁, Π₂) = (P₀, P₊ᵢ, P₊) der Quellstrahlprojektoren zu
  a = (1,0,0,0), b = (1,0,1,0), c = (1,0,i,0):
  tr(Π₀Π₁Π₂) = **(1−i)/4** exakt; die umgekehrte Orientierung gibt
  (1+i)/4; alle drei Paarüberlappungen sind 1/2; alle drei Strahlen (und
  ihr komplex Konjugiertes) sind tatsächliche Quellstrahlen.
- **Reflexionswort-Zeuge:** R₀R₊Rᵢ = diag(−i,1,−i,1) und
  R₀RᵢR₊ = diag(i,1,i,1) exakt; mit dem internen Referenzstrahl (1,1,0,0)
  und Auslesestrahl (1,i,0,0) (beide tatsächliche Quellstrahlen) sind die
  Born-Wahrscheinlichkeiten exakt **1 und 0**. Ohne Kreuzblockreferenz
  sieht die Sonde die Phase nicht (Negativkontrolle).
- Die separate Aufgabe „TFPT-Universalraum-Forschungspaper"
  (Reflexionswort-Transfer) war bei Abruf **aktiv**; ihre Artefakte bleiben
  **pending** — hier werden nur die dokumentierten Werte als Wachen
  geführt, keine Transferbehauptung übernommen.

## 4. Der vollständige aufgezeichnete kleine Versuch (v1.6.9-Fassung)

**Träger:** K₃ = span{p₀, R₇, b₀} im nativen Kanal-0-Stern des gepinnten W
(8 Blätter, Vorzeichen (−1,1,1,−1,−1,1,1,−1); Adapter J isometrisch,
H₉J = JH₃, N_b und Bosonparität erhalten K₃ — alles exakt geguardet).

**Ablauf:** Anfangszustand p₀ = |4,57⟩ in beiden Armen; Folgen
U·I·U (Kontrolle) und U·Z_b·U (Impuls), τ = π/(2Ω), Ω² = Δ²/4 + 8g²;
zulässige Auslese n₅ (Effekt E = diag(0,1/7,0)); Aufzeichnung zur Mitte mit
dem neutralen Zeiger Vψ = (I−B)ψ⊗|0⟩ + Bψ⊗|1⟩.

**Alle Ergebniswahrscheinlichkeiten (exakt, d = Δ/(2Ω), c = cos πd):**

| Arm | P(n₅=1) | P(n₅=0) | P(N_b=1 Ende) |
|---|---|---|---|
| Kontrolle | (1+c)/32 | 1 − (1+c)/32 | 0 (exakt) |
| Impuls | [1+(1−2d²)²−2(1−2d²)c]/64 | 1 − das | d²(1−d²)/2 |
| Mitte (beide) | — | — | (1−d²)/8 |

**Prüfpunkt Δ = 1, g = 1/20** (d² = 25/27 exakt; numerisch, Toleranz 10⁻¹⁴,
zusätzlich gegen die dokumentierten Konstanten mit 10⁻¹⁶ geguardet;
unabhängiges expm-Replay auf dem **neundimensionalen nativen Stern** ohne
symbolische Halbperiodenformel bestätigt beide Arme und den
sechsdimensionalen Recorderprozess):

| Größe | Wert |
|---|---:|
| n₅ ohne Impuls | 0.0002194998817122665 |
| n₅ mit Z_b | 0.0005299169088385700 |
| Differenz | +0.0003104170271263035 |
| Recorder (Zeiger ignoriert) | 0.0003747083952754197 = (p₀+p₁)/2 |
| Recorder-Differenz | +0.0001552085135631517 = **exakt die Hälfte** |

**Paarkohärenz-Erhalt:** V†(O⊗I)V = O für die gesamte Paarblockalgebra
(P_{p₀}, P_{R₇}, und beide Offdiagonal-Kohärenzen |p₀⟩⟨R₇| ± h.c.), exakt;
V†V = I (voller gemeinsamer Gram erhalten); verworfener Zeiger gibt den
echten CPTP-Update (ρ + Z_bρZ_b)/2; Zeigerüberlapp η interpoliert
(1−η)/2 des Impulssignals; Zeigerverzweigungsgewichte = (1−d²)/8;
keine Postselektion.

**Arbeitsdeponien (exakt):** Impuls Δ(1−d²)/4 = **Δ/54**; Recorder
Δ(1−d²)/8 = **Δ/108** am Prüfpunkt. Z_b direkt auf dem unpräparierten Start
hätte keinen Effekt (Z_b p₀ = p₀); die Vorentwicklung ist wesentlich.

**Instrumentengrenze (ehrlich mitgeführt):** die terminale n₅-Lüders-
Rückwirkung erhält K₃ nicht: (n₅J − JE)†(n₅J − JE) = diag(0, 6/49, 0)
exakt — Wiederverwendung desselben Exemplars nach der Endmessung wird nicht
behauptet.

## 5. Symmetrie: voller markierter Prozess vs. W allein

| Gruppe | „W allein" | markierter Prozess |
|---|---:|---:|
| Deklarierte diskrete Gruppe | **768** = 32×24 (BFS, alle Elemente element-exakt kovariant) | **4** (Index 192) |
| … mit Clock | **4608** = 192×24 (Erzeuger kovariant + Homomorphielemma + 64er-Stichprobe) | **8** (Index 576) |
| Lie so(10)⊕su(4) | **60** (alle Generatoren kovariant, X_B gaußganzzahlig) | **34** (26 Richtungen gebrochen, exakter Rang über Q(i)) |

Der markierte Stabilisator (Ordnung 4) ist eine Kleinsche Vierergruppe:
Identität, globale Fermionparität (−I, wirkt auf Paare/Bosonen trivial),
eine farbvertauschende Involution (16 Transpositionen, Modi 4, 5, 57 fest)
und deren Produkt; die signierte Verfeinerung (Zustand statt Strahl) gibt
4 bzw. 4. Z_b und der Paar/Boson-Recorder sind unter **jeder** W-Symmetrie
invariant und schränken den Stabilisator nicht weiter ein (geguardet); das
Fixieren des Saatpaars fixiert den Bosonkanal 0 automatisch (geguardet).

## 6. Ausführbarkeitsklassifikation

| Operation | Typ | repräsentierbar | aus dem dokumentierten Alphabet ausführbar |
|---|---|---|---|
| Deklarierte passive Lifts, Clock | Γ | ja | **ja** (Funktorialität bewiesen) |
| Fixes H = ΔN_b + gX | Observable | ja | **ja** (als feste Summe) |
| Z_b = e^{iπN_b} | Γ_b(−I₆₀) / ⟨X,N_b⟩ auf K₃ | ja | **bedingt**: nur über die dokumentierte bedingte Pulsfolge; unabhängige X/N_b-Schaltbarkeit nicht abgeleitet; aus fixem H nicht ausgebbar ([Z_b,H] ≠ 0) |
| n_r, Z_r = 1−2n_r | dΓ(e_rr) / S3 | ja | **bedingt (S3)**: außerhalb der S0–S2-Wortalgebra ([n₄,WᵀW] hat exakt 210 Nichtnullen, keyD-Befund hier re-guardet) und außerhalb ⟨GROUP, Clock⟩ (keyD) |
| Recorder + Zeiger | Instr. | ja | **nein**: Zeigerpräparation und bedingte Kopplung sind Zusatzressourcen |
| Terminale n₅-Auslese | Instr. | ja | **bedingt**: Effekt komprimierbar, Rückwirkung verlässt K₃ |

**Expliziter Caveat (exakter Gegenzeuge):** ein skalarer Kommutant beweist
weder vollständige Instrumentenkonstruktion noch unabhängige Schaltbarkeit.
Die Spin-1-Matrizen J_x, J_z auf C³ haben einen **skalaren** gemeinsamen
Kommutanten (Nullität 1, exakt), aber ihr Lie-Abschluss ist su(2)
(Dimension **3**), nicht su(3) (Dimension **8**; eine generische su(3)-Richtung
ist nachweislich nicht im Abschluss). Assoziative Vollständigkeit und
dynamische Erreichbarkeit sind verschiedene Aussagen.

## 7. Verifikation

`replay.py` führt die vier Prüfer normal und unter `-OO` aus und verlangt
byteidentische JSON-Ausgaben (bis auf Laufzeitfelder): Status PASS,
**564 Prüfwachen** (source_side 347 exakt; multiparticle 24 exakt;
recorded_experiment 92 = 84 exakt + 8 numerisch; process_symmetry 101 exakt).
Hashes in `replay_manifest.json`. Guardzahlen zählen Prüfbedingungen, keine
unabhängigen Theoreme. „Exakt" heißt ganzzahlig/gaußganzzahlig/rational/
symbolisch bzw. modulares Zertifikat; „numerisch" heißt float64 mit
Toleranz-Guard (nur der Prüfpunkt des Versuchs, §4).

## 8. Grenzen und nicht übernommene Behauptungen

- **Offen:** die typisierte Zuordnung der C⁴-Quellstrahlen zu globalen
  CAR-Charts (die Überlappungsquadrate {0,1/4,1/2,1} allein wählen weder c
  noch Bosonbanken noch die globale Vertexregel).
- **Offen:** unabhängige X/N_b-Schaltbarkeit, Zeigerbereitstellung und
  -kopplung, ursprüngliche p₀-Präparation, kalibrierter n₅-Detektor.
- **Pending:** Artefakte der separaten aktiven Reflexionswort-Transferaufgabe
  (hier nur dokumentierte Werte als Wachen).
- **Lücke:** die v1.6.9-Gesamtschau unter
  `~/Documents/Codex/2026-09-15/gen/outputs/abgleich169/` war aus dieser
  Sandbox nicht lesbar (Operation not permitted); die beiden
  v1.6.9-Hauptdokumente wurden stattdessen aus den eingefrorenen
  Repository-Kopien des Quellkompositions-Ordners gelesen.
- Keine Aussage über räumliche Träger, keine RH-/Faktorisierungs- oder
  P-vs-NP-Aussage, keine abgeleitete Hylæan-Fähigkeit, kein T1–T8-Tor
  geschlossen, keine Promotion nach `verification/`.
