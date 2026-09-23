# TFPT-Universalraum: Gesamtsynthese — beide Richtungen, vollständige Funktionsweise, drastische Effekte im Katalog-Befund

Stand: 14. September 2026. Analyse- und Synthese-Dokument (Chat-Runde vom 14.09.) auf
Grundlage von drei Quellen:

- `universal_room/tfpt_compiler_universalraum_2026-09-13.pdf` (Manuskript v1.0/1.1:
  „Vom geometrischen Compiler zum Prozess mit Aufzeichnung")
- `universal_room/TFPT_UNIVERSALRAUM_INVERSION_2026-09-14.md` (Inversionshypothese,
  Contract `experiments/theory-contracts/universalraum-inversion-20260914/`)
- `universal_room/tfpt_anschluss_zellen_seam_2026-09-14.pdf` (Fable-Runde 3:
  Zustandsgate, Trägerzellen, A3-Faktor des Seams)

sowie Pflichtabfragen des RH-Katalogs (`rh/catalog/rhcat.py`: stats, check-new,
search, family, dossier) gemäß Skill `rh-corpus-search` und Routing `AGENTS.md`.

**Evidenzkonvention** (wie im Manuskript): *gesetzt* = Ausgangsannahme, *exakt* =
Identität/Beweis unter genannten Voraussetzungen, *bedingt* = Folgerung mit
zusätzlicher Zuordnung, *offen* = ungeschlossene Herkunfts- oder Existenzfrage.
**Abgrenzung:** Dieses Dokument bewegt keinen Ledger-Marker, schließt kein T1–T8
und erhebt **keinen** RH-, Faktorisierungs- oder P-vs-NP-Anspruch. Es dokumentiert
eine Synthese und die Katalog-Lage; alle drastischen Routen haben getötete
Vorläufer mit benannten Kill-IDs (Teil 5).

## 1. Analyse: TFPT und die zwei Universalraum-Richtungen

### 1.1 Der tragende Kern in fünf Schritten

| Schicht | Inhalt | Status |
|---|---|---|
| Postulate | P1: orientierter Rand/Naht, \(c_3 = 1/(8\pi)\); P2: fünfteiliger Träger, \(g_{\rm car}=5\) | gesetzt |
| Verklebung | \(D_5 \oplus A_3\) (beide det = 4), Index-4-Überverband mit \(\mu_4\)-Glue ⇒ \(E_8\) | exakt |
| Zerlegung | \(248 = 45+15+60+64+64\), d. h. \((45{,}1)+(1{,}15)+(10{,}6)+(16{,}4)+(16{,}\bar 4)\) | exakt |
| Endliches Bild | 60 Strahlen in 15 Viererkontexten (Zwei-Qubit-Stabilizer); \(Sp(4,2)\cong S_6\); Clock \(\sigma\) (Ord. 3), Lift \(c=i\sigma\) (Ord. 12) | exakt |
| Auslesung | SM-Ladungstabelle (anomaliefrei, \(k_Y=5/3\)), Flavor-Seed \(\phi_0\approx0{,}05317\), \(\alpha^{-1}=137{,}0359992168\) (1,9σ neben CODATA 2022) | exakt als Formelwerte, bedingt als Physik |

Anker \(a=(1,1,2)\): elementarsymmetrische Größen \(4,5,2\); Potenzsummen
\(p_n = 2+2^n\); \(p_1p_2p_3 = 240\); \(240+p_4-p_3 = 248\). Alle
Abschlussbedingungen T1–T8 bleiben offen.

### 1.2 Richtung A: „Der Raum entsteht aus TFPT" (bottom-up)

Programm: Aus den Compilerdaten wird ein Prozess konstruiert; der „Raum" ist, was
der Compiler ausführt. Erreicht (13.09.-Manuskript + Fable-Runde 3):

1. **Die Zelle ist erzwungen, nicht gewählt** (Hüllensatz, exakt). Von
   \(4\otimes4 = 6\oplus10\) kommt in der 248 nur \(\Lambda^2(4)=6\) vor;
   \(\mathrm{Sym}^2(4)=10\) fehlt. Ein Vierträgerzustand mit \(E_8\)-zulässigen
   Paarmarginalien ist eindeutig \(\Omega=\Lambda^4\mathbb{C}^4\); für fünf Träger
   existiert keiner (\(\Lambda^5\mathbb{C}^4=0\)). \(H_{\rm tet}\) ist das
   Straffunktional dieser Hülle, \(J\) ihre Steifigkeit. Die Klammer
   \([(16,4),(16,4)]\) landet ausschließlich in \((10,6)\) (960 geordnete
   Wurzelpaare): die Quelle antisymmetrisiert Trägerindizes.
2. **Die Kontextregel ist erzwungen** (G1 halb, exakt). Aus \(B\) allein:
   symplektische Paarung, \(\mathbb{F}_2\)-Addition der 15 Labels, volles
   \(Sp(4,2)\) (720 Elemente), 1-Faktorisierung \(B=\sum_{j=1}^7 P_j\). Der
   kovariante Abschluss (5040 Terme → 4500 überdeckte perfekte Matchings)
   induziert exakt \(K=B/7\). Wegen \(7\nmid720\) entsteht die Gleichmäßigkeit
   durch Orbit-Überdeckung, nicht durch Transitivität. Offen: die Lift-Form
   (Messen-und-Präparieren vs. kohärente Permutation).
3. **Die relative Uhr ist lesbar und lift-unabhängig** (exakt).
   \(A^{\otimes4}\Omega=\det(A)\,\Omega\); \(\langle\Omega|c_1^n|\Omega\rangle
   =\mathrm{tr}(c^n)/4\); \(p_{1j}=(16-|\mathrm{tr}\,c^n|^2)/24\). Die
   3-Zykel-Klasse fixiert 3 der 15 Kontexte und 0 der 15 Paulis ⇒
   \(|\mathrm{tr}\,c|=1\) ⇒ \(p_{1j}=5/8\), \(\langle H_{\rm tet}\rangle=15J/8\).
   Periode 3 in Populationen, 12 nur im Überlapp.
4. **Die Kette regeneriert den Seam-Faktor** (numerisch, stark). Uniforme Ringe:
   \(\Delta\cdot n = 3{,}700/3{,}663\) gegen \(SU(4)_1\)-WZW \(3{,}701\);
   Sutherland-Grundenergie \(0{,}0877\) gegen \(0{,}0874\); \(c_{\rm fit}=3{,}16\)
   gegen \(c=3\). \((A_3)_1\) ist der Familienfaktor des Seams
   \((E_8)_1\supset(D_5)_1\otimes(A_3)_1\), \(c=8=5+3\).

Wand dieser Richtung: \(\lambda\), Graph, Cross-Register-\(CZ\), Präparation,
Registerversorgung, Zeitskala — gesetzt. Zusatzwarnung: \(\det K<0\), also ist
\(K\) nicht als Exponential einer reellen Matrix einbettbar (nur \(K^2\)).

### 1.3 Richtung B: „TFPT entsteht aus dem Raum" (Inversion, top-down)

Programm: Der Universalraum ist primär („System verbundener Veränderungen"), TFPT
eine strukturierte Auslesung \(\mathcal P\). Schärfetest: Schatten-Kommutator
\(\mathcal P(\Phi(X)) = D(\mathcal P(X))\). Maschinell belegt (325 + 147 exakte
Checks, 19 Tests, Quellpin `ba1da931…9e3995`):

1. **Kein autonomer Systemschatten** (exakt): Zeugenpaar \(X_1/X_2\) mit
   gleichem Schatten \(I_4/4\), aber verschiedenen Zukünften. Das
   Registerprotokoll ist Prozessdatum, nicht Zustandsdatum.
2. **Minimale Hülle = voller CQ-Zustand** (exakt): Kontext⊗System *mit*
   Korrelation, \(15\times16\) reelle Koordinaten. Der Universalraum ist
   erzwungenermaßen ein Prozessobjekt mit Gedächtnis — kein Zustandsraum.
3. **Zeit: statisch-relational ja, Uhrwerk nein** (exakt/offen): \(\Omega\) ist
   Page–Wootters-Zustand (vier orthogonale Lesarten à 1/4); aber
   \(\mathrm{spec}(2H_{\rm sys}/J)=\{0[4],3[40],6[20]\}\) hat nur drei Niveaus
   für vier Lesarten — nichtentartete PW-Uhr mit paarweisen Swaps obstruiert.
4. **Gedächtnis = Rekurrenzzeit** (exakt): kein geschlossenes endliches System
   erzeugt exaktes \((3/7)^n\) (Cesàro); \(m\) zyklisch wiederverwendete Register
   → Kontrastrückkehr nach \(2m\) Schritten. Exakte Irreversibilität erfordert
   offene Registerversorgung oder einen Grenzprozess.
5. **Teilsysteme relational eindeutig** (exakt, endlicher Rahmen): von allen 105
   Qubit-Paarungen macht genau eine alle sechs Swaps zwei-körperlich — die
   Trägerfaktorisierung. Identität liegt in der Lokalitätsstruktur der
   Wechselwirkung.

Kernurteil: Der Compiler ist nicht die Maschine, die Realität erzeugt — er ist
das Verfahren, ihre sichtbare Struktur zu lesen; diese Lesart ist nachweislich
unvollständig (verliert genau die Korrelationen/Aufzeichnungen, die die Zukunft
tragen).

## 2. Synthese: dieselbe Wand von beiden Seiten — der Fixpunkt

- Richtung A scheitert an: Zusammensetzung (\(\lambda\), Graph, Cross-Register)
  und Aufzeichnung (Frische, Versorgung).
- Richtung B scheitert an: Zusammensetzung (Schatten trägt Ausführungsregel
  nicht) und Aufzeichnung (verworfene Korrelationen tragen die Zukunft).

**Es ist dieselbe Wand.** Die Asymmetrie ist präzise lokalisiert: Wo die Algebra
vollständig ist, ist Algebra → Prozess eindeutig (Zelle per Hüllensatz, \(K\) per
kovariantem Abschluss, Uhrprotokoll per Lift-Fixierung). Wo der Prozess Gedächtnis
hat, ist Prozess → Algebra verlustbehaftet (kein autonomer Schatten,
CQ-Minimalität, Rekurrenz).

**These (bedingt, teils exakt untermauert):** Der Universalraum ist der minimale
autonome Prozess \(\mathcal R\), dessen lesbare Schatten die TFPT-Strukturen sind
*und* dessen Abschluss unter seinen eigenen erzwungenen Operationen die
Nahtalgebra regeneriert. Weder erzeugt der Compiler den Raum noch der Raum den
Compiler — beide sind zwei Auslesungen desselben selbstkonsistenten Fixpunkts.
„Entstehen" wird durch „Selbstkonsistenz" ersetzt. Die teilweise geschlossene
Schleife:

\[
E_8 \xrightarrow{\text{60 Strahlen, 15 Kontexte}} \text{Prozess}
\xrightarrow{\text{Hüllensatz}} \Omega=\Lambda^4\mathbb{C}^4
\xrightarrow{\text{Austausch, uniformer Limes}} (A_3)_1 \subset (E_8)_1
\]

**Physikalische Lesart: Der Raum *ist* die Naht.** Der Bulk eines holomorphen
Seams ist eine gapped invertible Phase (Fable-Korrektur) — „leer bis auf
Invertierbarkeit"; alle Struktur lebt auf der Naht. „Der Raum entsteht aus TFPT"
= die bulk-artige Erscheinung ist Auslesung des Nahtprozesses; „TFPT entsteht aus
dem Raum" = TFPT ist die Selbstbeschreibung der Naht in ihren eigenen Schatten.
Naht = Raum = Compiler: drei Schatten eines Prozessobjekts.

**Zahlentriade (offen, keine Bijektion behauptet):** minimal autonomer Zustand
\(15\times16=240\) reelle Koordinaten; \(E_8\) hat 240 Wurzeln; Anker
\(p_1p_2p_3=240\). Eine natürliche Bijektion (Kontext, Operatorbasis) ↔ Wurzeln
ist ein benennbares Ziel — bis dahin Numerologie.

**Zeitauflösung (Fable §8):** Hecke-Index \(|\det A|\) = Jones-Index des
Gitterunternetzes; \(\log|\det A|\) = bedingte Entropie (Pimsner–Popa); Zählfunktion
\(\prod_{k=0}^{7}\zeta(s-k)\), Pol bei \(s=8=c\). Arithmetische „Normzeit" =
RG-Zeit; physische Zeit = \(L_0\). Der Streit „elektrische Zeit vs. Normzeit"
löst sich als Kategorienunterschied auf.

## 3. Vollständige Funktionsweise als Ableitungskette

**Schicht 0 → 1 (Quelle → Compiler):** P1 + P2 ⇒ \(D_5\oplus A_3\)
\(\xrightarrow{\mu_4}\) \(E_8\) (exakt); 248-Zerlegung (exakt); endliches Bild
\(\mathbb{F}_2^4\) symplektisch → 60 Strahlen/15 Kontexte (exakt). **Stopp:**
Auswahl von P1/P2 (T1) offen.

**Schicht 1 → 2 (Compiler → Prozess) — ein Schritt der Maschine:**

1. Kontextwahl \(K=B/7\) — kovarianter Abschluss (exakt, Lift offen).
2. Messung — Born + scharf + wiederholbar + Rang-1 ⇒ Krausoperator eindeutig
   (exakt; Born-Regel selbst nicht hergeleitet).
3. Kopplung/Aufzeichnung — \(R=I-2\Pi\) (Kanalmittel = Dephasierung, kurze
   Identität speziell für Dimension 4), \(W=J_4/2-I\),
   \(A=(I-2|0\rangle\langle0|)W\), Cross-Register-\(CZ\) (Operator-Schmidt-Rang 4)
   ⇒ unitäre Vor-Messung \(U\), \(U^2=I\) (exakt am Modell). **Stopp:** erlaubte
   Verbindung verschiedener Träger und Registerversorgung gesetzt (G2).
4. Auslesung — zwei Schatten desselben \(T\) mit \(CT=KC\), \(ET=\Delta E\)
   (exakt); \(3/7\) kombinatorisch (drei von sieben Nachfolgekontexten tragen je
   eine relevante Pauli-Richtung); \(\ker T = \ker(C,F)\), Dim. 30, wird
   ausgelöscht (kein verborgenes Gedächtnis im Nullraum).

**Zelle:** \(\Omega=\Lambda^4\mathbb{C}^4\) eindeutig (Hüllensatz);
\(H_{\rm tet}=J\sum(I+S_{ij})/2\), Spektrum \((0,1),(2,45),(3,40),(4,135),(6,35)\),
Gap \(2J\). **Uhr:** Protokoll exakt, Dynamik obstruiert (3 Niveaus < 4
Lesarten). **Kette:** Schur–Weyl exakt bis \(n=16\); zwei Zellen eindeutig bis
\(\lambda\le6J\); Gap konvergiert für \(\lambda<J\), schließt wie \(1/n\) bei
\(\lambda=J\); uniformer Ring = \(SU(4)_1\)-WZW numerisch. **Stopp:** \(\lambda=J\)
und \((D_5)_1\) nicht abgeleitet.

**Schicht 2 → 3 (Prozess → Schatten):** kein autonomer Systemschatten; CQ-Zustand
minimal; Rekurrenz \(2m\); Offenheitszwang für exakte Irreversibilität;
\(\det K<0\); zwei Lifts mit Interferenz \(1/15\) vs. \(1\).

**Schicht 3 → 4 (Schatten → Physik):** Ladungstabelle, Familien \((16-1)/5=3\to48\),
Flavor-Seed, \(\alpha^{-1}\), CKM/PMNS/Kosmologie; Hierarchien \(x=Re^{-A}\) mit
\(A\)-Verhältnis \(1:5:10\) (\(\alpha^{-1}/5,\alpha^{-1},2\alpha^{-1}\));
Gravitations-Zielstruktur \(c_3^{-1}=8\pi\) als Koeffizientenidentifikation.
**Stopp:** T1–T8 offen (v. a. T2 renormiertes Half-Charge-Feld, T3 3+1D-Ursprung,
T5 Kontinuumslimes, T8 Anfangszustand).

**Funktionsweise in einem Satz:** endlicher, exakt kalkulierbarer Prozess aus
Kontextwahl, Messung, Aufzeichnung und Auslesung auf der \(E_8\)-Naht; Zellen und
Regeln großteils erzwungen statt gewählt; Gedächtnis sitzt in Aufzeichnungen,
nicht im Zustand; im uniformen Limes regeneriert der Prozess den Familienfaktor
seiner eigenen Algebra; fünf gesetzte Fugen bleiben (\(\lambda\), Graph,
Cross-Register-Kopplung, Präparation, Zeitskala).

## 4. Was wir damit machen können (legitime Fähigkeiten)

1. **Falsifikationsmaschine mit empirischen Klippen:**
   - Protonzerfall: 2-Loop mit quelleigenem Pati–Salam-Inhalt fällt \(\tau_p\) um
     Faktor 2,4–6 unter \(2{,}4\cdot10^{34}\) a — disfavoured, falls SO(10)
     oberhalb \(\Lambda\) geeicht („gauging fork"). Hyper-Kamiokande entscheidet
     empirisch. Koinzidenz \(M_{PS}/M_s = 1{,}2\)–\(1{,}4\) mit
     \(M_s = c_3^{7/2}\bar M_{\rm Pl} = 3{,}06\cdot10^{13}\) GeV überlebt 2-Loop.
   - \(\alpha^{-1}=137{,}0359992168\) vs. CODATA 2022 \(137{,}035999177(21)\):
     1,9σ — jede künftige CODATA-Revision ist Kill oder Bestätigung.
   - \(r\approx0{,}0033\)–\(0{,}0048\), \(n_s\approx0{,}96\): im Zugriff
     CMB-S4-artiger Programme.
2. **Diskret→Kontinuum-Brücke:** Zelle → Kette → \((A_3)_1\); Kondo-Schritt
   (\((16,4)\)-Kopplung an zehn Majoranas) mit Ziel \(c=8\) und
   \(\mathbb{Z}_4\)-Glue als Fixpunkt wäre die erste abgeleitete
   Kontinuumsfeldtheorie aus endlichen Postulaten.
3. **Konsistenz-Engine:** Auswahlregeln („\(E_8\) verbietet die 126",
   Hüllensatz, Klammer-Antisymmetrisierung) entscheiden, welche Sektoren
   existieren können.
4. **Konzeptuelle Werkzeuge:** Hecke = Jones (arithmetische Operationen tragen
   Entropie, nicht Energie); relationale Teilsystem-Identität;
   Aufzeichnungsanalyse (methodisch auf Hylæan übertragbar: gleiche momentane
   Antwort ≠ gleicher Gedächtnisprozess).
5. **Forschungsinfrastruktur:** RH-Katalog (2753 Records, 405 Kills), Lean-Layer,
   Kill-Ökonomie — negative Ergebnisse sind tragend.

## 5. Drastische Effekte — ehrlicher Katalog-Befund

Pflichtabfrage vor Bewertung (Skill `rh-corpus-search`): `rhcat stats`,
`check-new`, `search`, `family`, `dossier`. Katalog-Stand: records=2753,
curated=1097; open=122, killed=319 (curated) bzw. 405 total.

### 5.1 RH

Getötete Vorläufer derselben Familie (Kill-ID, failure_class):

- **r618** STRUCTURAL_MISMATCH: „E8 data are RH-neutral" — Coxeter-/Seifert-Daten
  sind Kongruenzinvarianten; Jensen-\(C_{n,8}\) verfehlen das 30er-Wurzelgitter;
  die Jensen/\(\Xi\)-Seite ist RH-äquivalent und passt nicht.
- **TFPT.HECKE.INDEX.01** NO_BRIDGE: 4D-Wirkung abwesend; Torus-Modularfluss
  trivial bzw. modenabhängig.
- **r613** WORLD_BLIND: bei \(\varepsilon=0\) dekorativ, bei \(\varepsilon=0{,}05\)
  Residuen TRUE ~ SCRAMBLE/WPERM.
- **r604** NUMERIC_ARTIFACT: Spektrum-Nullstellen-Kreuzkorrelation \(p\approx0{,}9\).
- **PRIME.HECKEMODRAM.01** LOSSY_CONSTANT; **E8.COXETER.EULER.COMPLETION.01**
  NO_BRIDGE.

Struktureller Tiefengrund (im Fable-Paper selbst belegt): Die Solomon-Zeta des
\(E_8\)-Gitters \(\prod_{k=0}^{7}\zeta(s-k)\) enthält RH achtfach (Nullstellen bei
\(\rho+k\)) — aber das ist RESTATEMENT: ein Produkt verschobener \(\zeta\)'s ist
exakt so schwer wie \(\zeta\). Und der Hecke-Index wird per Pimsner–Popa zu
**Entropie, nicht Hamiltonoperator**. Der Raum legt Arithmetik auf die
RG-/Entropie-Seite; Hilbert–Pólya braucht sie auf der Spektralseite
(selbstadjungierter Operator, Spektrum = Nullstellen, Spurformel = explizite
Formel). Kein Operator des Raums qualifiziert sich derzeit: \(L_0\) hat konforme
Gewichte (ganzzahlig), die Clock ist endlich (3/12), \(K\) ist wegen
\(\det K<0\) nicht Markov-einbettbar, \(H_{\rm tet}\) hat ein kombinatorisches
Fünf-Niveau-Spektrum.

Lebende RH-Fronten (nicht Universalraum): WEIL_POSITIVITY_WINDOWS (40 offen),
SCREW_SUBORDINATION_LSTAR (30 offen). Eine lebendige Route bräuchte:
selbstadjungierter Operator auf natürlichem Naht-Hilbertraum + volle
Weil-Positivität über alle Stellen inkl. Tails, Testabdeckung,
Interlevel-Kompatibilität.

### 5.2 Faktorisierung

- **r647** KILLED, STRUCTURAL_MISMATCH: die zusammengesetzte \(E_8\)-Gaußsumme
  ist exakt \(S_N(t)=N^4\gcd(t,N)^4\) — **die Faktoren von \(N\) stehen exakt im
  \(E_8\)-Gitter** — aber der natürliche Baum-/Clock-Ausleseweg ist \(O(N^3)\).
  Verdict: `E8_COUNT_FACTOR_EQUIVALENT_NO_FAST_READOUT`. Information vorhanden,
  schnelle Auslesung nicht.
- Allgemein: **Kodierung ≠ Algorithmus.** Ein Faktorisierungsvorteil bräuchte
  eine physikalische Schnellauslesung eines ggT-Moments; alle Sonden starben an
  der Auslesekomplexität.
- Zusätzlich: native Prozesse sind Stabilizer/Clifford auf 4-dim Trägern →
  klassisch effizient simulierbar (Aaronson–Gottesman, Manuskript [E4]). Shor
  bräuchte Nicht-Clifford-Ressourcen + kohärente Phasenschätzung — nicht
  vorhanden.

### 5.3 P vs NP

- Manuskript: „eine neue universelle Rechenfähigkeit folgt daraus gerade nicht"
  (Stabilizer-Simulierbarkeit). Die Prozesse leben in der Gottesman–Knill-Welt;
  die Räume (8 Qubits, 256 Dimensionen, 70er-Sektor) sind winzig.
- Strukturell: P vs NP ist Worst-Case-Asymptotik — kein endliches Gerät und
  keine fixe Algebra kann sie entscheiden, höchstens Algorithmen inspirieren.
  Die Rechenstärke des Raums ist Prüfbarkeit (exakte Checks, Pins, Kill-Klassen),
  nicht Geschwindigkeit.

### 5.4 Meta-Muster der Kills

failure_class-Verteilung als Taxonomie des Overclaims: CIRCULAR (28),
LOSSY_CONSTANT (118), NO_BRIDGE (163), STRUCTURAL_MISMATCH, NUMERIC_ARTIFACT
(28), ORACLE_LEAK (5), RESTATEMENT, WORLD_BLIND, UNCONVERGED. Die drastischen
Routen wurden maschinell geprüft und mit benannter Todesursache beerdigt — das
ist die Funktion des Raums: große Behauptungen *entscheidbar* machen.

## 6. Was tatsächlich drastisch werden könnte (Rangfolge) und nächste Schritte

1. **\(c=8\)-Fixpunkt** — Kondo-Schritt \((A_3)_1\times(D_5)_1\) mit
   \(\mathbb{Z}_4\)-Glue: erste aus endlichen Postulaten abgeleitete
   Kontinuumsfeldtheorie; echte Schließung von „der Raum entsteht aus TFPT".
2. **Protonzerfall / Gauging-Fork** — empirische Entscheidung über den
   \(E_8\)-Zweig in absehbarer Zeit (Hyper-K).
3. **Superaustausch aus den \(E_8\)-Strukturkonstanten** — zweiter Ordnung über
   \((16,4)\otimes(16,\bar4)\to(1,15)+(10,6)\); Erfolg: \(\lambda\) und Graph
   abgeleitet; Kill: jede Freiheit, die \(\mathrm{Sym}^2(4)\) erlaubt. Größte
   einzelne Hebelwirkung auf T3.
4. **G1-Lift-Zeuge** — Interferenz \(1/15\) vs. \(1\), aus der Quelle entschieden.
5. **Uhrwerk** — System-Hamiltonoperator mit \(\ge4\) nutzbaren Niveaus und
   erhaltener Uhrenanzeige.
6. **G5-Grenzprozess \(N\to\infty\)** — trägt er die exakte \((3/7)^n\)-Regel,
   wird Irreversibilität abgeleitet statt angenommen; schärfere
   Vielzellen-Schranken jenseits \(1/N\).
7. **240-Bijektion** — CQ-Koordinaten ↔ \(E_8\)-Wurzeln natürlich konstruieren;
   Erfolg wäre der Fixpunktsatz (minimale autonome Beschreibung = Wurzelsystem).
   Bis dahin offen.

**Falsifikationsbedingungen der Synthese (vorab benannt):** Superaustausch lässt
\(\mathrm{Sym}^2(4)\)-Freiheit; Kondo-Kopplung erreicht \(c=8\) nicht oder ohne
\(\mathbb{Z}_4\)-Glue; kein Uhren-Hamiltonoperator der Quellklasse mit \(\ge4\)
Niveaus; G1-Zeuge entscheidet gegen die kohärente Quellform; keine natürliche
240-Bijektion.

## 7. Reproduktion der Katalog-Abfragen

```sh
python3 rh/catalog/rhcat.py stats
python3 rh/catalog/rhcat.py check-new "Universalraum als CQ-Prozess auf der
  E8-Naht: L0-/Seam-Hamiltonoperator-Spektrum als Hilbert-Pólya-Kandidat"
python3 rh/catalog/rhcat.py search 'hilbert|polya|hecke|jones|seam|naht'
python3 rh/catalog/rhcat.py family LATTICE_E8_HECKE
python3 rh/catalog/rhcat.py dossier r618 ; python3 rh/catalog/rhcat.py dossier r647
python3 rh/catalog/rhcat.py open            # Fronten: WEIL_POSITIVITY_WINDOWS, SCREW_SUBORDINATION_LSTAR
python3 rh/catalog/map/rhmap.py gaps
```

Quellprüfer der drei Grundlagendokumente: siehe deren Anhänge
(`compiler-origin-audit-20260913`, `compiler-extension-audit-20260914`,
`universalraum-inversion-20260914`, `universalraum-fable-kernfragen-20260910/fable-runde3/`).

## 8. Grenzen

Keine Aussage dieses Dokuments schließt T1–T8, bewegt einen Ledger-Marker oder
stellt einen RH-/Faktorisierungs-/P-vs-NP-Anspruch. Die Synthese (Fixpunkt-These,
Naht = Raum = Compiler) ist *bedingt*: sie organisiert exakte Teilresultate zu
einem Kandidatenbild mit benannten Gattern und Kill-Bedingungen — sie ist kein
bewiesener Abschluss. Die Zahlentriade 240 ist *offen* (Numerologie bis zur
Bijektion). Die WZW-Identifikation ist numerisch (\(n\le16\)), keine
Kontinuumskonstruktion.
