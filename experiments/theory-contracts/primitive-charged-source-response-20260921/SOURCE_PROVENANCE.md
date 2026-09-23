# Was P1-Nahtkern und Transfer wirklich festlegen

**Stand:** 21. September 2026  
**Scope:** Quellen- und Rekonstruktionsaudit ohne \(\Gamma\)-, \(V_{\rm aux}\)-, RR- oder neue Modellannahmen; keine Änderung am TFPT-Repository.  
**Verdict:** **P1 deklariert Eigenschaften und Normierung eines reflexionspositiven skalaren Randkerns. Der separat angegebene Drei-Zustands-Transfer legt einen positiven Auslesekanal mit eindeutiger dimensionsloser Relaxationszeit fest. Eine Operatorgleichheit zwischen beiden ist im geprüften Quellenpfad nicht bewiesen. Weder Quelle legt dort die Feldalgebra, geladene Felder, den vollständigen Zustand oder physische/unitäre Zeit fest.** Das ist zuerst eine fehlende Herkunftsspezifikation; nach Ergänzung der vollständigen Daten bleiben konkrete Kontinuums- und Identifikationssätze zu beweisen.

## 1. Die stärkste quellentreue P1-Definition

Die ursprüngliche Definition lautet:

\[
  (P1):\quad
  \text{eine orientierte Naht }\Sigma\text{ trägt einen primitiven,
  reflexionspositiven Randkern mit }[u_\Sigma]=1,
  \qquad c_3=\frac1{8\pi}.
\]

Das ist die vollständige explizite Definition in `tfpt_1_architecture_e8.tex:163-176`. Sie setzt:

1. die orientierte Naht \(\Sigma\),
2. Reflexionspositivität des Randkerns,
3. Einheitswindung \([u_\Sigma]=1\),
4. die Selbstverkettungsnormierung \(c_3=1/(8\pi)\).

Sie gibt dort **keine** Menge von Feldsymbolen, keine Multiplikation oder CAR/CCR-Relationen, keinen Testfunktionsraum, keine Zeittranslationswirkung und keine Werte aller \(n\)-Punktfunktionen an. Der Ledger hält P1 deshalb weiterhin als deklarierten Input; die Identität

\[
  I\,\beta_{\rm angle}\,c_3=4\cdot2\pi\cdot\frac1{8\pi}=1
\]

ordnet den Wert ein, leitet den physischen Kern aber nicht her (`AX.P1.01`, `status_ledger.csv:2`).

Spätere Texte schärfen die beabsichtigte Lesart ausdrücklich zu **einem skalaren Zweipunktkern**: `tfpt_1_architecture_e8.tex:1543-1546` und `:1610-1623`. Dort wird der Schluss „ein Kern bestimmt alle Korrelationen“ nur für das bereits angenommene freie/quasifreie \(c=8\)-Majorana-Netz via Wick/Pfaffian gezogen. Das ist eine starke bedingte Vervollständigung von P1, nicht Inhalt der Definition in Zeile 167.

Damit ist „P1-Kern“ in den Quellen kein vollständig spezifiziertes Schwingerfunktional. Insbesondere ist \(c_3\) eine Normierung, keine Formel \(K(x,y)\) für alle Argumente.

## 2. Der separat definierte Transfer

Der konkrete endliche Nahttransfer ist

\[
T=J+\left(\frac23\right)^6 P_2+\left(\frac13\right)^6 P_3,
\]

mit

\[
J=\frac13\mathbf1\mathbf1^{\mathsf T},\qquad
P_2=\frac{(1,-1,0)^{\mathsf T}(1,-1,0)}2,\qquad
P_3=\frac{(1,1,-2)^{\mathsf T}(1,1,-2)}6.
\]

Er ist symmetrisch, strikt positiv, doppelt stochastisch und hat

\[
\operatorname{spec}T=\left\{1,\frac{64}{729},\frac1{729}\right\}
=\left\{1,\left(\frac23\right)^6,\left(\frac13\right)^6\right\}.
\]

Auf genau diesem dreidimensionalen Ausleseraum folgen ohne weitere Wahl:

- der eindeutige stationäre Vektor \(\pi=(1,1,1)/3\);
- geometrische Relaxation auf \(\pi\);
- der dimensionslose Gap \(\Delta=6\log(3/2)\);
- die eindeutige reelle Hauptlogarithmus-Einbettung \(Q=\log T\) als klassischer Markovgenerator;
- \(e^{tQ}\) als positive, doppelt stochastische Halbgruppe für \(t\ge0\).

Explizit

\[
Q=
\begin{pmatrix}
-\log(81/8)&\log(9/8)&2\log3\\
\log(9/8)&-\log(81/8)&2\log3\\
2\log3&2\log3&-4\log3
\end{pmatrix}.
\]

Diese Aussagen sind die exakte Reichweite von `verification/v221_seam_qecc.py:39-65` und `verification/v971_markov_embedding_generator.py:1-50,61-70,90-152`; `tfpt_research_contracts.tex:12726-12760` bezeichnet sie ausdrücklich als endliche, irreversible statistische Dynamik.

Der gleiche Transfer legt **nicht** fest:

- auf welcher Feldalgebra er wirkt;
- wie er auf ungeraden/geladenen Operatoren wirkt;
- eine lokale Hamiltondilatation;
- Lorentzzeit oder einen unitären Generator;
- die physische Dauer eines Schrittes.

Schreibt man bedingt \(T=e^{-aH}\), dann ist

\[
H=-a^{-1}\log T
\]

auf diesem dreidimensionalen Raum eindeutig, aber der Schritt \(a\), die Einbettung dieses Raums in die Feldtheorie und die Identifikation mit physischer Zeit sind zusätzliche Daten. Genau diese Trennung steht in `tfpt_research_contracts.tex:12762-12775`.

## 3. Exakter Rekonstruktionssatz, der tatsächlich anwendbar wäre

Die passende Rekonstruktion braucht zunächst eine **definierte** unital involutive Wortalgebra \(\mathfrak A\), erzeugt etwa von Feldsymbolen \(\Phi_a(f)\), mit:

- positiver-Zeit-Unteralgebra \(\mathfrak A_+\),
- Reflexion \(\Theta\),
- euklidischer Translationshalbgruppe \(\tau_s\), \(s\ge0\),
- einem normierten Funktional \(\omega_E:\mathfrak A\to\mathbb C\).

Reflexionspositivität ist dann die konkrete Ungleichung

\[
\omega_E\!\left(\Theta(F)F\right)\ge0
\qquad(F\in\mathfrak A_+).
\]

Mit

\[
\langle[F],[G]\rangle_{\rm OS}
=\omega_E\!\left(\Theta(F)G\right),\qquad
\mathcal N=\{F:\langle F,F\rangle_{\rm OS}=0\},
\]

folgt der Hilbertraum

\[
\mathcal H_{\rm OS}=\overline{\mathfrak A_+/\mathcal N},
\qquad \Omega=[1].
\]

Sind die Translationen wohldefiniert auf dem Quotienten, invariant und reflektionsverträglich und erfüllen sie die zusätzlich benötigten Kontraktions- und Stetigkeitsbedingungen, bilden sie dort eine stark stetige symmetrische Kontraktionshalbgruppe. Mit den hierfür nötigen OS-Domänen-/Regularitätsannahmen liefert der Halbgruppensatz

\[
T(s)[F]=[\tau_sF],\qquad T(s)=e^{-sH},\qquad H\ge0.
\]

Unter den übrigen OS-Annahmen — Regularität/Wachstum, euklidische Kovarianz, graded Symmetrie beziehungsweise Statistik und Clusterung — rekonstruiert die vollständige Familie euklidischer Greenfunktionen eine Wightman-Theorie bis auf unitäre Äquivalenz. Das ist etablierte Mathematik, kein offener TFPT-Satz.

GNS allein beginnt noch früher: Ist \(\mathfrak A\) bereits gegeben und \(\omega(A^*A)\ge0\), dann erzeugt

\[
\langle[A],[B]\rangle=\omega(A^*B)
\]

eine zyklische Darstellung. GNS **rekonstruiert eine Darstellung einer gegebenen Algebra**; es erfindet nicht die fehlende Algebra, Ladungswirkung oder Zeittranslationshalbgruppe.

## 4. Wie viele Korrelatoren nötig sind

### Allgemeiner, möglicherweise wechselwirkender Fall

Man braucht die gesamte Folge

\[
S_0,S_1,S_2,S_3,\ldots,
\]

beziehungsweise dasselbe Funktional auf allen Wörtern der Feldalgebra. Für eine fermionparitätserhaltende Theorie verschwinden typischerweise ungerade Funktionen; trotzdem sind im Allgemeinen **alle** \(S_{2n}\), \(n\ge1\), nötig. Ein Zweipunktkern reicht nicht.

Ein elementarer Gegenzeuge besteht schon für zwei Fermionmoden. Die Zustände

\[
\rho_A=\tfrac12(|00\rangle\langle00|+|11\rangle\langle11|),\qquad
\rho_B=\tfrac12(|10\rangle\langle10|+|01\rangle\langle01|)
\]

haben dieselben Zweipunktdaten

\[
\langle c_i^\dagger c_j\rangle=\tfrac12\delta_{ij},\qquad
\langle c_ic_j\rangle=0,
\]

aber

\[
\langle n_1n_2\rangle_{\rho_A}=\tfrac12,
\qquad
\langle n_1n_2\rangle_{\rho_B}=0.
\]

Beide Zustände sind positive Funktionale. Positivität plus Zweipunktdaten bestimmt also den Vierpunktsektor nicht.

### Quasifreier/Gaußscher Sonderfall

Eine **hinreichende** und in den späteren TFPT-Texten tatsächlich benutzte Route ist: Ein distributionwertiger Zweipunktkern bestimmt die Korrelatoren, wenn zusätzlich feststehen:

1. die CAR- oder CCR-Algebra und ihr Testfunktionsraum;
2. die Adjungierung/Realstruktur und gegebenenfalls die Gradierung;
3. Quasifreiheit, also Wick- beziehungsweise Pfaffianfaktorisierung;
4. die erforderliche Positivität, Regularität und Kovarianz des Kerns.

Für Majoranas lautet dann

\[
S_{2n}(1,\ldots,2n)=\operatorname{Pf}\bigl(S_2(i,j)\bigr),
\qquad S_{2n+1}=0.
\]

Das erklärt die spätere TFPT-Aussage „one kernel is the whole net“. Für diese Route muss die 16-Majorana-CAR-Algebra feststehen und Quasifreiheit entweder vorausgesetzt oder aus weiteren Quelldaten bewiesen sein. P1 allein enthält diese Angaben nicht. Quasifreiheit ist hier eine ausreichende Rekonstruktionsroute, keine behauptete notwendige Bedingung: In engeren Klassen können weitere algebraische Daten, etwa eine fest vorgegebene reine CAR-Projektorstruktur, den Slaterzustand bereits erzwingen.

## 5. Was für geladene Felder zusätzlich nötig ist

Ein neutraler/skalarer Kernel auf der beobachtbaren geraden Algebra rekonstruiert zunächst diese beobachtbare Darstellung. Geladene Felder sind Operatoren, die zwischen Ladungssektoren wechseln. Geeignete zusätzliche Daten sind:

- eine physisch graduierte Feldalgebra einschließlich ungerader Generatoren und ihrer gemischten Korrelatoren;
- oder, im Anwendungsbereich der Doplicher--Roberts-Rekonstruktion, ein lokales Observable-Netz mit den dort verlangten Sektoren endlicher Statistik und symmetrischer Tensor-Kategorie, aus der Feldalgebra und kompakte Eichgruppe rekonstruiert werden können;
- sowie die Wirkung der Zeittranslation auf diesen geladenen Generatoren.

Der jüngste exakte interne Gegenzeuge lokalisiert die fehlende Information innerhalb seiner ausdrücklich eingeschränkten Datenklasse. Für

\[
\mathcal B_{\rm even}=M_4\oplus M_4,
\qquad
H_\Delta=H_+\oplus(H_-+\Delta I)
\]

ist die gesamte gerade Dynamik unabhängig von \(\Delta\). Für einen blockwechselnden geladenen Operator \(X=P_-XP_+\) gilt dagegen

\[
\alpha_t^{(\Delta)}(X)
=e^{it\Delta}e^{itH_-}Xe^{-itH_+}.
\]

Im einfachen positiven Grundzustandsbeispiel ändert sich die euklidische geladene Zweipunktfunktion als \(e^{-\Delta t}\), während Zustand und alle geraden Mehrzeitdaten gleich bleiben (`source-charged-extension-selection-20260921/PROOF.txt:66-106`). Damit bestimmen **diese scoped geraden Daten** die geladene Zeit nicht. Der Vertrag sagt selbst, dass seine Familie nicht alle P1/P2-Bedingungen oder eine künftige gemeinsame Clock-Realisierung erfüllen muss (`PROOF.txt:26-30`); daraus folgt kein Gegenmodell zur vollen, erst noch zu präzisierenden P1-Axiomatik.

Eine vollständige Gibbs-Dichte auf **beiden** Blöcken könnte den relativen Offset bedingt bestimmen:

\[
\Delta=\beta^{-1}\log\frac{Z_-w_+}{Z_+w_-},
\]

aber die KMS-Bedingung auf der direkten Summe allein legt die zentralen Gewichte \(w_\pm\) nicht fest. Das ist ein präzises Beispiel für fehlenden Zustandsinput, kein allgemeines No-Go.

## 6. Ergebnis nach Datenart

| Zielgröße | Aus P1 allein | Aus P1 + endlichem \(T\) | Mit vollständigem OS/GNS-Datum |
|---|---|---|---|
| Normierung | \(c_3=1/(8\pi)\) | zusätzlich normierter 3-Zustands-Kanal | im Funktional enthalten |
| Algebra | nicht festgelegt | nicht festgelegt | muss vorgegeben oder als Wortalgebra samt Relationen im Datum enthalten sein |
| Neutraler Zustand | kein vollständiger Zustand | stationärer Vektor nur auf dem 3D-Ausleseraum | \(\Omega\) und \(\omega\) werden rekonstruiert |
| Höhere Korrelatoren | nicht festgelegt | nicht festgelegt | alle \(S_n\); nur quasifrei aus \(S_2\) |
| Geladene Felder | nicht festgelegt | nicht festgelegt | nur wenn geladene Generatoren/Korrelatoren oder Superselektionsdaten enthalten sind |
| Zeit | keine Translationshalbgruppe definiert | \(Q=\log T\), dimensionslose dissipative Auslesezeit | \(H\ge0\) aus OS-Translationshalbgruppe; physische Einheit weiter zu kalibrieren |
| Unitarität/Lokalität | nicht festgelegt | nicht festgelegt | folgt nur unter vollständigen OS-/Wightman-Voraussetzungen |

### Operator- und Premisseninventar

| Objekt | Im Original tatsächlich gegeben | Status und genaue Stelle | Was dadurch feststeht | Noch benötigte Prämisse |
|---|---|---|---|---|
| P1-Randkern | kein explizites `K(x,y)`, sondern RP, Orientierung, `[u_Σ]=1`, `c3=1/(8π)` | `tfpt_1_architecture_e8.tex:163-176`; `status_ledger.csv:2` | Normierung und deklarierte Positivitätseigenschaft | Feldalphabet, Algebra, Argumentraum, vollständiges Funktional, Translation |
| rohe Calderón-Abbildung `C_Σ` | semantisches Ziel einer RP-Randabbildung | `status_ledger.csv:257`; `tfpt_research_contracts.tex:299-340` | formuliert den nötigen Operatorvergleich | Gleichheit mit der `μ4`-äquivarianten freien `c=8`-Kontraktion ist offen; v178 löst nur einen endlichen multiplikitätsfreien Block |
| endlicher Auslesetransfer `T` | die oben angegebene exakte 3×3-Matrix | `verification/v221_seam_qecc.py:39-65`; `tfpt_research_contracts.tex:12726-12760` | Spektrum, stationärer Vektor, diskrete Relaxation | Einbettung in eine Feldalgebra oder in den rohen Calderón-Operator |
| `Q=log T` | exakter reeller Hauptlogarithmus | `verification/v971_markov_embedding_generator.py:1-50,61-70,90-152`; `tfpt_research_contracts.tex:12726-12775` | positive klassische Markovhalbgruppe auf dem 3D-Raum | physische Zeiteinheit, Lorentz-/unitäre Fortsetzung, Feldwirkung |
| quasifreier Lift `Γ(t)` | Bogoliubov-Zweitquantisierung **unter angenommener Identifikation** | `tfpt_research_contracts.tex:10739-10760` | voller Wick/Pfaffian-Transfer, falls 16-Majorana-CAR und Einteilchenkontraktion bereits feststehen | Nachweis, dass der rohe Naht-/RG-Transfer tatsächlich dieser `t` ist |
| mikroskopische geladene CAR-Felder | `Ψ_N(g)` samt Adjungierten und Mehrzeitmomenten für eine gewählte QWZ-Quelle | `experiments/theory-contracts/microscopic-charged-car-limit/README.md:1-22,48-67,193-202,250-266` | bedingtes geladenes Feldmodell mit wirklicher Zeitentwicklung | P1-Herkunft, acht Kanäle, Halb-Ladung und Identifikation mit der physischen Naht |
| relativer Sektoroffset `H_Δ` | exakte Familie auf `M4 ⊕ M4` | `source-charged-extension-selection-20260921/PROOF.txt:66-106` | zeigt innerhalb der angegebenen geraden Datenklasse die fehlende relative geladene Zeit; Gibbs-Datum kann `Δ` bedingt invertieren (`:108-141`) | Beweis, dass die vollständige P1-Quelle gerade diese Datenklasse und den gemeinsamen Zustand liefert |
| volle Fock-Rekonstruktionen | Rekonstruktionssätze unter irreduzibler 64-CAR/60-CCR-Fockdarstellung, globalen Antworten und gemeinsamer Domäne | `source-mixed-response-reconstruction-20260921/contract_index.json:8-12,42-47`; `source-stable-low-charge-reconstruction-20260921/contract_index.json:17-21,37-42` | vollständiger/stabiler Generator innerhalb dieser angenommenen Darstellung | gemeinsame geladene Quelldictionary, Quelljets, Zustand und physische Zeit aus P1/P2 |

Hier sind drei Begriffe getrennt zu halten: `T` ist zunächst ein endlicher **Auslese-/RG-Relaxationstransfer**; `e^{tQ}` ist seine kontinuierliche **dissipative Markovzeit**; ein `e^{-itH}` auf der rekonstruierten Feldtheorie wäre **reversible physische Zeit**. Die erste Größe ist exakt vorhanden, die zweite auf dem 3D-Raum exakt konstruiert, der Übergang zur dritten ist im Original nicht bewiesen.

### Audit der späteren Verträge

Kein bis 21. September 2026 geprüfter späterer Vertrag liefert eine aus P1 abgeleitete vollständige geladene Transferwirkung. Die stärksten positiven Ergebnisse sind bedingte Rekonstruktionen:

- `source-current-operator-time-20260921/contract_index.json:32-49` findet einen kanonischen Stromquotienten, verlangt aber weiterhin einen quellenbestimmten GNS-/Zeitadapter.
- `source-joint-response-20260921/contract_index.json:41-50` konstruiert die gemeinsame Antwort nur innerhalb einer spezifizierten bedingten Quelle; Herkunft von Quelle, Zustand und Zeit sowie die volle multiplikative CAR/CCR-Abbildung bleiben offen.
- `source-mixed-response-reconstruction-20260921/contract_index.json:8-12,42-47` und `source-stable-low-charge-reconstruction-20260921/contract_index.json:17-21,37-42` rekonstruieren einen Generator aus starken globalen Fock-/Antwortannahmen; genau die P1-Herkunft dieser Annahmen ist nicht hergeleitet.
- `source-maxwell-field-transfer-20260921/contract_index.json:37-47` liefert eine bedingte elektrische Dressing-Aussage, nicht den nativen Quell- oder Feldtransfer.
- `source-localized-spinor-20260919/contract_index.json:18-22` hebt beschränkte Quellwörter bedingt in einen bekannten lokalisierten Sektor; es konstruiert weder das mikroskopische geladene Feld noch die Präparation noch den rohen P1-Kern.

Damit ist die stärkste konstruktive Route bereits sichtbar, aber ihre Startdaten sind noch nicht aus P1 gewonnen: (i) gemeinsame lokale/gradierte CAR/CCR-Algebra, (ii) vollständiges positives Wortfunktional oder ein hinreichender quasifreier Projektorsatz, (iii) gemeinsame euklidische Translation auf neutralen und geladenen Generatoren, (iv) OS/GNS-Rekonstruktion, (v) Operatoridentität des endlichen `T` mit einer Einschränkung der rekonstruierten Halbgruppe und erst danach der kontrollierte lokale Grenzwert.

## 7. Wo genau die offene Arbeit liegt

Die erste offene Kante ist nicht „finde einen neuen Rekonstruktionssatz“. Der Satz existiert. Sie lautet:

Im geprüften Quellenpfad gibt es **keine bewiesene Herleitung**

\[
\text{P1-Skalar/Zweipunktkern + 3D-Auslesetransfer}
\longrightarrow
\text{vollständiges positives Feldfunktional auf einer geladenen lokalen Algebra}.
\]

Das ist eine Aussage über den dokumentierten Beweisstand. Sie wird hier nicht als axiomatisches No-Go formuliert, weil kein Paar vollständiger Gegenmodelle geprüft wurde, das sämtliche Bedingungen einer formal ausbuchstabierten P1-Axiomatik erfüllt.

Um die OS/GNS-Rekonstruktion anzuwenden, muss die ursprüngliche Quelle herleiten:

1. die lokale/gradierte Wort- oder CAR-Algebra und die physische Gradierung;
2. ein vollständiges positives Funktional auf allen Wörtern — oder Quasifreiheit als echten Quellsatz;
3. die euklidische Translationswirkung auf neutralen **und** geladenen Generatoren;
4. die Identifikation des endlichen \(T\) mit der Einschränkung dieser Halbgruppe;
5. Regularität, Kovarianz, Clusterung und einen kontrollierten Kontinuumsgrenzwert.

Danach sind zwei echte mathematische Pflichten übrig:

- **`QGEO.KERNEL.01`**: die rohe RP-Calderón-Abbildung ist als Operator tatsächlich die \(\mu_4\)-äquivariante freie, gapped Einteilchenkontraktion, nicht nur isospektral;
- **`SEAM.EQUIV.01` / `SEAM.MMST.TYPEIII.CHARGED.01`**: der geladene lokale Skalierungsgrenzwert und die Netzerweiterung existieren mit der erforderlichen gemeinsamen Adjungierung, Zeit und Positivität.

Die jetzige Lage ist daher zweistufig:

- **fehlender Input beziehungsweise fehlende Herkunftsherleitung** zwischen P1/\(T\) und dem vollständigen Feldfunktional;
- **echter konstruktiv-analytischer Beweis** für Operatoridentität und Kontinuumsgrenzwert, sobald dieser Input unabhängig definiert ist.

Das Ergebnis widerlegt weder TFPT noch die Möglichkeit, dass eine künftige stärkere P1-Formulierung alles rekonstruiert. Es zeigt präzise, welches Objekt P1 dafür sein müsste: nicht eine Zahl und nicht nur ein Zweipunktkern, sondern ein reflexionspositives, kompositionsverträgliches Funktional auf der vollständigen neutralen und geladenen Prozessalgebra samt Translationswirkung.

## 8. Quellenbasis (19, Theoriegraph zuerst)

### TFPT-Originalquellen

1. `verification/theory_primer.md` und Claim-Dossiers `AX.P1.01`, `AX.P2.01`, `QGEO.KERNEL.01`, `SEAM.EQUIV.01` — aktueller Graph: 5950 Knoten, 64057 Kanten, 260 Contracts.
2. `tfpt_1_architecture_e8.tex:163-176`, `:1543-1546`, `:1610-1623` — P1-Definition und spätere Zweipunkt-/Quasifreiheitslesart.
3. `verification/status_ledger.csv:2`, `:257`, `:381`, `:1171` — verbindliche Typisierung von P1, Kernidentifikation, Seam Equivalence und geladenem Skalierungsgrenzwert.
4. `tfpt_research_contracts.tex:423-435`, `:10658-10674`, `:10729-10737`, `:12726-12775` — RP/OS-Rekonstruktion, Gauß-/Wick-Voraussetzung, voller Schwingerkegel und drei Dynamikbegriffe.
5. `origin_theory.tex:1730-1765` — „one scalar two-point kernel“ und ehrliche Realisierungsgrenze.
6. `experiments/theory-contracts/universalraum-primitive-source-audit-20260915/RESULTS.md:146-193,203-220` — GNS-/Gram-Rekonstruktion aus einem vollständigen positiven Prozesskern; Restoperator \(R_a\).
7. `experiments/theory-contracts/compiler-kernel-foundation-20260914/EINFACH.md:67-83,95-115` — Komposition und positive Ablaufbewertung; physische Ausführungswahl bleibt offen.
8. `experiments/theory-contracts/primitive-transfer-selection-20260912/FOUR_PRIMITIVE_PROCESS.md` und `SIMPLE_TYPED_BRIDGE.md` — explizite Zusatzhypothesen der Prozess- und DtN-Lesarten.
9. `experiments/theory-contracts/microscopic-charged-car-limit/README.md:1-22,48-67,193-202,250-266` — bedingte mikroskopische CAR-Felder, beide Adjungierte und Mehrzeitmomente; keine P1-Auswahl der geladenen Erweiterung.
10. `experiments/theory-contracts/charged-source-time-audit-20260920/README.md` — neutrale Ströme sind für den Viertelholonomie-Quellterm blind; geladene Operatoren sehen ihn.
11. `experiments/theory-contracts/source-charged-extension-selection-20260921/PROOF.txt` — exakte relative Sektorzeit-Unterbestimmung und bedingte Gibbs-Inversion.
12. `verification/v221_seam_qecc.py:39-65` — Definition und Spektrum des endlichen Transfers.
13. `verification/v971_markov_embedding_generator.py:1-50,61-70,90-152` — exakter Hauptlogarithmus und Markovhalbgruppe; unitäre Feldzeit bleibt offen.
14. Spätere Quellverträge `source-current-operator-time-20260921`, `source-joint-response-20260921`, `source-mixed-response-reconstruction-20260921`, `source-stable-low-charge-reconstruction-20260921`, `source-maxwell-field-transfer-20260921` und `source-localized-spinor-20260919` — positive bedingte Rekonstruktionen und ihre explizit nicht hergeleiteten P1-/Zeit-/Zustandsdaten.

### Primärliteratur

15. K. Osterwalder, R. Schrader, [Axioms for Euclidean Green's functions](https://doi.org/10.1007/BF01645738), *Commun. Math. Phys.* **31** (1973), 83–112 — vollständige Familie euklidischer Greenfunktionen und Rekonstruktion.
16. K. Osterwalder, R. Schrader, [Axioms for Euclidean Green's functions II](https://doi.org/10.1007/BF01608978), *Commun. Math. Phys.* **42** (1975), 281–305 — korrigierte/härtere Regularitätsvoraussetzungen.
17. R. van Leeuwen, G. Stefanucci, [Wick Theorem for General Initial States](https://arxiv.org/abs/1102.4814), *Phys. Rev. B* **85** (2012), 115119 — allgemeine Anfangszustände verlangen die entsprechende Korrelationshierarchie; die gewöhnliche Wick-Reduktion ist der unkorrelierte/quasifreie Sonderfall.
18. C. J. Fewster, B. Lang, [Pure quasifree states of the Dirac field from the fermionic projector](https://arxiv.org/abs/1408.1645), *Class. Quantum Grav.* **32** (2015), 095001 — konstruiert einen reinen quasifreien CAR-Zustand nur nach Vorgabe von Raumzeit, Diracfeld, CAR-Algebra und Projektordaten; ein Projektor kann in dieser engeren Klasse ausreichend sein.
19. S. Doplicher, J. E. Roberts, [Why there is a field algebra with a compact gauge group describing the superselection structure in particle physics](https://doi.org/10.1007/BF02097680), *Commun. Math. Phys.* **131** (1990), 51–107 — Feldalgebra/Eichgruppe aus lokalem Observable-Netz und passender Superselektionsstruktur; keine automatische Anwendung auf eine chirale, gebraidete Kategorie und keine Rekonstruktion aus einem isolierten neutralen Zweipunktkern.
