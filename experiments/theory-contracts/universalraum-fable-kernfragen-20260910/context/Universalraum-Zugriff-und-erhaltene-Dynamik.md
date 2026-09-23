# Wann eine eingeschränkte Sicht eine eigene Dynamik besitzt

10. September 2026. Endliche, exakt kontrollierbare Sätze und Gegenbeispiele zum gemeinsamen Prozessbild. Die Aussagen bestimmen, was beim Übergang zu einer beobachtbaren Darstellung erhalten bleiben muss. Sie sind keine Herleitung schwarzer Löcher, von Raumzeit oder Bewusstsein.

## 1. Der genaue Satz über den Verlust von Information

Seien V und W Vektorräume, E:V→W eine surjektive lineare Beobachtungsabbildung und T:V→V eine lineare Entwicklung. Zwei vollständige Beschreibungen v und v′ sehen gleich aus, wenn Ev=Ev′. Eine eigenständige Entwicklung auf der sichtbaren Beschreibung ist genau eine Abbildung T̄ mit

\[
ET=\overline T E.
\]

**Satz.** Eine solche lineare T̄ existiert genau dann, wenn

\[
T(\ker E)\subseteq\ker E.
\]

**Beweis.** Existiert T̄ und ist Ev=0, dann ETv=T̄Ev=0. Umgekehrt definiere T̄(Ev)=ETv. Sind Ev=Ev′, so ist v−v′∈ker E. Die Voraussetzung gibt ET(v−v′)=0, also ist der Wert unabhängig vom gewählten Vertreter. Surjektivität liefert Existenz auf ganz W und Eindeutigkeit; Linearität folgt aus der Definition. □

Der Satz gilt für jeden deklarierten Operationsgenerator. Er gilt dann durch Komposition für alle Wörter aus diesen Generatoren. Für inverse Operationen muss die Voraussetzung auch invers gelten; für endlichdimensionale V und invertierbares T folgt aus der Inklusion bereits Gleichheit der Kerne.

**Bedeutung:** Eine momentan unsichtbare Unterscheidung darf durch eine zulässige spätere Operation nicht wieder sichtbar werden, wenn die verkürzte Beschreibung wirklich abgeschlossen sein soll. Andernfalls braucht sie zusätzliche Gedächtnis- oder Umgebungsdaten.

## 2. Anwendung auf ein offenes Quantensystem

Für ein endliches System A und eine Umgebung B sei

\[
E(\rho)=\operatorname{Tr}_B\rho,\qquad
\mathcal T(\rho)=U\rho U^*.
\]

Gesucht ist ein einziger Kanal Φ auf A, der **für alle gemeinsamen Eingangszustände**, einschließlich Korrelationen, erfüllt:

\[
\operatorname{Tr}_B(U\rho U^*)=\Phi(\operatorname{Tr}_B\rho).
\]

Der Satz aus Abschnitt 1 liefert genau die Kernelbedingung. Falls sie gilt, ist die induzierte Abbildung sogar ein vollständig positiver spurerhaltender Kanal: Wähle irgendeinen festen Umgebungszustand τ_B und den Kanal R(σ)=σ⊗τ_B. Es gilt ER=id, und Φ=E𝒯R ist eine Komposition solcher Kanäle. Die Kernelbedingung garantiert, dass dieser Φ auch für korrelierte Eingaben richtig ist. Ohne sie gilt die übliche Formel nur für die vorgegebene Präparation mit τ_B.

## 3. Ein vollständiges Gegenbeispiel: momentan unsichtbar, später unterscheidbar

Setze

\[
|\Phi_\pm\rangle=\frac{|00\rangle\pm|11\rangle}{\sqrt2},
\qquad\rho_\pm=|\Phi_\pm\rangle\langle\Phi_\pm|.
\]

Auf A sehen beide Zustände identisch aus:

\[
E\rho_+=E\rho_-=I/2.
\]

Nun wirke die kontrollierte Nicht-Operation CNOT mit A als Steuerung und B als Ziel. Dann

\[
U|\Phi_\pm\rangle=|\pm\rangle_A\otimes|0\rangle_B,
\qquad E\mathcal T(\rho_\pm)=|\pm\rangle\langle\pm|.
\]

Eine X-Messung auf A unterscheidet die Ausgaben perfekt. Derselbe Eingang I/2 müsste unter einem angeblichen universellen Φ also zwei verschiedene Ausgänge erhalten. Das ist unmöglich. Konkret ist X₀=ρ₊−ρ₋ im Kernel von E, aber `E𝒯(X₀)=σ_x≠0`.

Eine reine Beschränkung des momentanen Zugriffs definiert folglich noch keinen dauerhaft undurchlässigen Horizont. Für einen kausalen Horizont müssen die **zulässigen** zukünftigen Operationen und erreichbaren Gebiete mitbestimmt werden. Die im Beispiel verwendete gemeinsame CNOT-Operation darf nicht nachträglich als von außen erlaubte Operation an einem wirklichen Innenraum vorausgesetzt werden.

## 4. Auch eine ungefähre Rückgewinnung hat eine beweisbare Grenze

Verwende den Spurabstand `D(ρ,σ)=||ρ−σ||₁/2`. Haben zwei Eingangszustände dieselbe sichtbare Beschreibung und sind ihre gewünschten sichtbaren Ausgaben η₊ und η₋, muss jede auf dieser Beschreibung allein arbeitende Regel denselben Kandidaten ξ liefern. Aus der Dreiecksungleichung folgt

\[
\max\{D(\eta_+,\xi),D(\eta_-,\xi)\}
\ \ge\ \frac12D(\eta_+,\eta_-).
\]

Im Bell/CNOT-Beispiel beträgt die rechte Seite 1/2. Kein genauerer Rechenalgorithmus und keine größere Datenstruktur, die nur mit I/2 initialisiert wird, kann diese fehlende Phaseninformation ergänzen. Zusätzliche Originaldaten oder ein eingeschränkter Eingabebereich können die Aufgabe verändern; aus der gleichen reduzierten Eingabe allein folgt die Schranke.

Dieselbe Dreiecksrechnung gilt für die Wiederherstellung der beiden ursprünglichen Bellzustände aus I/2. Eine echte Rekonstruktion benötigt also eine ausdrücklich bezeichnete Zustands-/Codefamilie, auf der die Antwort erhalten bleibt. Sie ist kein pauschaler Rückweg von jedem „Schatten“ zur ganzen Welt.

## 5. Eine streng einseitige Grenze passt nicht in jede endliche Unitärbeschreibung

Ein bekannter Satz verschärft die Aussage. Bei einer **festen endlichen bipartiten Zerlegung und einer globalen unitären Operation** ist vollständiges Nichtsignalisieren von B nach A nur möglich, wenn

\[
U=U_A\otimes U_B.
\]

Der klassische Satz steht bei [Beckman–Gottesman–Nielsen–Preskill, Theorem 7](https://arxiv.org/pdf/quant-ph/0102043). Hier folgt ein kurzer Algebra-Beweis für die oben ausdrücklich geforderte Abhängigkeit der reduzierten Ausgabe allein vom reduzierten Eingang.

Im Heisenbergbild gilt für jede Matrix a auf A

\[
U^*(a\otimes I)U=\Phi^*(a)\otimes I.
\]

Konjugation erhält Produkte und Adjunkte. Daher ist Φ* ein unitaler injektiver *-Homomorphismus der vollen endlichen Matrixalgebra in sich. Wegen gleicher Dimension ist er ein Automorphismus. Dieser ist durch ein Unitär V implementiert: `Φ*(a)=V*aV`.

Warum ist dieser letzte Schritt elementar? Die Bilder der Matrixeinheiten E_ii sind paarweise orthogonale minimale Projektionen mit Summe I; wähle ihre Einheitsvektoren. Die Produkte der Bilder von E_ij fixieren die relativen Phasen. In dieser Basis sind alle Bilder die ursprünglichen Matrixeinheiten. Der Basiswechsel ist V.

Nach Abziehen von V_A liegt U im Kommutanten der gesamten A-Algebra. Dieser ist `I_A⊗M_B`, also bleibt ein Unitär auf B. Damit ist U ein Produkt. Die Umkehrung folgt unmittelbar durch die partielle Spur. □

**Scope:** Dies ist kein Ausschluss schwarzer Löcher oder emergenter Horizonte. Ein ernsthaftes Modell kann lokale Feldalgebren, zeitlich wechselnde Gebiete, eingeschränkte physische Zustandsräume, offene Kanäle oder kontrollierte Grenzprozesse besitzen. Es ist ein Ausschluss der gleichzeitigen Kombination „feste endliche vollständige Tensorhälften + geschlossenes globales Unitär + nichttriviale streng einseitige Kopplung für sämtliche Zustände“. Ein kleines endliches Compilerregister darf daher nicht ohne zusätzliche Struktur als exakter Innen-/Außenraum ausgegeben werden.

## 6. Thermische Antwort ohne schwarzes Loch

Für 0<p<1/2 betrachte

\[
|\Psi_p\rangle=\sqrt{1-p}|00\rangle+\sqrt p|11\rangle.
\]

Der Gesamtzustand ist rein; auf A gilt `ρ_A=diag(1−p,p)`. Zu jedem gewählten Energieabstand ε>0 setze

\[
H_\varepsilon=\varepsilon|1\rangle\langle1|,\qquad
\beta_\varepsilon=\frac1\varepsilon\log\frac{1-p}{p}.
\]

Dann ist exakt

\[
\rho_A=\frac{e^{-\beta_\varepsilon H_\varepsilon}}
{\operatorname{Tr}(e^{-\beta_\varepsilon H_\varepsilon})}.
\]

Der endliche Beobachter sieht einen Gibbszustand mit positiver Entropie. Das Modell enthält weder eine Raumzeitmetrik noch eine Horizontfläche oder Gravitation. Die Gibbsform allein identifiziert deshalb keine Hawking-Strahlung. Außerdem bestimmt dieselbe Dichtematrix nur das Produkt βH bis zur additiven Normierung: Wird ε verdreifacht und β gedrittelt, bleibt ρ_A gleich. Für eine physische Temperatur muss die physische Energie- beziehungsweise Zeitnormierung zusätzlich feststehen.

Eine Gibbsform des Zustands ist auch noch keine Strahlungsflussberechnung: Dafür fehlen die Kopplung an einen Detektor, Ausbreitung, relevante Moden und deren tatsächliche Dynamik.

## 7. Was dieses Resultat dem Universalraum-Programm hinzufügt

Ein verlustfreier Darstellungswechsel, eine reduzierte Beobachtung und eine kausale Zugriffsgrenze sind drei unterschiedliche mathematische Operationen. Der frühere Graph-Transfer bewahrte den ganzen angegebenen Sektor. Eine partielle Spur verwirft dagegen Korrelationen. Ein Horizont benötigt zusätzlich die Organisation zulässiger künftiger Zugriffe.

Der neue direkte Prüfschritt für einen TFPT-„Schatten“ ist deshalb: **Den Original-Beobachter E und die Originaloperation T angeben und testen, ob zwei unter E identische Präparationen nach T verschieden antworten.** Ein solches Paar widerlegt eine behauptete abgeschlossene Dynamik sofort. Fehlt ein solches Paar, ersetzt ein endlicher Test noch nicht den allgemeinen Kernelbeweis. Für einen Horizont müssen schließlich der physische Zustandsbereich und die zugelassenen lokalen Operationen aus derselben Quelle folgen.

Die Beweise oben sind endlichdimensional und ausgeschrieben. `check_access.py` ergänzt konkrete Matrix-, Gibbs- und Kanalgegenprüfungen. Theorem 7 ist ein bekanntes Literaturresultat; die Darstellung und die Verbindung zum TFPT-Prüfvertrag sind keine Behauptung neuer mathematischer Priorität. Eine Identifikation mit einem konkreten TFPT-Horizont ist weiterhin offen.
