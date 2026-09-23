# TFPT / Universalraum: v1.6.9 Modellselektion (Paket 2)

**Forschungsvertrag, 15. September 2026.** Endliche, nichtarithmetische
Fortsetzung. Kein neuer Hamiltonterm, keine Zustandsauswahl, keine
Promotion, kein T1–T8-Tor, kein RH-/Faktorisierungs-/P-vs-NP-Resultat.
Der Prüfer läuft normal und unter `-OO` mit byteidentischen Berichten;
maßgeblich ist `replay_manifest.json`.

Modellvertrag (unverändert):
\(H=\Delta N_b+g\sum_{A=1}^{60}(b_A^\dagger P_A+P_A^\dagger b_A)\),
\(P_A=\sum_{i<j}W_{A,ij}f_jf_i\), \(N=N_f+2N_b\), 64 Fermionmoden,
60 Bosonmoden, \(WW^\dagger=8I_{60}\), 480 Vertizes.

## 1. Antworten zuerst

- **Welche freie Wahl wird eliminiert?** Familie 1 (Zwei-Chart): der
  Überlappungsparameter \(c\in[0,1]\) wird aus \(I_4=1+c^4\) eindeutig
  zurückgewonnen (injektiv auf \([0,1]\)). Familie 2 (gemeinsame Bank):
  \(Q=C^\dagger C\) wird aus \(G_C^{(3)}\) rekonstruiert; \(C\) selbst wird
  **nicht** ursprünglich ausgewählt (Bedingung B6).
- **Welche Annahme bleibt?** Familie 1: A5 (c ist der einzige freie Parameter)
  plus die offene typisierte Chart-Verklebungsabbildung. Familie 2: B6
  (endliche Sektor-Tests geben keine uneingeschränkte globale Eindeutigkeit).
- **Welches Experiment unterscheidet?** Familie 1: das vierte
  Energiemoment \(I_4\) (oder die Übergangswahrscheinlichkeit \(P(L\to R;t)\)
  in Ordnung \(t^4\)). Familie 2: die Anzahl der \(N=3\)-Ein-Boson-Eigenzustände
  bei Energie \(\Delta\): **0 (verteilt) vs 64 (kollektiv)**.

**Akzeptanzergebnis:** **(a)** für Familie 1 (Eindeutigkeit modulo
operationeller Äquivalenz; Äquivalenz = Identität auf \([0,1]\)); **(b)** für
Familie 2 (explizites Gegenmodellpaar verteilt vs kollektiv mit
unterscheidendem Experiment); die Selektionsfrage (Aufgabe 3) wird durch
**(c)** beantwortet — die präzise lokalisierte offene Fortsetzungsbedingung
ist die fehlende typisierte Chart-Verklebungsabbildung.

## 2. Zulässige Modellklasse (`model_selection.py`, Section 1)

Die Spezifikation (Träger, Wechselwirkungsordnung, Ladungen,
Kompositionsregeln, Zustände, Instrumente) wird im JSON-Bericht als
`model_class` geführt. Jede zusätzliche Annahme pro Familienmitglied ist
namentlich benannt:

- **Familie 1 (Zwei-Chart):** A1 (zwei Charts teilen die 64 a-Moden; d-Moden
  unabhängige CAR-Kopie), A2 (jeder Chart nutzt denselben nativen W), A3
  (gleiche Kopplung g und Δ), A4 (separate Boson-Banken), A5 (c∈[0,1] ist
  der einzige freie Parameter), A6 (intern-invariante Vergleichsobservablen).
- **Familie 2 (gemeinsame Bank):** B1 (L identische Kopien), B2 (eine
  gemeinsame Boson-Bank), B3 (C symmetrisch normiert, C C†=I_L; C frei),
  B4 (Paar-Gram bleibt 8 I₆₀ für jedes zulässige C), B5 (matrixaufgelöster
  G_C^(3) beobachtbar), B6 (endliche Sektor-Tests geben keine uneingeschränkte
  globale Eindeutigkeit).

Strukturelle Guards: W-Form (60×2016), 480 Vertizes, 60-Boson-Bank — alle
exakt gegen die rekonstruierte Quelle geprüft (SHA-256 gepinnt).

## 3. Inverser Test (i): \(I_4 = 1+c^4\) (Familie 1, exakt)

Momentenstruktur aus der CAR-Überlappungsalgebra und dem nativen W:
\(\mu_1=0\), \(\mu_2=g^2 S\) mit \(S=\operatorname{tr}(WW^\dagger)=8\cdot60=480\)
(c-unabhängig, da jeder Chart denselben W nutzt), \(\mu_3=0\) (Bosonzahl-Parität),
\(\mu_4=g^4(S_2+c^4 X_4)\). Die native Zwei-Teilchen-Casimir-Identität
\(8W^\dagger W+4C_{\mathrm{Spin}(10)}+4C_{\mathrm{SU}(4)}=120\,I\) auf allen
2016 Paaren liefert nach Summation über die 60 Vermittler und Kontraktion der
beiden Paarindizes exakt \(S=480\), \(S_2=S^2=230\,400\), \(X_4=S^2=230\,400\).
Also \(I_4=\mu_4/\mu_2^2=(230\,400+c^4\cdot230\,400)/480^2=1+c^4\).

| \(c\) | \(I_4\) exakt | \(1+c^4\) erwartet | Status |
|---|---|---|---|
| 3/5 | 706/625 | 706/625 | exakt |
| 4/5 | 881/625 | 881/625 | exakt |
| 0 | 1 | 1 | exakt |
| 1/4 | 257/256 | 257/256 | exakt |
| 1/2 | 17/16 | 17/16 | exakt |
| 1 | 2 | 2 | exakt |

\(I_4(3/5)\neq I_4(4/5)\): die beiden Werte behalten dieselben einzelnen
lokalen W-Identitäten, haben aber verschiedene Antworten. **Für die
nichtnegative Familie ist c aus \(I_4\) eindeutig zurückgewinnbar** (x⁴
monoton auf [0,1]).

**C4-Quellstrahlen:** Die Überlappungsquadrate \(\{0,1/4,1/2,1\}\) sind
Kandidaten für \(c^2\). \(I_4=1+c^4=1+(c^2)^2=1+s^2\):

| \(s=c^2\) | \(I_4=1+s^2\) | c rational? |
|---|---|---|
| 0 | 1 | ja (c=0) |
| 1/4 | 17/16 | ja (c=1/2) |
| 1/2 | 5/4 | **nein** (c=1/√2) |
| 1 | 2 | ja (c=1) |

## 4. Inverser Test (ii): \(Q=(1/960)\operatorname{Tr}_{\rm intern}(8I-G_C^{(3)})\) (Familie 2, exakt)

Bei \(L=2\): verteilt \(C=I_2/\sqrt2\), kollektiv \(C=J_2/2\).
\(Q=C^\dagger C\):

| Wahl | \(Q\) (exakt) | Eigenwerte | tr Q |
|---|---|---|---|
| verteilt | \(I_2/2\) | {1/2, 1/2} | 1 |
| kollektiv | \(J_2/2\) | {0, 1} | 1 |

Beide haben gleiche pro-Chart-Paar-Gram (tr Q = 1 ⇒ 8 I₆₀ pro Chart) und
gleiche **gesamte** N=2-Spektren. Die allgemeine Identität
\(G_C^{(3)}=8I-Q\otimes K\), \(\operatorname{tr}K=960\), liefert
\(8I-G_C^{(3)}=Q\otimes K\) und damit
\(Q=(1/960)\operatorname{Tr}_{\rm intern}(8I-G_C^{(3)})\) exakt. Für beide
C-Wahlen rekonstruiert (Guard: Q_recon == Q_exact).

**Die 0-vs-64 N=3-Aufspaltung** wird auf dem 64-dimensionalen
χ-Kompositblock (16′,4̄) reproduziert — **nicht** auf dem vollen
349056-dimensionalen N=3-Träger. Auf dem χ-Block wirkt K als Skalar;
\(G_C^{(3)}|_\chi=8I_{64}-Q\otimes k_\chi\). Verteilt (Q-Eigenwert 1/2,
doppelt): Eigenwerte \(8-(1/2)k_\chi\), keines gleich \(8-k_\chi\) ⇒
**0 Eigenzustände** bei der kollektiven Resonanzenergie. Kollektiv
(Q-Eigenwerte {0,1}): Eigenwerte 8 (Vielfachheit 64) und \(8-k_\chi\)
(Vielfachheit 64) ⇒ **64 Eigenzustände** bei der Resonanz. Dies ist kein
Port-Umbenennungseffekt. Der vollständige 349056-dim-Contraction wurde
**nicht** neu gebaut; der reduzierte Gram-Operator ist die exakte kleine
Reproduktion.

## 5. Selektionsfrage (Aufgabe 3) — das fehlende typisierte Map

Die dokumentierten Abbildungen (Cartan-Ladungen FW→BW, ganzzahlig, an allen
480 Vertizes) tragen **keinen** reellen Überlappungsparameter. Guard: FW-
und BW-Einträge sind ganzzahlig (kein reeller Überlappungsdatum). Daher ist
**kein** Überlappungsquadrat der C4-Quellstrahlen durch die dokumentierten
Abbildungen allein einer CAR-Chart-Überlappung typisierbar.

**Präzise lokalisierte offene Fortsetzungsbedingung:** eine
Chart-Verklebungs-Homomorphismus \(\varphi:\{\text{C4-Quellstrahl-Überlappungsquadrate}\}\to[0,1]\)
(mit \(\varphi(s)=\sqrt{s}\)), die mit der Spin(10)×SU(4)-Ladungserhaltung an
allen 480 Vertizes verträglich ist und ein einzelnes c auswählt. Dies ist der
Kandidat für die offene Fortsetzungsbedingung.

## 6. Äquivalenzcheck (Aufgabe 4)

**Familie 1:** Operationelle Äquivalenz \(\sim_1\) identifiziert \((c,c')\)
g.d.w. alle intern-invarianten Prozesswahrscheinlichkeiten übereinstimmen.
Das unterscheidende Observable ist \(I_4=1+c^4\).
\(I_4(c)=I_4(c')\Rightarrow c^4=c'^4\Rightarrow c=c'\) (c,c'≥0). Also ist
\(\sim_1\) die **Identität** auf \([0,1]\): keine zwei verschiedenen c sind
äquivalent. Unterscheidendes Experiment: \(I_4\) (oder \(P(L\to R;t)\) in
Ordnung \(t^4\)); verschiedene c geben verschiedene unbedingte
Wahrscheinlichkeiten. Guard: \(I_4\) injektiv auf \(\{0,0{,}1,\ldots,1{,}0\}\).

**Familie 2:** \(\sim_2\) identifiziert \((C,C')\) g.d.w. alle geforderten
Observablen übereinstimmen (Paar-Gram 8 I₆₀, gesamte N=2-Spektren,
matrixaufgelöster N=3-Antwort-Operator \(G_C^{(3)}\)). Die ersten beiden sind
C-unabhängig; \(G_C^{(3)}\) unterscheidet über \(Q=C^\dagger C\).
Verteilt \(Q=I_2/2\) vs kollektiv \(Q=J_2/2\): **verschiedene Matrizen ⇒
nicht äquivalent**. Unterscheidendes Experiment: N=3-Ein-Boson-Eigenzustände
bei Energie Δ: 0 vs 64 (verschiedene unbedingte Wahrscheinlichkeiten, der
Spektralprojektor unterscheidet sich um 64). Innerhalb jeder Q-Klasse sind
alle C mit demselben \(C^\dagger C\) äquivalent (Paar-Gram, N=2-Spektren,
\(G_C^{(3)}\) hängen nur an Q). **Reichweite von \(\sim_2\**: Klassen
indiziert durch Q (positiv semidefinit, Spur 1, Rang 1 oder 2).

## 7. Phasensensitivität (Aufgabe 5)

Die \(Q=C^\dagger C\)-Formel rekonstruiert Q innerhalb der Familie, aber
**nicht** jede markierte Phase von C. Eine unitäre Phasenrotation
\(C\to CU\) mit \(U\) unitär und \([U,Q]=0\) lässt Q unverändert. Ein
phasensensitiver Test muss ein Observable messen, das keine Funktion von Q
allein ist.

**Konkreter phasensensitiver Test:** die kopieübergreifende
Boson-Kohärenz \(\langle b_A^\dagger(p)\,b_A(q)\rangle\) (\(p\neq q\)) =
\((CC^\dagger)_{pq}\). Bei \(L=2\), kollektive Klasse \(Q=J_2/2\):
- \(U=I_2\): \(CC^\dagger=J_2/2\) ⇒ Kopieübergreifend (außerhalb der
  Diagonale) \(+1/2\).
- \(U=\operatorname{diag}(1,-1)\): \(C=\operatorname{diag}(1,-1)J_2/2\),
  \(CC^\dagger=(1/2)\begin{pmatrix}1&-1\\-1&1\end{pmatrix}\) ⇒ außerhalb
  der Diagonale \(-1/2\).

**Selbes** \(Q=C^\dagger C=J_2/2\), **verschiedenes** \(CC^\dagger\) ⇒ der
Test unterscheidet markierte Phasen von C, die \(Q=C^\dagger C\) unsichtbar
lässt. Guard: außerhalb der Diagonale \(+1/2\) vs \(-1/2\) (exakt).

## 8. Reproduktion und Grenzen

`replay.py` führt den Prüfer normal und unter `-OO` aus und verlangt
Byteidentität (bis auf Laufzeitfelder). Der abschließende Lauf besteht mit
Status PASS und **50 Prüfwachen** (alle exakt, 0 numerisch). Guardzahlen
zählen Prüfbedingungen, keine unabhängigen Theoreme.

**Nicht geleistet:** die typisierte Chart-Verklebungsabbildung (Aufgabe 3,
offen); der vollständige 349056-dim-Contraction (reduziert reproduziert);
eine physikalische Herleitung des Zustandsfunktionals; ein T1–T8-Tor;
RH/Faktorisierung/P-vs-NP. Kein Commit, kein Push.

```sh
cd experiments/theory-contracts/universalraum-v169-model-selection-20260915
/opt/homebrew/bin/python3 replay.py   # PASS, 50 guards, byte-identical
```
