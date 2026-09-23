# Unabhängiger Quellenaudit: Rotor oder natives Fock-W als Herkunftspfad?

**Stand:** 20. September 2026  
**Urteil:** **PARTIAL / erster zu prüfender Pfad: natives Fock-W.**  
**Strenge Herkunftsaussage:** Gegenwärtig wählt **keine** der beiden Quellen die zehnkanalige Boundary-Wechselwirkung, den Energiepunkt `Vc` oder einen nichtverschwindenden Koeffizienten von `V_n+V_{-n}` aus. Das native W-Modell ist jedoch der einzige der beiden Kandidaten, bei dem die relevante Nicht-Gauß-Struktur schon als tatsächlicher Hamiltonterm mit festgelegter Zeitentwicklung implementiert ist. Der Rotor liefert eine exakt hergeleitete quartische **Kommutatorkomponente**, noch keinen solchen Term im effektiven Hamiltonian. Deshalb ist W der begründet erste Herkunftspfad. Der erste Test muss aber schon bei der **gemeinsamen Gruppen- und Feldwirkung** ansetzen: der 64er Fockträger ist unter den tatsächlichen E8-`C/J`-Clocks nicht abgeschlossen. Das ist eine Priorisierung für einen Ausschlusstest, keine Identifikation mit der Boundary-Theorie.

## Nachtrag der Hauptprüfung: der priorisierte Gate ist jetzt entschieden

Nach diesem unabhängigen Vergleich wurde der priorisierte erste W-Gate tatsächlich geprüft. [Der Familien-/Zentrumtest](../family_intertwiner/PROOF.md) zeigt: Das diagonale zentrale Element wirkt auf allen 64 nativen Fermion- und allen 60 Bosonmoden trivial, auf jedem ungeraden lokalen Feld des gemeinsamen T-Randgitters dagegen mit Minuszeichen. Daher scheitert bei unveränderter vollständiger Gruppenwirkung sogar jeder nichtlineare equivarianten Transfer dieses ungeraden Feldbeins. Der weiter unten formulierte Operator-/Zeit-Gate ist **für diesen unveränderten Kandidaten bereits an Voraussetzung1 gescheitert**. Er ist kein noch ausstehender RG-Optimierungsauftrag.

Der unmittelbar anschließende Originaltest fand die sechs Clifford-Übergänge `6 tensor bar4 -> 4` vor der Familienprojektion. In der wirklich exportierten geraden Familienkompression verschwinden die einzelnen Übergänge vollständig. Ihr Ort ist damit identifiziert; ihre Beförderung zu graduierten physikalischen Feldern samt Wechselwirkung wäre eine zusätzliche Herkunftsherleitung. Dieser Nachtrag stammt aus der Hauptprüfung; der ursprüngliche unabhängige Review beansprucht diese spätere Verstärkung nicht als eigene Prüfung.

**Zusätzlicher korrigierender Rotor-Folgetest:** Die elektrische Lücke ist nicht die vollständige Quelle. Die originale High-Masse4 liefert im vollständigen Gauß-neutralen Ein-Kantenraum eine kontrollierte Rang-eins-Spektralreduktion (E*=0.01996381…0.01996382, Fastanteil-Verhältnis<1/4000). Diese neue positive Aussage ersetzt jeden pauschalen Ausschluss gemeinsamer Rotor-/High-Elimination. Der verbleibende eindimensionale Block enthält aber keine freie Low-Feldalgebra und liefert keinen unabhängigen Quartik-Koeffizienten. Siehe den aktualisierten Rotorbeweis, Abschnitt3b.

## 1. Entscheidungsfrage und Abbruchkriterium

Geprüft wurde nur:

> Welche bereits vorhandene Nicht-Gauß-Quelle besitzt genügend echte Operator- und Dynamikstruktur, um als erster Kandidat für die Herkunft der bedingten zehnkanaligen Wechselwirkung geprüft zu werden?

Nicht geprüft oder neu konstruiert wurden ein weiteres Parentmodell, ein Ising-Phasendiagramm oder neue Kopplungen. Gleiche Spektren, gleiche Dimensionszahlen oder eine bloße Unterraumisomorphie gelten nicht als Herkunftsabbildung. Ein Kandidat scheidet als unmittelbarer Herkunftspfad aus, wenn seine gesuchte Nicht-Gauß-Struktur nicht Teil der ausgeführten Dynamik ist oder kein typisierter lokaler Operator-/Zeit-Intertwiner zur Boundary-Algebra angegeben werden kann.

Die Codeentdeckung begann wie vorgeschrieben im aktuellen Theoriegraphen. Er fand die Rotor-Provenienzfunktionen im Vertrag `clock-interaction-provenance`; die nativen W-Quellen waren dort nicht hinreichend erschlossen. Für die gepinnten Markdown-, Tensor- und Prüferquellen wurde deshalb gezielt auf die Originaldateien zurückgegriffen.

## 2. Was die Boundary verlangt

Der bedingte Randvertrag ist

\[
\Gamma=\mathbb Z^{10},\qquad K=\operatorname{diag}(1^9,-1),
\]

mit

\[
n=(1,1,1,-1,-1,-1,-1,-1,-1,3),\qquad z=e_9-e_{10}.
\]

Die vorhandene QWZ-/CAR-Quelle ist quadratisch. Reguläres gaußsches Eliminieren bleibt quadratisch und erzeugt weder einen Vierfermion- noch einen Zwölffermion-Hamiltonterm (`source-dynamics-selection`, Zeilen 6–28). In den ursprünglichen lokalen Fermionkoordinaten benötigt `n` zwölf elementare Fermionfaktoren und drei Ableitungen; niedrigere echte Wechselwirkungen dürften diesen Operator prinzipiell im RG erzeugen, die freie Quelle tut es aber nicht (Zeilen 217–235). `z` ist dagegen der einzige neutrale primitive bilineare Nullvektor im angegebenen Wörterbuch, doch Zulässigkeit setzt keinen Koeffizienten (Zeilen 237–243).

Das Herkunftsproblem lautet daher: Welche vorhandene Nicht-Gauß-Dynamik kann über eine **gemeinsame lokale Operator-, Ladungs-, Zustands- und Zeitabbildung** einen nichtverschwindenden Wilson-/OPE-Koeffizienten im `n`-Kanal erzeugen und zugleich den `z`-Kanal kontrollieren? Die bisherigen Werte `Vc` und `g_n=\pm g_z` sind diagnostische Setzungen, keine Quellausgabe.

## 3. Rotorpfad: echter Ursprung eines Quartik-Kommutators, aber noch kein Wechselwirkungsterm

Der kompakte U(1)-Parent besitzt eine wirkliche Rotorzeitentwicklung. Auf einem vorhandenen Link gelten

\[
[E,U]=U,\qquad H_E=\frac\kappa2E^2,\qquad
V=a(Uc_1^\dagger c_0+U^\dagger c_0^\dagger c_1),
\]

mit `a=1/12`, `kappa=1/100`. Aus den originalen Parenttermen folgt exakt

\[
[V,[H_E,V]]
=\kappa a^2\bigl[n_0+n_1-2n_0n_1+2E(n_0-n_1)\bigr],
\]

also die reine quartische Komponente

\[
-2\kappa a^2q_0q_1=-\frac1{7200}q_0q_1.
\]

Der vorhandene Prüfer rechnet dies auf allen 16 Fockmasken der vier tatsächlichen L/H-Moden und bei symbolischem beliebigem ganzzahligem Fluss nach; auch die Projektion des vollständigen ursprünglichen Kantenhoppings behält den Koeffizienten (`clock-interaction-provenance`, README Zeilen 132–173; Checker Zeilen 118–166).

Das ist ein positiver Herkunftsnachweis: Der Grad-4-Anteil wurde nicht von Hand als freie Vierfermion-Kopplung eingesetzt. Er entsteht, weil elektrische Rotoroperatoren nichtzentral mit dem Hopping wechselwirken. Round 43 gibt für den fixierten Parent eine starke Zeitentwicklung und eine exakte Darstellung des Materiezweigs für endliche Zeiten an (`MATTER_RESUMMATION.md`, Zeilen 9–66).

Für die aktuelle Auswahlfrage reicht dies nicht. Der quartische Ausdruck ist ein Term in einem doppelten Kommutator. Ohne festgelegtes Magnus-/Floquet-/Kontrollprotokoll oder kontrollierte Rotor-Elimination ist er **kein** Term eines hergeleiteten statischen effektiven Hamiltonians. Koeffizient im Effektivgenerator, Zeitordnung, Gaussreduktion und Zustand sind offen (`clock-interaction-provenance`, Zeilen 175–180). Außerdem lebt der Zeuge auf vier komplexen L/H-Moden an zwei Gitterpunkten plus unendlichem Rotor; eine Abbildung auf die zehn chiralen Boundary-Kanäle samt `q,Y`, Glue, `n,z`, Adjungiertem und physischer Zeit fehlt (Zeilen 182–187). Selbst der Parent ist ein deklarierter Kandidat und nicht eindeutig aus den TFPT-Axiomen ausgewählt.

**Rotor-Verdikt:** exakte Nicht-Gauß-Herkunftskante und echte Parent-Zeitentwicklung, aber die relevante Quartik ist bislang nur ein Kommutatorzeuge. Als unmittelbare Quelle der Boundary-Wechselwirkung ist der Pfad deshalb einen zusätzlichen Dynamikschritt und einen großen Typisierungsschritt entfernt.

## 4. Nativer Fock-W-Pfad: wirklicher Nicht-Gauß-Hamiltonian, aber noch ohne lokalen Randtransfer

Im nativen Modell ist die Kopplung selbst Teil des Hamiltonoperators:

\[
H_W=\Delta N_b+g\sum_{A=1}^{60}
\left(b_A^\dagger P_A+P_A^\dagger b_A\right),\qquad
P_A=\sum_{i<j}W_{A,ij}f_jf_i,
\]

\[
N=N_f+2N_b,\qquad WW^{\mathsf T}=8I_{60}.
\]

Dies ist auf dem kombinierten Fermion-Boson-Fockraum nichtgaußsch: jeder Wechselwirkungsterm koppelt einen Vermittler an ein Fermionpaar. Anders als beim Rotor-Kommutator ist kein zusätzliches Protokoll nötig, um diese Kopplung in den Zeitgenerator zu bringen. Die vorhandenen Krylov-, Sektor- und Antwortrechnungen wenden genau diesen Hamiltonvertrag an; `native_ground_state.py` implementiert die Erzeugungs-/Vernichtungsoperationen und baut `H=Delta*diag+g*offdiag` im fixierten Sektor.

Der strukturelle Anteil von W ist stark gepinnt:

- 64 Fermionmoden, 60 Bosonkanäle;
- pro Kanal acht disjunkte Fermionpaare, insgesamt 480 signierte Kanten;
- exakte Gewichtserhaltung auf allen 480 Kanten;
- `WW^T=8I_60`;
- exakte Spin(10)×SU(4)-Kovarianz und ein intern gewählter kovarianter Lift mit `W Λ²G_F=G_BW`.

Diese Aussagen folgen aus dem gepinnten Tensor mit SHA-256 `3f00a0892157a691e4ef26920c3702772c7bf76a250fad98ff04a079bb64b763` und werden in `common.py` geprüft (Zeilen 1–15, 28–75, 246–269). Das integrierte v1.6-Dokument rekonstruiert zusätzlich die Casimir-Identität auf allen 2016 Zweifermionzuständen und zeigt explizit, dass die signierte Kopplung nicht durch Beträge ersetzt werden darf (`update_body_v16.tex`, Zeilen 62–79, 99–106). Die Nicht-Gauß-Antwort ist daher kein Artefakt einer bloßen Majorana-Kovarianz.

Der in `common.py` geprüfte Lift darf dabei nicht mit der vollständigen vorzeichenrichtigen E8-Clockwirkung verwechselt werden. Der direkte Zensus der tatsächlichen `C_clk`- und `J_clk`-Permutationen zeigt, dass der native Träger `FW64` nicht invariant ist:

| tatsächliche E8-Clock | bleibt in `FW64` | geht in ganzzahlige D8-Wurzeln | geht in andere `s`-Halbwurzeln |
|---|---:|---:|---:|
| `C_clk` | 21 | 28 | 15 |
| `J_clk` | 32 | 0 | 32 |

Der gemeinsame `C/J`-Abschluss benötigt die volle 240-Wurzel-Quellalgebra. Damit ist `W Λ²G_F=G_BW` eine exakte Kovarianzaussage für den dort gewählten internen Spin(10)×SU(4)-Lift, aber noch kein Beweis, dass W die tatsächliche E8-`C/J`-Wirkung oder den lokalen `c`-Zweig transportiert. Auch eine vermeintlich „familienreine“ Fortsetzung ist unter dem festgehaltenen Produktgruppenwörterbuch nicht kostenlos: ein komplex-linearer SU(4)-Z4-Intertwiner und ein global antilinearer Spin(10)-Z4-Intertwiner scheitern. Eine bloße Konjugation auf einem Faktor des komplexen Tensorprodukts ist ohne zusätzliche reelle Struktur kein wohldefinierter Quelloperator. Insbesondere gibt es keine einfache native Abbildung `FW64→c`, auf der der Zeit-/RG-Test schon aufbauen könnte.

Aber auch hier muss „implementiert“ von „fundamental ausgewählt“ getrennt werden:

1. Die Algebra liefert den signierten Tensor W und seine Symmetrieeigenschaften. Die Beförderung zu genau dem Boson-Fermion-Hamiltonian sowie `Delta`, `g`, der Sektor und gegebenenfalls `mu N` sind Modellvertrag beziehungsweise Zustandswahl; sie sind nicht aus P1/P2 hergeleitet.
2. Es gibt keinen hergeleiteten räumlichen Träger. Ein Modenindex ist kein Raumpunkt (`RESULTS.md`, Zeilen 244–261); T3 bleibt offen (Zeilen 282–293).
3. Es gibt kein einheitliches Lorentz-Wörterbuch: je nach chiraler Gradierung zerfallen die 60 Vermittler in Vektor- und Tensorblöcke; einheitlich sind sie nur als antisymmetrischer Tensor, nicht als Skalar (`RESULTS.md`, Zeilen 220–261).
4. Es fehlt bereits eine gemeinsame, unter den tatsächlichen E8-`C/J`-Clocks geschlossene Gruppen-/Feldabbildung von der 240-Wurzel-Quellalgebra über W zu den zehn lokalen chiralen CAR-Feldern. Erst danach können `K`, `q`, `Y`, Glue, Fermionparität, Adjungierte, Impuls/Derivationen und dieselbe physische Zeit gemeinsam geprüft werden.
5. Deshalb ist weder ein `n`-Koeffizient noch das Verhältnis `g_n/g_z`, noch `Vc` aus W berechnet. Der bekannte Vierpunktdefekt zeigt nur, dass eine rein gaußsche Randübersetzung nicht genügt; die nichtlineare Feldübersetzung bleibt zu konstruieren (`update_body_v16.tex`, Zeilen 99–106).

**W-Verdikt:** ein tatsächlicher, ausgeführter Nicht-Gauß-Hamiltonian mit exakt gepinntem internen Kopplungstensor. Er ist gegenüber dem Rotor der erste kompatible Herkunftspfad, weil nicht erst bewiesen werden muss, dass die Nicht-Gauß-Struktur Teil des Zeitgenerators ist. Seine lokale Boundary-Deutung und seine physische Parameter-/Zustandswahl sind weiterhin offen.

## 5. Direkter Vergleich

| Kriterium | Rotorparent | Natives Fock-W |
|---|---|---|
| Ursprüngliche Nicht-Gauß-Struktur | Nichtzentrale Rotor-Hopping-Dynamik | Boson–Fermionpaar-Kopplung |
| Was exakt im Zeitgenerator steht | `H_E+H_hop+…`; kein freier Quartikterm | `H_W=ΔN_b+g(b†P+P†b)` |
| Nachgewiesener fermionischer Quartik | In `[V,[H_E,V]]`, Koeffizient `-1/7200` | Nach kontrollierter Bosonelimination zu erwarten; als voller Boson-Fermionterm bereits nichtgaußsch |
| Zusätzlicher Schritt bis zur wirksamen Quartik | Zeitprotokoll/Magnus oder kontrollierte Elimination erforderlich | Kontrollierte Elimination/RG erforderlich, aber kein Protokoll, um die Grundkopplung erst in `H` zu bringen |
| Interne Typisierung | 4 komplexe L/H-Moden + Rotor | 64 Fermion-, 60 Vermittlermoden; Spin(10)×SU(4); nur gewählter interner Clock-Lift, kein geschlossener voller E8-`C/J`-Träger |
| Räumlichkeit | Explizite Gitterkante | Kein hergeleiteter Raumträger |
| Zehnkanalige Boundary-Abbildung | Nicht vorhanden | Nicht vorhanden |
| `n`, `z`, `Vc`, `g_n/g_z` ausgewählt | Nein | Nein |
| Priorität | Zweiter Pfad | **Erster Ausschluss-/Herkunftstest** |

Die Wahl von W beruht nicht darauf, dass 64 „näher“ an 10 wäre oder dass Symmetrie bereits Dynamik auswählte. Entscheidend ist nur der erste tragende Unterschied: Bei W ist die signierte Nicht-Gauß-Kopplung im Hamiltonian; beim Rotor ist der relevante fermionische Quartikanteil bislang eine Kommutatorfolge.

## 6. Ein einziges nächstes entscheidendes Gate

### Gate `W→EDGE.GROUP_FIELD.01`

**Aufgabe:** Konstruiere oder widerlege zuerst einen expliziten graduierten Gruppen-/Feldintertwiner

\[
\mathcal I:\mathcal R_{E_8}^{(240)}\supset \mathcal R_W
\longrightarrow \mathcal F_{\mathrm{edge}}^{(10)},
\]

der auf einem **unter den tatsächlichen `C_clk,J_clk` geschlossenen** Quelldomänenträger definiert ist und:

1. die volle vorzeichenrichtige `C/J`-Wirkung transportiert, statt sie durch den gewählten internen Lift zu ersetzen;
2. den W-Kopplungstensor samt Fermion- und Vermittlermoden auf wohldefinierte lokale Feldtypen abbildet;
3. `q`, `Y`, Glue, Fermionparität, Adjungierte und die 9R/1L-Chiralitätsform `K` als **benannte Operator-/Stromdaten** erhält;
4. ausdrücklich zeigt, wie der `c`-Zweig erreicht wird, ohne eine nicht vorhandene familienreine lineare oder antilineare Dualisierung vorauszusetzen.

**PASS:** Ein und dieselbe Abbildung erfüllt 1–4 auf einem geschlossenen Quellträger, ohne eine neue Clockwirkung oder eine familienreine Konjugation stillschweigend einzusetzen. Erst danach ist ein Operator-/Zeitintertwiner mit kontrollierter Wilson-/OPE-Projektion auf `n` und ausgewiesenem `z`-Koeffizienten sinnvoll.

**FAIL:** Der notwendige geschlossene Träger oder die gemeinsame `C/J`-, W- und Boundary-Feldwirkung existiert nicht. Dann ist der native W-Pfad in der festgehaltenen Form ausgeschlossen, bevor Zeitentwicklung oder RG gerechnet werden; erst danach lohnt der zusätzliche Rotor-Protokollschritt.

Dieses Gate ist absichtlich früher als ein Zeit-/RG-Test. Es prüft die erste tragende Identifikation, die der neue C/J-Zensus als offen beziehungsweise für `FW64` allein als falsch ausweist. Spektralvergleich, interne Tensor-Kovarianz und ein nichtverschwindender Vierpunktkumulant können diesen Typentest nicht ersetzen.

## 7. Quellen und Pins

Es wurden zwölf gezielte lokale Original-/Vertragsquellen gelesen; keine neue Primärliteratur war für die interne Provenienzentscheidung nötig. Die allgemeinen Gauß- und Edge-RG-Rahmen sind bereits im geprüften `source-dynamics-selection`-Vertrag primär belegt. Die folgenden Hashes fixieren den gelesenen Stand:

| Quelle | SHA-256 | Verwendung |
|---|---|---|
| `source-dynamics-selection-20260920/PROOF.txt` | `03c09468b07cc68abd31d7f8d6715dd474564728d053ccb063a67a1ca71c89d2` | Boundary-Vertrag, Gauß-Barriere, Grad von `n`, offener Quellenweg |
| `source-dynamics-selection-20260920/SOURCE_INVENTORY.txt` | `570d8376a29ed7f364b106181ea069ee8a0a7c849b072d249ad09bee2823ff32` | Quellinventar |
| `clock-interaction-provenance/README.md` | `e40e116d86ee092e26317b2972cff8795fa7a1d22eb6a250e03f1f8c5252fa4c` | Interpretation und Scope des Rotor-Kommutators |
| `clock-interaction-provenance/checker.py` | `f1bc93d39c8f84f76bff55da901908dcd2ba97975753992464484279ebef3506` | Exakte Linkrechnung |
| `local-window-round37/checker.py` | `559afdf7c50a27f8f921b0e7087541962cec02986779d23dbcb52f6b1e073e52` | Originale Rotor-/Hoppingterme und Koeffizienten |
| `matter-resummation-round43/MATTER_RESUMMATION.md` | `9caa09130e63a03457c4edf4aa09eb98e6edf4d0b938d4ddae88e4d6d0232643` | Parent-Zeitentwicklung und ihre Grenzen |
| `universalraum-v16-integrated-20260915/replayed_sources/native.py` | `c95751338283a0a34d291b8b6f1a21d6946c823a7ae5f144a180787c160df07f` | Unabhängige Rekonstruktion von W, Gewichten und Ladungen |
| `universalraum-v16-integrated-20260915/main-v1.6/update_body_v16.tex` | `3a7bcec7eea26015c11a9c1c1431a8c795f60205c6bb485a0eac73fc4519edf5` | Integrierter Hamilton-/Auswahlvertrag und Grenzen |
| `universalraum-native-operations-ground-response-20260915/common.py` | `2cc97522457ecc7e6774d96a25b2581b5d67cd051ae35e28a26f0e98e2adb994` | Gepinnte W-Konventionen und exakte Kovarianzchecks |
| `universalraum-native-operations-ground-response-20260915/README.md` | `570d78549e126cc4c8c2440b3cc929d71feb72e459c2a0a0fe169345a36134a0` | Ausführung und Nichtbehauptungen |
| `universalraum-native-operations-ground-response-20260915/RESULTS.md` | `fa8e33605ebeff86b8438bd52213b3acb0b3edd12a4b9d4eb44ce6d3ec6b37dd` | Hamiltonian, Feldtyp-Census, T1–T8-Grenzen |
| `universalraum-native-operations-ground-response-20260915/native_ground_state.py` | `8ae0f2f103ba0cb0a5cb832681a33130b6756fe627395368b6be635587a2eb02` | Tatsächliche Fock-Implementierung der W-Dynamik |

Keine Repository-, Ledger-, Theoriegraph-, Paper- oder Quellmutation wurde vorgenommen. Dieses Review ist eine unabhängige Scope- und Herkunftsprüfung, keine Promotion eines neuen physikalischen Modells.
