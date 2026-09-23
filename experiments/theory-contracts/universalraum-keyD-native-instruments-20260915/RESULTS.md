# TFPT / Universalraum: Schlüssel D — native Instrumente des N=2-Kausalzeugen

**Theorievertrag, 15. September 2026.** Abgetrennter Forschungsordner. Keine
neuen Hamiltonterme, keine Änderung fremder Quellen, keine Promotion nach
`verification/`, kein Ledger-/Paper-/Website-Eintrag, kein T1–T8-Torabschluss.

Frage: Welche Schritte des bestätigten N=2-Kausalzeugen (v1.6.8,
Ordner `universalraum-common-process-20260915`) sind **nativ** — durch das
dokumentierte Alphabet (passive Focklifts, X = T₊ + T₋, N_b; Erhaltungssatz:
jedes Wort liegt in {N}′) und seine dokumentierten Stufen (S3-Besetzungen;
die minimale G-invariante Erweiterung Q = B₊ + B₋) abgedeckt? Gilt der
No-Go-Satz C_rs(t) = δ_rs·c(t) auch für die native 3-Punkt-Intervention
(Entnahme bei r, dann Messung von n_s)? Was ist das minimale Primitive, das
die verbleibende Lücke schließt?

## 1. Ergebnis in einem Absatz

Der Phasenimpuls Z_r = (−1)^{n_r} ist exakt der passive Focklift Γ(u_r) des
Vorzeichen-Relabelings f_r ↦ −f_r und liegt in {N}′ — als **Klasse** also
nativ; aber er wird weder von der geprüften diskreten Gruppe (mit oder ohne
Clock) noch von der S0–S2-Wortalgebra erreicht; exakt erzeugt wird er erst
auf Stufe S3 als Z_r = 1 − 2 n_r (**bedingt**). Der wörtliche
3-Punkt-Entnahmezeuge ist **exakt null**: Z_r f_r = f_r (CAR-Absorption
n_r f_r = 0), also verschwindet die markierte Intervention für jeden
Zustand, alle r, s, t und jedes H — der No-Go erstreckt sich, aber aus
CAR-Gründen, nicht aus Symmetrie. Der physikalische Mittelpunktszeuge auf
dem sternsymmetrischen (hellen) Zustand hat dagegen das Offdiagonalsignal
**−3x/128 ≠ 0 für jedes g ≠ 0**: auf Blockebene existiert ein nativer
Symmetrie-Zustandszeuge; die Symmetrie-No-Go erstreckt sich **nicht** auf
das native 3-Punkt-Mittelpunktsprotokoll. Die Produktzustand-Präparation
f₄†f₅₇†|0⟩ ist **nicht-nativ**: sie ändert N, und mit Q sind nur
N → N + 4ℤ erreichbar — N=2 ist weder vom Vakuum (2 ∉ 4ℤ) noch vom
N=64-Grundsektor (62 ≢ 0 mod 4) erreichbar. Das minimale schließende
Primitiv ist **ein geladenes Modeninstrument** {f_r, f_r†} an einer Mode
(Modentransport durch die transitive deklarierte Gruppe); es schließt
Präparation, Auslese (n_r = f_r†f_r) und Phase (Z_r = 1 − 2f_r†f_r)
gleichermaßen.

## 2. Ausgangspunkt und Konventionen

Sternkanal A = 0 aus der byte-gepinnten In-Repo-Quelle `native_source.py`
(SHA-256 `380577f8…`; Kopie aus
`universalraum-operations-groundstate-20260915`, kein npz-Zugriff). Blätter
(4,57), (5,56), (8,53), (9,52), (16,45), (17,44), (28,33), (29,32) mit
Vorzeichen (−1, 1, 1, −1, −1, 1, 1, −1); 16 disjunkte Moden; Sender 4 in
Blatt 0, Empfänger 5 in Blatt 1 — exakt die v1.6.8-Schnittstelle. Der
Clock-Konstruktor ist gepinnt (`9bf99de7…`). x = 4 cos²(πd/2),
d = Δ/(2Ω), Ω² = Δ²/4 + 8g², T = π/Ω.

## 3. Aufgabe 1: Alphabet-Mitgliedschaft von Z_r (alles exakt)

| Frage | Antwort | Exakter Grund |
|---|---|---|
| Passive Focklift-Klasse? | **ja** | Z_r = Γ(u_r) = Λ²(u_r) ⊕ I₆₀ auf N=2, u_r = I − 2e_rr (Operatoridentität, ganzzahlig) |
| Im Erhaltungssatz erlaubt? | **ja** | [Z_r, N] = [Z_r, N_f] = [Z_r, N_b] = 0; Z_r² = I; n_r² = n_r |
| In ⟨GROUP⟩ bzw. ⟨GROUP, Clock⟩? | **nein** | Schicht 1: jedes Element ist kron(S, C) mit C *vorzeichenloser* Farbpermutation; der Spinor-1-Farbblock von u_4 ist (−1,+1,+1,+1) — gemischte Vorzeichen, alle ungleich null — keine kron-Form möglich. Schicht 2: selbst der gröbere Spinor-Flip u_{spinor 1} = kron(S₁, I₄) (= Z₄Z₅Z₆Z₇ auf dem Fockraum) ist unerreichbar: der Schreier-Kern der Spinorgruppe ist genau {±I} (F2-Rang 1; |G_spin| = 32, mit Clock 192); das einzige erreichbare Diagonalphase ist die globale Fermionparität |
| In der S0–S2-Wortalgebra auf N=2? | **nein** | Doppelkommutant-Zeuge: P_bright = WᵀW/8 liegt im S1=S2-Kommutanten, aber [n₄, WᵀW] hat exakt 210 ganzzahlige Nichtnulleinträge |
| Auf Stufe S3 erzeugt? | **ja** | Z_r = 1 − 2 n_r, lineares Polynom im adjungierten Besetzungsinstrument |
| Symmetrie von H? | nein (nutzlos sonst) | [Z₄, X] ≠ 0 (exakt, ganzzahlig) |

**Befund (bedingt-nativ):** Z_r gehört zur dokumentierten Klasse passiver
Focklifts (die deklarierten Erzeuger sind selbst signierte Permutationen,
also Phasen-Relabelings), aber die konkret geprüfte diskrete Untergruppe
erreicht selbst die Spinor-Stufen-Phase nicht; erst S3-Besetzungen (oder
explizit adjungierte Einmoden-Phasenlifts) erzeugen Z_r exakt.

## 4. Aufgabe 2: der native 3-Punkt-Test

### 4.1 v1.6.8 mit ausschließlich nativen Schritten (exakt)

Auf dem 9-dimensionalen Stern: U_T = I + (z−1)·active, Z₄ = I − 2e₀,
n₅ = e₁. Produktzustand |p₀⟩: δ₄→₅ = x(25x−64)/1024 (negativ für
0 < g² ≤ 3Δ²/32 ⟺ 0 < x ≤ 2), Diagonalblatt +7x(64−25x)/1024,
Blatt-Summenregel exakt null; beide Arme enden mit N_f = 2, N_b = 0. Die
dokumentierte 3×3-Reduktion h₃ = [[0,0,−g],[0,0,√7 g],[−g,√7 g,Δ]],
z₃ = diag(−1,1,1), e₃ = diag(0,1/7,0) ist exakt gegen die 9×9-Rechnung
gegengeprüft (Invarianz des Unterraums unter H und Z₄; e₃-Kompression).
Boson-Seed-Zweitzeuge: unberührt exakt 0, gepulst
(1−d²)(1+d²−2d sin(πd/2))/128 > 0 für 0 < d < 1.

### 4.2 Wörtlicher 3-Punkt-Entnahmezeuge: exakt null (CAR, nicht Symmetrie)

Als exakte ganzzahlige Sparse-Sektormaps für N = 1→0, 2→1, 3→2 und alle 64
Moden geprüft (576 Identitäten):

\[
Z_r f_r = f_r,\qquad f_r^\dagger Z_r = f_r^\dagger,\qquad n_r f_r = 0 .
\]

Folge: für **jeden** Zustand Ω, jedes H, alle r, s, t gilt

\[
\langle\Omega|f_r^\dagger Z_r e^{iHt} n_s e^{-iHt} Z_r f_r|\Omega\rangle
=\langle\Omega|f_r^\dagger e^{iHt} n_s e^{-iHt} f_r|\Omega\rangle ,
\qquad \Delta n_s(t)\equiv 0 .
\]

Auf dem Stern zusätzlich zustandsbezogen für alle 16×16 Modenpaare gezeigt;
jede Einmoden-Markierung zur Entnahmezeit ist dort sogar nur eine globale
Phase (Ein-Fermion-Zustand). **Der No-Go erstreckt sich auf die wörtliche
3-Punkt-Intervention — exakt, aber der Mechanismus ist CAR-Absorption am
Entnahmeereignis, nicht Grundzustandsymmetrie.** Eine Phase kann ein
Entnahmeereignis an derselben Mode nicht markieren; der v1.6.8-Zeuge pulst
darum zur Mitte, nachdem die native Evolution die Sendermode wieder
teilweise gefüllt hat.

### 4.3 Zwei-Punkt-Analogon und der Mittelpunktszeuge auf dem symmetrischen Zustand

Zwei-Punkt-Entnahmeantwort auf dem hellen Sternzustand |B⟩ = (1/√8)Σσ_q|q⟩
(exakt; H = 0 auf N=1, da Paarannihilation zwei Fermionen braucht und N=1
keine Bosonen enthält):

\[
C^B_{rs}(t) = \delta_{rs}/8
\]

— keine Mode-zu-Mode-Struktur, konsistent mit der No-Go-Form. Aber das
native Mittelpunkts-3-Punkt-Protokoll (U_T, Z_r, U_T, Auslese n_s) auf
demselben symmetrischen Zustand ergibt für alle 56 geordneten
Offdiagonal-Blattpaare und jede Kopplung g ≠ 0 (exakt):

\[
\delta^B_{r\to s} = -\frac{3x}{128} < 0 \quad (r \neq s),
\qquad
\delta^B_{r\to s} = +\frac{21x}{128} \quad (\text{gleiches Blatt}),
\qquad
\sum_s \delta^B_{r\to s} = 0 .
\]

**Die Stern-symmetrische Zustandswahl tötet das Offdiagonalsignal nicht:
die Symmetrie-No-Go erstreckt sich nicht auf das native
3-Punkt-Mittelpunktsprotokoll auf Blockebene — ein nativer
Symmetrie-Zustandszeuge existiert.** Ohne Kopplungsintervallbeschränkung
(anders als der Produktzustand-Zeuge). Offen bleibt die echte
N=64-Singulett-Frage (außerhalb des exakten Budgets; keine
N=64-Grundzustandsvektorkonstruktion).

### 4.4 Numerische Gegenprobe auf dem vollen N=2-Block (numerisch)

2076 Dimensionen, expm_multiply, Prüfpunkt Δ = 1, g = 1/20
(x = 0,014047992429585): Produkt δ₄→₅ = −0,0008731815070419; hell
off-diagonal −0,0003292498225684 = −3x/128; hell diagonal
+0,0023047487579788 = 21x/128; Boson-Seed 2,7820733415024·10⁻⁶;
Sterneinschluss und Null-Bosonen-Endzustände bestätigt; symbolische
Sternzustände stimmen mit den eingebetteten 2076-Zuständen überein.

## 5. Aufgabe 3: Lückentabelle

| Zeugenschritt | Status | Exakter Grund |
|---|---|---|
| Native Vor/Nach-Evolution U_T | **nativ** | H = ΔN_b + gX; X, N_b sind die dokumentierten Kontrollen |
| Phasenimpuls Z₄ | **bedingt** | Γ(u₄)-Klasse ja, {N}′ ja; ∉ ⟨GROUP, Clock⟩ (kron-Obstruktion + Schreier-Kern {±I}); ∉ S0–S2-Wortalgebra ([n₄, WᵀW] ≠ 0); = 1 − 2n₄ exakt auf S3; auch Wort in einem geladenen Instrument |
| Besetzungsauslese n₅ | **bedingt** | S3-Instrument; außerhalb S0–S2 (derselbe Kommutantzeuge); auch n₅ = f₅†f₅ mit geladenem Instrument |
| Produktzustand-Präparation f₄†f₅₇†|0⟩ | **nicht-nativ** | N-ändernd; Alphabet ∪ S3 ⊆ {N}′; mit Q nur N → N + 4ℤ (Ladungsgraduierung exakt: alle Erzeugerterme haben Ladung 0, ±4, Ladung addiert sich unter Multiplikation); N=2 vom Vakuum (2 ∉ 4ℤ) und von N=64 (62 ≢ 0 mod 4) unerreichbar |
| Aufzeichnung | **nativ** | klassische Nebeninformation |

Bedingt-Anmerkung: innerhalb des N=2-Sektors ist der S3-Trägergraph
zusammenhängend (2076 Zustände, eine Komponente, exakt geprüft) — mit einem
nativen N=2-Startzustand würden S3-Instrumente plus Feedforward die
Paarpräparation leisten; dokumentiert ist aber kein nativer N=2-Start
(Vakuum N=0, Grundsektor N=64).

## 6. Aufgabe 4: Urteil — minimaler nativer Instrumentenvertrag

**Minimales schließendes Primitiv: ein geladenes Modeninstrument
{f_r, f_r†} an einer einzelnen Mode.** Begründung (alles exakt):
f_r† trägt N-Ladung +1; f₄†f₅₇†|0⟩ = +|Paar(4,57)⟩ ist exakt der
Zeugenstart (zwei Anwendungen ab Vakuum); n_r = f_r†f_r auf N=2 für alle 64
Moden geprüft, damit Z_r = 1 − 2f_r†f_r; die deklarierte Gruppe ist
transitiv auf den 64 Moden und ihr N=1-Lift ist die Einteilchenmatrix
selbst, also Γ(g) f₄† Γ(g)† = ±f_{g(4)}† — ein Instrument an einer Mode
erreicht alle.

**Q = B₊ + B₋ schließt die Lücke nicht**: Q ist die minimale G-invariante
{N}′-brechende Erweiterung (R₊ + R₋ = −[N_b, [Q, X]] exakt nachgeprüft,
ebenso [N_b, B₊] = 2B₊, [B₋, B₊] = N_b + 30, [T₋, B₊] = R₊), aber alle
Wortladungen bleiben in 4ℤ. Q trägt stattdessen nativ den N=4-Singulettblock
(β = B₊|0⟩/√30, ρ = R₊|0⟩/√480; T₋B₊|0⟩ = R₊|0⟩, T₊R₊|0⟩ = 16B₊|0⟩,
T₋R₊|0⟩ = 0 exakt; H = [[2Δ, 4g], [4g, Δ]], Umwandlungsmaximum 4/29 bei
g/Δ = 1/20) — ein N ≡ 0 (mod 4)-Analogon, nicht der bestätigte N=2-Zeuge.

**Modenphasen** sind bereits bedingt-nativ (S3) und N-erhaltend; sie können
die Präparation nicht leisten.

**Minimaler nativer Instrumentenvertrag für einen Kausalzeugen:**
dokumentiertes Alphabet {passive Focklifts, X, N_b} + S3-Besetzungen {n_r}
+ ein geladenes Modeninstrument. Damit ist jeder Schritt des bestätigten
N=2-Zeugen nativ. Das fehlende Primitiv ist genau das geladene Instrument —
spektral ist der Entnahmekanal längst gesichert (isolierter
64-fach-entarteter Pol, Z_low > 0,88, ε_h ≈ 0,0311Δ), aber seine
instrumentelle Verfügbarkeit ist die offene T1-Frage. Für einen echten
Grundzustandszeugen bei N=64 gilt zusätzlich: der wörtliche
Entnahme-markierte 3-Punkt ist CAR-null (§4.2); ein Grundzustandszeuge muss
die Mittelpunktsstruktur verwenden, die auf Blockebene durch Symmetrie
**nicht** ausgeschlossen ist (−3x/128, §4.3) — offen bei N=64.

## 7. Verifikation

`replay.py` führt die drei Prüfer normal und unter `-OO` aus und verlangt
byteidentische JSON-Ausgaben (bis auf Laufzeitfelder): Status PASS,
**2487 Prüfwachen** (alphabet 564 exakt; threepoint 1801 exakt + 9 numerisch;
gap 113 exakt). Hashes in `replay_manifest.json`. Guardzahlen zählen
Prüfbedingungen, keine unabhängigen Theoreme. Exakt heißt
ganzzahlig/rational/symbolisch; numerisch heißt float64 mit
Toleranz-Guard (nur §4.4).

## 8. Grenzen und nicht übernommene Behauptungen

- **Offen:** die echte N=64-Singulett-3-Punkt-Frage (kein
  Grundzustandsvektor gebaut; Budgetgrenze respektiert).
- **Offen:** ob der Compiler das geladene Instrument bereitstellt (T1).
- **Bedingt:** Z_r und n_r sind nativ genau dann, wenn S3-Besetzungen (oder
  Einmoden-Phasenlifts) gewährt sind.
- Keine Aussage über räumliche Träger, keine RH-/Faktorisierungs- oder
  P-vs-NP-Aussage, keine abgeleitete Hylæan-Fähigkeit, kein T1–T8-Tor
  geschlossen.
