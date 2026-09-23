# Originalaudit: gemeinsamer D5+A3-Lift der primitiven Quelle

## Begrenztes Ergebnis

**Verdict: PARTIAL mit einem echten positiven Fortschritt.** Die Originalarchitektur definiert den globalen Quotienten

\[
K=\frac{\operatorname{Spin}(10)\times SU(4)}{\Delta\mathbb Z_4}
\]

und die diagonale zentrale Neutralität der Darstellung \((16,4)\) exakt. Damit verschwindet das Vorzeichenproblem eines isolierten Spin(10)-Lifts: Ein ungerader U(5)-Clutchingloop hebt in \(\operatorname{Spin}(10)\) zu einem Pfad mit Endpunkt \(-1\); zusammen mit einem SU(4)-Pfad von \(1\) nach \(-I_4\) ist er ein geschlossener Loop in \(K\). Auf \((16,4)\) wirkt der Endpunkt als \((-1)(-1)=+1\).

Die Originale liefern jedoch **keine markierte Abbildung**

\[
\Phi_{\rm joint}: [u_\Sigma]=1\in K^1(S^1)\longmapsto [g_K]\in\pi_1(K)\cong\mathbb Z_4
\]

und wählen auch nicht eindeutig den kürzesten der kompatiblen gemeinsamen Lifts. Die exakte E8-Verklebung ist daher die richtige Zielstruktur und beseitigt die isolierte Spin-Hürde, aber sie ist noch keine Herleitung der physischen Quellenabbildung oder der Familienprojektivität.

## 1. Was im Original tatsächlich exakt festgelegt ist

### 1.1 Globaler Quotient und gekoppelte Zentralwirkung

`tfpt_1_architecture_e8.tex:5141-5165` gibt die exakte Verzweigung

\[
\mathfrak e_8=(45,1)\oplus(1,15)\oplus(10,6)\oplus(16,4)\oplus(\overline{16},\overline4).
\]

`tfpt_1_architecture_e8.tex:5198-5219` identifiziert die beiden Diskriminantengruppen mit \(\mathbb Z_4\), den Index vier und die isotrope diagonale Glue-Klasse. Auf Gruppenebene steht in `tfpt_1_architecture_e8.tex:5325-5336` ausdrücklich

\[
K=\frac{\operatorname{Spin}(10)\times SU(4)}{\Delta\mathbb Z_4}\subset E_8,
\]

mit Zentralcharakteren \((16,4):1+3=0\pmod4\) und \((10,6):2+2=0\pmod4\). Das ist mehr als bloße Dimensionsarithmetik: \((16,4)\) ist eine echte Darstellung des Quotienten.

Wählt man einen Generator \(z\in Z(\operatorname{Spin}(10))\) mit Wirkung \(i\) auf der 16, dann kann der Quotientskern als

\[
\langle (z,-iI_4)\rangle
\]

geschrieben werden. Sein Quadrat ist \((-1,-I_4)\). Da beide Faktoren der Überlagerungsgruppe einfach zusammenhängend sind, gilt \(\pi_1(K)\cong\mathbb Z_4\); der Vorzeichen kompensierende Loop ist die Klasse \(2\).

### 1.2 Die E8-Glue-Klasse ist arithmetisch starr

`tfpt_research_contracts.tex:11071-11095` und der dazugehörige Originalcheck `verification/v492_celestial_z4_orbifold.py:13-43` zeigen eine innere Ordnung-vier-Graduierung und lesen auf D5- und A3-Seite dieselbe diagonale Diskriminantenklasse \((1,1)\). Die ganzzahligen konformen Gewichte der diagonalen Glue-Sektoren belegen die Lokalität der E8-Erweiterung.

Das ist die exakte gemeinsame **Kompatibilitätsstruktur**. Der Check grenzt seine Reichweite selbst ein: `verification/v492_celestial_z4_orbifold.py:65-74,579-587` bezeichnet `clock^2=deck` als zusätzliche, durch die Arithmetik nicht erzwungene Identifikation und konstruiert weder die Kontinuumsquelle noch die physische Feldabbildung.

### 1.3 Die U(5)-Bündelklasse ist topologisch bereits bestimmt

Der ursprüngliche Higgs-/Clutching-Satz setzt

\[
(c_1(L_2),c_1(L_3))=(1,0)
\]

fest (`_archive/paper-latex/tfpt-42.tex:3900-3978`). Auf \(S^2\) bestimmt \((\operatorname{Rang},c_1)\) ein komplexes Vektorbündel bis Isomorphie; deshalb ist das Fehlen eines ausgeschriebenen diagonalen U(5)-Loops keine zusätzliche topologische Lücke. Der positive gemeinsame Lift beginnt genau bei dieser bereits ausgewählten odd-\(c_1\)-Klasse.

## 2. Der konstruktive gemeinsame Lift

Für einen odd-\(c_1\)-U(5)-Loop bildet die reelle U(5)-Wirkung den Generator von \(\pi_1(U(5))\cong\mathbb Z\) modulo zwei auf \(\pi_1(SO(10))\cong\mathbb Z_2\) ab. Sein Spinlift endet daher bei \(-1\). Jeder SU(4)-Pfad \(1\to-I_4\) ergänzt ihn zu einem Loop der Klasse \(2\in\pi_1(K)\). Diese Kompensation ist kanonisch auf Ebene der Endpunkte, aber der konkrete SU(4)-Kocharakter ist damit noch nicht eindeutig.

Der begrenzte exakte Check `work/source-joint-lift-20260922/checker.py` zeigt zwei ganzzahlige Homomorphismen ohne Quadratwurzelbündel:

\[
W_m=\Lambda^{\rm even}E\otimes\bigoplus_{j=1}^{4}(\det E)^{m_j},
\qquad \sum_jm_j=-2.
\]

Beide folgenden Wahlen schließen alle 64 Gewichte von \((16,4)\), liegen in Quotientenklasse 2 und erhalten dieselben Standardmodell-Ladungsmultiplizitäten:

| Lift | A3-Gewicht \(\beta=m+\frac12(1,1,1,1)\) | E8-Kocharakternorm² | Gradverteilung auf \(W_m\) |
|---|---:|---:|---:|
| \(m=(0,0,-1,-1)\) | \((\frac12,\frac12,-\frac12,-\frac12)\) | \(1+1=2\) | \((-1)^{16},0^{32},1^{16}\) |
| \(m=(0,0,0,-2)\) | \((\frac12,\frac12,\frac12,-\frac32)\) | \(1+3=4\) | \((-2)^8,(-1)^8,0^{24},1^{24}\) |

Der erste Lift ist besonders stark: Sein D5-Anteil ist das Vektorgewicht der weak-Determinantenrichtung mit Normquadrat 1, sein A3-Anteil liegt im Weyl-Orbit von \(\lambda_2\) mit Normquadrat 1. Zusammen ist er eine E8-Wurzel im \((10,6)\)-Sektor, also im Gluegrad 2. Das passt exakt zu `tfpt_1_architecture_e8.tex:5338-5364`, wo \((10,6)\) als Normzerlegung \(1+1=2\) erscheint.

**Dieser letzte Pfeil ist aber eine neue Rekonstruktion, kein bereits bewiesener Originalpfeil.** Der Higgs-Satz (`tfpt-42.tex:3900-3978`) führt weder ein A3-Gewicht \(\lambda_2\), noch den Quotienten \(K\), noch eine E8-Kocharakternorm ein. Umgekehrt liest die E8-Tabelle den \((10,6)\)-Block als D5-Vektor mal A3-Sechser, identifiziert ihn aber nicht mit der physischen weak-Determinanten-Clutchingrichtung. Die strukturelle Übereinstimmung ist daher ein begründeter Kandidat, noch keine Quellenherleitung.

## 3. Warum „primitive Nahtwindung“ den kürzesten Lift noch nicht nachweislich auswählt

Der primitive Ursprungssatz definiert ausschließlich

\[
[u_\Sigma]=1\in K^1(S^1)\cong\mathbb Z,
\qquad \operatorname{SF}(U_\Sigma)=1
\]

(`_archive/paper-latex/tfpt-42.tex:2319-2355`). Er enthält keine Abbildung in \(\pi_1(K)\), keinen A3-Kocharakter und keine E8-Norm.

Auch die spätere lexikographische Minimalität enthält keine **explizite** E8-Norm. Ihre fünf Einträge in der v4.2-Fassung sind

\[
\bigl(|\operatorname{SF}|,\operatorname{rank}H_{\rm prim}^{\rm fin},N_{\rm corner},c_1(L_2)+c_1(L_3),\dim\ker B_\Sigma\bigr)
\]

(`_archive/paper-latex/tfpt-42.tex:9017-9033`). Der Beweis wählt daraus die Windung eins und die Determinantenklasse \((1,0)\) (`tfpt-42.tex:9061-9105`), enthält aber weder die gemeinsame E8-Kocharakternorm noch das A3-Gewicht. Die beiden oben angegebenen Lifts stimmen in Windung, endlichem Rang, Eckenzahl, Determinantenklasse und Standardmodell-Ladungen überein. Beide sind als Gitterelemente primitiv; „primitiv“ allein unterscheidet Normquadrat 2 und 4 nicht.

**Korrektur nach Prüfung des letzten Defekts:** Aus dem Original folgt noch nicht, dass auch der letzte Nullitätseintrag für beide Lifts gleich ist. In der präziseren v4.5-Quellenfassung wird der letzte Defekt als

\[
d_3(B)=h_\Sigma^{\mathrm{red}}(B)
\]

definiert, als „residual boundary nullity after Calderon normal form“ (`_archive/tfpt-45/source_extracts/01_boundary_kernel_source.tex:523-559`). Eine konkrete Formel, das zugrunde liegende assoziierte Bündel und die Abhängigkeit von einem A3-Kocharakter werden dort nicht angegeben. Deshalb bleibt logisch möglich, dass eine noch zu konstruierende gemeinsame Realisierung die beiden Lifts über \(h_\Sigma^{\mathrm{red}}\) unterscheidet. Das bestehende Original beweist diese Auswahl aber nicht.

Genauer ist \(B_\Sigma\) nur als selbstadjungierter tangentialer Randoperator auf \(\Sigma=\partial M_+\) definiert, kompatibel mit den Randrestriktionen von \(J,\Gamma\), mit

\[
D_+=\gamma_n(\partial_n+B_\Sigma)
\]

(`tfpt-42.tex:909-925`; entsprechend `tfpt-45/source_extracts/01_boundary_kernel_source.tex:65-81`). Er wirkt auf den Rand-/Cauchydaten der abstrakten einseitigen Hilbertstruktur \(\mathcal H_+\). Eine Faktorisierung \(L^2(\widetilde M,S)\otimes\mathcal H_{\rm int}\) ist ausdrücklich nur eine analytische Realisierungswahl und kein Bestandteil des Randdatums (`tfpt-42.tex:927-935`). Der primitive Hilbertraum enthält zunächst nur Naht- und Gap-Sektor; Carrier- und Determinantenprojektoren kommen später (`tfpt-42.tex:1026-1044,1118-1143`). Die v4.5-Definition des primitiven Randkerns sagt zusätzlich ausdrücklich, dass noch keine Familiengeometrie oder Determinantenklasse Teil dieses Kerns ist (`tfpt-45/source_extracts/01_boundary_kernel_source.tex:714-731`). Ein gemeinsamer A3-Familienlift oder eine Ladungsauflösung von \(B_\Sigma\) ist somit nicht ausgeschrieben.

Dabei ist \(B_\Sigma\) nicht aus \([u_\Sigma]\) allein rekonstruiert. Der operative Seed enthält bereits

\[
(\mathfrak A_{\rm loc},\tau_t,\Theta,\omega,[u_\Sigma],\mathcal D_{\rm coll}),
\]

also Observable-Netz, Zeitentwicklung, Zustand und elliptischen Collaroperator als Eingaben (`tfpt-45/source_extracts/01_boundary_kernel_source.tex:465-497`). Die OS-Rekonstruktion liefert \(\mathcal H_+\), und \(\mathcal D_{\rm coll}\) bestimmt danach \(B_\Sigma\) (`ibid.:499-520`). Falls die Restnullität später zwischen den beiden gemeinsamen Lifts unterscheidet, wäre dies daher eine Auswahl durch den bereits gelieferten Operator-/Zustandsseed, nicht eine Herleitung aus primitiver Windung oder E8-Glue allein. Für die Ursprungsfrage müsste zusätzlich gezeigt werden, warum der Seed genau den unterscheidenden Collaroperator auswählt.

Die im exakten Hilfscheck ausgegebenen CP¹-Zahlen sind hiervon strikt getrennt: \([16,16]\) beziehungsweise \([24,24]\) sind bedingte **zweidimensionale Bulk-Dirac-Nullmoden** auf CP¹, nicht \(\dim\ker B_\Sigma\) und nicht \(h_\Sigma^{\rm red}\). Sie dürfen die letzte lexikographische Koordinate weder belegen noch widerlegen.

Als zusätzliche, ausdrücklich bedingte Kontrolle gilt: Für die standardmäßige Monopol-Chernverbindung am Äquator hängt die skalare Rand-Dirac-Spektralmultiplizität eines Summanden \(L^k\) nur von der Holonomie \((-1)^k\) ab. Lift A besitzt insgesamt 32 gerade und 32 ungerade Grade; Lift B ebenfalls 32 gerade und 32 ungerade Grade. Das **über alle internen Komponenten unaufgelöste** Kreisspektrum, einschließlich seiner Gesamt-Nullität, ist in dieser einfachsten Realisierung daher gleich. Ladungsaufgelöst sind die Verteilungen dagegen nicht identisch: Bereits im Ladungssektor 6 besitzt A zwei positive und zwei negative Holonomiezeichen, B vier negative. Ein Randoperator oder eine Calderón-Reduktion, die diese später definierte Feldraumgradierung sieht, könnte also unterscheiden. Das ist weder der originale abstrakte \(B_\Sigma\) noch ein Beweis seiner Nullität; es lokalisiert nur die noch fehlende Angabe auf die gemeinsame Operatorwirkung samt Gradierung.

`tfpt_1_architecture_e8.tex:5338-5364` beweist zwar, dass die 240 E8-Wurzeln Normquadrat 2 haben. Das ist eine Klassifikation bereits gewählter Wurzeln, keine Regel, nach der die Nahtquelle unter allen kompatiblen Klasse-2-Kocharakteren einen Wurzelvektor minimiert.

Damit ist „wähle den kürzesten kompatiblen E8-Kocharakter“ weiterhin eine **zusätzliche Auswahlregel**, solange weder eine entsprechende Killingnorm im Quellfunktional noch ein konkret gekoppelter Randoperator mit nachgewiesen kleinerer Restnullität hergeleitet wird. Die stärkere Aussage, der letzte Nullitätsterm könne grundsätzlich keine Auswahl leisten, wird nicht behauptet.

## 4. Folgt die benötigte Familienprojektivität aus den vier Nahtmarken?

Nein, jedenfalls nicht aus den derzeit ausgeschriebenen Abbildungen.

* Die vier Marken liefern exakt den A3-Wurzelraum: \(H_1(\mathbb P^1\setminus\mu_4)=\mathbb Z^3\), und die Vierteldrehung wirkt als A3-Coxeterelement mit Spektrum \(\{i,-1,-i\}\) (`tfpt_1_architecture_e8.tex:5173-5195`). Das ist eine Weyl-/Permutationswirkung auf dem reduzierten Rang-drei-Raum.
* Der kompensierende Lift benötigt dagegen einen **zentralen SU(4)-Pfad** mit Endpunkt \(-I_4\). Die Weylwirkung des Vierzyklus ist kein solcher Pfad.
* Das Original unterscheidet ausdrücklich beide Seiten: SU(4)/\(\mathbb Z_4\) gehört zur Vier-Ecken-/Glue-Seite, die physische Flavor-Monodromie wirkt auf \(H_1\cong\mathbb C^3\) und ist SU(3)-wertig (`origin_theory.tex:1210-1218`).
* Die physische Rang-drei-Verbindung ist sogar nur **unter der Annahme** einer flach trivialen Determinantenlinie SU(3)-wertig (`tfpt-42.tex:3702-3726`). Unter \(4\to3+1\) wirkt \(-I_4\) auf dem Dreierraum als \(-I_3\), dessen Determinante \(-1\) ist; es ist also keine Holonomie dieser SU(3)-Verbindung.

Folglich müsste die Theorie entweder das volle Vier-Ecken-SU(4)-Bündel zunächst als Teil des physischen \((16,4)\)-Feldes behalten und anschließend die Reduktion auf drei Familien definieren, oder eine projektive/U(3)-Erweiterung des Rang-drei-Familienbündels angeben. Keine dieser markierten Feldabbildungen ist in den geprüften Originalen definiert.

## 5. Erste noch fehlende mathematische Angabe

Die früheste fehlende Angabe ist nun präziser als „Spinstruktur offen“:

\[
\boxed{
\Phi_{\rm joint}:[u_\Sigma]=1\longmapsto
[g_K]=2\in\pi_1\!\left((\operatorname{Spin}(10)\times SU(4))/\Delta\mathbb Z_4\right),
}
\]

zusammen mit der Wahl des SU(4)-Kocharakters und der zugehörigen physischen Feldabbildung. Die Zahl 2 ist kein Widerspruch zur primitiven ganzzahligen Nahtklasse; sie ist deren noch herzuleitendes Bild im endlichen Quotienten. Sie darf aber nicht aus der bloßen Namensgleichheit der \(\mathbb Z_4\)-Strukturen eingesetzt werden.

Der kleinste entscheidende Folgetest ist kein weiterer Modellzweig: Konstruiere aus dem **bereits behaupteten einseitigen Collaroperator** den tatsächlichen gemeinsamen Randoperator

\[
B_\Sigma(W_m)\quad\text{auf dem }K\text{-assoziierten }(16,4)\text{-Bündel}
\]

und vergleiche \(h_\Sigma^{\rm red}\) für die beiden kompatiblen Lifts. Nur wenn diese Nullitäten verschieden und die kleinere eindeutig beim Norm-2-Lift liegt, wählt die vorhandene Defektlexikographie ihn ohne neue Normregel. Sind sie gleich — wie in der bedingten skalaren Monopol-Randrealisierung — ist im zweiten Schritt zu prüfen, ob das vorhandene Quellen-/Randfunktional nachweislich ein positives Vielfaches der E8-Killingnorm enthält. Der aktuelle Text führt weder die gemeinsame Randoperatorabbildung noch diesen Normterm aus.

## 6. Geprüfte Originalquellen und Reichweite

1. `tfpt_1_architecture_e8.tex:5141-5219,5315-5364` — D5+A3-Verzweigung, diagonale Z4-Glue, globaler Quotient, Normzerlegung der E8-Wurzeln.
2. `tfpt_research_contracts.tex:11045-11128` — innere Z4-Graduierung, exakte Glue-Arithmetik, ausdrücklich zusätzliche Clock–Deck-Identifikation und offene Kontinuumsäquivalenz.
3. `verification/v492_celestial_z4_orbifold.py:1-78,570-592` — ausführbarer Originalcheck mit eigener Reichweitenbegrenzung.
4. `origin_theory.tex:1199-1218` — konforme D5+A3-Einbettung und ausdrückliche Trennung von SU(4)-Glue und SU(3)-Flavor-Monodromie.
5. `_archive/paper-latex/tfpt-42.tex:909-1143,2319-2358,3678-3726,3898-4077,8930-9105,9158-9338` — Definition und Reichweite von \(B_\Sigma\), primitive Nahtklasse, physischer Rang-drei-Raum, determinant-triviale SU(3)-Holonomie, weak-Determinanten-Clutching und Minimalitätskriterien.
6. `_archive/tfpt-45/source_extracts/01_boundary_kernel_source.tex:42-90,500-560,627-709,714-731` — präzisere Defektfiltration mit \(h_\Sigma^{\rm red}\), Essentialisierung und ausdrückliche Abwesenheit von Familiengeometrie im primitiven Randkern.

Der Audit behauptet keine physische Zeitentwicklung, keinen CAR-Zustand und keine neue Flavor-Dynamik. Er zeigt ausschließlich: Der ursprüngliche E8-Quotient trägt einen sauberen gemeinsamen globalen Lift und beseitigt die isolierte Spin-Vorzeichenhürde; die Quelle wählt diesen Lift und insbesondere seinen kürzesten Vertreter noch nicht aus.
