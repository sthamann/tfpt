# TFPT / Universalraum: Clock als Verklebungsanweisung — exakter Test (keyB)

**Forschungsvertrag v1.6.3 · 15. September 2026 · experiments/, NON-RH**

Getestete Hypothese: *„die native Clock ist die Verklebungsanweisung, die den
einen Baustein zu einem Turm komponiert"*, konkret: der Ordnungs-6-Clock
\(\Lambda^2(C_{3,F})\) zerlegt den 2016-dim Fermion-Paarraum in eine
\(\mathbb{Z}_6\)-gradierte Slot-Struktur über seine sechs rotierten hellen
Unterräume \(V_k = \Lambda^2(G_F)^k\,\mathrm{image}(V)\), \(k=0{,}\ldots{,}5\).

## 1. Ergebnis in einem Absatz

**Partiell.** Die Clock ist exakt eine Ordnungs-6-Signaturpermutations-Symmetrie,
die den 1956-dim dunklen Kern und die 60-dim helle Paarschicht jeweils als Ganzes
erhält und den Paarterm \(W\) nach der rationalen Clock-Gradierung respektiert
(alle außerdiagonalen Übergangsränge sind null). Die sechs rotierten hellen
Räume fallen jedoch **identisch zusammen** — die 6×6-Überlappungstabelle ist
durchweg 60, der Union-Rang ist 60, nicht 360. Die Clock gradiert, aber sie
zerlegt nicht: sie liefert keine \(\mathbb{Z}_6\)-Kachelung des Paarraums und
damit keine kanonische, nicht-gewählte Verklebungsanweisung für einen Turm.

## 2. Unveränderte Quelle und Konventionen

\[
H=\Delta N_b+g\sum_{A=1}^{60}(b_A^\dagger P_A+P_A^\dagger b_A),\quad
P_A=\sum_{i<j}W_{A,ij}f_jf_i,\quad WW^{\mathsf T}=8I_{60},\quad N=N_f+2N_b.
\]

Tensor repo-lokal gelesen (SHA `3f00a089…`), Clock-Konstruktor gepinnt
(`9bf99de7…`). `common.py` verifiziert: \(WW^{\mathsf T}=8I_{60}\), 60 Kanäle ×
8 disjunkte Paare, Gewichtserhaltung auf 480 Paaren, Clock-Lift Periode sechs,
Kovarianz \(W\Lambda^2(G_F)=G_B W\). Alle Arithmetik exakt (ganz oder modular
GF\((p)\) mit CRT-Konsistenz über fünf große Primzahlen).

## 3. Aufgabe 1 — Sechs rotierte helle Räume, Überlappungstabelle

\(V = W^{\mathsf T}/\sqrt{8}\) ist eine Isometrie \(60 \to 2016\);
\(\mathrm{image}(V) = \mathrm{col}(W^{\mathsf T})\) ist der 60-dim helle
Unterraum.  \(M_k = \Lambda^2(G_F)^k W^{\mathsf T}\) (2016×60, ganz).
\(M_6 = M_0\) wird exakt verifiziert (\(\Lambda^2(G_F)^6 = I\)).

### 6×6-Überlappungsränge \(\mathrm{rank}(M_i^{\mathsf T} M_j)\) — **exakt**

| i\j | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| 0 | 60 | 60 | 60 | 60 | 60 | 60 |
| 1 | 60 | 60 | 60 | 60 | 60 | 60 |
| 2 | 60 | 60 | 60 | 60 | 60 | 60 |
| 3 | 60 | 60 | 60 | 60 | 60 | 60 |
| 4 | 60 | 60 | 60 | 60 | 60 | 60 |
| 5 | 60 | 60 | 60 | 60 | 60 | 60 |

**Union-Rang** \(\mathrm{rank}([M_0|\cdots|M_5])\) = **60** (exakt).
Kachel-Rang bei Orthogonalität wäre \(6 \times 60 = 360\).

**Tiling-Verdict: NEIN.** Die sechs rotierten hellen Räume sind paarweise
**identisch**, nicht orthogonal.  Die Clock erhält den hellen Raum als Ganzes
(wie die Kovarianz fordert: \(\Lambda^2(G_F) W^{\mathsf T} = W^{\mathsf T} G_B^{\mathsf T}\)
ist exakt null im dunklen Anteil — siehe Aufgabe 2), sie verschiebt ihn nicht in
fünf weitere disjunkte Slots.

## 4. Aufgabe 2 — Dunkler Kern erhalten

\(\ker W\) hat Dimension 1956.  \(\Lambda^2(G_F)\) erhält \(\ker W\) exakt,
verifiziert über die Projektorenidentität

\[
W\,\Lambda^2(G_F)\,(8I - W^{\mathsf T}W) = 0 \quad\text{(exakt, nnz = 0)}.
\]

Algebraisch aus der Kovarianz \(W\Lambda^2(G_F) = G_B W\):
\(W\Lambda^2(G_F)(8I - W^{\mathsf T}W) = 8G_B W - G_B(WW^{\mathsf T})W = 8G_B W - 8G_B W = 0\).
**Verdict: exakt erhalten.** Die Clock ist eine Symmetrie der Zerlegung
\(2016 = 60\,(\text{hell}) \oplus 1956\,(\text{dunkel})\).

## 5. Aufgabe 3 — Clock auf 60 Boson-Reihen und 480 Trägern

\(G_B\) ist eine **Signaturpermutation** (ein Nichtzero pro Spalte, Bijektion,
Vorzeichen \(\pm 1\)), **Ordnung exakt 6**.

**Permutationszyklen (ohne Vorzeichen):** 12×(3) + 12×(2) = 36 + 24 = 60.
**Signaturzyklen:** 12 Zyklen der Länge 3 mit Vorzeichenprodukt \(-1\),
12 Zyklen der Länge 2 mit Vorzeichenprodukt \(+1\).
Slot-Permutation \(p = (2,0,1,4,3)\) = Zyklen \((0\,2\,1)(3\,4)\) auf den
5 Slots, Vorzeichen \(-1\).  Die Ordnung-6 ergibt sich als
\(\mathrm{lcm}(3\cdot 2_{\text{sgn}}, 2) = 6\) (der Länge-3-Zyklus mit
Vorzeichen \(-1\) hat signierte Ordnung 6, der Länge-2-Zyklus mit
Vorzeichen \(+1\) hat Ordnung 2).

**480 Träger (A, Paar):** Clock wirkt als \((A,\text{Paar}) \mapsto
(G_B(A), \Lambda^2(G_F)(\text{Paar}))\).  Permutationszyklen:
48×(6) + 48×(3) + 24×(2) = 288 + 144 + 48 = 480.  Signierte Ordnung: 6.

## 6. Aufgabe 4 — Kompositionskonsistenz

\(V_1^{\mathsf T} V_0 = M_1^{\mathsf T} M_0\) ist **nicht null** (Rang 60, da
\(V_1 = V_0\)).  Die Zwei-Schicht-Isometrie \(V_1^\dagger V_0 = 0\) gilt
**nicht** — die Schichten fallen zusammen, nicht übereinander.

**Slot-Übergangsmatrix** des Paarterms \(T_+ = W^{\mathsf T}\) nach der rationalen
Clock-Gradierung (Zerlegung durch die Kreisteilungsfaktoren von \(x^6-1\)):
\(\Phi_1\) (\(k=0\), Eigenwert \(+1\)), \(\Phi_2\) (\(k=3\), \(-1\)),
\(\Phi_3\) (\(k=2,4\), \(\omega^2,\omega^4\)), \(\Phi_6\) (\(k=1,5\),
\(\omega,\omega^5\)).

| \(T_+\) Übergang | \(\Phi_1\) (k=0) | \(\Phi_2\) (k=3) | \(\Phi_3\) (k=2,4) | \(\Phi_6\) (k=1,5) |
|---|---:|---:|---:|---:|
| \(\Phi_1\) (k=0) | **12** | 0 | 0 | 0 |
| \(\Phi_2\) (k=3) | 0 | **24** | 0 | 0 |
| \(\Phi_3\) (k=2,4) | 0 | 0 | **0** | 0 |
| \(\Phi_6\) (k=1,5) | 0 | 0 | 0 | **24** |

**Außerdiagonal-Summe = 0** (exakt).  **Slot-Gradierung respektiert: JA.**
Der Paarterm mischt nicht zwischen Clock-Eigenräumen — er respektiert die
rationale \(\mathbb{Z}_6\)-Gradierung.  Diagonalsumme \(12+24+0+24 = 60\)
gleich dem vollen Bosonrang.  Der \(\Phi_3\)-Anteil (Eigenwerte
\(\omega^2,\omega^4\)) ist null: der Bosonraum trägt keine komplexen
Eigenwerte dieser Stufe, nur \(+1\), \(-1\) und \(\omega,\omega^5\).

## 7. Aufgabe 5 — Verdict

| Eigenschaft | Wert | Status |
|---|---|---|
| Clock ist Signaturpermutation Ordnung 6 auf Bosons | ja | **exakt** |
| Clock ist Signaturpermutation Ordnung 6 auf 480 Trägern | ja | **exakt** |
| Dunkler Kern (1956) erhalten | ja | **exakt** |
| Heller Raum (60) erhalten | ja | **exakt** (Union-Rang 60) |
| Sechs rotierte helle Räume orthogonal | **nein** | **exakt** (alle identisch) |
| Kachelung 2016 = 6×60 = 360 | **nein** | **exakt** (Union-Rang 60 ≠ 360) |
| \(V_1^\dagger V_0 = 0\) | nein | **exakt** (Rang 60) |
| Slot-Gradierung respektiert (kein Mixing) | ja | **exakt** (außerdiag. 0) |

**Verdict: PARTIELL.** Die Clock ist eine kanonische, nicht-gewählte Symmetrie
und eine \(\mathbb{Z}_6\)-Gradierung des Modells — sie erhält hellen und dunklen
Raum, sie respektiert die Slot-Struktur des Paarterms — aber sie ist **keine**
Verklebungsanweisung im Sinne einer Turmkomposition: die sechs rotierten Kopien
des hellen Raums fallen zusammen (Union-Rang 60 statt 360), so dass keine
orthogonalen Slots und keine Zwei-Schicht-Isometrie \(V_1^\dagger V_0 = 0\)
entsteht.  Die Clock gradiert das Gebäude, sie baut keinen Turm.

## 8. Diskriminierende Zahlen

- **60** (Union-Rang der sechs rotierten hellen Räume; bei Kachelung 360).
- **60** (jeder Eintrag der 6×6-Überlappungstabelle; bei Orthogonalität 0 außerhalb der Diagonal).
- **0** (außerdiagonale Slot-Übergangssumme; bestätigt Gradierung).
- **12+24+0+24 = 60** (diagonale Slot-Übergangsränge: \(\Phi_1,\Phi_2,\Phi_3,\Phi_6\)).
- **12×Zyklus(3, sgn −1) + 12×Zyklus(2, sgn +1)** (G_B auf 60 Boson-Reihen).
- **48×Zyklus(6) + 48×Zyklus(3) + 24×Zyklus(2)** (Clock auf 480 Trägern, Ordnung 6).
- **36** (Guardzahl, zählt Prüfbedingungen, keine unabhängigen Theoreme).

## 9. Nicht behauptet

Keine physische Herleitung der Clock als Raumzeit-Symmetrie, kein 3+1D-Träger,
keine Promotion nach `verification/`, Ledger, Papers oder Website.  Guardzahlen
zählen Prüfbedingungen, keine unabhängigen Theoreme.  Kein Commit oder Push.
