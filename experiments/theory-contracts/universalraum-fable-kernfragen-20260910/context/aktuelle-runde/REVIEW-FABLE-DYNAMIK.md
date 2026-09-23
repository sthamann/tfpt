Zusatzhinweis von Codex zur inzwischen revidierten Fable-Fassung: Bitte auch REVIEW-FABLE-ZUSATZ.md im selben Ordner lesen. Dort werden der neue 2x2-Volumensatz und der Duhamel-Spaltenbound mit Gegenzeugen geprüft; das Cap-Breathing wird bestätigt. Es folgt die unveränderte frühere Reviewfassung.

# Unabhängiger Review: Fables dynamische Theoreme 1–4

10. September 2026. Geprüft wurden die vorliegenden Abschnitte Theorem 1–4 einschließlich ihrer Folgerungen in `experiments/theory-contracts/universalraum-fable-kernfragen-20260910/fable/PROOF.md` und die entsprechenden Aussagen in `ERGEBNISSE.md`. Abgleich mit dem ursprünglichen unbeschnittenen U(1)-Rotor/CAR-Parent in `ground-state-loop-response/README.md` und der lokalen Algebra in `observable-dynamics/README.md`. Eigene Wilson-Cap- und Erweiterungsbeweise dienen als bezeichnete Vergleichsartefakte. Keine Prüfung von Theorem 5–6, kein erneuter Lauf der nativen Suite, keine Änderung der Fable-Dateien oder ursprünglichen Belege. Der andernorts festgestellte LL2-Checkerfehler wurde hier nicht nochmals untersucht; die darauf beruhenden Dressing-Zahlen werden nicht unabhängig zertifiziert.

**Urteil:** Die exakten Radix- und Überlagerungsidentitäten bleiben erhalten. Die Leakage-Gleichheit braucht eine zusätzliche Voraussetzung; ihr positiver unterer Grenzwert und damit das Verbot eines unverändert all-low bleibenden Codes gelten weiterhin. Das Dressing ist ein überprüfbarer erster Näherungsschritt, aber kein bewiesener minimaler oder abschließender dynamischer Ausbau. Für die Aussage über die erzeugte Rotoralgebra muss die Topologie angegeben werden. Die folgende Präzisierung erhält die konstruktiven Ergebnisse und entfernt die unbelegten Verallgemeinerungen.

## 1. Beliebige all-low Flux-Codes: korrigierte Identität und Gegenzeuge

Sei J eine endliche Isometrie in den all-low Sektor, mit Bild im Definitionsbereich des ursprünglichen H, und P=JJ*. Dort gilt

\[
HJ=H_{\rm diag}J+bTJ,\qquad
T=d^*A_Ul,\qquad H_{\rm diag}=H_E+\epsilon_L N.
\]

Die nichtdiagonalen LL-Terme sind Pauli-blockiert; die diagonalen Rückwege von \(cA_U^2\) gehören bereits zu \(\epsilon_L N\). Die Aussage „LL2 annihiliert den Zustand“ darf diese Rückwege nicht nochmals entfernen. Auf dem deklarierten einfachen kubischen Graphen entspricht jedem geordneten Nachbarpaar genau ein unitärer Linkshift. Die verschiedenen erzeugten Loch-/High-Muster sind orthogonal. Für beliebige, auch überlappende Fluxwellenfunktionen folgt deshalb direkt

\[
J^*T^*TJ=N_{\rm dir}I.
\]

Man benötigt weder einen Unterschied auf mindestens vier Links noch eine Basis aus einzelnen Fluxkonfigurationen. Der diagonale Austritt liegt im Sektor ohne High-Teilchen, der LH-Austritt im Sektor mit einem High-Teilchen. Diese beiden Beiträge sind orthogonal. Somit lautet der allgemeine Satz

\[
\boxed{\Gamma^*\Gamma
=J^*H_{\rm diag}(I-P)H_{\rm diag}J+b^2N_{\rm dir}I
\ \ge b^2N_{\rm dir}I.}
\]

Die Gleichheit aus Fable (1.1) gilt genau dann, wenn \((I-P)H_{\rm diag}J=0\). Ein von einzelnen Fluxbasiszuständen aufgespannter Unterraum erfüllt dies. Ein beliebiger Unterraum des all-low Fluxsektors muss es nicht erfüllen. Auch bei einem invarianten Unterraum ist \(J^*H_{\rm diag}J\) nicht in jeder gewählten Codebasis diagonal.

Der erste Term der eingerahmten Formel bedeutet den endlichen Gramoperator \((H_{\rm diag}J)^*(I-P)(H_{\rm diag}J)\). Damit genügt \(\operatorname{ran}J\subset\operatorname{Dom}H\); eine ungenannte Voraussetzung \(\operatorname{ran}J\subset\operatorname{Dom}H^2\) wird nicht benötigt.

**Expliziter physischer Gegenzeuge:** Auf dem ursprünglichen \(L=5\)-Torus, \(N=125\), wähle eine elementare Wilsonplaquette W und

\[
J(1)=\psi=\frac{\Omega_0+W\Omega_0}{\sqrt2}.
\]

Beide Summanden sind Gauss-neutral, all-low, orthonormal und haben endlichen Fluxsupport. Ihre diagonalen Energien sind \(\epsilon_LN\) und \(\epsilon_LN+2\kappa\). Also

\[
\operatorname{Var}_\psi(H_{\rm diag})=\kappa^2=\frac1{10000},
\qquad
\Gamma^*\Gamma=\frac{125}{96}+\frac1{10000}
=\frac{78131}{60000}.
\]

Das widerlegt die ausdrücklich behauptete Gleichheit für **jeden** beliebigen Flux-Code. Falls „spanned by states … arbitrary fluxes“ ausschließlich einzelne Fluxbasiszustände meint, ist das Theorem unter dieser engeren Voraussetzung richtig; genau diese Einschränkung muss dann im Satz stehen. Der ursprüngliche 16-dimensionale Wilson-Cap-Code ist diagonal-invariant und behält seine Gleichheit \(N/96\). Der strikte Austritt jedes all-low Codes folgt sogar aus der allgemeineren unteren Schranke.

Der unabhängige kleine Prüfer berechnet den vollständigen H-Austritt dieses Gegenzeugen mit allen 750 gerichteten LH-Termen, tatsächlichen CAR-Vorzeichen und ganzzahligen Fluxänderungen. Die 1500 ausgegebenen One-High-Basiszustände sind physisch und verschieden. Keine Fluxabschneidung wird verwendet.

## 2. Corollary 1.1 und 1.2: was sich retten lässt

Für einen **festen Fock-Besetzungsbasiszustand** auf dem zusammenhängenden einfachen kubischen Torus \(L\ge5\) lässt sich die Nichtinvarianz ebenfalls beweisen. Der Einteilchen-Hoppinggraph auf allen L- und H-Moden ist zusammenhängend: LL verbindet die L-Moden; jede H-Mode ist über LH mit ihnen verbunden. Gauss erzwingt insgesamt N besetzte von 2N Moden. Daher gibt es mindestens eine Kante von einer besetzten zu einer unbesetzten Mode. Ihr erlaubter NN-LL- oder LH-Hop verändert das feste Materiemuster und trägt einen unitären Rotorfaktor. Auf diesem Graphen kann kein zweistufiger LL-Term denselben NN-Endpunktübergang liefern. Die betreffende Materie-Ausgangskomponente lässt sich folglich nicht wegkürzen und liefert mindestens \(\min(a^2,b^2)=b^2\) zur Austrittsnorm. Auch Flux-Superpositionen ändern diesen unitären Beitrag nicht.

Dies ist ein reparierter Beweis für den festgelegten **Besetzungsmuster-Scope**. Es ist kein Satz für beliebige feste verschränkte Materievektoren, beliebige Graphen oder beliebige dynamisch gedresste Codes. Die Behauptung einer für alle gemischten Muster **volumenextensiven** Schranke folgt daraus nicht: Auf einem geraden Torus kann eine Hälfte der Orte beide Moden besetzt und die andere Hälfte beide leer haben. Die Gesamtladung ist null; ein ganzzahliger kompensierender Gaussfluss existiert auf dem verbundenen Graphen. Nur an einer endlich dicken Grenzschicht sind die endlichen Reichweiten-Hops erlaubt. Für einen einzelnen kompatiblen Fluxbasiszustand ist der diagonale Austritt null und die Hopping-Austrittsnorm höchstens von Ordnung \(L^2\), nicht zwingend \(L^3\). Der extensive Satz bleibt für das besondere all-low Muster richtig.

Die elektrische Nichtstationarität des bezeichneten S ist korrekt. Mit expliziter Plaquettenorientierung lautet die Wilsonformel

\[
e^{-itH_E}We^{itH_E}
=W\exp[-it\kappa(\sum_ep_eE_e+2)].
\]

Dabei \(p_e=\pm1\) und \(\sum p_e^2=4\); Vorzeichen dürfen nicht aus einer unorientierten Summe verschwinden. Nichtstationäre feste Marken widerlegen keine gemeinsam mitbewegten Marken. „Die einzige exakte Closure“ ist zu stark: Die mitbewegte Darstellung ist eine verfügbare exakte Konstruktion; daneben sind größere invariante Räume und deren konkret nachzuweisende Markierungen nicht ausgeschlossen.

## 3. Theorem 2: Dressing ist ein erster Schritt, kein Allordnungs-Satz

Die Formel für eine erste perturbative Beimischung ist unter den angegebenen nichtresonanten Nennern sinnvoll. Ein exakter Restfehler für vier Ringvektoren wäre nach Korrektur und erneuter unabhängiger Kontrolle ein belastbarer endlicher Befund. Daraus folgen weder „keine endliche Dressing-Ordnung kann schließen“ noch „kleinste dynamisch konsistente Erweiterung“. Dafür fehlen ein allgemeines Nichtabbruchargument beziehungsweise ein definiertes Minimalitätskriterium mit Beweis. Die Formulierung in `ERGEBNISSE.md`, es existiere deshalb kein endlicher invarianter Code mit kommutierender Z₄-Markierung, ist entsprechend unbelegt. Ein bloßer Z₄-Operator lässt sich sogar diagonal auf Energieeigenvektoren definieren; der anspruchsvolle Herkunftssatz verlangt dieselben vorgegebenen markierten Operationen und Beziehungen. Ein ganzer mit H kommutierender M₄-Faktor stellt wiederum andere, insbesondere Degenerationsanforderungen.

**Zweiter konkreter Scope-Test:** Im unbeschnittenen kubischen Parent gilt für einen erlaubten Hop

\[
\Delta(E)=M-\epsilon_L+\frac{2\sigma E+1}{200}
=\frac{9587+24\sigma E}{2400}.
\]

Bei \(\sigma E=-399\), erreichbar in einem Gauss-neutralen Wilsonloop-Fluxzustand, ist

\[
\Delta=\frac{11}{2400},\qquad \left|\frac b\Delta\right|=\frac{100}{11}>9.
\]

Für ganzzahliges E ist dieser einzelne Nenner zwar nie null, aber weder \(\Delta\approx4\) noch eine kleine Beimischung gelten gleichmäßig auf dem ganzen Rotor. Bei \(\sigma E=-400\) ist der Nenner bereits negativ. Eine kontrollierte Dressing-Aussage benötigt deshalb den konkreten Fluxbereich oder einen geeignet bewiesenen Zustands-/Energiekontrakt. Das ist unabhängig vom andernorts identifizierten LL2-Checkerproblem.

Eine bereits konkrete exakte Alternative zum Minimalitätsanspruch steht in `tfpt/ERWEITERUNG.md`: Für den ursprünglichen 16-Code ist \(\eta=\Gamma/\sqrt{N/96}\) eine neue Isometrie. Der erste Hamilton-Kopplungsblock ist exakt \(\sqrt{N/96}I\). Weitere tatsächliche Richtungen sind der neutrale Onsite-Loch/High-Kanal mit Kopplung \(-I/\sqrt{24}\) und ein positiv normierter Zwei-High-Kanal. Dies beweist den Nichtabschluss **dieser ersten Erweiterung**, ohne einen unbelegten Allordnungs-No-go daraus zu machen.

## 4. Theorem 3: Radix richtig, Algebra nur mit Topologie bestimmt

Die eindeutige Zerlegung \(n=4q+r\), \(E=4Q+R\), \(U=CL\), \(ZL=iLZ\) und (3.1) sind exakt. Der Kreuzterm \(8QR\) verhindert eine autonome elektrische Dynamik der vier Restklassen.

„Alg(L,E)=⊕ M₄“ ist ohne Festlegung ungenau, weil E unbeschränkt ist. Eine präzise Fassung verwendet die beschränkte Spektralalgebra von E und den von ihr und L erzeugten von-Neumann-Abschluss:

\[
W^*(L,\{f(E):f\in\ell^\infty(\mathbb Z)\})
\cong\ell^\infty(\mathbb Z;M_4).
\]

Das ist das beschränkte Produkt der q-Blöcke, nicht die algebraische direkte Summe oder zwingend die c₀-Summe. Die elektrische Dynamik erhält es blockweise. Fügt man U hinzu, ist der **von-Neumann-Abschluss** tatsächlich \(B(\ell^2(\mathbb Z))\): Ein mit allen Fluxprojektionen kommutierender Operator ist diagonal; kommutiert er zusätzlich mit U, ist seine Diagonale konstant. Das Kommutant ist somit skalar, das Bikommutant ganz B(H).

Für den **Normabschluss** ist die entsprechende Aussage falsch. Endliche Summen \(\sum_{|k|\le K}U^kf_k(E)\) haben endliche Bandbreite. Die Überlagerungsisometrie \(S_m|n\rangle=|mn\rangle\), \(m>1\), hat Abstand mindestens eins zu jedem solchen Operator A: Für genügend großes |n| liegt |mn⟩ orthogonal zum ganzen möglichen Träger von A|n⟩. Also \(\|(S_m-A)|n\rangle\|\ge1\). Der Normabschluss enthält S_m nicht. Native Zugehörigkeit zu der im Original bereits gewählten großen lokalen Algebra B(H), starke Erzeugung, Normerzeugung und dynamisch realisierbare Operation sind unterschiedliche Aussagen.

## 5. Theorem 4: Überlagerung richtig, Gauss- und Dynamik-Scope präzisieren

Die Isometrie-, Cuntz-, Gradmultiplikations- und Intertwineridentitäten (4.1) sind auf dem elektrischen Kern richtig und besitzen die üblichen passenden Operator-/Definitionsbereichsfortsetzungen. Die Primzahlrolle ist die eindeutige Zerlegung des positiven Überlagerungsgrades; daraus folgt noch keine Auswahl einer physikalischen Zeit oder eines arithmetischen Readers.

Auf dem reinen Plaquettenloopsektor \(E=\Phi p\) gilt

\[
H_E=\frac\kappa2\|p\|^2\Phi^2=2\kappa\Phi^2,
\]

und die **elektrische** Energie skaliert unter \(\Phi\mapsto m\Phi\) mit m². Dies ist keine m²-Skalierung des gesamten wechselwirkenden H und kein universeller Operationskostenvertrag.

Der volle physische Anschluss hängt von der konkreten Erweiterung ab. Die komponentenweise Skalierung aller Linkfluxe \(E\mapsto mE\) skaliert auch div E und verletzt bei festgehaltener geladener Materie im Allgemeinen Gauss. Eine andere, explizite Erweiterung erhält Gauss **auch bei geladenen Hintergründen**: Wähle einen Anker mit \(p_e=1\), schreibe eindeutig

\[
E=np+\xi,\qquad n=E_e,\quad\xi_e=0,
\]

und definiere die Isometrie \(|n,\xi,\mathrm{matter}\rangle\mapsto|mn,\xi,\mathrm{matter}\rangle\). Weil div p=0, bleibt div E unverändert. Der Anker und die Schleife bleiben ausdrücklich zusätzliche Markierungsdaten. Auf beliebigem Hintergrund lautet die elektrische Energiedifferenz jedoch

\[
\frac\kappa2\left[(m^2-1)n^2\|p\|^2
+2(m-1)n\langle\xi,p\rangle\right],
\]

nicht eine globale Multiplikation der gesamten Energie mit m². Ein nur auf dem reinen Loopsektor definierter S_m ist noch kein definierter Operator auf dem ganzen physischen Raum; eine solche Erweiterung muss bezeichnet werden.

Schließlich: Ein echter S_m mit m>1 kann auf dem ganzen Hilbertraum nicht gleich einer einzelnen geschlossenen-H-Evolution \(e^{-itH}\) sein, weil er eine echte Isometrie mit nichtsurjektivem Bild ist, während die Evolution unitär ist. Das ist ein harter, passender No-go. Dagegen beweist die endliche Shiftvokabel des Generators allein keine allgemeine Nichterreichbarkeit durch Dynamik, Kontrollen oder Messinstrumente: Schon das Exponential eines endlichen Bandoperators kann unendlich viele Verschiebungsweiten enthalten. Hier müssen realisierbare Kontrollen, Zeit, Hilfsregister und Erfolgswahrscheinlichkeit ausdrücklich festgelegt werden.

## Reproduzierbare Beleggrenze

`check_fable_dynamics_review.py` liefert **neun exakte Kontrollen**, darunter den vollständigen nativen CAR/Flux-Gegenzeugen zu Theorem 1, den nichtkleinen Dressing-Nenner und die Gauss-erhaltende Schleifenkoordinaten-Erweiterung mit ihrem Energiekreuzterm. Ergebnis: `fable-dynamics-review-checks.json`. Die allgemeinen Aussagen werden durch die ausgeschriebenen Argumente getragen, nicht durch die Anzahl der Kontrollen. Quellen und neue Artefakte sind in `fable-dynamics-review-pins.json` gehasht; die Originale bleiben unverändert.
