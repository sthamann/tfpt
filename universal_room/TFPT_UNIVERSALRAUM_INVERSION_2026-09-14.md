# TFPT-Universalraum: Die Inversionshypothese — Prüfung, vier Follow-ups und Gesamtinterpretation

Stand: 14. September 2026. Anschlusspaper zum Manuskript vom 13.09.
(`tfpt_compiler_universalraum_2026-09-13.pdf`), zum Herkunfts-Audit
(`compiler-origin-audit-20260913`) und zum Erweiterungs-Audit
(`compiler-extension-audit-20260914`). Alle neuen Befunde sind im Contract
`experiments/theory-contracts/universalraum-inversion-20260914/` maschinell
belegt (325 + 147 exakte Checks, 19 Tests, gleicher Quellpin
`ba1da931…9e3995` auf `context_instrument.py`).

**Evidenzkonvention** (wie im Manuskript): *gesetzt* = Ausgangsannahme,
*exakt* = Identität/Beweis unter genannten Voraussetzungen, *bedingt* =
Folgerung mit zusätzlicher Zuordnung, *offen* = ungeschlossene Herkunfts-
oder Existenzfrage. NON-RH. Keine T1–T8-Schließung, keine Promotion in
`verification/`, Ledger, Papers oder Website.

## 1. Ergebnis in einem Satz

**Die Umkehrhypothese — „der Universalraum ist das System verbundener
Veränderungen, TFPT ist eine strukturierte Auslesung davon" — besteht ihren
eigenen Schärfetest maschinell: Auf dem TFPT-Systemschatten existiert
nachweislich keine autonome Dynamik; die vollständige Rekonstruktion des
Universalraums scheitert an fünf benannten Gattern, von denen eines (die
Kontextregel) in dieser Runde zur Hälfte geschlossen wurde.**

## 2. Die Hypothese und ihr Prüfprogramm

Die eingereichte Hypothese verlangt drei Dinge von einem tieferen Ansatz:
(i) er muss die TFPT-Strukturen liefern (Träger, Markierungen, Kontexte,
Operatorbeziehungen — nicht nur Dimensionen); (ii) er muss die richtige
Ausführung liefern (Kopplung, Kontextwahl, Aufzeichnung gemeinsam); (iii)
er muss eine zusätzliche prüfbare Aussage machen. Ihr zentrales Kriterium
ist die Schatten-Kommutatorbedingung

\[
\mathcal P(\Phi(X)) = D(\mathcal P(X)):
\]

erst innen weiterentwickeln, dann auslesen = den Schatten nach eigener Regel
weiterentwickeln. Scheitert diese Bedingung, ist die Auslesung nachweislich
unvollständig.

## 3. Befund I — Die Anker der Hypothese sind korrekt (exakt)

An den gepinnten Quellobjekten erneut geprüft:

- **Registerexperiment:** gleicher sichtbarer Zustand \(I_4/4\) nach einem
  Schritt; kohärente Registerwiederverwendung kehrt zum reinen Zustand
  zurück (\(U^2=I\)), frische Register iterieren die Dephasierung.
- **Vierträgerzelle:** \(\Omega\in\Lambda^4\mathbb C^4\) rein und eindeutig,
  alle Einzelmarginalien \(I_4/4\), Paarmarginalien \((I-S)/12\) zertifizieren
  den Zustand.
- **30 unsichtbare Richtungen:** \(\ker T=\ker(C,F)\), Dimension 30 — sie
  werden von \(T\) *ausgelöscht*, leben also **nicht** als verborgenes
  Gedächtnis im reduzierten Prozess weiter. Das Gedächtnis sitzt in der
  größeren kohärenten Ausführung, nicht im Nullraum.
- **Kanaldreieck:** volle Symmetrie lässt die Familie
  \(K_{abc}=aI+\frac b6(B-I)+\frac c8(J-B)\); der Quellpunkt
  \((1/7,6/7,0)\) ist nicht symmetrieerzwungen.

## 4. Befund II — Kein autonomer Systemschatten; die minimale Hülle ist der CQ-Zustand (exakt)

Der Schärfetest der Hypothese, am tatsächlichen Prozess ausgeführt:

**Zeugenpaar.** \(X_1\) = Zustand nach einer Vormessung mit behaltenem
kohärentem Register; \(X_2\) = dephasierte Alternative mit frischem Register.
Beide haben denselben Systemschatten: \(\mathcal P(X_1)=\mathcal P(X_2)=I_4/4\).
Dieselbe erlaubte Fortsetzung \(\Phi\) (nochmaliges \(U\)) liefert
\(\mathcal P(\Phi X_1)=|+\rangle\langle+|\neq I_4/4=\mathcal P(\Phi X_2)\).
Also existiert **keine** Funktion \(D\) mit \(\mathcal P\circ\Phi=D\circ\mathcal P\)
für alle erlaubten Fortsetzungen. (PROOF.md, P2.)

**Präzisierung.** Für die Teilausführung „jedes Mal frisches Register"
existiert sehr wohl eine autonome Schattenregel (die Dephasierung \(\Delta\)).
Der Befund sagt also: *der Schatten allein bestimmt nicht, welche Ausführung
vorliegt* — das Registerprotokoll ist Prozessdatum, nicht Zustandsdatum.

**Minimale Hülle.** Der Kontextschatten allein ist autonom (\(K\)); der volle
CQ-Zustand ist autonom; aber System- **plus** Kontextmarginalie *ohne ihre
Korrelation* reichen nicht: ein Zeugenpaar mit identischen Marginalien und
verschiedener Kontext-System-Korrelation hat verschiedene Zukünfte. Die
minimale autonome Beschreibung in diesem Modell ist der volle CQ-Zustand
(15×16 reelle Koordinaten). **Der „Universalraum" ist hier also erzwungenermaßen
ein Prozessobjekt mit Gedächtnis — kein Zustandsraum.**

## 5. Befund III — Follow-up G1: Die Kontextregel ist der kovariante Abschluss der Quellkombinatorik (exakt, Restannahme offen)

Bisher war der Punkt \((1/7,6/7,0)\) nur durch zwei gesetzte Prinzipien
(\(c=0\): nur inzidente Nachfolger; \(\mu=0\): nichts Unsichtbares überlebt)
ausgewählt. Neu:

1. Aus der Inzidenzmatrix \(B\) allein werden rekonstruiert: die symplektische
   Paarung, die \(\mathbb F_2\)-Addition der 15 Labels, die volle Gruppe
   \(Sp(4,2)\) (exakt 720 Elemente) und eine 1-Faktorisierung
   \(B=\sum_{j=1}^{7}P_j\) in sieben perfekte Matchings.
2. Der kovariante Abschluss — Konjugation der sieben Matchings unter der
   ganzen Gruppe, 5040 Terme — überdeckt **4500 verschiedene** perfekte
   Matchings (von 24.601.472 möglichen; Multiplizitäten 1 und 4) und induziert
   **exakt** \(K=B/7\): jeder der sieben erlaubten Nachfolger erhält Gewicht
   \(1/7\).

Damit ist die Kontextregel nicht mehr gesetzt, sondern **der
\(Sp(4,2)\)-kovariante Abschluss der quelleneigenen Faktorisierung**.
Bemerkenswert: Die Gruppe kann wegen \(7\nmid 720\) nicht transitiv auf den
sieben Matchings wirken — die Gleichmäßigkeit entsteht erst durch die
Überdeckung von 4500 Matchings im Orbit, nicht durch Matching-Transitivität.

**Offen (Restannahme):** Warum die Labeldynamik eine Permutationsmischung
dieser kovarianten Form sein sollte, ist nicht abgeleitet; die Lift-Frage
(Messen-und-Präparieren vs. kohärente Permutation) bleibt unentschieden —
beide induzieren dieselbe Regel. G1 ist damit zur Hälfte geschlossen:
die *Regel* ist quellengeerdet, die *Ausführung* nicht.

## 6. Befund IV — Follow-up G3: Zeit — statische relationale Struktur ja, Uhrwerk nein (exakt)

- **Existenz:** \(H_{\text{sys}}=J\sum_{1\le i<j\le3}\frac{I+S_{ij}}2\) auf den
  Trägern 1–3 erhält jede Träger-0-Lesart (\([H_{\text{sys}},P_t]=0\)) und
  annihiliert \(\Omega\). Die vier bedingten Zustände
  \(\psi_t=\langle t|_0\Omega\) sind exakte Nullmoden, rein, paarweise
  orthogonal, je mit Wahrscheinlichkeit \(1/4\). \(\Omega\) ist also ein
  **statischer Page–Wootters-Zustand**: global stationär, intern relational
  strukturiert — die von der Hypothese genannte Möglichkeit ist im Modell
  realisiert.
- **Obstruktion:** \(\mathrm{spec}(2H_{\text{sys}}/J)=\{0[4],3[40],6[20]\}\)
  hat nur **drei** Niveaus für **vier** Lesarten. Eine nichtentartete
  PW-Uhr (\(C=\sum_t|t\rangle\langle t|\otimes(H_{\text{sys}}+h_tI)\) mit vier
  verschiedenen \(h_t\)) ist mit paarweiser Swap-Dynamik unmöglich.
  Zusätzlich verändert \(S_{01}\) die Anzeige von Träger 0
  (\(P_{t'}S_{01}P_t\neq0\)): Die Lesart ist unter der Vierträger-Kopplung
  nicht erhalten.

**Konsequenz (offen):** Ein Uhrwerk braucht einen reichhaltigeren
System-Hamiltonoperator (mindestens vier nutzbare Niveaus) oder eine
explizit uhr-erhaltende Aufspaltung — beides ist eine zusätzliche, bisher
nicht ausgewählte Struktur.

## 7. Befund V — Follow-up G5: Gedächtnis = Rekurrenzzeit; Zellenskalierung quantifiziert (exakt)

- **Satz (PROOF.md, P1):** Kein geschlossenes endliches Quantensystem erzeugt
  exaktes exponentielles Abklingen \((3/7)^n\) für alle \(n\): Jede
  Beobachtungssequenz ist eine endliche Summe von Phasenfaktoren, deren
  Cesàro-Mittel \(\overline{|f|^2}=\sum|c_m|^2>0\) ist — Widerspruch zu
  \(|f(n)|\le Cr^n\). Exakte Irreversibilität erfordert offene
  Registerversorgung oder einen Grenzprozess.
- **Quantitative Instanz:** Zyklische Wiederverwendung von \(m\) Registern mit
  dem tatsächlichen Quell-\(U\) (es gilt \(U^2=I\)) liefert exakt:

  | Gedächtnis \(m\) | Kontrastsequenz | Volle Rückkehr |
  |---|---|---|
  | 1 | \(1,0,1,0,1,0,\dots\) | nach 2 Schritten |
  | 2 | \(1,0,0,0,1,0,0,0,\dots\) | nach 4 Schritten |
  | 3 | \(1,0,0,0,0,0,1,\dots\) | nach 6 Schritten |

  **Rekurrenzzeit \(=2m\)** — der Kontrast kehrt exakt zurück, sobald jedes
  Register zweimal benutzt wurde. „Vergessen" ist in diesem Modell exakt so
  lange haltbar, wie frisches Gedächtnis nachgeliefert wird.
- **N Zellen:** Produktzustand liefert \(E_0\le(N-1)\frac{5\lambda}{8}\);
  wegen \(V\ge0\) und Weyl bleibt \(E_1\ge2J\), also
  \(\mathrm{Lücke}\ge2J-(N-1)\frac{5\lambda}{8}\): Eindeutigkeit geschützt
  für \(\lambda<\frac{16J}{5(N-1)}\) — die einfache Schranke degradiert mit
  \(1/N\), **keine** thermodynamische Aussage. Nullenergie ist für alle
  \(N\ge2\) verbaut: Die Kanten-Transpositionen erzeugen die volle
  symmetrische Gruppe (für \(N=2\) enumeriert: \(S_8\), Ordnung 40320), und
  \(\Lambda^{4N}\mathbb C^4=0\).

## 8. Befund VI — Follow-up G4: Teilsysteme sind relational eindeutig erkennbar (exakt, endlicher Rahmen)

Von **allen 105** Qubit-Paarungen der 8-Qubit-Kodierung:

- macht **genau eine** alle sechs Swap-Kopplungen \(S_{ij}\) zwei-körperlich:
  die Trägerfaktorisierung \(\{0,1\},\{2,3\},\{4,5\},\{6,7\}\);
- haben **genau vier** das Rang-6-Profil aller Paarmarginalien: die
  Trägerfaktorisierung plus drei „Bit-Swizzle"-Umgruppierungen;
- der **kombinierte** Fingerabdruck (Zwei-Körperlichkeit ∧ Rangprofil) ist
  eindeutig.

Die umgekehrte Bausteinfrage der Hypothese — „unter welchen Bedingungen
lassen sich in einem gemeinsamen Wirkungszusammenhang zwei unterscheidbare
Teilsysteme erkennen?" — hat hier eine präzise endliche Antwort: **an der
Lokalitätsstruktur der Wechselwirkung**. Die Identität der Träger liegt in
den Beziehungen, nicht in den isolierten Ansichten (die überall \(I_4/4\)
sind). Rahmen der Aussage: Qubit-Paarungen der festen Kodierung, nicht alle
denkbaren Faktorisierungen des 256-dimensionalen Raums.

## 9. Gesamtinterpretation: Was der Universalraum nach dieser Runde ist

Der Kandidat im Sinn der Hypothese ist ein **zusammensetzbarer Prozess**:

```
Universalraum := Träger + Operationen + Zusammensetzung + Zustand
                 + Aufzeichnung + Auslesung
```

| Komponente | Status nach dieser Runde |
|---|---|
| 15 Kontexte / 60 Strahlen aus E₈-Wurzeln, Inzidenz \(B\), Kontextspiegelungen, Vormessungen | quellenabgeleitet (exakt) |
| Kontextregel \(K=B/7\) | **kovarianter Abschluss der Quell-Faktorisierung** (exakt); Lift-Form offen |
| Autonome Ebene | voller CQ-Zustand (Kontext⊗System samt Korrelation) — nachgewiesenermaßen minimal |
| Statische relationale Zeitstruktur | vorhanden (\(\Omega\) als PW-Zustand, vier orthogonale Lesarten) |
| Uhrendynamik | **obstruiert** für paarweise Swaps (3 Niveaus < 4 Lesarten) |
| Irreversibilität | exakt nur mit offenem Gedächtnisnachschub; Rekurrenzzeit \(2m\) |
| Tetramer-\(H\), \(J\), Ω-Präparation, Inter-Register-CZ, Zeitskala | weiterhin **gesetzt** |

**Kernaussage der Inversion, jetzt belegt:** Der Compiler ist nicht die
Maschine, die Realität erzeugt — er ist das Verfahren, ihre sichtbare
Struktur zu lesen; und diese Lesart ist nachweislich unvollständig: Sie
verliert genau die Kontext-System-Korrelationen und Aufzeichnungen, die die
Zukunft tragen.

## 10. Verbleibende Gatter und nächste Schritte

- **G1 (halb):** Eine dynamische Begründung, warum die Labeldynamik die
  kovariante Permutationsform hat (statt Messen-und-Präparieren). Erfolg =
  ein Interferenzzeuge, der die Lifts unterscheidet *und* aus der Quelle
  entschieden wird.
- **G2:** Kopplung, Präparation, Registerversorgung aus der Quelle ableiten
  (unverändert das zentrale Herkunftsproblem).
- **G3:** System-Hamiltonoperator mit ≥4 nutzbaren Niveaus und erhaltener
  Uhrenanzeige suchen; Erfolg = bedingte Zustände entwickeln sich geordnet.
- **G4:** Von Qubit-Paarungen zu allgemeineren Faktorisierungsklassen
  (observablenbasiert statt qubitbasiert).
- **G5:** Schärfere Vielzellen-Schranken (jenseits der \(1/N\)-Degradation),
  z.B. über die volle S₄⊗…-Symmetrie; und die Frage, ob ein
  Grenzprozess \(N\to\infty\) die exakte \((3/7)^n\)-Regel trägt.

## 11. Grenzen

Keine Aussage dieser Runde schließt T1–T8. Die Vierträgerzelle bleibt ein
gesetztes Modell; ihre Kopplung, Stärke und Präparation sind nicht aus der
TFPT-Quelle abgeleitet. G4 ist ein endlicher Eindeutigkeitssatz innerhalb
der enumerierten Klasse. G5-Bounds sind variational/einfach. Nichts hier ist
ein RH-, Faktorisierungs- oder P-vs-NP-Resultat.

## 12. Reproduktion

```sh
cd experiments/theory-contracts/universalraum-inversion-20260914
python3 -B checker.py validation.json
python3 -B followup_checks.py followup_validation.json
python3 -B -m unittest test_checker test_followup   # 19 Tests, auch -OO
```

Quellpin: `context_instrument.py` SHA-256 `ba1da931…9e3995`; der Prüfer
bricht bei jeder Quelländerung geschlossen ab (Pin-Test). Herleitungen:
`PROOF.md` (P1 kein exaktes Abklingen geschlossen; P2 kein autonomer
Systemschatten; P3 Kontextpunkt; P4 relationale Lesarten ohne Dynamik).
