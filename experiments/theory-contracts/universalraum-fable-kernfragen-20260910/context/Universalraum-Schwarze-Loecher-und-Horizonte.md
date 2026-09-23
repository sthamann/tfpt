# Horizonte, Entropie und physikalische Zeit: belastbarer Anschluss

Stand: 10. September 2026. Geprüfte Primärliteratur und eigene elementare Ableitungen; kein TFPT-Gravitationsbeweis. **Die tragfähige Verbindung lautet: Eine Darstellung muss die tatsächlich zugänglichen Operationen und deren zeitliche Antworten erhalten. Daraus allein entstehen weder ein schwarzes Loch noch eine physikalisch normierte Uhr.**

## 1. Wann eine Zugriffsgrenze ein Ereignishorizont ist

Für eine zeitlich orientierte, asymptotisch flache Lorentz-Raumzeit mit zukünftigem Nullunendlich \(\mathscr I^+\) definiert man

\[
\mathcal B=M\setminus J^-(\mathscr I^+),\qquad
\mathcal H^+=\partial J^-(\mathscr I^+).
\]

Ein Ereignis in \(\mathcal B\) kann keinen zukünftigen kausalen Weg zu diesem Empfangsgebiet besitzen. Diese Definition benötigt die **globale Zukunft**; ein momentan nicht lesbarer Speicher genügt nicht. Für andere asymptotische Geometrien muss das Empfangsgebiet geeignet ersetzt werden. Ein scheinbarer Horizont auf einer gewählten räumlichen Zeitscheibe ist eine andere Konstruktion. Die Annahmen für einen klassischen Flächenzunahmesatz gehen über die Definition hinaus, insbesondere geeignete Energie- und globale Vorhersagbarkeitsbedingungen. [Carr–Hawking 1974, §2, S.404](https://adsabs.harvard.edu/pdf/1974MNRAS.168..399C).

Für unser Framework folgt als notwendige Zusatzstruktur: eine Zuordnung von Operationen zu Raumzeitregionen, eine kausale Ausbreitungsregel und ein festgelegter Beobachterzugriff. Eine abstrakte Unteralgebra beschreibt zunächst nur, welche Unterschiede der Zugriff auflösen kann. Gravitative Constraints machen zudem eine naive Tensorzerlegung „Innenraum ⊗ Außenraum“ nicht zu einer automatisch gültigen Voraussetzung.

## 2. Hawking-Antwort und Flächenentropie

Hawkings Rechnung verwendet Quantenfelder auf einem klassischen Kollaps-Hintergrund, einen definierten einlaufenden Vakuumzustand und ein spät annähernd stationäres, nicht extremales schwarzes Loch. Für eine schmale ausgehende bosonische Wellenpaketmode lautet das Resultat

\[
\langle N_\omega\rangle\simeq
\frac{\Gamma_\omega}{\exp(\hbar\omega/k_BT_H)-1},\qquad
T_H=\frac{\hbar\kappa}{2\pi c k_B}.
\]

Hier ist \(\Gamma_\omega\) der Absorptions-/Transmissionsfaktor und \(\kappa\) eine **Beschleunigung**. Bei der geometrischen Längenkonvention ist \(\kappa_{\rm geom}=\kappa/c^2\), entsprechend \(T_H=\hbar c\kappa_{\rm geom}/(2\pi k_B)\). Die Formel ist semiklassisch: nahe Planck-Krümmung oder beim letzten Verdampfungsstadium reicht diese Rechnung nicht aus. Ein thermischer Ausgangsfaktor bedeutet außerdem nicht, dass der gesamte Kollapszustand ein thermisches Gleichgewicht ist. [Hawking 1975, §2, besonders Gl.(2.29), S.211; S.219](https://astrofrelat.fcaglp.unlp.edu.ar/agujeros_negros/media/Papers/Hawking_1975-Particle_creation_by_black_holes.pdf).

Bekenstein begründete die Proportionalität von Entropie und Fläche; sein damaliges Abschätzungsverfahren bestimmte noch nicht den heute verwendeten Koeffizienten \(1/4\). [Bekenstein 1973, Gl.(14)–(18), S.2337–2338](https://doi.org/10.1103/PhysRevD.7.2333).

Für Einstein-Gravitation ergibt die Kombination der mechanischen ersten Hauptsatzrelation für benachbarte neutrale, nicht rotierende Gleichgewichtslösungen mit \(dE=T_HdS\):

\[
dE=\frac{\kappa c^2}{8\pi G}dA,
\quad dS=\frac{k_Bc^3}{4\hbar G}dA,
\quad S_{\rm BH}=\frac{k_BA}{4\ell_P^2},
\quad\ell_P^2=\frac{\hbar G}{c^3}.
\]

Die Integration fixiert die übliche Flächenform bis auf eine additive Konstante. Die erste Hauptsatzstruktur und die Zeitnormierung sind physikalische Eingaben, keine Folgen des Wortes „Information“. [Bardeen–Carter–Hawking 1973, §§2–4](https://doi.org/10.1007/BF01645742).

„Randentropie“ bezeichnet damit eine quantitative Gravitationsaussage. Sie besagt für sich allein nicht, dass alle Mikrozustände gewöhnliche lokale Teilchen auf der Randfläche sind. In anderen diffeomorphismusinvarianten Gravitationstheorien bestimmt die Wirkung eine allgemeinere Noether-Ladungsentropie; die nackte Flächenform ist nicht universell. [Wald 1993, Gl.(25)–(26)](https://arxiv.org/pdf/gr-qc/9307038).

## 3. Der bewiesene schmale Anschluss: modulare Zeit und Antworten

Bisognano–Wichmann identifizieren für eine geeignete lokale relativistische Feldtheorie den modularen Fluss der **Minkowski-Vakuum-Keilalgebra** mit Lorentz-Boosts. Vorausgesetzt werden unter anderem Poincaré-Kovarianz, Spektralbedingung, Lokalität und die passenden Operator-/Algebravoraussetzungen. In ihrer Konvention gilt

\[
\Delta=e^{2\pi K_3},\qquad
U(\Lambda(\eta))=e^{-i\eta K_3},\qquad
\Delta^{is}=U(\Lambda(-2\pi s)).
\]

Dies ist eine exakte Identifikation bestimmter Algebra-, Zustands- und Geometriedaten. Sie gilt nicht für ein beliebiges Paar aus Algebra und Zustand. Für eine gleichmäßig beschleunigte Bahn ist \(\eta=a\tau/c\); erst diese zusätzliche geometrische Zuordnung wandelt die dimensionslose KMS-Periode in \(T_U=\hbar a/(2\pi c k_B)\) um. [Bisognano–Wichmann 1975, S.985, §II, Theorem 2 und S.998](https://escholarship.org/content/qt2z26t9cd/qt2z26t9cd.pdf).

**Ein elementarer Antwort-Erhaltungssatz.** Seien \(\Phi:\mathcal A\to\mathcal A'\) ein *-Isomorphismus, \(\omega'\circ\Phi=\omega\), und \(\Phi\circ\alpha_t=\alpha'_t\circ\Phi\) für denselben physikalischen Zeitparameter. Dann gilt für beliebige zugängliche beschränkte Observablen

\[
\omega'(\alpha'_{t_1}(\Phi A_1)\cdots\alpha'_{t_n}(\Phi A_n))
=\omega(\alpha_{t_1}(A_1)\cdots\alpha_{t_n}(A_n)).
\]

Beweis: Intertwining in jeden Faktor einsetzen, Multiplikativität von \(\Phi\) anwenden, dann Zustandserhaltung. Damit bleiben auch Fourier-Antwortspektren und, bei Existenz der entsprechenden linearen Antwort,

\[
\chi_{AB}(t)=\frac{i}{\hbar}\theta(t)\,\omega([\alpha_t(A),B])
\]

erhalten. Die KMS-Randbedingung für analytische Elemente wird identisch transportiert, also auch ihre inverse Temperatur. Das ist ein **bedingter mathematischer Transfersatz**, keine neue Herleitung einer Hawking-Geometrie. Bei unbeschränkten Feldern müssen Definitionsbereiche und geeignete geschmierte Korrelatoren zusätzlich kontrolliert werden.

Wird dagegen \(\alpha_t\) nur auf \(\alpha'_{\gamma t}\) abgebildet, werden Frequenz- und Temperaturskalen mitverändert. Ein modularer Fluss liefert ohne solche Kalibrierung keine Sekunden oder Kelvin. Auch die geometrische Definition \(\xi^a\nabla_a\xi^b=\kappa_{\rm geom}\xi^b\) ändert \(\kappa_{\rm geom}\) bei \(\xi\mapsto b\xi\). Die übliche stationäre Zeit wird am Unendlichen normiert. [Wald 1993, Gl.(1), (21)](https://arxiv.org/pdf/gr-qc/9307038).

## 4. Exaktes Gegenbeispiel: thermisch ohne schwarzes Loch

Für \(\beta,\epsilon>0\) sei

\[
|\Psi\rangle=\frac{|00\rangle+e^{-\beta\epsilon/2}|11\rangle}
{\sqrt{1+e^{-\beta\epsilon}}},\qquad H_A=\epsilon|1\rangle\langle1|.
\]

Direktes Ausspuren ergibt

\[
\rho_A=\operatorname{Tr}_B|\Psi\rangle\langle\Psi|
=\frac{e^{-\beta H_A}}{\operatorname{Tr}e^{-\beta H_A}}.
\]

Der Gesamtzustand ist rein, die Einschränkung exakt Gibbs-förmig. Das System enthält dennoch weder eine Lorentz-Geometrie noch Gravitation, eine Horizontfläche oder eine kausale Einbahn-Grenze. Zusätzlich lassen \(H_A\mapsto bH_A\) und \(\beta\mapsto\beta/b\) dieselbe Matrix unverändert. **Thermische Reduktion impliziert weder Horizont noch eindeutige physikalische Temperatur.** Für \(e^{-\beta\epsilon}=1/3\) wurden Reinheit, partielle Spur und Gibbs-Identität exakt symbolisch geprüft; das ist eine elementare Gegenprobe, kein Gravitationsexperiment.

## 5. Was Rekonstruktion und Singularität erlauben

In einem kontrollierten holographischen Modell untersuchen Almheiri–Engelhardt–Marolf–Maxfield ein zweidimensionales JT-Gravitationssystem mit CFT und angeschlossenem Bad. Die relevante Fläche extremiert die verallgemeinerte Entropie; unter mehreren erlaubten extremalen Flächen wird die kleinste gewählt:

\[
S_{\rm gen}/k_B=A(X)/(4\ell_P^2)+S_{\rm bulk}(X)/k_B.
\]

Die Schreibweise zeigt den höherdimensionalen Einstein-Fall; in JT ersetzt der entsprechende Dilatonterm die Fläche. Der berechnete Wechsel der quantenextremalen Fläche liefert Page-artiges Verhalten im Modell. Rekonstruierbarkeit einer kodierten Innenraumobservable ist damit eine andere Frage als ein direkt aus dem Inneren auslaufendes kausales Signal. Das Resultat beweist keine vollständige vierdimensionale Verdampfungs- oder Singularitätsdynamik. [AEMM 2019, Einleitung und QES-Definition](https://arxiv.org/pdf/1905.08762).

Penroses klassisches Resultat erzwingt unter seinen geometrischen, Energie-, Cauchy- und Trapped-Surface-Voraussetzungen das Scheitern zukünftiger Nullgeodäten-Vollständigkeit. Es konstruiert keine Fortsetzung in einen anderen Zustandsraum und beweist für sich allein keinen Ereignishorizont. [Penrose 1965, S.58–59](https://journals.aps.org/prl/pdf/10.1103/PhysRevLett.14.57).

Die Deutung „Singularität = Ende einer Raumzeitprojektion“ ist daher eine **zulässige Forschungsfrage**, derzeit kein Folgesatz. Ein Beweis benötigt einen definierten erweiterten Zustandsraum, eine wohldefinierte Dynamik, eine Abbildung zur bekannten Raumzeit im gültigen Bereich und eine konsistente Fortsetzung der beobachtbaren Antworten. Das bloße Entfernen einer divergierenden Koordinate genügt nicht.

## 6. Erste konkrete TFPT-Anschlusslücke

Der nächste belastbare Nachweis wäre eine TFPT-Konstruktion, die **dieselben** Daten gemeinsam liefert: lokalisierte Observablen mit kausaler Ausbreitung; physikalisch normierte Zeit und Energie; geeigneten Feldzustand; daraus Horizont beziehungsweise Boost-Dynamik und messbare Antwort; schließlich gravitative Wirkung mit Newton-Kopplung, aus der die Entropie folgt. Ein Compiler-Spektrum oder ein positiver Zustand erfüllt diese Liste nicht automatisch.

Der engste positive Test ist die Konstruktion einer lokalisierten TFPT-Algebra und eines Zustands mit nachweisbarem geometrischem modularen Fluss **samt Zeitkalibrierung**. Erst dann kann der Antwort-Erhaltungssatz bekannte Horizontphysik übertragen. Die Zweiqubit-Gegenprobe sollte jeder breiteren Behauptung vorgeschaltet werden: Sie trennt echte zusätzliche Physik von bloßer Gibbs-Umschreibung.

## Quellen-Scope

- **Hawking 1975:** Original-PDF lokal extrahiert; S.199–206, 210–211 und 219 sowie relevante Passagen bis S.218 gelesen. Verwendet werden Kollaps-/Modenrechnung, Eq.(2.29) und semiklassische Grenze; späte historische Spekulationen sind keine bestätigten Folgerungen.
- **Bekenstein 1973:** Verlagsabstract und Originalscan S.2337–2339 visuell gelesen, besonders Eq.(14)–(19). Keine Zuschreibung des heutigen Viertel-Koeffizienten an seine damalige Abschätzung.
- **Bisognano–Wichmann 1975:** Berkeley-Reprint, §I–II, Theorem 2 und Tomita-Passage S.998 gelesen. Geltungsbereich: spezifizierte lokale relativistische Keilalgebra; kein allgemeiner Gravitationserzeugungssatz.
- **Bardeen–Carter–Hawking 1973:** Originalauszug S.162 zur Normierung gelesen; erste Hauptsatzrelation zusätzlich in Hawking S.203 und Wald Eq.(25) abgeglichen. Kein vollständiges Re-Audit aller Beweisschritte.
- **Carr–Hawking 1974:** Original §2, S.404–405 gelesen; verwendet werden Definitionen und deren geometrische Voraussetzungen, keine kosmologischen Zahlen von 1974.
- **Wald 1993:** Original S.4–5, 10–12, besonders Eq.(1), (21), (25)–(26), gelesen. Noether-Ladungsresultat für passende stationäre Lösungen; keine pauschale zweite Hauptsatzaussage.
- **AEMM 2019:** Originalabstract, Einleitung und QES-Definition gelesen. Verwendung auf dortiges semiklassisches JT/CFT/Bad-Modell begrenzt; kein allgemeiner Informationsparadox-Beweis.
- **Penrose 1965:** Original S.57–59 gelesen; Annahmen und Vollständigkeitswiderspruch, keine Quantengravitationsfortsetzung.
- **Eigene Rechnung:** endliches Zweiqubit-Gegenbeispiel, Zustand-/Dynamik-Transfer und SI-Koeffizienten; keine Behauptung wissenschaftlicher Neuheit.
