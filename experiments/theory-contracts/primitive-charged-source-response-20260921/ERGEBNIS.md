# TFPT: geladene Quellenantwort aus dem ursprünglichen Modell

21. September 2026 · Forschungsstand: **PARTIAL**

Der Auftrag verlangt die Herkunft der geladenen Felder, ihres Zustands und ihrer gemeinsamen Zeit aus der ursprünglichen Nahtquelle. Die geprüften Originalquellen liefern dafür zwei unterschiedlich weit bestimmte Objekte: den postulierten primitiven Nahtkern mit einem endlichen Auslesetransfer und eine explizite mikroskopische CAR-Realisierung. Ihre vollständige Identifikation ist weiterhin unbelegt. Die Rechnung unten verwendet ausschließlich die zweite, unabhängig vom späteren Randkandidaten definierte Quelle. Sie ist deshalb eine tatsächliche Quellenrechnung, aber noch keine Herleitung dieser Quelle aus P1/P2.

## 1. Ergebnis zu den drei verlangten Schritten

| Verlangter Schritt | Ergebnis | Beweisgrenze |
|---|---|---|
| Geladene Felder und Zustand aus dem ursprünglichen Nahtkern und Transfer | Im vorhandenen QWZ-Modell explizit bestimmt; der Übergang P1/P2 → dieses Modell bleibt offen. | Der finite Drei-Zustands-Transfer spezifiziert keinen geladenen lokalen Feldraum. |
| Gemeinsame Zeitkorrelatoren ohne Gamma, Vaux oder RR-Ziel | Für die wirklichen CAR-Felder des Modells einschließlich ihrer Produkte vollständig durch dessen Projektor und Einteilchengenerator bestimmt. | Der Feldgrenzwert ist ein vorhandener Satz vom 9. September; neu ist hier seine ausdrückliche gemeinsame Auswertung für den verlangten Quellenvergleich. |
| Ladungen, Produkte, Gram und Zeit mit dem bezeichneten Randkandidaten vergleichen | Ein reproduzierbarer Vergleich der Datenarten ist möglich; eine vollständige Gleichheit ist ohne eine hergeleitete Feldabbildung nicht definiert. | Ein passend gewähltes Wörterbuch oder die Übernahme des Kandidaten-W würde die zu beweisende Verbindung voraussetzen. |

Der Status der vollständigen physikalischen TFPT bleibt offen. Weder ein neuer Hilfshamiltonoperator noch ein vorausgesetzter RR-Block wird eingeführt.

## 2. Was die tatsächliche mikroskopische Quelle festlegt

Der ursprüngliche Contract `microscopic-charged-car-limit` verwendet den QWZ-Zylinder mit Breite 8, Masse 1 und Viertelholonomiesektor r=1. Diese Parameter und die CAR-Realisierung sind dort feste Modelldaten; ihre Auswahl aus P1/P2 ist kein Ergebnis dieses Berichts.

Für N Längsstellen und 16N Einteilchenmoden gelten

\[
P_N=\mathbf1_{h_N<0},\qquad D_N=\frac{N}{2\pi}h_N,
\]
\[
\Omega_N=\text{vollständig gefüllte negative See},\qquad
\mathcal H_N=d\Gamma(D_N)-\operatorname{Tr}(P_ND_N),\qquad
Q_N=d\Gamma(I)-8N.
\]

`dΓ` bezeichnet hier die gewöhnliche fermionische zweite Quantisierung des bereits vorhandenen Einteilchenoperators. Es bezeichnet **nicht** das ausgeschlossene zehnkanalige Gitter Gamma des Randkandidaten.

Die lokalen Quellfelder sind

\[
\Psi_N(f)=a_N(R_Nf),\qquad
R_Nf(x,y)=N^{-1/2}e^{-i\pi x/(2N)}f(x/N)\delta_{y,7}\frac{(1,1)}{\sqrt2}.
\]

Damit sind die Felder, ihr Ort, ihre Produkte, ihre Ladung und ihr Zustand gemeinsam definiert. Es gilt exakt

\[
[Q_N,\Psi_N]=-\Psi_N,\qquad
[Q_N,\Psi_N^\dagger]=\Psi_N^\dagger,
\quad \{a(f),a^\dagger(g)\}=\langle f,g\rangle I.
\]

Die untere Kante und die Bulkmoden werden bei der Definition von P_N und Omega_N nicht verworfen. Der untersuchte lokale Grenzwert betrifft die obere Kante.

## 3. Zeitkorrelatoren aus demselben Hamiltonoperator

Wir verwenden ein im zweiten Argument lineares Skalarprodukt und antilineare Vernichter a(f). Setze

\[
f_t=e^{itD_N}R_Nf.
\]

Dann folgen aus der tatsächlichen Quellzeit, ohne Zielanpassung,

\[
\Psi_N^\dagger(f,t)=a_N^\dagger(f_t),\qquad
\Psi_N(f,t)=a_N(f_t),
\]
\[
\langle\Psi_N^\dagger(f,t)\Psi_N(g,s)\rangle
=\langle g_s,P_Nf_t\rangle,
\]
\[
\langle\Psi_N(g,s)\Psi_N^\dagger(f,t)\rangle
=\langle g_s,(I-P_N)f_t\rangle.
\]

Der gefüllte Slaterzustand ist quasifrei. Deshalb ergeben sich alle endlichen Mehrzeitwörter aus diesen beiden Kontraktionen mit den CAR-Vorzeichen. Beispielsweise

\[
\left\langle
\Psi^\dagger(f_1,t_1)\Psi^\dagger(f_2,t_2)
\Psi(g_2,s_2)\Psi(g_1,s_1)
\right\rangle
=\det\left[\langle(g_a)_{s_a},P_N(f_b)_{t_b}\rangle\right]_{a,b=1,2}.
\]

Für n Erzeuger und n Vernichter ist es die entsprechende n×n-Determinante. Nicht normal geordnete Wörter werden unter Beibehaltung der zusätzlichen CAR-Kontraktionen umgeordnet. So werden auch gemeinsame Korrelationen von linearen Feldern, Paarprodukten und neutralen Bilinearen berechnet. Die Faktorisierung folgt aus dem definierten Slaterzustand; sie wird nicht nachträglich an P1 angehängt.

Die Anwendung der Wick-Struktur auf Mehrzeitfunktionen entspricht dem bekannten freien Fall, siehe [van Leeuwen–Stefanucci, 2012](https://arxiv.org/abs/1102.4814). Diese Literatur liefert keinen TFPT-Herkunftsbeweis.

## 4. Kontrollierter Randgrenzwert und Viertelladung

In der ursprünglichen ganzzahligen Modenbezeichnung ist

\[
\epsilon_j=\frac14-j,\quad j\in\mathbb Z,\qquad
P_{\rm edge}=\mathbf1_{j\ge1}.
\]

Teilchenmoden j≤0 haben Energie 1/4−j, Löcher in j≥1 Energie j−1/4. Äquivalent kann man r=1/2−j aus Z+1/2 verwenden. Dann lauten Einteilchenenergie und Seeprojektor

\[
h e_r=(r-1/4)e_r,\qquad C=\mathbf1_{r<0}.
\]

Auf dem geladenen Anregungsraum gilt

\[
\boxed{\mathcal H=L_0-\frac14Q.}
\]

Insbesondere bekommt ein Erzeuger relativ zur L0-Zeit den Faktor exp(−it/4), ein Vernichter exp(+it/4). Der Viertelterm ist in diesem Modell Teil derselben Quellenantwort. Er wurde nicht aus dem RR-Kandidaten übernommen.

Für endliche Fourierwörter und anschließend die im ursprünglichen Contract kontrollierte Verschmierung gilt beispielsweise

\[
K((g,s),(f,t))
=e^{-i(t-s)/4}\sum_{r<0}\overline{g_r}f_r e^{i(t-s)r}.
\]

Die positive euklidische Teilchenantwort ist entsprechend die Einschränkung von (1−C)exp(−τh), die Lochantwort diejenige von C exp(+τh), mit transponierter Labelanordnung für die antilinearen Lochzustände. Die volle gemeinsame Antwort wird aus denselben Kontraktionen gebildet.

Das ursprüngliche Randresultat enthält zudem

\[
E_{\rm top}(q)=\frac{q^2}{2}-\frac q4,\qquad q\in\mathbb Z.
\]

Das ist das Energieminimum innerhalb der oberen Randdarstellung. Es ist weder ein Minimum über den gesamten Zylinder noch eine Aussage über jede TFPT-Vervollständigung. Insbesondere werden die Moden nicht nachträglich auf 3,4,5 kalibriert.

## 5. Produkte und gemeinsamer Gramraum

Seien u_i=(1−C)f_i die unbesetzten Komponenten vorhandener Testmoden und

\[
p_{ij}=a^\dagger(f_i)a^\dagger(f_j)\Omega.
\]

Dann ist ihr wirklicher Gramoperator

\[
\langle p_{ij},p_{kl}\rangle
=\langle u_i,u_k\rangle\langle u_j,u_l\rangle
-\langle u_i,u_l\rangle\langle u_j,u_k\rangle.
\]

Die gesamte euklidische Paarantwort erhält man durch Ersetzen jeder Kontraktion durch

\[
\langle u_i,e^{-\tau h}u_k\rangle.
\]

Diese Determinante erzwingt Antisymmetrie und Pauli-Ausschluss. Eine als Mediator bezeichnete Linearkombination genau dieser Paarprodukte fügt keinen unabhängigen Zustand hinzu. Für J:e_α↦p_α und M=JB gilt identisch

\[
S=(J,M)=J(I,B),\qquad
G_S=\begin{pmatrix}G_J&G_JB\\B^\dagger G_J&B^\dagger G_JB\end{pmatrix}.
\]

Damit ist rank(G_S)=rank(G_J). Dasselbe Faktorisierungsgesetz gilt für die vollständige Zeitantwort. Es darf kein künstlicher zweiter Kanal durch doppelte Benennung eines Paarzustands entstehen.

Ein anderer, aus der Quelle definierter Keilvektor kann durchaus einen unabhängigen Zustand liefern. Auch dann ist er zunächst ein zusammengesetzter CAR-Operator; daraus folgt keine unabhängige kanonische Bosonenalgebra. Diese Unterscheidung ist ein algebraischer Vergleichstest, kein Ausschluss aller möglichen geladenen Erweiterungen.

## 6. Wo die Rückverbindung tatsächlich steht

| Datum | Tatsächliche mikroskopische Quelle | Bezeichneter zusätzlicher Randkandidat |
|---|---|---|
| Feldraum | Eine chiral-komplexe CAR-Feldspezies im oberen Randgrenzwert | 64 bezeichnete ungerade Felder und 60 Mediatorfelder aus einer zusätzlichen Gitterkonstruktion |
| Ladung | Ganzzahlige CAR-Zahl Q; Viertelholonomie im Generator | Markierte Mehrkomponentenladungen und zusätzliche Gitter-/Glue-Daten |
| Produkte | Vorgegebene CAR, Slaterdeterminanten und Komposite | Gittervertexprodukte/Kokzyklus und der dort bewiesene W-Kanal |
| Zustand | Tatsächliche gefüllte negative See | Ausgewähltes Gittervakuum und positive Randphase |
| Zeit | Nh_N/(2π), Grenzwert L0−Q/4 | Die in jenem Kandidaten festgelegte Konformalzeit und Energieform |
| Vergleichsabbildung | Keine aus P1 hergeleitete lokale ladungs-, produkt- und zeitverträgliche Abbildung zu den 64/60 Feldern vorhanden | Die Konstruktion setzt diese ursprüngliche Herkunft nicht selbst fest |

Die Aussage „eine Spezies“ ist kein Dimensionsargument gegen sämtliche Komposite: Ein räumliches Feld hat unendlich viele Moden und Produkte. Sie verhindert aber, zusätzliche unabhängige interne Kanäle ohne Herleitung als bereits vorhandene Quellfelder auszugeben.

Der Kandidatentest 3,4,5 ist deshalb **noch nicht ausführbar als behauptete Identifikation**: Es fehlen die quellseitig bestimmten Operatoren, die gerade dessen gemeinsame Paar-/Mediatorzustände darstellen sollen. Bloß ähnliche Energien an anderer Stelle des QWZ-Spektrums zu finden würde weder Ladungen noch Produkte noch den gemeinsamen Gramoperator vergleichen.

## 7. Die präzise offene Herkunftsaussage

Der Originalledger lässt `QGEO.KERNEL.01` offen: Der rohe Naht-Calderónoperator muss als Operator mit der vorgesehenen μ4-äquivarianten Einteilchenstruktur identifiziert werden. Hauptsymbol, ein endlicher Transferblock und übereinstimmende Spektrallisten liefern diesen Satz nicht bereits. Auch der geladene Netzanschluss bleibt in `SEAM.EQUIV.01` beziehungsweise `SEAM.MMST.TYPEIII.CHARGED.01` offen.

P1 ist dabei mehr als die Zahl c3: Es nennt Naht, Orientierung, Reflexionspositivität und Windung. Die geprüften Quellen definieren jedoch noch kein vollständiges geladenes Wortfunktional samt seiner Zeittranslationswirkung aus diesen Daten. Der Compiler, E8, die verzahnten Clocks und die vorhandenen positiven Rekonstruktionen werden dadurch nicht verworfen; gerade ihre physische gemeinsame Realisierung ist der zu beweisende Pfeil.

Ein abstrakter Rekonstruktionssatz kann aus einem vollständigen positiven Funktional Hilbertraum, Zustand und geeignete Operatoren zurückgewinnen. Er berechnet nicht die noch unbekannten Werte dieses Funktionals. Im CAR-Sonderfall kann ein festgelegter reiner Projektor den Slaterzustand bereits eindeutig bestimmen; fehlend bleiben dann die aus P1 hergeleitete CAR-Algebra und die tatsächliche geladene Zeitwirkung.

Der nächste belastbare Herkunftsnachweis muss daher die folgende Gleichheit mit unabhängig definierten linken Daten liefern:

\[
\omega_\Sigma\!\left(O_1(t_1)\cdots O_n(t_n)\right)
=\omega_{\rm micro}\!\left(\iota(O_1)(t_1)\cdots\iota(O_n)(t_n)\right),
\]

für eine aus den Ursprungsdaten konstruierte lokale, graduierte, ladungs- und adjungierungsverträgliche Abbildung iota, zunächst auf einer erzeugenden dichten Algebra und mit kontrolliertem Zeitgrenzwert. Die rechte Seite ist im hier untersuchten Modell jetzt ausdrücklich berechenbar. Die linke Seite und iota dürfen nicht durch diese rechte Seite definiert werden, wenn eine Herkunftsherleitung behauptet wird.

**Die vollständige Lösung ist damit nicht erreicht.** Erreicht ist eine konkrete Quellenantwort und eine präzise Lokalisierung dessen, was einer behaupteten Rückverbindung noch fehlt. Eine allgemeine Unmöglichkeit der TFPT oder der Herleitung aus stärkeren gemeinsamen Ursprungsprinzipien wird nicht behauptet.

## 8. Originale und Einordnung

- `microscopic-charged-car-limit/README.md`: vorhandener analytischer Einquellen-CAR- und Mehrzeitgrenzsatz, 9. September.
- `microscopic-energy-linearization/README.md`: ursprünglicher Quell-Hamiltonoperator, Projektion und Energievergleich; Hilfslinearisation ausdrücklich getrennt.
- `charged-source-time-audit-20260920/README.md`: frühere Unterscheidung neutraler und geladener Viertelholonomieantwort.
- `source-joint-response-20260921/SOURCE_AUDIT.md`: bedingte 2076-dimensionale Antwort des bezeichneten zusätzlichen Randkandidaten und ihre Herkunftsgrenze.
- `tfpt_1_architecture_e8.tex`, P1/P2-Definition sowie Abschnitt zur freien Majorana-Realisierung.
- `tfpt_research_contracts.tex`, Abschnitte zu QGEO.KERNEL, voller Schwingerstruktur und drei Dynamikbegriffen.
- `verification/status_ledger.csv`: maßgebliche offene Claims, nicht durch diesen Contract hochgestuft.

Die getrennten Anlagen enthalten den Quellenaudit, die ausdrückliche Korrelatorenrechnung und die Reproduktionsdaten. Die analytischen Aussagen werden nicht aus endlich vielen numerischen Kontrollen abgeleitet. Keine Papers, Ledger-Claims, empirischen Evidenzzeilen oder T1–T8-Gates werden promoviert.

## 9. Gezielte Reproduktion dieser Runde

Die 19 bestehenden Tests der unmittelbaren geladenen Quellklasse wurden mit Exit 0 reproduziert; das Protokoll liegt in `targeted_regression.log`. Der neue symbolische Begleitcheck lief normal und optimiert mit identischen Ergebnisdateien. Er prüft endliche CAR- und Mehrzeitidentitäten; er ersetzt nicht den ursprünglichen analytischen Grenzwertsatz. `validation.json` hält die Reichweite fest. Der Quellenvergleich erhält ausdrücklich den Status PARTIAL.
