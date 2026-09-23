# Ein echter Quartett-Beweisschritt und eine weitere versteckte Vereinfachung

Stand: 14. September 2026. Ausschließlich das deklarierte endliche C16-Austauschmodell und sein SU(4)-Singulett. Keine native Compiler-Schließung, keine vollständige TOE, keine globale Aussage über alle SU(4)-Sektoren.

## Kurzbefund

1. Der zuvor nur angekündigte **80 × 80-Multiplizitätsblock wurde explizit konstruiert**, sowohl numerisch als auch mit exakter endlicher Körperarithmetik.
2. **Alle 80 Eigenwerte dieses Blocks sind beweisbar einfach.** Eine exakte modulare Rechnung liefert ein quadratfreies charakteristisches Polynom; die Behauptung beruht nicht auf numerisch unterschiedlichen Dezimalzahlen.
3. Das **vollständige ganzzahlige charakteristische Polynom** wurde mittels chinesischem Restsatz eindeutig rekonstruiert. Eine exakte rationale Wurzelzählung beweist

   \[
   11.561762122<E_{\mathrm{std},0}/J<11.561762123,
   \]

   \[
   13.2464863<E_{\mathrm{std},1}/J<13.2464864.
   \]

   Dazwischen liegt kein weiterer Standardblock-Eigenwert. Innerhalb des Standard-isotypischen Raums ist jeder davon **exakt vierfach**, nicht nur ungefähr vierfach.
4. Eine zusätzliche **Tableau-Transpositionssymmetrie** erklärt die Spiegelung \(E\leftrightarrow40-E\). Im Standardsektor reduziert sie das Problem weiter auf **40 × 40**.
5. Noch weiter reicht eine exakte Gesamtzerlegung: Das gesamte 24.024-dimensionale Singulett zerfällt in **18 Multiplizitätsblöcke**, größter Block 262. Unter der neuen Spiegelung werden daraus **18 quadrierte Singularwertprobleme**, keines größer als **131 × 131**. Diese übrigen Matrizen sind hier noch nicht alle konstruiert oder spektral zertifiziert.

Dies ist ein konkreter mathematischer Fortschritt. Noch nicht bewiesen ist, dass kein anderer Symmetrie- oder SU(4)-Block ein tieferes oder zusammenfallendes Niveau besitzt. Deshalb ist es noch kein globaler Grundzustands-/Gesamtlückensatz.

## 1. Das präzise Modell

Die 16 Ecken sind die geraden Vorzeichenvektoren in \(\{\pm1\}^5\); eine Kante verbindet Ecken im Hammingabstand vier. Es gibt 40 Kanten. Auf dem Spechtraum der selbstkonjugierten Form \(\lambda=(4,4,4,4)\) definieren wir

\[
X=\sum_{e\in E(C_{16})}\rho((ij)),\qquad
H_0/J=20I+\frac12X.
\]

Die Youngdarstellung wird unabhängig erzeugt, nicht aus früher gespeicherten Eigenvektoren übernommen. Es wird keine 24.024 × 24.024-Matrix angelegt. Die vier SU(4)-Farben und die 16 Träger sind vorausgesetzt, nicht hier hergeleitet.

Die Graphsymmetrie enthält \(G=T\rtimes S_5\), \(T\cong(\mathbb Z_2)^4\). Die exakte Murnaghan–Nakayama-Charakterrechnung liefert

| Fixraum | Dimension |
|---|---:|
| \(T\) | 1764 |
| \(T\rtimes S_4\) | 108 |
| \(T\rtimes S_5\) | 28 |
| Differenz der letzten beiden Fixräume | **80** |

Mit den Gruppenmittelungsprojektoren ist

\[
P=P_T(P_{S_4}-P_{S_5}).
\]

Die Permutationsdarstellung \(\operatorname{Ind}_{S_4}^{S_5}1\) zerfällt in \(1\oplus\mathrm{std}\). Daher enthält \(\operatorname{im}P\) genau eine Fixlinie je Standardkopie, also genau den gewünschten Multiplizitätsraum. Weil \(X\) mit \(G\) kommutiert, gilt auf dem vollständigen Standard-isotypischen Raum

\[
X\cong A_{80}\otimes I_4.
\]

Das ist der Grund für den algebraischen Vierfachschutz; Einfachheit von \(A_{80}\) muss zusätzlich bewiesen werden.

## 2. Wie die Einfachheit wirklich zertifiziert wurde

Neben der orthogonalen numerischen Youngdarstellung konstruiert `checker.py` eine **rationale seminormale Darstellung modulo einer Primzahl**. Für benachbarte Tableaueinträge mit Inhaltsabstand \(d\) hat sie rationale Koeffizienten \(1/d\) und \(1\pm1/d\). Die Youngrelationsformeln sind bekannt; zusätzliche Coxeterproben prüfen die Implementierung. Sämtliche Symmetriefixbedingungen und die Block-Intertwineridentität werden anschließend auf **allen 80 Basisvektoren** exakt geprüft.

Aus zufällig gewählten ganzzahligen Testspalten entsteht durch den exakten Projektor eine Matrix \(B\in\mathbb F_p^{24024\times80}\). Zufall dient hier nur zur Auswahl eines bequemen Basiskandidaten: Rang 80 wird durch exakte Pivots zertifiziert. Es bleibt kein probabilistischer Rang- oder Spektralschluss.

Die reduzierte Matrix erfüllt

\[
XB=BA_{80}\pmod p
\]

an sämtlichen 1.921.920 Einträgen. Das charakteristische Polynom wird aus exakten Newton-Identitäten berechnet, seine Cayley–Hamilton-Identität zusätzlich vollständig geprüft. Für \(p=65521\) ergibt sich

\[
\gcd(\chi_{A_{80}},\chi'_{A_{80}})=1.
\]

Die Projektoren sind über \(\mathbb Q\) definiert, ihre Dimension 80 ist unabhängig exakt bekannt, und die modular invertierbare Pivotmatrix hebt zu einer über \(\mathbb Q\) invertierbaren Matrix. Damit ist dies die Reduktion des richtigen rationalen Blocks. Ein mehrfacher charakteristischer Faktor in Charakteristik null könnte bei einer guten Primzahl nicht zu einem quadratfreien Polynom werden. **Die 80 Eigenwerte sind also exakt einfach.**

Die numerische Parallelrechnung ist nur ein zusätzlicher Vergleich. Sie ergibt einen Frobeniusrest der Block-Intertwineridentität von etwa \(5.25\cdot10^{-13}\) und maximale Eigenpaarreste etwa \(9.43\cdot10^{-14}\); auf diese kleinen Werte stützt sich der Einfachheitsbeweis nicht.

## 3. Ganzzahliges Polynom und exakte spektrale Ordnung innerhalb des Blocks

\(X\) ist ein ganzzahliger Gruppenalgebraoperator. Sein rationaler invarianter Raum erhält das Schnittgitter mit einem ganzzahligen Spechtgitter. Deshalb ist sein monisches charakteristisches Polynom ganzzahlig. Da jeder Summand normierte selbstadjungierte Involution ist, liegen alle Eigenwerte von \(X\) in \([-40,40]\). Der Koeffizient an \(x^{80-k}\) erfüllt folglich

\[
|c_k|\le {80\choose k}40^k.
\]

`crt_certificate.py` rekonstruiert alle Koeffizienten aus **17 verschiedenen Primmoduli nahe \(10^8\)**. Ihr Produkt hat 452 Bits und übertrifft zweimal die größte vorab bewiesene Koeffizientenschranke (428 Bits). Damit ist die symmetrische CRT-Rekonstruktion eindeutig, unabhängig vom später erkannten tatsächlichen Koeffizientenwachstum. Eine **18. unbenutzte Primzahl** bestätigt das gesamte rekonstruierte Polynom.

`exact_polynomial.json` enthält alle 81 Koeffizienten. Das Polynom beginnt

\[
p(x)=x^{80}-1842x^{78}+1581110x^{76}-843228392x^{74}+\cdots.
\]

Die Wurzelzählungen benutzen ausschließlich ganze/rationale Polynomrechnung. Kein numerischer Intervallendpunkt wird als exakter Eigenwert ausgegeben. Sie schließen die beiden oben angegebenen niedrigsten Standardblock-Energien ein und beweisen insbesondere

\[
E_{\mathrm{std},1}/J-E_{\mathrm{std},0}/J>1.684724177.
\]

Das ist ein **Abstand innerhalb des Standard-Multiplizitätsblocks**. Es ist nicht der etwa 0,516 große Abstand zwischen dem bisher numerisch gefundenen globalen Singulettgrundzustand und dem Quartett.

## 4. Die übersehene einfache Symmetrie: Tableau-Transposition

Für jedes Standardtableau \(t\) sei \(t^\top\) das transponierte Tableau. Wähle \(\eta_t\) als Signum der Folge seiner Zellen in Zeilenordnung und setze in der orthogonalen Youngbasis

\[
\mathcal J|t\rangle=\eta_t|t^\top\rangle.
\]

Für das 4 × 4-Quadrat hat die Zellentransposition sechs Transpositionen, also gerades Signum. Damit gilt exakt

\[
\mathcal J^2=I,\qquad \mathcal J^\dagger=\mathcal J,
\qquad \mathcal J\rho((ij))\mathcal J=-\rho((ij)).
\]

Die letzte Identität folgt direkt: Tableau-Transposition negiert den Inhaltsabstand; Vertauschung zweier benachbarter Einträge negiert \(\eta_t\). `transpose_duality.py` prüft diese diskreten Identitäten für alle einschlägigen Tableaux und Generatoren, nicht nur auf Stichproben.

Alle 1920 Graphautomorphismen sind gerade Permutationen der 16 Träger. Daher kommutiert \(\mathcal J\) mit ihrer Darstellung, während es mit \(X\) antikommutiert:

\[
[\mathcal J,G]=0,\qquad \{\mathcal J,X\}=0,
\qquad \mathcal JH_0\mathcal J=40I-H_0.
\]

### Warum sogar alle Multiplizitätsblöcke gleich große Plus-/Minus-Hälften haben

Für jedes \(g\in G\) konstruiert der Prüfer eine **ungerade** Permutation \(h\in S_{16}\), die \(g\) zentralisiert. Hat \(g\) einen geraden Zyklus, genügt dieser Zyklus selbst. Andernfalls besitzt sein hier auftretender Zykeltyp zwei gleich lange ungerade Zyklen; deren Austausch ist eine ungerade zentralisierende Permutation. Alle 1920 Fälle werden diskret überprüft.

Folglich gilt

\[
\operatorname{tr}(\mathcal J\rho(g))
=\operatorname{tr}(\rho(h)\mathcal J\rho(g)\rho(h)^{-1})
=-\operatorname{tr}(\mathcal J\rho(g))=0.
\]

Die \(+1\)- und \(-1\)-Räume von \(\mathcal J\) besitzen also als \(G\)-Darstellungen denselben Charakter. **Jede einzelne Multiplizität halbiert sich.** In geeigneten Basen gilt

\[
X_\alpha=\begin{pmatrix}0&C_\alpha\\C_\alpha^\dagger&0\end{pmatrix},
\qquad E_{\alpha,j}/J=20\pm\frac12\sigma_j(C_\alpha).
\]

Die allgemeine Tabelle lautet:

| Impulsorbit | Kleine Gruppe | Multiplizitätsgrößen | Größen von \(C_\alpha C_\alpha^\dagger\) |
|---|---|---|---|
| 1 | \(S_5\) | 28, 80, 86, 80, 66, 42, 8 | 14, 40, 43, 40, 33, 21, 4 |
| 5 | \(S_4\) | 54, 176, 124, 194, 72 | 27, 88, 62, 97, 36 |
| 10 | \(S_2\times S_3\) | 124, 262, 140, 106, 232, 126 | 62, 131, 70, 53, 116, 63 |

Die Dimensionen mit den zugehörigen irreduziblen Darstellungsdimensionen gewichtet summieren sich exakt zu 24.024. Die Summe der Multiplizitäten ist 2000, die Summe der halben Dimensionen 1000. Für das Standardquartett ist \(C\) bereits konkret als numerische 40 × 40-Matrix gespeichert; \(p(x)=q(x^2)\) liefert sein exakt zertifiziertes Grad-40-Quadratspektrum.

**Nicht verwechseln:** Dieses \(\mathcal J\) ist eine innere endliche Austauschsignum-Symmetrie. Es ist keine hergeleitete Raumzeit-Chiralität, kein Nachweis chiraler Standardmodellmaterie und kein neuer Zeitpfeil.

## 5. Was davon bei vierter Ordnung erhalten bleibt

Für kantenlokale Vermittler sei \(B_v=\sum_{e\ni v}S_e\) und \(A_v=5I-B_v\). Dann ist die bereits gefundene lokale Korrektur

\[
F_4^{\rm loc}=\sum_v A_v(A_v-I)
=320I-18X+\sum_vB_v^2.
\]

Damit

\[
\mathcal JF_4^{\rm loc}\mathcal J=F_4^{\rm loc}+36X.
\]

Die einfache Energiespiegelung gilt also **nicht unverändert** für \(H_0+\epsilon^2F_4^{\rm loc}/2\). Die Graphautomorphismen bleiben jedoch erhalten, daher bleibt der 80er Standard-Multiplizitätsraum richtig.

Der Sternoperator ist \(A_v=5I-J_6\), wobei \(J_6\) das Jucys–Murphy-Element der sechs betreffenden Träger ist. Seine Inhalts-Eigenwerte sind ganzzahlig zwischen \(-5\) und \(5\); daher hat \(A_v\) nur ganzzahlige Eigenwerte in \([0,10]\). Somit ist \(A_v(A_v-I)\) positiv und höchstens \(90I\), was die Schranke gibt

\[
0\le F_4^{\rm loc}\le1440I.
\]

Mit Min–Max folgt für den Abstand der beiden niedrigsten Standardblock-Niveaus des trunkierten lokalen Operators

\[
g_{\rm std}^{(2+4)}/J>1.684724177-720\epsilon^2.
\]

Insbesondere bleibt der unterste Standardblock-Eigenwert für \(\epsilon\le1/21\) einfach und sein Niveau innerhalb des Standard-isotypischen Raums exakt vierfach. Bei \(\epsilon=1/640\) beträgt die garantierte Abstandsschranke **1.6829663645 J**. Bei \(1/20\) reicht diese grobe Normschranke nicht. Dies schließt weder die Konkurrenz anderer Blöcke noch den Rest aller höheren Ordnungen.

## 6. Was jetzt genau noch zu tun ist

1. **Die übrigen 17 kleinen Singulettblöcke konstruieren.** Die exakte Dimension und die passende Impuls-/Little-Group-Auswahl stehen fest. Mit dem neuen \(\mathcal J\) benötigt man für den führenden Austauschoperator höchstens 131 × 131-Quadratspektren.
2. **Die größten Singularwerte der Blöcke rigoros vergleichen.** Das liefert die globale Singulett-Spektralordnung, statt aus einer langen Lanczosliste auf ihre Vollständigkeit zu schließen.
3. **Die 63 anderen SU(4)-Sektoren kontrollieren.** Die neue Singulettzerlegung ersetzt diese Aufgabe nicht. Ihre eigene Graphsymmetriereduktion und/oder wirklich zertifizierte untere Schranken sind nötig.
4. **Die spektrale Ordnung auf das konkret gewählte mikroskopische Modell übertragen.** Hierfür müssen eine echte einheitliche Restschranke, die Vermittlerarchitektur und die native Phasen-/Symmetriezuordnung zusammenpassen.
5. **Keinen physikalischen Beweis vorziehen.** Selbst ein vollständig gelöstes endliches Spektrum liefert noch keine Vielzellengrenze, 3+1D-Raumzeit, chirales Maß oder dynamische Spin-2-Anregung.

## 7. Reproduzierbarkeit und Evidenzgrenzen

Eigene Dateien liegen ausschließlich in diesem `quartet/`-Ordner. Keine Änderungen an fremden Forschungsständen, kein Commit, keine PDF- oder Website-Promotion.

Reihenfolge:

```text
python3 checker.py --characters-only
python3 checker.py
python3 checker.py --floating
python3 crt_certificate.py
python3 little_group_reduction.py
python3 transpose_duality.py
python3 replay.py
```

`checker.py` benötigt NumPy, SciPy und SymPy. `crt_certificate.py` erzeugt fehlende Primmodulrechnungen selbst und prüft danach die exakte Rekonstruktion. Gespeicherte Ergebnisse enthalten Quellenprüfsummen. Die normale und optimierte Ausführung werden verglichen. Negative Kontrollen verändern einen Blockeintrag, einen Polynomkoeffizienten und die Eigenwertmultiplizität und müssen von den jeweiligen exakten Identitäten zurückgewiesen werden.

Die Beweiskette ist eine reproduzierbare computerunterstützte exakte Rechnung unter den angegebenen Darstellungssätzen und üblichen Integer-/Modulararithmetikannahmen. Es wurde kein unabhängiger Lean- oder anderer Proof-Assistant-Kern benutzt. Numerische Vergleichswerte sind getrennt als numerisch gekennzeichnet.

Fachlicher Hintergrund zur Young-Seminormaldarstellung: [Vershik–Okounkov, A New Approach to Representation Theory of Symmetric Groups](https://www.esi.ac.at/preprints/esi333.pdf). Die konkrete C16-Reduktion, die modularen Matrizen, die CRT-Koeffizienten und die explizite Zentralisatorprüfung sind hier neu ausgeführt.
