# TFPT-Universalraum: Die fünf gesetzten Fugen — Prüfung der Synthese und Vervollständigung

Stand: 14. September 2026. Anschluss an das Manuskript vom 13.09.
(`tfpt_compiler_universalraum_2026-09-13.pdf`), das Anschlusspapier
(`tfpt_anschluss_zellen_seam_2026-09-14.pdf`), die Inversionsprüfung
(`TFPT_UNIVERSALRAUM_INVERSION_2026-09-14.md`) und die daraus destillierte
Ableitungskette („Teil I–III", eingereicht am 14.09.). Alle neuen Befunde sind im
Contract `experiments/theory-contracts/universalraum-fugen-20260914/` maschinell
belegt (27 288 exakte Bedingungen in `checker.py`, 14 Tests, Schur–Weyl-Numerik in
`clebsch_su4.py`; gleicher Quellpin `ba1da931…9e3995` auf `context_instrument.py`).

**Evidenzkonvention** (wie im Manuskript): *gesetzt* = Ausgangsannahme,
*exakt* = Identität/Beweis unter genannten Voraussetzungen, *bedingt* =
Folgerung mit zusätzlicher Zuordnung/Lesart, *offen* = ungeschlossene Herkunfts-
oder Existenzfrage. NON-RH. Keine T1–T8-Schließung, keine Promotion in
`verification/`, Ledger, Papers oder Website.

## 1. Ergebnis in einem Satz

**Von den fünf Fugen, an denen die Ableitungskette bisher stoppte, liefert der
Compiler für zwei (λ und Graph) unter einer einzigen benannten Lesart eine
eindeutige Antwort — den Clebsch-Graphen mit uniformem, positivem Austausch —,
für zwei weitere (Cross-Register-Kopplung, Präparation) einen Beweis, dass sie
*nicht* aus der 248 kommen können, weil Aufzeichnung im E8-fremden Sektor
Sym²(4) lebt, und für die fünfte (Zeitskala) eine Lokalisierung auf ein einziges
Verhältnis t²/Δ; die 240-Bijektion ist als äquivariante Identifikation tot, und
der „c = 8-Kondo-Fixpunkt" ist in Wahrheit eine konforme Einbettung durch Z4-Eichung,
deren A3-Hälfte im Gitter bereits sichtbar ist.**

## 2. Prüfung der eingereichten Synthese

Die Ableitungskette Teil I–III ist gegen die drei Quellen geprüft. Alle dort
genannten Zahlen (Sektoren 45+15+64+64+60, 60 Strahlen in 15 Kontexten,
K = B/7 mit 1/7 + 12·1/14 + 47 Nullen, 5040 Terme über 4500 Matchings, 3/7,
Spektrum (0,1),(2,45),(3,40),(4,135),(6,35), Gap 2J, p₁ⱼ = 5/8, Δ·n = 3,700 vs.
3,701, det K < 0, Interferenz 1/15 vs. 1, α⁻¹ = 137,0359992168, 1,9σ) stimmen mit
den Quellen überein; das K4-Spektrum und Δ·n = 3,7002 wurden hier unabhängig
reproduziert. Die zitierten Kill-IDs (r618, r647, r613, r604, TFPT.HECKE.INDEX.01,
PRIME.HECKEMODRAM.01, E8.COXETER.EULER.COMPLETION.01) existieren im RH-Katalog
(`rh/catalog`, 14–25 Fundstellen je ID); ihr Inhalt wurde hier nicht neu bewertet.

Vier Stellen sind zu korrigieren oder zu schärfen:

1. **Konjugierter Sektor.** Die Zerlegung lautet
   248 = (45,1) + (1,15) + (10,6) + (16,4) + (**16̄**,4̄); im Anschlusspapier und in
   der Synthese steht (16,4̄). Maschinell: (16̄,4̄) = −(16,4) als Wurzelmenge.
2. **Zwei Klammerkanäle, nicht einer.** Das Anschlusspapier formuliert den
   Superaustausch als „(16,4) ⊗ (16,4̄) → (1,15) + (10,6)". Exakt sind zwei getrennte
   Kanäle: Träger–Träger [(16,4),(16,4)] → **nur (10,6)**, 960 geordnete Paare;
   Träger–Antiträger [(16,4),(16̄,4̄)] → (45,1) [640] + (1,15) [192] + Cartan [64],
   **nie (10,6)**. Der Austausch (Abschnitt 3) läuft über den ersten Kanal.
3. **„Kondo-Schritt zum c = 8-Fixpunkt".** (D5)₁ ⊗ (A3)₁ ⊂ (E8)₁ ist eine
   *konforme Einbettung* (c = 5 + 3 = 8 ohne Fluss): (E8)₁ ist die Erweiterung von
   (D5)₁ ⊗ (A3)₁ durch den Simple-Current (s,4) der Ordnung 4, gleichbedeutend mit
   der Eichung des diagonalen Zentrums Z4. Es gibt keinen RG-Fixpunkt zu suchen,
   sondern eine Z4-Eichung im Gitter zu konstruieren (Abschnitt 6). Die Synthese
   nennt an dieser Stelle einen Kondo-Fluss; das ist die falsche Klasse von Aufgabe.
4. **Die 240-Bijektion.** Als äquivariante Identifikation ist sie ausgeschlossen
   (Abschnitt 5); übrig bleibt eine Zählkoinzidenz 15 × 16 = 60 × 4.

## 3. Fugen 1 und 2 (λ, Graph): Der E8-Superaustausch wählt den Clebsch-Graphen (exakt / bedingt)

**Lesart (bedingt, eine Annahme):** Die 64 Wurzeln der (16,4) werden als
Einträgerzustände gelesen — *Ort* = D5-Spinorgewicht s (16 Orte), *Trägerzustand* =
A3-Gewicht a (4 Zustände). Das ist die D5 × A3-Aufspaltung des Seams selbst:
D5/Kragen als „wo", A3/Familie als „was". Alles Weitere ist exakt.

1. **Hard-core.** (s,a) + (s,b) hat Norm 5 und ist nie eine Wurzel: zwei Träger
   teilen keinen Ort.
2. **Graph.** (s,a) + (s',b) ist genau dann eine Wurzel, wenn s + s' ein Vektorgewicht
   ±eᵢ der 10 ist (s, s' stimmen in genau einer der fünf Koordinaten überein) und
   a ≠ b. Die so definierte Nachbarschaft auf den 16 Spinorgewichten ist der
   **Clebsch-Graph** (gefalteter 5-Würfel): 5-regulär, 40 Kanten, stark regulär
   (16,5,0,2), Adjazenzspektrum {5¹, 1¹⁰, (−3)⁵}, dreiecksfrei, nicht bipartit.
   Die fünf D5-Koordinaten liefern eine **1-Faktorisierung** in fünf perfekte
   Matchings; die zehn Bindungslabels ±eᵢ tragen je vier Kanten.
3. **Trägerkern pro Kante.** Von 16 geordneten Paaren (a,b) koppeln genau die 12 mit
   a ≠ b; (a,b) und (b,a) treffen dieselbe (10,6)-Wurzel; die sechs Ziele sind
   Λ²(4) = 6. Das ist auf allen 40 Kanten identisch (Uniformität).
4. **Vorzeichen.** Die E8-Klammer (16,4) × (16,4) → (10,6) ist ein D5 × A3-äquivarianter
   Kandidat in Λ²(16,4) = Sym²(16)⊗Λ²(4) ⊕ Λ²(16)⊗Sym²(4). Mit expliziten
   so(10)-Gammamatrizen: die invariante Paarung 16 × 16 → 10 ist **symmetrisch**
   (10 ⊂ Sym²(16) = 10 + 126; Λ²(16) = 120 enthält keine 10). Also ist der Kern
   symmetrisch in den Orten und **antisymmetrisch in den Trägern**. Mit diesem
   Vorzeichen gilt exakt K⁺K = I − S = 2P_Λ².
5. **Effektive Kopplung.** Zweite Ordnung über einen Bindungszwischenzustand der
   Energie Δ mit Hüpfamplitude t (|N_αβ| = 1 für alle 240·56 Wurzelpaare, weil E8
   einfach geschnürt ist — maschinell: ⟨α,β⟩ = −1 und β−α ∉ Φ):
   H_eff = −(t²/Δ) K⁺K = J·(I+S)/2 + const mit **J = 2t²/Δ > 0 auf jeder
   Clebsch-Kante, 0 sonst.**

**Konsequenzen für die Fugen.**

- *λ:* Ein einziger vermittelnder Sektor mit einheitlichen Strukturkonstanten
  erzwingt **gleiche Stärke auf allen existierenden Bindungen**. Eine
  Tetramerisierung λ < J bräuchte zusätzliche Daten; die uniforme Kopplung ist der
  datenfreie Default. Auf der Kettenlesart des Anschlusspapiers heißt das: die
  Kritikalität λ = J, dort als „nicht hergeleitet" markiert, ist der Default,
  nicht die Ausnahme — und damit (A3)₁.
- *Graph:* Ohne Lokalität (vollständiger Graph) ist die Zelle für N = 4m eindeutig
  mit E₀ = 5m(m−1)J und Gap **exakt 2J** für alle m (Inhaltsformel, exakt) — die Zelle
  wächst einfach mit; erst ein Graph macht Zellen zu Zellen. Der Compiler liefert
  unter der Lesart genau einen Graphen, und **K4 passt nicht hinein**: der
  Clebsch-Graph ist dreiecksfrei. Die Vierträgerzelle mit vollständigem Graphen
  ist also *nicht* die E8-native Kopplungsstruktur; sie bleibt als Hüllenbedingung
  (Zustandsaussage) richtig, als Hamiltonoperator ist sie gesetzt.

**Der Clebsch-Cluster, exakt diagonalisiert (Schur–Weyl, alle 64 Irreps λ ⊢ 16,
Σ dim S^λ · dim V^λ = 4¹⁶ geprüft):**

| Größe | Wert (J = 1) |
|---|---|
| Grundenergie E₀ | 11,045398 |
| Grundzustand | SU(4)-Singulett, S₁₆-Irrep (4,4,4,4), **eindeutig** |
| E₀ pro Kante / pro Ort | 0,2761 / 0,6903 |
| Sym²-Gewicht je Kante (alle 40 gleich, Streuung < 10⁻¹⁴) | 0,27613 |
| Sym²-Gewicht je Nichtkante (alle 80 gleich) | 0,61193 (unkorreliert: 0,625) |
| Summenregel Σ_{i<j} ⟨(I+S)/2⟩ = 60 | 60,000000 |
| erste Anregung | Singulett-Dublett bei 11,561762, **Gap 0,516 J** |
| erste magnetische Anregung | 15 (Irrep (5,4,4,3)) bei 12,133537, Gap 1,088 J |
| nächste | 20′ (5,5,3,3) bei 12,3228; 45 (5,5,4,2) bei 12,8751; 45 (6,4,3,3) bei 12,9816 |
| Referenzen | Ω-Produkt auf vier disjunkten 4-Zykeln (existiert; jede Ω-Produktform hat E ≥ 15 J, exakt): 15 J; uniformer Ring: 0,0874 J/Kante |

Lesart: Der E8-native 16-Träger-Cluster hat einen eindeutigen, voll
symmetrischen Singulett-Grundzustand (die Kantentransitivität des Graphen ist im
Zustand realisiert), aber eine niedrige nichtmagnetische Anregung unterhalb der
15 — das Signum eines frustrierten Austauschs (nicht bipartit). Die bindenden
Paare sind zu 72 % antisymmetrisch, nicht zu 100 % wie in Ω: der Cluster ist
keine Hülle im Sinn des Hüllensatzes, sondern ein resonierender Zustand.

**Was offen bleibt:** die Lesart selbst (Ort = Spinorgewicht), die
Fock-Struktur über den 64 Moden (der Superaustausch ist eine Vielteilchen-Lesart
der Lie-Klammer), und die beiden Skalen t und Δ.

## 4. Fugen 3 und 4 (Cross-Register-Kopplung, Präparation): Zelle und Aufzeichnung liegen in orthogonalen Sektoren (exakt)

Die Quellkopplung ist Q_C = I − 2 Σⱼ |j⟩⟨j| ⊗ |bⱼ⟩⟨bⱼ| (Register in Pointerbasis,
System in der Basis {bⱼ} des Kontexts C), die Vor-Messung
U_C = (W⊗I) Q_C (A⊗I) mit A|0⟩ = |+⟩; exakt gilt U_C(|0⟩⊗ψ) = Σⱼ |j⟩ ⊗ Πⱼψ und
U_C² = I für alle 15 gepinnten Kontexte (reproduziert).

**Satz (Sektortrennung).** Sei S der Austausch zweier Träger, Λ² = (I−S)/2,
Sym² = (I+S)/2 und Q̃_C = (V_C⊗V_C) Q (V_C⊗V_C)⁺ die *gleichkontextige* Aufzeichnung
(Register und System im selben Kontext gelesen). Dann gilt für alle 15 Kontexte:

1. Q̃_C wirkt auf Λ² als **Identität**; Q̃_C hat Spektrum (−1)⁴(+1)¹²; der reflektierte
   Vierraum liegt vollständig in Sym² (15/15).
2. Der Aufzeichnungszustand nach einem Schritt, Σⱼ |bⱼ⟩⊗Πⱼψ, liegt für jede Eingabe ψ
   vollständig in Sym² (15/15); seine Paarmarginale ist rein symmetrisch, die
   Zellmarginale (I−S)/12 rein antisymmetrisch — orthogonale Sektoren 10 bzw. 6.
3. **Zellen zeichnen sich nicht selbst auf:** Q̃_C auf jedem Trägerpaar (i,j) der
   Zelle lässt Ω fest (90/90 = 15 Kontexte × 6 Paare).
4. Q ist keine Linearkombination von I und S: die Kopplung ist nicht A3-kovariant,
   sondern kontextgebunden.

**Registerbasis als Zusatzdatum (exakt).** Die *Quellkopplung* Q_C (Register in der
festen Pointerbasis) ist auf Λ² nur im Rechenkontext trivial (1/15) und lässt Ω
nur dort fest (6/90). Die Lesebasis des Registers ist also ein eigenes Datum, das
im Manuskript stillschweigend mit dem Rechenkontext identifiziert ist.

**Konsequenz für G2 (Herkunft der Kopplung).** Aufzeichnung *braucht* den Sektor
Sym²(4) = 10 zwischen Register und System. Die 248 enthält keine (·,10): jedes von
der E8-Klammer erzeugte Zweiträgerpaar liegt in Λ²(4) (Abschnitt 3). Also kann die
Cross-Register-Kopplung **nicht** aus der Adjungierten kommen; G2 ist innerhalb
der 248 unschließbar — nicht, weil eine Matrix fehlt, sondern weil der Sektor
fehlt. Der kleinste E8-Modul mit Sym²(4)-Anteil ist nach der Standardverzweigung
die 3875 (135 ⊕ 1820 ⊕ 1920 unter SO(16); in 1820 = Λ⁴(16) ⊃ 10 ⊗ Λ³(6) =
(10, 10 ⊕ 10̄)); das ist darstellungstheoretische Buchführung, hier nicht maschinell
geprüft, und benennt, wo ein E8-nativer Aufzeichnungssektor überhaupt sitzen könnte.

**Präparation.** Ω ist die eindeutige Hülle (Hüllensatz) und zugleich unter
gleichkontextiger Aufzeichnung inert. Ein „frisches Register" ist per Konstruktion
ein Träger, der mit dem System *nicht* in der Hülle liegt; nach einem Schritt ist
das Paar rein symmetrisch. Die Registerversorgung des Manuskripts ist damit exakt
das Nachliefern von Trägern außerhalb der Hülle: Materie = Λ², Gedächtnis = Sym².
Was gesetzt bleibt, ist, *dass* das System in der Hülle startet (Temperatur ≪ Gap),
und die Registerlesebasis.

## 5. Die 240-Bijektion ist äquivariant ausgeschlossen (exakt)

Die CQ-Koordinaten (Kontext C, Pauli P) zerfallen unter Sp(4,2) ≅ S₆ (720 Elemente,
enumeriert) in Bahnen **15 + 45 + 180** (P = I; P ∈ C; P ∉ C). Die 240 Gauß-Wurzeln
sind 60 Strahlen × {1, i, −1, −i} (maschinell aus den gepinnten Z240); die
Clifford-Gruppe ist auf den 60 Quellstrahlen transitiv (Bahn des Rechenstrahls =
genau die 60 Quellstrahlen = die 60 Zwei-Qubit-Stabilizerzustände), W(E8) auf den 240
Wurzeln. Jede mit der Strahlstruktur verträgliche Gruppenwirkung auf Wurzeln hat
Bahnlängen in 60·ℤ; 15 und 45 sind das nicht. **Keine äquivariante Bijektion.**
Punkt 5 der Rangfolge in Teil III ist damit nicht „offen", sondern in seiner
natürlichen Form getötet; ein nicht-äquivarianter Kandidat müsste explizit
konstruiert und als Zusatzstruktur ausgewiesen werden.

## 6. Z4-Glue: konforme Einbettung statt Kondo-Fluss, und ihr Gitterinhalt (exakt / numerisch)

**Gitterebene (exakt).** E8 ⊃ D5 ⊕ D3 zerfällt in genau vier Glue-Klassen
(0,0), (v,v), (s,s), (c,c); die Glue-Gruppe ist zyklisch (2·(s,s) = (v,v)).
Normzählung: Θ_E8 = 1 + 240q + 2160q² + 6720q³; Stufe 1 des (E8)₁-Vakuummoduls:
60 + 60 + 64 + 64 = 248 (mit den 8 Cartan-Richtungen in (0,0)); χ = Θ/η⁸ =
q^{−1/3}(1 + 248q + 4124q² + …). Konforme Gewichte aus Minimalnormen:
D5 {0, 1/2, 5/8, 5/8}, A3 {0, 1/2, 3/8, 3/8}; die Paarung ergibt h = 0, 1, 1, 1
für die vier Klassen — ganzzahlig, also zulässige Simple-Current-Erweiterung.

**Was das für „c = 8" heißt.** (E8)₁ = [(D5)₁ × (A3)₁]/Z4^diag. Ein Gitterprogramm
braucht daher (i) die SU(4)-Trägerkette in *allen vier* N-alitätssektoren,
(ii) zehn Majorana-Moden in NS-gerade/NS-ungerade/R-Sektoren, (iii) die
Korrelation beider durch ein Z4-Gauß-Gesetz: **Trägerzahl mod 4 ↔
Fermionsektor.** (ii) ist frei-fermionisch exakt (h = 0, 1/2, 5/8, 5/8). (i) ist
hier geprüft:

| n Träger (Ring) | k = n mod 4 | Sektordimension | E₀ | x extrahiert | (A3)₁-Vorhersage |
|---|---|---|---|---|---|
| 8 | 0 | 2 520 | 0,539495 | −0,009 | 0 |
| 12 | 0 | 369 600 | 0,944508 | −0,005 | 0 |
| 6 | 2 | 180 | 0,697224 | 0,460 | 1/2 |
| 10 | 2 | 25 200 | 0,998465 | 0,501 | 1/2 |
| 5 / 7 | 1 / 3 | 60 / 630 | 0,690983 / 0,634808 | 0,507 / 0,282 (Mittel 0,395) | 3/8 |
| 9 / 11 | 1 / 3 | 7 560 / 92 400 | 0,898579 / 0,993060 | 0,454 / 0,320 (Mittel 0,387) | 3/8 |
| 13 | 1 | 1 201 200 | 1,205482 | 0,431 | 3/8 |

(x aus E₀ = n·e∞ − πv(c − 12x)/(6n) mit Sutherlands e∞ = 0,087439, v = π/4, c = 3;
die k = 1/3-Sektoren spalten bei ungeradem n auf und konvergieren im Mittel gegen
3/8.) Die vier A3-Glue-Klassen {0, 4, 6, 4̄} mit h = {0, 3/8, 1/2, 3/8} sind also
genau die vier Restklassen der Trägerzahl. Der noch fehlende Schritt ist (iii): die
Konstruktion, die Fermionsektor und Trägerzahl koppelt und die gemischten
Zustände (3/8, 5/8) projiziert. Erfolg wäre: 248 Zustände auf Stufe 1 im
Endlichgrößenspektrum des gekoppelten Rings.

## 7. Fuge 5 (Zeitskala): lokalisiert, nicht geschlossen

Die dimensionslose Struktur liefert J = 2t²/Δ als Verhältnis; t (Übergang
Träger ↔ Spinorslot) und Δ (Energie eines Bindungszwischenzustands) sind
dimensionsbehaftet und nicht in der 248. Die einzige dimensionale Eingabe der
Zahlenprogramme bleibt M̄_Pl. Die Zeitskala ist damit auf **ein** Verhältnis
t²/Δ und **eine** externe Skala reduziert; die Warnung des Manuskripts, keine
unverbundene Zahl (etwa M_s = c₃^{7/2} M̄_Pl) an diese Stelle zu setzen, gilt
weiter.

## 8. Stand der fünf Fugen nach dieser Runde

| Fuge | vorher | nachher | Evidenz |
|---|---|---|---|
| λ | gesetzt | **uniform J = 2t²/Δ > 0 auf jeder Bindung** (Vorzeichen exakt, Uniformität exakt); λ ≠ J bräuchte Zusatzdaten | exakt unter Lesart |
| Graph | gesetzt | **Clebsch (16,5,0,2)** aus der Klammer; K4-Zelle nicht einbettbar; Cluster hat eindeutiges Singulett, Gap 0,516 J | exakt (Graph) / numerisch (Spektrum) |
| Cross-Register-Kopplung | gesetzt | **nicht aus der 248 ableitbar** (Aufzeichnung ⊂ Sym²(4), fehlt in 248); Registerlesebasis als Zusatzdatum identifiziert | exakt (negativ) |
| Präparation | gesetzt | Ω inert unter gleichkontextiger Aufzeichnung; frisches Register = Träger außerhalb der Hülle; gesetzt bleibt der Start in der Hülle | exakt / gesetzt |
| Zeitskala | gesetzt | auf t²/Δ und M̄_Pl lokalisiert | offen |
| (Teil III, 1) c = 8 | „Kondo-Fixpunkt" | konforme Einbettung durch Z4-Eichung; A3-Hälfte im Gitter belegt | exakt / numerisch |
| (Teil III, 5) 240-Bijektion | offen | äquivariant tot (15+45+180 ≠ 60·k) | exakt |

## 9. Was jetzt entscheidbar ist (Rangfolge)

1. **Lesart-Test für den Clebsch-Graphen.** Die Lesart „Ort = Spinorgewicht" macht
   eine Vorhersage, die die Kettenlesart nicht macht: 16 Träger, 40 Bindungen,
   fünf perfekte Matchings = fünf Koordinaten des Fünferträgers (P2), eindeutiger
   Singulett-Grundzustand mit Singulett-Dublett bei 0,516 J. Kill: jede
   quellenseitige Stelle, die K4-Zellen oder eine Kette *erzwingt*.
2. **Z4-Gauß-Gesetz im Gitter** (Abschnitt 6 (iii)): SU(4)-Ring ⊗ zehn Majoranas mit
   sektorgekoppelten Randbedingungen; Erfolg = 248 auf Stufe 1.
3. **Aufzeichnungssektor in der 3875** maschinell verzweigen; Erfolg = ein E8-nativer
   (·,10)-Kanal, der Q_C trägt; Kill = jede solche Kopplung verletzt U² = I oder
   die Kontextstruktur.
4. **Fock-Struktur der 64 Moden** aus der Quelle statt aus der Lesart:
   welche Statistik tragen die Träger über den (16,4)-Slots? Erfolg = das
   Vorzeichen von Abschnitt 3.4 aus der Quelle statt aus so(10)-Rep-Theorie.

## 10. Grenzen

Keine Aussage dieser Runde schließt T1–T8. Der Clebsch-Graph ist exakt *unter der
Lesart* Ort = Spinorgewicht; die Lesart ist nicht abgeleitet. Der Superaustausch
ist Störungstheorie zweiter Ordnung in einer Vielteilchen-Lesart der Lie-Klammer;
t, Δ und die Fock-Struktur sind nicht aus der 248. Die Sektortrennung ist ein
exakter Satz über die gepinnte Kopplung Q, kein Verbot anderer Kopplungen. Die
Ring-Sektoren sind Endlichgrößen-Numerik bis n = 13 mit Logarithmus-Korrekturen;
die Clebsch-Spektren sind exakt bis auf Gleitkomma (ARPACK, tol 10⁻⁹). Nichts
hier ist ein RH-, Faktorisierungs- oder P-vs-NP-Resultat.

## 11. Reproduktion

```sh
cd experiments/theory-contracts/universalraum-fugen-20260914
python3 -B checker.py validation.json        # 27 288 Bedingungen, ~6 s
python3 -B -m unittest test_checker          # 14 Tests, auch -OO
python3 -B clebsch_su4.py                    # Ring-Sektoren + 64 Irreps, Log im Terminal
```

Quellpin `context_instrument.py` SHA-256 `ba1da931…9e3995`; Ergebnisse in
`validation.json`, `clebsch_su4.json`.
