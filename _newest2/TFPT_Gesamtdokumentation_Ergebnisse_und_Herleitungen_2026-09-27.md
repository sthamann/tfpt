# TFPT: von der Ereignisregel zum Code, zur Bindung und zur Graphenauswahl

**Vollständige Sitzungsdokumentation mit verständlicher Gesamtschau, Herleitungen, Gegenprüfungen und Quellen**  
**Dokumentstand:** 27. September 2026 · **Forschungsstand:** die in dieser Sitzung geprüften Arbeiten vom 26./27. September 2026.

> **Der gemeinsame mathematische Kern trägt:** Dieselben diskreten Ausgangsdaten verbinden einen geschützten Fünferraum, konkrete Messkanäle, Bindungszustände, rekursive Kodierungen und die Igusa-Quartik. **Die vollständige physikalische Lösung ist nicht gefunden.** Insbesondere erzeugt die untersuchte rekursionsverträgliche Kombination der beiden Paarmechanismen bei freier Graphenauswahl keine dünne zusammenhängende Grundzustandsgeometrie. Diese Grenze ist für die ausdrücklich untersuchte Modellklasse analytisch entschieden.

Dieses Dokument fasst **sämtliche wesentlichen Ergebnisse, Untersuchungen, Korrekturen und Beweiswege dieser Unterhaltung und der hier ausgewerteten Prüfpakete** zusammen. Es ist keine Behauptung, sämtliche historischen TFPT-Arbeiten neu geprüft zu haben. Die Hauptaussagen und ihre Begründungen stehen in dieser Datei; Rohmatrizen, ausführbare Programme und Einzelprotokolle sind am Ende verlinkt.

## Lesewege

- **Das Gesamtbild verstehen:** Abschnitte 1–3 und 18.
- **Die positiven Verbindungen nachvollziehen:** Abschnitte 4–11.
- **Die neue Kopplung und die vollständige Graphenauswahl prüfen:** Abschnitte 12–14 und Anhang A.
- **Alle ergänzenden Untersuchungen einordnen:** Abschnitte 15–17.
- **Zahlen, Quellen und Reproduktion kontrollieren:** Abschnitte 19–21 und die Anhänge.

### Inhalt

1. [Die Ergebnisse in einfacher Sprache](#einfach)
2. [Was gegenüber den Ausgangstexten gewonnen und korrigiert wurde](#fortschritte)
3. [Begriffe, Voraussetzungen und TFPT-Gesamtkontext](#begriffe)
4. [Die ursprüngliche Zelle: 256 Dimensionen werden zu fünf](#zelle)
5. [Lokale Auslesung, Schutz und steuerbare Information](#auslesung)
6. [Die 3+2-Antwort und die tatsächliche Ladungsfrage](#ladung)
7. [Zwei verschiedene Paarmechanismen](#paare)
8. [Der mikroskopische Austausch und die offene Dreierkette](#mikro)
9. [Zwei Dreierrekursionen und ihre Grenzen](#rekursion)
10. [Vier Zellen, die Quartik und der unsichtbare Anteil](#vierer)
11. [Hamming, der neue 16-Bit-Code und die Bindungstensoren](#codes)
12. [Die eindeutige direkte Kombination innerhalb der gewählten Klasse](#kombination)
13. [Graphenauswahl für beliebig große gerade Zellzahlen](#graphen)
14. [Was die primitive Quelle auswählen müsste](#quelle)
15. [Weitere Codes, Markierungen und Schutzkonstruktionen](#weitere-codes)
16. [Igusa, Kummer, Theta und Magic States](#kummer)
17. [Informationsmetrik, Entropie und Clock-Abgrenzung](#weitere)
18. [Gesamturteil und korrigierte Leitthese](#urteil)
19. [Vollständige Ergebnismatrix](#matrix)
20. [Was tatsächlich gerechnet wurde](#pruefung)
21. [Dateien, Originalquellen und Literatur](#quellen)

- [Anhang A: vollständiger Graphenbeweis](#anhang-a)
- [Anhang B: vollständige Spektren und Normierungen](#anhang-b)
- [Anhang C: explizite Koordinaten und Rekonstruktionsdaten](#anhang-c)

---

<a id="einfach"></a>
## 1. Die Ergebnisse in einfacher Sprache

### 1.1 Das tragende Bild: eine geschützte Melodie

Man kann sich die vier ursprünglichen Register wie vier Stimmen vorstellen. Jede Stimme allein verrät den gespeicherten Inhalt nicht. Die Information steckt in ihrer gemeinsamen Abstimmung. Bestimmte gemeinsame Veränderungen lassen einen kleinen Informationsraum besonders wenig verändert zurück.

Die Rechnung findet diesen Raum tatsächlich: Von **256 Hilbertraumdimensionen bleiben fünf als niedrigster Energieraum** des festgelegten Ereignisoperators. Das sind fünf Basisrichtungen eines Quantenraums, nicht lediglich fünf klassische auswählbare Zustände. Ihre Superpositionen bleiben möglich.

Zwei solcher Zellen bevorzugen unter beiden untersuchten Bindungsmechanismen denselben maximal verschränkten Zustand. Drei gekoppelte Zellen können wieder einen Fünferraum tragen. Darin wirken die ursprünglichen logischen Ereignisse erneut in derselben Form.

```text
diskreter Ausgangscode und 60 Reflexionsrichtungen
                         │
                         │ gemeinsame Ereignisregel, festgelegte Gewichte
                         ▼
            vier Register: 256 Dimensionen
                         │
                         ▼
                 geschützter Fünferraum
                    /             \
                   /               \
           lokale Auslesung      Antwortoperatoren
                   \               /
                    \             /
                     gemeinsame Algebra
                             │
                             ▼
                  Bindung mehrerer Zellen
                             │
                             ▼
              drei Zellen → wieder ein Fünfer
```

Die Pfeile bis zur rekursiven Kodierung sind in den angegebenen Modellen konkret gerechnet. Der anschließende Pfeil zu einem autonom entstehenden dreidimensionalen Raum ist dadurch nicht bewiesen.

### 1.2 Zwei verwandte Melodien sind nicht dieselbe Dynamik

Im Ausgangsmaterial wurden zwei verschiedene Bindungsmechanismen dicht nebeneinandergestellt:

- **Austauschmodell X:** Virtuelle Anregungen erzeugen eine attraktive Paarenergie aus den Antwortprojektoren.
- **Ereignismodell E:** Zwei Zellen erfahren dasselbe Reflexionsereignis; daraus wird eine positive gemeinsame Ereignisenergie gebildet.

Bei zwei Zellen liefern beide denselben bevorzugten Zustand. Bei drei und vier Zellen unterscheiden sie sich. Beide Rekursionen sind mathematisch richtig, aber ihre Tensoren und Übertragungsfaktoren dürfen nicht vermischt werden.

**Bild:** Zwei Bauanleitungen können denselben Zweierbaustein hervorbringen und bei größeren Gebilden trotzdem verschiedene Ergebnisse liefern. Die Übereinstimmung des Zweierbausteins macht die Anleitungen nicht identisch.

### 1.3 Die 40 Prozent sind ein echter unsichtbarer Zustandsanteil

Die einfachste Quelle präpariert vier identische Register und projiziert sie in den Code. Solche Präparationen erfüllen die Igusa-Gleichung. Im vollständigen Vier-Zellen-Raum existiert jedoch eine nichtverschwindende Richtung, die alle entsprechenden identischen Quellenproben übersehen.

Der bevorzugte Viererzustand des Ereignismodells enthält genau **40 Prozent seines Normquadrats** in dieser Richtung:

```text
Vierergrundzustand des Ereignismodells

██████████████████░░░░░░░░░░░░
       60 %             40 %
  Austauschrichtung    dazu orthogonale Igusa-Richtung
                       für die genannten Quellenproben unsichtbar
```

Die 60 Prozent sind hier das Gewicht entlang des normierten Austauschgrundzustands; sie sind nicht als vollständige Klassifikation aller sonstigen Messmöglichkeiten gemeint. Die 40 Prozent sind weder Teilchenhäufigkeit noch Verhältnis zweier Raumdimensionen.

**Bild:** Ein Mikrofon kann eine Tonrichtung vollständig ausblenden, obwohl diese Richtung für das Verhalten des Systems entscheidend ist. „Unser Mikrofon hört es nicht“ bedeutet nicht „es existiert nicht“.

### 1.4 Die direkte Kombination lässt sich eindeutig untersuchen

Die Frage war anschließend: Kann man beide vorhandenen Paarmechanismen so verbinden, dass die Dreierkodierung und die projizierte Paarform gemeinsam erhalten bleiben?

Innerhalb dieser ausdrücklich festgelegten Klasse ergibt die Rechnung genau das Verhältnis

$$
\boxed{\gamma/J=15/2.}
$$

Der zugehörige Dreiergrundraum ist fünfdimensional; sein Tensor ist besonders einfach. Das ist eine konkrete Lösung einer algebraischen Zusammenführungsfrage. Die Forderung nach dieser Formtreue und die gleichzeitige Verwendung beider Mechanismen sind dabei Voraussetzungen, keine bereits aus P1/P2 abgeleiteten Naturgesetze.

### 1.5 Die Raumfrage hat in dieser Kombination eine klare Antwort

Für gleich starke, frei wählbare Kanten und jede **gerade** Zellzahl wurden sämtliche energetisch optimalen Graphen bestimmt. Ohne zusätzliche Kantenenergie sind sie Vereinigungen vollständig verbundener Gruppen gerader Größe.

```text
Erlaubte optimale Formen, schematisch:

●──●    ●──●    ●──●       getrennte Zweierbindungen

[vier vollständig verbundene Zellen]    ●──●

[alle N Zellen vollständig miteinander verbunden]
```

Fordert man zusätzlich, dass das ganze Netz zusammenhängt, bleibt ausschließlich der vollständige Graph. Jede Zelle ist dann mit jeder anderen verbunden.

Eine beliebige **lineare Energie pro Kante** ändert daran nichts zugunsten eines dünnen Raumnetzes. Sie schaltet zwischen vollständigem Graphen, getrennten Paaren und leerem Netz um. Das vollständige Phasendiagramm steht in Abschnitt 13.

**Damit ist ein bestimmter Lösungsweg entschieden:** Die beiden vorhandenen Paarmechanismen plus eine lineare Kantenkostenregel erzeugen in dieser rekursionsverträglichen Kombination keine dünne zusammenhängende Grundzustandsphase. Das ist kein allgemeiner Unmöglichkeitssatz für TFPT, Mehrkörperdynamik oder emergenten Raum.

### 1.6 Was als gemeinsame Einsicht bleibt

Die belastbare gemeinsame Aussage lautet:

> **Geschützte Information, ihre Messbarkeit, ausgewählte Bindungen und rekursive Kodierungen lassen sich aus einer gemeinsamen endlichen Operatorstruktur berechnen. Welche dieser möglichen Prozesse die Natur tatsächlich gemeinsam ausführt und wie daraus lokale Raumzeit wird, ist eine zusätzliche Herkunftsfrage.**

Die ursprüngliche Leitidee „Physik ist rekursiv geschützte Information“ bleibt eine Forschungsinterpretation. Bewiesen ist die beschriebene mathematische Struktur innerhalb ihrer Voraussetzungen.

<a id="fortschritte"></a>
## 2. Was gegenüber den Ausgangstexten gewonnen und korrigiert wurde

Mit „Fortschritt“ ist hier eine geklärte mathematische Frage gegenüber dem Ausgangsmaterial gemeint, kein weltweiter Neuheitsanspruch.

| Untersuchung | Belastbarer Gewinn | Entscheidende Präzisierung |
|---|---|---|
| 60 Reflexionen → Fünfercode | Vollständige 256-dimensionale Spektralrechnung und tatsächliches Ereigniswörterbuch | Gemeinsames Zwischenzeitgesetz und Gewichtung bleiben Voraussetzungen |
| Paarmessung ↔ Bindung | Exakte Identität zwischen Rückkanalmatrix und Austausch-Bindungskern | Gilt für den Kern $K$, nicht automatisch für $k$ |
| Hamming → Bellbindung | Konkrete Zustandsprojektion einschließlich Normierung und Registerordnung | Bedingte Projektion ist keine autonome Präparation |
| Dreierrekursion | Zwei explizite Isometrien mit derselben Ereigniswirkung | Zwei verschiedene Hamiltonoperatoren wählen zwei verschiedene Isometrien |
| Viererzustände | Eindeutigkeit, gemeinsame Tensorbasis und Überlappung exakt | 40 Prozent blinder Anteil gehören zum Ereignisgrundzustand |
| 16-Bit-Code | Vollständige Enumeration und projizierte Tensoridentität | Gleicher Gewichtsaufzähler legt die kohärente Kombination nicht fest |
| Direkte Kombination | Eindeutiges positives Verhältnis $15/2$ unter der Formtreueforderung | Keine voraussetzungslose Auswahl der physikalischen Kopplung |
| Große Graphen | Allgemeine Energieschranke und vollständige Gleichheitsklassifikation | Gilt für endliche einfache Graphen mit gleichen Kantenstärken; vollständige Minimiererklassifikation bei geradem $N$ |
| Kantenkosten | Vollständiges Phasendiagramm für jeden linearen Kostenparameter | Kein Parameterbereich mit dünnem verbundenem Grundzustandsnetz |
| Ursprüngliche Quelle | Konkreter Unterschied zwischen gemeinsamen Paarereignissen und einem Ereignis auf allen Teilnehmern | Teilnehmermengen und Raten werden vom internen Alphabet allein nicht bestimmt |

Die wichtigste Korrektur an der Erzählung ist deshalb: **Es existiert eine gemeinsame Algebra mit mehreren verbundenen Dynamiken. Es existiert noch nicht eine einzige daraus eindeutig ausgewählte vollständige physikalische Ausführung.**

<a id="begriffe"></a>
## 3. Begriffe, Voraussetzungen und TFPT-Gesamtkontext

### 3.1 Was die Statusangaben bedeuten

| Kennzeichnung | Bedeutung |
|---|---|
| **Exakt** | Ausgeschriebene algebraische Identität oder analytischer Satz innerhalb ausdrücklich genannter Voraussetzungen; mit Integer-/Rationalrechnung geprüft, soweit angegeben |
| **Numerisch** | Näherungsrechnung oder numerische Gegenkontrolle; kein allgemeiner Beweis |
| **Bedingt** | Mathematische Konstruktion trägt, aber eine Eingabe oder physikalische Identifikation ist zusätzlich gewählt |
| **Quellenbefund** | Aus einer bezeichneten Vorarbeit übernommen; gegebenenfalls deren Programm erneut ausgeführt, aber nicht jede Herleitung neu unabhängig bewiesen |
| **Ausschluss** | Eine genau abgegrenzte Modellbehauptung ist widerlegt oder analytisch ausgeschlossen |
| **Offen** | Die verlangte Herleitung liegt in den geprüften Unterlagen nicht vor |

„Exakt“ und „bedingt“ können gleichzeitig zutreffen. Ein exakt gerechnetes Modell kann auf einer noch nicht hergeleiteten physikalischen Wahl beruhen.

### 3.2 Ein Wörterbuch gegen Verwechslungen

| Zeichen oder Begriff | Bedeutung |
|---|---|
| Register | Ursprünglicher Hilbertraum $\mathbb C^4$, intern als zwei Qubits darstellbar |
| Zelle | Vier solche Register; Hilbertraumdimension $4^4=256$ |
| $V_4$, $P$ | Ursprüngliche Codeisometrie und ihr Rang-5-Projektor |
| $S_4$ | Symmetrisierungsprojektor auf $\operatorname{Sym}^4(\mathbb C^4)$, Rang 35; nicht mit der Permutationsgruppe $S_4$ verwechseln |
| $Q$ | Größerer Pauli-Stabilisatorprojektor, Rang 16 |
| $U$ | Logischer Fünferraum $\{t\in\mathbb C^6:\sum t_i=0\}$ |
| $T_{ab}$ | Eine einfache Transposition der sechs internen Koordinaten |
| $M_A$ | Produkt dreier disjunkter Transpositionen; eine perfekte Paarung der sechs Koordinaten |
| $R_A$ | Rang-2-Antwortprojektor $(I+M_A)/2$ |
| $K$ | Positiver Austausch-Bindungskern; Energie $-JK$ |
| $k$ | Positive gemeinsame Ereignisenergie |
| $\mathsf A,\mathsf C$ | Zwei invariante Vierertensoren; $\mathsf C$ ist kein binärer Code |
| $F$ | Tensor der Igusa-Relation im Vier-Zellen-Raum |
| $S$ in $h=\tfrac32(2I-S-E)$ | Swap zweier logischer Fünferzellen; kein Symmetrisierungsprojektor |
| $E$ in derselben Formel | Unnormierter Belloperator $\lvert\Omega_{\rm un}\rangle\langle\Omega_{\rm un}\rvert$, kein Identitätsoperator |
| Interner Graph | Graph auf den sechs Ereigniskoordinaten; beschreibt Ereignisgeneratoren |
| Äußerer Graph | Graph zwischen ganzen Codezellen; Kandidat für räumliche Nachbarschaft |

### 3.3 Der größere TFPT-Zusammenhang bleibt erhalten

Der kanonische Gesamtkontext beschreibt zwei verzahnte Wege: den diskreten Träger-/Familienabschluss bis $E_8$ und die Randantwort bis zu Flavor, $\alpha$, Skalenrelationen und geometrischen Kanälen. P1 umfasst strukturierte Naht-/Randdaten; P2 die fünfteilige Trägerschnittstelle mit 3+2-Struktur. Die heutigen Codebefunde untersuchen einen möglichen tieferen Anschluss dieser Daten.

Der bekannte Gitterabschluss $D_5+A_3\to E_8$, der Halbspinor $\Lambda^{\rm even}\mathbb C^5$, die Flavoroperatoren, die elektromagnetische Fixpunktgleichung und die verschiedenen Clocks bleiben eigene, verbundene Teile der Theorie. Dieses Dokument führt keine neue empirische Gesamtprüfung dieser Teile durch.

Insbesondere sind verschiedene „Uhren“ auseinanderzuhalten: endliche Gruppenordnung, Übertragungsrate, Blockskala, thermische Zeit und physische Dauer. Die Coxeterzahl 30, die 4er-/5er-/6er-Strukturen und ihre Galoisbeziehungen liefern algebraische Verbindungen; ihre gemeinsame physikalische Ausführung ist eine weitere Aussage.

Der Begriff **Universalraum** meint hier den Raum operational unterscheidbarer Prozesse: Träger, erlaubte Operationen, Zusammensetzung, Zustände, Aufzeichnung und Auslesung. Gleiche momentane Messdaten garantieren keine gleiche zukünftige Wirkung.

<a id="zelle"></a>
## 4. Die ursprüngliche Zelle: 256 Dimensionen werden zu fünf

### 4.1 Explizite Codebasis

Auf $(\mathbb C^4)^{\otimes4}$ bilden folgende fünf Zustände eine orthonormale Basis des Codes:

$$
c_0=\frac12\sum_{a=0}^3\lvert aaaa\rangle,
$$

$$
\begin{aligned}
c_1&=\frac{\sum_{\rm perm}\lvert0011\rangle+\sum_{\rm perm}\lvert2233\rangle}{\sqrt{12}},\\
c_2&=\frac{\sum_{\rm perm}\lvert0022\rangle+\sum_{\rm perm}\lvert1133\rangle}{\sqrt{12}},\\
c_3&=\frac{\sum_{\rm perm}\lvert0033\rangle+\sum_{\rm perm}\lvert1122\rangle}{\sqrt{12}},\\
c_4&=\frac1{\sqrt{24}}\sum_{\rm perm}\lvert0123\rangle.
\end{aligned}
$$

Jede Summe enthält nur verschiedene Permutationen. Für die unnormierten Supportspalten $B$ gilt

$$
D=B^\dagger B=\operatorname{diag}(4,12,12,12,24),\qquad
V_4=BD^{-1/2},\qquad P=V_4V_4^\dagger.
$$

Diese Normierung ist wesentlich: In der rationalen Basis $B$ ist die Metrik $D$, nicht die Einheitsmatrix.

### 4.2 Derselbe Hamming-Seed liefert die 60 Richtungen

Der erweiterte Hamming-Code $H_8=\operatorname{RM}(1,3)=[8,4,4]$ besteht aus den 16 Auswertungstabellen affiner Funktionen auf $\mathbb F_2^3$. Seine Gewichte sind 0 einmal, 4 vierzehnmal und 8 einmal.

Aus $\pm2e_i$ und allen Vorzeichenbelegungen der 14 Gewicht-4-Supports entstehen 240 reelle $E_8$-Wurzeln in der verwendeten Normierung. Paarung benachbarter reeller Koordinaten zu vier komplexen Koordinaten ergibt 60 verschiedene Strahlprojektoren. Für normierte Richtungen $\psi_\ell$ setzen wir

$$
r_\ell=I-2\lvert\psi_\ell\rangle\langle\psi_\ell\rvert,
\qquad U_\ell=r_\ell^{\otimes4}.
$$

Der vierte Quellenmoment und der Stabilisatorprojektor erfüllen exakt

$$
M_4=\frac1{60}\sum_\ell
(\lvert\psi_\ell\rangle\langle\psi_\ell\rvert)^{\otimes4},
\qquad 40M_4=S_4+P,
$$

$$
Q=\frac1{16}\sum_{A\in\mathcal P_2}A^{\otimes4},
\qquad Q^2=Q,\quad\operatorname{rank}Q=16,\quad P=S_4Q.
$$

### 4.3 Ereignisenergie und vollständiges Spektrum

Das gemeinsame minimale Ereignisgesetz $I-U_\ell$ ergibt nach Mittelung und Abzug der tiefsten Energie

$$
\boxed{G_4=\frac35I-\frac1{60}\sum_{\ell=1}^{60}U_\ell.}
$$

| Eigenwert von $G_4$ | Vielfachheit |
|---:|---:|
| $0$ | 5 |
| $2/5$ | 70 |
| $8/15$ | 135 |
| $4/5$ | 45 |
| $8/5$ | 1 |

Der Nullraum ist exakt der oben definierte Code; die Lücke ist $2/5$. Ein ganzzahliges Vielfaches $N=30G_4$ wird durch das Polynom mit Nullstellen $0,12,16,24,48$ annihiliert. Exakte Spuren bestimmen die Vielfachheiten. Die Zahlen wurden daher nicht allein aus gerundeten Eigenwerten abgelesen.

Die operationale Bedeutung lautet

$$
\left\langle v,\left(I-\frac1{60}\sum_\ell U_\ell\right)v\right\rangle
=\frac1{120}\sum_\ell\|v-U_\ell v\|^2.
$$

Der Code minimiert die mittlere Veränderung. Diese ist **nicht null**: Die linke Seite beträgt im Code $2/5$; die mittlere quadrierte Zustandsänderung beträgt $4/5$.

Jedes einzelne Ereignis erhält den Code. Auf ihm wirken die 60 Ereignisse als alle 15 einfachen Transpositionen $T_{ab}$, jede genau viermal. Das tatsächliche Wörterbuch wurde für alle Ereignisse geprüft.

### 4.4 Verhältnis zum früheren Momenten-Parent

Der frühere Schutzoperator lautet in einer gebräuchlichen Normierung

$$
H_{\rm mom}=\Delta(2I-P-S_4).
$$

Er besitzt das Spektrum $0^{(5)},\Delta^{(30)},(2\Delta)^{(221)}$. Die andere in den Quellen benutzte Normierung $I-20M_4$ ist genau die Hälfte der dimensionslosen Form.

Mit $C_{60}=\sum U_\ell$ gilt

$$
H_{\rm ref}=\frac\Delta{24}(36I-C_{60})=\frac{5\Delta}{2}G_4,
\qquad (H_{\rm ref}-H_{\rm mom})S_4=0.
$$

Die Operatoren stimmen auf allen 35 symmetrischen Zuständen überein. Außerhalb unterscheiden sie sich. Die frühere Konstruktion und die Ereignisrechnung haben damit denselben Code und denselben symmetrischen Schutzsektor, aber nicht überall dieselbe Anregungsdynamik.

### 4.5 Warum vier Register in einem Schutzterm wesentlich sind

Für $k=1,2,3$ gilt

$$
\operatorname{Tr}_{4-k}(P/5)=\operatorname{Tr}_{4-k}(S_4/35).
$$

Jede Energie aus höchstens dreiregistrigen Termen hat deshalb in beiden gemischten Zuständen denselben Erwartungswert. Wenn der ganze Code Grundraum ist, muss wegen Positivität von $H-E_0I$ auch der gesamte symmetrische 35er-Raum im Grundraum liegen. **Genau den Fünfercode als alleinigen Grundraum kann ein solcher Hamiltonoperator auf denselben vier Registern nicht isolieren.**

Das verbietet keine Zweiregistersteuerung innerhalb eines bereits geschützten Codes. Schutzordnung und Steuerordnung sind unterschiedliche Fragen.

### 4.6 Was die Auswahl noch nicht leistet

Ein anderer kontinuierlicher Verlauf kann dieselben Reflexionsendpunkte erreichen. Bei getrennt additiv bewegten Registern wird die gemittelte Energie im betrachteten Gegenfall $2I$; die Codeauswahl verschwindet. Das Alphabet allein wählt also noch nicht das gemeinsame Zwischenzeitgesetz.

Auch zufälliges Anwenden der codeerhaltenden Reflexionen kühlt nicht in den Code:

$$
\operatorname{tr}[P\,\mathcal T(\rho)]=\operatorname{tr}(P\rho).
$$

Die Codebesetzung bleibt erhalten. Energieauswahl, logische Bewegung und tatsächliche Präparation sind drei getrennte Aussagen.

<a id="auslesung"></a>
## 5. Lokale Auslesung, Schutz und steuerbare Information

### 5.1 Ein, zwei und drei Register

Die Reduktionskanäle $\mathcal E_k(X)=\operatorname{Tr}_{4-k}(V_4XV_4^\dagger)$ haben die Ränge

$$
\boxed{1,\ 10,\ 25\quad\text{für }k=1,2,3.}
$$

| Zugriff | Exakte Aussage | Einfach erklärt |
|---|---|---|
| Ein Register | Zustand immer $I_4/4$ | Es enthält genau keine logische Information |
| Zwei Register | Linearer Ausleserang 10 einschließlich Identität | Neun spurfreie Richtungen werden sichtbar |
| Drei Register | Voller Operatorrang 25 und expliziter Decoder | Der ganze logische Zustand ist rekonstruierbar |

Die 25 sind Operatorraumdimensionen. Ein allgemeiner gemischter Fünferzustand hat 24 reelle freie Parameter, ein reiner acht. Der bekannte Verlust eines Registers ist exakt korrigierbar. Ein beliebiger unbekannter Einregisterfehler an unbekannter Position ist damit nicht automatisch korrigierbar.

Schreibt man $V_4$ nach einem Register als Matrizen $V_a$, gilt

$$
V_a^\dagger V_b=\frac{\delta_{ab}}4I_5.
$$

Die Isometrien $W_a=2V_a$ haben orthogonale Bilder. Ein logischer Operator $O$ wird auf drei Registern durch $O_3=\sum_aW_aOW_a^\dagger$ dargestellt; es gilt $(I\otimes O_3)V_4=V_4O$.

### 5.2 Die Paarmessung ist ein konkreter Kanal

Zehn reelle Vektoren $w_\nu\in\mathbb R^5$ erfüllen

$$
\sum_\nu w_\nu w_\nu^T=I,
\quad\|w_\nu\|^2=\frac12,
\quad|w_\nu^Tw_\mu|=\frac16\;(\nu\ne\mu).
$$

Mit zehn orthonormalen symmetrischen Bellvektoren $b_\nu$ gilt

$$
V_4\psi=\sum_\nu(w_\nu^T\psi)\,b_\nu\otimes b_\nu,
$$

$$
\mathcal E_2(\rho)=\sum_\nu\operatorname{tr}(F_\nu\rho)
\lvert b_\nu\rangle\langle b_\nu\rvert,
\qquad F_\nu=w_\nu w_\nu^T.
$$

Der Kanal misst und präpariert. Er ist bezüglich einer äußeren Referenz entanglement breaking: Zehn unabhängige Ausleseeffekte sind nicht zehn vollständig erhaltene Quantenfreiheitsgrade.

Für die Referenz $I_5/5$ ist die Petz-Rückkomposition

$$
\Phi=\mathcal R_2\mathcal E_2,
\qquad \Phi(\rho)=2\sum_\nu F_\nu\rho F_\nu,
$$

$$
\operatorname{spec}\Phi=\{1^{(1)},(4/9)^{(9)},0^{(15)}\}.
$$

Die referenznormalisierte Singularübertragung der einfachen Auslesung beträgt $2/3$; der echte Hin-und-zurück-Kanal hat $4/9$. Diese Größen dürfen nicht als dieselbe Clockrate bezeichnet werden.

### 5.3 Unsichtbare Zustände und Petersen-Rahmen

Die sechs nativen Simplexmarken ergeben sechs reine Zustände $\rho_q$, für die

$$
\mathcal E_2(\rho_q)=P_{\rm sym,2}/10,
\qquad\frac16\sum_q\rho_q=I_5/5.
$$

Ihre fünf unabhängigen Differenzen $B_q=\rho_q-I_5/5$ spannen den reellen Blindraum auf:

$$
\operatorname{tr}(B_qB_r)=\frac{24}{25}\delta_{qr}-\frac4{25}.
$$

Aus der Gram-Matrix der zehn Auslesevektoren entsteht eine Vorzeichenmatrix $C_P=6WW^T-3I$ mit $C_P^2=9I$. Genau sechs reguläre Vorzeichenrahmen liefern die Petersen-Graphen mit Parametern $(10,3,0,1)$. Die sechs ursprünglichen Markierungen wurden direkt diesen Rahmen zugeordnet.

Der Grad drei des Petersen-Graphen ist keine hergeleitete Raumdimension. Er betrifft die Struktur dieser Auslesung.

### 5.4 Erlaubte Bewegung macht verborgene Information sichtbar

Ein einzelner physischer Paarterm $A_1A_2$ erhält den Code im Allgemeinen nicht. Für seine logische Einschränkung $h_A$ beträgt die maximale Austrittswahrscheinlichkeit beim Puls $e^{-itA_1A_2}$

$$
\frac89\sin^2t.
$$

Die symmetrisierte Paarkontrolle

$$
\widehat h_A=\frac16\sum_{r<s}A_rA_s
$$

erhält dagegen den Code exakt. Vier passende spurfreie Generatoren wachsen unter Kommutatoren mit den Rängen $4,7,12,17,22,24$ zu $\mathfrak{su}(5)$.

Die 35 projektiven Dreierlinien der 15 Pauli-Adressen zerfallen in 15 kommutierende und 20 antikommutierende Linien. Ihre Dreiregisterantworten liefern die 15 reellsymmetrischen und die zehn imaginär antisymmetrischen Hermiteschen Richtungen. Insgesamt wird der volle 25-dimensionale Operatorraum zugänglich.

Das ist kontrollierte Bewegung bei verfügbaren Pulsen. Es bestimmt keinen autonomen Zeitverlauf und keine physische SU(5)-Eichgruppe.

<a id="ladung"></a>
## 6. Die 3+2-Antwort und die tatsächliche Ladungsfrage

Für einen nichttrivialen Hermiteschen Zweiqubit-Pauli $A$ sei $D_A=\sum_{r=1}^4A^{(r)}$. Die erste und zweite Antwort lauten

$$
V_4^\dagger D_AV_4=0,
\qquad V_4^\dagger D_A^2V_4=16R_A,
\quad R_A^2=R_A,\quad\operatorname{rank}R_A=2.
$$

Drei Richtungen reagieren auf diese zweite Antwort nicht, zwei reagieren. Auf dem Nullsummenraum wird dies durch $R_A=(I+M_A)/2$ aus einer dreifachen disjunkten Transposition dargestellt.

Die primitive ganzzahlige spurfreie Markierung ist $5R_A-2I$; mit der gewählten Ladungsnormierung

$$
Y_A=\frac{5R_A-2I}{6},\qquad
\operatorname{spec}Y_A=(-1/3)^{(3)},(1/2)^{(2)},
\quad\operatorname{tr}Y_A^2=5/6.
$$

Ein einzelner markierter Projektor hat den Zentralisator $S(U(3)\times U(2))$. Für **alle** 15 Antwortprojektoren gemeinsam gilt dagegen

$$
\{X:[X,R_A]=0\ \forall A\}=\mathbb CI.
$$

Die gemeinsame Kommutatorgleichung hat auf den 24 spurfreien Richtungen vollen Rang. Der Satz über eine Markierung ist daher kein Satz über die kontinuierliche gemeinsame Symmetrie aller Markierungen.

Auch die gegenseitige Ebenengeometrie ist fest:

$$
\sum_AR_A=6I.
$$

Für verschiedene kommutierende Pauli-Adressen gilt $\operatorname{tr}(R_AR_B)=1$; für antikommutierende gilt $R_AR_BR_A=R_A/4$ und $\operatorname{tr}(R_AR_B)=1/2$. Die 105 Paare zerfallen in 45 beziehungsweise 60 Fälle.

**Wesentliche Korrektur:** Das neue $Y_A$ ist nicht ohne Weiteres die ursprünglich markierte TFPT-Hyperladung $Y_{\rm nat}$. Unter der geprüften nativen Slotzuordnung liegt $Y_{\rm nat}$ außerhalb des unmittelbaren Paaroperatorraums $\mathcal O_2$. Selbst nach Variation der verbleibenden zulässigen Phase gilt

$$
\min_\theta d_{\rm HS}^2(Y_\theta,\mathcal O_2)
=\frac{29}{60}-\frac{\sqrt6}{10}>0.
$$

Gleiches Eigenwertspektrum beweist keine gleiche markierte Einbettung. Direkt benötigt das native Ladungswort mindestens drei Register. In der vollständigen Paar-Kontrollfamilie ist es über zweite verschachtelte Kommutatoren erreichbar; seine minimale Lie-Ordnung ist drei. Das ist eine Pulssyntheseaussage, kein einzelner Paarpuls.

<a id="paare"></a>
## 7. Zwei verschiedene Paarmechanismen

### 7.1 Definitionen und Spektren

Wir unterscheiden durchgehend

$$
K=\sum_{A=1}^{15}R_A\otimes R_A,
\qquad H_X=-J\sum_{ij}K_{ij},\quad J>0,
$$

$$
k=I-\frac1{15}\sum_{a<b}T_{ab}\otimes T_{ab},
\qquad H_E=\gamma\sum_{ij}k_{ij},\quad\gamma>0.
$$

| Gemeinsamer $S_6$-Sektor | Dimension | $K$ | $k$ |
|---|---:|---:|---:|
| Triviale Richtung | 1 | 6 | 0 |
| Fünfersektor | 5 | $3/2$ | $2/5$ |
| Neunersektor | 9 | $7/2$ | $2/3$ |
| Zehnersektor | 10 | $3/2$ | $4/5$ |

Beide wählen bei zwei Zellen eindeutig

$$
\Omega_5=\frac1{\sqrt5}\sum_{i=0}^4c_i\otimes c_i.
$$

Dennoch existieren keine Skalare $a,b$ mit $k=aK+bI$. Die beiden 15er-Ereignisfamilien sind unterschiedliche Konjugationsklassen: einfache Transpositionen einerseits, Produkte dreier disjunkter Transpositionen andererseits.

### 7.2 Die Messungs-Bindungsidentität

Unter der festgelegten reellen orthonormalen Vektorisierung von Matrizen gilt

$$
\boxed{K=\frac32I_{25}+\frac92\Phi.}
$$

Auf der rechten Seite steht die Superoperatormatrix des Rückkanals. Gleichwertig:

$$
\Xi(\rho):=\frac16\sum_AR_A\rho R_A
=\frac14\rho+\frac34\Phi(\rho).
$$

Der gleichmäßig gemischte Kanalfixpunkt $I_5/5$ entspricht unter Vektorisierung der stärksten Bell-Bindungsrichtung. Das ist die präzise Fassung des Zusammenhangs „Messbarkeit und Bindung stammen aus derselben Algebra“.

Der native logische Reflexionskanal $T_5$ hat die Eigenwerte $1,3/5,1/3,1/5$ auf den Sektoren $1,5,9,10$. Die Vorarbeit gibt den konkreten Anschluss

$$
\Phi=\frac{(5T_5-3I)(5T_5-I)(15T_5-13I)}{16}.
$$

Das Polynom ist eine Operatoridentität; seine negativen Koeffizienten sind keine Anleitung für eine positive Zufallsmischung von Operationen.

### 7.3 Gemeinsame gegenüber unabhängigen Ereignislabels

Für zwei ursprüngliche Zellen lautet die gemeinsame Ereignisenergie

$$
\mathcal K_{LR}=I-\frac1{60}\sum_\ell U_\ell^L\otimes U_\ell^R.
$$

Sie ist positiv, erhält beide Codes und schränkt sich auf $k$ ein. Die Kombination

$$
\widehat H_2=\kappa(G_4^L+G_4^R)+\gamma\mathcal K_{LR}
$$

hat für positive $\kappa,\gamma$ den eindeutigen Code-Bellzustand als globalen Grundzustand und die Untergrenze

$$
\operatorname{gap}\widehat H_2\ge\frac25\min(\kappa,\gamma).
$$

Außerhalb der Codes kostet bereits der positive Schutzterm mindestens $2\kappa/5$; innerhalb liefert das Paarspektrum die Lücke $2\gamma/5$.

Bei unabhängigen Labels ist der gemittelte logische Ereignisoperator dagegen $(3I/5)\otimes(3I/5)=9I/25$. Die Energie wird $16I/25$, also zustandsunabhängig. Gleiche lokale Statistiken reichen nicht aus, um die Bindung zu bestimmen; die gemeinsame Ausführung ist wesentlich.

Der gemeinsame mikroskopische Schritt betrifft bis zu acht ursprüngliche Register. Eine Zweizellenkopplung ist deshalb nicht automatisch eine Zweiregisterkopplung.

<a id="mikro"></a>
## 8. Der mikroskopische Austausch und die offene Dreierkette

### 8.1 Ein einzelner Austauschkanal ist exakt lösbar

Mit der Schutzenergie $H_{\rm cell}=\Delta(2I-P-S_4)$ und einer gewählten Wechselwirkung $gD_A^LD_B^R$ bestehen vier identische aktive Zweierblöcke:

$$
\begin{pmatrix}0&16g\\16g&2\Delta\end{pmatrix}.
$$

Ihre untere Energie ist

$$
E_-=\Delta-\sqrt{\Delta^2+256g^2}
=-\frac{128g^2}{\Delta}+\frac{8192g^4}{\Delta^3}+O(g^6).
$$

Die virtuelle Wechselwirkung entsteht somit als Entwicklung eines exakt lösbaren endlichen Blocks. Nach einer vollständigen Wiederkehr verschwindet der angeregte Anteil wieder. Für ein kontrolliertes Minuszeichen nach $m\ge2$ Wiederkehren gilt in der untersuchten Pulswahl

$$
\frac g\Delta=\frac{\sqrt{2m-1}}{16(m-1)},\qquad
T_{\rm ges}=\frac{(m-1)\pi}{\Delta},\qquad
p_{\rm Austritt,max}=\frac{2m-1}{m^2}.
$$

Am Endpunkt ist die Austrittswahrscheinlichkeit null. Die Pulswahl ist zusätzliche Kontrolle, keine hergeleitete physikalische Zeit oder passive Fehlerkorrektur während des Pulses.

### 8.2 Isotroper Austausch und der vollständige Zweizellensatz

Der gleichgewichtete Austauschoperator lautet

$$
\mathcal W=\sum_{A\ne I}D_A^LD_A^R
=4\sum_{r,s=1}^4\operatorname{SWAP}_{Lr,Rs}-16I,
\qquad\|\mathcal W\|\le80.
$$

Die erste komprimierte Ordnung verschwindet. In zweiter Ordnung folgt

$$
H_{\rm eff}^{(2)}=-\frac{128g^2}{\Delta}K,
\qquad J=128g^2/\Delta.
$$

Zusätzlich existiert ein exakt invarianter Zweierblock des vollständigen physischen Hamiltonoperators. Mit

$$
\lvert e\rangle=\frac{\mathcal W\Omega_5}{16\sqrt6}
$$

ist er

$$
H_{\rm bond}=
\begin{pmatrix}0&16\sqrt6g\\16\sqrt6g&2\Delta+16g\end{pmatrix}.
$$

Die untere Energie und der angeregte Normanteil sind

$$
E_0=\Delta+8g-\sqrt{(\Delta+8g)^2+1536g^2},
$$

$$
\epsilon=\frac12\left(1-
\frac{\Delta+8g}{\sqrt{(\Delta+8g)^2+1536g^2}}\right).
$$

Für $g>0$ lautet der Zustand $\sqrt{1-\epsilon}\,\Omega_5-\sqrt\epsilon\,e$; bei negativem $g$ ändert sich das relative Vorzeichen. Es ist eine kohärente Superposition, kein klassisches Gemisch.

Für

$$
0<|g|\le\Delta/200
$$

ist dieser Zustand der **eindeutige globale Grundzustand** auf dem gesamten Raum der acht ursprünglichen Register. Eine analytische Untergrenze lautet

$$
\operatorname{gap}H\ge\frac{1200}{7}\frac{g^2}{\Delta}.
$$

Der Beweis trennt Symmetrie- und Syndromsektoren. Im relevanten neutralen Sektor liegen 25 Code-Code-Richtungen und 60 angeregte Richtungen. Nach Entfernen des exakten Zweierblocks bleiben 24 niedrige und 59 hohe Richtungen; quadratische Ergänzung und $\|\mathcal W\|\le80$ trennen deren Energien vom gefundenen Grundzustand. Die Rechnung erfordert keine behauptete vollständige numerische Diagonalisierung einer $65\,536\times65\,536$-Matrix.

Die Bindungsentropie ist

$$
S_L=\log_2 5+h_2(\epsilon)+\epsilon\log_2 6.
$$

Projektion zurück auf beide Codes ergibt exakt $\Omega_5$ mit Wahrscheinlichkeit $1-\epsilon$.

Der Austausch-Grundzustand ist damit bei endlichem $g$ **gedresst**, also mit Anregungen außerhalb des nackten Codes verbunden. Im direkten Ereignismodell aus Abschnitt 7 ist der Bellzustand dagegen bereits exakt im Code. Diese Aussagen sind vereinbar, weil die Hamiltonoperatoren verschieden sind.

### 8.3 Eine weitere untersuchte Zweilink-Kopplung

Eine frühere Untersuchung benutzt die halbierte Parentnormierung $H_{\rm mom}=I-(P+S_4)/2$ und zwei einzelne physische Links:

$$
V_g=g(a_1^Aa_1^B+a_2^Aa_2^B).
$$

Für die logischen Einschränkungen $h_A,h_B$ ergibt sich

$$
H_{\rm eff}^{(2)}=\frac{g^2}{\Delta}
\left[-\frac{29}{24}I-\frac{11}{24}(h_A\otimes I+I\otimes h_B)
-\frac{15}{8}h_A\otimes h_B\right].
$$

Dies ist eine eigenständige Kopplungswahl und eine andere Normierung; ihre Koeffizienten dürfen nicht mit $-128g^2K/\Delta$ vermischt werden. Numerische Verkleinerung von $g/\Delta$ bestätigt die Störungskoeffizienten, ersetzt aber keinen Satz für beliebig starke Kopplung.

### 8.4 Die offene Dreierkette zeigt die Grenze unabhängiger Bellbindungen

Für zwei Kanten $AB,BC$ des Austauschmodells ist

$$
\lambda_{\max}(K_{AB}+K_{BC})
=\frac{29+\sqrt{73}}4\approx9{,}386000936
$$

fünffach entartet. Der nächste Eigenwert ist $15/2$. Der effektive Grundraum ist also wieder fünfdimensional, mit Lücke

$$
J\frac{\sqrt{73}-1}{4}.
$$

Zwei unabhängig perfekte Bindungen hätten $12$ erreicht. Die Differenz $(19-\sqrt{73})/4$ ist unvermeidlich.

Für die Bellprojektoren gilt unabhängig davon exakt

$$
P_{\Omega,AB}P_{\Omega,BC}P_{\Omega,AB}=\frac1{25}P_{\Omega,AB},
$$

$$
\boxed{\langle P_{\Omega,AB}\rangle+\langle P_{\Omega,BC}\rangle\le\frac65.}
$$

Eine ganze Fünferzelle kann nicht gleichzeitig mit zwei verschiedenen Partnern rein maximal verschränkt sein. Ein Netz muss deshalb als gemeinsamer Mehrparteienzustand bestimmt werden.

### 8.5 Dritte Ordnung: ein kompatibler Schleifenterm

Für den in den Ausgangstexten bezeichneten virtuellen Umlauf über drei verschiedene Dreieckskanten wird der Beitrag

$$
H^{(3)}_{\triangle,\,\rm drei\ Kanten}
=\frac{6144g_{12}g_{23}g_{31}}{\Delta^2}
\sum_AR_A\otimes R_A\otimes R_A
$$

angegeben. Der Koeffizient stammt dort aus sechs Reihenfolgen, Zwischenenergien $2\Delta$ und Antwortamplitude $16R_A$.

**Hier unabhängig exakt bestätigt wurde die Operatorwirkung**

$$
\left(\sum_AR_A^{\otimes3}\right)V_X=\frac{15}{4}V_X.
$$

Der angegebene Schleifenterm verschiebt innerhalb dieses Codes nur die Energie. Eine vollständige unabhängige Ableitung aller dritten und höheren Schrieffer-Wolff-Terme wurde in dieser Sitzung nicht durchgeführt. Der einzelne kompatible Beitrag beweist daher keine Allordnungsstabilität.

<a id="rekursion"></a>
## 9. Zwei Dreierrekursionen und ihre Grenzen

### 9.1 Zwei Tensoren reichen für beide Konstruktionen

Seien $q_i\in\mathbb R^5$, $i=1,\dots,6$, die Simplexvektoren mit

$$
q_i^Tq_j=\delta_{ij}-1/6.
$$

Definiere

$$
\mathsf A_{abcd}=\delta_{ab}\delta_{cd}
+\delta_{ac}\delta_{bd}+\delta_{ad}\delta_{bc},
\qquad
\mathsf C_{abcd}=\sum_i(q_i)_a(q_i)_b(q_i)_c(q_i)_d.
$$

Ein Vierertensor kann als Vier-Zellen-Zustand oder, mit einem Eingangsindex, als Abbildung von einer auf drei Zellen gelesen werden. Diese beiden Lesarten haben unterschiedliche Gesamtnormierungen.

Die beiden Encoder sind

$$
\boxed{V_X=\sqrt{\frac3{40}}(\mathsf A-2\mathsf C),
\qquad V_E=\frac{\mathsf A+6\mathsf C}{\sqrt{72}}.}
$$

| Dreieck mit allen drei Kanten | Grundenergie | Grunddimension | Lücke |
|---|---:|---:|---:|
| Austausch $-J\sum K$ | $-27J/2$ | 5 | $3J$ |
| Ereignisse $\gamma\sum k$ | $4\gamma/5$ | 5 | $2\gamma/5$ |

Für beide gilt exakt

$$
V^\dagger V=I,
\qquad T_{ab}^{\otimes3}V=VT_{ab}\quad\text{für alle 15 Ereignisse}.
$$

Diese Gleichung setzt sich auf jeder endlichen Kodierungsbaumtiefe fort. Sie beschreibt verlustfreie globale Kodierung und dieselbe Gruppenwirkung; sie ist kein Klonen unbekannter Zustände.

### 9.2 Das Ereignisalphabet allein wählt den Encoder nicht aus

Schon die ganze reelle Familie $\mathsf A+a\mathsf C$ ist intertwining-kompatibel. Ihre Isometrienorm lautet

$$
(\mathsf A+a\mathsf C)^\dagger(\mathsf A+a\mathsf C)
=\left(21+5a+\frac7{12}a^2\right)I.
$$

Die Klammer ist für jedes reelle $a$ positiv. Erst die jeweilige Energie wählt $a=-2$ beziehungsweise $a=6$. Wiederkehrende Dimension und erhaltene Ereigniswirkung reichen daher nicht als Eindeutigkeitsargument.

### 9.3 Lokale Information in den größeren Zellen

Für den Kanal $X\mapsto V^\dagger X^{(r)}V$ gelten auf den Sektoren $1,5,9,10$:

| Encoder | Identität | Fünfersektor | Neunersektor | Zehnersektor |
|---|---:|---:|---:|---:|
| $V_X$ | 1 | $19/60$ | $7/12$ | $17/60$ |
| $V_E$ | 1 | $3/4$ | $11/36$ | $1/4$ |

Ein einzelnes Ausgangsregister des Dreierblocks enthält bereits abgeschwächte logische Information. Der neue Block reproduziert somit **nicht den ursprünglichen Einregister-Erasure-Schutz** der Vierregisterzelle. Er reproduziert den Fünferträger und die angegebene Ereigniswirkung.

Entlang eines einzelnen Kodierungsastes werden nichttriviale Informationsrichtungen mit diesen Faktoren gedämpft; auf dem vollständigen Baum bleibt die Isometrie verlustfrei.

### 9.4 Was bei Antwort und Bindung erhalten bleibt

Im Austauschmodell gilt für jede der drei Zellen

$$
V_X^\dagger R_A^{(r)}V_X=\frac7{12}R_A+\frac16I,
\qquad Y_A\mapsto\frac7{12}Y_A.
$$

Der komprimierte $R_A$ ist kein Projektor; seine Eigenwerte sind $1/6$ dreifach und $3/4$ zweifach. Seine beiden Unterräume bleiben jedoch dieselben.

Für eine Brückenkante zwischen zwei Blöcken:

$$
K\mapsto\frac{49}{144}K+\frac{19}{12}I,
\qquad K_c:=K-\frac{12}{5}I\mapsto\frac{49}{144}K_c.
$$

Im Ereignismodell lautet die Antwort dagegen

$$
R_A\mapsto\frac{11}{36}R_A+\frac5{18}I,
\qquad Y_A\mapsto\frac{11}{36}Y_A.
$$

Der tatsächliche Paaroperator $k$ bleibt **nicht** durch bloße Skalierung und Verschiebung erhalten. Mit den orthogonalen Operatoranteilen von $t_{ab}=T_{ab}-3I/5$ und

$$
B_d=\frac1{15}\sum_{a<b}t_{ab}^{(d)}\otimes t_{ab}^{(d)}
$$

gilt

$$
k=\frac{16}{25}I-B_5-B_9,
$$

$$
k'=\frac{16}{25}I-\frac9{16}B_5-\frac{121}{1296}B_9.
$$

Das Verhältnis der beiden nichttrivialen Koeffizienten ändert sich um $729/121$. Der exakte Rang von $(I,k)$ ist zwei, der von $(I,k,k')$ drei. Es existiert folglich kein $k'=ak+bI$.

### 9.5 Projektion ist keine vollständige dynamische Invarianz

Für zwei kodierte Dreierblöcke sei $W=V\otimes V$, $P_B=WW^\dagger$. Eine äußere Kante koppelt an verworfene Blockanregungen, wenn $(I-P_B)hW\ne0$.

Die exakt berechneten Leckagespuren sind

$$
\operatorname{tr}\bigl(W^\dagger K(I-P_B)KW\bigr)=\frac{18335}{576}>0
$$

im Austauschmodell und

$$
\operatorname{tr}\bigl(W^\dagger k(I-P_B)kW\bigr)=\frac{148117}{209952}>0
$$

im Ereignismodell. Die projizierten Identitäten sind richtig; ein vollständig geschlossener Hamilton-Fixpunkt bei endlicher Brückenkopplung folgt daraus nicht. Dafür müssten die ausgelassenen Anregungen beziehungsweise ihre kontrollierten Korrekturen berücksichtigt werden.

<a id="vierer"></a>
## 10. Vier Zellen, die Quartik und der unsichtbare Anteil

### 10.1 Zwei eindeutige Vierergrundzustände

Auf dem vollständigen Vierergraphen gelten

$$
\Psi_X=\frac{\mathsf A-2\mathsf C}{\sqrt{200/3}},
\quad E_X=-27J,
$$

$$
\Gamma_E=\frac{\mathsf A+6\mathsf C}{\sqrt{360}},
\quad E_E=8\gamma/5.
$$

Beide Zustände sind eindeutig. Summiert man die vier Dreiecksuntergrenzen, wird jede Kante zweimal gezählt. Die genannten Vierertensoren sättigen diese Untergrenze auf jeder Fläche. Die exakte Schnittrechnung zweier Flächengrundräume liefert bereits einen eindimensionalen Schnitt; ein Rangzertifikat mit Rang 24 auf dem ersten 25-dimensionalen Flächenraum belegt die Eindeutigkeit.

Für beide Modelle gilt außerdem die Choi-artige Zustandsidentität

$$
\Psi_X=(I\otimes V_X)\Omega_5,
\qquad \Gamma_E=(I\otimes V_E)\Omega_5.
$$

Die Viererbindung entsteht also durch Kodieren einer Hälfte der Zweierbindung.

Im Ausgangstext genannte hinreichende Schutzbedingungen für das vollständige ursprüngliche Ereignismodell sind $\kappa>2\gamma$ beim Dreieck und $\kappa>4\gamma$ beim Viererverbund. Diese Angaben sind als bedingte Schutzabschätzungen der Vorarbeit zu lesen; sie bestimmen das Verhältnis nicht aus P1/P2.

### 10.2 Die Igusa-Gleichung der einfachen Quelle

Für vier identisch präparierte Register $x\in\mathbb C^4$ gilt

$$
\alpha(x)=V_4^\dagger x^{\otimes4}
=\left(f_0/2,\sqrt3f_1,\sqrt3f_2,\sqrt3f_3,\sqrt{24}f_4\right),
$$

$$
\begin{aligned}
f_0&=\sum_i x_i^4,&f_1&=x_0^2x_1^2+x_2^2x_3^2,\\
f_2&=x_0^2x_2^2+x_1^2x_3^2,&f_3&=x_0^2x_3^2+x_1^2x_2^2,\\
f_4&=x_0x_1x_2x_3.
\end{aligned}
$$

In passenden sechs Nullsummenkoordinaten $t_i$ ist ihre Gleichung

$$
\mathcal I(t)=4s_4-s_2^2=0,
\qquad s_k=\sum_i t_i^k.
$$

Es sind Amplitudenpotenzen ohne komplexe Konjugation. Die Gleichung beschreibt eine Präparationsmannigfaltigkeit, nicht den gesamten linearen Codezustandsraum.

Der Austausch-Bindungstensor hat das Polynom

$$
(\mathsf A-2\mathsf C)(t)=3s_2^2-2s_4
=\frac52s_2^2-\frac12\mathcal I(t).
$$

### 10.3 Der genaue 40-Prozent-Beweis

Die Tensorgramdaten lauten

$$
\langle\mathsf A,\mathsf A\rangle=105,
\quad\langle\mathsf A,\mathsf C\rangle=25/2,
\quad\langle\mathsf C,\mathsf C\rangle=35/12.
$$

Setze

$$
F=4\mathsf C-\mathsf A/3.
$$

Sein Polynom ist genau $\mathcal I$; als Hilbertvektor hat er jedoch

$$
\|F\|^2=25,\qquad\langle F,\Psi_X\rangle=0.
$$

Die gemeinsame Identität lautet

$$
\boxed{\Gamma_E=\sqrt{\frac35}\,\Psi_X
+\sqrt{\frac25}\,\frac F5.}
$$

Damit folgen exakt

$$
|\langle\Psi_X,\Gamma_E\rangle|^2=3/5,
\qquad |\langle F/5,\Gamma_E\rangle|^2=2/5.
$$

Für sämtliche identischen Quellenproben gilt $\langle F,\alpha(x)^{\otimes4}\rangle=0$. Die Norm ist trotzdem positiv. Die Nullrelation im Ring der Quellenfunktionen ist kein Nullvektor im dynamischen Hilbertraum.

### 10.4 Gleiche Quellenamplituden, andere Energie

Spiegele nur den Anteil entlang $F/5$:

$$
\Gamma'_E=\sqrt{3/5}\,\Psi_X-\sqrt{2/5}\,F/5.
$$

Beide Zustände sind normiert und liefern dieselben genannten komplexen Quellenamplituden. Im Ereignismodell sind ihre Energien aber

$$
\langle H_E\rangle_{\Gamma_E}/\gamma=8/5,
\qquad\langle H_E\rangle_{\Gamma'_E}/\gamma=392/125.
$$

Für die reine normierte Blindrichtung beträgt der Energieerwartungswert $64\gamma/25$. Das sind drei verschiedene Aussagen über Zustände, keine drei Eigenwerte desselben Einzustandsproblems.

Die daraus motivierte Kompressionsregel lautet: **Zustände nur dann identifizieren, wenn sämtliche zulässigen zukünftigen Antworten erhalten bleiben.** Ob eine konkrete Hylæan-Reduktion solche Information verloren hat, wurde hier nicht untersucht; die im Ausgangstext vermutete Rückwirkung bleibt eine Hypothese.

<a id="codes"></a>
## 11. Hamming, der neue 16-Bit-Code und die Bindungstensoren

### 11.1 Hamming liefert bereits die Zweierbindung

Für zwei Wörter $c,d\in H_8$ werden ihre Bits zu Ququartwerten $2c_j+d_j$ zusammengefasst. Der normierte Zustand ist

$$
\lvert H_8^{(2)}\rangle=\frac1{16}\sum_{c,d\in H_8}
\lvert2c_1+d_1,\ldots,2c_8+d_8\rangle.
$$

Bei der geprüften Aufteilung in zwei Vierregisterzellen gilt

$$
\boxed{(P\otimes P)\lvert H_8^{(2)}\rangle
=\frac{\sqrt5}{4}\Omega_5.}
$$

Die Wahrscheinlichkeit ist $5/16$. Der ganzzahlige Zählbeweis lautet $B^THB=4D$ für die Hamming-Amplitudenmatrix vor Zustandsnormierung. Die ursprüngliche Koordinatenordnung wurde beibehalten.

Auch das Amplitudenpolynom stimmt exakt:

$$
\operatorname{cwe}_{H_8}^{(2)}(x)
=\sum_i x_i^8+14\sum_{i<j}x_i^4x_j^4
+168x_0^2x_1^2x_2^2x_3^2
=4\sum_{i=0}^4\alpha_i(x)^2.
$$

### 11.2 Der zusätzliche selbstduale Code $[16,8,4]$

Nimm alle $x\in\mathbb F_2^8$ geraden Gewichts und verdopple jedes Bit:

$$
D_0=\{(x_1,x_1,\ldots,x_8,x_8):\sum_i x_i=0\}.
$$

Mit $v=(1,0,1,0,\ldots,1,0)$ sei

$$
C_{16}=D_0\cup(D_0+v).
$$

Der Code ist linear, hat 256 Wörter, Dimension acht, Mindestabstand vier, ist selbstdual und doppelt gerade. Die doppelt geraden Gewichte folgen direkt: Wörter in $D_0$ haben Gewicht $2|x|$, Wörter im zweiten Coset Gewicht acht. Selbstorthogonalität und halbe Gesamtdimension ergeben Selbstdualität.

Alle $65\,536$ geordneten Codewortpaare wurden enumeriert. Das vollständige Gewichtspolynom zweiter Ordnung stimmt in allen 45 Monomen mit demjenigen von $H_8\oplus H_8$ überein:

$$
\operatorname{cwe}^{(2)}_{C_{16}}
=\operatorname{cwe}^{(2)}_{H_8\oplus H_8}.
$$

Das macht die Codes nicht identisch und bestimmt nicht ihre blockweise Korrelation.

### 11.3 Die projizierten Vierertensoren

Der normierte Ququart-Codezustand lautet

$$
\lvert C_{16}^{(2)}\rangle=\frac1{256}\sum_{c,d\in C_{16}}
\lvert2c_1+d_1,\ldots,2c_{16}+d_{16}\rangle.
$$

Nach der festgelegten Verteilung auf vier Zellen und Codeprojektion ist der **unnormierte** logische Tensor

$$
d_4=\frac{\mathsf A-3\mathsf C}{36},
\qquad\|d_4\|^2=\frac{25}{576}.
$$

Für zwei Hammingcodes und das kohärente Mittel über die drei Paarungen lautet der ebenfalls unnormierte Vergleichstensor

$$
e_4=\frac{\mathsf A}{48}.
$$

Die Relationen sind

$$
\boxed{d_4-e_4=-F/48,}
$$

$$
\boxed{\mathsf A-2\mathsf C=8(2e_4+3d_4),
\qquad\mathsf A+6\mathsf C=24(6e_4-3d_4).}
$$

Auf identischen Amplituden folgt $d_4(t)-e_4(t)=-\mathcal I(t)/48$. Genau auf der einfachen Quellenmannigfaltigkeit ist der Unterschied unsichtbar.

**Die gemeinsame Codebrücke erklärt beide Bindungstensoren. Sie entscheidet nicht, welche relative kohärente Phase physisch erzeugt wird.** Die Koeffizienten 2 und 3 sind keine zusätzliche Herleitung von SU(2) und SU(3).

### 11.4 Drei verschiedene „16er“ auseinanderhalten

| Objekt | Parameter/Bedeutung |
|---|---|
| Neuer selbstdualer $C_{16}$ dieses Abschnitts | Binärer $[16,8,4]$-Code, 256 Wörter |
| Kummer-/Reed–Muller-Code | $\operatorname{RM}(1,4)=[16,5,8]$, 32 Wörter |
| Größerer Quantencode $Q$ | Logische Hilbertraumdimension 16 in vier Ququarts |

Auch die ältere native-Fock-Untersuchung mit der Bezeichnung „C16“ ist eine andere Konstruktion. Gleicher Name oder gleiche Zahl ist kein Übertragungsbeweis.

<a id="kombination"></a>
## 12. Die eindeutige direkte Kombination innerhalb der gewählten Klasse

### 12.1 Die genau beantwortete Frage

Gesucht wurde innerhalb

$$
h(t)=-K+tk,\qquad t=\gamma/J>0
$$

ein Dreiecksgrundraum mit genau der ursprünglichen $S_6$-Fünferdarstellung, dessen lokaler Blockkanal die beiden nichtkonstanten Operatoranteile der Paarenergie mit einem gemeinsamen Faktor überträgt. Das ist eine präzise Formtreueforderung für projizierte Operatoren.

Die beiden Mechanismen gleichzeitig anzusetzen ist eine erklärte Kombination. Die Rechnung beweist ihre innere Auswahl unter dieser Forderung, nicht ihre Herkunft aus dem primitiven Randkern.

### 12.2 Warum die Familie $\mathsf A+a\mathsf C$ hier genügt

Die Multiplizität der Standarddarstellung $U$ in $\operatorname{Sym}^3U$ ist zwei; in $\Lambda^3U$ ist sie null. Die übrigen $U$-Kopien tragen eine zweidimensionale Zellpermutationsdarstellung und würden mindestens zehn Grundzustände liefern. Ein einzelner fünfdimensionaler Grundraum vom geforderten Typ liegt deshalb in der von $\mathsf A,\mathsf C$ beschriebenen Familie. Die Multiplizitäten wurden unabhängig über alle 720 Elemente von $S_6$ bestimmt.

Für reelles $a$ sind die relevanten lokalen Kanalfaktoren

$$
\lambda_5(a)=\frac{17a^2+156a+396}{3(7a^2+60a+252)},
\qquad
\lambda_9(a)=\frac{a^2+60a+396}{3(7a^2+60a+252)}.
$$

Da bei $t>0$ beide nichtkonstanten Paarsektoren vorhanden sind, erfordert Formtreue $\lambda_5^2=\lambda_9^2$. Der Zähler faktorisiert als

$$
288a(a+6)(a^2+12a+44).
$$

Reelle Kandidaten sind nur $a=0,-6$. Der reine $\mathsf C$-Grenzfall hat Faktoren $17/21$ und $1/21$ und scheidet aus.

### 12.3 Die Energie wählt genau einen Kandidaten

In der Basis $(\mathsf A,\mathsf C)$ sind die Dreiecksmatrizen

$$
M_X=\begin{pmatrix}-15&-3/4\\18&-9/2\end{pmatrix},
\qquad
M_E=\begin{pmatrix}6/5&-1/15\\-12/5&6/5\end{pmatrix}.
$$

Die Eigenvektorbedingung für $(1,a)^T$ lautet

$$
4a^2t+45a^2+630a-144t+1080=0.
$$

Bei $a=-6$ bleibt $-1080=0$; es existiert kein endliches $t$. Bei $a=0$ folgt

$$
\boxed{t=15/2,\qquad V_0=\mathsf A/\sqrt{21}.}
$$

Die vollständige Spektralprüfung bestätigt, dass dies der gesamte Dreiecksgrundraum und nicht nur ein Eigenraum oberhalb des Grundzustands ist. Die Grundenergie ist $-6J$, die Dimension fünf, die Lücke $9J$. Die Randfälle mit einer verschwindenden Kopplung gehören nicht zu diesem Eindeutigkeitssatz; der reine Austauschfall bleibt ein eigener Kandidat.

### 12.4 Vereinfachung zur orthogonal invarianten Paarenergie

Für $\Omega_{\rm un}=\sum_{a=1}^5\lvert aa\rangle$ und $E=\lvert\Omega_{\rm un}\rangle\langle\Omega_{\rm un}\rvert$ gilt exakt

$$
\boxed{h=-K+\frac{15}{2}k=\frac32(2I-S-E).}
$$

Der Operator besitzt eine gemeinsame interne O(5)-Symmetrie. Sein Paarspektrum ist

$$
(-6)^{(1)},\qquad(3/2)^{(14)},\qquad(9/2)^{(10)}.
$$

Die O(5)-Symmetrie ist keine hergeleitete Raumzeit- oder Eichgruppe.

Der vollständige lokale Kanal lautet

$$
\mathcal L(X)=\frac{9X+2X^T+2\operatorname{tr}(X)I}{21}.
$$

Er skaliert den symmetrischen spurfreien Bereich mit $11/21$, den antisymmetrischen mit $1/3$. Daraus folgt

$$
\boxed{(\mathcal L\otimes\mathcal L)(h)
=\frac{121}{441}h+\frac{256}{147}I.}
$$

Auch hier ist die Leckage strikt positiv. Für
$D_B=W^\dagger h^2W-(W^\dagger hW)^2$, $W=V_0\otimes V_0$, gelten:

| Sektor | Dimension | Eigenwert von $D_B$ |
|---|---:|---:|
| Singulett | 1 | $5540/441$ |
| Symmetrisch spurfreier Teil | 14 | $12255/2401$ |
| Antisymmetrischer Teil | 10 | $1433/441$ |

Die Kombination schließt also die **projizierte Paarform**, nicht die volle unprojizierte Dynamik.

<a id="graphen"></a>
## 13. Graphenauswahl für beliebig große gerade Zellzahlen

### 13.1 Die Voraussetzungen des Graphenvergleichs

Es gibt $N$ identische logische Zellen. Der äußere Graph ist einfach und ungewichtet. Jede vorhandene Kante trägt dieselbe positive Energieskala. Optimiert wird über Graph **und** Quantenzustand. Zusätzliche Mehrkörperterme, graphabhängige Normierungen, Knotenkapazitäten, Temperatur oder nichtstationäre Auswahl sind nicht enthalten.

Diese Voraussetzungen sind der Geltungsbereich der folgenden Sätze. Sie sind kein universelles Verbot emergenter Geometrie.

### 13.2 Drei bereits entschiedene direkte Varianten

**Reiner Austausch:** Weil $K\ge3I/2$, senkt jede zusätzliche Kante die Grundenergie mindestens um $3J/2$. Der vollständige Graph gewinnt eindeutig. Monogamie verhindert dies nicht.

**Rohe positive Ereignisenergie:** Weil $k\ge0$, gewinnen der leere Graph sowie disjunkte Bellpaare und isolierte Zellen mit Energie null. Für zwei angrenzende Kanten gilt

$$
k_{12}+k_{23}\ge\frac25(2I-P_{\Omega,12}-P_{\Omega,23})
\ge\frac8{25}I.
$$

Ein zusammenhängender Graph mit mindestens drei Knoten liegt daher strikt höher. Bei zusätzlich erzwungenem Zusammenhang existiert wegen Monotonie mindestens ein minimierender Baum; seine Dimension ist damit nicht bestimmt.

**Ereignisgewinn relativ zu unabhängigen Quellen:** Für $h_{\rm rel}=k-16I/25$ gilt für jeden Graphen mit maximalem Grad $D$

$$
E_0(G)\ge-\frac{8DN}{25}.
$$

Ein normierter Simplex-Produktzustand liefert auf dem vollständigen Graphen

$$
E_0(K_N)\le-\frac{4N(N-1)}{25}.
$$

Für $N>2D+1$ ist damit jeder Kandidat mit fest begrenztem Grad schlechter. Diese Schranke beweist den Vergleich mit dünnen Graphfolgen, nicht den vollständigen exakten Grundzustand dieser Variante.

### 13.3 Allgemeiner Satz für die rekursionsverträgliche Kombination

Für $h=\tfrac32(2I-S-E)$ und $H(G)=J\sum h_{ij}$ gilt für jeden endlichen Graphen

$$
\boxed{H(G)\ge-3JN_{\rm aktiv}I\ge-3JNI.}
$$

$N_{\rm aktiv}$ zählt nichtisolierte Knoten. Bei **geradem $N$** wird $-3JN$ genau von Vereinigungen vollständiger Graphen gerader Größe erreicht. Auf jeder Komponente liegt ein eindeutiger Wick-Singulett, also die vollständig symmetrische Summe aller Paarungen von Kroneckerdeltas.

Beispiele sind ein perfektes Matching, eine Viererclique plus weitere gerade Cliquen und der vollständige Graph $K_N$. Auf jedem festen minimierenden Graphen ist der Gesamtzustand bis auf Phase eindeutig.

**Unter zusätzlicher Zusammenhangsforderung ist $K_N$ der einzige Graphminimierer.**

### 13.4 Die Beweisidee in verständlicher Form

1. Betrachte eine Zelle und alle ihre Nachbarn, also einen Stern. Ganz gleich, wie viele Nachbarn sie hat: Die Summe ihrer Bindungsenergien kann nicht unter $-6J$ sinken.
2. Summiert man über alle Zellen, wird jede Kante zweimal gezählt. Daraus folgt $-3JN$.
3. Eine Zelle erreicht die Schranke nur mit einer ungeraden Nachbarzahl und einem bestimmten **reinen gemeinsamen Zustand** auf ihrer gesamten abgeschlossenen Nachbarschaft.
4. Zwei solche reinen, vollständig verschränkten Nachbarschaftszustände können nicht beliebig überlappen. Für benachbarte Zellen müssen ihre abgeschlossenen Nachbarschaften identisch sein.
5. Deshalb ist jede zusammenhängende Komponente vollständig verbunden. Ihre Größe ist gerade.

Der vollständige Operatorbeweis einschließlich aller Gleichheitsfälle steht in Anhang A. Die Aussage für beliebig große Graphen stammt aus diesem Beweis, nicht aus einer Extrapolation kleiner numerischer Beispiele.

### 13.5 Beliebige lineare Kantenenergie: vollständiges Phasendiagramm

Setze diagnostisch

$$
H_\mu(G)=J\sum_{\{i,j\}\in E(G)}(h_{ij}+\mu I)
$$

bei festem geradem $N$. $\mu$ ist dimensionslos; die wirkliche Energie pro Kante beträgt $J\mu$.

| Parameter | Alle optimalen Graphen | Minimale Energie geteilt durch $J$ |
|---|---|---:|
| $\mu<0$ | Nur $K_N$ | $-3N+\mu N(N-1)/2$ |
| $\mu=0$ | Vereinigungen vollständiger Komponenten gerader Größe | $-3N$ |
| $0<\mu<6$ | Perfekte Matchings | $N(\mu/2-3)$ |
| $\mu=6$ | Beliebige Matchings einschließlich leerem Graphen | 0 |
| $\mu>6$ | Nur der leere Graph | 0 |

Der Beweis benutzt $m=|E(G)|\ge N_{\rm aktiv}/2$. Für $\mu>0$ folgt

$$
E_\mu(G)/J\ge-3N_{\rm aktiv}+\mu m
\ge N_{\rm aktiv}(\mu/2-3).
$$

Die Gleichheitsfälle ergeben die Matchingphasen. Für $\mu<0$ sättigt $K_N$ die Grundschranke und gewinnt zusätzlich durch seine maximale Kantenzahl. Bei $\mu>6$ ist schon jede einzelne nichtleere Kante positiv definit.

**Eine lineare Kantenkostenregel erzeugt in dieser Modellklasse für keinen Parameterwert ein dünnes verbundenes Grundzustandsnetz.**

### 13.6 Warum die Rekursionskonstante physikalisch zählt

Die Projektionsregel enthält eine Konstante pro Kante:

$$
h\mapsto\alpha h+\beta I,
\qquad\alpha=121/441,\quad\beta=256/147.
$$

Bei festem Graphen darf man sie für Zustandsvergleiche als Gesamtverschiebung behandeln. Bei freier Graphenauswahl ändert sie den Preis jeder Kante.

Ein unter der Projektion rein skalierender Operator $h+\mu I$ verlangt

$$
\beta+\mu=\alpha\mu,
\qquad\boxed{\mu_*=-12/5.}
$$

Dies ist die Zentrierung um $\operatorname{tr}(h)/25=12/5$. Sie liegt in der Phase des eindeutig vollständigen Graphen, mit

$$
E_0(K_N)=J\left[-3N-\frac65N(N-1)\right].
$$

Die Zentrierung ist bei dynamischem Graphen eine echte Änderung der Energie. Sie darf nicht erst entfernt und danach als unveränderte Ausgangsdynamik ausgegeben werden.

### 13.7 Auch Korrelationen liefern hier keine ausgezeichnete lokale Nachbarschaft

Der eindeutige Wick-Grundzustand auf $K_N$ ist unter allen Zellvertauschungen invariant. Jede ohne zusätzliche Markierung daraus kovariant konstruierte Paarentfernung ist deshalb für alle verschiedenen Paare gleich. Der Wechsel von Kantenabstand zu Korrelationsabstand löst die Nachbarschaftsfrage für diesen endlichen Grundzustand nicht.

Das schließt andere Zustände, dynamische Symmetriebrechung, gewichtete Modelle oder thermodynamische Untersuchungen nicht pauschal aus. Diese wären eigene Fragen mit zusätzlichen Voraussetzungen.

<a id="quelle"></a>
## 14. Was die primitive Quelle auswählen müsste

### 14.1 Die erste fehlende Eingabe ist konkret

Die interne Ereignisregel sagt noch nicht, **welche Zellen an einem gemeinsamen Ereignis teilnehmen**. Eine allgemeine Schreibweise für diese noch fehlende Information wäre

$$
H[\lambda]=\sum_{S}\lambda_S
\left[I-\frac1{60}\sum_\ell\prod_{i\in S}U_\ell^{(i)}\right].
$$

Das ist eine Darstellung der offenen Eingaben, kein zusätzlich vorgeschlagenes Naturgesetz. Die Teilnehmermengen $S$, Raten $\lambda_S$, ihre Beschränkungen und ihre mögliche Zustandsabhängigkeit enthalten bereits die Grundlage äußerer Nachbarschaft.

### 14.2 Derselbe Ereignistyp auf allen Teilnehmern ergibt andere Grundräume

Ein einziges gemeinsames logisches Ereignis auf $N$ Zellen hat den Generator

$$
G_N^{\rm global}=I-\frac1{15}\sum_{a<b}T_{ab}^{\otimes N}.
$$

Sein Grundraum besteht aus den invarianten Tensoren. Die Dimensionen sind

| Zellzahl | Grunddimension dieses globalen Ereignisses |
|---:|---:|
| 2 | 1 |
| 3 | 1 |
| 4 | 4 |

Bei drei Zellen ist der eindeutige Invariant $\sum_iq_i^{\otimes3}$ mit Normquadrat $10/3$. Jeder $U$-artige rekursive Fünferraum liegt dagegen bei Energie $2/5$.

```text
Ein Ereignis betrifft gemeinsam drei Zellen
                   → Grundraum 1D

Drei Paarereignisenergien auf dem Dreieck
                   → Grundraum 5D
```

Alphabet und $I-U$-Gesetz sind gleichartig; die Teilnehmerstruktur entscheidet das Ergebnis. Der Quellenanschluss muss genau diesen Unterschied auflösen.

### 14.3 Was die geprüften Originalauswahltexte enthalten

Der operationale Seed der geprüften Randquelle enthält ein quasilokales Netz, Zeitentwicklung, Reflexion, Zustand, Nahtklasse und elliptischen Kragengenerator:

$$
\mathfrak S=(\mathfrak A_{\rm loc},\tau_t,\Theta,\omega,[u_\Sigma],\mathcal D_{\rm coll}).
$$

Die diskreten Defekte sind Spektralfluss, wesentlicher endlicher Rang, Determinantengrad und reduzierte Randnullität. Die Existenz eines lexikographisch minimalen Defektvektors klassifiziert nicht automatisch alle Operatoren mit diesen Defekten.

Im untersuchten Masterfunktional wird die Klasse des minimalen Randobjekts durch eine Barriere festgelegt:

$$
\mathbb B_{\rm lex}(\mathcal B)=
\begin{cases}0,&\mathcal B\cong\mathcal B_{\min},\\+\infty,&\text{sonst.}\end{cases}
$$

Die anschließend angezeigten stetigen Variablen sind

$$
\xi=(\alpha,\chi_{\rm geo},\delta_{\rm ph},\rho_{\rm vac}).
$$

Die Wirkung kombiniert die relative Zustandssumme, einen Zeta-Determinantenterm, die Eta-Invariante, einen Transportdeterminanten und den Vakuumterm. Ihre stationären Gleichungen betreffen diese vier Sektoren. In den tatsächlich geprüften Formeln ist keine zusätzliche Variation über gemeinsame Ereignisteilnehmer oder deren Raten ausgeschrieben.

Das ist eine begrenzte Aussage über die bezeichneten Originalstellen, kein pauschales Urteil über unbekannte weitere TFPT-Quellen. Ein bereits vorhandenes quasilokales Netz kann als Rekonstruktionsvoraussetzung sinnvoll sein; es ist dann nicht zugleich aus dem neuen geometriefreien Zellmodell hergeleitet.

### 14.4 Maßgebliche vorhandene Herkunftsgrenzen

| Originalcontract | In dieser Sitzung berücksichtigter Befund |
|---|---|
| `UR.COMPILER.CONTINUOUS_EVENT_ORIGIN.15` | Minimaler positiver Logarithmus gilt für gegebenen Lift, gegebene Dauer und konstanten Generator; gemeinsamer und tensoradditiver Verlauf können dieselben Endpunkte mit unterschiedlichen Zwischenenergien haben |
| `UR.SOURCE.VARIATION_ORIGIN.01` | Diskrete Defektminimierung ersetzt nicht die vollständige Auswahl des Quelloperators innerhalb einer Faser |
| `QGEO.STATE.01` | Ein Zustandsprojektor allein bestimmt keine vollständigen Energieabstände und mehrzeitigen Antworten |

Die neuen Rechnungen verändern den kanonischen Ledger nicht. Ihre positiven Resultate spezifizieren konkrete Zieloperatoren für den Quellenanschluss; ihre Ausschlüsse verhindern, dass nicht hergeleitete Auswahlregeln unbemerkt als Folgen dieser Operatoren gelten.

<a id="weitere-codes"></a>
## 15. Weitere Codes, Markierungen und Schutzkonstruktionen

Diese Ergebnisse stammen aus den in der Sitzung ausgewerteten und erneut ausgeführten Vorpaketen. Sie gehören zur Gesamtschau, sind aber nicht sämtlich neue Entdeckungen des späteren Kopplungsvergleichs.

### 15.1 Der größere 16-dimensionale Code

Der Projektor $Q$ aus Abschnitt 4 hat Rang 16. Nach Umordnung der acht internen Qubits ist er das Produkt zweier bekannter $[[4,2,2]]$-Codes. Eine Basis besteht aus

$$
\lvert\beta_A\rangle_{12}\lvert\beta_A\rangle_{34},
\qquad\beta_A=\operatorname{vec}(A)/2,
$$

für die 16 Hermiteschen Zweiqubit-Paulis. Ein einzelnes Register verrät keine logische Information; sein bekannter Verlust ist korrigierbar. Die Parameter $((4,16,2))_4$ sättigen die entsprechende Singleton-Grenze.

Für den **gleichmäßig gemischten** Codezustand $Q/16$ sind alle Marginalen auf höchstens drei Registern maximales Gemisch. Seine vier Bits Einschränkungsinformation liegen ausschließlich in der gemeinsamen Viererstruktur. Ein höchstens dreiregistriger Hamiltonoperator kann genau $Q$ daher ebenfalls nicht als vollständigen Grundraum isolieren.

Die drei Paaraufteilungen $12|34,13|24,14|23$ liefern drei gegenseitig unverzerrte Basen mit Übergangswahrscheinlichkeit $1/16$. Alle sechs Paarauslesen zusammen haben Rang

$$
1+3(16-1)=46.
$$

Von 255 spurfreien Dichtematrixrichtungen bleiben 210 unsichtbar. Geeignete Paarsteuerungen erzeugen dennoch unter Kommutatoren die Rangfolge $45\to165\to255$, also $\mathfrak{su}(16)$. Direkte Unsichtbarkeit ist nicht dasselbe wie Unzugänglichkeit nach kontrollierter Bewegung.

### 15.2 Zwei verschiedene Fünfer und die äußere Automorphie von $S_6$

Der größere Code zerfällt unter Quell- und Registerwirkung als

$$
Q\mathcal H\cong W_5\otimes\mathbf1
\;\oplus\;W'_5\otimes\mathbb C^2_{\rm std}
\;\oplus\;\mathbb C_{\rm sign}.
$$

Die Dimensionen sind $5+10+1$, aber der mittlere Teil ist ein anderer Fünfer mit zweidimensionaler Multiplizität, nicht automatisch $\Lambda^2W_5$.

Die zweite Fünferdarstellung ist

$$
W'_5(g)=\operatorname{sign}(g)\,W_5(\omega(g)),
$$

mit der äußeren Automorphie $\omega$ von $S_6$. Ihr konkreter Aufbau benutzt 15 Duaden, 15 Synthemen und sechs Pentaden. Die Pentadenwirkung verwandelt eine einfache Transposition in drei disjunkte Transpositionen. Der zusätzliche Vorzeichencharakter ist notwendig. Ein Intertwiner wurde für alle 60 nativen Reflexionen und die Quotientenwirkung für alle 720 Elemente geprüft.

Unter dem markierten $S_5$-Stabilisator zerfällt $W_5=1+4$, während $W'_5$ irreduzibel bleibt. Der Hom-Raum des fünfstelligen Permutationsträgers in $Q\mathcal H$ hat unter $S_5$ Dimension zwei, unter nur $S_3\times S_2$ Dimension zwölf. Das sind Dimensionen von Abbildungsräumen, keine Anzahlen diskreter physischer Lösungen. Die volle Markierung trägt mehr Auswahlkraft als die bloße 3+2-Zerlegung.

### 15.3 Warum der 16er-Code nicht bereits der Materiehalbspinor ist

Der direkte Clockvergleich liefert:

| Native Operation | Spur auf $Q\mathcal H$ | Spur auf $\Lambda^{\rm even}(W_5)$ |
|---|---:|---:|
| Eine Reflexion | 4 | 0 |
| Familien-Dreierclock | 1 | 4 |

Spuren bleiben bei einem Basiswechsel erhalten. Auch eine Gesamtphase behebt die unterschiedlichen Beträge nicht. Daher gibt es keinen Intertwiner zwischen diesen konkret vorgegebenen Wirkungen. **Die Gleichheit $16=1+5+10$ ist kein Materiewörterbuch.**

Der gesonderte TFPT-Weg über den markierten Fünferträger, seine Außenalgebra und den $E_8$-Lift bleibt davon zu unterscheiden.

### 15.4 Der ursprüngliche Hammingzustand liegt selbst im Fünfercode

Bei der geprüften nativen Bitpaarung gilt für die gleichphasige Überlagerung der 16 ursprünglichen Hammingwörter

$$
\lvert H_8\rangle=\frac{B_0+B_3}{4}
=\frac12c_0+\frac{\sqrt3}{2}c_3.
$$

Seine native Bahn besteht aus 15 Strahlen, die durch Zweiermengen der sechs Simplexmarken adressiert werden. Ihre Projektoren summieren sich zu $3P$. Zwei verschiedene Zustände haben in der angegebenen Phasenkonvention Überlappung $1/4$ bei einem gemeinsamen Index und $-1/2$ bei disjunkten Indexpaaren. Die Übergangswahrscheinlichkeiten sind $1/16$ und $1/4$.

Die Paarreduktionen des ursprünglichen Hammingzustands haben vier Eigenwerte $1/4$; er ist kein $\operatorname{AME}(4,4)$-Zustand.

### 15.5 Eine perfekte Sechsregister-Purifikation

Der größere Code besitzt eine explizite $\operatorname{AME}(6,4)$-Purifikation: Jede Dreiregisterreduktion ist $I_{64}/64$, und die Reduktion auf die bezeichneten vier Register ist $Q/16$.

Die Konstruktion benutzt zwei Kopien eines Sechs-Qubit-Graphzustands — Fünferzyklus plus Zentrum — mit passenden lokalen Cliffordoperationen. Je zwei entsprechende Qubits werden zu einem Ququart zusammengefasst. Alle 20 Dreierpartitionen und die Viererreduktion wurden exakt geprüft.

Zusätzlich gewählt ist die Faktorisierung der beiden Referenzregister. Das Existenzresultat liefert keinen bereits physisch ausgewählten Tensorennetzraum.

### 15.6 Zwei perfekte ursprüngliche Fünferzellen dürfen nicht wörtlich Register teilen

Für zwei identisch orientierte eingebettete Codeprojektoren auf Vierermengen mit $s=1,2,3$ gemeinsamen vollständigen Registern ist der Bildschnitt jeweils null.

| Gemeinsame Register | Nichtnull Hauptwinkelkosinus | Vielfachheit | Kleinster Wert von $(I-P_A)+(I-P_B)$ |
|---:|---:|---:|---:|
| 1 | $1/4$ | 100 | $3/4$ |
| 2 | $1/2$ | 10 | $1/2$ |
| 3 | $1/4$ | 20 | $3/4$ |

Ein gemeinsamer Zustand müsste durch die überlappenden Permutationssymmetrien global symmetrisch werden. Die transportierten Stabilisatorbedingungen würden dann zugleich antikommutierende Zweiregisterpaulis auf Eigenwert +1 festlegen. Das ist unmöglich.

Der Satz betrifft identische Einbettung und tatsächlich gemeinsame Tensorfaktoren. Anders gedrehte Codes, zusätzliche Schnittstellen und getrennte wechselwirkende Blöcke sind nicht allgemein ausgeschlossen.

### 15.7 Ein kompatibler Siebenregisterschutz erhält die ursprüngliche Viererwirkung

Der Zeilenraum $C$ der binären Matrix

```text
H7 = 1 1 1 1 0 0 0
     1 1 0 0 1 1 0
     1 0 1 0 1 0 1
```

ist selbstorthogonal; alle sieben Nichtnullwörter haben Gewicht vier und schneiden sich paarweise in zwei Positionen. Es gilt konkret

$$
\{(c,0)+b\mathbf1_8:c\in C,\ b\in\mathbb F_2\}=H_8.
$$

Die Kodierung zweier zusammengefasster Steane-Codes lautet

$$
V_7\lvert ab\rangle=\frac18\sum_{u,v\in C}
\lvert2(u+a\mathbf1)+(v+b\mathbf1)\rangle,
$$

mit binärer Addition in den Klammern. Sie schützt einen logischen $\mathbb C^4$-Raum gegen beliebige Fehler auf einem Ququart.

Für alle 60 ursprünglichen Reflexionen ist exakt

$$
U^{\otimes7}V_7=V_7\overline U,
\qquad U^{\otimes49}V_{49}=V_{49}U.
$$

Die zweite Gleichung folgt durch zweimalige Konjugation, nicht durch Diagonalisierung eines 49-Registersystems. Zentrale Phasen und die native Viererdarstellung bleiben hier erhalten; das ist ein anderer Schutzauftrag als die Fünferauslesung.

Der kommutierende Parent $H_F=\sum_S(I-Q_S)$ hat das exakte Spektrum

| Energie | Vielfachheit |
|---:|---:|
| 0 | 4 |
| 4 | 420 |
| 6 | 5880 |
| 7 | 10080 |

Die Zahlen summieren sich zu $4^7=16384$. Die Länge sieben ist innerhalb der bezeichneten doppelt geraden, selbstorthogonalen CSS-Klasse mit Einzelfehlerkorrektur minimal. Sie ist keine voraussetzungslos hergeleitete Naturkonstante.

<a id="kummer"></a>
## 16. Igusa, Kummer, Theta und Magic States

### 16.1 Der geometrische Kreis ist konkret

Die quartischen Quellenpolynome bilden eine endliche Abbildung $\mathbb P^3\to\mathbb P^4$ auf die Igusa-Quartik. Die generische Faser hat 16 Punkte und entspricht dem projektiven Pauli-Orbit. Es existiert kein Basispunkt. Die einzige erste Polynomrelation tritt in Grad vier auf: Die Monomabbildungen haben für Grade 1–4 die Ränge $5,15,35,69$, bei 70 möglichen Quartikmonomen.

Die 15 projizierten Stabilisatorstrahlen sind ausgezeichnete Punkte mit sechs Koordinaten proportional zu $(2,2,-1,-1,-1,-1)$. Sie liegen je auf drei der 15 singulären Geraden; jede Gerade enthält drei dieser Punkte. Das ist die konkrete Cremona–Richmond-Konfiguration $15_3$.

```text
ursprünglicher Hamming-Code
          │
          ▼
E8 und 60 Quellrichtungen
          │
          ▼
quartische Pauli-Invarianten → Igusa-Quartik
                                  │
                                  ▼
                         Kummer-Geometrie
                                  │
                                  ▼
                          RM(1,4) auf 16 Bits
                                  │ Halbierung
                                  └────────────→ ursprünglicher Hamming-Code
```

### 16.2 Segre-Dualität und ein vollständig geprüftes Kummerbeispiel

Für Nullsummenkoordinaten $z_i$ setzen wir

$$
g_i=z_i\sum_jz_j^2-4z_i^3+\frac23\sum_jz_j^3.
$$

Dann gilt $\sum g_i=0$ und modulo der Igusa-Gleichung $\sum g_i^3=0$: Die Tangentialdaten liegen auf der dualen Segre-Kubik. Die zehn symmetrischen Pauli-Quadriken $(x^TAx)^2$ entsprechen ihren zehn ausgezeichneten singulären Punkten.

Beim geprüften Eingang $a=(1,2,4,7)$ ergibt der Tangentialrückzug nach Entfernung eines gemeinsamen Faktors

$$
\begin{aligned}
\mathcal K_a(x)={}&13\sum_i x_i^4
-44(x_0^2x_1^2+x_2^2x_3^2)\\
&-156(x_0^2x_2^2+x_1^2x_3^2)
+1846(x_0^2x_3^2+x_1^2x_2^2)
-3136x_0x_1x_2x_3.
\end{aligned}
$$

Die 16 Pauli-Bilder von $a$ sind gewöhnliche Doppelpunkte. Ableitungen und lokale Hesse-Matrizen wurden geprüft; eine Gröbnerrechnung schließt weitere singuläre Punkte einschließlich solcher im projektiven Unendlichen aus. Dieses Beispiel hat genau 16 Knoten. Der gewählte Punkt ist ein Existenzzeuge, kein hergeleitetes Vakuum.

### 16.3 Der Kummercode ist $[16,5,8]$, nicht der neue $[16,8,4]$

Die affinen Hyperebenen von $\mathbb F_2^4$ liefern

$$
\operatorname{RM}(1,4)=[16,5,8],
\qquad W(z)=1+30z^8+z^{16}.
$$

Aus dem ursprünglichen $H_8$ entsteht er durch $(c,c+b\mathbf1)$. Einschränkung auf die erste Hälfte gibt den ursprünglichen Code in seiner Koordinatenordnung zurück. Punktieren ergibt $[15,5,7]$ mit Gewichtspolynom $1+15z^7+15z^8+z^{15}$.

Die geometrischen geraden Achtermengen gehören zum Kummergitter mit Diskriminante 64. Dieses Gitter ist nicht $E_8(-1)^2$, dessen Diskriminante eins wäre. Ebenso sind 16 Kummerknoten keine Identifikation mit 16 Materiekomponenten. Die äußere $S_6$-Automorphie zwischen verschiedenen nativen Beschriftungen muss bei jedem vollständigen Wörterbuch berücksichtigt werden.

### 16.4 Der bedingte Theta-/Magic-State-Anschluss

Für den bereits gewählten quadratischen Produkttorus mit $\Omega=\operatorname{diag}(i,i)$ sind die Theta-Koordinaten in der verwendeten Produktmarkierung proportional zu

$$
x_\theta=(1,r,r,r^2),\qquad r=\sqrt2-1=\tan(\pi/8).
$$

Als normierter Hilbertvektor ist dies

$$
\lvert H\rangle\otimes\lvert H\rangle,
\qquad\lvert H\rangle=\cos(\pi/8)\lvert0\rangle+\sin(\pi/8)\lvert1\rangle.
$$

Eine Cliffordrotation führt diesen Einqubitstrahl in einen üblichen T-Ressourcenstrahl über. Der punktierte Reed–Muller-Code ergibt den bekannten $[[15,1,3]]$-CSS-Code mit $d_X=7,d_Z=3$; physisches $T^{\otimes15}$ implementiert logisch $T^\dagger$.

Für einen normierten Zweiqubitzustand ist die Projektion auf den Fünfercode

$$
p_5(x)=\frac1{16}\sum_A\langle A\rangle_x^4
=\frac14\,2^{-M_2(x)}.
$$

Beim Theta-Zustand gilt $p_5=9/64$ und $M_2=\log_2(16/9)$; für die 60 ursprünglichen Stabilisatorstrahlen $p_5=1/4$ und $M_2=0$.

Zusätzlich gewählt sind der Produkttorus, die kompatible Markierung und die Interpretation seiner Theta-Koordinaten als tatsächlich präparierter Hilbertzustand. Die bekannten Code- und Destillationsstrukturen sind keine Neuentdeckungen dieser Sitzung.

### 16.5 Zwei entscheidende Grenzen dieser Geometrie

Beim quadratischen Produkttorus degeneriert der betrachtete Tangentialrückzug zu

$$
\mathcal K_\theta(x)=\text{const.}\,(x_0x_3-x_1x_2)^2.
$$

Das ist eine doppelte Quadrik, keine generische Quartik mit 16 isolierten Knoten. Im geprüften nativen Anschluss ist dieser Igusa-Punkt außerdem nicht vom Familienzyklus fixiert. Daraus folgt kein Ausschluss jeder denkbaren anderen kompatiblen Markierung.

Die gesamte Igusa-Quartik besitzt projektiv keine nichttriviale kontinuierliche **lineare** Symmetrie: Die entsprechende infinitesimale Gleichung lässt nur skalare Matrizen zu. Die volle SU(5)-Kontrollfamilie kann deshalb nicht ausschließlich innerhalb dieser Quellenmannigfaltigkeit wirken.

Konkret liegt $c_4$ außerhalb der Kopienquelle, lässt sich aber durch zwei codeerhaltende Paarpulse aus $c_0$ erzeugen. Das ist eine weitere explizite Demonstration, dass der volle lineare Zustandsraum größer ist als das einfache Präparationsbild.

<a id="weitere"></a>
## 17. Informationsmetrik, Entropie und Clock-Abgrenzung

### 17.1 Informationsmetrik ist nicht schon Gravitation

Die Identität

$$
P\,d\Gamma_4(X)\,P=\operatorname{tr}(X)P
$$

führt im bezeichneten Orientierungsraum für spurfreie $X,Y$ auf

$$
g(X,Y)=8\operatorname{tr}(XY),\qquad F_Q=\frac45g.
$$

Der Raum hat 15 reelle Tangentialrichtungen und eine positive Informationsmetrik. Das ist keine Lorentzmetrik.

Für kollektiv bewegte Codebasen $U^{\otimes4}V_4$ lautet die Berry-Verbindung

$$
\mathcal A=\operatorname{tr}(U^\dagger dU)I_5.
$$

Sie verschwindet auf SU(4); lokal ist ihre Krümmung auch in der bezeichneten U(4)-Familie null. Diese kollektive Orientierungsfamilie allein erzeugt somit kein kontinuierliches nichtabelsches Berry-Eichfeld. Diskrete Holonomie und die Riemannsche Krümmung einer anderen Metrik sind damit nicht ausgeschlossen.

### 17.2 Der Entropiepunkt $t=1/27$

Im untersuchten Kontrastqubit sind $\lambda_X=2/3$, $\lambda_Z=1/3$ und $\lambda_Y=6t$ vorgegeben. Die Choi-Pauliwahrscheinlichkeiten sind

$$
\begin{aligned}
p_0&=(1+x+y+z)/4,&p_X&=(1+x-y-z)/4,\\
p_Y&=(1-x+y-z)/4,&p_Z&=(1-x-y+z)/4.
\end{aligned}
$$

Entropiestationarität fordert $p_Xp_Z=p_0p_Y$; ihre Differenz ist $-(27t-1)/18$. Strikte Konkavität liefert

$$
t=1/27,\qquad\lambda_Y=2/9,
\qquad(p_0,p_X,p_Y,p_Z)=(5/9,5/18,1/18,1/9).
$$

Eine kontinuierliche Realisierung am gewählten Einheitszeitpunkt ist

$$
\mathcal L_{\rm Pauli}(\rho)=\frac{\ln3}{2}(X\rho X-\rho)
+\frac{\ln(3/2)}2(Z\rho Z-\rho).
$$

Sie hat keine unabhängige Y-Sprungrate und erfüllt $\lambda_Y=\lambda_X\lambda_Z$. Die Wahl des Entropieobjekts und der Quellenregel bleibt wesentlich.

Andere in den Vorarbeiten untersuchte Entropieobjekte haben numerisch andere Maximalstellen: ungefähr $0{,}0357983733$ für das Sechsereignisobjekt und $0{,}0365656628$ für den bezeichneten Dreiniveau-Choi-Kanal. Eine erwähnte neue Gleichsetzung mit einem Jarlskog-Invarianten wurde mangels vollständiger Definition nicht neu zertifiziert. Ein konjugationsinvariantes Entropiefunktional wählt ohnehin kein Vorzeichen einer konjugationsungeraden Größe.

### 17.3 Interne gewichtete Bindungslücke und Aldous-Anschluss

Der Ausgangstext beschreibt für

$$
k_w=\sum_{a<b}w_{ab}(I-T_{ab}\otimes T_{ab}),\qquad w_{ab}\ge0,
$$

auf einem verbundenen internen Sechskoordinatengraphen die Gleichheit

$$
\operatorname{gap}(k_w)=\lambda_2(L_w).
$$

Der allgemeine Hintergrund ist der Aldous-Spektrallückensatz. In dieser Darstellung liegt die Standardmode tatsächlich im Zweizellenraum; zusammen mit der allgemeinen Untergrenze ergibt das die Gleichheit bei konsistenter Gewichtsnormierung. Ein Spannbaum reicht für die eindeutige Bellrichtung. Für den Sechserpfad mit Einheitsgewichten ist die Lücke $2-\sqrt3$. Bei zwei getrennten Dreierstücken entstehen drei Invariantenrichtungen.

**Prüfstatus:** Dieser gewichtete Satz und die Beispiele werden aus dem eingereichten Ergebnis samt mathematischem Hintergrund dokumentiert; ein eigener neuer gewichteter Verifier wurde in dieser Sitzung nicht ausgeführt. Die von uns unabhängig gerechnete Gleichgewichtung $w_{ab}=1/15$ liefert die passende Lücke $2/5$.

Der Graph beschreibt interne Ereignisgeneratoren. Er ist nicht der äußere Zellgraph und keine Raumdimension.

### 17.4 Invariantengrade und der Jacobian

Auf sechs Nullsummenkoordinaten beginnen symmetrische Invarianten mit Graden $2,3,4,5,6$. Die Igusa-Relation setzt $s_4=s_2^2/4$. In der bezeichneten Quellenkonstruktion verbleiben die Grade $2,3,5,6$; weil die Koordinaten selbst quartisch in den ursprünglichen Registeramplituden sind, entstehen

$$
(2,3,5,6)\cdot4=(8,12,20,24).
$$

Die Differenzialdeterminante hat Grad $7+11+19+23=60$. Unter den angegebenen Reflexions- und Unabhängigkeitsvoraussetzungen erzwingt ihr Vorzeichenwechsel die 60 Spiegel als Faktoren. Der Ausgangstext nennt bei seiner Normierung

$$
\det\frac{\partial(Q_8,Q_{12},Q_{20},Q_{24})}{\partial(x_0,x_1,x_2,x_3)}
=\frac{5\cdot3^{17}}{64}\prod_{\ell=1}^{60}\ell_\ell(x).
$$

**Prüfstatus:** Der konkrete Vorfaktor wurde in dieser Sitzung nicht erneut aus vollständig fixierten $Q_d$-Definitionen ausgewertet. Er ist normierungsabhängig und wird nicht als neue Naturkonstante oder als hier neu zertifiziertes Ergebnis ausgegeben.

### 17.5 Wiederkehrende Zahlen sind nicht automatisch identische Operatoren

Der aus dem Reflexionsmittel $A=C_{60}/60$ gebildete Hilbertraumtransfer

$$
T=\frac58(I+A)
$$

hat das Spektrum

$$
1^{(5)},(3/4)^{(70)},(2/3)^{(135)},(1/2)^{(45)},0^{(1)}.
$$

Der bisherige Familientransfer mit Eigenwerten $1,2/3,1/3$ lässt sich nicht injektiv schritterhaltend darin einbetten, weil $1/3$ fehlt. Außerdem ist dieser Hilbertraumtransfer nicht automatisch ein spurerhaltender Quantenkanal; sein Nullraum verhindert einen endlichen Hamiltonlogarithmus auf dem ganzen Raum.

Die im Material vorkommenden Faktoren haben deshalb verschiedene Bedeutungen:

| Zahl | Hier tatsächlich berechnete Bedeutung |
|---|---|
| $2/3$ | Referenznormalisierte Singularübertragung der Paarmessung; außerdem Eigenwert eines anderen Hilbertraumtransfers |
| $4/9$ | Eigenwert der Petz-Rückkomposition |
| $7/12$ | Austausch-Blockantwort im Neunersektor; auch Eigenwert eines bestimmten Antwortkanals |
| $49/144$ | Skalierung des zentrierten Austausch-Paarkerns |
| $3/4,11/36,1/4$ | Lokale Sektorfaktoren des Ereignisencoders |
| $11/21,1/3$ | Symmetrische beziehungsweise antisymmetrische Faktoren des gemischten Encoders |
| $121/441$ | Paarformskalierung der direkten Kombination |

Eine einzige universelle Übertragungszahl ist aus diesen Rechnungen nicht hergeleitet.

<a id="urteil"></a>
## 18. Gesamturteil und korrigierte Leitthese

### 18.1 Was mathematisch geschlossen ist

Es gibt eine gemeinsame, konkret berechenbare Struktur:

```text
Hamming-Seed ───────────────→ E8-Wurzelbeschreibung
     │                              │
     │                              ▼
     │                       60 Reflexionen
     │                              │
     │                              ▼
     │                    ursprünglicher Fünfercode
     │                         /           \
     │                        /             \
     │                 Paarmessung       15 Antworten
     │                        \             /
     │                         \           /
     │                          Bindungsalgebra
     │                           /        \
     │                       Austausch   Ereignisse
     │                         │             │
     │                       A−2C          A+6C
     │                         \             /
     │                          \           /
     └─ Codeprojektionen ──────── A, C und Igusa-Tensor
                                      │
                                      ▼
                          direkte Kombination: A
                                      │
                                      ▼
                         exakt bestimmte Graphenminima
```

Der Zusammenhang ist stärker als eine Liste passender Dimensionen. Es gibt tatsächliche Abbildungen zwischen Codewörtern, Zuständen, Gruppenwirkungen und Operatoren.

### 18.2 Was die bildlichen Aussagen leisten — und was nicht

| Aussage aus dem Ausgangsbild | Präzisierte Lesart |
|---|---|
| „Die Zelle ist geschützte Information“ | Exakter endlicher Code mit definierter Erasure-Eigenschaft und einem gapped Schutzoperator; keine automatische Selbstheilung bei beliebigen Fehlern |
| „Information = Messung = Bindung“ | Gemeinsame Algebra und exaktes Vektorisierungswörterbuch; nicht Identität aller physikalischen Operationen |
| „Drei Zellen werden wieder eine Zelle“ | Erhaltene Fünferdarstellung und Ereigniswirkung; ursprünglicher vollständiger Fehlerschutz wird nicht reproduziert |
| „Die Rekursion schließt“ | Ereignisintertwiner schließen; projizierte Paarform nur in bestimmten Fällen; volle Hamiltoninvarianz scheitert an positiver Leckage |
| „3+2 liefert das Standardmodell“ | Konkretes Ladungsspektrum und Zentralisator; Auswahl, Transport, lokale Eichfelder, Spin und Chiralität nicht mitbewiesen |
| „Raum ist Beziehung“ | Tragfähige Forschungsinterpretation; die untersuchten Grundenergien wählen noch keine lokale dreidimensionale Phase |
| „Zeit ist Ereignisreihenfolge“ | Eine Ordnung allein liefert weder physische Dauern noch Lorentzkausalität oder eine eigenständige Zeitrichtung |
| „Stabile Defekte sind Materie“ | In dieser Sitzung kein entsprechendes Defektspektrum mit Feldstatistik und chiraler Dynamik abgeleitet |
| „E8 ist der Schatten eines tieferen Codes“ | Derselbe Code besitzt mehrere algebraische Realisierungen; daraus folgt noch keine physische Priorität einer Realisierung |
| „40 Prozent wurden wegkomprimiert“ | Exakter Blindanteil für die bezeichnete Quellenfamilie; keine gemessene Aussage über ein konkretes anderes Software- oder Physiksystem |

Die Hilberträume, Tensorprodukte und Quantenoperationen sind in den Rechnungen bereits verwendet. Eine Herleitung der gesamten Quantenmechanik aus klassischen Bits wurde nicht durchgeführt.

### 18.3 Die physische Gesamtlösung bleibt eine andere Aussage

Für eine vollständige TFPT-/Universalraum-Herleitung wären weiterhin insbesondere zu verbinden:

1. Der ursprüngliche Randkern mit dem konkreten gemeinsamen Ereignisverlauf, den Teilnehmermengen und Raten.
2. Die tatsächliche Präparation beziehungsweise Zustandsauswahl mit dieser Dynamik.
3. Eine autonome lokale räumliche Phase mit einer unabhängigen kausalen Zeitstruktur.
4. Die markierte geladene Feldalgebra mit chiraler Materie, Eichfeldern und den bestehenden Flavor-/Kopplungsausgaben.
5. Ein kontrollierter wechselwirkender Kontinuumsgrenzwert und gravitative Dynamik.

Ein Tetraedergraph, ein ternärer Baum, der interne Sechsknoten-Laplacian und die 3+2-Ladungszerlegung sind verschiedene Objekte. Keines ist für sich ein Beweis von 3+1-Raumzeit. Für eine spektrale Raumdimension drei müsste eine begründete Graphfolge in einem skalierenden Zeitbereich etwa $P_{\rm return}(t)\propto t^{-3/2}$ zeigen. Ein einzelner passender Punkt oder eine kleine Zeichnung genügt nicht.

Die ursprünglichen Abschlussfragen T1–T8 wurden durch diese Sitzung nicht als Ganzes geschlossen. Es wurde keine neue Naturkonstante, kein neuer experimenteller Gesamtfit und keine vollständige Weltlösung behauptet.

### 18.4 Komprimierte abschließende Aussage

> **Gefunden ist ein eng verbundenes endliches System aus Code, Auslesung, Bindung, Quartik und rekursiver Darstellung. Die direkte formtreue Kombination seiner zwei Paarmechanismen ist bestimmt; ihre Graphenminima sind vollständig klassifiziert. In dieser Modellklasse entsteht keine dünne zusammenhängende Grundzustandsgeometrie. Die fehlende physikalische Auswahl liegt in der gemeinsamen Quelle und ihrer Teilnehmer-/Dynamikregel.**

<a id="matrix"></a>
## 19. Vollständige Ergebnismatrix

Die Kennungen dieser Tabelle dienen nur der Navigation in diesem Dokument; sie sind keine neu registrierten Theorie-Claims. „Exakt“ bezieht sich stets auf die erläuterten Voraussetzungen.

| Nr. | Ergebnis oder Untersuchung | Status | Detail |
|---:|---|---|---|
| 01 | Konkrete Fünferbasis in vier Ququarts | Exakt | §4.1 |
| 02 | Hamming → 240 Wurzeln → 60 Strahlen | Exakt rekonstruiert | §4.2 |
| 03 | $40M_4=S_4+P$, $P=S_4Q$ | Exakt | §4.2 |
| 04 | Vollständiges $G_4$-Spektrum, Lücke $2/5$ | Exakt | §4.3 |
| 05 | Alle 60 Ereignisse → 15 Transpositionen je viermal | Exakt | §4.3 |
| 06 | Momenten- und Reflexionsparent auf dem symmetrischen Raum gleich | Exakt, normierungsgebunden | §4.4 |
| 07 | Schutzordnung vier ist auf diesen Registern notwendig | Analytischer Ausschluss | §4.5 |
| 08 | Gleiche Endpunkte wählen nicht denselben Verlauf | Gegenmodell | §4.6 |
| 09 | Reflexionsmischung präpariert den Code nicht autonom | Exakte Besetzungserhaltung | §4.6 |
| 10 | Lokale Ausleseränge $1,10,25$ | Exakt | §5.1 |
| 11 | Einregister-Erasure-Decoder | Exakt | §5.1 |
| 12 | Zehn Effekte, Bell-Paarmessung und Rückkanal $4/9$ | Exakt | §5.2 |
| 13 | Sechs lokal ununterscheidbare reine Markierungen | Exakt | §5.3 |
| 14 | Sechs Petersen-Vorzeichenrahmen aus nativen Marken | Exakt | §5.3 |
| 15 | Einzelpaar-Leckage und symmetrisierte codeerhaltende Steuerung | Exakt | §5.4 |
| 16 | SU(5)-Kontrollalgebra und volle Dreiregisterauslesung | Exakt; Kontrolle vorausgesetzt | §5.4 |
| 17 | 15 Rang-2-Antworten und 3+2-Ladung | Exakt | §6 |
| 18 | Gemeinsamer Kommutant aller Antworten nur skalar | Exakt | §6 |
| 19 | Neue Antwortladung ist nicht native markierte Hyperladung | Exakter Einbettungsgegencheck | §6 |
| 20 | Paaroperatoren $K$ und $k$ sind verschieden | Exakt | §7.1 |
| 21 | Messungs-Bindungsidentität $K=3I/2+9\Phi/2$ | Exakt mit Vektorisierung | §7.2 |
| 22 | Gemeinsame Quelle bindet; unabhängige Labels verlieren Selektion | Exakt unter jeweiligem Quellenvertrag | §7.3 |
| 23 | Exakter mikroskopischer Zweierblock und globales kleines-g-Theorem | Exakt/bedingt | §8.1–8.2 |
| 24 | Alternative Zweilink-Störungskopplung | Exakter Zweitordnungskoeffizient | §8.3 |
| 25 | Offene Dreierkette: $(29+\sqrt{73})/4$, Grunddimension fünf | Exakt effektiv | §8.4 |
| 26 | Bell-Monogamieschranke $6/5$ | Exakt | §8.4 |
| 27 | Einzelner Dreiecksschleifenterm wirkt skalar | Tensorwirkung exakt; Gesamtordnung nicht neu hergeleitet | §8.5 |
| 28 | Zwei Dreierencoder $V_X,V_E$ und volle Dreierspektren | Exakt | §9, Anhang B |
| 29 | Ereignisintertwiner auf jeder endlichen Baumtiefe | Exakt durch Komposition | §9.1 |
| 30 | Kontinuierliche Encoderfamilie zeigt fehlende Auswahl durch Gruppenwirkung allein | Exakt | §9.2 |
| 31 | Lokale Blockkanäle und Antwortfaktoren | Exakt | §9.3–9.4 |
| 32 | Ereignis-Paarkern ist nicht affin blockgeschlossen | Exakter Ranggegencheck | §9.4 |
| 33 | Beide reinen Modelle koppeln an verworfene Blockanregungen | Exakte positive Leckage | §9.5 |
| 34 | Eindeutige Vierergrundzustände und Choi-/Kodierungsrelation | Exakt | §10.1 |
| 35 | Igusa-Präparationsrelation und voller Zustandsraum verschieden | Exakt | §10.2, §16.5 |
| 36 | Viererüberlappung $3/5$ und blinder Normanteil $2/5$ | Exakt | §10.3 |
| 37 | Quellenidentische Zustände mit Energien $8/5$, $392/125$ | Exakt | §10.4 |
| 38 | Hamming-Zustandsprojektion auf $\Omega_5$ | Exakt | §11.1 |
| 39 | Selbstdualer $[16,8,4]$-Code, 65.536 Paare, 45 Monome | Vollständige exakte Enumeration | §11.2 |
| 40 | $d_4,e_4$, Igusa-Differenz und beide Bindungskombinationen | Exakt | §11.3 |
| 41 | Direkte positive Mischungsformtreue erzwingt $\gamma/J=15/2$ | Exakt innerhalb der benannten Klasse | §12 |
| 42 | Interne O(5)-Paarform, gemischter Kanal und Spektren | Exakt | §12.4 |
| 43 | Auch die gemischte Blockdynamik hat Leckage | Exakt | §12.4 |
| 44 | Drei direkte freie Graphvarianten scheitern an dünner Grundphase | Analytische begrenzte Ausschlüsse | §13.2 |
| 45 | Allgemeine Stern-/Graphenschranke | Analytischer Satz | §13.3, Anhang A |
| 46 | Sämtliche Graphenminimierer bei geradem N: gerade Cliquen | Analytische vollständige Klassifikation | §13.3, Anhang A |
| 47 | Vollständiges lineares Kantenkosten-Phasendiagramm | Analytischer Satz | §13.5 |
| 48 | Dynamisch relevante Rekursionszentrierung $-12/5$ | Exakt, als Graphenergieänderung ausgewiesen | §13.6 |
| 49 | Globales Ereignis auf 2/3/4 Zellen: Grunddimension 1/1/4 | Exakt unabhängig geprüft | §14.2 |
| 50 | Teilnehmer-/Ratenauswahl aus Randquelle | In den geprüften Formeln nicht hergeleitet | §14.3–14.4 |
| 51 | Größerer 16er-Erasurecode, 46 sichtbare/210 blinde Richtungen | Quellenbefund aus ausgeführten Vorpaketen | §15.1 |
| 52 | Äußere S6-Automorphie und anderer Fünfer | Exakter Quellenbefund | §15.2 |
| 53 | 16er-Code ≠ Materiehalbspinor unter Originalclocks | Exakter Spurgegencheck | §15.3 |
| 54 | Ursprünglicher Hammingzustand im Fünfercode und 15er-Bahn | Exakter Quellenbefund | §15.4 |
| 55 | AME(6,4)-Purifikation | Exakter bedingter Existenzzeuge | §15.5 |
| 56 | Wörtlich überlappende perfekte Fünfercodes unvereinbar | Exakter begrenzter Ausschluss | §15.6 |
| 57 | Siebenregistercode schützt native C4-Wirkung | Exakt innerhalb genannter CSS-Klasse | §15.7 |
| 58 | Igusa-/Segre-/Kummer-Brücke und genau 16 Knoten im Beispiel | Exakter Quellenbefund | §16.1–16.2 |
| 59 | Kummer-RM-Codekreis und Theta/Magic-State-Verbindung | Algebra exakt; Zustandswahl bedingt | §16.3–16.4 |
| 60 | Produkttorusdegeneration und lineare Igusa-Symmetriegrenze | Exakte Gegenprüfungen | §16.5 |
| 61 | Positive Informationsmetrik, skalare flache Berry-Verbindung | Exakt im angegebenen Orientierungsraum | §17.1 |
| 62 | Entropiepunkt 1/27 und zwei unabhängige Pauli-Sprünge | Exakt für das gewählte Entropieobjekt | §17.2 |
| 63 | Andere Entropiemaxima | Numerisch, gesonderte Objekte | §17.2 |
| 64 | Gewichtete interne Bindungslücke = Graphlücke | Dokumentierter Quellenbefund; kein neuer allgemeiner gewichteter Prüflauf | §17.3 |
| 65 | Grade 8,12,20,24 und Grad-60-Jacobian | Struktur dokumentiert; konkreter Vorfaktor nicht neu ausgewertet | §17.4 |
| 66 | Lazy-Transfer mit 2/3 ist nicht bisheriger Familientransfer | Exakter Spektralgegencheck | §17.5 |
| 67 | Autonome lokale 3+1D-Raumzeit, chirale Materie, Gravitation | Nicht hergeleitet | §18 |

<a id="pruefung"></a>
## 20. Was tatsächlich gerechnet wurde

### 20.1 Originalpakete und unabhängige Rekonstruktion unterscheiden

Verfügbare ältere September-26-Pakete wurden in Arbeitskopien erneut ausgeführt. Dazu gehören Quartikfortsetzung, vertiefte Code-/Geometrie-/Dynamikrechnung, Igusa-Verbindungen und frühere Sitzungssynthese. Die Originaldateien blieben unverändert.

Die neuesten im Nutzertext ausgeschriebenen Dreier-, Vierer- und $[16,8,4]$-Resultate wurden **unabhängig aus ihren Definitionen rekonstruiert**. Ihre neuesten Originalarchive waren in den erfolgreich geladenen Chatansichten nicht eindeutig als entsprechende Pakete verfügbar. Deshalb wird kein Replay aller neuesten Chat-Artefakte behauptet.

| Prüfebene | Datei oder Programm | Dokumentiertes Ergebnis |
|---|---|---|
| Ursprüngliche Zellereignisse | `source_event_check.py` | 248 exakte Einzelbedingungen; volle Spektral- und Ereigniszuordnung |
| Zwei reine Mehrzellenmodelle | `exact_comparison.py` | 90 exakte Bedingungen; Spektren, Tensoren, Kanäle, Eindeutigkeit, Leckage |
| Neuer 16-Bit-Code | `code16_check.py` | 2507 Bedingungen; vollständige Enumeration und Tensoridentitäten |
| Unabhängige numerische Darstellung | `compare_models.py` | Gegenrechnung in separat erzeugter orthonormaler Basis |
| Direkte Kopplungskombination | `joint_selection.py` | Rationale Auswahlgleichung, vollständige Spektren, O(5)-Form und Projektion |
| Gemischter Kanal und Wickzustände | `joint_graph_check.py` | 45 exakte Bedingungen; Wick-Sättigung bei N=2,4,6, Leckage und Zentrierung |
| Teilnehmerregel und Darstellungen | `joint_source_check.py` | S6-Multiplizitäten über 720 Permutationen und globaler Dreizellengegenfall |
| Vorpaket Quartikfortsetzung | `audit.py` | 385 bestandene Prüfungen gemäß Replay-Protokoll |
| Vorpaket vertiefte Dynamik | `verify_deeper.py` | 707 benannte exakte Prüfungen; numerische Zusatzkontrollen gesondert |
| Vorpaket Igusa/weitere Codes | `verify_all.py` | Alle bezeichneten Komponenten erfolgreich; Umfang im Replay-Verzeichnis |

Diese Zahlen zählen Prüfbedingungen, keine unabhängigen Entdeckungen oder unabhängigen physikalischen Bestätigungen.

### 20.2 Art der Exaktheit

Die neuen eigenständigen Prüfer rekonstruieren ihre Matrizen aus ausgeschriebenen endlichen Regeln. Sie benutzen ganzzahlige und rationale Identitäten sowie analytische Beweise. Numerische Diagonalisierungen dienen zum Finden oder Gegenprüfen von Kandidaten; die entscheidenden endlichen Spektren werden durch exakte Polynome und Spuren abgesichert.

Die Programme `source_event_check.py`, `exact_comparison.py`, `code16_check.py` sowie die drei `joint_...`-Programme liefen normal und mit `python3 -OO`; die entsprechenden Resultate beziehungsweise Ausgabeprotokolle stimmen bytegenau überein. Sie verwenden explizite Fehlerbedingungen. **Diese -OO-Aussage gilt nicht pauschal für sämtliche älteren Archive:** In einigen Vorpaketen sind Python-Assertions Teil der Prüfung und normale Ausführung ist erforderlich.

Der allgemeine Graphensatz stammt aus dem vollständigen analytischen Beweis in Anhang A. Die endlichen Wick-Prüfungen unterstützen einzelne Identitäten; sie beweisen nicht allein die Aussage für alle N. Eine gesonderte Agentengegenprüfung kontrollierte Sternschranke, Gleichheitsfälle, Cliquenklassifikation und Kantenkostenfälle. Es liegt keine formale Lean-Verifikation vor.

### 20.3 Nicht als neu vollständig geprüft ausgegeben

- Der normierungsabhängige Jacobian-Vorfaktor $5\cdot3^{17}/64$.
- Sämtliche dritten und höheren Schrieffer-Wolff-Terme; geprüft wurde die ausdrücklich genannte Schleifenwirkung.
- Die vollständige kontinuierliche Symmetrieklassifikation des ursprünglichen Paarkerns; der gemeinsame Antwortkommutant wurde dagegen exakt neu geprüft.
- Ein allgemeiner gewichteter Aldous-Anwendungsprüfer; der entsprechende Quellenbefund wurde eingeordnet.
- Der im Ausgangstext erwähnte zusätzliche Gegencheck einer naiven Reed–Muller-Vergrößerung, soweit dafür kein eindeutig zugeordneter neuer Verifier vorlag. Die hier dokumentierten RM(1,4)- und CSS-Rechnungen sind separat belegt.
- Ein thermodynamischer Grenzübergang, eine allgemeine gewichtete Graphenphase, endliche Temperatur oder autonome Kühlung.
- Ein vollständiger heutiger Lauf der kanonischen TFPT-, Wolfram- oder Lean-Suite.
- Ein neuer empirischer Fit von Flavor, $\alpha$, Kosmologie oder Gravitation.

### 20.4 Dokumentation gegenüber neuem Forschungsstand

Diese Markdown-Datei konsolidiert den vorhandenen Sitzungsstand. Die mathematischen Prüfungen werden mit ihren vorhandenen Ergebnissen dokumentiert; allein das Erstellungsdatum dieser Datei macht daraus keinen neuen vollständigen Physikprüflauf.

Die damalige Theoriegraphprüfung bezog sich auf den dort erfassten Korpus mit Erzeugungsdatum 22. September. Die neuen lokalen Ergebnisse waren damit nicht automatisch in den kanonischen Theoriegraphen oder Ledger integriert. Paper, Ledger und Ursprungspostulate wurden durch diese Sitzung nicht verändert.

<a id="quellen"></a>
## 21. Dateien, Originalquellen und Literatur

### 21.1 Hauptbelege dieser Sitzung

Die folgenden Dateiverweise öffnen die lokal gespeicherten Herleitungen und Prüfdaten. Die wesentlichen Aussagen und Beweise sind bereits in dieser Markdown-Datei enthalten; die verlinkten Dateien ergänzen sie um ausführbare Rechnungen und Originalprotokolle.

| Inhalt | Datei |
|---|---|
| Erste vollständige Zusammenführung der beiden reinen Modelle | [TFPT_Gesamtpruefung_2026-09-26.txt](</Users/stefanhamann/Documents/Codex/2026-09-26/berpr-fe-das-alles-zusammen-und/outputs/TFPT_Gesamtpruefung_2026-09-26.txt>) |
| Vollständiger Beweis zur direkten Kombination und Graphenwahl | [TFPT_Kombination_Eindeutigkeit_2026-09-26.txt](</Users/stefanhamann/Documents/Codex/2026-09-26/berpr-fe-das-alles-zusammen-und/outputs/TFPT_Kombination_Eindeutigkeit_2026-09-26.txt>) |
| Erstes reproduzierbares Prüfpaket | [TFPT_Gesamtpruefung_Pruefpaket_2026-09-26.zip](</Users/stefanhamann/Documents/Codex/2026-09-26/berpr-fe-das-alles-zusammen-und/outputs/TFPT_Gesamtpruefung_Pruefpaket_2026-09-26.zip>) |
| Prüfpaket zur Kombination | [TFPT_Kombination_Pruefpaket_2026-09-26.zip](</Users/stefanhamann/Documents/Codex/2026-09-26/berpr-fe-das-alles-zusammen-und/outputs/TFPT_Kombination_Pruefpaket_2026-09-26.zip>) |
| Quellenpfade und Hashes | [source_manifest.json](</Users/stefanhamann/Documents/Codex/2026-09-26/berpr-fe-das-alles-zusammen-und/outputs/source_manifest.json>) |
| Verwendete Originalauszüge des Rand-/Masteransatzes | [primary_source_excerpt.json](</Users/stefanhamann/Documents/Codex/2026-09-26/berpr-fe-das-alles-zusammen-und/outputs/primary_source_excerpt.json>) |
| Erster begrenzter Forschungsstatus | [research_verdict.json](</Users/stefanhamann/Documents/Codex/2026-09-26/berpr-fe-das-alles-zusammen-und/outputs/research_verdict.json>) |
| Normale/optimierte Reproduktion | [reproduction_results.json](</Users/stefanhamann/Documents/Codex/2026-09-26/berpr-fe-das-alles-zusammen-und/work/reproduction_results.json>) |
| Getrennte mathematische Gegenprüfung des Graphenbeweises | [joint_bound_review.txt](</Users/stefanhamann/Documents/Codex/2026-09-26/berpr-fe-das-alles-zusammen-und/work/joint_bound_review.txt>) |
| Umfang der erneut ausgeführten Vorarchive | [Replay-README](</Users/stefanhamann/Documents/Codex/2026-09-26/berpr-fe-das-alles-zusammen-und/work/source_replay/README.md>) |

### 21.2 Programme und Ergebnisdateien

| Rechnung | Programm | Ergebnis |
|---|---|---|
| Quelle und Fünfercode | [source_event_check.py](</Users/stefanhamann/Documents/Codex/2026-09-26/berpr-fe-das-alles-zusammen-und/work/source_event_check.py>) | [source_event_results.json](</Users/stefanhamann/Documents/Codex/2026-09-26/berpr-fe-das-alles-zusammen-und/work/source_event_results.json>) |
| Reine Mehrzellenmodelle | [exact_comparison.py](</Users/stefanhamann/Documents/Codex/2026-09-26/berpr-fe-das-alles-zusammen-und/work/exact_comparison.py>) | [exact_results.json](</Users/stefanhamann/Documents/Codex/2026-09-26/berpr-fe-das-alles-zusammen-und/work/exact_results.json>) |
| C16-Projektion | [code16_check.py](</Users/stefanhamann/Documents/Codex/2026-09-26/berpr-fe-das-alles-zusammen-und/work/code16_check.py>) | [code16_results.json](</Users/stefanhamann/Documents/Codex/2026-09-26/berpr-fe-das-alles-zusammen-und/work/code16_results.json>) |
| Numerischer Gegenweg | [compare_models.py](</Users/stefanhamann/Documents/Codex/2026-09-26/berpr-fe-das-alles-zusammen-und/work/compare_models.py>) | [comparison_results.json](</Users/stefanhamann/Documents/Codex/2026-09-26/berpr-fe-das-alles-zusammen-und/work/comparison_results.json>) |
| Gemischte Kopplung | [joint_selection.py](</Users/stefanhamann/Documents/Codex/2026-09-26/berpr-fe-das-alles-zusammen-und/work/joint_selection.py>) | [joint_selection_results.json](</Users/stefanhamann/Documents/Codex/2026-09-26/berpr-fe-das-alles-zusammen-und/work/joint_selection_results.json>) |
| Kanal und Graphidentitäten | [joint_graph_check.py](</Users/stefanhamann/Documents/Codex/2026-09-26/berpr-fe-das-alles-zusammen-und/work/joint_graph_check.py>) | [joint_graph_results.json](</Users/stefanhamann/Documents/Codex/2026-09-26/berpr-fe-das-alles-zusammen-und/work/joint_graph_results.json>) |
| Globales Ereignis und S6-Zählung | [joint_source_check.py](</Users/stefanhamann/Documents/Codex/2026-09-26/berpr-fe-das-alles-zusammen-und/work/joint_source_check.py>) | [joint_source_results.json](</Users/stefanhamann/Documents/Codex/2026-09-26/berpr-fe-das-alles-zusammen-und/work/joint_source_results.json>) |

Aus dem Projektordner lassen sich die neuen Rechnungen mit Python 3 ausführen:

```bash
python3 work/run_checks.py
python3 work/joint_selection.py
python3 work/joint_graph_check.py
python3 work/joint_source_check.py
```

Verwendete Umgebung der neuen Rechnungen: NumPy 2.4.2, SciPy 1.17.0 und SymPy 1.14.0. Nicht jedes Einzelprogramm benötigt alle drei Bibliotheken. Eine Installation oder Aktualisierung ist keine Voraussetzung zum Lesen dieser Datei.

### 21.3 Ursprüngliche Dokumente und Gespräche

- [Quartikfortsetzung mit lokalen Kanälen und Siebenregistercode](</Users/stefanhamann/Documents/Codex/2026-09-26/berpr-fe-das-alles-zusammen-und/work/source_replay/replay/TFPT_Quartik_Fortsetzung_Pruefpaket_20260926/TFPT_Quartik_Fortsetzung/DERIVATIONS.md>).
- [Vertiefte Code-, Igusa- und Austauschherleitung](</Users/stefanhamann/Documents/Codex/2026-09-26/berpr-fe-das-alles-zusammen-und/work/source_replay/replay/TFPT_Vertiefung_Code_Geometrie_Dynamik_20260926/tfpt_deep_20260926/HERLEITUNG.md>).
- [Frühere Zusammenführung der Sitzungen](</Users/stefanhamann/Documents/Codex/2026-09-26/berpr-fe-das-alles-zusammen-und/work/source_replay/replay/TFPT_Sessionen_Verbindungspruefung_2026-09-26/BERICHT.md>).
- [Versteckte Codes, äußere Automorphie und Clock-Gegenprüfungen](</Users/stefanhamann/Documents/Codex/2026-09-26/berpr-fe-das-alles-zusammen-und/work/source_replay/replay/TFPT_Versteckte_Codes_Pruefpaket_2026-09-26/TFPT_Versteckte_Codes_und_Auswahl_2026-09-26.txt>).
- [Igusa-, Kummer- und Magic-State-Verbindungen](</Users/stefanhamann/Documents/Codex/2026-09-26/berpr-fe-das-alles-zusammen-und/work/source_replay/replay/TFPT_Igusa_Kummer_Magic_Pruefpaket_2026-09-26/TFPT_Igusa_Kummer_Magic_Verbindungen_2026-09-26.md>).
- Gespräche als Herkunftskontext: [TFPT einfach erklärt](https://chatgpt.com/c/6ab7704d-5908-83eb-bfa6-30a8a2f2646f), [Thesen untersuchen TFPT vollständig](https://chatgpt.com/c/6ab77a97-5ec0-83eb-b618-1c94f668371c), [Untersuche Zuse und TFPT](https://chatgpt.com/c/6ab7799a-06b4-83eb-b4b3-69ba3f83a9e5). Die archivierten Dateien und Prüfprotokolle bestimmen den hier tatsächlich ausgewerteten Umfang.

Der übergeordnete Einstieg war [tfpt-gesamtkontext.md](/Users/stefanhamann/.codex/context/tfpt-gesamtkontext.md), Stand 17. September; er ist eine Orientierungskarte, keine zusätzliche Beweisquelle. Die besonders geprüften Originalstellen liegen in `tfpt-theoryv4/_archive/tfpt-45/source_extracts/01_boundary_kernel_source.tex`, Zeilen 480–560 und 629–683, sowie `02_carrier_source.tex`, Zeilen 3020–3146. Ihre Auszüge samt Dateihashes sind oben verlinkt.

### 21.4 Mathematischer Hintergrund

Die folgende Literatur ordnet bekannte Strukturen ein. Sie ersetzt nicht die konkreten TFPT-Matrixprüfungen und wird nicht als Beleg für eine vollständige physikalische Herleitung zitiert.

- [Zhu, Kueng, Grassl, Gross: *The Clifford group fails gracefully to be a unitary 4-design*](https://arxiv.org/abs/1609.08172) — vierte Cliffordmomente und zusätzliche Codesektoren.
- [Nebe, Rains, Sloane: *The invariants of the Clifford groups*](https://arxiv.org/abs/math/0001038) — Cliffordinvarianten und vollständige Gewichtspolynome.
- [Eklund: *Curves on Heisenberg invariant quartic surfaces in projective 3-space*](https://arxiv.org/abs/1010.4058) — Heisenberg-Invarianten und Igusa-/Quartikgeometrie.
- [Bravyi, DiVincenzo, Loss: *Schrieffer-Wolff transformation for quantum many-body systems*](https://arxiv.org/abs/1105.0675) — effektive Hamiltonoperatoren und kontrollierte Niedrigenergieentwicklungen.
- [Steane: *Multiple Particle Interference and Quantum Error Correction*](https://arxiv.org/abs/quant-ph/9601029) — klassische Codeverbindungen zur Quantenfehlerkorrektur.
- [Barnum, Knill: *Reversing quantum dynamics with near-optimal quantum and classical fidelity*](https://arxiv.org/abs/quant-ph/0004088) — Rückgewinnungskanäle.
- [Chen, Ji, Zeng, Zhou: *From Ground States to Local Hamiltonians*](https://arxiv.org/abs/1110.6583) — Marginaldaten und lokale Grundzustandsfragen.
- [Eastin, Knill: *Restrictions on Transversal Encoded Quantum Gate Sets*](https://arxiv.org/abs/0811.4262) — Grenze universeller transversaler Kontrolle; kein Widerspruch zu den hier nichttransversalen Paar-/Dreierkontrollen.
- [Caputo, Liggett, Richthammer: *Proof of Aldous' spectral gap conjecture*](https://arxiv.org/abs/0906.1238) — interner gewichteter Transpositionsgraph.
- [Howard, Millson, Snowden, Vakil: *A description of the outer automorphism of S6, and the invariants of six points in projective space*](https://math.stanford.edu/~vakil/files/sixjan2308.pdf) — äußere Automorphie und Sechspunktinvarianten.
- [Mazurek et al.: *Quantum error correction codes and absolutely maximally entangled states*](https://arxiv.org/abs/1910.07427) und [Raissi et al.: *Constructing optimal quantum error correcting codes from absolute maximally entangled states*](https://arxiv.org/abs/1701.03359) — AME-/Code-Verbindung.
- [NIST DLMF, Kapitel 20.7](https://dlmf.nist.gov/20.7) — Theta-Identitäten des bedingten Torusanschlusses.
- [Bravyi, Kitaev: Magic-State-Quantenrechnung](https://arxiv.org/abs/quant-ph/0403025) — bekannter Rahmen der nicht-Cliffordschen Ressourcen.
- [Stabilizer-Rényi-Entropie](https://arxiv.org/abs/2106.12587) — Hintergrund der angegebenen Entropiegröße $M_2$.
- [Tu, Orus: *Effective field theory for the SO(n) bilinear-biquadratic spin chain*](https://arxiv.org/abs/1104.0494) und [Orus, Wei, Tu: *Phase diagram of the SO(n) bilinear-biquadratic chain from many-body entanglement*](https://arxiv.org/abs/1010.5029) — bekannte orthogonal symmetrische Spinmodelle; keine Quellen des hier ausgeschriebenen freien Graphensatzes.
- [Konopka, Markopoulou, Severini: *Quantum Graphity: a model of emergent locality*](https://arxiv.org/abs/0801.0861) — etablierter Rahmen dynamischer Graphen. Seine zusätzlichen Graphterme wären hier eigene, erst zu begründende Modellannahmen.

---

<a id="anhang-a"></a>
## Anhang A. Vollständiger Beweis der Graphenschranke und aller Gleichheitsfälle

Dieser Anhang enthält den tragenden allgemeinen Beweis, damit die Hauptaussage nicht vom Öffnen einer weiteren Datei abhängt. Wir setzen $J=1$; am Ende multiplizieren sich alle Energien mit $J>0$.

### A.1 Sternreduktion durch Positivität

Betrachte eine zentrale Zelle 0 und $n\ge1$ Nachbarn. Setze

$$
M_n=\sum_{j=1}^n(S_{0j}+E_{0j}).
$$

In der gewöhnlichen Farbwortbasis von $(\mathbb C^5)^{\otimes(n+1)}$ ist diese Matrix reell symmetrisch und eintragsweise nichtnegativ. Ein Vektor zum größten Eigenwert kann nichtnegative Einträge haben: Für reelle $x$ gilt $x^TM_nx\le|x|^TM_n|x|$. Das Rayleighmaximum wird daher von einem nichtnegativen Vektor erreicht.

$M_n$ kommutiert mit allen Nachbarpermutationen. Das Mitteln eines solchen nichtnegativen maximalen Eigenvektors über die Nachbarpermutationen bleibt nichtnull und ist weiterhin ein Eigenvektor mit demselben Eigenwert. Der größte Eigenwert wird deshalb auch auf

$$
\mathbb C^5\otimes\operatorname{Sym}^n(\mathbb C^5)
$$

erreicht. Eine obere Schranke auf diesem Teilraum ist somit eine obere Schranke auf dem gesamten Sternraum.

### A.2 Bosonenrechnung der scharfen Schranke

Identifiziere den symmetrischen Nachbarraum mit dem n-Teilchenraum von fünf bosonischen Moden. Es gelten $[b_a,b_b^\dagger]=\delta_{ab}$. Die Mittelpunktmatrix von $M_n$ lautet

$$
(M_n)_{ab}=b_b^\dagger b_a+b_a^\dagger b_b.
$$

Für ein Vektortupel $v=(v_1,\ldots,v_5)$ definiere

$$
\mathcal C(v)=\sum_ab_a^\dagger v_a,
\qquad\mathcal B(v)=\sum_ab_av_a.
$$

$\mathcal C$ bildet in $\operatorname{Sym}^{n+1}$, $\mathcal B$ in $\operatorname{Sym}^{n-1}$ ab. Wegen der Vertauschungsrelationen gilt

$$
M_n=\mathcal C^\dagger\mathcal C+\mathcal B^\dagger\mathcal B-I.
$$

Ferner

$$
\mathcal C\mathcal C^\dagger=\sum_ab_a^\dagger b_a=(n+1)I,
$$

$$
\mathcal B\mathcal B^\dagger=\sum_ab_ab_a^\dagger=(n+4)I.
$$

Damit sind die größten Eigenwerte von $\mathcal C^\dagger\mathcal C$ und $\mathcal B^\dagger\mathcal B$ höchstens $n+1$ und $n+4$. Es folgt

$$
M_n\le(2n+4)I,
$$

$$
\boxed{\sum_{j=1}^nh_{0j}=\frac32(2nI-M_n)\ge-6I.}
$$

Die Nachbarzahl fällt aus der unteren Energieschranke heraus.

### A.3 Wann die Sternschranke erreicht wird

Gleichheit verlangt gleichzeitig

$$
v\in\operatorname{Ran}\mathcal C^\dagger
\cap\operatorname{Ran}\mathcal B^\dagger.
$$

Im Bargmann-Polynombild werden Erzeuger zu Multiplikation mit $x_a$, Vernichter zu $\partial_a$. Deshalb müssen homogene Polynome $f,g$ existieren mit

$$
v_a=\partial_af=x_ag.
$$

Vertauschen zweier Ableitungen liefert

$$
x_a\partial_bg=x_b\partial_ag.
$$

Das bedeutet Invarianz unter den infinitesimalen Rotationen. Ein invariantes Polynom eines einzelnen Fünfervektors ist ein Polynom in $r^2=\sum_ax_a^2$. Weil $g$ Grad $n-1$ hat, gibt es eine nichtnull Lösung genau für ungerades $n$; dann ist sie bis auf Faktor

$$
g=(r^2)^{(n-1)/2}.
$$

Das liefert im nachbarsymmetrischen Teilraum genau eine Gleichheitsrichtung. Für $P_b=\sum_a(b_a^\dagger)^2$ lautet sie

$$
v_a=b_a^\dagger P_b^{(n-1)/2}\lvert0\rangle.
$$

Die Identität

$$
b_aP_b^{(n+1)/2}\lvert0\rangle
=(n+1)b_a^\dagger P_b^{(n-1)/2}\lvert0\rangle
$$

zeigt zugleich, dass der Mittelpunkt mit den anderen Positionen symmetrisch eingebettet ist. Der entstehende Zustand ist der Wick-Singulett auf $n+1$ Zellen.

### A.4 Warum es keine zusätzlichen unsymmetrischen Gleichheitszustände gibt

$M_n$ erhält die Parität der gesamten Anzahl jeder der fünf Farben. Innerhalb jedes solchen Paritätssektors ist die Matrix irreduzibel:

- Die Sternvertauschungen erzeugen beliebige Positionspermutationen.
- Der Bellterm kann ein gleiches Farbpaar $aa$ in $bb$ umwandeln.
- Damit lassen sich alle Wörter gleicher Farbparitäten ineinander überführen: Einzelreste der ungeraden Farben bleiben erhalten, übrige Paare können zwischen Farben verschoben werden.

In jedem Sektor existiert daher ein eindeutiger positiver Perronvektor. Würde ein Sektor die obere Schranke $2n+4$ erreichen, könnte sein Perronvektor ohne Paritätsänderung über Nachbarpermutationen gemittelt werden. Nach A.3 müsste das Resultat die radiale Wickrichtung sein. Diese liegt ausschließlich im Nullparitätssektor.

Nur dieser Sektor kann also Gleichheit erreichen. Wegen Irreduzibilität ist der maximale Eigenraum dort eindimensional. Für gerades $n$ gibt es überhaupt keine Gleichheit; für ungerades $n$ ist der volle Sterngrundzustand eindeutig.

### A.5 Summation über einen beliebigen Graphen

Jeder aktive Knoten trägt einen Stern mit unterer Energie $-6$. Summiert man alle aktiven Sterne, erscheint jede Kante zweimal. Daher

$$
2H(G)\ge-6N_{\rm aktiv}I,
\qquad H(G)\ge-3N_{\rm aktiv}I.
$$

Für einen Graphen, der $-3N$ erreicht, darf es keine isolierten Knoten geben. Außerdem muss jeder positive Sterndefizitoperator im globalen Zustand verschwinden. Jede abgeschlossene Nachbarschaft trägt folglich ihren eindeutigen reinen Wick-Grundzustand und hat gerade Größe.

### A.6 Die Wickzustände erzwingen vollständige Komponenten

Ein Wickzustand auf einer geraden Zellzahl ist unter allen Zellpermutationen und unter O(5) invariant. Seine Einzelsystemmarginalen sind $I_5/5$, und jeder Swap zweier Positionen hat Erwartungswert eins.

Er kann über keinen nichttrivialen Schnitt faktorisieren. Bei einem Produkt über einen Schnitt wäre die Reduktion eines Paars auf verschiedenen Seiten nämlich $(I_5/5)\otimes(I_5/5)$; dessen Swap-Erwartung ist $\operatorname{tr}[(I_5/5)^2]=1/5$, im Widerspruch zu eins.

Hat ein globaler Zustand auf einer Teilmenge eine reine Reduktion, faktorisiert diese Teilmenge gegenüber ihrem Komplement. Zwei reine Wick-Reduktionen dürfen deshalb nicht echt überlappen: Andernfalls würde eine der Wick-Reduktionen über die Überschneidung in zwei nichtleere Teile faktorisieren.

Für benachbarte Knoten $u,v$ schneiden sich ihre abgeschlossenen Nachbarschaften $N[u],N[v]$. Auch eine echte Inklusion ist ausgeschlossen: Die größere reine Wickreduktion würde durch die Reinheit der kleineren über einen nichttrivialen Schnitt faktorisieren. Es folgt

$$
N[u]=N[v].
$$

Entlang jeder Kante sind somit die abgeschlossenen Nachbarschaften gleich. Jede Zusammenhangskomponente ist vollständig. Da jeder Grad ungerade ist, besitzt jede Komponente gerade Größe.

### A.7 Umkehrung und Eindeutigkeit

Auf einer vollständigen geraden Komponente ist jeder Stern die gesamte Komponente. Ihr Wick-Singulett sättigt deshalb sämtliche Sterne und hat Energie $-3$ mal Komponentengröße. Produkte über gerade Cliquen erreichen $-3N$.

Umgekehrt erzwingen die reinen lokalen Reduktionen genau dieses Produkt. Auf jedem solchen festen Graphen ist der Grundzustand eindeutig bis auf eine Gesamtphase.

Damit sind Schranke, Erreichbarkeit und sämtliche Gleichheitsfälle vollständig bewiesen. Der Beweis verlangt keine numerische Grenzwertvermutung. Die vollständige Minimiererklassifikation und ihre Anwendung auf $K_N$ sind hier für gerade $N$ formuliert; die allgemeine Schranke selbst gilt auch für ungerades $N$.

---

<a id="anhang-b"></a>
## Anhang B. Vollständige endliche Spektren und Normierungsvergleich

### B.1 Drei Darstellungen derselben ursprünglichen Zellenergie

| Vielfachheit | $C_{60}=\sum r_\ell^{\otimes4}$ | $60I-C_{60}$ | $G_4$ |
|---:|---:|---:|---:|
| 5 | 36 | 24 | 0 |
| 70 | 12 | 48 | $2/5$ |
| 135 | 4 | 56 | $8/15$ |
| 45 | −12 | 72 | $4/5$ |
| 1 | −60 | 120 | $8/5$ |

Die in früheren Texten genannte Lücke 24 gehört zu $36I-C_{60}=60G_4$. Sie widerspricht der Lücke $2/5$ nicht.

Eine unabhängig dokumentierte Momententwicklung lautet

$$
C_{60}=12I+12\sum_{r<s}\operatorname{SWAP}_{rs}
-24\sum_{|T|=3}P_{{\rm sym},T}+24S_4+24P.
$$

Die Schurtypen der vier Register liefern daraus dieselbe Spektralzerlegung.

### B.2 Vollständiges Austausch-Dreiecksspektrum

Hamiltonoperator $-J(K_{12}+K_{23}+K_{13})$:

| Energie geteilt durch $J$ | Vielfachheit |
|---:|---:|
| $-27/2$ | 5 |
| $-21/2$ | 5 |
| $-19/2$ | 9 |
| $-9$ | 10 |
| $-15/2$ | 42 |
| $-6$ | 25 |
| $-5$ | 18 |
| $-9/2$ | 11 |

Summe: 125.

### B.3 Vollständiges Ereignis-Dreiecksspektrum

Hamiltonoperator $\gamma(k_{12}+k_{23}+k_{13})$:

| Energie geteilt durch $\gamma$ | Vielfachheit |
|---:|---:|
| $4/5$ | 5 |
| $6/5$ | 1 |
| $8/5$ | 25 |
| $28/15$ | 27 |
| $2$ | 25 |
| $11/5$ | 32 |
| $12/5$ | 10 |

Summe: 125.

### B.4 Vollständiges gemischtes Dreiecksspektrum

Hamiltonoperator $J(h_{12}+h_{23}+h_{13})$ mit $h=-K+15k/2$:

| Energie geteilt durch $J$ | Vielfachheit |
|---:|---:|
| $-6$ | 5 |
| $3$ | 10 |
| $9/2$ | 30 |
| $9$ | 70 |
| $27/2$ | 10 |

Summe: 125.

### B.5 Alle drei Dreier- und Vierertensoren nebeneinander

| Modell | Dreierisometrie | Viererzustand auf $K_4$ | Viererenergie |
|---|---|---|---:|
| Austausch | $\sqrt{3/40}(\mathsf A-2\mathsf C)$ | $(\mathsf A-2\mathsf C)/\sqrt{200/3}$ | $-27J$ |
| Ereignisse | $(\mathsf A+6\mathsf C)/\sqrt{72}$ | $(\mathsf A+6\mathsf C)/\sqrt{360}$ | $8\gamma/5$ |
| Kombination | $\mathsf A/\sqrt{21}$ | $\mathsf A/\sqrt{105}$ | $-12J$ |

Die Viertensor-Norm ist jeweils fünfmal die Isometrienorm, weil über fünf orthonormale Eingangsrichtungen summiert wird.

### B.6 Charaktersummen für das globale Ereignis

Für die Standarddarstellung von $S_6$ ist $\chi_U(\sigma)=\operatorname{fix}(\sigma)-1$. Daher

$$
\dim\operatorname{Inv}(U^{\otimes N})
=\frac1{720}\sum_{\sigma\in S_6}(\operatorname{fix}(\sigma)-1)^N.
$$

Die Summe ergibt $1,1,4$ für $N=2,3,4$. Für die symmetrische beziehungsweise antisymmetrische dritte Potenz werden

$$
\chi_{\operatorname{Sym}^3U}(g)
=\frac{\chi(g)^3+3\chi(g)\chi(g^2)+2\chi(g^3)}6,
$$

$$
\chi_{\Lambda^3U}(g)
=\frac{\chi(g)^3-3\chi(g)\chi(g^2)+2\chi(g^3)}6
$$

mit $\chi_U$ skalar multipliziert und über die Gruppe gemittelt. Das liefert die in Abschnitt 12 benutzten Multiplizitäten zwei und null.

---

<a id="anhang-c"></a>
## Anhang C. Explizite Koordinaten und Rekonstruktionsdaten

### C.1 Zehn Messvektoren ohne freie Anpassung

Die zehn symmetrischen Zweiqubit-Paulis sind in dieser Reihenfolge

```text
II IX IZ XI XX XZ YY ZI ZX ZZ
```

Mit $D=\operatorname{diag}(4,12,12,12,24)$ lautet die Matrix ihrer logischen Messvektoren

$$
W_{10}=\frac14F_{\rm num}D^{-1/2},
$$

```text
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

Damit sind sämtliche Messungen und Gramidentitäten aus Abschnitt 5 direkt rekonstruierbar.

### C.2 Eine verwendete orthonormale Igusa-Abbildung

Für normalisierte logische Koordinaten $z\in\mathbb C^5$ setzt die vertiefte Herleitung $t=Wz$ mit

$$
W=\begin{pmatrix}
\sqrt3/6&-1/2&-1/2&-1/2&0\\
\sqrt3/6&-1/2&1/2&1/2&0\\
\sqrt3/6&1/2&-1/2&1/2&0\\
\sqrt3/6&1/2&1/2&-1/2&0\\
-\sqrt3/3&0&0&0&\sqrt2/2\\
-\sqrt3/3&0&0&0&-\sqrt2/2
\end{pmatrix}.
$$

Es gilt $W^\dagger W=I$, $\sum_it_i=0$. Die Zeilen von $W$ sind Simplexvektoren mit Gram $\delta_{ij}-1/6$. Unter dieser Abbildung werden die Antwortebenen zu den durch perfekte Paarungen definierten Ebenen. Andere Quellen benutzen permutierte Sechspunktkoordinaten; für Vergleiche nativer Markierungen ist das tatsächliche Wörterbuch beizubehalten.

### C.3 Rationale Basis für die unabhängigen Operatorrechnungen

Die exakten neuen Prüfer können ohne Quadratwurzeln auf dem Nullsummenraum arbeiten. Wähle die fünf Spalten

$$
B_j=(\underbrace{1,\ldots,1}_{j\ \rm Einträge},-j,0,\ldots,0)^T,
\qquad j=1,\ldots,5.
$$

Ihre Gram-Matrix ist

$$
D_U=\operatorname{diag}(2,6,12,20,30).
$$

Für eine Sechskoordinaten-Permutationsmatrix $P_\sigma$ lautet die logische Matrix

$$
T_\sigma=D_U^{-1}B^TP_\sigma B.
$$

Adjungierte müssen mit dieser Metrik gebildet werden. Tensoren werden entsprechend mit der Produktmetrik behandelt. Auf dieser Basis sind die Matrizen, charakteristischen Polynome und Kompressionsgleichungen rational.

### C.4 Wicktensor ohne Eigenwertsolver

Für gerade $N$ ist der unnormierte Wicktensor die Summe aller perfekten Paarungen der N Positionen. Für ein Farbwort $(a_1,\ldots,a_N)$ mit Farbanzahlen $n_c$ gilt direkt

$$
\mathcal W_N(a_1,\ldots,a_N)=
\begin{cases}
\prod_{c=1}^5(n_c-1)!!,&\text{alle }n_c\text{ gerade},\\
0,&\text{sonst},
\end{cases}
$$

mit $(-1)!!=1$. Die geprüften Normquadrate sind 5 für $N=2$, 105 für $N=4$ und 4725 für $N=6$. Der Integerprüfer kontrolliert bei diesen drei Größen die Sättigung jedes einzelnen Sterns. Der allgemeine Sättigungssatz wurde unabhängig davon in Anhang A bewiesen.

### C.5 Zusätzliche Gewichts- und Quelleninformationen

Der neue selbstduale $[16,8,4]$-Code hat das gewöhnliche Gewichtspolynom

$$
1+28z^4+198z^8+28z^{12}+z^{16}.
$$

Dies folgt unmittelbar aus seiner Konstruktion: Der verdoppelte gerade Achtbitcode liefert die Gewichte 0,4,8,12,16 mit Häufigkeiten 1,28,70,28,1; der verschobene Coset ergänzt 128 Wörter vom Gewicht acht. Die stärkere in Abschnitt 11 geprüfte Identität betrifft das vollständige Gewichtspolynom **zweiter Ordnung**, nicht nur dieses gewöhnliche Polynom.

---

## Schlussblatt: die Gesamtresultate auf einen Blick

**Tragende Konstruktion:** Ein Hamming-/Reflexionsseed erzeugt einen konkreten Fünfercode. Seine Auslesung, Antwortprojektoren, Bellbindung und Quartik sind ausdrücklich verbunden.

**Tragende Rekursion:** Es gibt zwei verschiedene exakte Dreierencoder mit derselben logischen Ereigniswirkung. Ihre Viererzustände sind eindeutig und besitzen eine exakt bestimmte Beziehung.

**Tragender Informationsbefund:** Die einfache Quellenmannigfaltigkeit ist nicht der volle dynamische Zustandsraum. Im Ereignis-Vierergrundzustand trägt ihre unsichtbare Igusa-Richtung 40 Prozent des Normquadrats.

**Tragende Zusammenführung:** Unter der angegebenen projizierten Formtreueforderung ist die direkte positive Kopplungskombination mit $\gamma/J=15/2$ bestimmt.

**Tragende Entscheidung zur Raumfrage:** Für diese Kombination sind die Graphenminima und alle linearen Kantenkostenfälle analytisch klassifiziert. Sie liefern vollständige Gruppen, getrennte Paare oder Leere. Ein dünnes verbundenes Grundzustandsnetz wird nicht ausgewählt.

**Physischer Abschluss:** Die gemeinsame Quelle, ihre Teilnehmerregel, autonome Zustandsauswahl, lokale 3+1D-Raumzeit und deren vollständige Materie-/Gravitationsdynamik sind durch diese Sitzung nicht hergeleitet.
