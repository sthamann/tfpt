# Quellenkomposition: dieselben lokalen Vertices, verschiedene gemeinsame Fermionen

15. September 2026 · v1.6.9 · NON-RH · isolierter Quellenstrang

## Stärkstes neues Ergebnis

Die geprüfte Quelle bestimmt bereits **einen gemeinsamen lokalen CAR-Träger mit 64 Fermionmoden**, nicht 480 unabhängige Wechselwirkungsbanken. Jeder dieser Fermionmoden kommt in genau 15 der 480 nichtverschwindenden Vertices vor. Aber die Quelle bestimmt in den untersuchten Konstruktionen **noch keine Überlappung zweier vollständiger Kopplungs-Charts dieses Trägers**.

Das lässt sich durch ein genau geschlossenes Gegenmodell sichtbar machen: Zwei Modelle auf derselben Fockbasis mit 128 Fermion- und 120 Bosonmoden behalten jeden lokalen W-Koeffizienten, dieselbe Kopplung g, dieselbe Bosonenergie Δ, volles G = Spin(10) × SU(4), denselben passiven Clock und dieselbe erhaltene Gesamtzahl. Beide benutzen wirklich gemeinsame Fermionressourcen. Trotzdem ergeben sie verschiedene Übergangswahrscheinlichkeiten. Eine dimensionslose Kombination der ersten vier Energiemomente liest die zusätzlich gewählte Überlappung exakt wieder aus.

**Status:** exakter Satz über die hier angegebene Familie; kein Satz über alle Compiler, keine ausgewählte Raumgeometrie und keine Herleitung physischer Präparation oder Zeit.

## 1. Was die gelesenen Quellen tatsächlich zusammensetzen

Alle genannten Dateien sind in [inputs](inputs/) eingefroren; Originalpfade, Bytezahlen und SHA-256 stehen im [Manifest](inputs_manifest.json). Der Prüfer importiert keine beweglichen Repository-Dateien.

| Quellschritt | Tatsächlich gegeben | Nicht durch diesen Schritt gegeben |
|---|---|---|
| `verification/v566_parabolic_anchor_selfcode.py`, Konstanten 111–121 und S1 | U und V auf **demselben C³**; die sieben Wörter I,U,V,UV,VU,V²,VUV spannen eine 7-dimensionale, unter allen 49 Produkten geschlossene Algebra. Neu exakt nachgerechnet. | Neue Träger, Fockfaktoren, räumliche Nachbarschaft oder eine CAR-Einbettung von C³ in das spätere Modell. |
| `verification/v783_two_qubit_clifford.py`, P0/P1; `compiler-origin-audit-20260913/context_instrument.py`, 69–114 | 60 konkrete Gaußwurzelstrahlen auf **demselben C⁴**, ihre Projektoren und exakten Überlappungen. Neu aus dem gepinnten Originalpräfix rekonstruiert. | Die Identifikation dieses C⁴ mit einer G-trivialen Kopien-/Multiplizitätsebene des 64-Fermionmodells. |
| `universalraum-singlet-observable-20260915/sources/native_source.py`, 36–85, 132–220 | Aus fünf Hilfs-Jordan-Wigner-Moden, geradem Spinor und antisymmetrischem Farbfaktor entsteht W: Λ²C⁶⁴ → C⁶⁰. Die **physischen** 64 Fermionmoden werden gemeinsam benutzt. WWᵀ=8I; alle 60 Lie-Intertwiner werden geprüft. | Ein Ortsindex x, eine Zahl von Kopien, deren gegenseitige Antikommutatoren oder ein globaler Site-Tensor. Die fünf Hilfs-CAR-Moden des Cliffordbaus sind nicht die 64 physischen f-Moden. |
| `universalraum-native-operations-ground-response-20260915/common.py`, 1–17 | Das deklarierte native H und N=Nf+2Nb auf dieser einen Fockbank. | Ein Eindeutigkeitssatz, dass die ursprüngliche Compilergrammatik genau dieses physische H, g/Δ oder seinen Mehrteilträger erzwingt. |
| `compiler-origin-audit-20260913/record_composition.py` | Gegebene Kontext-Vormessungen lassen sich als Matrizen multiplizieren; kohärent wiederverwendete und frische Register sind unterschiedliche Prozesse. Schon der Header nennt die zusätzlichen Ressourcen. | Lieferung frischer Register, inter-Register-Kopplung, Kontextpolitik, Born-Regel oder physische Zeit. |
| `systematic-origin-audit-20260912/interaction/composition.py` | Bedingt gesetzte Bell-Kanten teilen einen echten Faktor; überlappende Projektoren sind nicht unabhängig. | Physischer Graph und Tensorfaktorisierung. Der Header grenzt das selbst ausdrücklich ab. |
| `universalraum-fugen-20260914/checker.py`; `universalraum-v14-F2-architektur-20260914/README.md` und `checker.py` | Explizite Modelle für interne Clebsch-Kanten, Tetramerzellen, Zell- oder Kantenbanken. Die F2-Auswahl gilt für die deklarierte harte C16-/Matching-/diagonale Gaugeklasse ohne Hopping. | Eine unbedingte Auswahl derselben Architektur im v1.6.x-Voll-G-Modell. Die README nennt ausdrücklich als fehlenden möglichen Quellschritt eine Vorschrift, die K4-Zellen oder eine Kette erzwingt. |

Die Quellen enthalten also echte Multiplikation, Überlappung und interne Verklebung. Die fehlende Kante ist **nicht „es gibt überhaupt keine Komposition“**, sondern der typisierte Übergang von diesen festliegenden internen Trägern zu globalen gemeinsam benutzten CAR-Ressourcen.

### Clock ist keine automatische Vervielfältigung

Der ursprüngliche Clock wird aus `experiments/tfpt-discovery/seam_state_derivation_probe.py`, S0.1–S0.4, neu ausgeführt. Sein dokumentierter passiver Lift erfüllt mit L=Λ²GF:

W L = GB W,   Lᵏ Wᵀ = Wᵀ GBᵏ,   k=0,…,5.

Da GB orthogonal ist und W Rang 60 hat, sind alle sechs rotierten hellen Räume genau derselbe 60-dimensionale Raum. Der Vereinigungsrang ist **60, nicht 360**. Das wird durch sechs exakte Matrixidentitäten bewiesen; der in `clock_gluing.py` vorhandene Mehrprimzahl-Rangheurismus wird dafür nicht verwendet. Interne Clock-Wiederholung allein liefert deshalb keinen neuen unabhängigen hellen Kopienträger.

## 2. Kleinstes skalares Überlappungs-Gegenmodell

Seien a_i,d_i, i=0,…,63, zwei kanonische Familien auf **einer** gemeinsamen CAR-Fockbasis. Setze für 0<c<1 und s=√(1−c²):

f_i^L=a_i,   f_i^R=c a_i+s d_i.

Jeder Chart für sich ist kanonisch; gegenseitig gilt

{f_i^L,f_j^{R†}}=c δij.

Das sind überlappende Charts, **keine unabhängigen räumlichen Orte**. Ihre gemeinsame Gramform ist [[1,c],[c,1]]⊗I64 und hat Rang 128. Für den erklärten skalaren, nichtdegenerierten Überlappungsansatz sind 128 globale Fermionmoden daher minimal. Für beide Vergleichsmodelle sind c und s ungleich null: Es wird kein unbenutzter Fermion-Kopienraum als bloßer Zuschauer hinzugefügt.

Zusätzlich gibt es zwei unabhängige Bosonbanken b_A,L und b_A,R, A=0,…,59. Mit exakt demselben eingefrorenen W definieren wir

P_A,x = Σ_{i<j} W_A,ij f_j^x f_i^x,

H_c = Δ(Nb,L+Nb,R) + g Σ_{A,x}(b_A,x† P_A,x + P_A,x† b_A,x).

Diese Summe ist die **deklarierte Gegenmodell-Kompositionsregel**, nicht ein behaupteter Originalcompiler-Output. Sie ist auf jedem festen N-Sektor eine endliche hermitesche Matrix. Erhalten sind

N = Na+Nd+2(Nb,L+Nb,R),   volles G,   der diagonal wirkende ursprüngliche Clock.

„Dieselben lokalen Daten“ bedeutet hier: Beide isolierten Chart-Algebren und beide einzelnen Chart-Hamiltonoperatoren sind durch kanonische Einbettungen exakt dieselben nativen Modelle, einschließlich ihrer höheren lokalen Operatoridentitäten. Es bedeutet **nicht**, dass bei gleichzeitig eingeschalteter globaler Summe jeder bisherige Einchart-Messwert unverändert bleibt. Gerade die gemeinsame Ressourcenbenutzung ist zusätzliche Dynamik.

Die vollständige G-Kovarianz folgt aus allen 45+15 neu geprüften W-Intertwinern und der exakten Identität (I₂⊗X)(u⊗I64)=(u⊗I64)X. Alle global erweiterten Vertices werden zusätzlich gegen sämtliche acht Cartangewichte geprüft. Es wird kein neues Zahl-veränderndes Referenzsystem benötigt.

**Ressourcenbuch:** W und seine internen Symmetrien stammen aus dem eingefrorenen nativen Konstrukt. Hinzugefügt sind zwei Chartnamen, ihre Einbettungen und c, zwei Bosonbanknamen, die summierte H-Regel, sowie die Präparations-/Auslesedeutung. Weder Bosonbanken noch c werden heimlich aus algebraischer Verfügbarkeit zu experimenteller Kontrolle erklärt.

## 3. Exakt geschlossener Ablauf und messbarer Unterschied

Auf N=2 hat die gemeinsame Paarabbildung C_c exakt den Gramoperator

C_c C_cᵀ = 8 [[I60,c²I60],[c²I60,I60]].

Der Prüfer baut dafür die ursprünglichen 480 W-Verticesterme mit ihren korrekten CAR-Vorzeichen auf allen C(128,2)=8128 Zweifermion-Basiszuständen aus. Insbesondere bekommt d_i†a_j† beim Umsortieren das Minuszeichen. Beide lokalen Diagonalblöcke bleiben 8I60; der neue Überlappungsblock ist 8c²I60.

Für jedes A ist der Raum aus drei normierten Paar-Flavorkombinationen (aa, symmetrisch-ad, dd) und beiden Bosonen ein **exakter reduzierender 5-Zustandsraum**, keine Projektion mit weggelassener Leakage. Seine Kopplungsmatrix ist

B = √8 g [[1,0,0],[c²,√2cs,s²]],   H₅ = [[0₃,Bᵀ],[B,ΔI₂]].

Ein Paarzustand ist dunkel. Vom linken Boson aus ist der zyklisch erreichbare Raum für g≠0 **genau vierdimensional**: Der Gramdeterminant der ersten vier Krylovvektoren ist 8⁶ c⁸(1−c⁴)g¹²>0. Der gesamte N=2-Sektor hat Dimension 8248, Paarabbildungsrang 120 und 8008 fermionische Dunkelzustände. Die 60 reduzierenden Fünferblöcke enthalten bereits 60 dieser Dunkelzustände; die übrigen 7948 liegen außerhalb ihrer Summe.

Die beiden hellen Kopplungsquadrate sind λ±=8(1±c²). Für Ω±=√(Δ²+4g²λ±) lautet die exakte Bosonamplitude jeder Rabi-Dublette

u±(t)=e^(−iΔt/2)[cos(Ω±t/2)−i(Δ/Ω±)sin(Ω±t/2)].

Damit gilt, ohne Schrieffer-Wolff- oder Klein-g-Näherung:

P(L→R;t)=|(u+(t)−u−(t))/2|² = 16g⁴c⁴t⁴ + O(t⁶).

Der volle G-invariante Test benötigt keine Auswahl eines intern ausgezeichneten A: Präpariere die gleichgewichtete Mischung ρL=(1/60)Σ_A |b_A,L⟩⟨b_A,L| und lies die gesamte rechte Bosonzahl Nb,R aus. Beide sind G-invariant. Da alle A denselben Kanalblock haben, ergibt sich dieselbe obige Wahrscheinlichkeit. Die Präparierbarkeit und Messbarkeit werden als Gegenmodell-Dictionary vorausgesetzt, nicht hergeleitet.

| Gemeinsame-Fermion-Komposition | c=3/5, s=4/5 | c=4/5, s=3/5 |
|---|---:|---:|
| Lokales WWᵀ in jedem Chart | 8I60 | 8I60 |
| λ+, λ− | 272/25, 128/25 | 328/25, 72/25 |
| Koeffizient von g⁴t⁴ im Transfer | 1296/625 | 4096/625 |
| Dimensionsloses viertes Moment unten | 706/625 | 881/625 |

Für dieselbe ρL seien μk=Tr(ρL H_c^k). Beide Modelle haben exakt

μ1=Δ,   μ2=Δ²+8g²,   μ3=Δ³+16Δg².

Erst μ4=Δ⁴+24Δ²g²+64(1+c⁴)g⁴ trennt sie. Besonders wichtig:

I4 = (μ4−3μ1²μ2+2μ1⁴)/(μ2−μ1²)² = 1+c⁴,

c=(I4−1)^(1/4) für die erklärte nichtnegative Familie.

**Positive Umkehrung:** Eine höhere Antwort macht den fehlenden globalen Überlappungsparameter beobachtbar. Er kann nicht durch eine geänderte Zeitskala oder bloße Umbenennung bei erhaltener Vorbereitungs-/Messdictionary verschwinden. Unser Gegenmodell behauptet ausdrücklich **nicht** identische globale N=2-Daten: Sein globaler Gramblock unterscheidet die Komposition bereits. Der parallele Ein-Bosonbank-Strang der Hauptrunde untersucht die stärkere Grenze, dass auch identische vollständige N=2-Daten noch unterschiedliche N=3-Antworten erlauben; dessen Beweis und allgemeine komplexe Konventionen sind nicht Teil dieses unabhängigen Zertifikats.

## 4. Echter gemeinsamer Ressourcenanteil, keine versteckte Einzelkopienzerlegung

Die beiden reellen symmetrischen Flavor-Kopplungstensoren lauten CL=uuᵀ und CR=vvᵀ, u=(1,0), v=(c,s). Sie erfüllen

Tr(CL CR)=c²∈(0,1),   ‖[CL,CR]‖²_HS=2c²s²>0.

Zwei Rang-eins-symmetrische Matrizen können hier nicht gleichzeitig durch denselben passiven unitären Flavorbasiswechsel Takagi-diagonal werden: Dafür müssten ihre erzeugenden Geraden parallel oder orthogonal sein; ihr Skalarprodukt bleibt unter einem gemeinsamen Unitärwechsel erhalten. Das ist nicht der Fall. Der gemeinsame Projektorkommutant in M₂(C) ist exakt eindimensional, Span(I₂).

Somit gibt es **keine nichttriviale reine Einzel-Flavor-Parität nach einem gemeinsamen passiven Basiswechsel, die beide benannten Bosonbanken unverändert lässt**. Eine solche Parität müsste u und v mit Vorzeichen ±1 erhalten; wegen ihrer nichtverschwindenden Überlappung haben beide dasselbe Vorzeichen. Es bleibt nur die gesamte Fermionparität. Die Aussage verbietet nicht zusätzliche Transformationen, die gleichzeitig Bosonbankphasen oder Banknamen ändern.

Das liefert den präzisen Unterschied zur Ein-Bosonbank-Familie mit einem einzigen symmetrischen Site-Tensor: Mehrere nichtkompatible Kopplungstensoren können eine gemeinsame Einzelkopien-Paritätszerlegung aufbrechen. Deren **Auswahl** bleibt aber neuer Geometrieinput.

## 5. Liefern frühe Quellprojektoren bereits c?

Der neu ausgeführte Original-P0/P1-Weg bestätigt exakt

|⟨zα/2,zβ/2⟩|² ∈ {0,1/4,1/2,1}.

Die Zahlen c=1/2 oder c=1/√2 sind also als Beträge konkreter ursprünglicher C⁴-Strahlenüberlappungen vorhanden. Dies ist mehr als eine frei erfundene Kandidatenzahl. Es ist aber noch **kein typkorrekter Quellschritt zu diesem H_c**:

1. Die C⁴-Projektoren wirken auf dem bestehenden Compilerträger. Das Flavor-C² unseres Gegenmodells ist dagegen eine G-triviale Multiplizitätsebene des 64-dimensionalen nativen Fermionträgers.
2. Die untersuchten Quellen liefern keine Intertwiner-/Ressourcenzuordnung, die gerade zwei dieser Strahlen zu den beiden globalen CAR-Chart-Einbettungen macht.
3. Sie wählen keine zwei Strahlen, deren Phasenlift, Bosonbankzuordnung oder Summe von Vertices als globalen Prozess aus.

Das bloße Einsetzen einer bekannten Quellzahl würde diese drei Schritte nicht ersetzen. Unsere rationalen c=3/5,4/5 sind bewusst klar benannte Gegenmodellparameter; sie werden nicht als ursprüngliche Strahlenüberlappungen verkauft. **Falls** künftig der fehlende typisierte Strahlen→Chart-Schritt abgeleitet wird, kann die Familie auf diskrete Kandidaten eingeschränkt werden und I4 deren unterschiedliche Antworten direkt testen.

Der Typengpass lässt sich noch genauer fassen: Soweit das C⁴ in der bereits verwendeten nativen Identifikation den internen SU(4)-Fundamentalfaktor trägt, darf es nicht ohne weiteren Schritt als unabhängiger **G-trivialer** Multiplizitätsraum ausgegeben werden. Die 15 originalen SU(4)-Generatoren haben auf C⁴ keinen gemeinsamen Fixvektor, und ihr Endomorphismenkommutant besteht exakt nur aus Skalaren; beides ist separat geprüft. Also Hom_G(1,4)=0 und End(4)=1⊕15; der skalare Anteil jedes normierten Rang-eins-Projektors ist derselbe I4/4. Ein fixer linearer equivarianter Import erzeugt hieraus keine verschiedenen Kopien. **Paarinvarianten** wie Tr(PαPβ) sind dagegen durchaus unterscheidbar und bleiben brauchbare Kandidatendaten; ihnen fehlt weiterhin die erklärte globale Einbettungs-/Vertexregel. Eine andere Feldzuordnung oder gezielte Symmetriebrechung ist damit nicht allgemein verboten.

## 6. Nächster erster fehlender Quellschritt

Gesucht ist eine explizite, typisierte globale Zuordnung

Originalwort / markiertes Quellobjekt → gemeinsamer Einteilchenraum Vglobal, Isometrien Ex:C64→Vglobal und Bosonbank-/Vertex-Zuordnung.

Sie muss insbesondere Ex†Ey festlegen. Erst dann darf ein Parameter wie c als hergeleitet gelten. Danach sind H, erhaltene Größen und die im Elternstrang ergänzte höhere geladene Antwort auf derselben Grundlage zu prüfen. Die bereits vorhandenen lokalen Zahlen, vollständige interne Symmetrie oder wiederholter Clock wählen diesen Schritt nicht von selbst.

## 7. Reproduktion und Prüfgrenze

`python3 verify.py --output results_normal.json` und `python3 -OO verify.py --output results_optimized.json`; [REPLAY.json](REPLAY.json) versiegelt Exitcodes, Prüferhash und identische Resultatbytes. `replay.py` führt beide Varianten lokal aus. Keine Netz-/Live-Repo-Imports, keine große Grundzustandsdiagonalisierung und keine Änderung älterer v1.6.8-Dateien.

Alle neuen algebraischen Aussagen sind mit ganzen Zahlen, Gauß-Ganzzahlen oder SymPy-Rationalen geprüft; es gibt **keine numerischen Toleranzprüfungen**. Der native Konstruktor verwendet komplexe Maschinenarrays für ganzzahlige Gaußwerte und kontrollierte kleine exakte Operationen; W- und globale Paargramme sind int64. **270 eigene exakte Guards, 0 numerische Guards**, daneben 17 übernommene native Konstruktionsguards und 1073 übernommene P0/P1-Adapterguards. Die Clock-Originalguards sind einzeln in der eigenen Checkliste gekennzeichnet; keine Quelle wird als neuer unabhängiger Beweis ausgegeben.

Ein erster Prüflauf wurde korrekt abgebrochen, weil SymPy den Ausdruck 2(−1−i)(−1+i) vor Expansion strukturell nicht mit 4 gleichsetzt. Ein Minimalbeispiel reproduzierte genau diese Darstellungsursache; die Korrektur besteht nur in exakter polynomialer Expansion vor dem Normvergleich. Kein Toleranzwert und keine abgeschwächte mathematische Bedingung wurden eingeführt.
