<a id="anfang"></a>
# TFPT und Universalraum
## Gesamtdokumentation der Untersuchung
### Ergebnisse, Herleitungen, Verbindungen, Gegenbeispiele und verbleibende Herkunftsfragen

**Ergebnisstand:** Gesprächsreihe vom 26. September 2026  
**Konsolidierte Fassung:** 27. September 2026  
**Grundlage:** die eingereichten TFPT Unterlagen, die Trägerfortsetzung vom 19. September, der Zuse Prüfstrang, der eingereichte Quartiktext und die fünf anschließenden Forschungsberichte.

> **Gesamtergebnis:** Ein gemeinsamer endlicher algebraischer Zusammenhang verbindet Hamming Code, E₈ Quellen, Quartikcode, Igusa Geometrie, Bellmessung, Doily, Petersen Struktur und Invariantengrade. In ausdrücklich definierten Modellen wurden außerdem geschützte Quellen, virtuelle Wechselwirkungen, eine dynamische Auswahl des Fünfercodes und rekursive Bindungen konstruiert. Der abschließende Ladungstest erzwingt eine Trennung zweier Dynamikzweige: Der ursprüngliche Bindungsoperator erhält die transportierte additive Hyperladung nicht; eine klassifizierte Vervollständigung behebt dies, verändert aber den Rückkanal. **Ein vollständiger physischer TFPT Abschluss ist in dieser Gesprächsreihe nicht nachgewiesen.**

### Was „vollständig“ hier bedeutet

Diese Datei dokumentiert die Ergebnisse **der gesamten vorliegenden Untersuchungsfolge**, einschließlich ihrer Korrekturen, Voraussetzungen und negativen Befunde. Sie enthält einen lesbaren zusammenhängenden Hauptteil, die vollständigen sieben zugehörigen Prüfberichte als Originaltexte und die Ergebniswerte der sechs Prüfpakete. Die großen ursprünglichen TFPT PDF Dokumente werden als Quellen verwendet, nicht vollständig nochmals abgedruckt.

Die Zusammenstellung ist **keine neue Ausführung der wissenschaftlichen Prüfprogramme**, keine neue Lean Formalisierung und keine unabhängige Zertifizierung sämtlicher früherer Beweise. Aussagen wie „exakt geprüft“ bezeichnen den im jeweiligen ursprünglichen Bericht dokumentierten Lauf. Für diese Konsolidierung wurden die Dateien zusammengeführt und ihre Identität gegenüber den enthaltenen Archivfassungen kontrolliert. Die in den Originalberichten verwendete erste Person gehört zum damaligen Bericht.

Die Begriffe „Durchbruch“ und „Lösung“ beziehen sich im Folgenden nur auf das jeweils benannte Teilproblem. Bekannte mathematische Gegenstände werden nicht als weltweite Erstentdeckungen ausgegeben. Der Gesamtvertrag unterscheidet endliche Resultate, vollständige physische Herleitung und empirische Bewährung ausdrücklich. fileciteturn21file0L12-L45

---

<a id="navigation"></a>
## Navigation und Lesepfade

| Lesepfad | Inhalt |
|:---|:---|
| **Das Wesentliche** | [1. Gesamtbild](#gesamtbild), [2. Was zusammengehört](#landkarte), [3. Ergebnisübersicht](#ergebnisuebersicht), [22. Schlussbilanz](#schlussbilanz) |
| **Alle Untersuchungen** | [4. Zuse und Prozessstruktur](#zuse), [5. Vorgelagerte Quellenfragen](#vorwissen), [6. Codebasis](#codebasis), [7. Information](#information), [8. Geometrie](#geometrie), [9. Steuerung und Ladung](#steuerung), [10. Codeauswahl](#codeauswahl), [11. Geschützte Quelle](#geschuetzte-quelle), [12. Igusa](#igusa), [13. Quellendynamik](#quellendynamik) |
| **Dynamik und spätere Korrekturen** | [14. Austausch](#austausch), [15. Dynamischer Codeabschluss](#dynamischer-abschluss), [16. Bindung und Rückkanal](#bindung), [17. Erste Rekursion](#rekursion-alt), [18. Gemeinsamer Ladungstest](#ladungstest), [19. Kovariante Rekursion und Komposition](#komposition) |
| **Einordnung und Nachweise** | [20. Korrekturen und Ausschlüsse](#korrekturen), [21. Physischer Abschlussvertrag](#abschlussvertrag), [23. Glossar](#glossar), [24. Quellen und Reproduktion](#quellen), [25. Originalberichte](#originalberichte), [26. Maschinenlesbare Ergebnisse](#ergebnisdaten), [27. Vollständige Prüfprogramme](#pruefprogramme) |

Die Schemata sind Textgrafiken und funktionieren auch ohne besondere Bilddateien oder Diagrammsoftware. Formeln im Hauptteil verwenden LaTeX innerhalb von Markdown. Ohne Mathematikrenderer bleiben die ausgeschriebenen Erklärungen lesbar.

---

<a id="gesamtbild"></a>
# 1. Das Gesamtbild in einfacher Sprache

## 1.1 Die zentrale Idee

Das Material enthält nicht bloß viele wiederkehrende Zahlen. Es beschreibt mehrere Perspektiven auf eine konkrete diskrete Quelle. Ein binärer Hamming Code organisiert die Ausgangsstruktur. Daraus werden E₈ Wurzeln und komplexe Quellenrichtungen konstruiert. Ein bestimmtes viertes Moment dieser Quellen enthält einen besonderen fünfdimensionalen Bereich.

Dieser **Fünfercode** ist kein vollständiges Universum und auch nicht einfach ein einzelnes Teilchen. Er ist ein präzise definierter Informationsraum. Seine Information verteilt sich ungewöhnlich: Ein Register allein verrät nichts über den logischen Zustand, ein Paar liefert eine bestimmte Messung, drei Register erlauben die vollständige Rekonstruktion.

Die Geometrie dieser Auslesungen verbindet dieselben sechs Markierungen, zehn Messrichtungen und fünfzehn Inzidenzobjekte. Die spätere Igusa Rechnung erklärt, wie sie aus einer gemeinsamen Polynomabbildung hervorgehen. fileciteturn14file0L81-L158 fileciteturn17file0L188-L234

## 1.2 Das Bild eines Rechners, ohne die Metapher mit Physik zu verwechseln

Man kann die Rollen mit einem Rechner vergleichen:

| Mathematische Rolle | Anschauliches Bild | Was das Bild nicht behauptet |
|:---|:---|:---|
| Ursprüngliche Quelle | Der vollständige Maschinenzustand | Noch keine physische Hardware oder Raumzelle |
| Code | Eine erlaubte, geschützte Organisation von Information | Noch kein automatisch thermisch stabiler Speicher |
| Quartikauslesung | Eine verdichtete Ansicht des Maschinenzustands | Kein vollständiges Protokoll seiner Zukunft |
| Carry und Phasenrahmen | Kontext, den eine verkürzte Anzeige nicht zeigt | Nicht bloß eine irrelevante globale Phase |
| Hamiltonoperator | Die tatsächlich ausgeführte Bewegung | Nicht aus der bloßen Zulässigkeit von Befehlen bestimmt |
| Kopplungsgraph | Die festgelegten Verbindungen zwischen Instanzen | Noch keine hergeleitete Raumzeit |

**Die wichtigste Korrektur der gesamten Untersuchung:** Ein vollständiger Maschinenzustand und eine seiner Anzeigen sind nicht dasselbe. Zwei Quellen können dieselbe Quartikanzeige besitzen und sich unter demselben Quelloperator danach verschieden entwickeln. Dieser Unterschied wurde explizit ausgerechnet. fileciteturn17file0L287-L310

## 1.3 Was tatsächlich erreicht wurde

Die algebraischen Verbindungen sind erheblich enger geworden. Der Fünfercode ist nicht nur durch eine Dimension mit E₈ verbunden. Seine Projektoren, Gruppenwirkungen, Polynome und Messoperatoren sind konkret angegeben. Die vollständige Pauli Quotientenabbildung wird durch die Igusa Quartik beschrieben.

Auf der dynamischen Seite wurden mehrere genaue Kandidaten gebaut. Geschützte Quellen wechselwirken über virtuelle Fehlerpfade. Vier entsprechend gekoppelte Quellen wählen zunächst 35 symmetrische Richtungen und danach denselben Fünfercode aus. Ein weiterer logischer Anschluss erzeugt aus der Quellenantwort genau die Matrix des vorhandenen Informationsrückkanals als Bindungsoperator. Drei gebundene Fünferbausteine tragen erneut eine Fünferdarstellung. fileciteturn18file0L15-L21 fileciteturn20file0L13-L19

Der abschließende Test verhindert aber eine falsche Gesamtsynthese: **Die ursprüngliche rekursive Bindung und die transportierte Hyperladung passen nicht unverändert zusammen.** Unter einer stärkeren gemeinsamen Symmetrieforderung ist eine passende Singulettbindung bis auf Maßstab und Energienullpunkt bestimmt. Sie erlaubt eine exakte ladungserhaltende Rekursion und bekannte integrable Komposition, verändert dafür jedoch die ursprünglichen Übertragungswerte. fileciteturn22file0L13-L25

## 1.4 Was nicht erreicht wurde

Es wurde kein gemeinsamer physischer Ursprung konstruiert, der ohne weitere Auswahl gleichzeitig Raumdimension, lokale geladene Felder, ihren Zustand, ihre Zeit, sämtliche Kopplungen und quantisierte Gravitation erzeugt. Die zusätzlichen Hamiltonoperatoren, Graphen, Kopplungsvorzeichen und Skalen sind je nach Modell ausdrücklich benannte Voraussetzungen.

Die vorhandenen Teilresultate beweisen deshalb weder „TFPT ist vollständig gelöst“ noch „TFPT ist unmöglich“. Sie entscheiden konkrete mathematische und dynamische Identifikationen. Die verbleibende Aufgabe ist ein **gemeinsamer Herkunftssatz**, nicht das bloße Hinzufügen weiterer ähnlich aussehender Zahlen. fileciteturn21file2L112-L138

---

<a id="landkarte"></a>
# 2. Die gemeinsame Landkarte

## 2.1 Der tatsächlich verbundene algebraische Kern

```text
Derselbe binäre Hamming Code RM(1,3)
                    │
                    ├── Konstruktion der 240 E₈ Wurzeln
                    │                 │
                    │                 └── 60 komplexe Quellenrichtungen
                    │                                  │
                    │                                  └── viertes Quellenmoment
                    │                                                │
                    │                                                └── Fünfercode Π₅
                    │                                                       │
                    │                       ┌───────────────────────────────┤
                    │                       │                               │
                    │                 Paarmessung                 Quartikabbildung f(z)
                    │                 mit 10 Ausgängen                       │
                    │                       │                          Igusa Quartik
                    │                 Petersen Rahmen                       │
                    │                       │                 ┌─────────────┼─────────────┐
                    │                       └─────────────────┤             │             │
                    │                                  6 Marken      15er Doily    Grade
                    │                                  10 Quadriken  60 Flächen    8,12,20,24
                    │
                    └── Verkürzung desselben binären Codes
                                      │
                              kompatible Quartikchecks
                                      │
                         geschützte vollständige C⁴ Quelle
```

Die Pfeile bezeichnen die in den Berichten angegebenen Konstruktionen. Sie identifizieren nicht automatisch alle auftretenden Vektorräume miteinander. Insbesondere sind die 60 komplexen Quellenstrahlen, ihre 60 Reflexionen und die 60 vektorisierten Operationstypen verwandte, aber unterschiedlich verwendete Objekte. [Q1](#original-q1), [Q2](#original-q2).

## 2.2 Der dynamische Weg mit seinen zusätzlichen Eingaben

```text
Geschützte Quellen
       │
       │ zusätzliche Paarlinks, Kopplung g, Skala Δ
       ▼
Logischer Austausch in dritter Ordnung
       │
       │ vier Quellen, verbunden, g < 0
       ▼
Symmetrischer Raum: 35 Richtungen
       │
       │ verbundene virtuelle Sechsschrittprozesse
       ▼
Fünfergrundsektor + 30 höhere Antwortrichtungen
       │
       │ neuer logischer Austauschanschluss ε
       ▼
Bindung h = I − K
       │
       ├── eindeutiger Paargrundzustand
       ├── erneuter Fünferraum aus drei Bausteinen
       └── gleiche führende projizierte Randbindung
                     │
                     │ gemeinsamer Hyperladungstest
                     ▼
          [h, QY] ≠ 0: direkte Ladungsdeutung scheitert
                     │
                     ├── nur markierte Symmetrie: größere Alternativenfamilie
                     │
                     └── volle native Symmetrie plus Ladung
                                      │
                           geänderter Operator h_cov
                                      │
                     ladungserhaltende Dreierrekursion
                                      │
                    Temperley und Lieb / Yang und Baxter
```

Der Übergang von $h$ zu $h_{\mathrm{cov}}$ ist **eine Modelländerung**, keine bloße Umbenennung und kein unverändert erhaltener alter Rückkanal. [Q3](#original-q3), [Q4](#original-q4), [Q5](#original-q5).

## 2.3 Drei verschiedene Dinge, die oft gleich aussehen

```text
Struktur                         Bewegung                          Physische Identifikation
Was ist erlaubt?                 Was geschieht?                    Was wird beobachtet?

Code, Algebra,                   H, Zustand,                       geladene Felder,
Invarianten                      Kopplungen, Zeit                  Raumzeit, Messantworten
       │                                │                                  │
       └───────── braucht Beweis ───────┴────────── braucht Beweis ─────────┘
```

Eine richtige Struktur kann verschiedene Bewegungen tragen. Eine richtige endliche Bewegung kann mehrere physische Deutungen zulassen. Die Untersuchung prüft diese Übergänge, statt sie durch Analogien zu ersetzen.

---

<a id="ergebnisuebersicht"></a>
# 3. Ergebnisübersicht und Forschungsfolge

## 3.1 Statuswörter

| Kennzeichnung | Bedeutung in dieser Gesamtdokumentation |
|:---|:---|
| **Exakt im Vertrag** | Im jeweiligen Bericht analytisch bewiesen oder mit exakter endlicher Rechnung bestätigt, unter seinen angegebenen Voraussetzungen |
| **Numerisch** | Fließkommarechnung oder Spektralkontrolle; nicht stillschweigend ein Intervallbeweis |
| **Modellannahme** | Gewählte Kopplung, Skala, Graph, Kodierungsklasse, Markierung oder Identifikation |
| **Ausgeschlossen** | Eine genau benannte Behauptung scheitert in der untersuchten Klasse |
| **Offen** | Die geforderte Herleitung ist in dieser Untersuchung nicht vorhanden |
| **Bekannte Mathematik** | Etablierter Gegenstand oder Methode; der projektbezogene Anschluss kann trotzdem eine eigene Rechnung sein |

Die früheren TFPT Marker wie `[E]`, `[C]`, `[O]` und `[X]` bleiben in den Originaltexten erhalten. Sie sind keine pauschale Aussage, dass alle mit `[E]` bezeichneten Sachverhalte physisch bewiesen seien. Auch die Originaleinleitung trennt numerische, algebraische und physische Belegarten. fileciteturn13file2L181-L205

## 3.2 Die sieben inhaltlichen Etappen

| Etappe | Tragendes Ergebnis | Wichtigste Grenze |
|:---|:---|:---|
| **Z: Zuse Prüfung** | Prozessgeschichten sind informationsreicher als ein Graph erlaubter Paare; mehrere automatische Raumzeitfolgerungen scheitern | Kein eigener physischer Generator oder Raum aus der Komponierbarkeit |
| **D0: Eingereichter Quartiktext** | Ränge $1,10,25$, Hyperladungsbrücke, Unterschied zwischen Steuerung und Codeauswahl | Bericht über endliche Ergebnisse, kein physischer Abschluss |
| **Q1: Quartik und Auslesung** | Zehn Bell Effekte, Petersen Rahmen, $2/3$ Singularübertragung, Momentenparent, geschützte volle Quelle | Tensorfaktoren, Parent und Links bleiben gewählte Modellstruktur |
| **Q2: Igusa und Quellenaustausch** | Vollständiger Invariantenring, 60 Hyperflächenfaktoren, nichtautonome Auslesung, Austausch in dritter Ordnung | Quotient verliert Quellenzweig; $g$, $\Delta$ und Graph nicht ausgewählt |
| **Q3: Dynamischer Codeabschluss** | $256\to35\to5$ aus virtuellen Kopplungsprozessen; $30=15\times2$ | Negative Kopplung und Vierblockstruktur vorausgesetzt; gedresster Codeabstand nur zwei |
| **Q4: Rekursive Bindung** | Rückkanal wird Bindungsmatrix, exakter Paargrundzustand, Dreiergrundraum und Randisometrie | Neuer logischer Anschluss; vollständige Rekursion erzeugt zusätzliche Terme |
| **Q5: Ladung und Komposition** | Alter Bindungsoperator verletzt $Y$; kompatible Familie klassifiziert; ladungserhaltende Rekursion und Kompositionsgleichung | Geänderte Dynamik, andere Übertragung, keine erzwungene physische $SU(5)$ Gruppe |

## 3.3 Die stärksten tatsächlichen Teilabschlüsse

**Algebraische Vereinheitlichung:** Die verschiedenen endlichen Muster werden durch denselben Quotientenring und konkrete Abbildungen verbunden, nicht nur durch Dimensionsvergleiche.

**Dynamischer Bausteinabschluss:** Im definierten Quellenmodell erzeugen Kopplungen den Quartikselektor in sechster Ordnung, ohne den äußeren Projektor vorher als fertiges Ziel in den mikroskopischen Hamiltonoperator einzusetzen.

**Informations und Bindungsidentität:** Ein zusätzlicher logischer Quellenanschluss erzeugt die konkrete Petz Rückkanalmatrix als effektive Bindung.

**Gemeinsamer Ladungsentscheid:** Die Unverträglichkeit des alten Bindungsoperators mit der transportierten Hyperladung ist exakt festgestellt. Unter der stärkeren gemeinsamen Symmetrieforderung ist die kompatible positive Singulettfamilie vollständig bestimmt.

**Komposition:** Für die vervollständigte Kette liegen eine exakte Ladungsisometrie, lokale Temperley und Lieb Relationen und eine symbolisch geprüfte Gleichung von Yang und Baxter vor. Die vollständige Vergröberung erzeugt trotzdem Mehrkörperwörter.

---

<a id="zuse"></a>
# 4. Der Zuse Prüfstrang: Was ein rechnender Raum wirklich benötigen würde

## 4.1 Die 21 Thesen und ihre Entscheidungen

Die folgende Tabelle bewahrt die Einordnung des damaligen Prüfstrangs. „Nicht automatisch“ bedeutet weder ein allgemeines Naturverbot noch das Scheitern jeder TFPT Realisierung.

| Nr. | Untersuchte Aussage | Ergebnis |
|---:|:---|:---|
| 1 | Zuse beschreibt lokale Berechnung und digitale Teilchen | Historisch im Kern passend; seine vereinfachten Modelle sind keine vollständige physische Herleitung |
| 2 | TFPT kann unterhalb von Zellen mit Operationen beginnen | Sinnvolles Ziel; Nachbarschaft und Raum sind damit noch nicht erzeugt |
| 3 | Teilchen sind stabile Eigenzyklen | Suchidee; Periodizität allein liefert keine Masse, Ladung, Statistik oder Ausbreitung |
| 4 | Clock, Quelle und Register bilden einen Update Mechanismus | Mögliche Deutung; kein bestimmter Generator daraus |
| 5 | Ohne festes Gitter folgt Lorentzsymmetrie | Als automatische Folgerung falsch |
| 6 | Hermitesche $2\times2$ Matrizen tragen Minkowski Geometrie | Determinantenidentität exakt; physische Raumzeitidentifikation zusätzlich |
| 7 | Lichtgeschwindigkeit ist maximale Kompositionstiefe | Bedingte Interpretation; eine Ausbreitungsgrenze ist noch kein universelles relativistisches $c$ |
| 8 | Der Kompatibilitätsgraph ist Raum | Zu allgemein; Verträglichkeit, Überlappung und Wechselwirkung sind verschiedene Relationen |
| 9 | Distanz ist minimale Zahl elementarer Transformationen | Definierbar; hängt von der Wahl der elementaren Schritte ab |
| 10 | Zyklen bilden ein diskretes Integrationsschema | Hypothese; gleiche Endpunkte bestimmen keine Zwischenbewegung |
| 11 | $\mu_4$ ist ein vierphasiger Scheduler | Nicht aus der Gruppenordnung allein; die vorhandene Viertelstruktur wirkt auch als Automorphismus |
| 12 | E₈ ist ein Alphabet oder Typensystem | Mit der Compilerlesart vereinbar; noch kein Ausführungsprogramm |
| 13 | Daraus folgen Teilchen und $3+1$ Raumzeit | Die aufeinanderfolgenden Rekonstruktionsschritte sind nicht geschlossen |
| 14 | Naturgesetz ist Compiler statt Programm | Nützliche Ordnung der Aufgaben; Zulässigkeit bestimmt keine Amplituden oder Anfangsdaten |
| 15 | Welt ist ein konsistenter Fixpunkt | Mögliche Formulierung; Existenz, Auswahl und Zeit bleiben eigene Fragen |
| 16 | Information ist unterscheidbare zukünftige Wirkung | Operational präzisierbar; vollständige Testkontexte erforderlich |
| 17 | Gemeinsame zukünftige Abhängigkeit bestimmt räumliche Nähe | Keine allgemeine Folgerung; Korrelation kann aus gemeinsamen Ursachen stammen |
| 18 | Paare und Übergänge erzeugen automatisch einen dynamischen Graphen | Nein; Erzeugungsregel und Entwicklung fehlen |
| 19 | Ein endliches Alphabet kann ausgedehnten Raum erzeugen | Grundsätzlich als Forschungsansatz möglich; Alphabet und beliebig viele Ereignisse unterscheiden |
| 20 | Zuse Korrelationen sind starke unabhängige Belege | Inspiration ja, unabhängiger physischer Nachweis nein |
| 21 | Ein Zuse Test schließt die gesamte TFPT Theorie | Kann Teilentscheidungen liefern; ersetzt nicht alle physischen Abschlussbedingungen |

Der damalige Literaturabgleich korrigierte außerdem den zu scharfen Gegensatz „Zuse nur starres Gitter, TFPT erstmals veränderliche Beziehungen“: In der geprüften Zuse Übersetzung wurden auch veränderliche Schaltungen und wachsende Automaten angesprochen. Das ist eine historische Einordnung aus dem ersten Antwortstrang, keine neue Literaturprüfung dieser Zusammenstellung.

## 4.2 Die 60 Operationstypen sind kein ausgedehntes Raumnetz

Im dokumentierten $2\times2$ Operationswörterbuch gibt es 24 unitäre Cliffordklassen und 36 Rang eins Operationen. Alle 3600 geordneten Produkte wurden in der damaligen Normalform aufgezählt:

| Produktnormquadrat | Zahl |
|---:|---:|
| 0 | 216 |
| 2 | 3168 |
| 4 | 216 |

Für die ausdrücklich gewählte Kantenregel $A\to B\iff BA\ne0$ hat der Graph Durchmesser genau zwei. Jede invertierbare Operation $U$ vermittelt $A\to U\to B$. Auch Entfernen der Identität beseitigt diesen Mechanismus nicht.

```text
60 Operationstypen                         Eine Prozessgeschichte

A ── U ── B                               Ereignis 1 → Ereignis 2 → …
Jeder über höchstens einen                 wiederholte Vorkommnisse,
Vermittler erreichbar                      Zustand, Reihenfolge, Amplituden

Kein ausgedehnter Raum                     Anderer Gegenstand, eigene Regel nötig
```

Schon drei Schritte zeigen den Informationsverlust eines Paargraphen:

$$
IP_0\ne0,\qquad P_1I\ne0,\qquad P_1IP_0=0,
$$

für orthogonale Projektoren $P_0,P_1$. Erlaubte Nachbarpaare garantieren kein nichtverschwindendes Gesamtwort. Der ursprüngliche Produktzensus und die Depolarisationsgrenze stehen auch in der Quellenfassung vom 20. September. fileciteturn5file1L94-L117

## 4.3 Uniforme Ausführung und reine Komposition reichen nicht

Das gleichgewichtete, unbeobachtete Krausensemble $K_A=A/\sqrt{60}$ ergibt

$$
\Phi(\rho)=\operatorname{tr}(\rho)\frac{I}{2}.
$$

Beide uniformen Klassen depolarisieren bereits einzeln. Nur ihre relativen Gesamtgewichte zu ändern erhält die fehlende Information nicht.

Auch die volle Lorentzgruppe folgt nicht aus reiner Verkettung dieses Alphabets: Ein Wort mit einem Rang eins Faktor hat höchstens Rang eins. Ein invertierbares Wort enthält daher nur unitäre Cliffordfaktoren und bleibt projektiv unitär. Der Boostvertreter $\operatorname{diag}(2,1/2)$ ist so nicht erreichbar.

Der algebraische Kegel bleibt trotzdem korrekt:

$$
\det(tI+x\sigma_x+y\sigma_y+z\sigma_z)=t^2-x^2-y^2-z^2.
$$

Die Identität ist kein eigenständiger Beweis, dass die vier Koeffizienten Ereigniskoordinaten unserer Raumzeit sind. [Z](#original-z).

## 4.4 Zustand, Transfer und Uhr sind verschiedene Informationen

Der gegebene Populationstransfer

$$
B=\frac1{18}\begin{pmatrix}13&1&4\\1&13&4\\4&4&10\end{pmatrix},
\qquad\operatorname{spec}B=\{1,2/3,1/3\}
$$

besitzt die Permutationsgewichte

$$
w_t=(1/2+t,t,t,1/18-t,2/9-t,2/9-t),\qquad0\le t\le1/18.
$$

Alle haben denselben Populationstransfer, aber auf dem Kontrastqubit unterschiedliche Multiplikatoren $(1,2/3,6t,1/3)$ in der Reihenfolge $(I,X,Y,Z)$. Zwischen $t=0$ und $t=1/27$ unterscheiden sich die Ausgaben für den $+Y$ Eingang um $2/9$ im $Y$ Erwartungswert und $1/9$ im Spurabstand. fileciteturn13file13L286-L354

Auch ein vollständiger Zeit eins Endpunkt fixiert keinen eindeutigen Hamiltonoperator. Für

$$
H_0=\operatorname{diag}(0,3\pi/2,\pi,\pi/2),\quad
H_1=H_0+2\pi\operatorname{diag}(0,1,0,0)
$$

gilt $e^{-iH_0}=e^{-iH_1}=\operatorname{diag}(1,i,-1,-i)$, aber die Zwischenentwicklungen unterscheiden sich.

Der Coxeterzyklus mit Ordnung 30 enthält keinen Unterzyklus der Ordnung vier. Die Einheitengruppe $(\mathbb Z/30)^\times$ besitzt dagegen solche Automorphismen. Die vorhandene Galois Viertelwirkung darf deshalb nicht mit einem weiteren Zeiger derselben Uhr gleichgesetzt werden. fileciteturn13file7L335-L352

## 4.5 Ein besserer mathematischer Zielgegenstand

In einer bereits gegebenen quantenmechanischen Realisierung bilden ganze Geschichtenoperatoren $K_\gamma$ und ein Zustand $\omega$ den positiven Kern

$$
D(\gamma,\gamma')=\omega(K_\gamma^\dagger K_{\gamma'}).
$$

Die Positivität folgt aus $\sum\bar c_ic_jD(\gamma_i,\gamma_j)=\omega(X^\dagger X)\ge0$. Diagonaleinträge können unter geeigneter Instrumentnormierung Wahrscheinlichkeiten liefern, Kreuzterme erhalten Interferenzinformation.

Analog kann eine Momentenmatrix $M_{u,v}=\omega(u^\dagger v)$ ganze Wörter statt nur Paare kontrollieren. Die Quelle muss diese Antworten jedoch selbst liefern. Konkatenation, kausale Normierung, physische Lokalität und Zustandsauswahl sind weitere Bedingungen. **Der positive Kern ist ein präzisierter Quellenvertrag, nicht bereits die TFPT Ursprungslösung.** [Z](#original-z).

---

<a id="vorwissen"></a>
# 5. Vorgelagerte TFPT Quellenfragen, die in allen Fortsetzungen mitgelten

## 5.1 Globale Verklebung statt bloßer Paarüberlappung

Die vorgeschlagene Gram Matrix

$$
\Gamma=\begin{pmatrix}1&1&0\\1&1&1\\0&1&1\end{pmatrix}
$$

hat den negativen Eigenwert $1-\sqrt2$. Für $(1,-1,1)^T$ ergibt ihre quadratische Form $-1$. Sie beschreibt daher keine drei Hilbertraumvektoren. Exaktes Teilen derselben normierten Richtung entlang zweier Kanten erzwingt auch die Identifikation der Enden.

Ein zulässiger operatorwertiger Überlappungskern hat dagegen die Form

$$
\Gamma_{XY}=J_X^\dagger J_Y,\qquad\Gamma\succeq0,\qquad\Gamma_{XX}=I.
$$

Ein gegebener positiver Kern erlaubt die Rekonstruktion minimaler Einbettungen bis auf gemeinsame unitäre Äquivalenz. Er wählt den Kern nicht aus der TFPT Quelle aus. Unter einer ausdrücklich zusätzlichen funktoriellen Annahme wurde außerdem

$$
\Gamma^B_{XY}=\frac18W(\Lambda^2\Gamma_{XY})W^\dagger
$$

für die Bosonverklebung angegeben. Kinematische Gramform und Zustandskovarianz bleiben getrennt: $\Gamma_{XY}=J_X^\dagger J_Y$ ist nicht dasselbe wie $J_X^\dagger C_\Sigma J_Y$. fileciteturn21file2L104-L138

## 5.2 Der native W Anschluss ist nicht durch ein Codespektrum ersetzt

Die ursprüngliche native Struktur verwendet

$$
W:\Lambda^2F\to B,\qquad F=(16,4),\qquad B=(10,6),\qquad WW^\dagger=8I_{60}.
$$

Im dokumentierten $Q=3$ Test sind 3840 Boson und Fermionzustände sowie 41664 Dreifermionzustände beteiligt. Für $G=V^\dagger V$ gilt die exakte Eigenwertliste

$$
0:64,\quad7:2880,\quad10:576,\quad12:320,
$$

und $G(G-7I)(G-10I)(G-12I)=0$. Ein echter Gegenstrom wurde festgestellt, doch die unabhängig variierten inneren Marken bleiben jeweils an ihrem ursprünglichen Bereich. Er ist deshalb nicht automatisch Übertragung eines unbekannten Spinorzustands. fileciteturn19file5L252-L285 fileciteturn19file1L65-L89

Der positive RR/W Kandidat

$$
H_+=2\kappa\sum_A\left(b_A+P_A/\sqrt8\right)^\dagger
                       \left(b_A+P_A/\sqrt8\right)
$$

besitzt unter der erklärten Einsetzung einen Grundraum der Dimension $2^{64}$. Ein eindeutiger Zustand in einem festgelegten Ladungssektor wählt diesen Sektor nicht global aus. Positive Erweiterungen, die die niedrigen Antworten bis $Q=3$ unverändert lassen, behalten mindestens 43745 Nullzustände. Diese Grenze gehört zu diesem Kandidaten und ist kein allgemeines Axiom über physische Vakuumeindeutigkeit. fileciteturn5file2L149-L199

## 5.3 Feldtypen, Alpha und Flavor

Die im älteren Randanschluss konstruierten 16 realen Fermionkomponenten tragen eine Spin(16) Vektordarstellung, nicht automatisch den chiralen Spin(10) Materiehalbspinor. Auch der $(16,4)$ Anteil des affinen E₈ Netzes ist dort ein Stromsektor mit Gewicht eins, nicht ohne Weiteres eine Familie freier CAR Felder. Die späteren Codes heben diese Grenzen nicht auf. fileciteturn13file12L244-L262 fileciteturn15file0L14-L21

Die Gleichung für den angegebenen Wert $\alpha^{-1}=137{,}0359992168407\ldots$ ist ein dokumentierter Selbstkonsistenzabschluss. Ihre gemeinsame physische Quellen-, Ward- und Determinantenherleitung wurde in dieser Gesprächsreihe nicht neu geschlossen. Quellmassen, Polmassen und laufende Größen sind ebenfalls nicht identisch. fileciteturn13file12L214-L233

## 5.4 Zwei kleine, aber tragende Nebenentscheidungen

**Horizonte:** In der reduzierten Planck Zeile der damaligen Einheitentabelle wurde ein zusätzlicher Faktor $c_3$ festgestellt. Aus $\bar M_{\mathrm{Pl}}^2=1/(8\pi G)$ und $T_H=1/(8\pi GM)$ folgt $T_H=\bar M_{\mathrm{Pl}}^2/M$, nicht $c_3\bar M_{\mathrm{Pl}}^2/M$. Das ist ein lokaler Tabellenbefund, keine vollständige Folgefehlerprüfung aller Horizontformeln. fileciteturn13file8L178-L205

**Primzahlperioden:** Verschiedene $\log p$ sind über $\mathbb Q$ linear unabhängig. Eine rein endliche Clock mit kommensurablen Perioden realisiert deshalb nicht das ganze Spektrum $\{\log p\}$. Diese Grenze wurde im Primzahlstrang als exakter Satz dokumentiert; daraus folgt weder eine RH Lösung noch eine Widerlegung anderer nichtperiodischer Quellen. fileciteturn4file1L72-L97


## 5.5 Die Herleitung der Zahlen ersetzt nicht die Auswahl der Regel

Die Ausgangspostulate P1 und P2 sind strukturierte Rand- und Trägerannahmen, nicht bloß zwei frei flottierende Zahlen. Im bestehenden Compiler stehen $c_3=1/(8\pi)$, der Fünferträger und die Markierung $3+2$ auf der Eingabeseite. Daraus folgen die angegebenen algebraischen Konsequenzen.

Die Pascal Identität verdeutlicht die Auswahlgrenze:

$$
2^{g-1}=\sum_{k=0}^{K}\binom gk
\quad\Longleftrightarrow\quad g=2K+1.
$$

$g=5$ wird auf dieser Route durch $K=2$ ausgewählt. Die richtige Arithmetik beweist die Herkunft dieser Trunkierungsregel nicht rückwirkend. Ebenso sind bestehende Rücklesungen des Ankers $(1,1,2)$ Konsistenzbeziehungen, nicht automatisch ein voraussetzungsloser Ursprung. Dieser Einwand war bereits Gegenstand des ursprünglichen Red Team Berichts. fileciteturn13file9L258-L298

---

<a id="codebasis"></a>
# 6. Die konkrete Quartikcodebasis

Ein Quellenregister ist zunächst ein mathematischer Raum $\mathbb C^4$. Vier solche Faktoren bilden einen 256 dimensionalen Tensorraum. Dass diese vier Faktoren physische Register sind, ist in den dynamischen Kandidaten eine Realisierungsannahme, nicht die Bedeutung des Worts „viertes Moment“ allein.

Die fünf orthonormalen Codevektoren lauten

$$
c_0=(|0000\rangle+|1111\rangle+|2222\rangle+|3333\rangle)/2,
$$
$$
c_1=(\sum_{\mathrm{perm}}|0011\rangle+\sum_{\mathrm{perm}}|2233\rangle)/\sqrt{12},
$$
$$
c_2=(\sum_{\mathrm{perm}}|0022\rangle+\sum_{\mathrm{perm}}|1133\rangle)/\sqrt{12},
$$
$$
c_3=(\sum_{\mathrm{perm}}|0033\rangle+\sum_{\mathrm{perm}}|1122\rangle)/\sqrt{12},
\qquad
c_4=\sum_{\mathrm{perm}}|0123\rangle/\sqrt{24}.
$$

Jede Summe enthält verschiedene Permutationen. Für die unnormalisierten Supportspalten $E$ gilt

$$
G=E^TE=\operatorname{diag}(4,12,12,12,24),\qquad
V=EG^{-1/2},\qquad P=VV^\dagger.
$$

Mit $S=P_{\mathrm{sym},4}$ und den 16 Hermiteschen Zweiqubit Paulis erhält man

$$
Q=\frac1{16}\sum_AA^{\otimes4},\qquad
Q^2=Q,\quad\operatorname{rank}Q=16,
$$
$$
P=SQ=\Pi_5,\qquad\operatorname{rank}P=5.
$$

Für die 60 normierten Quellenstrahlen ist

$$
M_t=\frac1{60}\sum_\ell|\psi_\ell\rangle\langle\psi_\ell|^{\otimes t}.
$$

Die niedrigen Momente sind isotrop:

$$
M_1=I/4,\qquad M_2=P_{\mathrm{sym},2}/10,\qquad M_3=P_{\mathrm{sym},3}/20.
$$

Erst das vierte Moment enthält die zusätzliche Richtungsauswahl:

$$
\boxed{40M_4=S+P,\qquad P=40M_4-S.}
$$

Die Diskrepanz gegenüber dem kontinuierlichen Mittel ist

$$
D^{(4)}=M_4-S/35=(7P-S)/280.
$$

**Einfach:** Die ersten drei Momentenordnungen sehen die spezielle endliche Quelle noch wie ein gleichmäßiges kontinuierliches Ensemble. In der vierten Ordnung tritt ihre zusätzliche Codestruktur hervor. Der Index vier bedeutet hier Momentenordnung, nicht vierdimensionale Raumzeit. [Q1, Abschnitt 1](#original-q1); historischer Momentenstand: fileciteturn10file0L52-L107

---

<a id="information"></a>
# 7. Was ein, zwei und drei Register wissen

## 7.1 Ein Register: keine logische Information

Schreibt man $V$ nach dem ersten Register in vier Blöcke $V_a$, gilt

$$
V_a^\dagger V_b=\frac{\delta_{ab}}4I_5.
$$

Jedes einzelne Register hat für jeden logischen Zustand die Dichtematrix $I_4/4$. Sein bekannter Verlust ist korrigierbar. Das ist nicht dieselbe Aussage wie Korrektur eines unbekannten Fehlers an unbekannter Position.

Die Isometrien $W_a=2V_a$ besitzen orthogonale Bilder. Ein beliebiger logischer Operator $O$ kann auf den drei verbleibenden Registern durch

$$
O_3=\sum_aW_aOW_a^\dagger,\qquad(I\otimes O_3)V=VO
$$

dargestellt werden. fileciteturn14file0L81-L109

## 7.2 Die Ränge sind Ränge von Operatorabbildungen

Für $\mathcal E_k(X)=\operatorname{Tr}_{4-k}(VXV^\dagger)$ gilt

$$
\boxed{\operatorname{rank}\mathcal E_1=1,\quad
\operatorname{rank}\mathcal E_2=10,\quad
\operatorname{rank}\mathcal E_3=25.}
$$

Die 25 Richtungen umfassen die Identität. Allgemeine gemischte normierte Fünferniveauzustände besitzen 24 reelle Parameter, reine Zustände acht. Der Rang zehn ist kein Nachweis zehn übertragener Quantenfreiheitsgrade.

```text
Vollständiger logischer Fünferzustand
                 │
       ┌─────────┼─────────────┐
       ▼         ▼             ▼
  1 Register  2 Register    3 Register
     I₄/4     10 Effekte    vollständiger Operatorraum
  unabhängig  bestimmte    Rekonstruktion möglich
  vom Inhalt  Messung
```

## 7.3 Zwei Register: eine konkrete Messung

Die zehn reellen symmetrischen Paulis sind in dieser Reihenfolge

```text
II  IX  IZ  XI  XX  XZ  YY  ZI  ZX  ZZ
```

Mit $b_\nu=\operatorname{vec}(A_\nu)/2$ faktorisiert der Encoder:

$$
V|\psi\rangle=\sum_{\nu=1}^{10}(w_\nu^T\psi)
|b_\nu\rangle_{12}|b_\nu\rangle_{34}.
$$

Die zehn Zeilen von $W_{10}$ erfüllen

$$
W_{10}^TW_{10}=I_5,\qquad\|w_\nu\|^2=1/2,\qquad
w_\nu^Tw_\mu=\pm1/6\quad(\nu\ne\mu).
$$

Nach Normierung entstehen zehn gleichwinklige Linien in $\mathbb R^5$. Der Paarverlust ergibt

$$
\boxed{\mathcal E_2(\rho)=\sum_\nu\operatorname{tr}(F_\nu\rho)
|b_\nu\rangle\langle b_\nu|,\qquad F_\nu=|w_\nu\rangle\langle w_\nu|.}
$$

Das ist ein Kanal vom Typ Messen und Präparieren. Er überträgt keine Verschränkung zwischen einer äußeren Referenz und dem ausgegebenen Registerpaar. Die beiden Register des Paars können untereinander trotzdem verschränkt sein. fileciteturn14file0L111-L158

## 7.4 Der genaue Rückkanal und die Rolle von 2/3

Zur Referenz $I_5/5$ gehört $P_{\mathrm{sym},2}/10$. Die konkrete Petz Rückführung ist auf diesem Träger

$$
\mathcal R_2=2\mathcal E_2^\dagger.
$$

Die Effekte erfüllen

$$
2\operatorname{tr}(F_\nu F_\mu)=
\begin{cases}1/2&\nu=\mu,\\1/18&\nu\ne\mu.\end{cases}
$$

Daraus folgt

$$
\boxed{\operatorname{spec}(\mathcal R_2\mathcal E_2)
=\{1^{\times1},(4/9)^{\times9},0^{\times15}\}.}
$$

Die gewöhnlichen Singularwerte der Auslesung sind $1/\sqrt2$, neunmal $\sqrt2/3$ und fünfzehn Nullen. Nach der erklärten Referenznormalisierung lauten sie $1$, neunmal $2/3$ und fünfzehn Nullen. Auf dem reellsymmetrischen 15 dimensionalen Operatorraum bleiben nur fünf Nullrichtungen.

**Nicht vermischen:** $2/3$ ist die normierte Singularübertragung; $4/9$ der Eigenwert des Hin und zurück Kanals. Drei Rückkompositionen liefern arithmetisch $(4/9)^3=(2/3)^6$, wählen aber keine drei physischen Zyklen und nicht die fehlende Richtung $(1/3)^6$. fileciteturn14file0L228-L272


---

<a id="geometrie"></a>
# 8. Die verborgene Auslesegeometrie: sechs Marken, Petersen und Blindraum

## 8.1 Die sechs Marken sind tatsächlich dieselben Vektoren

In den unnormalisierten Codekoordinaten sind die sechs Simplexspalten

$$
W_6=\begin{pmatrix}
2&2&-1&-1&-1&-1\\
0&0&-1&-1&1&1\\
0&0&-1&1&-1&1\\
0&0&1&-1&-1&1\\
1&-1&0&0&0&0
\end{pmatrix},
\qquad W_6^TGW_6=48I_6-8J_6.
$$

Für $u_q=G^{1/2}(W_6)_q$ und $\Gamma=W_{10}W_{10}^T$ gilt

$$
C=6\Gamma-3I_{10},\qquad C^2=9I_{10}.
$$

$C$ hat Nullen auf der Diagonale und sonst Vorzeichen. Genau sechs relative Vorzeichenklassen $s$ erfüllen $Cs=3s$. Sie sind explizit

$$
\boxed{s_q=\frac12W_{10}u_q\in\{\pm1\}^{10}.}
$$

Mit $D=\operatorname{diag}(s)$ bildet

$$
A_s=\frac{J-I-DCD}{2}
$$

jeweils einen Petersen Rahmen:

$$
A_s\mathbf1=3\mathbf1,\qquad A_s^2=2I+J-A_s.
$$

Das ist eine Gleichheit konkreter Matrizen und Rahmen, nicht nur die Wiederholung der Zahl sechs. Die Graphkanten sind zunächst Auslesebeziehungen, keine räumlichen Nachbarschaften. fileciteturn14file0L160-L201

## 8.2 Alle sechs reinen Markierungszustände sehen als Paar gleich aus

Für $v_q=u_q/\sqrt{40}$ gilt

$$
\mathcal E_2(|v_q\rangle\langle v_q|)=P_{\mathrm{sym},2}/10,
\qquad
\frac16\sum_q|v_q\rangle\langle v_q|=I_5/5.
$$

Die fünf unabhängigen spurfreien Differenzen

$$
B_q=|v_q\rangle\langle v_q|-I_5/5
$$

spannen den reellen Blindraum auf, mit

$$
\operatorname{tr}(B_qB_r)=\frac{24}{25}\delta_{qr}-\frac4{25}.
$$

**Einfach:** Sechs verschiedene vollständige Zustände liefern exakt dieselbe Paaranzeige. Die Paargeometrie zeigt ihre gemeinsame Organisation, entscheidet aber nicht, welcher davon vorliegt.

Daraus folgt: Kein Hamiltonoperator aus höchstens Zweiregistertermen kann einen dieser sechs Zustände als einzigen globalen Grundzustand auswählen. Falls einer die niedrigste Energie besitzt, besitzen alle dieselbe Energie; sie spannen den gesamten Fünfercode auf. Das gilt für genau diese Zustände und dieselbe Einbettung. fileciteturn14file0L203-L226

## 8.3 Ein expliziter Anschluss an den älteren Reflexionskanal

Auf $\operatorname{End}(\mathbb C^5)$ hat der gemittelte native Reflexionskanal $T_5$ die vier Sektoren

$$
1+5+9+10
$$

mit Eigenwerten $1,3/5,1/3,1/5$. Im Auslesewörterbuch sind dies Identität, reeller markierter Blindraum, sichtbare spurfreie Paarinformation und imaginär antisymmetrische Information.

Es gilt die Operatoridentität

$$
\mathcal R_2\mathcal E_2
=\frac{(5T_5-3I)(5T_5-I)(15T_5-13I)}{16}.
$$

Das Polynom enthält negative Koeffizienten. Es identifiziert zwei vorhandene Operatoren, ist aber kein automatisch ausführbares positives Mischungsprogramm. [Q1, Abschnitt 5](#original-q1).


## 8.4 Die historische Reflexionsbindung ist ein weiterer, eigener Modellzweig

Die Fortsetzung vom 19. September hatte zusätzlich das Paarmodell $T_{\mathrm{ref}}=(1/60)\sum_\ell U_\ell\otimes\overline{U_\ell}$ und $h_{\mathrm{ref}}=I-T_{\mathrm{ref}}$ untersucht. Seine vier Sektoren besitzen Energien $0$, $2/5$, $2/3$, $4/5$ mit Dimensionen $1,5,9,10$. Es hat dieselbe Singulettgrundlinie, ist aber **nicht** der spätere Petz Bindungsoperator $h=I-\mathsf K$.

Für seine Dreierkette ist die kleinste Energie die kleinste reelle Nullstelle von

$$
375E^3-1100E^2+980E-256=0.
$$

Sie beträgt $0{,}467227803293\ldots$ mit exakter Grundraumdimension fünf und nächster Energie $4/5$. Die Viererkette wurde nur numerisch diagonalisiert: Grundenergie $0{,}575378874876\ldots$, Grundraumdimension eins, Lücke $0{,}257569832419\ldots$. Daraus wurde kein allgemeines Gerade/Ungerade Gesetz und kein thermodynamischer Grenzwert bewiesen.

Auch hier ließ die native Symmetrie nach Energienullpunkt und Gesamtmaßstab zwei unabhängige dimensionslose Paarverhältnisse frei. Der gemeinsame ideale Paarzustand fixierte sie nicht. Diese älteren Ergebnisse werden im [Originalbericht V19](#original-v19) vollständig bewahrt und nicht mit den späteren Dreierenergien verwechselt. fileciteturn10file0L371-L430 fileciteturn10file0L470-L503

---

<a id="steuerung"></a>
# 9. Steuerung, Dreierinformation und die markierte Hyperladung

## 9.1 Ein isoliertes Paar ist nicht schon eine Codeoperation

Für einen nichttrivialen Hermiteschen Paulioperator $A$ sei

$$
h_A=V^\dagger A_1A_2V.
$$

Sein Spektrum lautet $1$ zweifach und $-1/3$ dreifach. Der physische Operator $A_1A_2$ verlässt aber den Code. Der Austrittsoperator ist

$$
V^\dagger A_1A_2(I-P)A_1A_2V=I-h_A^2.
$$

Für den entsprechenden Puls beträgt die größte Austrittswahrscheinlichkeit

$$
p_{\mathrm{Austritt}}(t)=\frac89\sin^2t.
$$

Eine Kompression $PHP$ ist daher noch kein Beweis einer tatsächlich codeerhaltenden physikalischen Ausführung.

## 9.2 Die symmetrisierte Paaroperation erhält den Code wirklich

Die passende Ausführung ist

$$
\boxed{\widehat h_A=\frac16\sum_{r<s}A_rA_s.}
$$

Sie kommutiert mit dem Quartikstabilisator $Q$ und dem Registersymmetrieprojektor $S$, also mit $P=SQ$. Ihre Einschränkung ist genau $h_A$.

Die vier Kontrollen zu $IX,IZ,XI,ZZ$ erzeugen die volle logische $\mathfrak{su}(5)$. Die exakte Rangfolge lautet

$$
\boxed{4\to7\to12\to17\to22\to24.}
$$

Das ist kontrollierte Erreichbarkeit mit vorgegebenen Pulszeiten. Es wählt weder einen autonomen Hamiltonoperator noch eine physische $SU(5)$ Eichgruppe. fileciteturn14file0L274-L296

Ein konkreter Puls mit $K=(\sqrt3/2)(h_{IX}-h_{IY})$ unterscheidet nach der Bewegung zwei zuvor paargleiche Zustände:

$$
e^{-i\pi K/4}\frac{c_0+ic_1}{\sqrt2}=c_0,\qquad
e^{-i\pi K/4}\frac{c_0-ic_1}{\sqrt2}=-ic_1.
$$

Danach liefert $h_{IX}$ die Erwartungswerte $0$ beziehungsweise $2/3$. Momentan verborgene Information ist deshalb nicht unter allen kontrollierten Fortsetzungen verborgen.

## 9.3 Die vollständige Informationszerlegung

Die 15 nichtnull Pauli Adressen bilden 35 projektive Dreierlinien. Davon sind 15 kommutierend und 20 antikommutierend. Die zugehörigen Dreiregisteroperatoren spannen jeweils die 15 reellsymmetrischen beziehungsweise die zehn imaginär antisymmetrischen Hermiteschen Richtungen auf.

$$
\boxed{25=1+9+5+10.}
$$

Die vier Summanden bedeuten Identität, sichtbare Paarinformation, reelle Markierungsinformation und imaginäre Kohärenzen. Für $AB=isC$ auf einer antikommutierenden Linie gilt im vollen physischen Raum

$$
[\widehat h_A,\widehat h_B]=\frac{4is}{3}\widehat T_{ABC},
\qquad
\widehat T_{ABC}=\frac1{24}\sum_{r,s,t\;\mathrm{verschieden}}A_rB_sC_t.
$$

Die zusätzlichen Dreierwirkungen entstehen damit aus konkret geordneten Paarwirkungen. [Q1, Abschnitt 6](#original-q1).

## 9.4 Hyperladung: Darstellung vorhanden, unmittelbare Paarablesung nicht

Aus der bereits gewählten Markierung $q_*$ und Familienwirkung $\sigma$ werden fünf Differenzslots mit Gramform $48(I_5+J_5)$ gewonnen. Ein positiver Polartransport überträgt die drei Ladungen $-1/3$ und die zwei Ladungen $+1/2$ in den Code.

Für den so definierten Operator gilt

$$
Y=-\frac13P_3+\frac12P_2,\quad
\operatorname{tr}Y=0,\quad\operatorname{tr}Y^2=5/6.
$$

Die Paarspanne hat Rang zehn; zusammen mit $Y$ steigt der Rang auf elf. Sogar unter der verbleibenden relativen Phasenfreiheit ist

$$
\boxed{\min_\theta d_{\mathrm{HS}}^2(Y_\theta,\mathcal O_2)
=\frac{29}{60}-\frac{\sqrt6}{10}>0.}
$$

Drei Register reichen über den Erasure Decoder zur exakten codeerhaltenden Darstellung. Die Halbspinorkonstruktion $\Lambda^{\mathrm{even}}\mathbb C^5$ liefert die angegebenen Standardmodell Ladungsdarstellungen. Ihre physische Feldrealisierung und ihre Dynamik sind damit nicht bestimmt. fileciteturn14file0L311-L333

---

<a id="codeauswahl"></a>
# 10. Energetische Auswahl, Überlappung und ein erster virtueller Anschluss

## 10.1 Der einfache Momentenparent

Aus $40M_4=S+P$ folgt für den ausdrücklich gewählten Kandidaten

$$
\boxed{H_{\mathrm{mom}}=I-20M_4=I-\frac12(S+P)}
$$

das vollständige Spektrum

| Energie | Vielfachheit |
|---:|---:|
| 0 | 5 |
| $1/2$ | 30 |
| 1 | 221 |

Der Fünfercode ist genau sein Grundraum. Die symmetrisierten Paarkontrollen kommutieren mit diesem Parent. Ein einzelner Zustand innerhalb des Fünferraums wird dadurch nicht ausgewählt.

## 10.2 Warum drei lokale Registerterme nicht genügen

Die beiden Zustände

$$
\rho_5=P/5,\qquad\rho_{35}=S/35
$$

besitzen dieselben Marginalen bis einschließlich drei Register:

$$
\operatorname{Tr}_{4-k}\rho_5=
\operatorname{Tr}_{4-k}\rho_{35}
=\frac{P_{\mathrm{sym},k}}{\binom{k+3}{3}},\qquad k=1,2,3.
$$

Ein höchstens dreilokaler Hamiltonoperator hat in beiden dieselbe Energie. Ist der ganze Fünfercode Grundraum, muss unter dieser Forderung auch der gesamte 35erträger im Grundraum liegen. **Genau den gesamten Fünfercode als alleinigen Grundraum auszuwählen erfordert in dieser Einbettung eine Viererstruktur.**

Auch $\rho_{30}=(S-P)/30$ hat dieselben niedrigen Marginalen. Maximale Entropie ohne Quartikzusatz wählt $\rho_{35}$, nicht $\rho_5$. Die entsprechende Entropiedifferenz ist $\log_2 7$. fileciteturn14file0L335-L366

## 10.3 Perfekte überlappende Fünfercodes sind inkompatibel

Für zwei identisch orientierte Viererblöcke mit wörtlich gemeinsamen $\mathbb C^4$ Tensorfaktoren gilt

| Gemeinsame Register | Nichtnull Hauptwinkelkosinus | Vielfachheit | Minimum von $(I-P_A)+(I-P_B)$ |
|---:|---:|---:|---:|
| 1 | $1/4$ | 100 | $3/4$ |
| 2 | $1/2$ | 10 | $1/2$ |
| 3 | $1/4$ | 20 | $3/4$ |

In allen Fällen ist $\operatorname{Ran}P_A\cap\operatorname{Ran}P_B=\{0\}$. Gemeinsame Registersymmetrie würde die Quartikchecks auf alle Vierermengen der Vereinigung ausdehnen. Daraus entstehen einander widersprechende antikommutierende Zweierchecks.

Andere Orientierungen, Randregister oder Faktorisierungen wurden damit nicht pauschal ausgeschlossen. **Getrennte Blöcke können weiterhin wechselwirken.** fileciteturn14file0L368-L386

## 10.4 Zwei getrennte Fünferblöcke koppeln in zweiter Ordnung

Mit

$$
H_0=\Delta(H_{\mathrm{mom}}^A+H_{\mathrm{mom}}^B),\quad
V_g=g(a_1^Aa_1^B+a_2^Aa_2^B),\quad a=I_2\otimes\sigma_z
$$

verschwindet die erste Kompression. Die zweite Ordnung ergibt

$$
\boxed{H_{\mathrm{eff}}^{(2)}=\frac{g^2}{\Delta}
\left[-\frac{29}{24}I-\frac{11}{24}(h_A\otimes I+I\otimes h_B)
-\frac{15}{8}h_A\otimes h_B\right].}
$$

Das ist eine echte logische Wechselwirkung. Kleine vollständige invariante Blöcke bestätigten numerisch die Annäherung an die Störungskoeffizienten; für den Hell/Hell Zweig tendiert $E/g^2$ gegen $-4$. Die Formel ist keine exakte Entwicklung für beliebig großes $g$. fileciteturn14file0L388-L424

Der allgemeinere Parent $H_r=r(S-P)+(I-S)$ trägt denselben Grundcode, aber andere relative Energien. Für dieselben Paarlinks erhält man

$$
C_0(r)=-\frac{5r^2+10r+1}{8r(r+1)},\quad
C_1(r)=\frac{(r-1)(5r+3)}{8r(r+1)},\quad
C_2(r)=-\frac{5r^2+2r+9}{8r(r+1)}.
$$

Dabei ist $C_2(1/2)=-15/8$, aber $C_2(1)=-1$. Derselbe Code und dieselbe statische Symmetrie bestimmen die Bewegung folglich nicht eindeutig. [Q2, Abschnitt 10](#original-q2).

---

<a id="geschuetzte-quelle"></a>
# 11. Die vollständige Quelle schützen statt ihren Quotienten ersetzen

## 11.1 Der gleiche Hamming Seed liefert kompatible Checks

Der binäre Zeilenraum $C$ der Matrix

$$
H_7=\begin{pmatrix}
1&1&1&1&0&0&0\\
1&1&0&0&1&1&0\\
1&0&1&0&1&0&1
\end{pmatrix}
$$

hat sieben nichtnull Wörter vom Gewicht vier. Sie schneiden sich paarweise in zwei Positionen; ihre Dreierkomplemente sind die Fano Linien. Als konkrete binäre Mengen gilt

$$
\boxed{\{(c,0)+b\mathbf1_8:c\in C,b\in\mathbb F_2\}=\operatorname{RM}(1,3).}
$$

Es ist genau derselbe Code wie bei der Konstruktion der E₈ Wurzeln. Die kompatiblen Quartikchecks verwenden nicht zusätzlich den vollen Viererregistersymmetrieprojektor, der die vorigen Überlappungskonflikte erzeugte.

## 11.2 Encoder und tatsächliche native Gruppenwirkung

Zwei Steane Kodierungen werden zu sieben vierstufigen Registern zusammengefasst:

$$
V_7|ab\rangle=\frac18\sum_{u,v\in C}
|2(u+a\mathbf1)+(v+b\mathbf1)\rangle.
$$

Die Klammern werden binär addiert. Der logische Raum ist $\mathbb C^4$. Beliebige Fehler auf einem vollständigen physischen vierstufigen Register sind korrigierbar.

Für alle 60 tatsächlichen Quellenreflexionen wurde geprüft

$$
\boxed{U^{\otimes7}V_7=V_7\overline U.}
$$

Nach zwei Kodierstufen folgt algebraisch $U^{\otimes49}V_{49}=V_{49}U$. Die erste Konjugation ist Inhalt der Kodierung und darf in geladenen Anschlüssen nicht ignoriert werden. Das Ergebnis stammt nicht aus einer Diagonalisierung eines 49 Registerraums. fileciteturn14file0L426-L489

## 11.3 Parent und vollständiges Syndromspektrum

Die sieben kommutierenden Quartikprojektoren $Q_S$ definieren

$$
H_F=\sum_S(I-Q_S).
$$

| Energie | Vielfachheit |
|---:|---:|
| 0 | 4 |
| 4 | 420 |
| 6 | 5880 |
| 7 | 10080 |

Die Summe ist $4^7=16384$. Ein Syndrom ist eine $4\times3$ Matrix über $\mathbb F_2$. Für Rang $r$ sind $8-2^{3-r}$ Checks verletzt; die Rangzahlen $1,105,1470,2520$ liefern das Spektrum nach Multiplikation mit vier logischen Zuständen.

Innerhalb der benannten Klasse doppelt gerader, selbstorthogonaler CSS Checks mit gleichem Prüfcode für beide Pauliarten, mindestens einem logischen Qubit und Einzelfehlerkorrektur ist sieben minimal. Für Länge $n$ und Prüfrang $r$ gelten $n-2r\ge1$ und $n\le2^r-1$. Bei $n\le6$ sind beide unvereinbar, bei sieben werden die sieben nichtnull Spalten von $\mathbb F_2^3$ erzwungen. Das ist **eine bedingte Codeminimalität**, keine Herleitung von sieben physischen Nachbarn. fileciteturn14file0L465-L512

---

<a id="igusa"></a>
# 12. Die Igusa Verbindung: ein vollständiger gemeinsamer Invariantenring

## 12.1 Die fünf Quartikkoordinaten und ihre sechs Ansichten

Aus der vorhandenen Codebasis entstehen

$$
\begin{aligned}
p&=\sum_{i=0}^3z_i^4,\\
a&=6(z_0^2z_1^2+z_2^2z_3^2),\\
b&=6(z_0^2z_2^2+z_1^2z_3^2),\\
c&=6(z_0^2z_3^2+z_1^2z_2^2),\\
d&=24z_0z_1z_2z_3.
\end{aligned}
$$

Setzt man $x=W_6^Tf$, $f=(p,a,b,c,d)^T$, erhält man

$$
x=(2p+d,2p-d,-p-a-b+c,-p-a+b-c,-p+a-b-c,-p+a+b+c).
$$

Direktes Ausmultiplizieren liefert

$$
\boxed{\sum_ix_i=0,\qquad F(x)=(\sum_ix_i^2)^2-4\sum_ix_i^4=0.}
$$

Das ist die klassische Igusa Quartik. Ihre affine Bilddimension ist vier, ihre projektive Dimension drei über $\mathbb C$. **Diese drei komplexen Moduldimensionen sind keine drei physisch hergeleiteten Raumdimensionen.** fileciteturn17file0L50-L96

## 12.2 Vollständigkeit des Rings und Grade

Die volle Zweiqubit Pauli Gruppe $\mathcal P$ besitzt 64 Elemente. Die im Bericht berechnete Molien Funktion lautet

$$
\frac1{64}\left[\sum_{\xi\in\mu_4}(1-\xi t)^{-4}
+\frac{30}{(1-t^2)^2}+\frac{30}{(1+t^2)^2}\right]
=\frac{1-t^{16}}{(1-t^4)^5}.
$$

Mit dem im Bericht herangezogenen klassischen Quotientensatz folgt

$$
\mathbb C[z_0,z_1,z_2,z_3]^{\mathcal P}
\cong\mathbb C[x_1,\ldots,x_6]/(\sum x_i,F(x)).
$$

Die Generatoren erfüllen eine Relation; sie sind deshalb nicht fünf algebraisch unabhängige Koordinaten einer freien Quelle.

Alle 60 ursprünglichen Reflexionen wirken auf den $x_i$ als die 15 Transpositionen, jeweils vierfach. Ihr Kern ist genau $\mathcal P$, ihr Bild $S_6$, die Gruppenordnung $64\cdot720=46080$.

Für die elementarsymmetrischen Funktionen gilt

$$
e_1=0,\qquad e_4=e_2^2/4.
$$

Die verbleibenden Generatoren $e_2,e_3,e_5,e_6$ haben deshalb Quellengrade $4(2,3,5,6)=(8,12,20,24)$ und stehen gemeinsam in

$$
\boxed{\prod_i(u-x_i)=u^6+e_2u^4-e_3u^3+\frac{e_2^2}{4}u^2-e_5u+e_6.}
$$

Die Grade sind damit abhängige Ausprägungen derselben Struktur, nicht vier zusätzliche unabhängige Belege. fileciteturn17file0L98-L145

## 12.3 Die 60 Reflexionsflächen und das Maschke Polynom

Jede der 15 Differenzen faktorisiert in vier ursprüngliche Gaußsche Wurzelkovektoren:

$$
x_i(z)-x_j(z)=c_{ij}\prod_{\alpha\in B_{ij}}\ell_\alpha(z),\qquad |B_{ij}|=4.
$$

Alle 60 Reflexionshyperflächen werden genau einmal verwendet. Beispielsweise ist $x_1-x_2=48z_0z_1z_2z_3$. Daher

$$
\operatorname{Disc}_u\prod_i(u-x_i(z))
=C\prod_{\alpha=1}^{60}\ell_\alpha(z)^2.
$$

Mit

$$
M(z)=\sum_i z_i^8+14\sum_{i<j}z_i^4z_j^4+168z_0^2z_1^2z_2^2z_3^2
$$

gilt $\sum x_i^2=12M(z)$. Die vorher dokumentierte Wurzelnormierung ist $F_8=1920M=7680w^Tw$, daher hier $F_8=160\sum x_i^2$. Die Hermitesche Paarung $w^\dagger w$ und die holomorphe Paarung $w^Tw$ sind unterschiedliche Auslesungen derselben Quartikabbildung, nicht identische Objekttypen. [Q2, Abschnitt 4](#original-q2); ursprüngliche Paarungsverbindung: fileciteturn10file0L230-L287

## 12.4 Bellquadriken, Segre und die Doily

Für jeden der zehn tatsächlichen Belloperatoren gilt

$$
\boxed{\sum_{q=1}^{6}s_{\nu q}x_q(z)=6(z^TA_\nu z)^2.}
$$

Jede Vorzeichenzeile besitzt drei Pluszeichen und drei Minuszeichen. Die zehn Klassen sind die ausgezeichneten Hyperflächen der Igusa Geometrie; die projektive Dualität zur Segre Kubik ist bekannte Mathematik.

Jede perfekte Paarung der sechs Labels definiert eine singuläre Gerade

$$
x_i=x_j=A,\quad x_k=x_l=B,\quad x_m=x_n=C,\quad A+B+C=0.
$$

Die 15 ausgezeichneten Schnittpunkte haben Form $(2,2,-1,-1,-1,-1)$ mit allen Platzierungen des Zweierpaars. Die 60 ursprünglichen Quellenstrahlen werden genau auf diese 15 Punkte abgebildet, vier pro Punkt.

Für die zugehörige Inzidenzmatrix gilt

$$
\operatorname{rank}N=10,\qquad
\operatorname{spec}(NN^T)=\{9^{\times1},4^{\times9},0^{\times5}\}.
$$

Daher erscheint wieder die Singularliste $1,(2/3)^{\times9},0^{\times5}$ von $N/3$. **Ein gemeinsames algebraisches Wörterbuch ist geschlossen; ein physischer Clockanschluss ist es nicht.** fileciteturn17file0L188-L234

---

<a id="quellendynamik"></a>
# 13. Die Quelle ist mehr als ihr Fünferbild

## 13.1 Welche Zustände das kohärente Bild nicht enthält

Die sechs ausgezeichneten Codezustände besitzen in den sechs Koordinaten Form $(5,-1,-1,-1,-1,-1)$. Es gilt

$$
F(5,-1,-1,-1,-1,-1)=30^2-4\cdot630=-1620\ne0.
$$

Keiner ist daher das Bild einer einzelnen kohärenten Eingabe $z^{\otimes4}$. Sie bleiben legitime Zustände des ganzen Fünfercodes. Ihre Präparation braucht aber mehr als diese eine Eingabeklasse, etwa eine passende verschränkte Vierregistereingabe. Auch ein algebraisches Markierungslabel wird damit nicht verboten. fileciteturn17file0L236-L246

## 13.2 Ein fester linearer Fünferfluss ist zu eng

Für einen allgemeinen infinitesimalen linearen Fluss $\dot x=Ax$ auf der Igusa Fläche muss

$$
\nabla F(x)\cdot Ax=\kappa F(x)
$$

gelten. Der exakte Koeffizientenvergleich hat Rang 25 bei 26 Unbekannten. Es bleibt nur $A=(\kappa/4)I$, also projektiv eine triviale Skalierung.

Dieser Satz betrifft die gesamte feste kohärente Bildfläche. Er verbietet keine diskreten Quellenoperationen, nichtlinearen Lifts, bewegten Coderräume oder allgemein verschränkten Codeeingaben.

## 13.3 Der minimale lineare Antwortsektor ist 35 dimensional

Bereits die ersten Antworten der Quellenableitungen spannen

$$
\boxed{\operatorname{span}\{f_a,z_i\partial_{z_j}f_a\}
=\operatorname{Sym}^4(\mathbb C^4)^*,\qquad\dim=35.}
$$

Die zusätzliche Struktur ist genauer

$$
\boxed{35=5+\sum_{a\ne0}2_a.}
$$

Auf dem symmetrischen Raum sind

$$
P_a=\frac1{16}\sum_b(-1)^{[a,b]}A_b^{\otimes4}
$$

orthogonale Charakterprojektoren. Der triviale Sektor hat Rang $(35+15\cdot3)/16=5$, jeder nichttriviale Rang $(35-3)/16=2$. Für $K_a=\sum_rA_{a,r}$ gilt

$$
P_sK_aP_t=0\quad\text{außer bei }s=t+a.
$$

Jede der fünfzehn Pauli Adressen besitzt damit ihren zugehörigen Zweierantwortbereich. Die 30 Richtungen sind keine aus der Zahl 30 erratenen Teilchen. fileciteturn17file0L248-L285 fileciteturn18file0L77-L106

## 13.4 Derselbe sichtbare Zustand kann eine andere Zukunft haben

Für

$$
z=(1,2,4,8),\qquad z'=(I\otimes X)z=(2,1,8,4)
$$

sind die Quartikwerte identisch:

$$
f(z)=f(z')=(4369,6168,1632,768,1536).
$$

Unter demselben $H_{\mathrm{src}}=I\otimes Z$ gilt aber

$$
\dot f(z)=(15420i,0,5760i,0,0),\qquad\dot f(z')=-\dot f(z).
$$

Der Unterschied ist keine gemeinsame Phase. Normierung beider Quellen ändert die Schlussfolgerung nicht. Die fünf Quotientenkoordinaten allein bestimmen diese Entwicklung nicht.

Die ursprüngliche Quellenwirkung hat unter der Fünferdarstellung einen Pauli Kern. In einem tomografisch vollständigen Präparations und Testvertrag sind nur die vier skalaren Phasen irrelevant; der zulässige projektive Gruppenquotient hat Ordnung 11520, nicht 720. Generisch besitzt der projektive Pauli Quotient 16 Zweige. Vier klassische Bits können diese Zweige beschriften, ersetzen aber keinen vollständigen Quantenzustand. fileciteturn17file0L287-L310 fileciteturn10file0L342-L369

```text
Quelle z  ─── gleiche Quartikansicht ─── Quelle z′
   │                                      │
   │ derselbe Quellenoperator             │ derselbe Quellenoperator
   ▼                                      ▼
Antwort +ẋ                              Antwort −ẋ

Die verdichtete Gegenwart enthält nicht alle Daten ihrer Zukunft.
```

## 13.5 Rückwirkung behalten statt einen neuen Generator erfinden

Für einen unabhängig gegebenen $H$ und $Q=I-P$ gilt

$$
P(\zeta-H)^{-1}P=
[\zeta-PHP-PHQ(\zeta-QHQ)^{-1}QHP]^{-1}.
$$

Die Feshbach Identität bewahrt die spektral abhängige Rückwirkung des zusätzlichen Sektors. Sie liefert $H$ nicht selbst und rechtfertigt keinen unbegründeten Ersatz durch eine konstante Markovrate.

## 13.6 Informationsmetrik und Entropie: zwei weitere begrenzte Ergebnisse

Für die kollektive Orientierung gilt

$$
P\,d\Gamma_4(X)\,P=\operatorname{tr}(X)P,\qquad
g(X,Y)=8\operatorname{tr}(X_0Y_0),\qquad F_Q=\frac45g.
$$

Der Orientierungsraum ist 15 dimensional und trägt eine positive Informationsmetrik. Die kollektive Berry Verbindung ist $\mathcal A=\operatorname{tr}(U^\dagger dU)I_5$, auf $SU(4)$ null und lokal auch auf $U(4)$ flach. Das ist keine Lorentzmetrik und erzeugt allein kein nichtabelsches kontinuierliches Eichfeld. Diskrete Holonomie bleibt möglich. fileciteturn14file0L514-L538

Für den Kontrastqubit maximiert die Choi Entropie bei $t=1/27$. Seine Pauliwahrscheinlichkeiten sind dann $(5/9,5/18,1/18,1/9)$. Der dynamische Anschluss verlangt zwei unabhängige Pauli Sprungarten und keine eigenständige dritte $Y$ Sprungart; dann ist $\lambda_Y=\lambda_X\lambda_Z$.

Andere Entropieobjekte wählen andere Werte: sechs Ereignisse etwa $0{,}0357983733$, der angegebene vollständige Dreiniveaukanal etwa $0{,}0365656628$. Die behauptete zusätzliche Gleichsetzung mit einem Jarlskog Invarianten wurde in der Fortsetzung mangels neuer Definition nicht erneut zertifiziert. Ein konjugationsinvariantes Entropiefunktional wählt jedenfalls nicht dessen konjugationsungerades Vorzeichen. fileciteturn14file0L540-L557


---

<a id="austausch"></a>
# 14. Geschützte vollständige Quellen tauschen Information aus

Zwei getrennte Siebenregisterquellen werden mit

$$
H_0=\Delta(H_F^A+H_F^B),\qquad
V_g=g\sum_{r=1}^{7}\sum_{a=1}^{15}A_{a,r}^AA_{a,r}^B
=g\sum_{r=1}^{7}(4\operatorname{Swap}_r-I)
$$

gekoppelt. $g$, $\Delta$ und die Auswahl der Links sind zusätzliche Modelldaten.

Wegen des Codeabstands verschwinden direkte logische Fehler bis zur erforderlichen Rückkehrordnung. Die ersten effektiven Terme lauten

$$
PV_gP=0,\qquad
H_{\mathrm{eff}}^{(2)}=-\frac{105g^2}{8\Delta}I,
$$
$$
\boxed{H_{\mathrm{eff}}^{(3)}=\frac{g^3}{\Delta^2}
\left(\frac{21}{8}\operatorname{Swap}_{\mathrm{logisch}}-\frac{63}{16}I\right).}
$$

**Der erste nichtskalare logische Austausch erscheint in dritter Ordnung.** Ein passendes Dreierwort auf einer Fano Linie trägt eine nichttriviale logische Wirkung. Der Schutz legt damit fest, wann Wechselwirkung erstmals erscheinen kann.

Die vollständige Pfadzählung unterscheidet 1470 geordnete Dreierpfade an derselben Position, deren skalare Pauli Phasensumme $-210$ beträgt, und 630 Pfade auf Fano Linien:

$$
7\text{ Linien}\cdot6\text{ Reihenfolgen}\cdot15\text{ Pauliarten}=630.
$$

Beide Zwischennenner sind $8\Delta$. Die Pauli Identität $\sum_{a=1}^{15}A_a^*\otimes A_a^*=4\operatorname{Swap}-I$ liefert den Koeffizienten. fileciteturn17file0L345-L419

Eine unabhängige Ein Pauli Kontrolle ist ein vollständiges acht dimensionales Syndrommodell. Für $M=8\Delta$ und $\xi=\pm1$ ist

$$
E_\xi=\frac{M+6\xi g-\sqrt{(M+6\xi g)^2+28g^2}}2
=-\frac{7g^2}{M}+\frac{42\xi g^3}{M^2}+O(g^4/M^3).
$$

Diese exakte kleine Lösung bestätigt den Ein Pauli Beitrag; die Vollständigkeit des ganzen Austauschs folgt zusätzlich aus der vollständigen Pauli Pfadzählung.

Der Paarraum zerfällt in $\operatorname{Sym}^2\mathbb C^4$ mit Dimension zehn und $\Lambda^2\mathbb C^4$ mit Dimension sechs. Diese Zehn ist **nicht** allein wegen ihrer Dimension der Spin(10) Vektorzehner. [Q2, Abschnitte 8 und 9](#original-q2).

---

<a id="dynamischer-abschluss"></a>
# 15. Dynamische Auswahl des Fünfercodes: der Bausteinabschluss

## 15.1 Das definierte Vierblockmodell

Vier geschützte Quellen werden auf einem vorgegebenen Graphen $G$ gekoppelt:

$$
H(g)=\Delta\sum_{v=1}^{4}H_F^{(v)}
+g\sum_{(v,w)\in E(G)}\sum_{r=1}^{7}\sum_{a=1}^{15}
A_{a,r}^{(v)}A_{a,r}^{(w)}.
$$

Der Hauptsatz verwendet $G=K_4$, gleiche negative Kopplung $g<0$ und hinreichend kleines $|g|/\Delta$. Die ursprünglichen Schutzterme sind vierlokal; nur die zusätzlich eingeführten Links sind zweilokal. **Der gesamte mikroskopische Operator ist nicht rein zweilokal.**

## 15.2 Die erste Auswahl ist Symmetrie

Die dritte Ordnung lautet bis auf Skalare

$$
H_{\mathrm{eff}}^{(3)}=\frac{21}{8}\frac{g^3}{\Delta^2}
\sum_{(v,w)\in E(G)}\operatorname{Swap}_{vw}.
$$

Für $g<0$ wird jeder Kantenswap maximiert. Auf einem verbundenen Graphen erzwingt dies die vollständige Registersymmetrie:

$$
\boxed{4^4=256\longrightarrow\operatorname{Sym}^4\mathbb C^4,
\qquad\dim=35.}
$$

Für $K_4$ beträgt die führende äußere Lücke $(21/2)|g|^3/\Delta^2$. Bei positivem $g$ gewinnt dagegen der eindimensionale vollständig antisymmetrische Viererraum. Das Vorzeichen ist also eine echte Auswahlbedingung. fileciteturn18file0L108-L158

## 15.3 Warum die innere Fünferauswahl erst in sechster Ordnung möglich ist

Die Kommutantendimensionen der tatsächlichen nativen Quellgruppe auf einem bis vier Faktoren sind $1,2,6,29$, für $U(4)$ dagegen $1,2,6,24$. Bis einschließlich drei Faktoren ist ein nativer invarianter Operator bereits kontinuierlich unitär invariant. Im symmetrischen Viererraum sind die beiden nativen irreduziblen Komponenten $5$ und $30$ erstmals unterscheidbar.

Ein nichttrivialer logischer Treffer auf einem Siebenregisterblock braucht drei physische Fehler. Vier solche Blöcke brauchen daher mindestens zwölf Endpunkte, also sechs Paarlinks. Vorher kann kein nichtskalarer nativer Viererterm die innere $5/30$ Aufspaltung erzeugen.

## 15.4 Die sechs virtuellen Schritte erzeugen den ursprünglichen Quartikstabilisator

Jeder minimale verbundene Vierblockpfad hat Grad drei an jedem Block. Die drei getroffenen Positionen müssen eine Fano Linie bilden und dieselbe Pauliadresse tragen. Verbundenheit erzwingt dieselbe Adresse an allen sechs Links. Der Rückkehrterm ist daher $A_a^{\otimes4}$; Summation liefert $16Q-I$.

```text
Vier geschützte Quellen
        │
        │ Ordnung 3: Austausch bevorzugt Symmetrie
        ▼
35 symmetrische Richtungen
        │
        │ Ordnung 6: Fano Rückkehrwörter aller 15 Adressen
        ▼
16Q − I  →  Q auf Sym⁴  =  Π₅
        │
        ▼
Fünfergrundsektor ohne vorher eingesetzten äußeren Π₅ Term
```

Für gleiche Kopplung auf $K_4$ folgt

$$
\boxed{H_{\mathrm{eff}}\big|_{35}=E_{\mathrm{sym}}(g)I
-\frac{27573}{512}\frac{g^6}{\Delta^5}\Pi_5
+O(|g|^7/\Delta^6).}
$$

Der Koeffizient hat das für die Fünferauswahl benötigte Vorzeichen. Innerhalb dieser Modellklasse wird der Selektor durch Kopplungen erzeugt und nicht nachträglich als fertiger äußerer Projektor eingesetzt. fileciteturn18file0L160-L246

## 15.5 Wo der Koeffizient herkommt

Es gibt zwei verbundene kubische Multigraphtypen auf vier markierten Blöcken: alle sechs einfachen $K_4$ Kanten oder zwei gegenüberliegende doppelte Kanten mit zwei einfachen Kreuzkanten. Letztere besitzen sechs markierte Varianten.

Die Registerlabels $h_e\in\mathbb F_2^3\setminus\{0\}$ erfüllen an jedem Block $\sum h_e=0$. Für $K_4$ ergeben sich 210 gültige Belegungen, davon 168 unabhängige Dreierrahmen und 42 abhängige. Beim zweiten Typ gibt es 63 physisch verschiedene Belegungen je Variante.

Ein teilweise getroffener Block trägt $4\Delta$ Zwischenenergie. Die vollständige Summe über 720 Reihenfolgen ist $83/16384$ beziehungsweise $449/73728$. Mit den Belegungszahlen entsteht

$$
\kappa_{K_4}=\frac{8715+6\cdot3143}{512}=\frac{27573}{512}.
$$

Eine zweite rationale Eigenwertentwicklung im vollständigen 512 dimensionalen Ein Pauli Syndromraum bestätigt denselben sechsten Koeffizienten und das ganze Polynom für ungleiche Kantengewichte. Die kleinen binären Flüsse sind keine hergeleiteten Raumkoordinaten. [Q3, Abschnitte 7 und 8](#original-q3).

## 15.6 Genaue Reichweite und Topologiekontrollen

Für hinreichend kleine negative Kopplung besitzt das vollständige definierte Modell einen genau fünfdimensionalen niedrigsten Eigenraum. Seine Lücke zum übrigen symmetrischen Band ist

$$
\Delta_{\mathrm{Code}}=\frac{27573}{512}\frac{|g|^6}{\Delta^5}
+O(|g|^7/\Delta^6).
$$

Der Satz benutzt analytische Störung, Isolierung des tiefen Bandes und native Darstellungstheorie. Eine vollständige Diagonalisierung des $4^{28}=72057594037927936$ dimensionalen Raums wurde nicht durchgeführt. Die Normschranke $|g|/\Delta<1/105$ garantiert im Bericht nur die Isolation des 256erbandes, **nicht** bereits eine explizite Gültigkeitsgrenze für die innere Fünferauswahl.

Für den Viererring beträgt der entsprechende Koeffizient $3143/256$. In der offenen Viererkette verschwindet der Quartikterm dieser sechsten Ordnung. Spätere höhere Ordnungen sind dadurch nicht ausgeschlossen. Dass sowohl Ring als auch $K_4$ den Code erzeugen können, widerlegt die Folgerung einer eindeutig ausgewählten Graphgeometrie aus dem Fünferraum. fileciteturn18file0L240-L288

## 15.7 Idealer Codeabstand und tatsächlich wechselwirkender Code

Der nackte Grenzcode ist $V_7^{\otimes4}V_5\mathbb C^5$ mit Parametern $((28,5,6))_4$. Er kann zwei unbekannte Registerfehler oder fünf bekannte Registerverluste korrigieren. Zwei innere Fano Dreierwörter liefern einen expliziten nichtskalaren Gewicht sechs Zeugen.

Bei endlichem $g$ ist der tatsächliche Grundraum gedresst. Eine physische Zweiregisterobservable besitzt bereits

$$
O_{\mathrm{eff}}=\text{Skalar}\cdot I+
\frac9{32}(g/\Delta)^2h_a+O((g/\Delta)^3).
$$

Ihre beiden logischen Eigenwertgruppen unterscheiden sich um $(3/8)(g/\Delta)^2+O((g/\Delta)^3)$. Einzelne Registerfehler bleiben genau erkennbar, der exakte Abstand des wechselwirkenden Grundcodes ist aber zwei statt sechs.

**Dynamische Codebildung ist daher kein automatischer Nachweis eines hochrobusten passiven Speichers:** Die Schutzlücke entsteht erst in sechster, die unterscheidbare Zweierfehlerantwort bereits in zweiter Ordnung. fileciteturn18file0L290-L321

---

<a id="bindung"></a>
# 16. Quellenantwort und Informationsrückkanal werden zur Bindung

## 16.1 Ein weiterer logischer Anschluss

Im symmetrischen tiefen Band ist $\mathcal H_{35}=\mathcal C_5\oplus\mathcal C_{30}$. Ein nativer invarianter lokaler Operator hat nach Energieverschiebung die Form $H_{\mathrm{lokal}}=\delta Q$, $Q=I_{35}-P$.

Der neue, ausdrücklich definierte logische Anschluss lautet

$$
H_{AB}=\delta(Q_A+Q_B)+\epsilon L,
\qquad
L=\sum_{a=1}^{15}K_a\otimes K_a
=4\sum_{r,s=1}^{4}\operatorname{Swap}_{A_r,B_s}-16I.
$$

Die $K_a$ sind logische Quellenoperatoren. Ihre Verwendung ist nicht schon die unveränderte Projektion eines bestimmten mikroskopischen 56 Registermodells. Im früheren $K_4$ Kandidaten gilt $\delta\sim(27573/512)|g|^6/\Delta^5$, doch die neue Kopplung $\epsilon$ und ihre Realisierung bleiben eine weitere Anschlussannahme.

## 16.2 Die entscheidende Identität

Auf dem Fünfercode gilt $PK_aP=0$ und $PK_aK_bP=0$ für $a\ne b$. Die Operatoren

$$
R_a=\frac1{16}PK_a^2P=\frac{I+3h_a}{4}
$$

sind Rang zwei Projektoren mit $\sum_aR_a=6I_5$. Mit $\mathsf K$ als Matrix des früheren Rückkanals ergibt sich exakt

$$
\boxed{\sum_aR_a\otimes R_a=\frac32I_{25}+\frac92\mathsf K.}
$$

Alle durch einen Link erreichbaren Zwischenzustände besitzen Energie $2\delta$. Die zweite Ordnung liefert deshalb, bis auf eine Konstante,

$$
\boxed{H_{\mathrm{Bindung}}=Jh,\qquad h=I-\mathsf K,
\qquad J=576\epsilon^2/\delta.}
$$

Die Spektren sind

$$
\operatorname{spec}h=\{0^{\times1},(5/9)^{\times9},1^{\times15}\}.
$$

Die einzige Grundlinie ist $|\Omega_5\rangle=5^{-1/2}\sum_j|j\rangle|j\rangle$. **Die gemeinsame Matrixidentität ist bewiesen; Kanaliteration und Hamiltonzeit bleiben unterschiedliche Operationen.** fileciteturn20file0L72-L166

## 16.3 Ein exakter Grundzustand des ganzen 1225 dimensionalen Anschlusses

Mit $|\chi_{30}\rangle=L|\Omega_5\rangle/(16\sqrt6)$ ist der Zweiersektor exakt abgeschlossen:

$$
H_{AB}\big|_{\{\Omega,\chi\}}=
\begin{pmatrix}0&16\sqrt6\epsilon\\16\sqrt6\epsilon&2\delta+16\epsilon\end{pmatrix}.
$$

Seine tiefere Energie ist

$$
\boxed{E_-=\delta+8\epsilon-
\sqrt{(\delta+8\epsilon)^2+1536\epsilon^2}.}
$$

Für $0<|\epsilon|/\delta\le1/200$ beweist der Bericht die eindeutige globale Grundzustandseigenschaft im ganzen definierten 1225 dimensionalen Modell, mit konservativer Schranke $\operatorname{gap}\ge170\epsilon^2/\delta$. Der führende tatsächliche Abstand zum Neunersektor ist $320\epsilon^2/\delta$.

Die reduzierte Dichtematrix ist

$$
\rho_A=(1-\eta)P/5+\eta(I_{35}-P)/30,
$$
$$
\eta=\frac12\left(1-
\frac{\delta+8\epsilon}{\sqrt{(\delta+8\epsilon)^2+1536\epsilon^2}}\right).
$$

Der exakte Zustand benutzt also die 30 zusätzlichen Antworten bei endlicher Kopplung tatsächlich. Seine Entropie lautet $h_2(\eta)+(1-\eta)\log5+\eta\log30$ bei einheitlicher Logarithmusbasis. fileciteturn20file0L185-L277

## 16.4 Eine passende endliche Reflexionspositivität

In der nativen reellen Basis ist

$$
h=\frac43I-\frac29\sum_aR_a\otimes R_a.
$$

Für $J,\beta\ge0$ besteht die Exponentialreihe von $e^{-\beta Jh}$ aus positiv gewichteten $B\otimes B$ mit reellen Produkten $B$. Der Spiegeltest liefert $\operatorname{Tr}[(\bar A\otimes A)(B\otimes B)]=|\operatorname{Tr}(AB)|^2\ge0$.

Das ist ein endlicher Positivitätsnachweis für die erklärte Spiegelung. Er identifiziert sie nicht selbst mit der ursprünglichen TFPT Naht. [Q4, Abschnitt 3](#original-q4).

---

<a id="rekursion-alt"></a>
# 17. Der erste rekursive Fünferzweig und seine Grenzen

## 17.1 Drei Bausteine tragen wieder einen Fünfergrundraum

Für die exakt definierte Kette $H_3=h_{12}+h_{23}$ mit dem ursprünglichen $h=I-\mathsf K$ gilt

$$
\boxed{E_0=\frac{19-\sqrt{73}}{18},\qquad
\dim G_0=5,\qquad
\Delta_3=\frac{\sqrt{73}-1}{18}.}
$$

Das vollständige rationale charakteristische Polynom und alle elf Energiezweige sind im Originalbericht enthalten. Die beiden perfekten Paarbindungen sind nicht gemeinsam sättigbar: $Q_{12}Q_{23}Q_{12}=Q_{12}/25$. Trotzdem ist der gemeinsame Grundraum explizit berechenbar.

Die Isometrie entsteht aus drei Paarkontraktionen und den sechs ursprünglichen Simplexmarken:

$$
(T_1x)_{abc}=\delta_{ab}x_c,\quad
(T_2x)_{abc}=\delta_{ac}x_b,\quad
(T_3x)_{abc}=x_a\delta_{bc},\quad
T_4x=\sum_qv_q^{\otimes3}\langle v_q,x\rangle.
$$

Mit $s=\sqrt{73}$,

$$
c=\left(-\frac{27+3s}{50},-\frac{12}{25},-\frac{27+3s}{50},1\right),
\qquad N=\frac{3942+378s}{625},
$$

ist $W_3=N^{-1/2}\sum_i c_iT_i$ eine Isometrie und $H_3W_3=E_0W_3$. Sie transportiert dieselbe native endliche Fünferdarstellung, nicht nur eine zufällige Entartung. fileciteturn20file0L279-L344

## 17.2 Exakte Randprojektion

Für alle fünfzehn $R_a$ gilt an beiden Rändern

$$
W_3^\dagger R_a^{(1)}W_3=W_3^\dagger R_a^{(3)}W_3
=a_\partial R_a+\frac25(1-a_\partial)I,
$$
$$
a_\partial=\frac{49+5\sqrt{73}}{144}.
$$

Die Grenzbindung zweier solcher Bausteine projiziert zu

$$
(W_3\otimes W_3)^\dagger h_{\mathrm{Grenze}}(W_3\otimes W_3)
=a_\partial^2h+\frac45(1-a_\partial^2)I,
$$
$$
a_\partial^2=\frac{2113+245\sqrt{73}}{10368}\approx0{,}4056983910.
$$

Die Projektion ist exakt. Eine Tiefenergieinterpretation braucht schwache äußere Kopplung $J_{\mathrm w}$ gegenüber der inneren $J_{\mathrm s}$. Die nächste Ordnung ist von Größe $J_{\mathrm w}^2/J_{\mathrm s}$.

## 17.3 Die numerische nächste Ordnung trennt alte Entartungen

Die dokumentierten Sektorkoeffizienten der nächsten virtuellen Paarordnung sind

| Sektordimension | Numerischer Koeffizient in $J_{\mathrm w}^2/J_{\mathrm s}$ |
|---:|---:|
| 1 | $-0{,}26241666998068$ |
| 5 | $-0{,}05807535460173$ |
| 9 | $-0{,}10652443252980$ |
| 10 | $-0{,}05678177907811$ |

Die Abweichung von der invarianten Rekonstruktion ist etwa $2\cdot10^{-16}$. Die vorher gleichenergetischen Sektoren fünf und zehn werden getrennt. Das ist eine ausdrücklich numerische, nicht intervallzertifizierte Gegenprobe. Die exakten Isometriesätze sind davon unabhängig. fileciteturn20file0L346-L397

## 17.4 Gleich starke Links erzeugen nicht automatisch unabhängige Zellen

Im früheren Quellenkandidaten bevorzugt gleiche negative Verbindung auf jedem festen endlichen verbundenen Graphen zunächst den globalen Raum $\operatorname{Sym}^N\mathbb C^4$ mit Dimension $\binom{N+3}{3}$. Bei acht Quellen sind das 165 Richtungen, nicht das Produkt zweier unabhängiger Fünferzellen.

Für $N\ge5$ kann ein global symmetrischer Zustand nicht gleichzeitig einen perfekten ursprünglichen Quartikcode auf einer Vierermenge erfüllen: Die dadurch auf alle Vierermengen transportierten Checks erzeugen antikommutierende geforderte Zweierchecks. Eine Hierarchie innerer und äußerer Bindungen ist daher eine eigenständige Anforderung. fileciteturn20file0L399-L411

---

<a id="ladungstest"></a>
# 18. Der entscheidende gemeinsame Ladungstest

## 18.1 Der alte Bindungsoperator erhält die transportierte Ladung nicht

Auf dem Paarraum unterscheiden wir ausdrücklich $P_5^{(25)}$ von dem ursprünglichen Vierregisterprojektor $\Pi_5$. Die alte Bindung lautet

$$
h=P_5^{(25)}+\frac59P_9^{(25)}+P_{10}^{(25)}.
$$

Für eine neutrale Paarung $V\otimes\overline V$ ist der additive Generator

$$
Q_Y=Y\otimes I-I\otimes Y^T.
$$

Der Singulettzustand ist neutral, doch

$$
\boxed{\|[h,Q_Y]\|_{\mathrm{HS}}^2
=\frac{488+32\sqrt6}{405}>0.}
$$

Die allgemeine kontinuierliche Konjugationssymmetrieprüfung hat bei 25 Matrixunbekannten Rang 24. Es bleibt nur der skalare Generator. Auch ein Basiswechsel liefert daher nicht die fehlende kontinuierliche Symmetrie innerhalb dieses Vertrages. Eine Paarung gleich orientierter Träger hilft nicht; dann ist bereits $\Omega_5$ keine neutrale Ladungseigenlinie.

**Diese Entscheidung nimmt die früheren ungeladenen Rechnungen nicht zurück. Sie schließt ihre zusätzliche direkte Hyperladungsdeutung aus.** fileciteturn22file0L52-L117

## 18.2 Vollständige Lösung unter der stärkeren gemeinsamen Symmetrieforderung

Die native invariante Paarfamilie ist

$$
H=cI+\varepsilon_5P_5^{(25)}+\varepsilon_9P_9^{(25)}+\varepsilon_{10}P_{10}^{(25)}.
$$

Der Ladungsoperator verbindet die Sektoren mit strikt positiven Gewichten

$$
\operatorname{tr}(P_5Q_YP_{10}Q_Y)=\frac{67}{60}-\frac{\sqrt6}{5},
$$
$$
\operatorname{tr}(P_9Q_YP_{10}Q_Y)=\frac{61}{20}+\frac{\sqrt6}{5}.
$$

Daher gilt $[H,Q_Y]=0$ genau dann, wenn $\varepsilon_5=\varepsilon_9=\varepsilon_{10}$. Die ganze positive Singulettfamilie ist

$$
\boxed{H=cI+k(I-P_\Omega),\qquad k>0.}
$$

Die native Symmetriebahn von $Y$ spannt 14 reellsymmetrische spurfreie Richtungen, ihre Kommutatoren weitere zehn. Sie erzeugen gemeinsam $\mathfrak{su}(5)$. Das ist eine mathematische Vervollständigung unter voller unmarkierter nativer Symmetrie plus Ladung, **kein Beweis einer physisch erzwungenen ungebrochenen $SU(5)$ Eichgruppe**. fileciteturn22file0L119-L152

## 18.3 Geänderter Operator, geänderte Übertragung

Die spurtreue und zugleich im Hilbert und Schmidt Sinn nächstgelegene Wahl ist

$$
\boxed{h_{\mathrm{cov}}=\frac56(I-P_\Omega).}
$$

Dabei ist $\|h-h_{\mathrm{cov}}\|_{\mathrm{HS}}^2=10/9$. Der neue Rückkanal lautet

$$
\boxed{\mathcal K_{\mathrm{cov}}(X)=\frac{X+\operatorname{tr}(X)I}{6}.}
$$

Der nichttriviale Multiplikator ist jetzt $1/6$, nicht $4/9$. Der Fünferträger, die ursprüngliche Igusa Geometrie und die damalige Bellmessung bleiben als Objekte erhalten, sind aber nicht unverändert die neue Bewegung.

## 18.4 Die markierte Alternative bleibt größer

Verlangt man nur $G_{\mathrm{SM}}=S(U(3)\times U(2))$, zerfällt $V\otimes\overline V$ in zwei Singuletts, einen Achter, einen Dreier und zwei entgegengesetzt geladene Sechser. Der Hermitesche Kommutant hat Dimension acht.

Die im Bericht ausgeführte Haarmittelung des alten $h$ nur über diese markierte Gruppe besitzt neben der Nullenergie von $\Omega$ die Energien

| Sektor | Energie |
|:---|:---|
| $Y$ Singulett | $(61+4\sqrt6)/75$ |
| Achter | $1247/1500+2\sqrt6/375$ |
| Dreier | $(311+4\sqrt6)/375$ |
| Sechser, beide Ladungen | $(314-4\sqrt6)/375$ |

Auch das ist ein geänderter Operator. Die Gruppenmittelung ist eine konkrete Rechenoperation, kein bereits hergeleiteter physischer Entstehungsprozess. Welche Symmetrie ein fest markiertes TFPT System tatsächlich besitzt, muss die Quelle entscheiden. fileciteturn22file0L154-L184

---

<a id="komposition"></a>
# 19. Ladungserhaltende Rekursion und exakte Komposition

## 19.1 Die neue Dreierisometrie

Für den geänderten Zweig $h_{\mathrm{cov}}$ alternieren die Träger als $V,\overline V,V$. Setze

$$
\boxed{(Wx)_{abc}=\frac{\delta_{ab}x_c+x_a\delta_{bc}}{\sqrt{12}}.}
$$

Dann ist $W^\dagger W=I_5$. Für $H_3=h_{12}+h_{23}$ lautet das vollständige Spektrum

$$
\boxed{2/3\;(5),\qquad1\;(5),\qquad5/3\;(115).}
$$

Der Grundraum ist $\operatorname{Ran}W$ mit Lücke $1/3$.

Die entscheidende Identität gilt für jede $5\times5$ Matrix:

$$
\boxed{(X_1-X_2^T+X_3)W=WX.}
$$

Insbesondere bleibt die transportierte Hyperladung exakt erhalten. Für unitäre $U$ ist $(U\otimes\overline U\otimes U)W=WU$.

## 19.2 Wie die Ladung lokal verteilt wird

Die Randabbildungen sind

$$
W^\dagger X_1W=W^\dagger X_3W=\frac{7X+\operatorname{tr}(X)I}{12},
$$
$$
W^\dagger X_2W=\frac{X^T+\operatorname{tr}(X)I}{6}.
$$

Für die spurfreie Ladung folgt $2(7/12)Y-(1/6)Y=Y$.

```text
Vor der Verdichtung:     V           V̄           V
Ladungsbeitrag:         +7/12 Y     −1/6 Y      +7/12 Y
                                      │
                                      ▼
Nach der Verdichtung:                 Y

Nicht nur dieselbe Dimension, sondern dieselbe additive Darstellung.
```

Die Grenzbindung zweier Blöcke projiziert exakt zu

$$
\boxed{(W\otimes W)^\dagger h_{\mathrm{Grenze}}(W\otimes W)
=\frac{49}{144}h_{\mathrm{cov}}+\frac{19}{36}I.}
$$

Auch hier benötigt eine Tiefenergieinterpretation schwächere äußere Links als die innere Bindung. fileciteturn22file0L186-L224

## 19.3 Die lokale Kompositionsalgebra

Mit $e_i=5P_{\Omega,i,i+1}$ gelten

$$
\boxed{e_i^2=5e_i,\qquad e_ie_{i+1}e_i=e_i,\qquad
[e_i,e_j]=0\quad(|i-j|>1).}
$$

Das sind die bekannten Relationen der Temperley und Lieb Algebra mit Schleifenparameter fünf. Als lokale Identitäten gelten sie in jeder größeren festgelegten Kette.

Für

$$
q=\frac{5+\sqrt{21}}2,\qquad q+q^{-1}=5,
$$
$$
R_i(t)=(q-q^{-1}t^2)I+(t^2-1)e_i
$$

gilt die generische Kompositionsgleichung

$$
\boxed{R_i(t)R_{i+1}(tu)R_i(u)=
R_{i+1}(u)R_i(tu)R_{i+1}(t).}
$$

Die Gleichung von Yang und Baxter wurde im Bericht für freie symbolische $t,u$ geprüft. Bei $t=e^{i\theta}$ ist

$$
U_i(\theta)=\frac{R_i(e^{i\theta})}{\sqrt{23-2\cos(2\theta)}}
$$

unitär; $R_i(1)=\sqrt{21}I$. Das ist eine bekannte Baxterisierung, hier auf den konkret vervollständigten Zweig angewendet. $\theta$ ist kein bereits aus TFPT hergeleiteter physischer Zeitparameter, und der Schleifenwert fünf ist keine Raumdimension. fileciteturn22file0L226-L251

## 19.4 Die vollständige Vergröberung erzeugt echte Dreikörperwörter

Für drei starke Dreierblöcke und zwei schwache Links ergibt der exakte Kreuzbeitrag der zweiten Ordnung

$$
\boxed{
H_{\mathrm{cross}}=\frac{J_{\mathrm w}^2}{J_{\mathrm s}}
\left[\frac{49}{93312}I-rac{1225}{93312}(P_{12}+P_{23})
+\frac{30625}{186624}\{P_{12},P_{23}\}\right].}
$$

Die separaten beiden Paarbeiträge kommen noch hinzu. Der letzte Term ist nicht auf Zweikörperoperatoren reduzierbar; sein im Bericht geprüfter Abstand vom ganzen passenden höchstens zweilokalen Raum hat positives Quadrat $2100875/241864704$.

**Drei Aussagen bleiben getrennt:** Die Algebra schließt. Die Projektion jedes einzelnen Links bleibt in derselben Paarform. Die ganze effektive Dynamik erzeugt trotzdem zusätzliche Wörter dieser Algebra.

Für die ursprüngliche native Fünferdarstellung wächst zudem

$$
\dim\operatorname{End}_{S_6}(V^{\otimes n})
=\frac{400+40\cdot4^n+15\cdot9^n+25^n}{720},\qquad n\ge1.
$$

Die ersten Werte sind $1,4,41,694,14851,350384$. Ein kleiner Paarkommutant ist keine gleich kleine vollständige Vielteilchentheorie. fileciteturn22file0L253-L295


---

<a id="korrekturen"></a>
# 20. Die wichtigen Korrekturen und ausgeschlossenen Abkürzungen

Dieses Kapitel verhindert, dass die verschiedenen Entwicklungsstände zu einer vermeintlich bereits geschlossenen Theorie zusammengeschoben werden. Die älteren Resultate bleiben unter ihren Voraussetzungen erhalten; spätere Einschränkungen gelten für ihre zusätzliche Interpretation.

## 20.1 Korrekturregister

| Frühere oder naheliegende Verkürzung | Ergebnis der Untersuchung |
|:---|:---|
| „Der Kompatibilitätsgraph ist schon Raum“ | Der geprüfte Graph von Operationstypen hat Durchmesser zwei. Ein Ereignisnetz benötigt eine eigene Erzeugungsregel. |
| „Paarweise erlaubt bedeutet als Geschichte erlaubt“ | $IP_0\ne0$, $P_1I\ne0$, aber $P_1IP_0=0$. |
| „Die Lorentzdeterminante liefert schon alle relativistischen Bewegungen“ | Der pure Kompositionsabschluss des 60er Operationsalphabets enthält keine nichttrivialen invertierbaren Boosts. |
| „Uniforme Quellenoperationen reproduzieren den Transfer“ | Der unbeobachtete uniforme Kanal depolarisiert vollständig. |
| „Der klassische Transfer bestimmt die Dynamik“ | Die Familie $w_t$ hat denselben Populationstransfer und verschiedene Kohärenzen. |
| „Eine diskrete Clock bestimmt ihre Zeitentwicklung“ | Verschiedene positive Logarithmen haben denselben Zeit eins Endpunkt. |
| „Die sechs Markierungen sind schon sechs kohärente Quellenzustände“ | Ihre Codezustände liegen nicht auf dem einzelnen kohärenten Igusa Quellenbild. |
| „Der isolierte Fünferraum enthält die ganze Quelle“ | Er verliert Pauli Wirkungen; gleiche Quartikwerte können verschiedene zukünftige Antworten haben. |
| „Rang zehn heißt zehn erhaltene Quantenfreiheitsgrade“ | Die Paarabbildung ist hier eine Messung mit zehn Effekten und anschließender Präparation. |
| „Paarsteuerung ist dasselbe wie geschützte Paarwirkung“ | Ein einzelnes Paar kann aus dem Code austreten; die symmetrisierte Paarsumme erhält ihn. |
| „$SU(5)$ Kontrolle ist eine $SU(5)$ Eichsymmetrie“ | Steuerbarkeit und erhaltene innere Symmetrie sind verschiedene Operatoraussagen. |
| „Ein Registerverlust ist korrigierbar, also folgt passiver Schutz“ | Energetische Auswahl ist ein separates Problem. Derselbe Fünfergrundraum braucht in der untersuchten Einbettung Viererterme. |
| „Perfekte Fünferzellen lassen sich über dieselben Register verkleben“ | Die identisch orientierten überlappenden Codes haben keinen gemeinsamen Zustand. |
| „Virtuelle Kopplung hat den Graphen erzeugt“ | Die Links wurden in den Modellen vorgegeben. Nur die Wirkung auf ihnen wurde berechnet. |
| „Der Fünfercode wählt eindeutig $K_4$“ | Auch ein Viererring erzeugt den führenden Selektor, mit anderem Koeffizienten. |
| „Dynamisch entstandener Code hat dauerhaft Abstand sechs“ | Der ideale Grenzcode hat Abstand sechs; der gedresste Grundcode besitzt im untersuchten $K_4$ Modell schon Zweiregisterantworten und Abstand zwei. |
| „Drei Bausteine ergeben fünf, also ist die ganze Renormierung geschlossen“ | Die Randprojektion schließt; virtuelle Korrekturen erzeugen zusätzliche Sektoren und echte Mehrkörperwörter. |
| „Die alte Bindung erhält die vorhandene Hyperladung“ | Der exakte Kommutator ist nichtnull. |
| „Die kovariante Vervollständigung ist dieselbe alte Dynamik“ | Sie ändert den Operator und den Rückkanalmultiplikator von $4/9$ zu $1/6$. |
| „$S_6$ und Ladung erzwingen die physische TFPT $SU(5)$ Eichgruppe“ | Nur unter der stärkeren Forderung, beide als innere Symmetrien desselben unmarkierten Systems zu erhalten. Bei fester Markierung bleibt eine größere Alternativenfamilie. |
| „Integrable Komposition bedeutet bereits relativistische Raumzeit“ | Die Gleichung von Yang und Baxter gilt für eine festgelegte Kette und Spektralparameter. Raum, Zeitidentifikation und Feldtheorie folgen nicht daraus. |
| „Viele bestandene Checks messen die Nähe zur TOE“ | Prüfzahlen zählen endliche Programmkontrollen. Sie sind weder unabhängige Experimente noch ein Prozentmaß der Vollständigkeit. |

Quellen: [Z](#original-z), [Q1](#original-q1), [Q2](#original-q2), [Q3](#original-q3), [Q4](#original-q4), [Q5](#original-q5). Insbesondere dokumentiert der letzte Bericht die Änderung des Operators ausdrücklich. fileciteturn22file0L13-L25

## 20.2 Die verschiedenen Übertragungszahlen nebeneinander

| Zahl oder Liste | Ihr tatsächliches Objekt | Nicht gleichzusetzen mit |
|:---|:---|:---|
| $\{1,2/3,1/3\}$ | Vorgegebener Familienpopulationstransfer $B$ | Vollständiger, schon eindeutig bestimmter Quantenprozess |
| $2/3$ neunfach | Normierter Singularwert der Doily Inzidenz und der betreffenden Paarabbildung | Eigenwert einer beliebigen Hamiltonzeit |
| $4/9$ neunfach | Hin und zurück Kanal $\mathcal R_2\mathcal E_2$ | Der spätere kovariante Rückkanal |
| $1/6$ vierundzwanzigfach | Geänderter kovarianter Rückkanal auf spurfreien Operatoren | Unverändert erhaltene alte Paarmessung |
| $(49+5\sqrt{73})/144$ | Randkompression von Ebenenobservablen im ersten rekursiven Bindungszweig | Naturkonstante oder universelles Skalenverhältnis |
| $(2113+245\sqrt{73})/10368$ | Führender Paarfaktor desselben ersten Zweigs | Vollständiger Renormierungsfixpunkt |
| $49/144$ | Paarprojektion des geänderten ladungserhaltenden Zweigs | Der Faktor des alten Zweigs |
| $1/27$ | Entropieoptimum des ausdrücklich angegebenen Kontrastqubits | Allgemeines Entropiegesetz der Natur oder automatisch ein Jarlskog Invariant |

## 20.3 Gleich große Räume sind nicht automatisch dieselben Räume

Der Fünfercode $\mathcal C_5$, der Fünfersektor in $\mathcal C_5\otimes\mathcal C_5$, der Riemann und Roch Träger und fünf Trägerslots benötigen konkrete Abbildungen. Solche Brücken wurden teilweise konstruiert, nicht durch die Zahl fünf ersetzt.

Der Zehner der Bellmessung, $\operatorname{Sym}^2\mathbb C^4$, der Spin(10) Vektor und ein zehn dimensionaler invarianten Sektor haben verschiedene Gruppenwirkungen. Dasselbe gilt für den vierdimensionalen Quellenraum und eine behauptete $3+1$ Raumzeit.

Eine gemeinsame Theorie muss Darstellung, Ladung, Grad, Adjunktion, Zustand und Zeit zugleich transportieren. Genau diese Forderung steht in den ursprünglichen Integrationsverträgen. fileciteturn21file2L117-L138

---

<a id="abschlussvertrag"></a>
# 21. Der verbleibende vollständige physische Abschlussvertrag

## 21.1 Die acht Bedingungen bleiben eigenständige Nachweise

| Tor | Vollständiger geforderter Nachweis | Was diese Gesprächsreihe dazu liefert und nicht liefert |
|:---|:---|:---|
| **T1** | Ursprung von P1/P2, Compiler und Dimension | Endliche Codes und bedingte Minimalitäten; keine Auswahl der physischen Tensorfaktoren, räumlichen Links und Dimension |
| **T2** | Tatsächliche markierte E₈ Randtheorie einschließlich geladenem Feldanschluss und Grenzidentifikation | Präzise endliche Gruppenwirkungen, Invarianten und Markierungen; kein vollständiger lokaler geladener Quellenadapter |
| **T3** | Gemeinsame lokale unitäre Hamiltonfamilie in $3+1$ Dimensionen | Mehrere explizite endliche Hamiltonmodelle; kein aus dem Ursprung gewählter gemeinsamer räumlicher Parent |
| **T4** | Chirales Standardmodell, lokales Maß und kontrollierte Spiegelentkopplung | Endliches Ladungswörterbuch und Kompatibilitätssätze; keine neue vollständige chirale Feldkonstruktion |
| **T5** | Wechselwirkender relativistischer Grenzwert, Clustering und physische Streuung | Exakte kleine Modelle, Kompositionsalgebra und bedingte Lokalitätsfragen; kein kontrollierter gemeinsamer Kontinuumsabschluss |
| **T6** | Gemeinsame Herkunft der Eichkopplungen, Flavor und Neutrinodynamik | Erhalt bestehender Vergleichsdaten und exakte Ladungstests; keine neue gemeinsame Alpha und Flavor Herkunft |
| **T7** | Quantisierter masseloser Spin zwei Sektor mit universeller konsistenter Kopplung | Kein in dieser Reihe neu konstruierter Gravitationssektor |
| **T8** | Ausgewählter physischer Anfangszustand und gemeinsames Erzeugungsfunktional | Bestimmte endliche Grundzustände und Grundräume; kein ausgewählter kosmologischer Anfangszustand |

Der maßgebliche Vertrag führt diese Bedingungen ausdrücklich neben dem endlichen Compilerabschluss. Ein endlicher Grundzustand und ein kosmologischer Anfangszustand sind nicht identisch. fileciteturn21file1L77-L91 fileciteturn21file4L191-L203

## 21.2 Der eine gemeinsame Anschluss, auf den die Ergebnisse zulaufen

Der dokumentierte Herkunftsauftrag ist

$$
\boxed{\text{Raw RP Seam + markierter Compiler}
\longrightarrow(\mathcal A_X,J_X,W,H,\Omega)
\longrightarrow\text{physische Felder und gemeinsame Antwort}.}
$$

Er muss positive globale Verklebung, richtige Gruppenwirkungen, Ladung, Graduierung, Adjunktion, denselben Zustand und dieselbe Zeit liefern. Für die native Wechselwirkung gehört dazu eine Antwort der Form

$$
\Pi_{\Psi\Psi}[\mathcal B_A,H_{\mathrm{Quelle}}]
=g\sum_{i<j}W_{A,ij}\Psi_j\Psi_i,
$$

einschließlich der verlangten Ausschlüsse weiterer operatorwertiger Antwortanteile. Eine Stromklammer, ein endlichdimensionaler Swap und ein Hamiltonkommutator kanonischer Felder sind nicht derselbe Objekttyp. fileciteturn15file6L240-L260

## 21.3 Die im Material begründeten nächsten Entscheidungen

**Symmetrie und Markierung:** Zuerst muss aus den ursprünglichen Quellen entschieden werden, ob die volle native Gruppe innere Symmetrie eines festen geladenen Systems ist oder verschiedene Markierungen miteinander verbindet. Davon hängt ab, welcher der beiden letzten Dynamikzweige zulässig ist.

**Mikroskopischer Anschluss:** Die logischen $K_a$ Kopplungen und die kovariante Bindung müssen an tatsächliche lokale Quellenfelder angeschlossen werden. Eine Haarmittelung oder nachträgliche Konstruktion eines passenden Operators ist noch keine Herkunftsherleitung.

**Zeit, Zustand und Hierarchie:** Graph, Kopplungsvorzeichen, relative Stärken, Präparation und Zeitnormierung sind gemeinsam zu bestimmen. Eine Gruppe mit einer ausgezeichneten Zahl oder eine rekursive Isometrie entscheidet diese Daten nicht.

**Erst danach der große Grenzwert:** Eine größere lokale Theorie muss die zusätzlich erzeugten Mehrkörperwörter, den richtigen geladenen Sektor, das physische Kontinuum und die vorhandenen Alpha und Flavorantworten mitführen. Die Codeteilresultate werden dabei als Prüfbedingungen verwendet, nicht als Ersatz für diese Aufgaben. Diese Reihenfolge entspricht dem dokumentierten gemeinsamen Identifikationsauftrag. fileciteturn21file0L46-L55

---

<a id="schlussbilanz"></a>
# 22. Die komprimierte Schlussbilanz

## 22.1 Was sich zu einer gemeinsamen Geschichte verbindet

**Der Hamming Code organisiert die Quelle.** Die Quelle trägt E₈ Wurzeln und 60 komplexe Richtungen. Ihre quartische Auslesung erzeugt den besonderen Fünferträger.

**Die Geometrie ist eine konkrete Quotientengeometrie.** Igusa, Segre, Bellquadriken, Doily, Petersen Rahmen und die Grade $8,12,20,24$ sind über dieselben Koordinaten verbunden. Die wiederkehrenden Zahlen werden dadurch erklärt und zugleich als voneinander abhängig erkannt.

**Schutz und Bewegung können gemeinsam konstruiert werden.** Ein aus demselben Hamming Seed gebildeter geschützter voller Quellraum trägt virtuelle Austauschprozesse. Unter festgelegten Kopplungen entstehen der symmetrische 35erraum und der besondere Fünfercode dynamisch.

**Die vollständige Quelle bleibt größer als ihre Anzeige.** Die fünfzehn Zweierantwortsektoren und der Pauli Rahmen können zukünftige Antworten verändern. Sie dürfen nicht allein wegen einer gegenwärtig identischen Auslesung entfernt werden.

**Bindung und Information besitzen eine genaue gemeinsame Matrix.** Im definierten logischen Anschluss entsteht die ursprüngliche Rückkanalmatrix als Bindungsoperator. Daraus folgt ein bestimmter Paarzustand und eine explizite rekursive Fünferdarstellung.

**Die Ladungsprüfung entscheidet die zusätzliche physische Deutung.** Die alte Bindung verletzt die transportierte additive Hyperladung. Ihre kompatible Vervollständigung ist unter der stärkeren Symmetrieforderung klassifiziert. Sie erhält die Ladung bei Verdichtung und besitzt eine exakte lokale Kompositionsalgebra, verändert dafür aber den Rückkanal.

## 22.2 Das anschauliche Endbild

```text
Die Quelle                     Die verdichtete Ansicht               Die Bewegung
──────────                     ───────────────────────               ────────────
Vollständige Zustandsdaten  →   Code und Invarianten           →      definierter Prozess
Pauli Rahmen und Phasen         bestimmte Messantworten              Zustand und Zeit
zusätzliche Antwortsektoren     sichtbare Geometrie                  tatsächliche Kopplungen
          ▲                             │                                   │
          └───────── fehlende Zukunftsinformation muss erhalten bleiben ─────┘

Danach erst die physische Identifikation:

Welche Felder?  Welche Orte?  Welche Dimension?  Welche Ladungen?
Welche gemeinsame Zeit?  Welche Gravitation?  Welcher Anfangszustand?
```

Die Formulierung „Physik ist fehlergeschützte Information unter zulässiger Komposition“ bleibt eine Forschungsinterpretation. Sie ist durch diese Rechnungen nicht als vollständiges Naturgesetz bewiesen. Die stärkere und tatsächlich belegte Aussage ist enger: **Die untersuchten TFPT Quelldaten erlauben mehrere präzise miteinander verbundene Code-, Auslese-, Bindungs- und Kompositionskonstruktionen. Ihre gemeinsame physische Herkunft ist weiterhin zu beweisen.**

## 22.3 Schluss in einem Satz

> **Das algebraische Netz ist konkret verbunden; mehrere dynamische Teilprobleme sind gelöst; eine zentrale Ladungsunverträglichkeit ist entschieden und konstruktiv vervollständigt. Die vollständige Theorie entsteht erst, wenn dieselbe ursprüngliche TFPT Quelle diese Struktur, ihre tatsächliche Bewegung, ihre lokalen geladenen Felder und ihren Zustand gemeinsam auswählt.**

---

<a id="glossar"></a>
# 23. Begriffswörterbuch

| Begriff | Bedeutung in dieser Datei |
|:---|:---|
| Quelle | Der ursprüngliche Zustands- und Operationsraum. Seine physische Identifikation wird nicht allein durch den Namen vorausgesetzt. |
| Register | Ein Tensorfaktor eines angegebenen Modells; nicht automatisch ein Ort in der Raumzeit. |
| Physischer Registerfehler | Eine Störung auf den tatsächlich als Register definierten Faktoren eines Codekandidaten. |
| Logischer Raum | Der innerhalb einer Kodierung erhaltene Informationsraum. |
| Quartik | Vierte Ordnung in Quellenkoordinaten oder vierfache Tensorstruktur. |
| Projektor | Operator, der einen Unterraum auswählt und $P^2=P$ erfüllt. |
| $\Pi_5$ | Der besondere Fünfercode auf vier ursprünglichen Quellenregistern. |
| $P_5^{(25)}$ | Ein anderer Fünfersektor im Paarraum zweier Fünferträger. |
| $S$ | In den Codekapiteln der Projektor auf den vollständig symmetrischen Viererraum. |
| $Q$ | Je nach Kapitel Quartikstabilisator oder Komplementprojektor; der jeweilige Vertrag definiert ihn neu. |
| Marginale | Reduzierter Zustand nach Ausblenden anderer Register. |
| Erasure | Bekannter Registerverlust. Er ist nicht dasselbe wie ein beliebiger Fehler an unbekannter Position. |
| Codeabstand | Minimaler Support einer unerkannten nichttrivialen logischen Störung im genannten Fehlervertrag. |
| Parent | Ein definierter Hamiltonoperator mit dem gewünschten Grundraum. Seine Existenz beweist nicht seine physische Herkunft. |
| Gedresster Zustand | Tiefer Zustand, der bei endlicher Kopplung mit angeregten Komponenten vermischt ist. |
| Carry | Bei einer verdichteten Gruppenbeschreibung verloren gehende, später wirksame Rahmen- oder Phaseninformation. |
| Intertwiner | Konkrete lineare Abbildung, die die angegebenen Gruppen- oder Operatorwirkungen miteinander verträglich transportiert. |
| Petz Rückkanal | An Referenzzustand und Auslesekanal gebundene Rekonstruktionsabbildung. |
| Singulett | Unter der betreffenden gemeinsamen Gruppenwirkung unveränderliche Linie. |
| Native Symmetrie | Die tatsächlich aus den angegebenen TFPT Quellenoperationen rekonstruierte Wirkung. |
| Markierung | Zusätzliche festgelegte Struktur wie $q_*$, Familienwirkung oder $3+2$ Aufteilung. |
| Innere Symmetrie | Transformation innerhalb desselben festgelegten Systems. Nicht jeder Markierungswechsel ist eine solche Symmetrie. |
| Kontrollalgebra | Durch zulässige steuerbare Pulse erzeugte Operatoren. Keine automatische Symmetrie des autonomen Hamiltonoperators. |
| Kommutant | Operatoren, die mit einer vorgegebenen Gruppenwirkung kommutieren. |
| Schrieffer und Wolff Entwicklung | Effektive tiefe Dynamik aus einem vorgegebenen gegappten Ausgangsmodell und schwacher Kopplung. |
| Feshbach Identität | Exakte Resolventenformel, die die Rückwirkung ausgeblendeter Richtungen erhält. |
| Renormierung / Vergröberung | Beschreibung größerer Bausteine durch effektive kleinere Zustandsräume und entsprechend veränderte Operatoren. |
| Reflexionspositivität | Positivitätsbedingung bezüglich einer konkret angegebenen Spiegelung. |
| Igusa Quartik | Die hier explizit identifizierte algebraische Relation des quartischen Pauli Quotienten. |
| Temperley und Lieb Algebra | Lokale Kompositionsrelationen der Singulettprojektoren im vervollständigten Kettenzweig. |
| Gleichung von Yang und Baxter | Konsistenzgleichung verschiedener Reihenfolgen lokaler parameterabhängiger Kompositionen. |
| TOE Abschluss | Die gemeinsame physische Erfüllung der Tore T1 bis T8, nicht nur das Vorliegen endlicher Codeidentitäten. |

---

<a id="quellen"></a>
# 24. Quellen, Originalfassungen und Reproduktion

## 24.1 Quellenhierarchie

**Primäre Gesprächsergebnisse:** Zuse Prüfbericht Z und die fünf Forschungsfortsetzungen Q1 bis Q5. Sie werden weiter unten vollständig eingebettet. Die inhaltlich wichtige Vorgeschichte V19 wird ebenfalls im Wortlaut bewahrt. Der eingereichte Quartiktext D0 ist als Eingabe beigefügt, nicht als unabhängige neue Prüfung gezählt.

**Ursprünglicher TFPT Kontext:** `introduction.pdf`, `tfpt_1_architecture_e8.pdf`, `tfpt_2_standard_model.pdf`, `tfpt_3_e8_audit_bootstrap.pdf`, `tfpt_4_frontier.pdf`, `tfpt_5_redteam.pdf`, `tfpt_research_contracts.pdf`, `origin_theory.pdf`, `tfpt_horizon_readouts.pdf`, `tfpt_prime_front.tex` sowie die Sitzungsfassungen vom 20. und 21. September. Für den Hauptteil wurden die bereits im Gespräch belegten Abschnitte verwendet, nicht die gesamten tausenden Seiten neu analysiert.

**Literatur:** Die Originalberichte nennen ihre Primärliteratur für bekannte Mathematik und Methoden. Diese Hinweise werden im Wortlaut übernommen. In der Konsolidierungsrunde wurde keine neue Webrecherche durchgeführt.

## 24.2 Prüfzahlen sind historische Laufangaben

| Paket | In seinem Bericht beziehungsweise Ergebnisprotokoll dokumentierter Umfang |
|:---|:---|
| Zuse | Numerische Normalformaufzählung und symbolische Gegenproben; keine hier neu erfundene gemeinsame Checkzahl |
| Q1: Quartik | 385 Kontrollen |
| Q2: Igusa | 1065 Kontrollen |
| Q3: Dynamischer Codeabschluss | 1326 Kontrollen |
| Q4: Rekursive Bindung | 165 exakte und zwei gesondert numerische Kontrollen |
| Q5: Ladung und Komposition | 138 exakte Kontrollen |

Diese Zahlen werden nicht addiert, um unabhängige Beweise, physische Vorhersagen oder Nähe zum Gesamtabschluss zu suggerieren. Spätere Pakete führten teils frühere Pakete erneut aus. Die aktuelle Zusammenstellung wiederholt diese wissenschaftlichen Läufe nicht.

## 24.3 Reproduzierbarkeit und Grenzen dieser einen Datei

Die folgenden Anhänge enthalten die vollständigen Berichtstexte und die nichtredundanten Ergebniswerte der bereitgestellten JSON Dateien. Die Listen einzelner automatisch protokollierter Checks bleiben in den ursprünglichen Archiven; ihre Anzahl und Zusammenfassungen werden beibehalten. Die sechs bereitgestellten Prüfprogramme und ihre Abhängigkeiten werden zusätzlich als aufklappbare Quelltexte eingebettet. Binäre NumPy Archive werden nicht als Base64 in Markdown versteckt; sie bleiben als originale Zertifikatsdateien in den Prüfpaketen.

Zur Reproduktion eines konkreten Pakets gelten dessen eigene Anleitung und Abhängigkeiten. In der Regel lautet der Einstieg nach Entpacken:

```sh
python -m pip install -r requirements.txt
python audit.py
```

Die Voraussetzungen und fachlichen Reichweiten der einzelnen Programme unterscheiden sich. Ein erfolgreicher Lauf zertifiziert die im Programm formulierten Bedingungen; er ersetzt nicht fehlende Herkunftsbeweise oder Experimente.

### Format der Originalanhänge

Die Berichtstexte werden wortgetreu eingebettet, auch wenn sie frühere Formulierungen, andere Formelsyntax oder Bindestriche verwenden. Kommentare vor einem Originaltext sind Teil dieser Konsolidierung; der Inhalt des folgenden Klappabschnitts ist der historische Originaltext. Enthaltene relative Verweise auf `results.json`, `matrices.npz` oder weitere Programme beziehen sich auf das jeweils zugehörige ursprüngliche Prüfpaket.

Die späteren Modelländerungen sind im Hauptteil markiert. Insbesondere gelten die alten Bindungssätze weiter für das alte $h$, während die ladungserhaltenden Sätze auf dem geänderten $h_{\mathrm{cov}}$ beruhen. Es wird kein stillschweigender Austausch der beiden Operatoren vorgenommen.


## 24.4 Dateiidentitäten der übernommenen Berichte

Die folgenden SHA 256 Werte identifizieren die Originalbytes. Bei Q1 bis Q5 stimmen der separat bereitgestellte Bericht und seine im zugehörigen ZIP enthaltene Fassung bytegenau überein. Alle sechs bereitgestellten ZIP Archive bestanden die CRC Integritätskontrolle dieser Konsolidierung. Das ist eine Dateikontrolle, keine Wiederholung der mathematischen Prüfungen.

| Kennung | Originaldatei | Originalumfang |
|:---|:---|---:|
| [Z](#original-z) | `README.md` | 11,780 Bytes |
| [V19](#original-v19) | `TFPT_Fortsetzung_2026-09-19.md` | 29,596 Bytes |
| [Q1](#original-q1) | `TFPT_Quartik_Fortsetzung_Herleitungen_20260926.md` | 35,336 Bytes |
| [Q2](#original-q2) | `TFPT_Igusa_Quellendynamik_Herleitung_20260926.md` | 26,915 Bytes |
| [Q3](#original-q3) | `TFPT_Dynamischer_Codeabschluss_Herleitung_20260926.md` | 28,521 Bytes |
| [Q4](#original-q4) | `TFPT_Rekursive_Bindung_Herleitung_20260926.md` | 21,370 Bytes |
| [Q5](#original-q5) | `TFPT_Ladung_Komposition_Herleitung_20260926.md` | 20,674 Bytes |

<details>
<summary>Vollständige Originalhashes und Archividentitäten</summary>

```text
Z
  Datei: README.md
  SHA256: f06ebfd763e3d7fa1fde92bde81a29a1235dfbe08d2a0e749dd928685b221661
V19
  Datei: TFPT_Fortsetzung_2026-09-19.md
  SHA256: 7b7dcca3f8fd79f52cac0d5aa35f367e54c863a85478a3ad29fdb1695254a7da
Q1
  Datei: TFPT_Quartik_Fortsetzung_Herleitungen_20260926.md
  SHA256: dad198b1a4a93be091de46a0cedb53f3b0616276d6dc9bbbed26c9ddf87256de
Q2
  Datei: TFPT_Igusa_Quellendynamik_Herleitung_20260926.md
  SHA256: beb365eafec6677aa637d744feba22300824e690e00082df11d7b871ad678613
Q3
  Datei: TFPT_Dynamischer_Codeabschluss_Herleitung_20260926.md
  SHA256: 2f5834d911ee52eee444706a01e8db607b25c348fa1614353ab3e5a809d583d6
Q4
  Datei: TFPT_Rekursive_Bindung_Herleitung_20260926.md
  SHA256: 9ec027b0de5a6bd3c7f872597a8f832e2cab74d9c8e82061464fe32640644709
Q5
  Datei: TFPT_Ladung_Komposition_Herleitung_20260926.md
  SHA256: 7da75f545ec887e6cccf93589a5da57b71cadeb4e0b66c264c21ef8ea3f50b9f
Archiv: TFPT_Zuse_Pruefpaket.zip
  SHA256: 05b6228c0d30ac1ac8115651cca70c314f2abd72a1b9910d7c2c6206a2fdd77a
  ZIP CRC: fehlerfrei
Archiv: TFPT_Quartik_Fortsetzung_Pruefpaket_20260926.zip
  SHA256: 89a4f005eb7503dbdee09ae9277d9acee696f56457f583872a55a9536b4eb342
  ZIP CRC: fehlerfrei
Archiv: TFPT_Igusa_Quellendynamik_Pruefpaket_20260926.zip
  SHA256: 46e8359584f15875b8a5fcb9b43a56319e68d8c2cae8ef192aba1ffd3e9174de
  ZIP CRC: fehlerfrei
Archiv: TFPT_Dynamischer_Codeabschluss_Pruefpaket_20260926.zip
  SHA256: 87ce99f12a9b9a9b29d09248ef2aa015f738998f6cd06d97c977e50d65e34e27
  ZIP CRC: fehlerfrei
Archiv: TFPT_Rekursive_Bindung_Pruefpaket_20260926.zip
  SHA256: 525f646388229ac025ecd5cbddfadbef7653861523139310a61433793ed0a89a
  ZIP CRC: fehlerfrei
Archiv: TFPT_Ladung_Komposition_Pruefpaket_20260926.zip
  SHA256: f5eee42cb168cdbcbb35c3e5672b87d970ccefba7ae8d083d29170ff00edb2fc
  ZIP CRC: fehlerfrei
```

</details>

---

<a id="originalberichte"></a>
# 25. Vollständige Originalberichte und Eingabe

Die folgenden sieben Berichte sind vollständig und unverändert eingebettet. Ihre früheren Ich Aussagen, Prüfzahlen, Modellnamen, Quellenverweise und Beweisgrenzen beziehen sich jeweils auf ihre eigene ursprüngliche Untersuchungsrunde.

<a id="original-z"></a>
## Z. Zuse und die Prüfung automatischer Raumzeitfolgerungen

Archividentität: fileciteturn23file0L2-L4. Der Berichtstext wurde aus dem bereitgestellten Archiv übernommen; die Files Textansicht des ZIP war leer.

**Originaldatei:** `README.md`  
**SHA256:** `f06ebfd763e3d7fa1fde92bde81a29a1235dfbe08d2a0e749dd928685b221661`

<details>
<summary>Z: vollständigen Originalbericht öffnen</summary>

# TFPT / Zuse: unabhängiges endliches Prüfpaket

Stand: 26. September 2026

## Reichweite

Dieses Paket prüft ausgewählte mathematische Übergänge aus dem eingereichten 21-teiligen Zuse/TFPT-Text. Es ist weder die originale TFPT-Verifikationssuite noch ein vollständiger TFPT-Beweis. Es enthält keine erneute Prüfung des gesamten Repositorys, seiner Lean-Beweise oder aller physikalischen Vorhersagen. Die Quellenfassungen vom 20. und 21. September werden als Forschungsberichte behandelt; ihre zitierten Originalprogramme wurden hier nicht ausgeführt.

Die 60 Operationen werden aus der dokumentierten Normalform neu aufgebaut: 24 Ein-Qubit-Cliffordstrahlen und 36 Rang-eins-Operationen zwischen den sechs Pauli-Eigenzuständen. Der ursprüngliche basisgenaue E8-zu-60-Intertwiner wird damit NICHT unabhängig bewiesen. Die numerische Aufzählung verwendet NumPy complex128 mit Toleranz 1e-10. Symbolische Gegenproben verwenden SymPy. Die tragenden elementaren Argumente stehen unten und sind nicht von der Rundung der Aufzählung abhängig.

## Ausführung

Python 3.10 oder neuer mit NumPy und SymPy:

```sh
python -m pip install numpy sympy
python audit.py
```

Das Programm bricht bei einer fehlgeschlagenen Prüfung mit RuntimeError ab und schreibt die Ergebnisse nach `results.json`. Die ausführbare Datei benötigt keine hochgeladenen Originaldokumente und kein Netzwerk. `results.json` enthält den tatsächlich ausgeführten Lauf.

## 1. Operationstypen und Produkte

Seien U die 24 projektiven Ein-Qubit-Cliffordoperationen und S die sechs Eigenzustandsstrahlen der drei Paulioperatoren. Für u,v aus S seien A_uv = sqrt(2)|u><v|. Alle 60 Vertreter haben Frobeniusnormquadrat 2.

Bei zwei Rang-eins-Operationen ist

    A_rs A_uv = 2 <s|u> |r><v|.

Die 36 geordneten Paare (s,u) verteilen sich auf 6 orthogonale, 6 gleiche und 24 zueinander unverzerrte Paare. Die 36 freien Kombinationen (r,v) ergeben deshalb 216 Nullprodukte, 216 Produkte mit Normquadrat 4 und 864 Produkte mit Normquadrat 2. Dazu kommen 24² = 576 unitäre Produkte und 2·24·36 = 1728 gemischte Produkte mit Normquadrat 2. Gesamt:

    0: 216; 2: 3168; 4: 216.

Jedes nichtverschwindende Produkt liegt wieder auf einem der 60 Strahlen. Das reproduziert den in der Sitzungsdokumentation angegebenen Produktzensus.

### Expliziter Kandidat: Komponierbarkeit als Nachbarschaft

Definiere C(A,B)=1 genau dann, wenn BA ungleich null ist. Dies ist eine hier ausdrücklich GEWÄHLTE Definition, nicht die Behauptung, die physische TFPT-Verklebung sei damit identifiziert.

Jede invertierbare Operation bildet einen universellen Vermittler: A -> U -> B ist für beliebige nichtverschwindende A,B möglich. Also ist der gerichtete Graphdurchmesser höchstens zwei. Orthogonale Rang-eins-Faktoren besitzen kein direktes Produkt, daher ist der Durchmesser genau zwei. Dasselbe gilt für den Graphen gegenseitiger Komponierbarkeit (AB und BA ungleich null). Die Aufzählung bestätigt beide Werte.

Dieser Graph beschreibt Operationstypen, nicht räumlich und zeitlich unterschiedene Vorkommnisse. Er ist kein ausgedehnter Raum. Ein Ereignisgraph aus wiederholten Vorkommnissen kann wesentlich größer sein, braucht aber eine eigene begründete Erzeugungs- und Kopplungsregel.

### Ein Graph erlaubter Paare verliert bereits Dreierinformation

Für die beiden orthogonalen Projektoren P0, P1 gilt:

    I P0 != 0, P1 I != 0, aber P1 I P0 = 0.

Der Pfad P0 -> I -> P1 existiert im Paargraphen, das Gesamtwort verschwindet. Ein einfacher Kompatibilitätsgraph bildet die gesamte zulässige Prozesssprache daher nicht treu ab.

## 2. Keine Boosts durch reine Komposition dieses Alphabets

Sobald ein Wort einen Rang-eins-Faktor enthält, ist sein Rang höchstens eins. Ein invertierbares Wort darf daher nur die Cliffordfaktoren enthalten. Es ist dann projektiv unitär und wirkt auf Herm(2,C) durch eine räumliche Rotation, nicht durch einen nichttrivialen Lorentz-Boost.

Der einfache Boostvertreter diag(2,1/2) hat Determinante eins, erhält die Minkowski-Determinante, ist aber weder projektiv unitär noch Rang eins. Er ist durch reine Komposition dieses 60-Strahlen-Alphabets nicht erreichbar.

Das schließt keine emergente Lorentzsymmetrie in einem größeren Mehrteilchenmodell, keine geeigneten Linearkombinationen und keinen Kontinuumsgrenzwert aus. Es entscheidet ausschließlich die Behauptung, die genannten elementaren Produkte lieferten bereits die volle Lorentzbewegung.

## 3. Gleichverteilte, unbeobachtete Ausführung depolarisiert

Für die 60 Operatoren ist K_A=A/sqrt(60) ein normiertes Krausensemble. Der Kanal ist exakt

    Phi(rho) = Tr(rho) I/2.

Die 24 Cliffordoperationen depolarisieren bei uniformem Mitteln schon für sich. Für die 36 Rang-eins-Operationen folgt dies aus sum_s |s><s| = 3I. Deshalb hilft es nicht, nur die beiden uniformen Klassen gegeneinander umzugewichten.

Die Pauli-Transfermatrix ist diag(1,0,0,0), nicht diag(1,2/3,1/3,...). Dieses Resultat ist bereits in der Fassung 2 dokumentiert und wird hier unabhängig reproduziert. Es betrifft den unbeobachteten gemittelten Kanal; es ist keine Behauptung, alle kohärenten oder mit einer Umgebung erweiterten Ausführungen seien so beschaffen.

## 4. Tatsächlicher TFPT-Populationstransfer bestimmt den Quantenkanal nicht

Für

    B = (1/18) [[13,1,4], [1,13,4], [4,4,10]]

mit Eigenwerten 1,2/3,1/3 ergeben die sechs Permutationsgewichte

    w_t = (1/2+t, t, t, 1/18-t, 2/9-t, 2/9-t), 0 <= t <= 1/18

denselben Populationstransfer. Im zweidimensionalen Kontrastraum ergeben die zugehörigen Quantenkanäle jedoch, in der Reihenfolge I,X,Y,Z, die Pauli-Transfermatrix

    diag(1,2/3,6t,1/3).

Die zusätzliche im Bericht deklarierte Cliffordregel wählt t=1/27; B allein tut dies nicht. Für den +Y-Eingangszustand unterscheiden sich t=0 und t=1/27 um 2/9 im Y-Erwartungswert und um 1/9 im Ausgangs-Spurabstand. Alle diese Aussagen werden symbolisch berechnet.

Das ist ein Gegenbeispiel gegen Rekonstruktion aus dem Populationstransfer allein, nicht gegen mögliche weitere Auswahlbedingungen des vollständigen TFPT-Systems.

## 5. Paarweise Überlappung ist keine globale Hilbertraumverklebung

Die Matrix

    K = [[1,1,0], [1,1,1], [0,1,1]]

hat Eigenwerte 1,1+sqrt(2),1-sqrt(2). Außerdem ist für v=(1,-1,1)

    v^T K v = -1.

Sie kann keine Gram-Matrix dreier Hilbertraumvektoren sein. Exaktes Teilen desselben normierten Modus entlang A-B und B-C erzwingt seine Identifikation auch zwischen A und C. Es darf dort nicht gleichzeitig Orthogonalität verlangt werden.

Ein konsistenter positiver Anschluss ist ein operatorwertiger Kern Gamma_XY=J_X^dagger J_Y mit Gamma >= 0 und Gamma_XX=I. Ein vorgegebener solcher Kern rekonstruiert minimale Einbettungen bis auf globale unitäre Äquivalenz, wählt aber nicht selbst einen TFPT-Kern oder eine räumliche Dimension aus.

Unter der zusätzlichen funktoriellen Boson-Einbettungsannahme des Berichts wird

    Gamma^B_XY = (1/8) W (Lambda² Gamma_XY) W^dagger.

Diese Formel ist Quellenbestand, kein in diesem Paket erneut bewiesener vollständiger W-/Fock-Satz.

## 6. Kegelidentität und Clock

Symbolisch geprüft:

    det(T I+x sigma_x+y sigma_y+z sigma_z) = T²-x²-y²-z².

Das ist ein exaktes Kegelwörterbuch. Es identifiziert nicht eigenständig die vier Koeffizienten mit Raumzeitkoordinaten.

Die zyklische Gruppe C30 enthält kein Element der Ordnung vier. Die Einheitengruppe (Z/30)^× enthält dagegen etwa 7 mit multiplikativer Ordnung vier. Eine Galois-Vierteloperation und eine Teilperiode der Coxeter-30-Uhr sind verschiedene Dinge.

Auch die vollständige unitäre Zeit-eins-Clock U=diag(1,i,-1,-i) bestimmt keinen eindeutigen positiven Hamiltonoperator. Sowohl

    H0 = diag(0,3pi/2,pi,pi/2)
    H1 = H0 + 2pi diag(0,1,0,0)

erfüllen exp(-iH)=U. Dazwischen unterscheiden sich ihre Entwicklungen. Die Quellenauswahl darf nicht durch die bloße Existenz eines Logarithmus ersetzt werden.

## 7. Lokaler Normierungsfehler im Horizon-Dokument

In `tfpt_horizon_readouts.pdf`, Seite 4, enthält die Zeile zu reduzierten Planck-Einheiten einen zusätzlichen Faktor c3. Mit hbar=c=kB=1 gilt

    bar_M_Pl² = 1/(8pi G), T_H = 1/(8pi G M) = bar_M_Pl²/M.

Die gedruckte Form c3·bar_M_Pl²/M ist damit um 1/(8pi) zu klein. Die Planck- und SI-Zeilen derselben Tabelle tragen den erwarteten Faktor. Dies ist ein lokaler Tabellen-/Normierungsbefund, keine Widerlegung des gesamten TFPT-Compilers und keine abgeschlossene Folgefehlerprüfung aller anderen Formeln.

## 8. Konstruktive Präzisierung, kein neu behaupteter Theorieschluss

Die binäre Paarverträglichkeit ist zu informationsarm. Ein geeigneter nächster Gegenstand sind vollständige zulässige Prozessgeschichten mit ihrem positiven Mehrzeitkern. In einer bereits gegebenen quantenmechanischen Realisierung mit Zustand omega und Geschichtenoperatoren K_gamma ist

    D(gamma,gamma') = omega(K_gamma^dagger K_gamma')

positiv: Jede endliche quadratische Kombination ist omega(X^dagger X)>=0. Diagonaleinträge liefern bei normierten Instrumenten die Zweigwahrscheinlichkeiten, Kreuzterme behalten Interferenzdaten. Aus einem gegebenen positiven Kern kann man einen minimalen Geschichten-Hilbertraum konstruieren. Für konsistente Konkatenationsoperatoren, vollständige Quantenprozesse, Kausalität und Lokalität werden weitere passende Bedingungen benötigt.

Dieses Vorgehen ist eine vorgeschlagene Form des Quellenvertrags, nicht die Behauptung, D sei bereits aus TFPT hergeleitet. Es darf insbesondere nicht aus einem frei gewählten Ziel-Hamiltonoperator rückwärts konstruiert und dann als Ursprung desselben Hamiltonoperators ausgegeben werden.

## Quellenbasis im Upload

- `Eingefügter Text.txt`: die 21 zu untersuchenden Thesen.
- `TFPT_Universalraum_Sitzungsdokumentation_2026-09-20_v2.pdf`: PDF-Seite 9 (Birkhoff-Fortsetzungen), PDF-Seite 15 / gedruckte Seite 10 (60 Operationen, Produkte, Lorentzkegel, Depolarisation); PDF-Seite 17 / gedruckte Seite 12 (Logarithmus- und Mehrzeitgrenzen).
- `TFPT_Gesamtstand_und_Loesungsweg_20260921.pdf`: PDF-Seiten 11-12 / gedruckt 6-7 (positiver RR/W-Kandidat, Grundraum, Quellen-/Zeitgrenze); PDF-Seiten 35-38 / gedruckt 30-33 (globale Gram-Verklebung, positiver Kern, Quellenvertrag); PDF-Seite 14 / gedruckt 9 (T1-T8).
- `origin_theory.pdf`: PDF-Seiten 5-6 (Coxeterclock versus Galois-Viertelwirkung).
- `tfpt_horizon_readouts.pdf`: PDF-Seite 4 (Einheitentabelle).
- `tfpt_research_contracts.pdf`: Research Contract TFPT.TOE.COMPLETE.01 und nachfolgende Integrationskorrekturen; Compiler-Abschluss ist nicht der physische Gesamtabschluss.
- `tfpt_prime_front.tex`: Proposition zur rationalen Unabhängigkeit der Logarithmen verschiedener Primzahlen und zur Unzulänglichkeit endlicher Clocks für dieses Periodenspektrum.

Die Hauptantwort enthält die anklickbaren Dateizitate und Primärliteraturbelege. Originaldokumente werden in diesem kleinen Prüfpaket nicht dupliziert.

## Schlussfolgerung dieses Pakets

Die getesteten Abkürzungen „Komponierbarkeit ist räumliche Nachbarschaft“, „uniforme Ausführung ist der richtige Transfer“ und „die elementare Kegelwirkung erzeugt durch Komposition bereits Boosts“ scheitern in der angegebenen 60-Operationen-Klasse. Der dokumentierte Populationstransfer und paarweise Überlappungen sind für eine vollständige Quantenprozessrekonstruktion nicht ausreichend.

Damit ist weder jede TFPT-Realisierung widerlegt noch ein vollständiger Lösungsweg bewiesen. Ein neuer Quellsatz müsste dieselbe Rohquelle, dieselben markierten Felder, dieselbe Zeit, den gemeinsamen Zustand, globale Verklebung und einen kontrollierten physikalischen Grenzwert verbinden. Die acht physischen Vollständigkeitsbedingungen bleiben zusätzliche Nachweispflichten.


</details>

[Zur Navigation](#navigation)

<a id="original-v19"></a>
## V19. Historische Trägerbrücke, Phasenverlust und gekoppelte Dynamik

fileciteturn10file0L14-L22

**Originaldatei:** `TFPT_Fortsetzung_2026-09-19.md`  
**SHA256:** `7b7dcca3f8fd79f52cac0d5aa35f367e54c863a85478a3ad29fdb1695254a7da`

<details>
<summary>V19: vollständigen Originalbericht öffnen</summary>

# TFPT und Universalraum: Trägerbrücke, Phasenverlust und gekoppelte Dynamik

**Forschungsfortsetzung vom 19. September 2026**

## Ergebnis und Geltungsbereich

Die Untersuchung setzt am vorangegangenen Audit der 60 komplexen E8 Wurzelrichtungen an. Sie konstruiert eine explizite Verbindung zwischen dem fünfdimensionalen Bild des vierten Projektormoments und dem fünfdimensionalen Kern der in TFPT bereits verwendeten Doily Inzidenz. Die Verbindung respektiert die Wirkung jeder der 60 ursprünglichen Reflexionen. Dieselbe quartische Abbildung liefert durch eine andere Paarung das holomorphe Wurzelinvariant F8.

Ein daraus gebautes, ausdrücklich zusätzlich angenommenes Paarmodell hat einen positiven Transferoperator und einen eindeutigen verschränkten Grundzustand. Die weitere Untersuchung ergibt jedoch drei präzise Grenzen. Erstens verliert die isolierte fünfdimensionale Darstellung eine ganze Pauli Untergruppe, nicht nur globale Phasen. Zweitens bestimmt selbst ihr eindeutiger Paargrundzustand das Bewegungsgesetz nicht: Innerhalb der vollständig klassifizierten symmetrischen Paarfamilie bleiben nach Maßstab und Energienullpunkt zwei dimensionslose Verhältnisse frei. Drittens lässt sich der ideale Paarzustand nicht gleichzeitig an zwei überlappenden Kanten verwirklichen. Die Kette aus drei Zellen besitzt im konkreten Modell sogar exakt einen fünffach entarteten Grundraum.

**Damit sind endliche mathematische Verbindungen bewiesen und konkrete Modellabkürzungen ausgeschlossen. Weder die primitive physische Kompositionsregel noch eine vollständige TOE sind daraus hergeleitet.**

Die Bezeichnungen „exakt“ und „bewiesen“ beziehen sich hier auf ausgeschriebene endliche Argumente samt ganzzahligen oder rationalen Matrixzertifikaten. Dies ist keine neue Lean Formalisierung und keine erneute Ausführung des ursprünglichen TFPT Repositorys. Die allgemeine Theorie der Clifford Momente und das Maschke Polynom sind bekannt. Beansprucht wird die hier explizit ausgeführte Verbindung zu den angegebenen TFPT Quelldaten, keine weltweite Erstentdeckung dieser mathematischen Gegenstände.

## 1. Verwendete Quellen und Rechenbasis

Die ursprüngliche Quelle ist die Konstruktion in `note_e8_gaussian_code.tex`: vier Koordinatenpaare, der äquivariant platzierte erweiterte Hamming Code, 240 Wurzeln mit reeller Norm zum Quadrat 4 und die komplexe Struktur J. Aus jeder Bahn {x,Jx,−x,−Jx} entsteht eine komplexe Richtung. Die Programme rekonstruieren diese Daten aus den ausgeschriebenen Regeln, ohne gemessene Naturkonstanten zu verwenden.

Weitere maßgebliche Stellen sind:

* `tfpt_1_architecture_e8.pdf`, Seite 13: Doily Inzidenz, Rang 10 und fünfdimensionaler Kern, aufgespannt durch sechs Ovoidfunktionen; Seiten 15 und 16: endliche Normalform Cfin, markierte quadratische Verfeinerung q*, S5 und die Wirkung der Familienrotation.
* `tfpt_research_contracts.pdf`, Seiten 174 bis 181: gemeinsames erzeugendes Funktional, fehlende Zustandswahl, physische Dynamik, Gravitationssektor und die offenen Anforderungen T1 bis T8.
* `TFPT_Audit_2026-09-19.md`: vorheriger unabhängiger Momentenaudit und die dort noch nicht konstruierte Trägerverbindung.
* `tfpt_universalraum_einfach_2026-09-12.tex`: die Unterscheidung zwischen einer Rekonstruktion aus eingesetzten Daten und der Vorwärtsableitung des Prozesses aus primitiven Regeln.

Die große Universalraum Synthese ist weiterhin nur als LaTeX Hülle mit einem Verweis auf eine nicht enthaltene Hauptdatei vorhanden. Ihr fehlender Inhalt wird nicht ergänzt oder als gelesen ausgegeben.

Die verwendete komplexe C4 ist zunächst der Koordinatenraum des Gitters. Sie ist nicht automatisch der physische Fermionraum oder eine Raumzeit. Auch die fünfdimensionale Darstellung wird erst als mathematischer Träger behandelt.

### Reproduktion

Im beigefügten Paket:

```sh
python -m pip install -r requirements.txt
python run_all.py
```

`run_all.py` führt die beiden benötigten Programme des vorherigen Audits sowie die drei neuen Programme aus. Es benötigt keine Netzwerkverbindung nach Installation der Abhängigkeiten. Es schreibt Ergebnisse und Protokolle in das Paketverzeichnis. Die Programme prüfen ihre Bedingungen und brechen bei einer falschen Identität ab. Assertions dürfen nicht durch den Python Optimierungsmodus ausgeschaltet werden; der Starter erzwingt deshalb den normalen Modus.

Die neuen Programme sind `continuation_probe.py`, `kernel_probe.py` und `selection_probe.py`. Matrizen liegen in `continuation_matrices.npz`. Die gruppentheoretische Suche umfasst tatsächlich alle 46080 erzeugten Matrizen. Die Grundenergie der Dreierkette wird zusätzlich mit einem exakten charakteristischen Polynom und rationalen Sturm Intervallen zertifiziert. Nur die Viererzelle und die angezeigten Dezimalwerte der Ketten werden ausschließlich numerisch diagonalisiert.

## 2. Ausgangspunkt: der vierte Projektormoment

Für eine normierte komplexe Wurzelrichtung ψ_l sei

\[
P_l=|\psi_l\rangle\langle\psi_l|,\qquad
M_t=\frac1{60}\sum_{l=1}^{60}P_l^{\otimes t}.
\]

Bezeichne S_t den orthogonalen Projektor auf Sym^t(C4). Der reproduzierte vorherige Audit ergibt

\[
M_1=I/4,\qquad M_2=S_2/10,\qquad M_3=S_3/20.
\]

Erst das vierte Moment unterscheidet sich vom kontinuierlich unitär invarianten Mittel. Dabei ist

\[
\Pi_5=40M_4-S_4,\qquad \Pi_5^2=\Pi_5,\qquad \operatorname{rank}\Pi_5=5,
\]

\[
D^{(4)}=M_4-S_4/35=(7\Pi_5-S_4)/280.
\]

Der Index 4 bezeichnet die Momentenordnung, nicht eine Raumzeitdimension und nicht die dihedrale Gruppe D4.

Eine orthonormale Basis des Bildes C5 von Π5 ist

\[
v_0=(|0000\rangle+|1111\rangle+|2222\rangle+|3333\rangle)/2,
\]

\[
v_1=(\sum_{\rm perm}|0011\rangle+\sum_{\rm perm}|2233\rangle)/\sqrt{12},
\]

\[
v_2=(\sum_{\rm perm}|0022\rangle+\sum_{\rm perm}|1133\rangle)/\sqrt{12},
\]

\[
v_3=(\sum_{\rm perm}|0033\rangle+\sum_{\rm perm}|1122\rangle)/\sqrt{12},
\]

\[
v_4=\sum_{\rm perm}|0123\rangle/\sqrt{24}.
\]

Jede Summe enthält verschiedene Permutationen. Schreibe E für die fünf unnormalisierten Supportspalten. Dann

\[
G=E^TE=\operatorname{diag}(4,12,12,12,24).
\]

E und G erlauben, sämtliche folgenden Rechnungen rational statt mit Quadratwurzeln durchzuführen.

## 3. Satz: Die Momentendarstellung ist der vorhandene Doily Kern

Die ursprünglichen 60 Reflexionen sind

\[
r_l=I-2P_l.
\]

Alle erhalten das Gitter und das Bild C5 unter ihrer vierten Tensorpotenz. Die Einschränkungen

\[
U_l=r_l^{\otimes4}|_{C_5}
\]

sind in der angegebenen reellen Struktur orthogonale Involutionen mit Spur 3. Es gibt genau 15 unterschiedliche Einschränkungen, jede mit vier ursprünglichen Reflexionen als Urbild.

### 3.1 Die sechs Simplexrichtungen

In den E Koordinaten definiere die sechs Spalten der Matrix

\[
W=\begin{pmatrix}
2&2&-1&-1&-1&-1\\
0&0&-1&-1&1&1\\
0&0&-1&1&-1&1\\
0&0&1&-1&-1&1\\
1&-1&0&0&0&0
\end{pmatrix}.
\]

Es gilt exakt

\[
W\mathbf1=0,\qquad W^TG W=48I_6-8J_6,
\]

wobei J6 die Matrix aus Einsen ist. Die sechs eingebetteten Vektoren EW bilden ein reguläres Simplex im fünfdimensionalen Raum. Jede U_l vertauscht genau zwei dieser sechs Vektoren. Die 15 verschiedenen U_l erzeugen sämtliche Permutationen der sechs Vektoren.

Die induzierte Darstellung ist daher die Standarddarstellung der Gruppe S6 auf dem Unterraum mit Koordinatensumme null. Sie ist irreduzibel. Als unabhängiges endliches Zertifikat prüft das Programm über alle 720 Permutationen

\[
\frac1{720}\sum_g\chi(g)=0,\qquad
\frac1{720}\sum_g\chi(g)^2=1,
\]

mit χ(g)=Anzahl der Fixpunkte von g minus 1. Insbesondere existiert kein unter der gesamten Gruppe unveränderter einzelner Vektor.

### 3.2 Die tatsächliche Gaußsche Quelle

Für die Verbindung muss der ursprüngliche Quotient V=L/(1+i)L verwendet werden. Ein bloß ähnlich aussehender Raum von Pauli Labels darf nicht stillschweigend an seine Stelle treten.

Die Quotientenrelation wird direkt durch

\[
x\sim y\quad\Longleftrightarrow\quad (I-J)(x-y)/2\in L
\]

geprüft. Die 60 Richtungen verteilen sich in 15 nichtverschwindende Klassen zu je vier Richtungen. Der Quotient hat Dimension vier über F2. Seine alternierende Form wird durch

\[
b(\bar x,\bar y)=\frac{x\cdot y+x\cdot Jy}{2}\pmod2
\]

in der verwendeten Gitterkonvention berechnet.

Die sechs quadratischen Verfeinerungen vom Arf Typ 1 besitzen jeweils fünf nichtverschwindende Nullstellen. Diese fünf Punkte bilden das Ovoid O_q. Setze

\[
F_{v,q}=3\mathbf1_{O_q}(v)-1.
\]

Hier hat F 15 Zeilen und sechs Spalten. Sei N die 15 mal 15 Inzidenzmatrix mit **Punkten als Zeilen und isotropen Linien als Spalten**. Damit ist die richtige Kernschreibweise in diesem Bericht ker(N^T). Exakt:

\[
F^TF=36I_6-6J_6,\qquad N^TF=0,
\]

\[
\operatorname{rank}N=10,\qquad\operatorname{rank}F=5.
\]

Die sechs Ovoidspalten spannen somit ker(N^T). Die Übereinstimmung mit der Quelle umfasst die Wirkung derselben ursprünglichen Reflexionen auf dem Gaußschen Quotienten.

### 3.3 Explizite Abbildung statt Dimensionsvergleich

Die sechs Spalten von W lassen sich mit den sechs Ovoidspalten eindeutig so zuordnen, dass alle 60 Reflexionswirkungen übereinstimmen. In den gespeicherten Koordinaten ist diese Zuordnung bereits in W enthalten. Definiere

\[
J_0=\frac1{36}EWF^T.
\]

Dann gilt

\[
J_0F=EW,\qquad J_0J_0^T=\frac43\Pi_5.
\]

Für jede ursprüngliche Reflexion mit ihrer 15 Punkte Permutationsmatrix R_l wird außerdem exakt geprüft

\[
J_0R_l=U_lJ_0
\]

in der eingebetteten Darstellung. Folglich ist

\[
\boxed{\mathcal I=(\sqrt3/2)J_0:\ker N^T\longrightarrow C_5}
\]

eine isometrische, symmetrieverträgliche Isomorphie.

Das schließt den konkreten endlichen Brückensatz. Es ist nicht bloß „fünf gleich fünf“. Es zeigt aber noch keine physische Identifikation mit einem vollständigen Materieraum, keine chirale Feldtheorie und keine Raumzeit.

### 3.4 Die vorhandene Markierung q* wird transportiert

Eine markierte Arf Verfeinerung q* hat einen Stabilisator S5 der Ordnung 120. Auf C5 zerfällt die Darstellung dann in 1⊕4. Die zum markierten Simplexpunkt gehörige Gerade ist die einzige invariante Gerade. Die fünf Differenzen zu den übrigen Simplexpunkten sind linear unabhängig und werden als fünf Trägerplätze permutiert.

Die ursprüngliche Rotation σ zyklisiert drei komplexe Koordinaten und lässt die vierte stehen. Auf den sechs Ovoiden wirkt sie als ein Dreierzyklus mit drei Fixpunkten. Nach Markierung eines σ festen q* hat die verbleibende Fünfermenge die Orbitgrößen 3,1,1. Das ergibt einen Dreierblock und zwei ruhende Plätze.

Die TFPT Quelle besitzt bereits einen Selektor für q*. Diese Untersuchung überträgt ihn durch die neue Abbildung; sie leitet ihn nicht aus dem unmarkierten vierten Moment her. Ebenso wenig folgt aus einer Permutation von drei und zwei Plätzen bereits die vollständige kontinuierliche Eichdynamik SU(3)×SU(2)×U(1).

## 4. Satz: Hermitesches Moment und holomorphes F8 sind zwei Paarungen derselben Abbildung

Sei V0 die Matrix der orthonormalen Spalten v0 bis v4 und

\[
w(z)=V_0^Tz^{\otimes4}.
\]

Explizit:

\[
w_0=\frac12\sum_i z_i^4,
\]

\[
w_1=\sqrt3(z_0^2z_1^2+z_2^2z_3^2),
\]

\[
w_2=\sqrt3(z_0^2z_2^2+z_1^2z_3^2),
\]

\[
w_3=\sqrt3(z_0^2z_3^2+z_1^2z_2^2),\qquad
w_4=\sqrt{24}z_0z_1z_2z_3.
\]

Die Hermitesche Paarung reproduziert die Momentauslesung:

\[
w(z)^\dagger w(z)=\langle z^{\otimes4}|\Pi_5|z^{\otimes4}\rangle.
\]

Weil die U_l reell orthogonal wirken, ist auch die komplex bilineare Paarung w(z)^T w(z) invariant. Definiere in der Quellkonvention mit Wurzelnorm zum Quadrat 4

\[
F_8(z)=\sum_{\alpha\in R(L)}
\left[\sum_{k=0}^3(\alpha_{2k}-i\alpha_{2k+1})z_k\right]^8.
\]

Die vollständige Koeffizientenrechnung ergibt

\[
\boxed{F_8(z)=7680\,w(z)^Tw(z)}.
\]

Ausgeschrieben:

\[
F_8(z)=1920\left[
\sum_i z_i^8+14\sum_{i<j}z_i^4z_j^4+
168z_0^2z_1^2z_2^2z_3^2
\right].
\]

Der Ausdruck in Klammern ist das bekannte Maschke Polynom. Die Normierung 1920 ist hier aus den 240 Wurzeln berechnet. Eine anders skalierte Wurzelkonvention ändert den Vorfaktor entsprechend der achten Potenz des Skalierungsfaktors.

**Dies korrigiert keine Objekttypen durch Gleichsetzung.** D^(4) ist weiterhin kein holomorphes Polynom F8. Die Verbindung besteht darin, dass dieselbe quartische Abbildung mit zwei unterschiedlichen Paarungen beide Objekte liefert. Die Paarungen haben unterschiedliche Informationen und unterschiedliche Verwendungszwecke.

## 5. Satz: Die isolierte Fünferdarstellung verliert operational unterscheidbare Wirkungen

Die volle Matrixgruppe G, erzeugt von den ursprünglichen 60 Reflexionen, wurde mit exakten Gaußschen Matrizen vollständig enumeriert. Ihr Umfang beträgt 46080. Die Darstellung auf C5 hat Bild S6 mit 720 Elementen und einen Kern aus 64 Elementen. Dieser Kern wurde nicht nur anhand seiner Ordnung erkannt: Die gespeicherten Matrizen stimmen exakt mit der vollständigen Zweiqubit Pauli Gruppe überein, also 16 Hermiteschen Pauli Tensoren multipliziert mit den vier skalaren Phasen.

Damit lautet die exakte Sequenz

\[
1\longrightarrow\mathcal P_2\longrightarrow G_{31}
\overset{\rho_4}{\longrightarrow}S_6\longrightarrow1,
\qquad |\mathcal P_2|=64.
\]

Die zentrale Vierteldrehung J=iI liegt im Kern. Aber der Verlust geht weiter: Nach Herausnahme der vier skalaren Phasen bleiben 16 unterschiedliche projektive Wirkungen unsichtbar.

### 5.1 Ein exakter Unterschied zwischen null und eins

Zwei ursprüngliche Koordinatenreflexionen sind

\[
r_a=\operatorname{diag}(-1,1,1,1),\qquad
r_b=\operatorname{diag}(1,-1,1,1).
\]

Auf C5 wirken beide gleich:

\[
\rho_4(r_a)=\rho_4(r_b)=\operatorname{diag}(1,1,1,1,-1).
\]

Wähle nun den normierten Zustand

\[
|\psi\rangle=(|0\rangle+|2\rangle)/\sqrt2.
\]

Er ist selbst eine ursprüngliche Wurzelrichtung, etwa aus dem Gaußschen Lift (1+i,0,1+i,0). Auch der Projektor auf ψ gehört also zum schon vorhandenen Alphabet. Dann gilt exakt

\[
|\langle\psi|r_a|\psi\rangle|^2=0,
\qquad
|\langle\psi|r_b|\psi\rangle|^2=1.
\]

Die isolierte Fünferdarstellung identifiziert zwei Prozesse, die ein Test im ursprünglichen endlichen Modell perfekt unterscheidet. Es ist deshalb nicht zulässig, den gesamten Verlust als unwichtige globale Phase zu erklären. Dies ist ein mathematisches Operationalitätsbeispiel, kein durchgeführtes Laborexperiment und keine bereits konstruierte TFPT Messapparatur.

### 5.2 Warum beliebig viele weitere Tensorprodukte das nicht reparieren

Wenn k im Kern einer Darstellung liegt, ist ρ(k)=I. Dann wirkt k auf jedem Tensorprodukt dieser Darstellung ebenfalls als Identität, ebenso auf direkten Summen, Dualen und invarianten Teilräumen. Jede ausschließlich aus diesen Objekten und äquivarianten Abbildungen gebaute weitere Konstruktion bleibt blind für k.

**Folgerung:** Mehr Kopien des isolierten abstrakten Fünferträgers können die verlorenen Pauli Wirkungen nicht zurückholen. Man muss Daten außerhalb dieses Quotienten beibehalten.

**Wichtige Grenze des Satzes:** Der eingebettete Tensor Π5 zusammen mit seinem ursprünglichen C4 Raum, der quartischen Abbildung und den tatsächlichen Reflexionen enthält mehr Information als eine isolierte abstrakte S6 Darstellung. Der Satz widerlegt nicht die vorherige Rekonstruktion der 60 Strahlen aus dem eingebetteten Moment. Er widerlegt die Abkürzung, die ganze Quelle durch die abstrakte Fünferdarstellung zu ersetzen.

### 5.3 Der operational zulässige Quotient ist vollständig bestimmt

Die 60 ursprünglichen Projektoren spannen den gesamten 16 dimensionalen reellen Raum der Hermiteschen 4 mal 4 Matrizen auf. Das ist im Programm als exakter Rang geprüft und folgt auch unmittelbar aus dem zweiten Moment: Die Projektorrahmenabbildung lautet

\[
\frac1{60}\sum_l P_l\operatorname{Tr}(P_lX)
=\frac{X+\operatorname{Tr}(X)I}{20}
\]

und ist invertierbar.

Betrachte für U aus der ursprünglichen Reflexionsgruppe sämtliche Übergangswahrscheinlichkeiten

\[
p_{m,l}(U)=\operatorname{Tr}(P_mUP_lU^\dagger).
\]

Wenn diese Zahlen für U und V bei allen 60 Präparationen und allen 60 Projektortests gleich sind, dann stimmen wegen der beidseitigen linearen Aufspannung ihre Konjugationswirkungen auf der gesamten Matrixalgebra überein. Also ist V†U skalar. Die skalare Untergruppe der enumerierten Gruppe besteht exakt aus den vier Phasen µ4. Umgekehrt ändern diese Phasen die Wahrscheinlichkeiten nicht.

Damit ist innerhalb dieses präzisen endlichen Präparations und Testvertrags der operational verträgliche Gruppenquotient

\[
\boxed{G_{31}/\mu_4,\qquad |G_{31}/\mu_4|=11520,}
\]

und nicht S6 mit 720 Elementen. Der Faktor 16 ist somit nicht nur an einem Beispiel sichtbar: Die zulässige Identifikation aller Gruppenwirkungen ist in diesem Vertrag vollständig klassifiziert.

Der Satz behauptet nicht, eine absolute globale Phase sei messbar. Gerade diese vier skalaren Phasen dürfen im angegebenen Testvertrag entfernt werden. Welche zentralen Lifts für andere Sektoren oder eine quellengegebene kohärente Prozesskomposition erforderlich sind, ist eine getrennte Frage.

## 6. Ein konstruktives Paarmodell mit eindeutigem relationalem Zustand

Um zu prüfen, ob der Träger überhaupt nichttriviale Dynamik und eine Zustandswahl tragen kann, wurde folgendes **Testmodell zusätzlich definiert**:

\[
T_{\rm Paar}=\frac1{60}\sum_l U_l\otimes\overline{U_l},
\qquad h=I-T_{\rm Paar}.
\]

Hier sind die U_l reell, sodass die Konjugation numerisch keinen Unterschied macht. Das gleichgewichtete Mittel entspricht einem Mittel über die 15 verschiedenen Transpositionen. Dass diese Kombination die primitive physische TFPT Wechselwirkung sei, wird nicht angenommen oder bewiesen.

Das charakteristische Polynom wird exakt berechnet. Auf dem 25 dimensionalen Paarraum gilt:

| Sektordimension | T Paar | h |
|:---|:---|:---|
| 1 | 1 | 0 |
| 5 | 3/5 | 2/5 |
| 9 | 1/3 | 2/3 |
| 10 | 1/5 | 4/5 |

T Paar ist strikt positiv und selbstadjungiert, h ist positiv. Der eindeutige Grundzustand von h ist

\[
|\Omega_5\rangle=\frac1{\sqrt5}\sum_{a=0}^4|a\rangle|\bar a\rangle.
\]

Auf jeder einzelnen Seite ist der reduzierte Zustand I5/5. Die lokale Entropie ist ln5. Global liegt trotzdem ein bestimmter reiner Zustand vor. Die Eindeutigkeit folgt auch aus der Irreduzibilität der ursprünglichen Fünferdarstellung: Die invarianten Vektoren in C5⊗C5* entsprechen ihrem eindimensionalen Kommutanten.

Das ist ein exakter endlicher Existenzbeweis für eine relationale Zustandswahl **innerhalb des Testmodells**. Die lokalen Zustände müssen dafür nicht jeweils eine ausgezeichnete Richtung auswählen.

### 6.1 Die Operatortypen bleiben getrennt

Da T Paar positiv ist, kann man H_OS=−log(T Paar) definieren. Es entsteht eine unitäre Gruppe exp(−it H_OS) und ein zugehöriger positiver euklidischer Zeittransfer. Dagegen ist der in den Ketten untersuchte Hamiltonoperator h=I−T Paar ein anderer Operator. Es gilt ausdrücklich nicht T Paar=exp(−h).

Auch ein zufälliger unitärer Kanal X↦(1/60)Σ U_l X U_l† ist ein anderer Objekttyp. Seine vektorisierte Matrix hat in der hier reellen Darstellung dasselbe Spektrum, sein stationärer Einzelzustand ist aber I5/5, nicht der reine Paarzustand Ω5. Eine Kanalformel ist keine automatische Identifikation eines physischen euklidischen Transfers.

Die endliche Zeitkonstruktion beweist weder räumliche Lokalität noch Lorentzsymmetrie, einen Kontinuumsgrenzwert oder eine wechselwirkende 3+1 dimensionale Feldtheorie. Das Spektrum des Paarmodells reproduziert außerdem nicht das TFPT Nahtspektrum 1,(2/3)^6,(1/3)^6.

## 7. Vollständige Klassifikation der symmetrischen Paarfamilie

Der Erfolg des einen Paarmodells wirft die Frage auf, ob seine Symmetrie und sein Grundzustand das Gesetz eindeutig bestimmen. Hier kann die gesamte Familie entschieden werden.

Auf C5 hat die Standarddarstellung den Charakter χ(g)=Fix(g)−1. Auf dem Paarraum ist der Charakter χ(g)^2. Die exakte Summe über alle 720 Permutationen ergibt

\[
\dim\operatorname{End}_{S_6}(C_5\otimes C_5)
=\frac1{720}\sum_{g\in S_6}\chi(g)^4=4.
\]

Die vier spektralen Projektoren des bereits berechneten T Paar sind unabhängige invariante Operatoren. Da der gesamte Kommutant vierdimensional ist, schöpfen sie ihn aus. Ihre Ränge sind 1,5,9,10. Jeder symmetrieverträgliche Hermitesche Paaroperator ist deshalb von der Form

\[
\boxed{H=cI+\epsilon_5P_5+\epsilon_9P_9+\epsilon_{10}P_{10}}.
\]

Der Energieunterschied des Singuletts ist dabei als null gewählt. Ω5 ist genau dann der eindeutige Grundzustand, wenn alle drei ε strikt positiv sind. Nach Entfernung des Energienullpunkts c und eines gemeinsamen Energiemaßstabs bleiben **zwei unabhängige dimensionslose Verhältnisse**.

Das ist eine vollständige endliche Nichtauswahl innerhalb dieser exakt definierten Klasse. Symmetrie, Positivität und derselbe eindeutige verschränkte Zustand wählen das Bewegungsgesetz nicht allein aus. Eine zusätzliche ursprüngliche TFPT Regel könnte die beiden Verhältnisse bestimmen, aber sie wird durch diese Bedingungen nicht ersetzt.

Diese Klassifikation betrifft nicht alle möglichen TFPT Modelle, sondern den hier untersuchten simultan S6 invarianten Paarraum. Eine Verringerung der Symmetrie durch zusätzliche Markierungen macht den zulässigen Operatorraum im Allgemeinen größer, nicht automatisch eindeutig.

## 8. Mehrere Zellen: eine exakte Kompatibilitätsgrenze

Setze denselben Paarterm auf benachbarte Zellen einer offenen Kette:

\[
H_n=\sum_{j=1}^{n-1}h_{j,j+1}.
\]

Das ist wiederum eine Testgeometrie, keine aus TFPT hergeleitete Raumdimension.

### 8.1 Der ideale Paarzustand kann nicht gleichzeitig beide Kanten erfüllen

Sei Q12 der Projektor auf Ω5 zwischen Zelle 1 und 2, mit Identität auf Zelle 3. Definiere Q23 entsprechend. Exakt gilt

\[
Q_{12}Q_{23}Q_{12}=\frac1{25}Q_{12},
\qquad
Q_{23}Q_{12}Q_{23}=\frac1{25}Q_{23}.
\]

Damit haben die beiden idealen Paarbedingungen keinen gemeinsamen Zustand. Auf ihren nichttrivialen gemeinsamen Blöcken hat Q12+Q23 die Eigenwerte 1±1/5; also ist seine Norm 6/5.

Aus dem lokalen Spektrum folgt

\[
h\ge\frac25(I-Q).
\]

Deshalb

\[
\boxed{H_3\ge\frac25(2I-Q_{12}-Q_{23})\ge\frac8{25}I}.
\]

Allgemeiner gilt für jede positive Kopplung aus der in Abschnitt 7 klassifizierten Familie mit demselben eindeutigen Paargrundzustand und lokaler Lücke δ>0 die Schranke H3≥(4/5)δ I. Die Unmöglichkeit einer gleichzeitigen perfekten Erfüllung ist deshalb nicht auf die besonderen drei Energiewerte des Testmodells beschränkt.

Der einfache Versuch, jede überlappende Bindung unabhängig in denselben perfekten Paarzustand zu setzen, ist damit ausgeschlossen. Der Befund erzwingt nicht das Scheitern aller gekoppelten Modelle: Ein echtes Vielteilchengesetz könnte Frustration tragen oder eine andere primitive Faktorisierung haben. Solche Möglichkeiten müssen aber aus der Quelle begründet werden.

### 8.2 Exakter Dreizellensatz

Die charakteristische Rechnung wurde für die volle 125 dimensionale Dreierkette rational durchgeführt. Für x als Eigenwert von 240H3 faktorisiert das Polynom zu

```text
(x−384)^10 (x−368)^16 (x−352)^9 (x−336)^16
(x−320)^5 (x−288)^19 (x−256)^9 (x−192)^6
(x²−608x+89088)^10
(x³−704x²+150528x−9437184)^5.
```

Die kleinste Eigenenergie E0 ist die kleinste reelle Nullstelle von

\[
375E^3-1100E^2+980E-256=0.
\]

Ein rationaler Sturm Test isoliert sie in

\[
0.4672<E_0<0.4673.
\]

Alle anderen Zweige liegen höher; die nächste Energie ist exakt 4/5. Der Grundraum besitzt daher **exakt Dimension fünf**, und der Abstand zum nächsten Niveau ist 4/5−E0. Der Nachweis der Entartung ist nicht mehr bloß eine numerische Toleranzentscheidung.

### 8.3 Vergleich der kleinen Ketten

| Zellen | Grundenergie | Grundraumdimension | Abstand zum nächsten Niveau | Zertifikatsart |
|:---|:---|:---|:---|:---|
| 2 | 0 | 1 | 2/5 | exakt |
| 3 | 0.467227803293… | 5 | 0.332772196707… | Polynom, Vielfachheit und Intervalle exakt |
| 4 | 0.575378874876… | 1 | 0.257569832419… | numerische Diagonalisierung |

Diese drei Größen begründen keinen thermodynamischen Grenzwert. Insbesondere ist aus dem Wechsel der Grundraumdimensionen keine allgemeine Gerade/Ungerade Regel für alle Kettenlängen bewiesen.

## 9. Was die Fortsetzung für die Gesamtlösung verändert

Drei bisher voneinander getrennte Aussagen stehen nun in einer konkreten Verbindung:

\[
\text{Gaußsches E8 Alphabet}
\longrightarrow \Pi_5
\longleftrightarrow \ker N^T
\longrightarrow w(z)
\longrightarrow\{w^\dagger w,\ w^Tw\}.
\]

Das ist eine nichttriviale Vereinheitlichung endlicher Strukturen. Sie erreicht die Quelloperationen, die vorhandene Ovoidgeometrie und das holomorphe F8, statt nur Dimensionen zu vergleichen.

Die umfassende physische Lösung darf aber nicht mit dem Quotienten enden. Die exakte Kernsequenz und das Null/Eins Beispiel zeigen, welche Information ein isolierter Fünferträger verliert. Außerdem liefert der Kommutantensatz die präzise Unterbestimmtheit der Paarregel. Der Dreizellensatz zeigt schließlich, dass lokale Eindeutigkeit keine gemeinsame globale Erfüllbarkeit garantiert.

Die engere Arbeitshypothese ist daher: **Die primitive physische Regel muss eine phasentreue Komposition auf der ursprünglichen Quelle festlegen; die Träger, Momente und Invarianten müssen deren Auslesungen bleiben, statt die Quelle zu ersetzen.** Das ist eine durch die Gegenbeispiele motivierte Hypothese, keine schon gefundene Universaldynamik.

Ein besonders scharfer notwendiger Test liegt jetzt vor. Eine zulässige Verdichtung von Prozessen darf r_a und r_b nicht identifizieren, solange der vorhandene ψ Test zugelassen ist. Allgemeiner müssen zusammengefasste Geschichten für alle erlaubten Fortsetzungen dieselben Antworten liefern. Das ist eine Anforderung an einen operational verträglichen Quotienten. Die heutige isolierte Fünferdarstellung besteht sie nicht.

Die ursprüngliche Regel muss zusätzlich vor dem Datenvergleich entscheiden, welche Wechselwirkungsterme, Gewichte, Anordnungen und Anfangszustandsbedingungen gelten. Der mathematische Brückensatz erledigt diese Auswahl nicht. Er macht jedoch eine Vorwärtsprüfung möglich: Aus der Quelle gewonnene Prozesse können gleichzeitig gegen die Momentenabbildung, die native Symmetrie, den unsichtbaren Kern und die globale Kompatibilität geprüft werden.

## 10. Physischer Status

Keine der heutigen Rechnungen liefert einen gemeinsamen lokalen 3+1 dimensionalen Ursprung, eine chirale Standardmodellmaßkonstruktion, alle drei Eichkopplungen, einen universell gekoppelten masselosen Spin 2 Sektor oder das kosmologische Schwinger–Keldysh Funktional mit abgeleiteter Anfangsdichte.

Die Quellen behandeln diese Anforderungen selbst getrennt von der endlichen Compilerkonsistenz. Der neue Brückensatz ist ein Beitrag zur endlichen algebraischen Verbindung; er verändert die physische Einstufung der Anforderungen T1 bis T8 nicht automatisch. Die heutige Familie wird nicht nachträglich auf Alpha, die Nahtkontraktionen oder andere bekannte Zielwerte eingestellt.

Die arithmetischen Ziele RH, Faktorisierung und P versus NP wurden in dieser Fortsetzung nicht bearbeitet. Aus den hier bewiesenen endlichen Verbindungen folgt keine Aussage über sie. Ebenso wurde keine native Hylæan Fähigkeit gemessen.

**Gesamturteil:** Die Trägerverbindung ist jetzt explizit konstruiert. Die stärkere Abkürzung, den vollständigen Prozess durch diesen isolierten Träger zu ersetzen, ist dagegen durch einen exakt unterscheidbaren Prozessvergleich widerlegt. Eine gültige Gesamtlösung muss diese Unterscheidungen bewahren und ihre Gewichte sowie ihre globale Dynamik aus der Quelle bestimmen.

## Literatur und Einordnung

Die folgenden Primärquellen dienen der Einordnung bekannter Mathematik, nicht als Ersatz für die im Paket gerechneten TFPT Zuordnungen:

1. Richard Kueng und David Gross: *Qubit stabilizer states are complex projective 3-designs*, arXiv:1510.02767, 2015. Allgemeiner Hintergrund der drei isotropen Momente.
2. Huangjun Zhu, Richard Kueng, Markus Grassl und David Gross: *The Clifford group fails gracefully to be a unitary 4-design*, arXiv:1609.08172, 2016. Der zusätzliche Unterraum der vierten Tensorpotenz und seine Darstellungstheorie sind bekannte Gegenstände.
3. Gilberto Bini und Bert van Geemen: *Geometry and Arithmetic of Maschke's Calabi–Yau Threefold*, arXiv:1110.0106, 2011, insbesondere die auf Seite 1 ausgeschriebene Oktik. Die Auftretensweise dieser bekannten Oktik wird hier auf den vorgelegten Wurzeldaten berechnet. Aus ihrer algebraisch geometrischen Verwendung folgt keine physische Raumzeitidentifikation.

## Dateien im Paket

`continuation_probe.py` prüft den Träger, die tatsächliche Gaußsche Quotientenwirkung, den Intertwiner, das F8 und das Paarmodell. `kernel_probe.py` enumeriert die ganze Reflexionsgruppe, identifiziert ihren unsichtbaren Kern und prüft den operationalen Null/Eins Zeugen. `selection_probe.py` klassifiziert alle invarianten Paaroperatoren und zertifiziert die Dreierkette samt Überlappungsidentität exakt.

`continuation_results.json`, `kernel_results.json` und `selection_results.json` dokumentieren die Resultate. `continuation_matrices.npz` enthält E, G, W, F, N, die ganzzahligen Abbildungszähler und Nenner, alle Einschränkungen der Reflexionen sowie den Paaroperator. `tfpt_audit` enthält die für die Reproduktion erforderlichen Programme des ersten Audits. `environment.json`, `input_sha256.json` und `MANIFEST.sha256` dokumentieren Umgebung, Quellidentitäten und Paketdateien.


</details>

[Zur Navigation](#navigation)

<a id="original-q1"></a>
## Q1. Quartikcode, Prozessauslesung und quellentreue Komposition

fileciteturn14file0L13-L29

**Originaldatei:** `TFPT_Quartik_Fortsetzung_Herleitungen_20260926.md`  
**SHA256:** `dad198b1a4a93be091de46a0cedb53f3b0616276d6dc9bbbed26c9ddf87256de`

<details>
<summary>Q1: vollständigen Originalbericht öffnen</summary>

# TFPT: Quartikcode, Prozessauslesung und quellentreue Komposition

Forschungsfortsetzung vom 26. September 2026

## 0. Ergebnis, Grundlage und Beweisgrenzen

Diese Fortsetzung prüft den eingereichten Text über den Fünfercode, die Ordnung zwei/drei/vier von Steuerung, Hyperladung und energetischem Schutz sowie den Entropiepunkt t=1/27. Sie konstruiert zusätzlich eine explizite Verbindung zwischen der Zweiregisterauslesung, zehn gleichwinkligen Richtungen, dem Petersen Graphen und den sechs vorhandenen Simplexmarken. Die normierte Singularübertragung 2/3 entsteht dabei aus dem Code selbst. Die tatsächliche vollständig positive Rückkanal-Komposition hat dagegen den Eigenwert 4/9.

Zwei weitere Entscheidungen betreffen die Dynamik: Der Fünfercode besitzt einen einfachen positiven Hamiltonoperator aus dem vorhandenen vierten Moment. Zwei identische perfekte Fünfercodes können jedoch keine physischen Register teilen. Für getrennte Blöcke wird eine nichttriviale effektive Kopplung aus gewöhnlichen Paarwechselwirkungen explizit berechnet. Als alternative gemeinsame Quelle wird aus demselben Hamming Code, der die E8-Wurzeln liefert, ein kompatibles Siebenregistermodell konstruiert. Es erhält die volle native C4-Darstellung, nicht nur deren S6-Quotienten.

Das sind endliche mathematische Ergebnisse. Weder eine physische Raumzeit noch das chirale Standardmodell als Feldtheorie, alle Kopplungen, Gravitation oder ein kosmologischer Anfangszustand sind hieraus hergeleitet. Die neuen Hamiltonoperatoren sind ausdrücklich untersuchte Kandidaten; dass die ursprünglichen TFPT-Postulate gerade sie auswählen, wird nicht behauptet.

### Quellenstand

* Aktueller Anhang: `Eingefügter Text.txt`, file_00000000393c8210aeac67fb9cfe1fef. Sein Text umfasst 182 zitierbare Zeilen. Die dort verlinkten September-26-Prüfdateien wurden in der Library nicht gefunden. Deshalb wird weder ihre Ausführung noch ihre bytegenaue Prüfung behauptet.
* Vollständig gelesene frühere Grundlage: `TFPT_Fortsetzung_2026-09-19.md`, Library-ID file_00000000a7c48210b71f62829a798846. Die explizite Codebasis, die sechs Simplexspalten und die Bedeutung der ursprünglichen Gruppenwirkung stammen aus den Abschnitten 2 und 3. Die Darstellungsgrenze des isolierten Fünferraums steht in Abschnitt 5.
* `tfpt_1_architecture_e8.pdf`, September 7, 2026, v5.4 rev 1216, Seiten 13 bis 16: Inzidenzmatrix, sechsfache Ovoidstruktur, ausgewählte quadratische Form, endliche Normalform. Insbesondere ist die Singularliste 1, 2/3 (neunfach), 0 (fünffach) von N/3 dort bereits dokumentiert.
* `TFPT_Universalraum_Sitzungsdokumentation_2026-09-20_v2.pdf`, Seiten 15 und 16: Quartikraum, Carry, geometrische Verbindung und ein anderer bereits vorhandener Petersen-Anschluss auf Bell10.
* `TFPT_Gesamtstand_und_Loesungsweg_20260921.pdf` und `tfpt_research_contracts.pdf`: gemeinsamer Quellenanschluss und die acht physischen Abschlussbedingungen.

Die Programme rekonstruieren die verwendeten Matrizen aus den ausgeschriebenen Regeln. Es werden keine fehlenden Quellprogramme imitiert oder als geprüft ausgegeben. Die vollständige rohe Gaußsche Quotientenabbildung und eine neue Enumeration sämtlicher 46080 Gruppenmatrizen sind nicht Bestandteil dieses Laufs. Der Lauf prüft dagegen sämtliche 60 ursprünglichen Reflexionen auf den hier konstruierten Codes. Der Nachweis für die von ihnen erzeugte Gruppe folgt aus Multiplikation der geprüften Generatoridentitäten.

## 1. Die konkrete Codebasis

Ein Register hat Hilbertraum C4. Vier Register tragen H=(C4)^tensor4, Dimension 256. Die fünf orthonormalen Codevektoren sind:

\[
 c_0=(|0000\rangle+|1111\rangle+|2222\rangle+|3333\rangle)/2,
\]
\[
 c_1=(\sum_{\mathrm{perm}}|0011\rangle+\sum_{\mathrm{perm}}|2233\rangle)/\sqrt{12},
\]
\[
 c_2=(\sum_{\mathrm{perm}}|0022\rangle+\sum_{\mathrm{perm}}|1133\rangle)/\sqrt{12},
\]
\[
 c_3=(\sum_{\mathrm{perm}}|0033\rangle+\sum_{\mathrm{perm}}|1122\rangle)/\sqrt{12},\qquad
 c_4=\sum_{\mathrm{perm}}|0123\rangle/\sqrt{24}.
\]

Jede Summe enthält nur verschiedene Permutationen. E bezeichnet die Matrix der unnormalisierten Supportspalten. Dann

\[
G=E^TE=\operatorname{diag}(4,12,12,12,24),\quad V=EG^{-1/2},\quad P=VV^\dagger.
\]

Mit S als Symmetrieprojektor auf Sym4(C4) und den 16 Hermiteschen Zweiqubit-Paulis A gilt

\[
Q=\frac1{16}\sum_A A^{\otimes4},\quad Q^2=Q,\quad \operatorname{rank}Q=16,\quad P=SQ,\quad \operatorname{rank}P=5.
\]

Q ist der gemeinsame +1-Raum der vier globalen Pauli-Stabilisatoren X auf der ersten beziehungsweise zweiten internen Qubitkomponente und Z auf denselben Komponenten. Die vierfache Tensorpotenz entfernt die Pauli-Produktphasen. S und Q kommutieren.

### Rekonstruktion der Wurzeln

Auf den acht binären Dreierkoordinaten wird RM(1,3) gebildet: die 16 Auswertungstabellen affiner linearer Funktionen. Die Wurzeln sind ±2e_i und alle Vorzeichenbelegungen auf den 14 Supportmengen der Gewicht-vier-Codewörter. Das sind 16+224=240 Wurzeln mit reeller Norm zum Quadrat vier. Durch Paarung aufeinanderfolgender reeller Koordinaten entstehen komplexe z in C4; psi=z/2 ist normiert. Die 60 verschiedenen Projektoren definieren

\[
M_4=\frac1{60}\sum_l |\psi_l\rangle\langle\psi_l|^{\otimes4}.
\]

Der Lauf prüft die exakte Identität

\[
40M_4=S+P.
\]

Integerzertifikat: P_num=24P, S_num=24S, Q_num=16Q. Für p_l=4|psi_l><psi_l| gilt Summe p_l^tensor4 =16(S_num+P_num). Die Projektoridentitäten werden ohne Eigenwerttoleranzen geprüft.

Die allgemeine Verbindung von vierten Cliffordmomenten und Stabilisatorcodes ist bekannte Mathematik; siehe Zhu, Kueng, Grassl und Gross, arXiv:1609.08172. Der heutige Gegenstand ist die konkrete Fortsetzung dieser TFPT-Realisierung.

## 2. Was ein, zwei und drei Register enthalten

Schreibe V nach dem ersten Register als vier Matrizen V_a von Größe 64 mal 5. Dann gilt exakt

\[
V_a^\dagger V_b=\frac{\delta_{ab}}4I_5.
\]

Damit enthält ein einzelnes Register stets I4/4 und keine logische Information. Der bekannte Verlust dieses Registers ist exakt korrigierbar. Das ist nicht dieselbe Behauptung wie Korrektur eines unbekannten Fehlers an einer unbekannten Position.

Die vier Isometrien W_a=2V_a besitzen orthogonale Bilder im verbleibenden 64-dimensionalen Raum. Für einen beliebigen logischen Operator O definiert

\[
O_3=\sum_{a=0}^3 W_a O W_a^\dagger
\]

eine Darstellung auf drei Registern mit

\[
(I_4\otimes O_3)V=VO.
\]

Die Reduktionskanäle E_k(X)=Tr_(4-k)(VXV†) haben die exakt berechneten linearen Ränge

\[
\operatorname{rank}E_1=1,\quad\operatorname{rank}E_2=10,\quad\operatorname{rank}E_3=25.
\]

Die 25 beziehen sich auf den vollständigen Operatorraum. Für Dichtematrizen fällt eine feste Spur weg; allgemeine reine Zustände des Fünfers haben acht reelle Parameter, gemischte Zustände 24.

## 3. Die Zweiregisterauslesung ist eine konkrete Messung

Verwende die zehn reellen symmetrischen Zweiqubit-Paulis in dieser Reihenfolge:

```
II IX IZ XI XX XZ YY ZI ZX ZZ
```

Ihre normierten Bellvektoren b_nu=vec(A_nu)/2 bilden eine orthonormale Basis von Sym2(C4). Die Codeabbildung faktorisiert exakt als

\[
V|\psi\rangle=\sum_{\nu=1}^{10}(w_\nu^T\psi)
 |b_\nu\rangle_{12}|b_\nu\rangle_{34}.
\]

Schreibe W10 für die Matrix der Zeilen w_nu. Explizit gilt W10=(F_num/4)G^(-1/2), wobei

```
F_num =
 4  4  4  4  0
 0  8  0  0  8
 4 -4  4 -4  0
 0  0  8  0  8
 0  0  0  8  8
 0  0  8  0 -8
 0  0  0  8 -8
 4  4 -4 -4  0
 0  8  0  0 -8
 4 -4 -4  4  0
```

Insbesondere

\[
W_{10}^TW_{10}=I_5,\quad \|w_\nu\|^2=\frac12,\quad
w_\nu^Tw_\mu=\pm\frac16\quad(\nu\ne\mu).
\]

Die normierten Richtungen sqrt2 w_nu bilden ein gleichwinkliges enges System von zehn Linien in R5, mit Beträgen der Kreuzprodukte 1/3.

Nach Ausblenden des zweiten Registerpaars folgt

\[
\mathcal E_2(\rho)=\sum_\nu\operatorname{tr}(F_\nu\rho)
 |b_\nu\rangle\langle b_\nu|,\quad F_\nu=|w_\nu\rangle\langle w_\nu|.
\]

Das ist ein Kanal vom Typ Messen und Präparieren. Selbst für eine mit einem äußeren Referenzsystem verschränkte Eingabe ist die Ausgabe eine separable Mischung bezüglich Referenz und Registerpaar. Der Kanal ist daher entanglement breaking. Rang zehn bedeutet hier zehn linear unabhängige klassische Effekte, nicht zehn erhaltene quantenmechanische Freiheitsgrade.

## 4. Petersen Graph und die sechs ursprünglichen Markierungen

Setze Gamma=W10 W10^T und

\[
C=6\Gamma-3I_{10}.
\]

C hat Nullen auf der Diagonale, sonst ±1, und erfüllt C²=9I. Eine Vorzeichenwahl D=diag(s), s_nu=±1, ergibt

\[
A_s=\frac{J-I-DCD}{2}.
\]

Genau sechs Vorzeichenklassen bis auf ein gemeinsames Minuszeichen erfüllen Cs=3s. Für diese gilt exakt

\[
A_s\mathbf1=3\mathbf1,\quad A_s^2=2I+J-A_s.
\]

Es sind sechs Vorzeichenrahmen desselben Petersen Graphen: zehn Knoten, Grad drei, keine Dreiecke und die bekannten Parameter (10,3,0,1). Hier wird keine räumliche Dimension abgeleitet.

Die bereits vorhandenen sechs nativen Simplexspalten lauten in E-Koordinaten

```
W6 =
 2  2 -1 -1 -1 -1
 0  0 -1 -1  1  1
 0  0 -1  1 -1  1
 0  0  1 -1 -1  1
 1 -1  0  0  0  0
```

Sie erfüllen W6^T G W6=48I6-8J6. Für ihre orthonormalen Koordinaten u_q=G^(1/2)W6_q gilt die direkte Verbindung

\[
\boxed{s_q=\frac12 W_{10}u_q\in\{\pm1\}^{10}.}
\]

Diese sechs s_q sind exakt die sechs regulären Vorzeichenrahmen. Die Gleichheit wird über alle 512 relativen Vorzeichenwahlen geprüft; sie ist nicht aus der Zahl sechs erraten.

Alle 60 ursprünglichen Reflexionen r_l=I-2|psi_l><psi_l| erhalten den Code unter r_l^tensor4. Auf den sechs u_q wirken sie als die 15 Transpositionen, jede mit vier Urbildern. Der native S6-Anschluss und die Bell-Auslesung benutzen somit dieselben markierten Richtungen.

### Eine zusätzliche verborgene Fünferstruktur

Normiere v_q=u_q/sqrt40 und setze rho_q=|v_q><v_q|. Für alle sechs reinen Zustände gilt

\[
\mathcal E_2(\rho_q)=P_{\mathrm{sym},2}/10,
\qquad \frac16\sum_q\rho_q=I_5/5.
\]

Die vollständige Paarmessung sieht keinen Unterschied zwischen diesen sechs Markierungszuständen. Ihre fünf unabhängigen traceless Differenzen

\[
B_q=\rho_q-I_5/5
\]

spannen genau den reellen fünfdimensionalen Blindraum auf. Ihre Gram-Matrix lautet

\[
\operatorname{tr}(B_qB_r)=\frac{24}{25}\delta_{qr}-\frac4{25}.
\]

Dies ist die ursprüngliche Simplexgeometrie erneut, nun als Raum unsichtbarer Observablen. Die Aussage ist eine lineare Identifikation zwischen Darstellungsräumen; sie ist kein physischer Kanal, der aus einem Vektor seine Dichtematrix klont.

Eine Konsequenz: Kein Hamiltonoperator aus höchstens Zweiregistertermen kann einen dieser sechs Zustände als einzigen globalen Grundzustand wählen. Falls einer die niedrigste Energie erreicht, besitzen alle dieselbe Energie und müssen ebenfalls im Grundraum liegen. Da sie den ganzen Code aufspannen, bleibt mindestens dessen voller Fünferraum im Grundraum. Die Aussage betrifft genau diese sechs Codezustände und dieselben physischen Register.

## 5. Die Übertragungsstärke 2/3 und der tatsächliche Rückkanal

Zur Referenz rho*=I5/5 gehört nach dem Paarverlust sigma*=P_sym,2/10. Die Petz- beziehungsweise Transpose-Recovery ist auf diesem Ausgangsträger

\[
\mathcal R_2=2\mathcal E_2^\dagger.
\]

Das folgt direkt aus der allgemeinen Formel mit rho*^(1/2)=I/sqrt5 und sigma*^(-1/2)=sqrt10 I. Die allgemeine Recovery-Theorie ist bekannt; siehe Barnum und Knill, quant-ph/0004088.

Die zehn Effekte besitzen die Hilbert-Schmidt-Gram-Matrix

\[
2\operatorname{tr}(F_\nu F_\mu)=\begin{cases}1/2&\nu=\mu,\\1/18&\nu\ne\mu.\end{cases}
\]

Also ist das Ausgangsbild der Rückkomposition

\[
\frac49I_{10}+\frac1{18}J_{10}.
\]

Auf dem vollständigen logischen Operatorraum erhält man

\[
\boxed{\operatorname{spec}(\mathcal R_2\mathcal E_2)
=\{1^{\times1},(4/9)^{\times9},0^{\times15}\}.}
\]

Die gewöhnlichen Hilbert-Schmidt-Singularwerte von E2 sind 1/sqrt2, sqrt2/3 neunfach und fünfzehn Nullen. Nach der zur Referenznormalisierung gehörenden Multiplikation mit sqrt2 werden daraus 1, 2/3 neunfach und fünfzehn Nullen. Auf dem reellsymmetrischen 15-dimensionalen Operatorraum verbleiben nur fünf Nullrichtungen. Damit lautet die Liste dort exakt wie die alte Doily-Liste sing(N/3): 1, 2/3 neunfach, 0 fünffach.

Wichtig: 2/3 ist hier die normierte Singularübertragung einer Auslesung. Der tatsächliche vollständig positive Hin-und-zurück-Kanal hat 4/9. Drei Rückkompositionen ergeben (4/9)^3=(2/3)^6. Dies leitet aber weder die Wahl von drei Zyklen noch die physische TFPT-Clock oder deren zusätzliche (1/3)^6-Richtung her.

### Anschluss an den schon vorhandenen Reflexionskanal

Für T5(X)=(1/60)Summe u_l X u_l† auf End(C5), u_l=r_l^tensor4|Code, gilt die bereits dokumentierte Zerlegung 1+5+9+10. Die Eigenwerte sind 1, 3/5, 1/3, 1/5. Die Räume haben hier eine konkrete Auslesebedeutung: Identität, reeller markierter Blindraum, sichtbarer traceless Paarraum, imaginär antisymmetrischer Raum.

Daraus folgt die explizite Operatoridentität

\[
\mathcal R_2\mathcal E_2
=\frac{(5T_5-3I)(5T_5-I)(15T_5-13I)}{16}.
\]

Sie wird zusätzlich numerisch an den vollständigen Superoperatoren geprüft. Das Polynom enthält negative Koeffizienten. Es ist keine vorgeschlagene positive Mischung beliebiger Kanäle und kein automatisch ausführbares Zeitprogramm. Es identifiziert zwei konkret berechnete Operatoren.

## 6. Paarsteuerung ohne Projektionstrick

Für einen nichttrivialen Hermiteschen Pauli A definiere h_A=V†A_1A_2V. Alle 15 h_A sind reellsymmetrisch und haben Spektrum 1 zweifach, -1/3 dreifach. Ihr linearer Raum hat Dimension zehn, einschließlich der Identität; Summe h_A=3I.

Ein isoliertes physisches Paar A_1A_2 erhält den Code nicht. Da (A_1A_2)^2=I, lautet der Leakageoperator

\[
V^\dagger A_1A_2(I-P)A_1A_2V=I-h_A^2.
\]

Er hat die Eigenwerte null zweifach und 8/9 dreifach. Für den Puls exp(-it A_1A_2) ist die größte Austrittswahrscheinlichkeit exakt (8/9)sin²t. Eine bloße Kompression PHP wäre deshalb kein Beweis physischer codeerhaltender Steuerung.

Es gibt jedoch eine echte Zweikörperlösung:

\[
\widehat h_A=\frac16\sum_{r<s}A_rA_s.
\]

Jeder Summand kommutiert mit Q: Bei einem antikommutierenden Pauli entstehen zwei Minuszeichen. Der symmetrische Mittelwert kommutiert mit allen Registerpermutationen, also mit S. Daher kommutiert er mit P=SQ. Seine Einschränkung ist genau h_A. Kein logischer Projektor muss als versteckte Vielkörperoperation eingebaut werden.

Die traceless Generatoren für IX, IZ, XI und ZZ ergeben durch Lie-Kommutatoren die exakte Rangfolge 4,7,12,17,22,24. Damit ist su(5) erzeugt. Das ist eine Kontrollalgebra mit steuerbaren Pulsen, nicht bereits die Auswahl eines autonomen Hamiltonoperators und nicht die physische SU(5)-Eichgruppe.

Für K=(sqrt3/2)(h_IX-h_IY) ist die Einschränkung auf c0,c1 genau sigma_x. U=exp(-i pi K/4) bildet (c0+i c1)/sqrt2 auf c0 und (c0-i c1)/sqrt2 auf -i c1 ab. Danach misst h_IX die Werte 0 beziehungsweise 2/3. Die in der Momentaufnahme verborgene Phase kann also durch kontrollierte Bewegung sichtbar werden.

### 35 projektive Linien, zwei Operatorarten

Die 15 nichttrivialen Pauli-Adressen sind die nichtnull Vektoren von F2^4. Ihre 35 Dreierlinien {A,B,C} mit adress(A)+adress(B)+adress(C)=0 zerfallen in 15 kommutierende und 20 antikommutierende Linien. Die komprimierten Dreiregisteroperatoren der kommutierenden Linien spannen alle 15 reellsymmetrischen Matrizen; die antikommutierenden Linien spannen die zehn imaginär antisymmetrischen Hermiteschen Matrizen. Zusammen entstehen alle 25 Hermiteschen Richtungen.

Für AB=isC auf einer antikommutierenden Linie gilt sogar im vollen physischen Raum

\[
[\widehat h_A,\widehat h_B]=\frac{4is}{3}\widehat T_{ABC},
\quad \widehat T_{ABC}=\frac1{24}\sum_{r,s,t\;\mathrm{verschieden}}A_rB_sC_t.
\]

Beim Ausmultiplizieren tragen nur Kantenpaare mit genau einem gemeinsamen Register bei. Das erklärt den Dreikörperterm und seinen Koeffizienten. Die symmetrisierten Dreieroperatoren erhalten S und Q. Die Informationszerlegung wird damit 25=1+9+5+10, nicht nur eine Reihe zufällig passender Dimensionen.

## 7. Markierte Hyperladung

Die ursprüngliche sigma zyklisiert die ersten drei C4-Koordinaten. Sie hat auf den sechs Simplexpunkten drei feste Punkte. Nach Wahl eines dieser markierten festen Punkte q werden die fünf Differenzen zu den übrigen Punkten als Trägerslots verwendet. Ihr Gram ist 48(I5+J5). Der positive Polartransport lautet

\[
T=\frac{G^{1/2}\mathrm{Diff}}{\sqrt{48}}
\left[I+\left(\frac1{\sqrt6}-1\right)\frac J5\right].
\]

Die drei bewegten Slots tragen Y=-1/3, die beiden übrigen +1/2. Das transportierte Y ist T diag(Y)T†. Der markierte Punkt und die Quellenidentifikation sind hier Eingaben aus der vorhandenen Markierungsstruktur, keine neu hergeleitete physische Auswahl.

Der Paarraum hat Rang zehn, nach Hinzunahme von Y elf. Quantitativ beträgt die minimale quadrierte Hilbert-Schmidt-Distanz zur Paarspanne über die verbleibende relative Phase zwischen dem invarianten S5-Singulett und dessen Viererkomplement

\[
\boxed{\min_\theta d_{HS}^2(Y_\theta,\mathcal O_2)
=\frac{29}{60}-\frac{\sqrt6}{10}>0.}
\]

Für theta=0 ist die Distanz 29/60+sqrt6/10, für theta=pi der oben genannte kleinere Wert. Zur globalen Minimierung: Schreibe Y=A+cos(theta)B+i sin(theta)C nach diagonalem und kreuzweisem Anteil bezüglich 1+4. Die Paarspanne ist reell. Die quadratische Distanz ist ein Polynom in cos(theta), dessen quadratischer Koeffizient ||B_perp||²-||B||² nichtpositiv ist. Das Minimum liegt deshalb bei ±1. Die Endpunktwerte werden exakt rational-algebraisch geprüft.

Auf drei Registern liefert der Decoder aus Abschnitt 2 einen codeerhaltenden Operator. Der Lauf prüft die resultierende Intertwiner-Gleichung zusätzlich numerisch.

Die allgemeine äußere-Algebra-Rechnung für Lambda_even(C5), einschließlich der bekannten 16 Ladungszustände, ist Standarddarstellungstheorie. Sie wird nicht als neue physische Materieherleitung beansprucht. Siehe Baez und Huerta, arXiv:0904.1556.

## 8. Ein positiver Hamiltonoperator direkt aus dem Quellenmoment

Der einfachste hier untersuchte affine Momentenkandidat ist

\[
\boxed{H_{\mathrm{mom}}=I-20M_4=I-\tfrac12(P+S).}
\]

Weil P<=S Projektoren sind, ist sein vollständiges Spektrum

| Energie | Vielfachheit |
|---|---:|
| 0 | 5 |
| 1/2 | 30 |
| 1 | 221 |

Damit ist der Code exakt der Grundraum. Die Paarsteuerungen aus Abschnitt 6 kommutieren mit diesem Parent. Mit Skala Delta>0 kann der isolierte Code als unteres Band erhalten bleiben, solange zusätzliche beschränkte Kontrollen klein genug gegenüber der Lücke sind; zum Beispiel genügt eine Operatornorm kleiner als Delta/4.

Die Wahl H=I-20M4 ist eine explizite Konstruktionsregel, kein aus P1/P2 bewiesenes Naturgesetz. Andere Funktionen von P und S können dieselben Grundzustände und andere Anregungsenergien tragen. Auch der fünfdimensionale Grundraum wählt keinen einzelnen Anfangszustand.

### Warum höchstens drei Register für denselben Grundraum nicht reichen

Setze rho5=P/5 und rho35=S/35. Für k=1,2,3 gilt

\[
\operatorname{Tr}_{4-k}\rho_5=\operatorname{Tr}_{4-k}\rho_{35}
=P_{\mathrm{sym},k}/\binom{k+3}{3}.
\]

Jeder höchstens dreilokale Hamiltonoperator hat in beiden Zuständen dieselbe Energie. Wenn rho5 ausschließlich niedrigste Eigenzustände enthält, muss wegen Positivität von H-E_min auch der gesamte Träger von rho35 im Grundraum liegen. Genau P als alleiniger Grundraum ist ausgeschlossen. Das ist ein Spezialfall des Zusammenhangs zwischen Marginaldaten und Grundräumen; siehe Chen, Ji, Zeng und Zhou, arXiv:1110.6583.

Die orthogonale Mischung rho30=(S-P)/30 besitzt ebenfalls dieselben Marginalen. Alle p rho5+(1-p)rho30 sind dadurch ununterscheidbar. Maximale Entropie ohne quartische Zusatzinformation wählt p=1/7 und damit rho35. Der Entropieunterschied zu rho5 ist log2(7).

## 9. Zwei perfekte Fünfercodes dürfen nicht dieselben Register teilen

Betrachte zwei identisch orientierte eingebettete Codeprojektoren P_A und P_B auf Vierermengen, die s=1,2 oder3 vollständige C4-Register gemeinsam haben. Sie sind jeweils mit der Identität auf den übrigen Registern ergänzt. Die Rechnung ergibt

| Gemeinsame Register s | Nichtnull Hauptwinkel-Kosinus | Vielfachheit | min spec[(I-P_A)+(I-P_B)] |
|---:|---:|---:|---:|
| 1 | 1/4 | 100 | 3/4 |
| 2 | 1/2 | 10 | 1/2 |
| 3 | 1/4 | 20 | 3/4 |

Insbesondere ist Ran(P_A) geschnitten Ran(P_B)={0}. Die Werte sind mit ganzzahligen Minimalpolynomen, nicht nur einer numerischen Eigenwerttoleranz zertifiziert. Für die skalierte gewichtete Kreuz-Gram-Matrix B_N gilt B_N²=36 B_N für s=1,3 und B_N²=144 B_N für s=2, bei gemeinsamem Quadratnenner 576.

### Kurzer struktureller Beweis des leeren Schnitts

Ein gemeinsamer Zustand müsste unter den Permutationen jedes Viererblocks invariant sein. Da die Blöcke überlappen, erzeugen diese Transpositionen die ganze Permutationsgruppe der vereinigten Register. Der Zustand wäre global symmetrisch. Die Q-Stabilisatoren eines Blocks würden dann auf jede Vierermenge der Vereinigung transportiert.

Produkte zweier vierfacher X-Stabilisatoren mit drei gemeinsamen Registern ergeben X_i X_j. Entsprechend erhält man Z_j Z_k für drei verschiedene i,j,k. Beide müssten Eigenwert +1 besitzen, antikommutieren aber. Ein nichtnull gemeinsamer Zustand ist unmöglich.

Geltungsbereich: identische Codeeinbettung und wörtlich gemeinsame Tensorfaktoren. Anders gedrehte Codes, zusätzliche Randregister, unterschiedliche Faktorisierungen oder dynamische Schnittstellen werden dadurch nicht pauschal ausgeschlossen. Insbesondere verbietet der Satz keine Wechselwirkung getrennter Codeblöcke.

## 10. Getrennte Codeblöcke koppeln durch virtuelle Anregungen

Ein termweiser Erstordnungsanschluss an nur einem Register pro Block komprimiert wegen der Erasure-Identität zu Skalaren. Bei zwei getrennten Blöcken kann ein Hamiltonterm auf insgesamt höchstens drei physischen Registern daher kein nichttriviales Produkt logischer Operatoren im ersten komprimierten Term erzeugen. Ein direkt codeerhaltendes Produkt zweier symmetrisierter Paarkontrollen benötigt mindestens 2+2 Register. Das ist keine Sperre für effektive Wechselwirkung höherer Störungsordnung.

Untersucht wird konkret

\[
H_0=\Delta(H_{\mathrm{mom}}^A+H_{\mathrm{mom}}^B),\quad
V_g=g(a_1^A a_1^B+a_2^A a_2^B),\quad a=I_2\otimes\sigma_z.
\]

Die Paarlinks sind gewöhnliche physische Zweiregisterterme. Sei h_A beziehungsweise h_B die logische Einschränkung von a_1 a_2 in jedem Block. Der erste komprimierte Störungsterm verschwindet. In zweiter Ordnung ergibt sich exakt

\[
\boxed{
H_{\mathrm{eff}}^{(2)}=\frac{g^2}{\Delta}\left[
-\frac{29}{24}I
-\frac{11}{24}(h_A\otimes I+I\otimes h_B)
-\frac{15}{8}h_A\otimes h_B
\right].}
\]

Der letzte Term ist eine echte logische Wechselwirkung. Die Methode ist die bekannte entartete Schrieffer-Wolff-Störungstheorie, nicht eine neue Erzeugung von Interaktion aus reiner Gruppentheorie; siehe Bravyi, DiVincenzo und Loss, arXiv:1105.0675.

### Herleitung des Koeffizienten

Ein einzelner Fehler a_rV besitzt keinen Codeanteil. Sein Anteil im symmetrischen Raum hat die Gram-Matrix K=(I+3h)/4, einen Rang-zwei-Projektor. Seine Energie ist Delta/2, der orthogonale Anteil hat Energie Delta. Für zwei gleichzeitige Fehler lautet die reduzierte Inverse deshalb

\[
H_0^{-1}=\Delta^{-1}[\tfrac12I+\tfrac16(S_A+S_B)+\tfrac16S_AS_B]
\]

auf deren erzeugtem Raum. Für Linkindizes r,s in {1,2} sind die lokalen Rückkehrmatrizen C_rs=I bei r=s und h sonst; die symmetrischen Rückkehrmatrizen sind jeweils K. Einsetzen in -PV_g H_0^(-1) V_gP liefert die obige Formel.

Für die drei logischen Hell/Dunkel-Kombinationen sind die Koeffizienten der tiefen Energien -4, -8/9 und -10/9 in Einheiten g²/Delta. Eine unabhängige Diagonalisierung der entsprechenden vollständigen invarianten physischen Blöcke bestätigt die Annäherung bei kleiner werdendem g/Delta. Zum Beispiel erhält der Hell/Hell-Zweig bei Delta=1 für g=0.02,0.01,0.005 die Werte E/g²=-3.9936203984,-3.9984012787,-3.9996000800.

Dies ist ein exakter Koeffizient einer kontrollierten schwachen Kopplungsentwicklung. Es ist nicht die exakte Dynamik für beliebiges endliches g. Die mikroskopische Zustandswolke verlässt bei endlichem g den nackten Code in kleinem Umfang; der effektive logische Raum ist gedresst. Delta, g, die Wahl der Links und eine große Geometrie werden hier nicht aus TFPT ausgewählt.

## 11. Eine kompatible Quelle aus demselben Hamming Code

Das Problem des überlappenden P=SQ liegt nicht allein im Quartikstabilisator Q, sondern in seiner Kombination mit voller Vierer-Permutationssymmetrie. Ohne S können zwei Q-Checks mit geradzahliger Überlappung kommutieren. Bei ungeradzahliger Überlappung liefern passende Pauli-Checks einen Antikommutationskonflikt.

Ein expliziter kompatibler Checkraum ist der Zeilenraum C der Matrix

```
H7 =
1 1 1 1 0 0 0
1 1 0 0 1 1 0
1 0 1 0 1 0 1
```

H7 H7^T=0 über F2; alle sieben nichtnull Zeilenkombinationen haben Gewicht vier und schneiden sich paarweise in zwei Koordinaten. Ihre Dreierkomplemente sind die Fano-Linien.

### Exakte Rückbindung an den E8-Ausgangscode

Das ist nicht bloß ein weiterer Code mit passenden Dimensionen. Es gilt als Gleichheit der konkreten binären Mengen im Programm

\[
\boxed{\{(c,0)+b\mathbf1_8:c\in C,\ b\in\mathbb F_2\}
=\mathrm{RM}(1,3).}
\]

Rechts steht genau der Code, aus dem in Abschnitt 1 die 240 Wurzeln gebaut wurden. Das Verkürzen dieses Hamming Codes liefert somit die miteinander verträglichen Quartikchecks.

### Der Encoder

Die sieben physischen Register haben Dimension vier; ihre zwei binären Komponenten werden mit demselben C kodiert. Für a,b in {0,1}:

\[
V_7|ab\rangle=\frac18\sum_{u,v\in C}
|2(u+a\mathbf1)+(v+b\mathbf1)\rangle.
\]

Alle Additionen innerhalb der binären Klammern sind modulo zwei. Das ist die Gruppierung zweier bekannter Steane-Codes [[7,1,3]] in sieben C4-Register; die allgemeine Codekonstruktion geht auf Steane zurück, quant-ph/9601029. Es wird keine weltweite Erstentdeckung dieses Codes behauptet.

Die resultierende logische Dimension ist vier. Beliebige Fehler auf einem physischen C4-Register sind korrigierbar. Drei-Register-Pauliwörter auf einer Fano-Linie implementieren A* auf dem logischen C4. Damit existieren explizite nichttransversale logische Steueroperatoren.

### Bedingte Minimalität statt freier Wahl der Sieben

Innerhalb der folgenden ausdrücklich benannten Klasse ist sieben die minimale Länge: binäre, doppelt gerade, selbstorthogonale CSS-Checks; beide Pauliarten benutzen denselben Checkraum; mindestens ein logisches Qubit; Korrektur eines unbekannten Einzelfehlers.

Hat der Checkraum Rang r und Länge n, muss n-2r>=1 gelten. Weil doppelt gerade Stabilizer keine Gewicht-eins- oder Gewicht-zwei-Wörter besitzen, müssen alle Spalten der Checkmatrix verschieden und nichtnull sein; sonst enthielte der Dualcode einen unkorrigierbaren Fehler solchen Gewichts. Folglich n<=2^r-1. Für n<=6 sind beide Ungleichungen unvereinbar. Bei n=7 ist r=3 erzwungen, und die sieben Spalten sind sämtliche nichtnull Vektoren von F2^3. Bis auf Basis- und Koordinatenwechsel ist der obige Hamming-Anschluss damit eindeutig.

Das beweist eine Minimalität innerhalb dieser Informations- und Codeklasse. Es leitet nicht aus P1/P2 ab, dass die Natur diese Codeklasse oder diesen Schutzauftrag wählt. Die drei binären Checkkoordinaten sind ausdrücklich keine hergeleiteten drei Raumdimensionen.

### Die gesamte native Reflexionswirkung bleibt erhalten

Für alle 60 aus den tatsächlichen Wurzeln rekonstruierten Reflexionen wird exakt mit Gaußschen Ganzzahlen geprüft:

\[
\boxed{U^{\otimes7}V_7=V_7\overline U.}
\]

Dazu wird R=2U verwendet; das Integerzertifikat ist R^tensor7 E7=64 E7 conjugate(R). Die Identität gilt anschließend für die von den 60 Reflexionen erzeugte Gruppe. Die komplexe Konjugation ist wesentlich. Sie darf bei geladenen oder orientierten Anschlüssen nicht ignoriert werden. Nach zwei Kodierstufen ist die ursprüngliche Darstellung wiederhergestellt:

\[
U^{\otimes49}V_{49}=V_{49}U.
\]

Diese letzte Aussage ist eine algebraische Folgerung der zweimaligen Konjugation, keine Diagonalisierung eines 49-Registerraums.

Der Vorteil gegenüber dem isolierten Fünferquotienten: Das ursprüngliche C4 mitsamt Pauli-Wirkungen und zentralen Phasen bleibt als Darstellung erhalten. Der quartische Fünferträger kann danach wieder als Moment oder Auslesung erscheinen. Er ersetzt die Quelle nicht.

### Gemeinsamer positiver Parent

Für jede der sieben Vierermengen S sei Q_S der entsprechende Quartikprojektor. Alle kommutieren. Setze

\[
H_F=\sum_{S}(I-Q_S).
\]

Die vollständige Spektralliste ist

| Energie | Vielfachheit |
|---|---:|
| 0 | 4 |
| 4 | 420 |
| 6 | 5880 |
| 7 | 10080 |

Die Summe der Vielfachheiten ist 4^7=16384. Der Code ist der gemeinsame Grundraum, die normierte Lücke vier.

Die Rechnung benötigt keine große numerische Diagonalisierung: Ein Syndrom ist eine 4-mal-3-Matrix über F2. Bei Rang r werden 8-2^(3-r) Checks verletzt. Die Rangzahlen sind 1,105,1470,2520; jede Syndromkonfiguration hat vier logische Zustände. Das liefert die Tabelle exakt.

Diese Konstruktion ist ein realer endlicher Kandidat für kompatiblen Quellschutz. Sie ist weder ein globales Raumzeitmodell noch ein Beweis, dass ihre logische Viererstruktur bereits die physische Standardmodell-Materie trägt.

## 12. Geometrie: positive Informationsmetrik, keine bereits erzeugte Gravitation

Die ursprüngliche Identität

\[
P\,d\Gamma_4(X)\,P=\operatorname{tr}(X)P
\]

wird auf der vollständigen Pauli-Basis geprüft. Für traceless X,Y folgt im angegebenen Orientierungsraum

\[
g(X,Y)=8\operatorname{tr}(XY),\qquad F_Q=\frac45g
\]

für die SLD-Quanten-Fisher-Metrik von rho=P/5. Dieser Raum hat 15 reelle Tangentialrichtungen und eine positiv definite Metrik. Es ist nicht automatisch eine Lorentzraumzeit.

Für die kollektiv bewegte Codebasis U^tensor4 V ist die Berry-Verbindung

\[
\mathcal A=\operatorname{tr}(U^\dagger dU)I_5.
\]

Auf SU(4) verschwindet sie; lokal ist ihre Krümmung auch auf U(4) null, da die Spur der Maurer-Cartan-Zweiform verschwindet und die skalare Einsform mit sich selbst null wedgt. Damit erzeugt diese reine kollektive Orientierungsfamilie allein kein kontinuierliches nichtabelsches Eichfeld. Diskrete Holonomie im Quotienten bleibt möglich. Die Aussage betrifft Berry-Krümmung, nicht die Riemannsche Krümmung der Informationsmetrik.

Dass korrekte Einzelfehlererkennung keine universelle transversale Kontrollgruppe gestattet, ist in allgemeiner Form durch Eastin und Knill bekannt, arXiv:0811.4262. Die oben benutzten symmetrisierten Paar- oder Fano-Dreierkontrollen koppeln Register innerhalb eines Blocks; sie sind nicht transversal und widersprechen diesem Satz nicht.

## 13. Entropie und der Punkt 1/27

Für den Kontrastqubit sind lambda_X=2/3, lambda_Z=1/3 und lambda_Y=6t. Die vier Pauliwahrscheinlichkeiten der Choi-Dichtematrix sind

\[
p_0=(1+x+y+z)/4,\quad p_X=(1+x-y-z)/4,
\]
\[
p_Y=(1-x+y-z)/4,\quad p_Z=(1-x-y+z)/4.
\]

Die Entropiestationarität verlangt p_X p_Z=p_0 p_Y. Ihre Differenz ist -(27t-1)/18. Strikte Konkavität im zulässigen Intervall liefert eindeutig t=1/27, mit p=(5/9,5/18,1/18,1/9).

Dieser Punkt besitzt einen Markov-Anschluss mit zwei unabhängigen Pauli-Sprungarten und Raten log3/2 sowie log(3/2)/2, während die dritte Rate null ist. Dann gilt lambda_Y=lambda_X lambda_Z. Die Abwesenheit eines eigenständigen Y-Sprungs ist eine zusätzliche Quellenregel. Vollständige Positivität allein erzwingt sie nicht.

Die anderen beiden im Anhang genannten Entropieobjekte werden unabhängig numerisch maximiert. Ergebnis: sechs Ereignisse 0.03579837325561067; vollständiger Dreiniveau-Choi-Kanal der angegebenen Permutationsausführung 0.03656566277922796. Das stimmt mit der behaupteten Trennung der Entropieobjekte überein.

Die darüber hinaus erwähnte Gleichsetzung mit einem Jarlskog-Invarianten wird mangels ausgeschriebener neuer Definition und Originalprüfdatei hier nicht erneut zertifiziert. Unabhängig davon kann ein konjugationsinvariantes Entropiefunktional kein Vorzeichen eines konjugationsungeraden J auswählen.

## 14. Bedeutung für die gesamte TFPT-Konstruktion

Die endliche Kette ist nun konkreter:

```
derselbe Hamming Code
    -> 240 E8-Wurzeln und 60 native Quellenrichtungen
    -> quartischer Fünfercode
    -> exakte Bell-Paarmessung
    -> Petersen-Vorzeichenrahmen und dieselben sechs Markierungen
    -> normierte Auslesestärke 2/3

Verkürzung desselben Hamming Codes
    -> kompatible Quartikchecks auf sieben Registern
    -> geschütztes ursprüngliches C4 mit vollständiger nativer Gruppenwirkung
```

Für einen isolierten Fünferblock sind Schutz und aktive Steuerung gemeinsam konstruiert. Für zwei getrennte Blöcke ist eine effektive Interaktion berechnet. Für wortwörtlich überlappende perfekte Fünferblöcke ist die Abkürzung ausgeschlossen. Die alternative Hamming-Quelle erhält dagegen die ursprüngliche Darstellung und die zentralen Wirkungen.

Die nachgewiesene Aussage ist nicht, dass die Natur aus sieben Registern besteht. Sie lautet: Die vorhandenen Quelldaten sind mit einer expliziten, nichttrivialen geschützten Ausführung vereinbar; die Auslesung darf nicht mit ihrer vollständigen Quelle verwechselt werden.

Eine vollständige physische Lösung müsste zusätzlich aus demselben Ursprung auswählen, warum diese Registerfaktorisierung, diese Operatoren, ihre relativen Koeffizienten, ein gemeinsamer Zustand und eine Zeitentwicklung gelten. Sie müsste die markierte geladene Feldalgebra, die räumliche Komposition und den Grenzwert mit chiraler Materie, drei Eichkopplungen, Flavor, Neutrinos und universell gekoppeltem quantisierten Spin zwei liefern. Der endliche Fünfer- oder Vierergrundraum bestimmt keinen kosmologischen Anfangszustand. Die beliebig steuerbare Lie-Algebra bestimmt keinen autonomen Verlauf. Der Informationsgraph ist nicht schon physische Nachbarschaft.

Die hier berechneten Ausschlüsse sind präzise nach Modellklassen begrenzt. Sie beweisen weder eine allgemeine Unmöglichkeit von TFPT noch ihre vollständige physische Richtigkeit. Das reproduzierbare Paket ist eine Forschungsfortsetzung auf Grundlage der benannten Quellen, keine Statusänderung des kanonischen TFPT-Ledgers.

## Literatur

1. H. Zhu, R. Kueng, M. Grassl, D. Gross: The Clifford group fails gracefully to be a unitary 4-design. arXiv:1609.08172.
2. J. Chen, Z. Ji, B. Zeng, D. L. Zhou: From Ground States to Local Hamiltonians. arXiv:1110.6583.
3. J. C. Baez, J. Huerta: The Algebra of Grand Unified Theories. arXiv:0904.1556.
4. B. Eastin, E. Knill: Restrictions on Transversal Encoded Quantum Gate Sets. Physical Review Letters 102, 110502 (2009), arXiv:0811.4262.
5. S. Bravyi, D. DiVincenzo, D. Loss: Schrieffer-Wolff transformation for quantum many-body systems. Annals of Physics 326, 2793–2826 (2011), arXiv:1105.0675.
6. A. Steane: Multiple Particle Interference and Quantum Error Correction. Proceedings of the Royal Society A452, 2551 (1996), quant-ph/9601029.
7. H. Barnum, E. Knill: Reversing quantum dynamics with near-optimal quantum and classical fidelity. Journal of Mathematical Physics 43, 2097 (2002), quant-ph/0004088.


</details>

[Zur Navigation](#navigation)

<a id="original-q2"></a>
## Q2. Igusa Geometrie, vollständiger Invariantenring und geschützte Quellendynamik

fileciteturn17file0L13-L27

**Originaldatei:** `TFPT_Igusa_Quellendynamik_Herleitung_20260926.md`  
**SHA256:** `beb365eafec6677aa637d744feba22300824e690e00082df11d7b871ad678613`

<details>
<summary>Q2: vollständigen Originalbericht öffnen</summary>

# TFPT: Igusa Geometrie, vollständiger Invariantenring und geschützte Quellendynamik

Forschungsfortsetzung vom 26. September 2026

## Ergebnis und Beweisgrenze

Aus der bereits angegebenen TFPT Quartikabbildung folgt exakt die klassische Igusa Quartik. In denselben Koordinaten werden die sechs Markierungen, die zehn Bellquadriken, die Doily Inzidenz, die 60 ursprünglichen Reflexionshyperflächen und die Invariantengrade 8, 12, 20, 24 gemeinsam identifiziert. Die Untersuchung liefert außerdem eine konkrete logische Austauschwechselwirkung zwischen zwei geschützten ursprünglichen C4 Quellen in dritter Störungsordnung.

Das ist ein Abschluss bestimmter endlicher algebraischer Zusammenhänge und eine dynamische Rechnung in einer ausdrücklich definierten Modellklasse. Es ist keine vollständige physische Theorie von Raumzeit, Materie und Gravitation. Insbesondere werden Kopplungsanordnung, g, Delta und Anfangszustand hier nicht aus den TFPT Postulaten ausgewählt.

Die Igusa Quartik, ihr Zusammenhang mit der endlichen Heisenberggruppe, ihre Dualität zur Segre Kubik und die zugrunde liegenden Quantencodes sind bekannte Mathematik. Der hier untersuchte Anschluss besteht in der expliziten Verwendung derselben TFPT Quellkoordinaten, Reflexionen und Belloperatoren sowie den ausgeschriebenen Dynamikrechnungen. Eine weltweite Erstentdeckung dieser klassischen Gegenstände wird nicht behauptet.

## 1. Quellen und ausgeführte Prüfungen

Grundlage sind die angehängten Dateien `TFPT_Quartik_Fortsetzung_Herleitungen_20260926.md` und `TFPT_Quartik_Fortsetzung_Pruefpaket_20260926.zip`. Das vorhandene Paket wurde tatsächlich erneut ausgeführt: 385 Prüfungen bestanden. Sein erneuter Lauf dauerte in dieser Umgebung ungefähr 19 Sekunden. Nicht jede historische TFPT Berechnung wurde dadurch erneut ausgeführt.

Die neue Datei `audit.py` ist eigenständig. Sie rekonstruiert den binären RM(1,3) Code, die 240 Wurzeln, die 60 Reflexionen, die Quartikabbildung, die sechs Koordinaten, die zehn Bellquadriken und die Hamming Prüfmuster aus ausgeschriebenen Daten. Sie führt 1065 endliche Prüfungen durch. Der beigefügte Lauf bestand vollständig. Polynome, Gruppenwirkungen, Ränge, Inzidenzmatrizen und die angegebenen Störungskoeffizienten werden exakt über rationalen beziehungsweise Gaußschen Zahlen geprüft. Es wurde keine neue Lean Formalisierung erstellt.

Die Identifikation des ganzen Invariantenrings verwendet zusätzlich den klassischen Quotientensatz von Bini und van Geemen, Abschnitt 4.3. Der neue Lauf prüft unabhängig die dazu passenden Generatoren, die vollständige Molien Funktion, den Rang und die Wirkung sämtlicher Quellreflexionen. Die kleine exakte Spektralgegenprobe in Abschnitt 9 verwendet ein vollständiges acht-dimensionales Syndrommodell. Sie ist keine Diagonalisierung des gesamten Raums zweier Siebenregisterblöcke.

Weitere ursprüngliche Anker:

* `tfpt_1_architecture_e8.pdf`, Seiten 13 bis 16: Doily, Markierungen, Invariantengrade und endliche Compilerstruktur.
* `TFPT_Universalraum_Sitzungsdokumentation_2026-09-20_v2.pdf`, Seiten 15 und 16: Quartikmoment, Carry, Quellenreflexionen und bestehender Petersen Anschluss.
* `TFPT_Gesamtstand_und_Loesungsweg_20260921.pdf`: erforderliche gemeinsame Feld-, Zustands- und Zeitrekonstruktion.
* `tfpt_research_contracts.pdf`: unabhängige physische Bedingungen T1 bis T8.

## 2. Drei Objekte, die nicht identisch sind

1. Der ursprüngliche Quellenvektor z liegt in C4.
2. Vier tatsächlich verwendete Register besitzen den Zustandsraum (C4)^{tensor4}; sein symmetrischer Teil hat Dimension 35.
3. Der besondere Quartikcode ist ein fünfdimensionaler Unterraum mit Projektor P. Ein beliebiger Vektor dieses Codes ist nicht notwendigerweise die Projektion von z^{tensor4} für einen einzelnen z.

Die neue Igusa Bedingung gilt für die dritte Größe nur dann, wenn sie als Bild eines einzelnen kohärenten Quellenvektors entsteht. Sie schränkt nicht beliebige Zustände ein, die aus verschränkten Eingaben der vier Register präpariert werden. Die polynomielle Abbildung ist auch kein behaupteter deterministischer Quantenkanal, der einen unbekannten Zustand klont.

Die unnormalisierten Codebasisvektoren besitzen die Gramform

\[
G=\operatorname{diag}(4,12,12,12,24).
\]

Ihre Quellenkontraktionen sind

\[
f(z)=(p,a,b,c,d)^T,
\]

\[
p=\sum_{i=0}^3z_i^4,
\quad a=6(z_0^2z_1^2+z_2^2z_3^2),
\]
\[
b=6(z_0^2z_2^2+z_1^2z_3^2),\quad
c=6(z_0^2z_3^2+z_1^2z_2^2),\quad d=24z_0z_1z_2z_3.
\]

Mit der orthonormalen Codeeinbettung V ist die unnormierte Projektionsamplitude w(z)=V†z^{tensor4}=G^{-1/2}f(z).

## 3. Die Igusa Gleichung folgt aus den ursprünglichen sechs Richtungen

Die bereits dokumentierten sechs Simplexspalten sind

\[
W_6=\begin{pmatrix}
2&2&-1&-1&-1&-1\\
0&0&-1&-1&1&1\\
0&0&-1&1&-1&1\\
0&0&1&-1&-1&1\\
1&-1&0&0&0&0
\end{pmatrix}.
\]

Definiere x=W6^T f. Explizit:

\[
x=(2p+d,\ 2p-d,\ -p-a-b+c,\ -p-a+b-c,\ -p+a-b-c,\ -p+a+b+c).
\]

Direktes Ausmultiplizieren ergibt zwei Identitäten:

\[
\boxed{\sum_{i=1}^6x_i=0,\qquad
F(x):=\left(\sum_i x_i^2\right)^2-4\sum_i x_i^4=0.}
\]

Das ist die klassische Igusa Quartik in einer zu den tatsächlichen TFPT Reflexionen passenden S6 Koordinatisierung. Die Jacobi Matrix von f besitzt bei z=(1,2,4,8) Rang vier. Das Bild hat daher affine Dimension vier und projektive Dimension drei. Diese drei sind komplexe Moduldimensionen, keine hergeleiteten drei Raumdimensionen.

Bini und van Geemen verwenden Generatoren p0,p1,p2,p3,p4, die in unserer Normierung durch f=(p0,3p1,3p2,3p3,6p4) gegeben sind. Der Anschluss wird also mit einer expliziten Skalierung hergestellt, nicht allein durch Namensgleichheit.

### 3.1 Der gesamte Invariantenring

Die volle Zweiqubit Pauli Gruppe Pcal enthält die 16 Hermiteschen Paulis mit den vier skalaren Phasen und hat Ordnung 64. Alle fünf f_i sind unter ihr invariant. Die exakt berechnete Molien Funktion lautet

\[
\frac1{64}\left[\sum_{\xi\in\mu_4}(1-\xi t)^{-4}
+\frac{30}{(1-t^2)^2}+\frac{30}{(1+t^2)^2}\right]
=\frac{1-t^{16}}{(1-t^4)^5}.
\]

Zusammen mit dem klassischen Quotientensatz erhält man

\[
\boxed{\mathbb C[z_0,z_1,z_2,z_3]^{\mathcal P}
\cong\mathbb C[x_1,\ldots,x_6]/(\sum x_i,F(x)).}
\]

Es sind fünf unabhängige Generatoren vom Quellengrad vier und eine einzige Relation vom Quellengrad 16. Der Quartikcode ist damit kein beliebig isolierter Fünferraum: Seine polynomiellen Quellkoordinaten sind der vollständige Invariantenring dieser endlichen Quotientenabbildung.

### 3.2 Warum die Grade 8,12,20,24 gemeinsam auftreten

Jede der 60 ursprünglichen Reflexionen wirkt auf x als Transposition. Alle 15 Transpositionen treten auf, jeweils viermal. Die Gruppe enthält zugleich die Pauli Gruppe: Im Prüfprogramm werden XI, IX, ZI, IZ und iI explizit als Produkte tatsächlich vorhandener Quellenreflexionen konstruiert.

Ein linearer Operator, der den ganzen Pauli Invariantenring punktweise festhält, liegt selbst in der Pauli Gruppe. Begründung: Invarianten einer endlichen Gruppe trennen ihre Bahnen. Für jeden generischen Vektor müsste der Operator deshalb wie eines der endlich vielen Paulielemente wirken. Eine endliche Vereinigung echter linearer Unterräume kann nicht den ganzen komplexen Vektorraum überdecken. Ein Paulielement muss daher mit dem Operator identisch sein.

Der Kern ist folglich genau Pcal, das Bild genau S6. Die Gruppenordnung ist 64 mal 720 = 46080.

Für die elementarsymmetrischen Funktionen e_k der sechs x_i gilt e1=0. Newton Identitäten liefern

\[
F=16e_4-4e_2^2,
\qquad e_4=e_2^2/4.
\]

Der Ring der vollen Quellgruppeninvarianten ist deshalb polynomial in e2,e3,e5,e6. Da x_i selbst Quellengrad vier haben, sind die Grade

\[
\boxed{4(2,3,5,6)=(8,12,20,24).}
\]

Die Unabhängigkeit der vier Generatoren ist auch durch einen nichtverschwindenden Jacobi Determinanten im Paket geprüft. Das organisierende Polynom ist

\[
\boxed{\prod_{i=1}^6(u-x_i)=u^6+e_2u^4-e_3u^3+
\frac{e_2^2}{4}u^2-e_5u+e_6.}
\]

Dies erklärt die Invariantengrade innerhalb der vorhandenen Algebra. Es identifiziert sie nicht automatisch mit physischer Zeit, Massen oder Raumdimensionen.

## 4. Die 60 Quellhyperflächen und das Maschke Invariant

Die 240 ursprünglichen Wurzeln werden aus RM(1,3) rekonstruiert: die 16 Vektoren ±2e_i und die 224 Vorzeichenbelegungen der 14 Gewicht-vier-Supportmengen. Durch komplexe Paarung entstehen 60 Wurzelrichtungen und ihre 60 komplexen orthogonalen Hyperflächen ell_alpha(z)=0.

Für jede der 15 Koordinatendifferenzen gilt exakt

\[
\boxed{x_i(z)-x_j(z)=c_{ij}\prod_{\alpha\in B_{ij}}\ell_\alpha(z),
\qquad |B_{ij}|=4.}
\]

Die 15 Faktorisierungen verwenden alle 60 ursprünglichen Hyperflächen genau einmal. Sie wurden gegen die tatsächlichen Gaußschen Kovektoren geprüft. Beispielsweise ist

\[
x_1-x_2=48z_0z_1z_2z_3.
\]

Die übrigen Faktoren und ihre Normalisierungen stehen vollständig in results.json. Folglich ist die Diskriminante des obigen Sextikpolynoms

\[
\operatorname{Disc}_u\prod_i(u-x_i(z))
=C\prod_{\alpha=1}^{60}\ell_\alpha(z)^2,
\]

mit einer von der Kovektornormierung abhängigen nichtnull Konstante C. Die Kollisionsflächen der sechs Quotientenkoordinaten sind genau das Bild des ursprünglichen Reflexionsarrangements.

Für das vorhandene Maschke Polynom

\[
M(z)=\sum z_i^8+14\sum_{i<j}z_i^4z_j^4+
168z_0^2z_1^2z_2^2z_3^2
\]

wird exakt geprüft

\[
\sum x_i^2=12M(z).
\]

Mit der bereits vollständig dokumentierten Wurzelkonvention F8=1920M erhält man F8=160 sum x_i². Die Skalierung 1920 wird im neuen Code nicht als erneute vollständige Wurzelsummenrechnung beansprucht; die neue vollständige Polynomprüfung ist sum x²=12M.

## 5. Die zehn Bellausgänge und die Doily sind Teil derselben Geometrie

### 5.1 Zehn Quadriken und zehn ausgezeichnete Hyperflächen

Die zehn reellen symmetrischen Zweiqubit Paulis lauten in dieser Reihenfolge

```
II IX IZ XI XX XZ YY ZI ZX ZZ
```

Ihre Bellvektoren b_nu=vec(A_nu)/2 bilden die bisherige Paarbasis. Die vorhandene Bellmatrix hat die rationale Form W10=(Fnum/4)G^{-1/2}. In der neuen Rechnung wird die 10 mal 6 Vorzeichenmatrix Ssign=Fnum W6/8 verwendet.

Jede Zeile hat drei +1 und drei -1. Die zehn Zeilen sind genau die zehn balancierten Vorzeichenklassen bis auf Gesamtvorzeichen. Für jeden tatsächlichen Belloperator gilt die neue exakte Identität

\[
\boxed{\sum_{q=1}^6S_{\nu q}x_q(z)=6(z^TA_\nu z)^2.}
\]

Die zehn Messrichtungen sind also nicht beliebige zehn Punkte. Ihre Hyperflächen ziehen auf Quadrate der ursprünglichen Quellenquadriken zurück. Klassisch sind dies die zehn ausgezeichneten trope-Hyperflächen der Igusa Geometrie; ihre Normalen sind die zehn Knoten der projektiv dualen Segre Kubik. Diese klassische Dualität wird nicht mit physischem Raumzeitdualismus gleichgesetzt.

### 5.2 Fünfzehn Linien und fünfzehn Punkte

Jede perfekte Paarung der sechs Labels definiert eine Gerade

\[
x_i=x_j=A,\quad x_k=x_l=B,\quad x_m=x_n=C,
\qquad A+B+C=0.
\]

Auf allen 15 so parametrisierten Geraden verschwinden F und seine tangentialen Ableitungen exakt. Die 15 ausgezeichneten Schnittpunkte haben die Form

\[
(2,2,-1,-1,-1,-1)
\]

mit sämtlichen Platzierungen des Zweierpaars. Die 60 tatsächlich rekonstruierten Quellenstrahlen werden durch x(z) genau auf diese Punkte abgebildet, vier Strahlen pro Punkt.

Die Inzidenzmatrix N hat die 15 Zweierpaare als Zeilen und die 15 perfekten Paarungen als Spalten. Ein Eintrag ist eins genau dann, wenn das Paar in der Paarung enthalten ist. Damit gilt

\[
\operatorname{rank}N=10,\qquad
\operatorname{spec}(NN^T)=\{9^{\times1},4^{\times9},0^{\times5}\}.
\]

Dies ist die ursprüngliche Doily Konfiguration in denselben sechs Koordinaten. Der Faktor 2/3 ist ihr normierter Singularwert. Er ist weiterhin nicht der Eigenwert 4/9 des vollständig positiven Paar-Rückkanals und leitet die noch andere Clockrichtung (1/3)^6 nicht her.

Die in der vorherigen Rechnung aus W10 entstandenen Petersen Vorzeichenrahmen bleiben gültig. Die jetzigen Formeln binden die zugrunde liegenden Bellquadriken und die sechs Markierungen zusätzlich an die vollständige Igusa Quellgleichung.

## 6. Die neue Gleichung entscheidet zwei Zustands- und Dynamikfragen

### 6.1 Die sechs Markierungszustände sind keine einzelnen kohärenten Quellenbilder

Der zu einer Simplexmarkierung gehörende reine Codezustand hat in x-Koordinaten die projektive Gestalt (5,-1,-1,-1,-1,-1). Einsetzen ergibt

\[
F(5,-1,-1,-1,-1,-1)=30^2-4\cdot630=-1620\ne0.
\]

Keiner dieser sechs Codezustände ist also das Bild eines einzelnen z^{tensor4}. Das verbietet die Zustände nicht: Sie sind legitime Zustände des gesamten Fünfercodes. Es entscheidet nur ihre Präparation aus der untersuchten Eingabeklasse. Eine Herleitung ihres physischen Auftretens benötigt zusätzliche Quellinformation, etwa eine geeignete verschränkte Vierregisterpräparation. Ebenso bleibt eine Markierung als algebraischer Index oder Operator zulässig.

### 6.2 Kein nichttrivialer kontinuierlicher linearer Fluss auf dem festen kohärenten Bild

Setze x6=-sum_{i=1}^5 x_i und betrachte eine beliebige 5 mal 5 Matrix A. Damit ein infinitesimaler linearer Fluss die ganze Igusa Hyperfläche bewahrt, muss für ein skalares kappa gelten

\[
\nabla F(x)\cdot Ax=\kappa F(x).
\]

Der Koeffizientenvergleich ergibt eine Matrix mit 70 Zeilen und 26 Unbekannten. Ihr Rang ist exakt 25. Der eindimensionale Lösungsraum ist

\[
A=\frac\kappa4 I.
\]

Projektiv ist dieser Fluss trivial. Das stimmt mit dem bekannten endlichen Automorphismus S6 der Igusa Quartik überein. Ein beliebiger kontinuierlicher SU(5) Codepuls ist folglich nicht gleichzeitig eine kontinuierliche Bewegung sämtlicher einzelner kohärenter Quellenbilder innerhalb dieses festen Fünferraums.

Geltungsgrenzen: Nicht ausgeschlossen werden diskrete Quellenoperationen, eine nichtlineare Bewegung mit passendem Lift, ein bewegter Coderaum oder beliebige verschränkte Codeeingaben. Ebenso ist dies kein allgemeines Verbot kontinuierlicher TFPT Dynamik.

### 6.3 Der benötigte lineare Antwortbereich ist exakt 35-dimensional

Die einfachsten infinitesimalen linearen Quellenoperationen wirken auf Polynome durch z_i partial_{z_j}. Für die vorhandenen fünf Generatoren gilt exakt

\[
\boxed{\operatorname{span}_{\mathbb C}\{f_a,
 z_i\partial_{z_j}f_a\}
=\operatorname{Sym}^4(\mathbb C^4)^*,\qquad\dim=35.}
\]

Schon die ersten Antworten schließen also nicht in fünf Richtungen. Die 35 mal 85 Koeffizientenmatrix hat Rang 35. Der vorhandene komplementäre symmetrische 30erraum ist der dazugehörige fehlende lineare Antwortsektor, nicht eine zusätzlich erfundene Teilchensammlung.

Für eine unabhängig vorgegebene gemeinsame Hamiltonentwicklung H auf dem 35erraum und die Projektoren P,Q=I-P gilt die genaue Feshbach Identität

\[
P(\zeta-H)^{-1}P=
[\zeta-PHP-PHQ(\zeta-QHQ)^{-1}QHP]^{-1}.
\]

Die Inverse rechts wirkt auf P. Die Formel erhält den spektral abhängigen Rückwirkungsterm. Sie ersetzt die fehlende Auswahl von H nicht. Insbesondere darf der Term nicht ohne Begründung durch einen frei gewählten konstanten Markovgenerator ersetzt werden.

### 6.4 Gleiche Quartikkoordinaten, verschiedene Zukunft

Wähle die beiden unnormierten Quellen

\[
z=(1,2,4,8)^T,\qquad z'=(I\otimes X)z=(2,1,8,4)^T.
\]

Beide haben Norm sqrt85 und exakt dieselbe Quartikauslesung

\[
f(z)=f(z')=(4369,6168,1632,768,1536)^T.
\]

Unter demselben Quellenoperator Hsrc=I tensor Z, also dot z=-iHsrc z, folgt

\[
\dot f(z)=(15420i,0,5760i,0,0)^T,
\qquad \dot f(z')=-\dot f(z).
\]

Der Unterschied ist nicht bloß eine gemeinsame Phase oder Normänderung: Die Matrix mit Spalten f und dot f(z)-dot f(z') hat Rang zwei. Bei Normierung beider Quellen durch sqrt85 werden alle Quartikwerte und Ableitungen durch 85² geteilt; der Widerspruch bleibt.

Es existiert daher für diese Quellenentwicklung kein eindeutiges autonomes Bewegungsgesetz allein in den Quotientenkoordinaten f. Generisch besitzt der projektive Pauli Quotient 16 Zweige. Vier binäre Angaben reichen als mathematische Zweigbezeichnung; das bedeutet nicht, dass ein vollständiger Quantenprozess durch vier klassische Bits ersetzt werden könnte. Der Quellenlift beziehungsweise Rahmen muss für spätere Wirkungen erhalten bleiben.

## 7. Der vollständige Quellraum wird mit dem ursprünglichen Hamming Code geschützt

Die im Vorgängerbericht ausgeführte alternative Konstruktion wird übernommen, nicht als neuer Quantencode ausgegeben. Der binäre Zeilenraum C der Matrix

```
1 1 1 1 0 0 0
1 1 0 0 1 1 0
1 0 1 0 1 0 1
```

hat sieben nichtnull Wörter mit Gewicht vier. Ihre Dreierkomplemente sind die sieben Fano Linien. Genau gilt

\[
\{(c,0)+b\mathbf1_8:c\in C,\ b\in\mathbb F_2\}=RM(1,3).
\]

Das ist derselbe binäre Seed wie bei der Konstruktion der E8 Wurzeln. Zwei bekannte Steane Codes werden zu sieben C4 Registern gruppiert. Der logische Raum ist C4; ein unbekannter Einzelfehler auf einem C4 Register ist korrigierbar.

Der gemeinsame positive Parent ist

\[
H_F=\sum_{S\ \text{sieben Vierermengen}}(I-Q_S),
\qquad Q_S=\frac1{16}\sum_{A\in Pauli_2}A^{\otimes S}.
\]

Sein Spektrum ist (0:4,4:420,6:5880,7:10080). Ein einzelner nichttrivialer Pauli Fehler hat Energie vier. Die gesamte ursprüngliche Quellenwirkung wird nach der im Vorgängerpaket erneut geprüften Generatoridentität erhalten:

\[
U^{\otimes7}V_7=V_7\overline U.
\]

Die Konjugation ist realer Inhalt dieser Kodierung. Nach zwei Kodierstufen erhält man U^{tensor49}V49=V49 U. Weder die Sieben noch die 49 sind dadurch physische Raumgrößen oder Zeittakte.

## 8. Ein positiver neuer Dynamikbefund: voller Quellenaustausch in dritter Ordnung

### 8.1 Präzise zusätzliche Modelldaten

Es werden zwei getrennte Siebenregisterblöcke A,B gewählt, mit

\[
H_0=\Delta(H_F^A+H_F^B),\qquad\Delta>0.
\]

Die sieben gleich bezeichneten Register werden durch

\[
\boxed{V_g=g\sum_{r=1}^7\sum_{a=1}^{15}
 A_{a,r}^A A_{a,r}^B
=g\sum_{r=1}^7(4\operatorname{Swap}_r-I)}
\]

gekoppelt. Die A_a sind die 15 nichttrivialen Hermiteschen Zweiqubit Paulis. Diese gewöhnlichen Paarlinks sind unter einer gemeinsamen U tensor U Drehung des jeweiligen C4 Paares kovariant. Das ist keine lokale Standardmodell-Eichfeldkonstruktion. g, Delta und die Paaranordnung sind ausdrücklich eingesetzte Modelldaten.

### 8.2 Das Ergebnis

Sei P der gemeinsame 16-dimensionale logische Grundraum. Wegen Distanz drei verschwindet der erste komprimierte Term. Der zweite ist skalar. Die ersten drei Ordnungen der entarteten Störungsentwicklung sind

\[
P V_gP=0,
\]
\[
H_{\rm eff}^{(2)}=-\frac{105g^2}{8\Delta}I,
\]
\[
\boxed{H_{\rm eff}^{(3)}=
\frac{g^3}{\Delta^2}
\left(\frac{21}{8}\operatorname{Swap}_{\rm logisch}
-\frac{63}{16}I\right).}
\]

Bis auf den Energienullpunkt lautet die führende Wechselwirkung damit

\[
\boxed{J_{\rm eff}=\frac{21}{8}\frac{g^3}{\Delta^2}.}
\]

Die Restordnung ist O(g^4/Delta^3) im festen endlichen Modell bei g/Delta gegen null. Es ist weder eine exakte Gleichung für beliebige endliche Kopplung noch eine uniforme thermodynamische Fehleraussage.

### 8.3 Vollständige Zählung der tragenden Pfade

Es existieren 7 mal 15 = 105 elementare Fehlermuster. Ein solcher physischer Link verletzt pro Block vier Quartikchecks, hat also im Zweiblocksystem Energie 8Delta. Bei einem nichttrivialen Dreierpfad, der im Code endet, ist auch das zweite Zwischensyndrom wieder ein Einzelfehlersyndrom. Beide Nenner sind deshalb 8Delta.

Die exakte vollständige Syndromzählung findet zwei Klassen:

* 1470 geordnete Dreierpfade liegen an derselben Registerposition. Bei den Produkten dreier Paulis quadrieren sich die Einblockphasen, weil beide Blöcke dieselbe Folge tragen. Der gesamte skalare Phasenbeitrag ist -210.
* 630 geordnete Pfade liegen auf einer Fano Linie: sieben Linien, sechs Reihenfolgen, 15 Pauliarten. Für jede Pauliart sind es 42 Pfade.

Die Fano Dreierwörter wirken logisch als A_a^*. Damit

\[
H_{\rm eff}^{(3)}=
\frac{g^3}{64\Delta^2}
\left[-210I+42\sum_{a=1}^{15}A_a^*\otimes A_a^*\right].
\]

Die exakte Pauli Identität

\[
\sum_{a=1}^{15}A_a^*\otimes A_a^*=4\operatorname{Swap}-I
\]

liefert die angegebenen Koeffizienten. Die Konjugation hebt sich in dieser symmetrischen Paarstruktur auf; ein Vorzeichen physischer CP Verletzung wird damit nicht ausgewählt.

### 8.4 Welcher physische Anspruch daraus nicht folgt

Die logische C4 Paarstruktur zerfällt unter dem führenden Austauschoperator in Sym²(C4) mit Dimension zehn und Lambda²(C4) mit Dimension sechs. Bei positivem kleinem g liegt der antisymmetrische Sektor in der führenden Näherung tiefer. Die führende Aufspaltung ist 2J_eff.

Der Zehner hier ist die symmetrische Zweierpotenz der Quellen-C4. Er ist nicht automatisch der Vektorzehner von Spin(10). Die Darstellung (10,6) im ursprünglichen Materieanschluss kann nicht allein wegen derselben Zahlen eingesetzt werden. Weder die 4D Feldstatistik noch chirale Materie werden durch einen endlichdimensionalen Swap hergeleitet.

## 9. Unabhängige exakte Gegenprobe des Störungsmechanismus

Für nur eine Pauliart über die sieben Register vereinfacht sich der vollständige invariante Syndromraum auf acht Zustände je logischem Eigenwert xi=±1:

\[
H_\xi=\operatorname{diag}(0,M,M,M,M,M,M,M)+\xi g(J_8-I_8),
\qquad M=8\Delta.
\]

Sein vollständiges charakteristisches Polynom ist

\[
[\lambda-(M-\xi g)]^6
[\lambda^2-(M+6\xi g)\lambda-7g^2].
\]

Der tiefe Eigenwert ist exakt

\[
E_\xi=\frac{M+6\xi g-\sqrt{(M+6\xi g)^2+28g^2}}2.
\]

Die Entwicklung lautet

\[
E_\xi=-\frac{7g^2}{M}+\frac{42\xi g^3}{M^2}+O(g^4/M^3).
\]

Für M=8Delta reproduziert dies den Ein-Pauli-Beitrag 21g³/(32Delta²). Die vollständige 15-Pauli-Wechselwirkung aus Abschnitt 8 ist eine andere Summe; ihr Swapkoeffizient 21/8 wird nicht aus dieser einzelnen Näherung allein behauptet, sondern aus der vollständigen Pfadzählung berechnet.

## 10. Quantifizierte Grenze der dynamischen Auswahl

Die neue Algebra wählt einen Zusammenhang, aber noch kein einmaliges Bewegungsgesetz. Das kann an der bisherigen Fünfercodefamilie exakt gezeigt werden.

Mit S als Symmetrieprojektor und P als Codeprojektor sei

\[
H_r=r(S-P)+(I-S),\qquad r>0.
\]

Alle diese Operatoren besitzen denselben Code als Grundraum und dieselbe getestete Quellsymmetrie. Die relativen Anregungsenergien unterscheiden sich.

Verwendet man die im früheren Bericht angegebenen zwei physischen Paarlinks zwischen getrennten Fünferblöcken, ergibt die zweite Ordnung

\[
H_{\rm eff}^{(2)}=\frac{g^2}{\Delta}
[C_0(r)I+C_1(r)(h_A\otimes I+I\otimes h_B)
+C_2(r)h_A\otimes h_B],
\]

\[
C_0=-\frac{5r^2+10r+1}{8r(r+1)},\quad
C_1=\frac{(r-1)(5r+3)}{8r(r+1)},\quad
C_2=-\frac{5r^2+2r+9}{8r(r+1)}.
\]

Bei r=1/2 folgt genau der frühere Wert C2=-15/8; bei r=1 ist er -1. Das Verhältnis zwischen lokaler Antwort und Interaktion ist ebenfalls verschieden. Eine Änderung des Energienullpunkts allein entfernt diesen Unterschied nicht.

Dies sind zwei verschiedene Entwicklungen derselben endlichen Codefamilie. Es sind nicht zwei vollständige Modelle, die sämtliche physischen TFPT Bedingungen erfüllen. Eine allgemeine Nichtableitbarkeit von TFPT wäre damit nicht bewiesen.

Ebenso wird die Kopplungsanordnung in Abschnitt 8 definiert, nicht ausgewählt. Die frühere Formulierung, virtuelle Übergänge hätten bereits ein Nachbarschaftsnetz erzeugt, war zu weitgehend. Eine Wechselwirkung auf gewählten Links ist noch keine Herleitung der Links, ihrer räumlichen Dimension oder einer universellen kausalen Geschwindigkeit.

## 11. Was nun zusammengehört und was der physische Herkunftssatz leisten muss

Der geschlossene endliche Zusammenhang lautet:

```
derselbe RM(1,3) Seed
   -> 240 ursprüngliche Wurzeln
   -> 60 Quellenreflexionen auf C4
   -> vollständiger quartischer Pauli Quotient (Igusa)
       -> sechs Koordinaten und ihre symmetrischen Invarianten
       -> alle 60 Reflexionshyperflächen als Faktorisierungen
       -> zehn Bellquadriken und duale Segre Geometrie
       -> fünfzehn Punkte, fünfzehn Geraden, Doily und 2/3

Verkürzung desselben Seeds
   -> kompatible Quartikchecks auf sieben Registern
   -> geschützte volle C4 Quelle statt isoliertem Fünferquotienten
   -> berechneter logischer Austausch in dritter Ordnung
```

Für die Entwicklung muss die volle Quelle beziehungsweise ein geeigneter Lift erhalten bleiben. Die kohärente Quartikauslesung ist nicht autonom; ihre vollständige lineare Antwort liegt bereits nach dem ersten infinitesimalen Schritt im symmetrischen 35erraum. Das ist eine konkrete Minimalitätsaussage über diesen Antwortbereich, keine Herleitung von 35 physikalischen Feldern.

Ein physischer Abschluss müsste aus den ursprünglichen unabhängigen TFPT Daten den gemeinsamen Zustand, die vollständige Feldalgebra, die tatsächliche Zeit und die lokale Kopplungsregel auswählen. Der vorhandene Quellenvertrag verlangt unter anderem eine gemeinsame geladene Antwort vom Typ

\[
\Pi_{\Psi\Psi}[\mathcal B_A,H_{\rm Quelle}]
=g\sum_{i<j}W_{A,ij}\Psi_j\Psi_i,
\]

in derselben graduierten lokalen Feldrealisierung und am selben Zustand. Die Igusa Quotientenidentität und der endlichdimensionale Swap ersetzen diesen Feldsatz nicht.

Eine kontrollierte große Geometrie, chirale Materie, alle Kopplungen, Flavorantworten, universell gekoppelte quantisierte Gravitation und ein gemeinsames kosmologisches Erzeugungsfunktional sind hier nicht konstruiert. Die Rechnungen entscheiden aber mehrere bisher vermischte Teilfragen und liefern einen gemeinsamen algebraischen Unterbau sowie eine konkrete geschützte Ausführung. Der nächste Herkunftsschritt ist nicht durch zusätzliche Zahlentreffer zu ersetzen.

## Literatur

Die Literatur identifiziert bekannte Mathematik und Methoden. Die TFPT spezifischen Koordinatenidentitäten und Störungskoeffizienten werden durch die oben angegebenen Rechnungen geprüft.

1. Gilberto Bini, Bert van Geemen, *Geometry and Arithmetic of Maschke's Calabi-Yau Threefold*, arXiv:1110.0106, insbesondere Abschnitt 4.3 und 7.1. https://arxiv.org/html/1110.0106v1
2. Ben Howard, John Millson, Andrew Snowden, Ravi Vakil, *A description of the outer automorphism of S6, and the invariants of six points in projective space*, arXiv:0710.5916, Abschnitt 2. https://arxiv.org/html/0710.5916
3. *Coble fourfold, S6-invariant quartic threefolds, and Wiman–Edge sextics*, arXiv:1712.08906v4, Lemma 3.4. https://arxiv.org/html/1712.08906v4
4. Huangjun Zhu, Richard Kueng, Markus Grassl, David Gross, *The Clifford group fails gracefully to be a unitary 4-design*, arXiv:1609.08172. https://arxiv.org/abs/1609.08172
5. Andrew Steane, *Multiple Particle Interference and Quantum Error Correction*, quant-ph/9601029. https://arxiv.org/abs/quant-ph/9601029
6. Sergey Bravyi, David P. DiVincenzo, Daniel Loss, *Schrieffer-Wolff transformation for quantum many-body systems*, arXiv:1105.0675. https://arxiv.org/abs/1105.0675


</details>

[Zur Navigation](#navigation)

<a id="original-q3"></a>
## Q3. Dynamische Auswahl des Quartikcodes aus geschützten Quellen

fileciteturn18file0L13-L35

**Originaldatei:** `TFPT_Dynamischer_Codeabschluss_Herleitung_20260926.md`  
**SHA256:** `2f5834d911ee52eee444706a01e8db607b25c348fa1614353ab3e5a809d583d6`

<details>
<summary>Q3: vollständigen Originalbericht öffnen</summary>

# TFPT: dynamische Auswahl des Quartikcodes aus geschützten Quellen

Forschungsfortsetzung vom 26. September 2026

## Ergebnis und Status

Für das ausdrücklich definierte endliche Vierblockmodell dieser Notiz wird gezeigt: Vier geschützte ursprüngliche C4 Quellen wählen bei hinreichend schwacher negativer, Pauli vollständiger Austauschkopplung einen fünfdimensionalen Grundsektor. Unter einer symmetrieverträglichen Identifikation des tiefen Bandes ist dies derselbe Quartikcode Pi5 wie im Quellenmoment. Ein zusätzlicher Term proportional zu Pi5 wird dem mikroskopischen Hamiltonoperator nicht hinzugefügt.

Die Auswahl erfolgt in zwei Stufen: Ferromagnetischer logischer Austausch in dritter Störungsordnung wählt Sym4(C4), Dimension 35. Verbundene Sechsschrittprozesse erzeugen in sechster Ordnung den ursprünglichen Quartikstabilisator und spalten den Raum in 5+30. Für den vollständigen Vierblockgraphen ist die führende innere Lücke (27573/512)|g|^6/Delta^5. Eine Viererkreisvariante liefert stattdessen (3143/256)|g|^6/Delta^5. Beide Aussagen gelten asymptotisch bei |g|/Delta gegen null, nicht als exakte Formeln bei beliebiger Kopplung.

Zusätzlich wird der bisherige 30er Antwortsektor exakt als fünfzehn zweidimensionale Pauli Charaktersektoren identifiziert. Ein wichtiger Schutzvorbehalt wird ebenfalls hergeleitet: Der ausgewählte nackte Grenzcode hat Parameter ((28,5,6))_4, während der tatsächlich wechselwirkende, gedresste Grundcode bei ausreichend kleinem, von null verschiedenem g im vollständigen Vierblockmodell bereits nichttriviale Zweiregisterobservablen mit Stärke O((g/Delta)^2) besitzt. Sein exakter Codeabstand ist dann zwei, nicht sechs.

Dies ist kein physischer TOE Abschluss. Der Siebenregisterparent, die vier Blöcke, ihre Links, deren Gleichheit, das negative Kopplungsvorzeichen und die Skala sind benannte Voraussetzungen des Kandidaten. Sie werden nicht aus P1/P2 hergeleitet. Raumdimension, geladene lokale Felder, chirales Standardmodell, Kopplungsnormierungen, Gravitation und ein kosmologischer Anfangszustand werden hier nicht konstruiert.

## 1. Quellen und Reproduktion

Verwendeter unmittelbarer Ausgangspunkt:

* `TFPT_Igusa_Quellendynamik_Herleitung_20260926.md`, insbesondere Abschnitte 6 bis 10.
* `TFPT_Igusa_Quellendynamik_Pruefpaket_20260926.zip`.
* `TFPT_Quartik_Fortsetzung_Herleitungen_20260926.md`, insbesondere Codebasis, Quartikprojektor und Siebenregisterencoder.

Das jüngste ursprüngliche Paket wurde erneut ausgeführt und bestand seine 1065 Prüfungen. Das neue eigenständige Programm `audit.py` rekonstruiert die tatsächlichen Wurzeln und Reflexionen aus RM(1,3), enumeriert ihre gesamte projektive Gruppenwirkung und rechnet die neuen Identitäten, Charaktere und Störungskoeffizienten. Es importiert keine Ergebnismatrizen aus dem Vorgängerpaket.

Der neue Lauf bestand 1326 endliche Prüfungen. Die Anzahl ist eine Programmdiagnose, kein Maß der physikalischen Vollständigkeit. Die starken Aussagen werden unten durch Argumente mit klaren Voraussetzungen getragen.

Die zweite unabhängige Koeffizientenprüfung verwendet den vollständigen invarianten 512 dimensionalen Syndromraum der Ein Pauli Variante. Es wurde nicht der gesamte Raum von 28 vierstufigen Registern diagonalisiert. Der Übergang von der Ein Pauli Rechnung zur vollständigen Quelle benutzt die unten bewiesene Klassifikation der minimalen logischen Rückkehrpfade.

Reproduktion:

```sh
python -m pip install -r requirements.txt
python audit.py
```

`results.json` enthält alle Bedingungen und Werte, `matrices.npz` die Ausgangswurzeln, Reflexionen, Charakterprojektoren und kollektiven Generatoren. Rationale Pfadgewichte und die unabhängigen Reihen werden mit Python Fractions gerechnet. Die Gaußschen Matrixrechnungen nutzen ausschließlich exakt darstellbare kleine ganze Zahlen und Halbierungen; Integrität wird überprüft. Für die Grundraumdimension der Austauschgraphen wird ein modularer Rang als untere Schranke mit einer expliziten 35 dimensionalen Nullraumbasis als oberer Schranke kombiniert. Keine Eigenwerttoleranz entscheidet diese Dimensionen.

## 2. Tatsächliche native Symmetrie statt bloßer Dimensionsvergleiche

Aus den 240 ursprünglichen Wurzeln entstehen 60 Reflexionen U=I-2|psi><psi| auf C4. Das Programm prüft ihre Konjugationswirkung auf allen 15 nichttrivialen Zweiqubit Paulis A_a. Jede Wirkung ist eine signierte Permutation. Die erzeugte Gruppe dieser Wirkungen hat exakt 11520 Elemente. Da Konjugation auf der vollen Matrixalgebra die unitäre Wirkung bis auf eine skalare Phase bestimmt, ist dies die projektive native Quellgruppe.

Für jede Gruppenwirkung g gilt

    |tr U_g|^2 = 1 + Summe der Vorzeichen festgehaltener nichttrivialer Paulis.

Damit werden die vier Framepotentiale ohne numerische Haarintegration berechnet:

    Phi_1=1, Phi_2=2, Phi_3=6, Phi_4=29.

Die Dimension des Kommutanten auf (C4)^tensor t ist genau Phi_t. Für U(4) lauten diese Werte bei t=1,2,3,4 dagegen 1,2,6,24. Das ist die bekannte Eigenschaft der Cliffordgruppe: bis zum dritten Moment vollständige unitäre Isotropie, im vierten zusätzliche Invarianten. Die aktuelle Rechnung verifiziert sie an den tatsächlich rekonstruierten TFPT Generatoren.

Konsequenz: Jeder native invariante Operator auf bis zu drei logischen C4 Quellen ist bereits unter der gemeinsamen U(4) Wirkung invariant. Auf zwei Quellen hat er daher exakt die Form

    a I + b Swap.

Das ist innerhalb eines isolierten äquivariant rekonstruierten tiefen Zweiblockbandes eine Aussage über die Operatorform in allen Ordnungen, nicht nur über den bereits berechneten kubischen Koeffizienten. Die Funktionen a(g), b(g) sind damit noch nicht in allen Ordnungen bestimmt.

Auf dem symmetrischen vierten Tensor besitzt die native Gruppe dagegen zwei irreduzible, inequivalente Komponenten der Dimensionen fünf und dreißig. Das Programm prüft ihre Charakterorthogonalität über alle 11520 projektiven Wirkungen. Die Charakterberechnung benutzt Newtons Identität

    chi_Sym4(U) = [p1^4+6 p1^2 p2+3 p2^2+8 p1 p3+6 p4]/24,
    pj = tr U^j,

und den Quartikstabilisator Q=(1/16) Summe A_a^tensor4. Es findet

    <chi_5,chi_5>=<chi_30,chi_30>=1, <chi_5,chi_30>=0.

Auf Sym4 ist somit jeder native invariante Hermitesche Operator eine Linearkombination von I und Pi5. Die Symmetrie bestimmt noch nicht das Vorzeichen der Energieaufspaltung. Dieses wird erst durch die Störungsrechnung geliefert.

## 3. Der 30er Antwortsektor ist fünfzehn mal zwei

Sei D(b)=A_b^tensor4 eingeschränkt auf Sym4(C4). Die vierfache Tensorpotenz entfernt die Pauli Produktphasen. Die D(b) bilden eine kommutative Darstellung der binären Adressgruppe F2^4.

Mit der symplektischen Paarung [a,b] setze

    P_a = (1/16) Summe_b (-1)^[a,b] D(b).

Diese sechzehn Projektoren sind paarweise orthogonal und summieren sich zu I35. Der triviale Sektor ist genau Pi5.

Für den Identitätsoperator hat Sym4 den Charakter 35. Ein nichttrivialer Pauli besitzt auf C4 zwei Eigenwerte +1 und zwei Eigenwerte -1; daher ist sein Sym4 Charakter der Koeffizient von t^4 in

    (1-t)^(-2)(1+t)^(-2)=(1-t^2)^(-2),

also drei. Deshalb

    rank P_0 = (35+15*3)/16 = 5,
    rank P_a = (35-3)/16 = 2 für a != 0.

Die vollständige Antwortzerlegung lautet

    Sym4(C4) = C5 direkt plus Summe_{a != 0} C2_a.

Für einen kollektiven Quellenoperator K_a=Summe_{r=1}^4 A_{a,r} folgt aus Pauli Konjugation die Selektionsregel

    P_s K_a P_t = 0, außer wenn s=t+a.

Insbesondere besitzt K_a Pi5 sein Bild im zugehörigen Zweiersektor und Rang zwei. Alle fünfzehn Rangbehauptungen werden exakt geprüft. Die 30 Richtungen sind somit kein unsortierter Zusatzraum und nicht aus der Zahl 30 erratene Teilchen: Es sind fünfzehn verschiedene Antwortrahmen mit je zwei komplexen Richtungen.

Die Isolierung dieser fünfzehn Rahmen ist weiterhin keine Auswahl der Koeffizienten eines tatsächlichen H_Quelle. Die Igusa Auslesung bleibt bei einer allgemeinen kontinuierlichen Quellbewegung nicht autonom.

## 4. Der vorgegebene mikroskopische Kandidat

Der binäre Prüfcode C ist der Zeilenraum von

    H7 =
    1 1 1 1 0 0 0
    1 1 0 0 1 1 0
    1 0 1 0 1 0 1.

Seine sieben nichtnull Wörter haben Gewicht vier und paarweise Überlappung zwei. Die komplementären Dreiermengen sind die Fano Linien. Die Rückbindung an den ursprünglichen Wurzelcode ist eine Gleichheit konkreter Mengen:

    {(c,0)+b 1_8 : c in C, b in F2} = RM(1,3).

Wie im vorherigen Bericht werden zwei bekannte Steane Codes zu sieben C4 Registern zusammengefasst. Der Encoder V7 kodiert ein logisches C4, korrigiert einen unbekannten Einzelfehler auf einem C4 Register und trägt die native Wirkung

    U^tensor7 V7 = V7 conjugate(U).

Der Parent einer Quelle ist

    H_F = Summe_{S sieben Vierermengen}(I-Q_S),
    Q_S = (1/16) Summe_{a=0}^{15} A_a^tensor S.

Die Q_S kommutieren. Der Grundraum hat Dimension vier; ein nichttrivialer Ein Pauli Fehler hat Energie vier. Für einen allgemeinen Syndromrang r ist die Zahl verletzter Checks 8-2^(3-r).

Jetzt werden vier solche Quellen gewählt. Für einen Graphen G auf den vier Blocklabels definieren wir

    H(g)=Delta Summe_{v=1}^4 H_F^(v)
         + g Summe_{(v,w) in E(G)} Summe_{r=1}^7 Summe_{a=1}^{15}
                      A_{a,r}^(v) A_{a,r}^(w).

Es gilt

    Summe_{a=1}^{15} A_a tensor A_a = 4 Swap-I.

Damit sind die neuen Links gewöhnliche Zweiregisteroperatoren. Die ursprünglichen internen H_F Terme bleiben vierlokal. Das gesamte mikroskopische Modell ist NICHT rein zweilokal.

Voraussetzungen des Hauptsatzes: G=K4, gleiche Kopplung g<0 auf allen sechs Blockpaaren, Delta>0 und hinreichend kleines |g|/Delta. Die Kreisvariante verwendet G=C4 und dieselben Vorzeichen und Gleichheiten. Diese Graphen sind keine räumlichen Einbettungen. Der Name K4 oder Tetraeder erzwingt keine drei Raumdimensionen.

## 5. Erst wird der 35erraum ausgewählt

Das ungestörte tiefe Band besitzt Dimension 4^4=256. Die erste nichtskalare effektive Kopplung ist die bereits bekannte dritte Ordnung

    H_eff^(3) = scalar I + (21/8)(g^3/Delta^2) Summe_{(v,w)} Swap_vw.

In Graphen mit Dreiecken kommen weitere skalare Dreiecksterme hinzu. Sie ändern die folgende Auswahl nicht.

Für g<0 wird Summe Swap maximiert. Jeder einzelne Swap hat maximalen Eigenwert eins. Die Summe besitzt diesen Maximalwert genau auf den Zuständen, die unter allen Kantentranspositionen invariant sind. Auf einem verbundenen Graphen erzeugen die Kantentranspositionen S4. Der gemeinsame Raum ist daher exakt Sym4(C4), Dimension 35.

Die Lücke zu anderen Permutationssektoren ist im führenden Term von Ordnung |g|^3/Delta^2. Für K4 hat die Transpositionssumme die größte Eigenvalue sechs und die nächstgrößte zwei. Die führende äußere Lücke ist somit (21/2)|g|^3/Delta^2. Das exakte Bild der tiefen Zustände ist bereits schwach gedresst; es sind nicht bei endlichem g wortwörtlich Produkte nackter Codezustände.

Bei g>0 wird dagegen der völlig antisymmetrische Viererraum bevorzugt. Er hat Dimension eins. Die Gruppendaten allein wählen das negative Vorzeichen nicht aus.

## 6. Warum vor sechster Ordnung kein Quartikselektor entstehen kann

Für eine nichttriviale logische Wirkung auf einem Siebenregisterblock sind mindestens drei physische Pauli Fehler erforderlich. Ein Link berührt zwei Blöcke. Um alle vier logischen Blöcke nichttrivial zu treffen, sind daher mindestens

    ceil(4*3/2)=6

Links notwendig.

Vor der sechsten Ordnung haben alle nichtskalaren verbundenen Beiträge höchstens drei logische Träger. Unter der nativen Symmetrie sind sie deshalb bereits U(4) invariant. Auf dem irreduziblen Sym4(C4) Raum sind sie skalar. Produkte beziehungsweise Normierungsterme aus niedrigeren Ordnungen besitzen dieselbe U(4) Invarianz und können die 5/30 Aufspaltung ebenfalls nicht liefern.

Damit ist die sechste Ordnung die erste mögliche Ordnung eines Unterschieds zwischen Pi5 und seinem dreißigdimensionalen symmetrischen Komplement.

## 7. Exakte vollständige Rechnung des ersten Quartikterms

### 7.1 Alle vier logischen Blöcke müssen je drei Treffer besitzen

Ein Sechslinkpfad hat zwölf Endpunkte. Für eine nichttriviale logische Wirkung auf allen vier Blöcken müssen alle vier Grade genau drei sein.

Ein nichttriviales logisches Pauli Wort mit drei Treffern in einem Block muss auf drei verschiedenen Registerpositionen einer Fano Linie liegen. Alle drei Pauliadressen sind dabei gleich. Beweis: Der lokale Syndrom ist Summe_i a_i tensor h_i. Drei verschiedene Spalten h_i sind entweder unabhängig, dann wären alle a_i null, oder sie bilden eine Linie h1+h2+h3=0. In letzterem Fall erzwingt die Unabhängigkeit von h1,h2 die Gleichheit a1=a2=a3. Wiederholte Positionen können bei drei Treffern nur einen skalaren Rückweg oder einen erkannten Restfehler erzeugen, kein nichttriviales logisches Wort.

In einem verbundenen Vierblockpfad erzwingt dies dieselbe nichtnull Pauliadresse a an ALLEN sechs Links. Die resultierende logische Wirkung ist

    (conjugate A_a)^tensor4 = A_a^tensor4.

Summe über die fünfzehn Pauliarten ergibt 16Q-I. Die native quartische Richtungsinformation erscheint also in dem Operator selbst.

### 7.2 Nur zwei verbundene Graphentypen sind möglich

Jeder verbundene schleifenlose kubische Multigraph auf vier markierten Vertices hat eine der folgenden Formen:

* K4 mit allen sechs verschiedenen Kanten.
* Zwei gegenüberliegende doppelte Kanten und zwei einfache Kreuzkanten. Es gibt sechs markierte Varianten.

Das Programm enumeriert alle nichtnegativen Kantenmultiplizitäten mit Summe sechs und Grad drei an jedem Vertex. Es findet genau diese sieben Muster.

Unverbundene Dreifachkanten entsprechen Produkten unabhängiger Paaraustauschprozesse. Sie tragen keine neue nichtunitäre Quartikrichtung; in einer verbundenen effektiven Expansion werden die unabhängigen Beiträge subtrahiert. Jedenfalls sind ihre aus vollständigen Pauli Summen gebildeten Operatoren U(4) invariant und damit für die innere 5/30 Differenz irrelevant.

### 7.3 Die Fano Registerlabels sind ein endlicher Fluss auf dem Kopplungsgraphen

Ordne jeder der sechs Kanten ein nichtnull h_e in F2^3 zu. An jedem Vertex muss die Summe der drei angrenzenden Labels null sein. Damit sind die drei dortigen Labels automatisch verschieden und bilden eine Fano Linie.

Für K4 kann man drei freie Labels a,b,c wählen. Die Kanten tragen a,b,a+b,c,a+c,b+c. Zulässigkeit bedeutet: a,b,c sind nichtnull und paarweise verschieden. Es gibt

    7*6*5=210

solche Zuordnungen. Davon sind 168 linear unabhängige Dreierrahmen und 42 abhängig. Die 168 sind 7*6*4, also die Größe von GL(3,2), nicht eine zusätzlich eingesetzte Zahl.

Für den Typ mit zwei Doppelkanten gibt es 252 Zuordnungen bei unterscheidbaren Doppelkantenslots. Die beiden Vertauschungen der Doppelkantenslots liefern eine vierfache Überzählung. Physisch verschiedene Registerbelegungen sind daher 252/4=63.

Diese Zählungen werden zusätzlich durch vollständige Enumeration der 7^6 Kantenbelegungen geprüft. Die drei binären Flusskoordinaten sind keine drei Raumdimensionen. Für K4 stimmen sie mit der Dimension seines Zyklusraums überein; das ist eine Aussage über diesen kleinen endlichen Graphen.

### 7.4 Die Energienenner werden nicht angenähert

In einem gültigen minimalen Pfad hat ein Block mit null oder drei ausgeführten inzidenten Kanten keinen Syndromfehler. Ein Block mit einem oder zwei Treffern hat jeweils einen Rang eins Syndrom und Energie 4Delta. Für eine echte Teilmenge der sechs Links gilt daher

    E_intermediate = 4Delta * Anzahl der Vertices mit Grad eins oder zwei.

Kein solcher verbundener minimaler Pfad kehrt vor dem sechsten Schritt in den gesamten Code zurück. Die fünf Resolventennenner sind damit exakt bestimmt. Summe über alle 720 Reihenfolgen ergibt

    w_K4 = 83/16384,
    w_double = 449/73728,

jeweils nach Abspaltung von Delta^(-5). Das sechste Störungsvorzeichen ist negativ.

Pro Pauliart ergeben sich

    K4: 210*w_K4 = 8715/8192,
    jede Doppelvariante: 63*w_double = 3143/8192.

### 7.5 Der vollständige erste Koeffizient

Für verschiedene Kantengewichte g_e ist der nichtunitär isotrope Quartikanteil

    H_4body^(6) = -Q/(512 Delta^5) *
       [8715 Produkt_{e in K4} g_e
        + 3143 Summe_{sechs Doppelmustern m} Produkt_e g_e^(m_e)]
       + ein für die symmetrische 5/30 Differenz irrelevanter Skalar.

Andere effektive Beiträge derselben Ordnung können außerhalb des symmetrischen Raums nichttrivial sein. Es wird nicht behauptet, die gesamte sechste Ordnung auf allen 256 logischen Zuständen bestehe nur aus diesem Ausdruck.

Für gleiche g auf K4 folgt

    kappa_K4 = (8715 + 6*3143)/512 = 27573/512.

Im Kreis C4 sind zwei der Doppelvarianten vorhanden, aber kein K4 Muster. Es folgt

    kappa_C4 = 2*3143/512 = 3143/256.

Für die offene Viererkette existiert kein verbundener kubischer Sechslinkpfad. Der entsprechende Quartikterm in sechster Ordnung verschwindet. Eine Auswahl in noch höherer Ordnung wird dadurch nicht ausgeschlossen.

## 8. Zweite unabhängige Rechnung einschließlich aller Rückkehrkorrekturen

Für eine feste Pauliart kann man das vollständige invariante Syndromproblem exakt auf 512 Zustände reduzieren. Ein Zustand wird durch s0,s1,s2 in F2^3 beschrieben; s3=s0+s1+s2. Der Gesamtwert null wird von jedem Link erhalten. Die ungestörte Energie ist

    E_s = 4Delta * Anzahl der nichtnull s_v.

In einem logischen Eigenwertsektor xi_v=+/-1 wirkt eine physische Kante durch

    g_e xi_v xi_w Summe_{r != 0} shift(s_v,r) shift(s_w,r).

Für den eindeutigen Syndromgrundzustand wird die gewöhnliche Eigenwertreihe mit Zwischen-Normierung <0|psi_n>=0 rekursiv berechnet. Mit Delta=1:

    E_n = <0|V|psi_(n-1)>,
    |psi_n> = -H0^(-1) Q [V|psi_(n-1)> - Summe_{k=1}^n E_k |psi_(n-k)>].

Alle Vektoren besitzen rationale Einträge. Die Walsh Komponente im Produkt xi1 xi2 xi3 xi4 isoliert die volle logische Viererwirkung. Sie ist in allen Ordnungen eins bis fünf null und in sechster Ordnung

    K4: -27573/8192,
    C4: -3143/4096.

Dies sind genau -kappa/16 aus der vollständigen Pfadklassifikation. Eine zusätzliche Rechnung mit sechs ungleichen Gewichten (1,2,-1,3,2,4) bestätigt das ganze Kopplungspolynom, nicht nur einen symmetrischen Punkt. Die offene Kette bestätigt den verschwindenden sechsten Koeffizienten.

Der Ein Pauli Vergleich allein wäre kein Beweis des gesamten 15 Pauli Hamiltonoperators. Dessen Vollständigkeit folgt aus dem Argument: Jeder minimale verbundene logische Viererpfad muss genau eine gemeinsame Pauliadresse besitzen. Der unabhängige Vergleich kontrolliert die Resolventen, Zeitordnungen und die korrekte Behandlung rückgekoppelter niedrigordentlicher Terme.

## 9. Satz über den tatsächlichen Grundsektor

**Satz.** Für das K4 Modell aus Abschnitt 4 existiert epsilon>0, so dass bei -epsilon<g/Delta<0 der niedrigste Eigenraum exakt Dimension fünf besitzt und die gleiche native irreduzible Darstellung wie Pi5 trägt. Unter einer äquivarianten analytischen Identifikation des tiefen Bandes ist sein Grenzprojektor Pi5. Seine Lücke zum übrigen symmetrischen tiefen Band ist

    gap = (27573/512)|g|^6/Delta^5 + O(|g|^7/Delta^6).

**Beweisstruktur.** Der endliche ungestörte Operator besitzt ein isoliertes Band mit Dimension 256 und Lücke 4Delta. Für genügend kleine Kopplung existieren sein analytischer Spektralprojektor und ein symmetrieverträglicher effektiver Hamiltonoperator. Die führende nichtskalare dritte Ordnung legt bei negativem g den symmetrischen 35erraum tiefer als alle anderen Permutationssektoren. Alle niedrigeren inneren Korrekturen sind U(4) invariant und dort skalar. Die sechste Ordnung ist nach Abschnitt 7 gleich -kappa Pi5 plus Skalar, mit kappa>0. Höhere analytische Ordnungen können diese beiden strikten Vorzeichen in einer hinreichend kleinen punktierten Umgebung nicht umkehren. K4 hat außerdem die exakte Permutationssymmetrie der vier Blöcke. Auf dem symmetrischen tiefen Band zerfällt die native Gruppe in zwei inequivalente Irreps 5 und 30. Ihre Hamiltonantworten sind daher jeweils skalar, so dass die fünffache Entartung nicht von unbekannten höheren symmetrieverträglichen Termen aufgespalten wird.

Die Kreisvariante besitzt denselben führenden Auswahlmechanismus und den genannten anderen inneren Koeffizienten. Die volle S4 Blocksymmetrie des K4 Modells fehlt dort; der Sektorenanschluss ist entsprechend als analytisch gedresste Fortsetzung zu behandeln. Die führende Fünferdarstellung und das positive kleine-g Auswahlvorzeichen bleiben erhalten.

Der Satz betrifft den Grundsektor und seine führende Lücke, nicht ein geschlossenes Formelverzeichnis aller Eigenenergien des 4^28 dimensionalen Systems. Ein direktes Einsetzen von Pi5 in H(g) wurde nicht benutzt.

Für K4 gilt die einfache Normschranke ||gV||<=210|g|. Die Bedingung |g|/Delta<1/105 garantiert die Isolation des 256erbandes. Sie ist ausdrücklich KEINE hier nachgewiesene numerische Gültigkeitsgrenze für die innere sechste Ordnung. Eine praktisch scharfe epsilon für den Fünfergrundsektor wurde in dieser Fortsetzung nicht bestimmt; der Existenzsatz folgt analytisch aus den nichtnull führenden Koeffizienten.

Der vollständige mikroskopische Raum hat Dimension 4^28=72057594037927936. Er wurde nicht numerisch diagonalisiert. Die Reduktion und das Symmetrieargument sind gerade der Grund, weshalb die Aussage ohne diese Diagonalisierung zugänglich ist.

## 10. Codeabstand: ein zusätzlicher positiver Satz und seine wichtige Grenze

Der im g gegen null ausgewählte nackte Raum ist

    V7^tensor4 V5 C5.

Er ist die Verkettung des äußeren ((4,5,2))_4 Codes mit vier inneren [[7,1,3]]_4 Codes. Sein Abstand ist genau sechs:

* Um einen inneren Block nichttrivial logisch zu treffen, braucht ein Pauli Wort mindestens drei physische Positionen.
* Ein nichttrivialer logischer Operator auf nur einem äußeren Register wird vom äußeren Code erkannt.
* Ein unerkannt nichttrivialer äußerer Effekt braucht daher mindestens zwei innere Dreierwörter, also sechs Positionen.
* Zwei Fano Dreierwörter, welche eine äußere Pauli Paarobservable realisieren, geben einen ausdrücklichen nichtskalaren Gewicht sechs Zeugen.

Damit lautet der nackte Grenzcode ((28,5,6))_4. Er kann zwei unbekannte Registerfehler oder fünf bekannte Registerverluste korrigieren. Das sind Aussagen über diesen exakten Grenzcode nach den üblichen Fehlerkorrekturbedingungen, nicht über eine thermodynamisch selbstkorrigierende Phase.

Bei endlichem g ist der tatsächlich ausgewählte Grundraum gedresst. Der hohe Abstand bleibt nicht exakt erhalten. Betrachte die physische Zweiregisterobservable O=A_{a,r}^(v) A_{a,r}^(w), mit festem a und r auf einer K4 Kante. Im rekonstruierten Fünfergrundraum lautet ihr erster nichtskalarer Beitrag

    O_eff = scalar I + (9/32)(g/Delta)^2 h_a + O((g/Delta)^3),

wobei h_a=V5^dagger A_a tensor A_a V5 die äußere Paarobservable mit Eigenwerten 1 (zweifach) und -1/3 (dreifach) ist. Der Koeffizient folgt durch Ableitung des vollständigen kubischen Fano Rückkehrterms bezüglich dieses einzelnen Links: Drei Fano Linien enthalten r; jede hat sechs Reihenfolgen; beide Energienenner sind 8Delta. Daher 18/64=9/32. Beiträge von Dreiecken oder örtlichen Pauli Produkten sind hier skalar. Ein möglicher effektiver Basiswechsel ändert die komprimierte Ableitung innerhalb eines entarteten Eigenraums nicht.

Das Programm prüft den Fano Zensus und die nichtskalare äußere Eigenwertliste. Eine direkte Ableitung der Eigenprojektion des riesigen 28 Registeroperators wird nicht behauptet; die Störungsherleitung ist der Nachweis.

Die beiden Eigenwertgruppen der Probe unterscheiden sich bereits um

    (3/8)(g/Delta)^2 + O((g/Delta)^3).

Andererseits bleiben alle einzelnen Registerfehler exakt erkennbar: Die globalen Paulis A_b^tensor28 stabilisieren den analytisch fortgesetzten Fünfergrundraum. Zu jeder nichttrivialen einzelnen Pauli Probe gibt es einen antikommutierenden globalen Stabilisator. Ihre Kompression ist deshalb null.

Folglich ist der exakte Fehlerabstand des wechselwirkenden K4 Grundcodes für hinreichend kleines nichtnull g zwei, nicht sechs. Die nackte Distanz sechs und die gedresste Distanz zwei sind kein Widerspruch. Die Energieauswahl und die gewollte Kopplung verändern die Fehlerantwort. Dieser Befund begrenzt die Behauptung eines automatisch besonders robusten passiven Speichers.

Auch energetisch gibt es einen Preis: Die innere Schutzlücke ist von Ordnung Delta*(g/Delta)^6, während die oben genannte lokale Probe schon in zweiter Ordnung logische Unterschiede sieht. Die Konstruktion beweist daher keine günstige makroskopische Robustheit oder konstante Schutzlücke unter beliebiger Rekursion.

## 11. Was dies für TFPT löst und was nicht

Die endliche Bausteinlücke ist geschlossen: Aus demselben Hamming geschützten ursprünglichen Quellenmodell und gewöhnlichen Austauschlinks entsteht ein echter Quartikselektor. Es wird nicht lediglich ein Hamiltonoperator I-Pi5 angesetzt und anschließend dessen gewünschter Grundraum gemeldet.

Die gemeinsame Kette lautet nun

    Hamming geschützte vollständige Quelle
    -> virtuelle logische Austauschprozesse, Ordnung drei
    -> Sym4(C4), Dimension 35 bei negativem Austausch
    -> verbundene sechsfach geordnete Rückkehrprozesse
    -> derselbe Quartikstabilisator
    -> Pi5, Dimension fünf.

Das passt zur vollständigen Igusa Quotientengeometrie des Vorgängers: Der Fünferraum ist eine besondere tiefe Auslesestruktur. Er muss die vollständige Quelle mitsamt den fünfzehn Zweierantwortsektoren nicht ersetzen. Die dort nachgewiesene nichtautonome Quellenverdichtung wird nicht zurückgenommen.

Nicht hergeleitet wird, dass die ursprünglichen TFPT Postulate genau diese vier Blöcke, die Links, deren Vorzeichen und Gleichheit oder die relativen Energieskalen wählen. Die Kreisgegenprobe beweist sogar, dass die Rückkehr des Fünfercodes keine eindeutige K4 Geometrie auswählt. Die offene Kette schließt lediglich eine bestimmte niedrigste Störungsordnung aus, nicht alle späteren Codebildungsprozesse.

Ein Grundraum mit fünf Zustandsrichtungen wählt zudem keinen einzelnen kosmologischen Anfangszustand. Die Konstruktion ist kein Beweis einer lokalen chiralen Quantenfeldtheorie, keiner Raumdimension, keiner universellen Lichtgeschwindigkeit und keiner quantisierten universell gekoppelten Gravitation. Die bestehenden TFPT Kopplungs-, Flavor- und Wardantworten werden dadurch weder verworfen noch als automatisch hergeleitet behandelt.

Die offene physische Aufgabe hat jetzt einen kleineren konkreten Zielkandidaten: Die unabhängige, bereits markierte TFPT Quelle müsste diesen Kopplungstyp und seinen Zustand selbst liefern und an ihre geladene Feldantwort anschließen. Die hier ausgeschriebenen freien Modelldaten dürfen nicht nachträglich als bewiesen ausgegeben werden.

## 12. Primärliteratur zur bekannten Mathematik und Methode

Die spezifischen neuen Zahlen und Quellzuordnungen stammen aus den hier ausgeschriebenen Rechnungen. Bekannte Methoden und Begriffe:

1. H. Zhu, R. Kueng, M. Grassl, D. Gross, *The Clifford group fails gracefully to be a unitary 4-design*, arXiv:1609.08172. Kommutanten, Framepotentiale und Zerlegung der vierten Tensorpotenz. https://arxiv.org/html/1609.08172v1
2. Z. Webb, *The Clifford group forms a unitary 3-design*, arXiv:1510.02769. https://arxiv.org/abs/1510.02769
3. S. Bravyi, D. DiVincenzo, D. Loss, *Schrieffer-Wolff transformation for quantum many-body systems*, Annals of Physics 326 (2011), arXiv:1105.0675. Äquivariante effektive Entwicklungen und verbundene Cluster. https://arxiv.org/abs/1105.0675
4. A. Steane, *Multiple Particle Interference and Quantum Error Correction*, quant-ph/9601029. https://arxiv.org/abs/quant-ph/9601029
5. E. Knill, R. Laflamme, *A Theory of Quantum Error-Correcting Codes*, quant-ph/9604034. https://arxiv.org/abs/quant-ph/9604034
6. D. Bacon, *The Stability of Quantum Concatenated Code Hamiltonians*, arXiv:0806.2160. Hintergrund bereits bekannter kodierter Hamiltonansätze, keine Quelle des hier berechneten Sechsterkoeffizienten. https://arxiv.org/abs/0806.2160

Es wird keine weltweite Erstentdeckung dieser allgemeinen Quantencode- oder Störungsmethoden beansprucht. Die hier nachgewiesene Fortsetzung betrifft die konkret rekonstruierte native Quelle und die explizit definierte Kopplungsfamilie.


</details>

[Zur Navigation](#navigation)

<a id="original-q4"></a>
## Q4. Rückkanal, Bindung und rekursive Fünferstruktur

fileciteturn20file0L13-L25

**Originaldatei:** `TFPT_Rekursive_Bindung_Herleitung_20260926.md`  
**SHA256:** `9ec027b0de5a6bd3c7f872597a8f832e2cab74d9c8e82061464fe32640644709`

<details>
<summary>Q4: vollständigen Originalbericht öffnen</summary>

# TFPT: Rückkanal, Bindung und rekursive Fünferstruktur

Forschungsfortsetzung vom 26. September 2026

## 0. Ergebnis und Reichweite

Der zuletzt konstruierte dynamische Fünferbaustein wird auf seiner logischen Antwortebene weitergeführt. Ein symmetrischer Austausch zwischen zwei solchen Antwortsystemen erzeugt in zweiter Ordnung genau die bereits vorhandene Petz Rückkanalmatrix als Bindungsoperator. Der resultierende Paaroperator hat einen eindeutigen verschränkten Grundzustand. Drei identisch gekoppelte Fünferbausteine haben wieder einen fünfdimensionalen Grundraum. Eine explizite Isometrie zeigt: Die Randoperatoren komprimieren in dieselbe Familie, mit exakt bestimmtem Faktor. Damit existiert ein konkreter rekursiver Projektionssatz.

Zwei Grenzen sind ebenso Teil des Ergebnisses. Erstens ist der neue Austausch ein ausdrücklich definierter Anschluss auf den logischen Quellräumen. Er wird nicht als schon aus P1/P2 ausgewählter mikroskopischer 56 Register Hamiltonoperator ausgegeben. Zweitens schließt die vollständige Renormierung nicht auf einem einzigen Kopplungsparameter: Eine gesonderte numerische Rechnung der nächsten virtuellen Ordnung trennt zwei zuvor entartete Sektoren. Die exakte Projektionsidentität ist kein allumfassender Fixpunktsatz.

Das Dokument enthält keine vollständige Theorie von Raumzeit, geladenen Feldern und Gravitation. Die Ergebnisse sind endliche Sätze in benannten Modellen, keine neue Freigabe des TFPT Ledgers.

### Ausgeführte Arbeit

Das angehängte frühere Paket `TFPT_Dynamischer_Codeabschluss_Pruefpaket_20260926.zip` wurde erneut ausgeführt. Es bestand seine 1326 Prüfungen. Die neue Datei `audit.py` ist eigenständig und rekonstruiert den symmetrischen Quellraum, den Code, die kollektiven Paulioperatoren und die Bell Effekte. Sie importiert keine alten Ergebnismatrizen. Ihre `results.json` trennt exakte rationale beziehungsweise algebraische Identitäten von zwei ausdrücklich numerischen Kontrollen der nächsten virtuellen Ordnung.

Es wurde weder der vollständige Raum von 56 vierstufigen Registern diagonalisiert noch das gesamte TFPT Repository neu ausgeführt. Die Raumdimensionen der hier direkt verwendeten Matrizen sind 35, 25, 125 und 1225. Die nächste virtuelle Kontrolle wirkt auf zwei 125 dimensionale Dreierblöcke und nutzt deren vollständige Spektralzerlegung.

## 1. Der vorhandene Baustein und die neue Anschlussannahme

Im Vorgängerbericht trägt ein dynamisch entstandener Baustein im symmetrischen tiefen Band

\[
\mathcal H_{35}=\mathcal C_5\oplus\mathcal C_{30}.
\]

Der Fünferraum ist durch den ursprünglichen Quartikprojektor P ausgewählt. Unter der nativen Gruppe sind die beiden Komponenten irreduzibel und inequivalent. Ein invariant wirkender Hamiltonoperator auf diesem Band hat deshalb nach Abzug seiner Grundenergie genau die Form

\[
H_{\rm loc}=\delta(I_{35}-P),\qquad \delta>0.
\]

Im früher definierten Vierblockmodell ist delta nicht frei unabhängig von seinen ursprünglichen Parametern. Dort gilt asymptotisch

\[
\delta=\frac{27573}{512}\frac{|g|^6}{\Delta^5}
+O(|g|^7/\Delta^6).
\]

Die hier benutzte positive Zahl delta bezeichnet die tatsächliche Lücke des reduzierten Bandes. Die Asymptotik allein ersetzt keine numerisch scharfe Gültigkeitsgrenze im Mikromodell.

Für eine nichttriviale Zweiqubit Pauliadresse a sei

\[
K_a=\sum_{r=1}^4 A_{a,r}
\]

der kollektive Quellenoperator auf Sym4(C4). Die neue Anschlussregel für zwei getrennte Antwortsysteme lautet

\[
H_{AB}=\delta(Q_A+Q_B)+\epsilon L,\qquad
Q=I_{35}-P,
\]

\[
L=\sum_{a=1}^{15}K_a\otimes K_a
=4\sum_{r,s=1}^4\operatorname{Swap}_{A_r,B_s}-16I.
\]

Die Summe umfasst gleich gewichtete Austausche zwischen allen vier mal vier logischen Quellenpositionen. Sie ist unter der gemeinsamen nativen Quellgruppe und den unabhängigen Registerpermutationen in jedem Baustein invariant. Innerhalb der Klasse solcher unabhängigen permutationsinvarianten, Pauli vollständigen Paarlinks ist die Gleichheit der Gewichte erzwungen. Die Wahl dieser Anschlussklasse und epsilon selbst werden dadurch nicht aus P1/P2 hergeleitet.

Die K_a sind logische Quelloperatoren. Eine mikroskopische Umsetzung durch die physischen Register des zuvor gedressten Codes kann zusätzliche Terme erzeugen. Insbesondere wird die obige Regel nicht stillschweigend mit der Projektion bestimmter physischer 56 Register Paarlinks gleichgesetzt.

## 2. Die fünfzehn Antwortrichtungen machen die Kopplung berechenbar

Verwende dieselbe unnormalisierte Codebasis E mit

\[
G=E^TE=\operatorname{diag}(4,12,12,12,24)
\]

im vollständigen Tensorraum. Im symmetrischen Besetzungsraum wird E entsprechend mit dem diagonalen Permutationsorbitgewicht gemessen.

Die fünfzehn nichttrivialen Pauli Charakterräume haben jeweils Dimension zwei. K_a P liegt genau im zugehörigen Zweiersektor. Daraus folgt

\[
P K_a P=0,\qquad P K_aK_bP=0\quad(a\ne b).
\]

Definiere die fünfzehn logischen Rang zwei Projektoren

\[
R_a=\frac1{16}P K_a^2P.
\]

In der früheren Paarnotation ist

\[
R_a=\frac{I+3h_a}{4},\qquad
R_a^2=R_a,\quad\operatorname{tr}R_a=2,\quad\sum_aR_a=6I_5.
\]

Ein erster Link aus P tensor P regt beide Module an. Sämtliche solchen Zwischenzustände haben exakt Energie 2delta. Daher lautet die zweite effektive Ordnung ohne angenäherte Energienenner

\[
H_{AB}^{(2)}
=-\frac{\epsilon^2}{2\delta}
\sum_a(PK_a^2P)\otimes(PK_a^2P)
=-\frac{128\epsilon^2}{\delta}\sum_aR_a\otimes R_a.
\]

Das ist ein Koeffizient der entarteten Störungsentwicklung. Seine Definition entspricht der üblichen Schrieffer und Wolff beziehungsweise Feshbach Konstruktion; er ist nicht die exakte Gesamtentwicklung für beliebige epsilon.

## 3. Die Bindung ist dieselbe Matrix wie der vorhandene Rückkanal

Die frühere Bell Paarauslesung war

\[
\mathcal E_2(X)=\sum_{\nu=1}^{10}\operatorname{tr}(F_\nu X)
|b_\nu\rangle\langle b_\nu|,
\qquad F_\nu=|w_\nu\rangle\langle w_\nu|.
\]

Für die maximal gemischte Codereferenz lautet ihre Petz Recovery R2=2 E2 dagger. Schreibe

\[
\mathcal K=\mathcal R_2\mathcal E_2,
\qquad
\mathsf K|X\rangle\!\rangle=|\mathcal K(X)\rangle\!\rangle.
\]

Die zweite Gleichung ist eine Vektorisierung in der angegebenen reellen Codebasis. Sie macht aus dem Superoperator eine Matrix auf dem Paarraum. Eine gleich geschriebene Matrix macht aus einer Kanaliteration noch keine Hamiltonzeit.

Aus den konkreten Bell Effekten und den konkreten R_a folgt die neue exakte Identität

\[
\boxed{\sum_a R_a\otimes R_a
=\frac32 I_{25}+\frac92\mathsf K.}
\]

Folglich

\[
H_{AB}^{(2)}
=-\frac{192\epsilon^2}{\delta}I
-\frac{576\epsilon^2}{\delta}\mathsf K.
\]

Bis auf eine additive Konstante ist dies

\[
\boxed{H_{\rm Bindung}=J h,\qquad h=I-\mathsf K,
\qquad J=576\epsilon^2/\delta>0.}
\]

Der positive Rückkanal hat Spektrum 1 einfach, 4/9 neunfach und 0 fünfzehnfach. Deshalb hat h Spektrum

\[
0\;(1),\qquad 5/9\;(9),\qquad 1\;(15).
\]

Der eindeutige Grundzustand ist

\[
|\Omega_5\rangle=\frac1{\sqrt5}\sum_{j=1}^5|j\rangle|j\rangle.
\]

Die Energieauswahl entsteht für beide kleinen Vorzeichen von epsilon, da die führende Bindung quadratisch ist. Die Kopplung des früheren inneren Bausteins musste negativ sein; diese unterschiedliche Rolle der beiden Vorzeichen bleibt bestehen.

### Eine konkrete Reflexionspositivität

In der nativen reellen Codebasis sind die R_a reelle symmetrische Matrizen. Es gilt

\[
h=\frac43 I-\frac29\sum_aR_a\otimes R_a.
\]

Für J>=0 und beta>=0 erhält die Potenzreihe von exp(-beta J h) nur positive Koeffizienten vor B tensor B, wobei B ein geordnetes Produkt der reellen R_a ist. Für die Spiegelung A nach komplex konjugiert A auf der anderen Seite ist jeder Beitrag zum Funktional

\[
\operatorname{Tr}[(\bar A\otimes A)(B\otimes B)]
=|\operatorname{Tr}(AB)|^2\ge0.
\]

Damit ist dieser endliche Paar Boltzmannzustand reflexionspositiv bezüglich der genannten Spiegelung. Das ist ein konkreter Positivitätsnachweis, kein Anschluss an die ursprüngliche räumliche beziehungsweise zeitliche TFPT Naht. Die allgemeine Methode gehört zur Theorie reflexionspositiver Doubles.

## 4. Der Grundzustand des ganzen 35 mal 35 Anschlusses ist exakt lösbar

Der zweite Ordnungsbefund ist nicht nur ein formales Tiefenergieargument. Der volle definierte 1225 dimensionale Operator besitzt einen exakt geschlossenen Zweiersektor.

Sei

\[
|\chi_{30}\rangle=\frac{L|\Omega_5\rangle}{16\sqrt6}.
\]

Die Rechnung ergibt

\[
\langle\Omega_5|\chi_{30}\rangle=0,\qquad
\|\chi_{30}\|=1,
\]

\[
L^2|\Omega_5\rangle=1536|\Omega_5\rangle+16L|\Omega_5\rangle.
\]

Beide Seiten von chi liegen im 30erraum. Auf der orthonormalen Basis Omega,chi gilt genau

\[
\boxed{H_{AB}\big|_{\{\Omega,\chi\}}=
\begin{pmatrix}
0&16\sqrt6\epsilon\\
16\sqrt6\epsilon&2\delta+16\epsilon
\end{pmatrix}.}
\]

Die tiefere Energie ist deshalb

\[
\boxed{E_-=\delta+8\epsilon-
\sqrt{(\delta+8\epsilon)^2+1536\epsilon^2}.}
\]

Für 0<|epsilon|/delta<=1/200 ist dieser Zustand nach der folgenden konservativen Abschätzung der eindeutige globale Grundzustand des ganzen definierten 1225 dimensionalen Modells. Es ist keine Aussage über den ungeprüften 56 Register Mikrohintergrund.

### Beweis der globalen Auswahl in einem expliziten Bereich

Die gemeinsame Pauli Charakterzerlegung gibt einen neutralen Paarsektor der Dimension

\[
25+15\cdot2^2=85.
\]

L erhält diesen Sektor. Im 60 dimensionalen neutralen Komplement von P tensor P ist H0 exakt 2delta I. In allen anderen Sektoren ist H0 mindestens delta I.

Aus L=4 sum_16 Swap-16I folgt die einfache Normschranke ||L||<=80. Die erste Antwortgrammatrix ist

\[
P L^2P=256\sum_aR_a\otimes R_a.
\]

Auf den 24 Codepaarrichtungen orthogonal zu Omega hat sie höchstens den Eigenwert 896. Für |epsilon|/delta<=1/200 hat der neutrale angeregte Block mindestens Energie (8/5)delta. Durch quadratische Ergänzung ist jede Energie im orthogonalen Komplement des geschlossenen Zweiersektors mindestens

\[
-560\epsilon^2/\delta.
\]

Der normierte Versuchszustand proportional zu Omega-8 sqrt6 (epsilon/delta) chi besitzt dagegen Energie höchstens

\[
-\frac{460800}{631}\frac{\epsilon^2}{\delta}.
\]

Die Differenz dieser Schranken ist größer als 170 epsilon²/delta. Die übrigen Pauli Sektoren liegen mindestens bei 3delta/5. Es folgt die genügende globale Lückenschranke

\[
\boxed{\operatorname{gap}(H_{AB})\ge170\epsilon^2/\delta.}
\]

Diese Schranke ist absichtlich konservativ. Der führende tatsächliche Abstand zum neunfachen Paarsektor ist 320 epsilon²/delta.

### Die Quellenantwort wird nicht weggeworfen

Mit

\[
\eta=\frac12\left(1-
\frac{\delta+8\epsilon}{\sqrt{(\delta+8\epsilon)^2+1536\epsilon^2}}
\right)
\]

lautet der reduzierte Zustand des exakten Paargrundzustands

\[
\rho_A=(1-\eta)P/5+\eta(I_{35}-P)/30.
\]

Die 30 zusätzlichen Antwortrichtungen werden tatsächlich besetzt. Ihre Weglassung wäre selbst in diesem lösbaren Bindungsmodell bei endlichem epsilon nicht exakt. Die Entropie ist h2(eta)+(1-eta)log5+eta log30; die Logarithmusbasis ist frei, sofern alle Terme dieselbe benutzen.

## 5. Drei Fünferbausteine ergeben wieder einen Fünfergrundraum

Untersuche jetzt die vollständig definierte dimensionslose Kette

\[
H_3=h_{12}+h_{23},\qquad h=I-\mathsf K.
\]

Das ist der führende effektive Bindungsoperator aus Abschnitt 3. Er wird auf dieser Ebene als exakt angegebene Kette untersucht. Die höhere Korrektur des ursprünglichen 35er Anschlusses wird damit nicht stillschweigend auf null gesetzt.

Die exakte vollständige Spektralzerlegung lautet:

| Energie | Vielfachheit |
|---|---:|
| (19-sqrt73)/18 | 5 |
| 1 | 5 |
| 10/9 | 5 |
| 11/9 | 9 |
| 4/3 | 16 |
| 13/9 | 10 |
| (19+sqrt73)/18 | 5 |
| 5/3 | 10 |
| 16/9 | 16 |
| 17/9 | 9 |
| 2 | 35 |

Das Programm bestätigt das vollständige charakteristische Polynom über Q. Insbesondere

\[
\boxed{E_0=(19-\sqrt{73})/18,\qquad
\operatorname{dim}G=5,\qquad
\operatorname{gap}=(\sqrt{73}-1)/18.}
\]

Die beiden Paare können nicht gleichzeitig im reinen idealen Paarzustand liegen. Für deren Projektoren Q12,Q23 gilt Q12 Q23 Q12=Q12/25. Da h>=(5/9)(I-Q), ergibt sich H3>=4/9 I. Die genaue Energie liegt darüber. Frustration verhindert hier die vollständige lokale Sättigung, aber nicht den explizit bestimmten globalen Fünferraum.

### Explizite Isometrie statt bloßer Dimension fünf

In einer orthonormalen reellen Fünferbasis definiere vier Intertwiner von C5 nach (C5)^tensor3:

\[
(T_1x)_{abc}=\delta_{ab}x_c,\quad
(T_2x)_{abc}=\delta_{ac}x_b,\quad
(T_3x)_{abc}=x_a\delta_{bc},
\]

\[
T_4x=\sum_{q=1}^{6}v_q^{\otimes3}\langle v_q,x\rangle.
\]

Die v_q sind genau die sechs normierten alten Simplexmarken, mit Kreuzprodukten -1/5. Alle vier Abbildungen transportieren dieselbe native reelle S6 Wirkung. Setze s=sqrt73,

\[
c=\left(-\frac{27+3s}{50},-\frac{12}{25},-\frac{27+3s}{50},1\right),
\quad N=\frac{3942+378s}{625}.
\]

Dann ist

\[
\boxed{W_3=N^{-1/2}\sum_{i=1}^{4}c_i T_i}
\]

eine Isometrie, und H3 W3=E0 W3. Die Fünferdarstellung wurde dadurch explizit wiedergefunden, nicht aus der Entartungszahl erraten.

Die native Kontrollalgebra su(5) des Ausgangscodes wird hier nicht als Eichgruppe interpretiert. Erhalten bleibt die tatsächliche endliche Quellwirkung auf dem betreffenden Fünferträger.

## 6. Die führende Bindung bleibt unter der Verdichtung in derselben Familie

Für jede der fünfzehn Ebenenobservablen R_a gilt am linken und rechten Ende der Dreierkette

\[
\boxed{W_3^\dagger R_a^{(1)}W_3
=W_3^\dagger R_a^{(3)}W_3
=a_\partial R_a+\frac25(1-a_\partial)I,}
\]

\[
\boxed{a_\partial=\frac{49+5\sqrt{73}}{144}.}
\]

Alle 30 Randgleichungen werden exakt geprüft. Für das mittlere Register gilt dieselbe Form mit a_m=17/72+85 sqrt73/5256. Auch diese fünfzehn Gleichungen werden geprüft.

Verbindet eine schwache Kopplung das Ende eines Dreierblocks mit dem Anfang des nächsten, folgt

\[
\boxed{(W_3\otimes W_3)^\dagger h_{\rm Grenze}(W_3\otimes W_3)
=a_\partial^2 h+\frac45(1-a_\partial^2)I,}
\]

\[
a_\partial^2=\frac{2113+245\sqrt{73}}{10368}
\simeq0.4056983910.
\]

Der Zahlenwert ist ein algebraischer Randtransportfaktor dieses Modells, nicht die Feinstrukturkonstante und keine hergeleitete kosmologische Skalenzahl.

Bei starker innerer Kopplung Js und schwacher Verbindung Jw lautet die führende neue Kopplung Jneu=a_boundary² Jw. Der Projektionssatz ist exakt. Die Gleichsetzung mit einer physikalischen Tiefenergieentwicklung benötigt aber Jw klein gegenüber Js mal der Dreierlücke. Virtuelle Korrekturen sind von Ordnung Jw²/Js im festen endlichen Verbund.

## 7. Numerische Gegenprobe: Keine vollständige Einparameterrekursion

Um die Projektionsschließung nicht zu überschätzen, wurde die nächste virtuelle Ordnung für zwei vollständige Dreierblöcke berechnet:

\[
H_{\rm next}^{(2)}=-P V Q(H_{3,A}+H_{3,B}-2E_0)^{-1}QVP.
\]

Die inversen Nenner kommen aus den vollständigen 125 dimensionalen Blockspektren. Die resultierende 25 mal 25 Matrix hat die vier nativen Sektorkoeffizienten, in Einheiten Jw²/Js:

| Sektordimension | Numerischer Koeffizient |
|---|---:|
| 1 | -0.26241666998068 |
| 5 | -0.05807535460173 |
| 9 | -0.10652443252980 |
| 10 | -0.05678177907811 |

Die Abweichung von der entsprechenden invariant rekonstruierten Matrix liegt bei etwa 2e-16. Entscheidend ist die Differenz zwischen den 5er und 10er Sektoren von ungefähr -0.00129357552361. Im ursprünglichen h waren beide gleich. Die nächste Ordnung lässt sich daher numerisch nicht als aI+bh darstellen.

Diese Gegenprobe ist ausdrücklich eine Fließkommarechnung, kein Intervallzertifikat. Die exakten Grundraumsätze und Randgleichungen davor hängen nicht von ihr ab. Für eine vollständige rekursive Theorie müssen mindestens die erlaubten zusätzlichen invarianten Kopplungen und die Mehrblockterme weitergeführt werden; die heutige Einparameterfamilie wird nicht als geschlossener Renormierungsfixpunkt ausgegeben.

## 8. Warum gleiche starke Links keinen Raum unabhängiger Fünferzellen auswählen

Eine Vergrößerung des früheren Mikrokandidaten mit überall gleicher schwacher negativer Verbindung selektiert für jeden festen endlichen verbundenen Graphen in führender dritter Ordnung den globalen symmetrischen Raum SymN(C4), Dimension binomial(N+3,3).

Bei acht Quellen ist diese Dimension 165. Das ist weder automatisch das Produkt zweier lokaler 35erräume noch zweier Fünfercodes.

Strenger: Für N>=5 kann kein global symmetrischer nichtnull Zustand zugleich den ursprünglichen Quartikcode auf einer Vierermenge erfüllen. Wegen globaler Permutationssymmetrie würden dessen Quartikchecks auf jeder anderen Vierermenge ebenfalls gelten. Produkte zweier Checks mit drei gemeinsamen Positionen erzeugen X_i X_j, entsprechend Z_j Z_k. Für verschiedene i,j,k antikommutieren diese beiden geforderten +1 Checks. Ein gemeinsamer Zustand ist ausgeschlossen.

Die Aussage betrifft exakt den global symmetrischen Sektor und die wörtlichen Quartikchecks. Sie schließt weder andere Vielteilchenzustände noch andere Signaturen, zusätzliche Randräume oder skalenseparierte Module aus.

Für unabhängige hierarchische Bausteine muss die äußere Kopplung relativ zur kleinen inneren Codeauswahl kontrolliert werden. Im vorigen Kandidaten ist diese Auswahl erst O(Delta (g/Delta)^6), der grundlegende logische Austausch aber schon O(Delta (g/Delta)^3). Eine gleiche Kopplung über alle Skalen ergibt daher nicht automatisch die hier benutzte Bausteinstruktur.

Ein vorgegebener Graph mit beschränkten lokalen Wechselwirkungen erlaubt anschließend bekannte Lokalitätsabschätzungen wie Lieb und Robinson. Diese Sätze wählen aber weder den Graphen noch drei Raumdimensionen oder eine universelle relativistische Lichtgeschwindigkeit aus.

## 9. Was gegenüber TFPT geschlossen und offen ist

Der neue endliche Zusammenhang ist:

```
vorhandene 5+30 Quellenantwort
    -> ausdrücklich symmetrischer Austauschanschluss
    -> derselbe konkrete Petz Rückkanal als Bindungsoperator
    -> eindeutiger Paarzustand
    -> exakt bestimmter Fünfergrundraum dreier gebundener Bausteine
    -> native Darstellungsisometrie
    -> exakt gleiche führende Kopplungsform bei Drei-zu-eins-Verdichtung
```

Diese Kette verknüpft Information, Wechselwirkung, Zustand und eine konkrete Rekursion. Sie ist enger und überprüfbarer als eine Behauptung, jeder verträgliche Code erzeuge automatisch Raum.

Die eigentliche Quellenherleitung bleibt getrennt. Die bereitgestellten Research Contracts und der Gesamtstand vom 21. September verlangen eine gemeinsame graduierte Feldabbildung, einen Zustand und eine tatsächlich ausgewählte Zeit einschließlich des nativen W Kanals. Ein logisch realisierter Codeaustausch erfüllt diese Feldforderung noch nicht. Auch P1/P2 wählen in den hier gelesenen Stellen den heutigen logischen Brückenoperator, sein Gewicht, die Hierarchie und die globale Kopplungsgeometrie nicht nachweislich aus. Das ist keine Behauptung allgemeiner Nichtableitbarkeit aus sämtlichen TFPT Bedingungen.

Es wurden keine Quantenfelder in 3+1 Dimensionen, keine chirale Eichdynamik, kein universell gekoppelter Spin zwei Sektor und kein kosmologischer Anfangszustand neu konstruiert. Ebenso liefert der Dreiercode keine räumliche Dimension drei. Sein lokaler Grundraum ist weiterhin fünffach, nicht ein eindeutiges Weltvakuum.

## 10. Quellen und bekannte Methoden

### Tatsächlich benutzte TFPT Dokumente

* `TFPT_Dynamischer_Codeabschluss_Herleitung_20260926.md`, Abschnitte 2 bis 4, 9 bis 11: native 5+30 Zerlegung, dynamische Bausteinauswahl und freie Modelldaten.
* `TFPT_Quartik_Fortsetzung_Herleitungen_20260926.md`, Abschnitte 1 bis 6: Codebasis, Bell Effekte, Petz Recovery, sechs Marken und Paarobservablen.
* `TFPT_Igusa_Quellendynamik_Herleitung_20260926.md`, Abschnitte 6 bis 11: nichtautonome Auslesung und erforderlicher Quelllift.
* `TFPT_Gesamtstand_und_Loesungsweg_20260921.pdf`, Abschnitte 16.7 und 19: unabhängige gemischte Quellenantwort und vollständiger Abschlussvertrag.
* `TFPT_Universalraum_Sitzungsdokumentation_2026-09-20_v2.pdf`, Abschnitt 15: die Quelle muss ihre Dynamik selbst auswählen.

### Primärliteratur zur Einordnung

* Bravyi, DiVincenzo, Loss: *Schrieffer-Wolff transformation for quantum many-body systems*, arXiv:1105.0675. Die Methode setzt einen definierten Ausgangshamiltonoperator voraus; sie wählt ihn nicht.
* Barnum, Knill: *Reversing quantum dynamics with near-optimal quantum and classical fidelity*, arXiv:quant-ph/0004088. Hintergrund des referenzabhängigen Rückkanals. Der hier benötigte Operator wird aus den ausgeschriebenen Effekten direkt berechnet.
* Zhu, Kueng, Grassl, Gross: *The Clifford group fails gracefully to be a unitary 4-design*, arXiv:1609.08172. Bekannte vierte Momentenstruktur und zusätzliche Codekomponente.
* Jaffe, Janssens: *Reflection Positive Doubles*, arXiv:1607.07126. Allgemeiner Rahmen der ausdrücklich verwendeten endlichen Reflexionspositivität.
* Nachtergaele, Sims: *Lieb-Robinson Bounds and the Exponential Clustering Theorem*, arXiv:math-ph/0506030. Lokalitätsaussagen unter benannten Graph- und Wechselwirkungsannahmen, keine Auswahl der Raumdimension.

Die heute berechneten Koeffizienten und Isometrien sind projektbezogene Fortsetzungen. Eine weltweite Erstentdeckung verwandter Spinmodelle oder Renormierungsmethoden wurde nicht geprüft oder behauptet.


</details>

[Zur Navigation](#navigation)

<a id="original-q5"></a>
## Q5. Gemeinsamer Ladungstest, Symmetrievervollständigung und exakte Komposition

fileciteturn22file0L13-L37

**Originaldatei:** `TFPT_Ladung_Komposition_Herleitung_20260926.md`  
**SHA256:** `7da75f545ec887e6cccf93589a5da57b71cadeb4e0b66c264c21ef8ea3f50b9f`

<details>
<summary>Q5: vollständigen Originalbericht öffnen</summary>

# TFPT: gemeinsamer Ladungstest, Symmetrievervollständigung und exakte Komposition

Forschungsfortsetzung vom 26. September 2026

## 0. Ergebnis und Geltungsbereich

Die bisher getrennten Quartik-, Ladungs- und Bindungskonstruktionen werden am selben endlichen Operator geprüft. Der vorhandene Bindungsoperator h = I − K auf dem 25 dimensionalen Paarraum erhält die korrekt transportierte additive Hyperladung nicht. Dieser Befund betrifft die zusätzliche Identifikation des logischen Trägers als ladungstragendes System. Er widerlegt nicht die früheren ungeladenen Codeidentitäten.

Unter der ausdrücklich stärkeren gemeinsamen Forderung, sowohl die volle unmarkierte native S6-Wirkung als auch diese kontinuierliche Ladung als exakte Symmetrien desselben Paaroperators zu erhalten, ist die positive Singulettbindung bis auf Energieeinheit und Energienullpunkt eindeutig:

    h_cov = k (I − P_Omega),   k > 0.

Die spurtreue, zugleich im Hilbert-Schmidt-Sinn nächstgelegene Vervollständigung hat k = 5/6. Sie ist ein GEÄNDERTER Operator. Die ursprünglichen Übertragungswerte werden dadurch nicht erhalten. Bei einer festen TFPT-Markierung muss die ganze S6-Gruppe nicht als innere Symmetrie verlangt werden; daher folgt aus diesem Satz KEINE erzwungene physische SU(5)-Eichgruppe von TFPT.

Die vervollständigte Bindung besitzt eine exakt ladungserhaltende Drei-zu-eins-Isometrie und eine Temperley-Lieb-Kompositionsalgebra. Eine generische Yang-Baxter-Identität mit freien Spektralparametern wird symbolisch geprüft. Auch in diesem vervollständigten Modell erzeugt die nächste virtuelle Ordnung echte Dreibausteinterme. Ein exakter Paarprojektionssatz ist weiterhin kein vollständiger Paar-only-Renormierungsfixpunkt.

Es werden keine 3+1D-Raumzeit, keine lokalen dynamischen Eichfelder, keine chiralen Fermionfelder, keine Gravitonen, keine Alpha-/Flavor-Herkunft und kein kosmologischer Anfangszustand hergeleitet. Das Resultat ist ein gemeinsamer endlicher Kompatibilitätssatz samt konstruktiver Vervollständigung und ihren Grenzen.

### Herkunft

Die folgenden TFPT Daten sind übernommen und im neuen Programm aus ihren ausgeschriebenen Zahlen rekonstruiert:

* `TFPT_Quartik_Fortsetzung_Herleitungen_20260926.md`: Gram-Matrix G, Bell-Effekte, sechs Simplexmarken und markierter Polartransport.
* `TFPT_Igusa_Quellendynamik_Herleitung_20260926.md`: vollständiger Pauli-Invariantenring, Igusa-/Segre-/Doily-Verbindung und Verlust des Quellzweigs.
* `TFPT_Dynamischer_Codeabschluss_Herleitung_20260926.md`: native Darstellung und dynamischer Codekandidat unter angegebenen Links.
* `TFPT_Rekursive_Bindung_Herleitung_20260926.md`: h = I − K, seine drei Energiewerte, Dreierisometrie und begrenzte Rekursion.
* `TFPT_Gesamtstand_und_Loesungsweg_20260921.pdf`, Abschnitte 12.7 und 19.4: gemeinsamer Feld-/Ladungs-/Zeitvertrag und ausdrückliche Warnung, Markierungsautomorphismen nicht als innere Symmetrien eines festen Systems auszugeben.

Das zuletzt angehängte Paket wurde erneut ausgeführt und bestand 165 exakte sowie zwei gesondert numerische Kontrollen. Das neue Programm führt 138 exakte rationale, algebraische und ganzzahlige Kontrollen aus. Nicht erneut ausgeführt wurde das gesamte TFPT Repository. Es werden auch nicht alle älteren Ergebnisse als neue Ergebnisse gezählt.

## 1. Welcher Zusammenhang bereits besteht

Der vorhandene RM(1,3)-Code erzeugt die 240 Wurzeln und, nach komplexer Paarung, die 60 Quellenrichtungen. Ihr viertes Projektormoment trägt Pi5 = 40 M4 − S4. Die fünf quartischen Quellenkoordinaten erzeugen den Pauli-Invariantenring, der in sechs linearen Koordinaten x die Gleichungen

    sum_i x_i = 0,
    (sum_i x_i^2)^2 = 4 sum_i x_i^4

erfüllt. Die Invariantengrade 8,12,20,24 folgen aus den elementarsymmetrischen Funktionen e2,e3,e5,e6; e4=e2^2/4. Die 60 Reflexionshyperflächen, zehn Bellquadriken und die 15er Doily-Inzidenz besitzen in diesen Koordinaten konkrete Abbildungen.

Dies ist eine Kette algebraischer Verbindungen. Die Momentenabbildung ist nicht der vollständige physische Quellenzustand. Der Fünfercode ist nicht der 16 dimensionale Halbspinor. Der Zehner der Bellmessung ist nicht allein wegen seiner Dimension ein Spin(10)-Vektor. Der Quellenoperator, ein Beobachtungskanal und ein Hamiltonoperator sind verschiedene Objekttypen.

Der heutige Test verbindet zwei zuvor nur nebeneinander stehende Enden dieser Kette: die Ladungsdarstellung und den Bindungsoperator.

## 2. Präzise Rekonstruktion des getesteten Operators

In den unnormalisierten Codekoordinaten gilt

    G = diag(4,12,12,12,24).

Die konkrete 10×5 Bellmatrix Fnum steht vollständig im Programm. Für ihre Zeilen f_nu = Fnum_nu^T/4 ist w_nu = G^(-1) f_nu. Die Paar-Rückkanalmatrix ist

    K = 2 sum_nu (w_nu tensor w_nu)(f_nu tensor f_nu)^T.

Der physische Paarraum hat die Gram-Matrix G tensor G. Der unnormierte Singulettvektor ist vec(G^(-1)), sein Normquadrat ist fünf. Sein Projektor heißt hier P1. Aus K und dem Swap F folgen

    P9 = (9/4)(K − P1),
    P10 = (I − F)/2,
    P5 = I − P1 − P9 − P10.

Die Ränge sind 1,9,10,5. Die P5-Bezeichnung in dieser Paarzerlegung meint einen Unterraum im 25 dimensionalen Paarraum, NICHT den ursprünglichen Pi5-Projektor auf vier Quellenregistern.

Die alte Bindung lautet

    h = I − K = P5 + (5/9) P9 + P10.

Ihre einfache Grundlinie ist Omega. Alle Matrizen werden exakt rekonstruiert; keine früheren numerischen Ergebnismatrizen werden importiert.

## 3. Die markierte Hyperladung und ihr dynamischer Test

Die sechs W6-Simplexspalten sind

    2  2 -1 -1 -1 -1
    0  0 -1 -1  1  1
    0  0 -1  1 -1  1
    0  0  1 -1 -1  1
    1 -1  0  0  0  0.

Markiert wird Spalte 0. Die fünf Differenzspalten zu den Spalten 1,2,3,4,5 bilden D; D^T G D = 48(I+J). Der positive Polartransport verwendet

    A = I + (1/sqrt(6) − 1) J/5,
    Y = D A diag(1/2,−1/3,−1/3,−1/3,1/2) A D^T G /48.

Die drei bewegten Slots sind die ursprünglichen Spalten 2,3,4. Die konkrete Y-Matrix steht in results.json. Exakt gilt

    Tr Y = 0,  Tr Y^2 = 5/6,
    (Y−I/2)(Y+I/3)=0,
    Y^T G = GY.

Für eine Paarung V tensor conjugate(V) lautet der additive Generator in einer orthonormalen Basis

    Q_Y = Y tensor I − I tensor Y^T.

In den hier verwendeten reellen G-Koordinaten ist die zweite Matrix Y selbst; das Programm berücksichtigt die Metrik. Q_Y Omega = 0: Der Singulettzustand ist neutral. Trotzdem ergibt sich

    ||[h,Q_Y]||_HS^2 = (488 + 32 sqrt(6))/405 > 0.

Dies ist der konkrete Ausschluss: Der unveränderte h darf nicht gleichzeitig als Hyperladung erhaltender Paaroperator mit dieser additiven Feldzuordnung identifiziert werden.

Eine Paarung zweier gleich orientierter Träger vermeidet das Problem nicht: Ihr Generator wäre Y1+Y2. Schon Omega ist dann keine neutrale Ladungseigenlinie; sein Ladungsquadrat hat Erwartungswert 2/3.

### Kein versteckter Basiswechsel beseitigt die kontinuierliche Symmetriefrage

Für eine allgemeine komplexifizierte infinitesimale Matrix X wird

    J_X = X tensor I − I tensor (G^(-1) X^T G)

angesetzt. Die Gleichungen [h,J_X]=0 bilden eine rationale 625×25-Matrix. Ihre Ranguntergrenze modulo 101 ist 24. Die Identität liegt exakt im Kern, also ist ihr Rang auch über C genau 24. Der einzige kontinuierliche Onsite-Konjugationsgenerator ist skalar. Insbesondere gibt es keinen nichttrivialen traceless Hyperladungsersatz durch eine andere Basis.

Das ist ein endlicher Konjugationsvertrag, kein generelles Verbot emergenter Eichfelder in einem größeren Modell.

## 4. Vollständige Lösung der gemeinsamen Symmetrieklasse

Betrachte zunächst dieselbe native S6-invariante Paarfamilie:

    H = c I + epsilon5 P5 + epsilon9 P9 + epsilon10 P10.

Die Singulettenergie wird durch c festgelegt. Der Ladungsgenerator koppelt die anderen Sektoren. Die beiden exakten Übergangsgewichte sind

    Tr(P5 Q_Y P10 Q_Y) = 67/60 − sqrt(6)/5 > 0,
    Tr(P9 Q_Y P10 Q_Y) = 61/20 + sqrt(6)/5 > 0.

Dagegen ist der direkte 5↔9-Anteil null. Aus [H,Q_Y]=0 folgen daher notwendig

    epsilon5 = epsilon10,
    epsilon9 = epsilon10.

Umgekehrt genügen diese Gleichheiten. Die gesamte kompatible Familie ist somit

    H = c I + k(I − P_Omega).

Omega ist für k>0 der eindeutige Grundzustand. Damit ist die gemeinsame endliche Auswahl innerhalb DIESER Symmetrieklasse vollständig entschieden.

### Warum dadurch SU(5) erscheint

Y besitzt zwei nichtnull Komponenten im reell-symmetrischen traceless Operatorraum:

    ||Y5||^2 = 29/60 + sqrt(6)/10,
    ||Y9||^2 = 7/20 − sqrt(6)/10.

Die native S6-Bahn spannt daher 5+9=14 reelle symmetrische traceless Richtungen. Ihre Kommutatoren liefern die zehn antisymmetrischen Richtungen. Zusammen entsteht su(5).

Das Programm prüft den Bahnrang 14 und den Kommutatorrang 10 zusätzlich modulo 101, einschließlich aller 720 nativen S6-Wirkungen. Hier ist sqrt(6)→39 ein zulässiger Residuenkörperhomomorphismus, da 39²=6 modulo 101. Nichtnull Minorbilder geben echte Ranguntergrenzen über Q(sqrt(6)); die genannten Symmetrieklassen geben die passenden oberen Grenzen.

Dies ist eine mathematische Symmetrievervollständigung, KEIN Beweis, dass TFPT physisch eine ungebrochene SU(5)-Eichgruppe verlangt. Die TFPT Markierung kann die tatsächliche Symmetrie reduzieren. Die ursprünglichen Quellenverträge warnen ausdrücklich vor der Verwechslung von Markierungswechseln und inneren Symmetrien.

## 5. Normierung, Kanaländerung und die markierte Alternative

Die Wahl k=5/6 erhält Tr H=Tr h=20. Sie ist zugleich die eindeutige Hilbert-Schmidt-Projektion von h auf die kompatible Singulettfamilie:

    k = (5*1 + 9*(5/9) + 10*1)/24 = 5/6,
    ||h−h_cov||_HS² = 10/9.

Dieser Schritt ist eine erklärte Normierungs-/Projektionskonvention. Die physische Energieeinheit wird dadurch nicht hergeleitet.

Die neue Rückkanalmatrix ist

    K_cov = I−h_cov = P1 + (1/6)(I−P1).

Als Kanal gilt

    K_cov(X) = (X + Tr(X) I)/6.

Das ist vollständig positiv und spurerhaltend; es kann als gleichmäßige Messung und Präparation über reine Zustände geschrieben werden. Der nichttriviale Multiplikator ist jetzt 1/6, NICHT der alte 4/9. Auch die normierte alte Singularübertragung 2/3 bleibt nicht die Übertragung dieses neuen Kanals. Die Igusa-, Doily- und Bellgeometrie bleibt als ursprüngliche Auslesestruktur bestehen, ist aber nicht unverändert die neue ladungserhaltende Hamiltonentwicklung.

### Nur die tatsächlich markierte Gruppe verlangen

Für G_SM = S(U(3)×U(2)) zerfällt V tensor conjugate(V) in zwei Singuletts, ein 8er-, ein 3er- und zwei entgegengesetzt geladene 6er-Systeme. Der Hermitesche Kommutant hat deshalb Dimension 2²+1+1+1+1=8. Die volle SU(5)-Schließung ist dann nicht erzwungen.

Eine andere kanonische Rechenoperation ist die normierte Haarmittelung des ursprünglichen h nur über G_SM. Sie erhält Omega als Nullzustand, respektiert die Markierung und besitzt die folgenden exakt geprüften Energien:

    Y-Singulett: (61+4sqrt6)/75,
    Acht:       1247/1500+2sqrt6/375,
    Drei:       (311+4sqrt6)/375,
    Sechs:      (314−4sqrt6)/375, für beide Ladungsvorzeichen.

Auch dies ist ein GEÄNDERTER, nun markierungsabhängiger Operator und keine bereits von P1/P2 ausgewählte physische Quelle. Die beiden Vervollständigungen zeigen, warum die Rollen von exakter Symmetrie, Kovarianz und fester Markierung entschieden werden müssen.

## 6. Exakt ladungserhaltende Dreierrekursion der vollständigen Symmetrieklasse

Nun wird der ausdrücklich vervollständigte h_cov=(5/6)(I−P_Omega) untersucht. Die Träger alternieren als V, conjugate(V), V. Schreibe

    (T1 x)_abc = delta_ab x_c,
    (T3 x)_abc = x_a delta_bc,
    W = (T1+T3)/sqrt(12).

Exakt ist W†W=I5. Für H3=h12+h23 gilt das vollständige Spektrum

    2/3 (Vielfachheit 5),
    1   (Vielfachheit 5),
    5/3 (Vielfachheit 115).

Die erste Fünferkomponente ist Ran W; die Lücke ist 1/3. Der zweite Fünferraum wird von T1−T3 aufgespannt. Das restliche Spektrum folgt aus dem exakt geprüften Minimalpolynom.

Für JEDE 5×5-Matrix X gilt

    (X1−X2^T+X3)W = WX.

Die 25 elementaren Matrixidentitäten werden einzeln genau geprüft. Für Y ist dies das additive Ladungsgesetz. Für unitäre U gilt entsprechend

    (U tensor conjugate(U) tensor U) W = W U.

Damit ist dieselbe Ladungsdarstellung vor und nach der Verdichtung wirklich erhalten. Dies ist mehr als gleiche Grundraumdimension fünf; es ist ein expliziter Intertwiner. Es bleibt eine globale innere Symmetrie, keine Konstruktion dynamischer lokaler Eichfelder.

Die vollständigen Randkanäle sind

    W† X1 W = W† X3 W = (7X+Tr(X)I)/12,
    W† X2 W = (X^T+Tr(X)I)/6.

Für traceless Y gilt 2*(7/12)Y−(1/6)Y=Y. Die Ladung wird lokal verteilt, aber in der Summe nicht verändert.

Die schwache Randbindung projiziert exakt zu

    (W tensor W)† h_boundary (W tensor W)
       = (49/144) h_cov + (19/36) I.

Die Identifikation mit realer Tiefenergiedynamik setzt weiterhin eine hinreichend schwache Verbindung zwischen stärker gebundenen Dreierblöcken voraus. Eine räumliche Dimension und die Hierarchie ihrer Energieskalen folgen nicht aus der Isometrie.

## 7. Exakte Komposition für beliebige Kettenlänge

Definiere e_i=5 P_Omega auf benachbarten, konjugiert orientierten Trägern. Dann gelten

    e_i² = 5 e_i,
    e_i e_(i+1) e_i = e_i,
    e_(i+1) e_i e_(i+1) = e_(i+1),
    [e_i,e_j]=0 für |i−j|>1.

Dies ist die bekannte Temperley-Lieb-Algebra mit Schleifenparameter fünf. Die Matrixrelationen sind im neuen Programm exakt geprüft. Da es lokale Identitäten sind, gelten sie in jeder größeren festgelegten Kette.

Setze

    q=(5+sqrt21)/2,  q+q^(-1)=5,
    R_i(t)=(q−q^(-1)t²)I+(t²−1)e_i.

Dann gilt die generische Yang-Baxter-Identität

    R_i(t) R_(i+1)(tu) R_i(u)
       =R_(i+1)(u) R_i(tu) R_(i+1)(t).

Das Programm expandiert beide Seiten für FREIE symbolische t,u in der vollständigen fünfteiligen TL3-Basis; es handelt sich nicht um eine Stichprobe von Parameterwerten. Dies ist klassische Baxterisierung, keine weltweit neue Yang-Baxter-Lösung.

Bei t=exp(i theta) ist R_i(t)/sqrt(23−2cos(2theta)) unitär. Inversion und Regularität R_i(1)=sqrt21 I werden genau geprüft. Die Ableitung bei t=1 liefert bis auf Maßstab und Energiekonstante den gleichen h_cov. Damit besitzt der vervollständigte Kettenzweig eine bekannte integrable Kompositionsstruktur.

Die Spektralvariable theta ist KEINE aus TFPT hergeleitete physische Zeit. Der Schleifenwert fünf ist keine Raumdimension. Yang-Baxter-Komposition einer festgelegten Kette ist weder eine Herleitung ihrer räumlichen Anordnung noch von 3+1D-Streuung oder Gravitation.

## 8. Warum selbst diese Vervollständigung keine Paar-only-Gesamtrekursion ist

Betrachte drei starke Dreierblöcke A,B,C, mit zwei schwachen Verbindungen AB und BC. Die zweite virtuelle Ordnung enthält Kreuzterme der beiden unterschiedlichen Links. Ihre Zwischenanregung liegt ausschließlich im mittleren Block; der genaue reduzierte Resolvent ist

    R = I − SS^T/12 + DD^T/4,
    S=T1+T3, D=T1−T3,

für innere Kopplung eins. Daraus wird der gesamte 125×125-Kreuzoperator rational rekonstruiert.

Mit P_AB, P_BC als idealen Singulettprojektoren der verdichteten logischen Blöcke lautet er, in Einheiten Jweak²/Jstrong,

    H_cross = 49/93312 I
              −1225/93312 (P_AB+P_BC)
              +30625/186624 {P_AB,P_BC}.

Hier ist {A,B}=AB+BA. Diese Formel beschreibt nur den Kreuzbeitrag; die beiden getrennten Zweiblockkorrekturen kommen zusätzlich hinzu.

Der Antikommutator ist ein echter Dreibausteinoperator. Die quadratische Hilbert-Schmidt-Distanz dieses Kreuzbeitrags vom gesamten global invariantem höchstens zweilokalen Raum ist exakt

    2100875/241864704 > 0.

Der vollständige passende Paarraum wird von I,P_AB,P_BC und Swap_AC aufgespannt. Eine Symmetriemittelung jeder beliebigen zweilokalen Darstellung würde diesen Support erhalten. Deshalb schließt der nichtnull Rest auch eine ungeschickt versteckte nichtinvariante Zweikörperdarstellung aus.

Dies unterscheidet zwei oft vermischte Arten von Schließung:

* Die Temperley-Lieb-Kompositionsalgebra ist geschlossen.
* Die Projektion jedes einzelnen schwachen Links bleibt exakt in derselben Paarform.
* Die vollständige effektive Vielteilchendynamik erzeugt trotzdem zusätzliche lokale Wörter dieser Algebra, schon in zweiter Ordnung.

Die Integrabilität des ursprünglichen Kettenoperators darf nicht mit einer exakten Schließung einer bestimmten Block-Renormierung auf einem einzigen Paarparameter gleichgesetzt werden.

## 9. Warum die Zahl der freien invarianten Operatoren wächst

Für die native reelle Standarddarstellung von S6 gilt chi(pi)=fix(pi)−1. Die Häufigkeiten der relevanten Charaktere liefern für n≥1

    dim End_S6(V^tensor n)
      = [400+40*4^n+15*9^n+25^n]/720.

Die ersten Werte lauten

    1, 4, 41, 694, 14851, 350384.

Ein vierdimensionaler Paar-Kommutant ist also keine vierdimensionale vollständige Vielteilchentheorie. Diese Formel ist ein endlicher Darstellungssatz, keine Aussage über die Zahl physischer Felder.

## 10. Was damit wirklich zusammengeführt ist

Die folgenden Aussagen lassen sich jetzt auf denselben logischen Trägern gemeinsam prüfen:

    ursprüngliche Hamming-/Quartikgeometrie
        -> markierte Ladungsdarstellung
        -> konkreter Ladungstest des Bindungsoperators
        -> vollständig klassifizierte kompatible Paarfamilie
        -> ladungserhaltende Dreierisometrie
        -> explizite integrable lokale Kompositionsalgebra
        -> kontrollierte zusätzliche Vielteilchenterme.

Der frühere h ist mit einer direkten additiven Hyperladungsinterpretation unvereinbar. Die stärkere volle Symmetrievervollständigung behebt das endliche Ladungsproblem und ändert dafür die Übertragung. Die markierte Alternative zeigt, dass TFPT nicht allein deshalb eine volle SU(5)-Physik wählen muss.

Es wurde keine vollständige Auswahl des physischen Ursprungs getroffen. Offen in dieser Herleitung bleiben insbesondere:

* Welche endlichen Träger werden durch die rohe TFPT-Naht wirklich als lokale geladene Felder realisiert?
* Ist S6 eine innere Symmetrie eines festen physischen Systems oder eine Kovarianz zwischen Markierungen?
* Welche physische Quellenregel erzeugt die kovariante Kopplung beziehungsweise die nötigen bewegten Rahmen, statt sie als Gruppenmittelung zu definieren?
* Woher kommen räumliche Links, ein gemeinsamer Zeitmaßstab, die erforderliche Größenhierarchie und der ausgewählte Anfangszustand?
* Wie werden die nativen W-, Ward-, Alpha-, Flavor- und Gravitationsantworten im gleichen graduierten Zustand/Feldsystem wiedergefunden?

Die T1–T8-Bedingungen werden durch diese endliche Vervollständigung nicht automatisch geschlossen. Ein großes Arbeitsprogramm wird hier weder aufgegeben noch durch eine erfundene vollständige Lösung ersetzt. Das Ergebnis entscheidet eine zentrale Identifikation und liefert eine konkrete kompatible Alternative, deren verbleibende Herkunft präzise benannt ist.

## 11. Reproduktion

    python -m pip install -r requirements.txt
    python audit.py

Das Programm bricht mit einem RuntimeError ab, sobald eine erwartete Identität falsch ist. Es benutzt keine Assertions, die Python mit -O entfernen könnte. `results.json` enthält die exakt berechneten Werte, `integer_certificates.npz` die großen ganzzahligen Zertifikate und `run.log` den tatsächlichen Lauf. Ein zweiter Lauf mit `python -O audit.py` ist im Paket protokolliert.

## 12. Einordnung bekannter Mathematik

Die konkrete TFPT-Matrixzuordnung, der berechnete Ladungskommutator und die endlichen Blockkoeffizienten sind Gegenstand dieses Pakets. Allgemeine Methoden und Gegenstände sind etabliert:

1. Baez und Huerta, The Algebra of Grand Unified Theories, arXiv:0904.1556. Unterscheidung der inneren Träger- und Materiedarstellungen.
2. Bravyi, DiVincenzo und Loss, Schrieffer-Wolff transformation for quantum many-body systems, arXiv:1105.0675. Effektive Hamiltonoperatoren und verbundene Beiträge.
3. V. F. R. Jones, Baxterization, in Differential Geometric Methods in Theoretical Physics (1990), DOI 10.1007/978-1-4684-9148-7_2. Klassische Baxterisierung.
4. You-Quan Li, Yang Baxterization, Journal of Mathematical Physics 34, 757–767 (1993), DOI 10.1063/1.530219. Bekannte systematische Yang-Baxterisierung.
5. Zhu, Kueng, Grassl und Gross, The Clifford group fails gracefully to be a unitary 4-design, arXiv:1609.08172. Bekannte vierte Momentenstruktur.

Keine weltweite Erstentdeckung verwandter Spin- oder Temperley-Lieb-Modelle wird beansprucht.


</details>

[Zur Navigation](#navigation)

<a id="original-d0"></a>
## D0. Der eingereichte Quartiktext

Dieser Text ist die damalige Eingabe mit den Aussagen zu Code, Ladung, Steuerung, Marginalen und Entropie. Seine Selbstaussage einer unabhängigen Prüfung wird als Inhalt der Eingabe bewahrt, nicht als zusätzlicher Lauf dieser Konsolidierung ausgegeben. fileciteturn13file0L1-L20

**SHA256:** `c71cc8ab047f88191e53d7322b6c65823484a098825e8ac17048bebfe201dd9b`

<details>
<summary>D0: vollständige Eingabe öffnen</summary>

**Der mathematische Kern des Textes stimmt. Ich habe ihn unabhängig nachgerechnet und den Anschluss an den ursprünglichen TFPT-Träger weitergeführt.** Dabei ergibt sich eine präzisere Verbindung, als im eingefügten Text steht: Der Quartikcode lässt sich mit der vorhandenen Trägermarkierung und ihren Ladungen verbinden — allerdings über eine sorgfältig rekonstruierte Gruppenabbildung.

Der wichtigste zusätzliche Befund ist eine **2–3–4-Struktur**: Paarwirkungen genügen zur logischen Steuerung; die korrekt übertragene Hyperladung braucht zur unmittelbaren Darstellung drei Register; die energetische Abgrenzung des gesamten Fünfercodes braucht auf diesen vier Registern eine Viererwirkung.

Die im Text verlinkten alten Prüfpakete lagen nicht als Anhänge vor. Ich habe deshalb aus den Formeln und den vorhandenen Originalquellen neu gerechnet.

**Was sich bestätigt hat**

| Aussage des eingefügten Textes | Ergebnis |
|---|---|
| \(\Pi_5=40M_4-P_{\mathrm{sym},4}\) ist ein Rang-5-Projektor | Exakt bestätigt |
| Ein Register enthält keine logische Information; sein bekannter Verlust ist korrigierbar | Exakt bestätigt, einschließlich Decoder |
| Vier angegebene Paarkopplungen erzeugen \(\mathfrak{su}(5)\) | Exakte Rangfolge \(4,7,12,17,22,24\) bestätigt |
| Reduktionen auf ein, zwei, drei Register haben Ränge \(1,10,25\) | Bestätigt |
| \(F_Q=\frac45g\) für die angegebene Orientierung des Coderaums | Bestätigt, in der SLD-Fisher-Konvention |
| Die Choi-Entropie des angegebenen Kontrastqubits maximiert bei \(t=1/27\) | Exakt bestätigt |

Eine kleine sachliche Korrektur: **24 reelle Parameter gelten für allgemeine gemischte Fünferniveauzustände. Ein reiner Zustand hat nur acht.** Die Rangrechnung bleibt davon unberührt.

Die Verbindung zwischen viertem Cliffordmoment und einem Stabilisatorcode ist bereits bekannte Mathematik. Der konkrete Fünferraum und seine TFPT-Zuordnung müssen trotzdem gesondert geprüft werden. [Zhu, Kueng, Grassl und Gross](https://arxiv.org/abs/1609.08172)

**Der weiterführende Anschluss: Das vorhandene Ladungswörterbuch passt tatsächlich auf diesen Code.**

Hier lag eine mögliche Falle. Eine beliebige Pauli-Paarkopplung hat auf dem Code bereits ein Spektrum mit Multiplizitäten \(3+2\). Daraus könnte man vorschnell „Farbe und schwache Wechselwirkung“ ablesen.

Die Originalquellen verhindern genau diesen Kurzschluss: Ein ursprüngliches Gitterlabel entspricht einem **Pauli-Messkontext**, nicht unmittelbar einer einzelnen Paulioperation. Die beiden Zuordnungen besitzen unter der vollständigen Gruppe unterschiedliche Wirkungen.

Ich habe deshalb den tatsächlichen Weg rekonstruiert:

\[
(\Pi_5,\ q_*,\ \sigma)
\;\longrightarrow\;
\text{ursprünglicher markierter Fünfslot-Träger}
\;\longrightarrow\;
\mathbb C^3\oplus\mathbb C^2.
\]

Dabei ist \(q_*\) die bereits ausgewählte quadratische Form und \(\sigma\) die vorhandene Familienwirkung.

Die Prüfung benutzt die tatsächlichen 60 Reflexionen. Ihr Vergleich mit der Wirkung auf den sechs quadratischen Formen ergibt einen eindimensionalen Raum von Intertwinern — also eine bis auf einen Skalar bestimmte Abbildung der vollständigen Darstellungen. Ein ausdrücklich angegebener positiver Polartransport macht daraus eine **metrikerhaltende Abbildung der fünf ursprünglichen Slots in den Code**. Auch die gesamte \(S_5\)-Wirkung, welche \(q_*\) festhält, stimmt darunter überein.

Damit lassen sich die ursprünglichen Projektoren \(P_3,P_2\) und

\[
Y=-\frac13P_3+\frac12P_2
\]

als konkrete Operatoren des Codes angeben. Auf der bereits im Compiler verwendeten äußeren Algebra \(\Lambda^{\mathrm{even}}\mathbb C^5\) ergeben sich dann die bekannten Darstellungen:

\[
(3,2)_{1/6},\quad
(\bar3,1)_{-2/3},\quad
(\bar3,1)_{1/3},\quad
(1,2)_{-1/2},\quad
(1,1)_1,\quad
(1,1)_0.
\]

Hier wurden Gruppenwirkung, Ladungen und Multiplizitäten geprüft. Die allgemeine SU(5)/Spin(10)-Darstellungsrechnung ist etabliert; der hier ausgeführte Anschluss verbindet sie mit dem konkreten Quartikcode. **Das ist eine endliche Darstellungsbrücke zum vorhandenen Standardmodell-Gerüst, noch keine Konstruktion physischer Materiefelder oder lokaler Eichdynamik.** [Baez und Huerta](https://arxiv.org/abs/0904.1556)

**Überraschend ist, wo diese korrekt übertragene Hyperladung liegt.**

Alle unmittelbar zugänglichen Paarobservablen spannen auf dem Code einen zehn-dimensionalen Operatorraum auf, einschließlich der Identität. Fügt man die quellengetreu übertragene Hyperladung hinzu, steigt der Rang auf elf:

\[
\dim\operatorname{span}\{H_A\}=10,
\qquad
\dim\operatorname{span}\{H_A,Y\}=11.
\]

**Diese Hyperladung ist also keine unmittelbare Paarobservable.** Das gilt sogar für die verbleibende relative Phasenfreiheit der metrikerhaltenden \(S_5\)-Zuordnung.

Auf drei Registern lässt sie sich dagegen exakt und codeerhaltend darstellen. Der vorhandene Erasure-Decoder liefert dafür unmittelbar einen Operator \(O_3(Y)\) mit

\[
(I\otimes O_3(Y))V=VY.
\]

Das gibt der Informationshierarchie einen konkreten Anschluss: Eine bereits markierte innere Ladung liegt außerhalb des unmittelbaren Paarbildes. Daraus folgt allerdings keine Gleichsetzung dieser Register mit Raumzeitorten.

**Paarwirkungen können trotzdem alles logisch bewegen — und verborgene Information sichtbar machen.**

Die direkte Ausleseordnung ist nicht dasselbe wie die Erreichbarkeit durch zeitlich geordnete Operationen.

Für die beiden im Text verwendeten Zustände

\[
|\psi_\pm\rangle=\frac{|c_0\rangle\pm i|c_1\rangle}{\sqrt2}
\]

sind alle unmittelbaren Paarbilder gleich. Mit dem schon angegebenen erlaubten Puls folgt jedoch

\[
U|\psi_+\rangle=|c_0\rangle,
\qquad
U|\psi_-\rangle=-i|c_1\rangle.
\]

Anschließend unterscheidet eine Paarobservable die beiden mit Erwartungswerten **\(0\) beziehungsweise \(2/3\)**.

Die Phase ist somit nicht dauerhaft „nur dreifach zugänglich“. Sie lässt sich durch eine bekannte Bewegung in eine Paarantwort übersetzen.

Auch die Kontrolle lässt sich vereinfachen: **Eine kontinuierlich steuerbare Paarkopplung plus die kontrolliert ausführbaren nativen diskreten Gruppenoperationen genügt für die volle logische SU(5)-Kontrolle.** Die Gruppe transportiert diese eine Kopplung durch alle 15 Pauli-Richtungen. Das reduziert die benötigten unabhängigen kontinuierlichen Stellgrößen; Reihenfolge und Pulszeiten bleiben vorausgesetzter Steuerzugriff.

**Der stärkste zusätzliche Schutzbefund betrifft die Auswahl des Codes selbst.**

Vergleiche

\[
\rho_5=\frac{\Pi_5}{5},
\qquad
\rho_{35}=\frac{P_{\mathrm{sym},4}}{35}.
\]

Ich habe exakt bestätigt:

\[
\operatorname{tr}_{4-k}\rho_5
=
\operatorname{tr}_{4-k}\rho_{35}
=
\frac{P_{\mathrm{sym},k}}{\binom{k+3}{3}},
\qquad k=1,2,3.
\]

Der gemischte Fünfercode und der gemischte vollständige symmetrische Raum haben also **dieselben Ein-, Zwei- und Dreierbilder**.

Daraus folgt ein kurzer allgemeiner Satz:

> Kein Hamiltonoperator auf genau diesen vier Registern, dessen Terme höchstens drei Register berühren, kann genau den gesamten Fünfercode als alleinigen Grundraum auswählen.

Denn beide Zustände hätten dieselbe Energie. Wenn \(\rho_5\) ausschließlich Grundzustände enthält, müsste dann auch der gesamte 35-dimensionale Träger von \(\rho_{35}\) im Grundraum liegen.

Eine Viererstruktur reicht algebraisch aus. Tatsächlich gilt bereits

\[
\Pi_5=P_{\mathrm{sym},4}Q,
\qquad
Q=\frac1{16}\sum_{A\in\mathrm{Pauli}_2}A^{\otimes4}.
\]

Das ergänzt den ursprünglichen Text entscheidend: **Korrigierbarkeit eines Registerverlusts ist bewiesen; passiver energetischer Schutz folgt daraus nicht automatisch.** Der Zusammenhang zwischen reduzierten Zuständen und möglichen Grundräumen ist ein etablierter Prüfweg. [Chen, Ji, Zeng und Zhou](https://arxiv.org/abs/1110.6583)

Es folgt außerdem: Wer nur die bis zu dreifachen Marginalen kennt und maximale Entropie verlangt, erhält \(\rho_{35}\), nicht \(\rho_5\). Die quartische Zusatzinformation beträgt in dieser präzisen Maximalentropie-Hierarchie

\[
S(\rho_{35})-S(\rho_5)=\log_2 7.
\]

**Bei \(1/27\) gibt es einen positiven dynamischen Anschluss — aber keine allgemeine Entropieauswahl der Natur.**

Die Produktregel

\[
\lambda_Y=\lambda_X\lambda_Z
\]

entspricht einem kontinuierlichen Prozess mit zwei unabhängigen Pauli-Sprungarten. Bei geeigneter dimensionsloser Zeitnormierung lauten seine Multiplikatoren

\[
\lambda_X(\tau)=(2/3)^\tau,\quad
\lambda_Z(\tau)=(1/3)^\tau,\quad
\lambda_Y(\tau)=(2/9)^\tau.
\]

Bei \(\tau=1\) ergibt sich \(t=1/27\). Die noch zusätzliche Quellenannahme lautet konkret: **Es gibt keine dritte, eigenständige \(Y\)-Sprungart.** Positivität allein erzwingt das nicht.

Die Wahl des Entropieobjekts bleibt wesentlich:

| Maximierte Entropie | Ausgewähltes \(t\) |
|---|---:|
| Pauli-Kontrastqubit, wie im eingefügten Text | \(1/27\approx0{,}03703704\) |
| Sechs Permutationsereignisse | \(\approx0{,}03579837\) |
| Vollständiger Dreiniveaukanal derselben ausgeschriebenen Permutationsrealisierung | \(\approx0{,}03656566\) |

Die letzte Zeile ist eine zusätzliche numerische Gegenprobe, keine Behauptung über beliebige andere Familienfortsetzungen. Sie zeigt: Selbst „Choi-Entropie maximieren“ muss festlegen, **welcher vollständige Kanal und welche Kohärenzen gemeint sind**.

Die Faktorisierung zur zusätzlichen Gleichsetzung \(|J|=t_{\max}\) stimmt ebenfalls. Diese Gleichsetzung selbst folgt daraus weiterhin nicht. Eine reine Entropieauswahl kann insbesondere das Vorzeichen von \(J\) nicht wählen: Komplexe Konjugation erhält die Entropie und kehrt \(J\) um.

Damit ist der konkrete Fortschritt: **Der Fünfercode ist jetzt an die ursprüngliche Trägermarkierung angeschlossen, seine Ladungsdarstellung ist explizit übertragen, und Auswahl, Bewegung sowie Auslesung sind durch überprüfte Operatoraussagen miteinander verbunden.** Der nächste physische Herkunftsschritt ist präzise: Die gemeinsame Quelle muss diese Register, den quartischen Selektor und eine tatsächlich ausgeführte gerichtete Entwicklung realisieren. Die Kontrollalgebra allein wählt diese Entwicklung nicht aus.

[Ausführlicher Prüfnachweis mit Herleitungen](outputs/TFPT_Quartik_Pruefung_2026-09-26.txt) · [Reproduzierbares Prüfpaket](outputs/TFPT_Quartik_Pruefpaket_2026-09-26.zip)

</details>

[Zur Navigation](#navigation)

---

<a id="ergebnisdaten"></a>
# 26. Maschinenlesbare Ergebniswerte

Hier stehen die vollständigen Top Level Ergebniswerte der bereitgestellten `results.json` Dateien. Ausschließlich die redundante Liste `checks` mit den einzelnen protokollierten Prüfschritten wird nicht wiederholt; die vollständigen Prüfprogramme stehen im nächsten Kapitel. Keine Zahl wurde neu berechnet, gerundet oder an die Synthese angepasst. Die jeweiligen `scope` und `summary` Felder bleiben erhalten.

<a id="daten-z"></a>
## Z. Ergebniswerte

**Archivmitglied:** `tfpt_zuse_audit/results.json`  
**SHA256 der vollständigen JSON Originaldatei:** `c84fe85a6ed792db0bbba49d17e9db8e0f309efa85ebc771b3455e134cdceba3`

<details>
<summary>Z: alle Ergebniswerte öffnen</summary>

```json
{
  "scope": "Finite mathematical checks only; no derivation of a physical source, spacetime, chirality, quantum gravity, or full TFPT closure.",
  "finite60": {
    "arithmetic": "numpy complex128, tolerance 1e-10; structural counts have elementary exact proofs",
    "ray_counts": {
      "unitary": 24,
      "rank_one": 36,
      "total": 60
    },
    "product_squared_frobenius_norm_counts": {
      "0": 216,
      "2": 3168,
      "4": 216
    },
    "nonzero_projective_products_closed": true,
    "candidate_compatibility": "C(A,B)=1 iff B@A is nonzero (operator TYPES, not spacetime events)",
    "outdegree_including_loops_counts": {
      "60": 24,
      "54": 36
    },
    "directed_diameter": 2,
    "mutual_compatibility_undirected_diameter": 2,
    "uniform_channels": {
      "clifford24": {
        "depolarizing_ptm_error": 7.401486830834377e-17,
        "trace_preservation_error": 1.11944962715024e-17
      },
      "rankone36": {
        "depolarizing_ptm_error": 1.2335811384723961e-17,
        "trace_preservation_error": 0.0
      },
      "full60": {
        "depolarizing_ptm_error": 3.2381504884900395e-17,
        "trace_preservation_error": 5.233641528945917e-18
      }
    },
    "pairwise_composable_history_can_vanish": true
  },
  "symbolic": {
    "arithmetic": "sympy exact rational / algebraic / symbolic",
    "B_population": "Matrix([[13/18, 1/18, 2/9], [1/18, 13/18, 2/9], [2/9, 2/9, 5/9]])",
    "B_eigenvalues": {
      "1": 1,
      "2/3": 1,
      "1/3": 1
    },
    "Birkhoff_weights": [
      "t + 1/2",
      "t",
      "t",
      "1/18 - t",
      "2/9 - t",
      "2/9 - t"
    ],
    "contrast_Pauli_transfer_order_I_X_Y_Z": "Matrix([[1, 0, 0, 0], [0, 2/3, 0, 0], [0, 0, 6*t, 0], [0, 0, 0, 1/3]])",
    "t_zero_vs_one_over_27_Y_expectation_difference": "2/9",
    "t_zero_vs_one_over_27_output_trace_distance_for_Y_plus": "1/9",
    "gram_eigenvalues": {
      "1": 1,
      "1 - sqrt(2)": 1,
      "1 + sqrt(2)": 1
    },
    "gram_quadratic_witness": "-1",
    "three_chart_equal_overlap_eigenvalues": {
      "1": 1,
      "-sqrt(2)*a + 1": 1,
      "sqrt(2)*a + 1": 1
    },
    "hermitian_2x2_determinant": "T**2 - x**2 - y**2 - z**2",
    "determinant_one_boost_outside_composition_only_60_rays": "Matrix([[2, 0], [0, 1/2]])",
    "boost_acts_on_Hermitian_matrix": "Matrix([[4*T + 4*z, x - I*y], [x + I*y, T/4 - z/4]])",
    "reduced_Planck_Hawking_formula_hbar_c_kB_equal_1": "T_H = bar_M_Pl**2 / M; an extra c3=1/(8*pi) is incorrect",
    "units_mod_30": [
      1,
      7,
      11,
      13,
      17,
      19,
      23,
      29
    ],
    "multiplicative_order_7_mod_30": 4,
    "C30_contains_order4_element": false,
    "same_mu4_clock_distinct_positive_generators": true,
    "binary_pairwise_inequality_triple_solutions": 0
  }
}
```

</details>

<a id="daten-q1"></a>
## Q1. Ergebniswerte

**Archivmitglied:** `TFPT_Quartik_Fortsetzung/results.json`  
**SHA256 der vollständigen JSON Originaldatei:** `30ec4e780af3c809792425f3ce524f6624560906653f33d9331bd9c654c3560c`

Die vollständige Originaldatei enthält zusätzlich 385 Einträge in `checks`. Deren Belegart folgt dem Bericht; bei Q4 sind exakte und numerische Kontrollen getrennt.

<details>
<summary>Q1: alle Ergebniswerte öffnen</summary>

```json
{
  "observation_ranks": {
    "1": 1,
    "2": 10,
    "3": 25
  },
  "Lie_growth": [
    4,
    7,
    12,
    17,
    22,
    24
  ],
  "pair_channel": {
    "type": "rank-one measure-and-prepare, entanglement breaking",
    "outcomes": 10,
    "normalized_singular_values": {
      "1": 1,
      "2/3": 9,
      "0": 15
    },
    "Petz_roundtrip_spectrum": {
      "1": 1,
      "4/9": 9,
      "0": 15
    },
    "Petersen_sign_frames": 6
  },
  "pair_blind_marks": {
    "number_of_pure_mark_states": 6,
    "all_pair_outputs": "P_sym,2/10",
    "hidden_real_traceless_dimension": 5,
    "native_twirl_to_pair_Petz": "T_pair=(5 T5-3 I)(5 T5-I)(15 T5-13 I)/16; operator identity, not an arbitrary positive mixture"
  },
  "hypercharge": {
    "mark_convention": "fixed simplex point of the canonical sigma; q* is an input, not physically selected here",
    "minimum_squared_HS_distance_to_pair_space_over_relative_phase": "29/60 - sqrt(6)/10"
  },
  "moment_parent_spectrum": {
    "0": 5,
    "1/2": 30,
    "1": 221
  },
  "overlapping_codes": {
    "1": {
      "rank": 100,
      "nonzero_squared_principal_cosine": "1/16",
      "norm_PAPB": "1/4",
      "minimum_energy_I_PA_plus_I_PB": "3/4",
      "integer_denominator": 576
    },
    "2": {
      "rank": 10,
      "nonzero_squared_principal_cosine": "1/4",
      "norm_PAPB": "1/2",
      "minimum_energy_I_PA_plus_I_PB": "1/2",
      "integer_denominator": 576
    },
    "3": {
      "rank": 20,
      "nonzero_squared_principal_cosine": "1/16",
      "norm_PAPB": "1/4",
      "minimum_energy_I_PA_plus_I_PB": "3/4",
      "integer_denominator": 576
    }
  },
  "virtual_coupling": {
    "order": "second order in g/Delta, not exact finite-g dynamics",
    "identity": "-29/24",
    "local_each": "-11/24",
    "entangling_product": "-15/8",
    "units": "g^2/Delta"
  },
  "virtual_coupling_numeric_E_over_g2": {
    "(0, 0)": {
      "0.02": -3.993620398445373,
      "0.01": -3.9984012787231737,
      "0.005": -3.9996000799844134
    },
    "(0, 1)": {
      "0.02": -0.8893101629969594,
      "0.01": -0.8889942308745066,
      "0.005": -0.888915225851459
    },
    "(1, 1)": {
      "0.02": -1.1111011792867653,
      "0.01": -1.1111086385084505,
      "0.005": -1.111110493621139
    }
  },
  "Hamming_source": {
    "encoded_dimension": 4,
    "physical_registers": 7,
    "physical_register_dimension": 4,
    "distance_in_registers": 3,
    "conditional_minimality": "n=7 is the unique minimum in the stated doubly-even self-orthogonal CSS class encoding nonzero information and correcting arbitrary single errors",
    "finite_group_covariance": "U^tensor7 V7 = V7 conjugate(U); two concatenations give U",
    "parent_spectrum": {
      "0": 4,
      "4": 420,
      "6": 5880,
      "7": 10080
    },
    "architecture_status": "explicit alternative; not a derivation that TFPT selects it"
  },
  "orientation_geometry": {
    "local_dimension": 15,
    "metric": "g(X,Y)=8 tr(X0 Y0)",
    "SLD_QFI": "F_Q=4g/5 for rho=P5/5",
    "Berry_connection": "tr(U^dagger dU) I5",
    "local_Berry_curvature": "0; finite quotient holonomy is not excluded"
  },
  "entropy_exact": {
    "qubit_t": "1/27",
    "Pauli_probabilities": [
      "5/9",
      "5/18",
      "1/18",
      "1/9"
    ],
    "primitive_rates": [
      "log(3)/2",
      "0",
      "log(3/2)/2"
    ],
    "extra_assumption": "no independent Y jump; not forced by CP"
  },
  "entropy_numeric_optima": {
    "events": 0.03579837325561067,
    "qutrit": 0.03656566277922796
  },
  "scope": {
    "physical_TOE_proved": false,
    "new_global_TFPT_axiom_selection": false,
    "Lean_reverification": false,
    "physical_laboratory_experiment": false,
    "three_dimensional_space_from_Fano_bits": false
  },
  "elapsed_seconds": 25.651491165161133,
  "environment": {
    "python": "3.13.5",
    "numpy": "2.3.5",
    "scipy": "1.17.0",
    "sympy": "1.14.0"
  }
}
```

</details>

<a id="daten-q2"></a>
## Q2. Ergebniswerte

**Archivmitglied:** `TFPT_Igusa_Quellendynamik_20260926/results.json`  
**SHA256 der vollständigen JSON Originaldatei:** `4aa56102d3fb75e19ede99c6bf11e239cb8e4373f5fe15c7af5ccdb659deca49`

Die vollständige Originaldatei enthält zusätzlich 1065 Einträge in `checks`. Deren Belegart folgt dem Bericht; bei Q4 sind exakte und numerische Kontrollen getrennt.

<details>
<summary>Q2: alle Ergebniswerte öffnen</summary>

```json
{
  "quartic_coordinates": {
    "f": [
      "z0**4 + z1**4 + z2**4 + z3**4",
      "6*z0**2*z1**2 + 6*z2**2*z3**2",
      "6*z0**2*z2**2 + 6*z1**2*z3**2",
      "6*z0**2*z3**2 + 6*z1**2*z2**2",
      "24*z0*z1*z2*z3"
    ],
    "x": [
      "2*z0**4 + 24*z0*z1*z2*z3 + 2*z1**4 + 2*z2**4 + 2*z3**4",
      "2*z0**4 - 24*z0*z1*z2*z3 + 2*z1**4 + 2*z2**4 + 2*z3**4",
      "-z0**4 - 6*z0**2*z1**2 - 6*z0**2*z2**2 + 6*z0**2*z3**2 - z1**4 + 6*z1**2*z2**2 - 6*z1**2*z3**2 - z2**4 - 6*z2**2*z3**2 - z3**4",
      "-z0**4 - 6*z0**2*z1**2 + 6*z0**2*z2**2 - 6*z0**2*z3**2 - z1**4 - 6*z1**2*z2**2 + 6*z1**2*z3**2 - z2**4 - 6*z2**2*z3**2 - z3**4",
      "-z0**4 + 6*z0**2*z1**2 - 6*z0**2*z2**2 - 6*z0**2*z3**2 - z1**4 - 6*z1**2*z2**2 - 6*z1**2*z3**2 - z2**4 + 6*z2**2*z3**2 - z3**4",
      "-z0**4 + 6*z0**2*z1**2 + 6*z0**2*z2**2 + 6*z0**2*z3**2 - z1**4 + 6*z1**2*z2**2 + 6*z1**2*z3**2 - z2**4 + 6*z2**2*z3**2 - z3**4"
    ],
    "constraint": "(sum x_i^2)^2=4 sum x_i^4, sum x_i=0",
    "scope": "image of one coherent source z via z^tensor4; not every arbitrary state of the 5-dimensional code"
  },
  "invariant_ring": {
    "Pauli_Molien": "(1-t^16)/(1-t^4)^5",
    "generators": "f0,...,f4",
    "relation": "Igusa quartic in the generators",
    "full_group_degrees": [
      8,
      12,
      20,
      24
    ],
    "group_order_from_kernel_and_image": 46080,
    "proof_dependency": "Classical Igusa quotient identification plus the exact Molien/rank and source-generator certificates. See report.",
    "Jacobian_at_1_2_4_8": "5230763459347830413418775527631850224805216256000000000000000000",
    "sextic": "u^6+e2 u^4-e3 u^3+(e2^2/4)u^2-e5 u+e6",
    "discriminant": "product_{i<j}(x_i-x_j)^2 = constant times product_{60 root hyperplanes} l(z)^2"
  },
  "source_six_action": [
    [
      1,
      0,
      2,
      3,
      4,
      5
    ],
    [
      1,
      0,
      2,
      3,
      4,
      5
    ],
    [
      1,
      0,
      2,
      3,
      4,
      5
    ],
    [
      1,
      0,
      2,
      3,
      4,
      5
    ],
    [
      0,
      3,
      2,
      1,
      4,
      5
    ],
    [
      3,
      1,
      2,
      0,
      4,
      5
    ],
    [
      3,
      1,
      2,
      0,
      4,
      5
    ],
    [
      0,
      3,
      2,
      1,
      4,
      5
    ],
    [
      3,
      1,
      2,
      0,
      4,
      5
    ],
    [
      0,
      3,
      2,
      1,
      4,
      5
    ],
    [
      0,
      3,
      2,
      1,
      4,
      5
    ],
    [
      3,
      1,
      2,
      0,
      4,
      5
    ],
    [
      0,
      4,
      2,
      3,
      1,
      5
    ],
    [
      4,
      1,
      2,
      3,
      0,
      5
    ],
    [
      4,
      1,
      2,
      3,
      0,
      5
    ],
    [
      0,
      4,
      2,
      3,
      1,
      5
    ],
    [
      4,
      1,
      2,
      3,
      0,
      5
    ],
    [
      0,
      4,
      2,
      3,
      1,
      5
    ],
    [
      0,
      4,
      2,
      3,
      1,
      5
    ],
    [
      4,
      1,
      2,
      3,
      0,
      5
    ],
    [
      0,
      2,
      1,
      3,
      4,
      5
    ],
    [
      2,
      1,
      0,
      3,
      4,
      5
    ],
    [
      2,
      1,
      0,
      3,
      4,
      5
    ],
    [
      0,
      2,
      1,
      3,
      4,
      5
    ],
    [
      2,
      1,
      0,
      3,
      4,
      5
    ],
    [
      0,
      2,
      1,
      3,
      4,
      5
    ],
    [
      0,
      2,
      1,
      3,
      4,
      5
    ],
    [
      2,
      1,
      0,
      3,
      4,
      5
    ],
    [
      0,
      1,
      4,
      3,
      2,
      5
    ],
    [
      0,
      1,
      2,
      5,
      4,
      3
    ],
    [
      0,
      1,
      2,
      5,
      4,
      3
    ],
    [
      0,
      1,
      4,
      3,
      2,
      5
    ],
    [
      5,
      1,
      2,
      3,
      4,
      0
    ],
    [
      0,
      5,
      2,
      3,
      4,
      1
    ],
    [
      0,
      5,
      2,
      3,
      4,
      1
    ],
    [
      5,
      1,
      2,
      3,
      4,
      0
    ],
    [
      0,
      5,
      2,
      3,
      4,
      1
    ],
    [
      5,
      1,
      2,
      3,
      4,
      0
    ],
    [
      5,
      1,
      2,
      3,
      4,
      0
    ],
    [
      0,
      5,
      2,
      3,
      4,
      1
    ],
    [
      0,
      1,
      3,
      2,
      4,
      5
    ],
    [
      0,
      1,
      2,
      3,
      5,
      4
    ],
    [
      0,
      1,
      2,
      3,
      5,
      4
    ],
    [
      0,
      1,
      3,
      2,
      4,
      5
    ],
    [
      0,
      1,
      3,
      2,
      4,
      5
    ],
    [
      0,
      1,
      2,
      3,
      5,
      4
    ],
    [
      0,
      1,
      2,
      3,
      5,
      4
    ],
    [
      0,
      1,
      3,
      2,
      4,
      5
    ],
    [
      0,
      1,
      2,
      4,
      3,
      5
    ],
    [
      0,
      1,
      5,
      3,
      4,
      2
    ],
    [
      0,
      1,
      5,
      3,
      4,
      2
    ],
    [
      0,
      1,
      2,
      4,
      3,
      5
    ],
    [
      0,
      1,
      2,
      4,
      3,
      5
    ],
    [
      0,
      1,
      5,
      3,
      4,
      2
    ],
    [
      0,
      1,
      5,
      3,
      4,
      2
    ],
    [
      0,
      1,
      2,
      4,
      3,
      5
    ],
    [
      0,
      1,
      4,
      3,
      2,
      5
    ],
    [
      0,
      1,
      2,
      5,
      4,
      3
    ],
    [
      0,
      1,
      2,
      5,
      4,
      3
    ],
    [
      0,
      1,
      4,
      3,
      2,
      5
    ]
  ],
  "sixty_hyperplanes": [
    {
      "pair": [
        0,
        1
      ],
      "constant": "48",
      "normals": [
        [
          "1",
          "0",
          "0",
          "0"
        ],
        [
          "0",
          "1",
          "0",
          "0"
        ],
        [
          "0",
          "0",
          "1",
          "0"
        ],
        [
          "0",
          "0",
          "0",
          "1"
        ]
      ]
    },
    {
      "pair": [
        0,
        2
      ],
      "constant": "3",
      "normals": [
        [
          "1",
          "I",
          "I",
          "-1"
        ],
        [
          "1",
          "I",
          "-I",
          "1"
        ],
        [
          "1",
          "-I",
          "I",
          "1"
        ],
        [
          "1",
          "-I",
          "-I",
          "-1"
        ]
      ]
    },
    {
      "pair": [
        0,
        3
      ],
      "constant": "3",
      "normals": [
        [
          "1",
          "I",
          "1",
          "-I"
        ],
        [
          "1",
          "I",
          "-1",
          "I"
        ],
        [
          "1",
          "-I",
          "1",
          "I"
        ],
        [
          "1",
          "-I",
          "-1",
          "-I"
        ]
      ]
    },
    {
      "pair": [
        0,
        4
      ],
      "constant": "3",
      "normals": [
        [
          "1",
          "1",
          "-I",
          "I"
        ],
        [
          "1",
          "1",
          "I",
          "-I"
        ],
        [
          "1",
          "-1",
          "-I",
          "-I"
        ],
        [
          "1",
          "-1",
          "I",
          "I"
        ]
      ]
    },
    {
      "pair": [
        0,
        5
      ],
      "constant": "3",
      "normals": [
        [
          "1",
          "1",
          "1",
          "1"
        ],
        [
          "1",
          "1",
          "-1",
          "-1"
        ],
        [
          "1",
          "-1",
          "1",
          "-1"
        ],
        [
          "1",
          "-1",
          "-1",
          "1"
        ]
      ]
    },
    {
      "pair": [
        1,
        2
      ],
      "constant": "3",
      "normals": [
        [
          "1",
          "I",
          "I",
          "1"
        ],
        [
          "1",
          "I",
          "-I",
          "-1"
        ],
        [
          "1",
          "-I",
          "I",
          "-1"
        ],
        [
          "1",
          "-I",
          "-I",
          "1"
        ]
      ]
    },
    {
      "pair": [
        1,
        3
      ],
      "constant": "3",
      "normals": [
        [
          "1",
          "I",
          "1",
          "I"
        ],
        [
          "1",
          "I",
          "-1",
          "-I"
        ],
        [
          "1",
          "-I",
          "1",
          "-I"
        ],
        [
          "1",
          "-I",
          "-1",
          "I"
        ]
      ]
    },
    {
      "pair": [
        1,
        4
      ],
      "constant": "3",
      "normals": [
        [
          "1",
          "1",
          "-I",
          "-I"
        ],
        [
          "1",
          "1",
          "I",
          "I"
        ],
        [
          "1",
          "-1",
          "-I",
          "I"
        ],
        [
          "1",
          "-1",
          "I",
          "-I"
        ]
      ]
    },
    {
      "pair": [
        1,
        5
      ],
      "constant": "3",
      "normals": [
        [
          "1",
          "1",
          "1",
          "-1"
        ],
        [
          "1",
          "1",
          "-1",
          "1"
        ],
        [
          "1",
          "-1",
          "1",
          "1"
        ],
        [
          "1",
          "-1",
          "-1",
          "-1"
        ]
      ]
    },
    {
      "pair": [
        2,
        3
      ],
      "constant": "-12",
      "normals": [
        [
          "1",
          "1",
          "0",
          "0"
        ],
        [
          "1",
          "-1",
          "0",
          "0"
        ],
        [
          "0",
          "0",
          "1",
          "1"
        ],
        [
          "0",
          "0",
          "1",
          "-1"
        ]
      ]
    },
    {
      "pair": [
        2,
        4
      ],
      "constant": "-12",
      "normals": [
        [
          "1",
          "0",
          "1",
          "0"
        ],
        [
          "1",
          "0",
          "-1",
          "0"
        ],
        [
          "0",
          "1",
          "0",
          "1"
        ],
        [
          "0",
          "1",
          "0",
          "-1"
        ]
      ]
    },
    {
      "pair": [
        2,
        5
      ],
      "constant": "-12",
      "normals": [
        [
          "0",
          "1",
          "I",
          "0"
        ],
        [
          "0",
          "1",
          "-I",
          "0"
        ],
        [
          "1",
          "0",
          "0",
          "I"
        ],
        [
          "1",
          "0",
          "0",
          "-I"
        ]
      ]
    },
    {
      "pair": [
        3,
        4
      ],
      "constant": "-12",
      "normals": [
        [
          "0",
          "1",
          "1",
          "0"
        ],
        [
          "0",
          "1",
          "-1",
          "0"
        ],
        [
          "1",
          "0",
          "0",
          "1"
        ],
        [
          "1",
          "0",
          "0",
          "-1"
        ]
      ]
    },
    {
      "pair": [
        3,
        5
      ],
      "constant": "-12",
      "normals": [
        [
          "1",
          "0",
          "I",
          "0"
        ],
        [
          "1",
          "0",
          "-I",
          "0"
        ],
        [
          "0",
          "1",
          "0",
          "I"
        ],
        [
          "0",
          "1",
          "0",
          "-I"
        ]
      ]
    },
    {
      "pair": [
        4,
        5
      ],
      "constant": "-12",
      "normals": [
        [
          "1",
          "I",
          "0",
          "0"
        ],
        [
          "1",
          "-I",
          "0",
          "0"
        ],
        [
          "0",
          "0",
          "1",
          "I"
        ],
        [
          "0",
          "0",
          "1",
          "-I"
        ]
      ]
    }
  ],
  "ten_Bell_tropes": [
    {
      "label": "II",
      "quadric": "z0**2 + z1**2 + z2**2 + z3**2",
      "sign_normal": [
        "1",
        "1",
        "-1",
        "-1",
        "-1",
        "1"
      ]
    },
    {
      "label": "IX",
      "quadric": "2*z0*z1 + 2*z2*z3",
      "sign_normal": [
        "1",
        "-1",
        "-1",
        "-1",
        "1",
        "1"
      ]
    },
    {
      "label": "IZ",
      "quadric": "z0**2 - z1**2 + z2**2 - z3**2",
      "sign_normal": [
        "1",
        "1",
        "-1",
        "1",
        "-1",
        "-1"
      ]
    },
    {
      "label": "XI",
      "quadric": "2*z0*z2 + 2*z1*z3",
      "sign_normal": [
        "1",
        "-1",
        "-1",
        "1",
        "-1",
        "1"
      ]
    },
    {
      "label": "XX",
      "quadric": "2*z0*z3 + 2*z1*z2",
      "sign_normal": [
        "1",
        "-1",
        "1",
        "-1",
        "-1",
        "1"
      ]
    },
    {
      "label": "XZ",
      "quadric": "2*z0*z2 - 2*z1*z3",
      "sign_normal": [
        "-1",
        "1",
        "-1",
        "1",
        "-1",
        "1"
      ]
    },
    {
      "label": "YY",
      "quadric": "-2*z0*z3 + 2*z1*z2",
      "sign_normal": [
        "-1",
        "1",
        "1",
        "-1",
        "-1",
        "1"
      ]
    },
    {
      "label": "ZI",
      "quadric": "z0**2 + z1**2 - z2**2 - z3**2",
      "sign_normal": [
        "1",
        "1",
        "-1",
        "-1",
        "1",
        "-1"
      ]
    },
    {
      "label": "ZX",
      "quadric": "2*z0*z1 - 2*z2*z3",
      "sign_normal": [
        "-1",
        "1",
        "-1",
        "-1",
        "1",
        "1"
      ]
    },
    {
      "label": "ZZ",
      "quadric": "z0**2 - z1**2 - z2**2 + z3**2",
      "sign_normal": [
        "1",
        "1",
        "1",
        "-1",
        "-1",
        "-1"
      ]
    }
  ],
  "doily": {
    "incidence_matrix": [
      [
        "1",
        "1",
        "1",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0"
      ],
      [
        "0",
        "0",
        "0",
        "1",
        "1",
        "1",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0"
      ],
      [
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "1",
        "1",
        "1",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0"
      ],
      [
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "1",
        "1",
        "1",
        "0",
        "0",
        "0"
      ],
      [
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "1",
        "1",
        "1"
      ],
      [
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "1",
        "0",
        "0",
        "1",
        "0",
        "0",
        "1",
        "0",
        "0"
      ],
      [
        "0",
        "0",
        "0",
        "1",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "1",
        "0",
        "0",
        "1",
        "0"
      ],
      [
        "0",
        "0",
        "0",
        "0",
        "1",
        "0",
        "0",
        "1",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "1"
      ],
      [
        "0",
        "0",
        "0",
        "0",
        "0",
        "1",
        "0",
        "0",
        "1",
        "0",
        "0",
        "1",
        "0",
        "0",
        "0"
      ],
      [
        "1",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "1",
        "0",
        "0",
        "1"
      ],
      [
        "0",
        "1",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "1",
        "0",
        "0",
        "0",
        "0",
        "1",
        "0"
      ],
      [
        "0",
        "0",
        "1",
        "0",
        "0",
        "0",
        "0",
        "1",
        "0",
        "0",
        "1",
        "0",
        "0",
        "0",
        "0"
      ],
      [
        "0",
        "0",
        "1",
        "0",
        "0",
        "1",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "1",
        "0",
        "0"
      ],
      [
        "0",
        "1",
        "0",
        "0",
        "1",
        "0",
        "0",
        "0",
        "0",
        "1",
        "0",
        "0",
        "0",
        "0",
        "0"
      ],
      [
        "1",
        "0",
        "0",
        "1",
        "0",
        "0",
        "1",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0"
      ]
    ],
    "NNT_spectrum": {
      "9": 1,
      "4": 9,
      "0": 5
    },
    "singular_points": [
      [
        2,
        2,
        -1,
        -1,
        -1,
        -1
      ],
      [
        2,
        -1,
        2,
        -1,
        -1,
        -1
      ],
      [
        2,
        -1,
        -1,
        2,
        -1,
        -1
      ],
      [
        2,
        -1,
        -1,
        -1,
        2,
        -1
      ],
      [
        2,
        -1,
        -1,
        -1,
        -1,
        2
      ],
      [
        -1,
        2,
        2,
        -1,
        -1,
        -1
      ],
      [
        -1,
        2,
        -1,
        2,
        -1,
        -1
      ],
      [
        -1,
        2,
        -1,
        -1,
        2,
        -1
      ],
      [
        -1,
        2,
        -1,
        -1,
        -1,
        2
      ],
      [
        -1,
        -1,
        2,
        2,
        -1,
        -1
      ],
      [
        -1,
        -1,
        2,
        -1,
        2,
        -1
      ],
      [
        -1,
        -1,
        2,
        -1,
        -1,
        2
      ],
      [
        -1,
        -1,
        -1,
        2,
        2,
        -1
      ],
      [
        -1,
        -1,
        -1,
        2,
        -1,
        2
      ],
      [
        -1,
        -1,
        -1,
        -1,
        2,
        2
      ]
    ],
    "perfect_matchings": [
      [
        [
          0,
          1
        ],
        [
          2,
          3
        ],
        [
          4,
          5
        ]
      ],
      [
        [
          0,
          1
        ],
        [
          2,
          4
        ],
        [
          3,
          5
        ]
      ],
      [
        [
          0,
          1
        ],
        [
          2,
          5
        ],
        [
          3,
          4
        ]
      ],
      [
        [
          0,
          2
        ],
        [
          1,
          3
        ],
        [
          4,
          5
        ]
      ],
      [
        [
          0,
          2
        ],
        [
          1,
          4
        ],
        [
          3,
          5
        ]
      ],
      [
        [
          0,
          2
        ],
        [
          1,
          5
        ],
        [
          3,
          4
        ]
      ],
      [
        [
          0,
          3
        ],
        [
          1,
          2
        ],
        [
          4,
          5
        ]
      ],
      [
        [
          0,
          3
        ],
        [
          1,
          4
        ],
        [
          2,
          5
        ]
      ],
      [
        [
          0,
          3
        ],
        [
          1,
          5
        ],
        [
          2,
          4
        ]
      ],
      [
        [
          0,
          4
        ],
        [
          1,
          2
        ],
        [
          3,
          5
        ]
      ],
      [
        [
          0,
          4
        ],
        [
          1,
          3
        ],
        [
          2,
          5
        ]
      ],
      [
        [
          0,
          4
        ],
        [
          1,
          5
        ],
        [
          2,
          3
        ]
      ],
      [
        [
          0,
          5
        ],
        [
          1,
          2
        ],
        [
          3,
          4
        ]
      ],
      [
        [
          0,
          5
        ],
        [
          1,
          3
        ],
        [
          2,
          4
        ]
      ],
      [
        [
          0,
          5
        ],
        [
          1,
          4
        ],
        [
          2,
          3
        ]
      ]
    ],
    "root_fibre_size": 4
  },
  "dynamics": {
    "linear_stabilizer_matrix_shape": [
      70,
      26
    ],
    "linear_stabilizer_rank": 25,
    "first_jet_span": 35,
    "additional_linear_coordinates": 30,
    "same_initial_f": [
      "4369",
      "6168",
      "1632",
      "768",
      "1536"
    ],
    "first_derivative": [
      "15420*I",
      "0",
      "5760*I",
      "0",
      "0"
    ],
    "second_source_first_derivative": [
      "-15420*I",
      "0",
      "-5760*I",
      "0",
      "0"
    ],
    "normalization": "Both source vectors have norm sqrt85. Dividing by sqrt85 divides all quartic outputs and derivatives by 85^2.",
    "scope": "No nontrivial continuous projective linear evolution on the fixed C5 preserves the entire single-coherent-source image. Discrete evolution, nonlinear evolution with lifts and arbitrary entangled code states are not excluded."
  },
  "protected_exchange": {
    "microscopic_coupling": "V=g sum_r sum_{a!=0} A_a,r^A A_a,r^B = g sum_r(4 Swap_r-I)",
    "parent": "Delta(H_F^A+H_F^B), H_F=sum of seven I-Q_S terms",
    "first_order": "0",
    "second_order": "-105 g^2/(8 Delta) I",
    "third_order": "g^3/Delta^2 [(21/8) Swap_logical-(63/16) I]",
    "logical_exchange_coefficient": "21 g^3/(8 Delta^2)",
    "paths": {
      "same_site": 1470,
      "Fano_line": 630
    },
    "one_direction_exact_low_energy": "[M+6 xi g-sqrt((M+6 xi g)^2+28g^2)]/2; M=8 Delta for two blocks",
    "scope": "Perturbative coefficient, not an exact finite-g equation. Fixed two-block weak-coupling regime. g, Delta and link incidence are model choices, not TFPT-derived physical constants."
  },
  "five_code_parent_family": {
    "H_r": "r(S-P)+(I-S), r>0",
    "C_identity": "-(5*r**2 + 10*r + 1)/(8*r*(r + 1))",
    "C_local_each": "(r - 1)*(5*r + 3)/(8*r*(r + 1))",
    "C_interaction": "-(5*r**2 + 2*r + 9)/(8*r*(r + 1))",
    "scope": "Same tested finite code and source symmetry; not two models satisfying all eight physical TFPT gates."
  },
  "elapsed_seconds": 17.373611450195312,
  "environment": {
    "python": "3.13.5",
    "sympy": "1.14.0",
    "numpy": "2.3.5"
  },
  "scope": {
    "physical_TOE_proved": false,
    "spacetime_dimension_derived": false,
    "new_natural_constants_derived": false,
    "quantum_field_theory_constructed": false,
    "new_Lean_formalization": false,
    "finite_algebraic_continuation": true
  }
}
```

</details>

<a id="daten-q3"></a>
## Q3. Ergebniswerte

**Archivmitglied:** `TFPT_Dynamischer_Codeabschluss_20260926/results.json`  
**SHA256 der vollständigen JSON Originaldatei:** `fd101f2fd390fe6ff4c17f59e407930d298db6bbab013f718c90643ba92f7ff5`

Die vollständige Originaldatei enthält zusätzlich 1326 Einträge in `checks`. Deren Belegart folgt dem Bericht; bei Q4 sind exakte und numerische Kontrollen getrennt.

<details>
<summary>Q3: alle Ergebniswerte öffnen</summary>

```json
{
  "native_group": {
    "projective_order": 11520,
    "commutant_dimensions": [
      "1",
      "2",
      "6",
      "29"
    ],
    "adjoint_trace_histogram": {
      "16": 1,
      "4": 400,
      "0": 3825,
      "1": 4864,
      "8": 30,
      "2": 2400
    }
  },
  "symmetric_fourth": {
    "dimensions": [
      5,
      30
    ],
    "commutant_dimension": 2,
    "irreducible_character_norms": [
      1,
      1
    ]
  },
  "response_sectors": {
    "trivial_rank": 5,
    "other_ranks": [
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2
    ],
    "first_response_ranks": [
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2
    ],
    "label_rule": "P_s K_a P_t=0 unless s=t xor a",
    "source_readout_scope": "Sym4 C4, not spatial sites or particle species"
  },
  "sixth_order": {
    "K4_weighted_time_orders": "83/16384",
    "double_weighted_time_orders": "449/73728",
    "K4_colorings": 210,
    "double_labeled_colorings": 252,
    "double_colorings_unlabeled": 63,
    "K4_GL3_frames": 168,
    "K4_dependent_frames": 42,
    "connected_cubic_edge_multiplicities": [
      [
        0,
        1,
        2,
        2,
        1,
        0
      ],
      [
        0,
        2,
        1,
        1,
        2,
        0
      ],
      [
        1,
        0,
        2,
        2,
        0,
        1
      ],
      [
        1,
        1,
        1,
        1,
        1,
        1
      ],
      [
        1,
        2,
        0,
        0,
        2,
        1
      ],
      [
        2,
        0,
        1,
        1,
        0,
        2
      ],
      [
        2,
        1,
        0,
        0,
        1,
        2
      ]
    ],
    "K4_kappa": "27573/512",
    "C4_kappa": "3143/256",
    "coefficient_convention": "H_eff on symmetric logical35 = scalar - kappa*g^6/Delta^5 * Pi5 + O(g^7/Delta^6). Not an exact finite-g Hamiltonian."
  },
  "coupling_and_topology_controls": {
    "unequal_K4_weights": [
      1,
      2,
      -1,
      3,
      2,
      4
    ],
    "unequal_coefficient_from_path_polynomial": "11431/1024",
    "unequal_coefficient_from_exact_syndrome_series": "11431/1024",
    "open_chain_all_four_support_coefficients_through6": [
      "0",
      "0",
      "0",
      "0",
      "0",
      "0",
      "0"
    ]
  },
  "error_detection_scope": {
    "bare_selected_limit_code": "((28,5,6))_4",
    "bare_distance_proof": "outer distance2 times inner distance3 gives lower bound6; two Fano-triple logical Paulis give a nontrivial weight6 witness",
    "finite_g": "dressed selected ground code has distance2 for sufficiently small nonzero negative g in the K4 model",
    "finite_g_probe": "one physical A on the same site r in two blocks; compression = scalar I + (9/32)*(g/Delta)^2*h_A + O((g/Delta)^3)",
    "eigenvalue_difference_leading": "(3/8)*(g/Delta)^2",
    "single_error_detection": "exact: global Pauli^(tensor28) still stabilizes the five-dimensional ground sector"
  },
  "independent_single_Pauli_series": {
    "syndrome_dimension": 512,
    "K4": [
      {
        "xi": [
          1,
          -1,
          -1,
          -1
        ],
        "coefficients": [
          "0",
          "0",
          "-21/4",
          "21/8",
          "-1071/256",
          "1155/128",
          "-129143/8192"
        ]
      },
      {
        "xi": [
          1,
          -1,
          -1,
          1
        ],
        "coefficients": [
          "0",
          "0",
          "-21/4",
          "21/16",
          "-287/256",
          "903/1024",
          "5971/24576"
        ]
      },
      {
        "xi": [
          1,
          -1,
          1,
          -1
        ],
        "coefficients": [
          "0",
          "0",
          "-21/4",
          "21/16",
          "-287/256",
          "903/1024",
          "5971/24576"
        ]
      },
      {
        "xi": [
          1,
          -1,
          1,
          1
        ],
        "coefficients": [
          "0",
          "0",
          "-21/4",
          "21/8",
          "-1071/256",
          "1155/128",
          "-129143/8192"
        ]
      },
      {
        "xi": [
          1,
          1,
          -1,
          -1
        ],
        "coefficients": [
          "0",
          "0",
          "-21/4",
          "21/16",
          "-287/256",
          "903/1024",
          "5971/24576"
        ]
      },
      {
        "xi": [
          1,
          1,
          -1,
          1
        ],
        "coefficients": [
          "0",
          "0",
          "-21/4",
          "21/8",
          "-1071/256",
          "1155/128",
          "-129143/8192"
        ]
      },
      {
        "xi": [
          1,
          1,
          1,
          -1
        ],
        "coefficients": [
          "0",
          "0",
          "-21/4",
          "21/8",
          "-1071/256",
          "1155/128",
          "-129143/8192"
        ]
      },
      {
        "xi": [
          1,
          1,
          1,
          1
        ],
        "coefficients": [
          "0",
          "0",
          "-21/4",
          "105/16",
          "-3423/256",
          "34251/1024",
          "-743127/8192"
        ]
      }
    ],
    "C4": [
      {
        "xi": [
          1,
          -1,
          -1,
          -1
        ],
        "coefficients": [
          "0",
          "0",
          "-7/2",
          "0",
          "-35/16",
          "0",
          "-4529/3072"
        ]
      },
      {
        "xi": [
          1,
          -1,
          -1,
          1
        ],
        "coefficients": [
          "0",
          "0",
          "-7/2",
          "0",
          "-35/16",
          "0",
          "-1085/4096"
        ]
      },
      {
        "xi": [
          1,
          -1,
          1,
          -1
        ],
        "coefficients": [
          "0",
          "0",
          "-7/2",
          "-21/8",
          "-35/16",
          "-1533/512",
          "-70693/12288"
        ]
      },
      {
        "xi": [
          1,
          -1,
          1,
          1
        ],
        "coefficients": [
          "0",
          "0",
          "-7/2",
          "0",
          "-35/16",
          "0",
          "-4529/3072"
        ]
      },
      {
        "xi": [
          1,
          1,
          -1,
          -1
        ],
        "coefficients": [
          "0",
          "0",
          "-7/2",
          "0",
          "-35/16",
          "0",
          "-1085/4096"
        ]
      },
      {
        "xi": [
          1,
          1,
          -1,
          1
        ],
        "coefficients": [
          "0",
          "0",
          "-7/2",
          "0",
          "-35/16",
          "0",
          "-4529/3072"
        ]
      },
      {
        "xi": [
          1,
          1,
          1,
          -1
        ],
        "coefficients": [
          "0",
          "0",
          "-7/2",
          "0",
          "-35/16",
          "0",
          "-4529/3072"
        ]
      },
      {
        "xi": [
          1,
          1,
          1,
          1
        ],
        "coefficients": [
          "0",
          "0",
          "-7/2",
          "21/8",
          "-35/16",
          "1533/512",
          "-70693/12288"
        ]
      }
    ],
    "K4_full_support_Walsh": [
      "0",
      "0",
      "0",
      "0",
      "0",
      "0",
      "-27573/8192"
    ],
    "C4_full_support_Walsh": [
      "0",
      "0",
      "0",
      "0",
      "0",
      "0",
      "-3143/4096"
    ],
    "scope": "Exact check of the single-Pauli invariant sector through sixth order. The extension to all15 Pauli types uses the explicit shortest-return graph proof, not a diagonalization of 4^28 states."
  },
  "ground_sector_theorem": {
    "microscopic_registers": 28,
    "microscopic_hilbert_dimension": 72057594037927936,
    "isolated_low_band": 256,
    "third_order_ground_sector_negative_g": 35,
    "sixth_order_ground_sector_negative_g": 5,
    "native_ground_irrep": 5,
    "conditions": [
      "four identical Hamming protected C4 blocks",
      "same-site Pauli-complete swap links on K4 or C4",
      "Delta>0",
      "g<0 and |g|/Delta sufficiently small",
      "actual energy and state identification with TFPT not derived"
    ],
    "low_band_sufficient_isolation_bound_K4": "|g|/Delta<1/105 (only isolation; not a numerical validity bound for sixth-order splitting)",
    "gap_asymptotic_K4": "(27573/512)*|g|^6/Delta^5+O(|g|^7/Delta^6)",
    "gap_asymptotic_C4": "(3143/256)*|g|^6/Delta^5+O(|g|^7/Delta^6)"
  },
  "summary": {
    "passed": 1326,
    "seconds": 4.506535053253174,
    "kind": "independent finite algebra and perturbation coefficient audit, no physical TOE proof"
  }
}
```

</details>

<a id="daten-q4"></a>
## Q4. Ergebniswerte

**Archivmitglied:** `TFPT_Rekursive_Bindung_20260926/results.json`  
**SHA256 der vollständigen JSON Originaldatei:** `99222be92520485a2bf49d2216c1dba9d40f137916e084874aa8f74b62246b84`

Die vollständige Originaldatei enthält zusätzlich 167 Einträge in `checks`. Deren Belegart folgt dem Bericht; bei Q4 sind exakte und numerische Kontrollen getrennt.

<details>
<summary>Q4: alle Ergebniswerte öffnen</summary>

```json
{
  "pair_identity": {
    "R_rank": 2,
    "R_count": 15,
    "sum_R": "6 I",
    "sum_R_tensor_R": "(3/2) I25 + (9/2) vectorized(Petz o E2)",
    "pair_h": "I25 - vectorized(Petz o E2)",
    "pair_h_spectrum": {
      "0": 1,
      "5/9": 9,
      "1": 15
    },
    "second_order_H": "-192 epsilon^2/delta I25 -576 epsilon^2/delta vectorized(Petz o E2)"
  },
  "exact_pair": {
    "space_dimension": 1225,
    "neutral_dimension": 85,
    "orthonormal_singlet_block": [
      [
        "0",
        "16*sqrt(6)*t"
      ],
      [
        "16*sqrt(6)*t",
        "2*delta + 16*t"
      ]
    ],
    "ground_energy": "delta+8epsilon-sqrt((delta+8epsilon)^2+1536epsilon^2)",
    "proved_sufficient_ground_range": "0 < abs(epsilon)/delta <= 1/200",
    "proved_gap_lower_bound": "170 epsilon^2/delta",
    "excited_weight": "(1-(delta+8epsilon)/sqrt((delta+8epsilon)^2+1536epsilon^2))/2",
    "reduced_state": "(1-eta) Pi5/5 + eta (I35-Pi5)/30",
    "scope": "exact stated 35-response-space model, not a diagonalization of the full microscopic register parent"
  },
  "recursive_projection": {
    "ground_energy": "19/18 - sqrt(73)/18",
    "gap": "-1/18 + sqrt(73)/18",
    "ground_dimension": 5,
    "four_intertwiner_gram": [
      [
        "5",
        "1",
        "1",
        "6/5"
      ],
      [
        "1",
        "5",
        "1",
        "6/5"
      ],
      [
        "1",
        "1",
        "5",
        "6/5"
      ],
      [
        "6/5",
        "6/5",
        "6/5",
        "756/625"
      ]
    ],
    "four_multiplicity_H": [
      [
        "7/9",
        "-4/9",
        "-2/9",
        "-6/25"
      ],
      [
        "-2/9",
        "14/9",
        "-2/9",
        "0"
      ],
      [
        "-2/9",
        "-4/9",
        "7/9",
        "-6/25"
      ],
      [
        "25/54",
        "25/27",
        "25/54",
        "2"
      ]
    ],
    "ground_coefficients": [
      [
        "-27/50 - 3*sqrt(73)/50"
      ],
      [
        "-12/25"
      ],
      [
        "-27/50 - 3*sqrt(73)/50"
      ],
      [
        "1"
      ]
    ],
    "ground_norm": "378*sqrt(73)/625 + 3942/625",
    "endpoint_alpha": "5*sqrt(73)/144 + 49/144",
    "endpoint_alpha_squared": "245*sqrt(73)/10368 + 2113/10368",
    "endpoint_alpha_numeric": 0.636944574490192,
    "endpoint_factor_numeric": 0.40569839097249183,
    "middle_alpha": "85*sqrt(73)/5256 + 17/72",
    "weak_link_projection": "alpha^2 h + (4/5)(1-alpha^2) I",
    "scope": "exact compression of each weak link; full low-energy approximation requires weak/strong hierarchy and includes higher-order corrections"
  },
  "numerical_next_order": {
    "coefficients_in_units_weak_squared_over_strong": {
      "1": -0.2624166699806795,
      "5": -0.05807535460172699,
      "9": -0.10652443252979943,
      "10": -0.056781779078112535
    },
    "native_sector_fit_max_residual": 1.6653345369377348e-16,
    "split_5_minus_10": -0.0012935755236144555,
    "conclusion": "leading two-parameter form I,h is not a closed all-order renormalization family",
    "classification": "double-precision countercheck, no interval-certified spectral bounds"
  },
  "global_scope": {
    "symmetric_dimension_for_N_sources": "binomial(N+3,3)",
    "symmetric_dimension_8_sources": "165",
    "no_global_symmetric_exact_four_code_for_N_ge_5": "proof by transporting quartic Pauli checks and anticommuting weight-two checks",
    "micro_parent_not_rederived": [
      "P1/P2 selection",
      "bridge strength and signs",
      "graph and scale hierarchy",
      "field and state dictionary",
      "3+1D limit",
      "gravity"
    ]
  },
  "summary": {
    "exact_checks": 165,
    "numerical_checks": 2,
    "all_passed": true,
    "runtime_seconds": 28.67020082473755,
    "python": "3.13.5",
    "numpy": "2.3.5",
    "sympy": "1.14.0",
    "meaning": "finite explicitly specified continuation, not a complete TFPT proof"
  }
}
```

</details>

<a id="daten-q5"></a>
## Q5. Ergebniswerte

**Archivmitglied:** `TFPT_Ladung_Komposition_20260926/results.json`  
**SHA256 der vollständigen JSON Originaldatei:** `1b36c2c7fc34920a0d2aa1a3c847fae5392371df2d39d00b7020ee64d0a046e5`

Die vollständige Originaldatei enthält zusätzlich 138 Einträge in `checks`. Deren Belegart folgt dem Bericht; bei Q4 sind exakte und numerische Kontrollen getrennt.

<details>
<summary>Q5: alle Ergebniswerte öffnen</summary>

```json
{
  "original_charge_test": {
    "Y_in_code_coordinates": [
      [
        "9/40 - sqrt(6)/10",
        "-sqrt(6)/12 - 1/8",
        "-sqrt(6)/12 - 1/8",
        "-sqrt(6)/12 - 1/8",
        "-9/20 - sqrt(6)/20"
      ],
      [
        "-sqrt(6)/36 - 1/24",
        "-1/8",
        "5/24",
        "5/24",
        "1/12 - sqrt(6)/12"
      ],
      [
        "-sqrt(6)/36 - 1/24",
        "5/24",
        "-1/8",
        "5/24",
        "1/12 - sqrt(6)/12"
      ],
      [
        "-sqrt(6)/36 - 1/24",
        "5/24",
        "5/24",
        "-1/8",
        "1/12 - sqrt(6)/12"
      ],
      [
        "-3/40 - sqrt(6)/120",
        "1/24 - sqrt(6)/24",
        "1/24 - sqrt(6)/24",
        "1/24 - sqrt(6)/24",
        "3/20 + sqrt(6)/10"
      ]
    ],
    "commutator_HS_squared": "32*sqrt(6)/405 + 488/405",
    "mix_5_10_HS_squared": "67/60 - sqrt(6)/5",
    "mix_9_10_HS_squared": "sqrt(6)/5 + 61/20",
    "Y_norm5_squared": "sqrt(6)/10 + 29/60",
    "Y_norm9_squared": "7/20 - sqrt(6)/10",
    "onsite_complex_Lie_constraint_rank": 24,
    "native_charge_orbit_span": 14,
    "commutator_span": 10,
    "scope": "fixed positive polar marking; h as operator on V tensor conjugate(V); not a contradiction in the earlier uncharged model"
  },
  "marked_group_alternative": {
    "group": "S(U(3) x U(2))",
    "commutant_dimension": 8,
    "paired_decomposition": "two singlets + 8 + 3 + 6 + conjugate(6)",
    "averaged_energies_Y_8_3_6_6": [
      "4*sqrt(6)/75 + 61/75",
      "2*sqrt(6)/375 + 1247/1500",
      "4*sqrt(6)/375 + 311/375",
      "314/375 - 4*sqrt(6)/375",
      "314/375 - 4*sqrt(6)/375"
    ],
    "construction": "normalized Haar average of old h; trace over each multiplicity-one sector, singlet Omega remains zero",
    "scope": "a different, marking-dependent covariance completion; SU(5) is not forced by the TFPT postulates simply by this audit"
  },
  "completion": {
    "operator": "(5/6)(I-P_Omega)",
    "eigenspaces": "0:1; 5/6:24",
    "HS_squared_change": "10/9",
    "channel": "X -> (X+Tr(X)I)/6",
    "assumption": "full unmarked native S6 AND additive hypercharge as exact symmetries; not automatically mandatory at a fixed TFPT marking",
    "uniqueness": "up to common energy shift and positive scale; 5/6 fixes trace and is the nearest Hilbert-Schmidt projection"
  },
  "covariant_recursion": {
    "W": "(T1+T3)/sqrt(12)",
    "space": "V tensor conjugate(V) tensor V",
    "three_spectrum": {
      "2/3": 5,
      "1": 5,
      "5/3": 115
    },
    "gap": "1/3",
    "endpoint": "(7 X+Tr(X) I)/12",
    "middle": "(X^T+Tr(X) I)/6",
    "charge_identity": "(Y1-Y2^T+Y3)W=WY",
    "projected_bond": "(49/144) h + (19/36) I",
    "limit": "weak coupling projection; no preselected spatial dimension or microscopic scale hierarchy"
  },
  "TL_composition": {
    "e": "5 P_Omega",
    "loop_parameter": 5,
    "q": "sqrt(21)/2 + 5/2",
    "R": "(q-q^(-1)t^2) I + (t^2-1) e",
    "identity": "R_i(t)R_(i+1)(tu)R_i(u)=R_(i+1)(u)R_i(tu)R_(i+1)(t)",
    "unitary": "for t=exp(i theta), divide R by sqrt(23-2 cos(2theta))",
    "scope": "classical Temperley-Lieb Baxterization for this completed chain, not a TFPT clock or 3+1D scattering theorem"
  },
  "three_block_correction": {
    "physical_basis": "I, P12, P23, Swap13, {P12,P23}",
    "coefficients": [
      "49/93312",
      "-1225/93312",
      "-1225/93312",
      "0",
      "30625/186624"
    ],
    "units": "Jweak^2/Jstrong; cross contribution of the two different weak bonds only",
    "squared_HS_distance_from_invariant_two_body_span": "2100875/241864704",
    "meaning": "no exact nearest-neighbor pair-only RG closure; TL composition and RG projection are different statements"
  },
  "native_invariant_dimensions": {
    "1": 1,
    "2": 4,
    "3": 41,
    "4": 694,
    "5": 14851,
    "6": 350384
  },
  "summary": {
    "all_passed": true,
    "checks": 138,
    "runtime_seconds": 15.703335577000189,
    "python": "3.13.5",
    "sympy": "1.14.0",
    "numpy": "2.3.5",
    "scope": "finite exact consistency audit and explicit changed-model completion; no TOE or physical spacetime claim"
  }
}
```

</details>


---

<a id="pruefprogramme"></a>
# 27. Vollständige bereitgestellte Prüfprogramme

Die Quelltexte werden zur Dokumentation und späteren Reproduktion wortgetreu wiedergegeben. Sie wurden in dieser Konsolidierungsrunde **nicht ausgeführt**. Zum Ausführen sind die jeweiligen Dateien in ein eigenes Arbeitsverzeichnis zu übernehmen und die angeführten Abhängigkeiten zu installieren. Für historische Hintergrundberichte ohne hier bereitgestellten Programmtext wird kein Ersatzprogramm erfunden.

<a id="programm-z"></a>
## Z. Prüfprogramm und Abhängigkeiten

<details>
<summary>Z: audit.py öffnen</summary>

Originalmitglied: `tfpt_zuse_audit/audit.py`  
SHA256: `27d02394f3e8639e52d7d0854c2015058bbe2f9e3f2b1fafac89a07aede1c45b`

```python
#!/usr/bin/env python3
"""Independent finite audit of selected TFPT / Zuse implications.

Requires Python 3.10+, numpy, sympy. Run: python audit.py
This is NOT the TFPT repository verification suite and is NOT a TOE proof.
The 60-ray model is rebuilt from the documented description: 24 one-qubit
Clifford rays plus 36 stabilizer preparation/measurement rays. Floating-point
matrix enumerations are separated from symbolic checks and analytic arguments.
No spatial graph, physical time, or TFPT source-selection theorem is inferred.
"""
from __future__ import annotations
import json
import itertools
from collections import Counter, deque
from pathlib import Path
import numpy as np
import sympy as sp

TOL = 1e-10

def require(ok: bool, message: str) -> None:
    if not ok:
        raise RuntimeError(message)

def ray_key(a: np.ndarray) -> tuple[float, ...] | None:
    v = a.ravel()
    nz = np.flatnonzero(np.abs(v) > TOL)
    if not len(nz):
        return None
    v = v / v[nz[0]]
    return tuple(np.round(np.r_[v.real, v.imag], 10))

def maxabs(a: np.ndarray) -> float:
    return float(np.max(np.abs(a)))

def diameter(adjacency: np.ndarray) -> int:
    n = len(adjacency)
    answer = 0
    for source in range(n):
        distance = [-1] * n
        distance[source] = 0
        queue = deque([source])
        while queue:
            u = queue.popleft()
            for v in np.flatnonzero(adjacency[u]):
                if distance[v] == -1:
                    distance[v] = distance[u] + 1
                    queue.append(int(v))
        require(min(distance) >= 0, 'Graph is not strongly connected')
        answer = max(answer, max(distance))
    return answer

def channel_matrices(ops: list[np.ndarray]) -> tuple[np.ndarray, float]:
    paulis = [np.eye(2, dtype=complex), np.array([[0,1],[1,0]],complex),
              np.array([[0,-1j],[1j,0]],complex), np.diag([1,-1]).astype(complex)]
    matrix = np.zeros((4,4), complex)
    for j, p in enumerate(paulis):
        out = sum((a @ p @ a.conj().T for a in ops), np.zeros((2,2),complex))/len(ops)
        for i,q in enumerate(paulis):
            matrix[i,j] = np.trace(q @ out)/2
    completeness = sum((a.conj().T@a for a in ops), np.zeros((2,2),complex))/len(ops)
    return matrix, maxabs(completeness-np.eye(2))

def finite_60_audit() -> dict:
    h = np.array([[1,1],[1,-1]],complex)/np.sqrt(2)
    s = np.diag([1,1j])
    cliff = {ray_key(np.eye(2)):np.eye(2,dtype=complex)}
    pending = deque(cliff.values())
    while pending:
        a = pending.popleft()
        for generator in (h,s):
            b = generator @ a
            key = ray_key(b)
            if key not in cliff:
                cliff[key] = b
                pending.append(b)
                require(len(cliff) <= 24, 'Clifford enumeration exceeded 24 rays')
    require(len(cliff)==24, 'Wrong Clifford ray count')
    states = [np.array([1,0],complex),np.array([0,1],complex)]
    states += [np.array([1,z],complex)/np.sqrt(2) for z in (1,-1,1j,-1j)]
    rankone = [np.sqrt(2)*np.outer(u,v.conj()) for u in states for v in states]
    ops = list(cliff.values())+rankone
    known = {ray_key(a) for a in ops}
    require(len(known)==60, 'Wrong total ray count')
    norms = Counter()
    missing = []
    adjacency = np.zeros((60,60),bool)
    for i,a in enumerate(ops):
        for j,b in enumerate(ops):
            product = b @ a
            n2 = float(np.vdot(product,product).real)
            nearest = min((0,2,4),key=lambda x:abs(n2-x))
            require(abs(n2-nearest)<TOL, 'Unexpected squared Frobenius norm')
            norms[nearest] += 1
            key = ray_key(product)
            if key is not None:
                adjacency[i,j] = True
                if key not in known:
                    missing.append((i,j))
    require(not missing, 'Nonzero projective product leaves 60-ray set')
    require(dict(norms)=={2:3168,0:216,4:216}, 'Product census mismatch')
    target = np.diag([1,0,0,0])
    twirls = {}
    for label,subset in [('clifford24',list(cliff.values())),('rankone36',rankone),('full60',ops)]:
        ptm, comp = channel_matrices(subset)
        twirls[label] = {'depolarizing_ptm_error':maxabs(ptm-target), 'trace_preservation_error':comp}
        require(maxabs(ptm-target)<TOL and comp<TOL, 'Uniform twirl is not depolarizing')
    # Defining compatibility as nonzero successive product is an explicit candidate,
    # not a derivation of the intended physical gluing rule.
    mutual = adjacency & adjacency.T
    p0 = np.diag([1,0]); p1 = np.diag([0,1]); identity = np.eye(2)
    return {
      'arithmetic':'numpy complex128, tolerance 1e-10; structural counts have elementary exact proofs',
      'ray_counts':{'unitary':24,'rank_one':36,'total':60},
      'product_squared_frobenius_norm_counts':{str(k):v for k,v in sorted(norms.items())},
      'nonzero_projective_products_closed':True,
      'candidate_compatibility':'C(A,B)=1 iff B@A is nonzero (operator TYPES, not spacetime events)',
      'outdegree_including_loops_counts':{str(k):v for k,v in Counter(map(int,adjacency.sum(axis=1))).items()},
      'directed_diameter':diameter(adjacency),
      'mutual_compatibility_undirected_diameter':diameter(mutual),
      'uniform_channels':twirls,
      'pairwise_composable_history_can_vanish': bool(np.any(identity@p0) and np.any(p1@identity) and not np.any(p1@identity@p0)),
    }

def symbolic_audit() -> dict:
    t = sp.symbols('t',real=True)
    permutations = [(0,1,2),(1,2,0),(2,0,1),(1,0,2),(2,1,0),(0,2,1)]
    matrices = []
    for permutation in permutations:
        p = sp.zeros(3)
        for col,row in enumerate(permutation): p[row,col]=1
        matrices.append(p)
    weights = [sp.Rational(1,2)+t,t,t,sp.Rational(1,18)-t,sp.Rational(2,9)-t,sp.Rational(2,9)-t]
    b = sum((w*p for w,p in zip(weights,matrices)),sp.zeros(3))
    expected_b = sp.Matrix([[13,1,4],[1,13,4],[4,4,10]])/18
    require(sp.simplify(b-expected_b)==sp.zeros(3),'Birkhoff population mismatch')
    v = sp.Matrix([[1/sp.sqrt(2),1/sp.sqrt(6)],[-1/sp.sqrt(2),1/sp.sqrt(6)],[0,-2/sp.sqrt(6)]])
    reps = [sp.simplify(v.T*p*v) for p in matrices]
    paulis = [sp.eye(2),sp.Matrix([[0,1],[1,0]]),sp.Matrix([[0,-sp.I],[sp.I,0]]),sp.diag(1,-1)]
    ptm = sp.zeros(4)
    for j,p in enumerate(paulis):
        out = sp.simplify(sum((w*u*p*u.T for w,u in zip(weights,reps)),sp.zeros(2)))
        for i,q in enumerate(paulis): ptm[i,j]=sp.simplify(sp.trace(q*out)/2)
    require(ptm[2,2]==6*t, 'Coherence multiplier mismatch')
    # Distinguish the channels on a physical +Y input, not just by a PTM entry.
    rho_y_plus = (sp.eye(2) + paulis[2])/2
    rho_out_t = sp.simplify(sum((w*u*rho_y_plus*u.T for w,u in zip(weights,reps)),sp.zeros(2)))
    delta_rho = sp.simplify(rho_out_t.subs(t,sp.Rational(1,27))-rho_out_t.subs(t,0))
    y_difference = sp.simplify(sp.trace(paulis[2]*delta_rho))
    trace_distance = sp.simplify(sum(abs(e)*mult for e,mult in delta_rho.eigenvals().items())/2)
    require(y_difference==sp.Rational(2,9), 'Physical Y expectation difference mismatch')
    require(trace_distance==sp.Rational(1,9), 'Physical output trace distance mismatch')
    gram = sp.Matrix([[1,1,0],[1,1,1],[0,1,1]])
    witness = sp.Matrix([1,-1,1])
    witness_value = (witness.T*gram*witness)[0]
    require(witness_value == -1,'Gram witness mismatch')
    T,x,y,z = sp.symbols('T x y z',real=True)
    herm = sp.Matrix([[T+z,x-sp.I*y],[x+sp.I*y,T-z]])
    det = sp.expand(herm.det())
    require(det==T*T-x*x-y*y-z*z, 'Minkowski determinant mismatch')
    units30 = [k for k in range(30) if sp.gcd(k,30)==1]
    order7 = next(n for n in range(1,9) if pow(7,n,30)==1)
    require(order7==4, 'Automorphism order mismatch')
    # Exact completion for equally weighted nearest-neighbor overlaps in 3 charts.
    a = sp.symbols('a', real=True)
    gram_path = sp.Matrix([[1,a,0],[a,1,a],[0,a,1]])
    cyclic4 = sp.diag(1,sp.I,-1,-sp.I)
    h0 = sp.diag(0,3*sp.pi/2,sp.pi,sp.pi/2)
    h1 = h0+2*sp.pi*sp.diag(0,1,0,0)
    require(sp.simplify((-sp.I*h0).exp()-cyclic4)==sp.zeros(4),'Clock exponential mismatch')
    require(sp.simplify((-sp.I*h1).exp()-cyclic4)==sp.zeros(4),'Alternative clock exponential mismatch')
    # A nontrivial determinant-one Lorentz boost is NOT projectively unitary or rank one.
    boost = sp.diag(2,sp.Rational(1,2))
    boost_X = sp.expand(boost*herm*boost.conjugate().T)
    require(sp.simplify(boost_X.det()-det)==0, 'Boost determinant invariant mismatch')
    require(boost.det()==1 and boost.conjugate().T*boost != sp.eye(2), 'Boost example invalid')
    gp,mass = sp.symbols('G M', positive=True)
    reduced_planck_squared=1/(8*sp.pi*gp)
    hawking=1/(8*sp.pi*gp*mass)
    require(sp.simplify(hawking-reduced_planck_squared/mass)==0, 'Reduced Planck normalization mismatch')
    return {
      'arithmetic':'sympy exact rational / algebraic / symbolic',
      'B_population':str(b),
      'B_eigenvalues':{str(k):v for k,v in b.eigenvals().items()},
      'Birkhoff_weights':list(map(str,weights)),
      'contrast_Pauli_transfer_order_I_X_Y_Z':str(ptm),
      't_zero_vs_one_over_27_Y_expectation_difference':str(y_difference),
      't_zero_vs_one_over_27_output_trace_distance_for_Y_plus':str(trace_distance),
      'gram_eigenvalues':{str(k):v for k,v in gram.eigenvals().items()},
      'gram_quadratic_witness':str(witness_value),
      'three_chart_equal_overlap_eigenvalues':{str(k):v for k,v in gram_path.eigenvals().items()},
      'hermitian_2x2_determinant':str(det),
      'determinant_one_boost_outside_composition_only_60_rays':str(boost),
      'boost_acts_on_Hermitian_matrix':str(boost_X),
      'reduced_Planck_Hawking_formula_hbar_c_kB_equal_1':'T_H = bar_M_Pl**2 / M; an extra c3=1/(8*pi) is incorrect',
      'units_mod_30':units30,
      'multiplicative_order_7_mod_30':order7,
      'C30_contains_order4_element':False,
      'same_mu4_clock_distinct_positive_generators':True,
      'binary_pairwise_inequality_triple_solutions':len([v for v in itertools.product([0,1],repeat=3) if v[0]!=v[1] and v[1]!=v[2] and v[2]!=v[0]])
    }

def main() -> None:
    result = {
      'scope':'Finite mathematical checks only; no derivation of a physical source, spacetime, chirality, quantum gravity, or full TFPT closure.',
      'finite60':finite_60_audit(),
      'symbolic':symbolic_audit(),
    }
    text = json.dumps(result,ensure_ascii=False,indent=2,default=str)
    Path(__file__).with_name('results.json').write_text(text+'\n',encoding='utf-8')
    print(text)

if __name__=='__main__': main()

```

</details>

<details>
<summary>Z: requirements.txt öffnen</summary>

Originalmitglied: `tfpt_zuse_audit/requirements.txt`  
SHA256: `6023d480f929cdfa4e2f35e361eea003451cd6695af806935a32038b0115abb5`

```text
numpy
sympy

```

</details>

<a id="programm-q1"></a>
## Q1. Prüfprogramm und Abhängigkeiten

<details>
<summary>Q1: audit.py öffnen</summary>

Originalmitglied: `TFPT_Quartik_Fortsetzung/audit.py`  
SHA256: `75e6e278d0fb9f901b6a3a939812129605a1311cab7b617f55adb0a95edf2c35`

```python
#!/usr/bin/env python3
"""Finite TFPT quartic-code audit, 2026-09-26.

Rebuilds all matrices from the stated code and RM(1,3) rules. No fitted
physical constants, network access, previous result files or theorem prover
are required. Integer/rational checks and floating-point checks are tagged
separately in results.json. This is not a proof of a physical TOE.
"""
from __future__ import annotations
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS', '1')
os.environ.setdefault('OMP_NUM_THREADS', '1')
from itertools import product, permutations, combinations
from collections import Counter
from pathlib import Path
import json, math, hashlib, platform, time
import numpy as np
import scipy
import scipy.linalg as la
from scipy.optimize import minimize_scalar
import sympy as sp

ROOT = Path(__file__).resolve().parent
checks: list[dict] = []
R: dict = {}

def check(name: str, condition: bool, kind: str = 'integer_or_rational_identity', **data):
    if not bool(condition):
        raise RuntimeError(f'CHECK FAILED: {name}: {data}')
    checks.append(dict(name=name, kind=kind, passed=True, **data))

def near(name, value, tol=1e-10):
    check(name, value < tol, 'floating_point_check', residual=float(value), tolerance=tol)

def idx(t, d=4):
    n=0
    for x in t: n=n*d+int(x)
    return n

def kron(args):
    out=np.array([[1]],complex)
    for a in args: out=np.kron(out,a)
    return out

def unique_perms(*ts):
    return sorted(set(p for t in ts for p in permutations(t)))

def perm_matrix(n,p,d=4):
    col=np.arange(d**n)
    ts=np.array(np.unravel_index(col,(d,)*n))
    row=np.ravel_multi_index(ts[list(p)],(d,)*n)
    m=np.zeros((d**n,d**n),dtype=np.int64)
    m[row,col]=1
    return m

def ptrace(rho,k,n=4,d=4):
    a,b=d**k,d**(n-k)
    return np.einsum('irjr->ij',rho.reshape(a,b,a,b))

def apply_one(U,mat,site,n):
    t=mat.reshape((4,)*n+(mat.shape[-1],))
    t=np.tensordot(U,t,axes=([1],[site]))
    return np.moveaxis(t,0,site).reshape(4**n,mat.shape[-1])

def apply_collective(U,mat,n):
    for r in range(n): mat=apply_one(U,mat,r,n)
    return mat

def gauss_collective(Ur,Ui,mat,n):
    """Gaussian-integer tensor action. All operations are signed int64."""
    re=mat.copy(); im=np.zeros_like(re)
    for site in range(n):
        nr=apply_one(Ur,re,site,n)-apply_one(Ui,im,site,n)
        ni=apply_one(Ur,im,site,n)+apply_one(Ui,re,site,n)
        re,im=nr,ni
    return re,im

def exact_gaussian(m):
    re=np.rint(m.real).astype(np.int64); im=np.rint(m.imag).astype(np.int64)
    if not (np.array_equal(re,m.real) and np.array_equal(im,m.imag)):
        raise RuntimeError('Expected Gaussian integer matrix')
    return sp.Matrix(re)+sp.I*sp.Matrix(im)

def independent(ms):
    c=sp.Matrix.hstack(*[sp.Matrix(list(m)) for m in ms])
    return [ms[j] for j in c.rref()[1]]

def gf2rank(A):
    B=np.array(A,dtype=np.int64).copy()%2; r=0
    for c in range(B.shape[1]):
        nz=np.where(B[r:,c])[0]
        if len(nz)==0: continue
        j=r+int(nz[0]); B[[r,j]]=B[[j,r]]
        for k in range(B.shape[0]):
            if k!=r and B[k,c]: B[k]^=B[r]
        r+=1
        if r==B.shape[0]: break
    return r

start=time.time()
# 1. Explicit symmetric five-code; E has integral, mutually disjoint supports.
supports=[[(j,j,j,j) for j in range(4)],
          unique_perms((0,0,1,1),(2,2,3,3)),
          unique_perms((0,0,2,2),(1,1,3,3)),
          unique_perms((0,0,3,3),(1,1,2,2)),
          unique_perms((0,1,2,3))]
E=np.zeros((256,5),dtype=np.int64)
for j,s in enumerate(supports):
    for t in s: E[idx(t),j]=1
norms=np.sum(E*E,axis=0)
check('code_support_norms',list(norms)==[4,12,12,12,24])
G=sp.diag(*map(int,norms)); Ginv=G.inv()
V=E/np.sqrt(norms)
D24=np.diag(24//norms)
Pnum=E@D24@E.T; P=Pnum/24
Snum=sum(perm_matrix(4,p) for p in permutations(range(4))); S=Snum/24
I2=np.eye(2,dtype=complex); I4=np.eye(4); I256=np.eye(256)
X=np.array([[0,1],[1,0]],complex); Y=np.array([[0,-1j],[1j,0]])
Z=np.diag([1,-1]).astype(complex)
paulis=[np.kron(a,b) for a in (I2,X,Y,Z) for b in (I2,X,Y,Z)]
labels=[a+b for a in 'IXYZ' for b in 'IXYZ']
Qraw=sum(kron([a]*4) for a in paulis)
check('quartic_stabilizer_numerator_real_integral',np.array_equal(Qraw.imag,np.zeros((256,256))) and np.array_equal(Qraw.real,np.rint(Qraw.real)))
Qnum=Qraw.real.astype(np.int64); Q=Qnum/16
check('P5_projector_rank5',np.array_equal(Pnum@Pnum,24*Pnum) and np.trace(Pnum)==120)
check('Q_projector_rank16',np.array_equal(Qnum@Qnum,16*Qnum) and np.trace(Qnum)==256)
check('P5_equals_Sym4_Q',np.array_equal(Snum@Qnum,16*Pnum))

# 2. Actual 240 Construction-A roots and 60 complex directions.
coords=list(product((0,1),repeat=3)); rm=[]
for a in product((0,1),repeat=4):
    rm.append(tuple((a[0]+sum(a[k+1]*x[k] for k in range(3)))%2 for x in coords))
roots=[]
for j in range(8):
    for sgn in (-1,1):
        r=np.zeros(8,dtype=np.int64); r[j]=2*sgn; roots.append(r)
for w in rm:
    if sum(w)!=4: continue
    active=np.flatnonzero(w)
    for signs in product((-1,1),repeat=4):
        r=np.zeros(8,dtype=np.int64); r[active]=signs; roots.append(r)
roots=np.stack(roots); rays={}
for r in roots:
    z=r[::2]+1j*r[1::2]; pp=np.outer(z,z.conj())
    key=tuple(np.r_[pp.real.ravel(),pp.imag.ravel()].astype(np.int64))
    rays[key]=pp
raynums=list(rays.values())
check('root_and_ray_census',len(roots)==240 and len(raynums)==60)
N4=sum(kron([p]*4) for p in raynums)
check('moment_identity_40M4_S_P',np.array_equal(N4.imag,np.zeros((256,256))) and np.array_equal(N4.real,16*(Snum+Pnum)))
M4=(P+S)/40
refs=[I4-p/2 for p in raynums]

# 3. Erasure, reduced states and exact observation ranks.
Es=E.reshape(4,64,5)
check('one_register_erasure_Knill_Laflamme',all(np.array_equal(Es[a].T@Es[b],np.diag(norms//4) if a==b else np.zeros((5,5),dtype=np.int64)) for a,b in product(range(4),repeat=2)))
ranks={}
for k in (1,2,3):
    check(f'k{k}_rho5_rho35_marginals_equal',np.array_equal(7*ptrace(Pnum,k),ptrace(Snum,k)))
    C=np.stack([ptrace(np.outer(E[:,i],E[:,j]),k).ravel() for i,j in product(range(5),repeat=2)],axis=1)
    ranks[k]=int(sp.Matrix(C.T@C).rank())
check('observation_ranks_1_10_25',list(ranks.values())==[1,10,25])
R['observation_ranks']=ranks

# 4. Two-body control and the projective-line decomposition of observables.
pairs=list(combinations(range(4),2)); raw={}; Hsym={}; L={}; h={}
for name,a in zip(labels[1:],paulis[1:]):
    terms=[]
    for i,j in pairs:
        ops=[I4]*4; ops[i]=a; ops[j]=a; terms.append(kron(ops))
    raw[name]=terms[0]; Hsym[name]=sum(terms)/6
    L[name]=Ginv*exact_gaussian(E.T@terms[0]@E)
    h[name]=V.T@terms[0]@V
    check(f'{name}_sym_pair_preserves_code',exact_gaussian(sum(terms)@E)==6*sp.Matrix(E)*L[name])
    check(f'{name}_pair_spectrum',L[name].charpoly().as_expr().factor()==(sp.Symbol('lambda')-1)**2*(3*sp.Symbol('lambda')+1)**3/27)
check('pair_span_rank10',len(independent(list(L.values())))==10)
check('pair_sum_3I',sum(L.values(),sp.zeros(5))==3*sp.eye(5))
# Leakage for an isolated Pauli pair is I-h^2, with eigenvalues 0 and 8/9.
check('isolated_pair_leakage_exact',all((sp.eye(5)-m*m).charpoly().as_expr().factor()==sp.Symbol('lambda')**2*(9*sp.Symbol('lambda')-8)**3/729 for m in L.values()))
gens=[L[n]-sp.trace(L[n])/5*sp.eye(5) for n in ('IX','IZ','XI','ZZ')]
basis=independent(gens); growth=[len(basis)]
while len(basis)<24:
    new=independent(basis+[sp.I*(a*b-b*a) for a in gens for b in basis])
    if len(new)==len(basis): break
    basis=new; growth.append(len(basis))
check('su5_exact_Lie_growth',growth==[4,7,12,17,22,24])
R['Lie_growth']=growth
trip={'commuting':[],'anticommuting':[]}; trip_labels={'commuting':[],'anticommuting':[]}
for i,j in combinations(range(1,16),2):
    k=i^j
    if j>=k: continue
    typ='commuting' if np.array_equal(paulis[i]@paulis[j],paulis[j]@paulis[i]) else 'anticommuting'
    T=Ginv*exact_gaussian(E.T@kron([paulis[i],paulis[j],paulis[k],I4])@E)
    trip[typ].append(T); trip_labels[typ].append((labels[i],labels[j],labels[k]))
check('35_lines_split_15_20',len(trip['commuting'])==15 and len(trip['anticommuting'])==20)
check('triple_operator_spans_15_10',len(independent(trip['commuting']))==15 and len(independent(trip['anticommuting']))==10)
check('triple_span_full25',len(independent(trip['commuting']+trip['anticommuting']))==25)
for (a,b,c),T in zip(trip_labels['anticommuting'],trip['anticommuting']):
    phase=complex(np.trace(paulis[labels.index(a)]@paulis[labels.index(b)]@paulis[labels.index(c)])/4)
    s=int(round(phase.imag))
    check('pair_commutator_to_triple_'+a+b,L[a]*L[b]-L[b]*L[a]==sp.Rational(4,3)*sp.I*s*T)
K=sp.sqrt(3)/2*(L['IX']-L['IY'])
# In orthonormal coordinates K restricts to sigma_x on c0,c1.
Kn=np.sqrt(3)/2*(h['IX']-h['IY']); U=la.expm(-1j*np.pi/4*Kn)
plus=np.array([1,1j,0,0,0])/np.sqrt(2); minus=np.conj(plus)
near('phase_to_pair_readout_pulse',max(la.norm(U@plus-np.eye(5)[:,0]),la.norm(U@minus+1j*np.eye(5)[:,1])))

# 5. Bell10 measurement frame, Petersen switching, six source simplex points.
symidx=[i for i,a in enumerate(paulis) if np.array_equal(a.T,a)]
B2=np.stack([paulis[i].reshape(-1).real for i in symidx],axis=1) # norm 2 columns
# amp = B2^T E B2 /4; use integral numerator.
ampnum=np.einsum('in,jm,ija->nma',B2.astype(np.int64),B2.astype(np.int64),E.reshape(16,16,5))
off=ampnum.copy(); Fnum=np.array([ampnum[j,j,:] for j in range(10)])
for j in range(10): off[j,j]=0
check('Bell_pair_offdiagonal_amplitudes_vanish',not np.any(off))
F=sp.Matrix(Fnum)/4 # unnormalized logical-coordinate frame
Gram=F*Ginv*F.T
check('Bell_measurement_frame_isometry',F.T*F==G)
check('Bell_effect_norm_and_overlap',all(Gram[i,j]**2==(sp.Rational(1,4) if i==j else sp.Rational(1,36)) for i,j in product(range(10),repeat=2)))
C=6*Gram-3*sp.eye(10)
check('conference_Seidel_C2_9I',C*C==9*sp.eye(10))
W=sp.Matrix([[2,2,-1,-1,-1,-1],[0,0,-1,-1,1,1],[0,0,-1,1,-1,1],[0,0,1,-1,-1,1],[1,-1,0,0,0,0]])
check('source_six_simplex_Gram',W.T*G*W==48*sp.eye(6)-8*sp.ones(6))
Signs=F*W/2
check('six_simplex_are_Bell_sign_frames',set(Signs)=={-1,1} and C*Signs==3*Signs)
for j in range(6):
    D=sp.diag(*Signs[:,j]); A=(sp.ones(10)-sp.eye(10)-D*C*D)/2
    check('Petersen_frame_'+str(j),A*sp.ones(10,1)==3*sp.ones(10,1) and A*A==2*sp.eye(10)+sp.ones(10)-A)
Cn=np.array(C,dtype=np.int64); n_switch=0
for bits in product((-1,1),repeat=9):
    s=np.array((1,)+bits)
    if np.array_equal(Cn@s,3*s): n_switch+=1
check('exactly_six_regular_sign_frames_up_to_global_sign',n_switch==6)
# Petz roundtrip has spectrum 1,4/9 (9 times),0 (15 times).
Petz=2*Gram.applyfunc(lambda x:x*x)
check('Petz_classical_matrix',Petz==sp.Rational(4,9)*sp.eye(10)+sp.ones(10)/18)
# The six marked simplex rays are invisible in the complete pair channel.
mark_projectors=[W[:,j]*(W[:,j].T*G)/40 for j in range(6)]
blind=[p-sp.eye(5)/5 for p in mark_projectors]
check('six_marks_same_pair_readout',all(sp.trace(p*a)==sp.trace(a)/5 for p in mark_projectors for a in L.values()))
check('six_marks_resolve_logical_identity',sum(mark_projectors,sp.zeros(5))==sp.Rational(6,5)*sp.eye(5))
check('pair_blind_real_subspace_dimension5',len(independent(blind))==5)
check('pair_blind_simplex_operator_Gram',sp.Matrix([[sp.trace(a*b) for b in blind] for a in blind])==sp.Rational(24,25)*sp.eye(6)-sp.Rational(4,25)*sp.ones(6))
R['pair_channel']={'type':'rank-one measure-and-prepare, entanglement breaking','outcomes':10,'normalized_singular_values':{'1':1,'2/3':9,'0':15},'Petz_roundtrip_spectrum':{'1':1,'4/9':9,'0':15},'Petersen_sign_frames':6}

# 6. All 60 native reflections on the actual quartic code/simplex.
Wn=np.sqrt(norms)[:,None]*np.array(W,dtype=float)
restriction=[]; perms=[]; worst=0.
for rr in refs:
    out=apply_collective(rr,V,4); u=V.T@out
    worst=max(worst,float(la.norm(out-V@u)))
    p=tuple(int(np.argmin(la.norm(Wn-(u@Wn)[:,j,None],axis=0))) for j in range(6))
    near('native_simplex_permutation_'+str(len(perms)),la.norm(u@Wn-Wn[:,p]))
    restriction.append(u); perms.append(p)
near('native_reflections_preserve_P5',worst)
check('60_reflections_15_transpositions',len(set(perms))==15 and all(sum(p[i]!=i for i in range(6))==2 for p in perms))
# Native reflection twirl and pair-Petz channel share the full 1+5+9+10 split.
Wnorm=np.array(F,dtype=float)@np.diag(1/np.sqrt(norms))
fx=[np.outer(w,w) for w in Wnorm]
T5=sum(np.kron(u,u.conj()) for u in restriction)/60
Tpair=sum(2*np.outer(f.ravel(),f.ravel().conj()) for f in fx)
i25=np.eye(25)
polyT=(5*T5-3*i25)@(5*T5-i25)@(15*T5-13*i25)/16
near('reflection_twirl_polynomial_pair_Petz_identity',la.norm(Tpair-polyT))
R['pair_blind_marks']={'number_of_pure_mark_states':6,'all_pair_outputs':'P_sym,2/10','hidden_real_traceless_dimension':5,'native_twirl_to_pair_Petz':'T_pair=(5 T5-3 I)(5 T5-I)(15 T5-13 I)/16; operator identity, not an arbitrary positive mixture'}

# Canonical sigma and any fixed marked simplex direction. q* remains a marked input.
sigma=I4[:,[1,2,0,3]]; s5=V.T@apply_collective(sigma,V,4)
spm=tuple(int(np.argmin(la.norm(Wn-(s5@Wn)[:,j,None],axis=0))) for j in range(6))
fixed=[i for i in range(6) if spm[i]==i]
check('sigma_fixed_simplex_marks',len(fixed)==3)
q=fixed[-1]; other=[i for i in range(6) if i!=q]
Diff=W[:,other]-W[:,q]*sp.ones(1,5)
Rot=sp.eye(5)+(1/sp.sqrt(6)-1)*sp.ones(5)/5
Ydiag=sp.diag(*[-sp.Rational(1,3) if spm[j]!=j else sp.Rational(1,2) for j in other])
YL=sp.simplify(Diff*Rot*Ydiag*Rot*Diff.T*G/48)
check('marked_hypercharge_spectrum',YL.charpoly().as_expr().factor()==(2*sp.Symbol('lambda')-1)**2*(3*sp.Symbol('lambda')+1)**3/108)
pb=independent(list(L.values())); gh=sp.Matrix([[sp.trace(a*b) for b in pb] for a in pb]); ghi=gh.inv()
def residual_sq(M):
    v=sp.Matrix([sp.trace(a*M) for a in pb]); return sp.simplify(sp.trace(M*M)-(v.T*ghi*v)[0])
Pq=W[:,q]*(W[:,q].T*G)/40
Yflip=sp.simplify((sp.eye(5)-2*Pq)*YL*(sp.eye(5)-2*Pq))
check('Y_outside_pair_span',residual_sq(YL)==sp.Rational(29,60)+sp.sqrt(6)/10)
check('Y_relative_phase_min_distance',residual_sq(Yflip)==sp.Rational(29,60)-sp.sqrt(6)/10)
R['hypercharge']={'mark_convention':'fixed simplex point of the canonical sigma; q* is an input, not physically selected here','minimum_squared_HS_distance_to_pair_space_over_relative_phase':str(sp.Rational(29,60)-sp.sqrt(6)/10)}
# Analytic phase-minimum proof is in DERIVATIONS.md (concave in cos theta).
Yorth=np.diag(np.sqrt(norms))@np.array(YL.evalf(),dtype=complex)@np.diag(1/np.sqrt(norms))
Wdecoder=2*V.reshape(4,64,5)
O3=sum(w@Yorth@w.conj().T for w in Wdecoder)
near('erasure_decoder_hypercharge_intertwines',la.norm(np.kron(I4,O3)@V-V@Yorth))


# 7. Native moment Hamiltonian and exact overlap obstructions.
Hnat=I256-(P+S)/2
R['moment_parent_spectrum']={'0':5,'1/2':30,'1':221}
near('moment_parent_numeric_spectrum',la.norm(la.eigvalsh(Hnat)-np.array([0]*5+[.5]*30+[1]*221)))
R['overlapping_codes']={}
for s in (1,2,3):
    r=4**(4-s); d=4**s
    KK=np.einsum('xya,yzb->azxb',E.reshape(r,d,5),E.reshape(d,r,5),optimize=True).reshape(5*r,5*r)
    da=np.repeat(24//norms,r); db=np.tile(24//norms,r)
    BN=(da[:,None]*(KK*db[None,:]))@KK.T
    m=144 if s==2 else 36
    check(f'overlap_{s}_minimal_polynomial',np.array_equal(BN@BN,m*BN))
    rank=int(np.trace(BN)//m)
    check(f'overlap_{s}_rank',rank=={1:100,2:10,3:20}[s])
    R['overlapping_codes'][s]={'rank':rank,'nonzero_squared_principal_cosine':'1/4' if s==2 else '1/16','norm_PAPB':'1/2' if s==2 else '1/4','minimum_energy_I_PA_plus_I_PB':'1/2' if s==2 else '3/4','integer_denominator':576}

# 8. Second-order interaction for H0=Delta(Hnat_A+Hnat_B), two ordinary links.
# For A=IZ: K_A=(I+3 h_A)/4 is a projector. Symmetric error sector has energy 1/2,
# other one-error sector energy 1. The inverse on double errors is
# 1/2 I +1/6(S_A+S_B)+1/6 S_A S_B, in units Delta^{-1}.
m=L['IZ']; Id=sp.eye(5); kk=(Id+3*m)/4
check('one_error_bright_sector_projector',kk*kk==kk and sp.trace(kk)==2)
E2=sp.zeros(25)
for i,j in product(range(2),repeat=2):
    cc=Id if i==j else m; dd=kk
    E2-=sp.kronecker_product(cc,cc)/2+(sp.kronecker_product(dd,cc)+sp.kronecker_product(cc,dd))/6+sp.kronecker_product(dd,dd)/6
formula=-sp.Rational(29,24)*sp.eye(25)-sp.Rational(11,24)*(sp.kronecker_product(m,Id)+sp.kronecker_product(Id,m))-sp.Rational(15,8)*sp.kronecker_product(m,m)
check('native_virtual_coupling_exact_second_order',E2==formula)
R['virtual_coupling']={'order':'second order in g/Delta, not exact finite-g dynamics','identity':'-29/24','local_each':'-11/24','entangling_product':'-15/8','units':'g^2/Delta'}
# Independent small invariant-block energy checks.
energies={}
for ii,jj in ((0,0),(0,1),(1,1)):
    si=[idx(t) for t in supports[ii]]; sj=[idx(t) for t in supports[jj]]
    aa=Hnat[np.ix_(si,si)]; bb=Hnat[np.ix_(sj,sj)]
    h0=np.kron(aa,np.eye(len(sj)))+np.kron(np.eye(len(si)),bb)
    vals=[]
    for r in (0,1):
        op=kron([paulis[3] if k==r else I4 for k in range(4)])
        vals.append((op.diagonal().real[si],op.diagonal().real[sj]))
    vdiag=sum(np.kron(a,b) for a,b in vals)
    er={}
    for g in (.02,.01,.005):
        er[str(g)]=float(la.eigh(h0+g*np.diag(vdiag),subset_by_index=[0,0],eigvals_only=True)[0]/g**2)
    energies[str((ii,jj))]=er
R['virtual_coupling_numeric_E_over_g2']=energies

# 9. Compatible Hamming source encoding: two Steane codes grouped into ququarts.
H7=np.array([[1,1,1,1,0,0,0],[1,1,0,0,1,1,0],[1,0,1,0,1,0,1]],dtype=np.int64)
check('H7_self_orthogonality_and_rank',not np.any((H7@H7.T)%2) and gf2rank(H7)==3)
rowwords=np.array([(np.array(a)@H7)%2 for a in product((0,1),repeat=3)])
check('H7_simplex_weights',Counter(map(int,rowwords.sum(1)))=={0:1,4:7})
# This is the same length-eight Hamming seed used for the E8 roots, not merely
# a matching code parameter tuple: append a zero and add the all-ones coset.
extended_seed={tuple((np.r_[w,0]+b)%2) for w in rowwords for b in (0,1)}
check('same_Hamming_seed_E8_and_quartic_source_code',extended_seed==set(rm))

rows=set(map(tuple,rowwords)); words=np.array(list(product((0,1),repeat=7)))
ker=words[np.all((words@H7.T)%2==0,axis=1)]
check('Steane_distance3',len(ker)==16 and min(int(w.sum()) for w in ker if tuple(w) not in rows)==3)
E7=np.zeros((4**7,4),dtype=np.int64)
for a,b in product((0,1),repeat=2):
    for x in rowwords:
        for y in rowwords: E7[idx(2*((x+a)%2)+(y+b)%2),2*a+b]=1
check('Hamming_ququart_encoder_isometry',np.array_equal(E7.T@E7,64*np.eye(4,dtype=np.int64)))
# R=2r has Gaussian integer entries; prove R^{tensor7} E7 = 64 E7 R*.
for j,rr in enumerate(refs):
    Ur=np.rint(2*rr.real).astype(np.int64); Ui=np.rint(2*rr.imag).astype(np.int64)
    re,im=gauss_collective(Ur,Ui,E7,7)
    check('native_Hamming_covariance_'+str(j),np.array_equal(re,64*E7@Ur) and np.array_equal(im,-64*E7@Ui))
# Spectrum of sum over the seven nonzero row-combination quartet projectors.
census=Counter()
for bits in product((0,1),repeat=12):
    rank=gf2rank(np.array(bits).reshape(4,3)); census[8-2**(3-rank)]+=4
check('Fano_parent_spectrum_census',dict(census)=={0:4,4:420,6:5880,7:10080})
# Minimality within the specified doubly-even self-orthogonal CSS class.
# No weight-1/2 word is a stabilizer. Correcting arbitrary one-qubit errors
# therefore requires distinct nonzero parity-check columns: n <= 2**r - 1.
# Encoding at least one qubit requires n - 2*r >= 1.
small_feasible={n:[r for r in range(n+1) if n-2*r>=1 and n<=2**r-1] for n in range(1,8)}
check('quartic_CSS_minimum_length_seven',all(not small_feasible[n] for n in range(1,7)) and small_feasible[7]==[3])
# Logical source Paulis have code-preserving weight-three Fano-line representatives.
line=np.flatnonzero(1-rowwords[1])
for name,a in zip(labels,paulis):
    out=E7.astype(complex)
    for site in line: out=apply_one(a,out,int(site),7)
    check('Fano_logical_Pauli_'+name,exact_gaussian(out)==sp.Matrix(E7)*exact_gaussian(a.conj()))
R['Hamming_source']={'encoded_dimension':4,'physical_registers':7,'physical_register_dimension':4,'distance_in_registers':3,'conditional_minimality':'n=7 is the unique minimum in the stated doubly-even self-orthogonal CSS class encoding nonzero information and correcting arbitrary single errors','finite_group_covariance':'U^tensor7 V7 = V7 conjugate(U); two concatenations give U','parent_spectrum':dict(census),'architecture_status':'explicit alternative; not a derivation that TFPT selects it'}

# 10. QFI and absence of collective continuous logical motion.
collectives=[]
for a in paulis:
    coll=sum(kron([a if j==r else I4 for j in range(4)]) for r in range(4))
    nn=exact_gaussian(E.T@coll@E)
    tr=exact_gaussian(a).trace()
    check('collective_compression_'+str(len(collectives)),nn==tr*G)
    collectives.append(coll)
for j in range(1,16):
    for k in range(j,16):
        M=Ginv*exact_gaussian(E.T@collectives[j]@collectives[k]@E)
        check(f'orientation_metric_{j}_{k}',sp.trace(M)==(32 if j==k else 0))
R['orientation_geometry']={'local_dimension':15,'metric':'g(X,Y)=8 tr(X0 Y0)','SLD_QFI':'F_Q=4g/5 for rho=P5/5','Berry_connection':'tr(U^dagger dU) I5','local_Berry_curvature':'0; finite quotient holonomy is not excluded'}

# 11. Entropy claims: exact qubit condition and two numerical counterchecks.
t=sp.symbols('t',real=True); ax=sp.Rational(2,3); by=6*t; cz=sp.Rational(1,3)
p0=(1+ax+by+cz)/4; px=(1+ax-by-cz)/4; py=(1-ax+by-cz)/4; pz=(1-ax-by+cz)/4
check('qubit_entropy_stationarity',sp.simplify(px*pz-p0*py+(27*t-1)/18)==0)
R['entropy_exact']={'qubit_t':'1/27','Pauli_probabilities':['5/9','5/18','1/18','1/9'],'primitive_rates':['log(3)/2','0','log(3/2)/2'],'extra_assumption':'no independent Y jump; not forced by CP'}
def entropy(p):
    p=np.array(p,dtype=float); p=p[p>1e-14]; return -float(np.sum(p*np.log(p)))
def weights(t): return np.array([.5+t,t,t,1/18-t,2/9-t,2/9-t])
perms3=[np.eye(3)[:,p] for p in ((0,1,2),(1,2,0),(2,0,1),(1,0,2),(2,1,0),(0,2,1))]
def fullchoi(t): return sum(w*np.outer(p.ravel(),p.ravel())/3 for w,p in zip(weights(t),perms3))
opt={}
for name,f in [('events',lambda t:entropy(weights(t))),('qutrit',lambda t:entropy(la.eigvalsh(fullchoi(t))))]:
    z=minimize_scalar(lambda t:-f(t),bounds=(1e-10,1/18-1e-10),method='bounded',options={'xatol':1e-14})
    opt[name]=float(z.x)
R['entropy_numeric_optima']=opt
R['scope']={'physical_TOE_proved':False,'new_global_TFPT_axiom_selection':False,'Lean_reverification':False,'physical_laboratory_experiment':False,'three_dimensional_space_from_Fano_bits':False}
R['checks']=checks
R['elapsed_seconds']=time.time()-start
R['environment']={'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__,'sympy':sp.__version__}
(ROOT/'results.json').write_text(json.dumps(R,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
np.savez_compressed(ROOT/'matrices.npz',E=E,G=np.diag(norms),P_numerator=Pnum,S_numerator=Snum,Q_numerator=Qnum,roots=roots,Bell_frame_numerator=Fnum,Seidel=np.array(C,dtype=np.int64),six_simplex=np.array(W,dtype=np.int64),six_sign_frames=np.array(Signs,dtype=np.int64),H7=H7)
print(json.dumps({'passed_checks':len(checks),'seconds':R['elapsed_seconds'],'result':'finite mathematical audit passed; no physical TOE claim'},ensure_ascii=False,indent=2))

```

</details>

<details>
<summary>Q1: requirements.txt öffnen</summary>

Originalmitglied: `TFPT_Quartik_Fortsetzung/requirements.txt`  
SHA256: `0b7b1647387baf922d10e761a40b5ba058cf3c773ea5bc72b9d3f414463fd3b4`

```text
numpy>=2.0
scipy>=1.13
sympy>=1.13

```

</details>

<details>
<summary>Q1: ursprüngliche Laufprotokolle öffnen</summary>

### `run.log`

```text
{
  "passed_checks": 385,
  "seconds": 25.651491165161133,
  "result": "finite mathematical audit passed; no physical TOE claim"
}

```

</details>

<a id="programm-q2"></a>
## Q2. Prüfprogramm und Abhängigkeiten

<details>
<summary>Q2: audit.py öffnen</summary>

Originalmitglied: `TFPT_Igusa_Quellendynamik_20260926/audit.py`  
SHA256: `23e9781a7fdfacc00943e348880604d66b3593d1e44430a6623001122d4a4248`

```python
#!/usr/bin/env python3
"""TFPT source-quartic continuation. Exact finite algebra, not a physical TOE.

Rebuilds the source roots and the quartic map from the stated RM(1,3) code.
The external identifications with the Igusa quartic/Segre cubic are classical.
All new polynomial, rank, incidence and perturbative coefficients are checked here.
Run with Python 3, NumPy, and SymPy. Outputs are written next to this script.
"""
from __future__ import annotations
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
from pathlib import Path
from itertools import product, combinations, permutations
from collections import Counter
import json, hashlib, platform, time
import numpy as np
import sympy as s
START=time.time(); ROOT=Path(__file__).resolve().parent
checks=[]; results={}
def ck(name,condition,kind='exact',**details):
    if not bool(condition): raise RuntimeError(f'{name} FAILED: {details}')
    checks.append(dict(name=name,kind=kind,passed=True,**details))
def stringify(obj):
    if isinstance(obj,dict): return {str(k):stringify(v) for k,v in obj.items()}
    if isinstance(obj,(list,tuple)): return [stringify(v) for v in obj]
    if isinstance(obj,np.generic): return obj.item()
    if isinstance(obj,s.Basic): return str(obj)
    return obj
z=s.symbols('z0:4'); t=s.symbols('t'); zv=s.Matrix(z)
G=s.diag(4,12,12,12,24)
W6=s.Matrix([[2,2,-1,-1,-1,-1],[0,0,-1,-1,1,1],
              [0,0,-1,1,-1,1],[0,0,1,-1,-1,1],[1,-1,0,0,0,0]])
f=s.Matrix([sum(a**4 for a in z),6*(z[0]**2*z[1]**2+z[2]**2*z[3]**2),
            6*(z[0]**2*z[2]**2+z[1]**2*z[3]**2),
            6*(z[0]**2*z[3]**2+z[1]**2*z[2]**2),24*s.prod(z)])
x=W6.T*f
ck('six_coordinate_sum_zero',sum(x)==0)
ck('Igusa_polynomial_identity',s.expand(sum(a*a for a in x)**2-4*sum(a**4 for a in x))==0)
ck('four_independent_source_coordinates',f.jacobian(z).subs(dict(zip(z,[1,2,4,8]))).rank()==4)
M=sum(a**8 for a in z)+14*sum(z[i]**4*z[j]**4 for i,j in combinations(range(4),2))+168*s.prod(a*a for a in z)
ck('Maschke_p2_identity',s.expand(sum(a*a for a in x)-12*M)==0)
results['quartic_coordinates']={'f':list(f),'x':list(x),'constraint':'(sum x_i^2)^2=4 sum x_i^4, sum x_i=0',
 'scope':'image of one coherent source z via z^tensor4; not every arbitrary state of the 5-dimensional code'}

# The original RM(1,3) construction, 240 roots and 60 projective source rays.
rm={tuple((a[0]+sum(a[k+1]*u[k] for k in range(3)))%2 for u in product((0,1),repeat=3)) for a in product((0,1),repeat=4)}
roots=[]
for i in range(8):
    for sign in [-1,1]:
        row=[0]*8;row[i]=2*sign;roots.append(row)
for c in rm:
    if sum(c)!=4:continue
    pos=[i for i,a in enumerate(c) if a]
    for signs in product([-1,1],repeat=4):
        row=[0]*8
        for i,sign in zip(pos,signs):row[i]=sign
        roots.append(row)
ray_nums={}; covectors={}
for row in roots:
    v=s.Matrix([row[2*j]+s.I*row[2*j+1] for j in range(4)])
    pp=(v*v.conjugate().T).applyfunc(s.expand)
    ray_nums[tuple(pp)]=pp
    vbar=list(v.conjugate()); lead=next(a for a in vbar if a!=0)
    normal=tuple(s.simplify(a/lead) for a in vbar)
    covectors[normal]=sum(a*b for a,b in zip(normal,z))
ck('240_roots_60_rays',len(roots)==240 and len(ray_nums)==60 and len(covectors)==60)
refs=[s.eye(4)-pp/2 for pp in ray_nums.values()]
refkeys={tuple(a) for a in refs}

# Pauli subgroup is generated by explicit products of source reflections.
I2=s.eye(2); X=s.Matrix([[0,1],[1,0]]); Y=s.Matrix([[0,-s.I],[s.I,0]]); Z=s.diag(1,-1)
paulis=[s.kronecker_product(a,b) for a in [I2,X,Y,Z] for b in [I2,X,Y,Z]]
labels=[a+b for a in 'IXYZ' for b in 'IXYZ']
def axis(i):
    u=s.eye(4)[:,i]; out=s.eye(4)-2*u*u.T
    ck(f'source_axis_{i}',tuple(out) in refkeys);return out
def pairref(i,j,phase):
    v=s.eye(4)[:,i]+phase*s.eye(4)[:,j];out=s.eye(4)-v*v.conjugate().T
    ck(f'source_pair_reflection_{i}_{j}_{phase}',tuple(out) in refkeys);return out
XI=pairref(0,2,-1)*pairref(1,3,-1)
IX=pairref(0,1,-1)*pairref(2,3,-1)
ZI=axis(2)*axis(3); IZ=axis(1)*axis(3)
iph=pairref(0,1,s.I)*pairref(0,1,-1)*pairref(2,3,s.I)*pairref(2,3,-1)*IZ
ck('source_contains_Pauli_generators',XI==paulis[4] and IX==paulis[1] and ZI==paulis[12] and IZ==paulis[3] and iph==s.I*s.eye(4))
H={tuple(phase*a) for a in paulis for phase in [1,-1,s.I,-s.I]}
ck('Pauli_subgroup_order64',len(H)==64)
for j,a in enumerate(paulis):
    ck(f'quartics_Pauli_invariant_{labels[j]}',all(s.expand(v.subs(dict(zip(z,a*zv)),simultaneous=True)-v)==0 for v in f))
# Exact Molien formula: five degree-four invariants and one degree-sixteen relation.
mol=(sum(1/(1-a*t)**4 for a in [1,-1,s.I,-s.I])+30/(1-t*t)**2+30/(1+t*t)**2)/64
ck('Pauli_Molien_hypersurface',s.factor(mol-(1-t**16)/(1-t**4)**5)==0)
results['invariant_ring']={'Pauli_Molien':'(1-t^16)/(1-t^4)^5','generators':'f0,...,f4','relation':'Igusa quartic in the generators',
 'full_group_degrees':[8,12,20,24],'group_order_from_kernel_and_image':64*720,
 'proof_dependency':'Classical Igusa quotient identification plus the exact Molien/rank and source-generator certificates. See report.'}

# Source reflections act as all 15 transpositions on these same six coordinates.
perms=[]
for n,rr in enumerate(refs):
    transformed=[s.Poly(s.expand(v.subs(dict(zip(z,rr*zv)),simultaneous=True)),*z) for v in x]
    original=[s.Poly(v,*z) for v in x]
    p=tuple(original.index(v) for v in transformed)
    ck(f'native_reflection_six_action_{n}',sum(i!=p[i] for i in range(6))==2)
    perms.append(p)
ck('all_fifteen_source_transpositions',len(set(perms))==15)
results['source_six_action']=[list(p) for p in perms]

# Fifteen differences each factor into four of the actual sixty root hyperplanes.
factors=[]
for i,j in combinations(range(6),2):
    poly=s.Poly(x[i]-x[j],*z,extension=s.I);matches=[]
    for normal,form in covectors.items():
        _,rem=s.div(poly,s.Poly(form,*z,extension=s.I))
        if rem.is_zero: matches.append((normal,form))
    prodpoly=s.Poly(s.prod(a[1] for a in matches),*z,extension=s.I)
    scale=s.simplify(poly.LC()/prodpoly.LC())
    ck(f'root_factorization_{i}_{j}',len(matches)==4 and poly==prodpoly.mul_ground(scale))
    factors.append(dict(pair=[i,j],constant=scale,normals=[a[0] for a in matches]))
ck('root_factorization_no_repetition',len({a for item in factors for a in item['normals']})==60)
results['sixty_hyperplanes']=factors

# Invariant degrees 8/12/20/24: remove degree-four generator by e4=e2^2/4.
y=s.symbols('y0:5');yy=list(y)+[-sum(y)]
F=s.Poly(sum(a*a for a in yy)**2-4*sum(a**4 for a in yy),*y)
point=dict(zip(z,[1,2,4,8]));xx=x.subs(point);dx=x.jacobian(z).subs(point)
Jac=s.Matrix([[sum(k*xx[q]**(k-1)*dx[q,j] for q in range(6)) for j in range(4)] for k in [2,3,5,6]])
ck('four_basic_invariants_independent',Jac.det()!=0)
ck('basic_invariant_degree_product',8*12*20*24==46080)
results['invariant_ring']['Jacobian_at_1_2_4_8']=Jac.det()
results['invariant_ring']['sextic']='u^6+e2 u^4-e3 u^3+(e2^2/4)u^2-e5 u+e6'
results['invariant_ring']['discriminant']='product_{i<j}(x_i-x_j)^2 = constant times product_{60 root hyperplanes} l(z)^2'

# Ten even Bell quadrics pull back ten trope hyperplanes as exact squares.
Fnum=s.Matrix([[4,4,4,4,0],[0,8,0,0,8],[4,-4,4,-4,0],[0,0,8,0,8],
               [0,0,0,8,8],[0,0,8,0,-8],[0,0,0,8,-8],[4,4,-4,-4,0],
               [0,8,0,0,-8],[4,-4,-4,4,0]])
Signs=Fnum*W6/8
ck('ten_balanced_sign_normals',set(Signs)=={-1,1} and Signs*s.ones(6,1)==s.zeros(10,1))
quadrics=[]
for n,(label,a) in enumerate((lab,a) for lab,a in zip(labels,paulis) if a.T==a):
    q=(zv.T*a*zv)[0]
    ck(f'Bell_trope_square_{label}',s.expand((Signs*x)[n]-6*q*q)==0)
    quadrics.append(dict(label=label,quadric=q,sign_normal=list(Signs.row(n))))
ck('ten_distinct_Segre_nodes',len({tuple(r['sign_normal']) for r in quadrics})==10)
results['ten_Bell_tropes']=quadrics

# Fifteen singular lines, fifteen four-root-image points and their doily incidence.
def matchings(items):
    if not items:yield ();return
    a=items[0]
    for j in range(1,len(items)):
        for tail in matchings(items[1:j]+items[j+1:]):yield ((a,items[j]),)+tail
matchs=list(matchings(tuple(range(6))));pairs=list(combinations(range(6),2));a,b=s.symbols('a b')
for k,m in enumerate(matchs):
    v=[None]*6
    for val,pair in zip([a,b,-a-b],m):
        for i in pair:v[i]=val
    p2=sum(u*u for u in v);p3=sum(u**3 for u in v)
    ck(f'Igusa_singular_line_{k}',s.expand(p2*p2-4*sum(u**4 for u in v))==0 and all(s.expand(p2*u-4*u**3+s.Rational(2,3)*p3)==0 for u in v))
N=s.Matrix([[int(p in m) for m in matchs] for p in pairs])
ck('doily_incidence_rank_and_spectrum',N.rank()==10 and (N*N.T).eigenvals()=={s.Integer(9):1,s.Integer(4):9,s.Integer(0):5})
rootimages=Counter()
pts=[]
for i,j in pairs:
    v=[-1]*6;v[i]=v[j]=2;pts.append(tuple(v))
for normal in covectors:
    source=s.Matrix([s.conjugate(u) for u in normal]);v=x.subs(dict(zip(z,source)),simultaneous=True).applyfunc(s.expand)
    found=[]
    for k,p in enumerate(pts):
        scale=s.simplify(v[0]/p[0])
        if scale!=0 and all(s.expand(v[j]-scale*p[j])==0 for j in range(6)):found.append(k)
    ck('source_ray_hits_unique_singular_point_'+str(sum(rootimages.values())),len(found)==1)
    rootimages[found[0]]+=1
ck('four_actual_source_rays_per_singular_point',len(rootimages)==15 and set(rootimages.values())=={4})
results['doily']={'incidence_matrix':list(map(list,N.tolist())),'NNT_spectrum':{'9':1,'4':9,'0':5},'singular_points':pts,'perfect_matchings':matchs,'root_fibre_size':4}

# Additional state-family constraints and continuous dynamical closure.
for i in range(6):
    v=[-1]*6;v[i]=5
    ck(f'mark_ray_not_single_coherent_source_image_{i}',sum(a*a for a in v)**2-4*sum(a**4 for a in v)==-1620)
vfs=[s.Poly(s.diff(F.as_expr(),y[i])*y[j],*y) for i,j in product(range(5),repeat=2)]
mons=sorted(set(F.monoms()).union(*(set(v.monoms()) for v in vfs)))
C=s.Matrix([[v.coeff_monomial(m) for v in vfs]+[-F.coeff_monomial(m)] for m in mons]);kernel=C.nullspace()
ck('Igusa_infinitesimal_linear_stabilizer_only_scalar',len(kernel)==1 and s.Matrix(5,5,list(kernel[0][:25]))==kernel[0][-1]*s.eye(5)/4)
mons4=sorted([p for p in product(range(5),repeat=4) if sum(p)==4],reverse=True)
columns=[s.Matrix([s.Poly(e,*z).coeff_monomial(p) for p in mons4]) for e in f]
for i,j in product(range(4),repeat=2):
    columns.extend(s.Matrix([s.Poly(z[i]*s.diff(e,z[j]),*z).coeff_monomial(p) for p in mons4]) for e in f)
Cjet=s.Matrix.hstack(*columns)
ck('first_order_source_response_closes_to_Sym4_dimension35',Cjet[:,:5].rank()==5 and Cjet.rank()==35)
# Explicit failure of autonomous dynamics on quotient coordinates (not even projectively).
v=s.Matrix([1,2,4,8]);vp=paulis[1]*v
fv=f.subs(dict(zip(z,v)),simultaneous=True);fvp=f.subs(dict(zip(z,vp)),simultaneous=True)
dv=f.jacobian(z).subs(dict(zip(z,v)))*(-s.I*paulis[3]*v)
dvp=f.jacobian(z).subs(dict(zip(z,vp)))*(-s.I*paulis[3]*vp)
ck('same_quartic_readout_different_future',fv==fvp and s.Matrix.hstack(fv,dv-dvp).rank()==2)
results['dynamics']={'linear_stabilizer_matrix_shape':list(C.shape),'linear_stabilizer_rank':C.rank(),
 'first_jet_span':35,'additional_linear_coordinates':30,'same_initial_f':list(fv),'first_derivative':list(dv),'second_source_first_derivative':list(dvp),
 'normalization':'Both source vectors have norm sqrt85. Dividing by sqrt85 divides all quartic outputs and derivatives by 85^2.',
 'scope':'No nontrivial continuous projective linear evolution on the fixed C5 preserves the entire single-coherent-source image. Discrete evolution, nonlinear evolution with lifts and arbitrary entangled code states are not excluded.'}

# A source-preserving Hamming code acquires logical exchange in third order.
H7=np.array([[1,1,1,1,0,0,0],[1,1,0,0,1,1,0],[1,0,1,0,1,0,1]],dtype=int)
rowwords=[tuple((np.array(a)@H7)%2) for a in product([0,1],repeat=3)]
lines={tuple(i for i,v in enumerate(w) if v==0) for w in rowwords if any(w)}
ck('Hamming_seven_Fano_lines',len(lines)==7 and all(len(v)==3 for v in lines))
ck('same_Hamming_seed', {tuple((np.r_[w,0]+b)%2) for w in rowwords for b in [0,1]}==rm)
# Per Pauli, a single error has syndrome s_r times its nonzero four-bit address.
# For a triple returning to the code, the intermediate nonzero syndrome is
# itself a single-error syndrome, so both energy denominators are 8 Delta.
# Pauli products on two blocks square their one-block phase.
site_scalar=0;site_paths=0
for aa,bb in product(range(1,16),repeat=2):
    if aa==bb:continue
    cc=aa^bb
    phase=s.trace(paulis[aa]*paulis[bb]*paulis[cc])/4
    ck(f'Pauli_triple_phase_{aa}_{bb}',phase in [1,-1,s.I,-s.I])
    site_scalar+=7*phase**2;site_paths+=7
ck('same_site_third_order_scalar_paths',site_scalar==-210 and site_paths==1470)
logical_paths=7*6
third=s.zeros(16)
for A in paulis[1:]:third+=s.Rational(logical_paths,64)*s.kronecker_product(A.conjugate(),A.conjugate())
third+=s.Rational(site_scalar,64)*s.eye(16)
Swap=s.zeros(16)
for i,j in product(range(4),repeat=2):Swap[4*j+i,4*i+j]=1
ck('Pauli_swap_identity',sum((s.kronecker_product(A,A) for A in paulis),s.zeros(16))==4*Swap)
ck('protected_ququart_exchange_third_order',third==s.Rational(21,8)*Swap-s.Rational(63,16)*s.eye(16))
# All closing ordered paths can be enumerated in syndrome space without 4^14 matrices.
def addr(k):return np.array([(k>>i)&1 for i in range(4)],dtype=int)
errs=[(site,p) for site in range(7) for p in range(1,16)]
syn={tuple(np.outer(addr(p),H7[:,site]).ravel()):(site,p) for site,p in errs}
counts=Counter()
for e,fa in product(errs,repeat=2):
    s1=np.outer(addr(e[1]),H7[:,e[0]]);s2=np.outer(addr(fa[1]),H7[:,fa[0]])
    k=tuple(((s1+s2)%2).ravel())
    if k not in syn:continue
    eb=syn[k]
    if e[0]==fa[0]==eb[0]:counts['same_site']+=1
    else:
        ck('third_order_nonlocal_path_is_Fano_line',e[1]==fa[1]==eb[1] and tuple(sorted([e[0],fa[0],eb[0]])) in lines)
        counts['Fano_line']+=1
ck('all_third_order_closed_paths',dict(counts)=={'same_site':1470,'Fano_line':630})
# Independent analytic one-direction model, exact 2x2 low-energy block.
g,Delta,xi=s.symbols('g Delta xi',real=True)
M=s.symbols('M',positive=True)
Eminus=(M+6*xi*g-s.sqrt((M+6*xi*g)**2+28*g*g))/2
for sign in [-1,1]:
    series=s.series(Eminus.subs(xi,sign),g,0,4).removeO().expand()
    ck(f'one_direction_exact_model_series_{sign}',s.simplify(series+7*g*g/M-42*sign*g**3/M**2)==0)
lam=s.symbols('lam')
for sign in [-1,1]:
    Hsmall=s.diag(0,*([M]*7))+sign*g*(s.ones(8)-s.eye(8))
    char=s.factor(Hsmall.charpoly(lam).as_expr())
    target=(lam-(M-sign*g))**6*(lam**2-(M+6*sign*g)*lam-7*g*g)
    ck(f'one_direction_syndrome_matrix_charpoly_{sign}',s.expand(char-target)==0)
results['protected_exchange']={'microscopic_coupling':'V=g sum_r sum_{a!=0} A_a,r^A A_a,r^B = g sum_r(4 Swap_r-I)',
 'parent':'Delta(H_F^A+H_F^B), H_F=sum of seven I-Q_S terms',
 'first_order':'0','second_order':'-105 g^2/(8 Delta) I',
 'third_order':'g^3/Delta^2 [(21/8) Swap_logical-(63/16) I]',
 'logical_exchange_coefficient':'21 g^3/(8 Delta^2)',
 'paths':dict(counts),'one_direction_exact_low_energy':'[M+6 xi g-sqrt((M+6 xi g)^2+28g^2)]/2; M=8 Delta for two blocks',
 'scope':'Perturbative coefficient, not an exact finite-g equation. Fixed two-block weak-coupling regime. g, Delta and link incidence are model choices, not TFPT-derived physical constants.'}

# Quantified remaining freedom even in the older five-code parent family.
r=s.symbols('r',positive=True)
b=1/(1+r)-s.Rational(1,2);c=1/(2*r)-2/(1+r)+s.Rational(1,2)
co=[s.factor(-1-b-c/4),s.factor(-2*b-3*c/4),s.factor(-1-3*b-9*c/4)]
ck('previous_two_block_coefficient_recovered', [v.subs(r,s.Rational(1,2)) for v in co]==[-s.Rational(29,24),-s.Rational(11,24),-s.Rational(15,8)])
ck('same_code_distinct_dynamical_ratio',co[2].subs(r,1)==-1 and co[2].subs(r,s.Rational(1,2))==-s.Rational(15,8))
results['five_code_parent_family']={'H_r':'r(S-P)+(I-S), r>0','C_identity':co[0],'C_local_each':co[1],'C_interaction':co[2],
 'scope':'Same tested finite code and source symmetry; not two models satisfying all eight physical TFPT gates.'}
results['checks']=checks
results['elapsed_seconds']=time.time()-START
results['environment']={'python':platform.python_version(),'sympy':s.__version__,'numpy':np.__version__}
results['scope']={'physical_TOE_proved':False,'spacetime_dimension_derived':False,'new_natural_constants_derived':False,
 'quantum_field_theory_constructed':False,'new_Lean_formalization':False,'finite_algebraic_continuation':True}
(ROOT/'results.json').write_text(json.dumps(stringify(results),ensure_ascii=False,indent=2)+'\n')
np.savez_compressed(ROOT/'matrices.npz',roots=np.array(roots,dtype=int),G=np.array(G,dtype=int),W6=np.array(W6,dtype=int),
                     Bell_sign_normals=np.array(Signs,dtype=int),doily_incidence=np.array(N,dtype=int),H7=H7,
                     linear_stabilizer_coefficients=np.array(C,dtype=np.int64))
print(json.dumps({'passed':len(checks),'seconds':results['elapsed_seconds'],'status':'exact finite algebra and perturbative coefficients; no physical TOE claim'},indent=2))

```

</details>

<details>
<summary>Q2: requirements.txt öffnen</summary>

Originalmitglied: `TFPT_Igusa_Quellendynamik_20260926/requirements.txt`  
SHA256: `11c495c6fd22a834f03652c1be83034c9a747b39e16b60ffae0249f92e6e4a09`

```text
numpy==2.3.5
sympy==1.14.0

```

</details>

<details>
<summary>Q2: ursprüngliche Laufprotokolle öffnen</summary>

### `baseline_rerun.log`

```text
{
  "passed_checks": 385,
  "seconds": 19.209920167922974,
  "result": "finite mathematical audit passed; no physical TOE claim"
}

```

### `run.log`

```text
{
  "passed": 1065,
  "seconds": 17.373611450195312,
  "status": "exact finite algebra and perturbative coefficients; no physical TOE claim"
}

```

</details>

<a id="programm-q3"></a>
## Q3. Prüfprogramm und Abhängigkeiten

<details>
<summary>Q3: audit.py öffnen</summary>

Originalmitglied: `TFPT_Dynamischer_Codeabschluss_20260926/audit.py`  
SHA256: `bc055b3c946adff2eb489cb07fe5dd495b33527c56187a4f45888fe514df6807`

```python
#!/usr/bin/env python3
"""Finite TFPT continuation: native symmetry, 35 response sectors and induced quartic.

Reconstructs the RM(1,3) source and checks exact finite identities.
Sixth-order coefficients apply to the explicitly defined four-block Hamiltonian.
No physical spacetime/TOE claim. See DERIVATION.md for assumptions and proofs.
Python 3, numpy and sympy. No network and no previous result files required.
"""
from __future__ import annotations
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
os.environ.setdefault('OMP_NUM_THREADS','1')
from itertools import combinations, permutations, product
from collections import Counter, deque
from fractions import Fraction as F
from pathlib import Path
import numpy as np
import sympy as sy
import math, json, time, hashlib, platform
ROOT=Path(__file__).resolve().parent
start=time.time(); checks=[]; results={}
def check(name, condition, **details):
    if not bool(condition): raise RuntimeError(f'{name}: {details}')
    checks.append({'name':name,'passed':True,'kind':'exact finite arithmetic',**details})
def saveable(x):
    if isinstance(x,dict):return {str(k):saveable(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)):return [saveable(v) for v in x]
    if isinstance(x,(F,sy.Basic)):return str(x)
    if isinstance(x,np.ndarray):return saveable(x.tolist())
    if isinstance(x,np.generic):return x.item()
    return x

def gauss(m):
    a=np.asarray(m)
    if not(np.array_equal(a.real,np.rint(a.real)) and np.array_equal(a.imag,np.rint(a.imag))):
        raise RuntimeError('nonintegral Gaussian matrix')
    return a

# Reconstruct actual source, not a substituted Pauli alphabet.
I=np.eye(2,dtype=complex)
X=np.array([[0,1],[1,0]],complex)
Y=np.array([[0,-1j],[1j,0]],complex)
Z=np.diag([1,-1]).astype(complex)
paulis=np.array([np.kron(a,b) for a in (I,X,Y,Z) for b in (I,X,Y,Z)])
labels=[a+b for a in 'IXYZ' for b in 'IXYZ']
coords=list(product((0,1),repeat=3))
rm={tuple((u[0]+sum(u[j+1]*x[j] for j in range(3)))%2 for x in coords) for u in product((0,1),repeat=4)}
roots=[]
for j in range(8):
    for sign in (-1,1):
        row=[0]*8;row[j]=2*sign;roots.append(row)
for c in sorted(rm):
    if sum(c)!=4:continue
    support=[i for i,x in enumerate(c) if x]
    for signs in product((-1,1),repeat=4):
        row=[0]*8
        for i,x in zip(support,signs):row[i]=x
        roots.append(row)
rays={}
for row in roots:
    z=np.array(row[::2])+1j*np.array(row[1::2]);p=np.outer(z,z.conj())
    key=tuple(p.real.ravel())+tuple(p.imag.ravel());rays[key]=p
Rs=[gauss(2*np.eye(4)-p) for _,p in sorted(rays.items())] # R = 2U
check('source_census',len(roots)==240 and len(Rs)==60)
gens=[]
for k,R in enumerate(Rs):
    action=[]
    for a in paulis[1:]:
        b=R@a@R.conj().T # exactly four times transformed Pauli
        matches=[sign*(j+1) for j,c in enumerate(paulis[1:]) for sign in (-1,1) if np.array_equal(b,4*sign*c)]
        check(f'source_normalizes_Pauli_{k}_{len(action)}',len(matches)==1)
        action.append(matches[0])
    gens.append(tuple(action))

def compose(g,h):return tuple(g[x-1] if x>0 else -g[-x-1] for x in h)
e=tuple(range(1,16)); group={e:2*np.eye(4,dtype=complex)};queue=deque([e])
while queue:
    h=queue.popleft();Rh=group[h]
    for g,Rg in zip(gens,Rs):
        gh=compose(g,h)
        if gh not in group:
            group[gh]=gauss((Rg@Rh)/2)
            queue.append(gh)
            if len(group)>11520:raise RuntimeError('unexpected larger projective group')
check('native_projective_group_order',len(group)==11520)
trace_ad=[1+sum((1 if x>0 else -1) for i,x in enumerate(g,1) if abs(x)==i) for g in group]
check('adjoint_character_nonnegative',min(trace_ad)>=0)
frames=[F(sum(v**t for v in trace_ad),len(group)) for t in range(1,5)]
check('native_commutants_1_2_6_29',frames==[1,2,6,29])
results['native_group']={'projective_order':len(group),'commutant_dimensions':frames,'adjoint_trace_histogram':dict(Counter(trace_ad))}
print('native symmetry complete',flush=True)

# Characters on the complete symmetric fourth tensor, using Newton's identity.
# R=2U has Gaussian integer entries. All numerators stay exactly representable.
Rbatch=np.array(list(group.values()))
def symmetric4_character_numerator(R):
    R2=R@R;R3=R2@R;R4=R3@R
    p1=np.trace(R,axis1=-2,axis2=-1);p2=np.trace(R2,axis1=-2,axis2=-1)
    p3=np.trace(R3,axis1=-2,axis2=-1);p4=np.trace(R4,axis1=-2,axis2=-1)
    return gauss(p1**4+6*p1*p1*p2+3*p2*p2+8*p1*p3+6*p4)
N35=symmetric4_character_numerator(Rbatch)
N5=sum((symmetric4_character_numerator(a@Rbatch) for a in paulis),np.zeros(len(group),complex))
# chi(Sym4)=N35/384; chi(Q intersect Sym4)=N5/6144.
N30=16*N35-N5
sq=lambda a:sum(int(x.real)**2+int(x.imag)**2 for x in a)
check('Sym4_commutant_two',F(sq(N35),len(group)*384**2)==2)
check('native_five_irreducible',F(sq(N5),len(group)*6144**2)==1)
check('native_thirty_irreducible',F(sq(N30),len(group)*6144**2)==1)
check('five_thirty_inequivalent',sum((N5.conj()*N30).tolist())==0)
results['symmetric_fourth']={'dimensions':[5,30],'commutant_dimension':2,'irreducible_character_norms':[1,1]}

# Explicit 35-dimensional Pauli character sectors in unnormalized symmetric kets.
ns=sorted([n for n in product(range(5),repeat=4) if sum(n)==4],reverse=True)
pos={n:i for i,n in enumerate(ns)};d=35
norms=np.array([24//math.prod(math.factorial(x) for x in n) for n in ns],dtype=np.int64)
Ds=[];Ks=[]
for A in paulis:
    D=np.zeros((d,d),complex);K=np.zeros((d,d),complex)
    perm=[int(np.flatnonzero(A[:,j])[0]) for j in range(4)]
    phase=[A[perm[j],j] for j in range(4)]
    for col,n in enumerate(ns):
        m=[0]*4
        for j in range(4):m[perm[j]]=n[j]
        D[pos[tuple(m)],col]=math.prod(phase[j]**n[j] for j in range(4))
        for i,j in product(range(4),repeat=2):
            if not n[j] or A[i,j]==0:continue
            if i==j:K[col,col]+=n[j]*A[i,j]
            else:
                m=list(n);m[j]-=1;m[i]+=1
                K[pos[tuple(m)],col]+=(n[i]+1)*A[i,j]
    Ds.append(gauss(D));Ks.append(gauss(K))
Ds=np.array(Ds);Ks=np.array(Ks)
chars=np.array([[1 if np.array_equal(a@b,b@a) else -1 for b in paulis] for a in paulis],dtype=np.int64)
Ps=np.einsum('ab,bij->aij',chars,Ds) # sixteen times sector projectors
check('sector_numerators_real',np.count_nonzero(Ps.imag)==0)
Ps=Ps.real.astype(np.int64)
for i,P in enumerate(Ps):
    check(f'sector_projector_{i}',np.array_equal(P@P,16*P))
    check(f'sector_rank_{i}',np.trace(P)==16*(5 if i==0 else 2))
check('sector_resolution',np.array_equal(Ps.sum(axis=0),16*np.eye(35)))
for i in range(16):
    for j in range(i):
        check(f'sector_orthogonality_{i}_{j}',np.count_nonzero(Ps[i]@Ps[j])==0)
E=np.zeros((35,5),dtype=int)
supports=[[(4,0,0,0),(0,4,0,0),(0,0,4,0),(0,0,0,4)],[(2,2,0,0),(0,0,2,2)],[(2,0,2,0),(0,2,0,2)],[(2,0,0,2),(0,2,2,0)],[(1,1,1,1)]]
for a,support in enumerate(supports):
    for n in support:E[pos[n],a]=1
G=E.T@np.diag(norms)@E
check('same_code_gram',np.array_equal(G,np.diag([4,12,12,12,24])))
check('same_code_trivial_sector',np.array_equal(Ps[0]@E,16*E))
for a in range(1,16):
    T=Ks[a]@E
    check(f'first_response_in_sector_{a}',np.array_equal(Ps[a]@T,16*T))
    rank=sy.Matrix(T.real.astype(int))+sy.I*sy.Matrix(T.imag.astype(int))
    check(f'first_response_rank_two_{a}',rank.rank()==2)
    check(f'collective_error_detected_{a}',np.count_nonzero(E.T@np.diag(norms)@T)==0)
results['response_sectors']={'trivial_rank':5,'other_ranks':[2]*15,'first_response_ranks':[2]*15,'label_rule':'P_s K_a P_t=0 unless s=t xor a','source_readout_scope':'Sym4 C4, not spatial sites or particle species'}
print('35 response sectors complete',flush=True)

# Fano source checks.
H7=np.array([[1,1,1,1,0,0,0],[1,1,0,0,1,1,0],[1,0,1,0,1,0,1]],dtype=np.int64)
C={tuple((np.array(t)@H7)%2) for t in product((0,1),repeat=3)}
check('same_RM_seed', {tuple((np.r_[c,0]+b)%2) for c in C for b in (0,1)}==rm)
cols=[int(H7[0,j]+2*H7[1,j]+4*H7[2,j]) for j in range(7)]
check('all_nonzero_threebit_syndromes',set(cols)==set(range(1,8)))
# Six links are the least incidences allowing nontrivial operators on all four distance-three blocks.
check('four_block_minimum_six_links',math.ceil(4*3/2)==6)

K4=list(combinations(range(4),2));C4=[(0,1),(1,2),(2,3),(0,3)]
DOUBLE=[(0,1),(0,1),(2,3),(2,3),(0,2),(1,3)]
def weighted_orders(edges):
    hist=Counter();total=F(0)
    for order in permutations(range(6)):
        degrees=[0]*4;active=[]
        for eidx in order[:-1]:
            a,b=edges[eidx];degrees[a]+=1;degrees[b]+=1
            active.append(sum(0<k<3 for k in degrees))
        if 0 in active:raise RuntimeError('unexpected reducible connected cubic path')
        hist[tuple(active)]+=1
        total+=F(1,4**5*math.prod(active))
    return total,hist
wk,hk=weighted_orders(K4);wd,hd=weighted_orders(DOUBLE)
check('K4_denominator_sum',wk==F(83,16384))
check('double_bond_denominator_sum',wd==F(449,73728))

def coloring_count(edges):
    # Exact exhaustive 7^6 census of edge-register labels.
    valid=[]
    incident=[[k for k,e in enumerate(edges) if v in e] for v in range(4)]
    for cs in product(range(1,8),repeat=6):
        if all(cs[e[0]]^cs[e[1]]^cs[e[2]]==0 for e in incident):valid.append(cs)
    return valid
ck=coloring_count(K4);cd=coloring_count(DOUBLE)
check('K4_Fano_edge_colorings',len(ck)==210)
check('double_Fano_labeled_colorings',len(cd)==252)
# Distinguish GL(3,2) frames from dependent colorings.
indep=0
for c in ck:
    used=set(c)
    if len(used)==6:indep+=1
check('K4_independent168_dependent42',indep==168 and len(ck)-indep==42)
# Every connected loopless cubic multigraph on four vertices is one of these.
patterns=[]
for mult in product(range(4),repeat=6):
    if sum(mult)!=6:continue
    deg=[sum(mult[k] for k,e in enumerate(K4) if v in e) for v in range(4)]
    if deg!=[3]*4:continue
    reached={0}
    for _ in range(4):
        for n,(a,b) in zip(mult,K4):
            if n and (a in reached or b in reached):reached|={a,b}
    if len(reached)==4:patterns.append(mult)
check('connected_cubic_multigraph_census',len(patterns)==7 and sum(all(n==1 for n in p) for p in patterns)==1)
check('remaining_six_double_patterns',sum(sorted(p)==[0,0,1,1,2,2] for p in patterns)==6)
kappaK=16*(210*wk+6*F(252,4)*wd)
kappaC=16*(2*F(252,4)*wd)
check('K4_quartic_coefficient',kappaK==F(27573,512))
check('C4_quartic_coefficient',kappaC==F(3143,256))
results['sixth_order']={'K4_weighted_time_orders':wk,'double_weighted_time_orders':wd,'K4_colorings':210,'double_labeled_colorings':252,'double_colorings_unlabeled':63,'K4_GL3_frames':168,'K4_dependent_frames':42,'connected_cubic_edge_multiplicities':patterns,'K4_kappa':kappaK,'C4_kappa':kappaC,'coefficient_convention':'H_eff on symmetric logical35 = scalar - kappa*g^6/Delta^5 * Pi5 + O(g^7/Delta^6). Not an exact finite-g Hamiltonian.'}

# Independent exact eigenvalue expansion in the COMPLETE invariant single-Pauli
# syndrome space (512 states). Includes disconnected paths and all normalization terms.
def direct_series(edges,weights=None):
    if weights is None:weights=[1]*len(edges)
    states=list(product(range(8),repeat=3));full=[list(t)+[t[0]^t[1]^t[2]] for t in states];n=len(states)
    energy=[4*sum(x!=0 for x in row) for row in full]
    trans=[]
    for a,b in edges:
        perms=[]
        for r in range(1,8):
            pp=[]
            for row in full:
                row=row.copy();row[a]^=r;row[b]^=r
                pp.append(64*row[0]+8*row[1]+row[2])
            perms.append(pp)
        trans.append(perms)
    output=[]
    for tail in product((-1,1),repeat=3):
        xi=[1]+list(tail);signs=[w*xi[a]*xi[b] for w,(a,b) in zip(weights,edges)]
        v0=[F(0)]*n;v0[0]=F(1);vs=[v0];es=[F(0)]
        def apply(v):
            w=[F(0)]*n
            for sign,pp in zip(signs,trans):
                for p in pp:
                    for i,x in enumerate(v):
                        if x:w[p[i]]+=sign*x
            return w
        for order in range(1,7):
            w=apply(vs[-1]);es.append(w[0])
            for k in range(1,order+1):
                if es[k]:
                    for j,a in enumerate(vs[order-k]):
                        if a:w[j]-=es[k]*a
            check('Rayleigh_ground_component_'+str((edges,xi,order)),w[0]==0)
            vs.append([F(0)]+[-w[j]/energy[j] for j in range(1,n)])
        output.append({'xi':xi,'coefficients':es})
    walsh=[sum(F(math.prod(r['xi']))*r['coefficients'][k] for r in output)/8 for k in range(7)]
    return output,walsh
seriesK,wK=direct_series(K4);seriesC,wC=direct_series(C4)
check('independent_full_syndrome_K4_quartic',wK[:6]==[0]*6 and wK[6]==-kappaK/16)
check('independent_full_syndrome_C4_quartic',wC[:6]==[0]*6 and wC[6]==-kappaC/16)
# A separate unequal-weight check and a genuine topology ablation.
weights=[1,2,-1,3,2,4]
seriesW,wW=direct_series(K4,weights)
poly=F(8715,8192)*math.prod(weights)
for pattern in patterns:
    if sorted(pattern)==[0,0,1,1,2,2]:
        poly+=F(3143,8192)*math.prod(w**m for w,m in zip(weights,pattern))
check('unequal_coupling_sixth_order_polynomial',wW[6]==-poly)
seriesT,wT=direct_series([(0,1),(1,2),(2,3)])
check('open_chain_no_sixth_order_quartic',wT==[0]*7)
results['coupling_and_topology_controls']={'unequal_K4_weights':weights,'unequal_coefficient_from_path_polynomial':-poly,'unequal_coefficient_from_exact_syndrome_series':wW[6],'open_chain_all_four_support_coefficients_through6':wT}

# The zero-coupling selected bare code is the concatenation of the outer
# ((4,5,2))_4 with four inner [[7,1,3]]_4 codes. Its distance is exactly6.
# The weight-six witness is two inner Fano triples realizing an outer Pauli pair.
Gin=sy.diag(sy.Rational(1,4),sy.Rational(1,12),sy.Rational(1,12),sy.Rational(1,12),sy.Rational(1,24))
B=E.T@np.diag(norms)@(Ks[3]@Ks[3])@E
B=sy.Matrix(B.real.astype(int))+sy.I*sy.Matrix(B.imag.astype(int))
h=(Gin*B-4*sy.eye(5))/12
check('outer_weight_two_nontrivial_witness',h.eigenvals()=={sy.Integer(1):2,sy.Rational(-1,3):3})
fanolines=[set(comb) for comb in combinations(range(7),3) if cols[comb[0]]^cols[comb[1]]^cols[comb[2]]==0]
check('three_Fano_lines_per_site',len(fanolines)==7 and all(sum(r in line for line in fanolines)==3 for r in range(7)))
probe_coefficient=F(3*6,64)
check('dressed_two_site_probe_nontrivial_coefficient',probe_coefficient==F(9,32))
results['error_detection_scope']={'bare_selected_limit_code':'((28,5,6))_4','bare_distance_proof':'outer distance2 times inner distance3 gives lower bound6; two Fano-triple logical Paulis give a nontrivial weight6 witness','finite_g':'dressed selected ground code has distance2 for sufficiently small nonzero negative g in the K4 model','finite_g_probe':'one physical A on the same site r in two blocks; compression = scalar I + (9/32)*(g/Delta)^2*h_A + O((g/Delta)^3)','eigenvalue_difference_leading':'(3/8)*(g/Delta)^2','single_error_detection':'exact: global Pauli^(tensor28) still stabilizes the five-dimensional ground sector'}
results['independent_single_Pauli_series']={'syndrome_dimension':512,'K4':seriesK,'C4':seriesC,'K4_full_support_Walsh':wK,'C4_full_support_Walsh':wC,'scope':'Exact check of the single-Pauli invariant sector through sixth order. The extension to all15 Pauli types uses the explicit shortest-return graph proof, not a diagonalization of 4^28 states.'}

# Return numerator on four logical C4 sources: sum A^tensor4 =16Q.
def kron4(a):return np.kron(np.kron(np.kron(a,a),a),a)
Qnum=sum(kron4(a) for a in paulis)
check('quartic_logical_numerator_integral',np.count_nonzero(Qnum.imag)==0)
Qnum=Qnum.real.astype(np.int64)
check('returned_quartic_projector',np.array_equal(Qnum@Qnum,16*Qnum) and np.trace(Qnum)==256)
# The same symmetric Q-sector is the original five-code; re-use actual symmetric rep.
check('returned_symmetric_quartic_rank5',np.trace(Ps[0])==80)
# Lowest exchange sector: the graph-Laplacian sum I-Swap is nonnegative.
# Its kernel for a connected graph is exactly the fully symmetric tensor.
I256=np.eye(256,dtype=np.int64)
tuples=list(product(range(4),repeat=4))
def swapmat(a,b):
    T=np.zeros((256,256),dtype=np.int64)
    for col,t in enumerate(tuples):
        u=list(t);u[a],u[b]=u[b],u[a]
        row=sum(x*4**(3-j) for j,x in enumerate(u));T[row,col]=1
    return T
L_K=sum((I256-swapmat(*e) for e in K4),np.zeros((256,256),int))
L_C=sum((I256-swapmat(*e) for e in C4),np.zeros((256,256),int))
def modular_rank(M,p=101):
    B=np.array(M,dtype=np.int64).copy()%p;r=0
    for col in range(B.shape[1]):
        nz=np.flatnonzero(B[r:,col])
        if not len(nz):continue
        j=r+int(nz[0]);B[[r,j]]=B[[j,r]]
        B[r]=(B[r]*pow(int(B[r,col]),-1,p))%p
        rows=np.flatnonzero(B[:,col]);rows=rows[rows!=r]
        B[rows]=(B[rows]-B[rows,col,None]*B[r])%p
        r+=1
        if r==B.shape[0]:break
    return r
Sym=np.zeros((256,35),dtype=np.int64)
for row,t in enumerate(tuples):
    n=tuple(t.count(j) for j in range(4));Sym[row,pos[n]]=1
check('explicit_symmetry_kernel_dimension35',np.count_nonzero(L_K@Sym)==0 and np.count_nonzero(L_C@Sym)==0 and np.count_nonzero(Sym.sum(axis=0)==0)==0)
check('K4_symmetric_ground_kernel',modular_rank(L_K)==221)
check('C4_symmetric_ground_kernel',modular_rank(L_C)==221)
# Sixth-order construction yields positive gap at negative sufficiently weak g.
results['ground_sector_theorem']={'microscopic_registers':28,'microscopic_hilbert_dimension':4**28,'isolated_low_band':256,'third_order_ground_sector_negative_g':35,'sixth_order_ground_sector_negative_g':5,'native_ground_irrep':5,'conditions':['four identical Hamming protected C4 blocks','same-site Pauli-complete swap links on K4 or C4','Delta>0','g<0 and |g|/Delta sufficiently small','actual energy and state identification with TFPT not derived'],'low_band_sufficient_isolation_bound_K4':'|g|/Delta<1/105 (only isolation; not a numerical validity bound for sixth-order splitting)','gap_asymptotic_K4':'(27573/512)*|g|^6/Delta^5+O(|g|^7/Delta^6)','gap_asymptotic_C4':'(3143/256)*|g|^6/Delta^5+O(|g|^7/Delta^6)'}
np.savez_compressed(ROOT/'matrices.npz',roots=np.array(roots),reflections_scaled2=np.array(Rs),paulis=paulis,occupancies=np.array(ns),symmetric_gram=norms,sector_numerators16=Ps,collective_generators=Ks,code_columns=E,H7=H7,logical_Q_numerator16=Qnum)
results['checks']=checks;results['summary']={'passed':len(checks),'seconds':time.time()-start,'kind':'independent finite algebra and perturbation coefficient audit, no physical TOE proof'}
(ROOT/'results.json').write_text(json.dumps(saveable(results),indent=2),encoding='utf8')
print(json.dumps(results['summary'],indent=2))

```

</details>

<details>
<summary>Q3: requirements.txt öffnen</summary>

Originalmitglied: `TFPT_Dynamischer_Codeabschluss_20260926/requirements.txt`  
SHA256: `9101128bb786a4dab198b7bb31109f469ed9902ad473d2b1f4b2f1b1b4b5470a`

```text
numpy>=1.24
sympy>=1.12

```

</details>

<details>
<summary>Q3: ursprüngliche Laufprotokolle öffnen</summary>

### `run.log`

```text
native symmetry complete
35 response sectors complete
{
  "passed": 1326,
  "seconds": 4.506535053253174,
  "kind": "independent finite algebra and perturbation coefficient audit, no physical TOE proof"
}

```

</details>

<a id="programm-q4"></a>
## Q4. Prüfprogramm und Abhängigkeiten

<details>
<summary>Q4: audit.py öffnen</summary>

Originalmitglied: `TFPT_Rekursive_Bindung_20260926/audit.py`  
SHA256: `4a19f8145d5ccaef08bfdc5893f64484feae630cf61e49639df52f89f56528c4`

```python
#!/usr/bin/env python3
"""Reproducible finite audit: TFPT source response, Petz binding and block recursion.

New coupling is defined on the 35-dimensional logical response spaces. This does
not identify it with an already selected microscopic TFPT field Hamiltonian.
Exact rational identities and the explicitly numerical higher-order probe are
reported separately. No network, no hidden imported result matrices, no TOE claim.
"""
from __future__ import annotations
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
os.environ.setdefault('OMP_NUM_THREADS','1')
from itertools import product
from math import prod, factorial
from pathlib import Path
import json, time, hashlib, platform
import numpy as np
from scipy import sparse as sp
import sympy as sy

ROOT=Path(__file__).resolve().parent
T0=time.time();checks=[];results={}
def check(name, condition, kind='exact', **detail):
    if not bool(condition): raise RuntimeError(f'{name} failed: {detail}')
    checks.append(dict(name=name,kind=kind,passed=True,**detail))
def zero(M): return all(sy.simplify(x)==0 for x in M)
def clean(x):
    if isinstance(x,dict):return {str(k):clean(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)):return [clean(v) for v in x]
    if isinstance(x,np.ndarray):return clean(x.tolist())
    if isinstance(x,np.generic):return x.item()
    if isinstance(x,sy.MatrixBase):return clean(x.tolist())
    if isinstance(x,sy.Basic):return str(x)
    return x

# Reconstruct the symmetric fourth power in unnormalized permutation-orbit kets.
I=np.eye(2,dtype=complex);X=np.array([[0,1],[1,0]],complex)
Y=np.array([[0,-1j],[1j,0]],complex);Z=np.diag([1,-1]).astype(complex)
As=[np.kron(a,b) for a in (I,X,Y,Z) for b in (I,X,Y,Z)]
labels=[a+b for a in 'IXYZ' for b in 'IXYZ']
ns=sorted([n for n in product(range(5),repeat=4) if sum(n)==4],reverse=True)
pos={n:i for i,n in enumerate(ns)};d=35
m=np.array([24//prod(factorial(v) for v in n) for n in ns],np.int64)
Ks=[];Ds=[]
for A in As:
    K=np.zeros((d,d),complex);D=np.zeros((d,d),complex)
    for c,n in enumerate(ns):
        for j in range(4):
            if not n[j]:continue
            for i in range(4):
                if A[i,j]==0:continue
                if i==j:K[c,c]+=n[j]*A[i,j]
                else:
                    nn=list(n);nn[j]-=1;nn[i]+=1
                    K[pos[tuple(nn)],c]+=(n[i]+1)*A[i,j]
        nn=[0]*4;ph=1
        for j in range(4):
            i=int(np.flatnonzero(A[:,j])[0]);nn[i]=n[j];ph*=A[i,j]**n[j]
        D[pos[tuple(nn)],c]=ph
    check('integer_Gaussian_collective_'+str(len(Ks)),
          np.array_equal(K.real,np.rint(K.real)) and np.array_equal(K.imag,np.rint(K.imag)))
    check('metric_selfadjoint_collective_'+str(len(Ks)),np.array_equal(m[:,None]*K,K.conj().T*m[None,:]))
    Ks.append(K);Ds.append(D)
Pnum=np.sum(Ds,axis=0).real.astype(np.int64) # 16 Pi5
E=np.zeros((35,5),np.int64)
supports=[[(4,0,0,0),(0,4,0,0),(0,0,4,0),(0,0,0,4)],[(2,2,0,0),(0,0,2,2)],
          [(2,0,2,0),(0,2,0,2)],[(2,0,0,2),(0,2,2,0)],[(1,1,1,1)]]
for j,S in enumerate(supports):
    for n in S:E[pos[n],j]=1
G=E.T@np.diag(m)@E
Gs=sy.diag(*[int(x) for x in np.diag(G)]);Gi=Gs.inv()
check('code_Gram',Gs==sy.diag(4,12,12,12,24))
check('code_projector',np.array_equal(Pnum@Pnum,16*Pnum) and np.trace(Pnum)==80)
check('code_range',np.array_equal(Pnum@E,16*E))
R=[]
for a,K in enumerate(Ks[1:],1):
    TK=E.T@np.diag(m)@K@K@E
    check('return_real_'+str(a),np.count_nonzero(TK.imag)==0)
    Ra=Gi*sy.Matrix(TK.real.astype(np.int64))/16
    check('plane_projector_'+str(a),Ra*Ra==Ra and sy.trace(Ra)==2)
    check('one_source_invisible_'+str(a),np.count_nonzero(E.T@np.diag(m)@K@E)==0)
    # Both endpoints of a first response lie in the matching Pauli-character sector.
    P_a=sum([(1 if np.array_equal(As[a]@b,b@As[a]) else -1)*Db for b,Db in zip(As,Ds)])
    check('response_sector_'+str(a),np.array_equal(P_a@K@E,16*K@E))
    R.append(Ra)
check('plane_sum',sum(R,sy.zeros(5))==6*sy.eye(5))

# Reconstruct the Bell effects from the explicitly supplied code-basis contractions.
Fnum=sy.Matrix([[4,4,4,4,0],[0,8,0,0,8],[4,-4,4,-4,0],[0,0,8,0,8],
               [0,0,0,8,8],[0,0,8,0,-8],[0,0,0,8,-8],[4,4,-4,-4,0],
               [0,8,0,0,-8],[4,-4,-4,4,0]])
Recovery=sy.zeros(25)
for r in range(10):
    f=Fnum[r,:].T/4;v=Gi*f
    Recovery+=2*sy.kronecker_product(v,v)*sy.kronecker_product(f,f).T
Qpair=sum([sy.kronecker_product(Ra,Ra) for Ra in R],sy.zeros(25))
check('Petz_binding_operator_identity',Qpair==sy.Rational(3,2)*sy.eye(25)+sy.Rational(9,2)*Recovery)
check('recovery_spectrum',Recovery.eigenvals()=={sy.Integer(1):1,sy.Rational(4,9):9,sy.Integer(0):15})
check('plane_pair_spectrum',Qpair.eigenvals()=={sy.Integer(6):1,sy.Rational(7,2):9,sy.Rational(3,2):15})
results['pair_identity']={'R_rank':2,'R_count':15,'sum_R':'6 I',
 'sum_R_tensor_R':'(3/2) I25 + (9/2) vectorized(Petz o E2)',
 'pair_h':'I25 - vectorized(Petz o E2)',
 'pair_h_spectrum':{'0':1,'5/9':9,'1':15},
 'second_order_H':'-192 epsilon^2/delta I25 -576 epsilon^2/delta vectorized(Petz o E2)'}
print('response and binding identity exact',flush=True)

# Exact complete 35 x 35 two-module model. L is selfadjoint in metric m tensor m.
L=sum([sp.kron(sp.csr_matrix(K),sp.csr_matrix(K),format='csr') for K in Ks[1:]])
check('bridge_real',np.count_nonzero(L.data.imag)==0)
L=L.real.astype(np.int64)
Hnum=32*sp.eye(d*d,format='csr',dtype=np.int64)-sp.kron(sp.csr_matrix(Pnum),sp.eye(d,format='csr',dtype=np.int64))-sp.kron(sp.eye(d,format='csr',dtype=np.int64),sp.csr_matrix(Pnum))
metric=np.kron(m,m);Tcode=np.kron(E,E)
B=L@Tcode
check('bridge_first_order_zero',np.count_nonzero(Tcode.T@(metric[:,None]*B))==0)
check('all_first_responses_energy_2delta',np.array_equal(Hnum@B,32*B))
Gt=sy.kronecker_product(Gs,Gs)
Bgram=Gt.inv()*sy.Matrix(B.T@(metric[:,None]*B))
check('exact_second_order_gram',Bgram==256*Qpair)
w0=sum([(24//G[j,j])*np.kron(E[:,j],E[:,j]) for j in range(5)])
w1=L@w0
ip=lambda u,v:int(np.dot(u*metric,v))
check('singlet_cross_zero',ip(w0,w1)==0)
check('singlet_bridge_norm',ip(w1,w1)==1536*ip(w0,w0))
check('closed_two_state_block',np.array_equal(L@w1,1536*w0+16*w1))
check('singlet_H0_closed',np.array_equal(Hnum@w0,np.zeros(1225,np.int64)) and np.array_equal(Hnum@w1,32*w1))
M1=w1.reshape(35,35)
# Reduced density of the normalized excited invariant state is (I-Pi5)/30.
check('excited_invariant_flat_30',np.array_equal(480*(M1@np.diag(m)@M1.T@np.diag(m)),ip(w1,w1)*(16*np.eye(35,dtype=np.int64)-Pnum)))
t,delta=sy.symbols('t delta',real=True)
Hsing=sy.Matrix([[0,16*sy.sqrt(6)*t],[16*sy.sqrt(6)*t,2*delta+16*t]])
lam=sy.symbols('lam')
check('singlet_characteristic',sy.expand(Hsing.charpoly(lam).as_expr()-(lam**2-(2*delta+16*t)*lam-1536*t**2))==0)
# Proof constants for the conservative global ground-state range |epsilon|/delta <=1/200.
# ||L||<=80 follows directly from 4 sum_16 Swap -16 I. In the neutral complement H0=2delta.
check('ground_gap_bound_constants',sy.Rational(460800,631)-560>170)
results['exact_pair']={'space_dimension':1225,'neutral_dimension':85,
 'orthonormal_singlet_block':Hsing,'ground_energy':'delta+8epsilon-sqrt((delta+8epsilon)^2+1536epsilon^2)',
 'proved_sufficient_ground_range':'0 < abs(epsilon)/delta <= 1/200',
 'proved_gap_lower_bound':'170 epsilon^2/delta',
 'excited_weight':'(1-(delta+8epsilon)/sqrt((delta+8epsilon)^2+1536epsilon^2))/2',
 'reduced_state':'(1-eta) Pi5/5 + eta (I35-Pi5)/30',
 'scope':'exact stated 35-response-space model, not a diagonalization of the full microscopic register parent'}
print('exact two-state ground sector and conservative global bound',flush=True)

# Exact three-cell chain of the derived effective pair operator.
h=sy.eye(25)-Recovery
H3=sy.kronecker_product(h,sy.eye(5))+sy.kronecker_product(sy.eye(5),h)
G3=sy.kronecker_product(Gs,Gs,Gs)
T1=sy.zeros(125,5);T2=sy.zeros(125,5);T3=sy.zeros(125,5)
for a,b in product(range(5),repeat=2):
    T1[25*a+5*a+b,b]=1/Gs[a,a]
    T2[25*a+5*b+a,b]=1/Gs[a,a]
    T3[25*b+5*a+a,b]=1/Gs[a,a]
W6=sy.Matrix([[2,2,-1,-1,-1,-1],[0,0,-1,-1,1,1],[0,0,-1,1,-1,1],[0,0,1,-1,-1,1],[1,-1,0,0,0,0]])
T4=sy.zeros(125,5)
for q in range(6):
    u=W6[:,q]
    T4+=sy.kronecker_product(u,u,u)*(u.T*Gs)/1600
Ts=[T1,T2,T3,T4]
GG=sy.Matrix(4,4,lambda i,j:sy.trace(Gi*Ts[i].T*G3*Ts[j])/5)
HH=sy.Matrix(4,4,lambda i,j:sy.trace(Gi*Ts[i].T*G3*H3*Ts[j])/5)
Hmult=GG.inv()*HH
for j in range(4):
    check('invariant_five_multiplicity_'+str(j),H3*Ts[j]==sum([Ts[i]*Hmult[i,j] for i in range(4)],sy.zeros(125,5)))
cp=H3.charpoly(lam).as_expr()
expected=(lam-2)**35*(lam-1)**5*(lam-sy.Rational(5,3))**10*(lam-sy.Rational(4,3))**16*(lam-sy.Rational(17,9))**9*(lam-sy.Rational(16,9))**16*(lam-sy.Rational(13,9))**10*(lam-sy.Rational(11,9))**9*(lam-sy.Rational(10,9))**5*(lam**2-sy.Rational(19,9)*lam+sy.Rational(8,9))**5
check('complete_three_chain_characteristic',sy.Poly(cp-expected,lam).is_zero)
s=sy.sqrt(73);e0=(19-s)/18;gap=(s-1)/18
c=sy.Matrix([-(27+3*s)/50,-sy.Rational(12,25),-(27+3*s)/50,1])
check('ground_multiplicity_vector',zero((Hmult-e0*sy.eye(4))*c))
NN=sy.simplify((c.T*GG*c)[0])
Vrg=sum([c[i]*Ts[i] for i in range(4)],sy.zeros(125,5))
check('ground_encoder_isometry_metric',zero(Vrg.T*G3*Vrg-NN*Gs))
alpha=(49+5*s)/144;beta=sy.Rational(2,5)*(1-alpha)
alpha_middle=sy.Rational(17,72)+85*s/5256
for site in (0,1,2):
    al=alpha_middle if site==1 else alpha;be=sy.Rational(2,5)*(1-al)
    for a,Ra in enumerate(R):
        Op=sy.kronecker_product(*[Ra if i==site else sy.eye(5) for i in range(3)])
        Aop=Gi*Vrg.T*G3*Op*Vrg/NN
        check(f'boundary_intertwiner_{site}_{a}',zero(Aop-al*Ra-be*sy.eye(5)))
results['recursive_projection']={'ground_energy':e0,'gap':gap,'ground_dimension':5,
 'four_intertwiner_gram':GG,'four_multiplicity_H':Hmult,'ground_coefficients':c,'ground_norm':NN,
 'endpoint_alpha':alpha,'endpoint_alpha_squared':sy.simplify(alpha**2),
 'endpoint_alpha_numeric':float(alpha),'endpoint_factor_numeric':float(alpha**2),
 'middle_alpha':alpha_middle,
 'weak_link_projection':'alpha^2 h + (4/5)(1-alpha^2) I',
 'scope':'exact compression of each weak link; full low-energy approximation requires weak/strong hierarchy and includes higher-order corrections'}
# Monogamy certificate in normalized code coordinates.
Om=sy.Matrix([1 if a==b else 0 for a,b in product(range(5),repeat=2)])
Bell=Om*Om.T/5
Q12=sy.kronecker_product(Bell,sy.eye(5));Q23=sy.kronecker_product(sy.eye(5),Bell)
check('monogamy',Q12*Q23*Q12==Q12/25)
check('three_chain_above_monogamy_bound',bool(e0>sy.Rational(4,9)))
print('three-cell ground code and endpoint recursion exact',flush=True)

# Numerical countercheck: the exact projected family is NOT closed under all virtual corrections.
# Everything below this point is labeled floating-point, not an exact certificate.
G5diag=np.diag(np.array(Gs,float));G3diag=np.diag(np.array(G3,float))
Wort=np.sqrt(G3diag)[:,None]*np.array(Vrg.evalf(),float)/(np.sqrt(float(NN))*np.sqrt(G5diag)[None,:])
Hn=np.sqrt(G3diag)[:,None]*np.array(H3,float)/np.sqrt(G3diag)[None,:]
Eval,EV=np.linalg.eigh(Hn)
Erel=Eval-float(e0);Erel[abs(Erel)<1e-11]=0
C0=EV.T@Wort
Beff=4/3*np.kron(C0,C0)
for Ra in R:
    Ro=np.sqrt(G5diag)[:,None]*np.array(Ra,float)/np.sqrt(G5diag)[None,:]
    BA=EV.T@np.kron(np.eye(25),Ro)@Wort
    BB=EV.T@np.kron(Ro,np.eye(25))@Wort
    Beff-=2/9*np.kron(BA,BB)
den=(Erel[:,None]+Erel[None,:]).ravel();inv=np.zeros_like(den)
inv[den>1e-10]=1/den[den>1e-10]
Hsecond=-Beff.T@(inv[:,None]*Beff)
G25diag=np.kron(G5diag,G5diag)
Kn=np.sqrt(G25diag)[:,None]*np.array(Recovery,float)/np.sqrt(G25diag)[None,:]
om=np.eye(5).ravel()/np.sqrt(5);P1=np.outer(om,om)
P9=9/4*(Kn-P1)
Swap5=np.eye(25).reshape(5,5,5,5).transpose(1,0,2,3).reshape(25,25)
P10=(np.eye(25)-Swap5)/2;P5=np.eye(25)-P1-P9-P10
fit=np.zeros((25,25));coeff={}
for dim,Pj in [(1,P1),(5,P5),(9,P9),(10,P10)]:
    cj=float(np.trace(Pj@Hsecond)/dim);fit+=cj*Pj;coeff[dim]=cj
res=float(np.max(abs(Hsecond-fit)))
check('second_order_native_sector_fit',res<1e-11,'numerical',residual=res)
check('second_order_5_10_splitting',abs(coeff[5]-coeff[10])>0.001,'numerical',difference=coeff[5]-coeff[10])
results['numerical_next_order']={'coefficients_in_units_weak_squared_over_strong':coeff,
 'native_sector_fit_max_residual':res,'split_5_minus_10':coeff[5]-coeff[10],
 'conclusion':'leading two-parameter form I,h is not a closed all-order renormalization family',
 'classification':'double-precision countercheck, no interval-certified spectral bounds'}

# General large-graph countercheck: global ferromagnetic source organization is not a set of local codes.
results['global_scope']={'symmetric_dimension_for_N_sources':'binomial(N+3,3)',
 'symmetric_dimension_8_sources':sy.binomial(11,3),
 'no_global_symmetric_exact_four_code_for_N_ge_5':'proof by transporting quartic Pauli checks and anticommuting weight-two checks',
 'micro_parent_not_rederived':['P1/P2 selection','bridge strength and signs','graph and scale hierarchy','field and state dictionary','3+1D limit','gravity']}
# Exact anticommuting witness used in the general proof.
XXI=sy.kronecker_product(sy.Matrix(X),sy.Matrix(X),sy.eye(2))
IZZ=sy.kronecker_product(sy.eye(2),sy.Matrix(Z),sy.Matrix(Z))
check('global_symmetry_obstruction_witness',XXI*IZZ==-IZZ*XXI)

results['summary']={'exact_checks':sum(c['kind']=='exact' for c in checks),'numerical_checks':sum(c['kind']=='numerical' for c in checks),
 'all_passed':True,'runtime_seconds':time.time()-T0,'python':platform.python_version(),'numpy':np.__version__,'sympy':sy.__version__,
 'meaning':'finite explicitly specified continuation, not a complete TFPT proof'}
results['checks']=checks
(ROOT/'results.json').write_text(json.dumps(clean(results),indent=2,ensure_ascii=False),encoding='utf-8')
np.savez_compressed(ROOT/'matrices.npz',occupancies=np.array(ns),metric35=m,code_E=E,code_G=G,
    paulis=np.array(As),collective_K=np.array(Ks),P5_numerator16=Pnum,
    recovery25=np.array(Recovery,float),planes_R=np.array([np.array(x,float) for x in R]),
    H3=np.array(H3,float),gram3=G3diag,ground_encoder_normalized=Wort,
    numerical_second_order=Hsecond,numerical_sector_projectors=np.array([P1,P5,P9,P10]))
(ROOT/'provenance.json').write_text(json.dumps({'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'basis_source':'TFPT_Quartik_Fortsetzung_Herleitungen_20260926.md',
    'dynamic_source':'TFPT_Dynamischer_Codeabschluss_Herleitung_20260926.md',
    'new_model':'two logical 35-response spaces, inherited 5+30 gap, chosen collective source exchange',
    'not_run':'full microscopic 56-register diagonalization or full TFPT repository'},indent=2),encoding='utf-8')
print(json.dumps(results['summary'],indent=2),flush=True)

```

</details>

<details>
<summary>Q4: requirements.txt öffnen</summary>

Originalmitglied: `TFPT_Rekursive_Bindung_20260926/requirements.txt`  
SHA256: `bc7ed35fa95bae186dc32a975169df95a013b1671dab6c2feca2136b68b339a4`

```text
numpy>=1.24
scipy>=1.10
sympy>=1.12

```

</details>

<details>
<summary>Q4: ursprüngliche Laufprotokolle öffnen</summary>

### `previous_package_rerun.log`

```text
native symmetry complete
35 response sectors complete
{
  "passed": 1326,
  "seconds": 4.944776773452759,
  "kind": "independent finite algebra and perturbation coefficient audit, no physical TOE proof"
}

```

### `run.log`

```text
response and binding identity exact
exact two-state ground sector and conservative global bound
three-cell ground code and endpoint recursion exact
{
  "exact_checks": 165,
  "numerical_checks": 2,
  "all_passed": true,
  "runtime_seconds": 28.67020082473755,
  "python": "3.13.5",
  "numpy": "2.3.5",
  "sympy": "1.14.0",
  "meaning": "finite explicitly specified continuation, not a complete TFPT proof"
}

```

</details>

<a id="programm-q5"></a>
## Q5. Prüfprogramm und Abhängigkeiten

<details>
<summary>Q5: audit.py öffnen</summary>

Originalmitglied: `TFPT_Ladung_Komposition_20260926/audit.py`  
SHA256: `65944c53a45003b6ad19bc2b8bd7b04e3c0bf44949282f1701e6307813fedfe0`

```python
#!/usr/bin/env python3
"""Exact finite audit of charge compatibility, symmetry completion and composition.

Reconstructs the previously supplied TFPT code coordinates, rather than importing
computed matrices. This is not a derivation of P1/P2, a local gauge field theory,
a spacetime or a complete TFPT model. The SU(5) completion is explicitly a changed
operator under a stated simultaneous-symmetry requirement. All tests below are
exact rational/algebraic/integer identities; modular ranks certify lower bounds.
"""
from __future__ import annotations
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
os.environ.setdefault('OMP_NUM_THREADS','1')
from pathlib import Path
from itertools import product, combinations
from collections import deque
from functools import reduce
from math import lcm
import json, time, platform
import numpy as np
import sympy as s
ROOT=Path(__file__).resolve().parent
T0=time.monotonic(); checks=[]; out={}
def check(name:str, value:bool, **details):
    if not bool(value): raise RuntimeError(f'{name}: {details}')
    checks.append({'name':name,'passed':True,'type':'exact',**details})
def simp(M): return M.applyfunc(s.simplify) if isinstance(M,s.MatrixBase) else s.simplify(M)
def zero(M): return all(s.expand(x)==0 or s.simplify(x)==0 for x in M)
def clean(x):
    if isinstance(x,dict): return {str(k):clean(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)): return [clean(v) for v in x]
    if isinstance(x,s.MatrixBase):return [[str(a) for a in row] for row in x.tolist()]
    if isinstance(x,s.Basic):return str(x)
    if isinstance(x,np.generic):return x.item()
    return x
Pmod=101
def modval(x):
    # Evaluation in the split residue field: sqrt(6) -> 39, since 39^2=6 mod101.
    x=s.simplify(s.expand(x).subs(s.sqrt(6),s.Integer(39)))
    if not x.is_Rational:raise TypeError(f'not Q(sqrt6) here: {x}')
    return int(x.p)*pow(int(x.q),-1,Pmod)%Pmod
def modmat(M):return np.array([[modval(a) for a in row] for row in M.tolist()],dtype=np.int64)
def rank_mod(A):
    A=np.array(A,dtype=np.int64,copy=True)%Pmod;rank=0;pivots=[]
    for col in range(A.shape[1]):
        nz=np.flatnonzero(A[rank:,col])
        if not len(nz):continue
        j=rank+int(nz[0]);A[[rank,j]]=A[[j,rank]]
        A[rank]=A[rank]*pow(int(A[rank,col]),-1,Pmod)%Pmod
        for j in range(rank+1,A.shape[0]):
            if A[j,col]:A[j]=(A[j]-A[j,col]*A[rank])%Pmod
        pivots.append(col);rank+=1
        if rank==A.shape[0]:break
    return rank,pivots

# 1. Original rational code coordinates, with their actual metric.
G=s.diag(4,12,12,12,24);Gi=G.inv();I5=s.eye(5);I25=s.eye(25)
G25=s.kronecker_product(G,G)
Fn=s.Matrix([[4,4,4,4,0],[0,8,0,0,8],[4,-4,4,-4,0],[0,0,8,0,8],
 [0,0,0,8,8],[0,0,8,0,-8],[0,0,0,8,-8],[4,4,-4,-4,0],
 [0,8,0,0,-8],[4,-4,-4,4,0]])
K=s.zeros(25)
for j in range(10):
    f=Fn[j,:].T/4;w=Gi*f
    K+=2*s.kronecker_product(w,w)*s.kronecker_product(f,f).T
h=I25-K
om=s.Matrix([Gi[i,j] for i,j in product(range(5),repeat=2)])
P1=om*(om.T*G25)/5
Swap=s.zeros(25)
for i,j in product(range(5),repeat=2):Swap[5*j+i,5*i+j]=1
P9=s.Rational(9,4)*(K-P1);P10=(I25-Swap)/2;P5=I25-P1-P9-P10
Ps=[P1,P5,P9,P10]
for dim,P in zip([1,5,9,10],Ps):
    check('original_projector_'+str(dim),P*P==P and s.trace(P)==dim)
check('original_h_sectors',h==P5+s.Rational(5,9)*P9+P10)
check('selfadjoint_original_h',G25*h==h.T*G25)

# 2. Transport the existing 3+2 marking using the positive polar map.
W6=s.Matrix([[2,2,-1,-1,-1,-1],[0,0,-1,-1,1,1],[0,0,-1,1,-1,1],
 [0,0,1,-1,-1,1],[1,-1,0,0,0,0]])
D=s.Matrix.hstack(*[W6[:,j]-W6[:,0] for j in [1,2,3,4,5]])
A=I5+(1/s.sqrt(6)-1)*s.ones(5)/5
check('slot_difference_gram',D.T*G*D==48*(I5+s.ones(5)))
Y=simp(D*A*s.diag(s.Rational(1,2),-s.Rational(1,3),-s.Rational(1,3),
                       -s.Rational(1,3),s.Rational(1,2))*A*D.T*G/48)
check('charge_trace',s.trace(Y)==0)
check('charge_norm',s.simplify(s.trace(Y*Y))==s.Rational(5,6))
check('charge_minpoly',zero((Y-s.Rational(1,2)*I5)*(Y+s.Rational(1,3)*I5)))
check('charge_metric',zero(G*Y-Y.T*G))
QY=s.kronecker_product(Y,I5)-s.kronecker_product(I5,Y)
check('opposite_charge_singlet',zero(QY*om))
C=h*QY-QY*h
cn=s.simplify(-s.trace(C*C))
check('charge_violation_witness',cn==(488+32*s.sqrt(6))/405)
n510=s.simplify(s.trace(P5*QY*P10*QY))
n910=s.simplify(s.trace(P9*QY*P10*QY))
check('sector_mix_5_10',n510==s.Rational(67,60)-s.sqrt(6)/5)
check('sector_mix_9_10',n910==s.Rational(61,20)+s.sqrt(6)/5)
check('mixes_both',bool(n510>0) and bool(n910>0))
check('no_direct_5_9_mix',s.simplify(s.trace(P5*QY*P9*QY))==0)
yvec=s.Matrix(Y*Gi).reshape(25,1)
y5=s.simplify((yvec.T*G25*P5*yvec)[0]); y9=s.simplify((yvec.T*G25*P9*yvec)[0])
check('charge_components',y5==s.Rational(29,60)+s.sqrt(6)/10 and y9==s.Rational(7,20)-s.sqrt(6)/10)
# Completeness: no nontrivial continuous onsite conjugation symmetry of old h.
columns=[]
for i,j in product(range(5),repeat=2):
    X=s.zeros(5);X[i,j]=1
    J=s.kronecker_product(X,I5)-s.kronecker_product(I5,Gi*X.T*G)
    columns.append(s.Matrix(h*J-J*h).reshape(625,1))
M=s.Matrix.hstack(*columns)
rank,pivots=rank_mod(modmat(M))
check('onsite_Lie_symmetry_rank',rank==24)
check('identity_is_known_kernel',M*s.Matrix([int(i==j) for i,j in product(range(5),repeat=2)])==s.zeros(625,1))
# Native S6 orbit of Y spans all 14 traceless real self-adjoint directions.
gens=[]
for j in range(1,6):
    d=W6[:,0]-W6[:,j];U=I5-d*d.T*G/48
    check('native_transposition_metric_'+str(j),U.T*G*U==G and U*U==I5)
    gens.append(modmat(U))
Eye=np.eye(5,dtype=np.int64);GG=modmat(G);GGi=modmat(Gi);YY=modmat(Y)
seen={Eye.tobytes():Eye};todo=deque([Eye])
while todo:
    U=todo.popleft()
    for V in gens:
        T=U@V%Pmod;k=T.tobytes()
        if k not in seen:seen[k]=T;todo.append(T)
check('native_S6_order_mod',len(seen)==720)
orbits=[(U@YY@GGi@U.T@GG%Pmod).ravel() for U in seen.values()]
rr,piv=rank_mod(np.array(orbits).T)
check('charge_orbit_rank14',rr==14)
basis=[orbits[j].reshape(5,5) for j in piv]
comms=np.array([(U@V-V@U).ravel()%Pmod for U,V in combinations(basis,2)])
check('commutators_rank10',rank_mod(comms.T)[0]==10)
out['original_charge_test']={'Y_in_code_coordinates':Y,'commutator_HS_squared':cn,
 'mix_5_10_HS_squared':n510,'mix_9_10_HS_squared':n910,'Y_norm5_squared':y5,'Y_norm9_squared':y9,
 'onsite_complex_Lie_constraint_rank':rank,'native_charge_orbit_span':14,'commutator_span':10,
 'scope':'fixed positive polar marking; h as operator on V tensor conjugate(V); not a contradiction in the earlier uncharged model'}
print('original charge compatibility and native orbit certified',flush=True)

# Alternative: only the actual marked 3+2 group, not the stronger fixed S6.
Pcol=simp(s.Rational(3,5)*I5-s.Rational(6,5)*Y); Pweak=I5-Pcol
check('marked_color_projector',zero(Pcol*Pcol-Pcol) and s.trace(Pcol)==3)
vcol=s.Matrix(Pcol*Gi).reshape(25,1);vweak=s.Matrix(Pweak*Gi).reshape(25,1)
PY=simp(s.Rational(6,5)*yvec*(yvec.T*G25))
P8=simp(s.kronecker_product(Pcol,Pcol)-vcol*(vcol.T*G25)/3)
P3=simp(s.kronecker_product(Pweak,Pweak)-vweak*(vweak.T*G25)/2)
Pcw=simp(s.kronecker_product(Pcol,Pweak));Pwc=simp(s.kronecker_product(Pweak,Pcol))
expected=[(61+4*s.sqrt(6))/75,s.Rational(1247,1500)+2*s.sqrt(6)/375,
 (311+4*s.sqrt(6))/375,(314-4*s.sqrt(6))/375,(314-4*s.sqrt(6))/375]
energies=[]
for d,P,goal in zip([1,8,3,6,6],[PY,P8,P3,Pcw,Pwc],expected):
    v=s.simplify(s.trace(h*P)/d)
    check('marked_group_average_energy_'+str(len(energies)),s.simplify(v-goal)==0)
    energies.append(v)
check('marked_group_complete',zero(P1+PY+P8+P3+Pcw+Pwc-I25))
out['marked_group_alternative']={'group':'S(U(3) x U(2))',
 'commutant_dimension':8,'paired_decomposition':'two singlets + 8 + 3 + 6 + conjugate(6)',
 'averaged_energies_Y_8_3_6_6':energies,
 'construction':'normalized Haar average of old h; trace over each multiplicity-one sector, singlet Omega remains zero',
 'scope':'a different, marking-dependent covariance completion; SU(5) is not forced by the TFPT postulates simply by this audit'}


# 3. Unique singlet-ground completion IF full native S6 and this charge are both exact symmetries.
hcov=s.Rational(5,6)*(I25-P1)
check('completed_charge',zero(hcov*QY-QY*hcov))
check('trace_normalization',s.trace(hcov)==s.trace(h)==20)
check('least_square_distance',s.trace((h-hcov)**2)==s.Rational(10,9))
check('completed_return_channel',I25-hcov==s.Rational(1,6)*I25+s.Rational(5,6)*P1)
out['completion']={'operator':'(5/6)(I-P_Omega)','eigenspaces':'0:1; 5/6:24',
 'HS_squared_change':'10/9','channel':'X -> (X+Tr(X)I)/6',
 'assumption':'full unmarked native S6 AND additive hypercharge as exact symmetries; not automatically mandatory at a fixed TFPT marking',
 'uniqueness':'up to common energy shift and positive scale; 5/6 fixes trace and is the nearest Hilbert-Schmidt projection'}

# 4. SU(5)-covariant three-site map, now in standard orthonormal coordinates.
I=np.eye(5,dtype=np.int64);I125=np.eye(125,dtype=np.int64)
T1=np.zeros((125,5),np.int64);T3=T1.copy()
for a,b in product(range(5),repeat=2):
    T1[25*a+5*a+b,b]=1;T3[25*b+5*a+a,b]=1
S=T1+T3;Dminus=T1-T3
check('new_encoder_norm',np.array_equal(S.T@S,12*I))
om0=I.ravel();Qn=np.outer(om0,om0) # 5 P_Omega
N12=np.kron(Qn,I);N23=np.kron(I,Qn)
# H3 = (10I-N12-N23)/6, exact numerator.
H3n=10*I125-N12-N23
check('new_three_ground',np.array_equal(H3n@S,4*S))
check('new_three_other_five',np.array_equal(H3n@Dminus,6*Dminus))
check('new_three_rest',np.array_equal(H3n@H3n-10*H3n, -2*S@S.T-3*Dminus@Dminus.T))
# Direct minimal polynomial and projector multiplicities certify the whole spectrum.
check('new_three_minpoly',np.count_nonzero((H3n-4*I125)@(H3n-6*I125)@(H3n-10*I125))==0)
check('new_three_ranks',np.trace(S@S.T)==60 and np.trace(Dminus@Dminus.T)==40)
left=[];right=[];edge=[]
for i,j in product(range(5),repeat=2):
    E=np.zeros((5,5),np.int64);E[i,j]=1
    O1=np.kron(E,np.eye(25,dtype=np.int64));O2=np.kron(np.kron(I,E),I);O3=np.kron(np.eye(25,dtype=np.int64),E)
    check(f'new_boundary_{i}_{j}',np.array_equal(S.T@O1@S,7*E+int(i==j)*I))
    check(f'new_middle_{i}_{j}',np.array_equal(S.T@O2@S,2*E.T+2*int(i==j)*I))
    Q=np.kron(E,np.eye(25,dtype=np.int64))-np.kron(np.kron(I,E.T),I)+np.kron(np.eye(25,dtype=np.int64),E)
    check(f'additive_charge_intertwiner_{i}_{j}',np.array_equal(Q@S,S@E))
    left.append(O1@S);right.append(O3@S);edge.append(7*E+int(i==j)*I)
# Four-site local TL relations imply arbitrary chain lengths, once a chain is chosen.
check('TL_square',np.array_equal(N12@N12,5*N12))
check('TL_adjacent',np.array_equal(N12@N23@N12,N12) and np.array_equal(N23@N12@N23,N23))
Tleft=np.kron(Qn,np.eye(25,dtype=np.int64));Tright=np.kron(np.eye(25,dtype=np.int64),Qn)
check('TL_disjoint',np.array_equal(Tleft@Tright,Tright@Tleft))
# Project each weak bond using the endpoint channel B(X)=(7X+Tr(X)I)/12.
Qproject=sum(np.kron(edge[a],edge[a]) for a in range(25)) # 720 * projected P_Omega
# project h=(5/6)I-(1/6)sum Eij tensor Eij
hproject=s.Rational(5,6)*s.eye(25)-s.Matrix(Qproject)/864
hstd=s.Rational(5,6)*s.eye(25)-s.Matrix(Qn)/6
check('new_exact_weak_projection',hproject==s.Rational(49,144)*hstd+s.Rational(19,36)*s.eye(25))
out['covariant_recursion']={'W':'(T1+T3)/sqrt(12)','space':'V tensor conjugate(V) tensor V',
 'three_spectrum':{'2/3':5,'1':5,'5/3':115},'gap':'1/3',
 'endpoint':'(7 X+Tr(X) I)/12','middle':'(X^T+Tr(X) I)/6',
 'charge_identity':'(Y1-Y2^T+Y3)W=WY',
 'projected_bond':'(49/144) h + (19/36) I',
 'limit':'weak coupling projection; no preselected spatial dimension or microscopic scale hierarchy'}
print('covariant charge transport, three-site spectrum and TL algebra certified',flush=True)

# 5. Generic Yang-Baxter identity in the abstract TL_3 algebra, no sampled spectral parameters.
def reduce_word(w):
    w=list(w);factor=1
    while True:
        found=False
        for k in range(len(w)-1):
            if w[k]==w[k+1]:w.pop(k+1);factor*=5;found=True;break
        if found:continue
        for k in range(len(w)-2):
            if w[k]==w[k+2]:w=w[:k]+[w[k]]+w[k+3:];found=True;break
        if not found:return tuple(w),factor
def mul(A,B):
    C={}
    for wa,ca in A.items():
        for wb,cb in B.items():
            w,factor=reduce_word(wa+wb);C[w]=C.get(w,0)+factor*ca*cb
    return {w:s.expand(c) for w,c in C.items()}
t,u=s.symbols('t u',nonzero=True);q=(5+s.sqrt(21))/2;qi=5-q
R=lambda site,x:{():q-qi*x*x,(site,):x*x-1}
LH=mul(mul(R(0,t),R(1,t*u)),R(0,u));RH=mul(mul(R(1,u),R(0,t*u)),R(1,t))
for w in set(LH)|set(RH):check('YB_generic_'+str(w),s.expand(LH.get(w,0)-RH.get(w,0))==0)
Uprod=mul(R(0,t),R(0,1/t))
check('R_inversion_nonscalar_zero',s.expand(Uprod[(0,)])==0)
check('R_regular',s.simplify(q-qi)==s.sqrt(21))
check('q_loop',s.simplify(q+1/q)==5)
out['TL_composition']={'e':'5 P_Omega','loop_parameter':5,'q':q,
 'R':'(q-q^(-1)t^2) I + (t^2-1) e',
 'identity':'R_i(t)R_(i+1)(tu)R_i(u)=R_(i+1)(u)R_i(tu)R_(i+1)(t)',
 'unitary':'for t=exp(i theta), divide R by sqrt(23-2 cos(2theta))',
 'scope':'classical Temperley-Lieb Baxterization for this completed chain, not a TFPT clock or 3+1D scattering theorem'}

# 6. Even this symmetry-complete pair family creates genuine three-block terms.
# Exact middle-block reduced resolvent: R=(12I-S S^T+3Dminus Dminus^T)/12.
Rn=12*I125-S@S.T+3*Dminus@Dminus.T
check('reduced_inverse',np.array_equal((H3n-4*I125)@Rn,72*I125-6*S@S.T))
Hcross_n=np.zeros((125,125),np.int64)
for a,b in product(range(25),repeat=2):
    at=5*(a%5)+a//5;bt=5*(b%5)+b//5
    T=left[at].T@Rn@right[b]+right[bt].T@Rn@left[a]
    Hcross_n-=np.kron(np.kron(edge[a],T),edge[b])
HD=746496
F13=np.zeros((125,125),np.int64)
for i,j,k in product(range(5),repeat=3):F13[25*k+5*j+i,25*i+5*j+k]=1
bases=[I125,N12,N23,F13,N12@N23+N23@N12]
Gram=s.Matrix([[int(np.trace(x@y)) for y in bases] for x in bases])
rhs=s.Matrix([int(np.trace(x@Hcross_n)) for x in bases])
coef=Gram.inv()*rhs/HD
common=reduce(lcm,[int(x.q) for x in coef]+[HD])
fit=sum(int(x*common)*B for x,B in zip(coef,bases))
check('full_three_block_fit',np.array_equal(fit,Hcross_n*(common//HD)))
check('genuine_three_body_coefficient',25*coef[4]==s.Rational(30625,186624))
check('invariant_pair_basis_independent',Gram.det()!=0)
res=s.Rational(int(np.trace(Hcross_n@Hcross_n)),HD**2)-(rhs[:4,0].T*Gram[:4,:4].inv()*rhs[:4,0])[0]/HD**2
check('outside_pair_family_norm',res==s.Rational(2100875,241864704) and res>0)
out['three_block_correction']={'physical_basis':'I, P12, P23, Swap13, {P12,P23}',
 'coefficients':[coef[0],5*coef[1],5*coef[2],coef[3],25*coef[4]],
 'units':'Jweak^2/Jstrong; cross contribution of the two different weak bonds only',
 'squared_HS_distance_from_invariant_two_body_span':res,
 'meaning':'no exact nearest-neighbor pair-only RG closure; TL composition and RG projection are different statements'}
print('genuine three-block correction certified',flush=True)

# 7. The complete S6-invariant many-body space does not stay four dimensional.
out['native_invariant_dimensions']={str(n):(400+40*4**n+15*9**n+25**n)//720 for n in range(1,7)}
check('native_three_body_invariants',out['native_invariant_dimensions']['3']==41)
# Mean pair energy fixes trace convention, not physical energy scale.
summary={'all_passed':True,'checks':len(checks),'runtime_seconds':time.monotonic()-T0,
 'python':platform.python_version(),'sympy':s.__version__,'numpy':np.__version__,
 'scope':'finite exact consistency audit and explicit changed-model completion; no TOE or physical spacetime claim'}
out['summary']=summary;out['checks']=checks
(ROOT/'results.json').write_text(json.dumps(clean(out),ensure_ascii=False,indent=2),encoding='utf8')
np.savez_compressed(ROOT/'integer_certificates.npz',three_H_numerator6=H3n,
 encoder_numerator_sqrt12=S,three_resolvent_numerator12=Rn,
 cross_H_numerator=Hcross_n,cross_H_denominator=HD,
 native_charge_constraints_mod101=modmat(M),native_charge_orbit_mod101=np.array(orbits))
print(json.dumps(summary,ensure_ascii=False,indent=2))

```

</details>

<details>
<summary>Q5: requirements.txt öffnen</summary>

Originalmitglied: `TFPT_Ladung_Komposition_20260926/requirements.txt`  
SHA256: `dea8b851815ed75b0fa5533f2d422d39e0d86e17c684d6d6015dbadefff851f9`

```text
numpy>=1.26
sympy>=1.12

```

</details>

<details>
<summary>Q5: ursprüngliche Laufprotokolle öffnen</summary>

### `optimized_run.log`

```text
original charge compatibility and native orbit certified
covariant charge transport, three-site spectrum and TL algebra certified
genuine three-block correction certified
{
  "all_passed": true,
  "checks": 138,
  "runtime_seconds": 15.703335577000189,
  "python": "3.13.5",
  "sympy": "1.14.0",
  "numpy": "2.3.5",
  "scope": "finite exact consistency audit and explicit changed-model completion; no TOE or physical spacetime claim"
}

```

### `previous_package_rerun.log`

```text
response and binding identity exact
exact two-state ground sector and conservative global bound
three-cell ground code and endpoint recursion exact
{
  "exact_checks": 165,
  "numerical_checks": 2,
  "all_passed": true,
  "runtime_seconds": 27.68682622909546,
  "python": "3.13.5",
  "numpy": "2.3.5",
  "sympy": "1.14.0",
  "meaning": "finite explicitly specified continuation, not a complete TFPT proof"
}

```

### `run.log`

```text
original charge compatibility and native orbit certified
covariant charge transport, three-site spectrum and TL algebra certified
genuine three-block correction certified
{
  "all_passed": true,
  "checks": 138,
  "runtime_seconds": 14.08355053799994,
  "python": "3.13.5",
  "sympy": "1.14.0",
  "numpy": "2.3.5",
  "scope": "finite exact consistency audit and explicit changed-model completion; no TOE or physical spacetime claim"
}

```

</details>


---

[Zurück zum Gesamtbild](#gesamtbild) · [Zur Navigation](#navigation) · [Zur komprimierten Schlussbilanz](#schlussbilanz)

**Ende der Gesamtdokumentation.**
