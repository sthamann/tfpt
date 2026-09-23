# Worker B: übersehene Identität im E₈-Randvertrag

15. September 2026. Status: **bedingte Doppel-Elimination bewiesen; primitive physische Auswahl nicht geschlossen.**

## Ergebnis

Innerhalb der bereits vorhandenen vollständigen affinen E₈-Vakuumrealisierung sind Zustand, alle Stromantworten und konforme Entwicklung nicht drei frei kombinierbare Objekte. Die markierte affine Stromalgebra bestimmt ihre Vakuumantworten; die geometrische Stromrotation bestimmt ihren Generator. Der signierte Paar-Tensor W ist ein abgeleiteter Operatorproduktkanal. Eine zusätzliche Auswahl eines Fock-Grundzustands und eines kubischen Paar-Hamiltonoperators gehört nicht zu dieser Randrealisierung.

Das ist eine belastbare Identität zwischen Beschreibungen **nach Festlegung der affinen Vakuum-/Konformalklasse**. Der vorhandene diskrete Compiler ist dadurch noch nicht mit dem gesamten physischen Prozess identifiziert. Seine Rohseam-Zustands-, Feld- und Zeitadapter sind gerade die Stellen, an denen die nötigen Voraussetzungen gegenwärtig fehlen. Der Satz ist Standardmathematik, hier mit dem tatsächlichen TFPT-Quellenvertrag abgeglichen; weder er noch die bekannte Wortkernrekonstruktion sind eine neue TOE.

## 1. Präziser Satz: Zustand und konforme Entwicklung sind gemeinsam bestimmt

Fixiere die komplexe Liealgebra e₈ mit ihrer positiv normierten kompakten reellen Form, einer markierten Generatorbasis und dem invarianten Bilinearformmaß (lange Wurzeln haben Quadratnorm 2). Fixiere Niveau k=1. In einer hermiteschen Basis gelten auf einer gemeinsamen invarianten algebraischen Domäne

\[
[J_m^a,J_n^b]=i f^{ab}{}_cJ_{m+n}^c+m\delta^{ab}\delta_{m+n,0},
\qquad (J_n^a)^\dagger=J_{-n}^a.
\]

Verlangt werden ein normierter Vektor Ω, die Vakuumrelationen J_n^a Ω=0 für jedes n≥0 und Zyklizität unter den negativen Strommoden. Die Existenz der positiven einfachen integrablen Vakuumdarstellung wird durch die bekannte E₈-Gitterrealisierung gewährleistet. Alle Aussagen zu unbeschränkten Moden gelten zunächst auf dem endlichen Energiekern.

**Teil A — eindeutiger Vakuumkern.** Alle Werte

\[
G(u,v)=\langle\Omega,u^\dagger v\Omega\rangle
\]

für endliche Wörter in den markierten Strommoden sind eindeutig bestimmt. Eine zweite zyklische positive Vakuumrealisierung derselben Relationen ist auf dem Wortkern und nach Vervollständigung unitär äquivalent; die markierten Ströme werden mitgenommen.

**Beweis.** Bringe ein endliches Wort mittels der affinen Kommutatorrelation in Dreiecksnormalform: negative Moden nach links, Nullmoden in die Mitte, positive Moden nach rechts. Jeder Kommutatorterm hat weniger Faktoren, sodass die Rekursion terminiert. Die positiven und Nullmoden töten Ω rechts; negative Moden töten ⟨Ω links. Nur der vollständig reduzierte Skalar bleibt. Damit sind sämtliche Matrixelemente und alle Nullrelationen festgelegt. Positivität und Existenz folgen aus der bekannten integrablen Vakuumrealisierung. Es wird kein frei gegebener vollständiger Kern vorausgesetzt: Seine Werte werden aus einer kurzen **bereits ausgewählten** affinen Regel rekursiv berechnet.

**Teil B — eindeutige konforme Rotation.** Verlange zusätzlich, dass die Entwicklung die festgelegte geometrische Kreisrotation auf den Strömen implementiert, also

\[
[H,J_n^a]=-nJ_n^a,\qquad H\Omega=0.
\]

Dann ist auf jedem negativen Modenwort

\[
H J_{-n_1}^{a_1}\cdots J_{-n_r}^{a_r}\Omega
=(n_1+\cdots+n_r)J_{-n_1}^{a_1}\cdots J_{-n_r}^{a_r}\Omega.
\]

Da diese Wörter dicht spannen, ist H der eindeutige diagonal schließbare konforme Energieoperator L₀. Der endliche Energiekern ist ein wesentlicher Selbstadjungiertheitskern dieser reellen diagonalen Wirkung; es wird keine freie Wahl einer Fortsetzung eingesetzt. Derselbe Operator folgt aus Sugawara:

\[
L_m=\frac1{2(1+30)}\sum_{a=1}^{248}\sum_{r\in\mathbb Z}:J^a_{m-r}J^a_r:,
\qquad c=\frac{248}{31}=8.
\]

Die Summen sind auf jedem endlichen Energievektor wohldefiniert. Für die volle konforme Stromwirkung gilt [L_m,J_n^a]=−nJ^a_{m+n}. Ein anderer Operator mit derselben Wirkung auf allen Strömen und Ω unterscheidet sich auf keinem zyklischen Wort. Das ist die Eindeutigkeit, die ein bloßes Vakuumprojektor- oder Clockargument nicht leisten kann.

**Konsequenz.** Alle mit diesen Entwicklungen gebildeten Mehrzeit-Wortantworten sind ebenfalls bestimmt. Auf dem Kreis mit Umfang L gilt für eine gewählte Geschwindigkeits-/Zeiteinheit v der physisch dimensionierte Randgenerator (2πv/L)L₀ relativ zum Vakuum. Der universelle Casimirterm −c/24 auf dem Zylinder ist ein additiver Bezugspunkt. L, v und die Identifikation dieser Randzeit mit einer physischen TFPT-Zeit werden nicht aus den affinen Relationen gewonnen.

Die bekannten affinen unitären VOAs sind stark lokal und liefern die zugehörigen Schleifengruppen-Konformalnetze; dies gibt hier auch einen etablierten analytischen Zielvertrag jenseits formaler Stromreihen. Quelle: [Carpi–Kawahigashi–Longo–Weiner, Beispiel 8.7](https://arxiv.org/html/1503.01260#S8). Der direkte Normalordnungs- und Eindeutigkeitsbeweis oben ist eine Anwendung auf die fixierten TFPT-Labels.

## 2. W, Paarantworten und die richtige Bedeutung des Niveaus

Im vorhandenen Außenproduktbericht wurde W einschließlich aller 480 Zeichen mit einem E₈-Gitterkozykel abgeglichen. Sein Vertrag lautet

\[
I_r(z)I_s(w)\sim\frac{\sum_AW_{A,rs}K_A(w)}{z-w},\qquad WW^T=8I_{60}.
\]

Damit folgt auf derselben Feldalgebra ohne unabhängige Paaroszillatoren

\[
K_A(w)=\frac18\sum_{r<s}W_{A,rs}\operatorname{Res}_{z=w}I_r(z)I_s(w).
\]

Das ist bereits bekannt und wird hier nicht als neue Entdeckung ausgewiesen. Der neue Prüfzweck ist die präzise Zählung: Die Paarfelder, ihre Symmetriewirkung und ihre Antworten müssen bei fixiertem vollständigem Stromvertrag nicht noch einmal ausgewählt werden. Ihre 64 Eingangsfelder und 60 Ausgangsfelder haben in der gewählten (D₅)₁×(A₃)₁-Einbettung konformes Gewicht 1. Die Spinorbezeichnung macht die 64 Eingänge nicht zu unabhängigen CAR-Erzeugern.

W allein trägt **keine Bestimmung des affinen Niveaus**: Der einfache Pol desselben Lieklammerkanals ist auch bei anderem k gleich; der zentrale Doppelpol und damit die Normen ändern sich. Insbesondere lautet ⟨J_n^a J_{−n}^b⟩=k n δ^{ab}. Positivität allein erlaubt mehrere positive ganzzahlige Niveaus. Wird dagegen die Standard-Gitter-VOA des fixierten normierten E₈-Gitters gewählt, ist k=1 eine Konsequenz dieser Konstruktion. Alternativ erzwingt c=8 zusammen mit der vollständigen affinen Sugawara-Realisierung 248k/(k+30)=8, also k=1. In beiden Fällen ist die verwendete Realisierung Voraussetzung; das Wort E₈ ersetzt sie nicht.

### Exakte Antwort außerhalb der bloßen Zwei-/Dreipunktliste

Für zwei Wurzeln aus dem vorhandenen 64er-Sektor wähle

\[
\alpha=\tfrac12(1,1,1,1,1,1,1,1),\quad
\beta=\tfrac12(-1,-1,-1,-1,1,-1,-1,1).
\]

Beide haben getrennt gerade Minusparität in den Fünfer-/Dreierblöcken. Es gilt α·β=−1 und γ=α+β=(0,0,0,0,1,0,0,1), eine der vorhandenen Paarwurzeln. Mit einem gemeinsamen Kozykelzeichen ε liefern die bekannten Gitter-Vertexformeln

\[
u=J^\alpha_{-1}J^\beta_{-1}\Omega
=\epsilon\alpha(-1)e^\gamma,\quad
v=J^\beta_{-1}J^\alpha_{-1}\Omega
=-\epsilon\beta(-1)e^\gamma.
\]

Da die Heisenbergmoden das kanonische Skalarprodukt tragen, ist der Vierstrom-Wortgram

\[
\begin{pmatrix}\langle u,u\rangle&\langle u,v\rangle\\
\langle v,u\rangle&\langle v,v\rangle\end{pmatrix}
=\begin{pmatrix}2&1\\1&2\end{pmatrix}.
\]

Insbesondere ||u−v||²=2 und ||u+v||²=6. Die erste Zahl stimmt mit der Modennorm des abgeleiteten Kommutators εJ^γ_{−2}Ω überein. Quelle für die Gitter-Vertexformel: [Huang, Abschnitte 2 und 5](https://sites.math.rutgers.edu/~yzhuang/rci/math/papers/va-lect-notes.pdf). Dies ist eine exakte vorhergesagte Antwort **in der ausgewählten Klasse**, kein unabhängiger TFPT-Holdout und kein Experiment an physischer Realität.

## 3. Scharfer Abtragungstest auf derselben E₈-Darstellung

Entferne allein die Forderung, dass die physische Entwicklung die geometrische Kreisrotation aller Ströme sein muss. Auf **demselben** E₈-Vakuum-Hilbertraum mit denselben markierten Strömen, derselben *-Struktur, demselben Ω und denselben internen Symmetrien setze

\[
H_A=L_0,\qquad H_B=L_0+4L_0(L_0-1).
\]

Das fügt weder einen Hilbertraum noch Felder oder Banken hinzu. Beide Operatoren sind selbstadjungiert, positiv und haben exakt dieselbe eindeutige Grundzustandsgerade: Auf Grad n≥1 ist H_B=n(4n−3)>0. Sie besitzen sogar dieselbe volle Viertelrotations-Clock

\[
e^{-i\pi H_A/2}=e^{-i\pi H_B/2},
\]

weil H_B−H_A auf jedem ganzzahligen Grad ein Vielfaches von 4 ist. Beide kommutieren ferner mit allen internen E₈-Symmetrien und somit auch mit den vorhandenen inneren Clock-/Spiegelungslifts. Die Viertelrotation im Exponenten wird ausdrücklich nicht mit dem inneren SU(4)-Marklift identifiziert.

Auf Grad 1 stimmen die Energien sogar überein; auf Grad 2 lauten sie 2 und 10. Für den normierten markierten Stromzustand ψ=J_{−2}^aΩ/√2 gilt

\[
\langle\psi,e^{-itH_A}\psi\rangle=e^{-2it},\quad
\langle\psi,e^{-itH_B}\psi\rangle=e^{-10it}.
\]

Bei t=π/8 sind die Antworten negativ zueinander. Das kann nicht durch eine gemeinsame Zeiteinheit erklärt werden, weil die Grad-1-Energie gleich bleibt. Es trennt die vollständigen Mehrzeitkerne trotz identischer Algebra, identischem statischem Vakuumkern und identischer Clock.

**Genaue Grenze:** H_B ist keine alternative geometrisch lokale konforme Stromrotation; bereits [H_B,J_{−2}^a]Ω=10J_{−2}^aΩ verletzt die geforderte Wirkung 2J_{−2}^aΩ. Das Gegenbeispiel widerlegt ausschließlich die Schlussregel „Algebra + Vakuum + positive Energie + diskrete Clock ⇒ ausgewählte kontinuierliche Dynamik“. Es widerlegt weder den Satz aus Abschnitt 1 noch eine zusätzliche, wirklich hergeleitete Lokalitäts-/Konformalbedingung. Es wird nicht als physisches Universalraum-Modell vorgeschlagen.

## 4. Quellenaudit: Was liefert der tatsächliche Compiler?

Alle lokalen Pfade in dieser Tabelle beziehen sich auf das Repository; SHA-256-Werte stehen in `normal.json`.

| Voraussetzung | Tatsächliche Quelle | Befund |
|---|---|---|
| Diskretes Anker-/Glue-Gerüst | `docs/THEORY.md:23–39`; `origin_theory.tex:960–981` | (1,1,2), D₅⊕A₃ und μ₄ gehören zum deklarierten Compiler. Die Origin-Quelle bezeichnet dessen Abschlussrahmen ausdrücklich als Metaeingabe. Kein Beweis „aus bloßer Konsistenz“. |
| Vollständige lokale Erweiterung im gewählten Randmodell | `verification/v154_simple_current_theorem.py:1–51`; `verification/v469_seam_crossedproduct_route.py:12–27` | Lokalität der einfachen Ströme, Gewichte 1, Index und Holomorphie greifen **auf bereits vorhandenen Niveau-1-Netzen**. v154 nennt die Identifikation des Rohseam-Netzes ausdrücklich als zusätzliche Voraussetzung. |
| W mit Phasen | `universalraum-native-exterior-reset-20260915/RESULTS.md`, Abschnitte 6–8 | Vorzeichengetreuer einzelner E₈-OPE-Kanal mit 480 Gleichungen; vollständige Standard-Gitter-VOA wird nicht durch diese 480 Tests allein bewiesen. |
| Niveau 1 | v154/v469; Standard-Gitterrealisierung | Im gewählten Gitter-/VOA-Funktor festgelegt; aus dem endlichen W-Liekanal allein nicht bestimmt. |
| Kompakte *-Struktur und positives zyklisches konformes Vakuum | Standard-V_E8; `origin_theory.tex:1810–1827` | Kanonische Zielrealisierung vorhanden. Quellenseitige Gleichheit des Rohseam-Zustands mit ihr ist die benannte H-Prämisse; ältere Prosa behauptet teils mehr, neuere analytische Kontrakte lassen Lücken offen. |
| Konforme Stromrotation/Sugawara | Standardaffine VOA; Außenproduktbericht §8 | Vollständig innerhalb dieser Klasse; kein nachgewiesener Adapter vom gesamten diskreten Compilertransport zur physisch ausgewählten Randzeit. |
| Geometrische Clock-/Markwirkung | `origin_theory.tex:1844–1872`; Außenproduktbericht §4 | Die Quelle benennt Auswahl-/Alignmentreste. Ein innerer Feldlift, geometrische Inversion und antiunitäre Reflexion sind verschiedene Objekte. Vakuuminvarianz allein bestimmt zentrale Liftphasen nicht. |
| Ganze Rohseam-Feldalgebra im Grenzwert | `verification/v973_seam_route_narrowing.py:8–31`; `docs/OPEN_PROBLEMS.md:21–34` | Die bilineare so(16)₁-Hälfte ist als gedeckt ausgewiesen; Erweiterungs-, Twist-, einseitiger Rand- und Holomorphienachweise sind nicht automatisch eingeschlossen. Die aktuelle Übersicht nennt als ersten T2-Rest ein renormiertes verschmiertes Halbladungsfeld zwischen Sektoren mit Quellenergie-/Adjungierungskontrolle, danach die aus der Quelle gewonnenen acht E₈-Kanäle und die Familie-/Clockidentifikation. |
| 3+1D-Physik/Anfangszustand/alle TFPT-Readouts | `docs/THEORY.md:7–12`; `docs/OPEN_PROBLEMS.md` T1–T8 | Kein vollständiger gemeinsamer Parent. Dieser Bericht schließt keinen dieser Elternverträge. |

### 4.1 Die konkrete Überdehnung in v469

Die Modulprosa `v469:28–38` benutzt „gleiche topologische Phase ⇒ gleicher Randgrenzprozess“. Die ausführbaren Abschnitte `v469:161–191` prüfen dazu die Übereinstimmung von Textlabels einer Theoremkette und registrieren die zentrale Realisierungsbehauptung mit `True`. Das sind weder eine Konstruktion der markierten Felder noch ein Beweis für Gleichheit ihrer Kerne. Dieselbe topologische Phase bestimmt geschützte Invarianten; vollständige markierte Korrelationsgleichheit und ihre Zeitnormierung sind stärkere Aussagen.

Der spätere `v973:8–31` führt die zitierte Literatur bereits sorgfältiger: Osborne–Stottmeister deckt die Konvergenz fermionischer Bilinearströme und der zugehörigen Virasoro-/Korrelationsobjekte. Vier weitere TFPT-Ziele werden dort ausdrücklich als nicht gedeckt klassifiziert: die μ₄/GSO-Erweiterung als Netzaussage, der Spin-/Twistsektor, die einseitige Randrealisierung des 2+1D-Bulks und der Holomorphieselektor. [Osborne–Stottmeister, Einleitung und Abschnitte 5–6](https://arxiv.org/html/2107.13834) beginnt mit ausgewählten Gitter-Hamiltonoperatoren, Observablenalgebren, Verfeinerungskanälen und Zustandsfolgen; daraus wird nicht ohne weitere Identifikation ein Satz über jeden Rohseam-Prozess.

Die positive abstrakte Erweiterung darf deshalb verwendet werden. Ihre bloße Existenz darf nicht als bereits bewiesene Herkunft derselben Erweiterung aus dem ursprünglichen Prozess gezählt werden. Insbesondere ist die bosonische spinorielle E₈-Erweiterung nicht unverändert dieselbe lokale CAR-Feldalgebra der 16 freien Majoranas.

## 5. Wie viel E₈ kann tatsächlich durch Eindeutigkeit entfallen?

[Dong–Mason, Theorem 1](https://arxiv.org/pdf/math/0203005) beweist: Eine holomorphe VOA vom CFT-Typ, C₂-kofinit, mit c=8 ist isomorph zu V_E8. „Holomorph“ ist dort eine rationale Theorie mit nur einem irreduziblen Modul; die Papierprämissen dürfen nicht auf „ein Vakuum beobachtet“ verkürzt werden. Die positive unitäre physische Interpretation benötigt zusätzlich eine geeignete unitäre Struktur. Das Ergebnis fixiert einen **Isomorphietyp**; eine markierte TFPT-Feldkarte wird durch einen unmarkierten Isomorphiesatz nicht gewählt.

In dieser festgelegten Theorieklasse ist c positiv und durch 8 teilbar. Wählt man zusätzlich die kleinste positive zentrale Ladung, folgt c=8 und dann E₈. Das ist eine saubere bedingte Eindeutigkeitsroute. Die Minimierung von c ist aber eine eigene Auswahlregel; weder Selbstkonsistenz noch Selbstbeschreibung beweist, dass gerade zentrale Ladung das physische Minimalitätsmaß sein muss. Bekannte holomorphe Theorien größerer zentraler Ladung erfüllen weiterhin die genannten Konsistenzbedingungen.

Der Satz schließt keine bloße Zahlenlücke: Er ist stärker als „c=8 und 248 passen zu E₈“. Er setzt dafür eine vollständige VOA-Klasse einschließlich ihrer Rationalitäts-/Endlichkeitsbedingungen voraus. Eine Netzaussage darf nicht ohne gesicherte VOA-Netz-Verbindung schlicht als Dong–Mason-Prämisse eingesetzt werden.

## 6. Abhängigkeitsgruppen und ehrliche Zählung

| Gruppe | Zusammenhängende Befunde | Eignung als zurückgehaltener Test nach E₈-/VOA-Wahl |
|---|---|---|
| Gitter | Rang 8, 240 Wurzeln, 248=240+8; gewählte D₅⊕A₃-Zerlegung und 45+15+60+64+64 | Nicht unabhängig; alle gehören zur fixierten Gitter-/Liealgebra. |
| Theta/Charakter | Θ_E8=E₄=1+240Σσ₃(n)qⁿ; χ=Θ_E8/η⁸; 1,248,4124,… | Der Charakter folgt aus Gitter und acht Oszillatorrichtungen. Keine zusätzliche Auswahlbestätigung. |
| OPE und W | Signierter W, Pair-Residuen, Außenquadrat-Kovarianz, Drei-/Vierstromantworten | Konsequenzen der gewählten markierten VOA und ihres Vakuums. Hier Prüfungen der Implementations-/Darstellungstreue. |
| Konformer Zeitkern | ⟨J_nJ_−n⟩=n, Energie n, q/(1−q)² | Konsequenzen von Niveau-1-Vakuum plus geometrischer Rotation; kein Beweis ihrer Rohseam-Herkunft. |
| Separater TFPT-Anschluss | Ward-Funktional und α-Wert mit seinen Normierungen; Quellclock als derselbe Feld-/Zeitoperator | In dieser Runde **kein** unabhängiger Ableitungs-/Holdout-Nachweis. |

Für ΔN muss die Zählkonvention sichtbar bleiben:

1. **Zusätzlich auszufüllende Darstellungsfelder:** Wer zum vollständig markierten affinen Vakuum-/Konformalvertrag noch ω und H_conf separat angeben wollte, braucht nach dem Satz beide nicht: N_before=2, N_after=0, ΔN_slots=2. Auch K_A ist keine unabhängige neue Bank. Diese Einsparung betrifft eine redundante Darstellungsweise.
2. **Tatsächlich freie mathematische Moduli in genau diesem vollständigen Vertrag:** Sie waren für ω und H_conf bereits vorher null; der Satz beweist N_before=N_after=0. Die Identität beseitigt ein Missverständnis über Freiheit, nicht zwei physisch variable Parameter in derselben Klasse.
3. **Unabhängige primitive Entscheidungen vom Rohcompiler bis zur Realität:** Die Zahl und das Maß sind nicht bestimmt; die nötige Rohseam-Feld-/Zustands-/Zeitidentifikation ist nicht bewiesen. ΔN_phys≥2 ist **nicht nachgewiesen**. Der Konformalvertrag darf nicht kostenlos in die Annahmen geschoben werden.

Somit besteht die attraktive Gegenhypothese auf der Ebene des vorhandenen Randmodells: Es gibt weniger unabhängige Wahlstellen als eine Fock-Erweiterung vermuten lässt. Sie gewinnt noch nicht gegen eine fehlende physische Selektionsregel für den Rohprozess.

## 7. Konkretes nächstes Entscheidungskriterium

Benötigt wird eine einzige **markierte Vakuum-/Konformalidentifikation** vom ursprünglichen Seam-Prozess in die bereits vorhandene V_E8-Realisierung: dieselben erzeugenden Felder einschließlich der einfachen Spinor-Erweiterung, dieselbe Adjungierung, derselbe zyklische Zustand und die geometrische Stromwirkung der Quellzeit. Kontrollierte Konvergenz auf einer gemeinsamen dichten Domäne, Energiebeschränkungen und Erzeugung der vollständigen Zielalgebra müssen dabei bewiesen werden; es genügt nicht, dieses Wörterbuch zu definieren.

Wenn dieser eine Brückensatz folgt, übernehmen Normalordnung und Sugawara alle Randkorrelationen und die konforme Entwicklung gemeinsam. Ein separater Rand-Hamiltonian- oder Vakuumselector wäre dann überflüssig. Daraus folgt noch keine 3+1D-Rekonstruktion und kein unabhängig geprüfter Ward-/α-Readout. Wenn nur endliche Charaktere und Symmetrieschatten übereinstimmen, ist die Brücke weiterhin offen.

Die verlangte Endformulierung „Eine physikalische Realität existiert genau dann, wenn ihr vollständiger Prozess ___“ kann Worker B nicht wahrheitsgemäß schließen. Präzise schließbar ist allein: **Ein markierter affiner E₈-Randprozess ist innerhalb seines Vakuum-/Konformalvertrags darstellungsstarr.**

## Reproduktion und Grenzen

`verify_identity_scope.py` prüft den Originaltensor ohne Imaginärteile wegzuschneiden, die exakten Gewicht-/Niveaubeziehungen, den Vierstrom-Wortgram und den Clock-Abtragungstest. Normaler Lauf und `python3 -OO` liefern identische JSON-Ausgaben mit 20 bestandenen endlichen Kontrollen. Die verwendeten Quellhashes sind vor und nach jedem Lauf identisch. Die vollständige frühere Kozykelrechnung wird nicht wiederholt. Die analytischen Aussagen werden durch die oben angegebenen Beweise und Literaturverträge getragen, nicht durch 20 Tests.

Während der Checker-Erstellung wurden zwei reine Prüferfehler behoben: SymPy-Wahrheitswerte dürfen nicht als arithmetische Summanden behandelt werden; expandierte und faktorisierte Polynome müssen durch verschwindende Differenz statt syntaktische Gleichheit verglichen werden. Die mathematischen Daten wurden nicht angepasst.

Nur dieser Worker-Unterordner wurde beschrieben. Keine Quelle, kein Paper, kein Ledger und kein Git-Commit wurde geändert.
