# π, Kreis und die konkrete P1-Brücke

Stand: 10. September 2026. Unabhängige begrenzte Quellen- und Beweisprüfung. Originalrepo unverändert; keine native Kampagne ausgeführt. Die beigefügte Datei `check.json` pinnt den gelesenen Quellenstand und dokumentiert ausschließlich kleine eigene exakte Kontrollen.

**Ergebnis.** Eine diskrete Gruppenalgebra kann unter ausdrücklich gewählter regulärer beziehungsweise universeller Vervollständigung einen vollständigen Kreis rekonstruieren. Positivität allein wählt weder diese Darstellung noch ihren Zustand oder ihre physische Zeitnormierung. Der echte native Ansatz für P1 lautet **Index4 × Winkelperiode2π × normierte Antwort =1**. Der unmittelbar beteiligte Faktor4 ist kein E8-Rang8. Ein späterer Originaltext beweist bereits die abstrakte symmetrische Vierkanalverteilung; seine Identifikation mit der konkreten TFPT-Determinantenantwort bleibt offen. Ein positiver, präziser Abschlussvertrag lässt sich dennoch formulieren.

## 1. Zwei verschiedene Bedeutungen von „nur π kontinuierlich“

„Ein einziger kontinuierlicher Raumparameter“ und „ein zusätzlicher transzendenter Skalar in einer endlichen Präsentation“ sind verschiedene Aussagen. Eine mehrdimensionale Charakterquelle widerlegt die zweite Lesart nicht. Der hier behandelte Test untersucht zunächst die skalare Präsentation und den einfachsten zyklischen Prozess; er ersetzt die vollständige TFPT-Charakterquelle nicht durch einen Kreis.

Die Körper Q(π) und seine algebraische Abschließung sind abzählbar: Es gibt abzählbar viele rationale Polynome und jedes nichtverschwindende Polynom hat endlich viele Nullstellen. Sie können daher nicht sämtliche reellen Skalare enthalten. Umgekehrt liefert die übliche Cauchy-Vervollständigung von Q bereits R; π muss dazu nicht als separater Input eingetragen werden. Eine Theorie darf also „π ist der einzige explizit eingetragene transzendente Koeffizient“ sagen. Daraus folgt kein Satz, dass π alle kontinuierlichen Zustands-, Dynamik- oder Geometriedaten auswählt. Welche Operationen, Grenzwerte und Vervollständigungen erlaubt sind, gehört zum Vertrag. Insbesondere wird hier keine unbekannte algebraische Unabhängigkeit etwa von π und e behauptet.

Native Herkunft: `docs/THEORY.md:23–39` formuliert die beiden Inputs c3 und g_car und das Präsentationsformat a=(1,1,2) plus π. Der operative Konstantenpfad `verification/tfpt_constants.py:13–16` setzt π und c3 explizit ein. Das ist eine konkrete kompakte Präsentation, kein universeller Eindeutigkeitssatz über positive Prozessmodelle.

## 2. Ein positiver Rekonstruktionssatz und seine scharfe Grenze

**Satz1 (regulärer zyklischer Prozess).** Sei A0=C[u,u⁻¹], mit u*=u⁻¹. Wähle das normalisierte Funktional

τ(Σ a_n u^n)=a_0.

Dann ist τ positiv, denn τ(p*p)=Σ|a_n|². Die GNS-Vervollständigung ist ℓ²(Z), u wirkt als bilateraler Shift, und der von diesem Shift erzeugte C*-Abschluss ist C(S¹). Der ausgezeichnete Zustand wird zur normierten Haarintegration. Diese Rekonstruktion ist bis auf die den ausgezeichneten Generator und den zyklischen Vektor respektierende unitäre Äquivalenz eindeutig.

**Beweis.** Die Monome u^n sind bezüglich τ orthonormal. Ihre Vervollständigung liefert die Standardbasis von ℓ²(Z). Die Fourierabbildung δ_n↦z^n ist unitär nach L²(S¹,dμ_Haar) und macht den Shift zu Multiplikation mit z. Laurentpolynome sind in C(S¹) gleichmäßig dicht. Die Operatornorm einer kontinuierlichen Multiplikationsfunktion ist wegen des vollen Haarträgers deren Supremumsnorm. Damit ist der Abschluss genau C(S¹). Dies ist die klassische Konstruktion in [de la Harpe–Jones, Proposition5.20](https://www.unige.ch/math/application/files/7016/3854/6556/cstar.pdf).

Eine alternative hinreichende Auswahlregel lautet: Der Zustand auf dem universellen C*(Z) ist unter allen dualen Drehungen γ_z(u)=zu invariant. Dann gilt für n≠0: τ(u^n)=z^nτ(u^n) für jedes z, also τ(u^n)=0. Normalisierung liefert den obigen Zustand. Der universelle C*-Abschluss enthält ohnehin alle unitären Charaktere und ist C(S¹); er darf nicht mit der GNS-Darstellung eines beliebigen einzelnen Zustandes verwechselt werden. Die komplexen Skalare und die C*- beziehungsweise Hilbertraum-Vervollständigung sind hier ausdrückliche mathematische Prämissen.

**Gegenbeispiele bei unveränderter Algebra und Positivität.** Jedes Wahrscheinlichkeitsmaß μ auf S¹ definiert ω_μ(p)=∫p,dμ und ω_μ(p*p)≥0.

| Zustand | Momente ω(u^n) | Seine GNS-Spektralwelt |
|---|---|---|
| Punktmasse bei1 | 1 für alle n | ein Punkt, Dimension1 |
| Gleichverteilung auf M-ten Einheitswurzeln | 1 falls M teilt n, sonst0 | M Punkte |
| Haar | δ_n0 | voller Kreis |
| Dichte 1+(1/2)cosθ gegen Haar | 1 bei n0;1/4 bei n=±1; sonst0 | voller Kreis, anderer markierter Zustand |

Schon ω((1−u)*(1−u)) ist beim Punktzustand0, bei Haar2 und bei der positiven Kosinusdichte3/2. Der letzte Zustand ist auf C(S¹) treu, denn seine Dichte ist mindestens1/2. Selbst voller Kreis und Treue wählen folglich den Zustand nicht. Noch stärker: gleichmäßiges Maß auf einem echten Kreisbogen ist auf der Laurentpolynomalgebra algebraisch treu, weil ein nichtverschwindendes Laurentpolynom auf dem Bogen nicht überall verschwinden kann; sein C*-Bild ist gleichwohl C(Bogen). Algebraische Treue erzwingt somit auch nicht den universellen Spektralträger.

**Endlicher positiver Vorläufer.** Gleichverteilung auf den M-ten Wurzeln reproduziert Haarmomente für 0<|n|<M exakt. Für Polynome mit Exponentenspanne d<M stimmen deshalb alle Paarungen p*q mit Haar überein. Das gibt eine echte endliche, positive Rekonstruktion jeder vorab begrenzten Momentenstufe. Es beweist weder, dass ein endlicher Zyklus der volle Kreis ist, noch dass der tatsächliche TFPT-See dieses Maß trägt.

## 3. Was die Zahl2π fixiert

Die Gruppen R/Z und R/(2πZ) sind durch θ=2πt isomorph. Derselbe Haarzustand ist

dμ=dt=dθ/(2π).

Bei einer Zeitkoordinatenänderung θ′=sθ, s>0, ändern sich Periode und Antwortdichte gemäß β′=sβ und c′=c/s; **βc ist invariant**. Eine topologische Kreisgruppe legt deshalb keinen numerischen physikalischen Zeitmaßstab fest. Im normierten komplexen Modell mit Generator i, i²=−1, besitzt exp(iθ) die primitive Periode2π. Die Wahl dieses normierten Generators beziehungsweise der radianischen Winkelkoordinate ist die zusätzliche Markierung. Ein unitärer Einzelschritt bestimmt außerdem keinen eindeutigen logarithmischen Hamiltonoperator: bereits U=1 besitzt neben H=0 auch H=2πP mit exp(iH)=1 für jede orthogonale Projektion P.

Ebenso ist die KMS-Inversttemperatur kein topologischer Kreisumfang. Rotationsdynamik kann eine reale Periode2π besitzen und für viele β>0 Gibbszustände zulassen. Die Identifikation gerade β_angle=2π ist ein geometrischer beziehungsweise physikalischer Vertrag. [Longo–Tanimoto](https://arxiv.org/abs/1608.08903) klassifizieren Rotations-KMS-Zustände bei vorgegebenem β und vorgegebener konformer Dynamik; sie wählen nicht aus diskreter Positivität einen besonderen β-Wert aus. Das native Artikeltheorem gilt ebenfalls für jedes β>0 (`holomorphic_kms_extension_en.tex:505–543`), während Definition1.4 und die P1-Korollarzeile β=2π zusätzlich setzen (`:145–154`, `:799–811`).

Die Konstruktion eines Gibbszustandes enthält eine gewichtete Spur, nicht automatisch die normierte Matrixspur. See-/Vakuumzustand, Rotations-Gibbszustand und geometrischer Translations-/Dilatations-KMS-Zustand dürfen nicht gleichgesetzt werden; der Originalartikel trennt sie ausdrücklich (`:157–166`). Auf einer kommutativen Algebra mit trivialer Dynamik erfüllen zudem alle Zustände die KMS-Bedingung für jedes β. Die Positivitäts- und KMS-Wörter allein sind daher keine Zustandsauswahl.

## 4. Präziser positiver Antwortsatz für P1

Die transitive Projektionsversion steht bereits im Originalartikel vom29.08., Lemma6.1 (`:763–794`). Die folgende Fassung macht die physische Response-Identifikation und Gesamtladung vollständig sichtbar und erlaubt auch positive Effekte statt scharfer Projektionen.

**Satz2 (gleichmäßige tatsächliche Sektorantwort).** Sei B eine unital C*-Algebra, α eine Z_I-Wirkung und ψ ein α-invarianter Zustand. Seien E_r≥0 echte identifizierte Antwort-Effekte mit Σ_rE_r=1 und α_s(E_r)=E_(r+s). Sei die tatsächlich zu berechnende integrierte Antwort über eine vollständige Periode durch

Q_r=Q ψ(E_r),  Q>0,

gegeben, und ihre mittlere Rate c_r=Q_r/β, β>0. Dann

Q_r=Q/I,  c_r=Q/(Iβ).

**Beweis.** Invarianz und Transitivität machen alle ψ(E_r) gleich. Ihre Summe ist ψ(1)=1. Substitution gibt die Aussage. Orthogonalität oder Kommutativität der Effekte wird nicht benötigt. Für eine überall konstante lokale Antwortdichte statt lediglich der periodengemittelten Rate muss zusätzlich deren Maß auf der Winkelkreisgruppe drehinvariant sein; dann ist es nach Haar-Eindeutigkeit Q/(Iβ)dθ pro Sektor.

Insbesondere ergibt **I=4, Q=1, β=2π und die Identifikation c3=c_r** exakt c3=1/(8π). Dies ist ein positiver Abschlussvertrag, kein Nachweis seiner TFPT-Prämissen.

**Warum jede sichtbare Prämisse benötigt wird.** Vier positive Gewichte (1/2,1/6,1/6,1/6) summieren sich zu1 und widerlegen Gleichverteilung ohne transitive Invarianz. Additivität allein reicht ebenfalls nicht: Die tatsächlichen Antworten müssen derselben invarianten Funktionalbewertung entsprechen, wie in Q_r=Qψ(E_r), oder selbst invariant sein. Symmetrie allein lässt den positiven Gesamtfaktor Q beliebig. Gleiche integrierte Kanalgewichte lassen eine lokale Dichte proportional zu1+εcosθ zu; ohne Drehinvarianz ist sie nicht konstant. Ein formaler Satz E_r=1/I wäre immer möglich, identifiziert aber keine vorhandenen physikalischen Antwortkanäle.

**Hinreichender Weg zur Invarianz ohne Ersetzen des Zustandes.** Wenn α mit der gegebenen Dynamik kommutiert, die vorgeschriebene Restriktion auf die Unteralgebra erhält und der gegebene β-KMS-Zustand genau eine β-KMS-Erweiterung besitzt, ist ψ∘α_s eine weitere solche Erweiterung und muss ψ gleichen. So liefert KMS-Eindeutigkeit die Invarianz des tatsächlichen Erweiterungszustandes. Ob der native See diese Restriktion und den richtigen Fluss realisiert, bleibt eine eigene Identifikation. Eine normierte Spur wird in diesem Argument nicht eingesetzt.

## 5. Was spätere native Belege wirklich bereitstellen

Alle Pfade in dieser Tabelle sind relativ zu `/Users/stefanhamann/Projekte/tfpt-theoryv4`; Dateihashes stehen in `check.json`.

| Original | Geprüfter positiver Inhalt | Verbleibende Grenze |
|---|---|---|
| `verification/tfpt_constants.py:13–29` | c3=1/(8π) eingesetzt; rankE8=g_car+N_fam=8 | Rang8 ist hier ein anderer abgeleiteter Knoten |
| `tfpt_1_architecture_e8.tex:160–175` | Index4 und2π organisieren P1 | nennt P1 ausdrücklich primitive Annahme und Brücke offen |
| `verification/v813_p1_index_kms.py:425–460` | endliche Index-/Spurvorläufer; genaue offene Response-Normierung | berechneter See ist ausdrücklich nicht gleichverteilt; physische Boost-Identifikation offen |
| `verification/v484_seam_contact_unit.py:1–47,58–108` | normierter Kreispropagator plus orbitgemittelte Einfügung; exakte Z4-Markmatrix | Kreispropagatornorm und Orbitmittelung sind Teil dieser konkreten Konstruktion; kein Nachweis, dass sie die gesamte native Response auswählen |
| `verification/v485_contact_diagonal_closed.py:14–24,62–96` | unter festem kurzen Abstandssubtraktionsschema G_reg(0;ℓ)=π⁻¹log(ℓ/(2π)) | die Null-Selbstenergie beiℓ=2π hängt am Subtraktionsschema |
| `verification/v985_quillen_channel_swap.py:1–41,79–109` | nach Charakterverschiebung2 stimmen drei nichtverschwindende absolute Eigenwertverhältnisse exakt4/ln2 überein | Spektrenvergleich ist keine Zustandsgleichverteilung; Kernkanal bleibt vorhanden; c3 kürzt sich heraus |
| `articles/2026-08-29/holomorphic_kms_extension_en.tex:505–543,763–844` | abstract holomorphic rotational KMS extension; bedingte transitive Vierkanalantwort | konkrete TFPT-Skalierungsgrenze, Antwortauflösung und physischer Koeffizient noch nicht identifiziert |
| `verification/v1014_bridge_refinements.py:12–36` | endliche Restriktionsabbildung; Orientierung wählt konjugierten Zweig; A0 fixiert konstanten Phasenanker | nennt character-blind determinant-response map als fehlendes Objekt; triviale Charakterprojektion ist keine demokratische Auslese aller Charakterräume |
| `tfpt_research_contracts.tex:14559–14714` | mehrere endliche Quillen-/Chern-/KMS-/Kanalvergleichsteile; letzter vermerkter Abschluss30.08. bleibt begrenzt | Kontinuumsvergleich von Metrik, Verbindung, beiden Twist-Holonomien sowie exakter Variation bleibt offen |

**Die unmittelbare8 in P1.** Der native Anker a=(1,1,2) hat e1=4, also c3=1/(2e1π). In der Index-KMS-Lesart ist der Faktor8 ebenso 4×2. Die Zahl rank(E8)=8 allein enthält weder den Index dieser konkreten Inklusion noch die tatsächliche Kanalauflösung oder die Winkelnorm. Auch ein als E8 identifizierter und wurzelnormierter Verband legt noch keinen physikalischen Response-Zustand fest. Unsere exakten Kontrollen zeigen zusätzlich: bloßer Rang8 bleibt unter positiver Skalierung der E8-Grammatrix erhalten, während deren metrische Determinante sich ändert. Dieser Skalierungstest behauptet ausdrücklich nicht, dass die zusätzliche Normmarkierung „Wurzellänge²=2 und unimodular“ erhalten bleibt.

**Die vorhandene Clockwirkung vertauscht ihre eigenen Charakterprojektoren nicht.** Im tatsächlich gelesenen v813-Code sind

P_q=(1/4)Σ_(j=0)^3 i^(−qj)U⁽ʲ⁾ (`:276–278`).

Da diese Projektoren Polynome in U sind, gilt Ad(U)(P_q)=P_q. Die Invarianz eines Zustandes unter dieser Clockwirkung macht seine vier Gewichte folglich nicht gleich. Schon U=diag(1,i,−1,−i) mit dem positiven diagonalen Zustand diag(1/2,1/6,1/6,1/6) ist ein exaktes Gegenbeispiel. Ein zyklischer Shift der Basis würde die Projektoren zwar permutieren, ist aber eine zusätzliche, duale Wirkung und nicht die ursprüngliche Clock-Konjugation. Im konkreten nativen l=2-Block betragen die Ränge sogar (6,4,2,4) (`:406–420`), sodass keine Automorphie dieser Matrixalgebra alle vier Projektoren transitiv vertauschen kann: Automorphismen bewahren den Rang. Der spätere Artikel fordert deshalb mit Recht eine weitere tatsächliche Antwortauflösung. Die vorliegende endliche Tracialgrenzformel allein liefert diese nicht. Diese endliche Obstruktion verbietet keine passende andere Auflösung oder deren unendlichen Grenzbau; sie lokalisiert die benötigte zusätzliche Abbildung.

**Konkrete Positivitätsgrenze der nativen Markmatrix.** Mit C=circ(0,1,2,1) ist G_marks=−4c3log2 C und

spec(G_marks)={−16c3log2,8c3log2,0,8c3log2}.

Damit ist diese renormalisierte Vierpunktmatrix indefinit. Schon der Einsvektor liefert nach Herausziehen des positiven Faktors4c3log2 den Wert−16. Sie kann selbst keine positive Zustands-Grammatrix oder positive Vierkanalauflösung sein. Die Null-Diagonale bei nichtverschwindenden Nebendiagonalen zeigt dasselbe über Cauchy–Schwarz. Dies widerspricht der Positivität des Operators |D|⁻¹ auf seinem richtigen Funktionsraum nicht: singuläre Punktauswertung mit anschließender Diagonalsubtraktion ist eine andere Operation. Eine positive Antwort kann gegebenenfalls aus einer anders definierten Messung oder Form entstehen; diese Identifikation ist zu liefern.

Das feste Subtraktionsschema ist ebenfalls prüfbar: Addiert man die erlaubte, aber in v485 nicht gewählte endliche Konstante κ zur renormalisierten Diagonale, wird G_reg^κ=π⁻¹log(ℓ/(2π))+κ. Ihr Nullpunkt liegt bei ℓ=2πe^(−πκ). Die Aussage „einziger Nullpunkt2π“ ist exakt **innerhalb des fixierten Schemas**; sie folgt nicht aus Positivität ohne Schemenvertrag. Ob native relative Normierung und Symmetrien diese konkrete Freiheit ausschließen, verlangt die eigentliche Vergleichsabbildung.

## 6. Wie man den Anomalieoffset wirklich ausschließt

Gleiche Chernzahl allein reicht nicht. Auf dem trivialen Hermiteschen Linienbündel über R/(2πZ) haben die unitären Verbindungen

∇_α=d+iαdθ,  α∈R,

sämtlich Krümmung0; ihr Paralleltransport um den Kreis ist exp(−2πiα). Modulo einwertige unitäre Eichtransformationen ist α nur moduloZ identifiziert. Insbesondere α=0 und α=1/4 haben gleiche Krümmung und positive Fasermetrik, aber verschiedene Holonomie. Auf dem Twistorus bestehen zwei solche Zyklusfreiheiten. Das native Verlangen nach Verbindung **und** beiden Holonomien ist damit substantiell. Auch die klassische Bismut–Freed-Theorie behandelt Krümmung und globale Holonomie getrennt; siehe [The Analysis of Elliptic FamiliesII](https://webhomes.maths.ed.ac.uk/~v1ranick/papers/bismfree2.pdf), Einleitung und Theorem3.16.

**Präziser Vergleichssatz.** Seien L1,L2 Hermitesche Linien mit unitären Verbindungen über einer zusammenhängenden Basis. Hat die Verhältnislinie L2⊗L1⁻¹ Krümmung0 und trivialen Transport um alle geschlossenen Wege, so bestimmt jede unitäre Identifikation an einem Referenzpunkt genau eine globale unitäre, verbindungserhaltende Identifikation: Man setzt sie entlang eines Weges durch Paralleltransport fort; triviale Verhältnis-Holonomie macht das wegunabhängig. Auf einem glatten zweidimensionalen Torus genügt für die flache Verhältnislinie die Holonomiegleichheit auf zwei Fundamentalzyklen. Bei ausgeschlossenen Nullmoden/Divisoren sind die tatsächlich zusätzlichen Schleifen ebenfalls zu berücksichtigen.

Dieser Satz erklärt, was A0 **nach** Verbindungs-/Holonomievergleich leisten kann: die letzte konstante Phase auswählen. A0 allein beseitigt keine unbekannte flache Holonomie. Eine Isomorphie als bloße topologische Linie oder ein gleicher integrierter Chernwert leistet den stärkeren Vergleich ebenfalls nicht. Außerdem impliziert selbst die verbindungstreue Identifikation noch nicht, dass die relevante zeta-regulierte Variation ein positives normalisiertes Funktional Qψ ist. Diese Response-Identifikation und ihre EinheitQ=1 müssen separat nachgewiesen werden; gewöhnliche logarithmische Determinantenvariationen sind im Allgemeinen nicht positive Zustände.

**Konkretes nächstes Beweisziel innerhalb des gewählten Vertrags.** Zu konstruieren ist eine markierte, mit Z4 und dem gegebenen Fluss verträgliche Abbildung der tatsächlichen determinant-line response auf eine positive Antwortauflösung E_r, mitsamt der Identität Q_r=Qψ(E_r). Danach sind Q=1, die geometrische β=2π-Markierung und der oben beschriebene Verbindungs-/Holonomievergleich zu beweisen. Erst diese Komposition würde Satz2 auf die native Physik anwenden. Die vorhandenen endlichen Kanal-, Index- und Quillenresultate sind verwendbare Bausteine; sie ersetzen diese Abbildung nicht. Andere mathematische Determinantenlinien, etwa von Singularitäts-Residuen, werden hier ohne nachgewiesenen Intertwiner ausdrücklich nicht mit der TFPT-Quillenlinie identifiziert.

## 7. Konkreter positiver Kandidat: markierte endliche Determinantenantwort

Die vorige eigene Fortsetzung `work/fundamental-continuation/tfpt-origin/CLOCK-CAP-ANSCHLUSS.md`, §2, konstruiert aus der tatsächlichen dargestellten Clock bereits die Isometrie

Vψ=(1/2)Σ_(r=0)^3 e_r⊗U^rψ.

Sie beweist dort auch die Wahrscheinlichkeit1/4 jedes aufgezeichneten Instrumentzweigs. Das ist ein vorhandener Herkunftssatz, keine heutige Neuerfindung. Der separat typisierte Einteilchen-CAR-Anschluss steht in `EINTEILCHEN-CAR-BRUECKE.md`; beide unveränderten Dokumente sind zusätzlich in `check.json` gepinnt. Das Rekordregister führt keine vier unabhängigen neuen physikalischen Fockmoden ein.

**Satz3 (tatsächliche Markeffekte und endliche Response).** Sei K ein endlichdimensionaler Hilbertraum, U unitär und V wie oben. Für M_r=|e_r⟩⟨e_r| gilt

V*(M_r⊗I)V=I/4.

Damit liefern diese tatsächlich aus dem Cap erzeugten Markeffekte auf jedem Eingangs-Zustand exakt1/4. Sie sind **nicht** die Spektralprojektoren P_q von U. Das bloße Markresultat trägt keine Information über ψ; die bedingten Beinoperatoren U^r/2 tragen gleichwohl den geordneten Prozess. Weder die Normierung der Eingangsdichtematrix noch ihre Besetzungen werden dabei durch einen anderen Zustand ersetzt.

Sei nun D invertibel auf K, [D,U]=0, und D′ eine beliebige Matrix; [D′,U]=0 ist nicht erforderlich. Definiere die nur am r-ten Rekordbein gestörte, auf den Cap komprimierte Familie

A_r(t)=V*[I⊗D+tM_r⊗D′]V.

Dann A_r(0)=D und für einen lokalen Logarithmus der nichtverschwindenden Determinante

(d/dt)logdet A_r(t)|_(t=0)
=Tr[D⁻¹V*(M_r⊗D′)V]
=(1/4)Tr[D⁻¹D′].

**Beweis.** Orthogonalität gibt V*(M_r⊗D′)V=(1/4)U^(−r)D′U^r. Jacobi-Differentiation liefert den ersten Spurterm, und endliche Spurzyklizität zusammen mit [D,U]=0 den zweiten. Die markierte Effektidentität ist der Spezialfall D′=I ohne D. Die Isometrie und die lokale Viertelantwort benötigen nur Unitarität; die Identifikation der vollständigen Gruppenerwartung und des zyklischen Slide-Gesetzes aus der ursprünglichen Clock benötigt weiterhin U⁴=I.

Das ist eine echte endliche Antwortgleichverteilung für eine ausdrücklich konstruierte Quellenfamilie. Wenn D>0 und D′≥0 ist die Antwort zusätzlich nichtnegativ. Für allgemeines D′ ist die logarithmische Variation kein positives Zustandsfunktional. Die Gesamtgröße Tr(D⁻¹D′) ist auch hier nicht automatisch1: etwa D′=D ergibt dimK. Weder die GesamtladungsnormQ=1 noch eine physikalische β=2π werden durch diese Viertelung bestimmt.

**Positiver zustandserhaltender Korollarfall.** Ist die bezeichnete endliche Dichtematrix ρ treu, Trρ=1 und [ρ,U]=0, kann man ausdrücklich die Quellenfamilie mit D=ρ⁻¹ konstruieren. Dann liefert Satz3

(d/dt)logdet A_r(t)|_0=(1/4)Tr(ρD′).

Für die Identitätseinfügung D′=I ist dies exakt1/4. Die relative Determinante lautet in diesem Fall det A_r(t)/det A_r(0)=det(I+tρ/4). Hier wird also eine positive normierte Antwort aus dem ursprünglichen Zustand gebaut; ein tracialer Ersatz ist nicht nötig. Dies ist eine konkrete mögliche Realisierung von Q=1, deren entscheidende zusätzliche Auswahl **D=ρ⁻¹ und die Identitätseinfügung** offen sichtbar bleibt. Weder die endliche native Clock noch der Cap allein beweisen, dass der physikalische Quillenoperator und seine Variation gerade diese Familie sind. Die native See-Kommutation mit U aus dem Herkunftsdokument wäre bei dieser Realisierung nutzbar; die tatsächliche Treue und der Kontinuumsvergleich bleiben entsprechend ihrem jeweiligen Träger zu prüfen.

**Determinantenraum.** Gemeint ist die Determinante der Kompression A_r(t) auf K, äquivalent zur komprimierten Operation auf RanV. Die Determinante des vollen Rekordraums wäre eine andere Größe: det(I₄⊗D)=det(D)^4. Die volle Einmark-Variation hätte Tr(D⁻¹D′), nicht dessen Viertel. Auch kann I⊗D+tM_r⊗D′ für t≠0 aus RanV herausführen; deshalb wurde ausdrücklich die Kompression definiert und keine invariante Restriktion behauptet.

**Verbleibende native Quillen-Brücke.** Es muss nachgewiesen werden, dass gerade diese komprimierte endliche Familie die tatsächliche relative Determinantenantwort approximiert, mit identifiziertem D, zulässiger Variation, richtigen markierten Beinoperatoren und konsistentem Zustand. Für eine unendliche beziehungsweise zeta-regulierte Determinante sind die benötigte Spurbarkeit oder ein Regulatornachweis der hier verwendeten Zyklizität erforderlich; bei regulierten Spuren darf ein Kommutator-/Anomalieterm nicht stillschweigend verworfen werden. Der metrische und holonomische Vergleich aus§6 sowie Gesamtladung und Zeitnormierung bleiben nötig. Der Satz bietet somit einen genauen **endlichen Response-Kandidaten** zur Schließung von P1; er ist noch kein Quillen-Identifikationsbeweis.

## 8. Prüfungsumfang

`check.py` benutzt nur rationale Arithmetik und liest native Dateien für Hashes und kleine Textanker. Es prüft exakte Moment-Grammatrizen und ihre Ränge, positive Gegenzustände, endliche Haarvorläufer, Kanalnormalisierung und Zeitskalierung, E8-Grammatrix und Skalierung, die native Markmatrix samt negativer Richtung und den begrenzten absoluten Kanalspektrenvergleich. Ein reproduzierbarer Lauf schreibt `check.json`. Endliche Kontrollen illustrieren die durchgeführten allgemeinen Beweise; sie ersetzen sie nicht.

Codeentdeckung begann mit MCP-Codegraphabfragen für P1 und Quillen. Die späteren exakten Originalpfade wurden anschließend gezielt gelesen. Symbolabfragen für einzelne neue Module lieferten keine ausreichenden Ergebnisse; bekannte Quellenpfade wurden dann direkt gelesen. Die Abdeckung umfasst die direkten P1-Nennungen, ihre Quillen-Verknüpfung und die späteren direkten Originalupdates bis v1014 im aktuellen Checkout; sie behauptet keine vollständige Validierung sämtlicher nativer Skripte. Zusätzlich wurde der aktuelle `verification/status_ledger.csv` selektiv gelesen: AX.P1.01 bleibt Axiom, P1.INDEX.KMS.01 und ALPHA.QUILLEN.EXACT.01 bleiben in ihren Vergleichs-/Normierungsbeweisen offen. Die spätere MMST-Elternzeile nennt bereits v1026s einheitliche Schranke und v1030s bedingten Rahmen, behält aber FE-GEN, Wort-/Adjungiertenschwänze, ALG-EXH und MMST-Identifikation offen. Diese spätere Ledgerinformation wurde als aktueller Quellenstatus aufgenommen, nicht als unabhängig neu bewiesene Analytik. Die vier Originalzeilen werden strukturiert in `check.json` mitgeführt. Es gibt keinen neuen Beweis von P1, keinen universellen Welt-Eindeutigkeitssatz und keine Ersetzung des nativen Seezustandes durch eine Spur.
