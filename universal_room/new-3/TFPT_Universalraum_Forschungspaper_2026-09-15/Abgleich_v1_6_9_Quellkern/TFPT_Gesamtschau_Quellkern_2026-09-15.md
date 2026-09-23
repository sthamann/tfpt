---
title: "TFPT und Universalraum: die übersehene Verbindung prüfen"
subtitle: "Abgleich v1.6.9, ursprüngliche Schleifenphasen und der Test modularer Zeit"
date: "15. September 2026 · Ergänzung 1.4"
lang: de-DE
---

# Ergebnis in einfachen Worten

**Die stärkste verbindende Idee ist eine einzige konsistente Beschreibung aller gemeinsamen Antworten.** Welche Teile sich Ressourcen teilen, welche Geschichten miteinander interferieren und was ein interner Beobachter unterscheiden kann, müssen darin zusammenpassen. Ein solches Antwortsystem kann einen gemeinsamen mathematischen Träger bestimmen. Es wählt aber noch nicht von selbst die richtigen Naturgesetze aus.

Die neue Version 1.6.9 bringt diese Idee weiter: Der andere Worker zeigt in zwei begrenzten Familien, wie höhere Antworten die eingesetzte Zusammensetzung rekonstruieren. Ich habe das vollständige neue Prüfpaket erneut ausgeführt und die Ergebnisbytes gegen die Lieferung abgeglichen. Die angegebenen 514 exakten Bedingungen und vier numerischen Kontrollen bestehen. Alle 94 im Archiv verzeichneten Dateihashes stimmen; 17 native, 1073 ursprüngliche Strahl-Guards und 13 kleine CAR-Querkontrollen sind gesondert ausgewiesen.

Meine neue Fortsetzung liefert eine konkrete Vorwärtsrichtung: **Eine positive Überlappungsmatrix bestimmt einen minimalen gemeinsamen Fermionträger bis auf eine gemeinsame unitäre Basisänderung.** An den tatsächlichen 60 Quellstrahlen wurden anschließend zwei einfache Vorschriften vollständig verglichen. Beide verwenden dieselben Quellprojektoren und dasselbe lokale W. Sie liefern dennoch unterschiedliche Träger und Antworten. Damit ist die Konstruktion aus einer festgelegten Überlappungsregel lösbar; die Auswahl dieser Regel bleibt offen.

Ein zweiter möglicher Denkfehler betrifft die Symmetrie. Die Symmetrie des lokalen W-Tensors ist nicht automatisch die Symmetrie eines Experiments mit ausgezeichneten Quellmarken, Präparationen und Zeigern. Mein früherer Referenzsatz gilt unter seinem ausdrücklich referenzfreien Vertrag. Er darf nicht als allgemeine Unbenutzbarkeit des 15er-Codes gelesen werden.

**Die zwei später gelieferten Deutungen wurden ebenfalls geprüft.** Ein direkter neuer Quelltest findet eine geordnete Dreierspur $(1-i)/4$, die in reinen Paarfidelitäten verloren geht. Gleichzeitig liefert die gleichgewichtete Mischung der 60 Originalstrahlen exakt $I_4/4$ und damit einen trivialen modularen Fluss. Die zusätzliche Rechnung modularer Zeit am kleinen v1.6.9-Modell wählt die physische Dynamik nicht aus. Der Nachtrag erklärt diese Befunde und die Grenzen der vorgeschlagenen Selbstgeschlossenheit.

# Was tatsächlich gelesen und geprüft wurde

Die drei gelieferten Markdown-Dateien und drei PDFs wurden eingefroren und mit SHA-256 versehen. Die PDFs enthalten zwei, zwei und 161 Seiten. Die Hauptfassung enthält die vollständige historische v1.6.8; aktuelle Aussagen stehen in den vorangestellten v1.6.9-Kapiteln und Teilberichten. Die neuen Quell-, Kompositions-, Prozess- und Feldargumente wurden gegen ihre Prüfer gelesen. Die PDF-Texte wurden extrahiert und die Kurzfassung mit den Formeln visuell kontrolliert.

Der Replay lief in einer eigens ausgepackten Arbeitskopie. Er bestätigte sowohl normale als auch optimierte Ausführung und dieselben Ergebnisse wie das Originalpaket. Diese Wiederholung ist eine Reproduktion der Worker-Rechnungen, keine unabhängige neue Methode für jede ihrer Aussagen. Die alte gesamte v1.6.8-Suite und der große native Grundzustandslauf wurden nicht erneut ausgeführt.

Zusätzlich wurden die zugänglichen Aufgaben **„Finde TFPT-Lösungen zur vollen TOE“** und **„Universelle Lösung erneut prüfen“** eingesehen. Die erste Aufgabe war beim ersten Abruf aktiv. Die zweite Aufgabe hat ihre Gesamtschau inzwischen abgeschlossen; der später vom Nutzer gelieferte zweite Text entspricht diesem Ergebnis. Ihre Aussagen zu Schleifenphasen und endlichen Sektoren wurden unten eigens geprüft. Der vollständig reproduzierte abgeschlossene Rechenstand ist das eingefrorene v1.6.9-Paket.

Die neue eigene Rechnung umfasst **44 exakte Bedingungen**, normal und optimiert bytegleich, sowie separat den wiederverwendeten ursprünglichen P0/P1-Lauf mit 1073 Guards. Vollständige Ganzzahl-Polynomidentitäten und Spuren von Spektralprojektoren ersetzen numerische Rangentscheidungen. Diese Zählungen dokumentieren den Prüfungsumfang, nicht den Abstand zu einer vollständigen Theorie.

# Was der andere Worker tatsächlich verbessert hat

## Die Zusammensetzung wird rückrechenbar

Für zwei überlappende Fermion-Charts mit gleichem ursprünglichem W gilt

$$f_i^L=a_i,\qquad f_i^R=c\,a_i+\sqrt{1-c^2}\,d_i.$$

Der Worker leitet bei festgelegtem Eingangs- und Messvertrag her:

$$P(L\to R;t)=16g^4c^4t^4+O(t^6),$$

$$I_4=\frac{\mu_4-3\mu_1^2\mu_2+2\mu_1^4}
{(\mu_2-\mu_1^2)^2}=1+c^4.$$

Die letzte Identität wurde hier zusätzlich durch eine eigene symbolische Blockrechnung bestätigt. Sie bestimmt $c$ in der angegebenen nichtnegativen Zwei-Chart-Familie. Sie bestimmt nicht die Präparation, die Messgeräte oder die Auswahl genau dieser Familie.

Eine zweite Familie verwendet eine gemeinsame Bosonbank und einen normierten symmetrischen Kopplungstensor C. Hier ergibt die matrixaufgelöste Dreiladungsantwort

$$G_C^{(3)}=8I-(C^\dagger C)\otimes K_{\mathrm{Austausch}},
\qquad \operatorname{tr}K_{\mathrm{Austausch}}=960,$$

$$C^\dagger C=\frac1{960}\operatorname{Tr}_{\mathrm{intern}}(8I-G_C^{(3)}).$$

Das ist ein stärkeres Identifikationsresultat: Selbst gleiche gesamte Zweiladungsspektren schließen unterschiedliche Dreiladungsspektren nicht aus. Die Orientierung der rekonstruierten Matrix benötigt jedoch die vollständige markierte Antwort, nicht bloß eine Eigenwertliste. Unterschiedliche phasenmarkierte C können dasselbe $C^\dagger C$ besitzen.

## Der Eingriff benötigt einen Operatortyp weniger

Der Impuls $Z_b=e^{i\pi N_b}$ ersetzt den zuvor zusätzlich gewährten Einzelmodenimpuls. Er gehört auf dem betrachteten Dreizustandsraum zur erklärten Kontrollalgebra aus X und $N_b$. Der ursprüngliche Hamiltonoperator bleibt während der freien Abschnitte derselbe.

Die unbedingte Wahrscheinlichkeit der Empfängermode steigt von ungefähr 0,00021950 auf 0,00052992. Die Differenz beträgt etwa **0,0310417 Prozentpunkte**. Ein neutraler Zeiger, der nur Paar und Boson unterscheidet, erhält die Interferenz innerhalb der Paare und liefert beim Ignorieren des Zeigers den halben Folgeeffekt.

Das ist eine reale Vereinfachung des bedingten Versuchs. Unabhängige Schaltbarkeit, Präparation, Zeigerkopplung und terminales Lesen sind weiterhin vorausgesetzt. Der globale Bosongriff ist noch kein hergeleiteter räumlich lokaler Sender.

## Der Feldadapter wurde am richtigen Ort angegriffen

Ein zusätzlicher Impuls ermöglicht einen minimalen Lorentz-Ausleseadapter vom gemischthändigen Komposit zum Weylspinor. Der entscheidende Test ist negativ: Beim vorgeschlagenen Produkt freier masseloser Felder verschwindet dessen Auslese auf den Bewegungsgleichungen exakt. Eine erlaubte Darstellung erzeugt daher noch kein sichtbares Teilchen.

Dieser Nulltest ist produktiv: Vor einem weiteren großen Feldbau muss ein nichtverschwindendes Matrixelement mit einer konsistenten Kinetik gefunden werden. Der Befund betrifft den angegebenen freien Feldansatz, nicht jede mögliche Interpretation der ursprünglichen Fockmoden.

## Ein älterer Fortschritt, der in der Gesamtschau erhalten bleiben muss

Die historische v1.6.8 enthält gegenüber unserem ursprünglichen v1.6.7-Snapshot eine stärkere Variationsschranke aus der fünften Bosonstufen-Norm:

$$E_0<-1.13847609\Delta.$$

Mit dem beibehaltenen N=63-Satz folgt dort

$$\epsilon>0.01657709\Delta.$$

Diese Verbesserung wurde in v1.6.9 nicht erneut hergestellt oder weiter verbessert. Ich habe sie als dokumentierten historischen Befund gelesen, nicht in dieser Runde neu verifiziert. Die sieben Ritz-Vektoren sind kein invarianter Unterraum; ihre Zustandsmittelwerte dürfen nicht mit denjenigen einer älteren Fünferkompression oder mit dem isolierten Polgewicht verwechselt werden. Die Schranken gelten nicht automatisch für die neuen zusammengesetzten Modelle.

# Eigener konstruktiver Schritt: aus Überlappungen zu gemeinsamen Fermionen

## Der endliche Satz

Sei $S$ eine hermitesche positiv semidefinite $m\times m$-Matrix mit $S_{aa}=1$. Dann gibt es normierte Vektoren $u_a$ mit

$$\langle u_a,u_b\rangle=S_{ab}.$$

Man erhält sie beispielsweise aus einer Faktorisierung $S=U^\dagger U$. Alternativ nimmt man den von formalen Labels aufgespannten Raum mit diesem Skalarprodukt und entfernt die Nullrichtungen. Der kleinste Raum hat Dimension $r=\operatorname{rank}S$.

Für einen ursprünglichen 64-dimensionalen Fermionträger definiere

$$\mathcal V_{\mathrm{global}}=\mathbb C^r\otimes\mathbb C^{64},
\qquad E_a v=u_a\otimes v.$$

Dann gilt

$$\boxed{E_a^\dagger E_b=S_{ab}I_{64}.}$$

Auf der gewöhnlichen Fockdarstellung über $\mathcal V_{\mathrm{global}}$ lassen sich damit Chartoperatoren wählen, deren gegenseitige CAR genau diese Überlappung tragen. Jedes einzelne Chart hat die ursprünglichen kanonischen CAR. Die innere Gruppe wirkt auf dem zweiten Faktor; dadurch sind alle $E_a$ Verflechter für denselben ursprünglichen inneren Träger.

**Eindeutigkeit bei gegebenem S:** Zwei minimale Vektorfamilien mit demselben Gram definieren durch $u_a\mapsto u'_a$ eine wohldefinierte Isometrie ihrer Spannen. Wegen Minimalität ist diese unitär. Das entfernt die zusätzliche Suche nach willkürlichen Einbettungsmatrizen, sobald der vollständige Kernel feststeht.

Dies ist eine endliche Form der bekannten Konstruktion von Hilberträumen aus positiven Kernen. Zum allgemeinen mathematischen Rahmen siehe [Alpay und Jorgensen, New characterizations of reproducing kernel Hilbert spaces](https://arxiv.org/abs/2011.09525). Der obige endliche Beweis und die Anwendung auf die hiesigen CAR-Charts sind hier ausgeschrieben; die Quelle begründet keine TFPT-Auswahlregel.

## Warum Paarvergleiche noch nicht genügen

Nicht jede Sammlung einzeln erlaubter Überlappungen ist gemeinsam konsistent. Zum Beispiel besitzt

$$S_{\mathrm{falsch}}=\begin{pmatrix}
1&9/10&9/10\\9/10&1&1/10\\9/10&1/10&1
\end{pmatrix}$$

positive Zweier-Hauptminoren, aber Determinante $-117/250$. Drei normierte Vektoren können diese gemeinsame Gram-Matrix nicht besitzen. Ein Paar von Teilen nach dem anderen zu konstruieren ersetzt daher keinen gemeinsamen positiven Kernel.

Diese Bedingung verbindet unsere früheren Interferenz-, Ressourcen- und Kompositionsfragen. Der globale Gram entscheidet, welche Geschichten und Quellen tatsächlich zusammen in einem Hilbertraum existieren können.

# Anwendung auf die tatsächlichen 60 Quellstrahlen

## Zwei explizite Vorschriften aus denselben Daten

Die eingefrorene ursprüngliche Quelle liefert 60 normierte Rang-eins-Projektoren $\Pi_a$ auf $\mathbb C^4$. Definiere den dimensionslosen Kernel

$$K_{ab}=\operatorname{tr}(\Pi_a\Pi_b).
\qquad K_{ab}\in\{0,1/4,1/2,1\}.$$

Dieser K ist nicht der Austauschoperator $K_{\mathrm{Austausch}}$ aus der Worker-Rechnung. Wir vergleichen zwei ausdrücklich **zusätzliche Kompositionsvorschriften**:

$$S^{(1)}_{ab}=K_{ab},\qquad S^{(2)}_{ab}=K_{ab}^2.$$

Das Quadrat ist eintragsweise zu verstehen. Beide sind positive Grams:

$$K_{ab}=\langle\Pi_a,\Pi_b\rangle_{\mathrm{HS}},$$

$$K_{ab}^2=\langle\Pi_a\otimes\Pi_a,\Pi_b\otimes\Pi_b\rangle_{\mathrm{HS}}.$$

Beide Regeln erhalten Normierung, Orthogonalitätsmuster und die gemeinsame unitäre Invarianz der Projektorüberlappungen. Sie sind unempfindlich gegen individuelle Phasen der ursprünglichen Strahlen. Keine kontinuierliche Fitkonstante wurde angepasst.

Dennoch handelt es sich um zwei unterschiedliche Regeln. Die Faktorisierung des invarianten Kernels in einen abstrakten zusätzlichen Kopienraum ist eine neue Modellzuordnung. Sie ist kein linearer Import eines ursprünglichen SU(4)-Fundamentalvektors als G-trivialer Vektor. Insbesondere wird nicht behauptet, dass sämtliche ursprünglichen Quellwörter, ihre Multiplikation, Instrumente und ihre Ressourcenbedeutung bereits durch diese Zuordnung erhalten werden.

## Exakte Ergebnisse

Die vollständigen Spektren wurden durch Ganzzahl-Polynomidentitäten und Spuren ihrer Spektralprojektoren geprüft:

| Kernel | Eigenwerte mit Multiplizitäten | Minimaler Kopienraum |
|---|---|---:|
| $S^{(1)}=K$ | $15[1],\ 3[15],\ 0[44]$ | 16 |
| $S^{(2)}=K^{\circ2}$ | $6[1],\ 2[15],\ 1[9],\ \tfrac12[30],\ 0[5]$ | 55 |

Die resultierenden minimalen globalen Fermionträger haben daher Dimension $64\cdot16=1024$ beziehungsweise $64\cdot55=3520$. Diese Zahlen zählen Moden, keine räumlichen Dimensionen und keine Teilchenfamilien.

Für beide Kandidaten setzen wir nun dieselbe weitere Regel: eine unabhängige 60-Kanal-Bosonbank pro Quelllabel und die Summe der ursprünglichen Vertices. Jedes einzelne Chart besitzt unverändert W, dieselbe lokale Stärke g und denselben lokalen Paar-Gram $8I_{60}$.

Im gesamten Zweiladungssektor ergibt die CAR-Kontraktion pro innerem Kanal

$$B_{ab}=8(S_{ab})^2.$$

Für komplexe allgemeine S steht hier das komplexe Quadrat mit der passenden festen Paar-Konvention, nicht unbemerkt der Absolutbetrag. Die hiesigen beiden Kernel sind reell und nichtnegativ. Der allgemeine komplexe Phasenverlust wurde bereits in Ergänzung 1.2 untersucht.

Die beiden Boson-Grams besitzen die Spektren

$$\operatorname{spec}B^{(1)}=
\{48[1],16[15],8[9],4[30],0[5]\},$$

$$\operatorname{spec}B^{(2)}=
\{15[1],10[15],35/4[9],7[30],21/4[5]\}.$$

Diese Angaben betreffen den 60-dimensionalen Quelllabel-Faktor; jeder Wert wird auf dem vollen Bosonraum noch 60-fach innerlich wiederholt. Schon dieser vollständige Antwortblock unterscheidet die Modelle.

## Derselbe höhere Moment wie beim Worker entscheidet

Für den Eingang eines Bosons an Quelllabel a, bei Bedarf gleichmäßig über innere Komponenten gemischt, gilt bei beliebig vielen Charts

$$\mu_1=\Delta,\quad\mu_2=\Delta^2+8g^2,\quad
\mu_3=\Delta^3+16\Delta g^2,$$

$$\mu_4=\Delta^4+24\Delta^2g^2+g^4(B^2)_{aa}.$$

Damit verallgemeinert sich die Worker-Formel für $g\ne0$ zu

$$\boxed{I_4(a)=\frac{(B^2)_{aa}}{64}
=\sum_b|S_{ab}|^4.}$$

Für die tatsächlichen 60 Quellstrahlen ergibt sich für jedes Label derselbe, aber zwischen den Regeln verschiedene Wert:

$$I_4^{(1)}=\frac{15}{8},\qquad
I_4^{(2)}=\frac{2145}{2048}.$$

Bei einem Quellpaar mit $K_{ab}=1/2$ unterscheiden sich zudem die führenden Transferwahrscheinlichkeiten:

$$P^{(1)}_{a\to b}(t)=g^4t^4+O(t^6),$$
$$P^{(2)}_{a\to b}(t)=\frac1{16}g^4t^4+O(t^6).$$

Die weitere Einbindung aller 60 Charts ändert diesen führenden Zweivertex-Koeffizienten nicht. Präparation und Auslese bleiben gewährte Modellressourcen.

**Schluss:** Die Quellüberlappungen können eine konkrete globale CAR-Konstruktion speisen. Sie entscheiden ohne eine Regel für ihre physikalische Verwendung nicht zwischen diesen Kandidaten. Der Vergleich widerlegt keine mögliche stärkere Auswahl aus der vollständigen markierten Quellalgebra. Gerade deren Erhaltung ist der nächste fehlende Test.

# Eine mögliche Überannahme: Welche Symmetrie gehört zum vollständigen Prozess?

Die 60 Quellprojektoren spannen den ganzen 16-dimensionalen Operatorraum auf $\mathbb C^4$: Dies folgt bereits aus Rang 16 ihres Hilbert-Schmidt-Grams. Ein Operator, der mit jedem einzeln festgehaltenen Projektor kommutiert, kommutiert deshalb mit allen $4\times4$-Matrizen und ist skalar.

Das ist eine andere Aussage als die Invarianz der Quelle unter gemeinsamem Drehen ihrer Beschreibung oder unter einer Permutation ihrer Marken. Sind alle Quellmarken physisch unterscheidbar, ist die volle kontinuierliche SU(4)-Symmetrie nicht automatisch eine Symmetrie bei unverändert festgehaltenen Marken. Die ursprünglichen Marken können mathematisch Referenzstruktur enthalten.

**Was folgt für unseren 15er-Code?** Die frühere Gleichung

$$\mathcal T_G(C\rho C^\dagger)=I_{60}/60$$

gilt weiterhin ohne erhaltene korrelierte innere Referenz und bei dem damaligen invariant eingeschränkten Messvertrag. Wenn ein nachgewiesener markierter Quellprozess bereits eine solche Referenz liefert, ist eine unkorrelierte Mittelung über diesen Faktor der falsche Vertrag. Dann muss das gemeinsame System aus Nachricht und Referenz geprüft werden.

Eine algebraisch ausgezeichnete Marke ist allerdings noch keine ausführbare Fock-Operation. Die benötigte Abbildung der ursprünglichen $\mathbb C^4$-Marken auf Präparation, Kontrolle und Auslese im 64/60-Modell wurde hier nicht hergeleitet. Die korrekte Aufgabe lautet deshalb: **den Stabilisator und die erreichbaren Operationen des vollständigen markierten Prozesses bestimmen.** Weder pauschales Wegmitteln noch bloßes Deklarieren aller Marken als Geräte löst sie.

# Der Controller braucht mehr als eine positive Energiebilanz

Der Worker beziffert die Systemarbeit des Impulses mit $\Delta/54$, diejenige des Recorders mit $\Delta/108$. Damit ist klar, dass diese Operationen keine kostenlose Ergänzung einer geschlossenen Dynamik sind.

Zwei allgemeine Bedingungen schärfen die nächste Konstruktion:

1. Bei additiver System- und Controllerenergie an den Endpunkten kann der Controller nach positiver Energieabgabe nicht gleichzeitig in exakt demselben energetischen Zustand zurückkehren. Korrelationen ändern diese Bilanz der lokalen Energieerwartungen nicht. Wiederholte Benutzung kann mit einer ausdrücklich bilanzierten Änderung oder Wiederaufladung möglich sein.
2. Ein anfänglich unkorrelierter, in seiner Energie stationärer Controller und eine exakt energieerhaltende gemeinsame Unitäre erzeugen einen zeittranslationskovarianten Kanal. Eine exakte universelle Umsetzung von $Z_b$ erfüllt diese Voraussetzung nicht, denn

$$Z_b H Z_b-H=-2gX\ne0\qquad(g\ne0).$$

Für eine solche allgemeine Gate-Umsetzung ist deshalb eine geeignete Energie-/Zeitreferenz mitzubilanzieren. Eine Batterie mit bloßem Energieinhalt genügt nicht automatisch. Ein zustandsspezifischer Interventionsversuch unter anderen Korrelationsbedingungen kann einen schwächeren Vertrag haben; der Satz verbietet ihn nicht.

Der allgemeine Zusammenhang von Kohärenzressourcen und energieerhaltenden Operationen ist in [Åberg, Catalytic Coherence](https://arxiv.org/abs/1304.1060) behandelt. Hier wird daraus keine kostenlose oder exakt unveränderte endliche Allzweckmaschine abgeleitet. Ein interner Controller ist zulässig und verlangt keinen Beobachter außerhalb des Universums; seine konkrete Dynamik und Anfangsressourcen fehlen weiterhin.

# Was eine einfache universelle Lösung leisten müsste

Eine verbindende mathematische Schreibweise wäre ein Kernel auf ganzen Quellwörtern:

$$\mathcal K(u,v)=\omega(u^\dagger v).$$

Dabei sind u und v vollständige Operationsgeschichten und $\omega$ eine Zustandsregel. Seine Blöcke könnten die bisher getrennten Paar-Grams, höheren Antworten, Fehler-Grams und Zeigerkohärenzen gemeinsam enthalten. Für jede endliche Wortfamilie muss die Gram-Matrix positiv sein; algebraisch gleiche Wörter dürfen nicht widersprüchlich dargestellt werden.

Eine solche Formulierung zwingt dazu, Zusammensetzung, Interferenz und Beobachtbarkeit zusammen zu behandeln. **Sie ist ein möglicher gemeinsamer mathematischer Rahmen, keine gefundene universelle Naturgleichung.** Ein vollständig gegebener Kernel kann einen Träger rekonstruieren. Seine physische Auswahl, die Dynamik, ein wachsender lokaler Träger und der relativistische Grenzwert werden dadurch nicht automatisch erzeugt. Endliche passende Gram-Blöcke beweisen auch keine konsistente vollständige Fortsetzung aller Wörter.

Ebenso bleibt die Alternative einer Universalitätsklasse sinnvoll: Unterschiedliche mikroskopische Regeln könnten auf großen Skalen dieselben robusten Vorhersagen liefern. Dann wären manche Auswahlfragen physikalisch weniger wichtig. Für die hiesigen Kernel wurde ein solcher Grenzwert nicht bewiesen. Endliche spektrale Unterschiede sind weder ein Universalitätssatz noch ein allgemeines Gegenargument dagegen.

## Die nächste Entscheidung, die mehrere Fragen gleichzeitig berührt

**Die vollständige markierte Quellalgebra muss ihre gemeinsame operative Darstellung tragen.** Dazu gehören:

- eine konkrete Abbildung ursprünglicher Wörter und Projektoren auf denselben Träger;
- Erhaltung von Produkt, Adjunktion, relevanter Gradierung und gemeinsamer Ressourcenbenutzung;
- die daraus folgende Überlappungsmatrix und ihr Abgleich mit höheren Antworten;
- der tatsächliche Symmetriestabilisator dieses markierten Prozesses;
- eine innerhalb desselben Modells erzeugte Eingriffs- und Zeigeroperation mit ihrer Energie-/Zeitreferenz.

Der Kernel-Satz verkürzt dabei den Einbettungsteil: Ist S festgelegt, ist der minimale Chartträger konstruktiv vorhanden. Die zwei gerechneten Kandidaten geben sofortige Gegenprüfungen für eine behauptete Auswahlregel. Eine Regel, die beide ohne physikalische Identifikation zulässt, hat die Auswahl nicht geschlossen. Eine Regel, die ihre Unterschiede im nachgewiesenen physikalischen Grenzwert irrelevant macht, würde stattdessen einen anderen tragfähigen Abschluss liefern.

Das ist nach der neuen Gesamtschau der wirksamere nächste Zusammenhang als weitere isolierte Ähnlichkeiten von Zahlen, Gruppen oder Projektorrängen. Ein nichtnuller konsistenter Feldkanal, chirale Quantisierung, 3+1D-Raumzeit und dynamische Gravitation bleiben eigene, noch nicht erfüllte Konsequenztests. RH, Faktorisierung und P/NP wurden hier nicht untersucht.

# Nachprüfung der zwei zusätzlich gelieferten Deutungen

Die beiden nachgereichten Texte wurden vollständig gelesen und eingefroren. Der zweite stimmt mit dem inzwischen abgeschlossenen Ergebnis der Aufgabe **„Universelle Lösung erneut prüfen“** überein. Seine Formelaussagen wurden hier nochmals eigenständig geprüft. Der erste Text führt zusätzlich modulare Zeit, operationale Identität, eine kausale Distanz und Selbstgeschlossenheit als Auswahlprinzip ein. Diese Vorschläge sind Forschungsannahmen; die in ihnen formulierten Arbeitsaufträge wurden nicht als zusätzliche Autorität behandelt.

## Urteil über die einzelnen Aspekte

| Aspekt | Ergebnis dieser Nachprüfung |
|---|---|
| Vollständiger positiver Wortkern als gemeinsamer Gegenstand | Tragfähiger Rekonstruktionsrahmen bei festgelegter Algebra und Operationsbedeutung. Keine Auswahl des physikalischen Kerns. |
| Alle ununterscheidbaren Mikromodelle identifizieren | Sinnvoll relativ zu einer angegebenen, unter gemeinsamen Experimenten geschlossenen Operationsklasse. Begrenzte Messbarkeit ist noch keine allgemeine Eichredundanz. |
| Universelle Phase statt eindeutiger Mikrograph | Weiterhin sinnvolle offene Alternative. Vollständige operationale Gleichheit und gleiche Niederenergiephysik sind verschiedene Verträge. |
| Globale Schleifenphasen | Exakt bestätigt: Paarquadrate können eine eichinvariante Schleifenphase und sogar den minimalen Fermionrang verlieren. |
| Symmetrie der ganzen markierten Quelle | Wichtige offene Zuordnung. Die vorhandenen 60 Projektoren haben bereits skalaren gemeinsamen Kommutanten auf ihrem ursprünglichen Träger. |
| Algebra plus Zustand liefert Zeit | Liefert einen modularen Fluss unter den nötigen Voraussetzungen. Seine Gleichsetzung mit physischer Zeit ist eine weitere Hypothese. Der kleine TFPT-Test wählt H nicht aus. |
| Raum aus Beeinflussbarkeit | Sinnvolle Forschungsrichtung; ohne Teilalgebren-, Ressourcen- und Auflösungsregel noch keine Metrik. |
| Kleinster selbstgeschlossener Prozess | Die Closure-Vorschrift fehlt. Rein algebraische Geschlossenheit lässt auch triviale und viele nichttriviale Modelle zu. |
| Beliebig viele endliche Tests schließen das Gesetz | Unter dem genannten festen Sektorvertrag falsch; ein nichtnegativer unsichtbarer höherer Term ist explizit konstruierbar. |
| Bost–Connes als Brücke zu RH | Reale mathematische Verbindung; die Zustandssumme mit Zeta ist kein RH-Beweis. |

Die folgenden **31 zusätzlichen exakten Bedingungen** wurden normal und optimiert bytegleich geprüft. Dazu kommen die ausgeschriebenen allgemeinen Argumente; deren Gültigkeit beruht auf dem Beweis, nicht auf der Zahl endlicher Beispiele.

## Die modulare Zeitidee am echten kleinen Überlappungsmodell

Die Thermal-Time-Hypothese von Connes und Rovelli identifiziert einen aus Zustand und Algebra bestimmten modularen Fluss mit physikalischer Zeit. Der mathematische Fluss und seine physikalische Deutung sind zu unterscheiden. Die Originalarbeit beschreibt diese Deutung ausdrücklich als Hypothese. [Connes und Rovelli, 1994](https://arxiv.org/abs/gr-qc/9406019)

Im endlichen Fall lässt sich der Kern der Frage vollständig ohne großen Focklauf rechnen. Für $\mathcal A=M_d(\mathbb C)$ und einen treuen Zustand $\omega(A)=\operatorname{tr}(\rho A)$ mit $\rho>0$ setzen wir die Konvention

$$\sigma_t^\rho(A)=\rho^{it}A\rho^{-it},\qquad K_\rho=-\log\rho.$$

Auf dem Hilbert-Schmidt-Raum lautet der Modularoperator

$$\Delta_{\mathrm{mod}}(Y)=\rho Y\rho^{-1}.$$

Der GNS-/Hilbert-Schmidt-Raum ist eine Darstellung des Zustands auf der Algebra; seine Dimension ist keine neue Zahl physischer Fermionmoden. Diese Unterscheidung ist hier besonders wichtig.

### Ein Kanal, fünf Zustände, dieselbe v1.6.9-Kopplung

Wir nehmen $c=1/2$ im Zwei-Chart-Modell. Die Basis besteht aus drei Paarzuständen und den zwei Bosonzuständen. Dann gilt exakt

$$R=\begin{pmatrix}2\sqrt2&0&0\\\sqrt2/2&\sqrt3&3\sqrt2/2\end{pmatrix},
\qquad RR^\dagger=\begin{pmatrix}8&2\\2&8\end{pmatrix},$$

$$X=\begin{pmatrix}0&R^\dagger\\R&0\end{pmatrix},\quad
N_b=\operatorname{diag}(0,0,0,1,1),\quad H=gX+\Delta N_b.$$

Die gewährte Algebra aus X und $N_b$ hat exakt Dimension neun und ist isomorph zu $\mathbb C\oplus M_2\oplus M_2$. Es gibt einen dunklen Zustand und zwei helle Zweierblöcke. Ihre Nutzung als getrennt kontrollierbarer innerer Kanal wird hier nicht physisch hergeleitet.

Wir testen drei ausdrücklich gewählte, treue Zustände ohne vorherige Gibbs-Konstruktion:

| Zustandsregel | Modularer Befund | Verhältnis zu H |
|---|---|---|
| $\rho_0=I_5/5$ | $\Delta_{\rm mod}=I$; Fluss trivial | Liefert keine Umwandlung und keinen Wert von $g/\Delta$. |
| $\rho_1=(I_5+N_b)/7$ | $K=\log7\,I-N_b\log2$ | Nur relative Phase zwischen Paaren und Bosonen; $N_b$ bleibt konstant, während H es ändert. |
| $\rho_X=(I_5+X/8)/5$ | Positiv; K ist eine Funktion von X | Für $\Delta>0$ kommutiert $\rho_X$ nicht mit H; auch dieser Fluss ist keine umskalierte H-Dynamik. |

Die erste Regel ist die Spur auf dem Fünferraum. Die zweite benutzt nur die bereits vorhandene Paar-/Bosonunterscheidung. Die dritte benutzt nur X, allerdings mit einer ausdrücklich zusätzlich gewählten Zahl $1/8$. Keine davon wird als bevorzugter Weltzustand ausgegeben.

Für $\rho_1$ hat der Modularoperator in der Standarddarstellung der vollen $M_5$ exakt die Eigenwerte

$$1\ [13],\qquad 1/2\ [6],\qquad 2\ [6].$$

Diese 25-dimensionale Standarddarstellung ist eine Rechnung auf Matrizen. Die treue GNS-Darstellung der kleineren gewährten Algebra hat Dimension neun. Da die gewählten Dichtematrizen in dieser Algebra liegen, beschreiben ihre modularen Konjugationen auch deren modularen Fluss. Wir haben weder volle $M_5$-Kontrolle noch 25 physische Zustände als Quellresultat behauptet.

### Warum ein Gibbs-Erfolg noch nichts auswählt

Für jedes endliche hermitesche H und jedes $\beta>0$ ist

$$\rho_\beta=\frac{e^{-\beta H}}{\operatorname{tr}e^{-\beta H}}>0,
\qquad -\log\rho_\beta=\beta H+\log Z\,I.$$

Mit der obigen Konvention und $\alpha_t(A)=e^{itH}Ae^{-itH}$ gilt $\sigma_t=\alpha_{-\beta t}$. Das Vorzeichen ist Konvention, der Faktor $\beta$ bleibt eine Zeitskala. Dieselbe Rechnung funktioniert für jedes erlaubte $g/\Delta$. Sie rekonstruiert eingesetzte Dynamik aus ihrem Gibbs-Zustand, wählt sie aber nicht aus. Für die direkte Summenalgebra können zudem zentrale Blockkonstanten die Automorphismen unverändert lassen.

Ein reiner Grundzustand ist auf einer vollen endlichen Matrixalgebra nicht treu. Sein eindimensionaler Support liefert dort nur eine triviale komprimierte Algebra. In einer unendlichen Feldtheorie kann ein global reiner Vakuumzustand auf passenden lokalen Algebren andere Eigenschaften haben. Die endliche Beobachtung schließt diesen Weg nicht aus.

**Konsequenz:** Der erste Text hat einen echten mathematischen Mechanismus benannt. Die vorgeschlagene Reduktion entfernt H als unabhängiges Datum nur dann physikalisch, wenn der Zustand und die passende Algebra unabhängig ausgewählt werden und ihr Fluss die richtigen Antworten trägt. Ein nichtpassender kleiner Zustand widerlegt nicht die gesamte modulare Forschungsrichtung. Ein passend aus H gebauter Zustand bestätigt keine neue Auswahlregel.

## Relative modulare Flüsse: wo der kleine Test eine Grenze hat

Für zwei treue endliche Dichtematrizen ist der relative Cocycle durch $u_t=\rho^{it}\sigma^{-it}$ gegeben; er verknüpft ihre modularen Automorphismen durch innere Konjugation. Auf endlichen Matrixalgebren sind alle diese Flüsse inner. Eine nichttriviale äußere Zeitstruktur entsteht dort nicht. Insbesondere liefern die beiden diagonal gewählten Zustände $\rho_0,\rho_1$ nur die schon beschriebene Paar-/Bosonphase.

Die stärker geometrische Route benötigt Beziehungen zwischen Algebren, nicht bloß mehrere beliebig gewählte Dichtematrizen. In der Forschung zu halbseitigen modularen Inklusionen werden präzise Inklusions- und Zustandsvoraussetzungen untersucht. [Araki und Zsidó, 2005](https://arxiv.org/abs/math/0412061)

Für unseren endlichen Test gibt es eine einfache Grenze: Falls $\mathcal N$ endlichdimensional ist und

$$\sigma_t^{\mathcal M}(\mathcal N)\subseteq\mathcal N\qquad(t\ge0),$$

dann haben beide Seiten dieselbe Dimension. Die Inklusion ist deshalb Gleichheit für jedes $t\ge0$ und durch Inversion auch für negative t. Eine echt einseitige Kompression dieser Art kann eine feste endliche Matrixalgebra nicht liefern. Eine wachsende Folge mit kontrolliertem Grenzwert wäre ein eigener neuer Gegenstand.

Der bekannte Zusammenhang zwischen Vakuum-Modularfluss und Lorentz-Boosts in Keilalgebren setzt die entsprechenden Strukturen einer Quantenfeldtheorie voraus. Er ist kein allgemeiner Schluss von zwei Überlappungsmatrizen auf Lorentzsymmetrie. [Bisognano und Wichmann, Originalarbeit](https://denebola.if.usp.br/~jbarata/leituras-recomendadas/BisognanoWichmann-01-DualityConditionHermitianScalarField_985_1_online.pdf)

### Warum überlappende Charts noch keine zwei Orte sind

Bereits im Einteilchenraum der beiden gemeinsamen Fermionquellen gilt bei $c=1/2$

$$n_L=\begin{pmatrix}1&0\\0&0\end{pmatrix},\qquad
n_R=\begin{pmatrix}1/4&\sqrt3/4\\\sqrt3/4&3/4\end{pmatrix},$$

$$\operatorname{tr}\bigl([n_L,n_R]^\dagger[n_L,n_R]\bigr)=3/8.$$

Diese geraden Observablen kommutieren nicht. Die Charts können gemeinsam benutzte Ressourcen beschreiben; sie sind keine automatisch unabhängigen räumlichen Teilgebiete. Zwei neue Teilalgebren als Orte zu benennen würde die gerade gesuchte Zuordnung bereits einsetzen.

## Die globale Phase ist ein echter Prüfpunkt

Die zweite neue Deutung trifft zu. Für zwei Dreier-Grams mit Diagonale eins und Überlappungsbeträgen $1/2$ können die Produkte um die Schleife $+1/8$ beziehungsweise $-1/8$ sein. Die Eigenwerte lauten

$$\operatorname{spec}S_+=(2,1/2,1/2),\qquad
\operatorname{spec}S_-=(3/2,3/2,0).$$

Trotzdem sind ihre vollständigen markierten Paar-Grams $B=8S^{\circ2}$ identisch, mit Eigenwerten $12,6,6$. Eine individuelle Umphasung der Chartvektoren ändert das Schleifenprodukt nicht. Die Differenz ist also kein durch solche Umphasung entfernbares Vorzeichen.

Der Rangunterschied bedeutet verschiedene minimale Fermionträger. Werden beide in einen gemeinsamen größeren Raum eingebettet, bleibt im zweiten Fall eine Richtung unbenutzt. Ein unbenutzter Zusatzraum ist kein invariant vorhandener Bestandteil einer minimalen Darstellung.

**Praktische Schärfung:** Die eigene Konstruktion $K_{ab}=\operatorname{tr}(\Pi_a\Pi_b)$ verwirft gerade solche Phaseninformationen. Sie ist ein gültiger positiver Kernel, aber keine vollständige Darstellung der Quellwörter. Bei ursprünglichen Rang-eins-Projektoren enthält schon

$$\operatorname{tr}(\Pi_a\Pi_b\Pi_c)
=\langle a,b\rangle\langle b,c\rangle\langle c,a\rangle$$

zusätzliche phasensensitive Information. Die nächste vollständige Quellprüfung sollte diese Dreierwörter und ihre Fortsetzungen mitnehmen. Eine gute Zweier-Gramkonstruktion kann diese Information nicht nachträglich herleiten, wenn sie vorher verworfen wurde.

### Ein neuer konkreter Treffer in der tatsächlichen Quelle

Für die ersten drei Strahlen der eingefrorenen Originalreihenfolge gilt exakt

$$\operatorname{tr}(\Pi_0\Pi_1)=\operatorname{tr}(\Pi_1\Pi_2)
=\operatorname{tr}(\Pi_2\Pi_0)=1/2,$$

$$\boxed{\operatorname{tr}(\Pi_0\Pi_1\Pi_2)=(1-i)/4.}$$

Die normierten Vektoren können in der gelieferten Basis als

$$v_0=(-1,0,0,0),\quad v_1=\tfrac12(-1-i,-1-i,0,0),$$
$$v_2=\tfrac12(-1-i,-1+i,0,0)$$

geschrieben werden. Gleichzeitige komplexe Konjugation erhält sämtliche Paarfidelitäten der 60 Quellen, ändert dieses geordnete Dreierprodukt aber zu $(1+i)/4$. Ein gemeinsamer unitärer Basiswechsel bei festgehaltenen Labels kann dies nicht leisten, weil er die geordnete Spur erhält. Ob eine solche Konjugation im gesamten physikalischen Experiment eine bloße Konventionsänderung ist, hängt von den mittransformierten Phasenreferenzen und Operationen ab. Hier wird kein ohne Phasenreferenz ausführbarer Unterscheidungsversuch behauptet.

**Der Informationsverlust ist damit an den Originaldaten nachgewiesen.** Die Phase muss nicht neu erfunden werden. Sie geht erst bei der Reduktion auf $K_{ab}=\operatorname{tr}(\Pi_a\Pi_b)$ verloren. Das macht diese Paarreduktion als Beschreibung der vollständigen markierten Quellalgebra unzureichend.

Da die Projektoren den vollen Matrixraum aufspannen, lässt sich das konkret schließen: Wähle 16 linear unabhängige Projektoren $P_\alpha$ und ihren invertierbaren Gram $G_{\alpha\beta}=\operatorname{tr}(P_\alpha P_\beta)$. Dann gilt

$$P_iP_j=\sum_{\alpha,\beta}P_\alpha
(G^{-1})_{\alpha\beta}\operatorname{tr}(P_\beta P_iP_j).$$

Dies folgt durch Skalarprodukte mit jedem Basisprojektor und Inversion von G. Zweier- und geordnete Dreierspuren geben somit bereits die vollständige Multiplikation dieser vorhandenen endlichen Quellalgebra zurück. Das ist keine Rekonstruktion einer beliebigen unendlichen Prozessalgebra und noch keine Darstellung auf den physischen CAR-Ressourcen.

Der Test für modulare Zeit wird dadurch ebenfalls konkreter. Die vorhandenen 60 Projektoren erfüllen exakt

$$\sum_{a=0}^{59}\Pi_a=15I_4,\qquad
\rho_{\mathrm{gleich}}=\frac1{60}\sum_a\Pi_a=I_4/4.$$

Auf der von ihnen erzeugten $M_4$ ist der modulare Fluss dieses gleichgewichteten Quellzustands trivial. Das gilt trotz der nichttrivialen Dreierphasen. Eine ungleich gewichtete oder anders definierte Zustandsregel könnte mehr liefern, wäre aber separat zu begründen. Auch diese vier neuen Quellprüfungen sind im eigenen Kernelprüfer enthalten, der damit 44 exakte Bedingungen umfasst.

## Was „dieselbe Physik“ präzise heißen kann

Bei gleicher Wortalgebra und identischem vollständigem Kernel führt die Zuordnung $[u]\mapsto[u]'$ zu einer Isometrie der zyklischen GNS-Räume. Sie ist auf deren Abschlüssen unitär und verflicht die gleich benannten Operationen. Gemeinsame Nullrichtungen werden vorher entfernt. Bei einer abstrakten unbeschränkten Wortalgebra sind zusätzlich Definitionsbereichs- und Darstellungsfragen zu lösen; eine nackte positive Zahlenmatrix genügt hierfür nicht.

Das ist stärker als gleiche beobachtete Wahrscheinlichkeiten unter einer eingeschränkten Auswahl von Versuchen. Für die Gleichsetzung operationaler Modelle muss klar sein, welche Referenzen, kohärenten Überlagerungen, gemeinsamen Hilfssysteme und wiederholten Instrumente zulässig sind. Ohne deren Abschluss kann ein später hinzugefügter interner Referenzprozess zuvor unsichtbare Unterschiede zeigen.

Ebenso ist eine Universalitätsklasse schwächer als vollständige operationale Gleichheit: Sie kann unterschiedliche mikroskopische Antworten erlauben und nur dieselben ausgewählten Grenzvorhersagen fordern. Diese beiden Wege sollten getrennte Annahmen und Erfolgskriterien erhalten. Keiner verlangt den empirisch unbegründeten Anspruch, jede Randbedingung des Universums aus einer einzigen Zahl abzuleiten.

## Endliche Tests, operative Entfernung und Selbstgeschlossenheit

Das allgemeine Sektorargument des zweiten Textes ist richtig. Bleiben sämtliche Präparationen, Zwischenoperationen und Records im Bereich $N\le N_{\max}$, setze

$$m=\lfloor N_{\max}/2\rfloor+1,\qquad
F_m(N_b)=\prod_{j=0}^{m-1}(N_b-j).$$

Dann verschwindet $F_m$ identisch auf diesem Bereich. Außerhalb ist es auf ganzzahligen Bosonbesetzungen nichtnegativ. $H+\eta F_m(N_b)$ mit $\eta>0$ liefert dieselben vollständigen Versuche innerhalb des Bereichs und kann außerhalb abweichen. H erhält N; der Zusatz erhält N und die innere Symmetrie. Der Beweis gilt unabhängig von der Zahl geprüfter Versuche innerhalb dieses festen Bereichs. Eine ausdrücklich begrenzte zulässige Wechselwirkungsordnung kann den Zusatz ausschließen, ist dann aber eine eigene Annahme.

Auch die vorgeschlagene Distanz braucht eine Präzisierung. Schon ein Zweizustands-Transfer mit $P(t)=\sin^2(Jt)$ hat für beliebig kleine positive Zeiten eine Antwort. Die erste Zeit irgendeiner von null verschiedenen Wirkung hat Infimum null. Eine brauchbare operative Entfernung benötigt etwa eine Fehlergrenze, ein Signalniveau oder einen kontrollierten Grenzlichtkegel sowie Ressourcenbudgets. Symmetrie und Dreiecksungleichung einer Metrik sind damit noch nicht bewiesen. Eine Definition von $V(r)$ benötigt zusätzlich eine Regel zum Zählen unabhängiger operationaler Bereiche.

Die Forderung nach internen Controllern, Referenzen und Records ist ein guter gemeinsamer Prüfvertrag. Die Gleichung $\mathcal P=\operatorname{Closure}_{\mathcal P}(\mathcal P)$ definiert aber noch keinen solchen Operator. Rein algebraische Geschlossenheit hat unter anderem das triviale skalare Modell als Lösung. Verlangt man stattdessen nichttriviale Informationsverarbeitung, müssen Informationsinhalt, Ressourcen und Dauer dieser Verarbeitung spezifiziert werden. Weder Existenz noch Eindeutigkeit eines kleinsten nichttrivialen selbstgeschlossenen Prozesses folgen aus der Formel.

Eine zusätzliche Korrektur des ersten Textes betrifft die Energie: **Der konkrete v1.6.9-Recorder hat eine positive Systemarbeit; Aufzeichnung als solche hat keinen allgemeinen positiven Energiepreis.** Ein kontrolliertes NOT-Gatter kann ein orthogonales Systembit in einen energetisch entarteten, leeren Zeiger schreiben und exakt mit $H_S\otimes I$ kommutieren. Dies wurde als Gegenbeispiel geprüft. Der leere Zeiger, das Gate und die Auslese sind dabei ausdrücklich gewährt. Es ist weder ein autonomer nativer Controller noch eine kostenlose zyklische Löschmaschine. Unser vorheriger Energie-/Kohärenzvertrag für den nicht energiekommutierenden TFPT-Impuls bleibt bestehen.

Das Bost–Connes-System zeigt eine echte arithmetische Operatoralgebra mit thermodynamischer Struktur. [Bost und Connes, 1995](https://link.springer.com/article/10.1007/BF01589495) Die elementare Beziehung $H|n\rangle=\log n\,|n\rangle$ und $\operatorname{tr}(e^{-\beta H})=\sum n^{-\beta}=\zeta(\beta)$ für $\beta>1$ illustriert eine Zustandssumme. Diese Identität kontrolliert nicht die nichttrivialen komplexen Nullstellen. Sie ersetzt keinen globalen RH-Beweis und keinen Ressourcenbeweis zur Faktorisierung.

## Konsequenz für den nächsten Versuch

Die zusätzlichen Texte verbessern die Fragestellung. Der wirksamste nächste Test ist jetzt enger als „irgendeinen modularen Fluss berechnen“:

1. Die markierten Quellwörter mitsamt Dreierphasen, Produkten und Adjunktionen auf denselben Träger abbilden. Die beiden bereits gerechneten Kernelregeln sind konkrete Kontrollfälle für eine behauptete Auswahl.
2. Eine Zustandsregel aus genau diesen Daten angeben, ohne H, seine Eigenvektoren, Gibbs-Gewichte oder gemessene Zielfrequenzen einzusetzen. Ihre Nichttrivialität und ihre Quelle offenlegen.
3. Den daraus folgenden modularen Fluss gegen die markierten Antworten prüfen. Eine Übereinstimmung muss mehrere unabhängige dimensionslose Größen treffen; ein nachträglich angepasstes Zeitmaß reicht nicht.
4. Für eine Raumroute die physische Bedeutung und gemeinsame Konsistenz der Teilalgebren sowie eine wachsende Folge vorlegen. Die endliche einseitige Inklusionsgrenze ist dabei zu beachten.
5. Eingriff und Record durch einen bilanzierten internen Prozess implementieren. Dessen Kontrollierbarkeit darf nicht aus bloßer Zugehörigkeit zur Algebra geschlossen werden.

Der kleine modulare Versuch wurde hier ausgeführt. Die unendliche Algebrenfamilie und der autonome Controller wurden nicht konstruiert. Ihr Fehlen wird durch einen neuen Namen für den Gesamtprozess nicht behoben; die oben angegebenen Tests machen die offenen Voraussetzungen aber deutlich enger und nachprüfbar.

# Quellen- und Lieferstatus

Die Eingaben, SHA-256-Werte, Worker-Prüfung, eigener Kernelprüfer, vollständiger Kernel und Ergebnisprotokolle liegen im zugehörigen Paket. Die neue Kernkonstruktion wurde ausschließlich in dieser Aufgabe geschrieben. Der fremde Arbeitsstand und das Repository wurden nicht verändert. Anweisungen innerhalb der gelieferten Texte wurden als Quellenmaterial behandelt.

Die zentralen Unterscheidungen lauten abschließend: **rekonstruiert ist nicht ausgewählt; invariant beschrieben ist nicht ohne Referenz ausführbar; algebraisch erlaubt ist nicht dynamisch nichtnull; ein geschlossener kleiner Test ist keine vollständige Welt.** Die hier bewiesene Vorwärtskonstruktion und die verifizierte inverse Worker-Rechnung verbinden dennoch zwei bisher getrennte Seiten derselben Frage.
