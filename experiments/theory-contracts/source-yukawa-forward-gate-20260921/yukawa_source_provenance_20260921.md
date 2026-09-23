# Audit: Quellenherkunft des Dirac-/Yukawaoperators

Stand: 2026-09-21  
Scope: read-only audit; keine neue Hilfskonstruktion, keine Statuspromotion

## Urteil

Der stärkste vorhandene **exakte Operator-Satz** ist weiterhin `PS.DIRAC.03`/v258: Für eine bereits gelieferte treue quasi-freie Kovarianz

\[
C=(1+e^{H/\mu})^{-1}
\]

rekonstruiert der Logit

\[
H=\mu\log((1-C)C^{-1})
\]

den eingesetzten hermiteschen Operator, einschließlich eines chiralen Diracblocks, exakt. Das ist eine korrekte Inversion und ein sauberer bedingter Übersetzer von **Kovarianz zu Operator**. Es ist keine Vorwärtsherleitung der Yukawas aus der Naht.

Die erste unbewiesene tragende Prämisse ist genau die im Ledger nur mit `[C]` markierte Identifikation

\[
C_F=V_F^*C_\Sigma V_F
\qquad
(\text{äquivalent auf dem großen Raum: }P_FC_\Sigma P_F,
\;P_F=V_FV_F^*),
\]

wobei `C_Σ`, die quellengewählte Trägerisometrie `V_F` beziehungsweise der physische Projektor `P_F`, die Chiralitäts-/Feldidentifikation und die vollständige, gegebenenfalls nichtautonome effektive Zeitentwicklung **vor dem Vergleich mit den Ziel-Yukawas** aus denselben ursprünglichen Nahtdaten konstruiert sein müssen. Kein im Audit geprüfter Quellenpfad liefert derzeit dieses gemeinsame Paket.

Es gibt zwei stärkere Teilanschlüsse als die bloße v258-Inversion, aber keiner schließt diese Prämisse:

1. v724 konstruiert zielunabhängig einen konkreten 6-dimensionalen Mutterzustand, vier Rang-3-Graphkompressionen und ihre modularen Generatoren aus Sheet-/Compilerdaten. Dies ist der stärkste vorhandene **Konstruktionsbauplan** für `Quelle → Kovarianz → Kompression → Generator`. Er ist jedoch weder der rohe Calderónzustand von `QGEO.KERNEL.01` noch der 18/96-dimensionale fermionische Trägerprojektor von `PS.DIRAC.03`; seine vier Projektionen sind Graphen der Flavoroperatoren `J,K,C,F`. Außerdem verfehlt die Konstruktion die vorgesehenen vier Dynamikklassen und endet korrekt mit `T3B-DEAD`.
2. Die jüngeren Lean-Module beweisen die algebraische Form der Stage-D-Schnittstelle und konstruieren aus einer **schon gegebenen dreidimensionalen Basis** eine Determinanten-Trilinearform. Sie definieren aber keinen Quellenkernel, keinen Higgs-/Materie-Overlap und keinen Diracoperator. `BoundaryYukawaKernelInterface.lean` sagt ausdrücklich, dass der Pfeil vom TFPT-Randkernel zur Schnittstelle nicht formalisiert ist.

Ein vorhandener **direkt ausgewerteter affiner Dreipunkttensor** ist der E8-Tensor aus `UR.SOURCE.FLAVOR_ORIGIN.01`: Er besitzt reale Down-/Lepton-Slots, aber sein Familientensor ist antisymmetrisch. Mit einem Higgs-Familienvektor entsteht eine Rang-2-Matrix mit Singularwerten `(||h||, ||h||, 0)`; in der direkten lokalen gleichartigen 4D-Weyl-Lesart verschwindet die Kopplung wegen der Austauschsymmetrie. Das ist eine positive Herkunftsaussage plus ein scharfer Ausschluss dieser direkten Lesart. Es widerlegt weder die geschlossenen Flavorverhältnisse noch jede mögliche Spinor-Yukawakopplung.

Daneben ist die symmetrische 820-Produktkarte mit der Zerlegung `100+720` ein echtes vollständiges Stromprodukt und besitzt die richtige lokale Weyl-Austauschsymmetrie. Damit ist sie strukturell mehr als eine Dimensionsanalogie. Der bisher verschwindende `O820`/Vektor-Majorana/Vektor-Majorana-Korrelator betrifft jedoch nur diese getestete Feldlesart. Weder die Produktkarte selbst noch dieser Nullbefund liefern bereits die physische Identifikation der Spinor- und Higgsfelder, einen lokalen Wirkungs- beziehungsweise Hamiltonterm oder dessen gemeinsame Quellenzeit. Deshalb ist auch dieser Kanal noch keine Vorwärtsherleitung des Yukawaoperators.

## Was exakt belegt ist

### 1. v258 invertiert die von ihm selbst erzeugte Kovarianz

In `verification/v258_dirac_covariance_induction.py:79-157` läuft die Datenrichtung in den entscheidenden Tests so:

1. Ein zufälliger Yukawablock `Y` beziehungsweise neun bereits vorgegebene geladene Massen werden zu `Dblk`/`Dmass` zusammengesetzt.
2. `kms_cov(D)` erzeugt daraus `C`.
3. `induce(C)` rekonstruiert `D`.
4. Der physische Satz `C_F=P_F C_Σ P_F` wird am Ende mit `check(..., True)` registriert.

Der heutige Einzelrun ergab `6 passed, 0 failed`. Das bestätigt die implementierten Identitäten. Es bestätigt nicht die Herkunft von `C_Σ` oder `P_F`. Insbesondere funktioniert dieselbe Rückrechnung für andere eingegebene Massen. Die Aussage „Majorana ist ein Kovarianzeintrag“ ist exakt **unter dem eingesetzten Majoranablock**; der Code leitet diesen Block nicht aus der Naht her.

Das Ledger trennt diese Ebenen selbst: `PS.DIRAC.03` ist `[E]` für Inversion, Positivität, Dirac-Ungeradheit, Spektrumsrückgewinnung und den bedingten Seesawblock, aber nur `[C]` für die physische Kompression. `CONTRACT.QFT4D.DIRAC.01` sagt außerdem ausdrücklich, dass die geladenen Yukawas bereits durch die Flavor-Schicht festgelegt sind und der offene Test die NCG-/Quellenkonsistenz von `D_F` ist.

### 2. v724 liefert eine echte, aber anders typisierte Vorwärtskonstruktion

`verification/v724_phys_t3b_modular_flows.py:156-199` baut ohne Zielklassen im Konstruktor:

- den Sheet-Tangentenoperator `S = Q diag(0,1,1)`;
- den chiralen Mutteroperator `D_Σ=[[0,S],[Sᵀ,0]]`;
- einen treuen KMS-Mutterzustand `C_Σ`;
- vier kanonische Graphisometrien aus `J,K,C,F` und damit vier Rang-3-Projektoren;
- komprimierte Kovarianzen und deren modulare Generatoren;
- eine gemeinsame KMS-Skala und eine stabile endliche Leiter.

Der heutige Einzelrun bestätigte unter anderem:

- `spec(C_Σ)=[0.04403723080377, 0.9559627691962]`;
- vier zielunabhängige Rang-3-Projektoren;
- eine stabile Leiter mit beobachteter Ordnung ungefähr 2;
- Connes-Kozykelkomposition bis etwa `1.6×10^-15`;
- eine einzige KMS-Skala `Δ=2.432790648649`.

Doch die harten Zielklassen scheitern sowohl rein modular als auch mit dem getesteten GKSL-Zusatz; das Modul gibt `VERDICT: T3B-DEAD` aus. Für diesen Audit ist noch grundlegender:

- `D_Σ` wird aus der schon vorhandenen Sheet-/Flavor-Matrix `Q` gebaut, nicht aus dem rohen RP-Calderónoperator;
- die Projektoren komprimieren auf Graphen der 3×3-Operatoren `J,K,C,F`, nicht auf den chiralen 18- oder 96-dimensionalen Materieträger;
- es gibt keine Abbildung auf lokale Spinorfelder, Higgsfeld und die neun geladenen Yukawaeinträge;
- die im Modul auftretende `F`-Graphprojektion ist nicht der physische fermionische `P_F` aus `PS.DIRAC.03`.

v724 zeigt deshalb, wie ein nichtzirkulärer Test aussehen muss. Es liefert nicht die gesuchte physische Kompression.

### 3. Die Lean-Yukawatürme sind genaue Schnittstellen, keine Quellenherleitung

`YukawaTrilinearForm.lean:83-153` nimmt als Primärdatum eine lineare Form

\[
\omega:\Lambda^3E\to K
\]

und definiert daraus die Kontraktion. Aus Injektivität plus Surjektivität folgt in endlicher, nichttrivialer Dimension `dim E=3`. Dieser Satz ist exakt und nützlich: Er sagt präzise, was ein erfolgreicher Quellenkernel liefern müsste.

`YukawaStageDExistence.lean:73-97, 291-327` geht in der Gegenrichtung vor: Aus `dim E=3` wird eine Basis gewählt, deren Determinante als `ω` benutzt wird. Damit ist die Existenz einer Stage-D-Form äquivalent zur bereits bekannten Dreidimensionalität. Die Konstruktion liefert keine quellenkanonische Form, keine Norm, keine Phase und keine physische Wechselwirkung.

`BoundaryYukawaKernelInterface.lean:18-57` markiert die Grenze unmissverständlich: Die Gleichheit der quellenproduzierten Form mit dem basisgebauten Zeugen ist offen; das Modul verpackt nur das Ziel. Die Struktur in Zeilen 86-93 enthält `ω`, Injektivität, Surjektivität und Nichttrivialität bereits als Felder. Der Konstruktor `ofFinrankEqThree` in Zeilen 117-126 baut dieselbe Struktur wieder aus einer gewählten Basis.

Auch die Higgs-Seite ist noch eine Schnittstelle: `HiggsTopForm.lean:162-208` nimmt eine lineare Äquivalenz des positiven Blocks mit dem algebraischen Schatten von `H⁰(P¹,O(1))` an. Sie konstruiert keinen gemeinsamen Higgs-/Materie-Overlap aus der Naht.

### 4. Direkt ausgewertete Dreipunktstrukturen sind noch keine physische Yukawaherleitung

`experiments/theory-contracts/source-flavor-origin-20260920/PROOF.txt:97-149` verwendet den vorhandenen affinen Tensor

\[
C_{(A,i)(B,j)(C,k)}=d_{ABC}\,\epsilon_{ijk}.
\]

Die echten Koeffizienten besitzen nichtverschwindende Down- und Lepton-Slots. Das ist stärker als eine Dimensionsanalogie. Die Familienkontraktion mit einem einzelnen Higgsvektor ist jedoch

\[
A(h)_{ij}=\epsilon_{ijk}h_k,
\qquad A(h)h=0,
\qquad \operatorname{rank}A(h)=2.
\]

Für dieselben lokalen Weylfelder ist der Lorentz-Skalar symmetrisch im kombinierten Feldlabel, während `d·ε` dort antisymmetrisch ist; die direkte lokale Kopplung verschwindet. Der Contract nennt deshalb in Zeilen 171-205 die kleinste fehlende Masseninformation: echte Quellenmatrixelemente `b,c` mit

\[
\det M_{\rm full}=-(h^Tb)(c^Th).
\]

Vollrang erfordert beide nichtverschwindenden Overlaps. Ein komplexer schwerer Masseneintrag allein repariert weder Rang noch physische Phase.

`UR.SOURCE.CRITICAL_FIELDS.01` konstruiert zusätzlich konkrete lokale ungerade Spinorfeldvektoren und ihre Ladungen. Der zugehörige Flavorblock bleibt aber Rang 2; ein bedingter Vierkomponentenweg benötigt eine zusätzliche Triplet-/Singulettkopplung, die weder durch die Higgs-Realstruktur noch durch den ursprünglichen Hamiltonoperator gewählt ist (`source-critical-local-fields-20260920/ERGEBNIS.md:144-183`).

Die symmetrische 820-Produktkarte erhält demgegenüber das vollständige Stromprodukt in den Komponenten `100+720` und passt zur lokalen Weyl-Austauschsymmetrie. Offen bleibt der physische Pfeil von diesen algebraischen Komponenten zu den tatsächlichen Spinor-/Higgsfeldern und zu einem lokalen Wirkungs- oder Hamiltonterm. Das Nullresultat des bislang geprüften `O820`/Vektor-Majorana/Vektor-Majorana-Korrelators ist daher kein Nullresultat für die ganze Produktkarte und kein No-go für Spinor-Yukawas.

## Bestandsmatrix: tatsächliche Daten, Bedingungen, fehlende Eingaben

| Bestandteil | Tatsächlich vorhanden | Nur bedingt/zusätzlich gewählt | Noch fehlend für `PS.DIRAC.03` |
|---|---|---|---|
| Rohzustand / `C_Σ` | v724: konkrete 6×6-KMS-Kovarianz aus Sheet-Tangente; v113-Kontext: reine CAR-Polarisation | Identifikation dieses Zustands mit dem rohen RP-Seam-Calderónzustand | Operatorgleichheit `QGEO.KERNEL.01`: rohes `C_Σ=U^-1 C_{μ4}U` samt physischer Dynamik |
| Projektion | v724: vier mathematische Graphprojektoren, Rang 3 | Wahl der Graphen `J,K,C,F`; keine Materiefeldinterpretation | Quellenkanonische Isometrie `V_F` auf den chiralen Materieträger; `P_F=V_FV_F*` |
| Interne 3+2-Auswahl | Compiler-/Darstellungsdaten downstream vorhanden | Separater interner Involutionsoperator wäre konsistent | Ableitung dieses Operators aus einem zusätzlichen rohen Quelloperator; die reine Polarisation besitzt U(5)-Symmetrie und wählt keine Dreiebene |
| Yukawa-Trilinearform | Exakte Lean-Sätze über eine gelieferte `ω`; basisgebauter Existenzzeuge bei `dim=3` | `BoundaryYukawaKernel` enthält `ω`, CI und CS als Daten | Konstruktion der kanonischen `ω` aus dem tatsächlichen Randkernel und Nachweis, dass sie denselben Feld-/Zeitkanal nutzt |
| Higgs-/Materie-Overlap | Affiner E8-Tensor mit echten Down-/Lepton-Slots; symmetrische 820-Produktkarte mit vollständigem `100+720`-Stromprodukt und passender Weyl-Symmetrie; lokale ungerade Spinorkandidaten | Einzelnes Higgs-Familientriplet; bedingter komplementärer Vierkanal; getestete Vektor-Majorana-Lesart | Physische Spinor-/Higgsidentifikation, nichtverschwindende quellenberechnete Overlaps, gemeinsame Statistik und lokaler Wirkungs-/Hamiltonterm |
| Zeitentwicklung | v724: gemeinsamer modularer Bauplan; andere Source-Contracts: konkrete bedingte Dynamiken | Gemeinsame Clock-Bedingung bzw. gewählte kritische Energie | Quellenbegründete volle Zeitentwicklung: bei nichtinvarianter Kompression einschließlich Leckage/Gedächtnis, oder unabhängig ausgewählter gemischter globaler KMS-Zustand |
| Diracoperator | v252: 96D-Slots/NCG-Struktur; v258: exakte Kovarianzinversion | Eingesetzte neun Massen und Majoranablock | Vorwärts berechnetes `C_F`, dessen Logit ohne Zielmassen denselben `D_F` ergibt |

## Warum die reine Nahtkompression derzeit nicht funktioniert

`UR.RAW_CARRIER_ORIGIN.01` lokalisiert das erste Hindernis noch vor dem Yukawaoperator:

- Wird der Träger wörtlich in die positive Polarisation `Ran P_+` komprimiert und dieselbe Involution eingeschränkt, bleibt nur das Pluszeichen; `E_-=0`.
- In einer reinen selbstdualen CAR-Polarisation paaren sich Plus und Minus unter der Realstruktur; auf einem stabilen endlichen Raum sind ihre Dimensionen gleich, nicht 3+2.
- Auf `E=Ran C` ist der natürliche Stabilisator `U(5)`. Jeder aus diesen Daten allein natürliche komplexlineare Operator ist skalar. Eine Dreiebene `W⊂E` und damit die 3+2-Involution ist eine Wahl im Raum `U(5)/(U(3)×U(2))`, keine Folge der Polarisation.
- Der Betrag eines vollen Quelloperators könnte diese Symmetrie brechen; sein Vorzeichen beziehungsweise seine reine Kovarianz allein enthält diese Information nicht.

Damit ist `P_F` nicht nur „noch nicht hingeschrieben“. Die aktuell benannten Rohdaten bestimmen ihn ohne zusätzliche, aber möglicherweise bereits physisch vorhandene Operatorstruktur nicht eindeutig.

Eine zweite, unabhängige Grenze betrifft die Zeit. Sei `C_Σ=C_Σ²` ein reiner Spektralprojektor und `Q=I-P_F`. Dann gilt für die Kompression exakt

\[
C_F(1-C_F)=(Q C_\Sigma P_F)^*(Q C_\Sigma P_F).
\]

Eine treue endliche Kovarianz `0<C_F<I` verlangt daher eine vollrangige Kopplung an den ausgeschlossenen Sektor. Ist zugleich `C_Σ` der Spektralprojektor desselben vollen Generators `h` und soll `P_F` dessen Zeit exakt autonom reduzieren, dann folgt `[P_F,h]=0`, also auch `[P_F,C_Σ]=0`; damit ist `C_F²=C_F`. Der endliche treue Logit von v258 ist dann unmöglich. Eine gangbare Quellenkonstruktion muss deshalb entweder einen unabhängig ausgewählten gemischten globalen KMS-Zustand liefern oder bei reiner globaler Kovarianz die nichtinvariante Kompression samt Leckage, Gedächtnis und voller effektiver Zeit physisch herleiten.

## Kleinster entscheidender konstruktiver Schritt

Der nächste Schritt sollte kein neues Effektivmodell und keine weitere Inversion sein. Er ist ein **quellenreiner Kompressions- und Zeitentwicklungssatz** mit einer harten Datenfluss-Firewall:

1. **Eingabe ausschließlich aus der ursprünglichen Quelle:** roher Seam-Operator beziehungsweise vollständiger Quellgenerator, Realstruktur, Ladung/Graduierung, Zustand und volle Zeitentwicklung. Keine v18/v252-Massen, keine Ziel-Yukawamatrix, keine nachträgliche 3+2-Basiswahl.
2. **Konstruiere eine physisch begründete Isometrie**
   \[
   V_F:H_F^{\rm finite}\longrightarrow H_\Sigma
   \]
   auf den tatsächlich lokalen ungeraden Materiesektor, so dass `P_F=V_FV_F*` aus den vollen Quelldaten folgt. Prüfe dabei Feldtyp, Ladung, Chiralität und Realstruktur. Fordere nicht pauschal `[P_F,h]=0`: Bei reiner Spektralprojektor-Kovarianz würde genau diese Invarianz die benötigte treue Kompression verhindern.
3. **Schließe Zustand und Zeit gemeinsam.** Es genügt eine der beiden physisch hergeleiteten Alternativen:
   - ein unabhängig quellengewählter gemischter globaler KMS-Zustand, dessen Kompression treu ist und dessen Dynamik zum Feldkanal passt;
   - oder eine reine globale Kovarianz mit `Q C_Σ P_F≠0`, wobei die nichtautonome reduzierte Zeit durch die komprimierte Resolvente beziehungsweise den Feshbach-Selbstenergieterm einschließlich Leckage/Gedächtnis bestimmt wird.
4. **Berechne vor jedem Zielvergleich**
   \[
   C_F=V_F^*C_\Sigma V_F,
   \qquad
   D_F^{\rm src}=\mu\log((1-C_F)C_F^{-1}).
   \]
   Der Konstruktor muss byte-/AST-seitig frei von Zielmassen und Zielmatrizen sein, analog zur brauchbaren Firewall von v724.
5. **Erstes Ja/Nein-Gate:** Prüfe gleichzeitig Treue, Chiralität und Zeitkonsistenz:
   \[
   0<C_F<I,
   \qquad
   \gamma_F C_F\gamma_F=I-C_F,
   \qquad
   C_F(1-C_F)=(Q C_\Sigma P_F)^*(Q C_\Sigma P_F).
   \]
   Danach ist zu prüfen, ob der chiralitätsungerade Block von `D_F^{src}` für Down und Leptonen Vollrang besitzt. In der direkt ausgewerteten affinen E8-Dreipunktdarstellung reduziert sich dieser Vollrangtest auf `hᵀb≠0` und `cᵀh≠0`. Erst nach diesen Gates darf das Ergebnis mit den bereits geschlossenen Flavorverhältnissen verglichen werden.

Ein negativer Ausgang wäre entscheidungsrelevant: Er schließt genau diese Quellenkompression aus, ohne `FLAV.QRATIO.01`, `FLAV.RIGID.02`, `FLAV.LEPTONC.01` oder `FLAV.UPOINT.01` zu berühren. Ein positiver Ausgang würde die bisher nur behauptete Vorwärtsrichtung von `PS.DIRAC.03` erstmals konkret herstellen; erst dann wäre die v258-Inversion mehr als eine korrekte Rückübersetzung.

## Bewahrte Flavor-Claims

Dieser Audit ändert keine geschlossene Flavoraussage:

- `FLAV.QRATIO.01`: Quarkverhältnisse auf dem abgeleiteten Selektorstratum geschlossen; absolute Skala bleibt separat.
- `FLAV.RIGID.02`: Verhältnisstarre auf `S_{8,Q}` geschlossen; kein Wiederöffnen durch den Quellenbefund.
- `FLAV.LEPTONC.01`: `c=(16/7,4/3,7/6)` exakt im angegebenen Leptonvertrag.
- `FLAV.UPOINT.01`: `[I]+[A]`; alle neun geladenen Amplituden bis auf den gemeinsamen Anker `v_geo` bestimmt.

Der offene Punkt ist die physische **Vorwärtsrealisierung dieser bereits festgelegten Daten als lokaler, quelleninduzierter Dirac-/Yukawaoperator**. Die symmetrische 820-Produktkarte mit `100+720` bleibt als vollständiges Stromprodukt erhalten; nur ihr bisher getesteter `O820`/Vektor-Majorana/Vektor-Majorana-Korrelator verschwindet. Dieser Nullbefund und der direkte Rang-2-Befund des affinen `d·ε`-Tensors betreffen konkrete Feldlesarten. Sie sind keine Widerlegung möglicher lokaler Spinor-Yukawas und keine Widerlegung der Flavorverhältnisse.

## Maßgebliche Originalquellen und bestätigte Review

1. `verification/status_ledger.csv`: `PS.DIRAC.03`, `CONTRACT.QFT4D.DIRAC.01`, `QGEO.KERNEL.01` und die vier bewahrten Flavorclaims.
2. `verification/v258_dirac_covariance_induction.py:65-157`: exakte Inversion und bedingter physischer Wahrheitscheck.
3. `verification/v724_phys_t3b_modular_flows.py:116-199,328-549`: konkrete Mutterkovarianz, Graphkompressionen, Zeitvergleich und `T3B-DEAD`.
4. `experiments/lean4-carrier-rigidity/TfptCarrier/BoundaryYukawaKernelInterface.lean:18-57,86-143`: explizite offene Rohkernel-Schnittstelle.
5. `experiments/lean4-carrier-rigidity/TfptCarrier/YukawaTrilinearForm.lean:76-220`: Form, Kontraktion und Rang-3-Satz.
6. `experiments/lean4-carrier-rigidity/TfptCarrier/YukawaStageDExistence.lean:43-54,73-97,291-327`: basisabhängiger Existenzzeuge und Äquivalenz mit Rang 3.
7. `experiments/lean4-carrier-rigidity/TfptCarrier/HiggsTopForm.lean:162-208`: algebraischer Higgs-Schatten als angenommene Äquivalenz.
8. `experiments/theory-contracts/raw-carrier-origin-gate-20260920/PROOF.txt:4-33,56-134,155-184`: Kompressions-, U(5)- und Calderónsymbolgrenzen.
9. `experiments/theory-contracts/source-flavor-origin-20260920/PROOF.txt:97-149,171-232`: tatsächlicher E8-Tensor, Rang-/Statistiktest und erforderliche Overlaps.
10. `experiments/theory-contracts/source-critical-local-fields-20260920/ERGEBNIS.md:50-183,194-249`: lokale ungerade Spinorkandidaten, bedingter Flavorweg und fehlende gemeinsame Quelle.
11. `experiments/theory-contracts/source-rg-clock-bridge-20260920/PROOF.txt:161-241`: Dynamikfamilie, Clock-Bedingung und präziser offener Rohkernelpfeil.
12. `work/covariance_compression_review_20260921.md`: exakte Gram-Identität, Chiralitätsbedingung und Unvereinbarkeit von reiner Spektralprojektor-Kovarianz, exakt autonomer Trägerzeit und treuem endlichem Logit.

Der Theoriegraph war beim Audit frisch (`THEORY-GRAPH OK`, 5954 Knoten, 64081 Kanten). Der Ledger bleibt für Statusaussagen maßgeblich; die Graphkanten wurden nur zur Quellensuche benutzt.
