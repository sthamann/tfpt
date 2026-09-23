# GPT-5.6 Sol — Universalraum, Runde 2

Stand: 14. September 2026, 14:48 Uhr.  
Arbeitskopie für Stefan Hamann.

## 0. Aussagegrenze

Diese Datei sammelt die in der zweiten GPT-5.6-Runde gelesenen Quellen,
reproduzierten Resultate, eigenen Gegenprüfungen, Korrekturen und Antworten.

Sie ist kein begutachteter Beweis einer Theory of Everything, kein
RH-Beweis und kein neuer schneller Faktorisierungsalgorithmus. Alle
Universalraum-Arbeiten bleiben NON-RH-Experimente beziehungsweise
Theory-Contracts. Es wurde kein Marker in `verification/`, Ledger, Papers
oder Website aufgewertet.

Die Evidenztypen werden getrennt:

- **exakt:** Identität oder endlicher Beweis unter benannten Voraussetzungen;
- **numerisch:** endliche Rechnung mit Residuen und Größenangabe;
- **bedingt:** Resultat nach einer zusätzlichen Modellwahl;
- **No-go:** Gegenbeispiel oder Ausschluss innerhalb eines genau benannten
  Scopes;
- **blockiert:** das erforderliche Objekt oder die reproduzierbare Quelle
  fehlt;
- **offen:** Herkunfts-, Eindeutigkeits-, Grenzwert- oder Physikfrage.

## 1. Direkte Gesamtantwort

Die vorliegenden Probleme sind nicht vollständig gelöst. Die Runde hat aber
vier Dinge klar entschieden:

1. Der neue In-Repo-Audit ist abgeschlossen und reproduzierbar; er lief nicht
   mehr, sondern lag bereits mit Ergebnis vor.
2. Der vollständige C16-Operator vierter Ordnung und ein konservativer
   all-sector-Ausschluss tragen bei \(t/\Delta=1/640\).
3. Zwei stärkere Behauptungen tragen nicht: Die Vierfachmultiplizität ist noch
   nicht exakt bewiesen, und die bekannte globale Restschranke ist viel zu
   grob, um den Betriebswert \(t/\Delta=1/20\) zu zertifizieren.
4. RH und der neue Faktorleser sind nicht „fast gelöst“: RH ist vor dem
   Kandidatenstart durch fehlende Quellen und Review-Drift blockiert; die
   Faktor-Lane endet mit `BLOCKED_MISSING_NATIVE_COMPILER`.

Der zentrale positive Forschungsgegenstand bleibt eine feste, reversible
Mikroregel mit kohärenzverträglicher History. Der zentrale negative Satz
bleibt: P1 und P2 bestimmen diese Mikroregel nach heutigem Stand nicht
eindeutig.

## 2. Gelesener neuer Stand

Maßgebliche neue Quellen:

- `universal_room/TFPT_Universalraum_Gesamtkonstrukt_2026-09-14.md`
- `universal_room/Konsolidierte_Fortsetzung.md`
- `universal_room/README.md`
- `docs/OPEN_PROBLEMS.md`
- `experiments/theory-contracts/universalraum-paired-release-20260914/new-input-audit/`
- `experiments/theory-contracts/compiler-single-execution-20260914/`
- `experiments/theory-contracts/universalraum-fugen-20260914/`
- `experiments/theory-contracts/compiler-origin-audit-20260913/`
- RH-Katalog und RH-Research-Engine in ihrem read-only Zustand
- Faktorroute r647 und ihr lokales Ergebnisartefakt

Die beiden neuen Konsolidierungen unterscheiden sauber zwischen:

\[
\text{Algebra}
\longrightarrow \text{Mikrodynamik}
\longrightarrow \text{Zustand/History}
\longrightarrow \text{Beobachtung}
\longrightarrow \text{Physik}.
\]

Keine Zahlengleichheit ersetzt eine der Abbildungen zwischen diesen Ebenen.
Insbesondere bleiben 240 \(E_8\)-Wurzeln und 240 reelle
CQ-Koordinaten verschiedene Objekte.

## 3. Eingefrorener `new-input-audit`

Der Audit wurde vollständig aus einer temporären Kopie reproduziert, ohne
Repo-Dateien zu ändern.

### 3.1 Replay

- `check.py`: **891/891** Checks;
- Mutationsprüfung: **5/5** Mutanten gefangen;
- normal und `python -OO`: byteidentische JSON-Ausgaben;
- SHA-256 der beiden Verifikationsausgaben:
  `2786e1878523993fc1d39d8536b0c5dd2ed6ae8010c3b413a9bbdceb6859d0cb`;
- `replay.json` stimmt mit dem erneuten Lauf überein;
- `check.py` SHA-256: `a6b1ddb3…28697`;
- `singlet_f4.py` SHA-256: `cdc11708…4a721`.

### 3.2 Singulettrechnung

Der Lauf ist abgeschlossen:

- Dimension: **24.024**;
- Grundwert:
  \[
  E_{0,s}/J=11.045398337068436;
  \]
- vier numerisch gefundene erste Moden:
  \[
  E_{1,s}/J=11.56176212280258\ldots;
  \]
- maximale Residue der zwölf berechneten Zustände:
  \[
  6.882\times10^{-14};
  \]
- F4-Grundwert:
  \[
  \langle0|F_4|0\rangle=555.4885003638373;
  \]
- vier F4-Werte des ersten gefundenen Clusters:
  \[
  583.2920386663852\ldots 583.2920386663872;
  \]
- maximale Abweichung vom Referenzwert:
  \[
  7.162\times10^{-12};
  \]
- erneute Laufzeit: etwa **11,32 s**;
- Referenzlaufzeit im JSON: **10,968 s**.

Die vier offenen Flags waren korrekt:

```text
full_non_singlet_comparison = false
exact_multiplicity_upper_bound = false
higher_order_bound = false
CAR_native_phase_equivalence = false
```

## 4. History-Bug und reparierter Vertex

### 4.1 Der Fehler

Der antisymmetrische Kanal identifiziert die beiden Eingänge kohärent:

\[
K|ab\rangle=|a\wedge b\rangle,\qquad
K|ba\rangle=-|a\wedge b\rangle,
\]

und damit

\[
K^\dagger K=I-S=2P_-,
\qquad \operatorname{rank}K=6.
\]

Speichert die History dagegen orthogonal die geordneten Eingänge
\(|h_{ab}\rangle\) und \(|h_{ba}\rangle\), fällt der Kreuzterm weg. Dann gilt

\[
\widetilde K^\dagger\widetilde K=I-D_{\rm diag},
\]

der Rang steigt auf 12, die kollektive SU(4)-Invarianz geht verloren, und der
gewünschte Austausch wird nicht mehr erzeugt.

Die dynamische Folge ist konkret:

- vollständiger Vierergraph: Grundraum 24-dimensional statt
  \(\mathbb C\Omega\);
- Viererstern: 108-dimensionaler falscher Grundraum.

### 4.2 Reparaturkriterium

Für zwei Vertexabbildungen gilt:

\[
L^\dagger L=K^\dagger K
\quad\Longleftrightarrow\quad
L=VK,
\]

wobei \(V\) auf dem Bild von \(K\) isometrisch ist.

History darf damit einen kohärenten Vertexausgang erweitern, aber nicht
Eingänge unterscheiden, die \(K\) bereits bis auf Vorzeichen identifiziert.
Die Lochkonfiguration darf verschiedene Kanten markieren; das innere
geordnete Farbpaar derselben Kante darf vor der benötigten Interferenz nicht
dauerhaft orthogonal gespeichert werden.

### 4.3 Expliziter unitärer Baustein

Mit \(W=K/\sqrt2\) gilt

\[
W^\dagger W=P_-,
\qquad WW^\dagger=I_6.
\]

Eine unitäre Fortsetzung ist

\[
U_W=
\begin{pmatrix}
P_+&-W^\dagger\\
W&0
\end{pmatrix}.
\]

Der symmetrische Nicht-Ereigniszweig bleibt erhalten; die antisymmetrischen
Reihenfolgen bleiben kohärent. Die Wahl dieses Bausteins, seiner Phase,
Energie, Belegung und Steuerung ist damit noch nicht aus P1/P2 hergeleitet.

## 5. Vollständiger C16-Operator vierter Ordnung

Für das harte Referenzmodell gilt

\[
H=\Delta N_b+t(B^\dagger+B).
\]

Mit

\[
M=Q_1B^\dagger P,\qquad
N=Q_2B^\dagger Q_1,\qquad
\mathcal D=M^\dagger M,\qquad
\mathcal C=NM
\]

lautet die kanonisch normalisierte effektive Entwicklung

\[
H_{\rm eff}
=-\frac{t^2}{\Delta}\mathcal D
+\frac{t^4}{\Delta^3}
\left(\mathcal D^2-\frac12\mathcal C^\dagger\mathcal C\right)
+O(t^6/\Delta^5).
\]

Für den Clebsch-Graphen ergibt sich

\[
F_4=
2\sum_eE_e
+\sum_{\substack{e<f\\e\cap f\ne\varnothing}}\{E_e,E_f\}
-2\sum_{\substack{e<f\\r(e)=r(f)}}E_eE_fT_{ef},
\]

\[
H^{(4)}=\frac{t^4}{\Delta^3}F_4.
\]

Die drei Klassen enthalten exakt:

- 40 Einzelkanten;
- 160 überlappende Kantenpaare;
- 60 disjunkte Paare mit gleichem Vermittlertyp.

Die älteren Projektor- und Swap-Formeln sind nur dann äquivalent, wenn
Trägersektor, Einzelbondsubtraktion und die auf dem Gesamtraum nicht konstante
Projektionsverschiebung mitgeführt werden.

## 6. C16-Nachfolgervertrag und Rigor-Korrektur

Neuer Arbeitsordner:

`experiments/theory-contracts/universalraum-parallel-closure-20260914/`

Enthalten:

- `README.md`
- `source_manifest.json`
- `c16_parallel_closure.py`
- `run_checks.py`
- `validation.json`
- `validation_optimized.json`
- `replay.json`

### 6.1 Reproduktionsstand

- **24** Checks;
- **6/6** Mutanten gefangen;
- normal und `-OO` byteidentisch;
- Laufzeit beider Prüfläufe zusammen: **66,64 s**;
- keine T1–T8-Promotion.

### 6.2 Korrekte F4-Norm

Eine erste Implementierung verwendete für überlappende Antikommutatoren
versehentlich Norm 4. Korrekt ist

\[
\|E_e\|=2,\qquad
\|\{E_e,E_f\}\|\le 2\|E_e\|\|E_f\|=8.
\]

Daher gilt auf dem vollen Raum

\[
\boxed{
\|F_4\|
\le40\cdot4+160\cdot8+60\cdot8
=1920.
}
\]

Der frühere Wert 1280 wurde verworfen.

### 6.3 All-sector-Ausschluss bei \(t/\Delta=1/640\)

Die gepinnte H-only-Rechnung enthält alle 64 SU(4)-Sektoren. Der niedrigste
Nichtsingulettwert liegt im Sektor \((5,4,4,3)\):

\[
E_{\rm ns}/J=12.133537149348086.
\]

Mit der konservativen Vollraumnorm und

\[
\epsilon^2=(1/640)^2
\]

bleibt nach der F4-Korrektur die Reserve

\[
\boxed{
\mathrm{margin}=1.0787638122797003\,J>0.
}
\]

Damit ist der Nichtsingulett-Ausschluss im benannten vierten-Ordnungsmodell
bei \(t/\Delta=1/640\) rigoros. Es wurde dafür kein kompletter neuer
F4-Lanczoslauf über alle 64 Sektoren benötigt; benutzt werden die gepinnten
H-only-Minima und eine Vollraum-Operatornorm.

### 6.4 Vierfachmultiplizität bleibt numerisch

Die erste Version des Nachfolgervertrags typisierte einen numerischen
\(W(D_5)\)-Charaktertest zu stark als exakten Multiplizitätsbeweis. Das wurde
korrigiert.

Richtig ist:

- \(|\operatorname{Aut}(\Gamma_{\rm Cl})|=1920\) ist exakt;
- der gefundene vierdimensionale Lanczos-Raum ist numerisch invariant;
- sein numerischer Charakter erfüllt
  \[
  \frac1{|G|}\sum_g\chi(g)^2\approx1;
  \]
- dies stützt einen irreduziblen 4-Raum;
- es beweist weder einen exakten Eigenprojektor noch den Ausschluss weiterer
  exakt gleicher Eigenvektoren.

Ein zweiter Ansatz über die \(W(D_5)\)-Isotypen zeigt zudem, dass die
4-dimensionalen Typen mehrfach im großen Specht-Raum vorkommen. Schurs Lemma
erzwingt daher nicht, dass der gesamte Eigenraum genau Dimension vier hat.

Korrektes Flag:

```text
symmetry_supported_irrep_dimension_four = true
exact_first_level_multiplicity = false
```

Benötigt wird ein exakter Eigenprojektor, ein Minimalpolynom- oder ein
zertifizierter Inertia-Nachweis.

### 6.5 Sechste Ordnung

Der geschlossene 544-dimensionale Sternblock zeigt:

- exakter mikroskopischer Gap bei \(t/\Delta=1/20\):
  \[
  0.00243396875136\ldots;
  \]
- Clusterkoeffizienten:
  \[
  c_4/\Delta=-2,\qquad c_6/\Delta=8;
  \]
- numerisches Verhältnis sechste/vierte Ordnung bei \(1/20\):
  \[
  0.02.
  \]

Das ist ein Blockresultat, keine globale C16-Restschranke.

Ein zweiter analytischer Versuch liefert zwar einen Kato–Cauchy-Rest im
Konvergenzkreis

\[
|t|<\Delta/320,
\]

aber die beste daraus ableitbare Größenordnung liegt am Arbeitspunkt
\(t/\Delta=1/640\) bei ungefähr

\[
3200\,J,
\]

also weit über der all-sector-Reserve \(1.0788J\). Die Schranke ist wahr,
aber nutzlos. Eine brauchbare Grenze verlangt eine wesentlich schärfere
globale Norm oder eine vollständige kombinatorische Pfadklassifikation
sechster Ordnung.

Korrektes Flag:

```text
numerical_block_t6_scaling_544 = true
global_t6_bound = false
```

Nach zwei ernsthaften Ansätzen wurde diese Beweislücke nicht weiter
„grün gerechnet“.

## 7. Angekleideter Stern und Präparation

Für den isolierten mikroskopischen Viererstern ist der erreichbare Block
544-dimensional. Seine allordentliche effektive Matrix lautet

\[
H_{\star,\rm eff}^{\rm mic}
=\frac{\Delta I-\sqrt{\Delta^2I+4t^2(6I-2G_\star)}}2.
\]

Der Grundzustand ist angekleidet. Bei \(t/\Delta=0.05\) beträgt das nackte
Gewicht

\[
0.9856429311786321.
\]

Darum ist der ideale Achtpunktfilter des nackten Tetramers kein exakter
Filter des mikroskopischen Spektrums. Die relevanten Wurzelabstände sind
nicht kommensurabel. Benötigt werden:

1. ein an das angekleidete Spektrum angepasster Filter;
2. eine kontrollierte Entkleidung; oder
3. eine explizite Näherungs- und Fehleranalyse.

Eine angepasste Verstärkungsphase existiert im endlichen Modell. Ihre
physikalische Steuerbarkeit und Herkunft bleiben Zusatzannahmen.

## 8. U-Auswahl und Phasenadapter

### 8.1 Was bereits exakt feststeht

- Der History-Gram muss erhalten bleiben.
- Ein kohärenter 22-dimensionaler Vertexbaustein existiert.
- Das gemeinsame endliche Laborprotokoll kann Präparation, Record und Echo in
  einem größeren unitären Clock-Operator organisieren.
- Der Austauschrecord ist in der benannten Qubitkodierung nicht Clifford.
- P1/P2 enthalten keine Auswahl von Belegung, \(t\), \(\Delta\), History,
  Mediatorlokalität, Anfangszustand oder Zugriffen.

### 8.2 Nichtidentifizierbarkeit

Schon die Familie

\[
U_\theta=
\begin{pmatrix}
P_++\cos\theta\,P_-&-\sin\theta\,W^\dagger\\
\sin\theta\,W&\cos\theta I_6
\end{pmatrix}
\]

enthält verschiedene unitäre Realisierungen derselben lokalen
Vertexgrammatik. Unterschiedliche \(\theta\) erzeugen verschiedene
Übergangswahrscheinlichkeiten und Spektren.

Damit ist die Abbildung

\[
\text{Mikrorealisierung}\longrightarrow\text{P1/P2-Compiler-Schatten}
\]

nicht injektiv, solange keine zusätzlichen Auswahlaxiome eingeführt werden.

Mindestens nötig wären:

- `A_hist`: kohärenzverträgliche isometrische History;
- `A_occ`: Belegungs- und Statistikregel;
- `A_med`: lokale/extensive Vermittlerarchitektur;
- `A_phase`: nativer Phasenadapter;
- `A_state`: Anfangs- und Reservoirzustand;
- gegebenenfalls `A_single`: Auswahl eines bestimmten \(\theta\).

### 8.3 Phasenadapter

Der U-/Phasen-Audit ist abgeschlossen:

- **24/24** exakte Checks;
- **6/6** Mutanten gefangen;
- normal und `-OO` byteidentisch;
- Laufzeit etwa **2,88 s**;
- Checker-SHA-256:
  `da9e9e257032d700b9cc366bfaf117bd0e2dcfe267dfb5b97a5680596dfe5996`.

Er bestätigt:

\[
K^\dagger K=I-S,\qquad \operatorname{rank}K=6,
\]

\[
L^\dagger L=I-D_{\rm diag},\qquad \operatorname{rank}L=12
\]

für die falsche geordnete History sowie den
\(\eta\)-Interpolationssatz

\[
G_\eta=I-\eta S-(1-\eta)D_{\rm diag}.
\]

Alle 40 Clebsch-Kanten tragen dieselbe lokale antisymmetrische
Gramregel. Der falsche History-Operator reproduziert die Grundraumdimensionen
24 auf \(K_4\) und 108 auf dem Stern.

Der Nichtinjektivitätszeuge ist ebenfalls exakt. Zwei unitäre
22D-Vervollständigungen \(U_0\) und \(U_i\) besitzen für den gewählten
Eingang dieselbe erste grobe Materie-/Vermittler-Auslesung, aber
orthogonale Zwei-Schritt-Ausgänge:

\[
|\langle U_0^2\psi,U_i^2\psi\rangle|^2=0.
\]

Auch ihre Spektren unterscheiden sich:

```text
U0: {-1, 1}
Ui: {-1, 1, i}
```

Das beweist die Unterbestimmung der globalen unitären Vervollständigung durch
die gepinnten lokalen Gramdaten. Es ist kein Satz, dass jede denkbare
Verstärkung von P1/P2 nicht eindeutig sein könne.

Der native Phasenadapter ist weiterhin nicht geschlossen:

```text
phase_adapter_verdict = BLOCKED_MISSING_NATIVE_PHASE_DATA
CAR_native_phase_equivalence = false
cycle_holonomy_comparator_ran = false
```

Die vorhandenen Quellen liefern:

- 240 phasenmarkierte Gaussian-\(E_8\)-Wurzelvektoren;
- Quell-Paulis und die Clock-Normalisierung;
- Wurzeltypen und \(|N_{\alpha\beta}|=1\);
- eine positive CAR-Kantenkonvention im Referenzmodell.

Es fehlt jedoch eine vollständige native Tabelle der signierten oder
komplexen \(E_8\)-Strukturkonstanten in genau derselben Basis wie der
CAR-Focklift. Ohne diese Daten kann keine ehrliche Zyklenholonomie zwischen
„native“ und „CAR“ verglichen werden.

Zieltest:

1. Kantenmatrizen in gemeinsamer Basis;
2. kanalweise Gauge-Freiheit bestimmen;
3. Holonomien aller Clebsch-Zyklen vergleichen;
4. denselben Adapter auf den F4-Operator anwenden;
5. jede verbleibende Cocycle-Klasse als harten Mismatch ausgeben.

Die Blockade gilt für die **gepinnten Adapter**. Sie ist kein Beweis, dass
eine signierte Phasentabelle nirgendwo im gesamten Repository oder in einer
zukünftigen Konstruktion existieren kann. Es wurden ausdrücklich keine
fehlenden Vorzeichen als \(+1\) geraten.

## 9. Vermittlerlokalität

Zwei Modelle müssen getrennt werden.

### Modell G: global geteilte Moden

Ein einziger Satz von 60 Bosonmoden wird von sämtlichen replizierten
C16-Zellen geteilt. Dadurch können weit entfernte Zellen ohne lokalen
Transportkanal über denselben Modus gekoppelt werden. Ohne zusätzliche
Normierung drohen nicht-extensive \(O(N^2)\)-Beiträge und keine
endliche Lieb–Robinson-Geschwindigkeit.

### Modell L: lokale Moden

Jede Zelle besitzt lokale Vermittlermoden; zwischen Zellen gibt es nur
explizite endlichreichweitige Hop-Terme. Dann kann ein lokaler
Lieb–Robinson-Kegel formuliert und eine extensive Energie erwartet werden.

Entscheidungstest für \(N=2,3,4\):

- Skalierung von \(E_N-NE_1\);
- Stabilität von \(E_N/N\);
- Norm pro Zelle;
- Kommutatorausbreitung entfernter lokaler Observablen;
- explizite Transportreichweite und Geschwindigkeit.

Dieser Test war zum Zeitpunkt dieser Rundenakte noch nicht ausgeführt.

## 10. RH-Lane

### 10.1 Infrastrukturstatus

Der regelkonforme Startcheck endet mit Exitcode 1:

```text
SOURCE_UNAVAILABLE
PAPER_SOURCE_OR_REVIEW_DRIFT
```

Fehlender Hauptpfad:

`/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/research`

Weitere in `source_scope.json` gepinnte Bäume unter
`2026-09-10/scha/work/...` fehlen ebenfalls.

Der Paper-/Review-Export ist zusätzlich veraltet:

- zwei Submissionen sind im Repo, aber nicht im Export;
- zwei neue Root-TeX-Dateien sind unreviewed;
- fünf gepinnte TeX-Hashes sind gedriftet.

Es wurde deshalb korrekt **kein** RH-Kandidat angelegt, kein `cycle`
ausgeführt, kein Pin geändert und kein Ergebnis registriert.

### 10.2 Nächster RH-Vertrag

Der sinnvolle Zielvertrag bleibt

\[
Q_\zeta(g)=\|Ag\|^2
\]

für alle \(g\) im vollständigen vorgeschriebenen Testraum, mit unabhängig
definiertem \(A\), vollständiger signierter Weil-Form, allen Stellen,
Randtermen, Involution und Interlevel-Kompatibilität.

Nahe bekannte Kills:

- r404: `RESTATEMENT` — Cholesky einer bereits positiv angenommenen Matrix;
- r444: `CIRCULAR`;
- All-Place-Audit: `NO_BRIDGE`;
- r623/r394: `STRUCTURAL_MISMATCH`.

Ein zulässiger endlicher Kandidat müsste kofinale Blöcke \(T_n\) und
Operatoren \(A_n\) liefern mit

\[
W_n(g)=\|A_ng\|^2,
\qquad
A_{n+1}\iota_n=\iota'_nA_n,
\]

sowie der korrekten Schur-Bildbedingung bei singulären Blöcken.

Solange die gepinnten Quellen nicht wieder verfügbar und die gedrifteten
Papers nicht neu reviewt sind, ist dieser Ast blockiert. Eine Scope- oder
Pinänderung nur zum Grünmachen wäre unzulässig.

## 11. Faktorisierungs-Lane

Neuer Arbeitsordner:

`experiments/theory-contracts/f4-modular-period-readout-20260914/`

Enthalten:

- `README.md`
- `source_manifest.json`
- `checker.py`
- `validation.json`
- `validation_optimized.json`
- `replay.json`

### 11.1 Reproduktion

- **33** Checks;
- **5/5** Mutanten gefangen;
- normal und `-OO` byteidentisch;
- Verdict:
  ```text
  BLOCKED_MISSING_NATIVE_COMPILER
  ```
- `native_modmul_compiler=false`;
- `compiled_primitive_count_from_audit=0`.

### 11.2 Toy-Ergebnisse

Für \(N=15\), \(a=7\):

\[
\operatorname{ord}_{15}(7)=4,
\]

und die übliche Periodennachverarbeitung liefert die Faktoren 3 und 5.

Für \(N=35\) ist der zunächst genannte Wert \(a=7\) **nicht** teilerfremd:

\[
\gcd(7,35)=7.
\]

Er liefert bereits klassisch einen Faktor und definiert keine
Mod-Mul-Permutation. Der korrigierte Periodentest verwendet \(a=3\):

\[
\operatorname{ord}_{35}(3)=12,
\]

mit Faktoren 5 und 7.

Die expliziten Tabellen sind nur
`ORACLE_SPECIFICATION`, keine native Kompilation. Die materialisierte
One-Hot-Darstellung hätte 225 beziehungsweise 1225 Bits. Das ist
**keine** untere Schranke für reversible modulare Arithmetik; die kompakte
Regel \((N,a):y\mapsto ay\bmod N\) ist klassisch kurz beschreibbar.

### 11.3 Warum kein neuer Algorithmus vorliegt

Der geprüfte Universalraum-Adapter stellt feste Blöcke mit Dimensionen
256, 544, 832 und 6656 bereit. Er enthält keine \(N\)-skalierende
Registerfamilie, keinen kontrollierten modularen Multiplizierer und keine
skalierende QFT-Schnittstelle.

Die bereits getöteten Wege bleiben:

- \(O(N)\) ggT-Momentgewinnung;
- \(O(N^3)\) E8-Baumkontraktion;
- gleichverteilte E8-Fourierauslesung bei teilerfremdem Takt;
- \(N^{1/4}\)-Klasse nach unstrukturierter Verstärkung seltener Takte.

Das Ergebnis ist ein Blocker des **vorliegenden Interfaces**, keine
universelle Schaltkreis-Untergrenze. Eine zukünftige positive Lane müsste
einen nativen, reproduzierbaren `poly(log N)`-Compiler liefern. Wird dabei
nur Shors modulare Exponentiation implementiert, ist das eine
Implementierungsleistung, kein neuer Faktorisierungsalgorithmus.

## 12. T1–T8 nach Runde 2

### T1 — Quelle

**Zugewinn:** kohärenzverträglicher Vertex, unitäre Ausführung,
P1/P2-Nichtidentifizierbarkeit als explizite Faser von Realisierungen.

**Offen:** native Auswahl von Belegung, Statistik, Parametern, History,
Mediatorlokalität, Zustand und Zugriffen.

### T2 — chirale \(E_8\)-Naht

**Zugewinn:** korrekte algebraische Grade und klare Trennung von
Gitter-VOA und physischem Skalierungsgrenzwert.

**Offen:** nativer phasentreuer Bulk/Rand-Adapter mit Domänen,
Korrelatoren, Level und Chiralität aus derselben Mikroregel.

### T3 — 3+1D und gemeinsamer Kegel

**Zugewinn:** Vermittlerlokalität als konkrete Modellgabel.

**Offen:** gewählte lokale Vielzellenfamilie, thermodynamischer Impulsraum,
tatsächliche Pole und gemeinsamer Lorentz-RG-Fluss mehrerer Sektoren.

### T4 — chirales Standardmodell

**Zugewinn:** Spin(10)-Belegungsobstruktion und falsche Familienzählformeln
sind klar getrennt.

**Offen:** interner Diracoperator mit drei propagierenden Familien,
Spiegelentkopplung und konsistentem fermionischem Maß.

### T5 — Wechselwirkung und Kontinuum

**Zugewinn:** vollständiger C16-F4-Operator, 64-Sektor-Ausschluss bei
\(1/640\), exakter Sternblock.

**Offen:** exakte Quartettmultiplizität, globale Restschranke, Betriebswert
\(1/20\), lokale Vermittlerwahl und Kontinuumsgrenzwert.

### T6 — Kopplungen und Massen

**Zugewinn:** historische Werte und Spannungen bleiben in einem
Transfer-/Unsicherheitsvertrag sichtbar.

**Offen:** Herleitung von Kopplungen, Yukawas, Neutrinos und Skala aus dem
gleichen Vakuum, mit Theorieunsicherheiten und eindeutigem Schema.

### T7 — Gravitation

**Zugewinn:** Kinematik, Spin-2-Existenz und universelle Kopplung werden
nicht mehr vermischt.

**Offen:** positiver masseloser Spin-2-Pol, zwei Helizitäten,
Ward-Identitäten, Einstein-Grenzwert und universelle Kopplung aus einem
abgeleiteten Korrelator.

### T8 — Zustand und Funktional

**Zugewinn:** endliche Präparation, Echo und ein expliziter bedingter
Relaxationskanal.

**Offen:** Herkunft von Reservoir, Anfangszustand, Zugriffsrechten,
Born-Regel und kosmologischem Funktional.

Alle acht Tore bleiben offen.

## 13. Finale Querfragen

Diese Fragen sind derzeit nicht unabhängig ausführbar:

- **Dunkle Materie:** braucht mindestens T4, T7 und einen Produktionszustand
  aus T8.
- **Dunkle Energie:** braucht eine effektive gravitative Vakuumwirkung,
  Zustandsgleichung und radiative Stabilität aus T6/T7.
- **Baryogenese:** braucht chirale Materie, CP-Verletzung,
  Nichtgleichgewicht und Anfangszustand aus T4/T5/T8.
- **Starkes CP:** braucht das tatsächliche fermionische Maß,
  Quarkmassenphasen und Renormierung aus T4/T6.
- **Schwarze Löcher:** brauchen zuerst einen quantisierten
  Gravitationssektor aus T7.

Ein ungelesenes Register, ein Faktor \(8\pi\), ein Lorentzkegel oder eine
passende Entropiezahl löst keine dieser Aufgaben.

## 14. Aktueller Maschinenstatus

### Grün

- `new-input-audit`: 891 Checks, 5 Mutanten;
- C16-Nachfolger: 24 Checks, 6 Mutanten;
- U-/Phasen-Audit: 24 Checks, 6 Mutanten;
- Faktorvertrag: 33 Checks, 5 Mutanten;
- normal/`-OO` jeweils byteidentisch.

### Scoped positiv

- vollständiger F4-Operator;
- Singulett-F4-Korrektur;
- all-sector-Ausschluss bei \(t/\Delta=1/640\);
- kohärenzverträglicher lokaler Vertex;
- expliziter Nichtinjektivitätszeuge für unitäre Vervollständigungen;
- deterministische ideale Präparation unter benannten Kontrollen;
- exakte Toy-Perioden bei \(N=15,35\).

### Scoped negativ oder blockiert

- exakte Quartettmultiplizität nicht bewiesen;
- globale C16-Restschranke nicht nützlich;
- \(t/\Delta=1/20\) nicht global zertifiziert;
- CAR/native Phasenadapter offen;
- Vermittlerlokalität noch nicht entschieden;
- RH vor Kandidatenstart blockiert;
- kein nativer modularer Compiler;
- keine T1–T8-Schließung.

## 15. Nächste überprüfbare Arbeiten

1. Die fehlende native signierte \(E_8\)-Klammerphasentabelle in derselben
   Basis wie den CAR-Focklift bereitstellen oder herleiten; erst dann den
   Zyklenholonomie-Vergleich starten.
2. Globale und lokale Vermittlerfamilien für \(N=2,3,4\) auf Extensivität
   und Kommutatorausbreitung vergleichen.
3. Einen exakten Eigenprojektor- oder Inertia-Nachweis für die
   Vierfachmultiplizität suchen; nach der bereits erreichten
   Zwei-Versuche-Stop-Regel ist dafür ein wirklich neuer mathematischer
   Ansatz erforderlich.
4. Eine kombinatorische sechste-Ordnungs-Pfadklassifikation oder eine
   wesentlich schärfere lokale Schrieffer–Wolff-Schranke entwickeln.
5. Die fehlenden RH-Quellbäume wiederherstellen und die gedrifteten Papers
   neu reviewen, bevor ein Weil-Block-Kandidat registriert wird.
6. Für Faktorisierung nur dann weiterarbeiten, wenn eine echte
   \(N\)-skalierende native Gatefamilie angegeben wird.

## 16. Schluss

Der größte Fortschritt dieser Runde ist nicht eine behauptete Weltformel,
sondern eine schärfere Trennung:

\[
\boxed{
\text{endliche konsistente Ausführung}
\ne
\text{native eindeutige Quelle}
\ne
\text{skalierende Physik}
\ne
\text{RH oder schneller Faktorleser}.
}
\]

Der C16-Kern ist wesentlich besser kontrolliert als zuvor. Die offenen
Stellen sind jetzt konkrete Beweisobjekte: exakter Spektralprojektor,
sechste-Ordnungs-Rest, native Phase, lokale Vermittlerfamilie,
Vielzellenpropagator, chiraler Diracoperator, Spin-2-Korrelator und
Quellfunktional. Solange diese Objekte fehlen, bleibt die richtige
wissenschaftliche Antwort „teilweise geschlossen und präzise
falsifizierbar“, nicht „vollständig gelöst“.
