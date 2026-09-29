# TFPT: Code, Quartik, Bindung und rekursive Geometrie

## Gesamtdokumentation der Untersuchungsfolge vom 26. September 2026

**Fassung 1.0 · konsolidierte Herleitungen, Ergebnisse, Gegenproben und Beweisgrenzen**

> **Das Gesamtergebnis:** Aus derselben endlichen Code und Quellenstruktur lassen sich ein geschützter Fünferraum, seine Informationskanäle, fünfzehn ausgezeichnete Antwortbereiche, eine Igusa Quartik, konkrete Bindungszustände und eine rekursive Fünferkodierung gemeinsam konstruieren. Mehrere zuvor getrennte Muster sind durch explizite Operatoren und Tensoridentitäten verbunden. **Eine daraus eindeutig ausgewählte Welt mit drei Raumdimensionen, relativistischer Zeit, chiraler Materie und Gravitation ist in dieser Untersuchungsfolge nicht hergeleitet.**

Diese Datei dokumentiert die vorliegende Gesprächsfolge und ihre tatsächlich gelesenen mathematischen Grundlagen. Sie ist keine vollständige Neuprüfung des gesamten historischen TFPT Repositoriums. Ergänzungen aus unmittelbar zugehörigen vorhandenen Herleitungen sind ausdrücklich zugeordnet. Die während des Gesprächs vorgeschlagenen letzten Raumideen werden nicht nachträglich zu ausgeführten Rechnungen erklärt.

---

<a id="inhalt"></a>
## Inhalt und Lesepfade

**Für das Gesamtbild:** Kapitel 1 bis 3 und 24.  
**Für die mathematische Substanz:** Kapitel 4 bis 18.  
**Für die Bewertung des Raumansatzes:** Kapitel 16 bis 20 sowie 25.  
**Für Nachrechnung und Quellen:** Kapitel 27 bis 30 und die Anhänge.

1. [Das Ergebnis auf einer Seite](#gesamtbild)
2. [Die gesamte Konstruktion bildlich](#bildlich)
3. [Was als bewiesen, berechnet oder vorgeschlagen gilt](#status)
4. [Die Objekte: Quelle, Register, Code und Darstellung](#objekte)
5. [Hamming, E₈ und die 60 Quellen](#hamming-e8)
6. [Der vierte Moment und der geschützte Fünferraum](#vierter-moment)
7. [Was ein, zwei und drei Register verraten](#auslesung)
8. [Petersen, Simplex und die unsichtbare Information](#petersen)
9. [Warum 2/3 und 4/9 verschiedene Aussagen sind](#transfer)
10. [Paarsteuerung, 3+2 und die Grenze zur Eichphysik](#dynamik-ladung)
11. [Igusa Quartik, Invariantenring und Reflexionsgeometrie](#igusa)
12. [Warum perfekte Fünferzellen nicht überlappen dürfen](#ueberlappung)
13. [Virtuelle Wechselwirkung und exakte Zweizellenbindung](#bindung)
14. [Die Rückbindung an den Hamming Code](#hamming-bindung)
15. [Drei Fünfer werden wieder zu einem Fünfer](#dreierrekursion)
16. [Viererbindung, C₁₆ und derselbe Quartiktensor](#vierer-code16)
17. [Höhere Ordnung, kleine Graphen und Grenzen der Rekursion](#hoehere-ordnung)
18. [Der Test bis 6561 Knoten](#6561)
19. [Doily, Tutte Coxeter und das lokale Routing](#doily)
20. [Operationspfade und der noch offene Raumquotient](#quotient)
21. [Eine alternative geschützte Quelle mit sieben Registern](#sieben)
22. [Entropie, Clock und Informationsgeometrie](#entropie)
23. [Die Zahlen und ihre wirklichen Verbindungen](#muster)
24. [Was die Gesamtsynthese jetzt trägt](#synthese)
25. [Verworfene Abkürzungen und verbleibende Beweisaufgaben](#offene-tore)
26. [Bedeutung für Hylæan](#hylaean)
27. [Glossar](#glossar)
28. [Prüfstand und Reproduktion](#pruefstand)
29. [Quellen und Versionszuordnung](#quellen)
30. [Schlussbild](#schlussbild)

**Anhänge:** [A: Ergebnisdaten](#anhang-a) · [B: ausführbare Prüfprogramme](#anhang-b) · [C: Extraktion und Start](#anhang-c)

Die Formeln benutzen überwiegend orthonormale Koordinaten. Wo rationale, nicht orthonormale Koordinaten zum Einsatz kommen, wird ihre Metrik ausdrücklich angegeben. Energien und Zeiten stehen in den Abschnitten mit Dynamik in Einheiten mit ℏ = 1.

---

<a id="gesamtbild"></a>
## 1. Das Ergebnis auf einer Seite

### 1.1 Was tatsächlich zusammenpasst

Der gemeinsame Ausgangspunkt ist der erweiterte binäre Hamming Code **[8,4,4]**, auch als **RM(1,3)** beschreibbar. Über eine festgelegte reelle und komplexe Darstellung verbindet er sich mit 240 E₈ Wurzeln und 60 komplexen Quellenrichtungen. Diese Quellen liefern einen vierten Moment, der einen besonderen fünfdimensionalen Unterraum in vier vierdimensionalen Registern identifiziert. [S0, §§ 1–2; S1, §§ 1–2; S5]

Dieser Fünferraum ist kein frei gewählter Ausschnitt. Für die angegebene Konstruktion gilt die exakte Identität

$$
P=40M_4-S.
$$

Aus demselben Moment lässt sich eine positive Energie mit genau diesem Grundraum bauen. Einzelregister verraten nichts über den logischen Zustand. Paare sehen nur einen Teil seiner Information. Drei Register reichen zur vollständigen Rekonstruktion. Vierregisterinformation ist notwendig, um den ganzen Code als alleinigen exakten Grundraum auf diesem Hilbertraum auszuzeichnen. [S0, §§ 2–3, 8; S1, § 2]

Die zweite Antwort auf die fünfzehn nichttrivialen Zweiqubit Paulis ergibt fünfzehn Rang 2 Projektoren im Fünferraum. Jeder trennt zwei aktive von drei inaktiven Richtungen. Daraus folgt eine natürliche **3+2 Markierung**. Diese Markierung hat einen Zentralisator mit der Lie Algebra des Standardmodells. Das ist eine präzise algebraische Aussage, noch keine Konstruktion physischer Eichfelder. [S1, § 3]

Die fünfzehn Antwortbereiche sind in einer expliziten Koordinatisierung genau die fünfzehn singulären Linien der Igusa Quartik. Die Quartik beschreibt eine bestimmte Quellenpräparation, **nicht den gesamten dynamisch erreichbaren Fünferraum**. Die Dynamik kann die Quellenmannigfaltigkeit verlassen, ohne den geschützten Code zu verlassen. [S1, § 4]

Zwei getrennte Zellen koppeln über virtuelle Anregungen. Gleichmäßiger Austausch wählt im schwachen Kopplungsintervall einen eindeutigen mikroskopischen Grundzustand, dessen Codekomponente genau die maximale Fünferverschränkung Ω₅ ist. Eine unabhängig definierte Hamming Projektion ergibt denselben logischen Bindungszustand. [S1, §§ 5–7]

Im daraus abgeleiteten effektiven Paarmodell bilden drei vollständig miteinander gekoppelte Fünferzellen wieder einen fünfdimensionalen Grundraum. Unter dieser Kodierung bleiben die Antwortmarkierung und die führende Paarform erhalten:

$$
Y_A\mapsto\frac7{12}Y_A,
\qquad
K_c\mapsto\frac{49}{144}K_c.
$$

Derselbe Tensor liefert die Dreierkodierung, die eindeutige Viererbindung und eine genau bestimmte kohärente Kombination zweier selbstdualer Codekonstruktionen. [S2, §§ 3–6]

### 1.2 Was der Raumtest entschieden hat

Die ausdrücklich gewählte kartesische Dreierfortsetzung ergibt Hamming Graphen H(n,3). Bis n = 8, also 6561 Knoten, und analytisch für beliebiges n zeigt sich **keine stabile räumliche Dimension drei**. Das Maximum der untersuchten spektralen Dimension wächst linear mit der Rekursionstiefe. [S3; A1]

Die interne Kompatibilität ergibt dagegen eine feste endliche Geometrie: fünfzehn Kanäle, fünfzehn Dreierkontexte, einen kubischen Inzidenzgraphen mit 30 Knoten und eine eindeutige lokale Routingregel in 180 Fällen. Diese Struktur ist das generalisierte Viereck GQ(2,2); sein Inzidenzgraph ist der Tutte Coxeter Graph. **Ein endlicher interner Inzidenzgraph ist aber noch kein physischer Raum.** [S3; A1; L6]

### 1.3 Die knappe Bilanz

| Teilfrage | Ergebnis dieser Untersuchungsfolge |
|---|---|
| Gibt es einen konkreten geschützten Fünfercode? | Ja, mit expliziter Basis, Projektor und positiver Modellenergie. |
| Sind Information, Antwortgeometrie und Quartik verbunden? | Ja, über ausgeschriebene Matrizen, Polynome und Inzidenzen. |
| Gibt es echte Wechselwirkung zwischen getrennten Codes? | Ja, für definierte Kopplungen und kontrollierte Energien. |
| Gibt es eine nichttriviale rekursive Fünferstruktur? | Ja, als exakter Kodierungsschritt und führende effektive Operatoridentität. |
| Sind Hamming, C₁₆, Bindung und Quartik direkt verbunden? | Ja, durch Projektionen und eine exakte Tensoridentität. |
| Erzeugt die getestete Dreierrekursion unseren Raum? | Nein. Dieser konkrete Ansatz besteht den Dimensionstest nicht. |
| Erzeugt das lokale Routing bereits eine eindeutige Welt? | Nicht nachgewiesen; globale Verklebung und physische Auswahl fehlen. |
| Ist damit die gesamte TFPT Physik gelöst? | Nein. Die endliche Konstruktion und die physische Gesamtableitung sind zu trennen. |

**Die stärkste Aussage lautet deshalb:** Es liegt ein konkret berechenbares gemeinsames System für Schutz, Auslesung, Transformation, Bindung und Blockbildung vor. Die zusätzlichen Übergänge von diesem System zu unserer physikalischen Welt sind noch eigenständige Beweisaufgaben.

---

<a id="bildlich"></a>
## 2. Die gesamte Konstruktion bildlich

### 2.1 Nicht nur ein Baukasten, sondern eine Regel für erlaubte Bausteine

Stell dir vier kleine Speicher vor. Zusammen haben sie 256 unabhängige Basiszustände. Durch die gemeinsame Quellenstruktur entsteht darin ein besonderer Bereich mit fünf logischen Basiszuständen.

```text
Vier physische Register: je 4 Basiszustände

    [Register 1] [Register 2] [Register 3] [Register 4]
                         │
                         ▼
                 256 Basiszustände
                         │  Symmetrie
                         ▼
                  35 Richtungen
                         │  Quartikcode
                         ▼
                  5 logische Zustände
```

Die positive Modellenergie macht diese fünf Richtungen zum tiefsten Energiebereich. Das Bild vom Gebäude passt: Die fünf Richtungen liegen energetisch im Keller. Es sind allerdings keine fünf vorgegebenen klassischen Zimmer. Beliebige kohärente Überlagerungen innerhalb dieses fünfdimensionalen Raums sind ebenfalls erlaubt.

### 2.2 Drei verschiedene Fragen

```text
VIER REGISTER                  DREI REGISTER                  PAAROPERATIONEN
Welche gemeinsame              Welche vollständige           Wie lässt sich die
Codeinformation unterscheidet  logische Information          Information innerhalb
den Grundraum?                 war gespeichert?              des Codes verändern?

Codeauswahl                    Rekonstruktion                aktive Steuerung
```

Diese Ordnung 4/3/2 ist eine Eigenschaft der untersuchten Kodierung. Sie ist kein allgemeines Gesetz, nach dem die Natur aus vier, drei und zwei räumlichen Richtungen bestehen müsste.

### 2.3 Warum lokale Anzeigen nicht die ganze Information zeigen

Sechs verschiedene Codezustände können an derselben Paarmessung exakt dieselbe Anzeige liefern. Sie sind dennoch global verschieden. Ein späterer erlaubter Puls kann einen vorher unsichtbaren Unterschied in eine messbare Größe verwandeln.

```text
Zustand A ── Paarmessung ──► gleiche Anzeige
Zustand B ── Paarmessung ──► gleiche Anzeige

Zustand A ── erlaubter Puls ── Paarmessung ──► Ergebnis A
Zustand B ── erlaubter Puls ── Paarmessung ──► Ergebnis B
```

Die unsichtbare Information ist hier gewöhnliche Quanteninformation in globalen Korrelationen. Sie ist nicht schon eine klassische Theorie verborgener Variablen.

### 2.4 Die rekursive Zelle

```text
   Fünfer A                 drei gekoppelte Zellen
      ╲                     besitzen gemeinsam
       ╲                    wieder einen Fünfergrundraum
        Fünfer B
       ╱          ╲                 │
      ╱            ╲                ▼
   Fünfer C  ────────       effektiver größerer Fünfer
```

Die Zeichnung ist symbolisch. Eine zuverlässigere mathematische Darstellung ist:

```text
                     V△
       ein Fünfer ─────────────► drei Fünfer

       gleiche Antwortbereiche, veränderte Antwortstärke
       Y → (7/12)Y
```

Der neue Block hat jedoch nicht denselben vollständigen Einregisterschutz wie die ursprüngliche Vierregisterzelle.

### 2.5 Wo die Landkarte endet

```text
Hamming / Quellen
        │
        ▼
Code → Auslesung → Antwortgeometrie → Bindung → Rekursion
                                                  │
                                     bisher kein eindeutiger
                                     physischer Übergang
                                                  ⋮
                                       große lokale Welt
                                                  ⋮
                                      Raumzeit und Materie
                                                  ⋮
                                            Gravitation
```

Die durchgezogenen Verbindungen stehen für konkrete endliche Konstruktionen. Die punktierten Übergänge stehen für noch zu beweisende physische Herkunftssätze. Genau diese Unterscheidung verhindert, dass eine überzeugende Erzählung mit einem vollständigen Beweis verwechselt wird.

---

<a id="status"></a>
## 3. Was als bewiesen, berechnet oder vorgeschlagen gilt

### 3.1 Belegklassen

**Exakte Identität oder Satz:** Eine ausgeschriebene analytische Herleitung, eine endliche rationale beziehungsweise ganzzahlige Matrixprüfung oder beides. Ein solcher Satz gilt unter seinen angegebenen Voraussetzungen.

**Numerische Gegenprobe:** Eine Berechnung mit Gleitkommazahlen, beispielsweise eine Diagonalisierung oder ein Adaptierungsfehler. Sie kann eine exakte Herleitung unterstützen, ersetzt sie aber nicht.

**Modellentscheidung:** Eine bewusst gewählte Energie, ein Puls, eine Anordnung der Kopplungen, eine Blockbildung oder eine Quellenregel. Ihre mathematischen Folgen können exakt sein, obwohl ihre physische Auswahl nicht hergeleitet wurde.

**Hypothese:** Eine mögliche Interpretation oder ein noch nicht abgeschlossener Herkunftsschritt. Dazu gehören die globale Raumkonstruktion, das vorgeschlagene Quotientieren von Ereignispfaden und die Identifikation von Defekten mit beobachteten Teilchen.

### 3.2 Die zentrale logische Trennung

$$
\boxed{
\text{exakt gelöstes Modell}
\ \ne\
\text{aus TFPT eindeutig ausgewähltes Naturgesetz}.
}
$$

Auch hundert bestandene Prüfbedingungen sind nicht hundert unabhängige Entdeckungen. Häufig prüfen sie verschiedene Mitglieder derselben endlichen Familie. Ebenso ist eine erneut ausgeführte Python Rechnung keine formale Verifikation durch Lean oder Coq.

### 3.3 Was bei dieser Zusammenstellung erneut ausgeführt wurde

Die verfügbaren Rekursionsprogramme wurden in einer separaten Arbeitskopie im normalen und im optimierten Python Modus erneut ausgeführt. Alle vier zentralen Ergebnisdateien waren zwischen diesen beiden neuen Läufen bytegleich. Der exakte Dreierblock enthält 60 bestandene Prüfbedingungen. Zusätzlich wurde ein eigener Konsolidierungsprüfer mit 230 Bedingungen ausgeführt. Er bestätigt unter anderem sämtliche 180 Routingfälle, das exakte Inzidenzspektrum und eine explizite dünnbesetzte Darstellung von H(8,3). [A1]

Die älteren Berichte über Quellenmoment, Zweizellenenergie, sieben Register und Invarianten wurden textlich vollständig gelesen. Ihre dort angegebenen historischen Prüfzahlen werden nicht als neue Ausführung dieser Zusammenstellung ausgegeben.

---

<a id="objekte"></a>
## 4. Die Objekte: Quelle, Register, Code und Darstellung

### 4.1 Notation

| Zeichen | Bedeutung |
|---|---|
| x oder z_src ∈ ℂ⁴ | Ursprünglicher Quellenvektor eines Registers. |
| ψ_ℓ | Eine der 60 normierten Quellenrichtungen. |
| ℋ = (ℂ⁴)⊗⁴ | Vierregisterraum, Dimension 256. |
| S | Projektor auf Sym⁴(ℂ⁴), Rang 35. |
| Q_P | Pauli Stabilisatorprojektor, Rang 16. |
| P | Quartischer Codeprojektor, Rang 5. |
| V | Isometrie von ℂ⁵ in den ursprünglichen Vierregisterraum. |
| D_A | Summe derselben Paulioperation über vier Register. |
| R_A | Rang 2 Antwortprojektor im logischen Fünferraum. |
| Y_A | Spurfreie, auf R_A beruhende 3+2 Markierung. |
| K | Effektive Paarmatrix Σ_A R_A ⊗ R_A. |
| K_c | Zentrierte Paarmatrix K − 12I/5. |
| Ω₅ | Maximal verschränkter Zustand zweier logischer Fünfer. |
| U = {t ∈ ℂ⁶ : Σtᵢ = 0} | Redundante Sechskoordinatendarstellung des Fünfers. |
| T_m | Drei gleichzeitige Paarvertauschungen eines perfekten Matchings auf sechs Labels. |
| V_△ | Isometrie von einem Fünfer in den Dreizellengrundraum. |
| 𝒜, 𝒞, 𝒯 | Die drei später verwendeten Vierertensoren. |
| G | Bei Codekoordinaten die Grammetrik; bei Graphen ausdrücklich der Graph. |

**Wichtig:** Ein ursprüngliches Register ist vierdimensional und kann intern als zwei Qubits gelesen werden. Ein Zweiregisterterm ist deshalb nicht automatisch ein Zweiqubitterm. Eine logische Fünferzelle besteht zunächst aus vier solchen Registern, also acht Qubits als gewählter Darstellung.

### 4.2 Explizite Codebasis

Die orthonormalen Codevektoren sind

$$
c_0=\frac12\sum_{x=0}^3|xxxx\rangle.
$$

Für a = 1,2,3 sei T_a die Menge aller Wörter mit zwei verschiedenen Werten x,y, jeweils zweimal, und x XOR y = a. Dann

$$
c_a=\frac1{\sqrt{12}}\sum_{s\in T_a}|s\rangle,
\qquad
c_4=\frac1{\sqrt{24}}\sum_{\pi\in S_4}|\pi(0,1,2,3)\rangle.
$$

Explizit bestehen die mittleren Träger aus den verschiedenen Permutationen von 0011 und 2233, von 0022 und 1133 sowie von 0033 und 1122. Die fünf Träger sind disjunkt und haben Größen

$$
w=(4,12,12,12,24).
$$

Ist B die ganzzahlige 256 × 5 Indikatormatrix dieser Träger, gilt

$$
G=B^\mathsf TB=\operatorname{diag}(4,12,12,12,24),
\qquad V=BG^{-1/2},\qquad P=VV^\dagger.
$$

In der unnormalisierten Basis B ist G die Metrik. Ein gewöhnliches Transponieren ohne diese Metrik kann falsche Aussagen über Hermitizität, Normen und Symmetrien erzeugen. [S0, § 1; S1, § 1]

### 4.3 Drei Dimensionen, die nicht verwechselt werden dürfen

Der logische Hilbertraum hat komplexe Dimension fünf. Seine reinen Zustände modulo Norm und gemeinsamer Phase haben acht reelle Parameter. Allgemeine normierte Dichtematrizen haben 24 reelle Parameter.

Die spezielle projektive Quellenmannigfaltigkeit der Quartik hat komplexe Dimension drei. Diese Zahl ist **keine abgeleitete Anzahl räumlicher Dimensionen**. Sie beschreibt die Dimension einer internen algebraischen Präparationsvarietät.

---

<a id="hamming-e8"></a>
## 5. Hamming, E₈ und die 60 Quellen

### 5.1 Der binäre Ausgangscode

Die 16 Wörter von RM(1,3) sind die Auswertungstabellen aller affinen Booleschen Funktionen auf den acht Punkten von 𝔽₂³:

$$
f(u)=a_0+a_1u_1+a_2u_2+a_3u_3.
$$

Ihre Gewichtsverteilung ist

$$
0^{\times1},\quad4^{\times14},\quad8^{\times1}.
$$

Der Code ist binär, linear, selbstdual und doppelt gerade. Die Bezeichnung [8,4,4] bedeutet Länge acht, Dimension vier und Mindestabstand vier. Sie bedeutet nicht acht Raumrichtungen, vier Familien und vier Raumzeitdimensionen.

### 5.2 Der Anschluss an E₈

In der verwendeten skalierten Construction A Darstellung entstehen 240 Wurzeln: 16 Koordinatenwurzeln ±2eᵢ und 224 Vorzeichenbelegungen auf den 14 Trägern der Gewicht 4 Wörter. Die quadratische Norm ist in dieser Konvention vier; gegenüber einer häufig verwendeten E₈ Normierung ist eine Skalierung zu beachten. [S0, § 1; S5]

Nach Festlegung einer geeigneten komplexen Struktur und von vier reellen Koordinatenpaaren werden sie zu 60 komplexen Strahlen zusammengefasst. Je vier Wurzeln eines Strahls unterscheiden sich durch die vierten Einheitswurzeln. In der Gaußschen Codebrücke verteilen sich die 240 Wurzeln über 15 nichttriviale Klassen mit je 16 Wurzeln; jede Klasse enthält vier der 60 komplexen Linien. [S5]

Diese komplexe Paarung ist Teil der Konstruktion. Die nackte Zahl 240 bestimmt nicht von allein die relevante komplexe Struktur oder das physische Quellenwörterbuch.

### 5.3 Was der Zusammenhang wirklich bedeutet

Es gibt eine konkrete Beziehung

```text
binärer Hamming Code
       │ Construction A
       ▼
     E₈ Gitter
       │ gewählte komplexe Struktur und Quotient
       ▼
60 komplexe Quellen / 15 nichttriviale Klassen
```

Es ist zulässig, dies als gemeinsame diskrete Herkunft mehrerer Erscheinungsformen zu lesen. Es ist nicht zulässig, daraus ohne weiteren Satz abzuleiten, dass E₈ selbst die physische Eichgruppe oder der vollständige Raum aller möglichen dynamischen Operationen sei.

Das E₈ Gitter, die Lie Algebra 𝔢₈, die endliche komplexe Reflexionsgruppe G₃₁ und die kontrollierbare Lie Algebra 𝔰𝔲(5) sind verschiedene mathematische Objekte. Sie dürfen nicht unter dem Sammelbegriff „E₈ Transformationen“ zusammengezogen werden.

---

<a id="vierter-moment"></a>
## 6. Der vierte Moment und der geschützte Fünferraum

### 6.1 Zwei äquivalente Definitionen des Codes

Für die 16 Hermiteschen Zweiqubit Paulis einschließlich der Identität gilt

$$
Q_P=\frac1{16}\sum_{A\in\mathcal P_2}A^{\otimes4},
\qquad P=SQ_P.
$$

Die vierten Tensorpotenzen bilden eine abelsche Stabilisatorgruppe. Die Phasen aus der Pauli Multiplikation verschwinden in dieser Tensorpotenz. Q_P hat Rang 16, S Rang 35 und ihr gemeinsamer Teil P Rang 5.

Unabhängig davon liefert die Gleichverteilung über die 60 Stabilisatorstrahlen

$$
M_4=\frac1{60}\sum_{\ell=1}^{60}
\bigl(|\psi_\ell\rangle\langle\psi_\ell|\bigr)^{\otimes4}
$$

die Identität

$$
\boxed{40M_4=S+P.}
$$

Damit ist der zusätzliche quartische Sektor sowohl als Stabilisatorraum als auch aus einem Quellenmoment identifiziert. Der allgemeine Zusammenhang zwischen vierten Cliffordmomenten und zusätzlichen Stabilisatorsektoren ist bekannte Mathematik; die hier benutzte konkrete Realisierung ist der Untersuchungsgegenstand. [S0, § 1; S1, § 1; L1]

### 6.2 Eine positive Schutzenergie

Für Δ > 0 wird gewählt

$$
\boxed{H_{\mathrm{cell}}=\Delta(2I-P-S)=2\Delta(I-20M_4).}
$$

Weil P ≤ S, zerfällt der Hilbertraum orthogonal in P, S − P und I − S:

| Sektor | Dimension | Energie |
|---|---:|---:|
| P | 5 | 0 |
| S − P | 30 | Δ |
| I − S | 221 | 2Δ |

Damit ist P genau der Grundraum und Δ die Lücke. Ferner gilt

$$
H_{\mathrm{cell}}(H_{\mathrm{cell}}-\Delta I)(H_{\mathrm{cell}}-2\Delta I)=0.
$$

Der frühere normierte Kandidat H_mom = I − 20M₄ ist derselbe Operator bis auf die Skalierung H_cell = 2ΔH_mom. Seine Energien sind 0, 1/2 und 1. [S1, § 2]

**Modellentscheidung:** Dass gerade diese affine Funktion des Quellenmoments als physische Energie gelten soll, ist nicht allein aus der Projektoridentität bewiesen. Andere Energien können denselben Grundraum, aber andere virtuelle Anregungen und damit andere Kopplungskoeffizienten besitzen.

### 6.3 Warum drei Register nicht genügen, um genau diesen ganzen Grundraum auszuwählen

Für k = 1,2,3 gilt

$$
\operatorname{Tr}_{4-k}\frac P5
=
\operatorname{Tr}_{4-k}\frac S{35}
=
\frac{P_{\mathrm{sym},k}}{\binom{k+3}{3}}.
$$

Sei H eine beliebige Summe Hermitescher Terme, die jeweils höchstens drei dieser Register betreffen. Sind alle Codevektoren Grundzustände mit Energie E₀, dann

$$
\operatorname{tr}(HP/5)=\operatorname{tr}(HS/35)=E_0.
$$

Da H − E₀I positiv ist und S/35 auf dem ganzen symmetrischen Raum vollen Rang hat, folgt

$$
(H-E_0I)S=0.
$$

Der gesamte 35erraum läge im Grundraum. Also kann H nicht exakt nur den Fünfercode isolieren. Dieser Beweis braucht keine Frustrationsfreiheit und keine vorausgesetzte Symmetrie von H. [S0, § 8; S1, § 2]

**Geltungsbereich:** Derselbe Vierregisterraum, derselbe gesamte exakte Code als Grundraum und höchstens dreilokale Terme. Zusatzregister, approximative Energien, andere Codes oder die Auswahl eines einzelnen anderen Zustands sind nicht pauschal ausgeschlossen.

### 6.4 Entropie macht den Code nicht automatisch bevorzugt

Auch (S − P)/30 besitzt dieselben Marginalen bis zur dritten Ordnung. Ohne zusätzliche quartische Information bleiben Mischungen

$$
\rho_p=pP/5+(1-p)(S-P)/30
$$

lokal ununterscheidbar. Maximale Entropie wählt p = 1/7 und damit S/35, nicht P/5. Der Entropieunterschied ist log₂7. Der Schutzcode wird folglich nicht schon durch „möglichst viel Entropie“ ausgewählt. [S0, § 8]

---

<a id="auslesung"></a>
## 7. Was ein, zwei und drei Register verraten

### 7.1 Ein bekannt verlorenes Register ist korrigierbar

Schreibt man V nach einem Register als vier Matrizen V_a der Größe 64 × 5, gilt

$$
V_a^\dagger V_b=\frac{\delta_{ab}}4I_5.
$$

Ein einzelnes Register trägt daher stets I₄/4 und keine logische Information. Der Verlust eines **bekannten** Registers ist exakt korrigierbar. Das ist nicht dieselbe Aussage wie die Korrektur eines beliebigen unbekannten Fehlers an einer unbekannten Position. [S0, § 2]

Mit W_a = 2V_a sind die vier Bilder orthogonal. Für jeden logischen Operator O definiert

$$
O_3=\sum_{a=0}^3W_aOW_a^\dagger
$$

eine Darstellung auf den drei verbleibenden Registern:

$$
(I_4\otimes O_3)V=VO.
$$

### 7.2 Die vollständigen linearen Ausleseränge

Für

$$
\mathcal E_k(X)=\operatorname{Tr}_{4-k}(VXV^\dagger)
$$

gilt

$$
\boxed{\operatorname{rank}\mathcal E_1=1,\quad
\operatorname{rank}\mathcal E_2=10,\quad
\operatorname{rank}\mathcal E_3=25.}
$$

25 ist die Dimension des vollständigen logischen Operatorraums. Bei normierten Dichtematrizen ist die Spur bereits festgelegt.

### 7.3 Die Paarinformation ist eine konkrete Messung mit zehn Ausgängen

Verwendet werden die zehn reellen symmetrischen Zweiqubit Paulis

```text
II  IX  IZ  XI  XX  XZ  YY  ZI  ZX  ZZ
```

Ihre Bellvektoren b_ν = vec(A_ν)/2 bilden eine orthonormale Basis von Sym²(ℂ⁴). Es gilt die Zerlegung

$$
V|\psi\rangle=\sum_{\nu=1}^{10}(w_\nu^\mathsf T\psi)
|b_\nu\rangle_{12}|b_\nu\rangle_{34}.
$$

Die Zeilenmatrix W₁₀ mit Zeilen w_ν erfüllt

$$
W_{10}^\mathsf TW_{10}=I_5,\qquad
\|w_\nu\|^2=\frac12,\qquad
w_\nu^\mathsf Tw_\mu=\pm\frac16\quad(\nu\ne\mu).
$$

Mit F_ν = |w_ν⟩⟨w_ν| lautet die Paarreduktion

$$
\mathcal E_2(\rho)=\sum_\nu\operatorname{tr}(F_\nu\rho)
|b_\nu\rangle\langle b_\nu|.
$$

Sie ist ein Kanal vom Typ **Messen und Präparieren** und zerstört die Verschränkung zwischen dem ausgegebenen Registerpaar und einer äußeren Referenz. Rang zehn bedeutet deshalb nicht, dass zehn unabhängige Quantenfreiheitsgrade übertragen werden. [S0, § 3]

### 7.4 Explizite Auslesematrix

In der Basis mit Grammetrik G gilt W₁₀ = (F_num/4)G⁻¹ᐟ² mit

```text
F_num =
 4   4   4   4   0
 0   8   0   0   8
 4  -4   4  -4   0
 0   0   8   0   8
 0   0   0   8   8
 0   0   8   0  -8
 0   0   0   8  -8
 4   4  -4  -4   0
 0   8   0   0  -8
 4  -4  -4   4   0
```

Damit ist die Paarinformation unabhängig von metaphorischen Erklärungen vollständig definiert.

---

<a id="petersen"></a>
## 8. Petersen, Simplex und die unsichtbare Information

### 8.1 Zehn gleichwinklige Linien

Die normierten Vektoren √2w_ν bilden zehn gleichwinklige Linien in ℝ⁵ mit absolutem Kreuzprodukt 1/3. Setze

$$
\Gamma=W_{10}W_{10}^\mathsf T,\qquad C=6\Gamma-3I_{10}.
$$

C besitzt Diagonale null, sonst Einträge ±1 und erfüllt C² = 9I.

Für Vorzeichen s_ν ∈ {−1,+1} und D_s = diag(s) entsteht

$$
A_s=\frac{J_{10}-I_{10}-D_sCD_s}{2}.
$$

Genau sechs relative Vorzeichenklassen erfüllen Cs = 3s. Für sie gilt

$$
A_s\mathbf1=3\mathbf1,\qquad A_s^2=2I+J-A_s.
$$

Das sind sechs Vorzeichenrahmen des Petersen Graphen. Der Graph hat zehn Knoten, Grad drei und keine Dreiecke. Dieser Grad beschreibt erneut eine endliche interne Struktur, nicht drei Raumdimensionen. [S0, § 4]

### 8.2 Dieselben sechs Simplexmarkierungen

In den unnormalisierten Codekoordinaten lauten die sechs Spalten

```text
W6 =
 2   2  -1  -1  -1  -1
 0   0  -1  -1   1   1
 0   0  -1   1  -1   1
 0   0   1  -1  -1   1
 1  -1   0   0   0   0
```

Sie erfüllen

$$
W_6^\mathsf TGW_6=48I_6-8J_6.
$$

Mit u_q = G¹ᐟ²(W₆)_q lautet das konkrete Wörterbuch

$$
s_q=\frac12W_{10}u_q\in\{\pm1\}^{10}.
$$

Die sechs s_q sind genau die sechs regulären Vorzeichenrahmen. Hier sind nicht nur zwei Mengen gleich groß; eine explizite lineare Abbildung identifiziert sie.

### 8.3 Sechs unterschiedliche Zustände mit gleicher Paaranzeige

Normiere v_q = u_q/√40 und ρ_q = |v_q⟩⟨v_q|. Dann

$$
\mathcal E_2(\rho_q)=\frac{P_{\mathrm{sym},2}}{10},
\qquad\frac16\sum_q\rho_q=\frac{I_5}{5}.
$$

Die sechs Zustände sind nicht sechs orthogonale Speicherzustände eines Fünfers. Sie bilden einen nichtorthogonalen Simplex. Die fünf unabhängigen Differenzen B_q = ρ_q − I/5 besitzen Gramform

$$
\operatorname{tr}(B_qB_r)=\frac{24}{25}\delta_{qr}-\frac4{25}.
$$

Sie spannen den reellen symmetrischen Blindraum der Paarmessung auf. Auf dem gesamten Operatorraum kommen zehn imaginär antisymmetrische Blindrichtungen hinzu. [S0, §§ 4–5]

### 8.4 Eine energetische Konsequenz

Kein Hamiltonoperator aus höchstens Zweiregistertermen kann einen dieser sechs Zustände als einzigen globalen Grundzustand auswählen. Alle sechs haben dieselben Paarmarginalen und daher denselben Energieerwartungswert. Erreicht einer das globale Minimum, erreichen es alle; da sie den Fünferraum aufspannen, bleibt mindestens dieser ganze Raum im Grundraum.

Das ist eine Aussage über diese sechs speziellen Zustände und diesen Träger, kein Verbot beliebiger Zustandsauswahl durch beliebige Zweikörpermodelle.

---

<a id="transfer"></a>
## 9. Warum 2/3 und 4/9 verschiedene Aussagen sind

### 9.1 Normierte Singularübertragung

Die gewöhnlichen Hilbert Schmidt Singularwerte von ℰ₂ sind

$$
1/\sqrt2,\qquad(\sqrt2/3)^{\times9},\qquad0^{\times15}.
$$

Nach der angegebenen Referenznormalisierung werden daraus

$$
1,\qquad(2/3)^{\times9},\qquad0^{\times15}.
$$

Beschränkt man sich auf den 15 dimensionalen reellsymmetrischen Operatorraum, verbleiben fünf statt fünfzehn Nullrichtungen. Dort lautet die Liste

$$
1,\quad(2/3)^{\times9},\quad0^{\times5}.
$$

Das ist genau die Form der Singularliste der normierten Doily Inzidenzmatrix N/3. [S0, § 5; S4, § 5]

### 9.2 Der tatsächliche Rückkanal

Zur Referenz ρ* = I₅/5 gehört σ* = P_sym,2/10. Die zugehörige Petz Rückabbildung ist auf diesem Ausgangsträger

$$
\mathcal R_2=2\mathcal E_2^\dagger.
$$

Damit

$$
\boxed{\operatorname{spec}(\mathcal R_2\mathcal E_2)
=1^{\times1},\ (4/9)^{\times9},\ 0^{\times15}.}
$$

Eine Singularstärke 2/3 einer Abbildung wird bei dieser Hin und Rückkomposition quadriert. Sie ist nicht automatisch ein zeitlicher Eigenwert eines grundlegenden physikalischen Ticks.

### 9.3 Verbindung zum Reflexionskanal

Für den gemittelten logischen Quellenreflexionskanal

$$
\mathcal T_5(X)=\frac1{60}\sum_\ell u_\ell Xu_\ell^\dagger
$$

zerfällt der Operatorraum in Dimensionen 1 + 5 + 9 + 10. Die Eigenwerte sind 1, 3/5, 1/3 und 1/5. Die Sektoren entsprechen Identität, reeller Blindinformation, sichtbarer spurfreier Paarinformation und imaginär antisymmetrischen Richtungen.

Es gilt die konkrete Superoperatoridentität

$$
\mathcal R_2\mathcal E_2
=\frac{(5\mathcal T_5-3I)(5\mathcal T_5-I)(15\mathcal T_5-13I)}{16}.
$$

Das Polynom enthält negative Koeffizienten. Es ist deshalb nicht ohne Weiteres als positive Mischung physisch ausführbarer Kanäle zu lesen. [S0, § 5]

### 9.4 Was daraus gerade nicht folgt

Drei Rückkompositionen ergeben (4/9)³ = (2/3)⁶. Daraus folgt weder, dass genau drei Zyklen stattfinden, noch dass dies die physische TFPT Clock ist, noch dass eine andere Richtung (1/3)⁶ denselben Ursprung hat.

Die stärkere frühere Formulierung „universeller Informationsfaktor 2/3“ wird daher ersetzt durch:

> In verschiedenen ausdrücklich verbundenen Auslesedarstellungen tritt 2/3 als normierter Singularwert auf. Andere physisch oder logisch definierte Abbildungen haben andere Faktoren.


---

<a id="dynamik-ladung"></a>
## 10. Paarsteuerung, 3+2 und die Grenze zur Eichphysik

### 10.1 Zweite Antwort eines geschützten Codes

Für einen nichttrivialen Hermiteschen Zweiqubit Pauli A sei

$$
D_A=\sum_{r=1}^4A^{(r)},\qquad H_A=\sum_{r<s}A^{(r)}A^{(s)}.
$$

Dann D_A² = 4I + 2H_A und

$$
V^\dagger D_AV=0,\qquad V^\dagger D_A^2V=16R_A,
$$

wobei

$$
R_A^2=R_A,\quad\operatorname{rank}R_A=2.
$$

Die logische Einschränkung ist

$$
V^\dagger H_AV=8R_A-2I,
$$

mit Eigenwert −2 dreifach und +6 zweifach. Alle fünfzehn H_A erhalten den Code exakt. Für den gewählten Parent gilt zudem

$$
H_{\mathrm{cell}}D_AP=\Delta D_AP,\qquad D_A^3P=16D_AP.
$$

D_A hebt den aktiven Zweierbereich in einen orthogonalen Anregungsbereich mit Übergangsamplitude vier. Schutz bedeutet hier nicht „es passiert nichts“, sondern „die erste logische Antwort verschwindet, während virtuelle und höherordentliche Antworten existieren“. [S1, § 3]

### 10.2 Ein einzelnes Paar und eine symmetrisierte Paaroperation sind verschieden

Setze zur Unterscheidung

$$
h_A=V^\dagger A^{(1)}A^{(2)}V=\frac{4R_A-I}{3}.
$$

Das Spektrum ist +1 zweifach und −1/3 dreifach. Ein isolierter physischer Puls A¹A² erhält den Code im Allgemeinen nicht. Sein Austrittsoperator ist I − h_A²; für exp(−itA¹A²) beträgt die maximale Austrittswahrscheinlichkeit

$$
\frac89\sin^2t.
$$

Die symmetrisierte Operation

$$
\widehat h_A=\frac16\sum_{r<s}A^{(r)}A^{(s)}
$$

kommutiert dagegen sowohl mit S als auch mit Q_P und damit mit P. Ihre Einschränkung ist genau h_A. Dies ist echte codeerhaltende Steuerung, keine nachträgliche Projektion eines physisch undichten Pulses. [S0, § 6]

### 10.3 Vollständige logische Steuerbarkeit

Die spurfreien Generatoren für IX, IZ, XI und ZZ erzeugen durch Lie Kommutatoren die Rangfolge

$$
4,7,12,17,22,24.
$$

Damit entsteht 𝔰𝔲(5). Allgemeine logische Unitärtransformationen sind durch passende gesteuerte Pulsfolgen zugänglich. Daraus folgt weder ein automatisch ausgewählter autonomer Hamiltonoperator noch eine physische SU(5) Eichsymmetrie.

Die 35 projektiven Linien der Pauliadressen in 𝔽₂⁴ zerfallen in 15 kommutierende und 20 antikommutierende Dreierlinien. Die komprimierten Dreiregisteroperatoren der ersten Klasse spannen die 15 reellsymmetrischen Matrizen; diejenigen der zweiten Klasse die zehn imaginär antisymmetrischen Hermiteschen Richtungen. Zusammen ergeben sie den ganzen 25 dimensionalen Operatorraum.

Für AB = isC auf einer antikommutierenden Linie gilt sogar physisch

$$
[\widehat h_A,\widehat h_B]=\frac{4is}{3}\widehat T_{ABC},
\qquad
\widehat T_{ABC}=\frac1{24}\sum_{r,s,t\;\mathrm{verschieden}}A_rB_sC_t.
$$

So lässt sich die vollständige Auslese und Steuerstruktur aus denselben Operationen organisieren. [S0, § 6]

### 10.4 Die natürliche 3+2 Markierung

Der primitive ganzzahlige spurfreie Operator, der auf den beiden Antwortsektoren konstant ist, lautet bis auf Vorzeichen

$$
Q_A=5R_A-2I.
$$

Seine Eigenwerte sind −2 dreifach und +3 zweifach. Mit der Konvention, den positiven Wert auf 1/2 zu normieren,

$$
\boxed{Y_A=\frac{5R_A-2I}{6}},
$$

folgt

$$
\operatorname{spec}Y_A=(-1/3)^{\times3},(1/2)^{\times2},
\qquad\operatorname{tr}Y_A^2=\frac56.
$$

Der Zentralisator einer ausgewählten solchen Markierung in SU(5) ist S(U(3) × U(2)); seine Lie Algebra ist

$$
\mathfrak{su}(3)\oplus\mathfrak{su}(2)\oplus\mathfrak u(1).
$$

Die globale kompakte Gruppe ist in dieser Einbettung nicht ohne weitere Präzisierung das direkte Produkt, sondern besitzt die entsprechende endliche Z₆ Identifikation. Auch das ist zunächst Gruppentheorie, keine lokale Feldkonstruktion. [S1, § 3; mathematische Folgerung aus der Blockeinbettung]

### 10.5 Die fünfzehn Antwortbereiche haben eine feste gegenseitige Geometrie

$$
\sum_{A\ne I}R_A=6I.
$$

Für verschiedene kommutierende Paulis gilt

$$
[R_A,R_B]=0,\qquad\operatorname{tr}(R_AR_B)=1.
$$

Ihre aktiven Ebenen schneiden sich in einer Linie. Für antikommutierende Paulis gilt

$$
R_AR_BR_A=\frac14R_A,\qquad\operatorname{tr}(R_AR_B)=\frac12.
$$

Die beiden quadrierten Hauptwinkelkosinuswerte betragen dann jeweils 1/4. Von den 105 ungeordneten Paaren sind 45 kommutierend und 60 antikommutierend. [S1, § 3]

### 10.6 Zwei verschiedene Ladungsaussagen dürfen nicht verschmolzen werden

Die eben definierte Antwortmarkierung Y_A liegt bereits in der Paarspanne, denn sie ist affin in R_A. Eine ältere, aus einer besonderen Simplexmarkierung und einem Polartransport aufgebaute Ladung Y_mark ist ein anderes Objekt. Für jene Konstruktion wurde eine strikt positive minimale Distanz zur Paarspanne bestimmt:

$$
\min_\theta d_{HS}^2(Y_{\mathrm{mark},\theta},\mathcal O_2)
=\frac{29}{60}-\frac{\sqrt6}{10}>0.
$$

Sie kann mithilfe des Dreiregisterdecoders dargestellt werden. Daraus darf man nicht die universelle Aussage machen, jede mögliche Ladung brauche zwingend drei Register. Gleiches Spektrum ist noch kein Nachweis identischer Operatoren. [S0, § 7; S1, § 3]

### 10.7 Was zur Eichphysik fehlt

Für die ganze Familie gilt

$$
\{X:[X,R_A]=0\ \forall A\}=\mathbb CI.
$$

Außerdem hat die lineare Gleichung

$$
[K,X\otimes I+I\otimes X]=0
$$

auf den 24 spurfreien Generatorrichtungen Rang 24. Dasselbe gilt im untersuchten metrisch korrekten Ansatz für die konjugierte Wirkung X ⊗ I − I ⊗ Xᵀ. Die gleichgewichtete Paarmatrix ist also nicht automatisch kontinuierlich SU(5) invariant. [S2, § 8; erneut geprüft: A1]

Eine vollständige physische Identifikation verlangt mindestens die Auswahl der Markierung, ihren Transport zwischen Zellen, einen lokalen Eichfeldträger, chirale Materiedarstellungen und eine gemeinsame Dynamik. Der Zentralisator allein liefert diese Dinge nicht.

---

<a id="igusa"></a>
## 11. Igusa Quartik, Invariantenring und Reflexionsgeometrie

### 11.1 Fünf Quartikpolynome aus vier identischen Quellenkopien

Für eine normierte oder unnormierte Quellenpräparation x ∈ ℂ⁴ werden vier gleich präparierte Register vorausgesetzt. Die bedingte Codeamplitude lautet

$$
\alpha(x)=V^\dagger x^{\otimes4}.
$$

Dies ist kein Klonen eines unbekannten Zustands: Die vier Kopien sind Eingangsdaten der Konstruktion. Die Projektion ist konditioniert.

Setze

$$
\begin{aligned}
f_0&=x_0^4+x_1^4+x_2^4+x_3^4,\\
f_1&=x_0^2x_1^2+x_2^2x_3^2,\\
f_2&=x_0^2x_2^2+x_1^2x_3^2,\\
f_3&=x_0^2x_3^2+x_1^2x_2^2,\\
f_4&=x_0x_1x_2x_3.
\end{aligned}
$$

Dann

$$
\alpha=(f_0/2,\sqrt3f_1,\sqrt3f_2,\sqrt3f_3,\sqrt{24}f_4).
$$

Die fünf Polynome erfüllen die Relation

$$
\begin{aligned}
F(f)={}&f_0^2f_4^2-f_0f_1f_2f_3
+f_1^2f_2^2+f_1^2f_3^2+f_2^2f_3^2\\
&-4(f_1^2+f_2^2+f_3^2)f_4^2+16f_4^4=0.
\end{aligned}
$$

Die Koeffizientenabbildungen in den logischen Polynomgraden eins bis vier haben Ränge 5, 15, 35 und 69. Bei Grad vier gibt es 70 Monome und damit genau eine Relation. Bei kleineren Graden existiert keine. [S1, § 4]

### 11.2 Sechs Koordinaten, aber nur fünf Dimensionen

Für logische orthonormale Koordinaten z sei t = Wz mit

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

Es gilt W†W = I₅ und Σtᵢ = 0. Die Quellenrelation wird zu

$$
\boxed{\mathcal I(t)=4\sum_{i=1}^6t_i^4-\left(\sum_{i=1}^6t_i^2\right)^2=0.}
$$

Dies ist die Igusa Quartik. Die Quadrate sind holomorphe Amplitudenquadrate, keine Betragsquadrate. [S1, § 4; L3]

### 11.3 Fünfzehn singuläre Geraden

Jedes perfekte Matching der sechs Koordinaten in drei Paare liefert eine Ebene

$$
(t_1,\ldots,t_6)=(a,a,b,b,c,c),\qquad a+b+c=0,
$$

nach entsprechender Umordnung. Sie hat Vektordimension zwei und projektive Dimension eins. Auf jeder dieser fünfzehn Ebenen verschwinden sowohl 𝓘 als auch alle ersten Ableitungen.

Unter der expliziten Isometrie W sind dies genau die aktiven Ebenen der R_A. Zum Beispiel entspricht R_ZI = diag(1,1,0,0,0) dem Matching (12)(34)(56) in dieser Nummerierung. [S1, § 4]

Die 60 Stabilisatorpräparationen ψ_ℓ⊗⁴ projizieren auf fünfzehn logische Strahlen, jeweils vier Urbilder pro Strahl. Die Projektionswahrscheinlichkeit beträgt 1/4. Jeder logische Strahl liegt auf drei der singulären Geraden, und jede Gerade enthält drei der ausgezeichneten Strahlen: die 15₃ Inzidenz.

### 11.4 Die Quellenmannigfaltigkeit ist nicht der gesamte Code

In orthonormalen Codekoordinaten lautet eine äquivalente Quartik

$$
\begin{aligned}
F_{\log}(z)={}&z_4^4+(6z_0^2-2z_1^2-2z_2^2-2z_3^2)z_4^2\\
&+4(z_1^2z_2^2+z_1^2z_3^2+z_2^2z_3^2)
-8\sqrt3z_0z_1z_2z_3.
\end{aligned}
$$

Es gilt F_log(c₄) = 1. Dennoch erreichen echte codeerhaltende Paarpulse diesen Zustand:

$$
A_{01}=\frac{H_{IX}-H_{IY}}{4\sqrt3},\qquad
A_{14}=\frac{H_{XX}-H_{YY}+H_{XY}-H_{YX}}{8\sqrt2},
$$

$$
e^{-i\pi A_{14}/2}e^{-i\pi A_{01}/2}c_0=-c_4.
$$

Damit ist direkt bewiesen:

$$
\boxed{\text{Bild der identischen Quellenpräparation}
\subsetneq\text{dynamisch erreichbarer Codezustandsraum}.}
$$

Eine erzwungene Rückprojektion auf 𝓘 = 0 nach jedem Schritt entfernt erlaubte Dynamik. Die Umkehrung „𝓘 ≠ 0 bedeutet automatisch eine bestimmte universelle Verschränkungsklasse“ ist damit aber nicht bewiesen. Die Quartik ist hier ein Kriterium für eine spezielle Präparationsklasse, kein allgemeiner Entanglement Witness. [S1, § 4]

### 11.5 Ergänzender Quellenbefund: der vollständige Pauli Invariantenring

Die zugehörige vorhandene Herleitung [S4] betrachtet die volle Zweiqubit Pauli Gruppe einschließlich zentraler Phasen, Ordnung 64. Ihre Molien Funktion ist

$$
\frac{1-t^{16}}{(1-t^4)^5}.
$$

Zusammen mit dem klassischen Quotientensatz folgt: Der Invariantenring wird von fünf Quartikpolynomen erzeugt, mit einer einzigen Relation vom Quellengrad 16. In sechs redundanten Koordinaten ist er

$$
\mathbb C[x_1,\ldots,x_6]/(\sum_i x_i,\mathcal I(x)).
$$

**Genauigkeit der Formulierung:** Die fünf Generatoren sind minimal benötigt, aber nicht alle algebraisch unabhängig; die Quartikrelation verbindet sie. Die affine Quotientendimension ist vier. [S4, § 3; L4]

Die Quellenkoordinaten dieses ergänzenden Berichts verwenden die unnormalisierten Polynome (p,a,b,c,d) = (f₀,6f₁,6f₂,6f₃,24f₄) und die explizite Karte

$$
x=(2p+d,\ 2p-d,\ -p-a-b+c,\ -p-a+b-c,\ -p+a-b-c,\ -p+a+b+c).
$$

Diese Karte ist nicht kommentarlos mit der orthonormalen Karte W gleichzusetzen. Beide beschreiben die Quartik in ausdrücklich gegebenen Koordinaten; Normierung, Markierung und Operatortransport müssen jeweils mitgeführt werden.

### 11.6 Die Grade 8,12,20,24 haben einen gemeinsamen algebraischen Ursprung

Auf den sechs Quotientenkoordinaten wirken die 60 Quellenreflexionen als fünfzehn einfache Transpositionen, jeweils viermal. Der Kern ist die Pauli Gruppe; das Bild ist S₆. Für die untersuchte endliche Quellenreflexionsgruppe ergibt sich damit Ordnung 64 · 720 = 46080. [S4, § 3]

Sind e_k die elementarsymmetrischen Funktionen der sechs Koordinaten, gilt e₁ = 0 und

$$
e_4=e_2^2/4.
$$

Der vollständige Gruppeninvariantenring ist daher polynomial in e₂,e₃,e₅,e₆. Weil jede Quotientenkoordinate Quellengrad vier hat, entstehen

$$
\boxed{4(2,3,5,6)=(8,12,20,24).}
$$

Das organisierende Polynom lautet

$$
\prod_{i=1}^6(u-x_i)
=u^6+e_2u^4-e_3u^3+\frac{e_2^2}{4}u^2-e_5u+e_6.
$$

Die Grade sind damit nicht nur passende Zahlen. Sie stammen aus einem konkreten Invariantenring. Eine physische Zuordnung zu Massen oder Zeitskalen ist damit noch nicht gegeben.

### 11.7 Die 60 Spiegel und zehn Bellquadriken

Für jede der fünfzehn Koordinatendifferenzen gilt im ergänzenden Bericht eine vollständige Faktorisierung

$$
x_i(z_{\rm src})-x_j(z_{\rm src})
=c_{ij}\prod_{\alpha\in B_{ij}}\ell_\alpha(z_{\rm src}),\qquad |B_{ij}|=4.
$$

Die fünfzehn Viererpakete verwenden alle 60 Quellenhyperflächen genau einmal. Daher ist die Diskriminante des Sextikpolynoms proportional zu

$$
\prod_{\alpha=1}^{60}\ell_\alpha(z_{\rm src})^2.
$$

Für die zehn balancierten Vorzeichenklassen auf sechs Labels gilt zudem

$$
\sum_q S_{\nu q}x_q(z_{\rm src})=6(z_{\rm src}^\mathsf TA_\nu z_{\rm src})^2.
$$

So hängen die zehn Bellquadriken, zehn ausgezeichnete Hyperflächen der Igusa Quartik und die Knoten der dualen Segre Kubik zusammen. Das ist algebraische projektive Dualität, kein bereits bewiesener physikalischer Raumzeitdualismus. [S4, §§ 4–5]

### 11.8 Die 15 Matchingoperationen und 15 Quellenoperationen sind nicht dieselbe Liste

R_m = (I + T_m)/2 verwendet **drei gleichzeitige Transpositionen** T_m. Die native Reflexionswirkung auf den sechs Markierungen verwendet **einfache Transpositionen**. Beide Klassen haben fünfzehn Elemente, aber unterschiedliche Eigenwertmuster auf dem Fünferraum.

Die besondere äußere Automorphie von S₆ verbindet diese beiden Konjugationsklassen auf abstrakter Gruppenebene. Sie ersetzt keinen phasentreuen physikalischen Intertwiner. Das bloße Gleichsetzen beider Listen würde unterschiedliche dynamische Modelle vermischen. [S2, § 2; S4, § 3; L7]

---

<a id="ueberlappung"></a>
## 12. Warum perfekte Fünferzellen nicht überlappen dürfen

### 12.1 Der direkte Überlappungsversuch

Zwei identisch orientierte Codeprojektoren P_A und P_B sollen auf Vierermengen wirken, die s = 1,2 oder3 ganze Ququartregister gemeinsam haben. Für diese Einbettung gilt

$$
\operatorname{Ran}P_A\cap\operatorname{Ran}P_B=\{0\}.
$$

Die genaue Hauptwinkelrechnung ergibt:

| Gemeinsame Register | Nichtnull Hauptwinkelkosinus | Vielfachheit | Kleinste Energie von (I−P_A)+(I−P_B) |
|---:|---:|---:|---:|
| 1 | 1/4 | 100 | 3/4 |
| 2 | 1/2 | 10 | 1/2 |
| 3 | 1/4 | 20 | 3/4 |

[S0, § 9]

### 12.2 Warum der Konflikt strukturell entsteht

Ein gemeinsamer Zustand müsste unter den Permutationen jedes Viererblocks invariant sein. Bei überlappenden Blöcken erzeugen diese die Permutationen der ganzen vereinigten Registermenge. Der Zustand wäre damit global symmetrisch.

Die quartischen Pauli Stabilisatoren eines Blocks ließen sich auf jede Vierermenge transportieren. Produkte geeigneter Stabilisatoren würden beispielsweise XᵢXⱼ und ZⱼZₖ mit drei verschiedenen Registern erzwingen. Beide müssten denselben Zustand stabilisieren, antikommutieren aber. Ein nichtverschwindender gemeinsamer Zustand ist unmöglich.

### 12.3 Was nicht ausgeschlossen ist

Der Satz verbietet nicht die Kopplung getrennter Zellen. Er schließt auch nicht pauschal anders orientierte Codes, zusätzliche Randregister, andere Faktorisierungen oder dynamische Schnittstellen aus.

Die Konsequenz ist nicht „es gibt keine Mehrzellenphysik“, sondern:

> Die ursprüngliche perfekte Vierregisterzelle lässt sich nicht durch bloßes gemeinsames Benutzen ganzer Register zu einem frustrationsfreien Netz verkleben.

---

<a id="bindung"></a>
## 13. Virtuelle Wechselwirkung und exakte Zweizellenbindung

### 13.1 Getrennte Zellen können trotz erster logischer Blindheit koppeln

Ein einzelner physischer Eingriff pro Zelle komprimiert in erster Ordnung zu keinem nichttrivialen Produkt logischer Observablen. Das schließt virtuelle Prozesse nicht aus.

Für zwei getrennte Zellen und

$$
V_{AB}=gD_A^LD_B^R
$$

entsteht in jedem aktiven logischen Kanal der exakte Block

$$
\begin{pmatrix}0&16g\\16g&2\Delta\end{pmatrix}.
$$

Seine untere Energie ist

$$
E_-=\Delta-\sqrt{\Delta^2+256g^2}
=-\frac{128g^2}{\Delta}+\frac{8192g^4}{\Delta^3}+O(g^6).
$$

Vier gemeinsame logische Richtungen sind aktiv; die übrigen 21 sind in diesem Einzelkanal ungekoppelt. [S1, § 5]

### 13.2 Exakte Rückkehrpulse

Nach

$$
T_0=\frac{\pi}{\sqrt{\Delta^2+256g^2}}
$$

verschwindet die Restbesetzung außerhalb des Codes. Im aktiven Bereich bleibt die Phase

$$
\phi=\pi\left(1-\frac{\Delta}{\sqrt{\Delta^2+256g^2}}\right).
$$

Für m ≥ 2 vollständige Rückkehrzyklen liefert

$$
\frac g\Delta=\frac{\sqrt{2m-1}}{16(m-1)}
$$

ein kontrolliertes Minuszeichen. Die **gesamte** Pulsdauer ist dann

$$
T_{\mathrm{gesamt}}=mT_0=\frac{(m-1)\pi}{\Delta}.
$$

Die größte zwischenzeitliche Austrittswahrscheinlichkeit beträgt (2m − 1)/m²; am Endpunkt ist sie null. Das ist eine gesteuerte Implementierung, keine Behauptung passiver Fehlertoleranz während des Pulses.

### 13.3 Gleichmäßiger Austausch

Ohne Bevorzugung eines einzelnen Paulilabels sei

$$
\mathcal W=\sum_{A\ne I}D_A^LD_A^R,
\qquad H=H_{\mathrm{cell}}^L+H_{\mathrm{cell}}^R+g\mathcal W.
$$

Die Pauli Vollständigkeit ergibt

$$
\boxed{\mathcal W=4\sum_{r,s=1}^4\mathrm{SWAP}_{Lr,Rs}-16I.}
$$

Auf dem vollständigen Hilbertraum gilt ‖𝒲‖ ≤ 80. Mit P_LR = P ⊗ P verschwinden die erste logische Antwort und die gemischten unterschiedlichen Syndrome:

$$
P_{LR}\mathcal WP_{LR}=0,\qquad PD_AD_BP=0\quad(A\ne B).
$$

Damit

$$
P_{LR}\mathcal W^2P_{LR}=256\sum_A R_A\otimes R_A.
$$

Die effektive zweite Ordnung ist

$$
\boxed{H_{\mathrm{eff}}^{(2)}=-\frac{128g^2}{\Delta}K,
\qquad K=\sum_A R_A\otimes R_A.}
$$

Das exakte Spektrum der 25 × 25 Matrix K lautet

$$
6^{\times1},\quad(7/2)^{\times9},\quad(3/2)^{\times15}.
$$

Die eindeutige stärkste Richtung ist

$$
\boxed{|\Omega_5\rangle=\frac1{\sqrt5}\sum_{i=0}^4|c_i\rangle_L|c_i\rangle_R.}
$$

[S1, § 6]

### 13.4 Der vollständige mikroskopische Grundzustand ist leicht angeregt

Definiere

$$
|E\rangle=\frac{\mathcal W|\Omega_5\rangle}{16\sqrt6}.
$$

Dann ist E normiert, orthogonal zu Ω₅, besitzt unter der ungekoppelten Energie den Wert 2Δ und erfüllt

$$
\mathcal W|E\rangle=16\sqrt6|\Omega_5\rangle+16|E\rangle.
$$

Daher ist der Zweierblock

$$
H_{\mathrm{bond}}=\begin{pmatrix}
0&16\sqrt6g\\16\sqrt6g&2\Delta+16g
\end{pmatrix}
$$

exakt invariant. Die untere Energie ist

$$
\boxed{E_0=\Delta+8g-\sqrt{(\Delta+8g)^2+1536g^2}.}
$$

Mit d = Δ + 8g und r = √(d² + 1536g²) lautet der angeregte Normanteil

$$
\epsilon=\frac12(1-d/r).
$$

Für g > 0 kann der Grundzustand als √(1 − ε)Ω₅ − √εE geschrieben werden. **Bei endlichem g ist also nicht der nackte Zustand Ω₅ der exakte mikroskopische Grundzustand.** Exakt Ω₅ erhält man nach konditionierter Projektion beider Zellen auf ihre Codes, mit Wahrscheinlichkeit 1 − ε.

### 13.5 Globaler Grundzustandssatz

Für

$$
0<|g|\le\Delta/200
$$

ist dieser Eigenzustand der eindeutige globale Grundzustand auf dem vollständigen Raum von acht Ququartregistern, Dimension 65536. Es gilt die konservative Schranke

$$
\boxed{\operatorname{gap}(H)\ge\frac{1200}{7}\frac{g^2}{\Delta}.}
$$

Der Beweis verwendet die Symmetrie und Syndromzerlegung, nicht eine behauptete vollständige numerische Diagonalisierung der 65536 × 65536 Matrix. Außerhalb des relevanten symmetrischen Sektors liegen die Energien mindestens bei 2Δ − 80|g|. Nichttriviale gemeinsame Syndrome liegen mindestens bei Δ − 80|g|. Im neutralen Sektor bleiben 25 tiefe und 60 angeregte Richtungen.

Nach Entfernen des exakten Zweierblocks ist die quadrierte verbleibende Kopplungsnorm höchstens 896. Bei Anregungsenergie mindestens 8Δ/5 folgt E_⊥ ≥ −560g²/Δ. Die exakte Grundenergie erfüllt im gewählten Intervall E₀ ≤ −(5120/7)g²/Δ. Ihre Differenz ist die angegebene Lückenschranke. [S1, § 6]

### 13.6 Zahlen aus der ursprünglichen numerischen Gegenprobe

| g/Δ | E₀/Δ | Numerische Lücke/Δ | Bewiesene untere Lücke/Δ | ε |
|---:|---:|---:|---:|---:|
| 0,001 | −0,0007616170334794 | 0,0003184740481503 | 0,0001714285714286 | 0,0003775009975693 |
| 0,002 | −0,0030191362285596 | 0,0012659081330330 | 0,0006857142857143 | 0,0014813932934241 |
| 0,005 | −0,0183005244258363 | 0,0077000796120838 | 0,0042857142857143 | 0,0086461850880047 |

Diese Tabelle stammt aus [S1]. Sie wurde in dieser Konsolidierung nicht durch erneute Diagonalisierung dieses mikroskopischen Modells erzeugt.

Der angeregte Zustand E besitzt 30 gleiche Schmidtkoeffizienten. Die Bindungsentropie des exakten Grundzustands ist

$$
S_L=\log_2 5+h_2(\epsilon)+\epsilon\log_2 6.
$$

Eine energetische Auswahl ist noch keine autonome Präparation aus jedem Anfangszustand. Dafür wären eine Anfangsbedingung, Kühlung, Messung oder eine entsprechend begründete dissipative Dynamik nötig.

### 13.7 Das frühere Zweilinksbeispiel

Ein anderer ausdrücklich untersuchter Aufbau verwendet H₀ = Δ_m(H_mom^A + H_mom^B) und zwei physische Links g(a₁^Aa₁^B + a₂^Aa₂^B), mit a = I₂ ⊗ σ_z. In seiner eigenen Energienormierung gilt

$$
H_{\mathrm{eff}}^{(2)}=\frac{g^2}{\Delta_m}
\left[-\frac{29}{24}I-\frac{11}{24}(h_A\otimes I+I\otimes h_B)
-\frac{15}{8}h_A\otimes h_B\right].
$$

Der letzte Term ist eine echte Wechselwirkung. Δ_m darf nicht ohne Faktorvergleich mit dem Δ des späteren H_cell Modells gleichgesetzt werden. Aufbau, Linkzahl und virtuelle Nenner sind verschieden. [S0, § 10]

---

<a id="hamming-bindung"></a>
## 14. Die Rückbindung an den Hamming Code

### 14.1 Dasselbe vollständige Gewichtspolynom

Für die unnormalisierten Quellenamplituden α(x) gilt

$$
\begin{aligned}
\Phi_8(x)&=4\sum_{i=0}^4\alpha_i(x)^2\\
&=\sum_i x_i^8+14\sum_{i<j}x_i^4x_j^4
+168x_0^2x_1^2x_2^2x_3^2\\
&=4\sqrt5\langle\Omega_5|x^{\otimes8}\rangle.
\end{aligned}
$$

Die Quadrate sind erneut Amplitudenquadrate ohne komplexe Konjugation. Das vollständige Gewichtspolynom zweiter Ordnung des binären Codes C ist

$$
\operatorname{cwe}^{(2)}_C(x)=\sum_{c,d\in C}\prod_{j=1}^8x_{2c_j+d_j}.
$$

Die Enumeration der 256 geordneten Hamming Wortpaare liefert

$$
\boxed{\operatorname{cwe}^{(2)}_{[8,4,4]}(x)=\Phi_8(x).}
$$

Dies ist Koeffizientengleichheit sämtlicher Monome, nicht nur gleiche Polynomordnung. [S1, § 7; allgemeiner Kontext: L2]

### 14.2 Stärker: die Zustandsprojektion selbst

Ordne die acht Punkte von 𝔽₂³ lexikografisch; die erste Koordinate trennt die linke von der rechten Vierregisterzelle. Der normierte Ququartzustand ist

$$
|C^{(2)}\rangle=\frac1{16}\sum_{c,d\in C}
|2c_1+d_1,\ldots,2c_8+d_8\rangle.
$$

Dann

$$
\boxed{(P\otimes P)|C^{(2)}\rangle=\frac{\sqrt5}{4}|\Omega_5\rangle.}
$$

Die Projektionswahrscheinlichkeit beträgt 5/16. In der unnormalisierten Codebasis lautet die Zählidentität

$$
B^\mathsf TTB=4\operatorname{diag}(4,12,12,12,24).
$$

Die Diagonalzählungen sind 16, 48, 48, 48 und 96; alle außerdiagonalen Einträge verschwinden. Nach Normierung wird daraus I₅/4. [S1, § 7]

### 14.3 Was die geschlossene Schleife beweist

```text
60 Quellen → M₄ → P → gewählte Schutzenergie und Austausch → Ω₅
                                                              ▲
                                                              │
                          projizierter doppelter Hamming Code ─┘
```

Die beiden Wege treffen sich in einem exakt identifizierten Zustand. Das ist eine substanzielle algebraische Verbindung. Die unprojizierte Hamming Wortsuperposition ist trotzdem nicht der unprojizierte gedresste mikroskopische Grundzustand. Ebenso folgt aus der konsistenten Schleife noch keine eindeutige Auswahl ihrer physikalischen Realisierung.

---

<a id="dreierrekursion"></a>
## 15. Drei Fünfer werden wieder zu einem Fünfer

### 15.1 Matchingdarstellung der Antwortprojektoren

Arbeite im Nullsummenraum U ⊂ ℂ⁶. Zu jedem der fünfzehn perfekten Matchings m gehört die Involution T_m, die seine drei Paare vertauscht. Auf U gilt

$$
R_m=\frac{I+T_m}{2},\qquad\sum_mR_m=6I.
$$

Daraus folgt

$$
\boxed{K=\frac94I+\frac14\sum_mT_m\otimes T_m.}
$$

Die Gram Matrix tr(R_mR_n) hat Spektrum 12 einfach, 2 neunfach, 0 fünffach. Die fünfzehn Projektoren spannen also einen **zehndimensionalen**, nicht fünfzehndimensionalen Operatorraum. [S2, § 2; erneut geprüft: A1]

### 15.2 Der exakt gelöste Dreierblock

Für drei Zellen mit allen drei Kanten sei

$$
\mathcal K_\triangle=K_{12}+K_{23}+K_{13},\qquad
H_\triangle=-J\mathcal K_\triangle,\quad J>0.
$$

Sein vollständiges Spektrum lautet:

| Eigenwert von 𝒦_△ | Multiplizität |
|---:|---:|
| 9/2 | 11 |
| 5 | 18 |
| 6 | 25 |
| 15/2 | 42 |
| 9 | 10 |
| 19/2 | 9 |
| 21/2 | 5 |
| 27/2 | 5 |

Die Multiplizitäten summieren sich zu 125 = 5³. Daher

$$
\boxed{E_0=-27J/2,\quad\dim\mathcal G_\triangle=5,\quad\operatorname{gap}=3J.}
$$

Die Spektralaussage ist exakt zertifiziert. In rationalen Koordinaten ist 4𝒦_△ ganzzahlig; ein annihilierendes Polynom und die Spuren seiner Lagrange Spektralprojektoren bestimmen Eigenwerte und Multiplizitäten. [S2, § 3]

### 15.3 Der explizite Kodierungstensor

Sei Q_U = I₆ − 11ᵀ/6 und qᵢ = Q_Ueᵢ. In einer reellen orthonormalen Basis von U gilt

$$
q_i^\mathsf Tq_j=\delta_{ij}-\frac16,\qquad
\sum_i|q_i\rangle\langle q_i|=I_5.
$$

Definiere Abbildungen von U nach U⊗³:

$$
\mathcal A(v)=\sum_a\bigl(|aa\rangle\otimes v+|a\rangle\otimes v\otimes|a\rangle+v\otimes|aa\rangle\bigr),
$$

$$
\mathcal C(v)=\sum_{i=1}^6q_i^{\otimes3}\langle q_i,v\rangle.
$$

Dann

$$
\mathcal K_\triangle\mathcal A=15\mathcal A-18\mathcal C,
\qquad\mathcal K_\triangle\mathcal C=\frac34\mathcal A+\frac92\mathcal C,
$$

$$
\mathcal A^\dagger\mathcal A=21I,\qquad
\mathcal A^\dagger\mathcal C=\frac52I,\qquad
\mathcal C^\dagger\mathcal C=\frac7{12}I.
$$

Setze D = 𝒜 − 2𝒞. Dann

$$
\mathcal K_\triangle D=\frac{27}{2}D,
\qquad D^\dagger D=\frac{40}{3}I.
$$

Also ist

$$
\boxed{V_\triangle=\sqrt{\frac3{40}}(\mathcal A-2\mathcal C)}
$$

eine Isometrie auf den gesamten Grundraum. Hier wird eine echte Kodierung angegeben, nicht bloß die Zahl fünf wiedergefunden.

### 15.4 Der exakte Operatortransport

Für alle fünfzehn Antwortprojektoren und jede Position r im Dreierblock gilt

$$
\boxed{V_\triangle^\dagger R_A^{(r)}V_\triangle
=\frac7{12}R_A+\frac16I.}
$$

Der rohe komprimierte Operator ist kein Projektor mehr: Er besitzt Eigenwert 1/6 dreifach und 3/4 zweifach. Seine beiden ausgezeichneten Teilräume bleiben jedoch dieselben.

Für Y_A verschwindet der konstante Anteil:

$$
\boxed{V_\triangle^\dagger Y_A^{(r)}V_\triangle=\frac7{12}Y_A.}
$$

Die 3+2 Markierung überlebt also genau als Markierung mit abgeschwächter Antwortstärke. [S2, § 4]

### 15.5 Der Formschluss der Paarwechselwirkung

Eine Kante zwischen zwei solchen Blöcken wird unter Kompression zu

$$
K\mapsto\frac{49}{144}K+\frac{19}{12}I.
$$

Mit

$$
K_c=K-\frac{12}{5}I
=\sum_A(R_A-2I/5)\otimes(R_A-2I/5)
$$

folgt

$$
\boxed{K_c\mapsto\frac{49}{144}K_c.}
$$

Die Relation λ_K = λ_Y² ist hier eine Folge der beiden Enden einer bilinearen Kopplung, keine unabhängige zusätzliche Zahl.

**Physische Reichweite:** Bei starkem J_in innerhalb der Dreiecke und schwachen äußeren Verbindungen J_out ist dies der führende komprimierte Term. Höhere virtuelle Blockanregungen können zusätzliche Operatoren erzeugen. Ein exakter vollständiger Renormierungsfluss des gesamten mikroskopischen Hamiltonoperators ist damit nicht bewiesen.

### 15.6 Iteration und ihre Voraussetzungen

Als abstrakte Isometrie lässt sich V_△ auf einem vorgegebenen ternären Baum iterieren. Für ein einzelnes Blatt nach n Ebenen gilt

$$
Y_A\mapsto(7/12)^nY_A.
$$

Für eine einzelne Kante zwischen zwei solchen Blöcken gilt entsprechend

$$
K_c\mapsto(49/144)^nK_c.
$$

Bei mehreren Kanten müssen ihre Beiträge und ihre konkrete Anordnung addiert werden. Genau drei gleichartige äußere Kanten ergeben in dieser Kompression beispielsweise 3 · 49/144 = 49/48. Weder drei Kanten noch der ternäre Baum werden dadurch energetisch automatisch ausgewählt.

### 15.7 Der neue Block ist nicht derselbe ursprüngliche Fehlerkorrekturcode

Der lokale Heisenberg Kanal eines einzelnen Registers der Dreierkodierung hat Spektrum

$$
1^{\times1},\quad(7/12)^{\times9},\quad(19/60)^{\times5},\quad(17/60)^{\times10}.
$$

Er hat vollen linearen Rang. Ein einzelnes Register ist daher nicht logisch blind. Rekursiv erhalten bleiben die Fünferdarstellung und die Antwortform; nicht alle ursprünglichen Schutzeigenschaften. [S2, § 4]

### 15.8 Die sogenannten Skalierungsexponenten

Es gilt rechnerisch

$$
\alpha_Y=-\frac{\ln(7/12)}{\ln3}=0.49061575798149\ldots,
$$

$$
\alpha_K=-\frac{\ln(49/144)}{\ln3}=0.98123151596299\ldots=2\alpha_Y.
$$

Da N = 3ⁿ, beschreiben diese Zahlen die Abschwächung relativ zur Anzahl der Blätter, beispielsweise λ_Yⁿ = N^−α_Y. Sie sind **ohne abgeleiteten linearen Längenfaktor noch keine räumlichen Skalierungsdimensionen**.

Wenn ein physischer Blockschritt einen Längenfaktor b hätte, wäre die entsprechende räumliche Skalierungsdimension −lnλ/lnb. b = 3 folgt nicht daraus, dass drei Zellen zusammengefasst werden. Die frühere Bezeichnung als bereits echte physische RG Exponenten war deshalb zu stark.

---

<a id="vierer-code16"></a>
## 16. Viererbindung, C₁₆ und derselbe Quartiktensor

### 16.1 Ein Tensor mit drei Rollen

In orthonormalen Fünferkoordinaten setze

$$
\mathsf A_{abcd}=\delta_{ab}\delta_{cd}+\delta_{ac}\delta_{bd}+\delta_{ad}\delta_{bc},
$$

$$
\mathsf C_{abcd}=\sum_{i=1}^6(q_i)_a(q_i)_b(q_i)_c(q_i)_d,
$$

$$
\boxed{\mathsf T=\mathsf A-2\mathsf C.}
$$

Als Abbildung von einem auf drei Register ist dies der vorherige D Tensor. Als Viererzustand hat er Normquadrat 200/3. Der normierte Zustand

$$
|\Psi_4\rangle=\sqrt{\frac3{200}}|\mathsf T\rangle
=(I\otimes V_\triangle)|\Omega_5\rangle
$$

ist der eindeutige Grundzustand von vier Zellen mit allen sechs Kanten:

$$
\left(\sum_{i<j}K_{ij}\right)|\Psi_4\rangle=27|\Psi_4\rangle.
$$

Jede Dreiecksrestriktion ist höchstens 27/2; in der Summe der vier Dreiecke wird jede Kante zweimal gezählt. Somit ist ΣK ≤ 27I. Der Tensor erreicht die Schranke. Die eindimensionale Schnittmenge zweier überlappender Dreiecksgrundräume sichert die Eindeutigkeit. [S2, § 5]

### 16.2 Die Quartik steckt direkt im Bindungstensor

Für t ∈ U und s₂ = Σtᵢ², s₄ = Σtᵢ⁴ gilt

$$
\mathsf T(t)=3s_2^2-2s_4
=\frac52s_2^2-\frac12\mathcal I(t).
$$

Damit stehen Quellquartik und Mehrzellenbindung in einer direkten Polynomidentität. Ein kombinatorischer Vierknotengraph mit sechs Kanten kann als Tetraedergraph bezeichnet werden. Das ist keine Herleitung einer räumlichen Einbettung in drei Dimensionen.

### 16.3 Der zusätzliche binäre Code C₁₆

Definiere

$$
C_{16}=\{(x_1,x_1,\ldots,x_8,x_8):x\in\mathbb F_2^8,\ \sum_ix_i=0\}
\cup\bigl[\text{dieselbe Menge}+(1,0,1,0,\ldots,1,0)\bigr].
$$

Die erste Menge ist ein siebendimensionaler Unterraum, die Vereinigung ein acht dimensionaler linearer Code. Er hat 256 Wörter und Gewichtsverteilung

$$
0^{\times1},4^{\times28},8^{\times198},12^{\times28},16^{\times1}.
$$

Alle inneren Produkte verschwinden modulo zwei, und alle Gewichte sind durch vier teilbar. Damit handelt es sich um einen doppelt geraden selbstdualen [16,8,4] Code. „Zusätzlich“ bedeutet hier zusätzlich in dieser TFPT Konstruktion, nicht beanspruchte weltweite Erstentdeckung eines klassischen Codes. [S2, § 6; L2]

### 16.4 Projektion in vier ursprüngliche Fünferzellen

Der normierte Doppelcodezustand ist

$$
|C_{16}^{(2)}\rangle=\frac1{256}\sum_{c,d\in C_{16}}
|2c_1+d_1,\ldots,2c_{16}+d_{16}\rangle.
$$

Je vier aufeinanderfolgende Ququartregister bilden eine ursprüngliche Zelle. Nach Codeprojektion und deklarierter Identifikation der logischen Koordinaten gilt

$$
\boxed{|d_4\rangle=P^{\otimes4}|C_{16}^{(2)}\rangle
=\frac{\mathsf A-3\mathsf C}{36}.}
$$

Die Projektionswahrscheinlichkeit ist 25/576. Die Enumeration verwendet sämtliche 65536 geordneten Codewortpaare.

Für H₈ ⊕ H₈ erhält jede der drei Paarungen der vier Zellen zwei Hamming Bindungen. Der unnormierte **kohärente Mittelwert** ihrer projizierten Zustände ist

$$
|e_4\rangle=\frac{\mathsf A}{48}.
$$

Ein kohärenter Mittelwert von Amplituden ist nicht dasselbe wie ein statistisches Gemisch von Dichtematrizen.

### 16.5 Gleiches Gewichtspolynom, verschiedene Blockkorrelation

Es gilt exakt

$$
\operatorname{cwe}^{(2)}_{C_{16}}
=\operatorname{cwe}^{(2)}_{H_8\oplus H_8}.
$$

Alle 45 vorkommenden Monome und ihre Koeffizienten stimmen überein. Die blockweise projizierten Zustände sind dennoch verschieden. Ihre Differenz auf diagonal gleichen logischen Amplituden ist

$$
\boxed{d_4(t)-e_4(t)=-\frac1{48}\mathcal I(t).}
$$

Auf der ursprünglichen Quellenmannigfaltigkeit verschwindet die Differenz. Die eingeschränkten identischen Quellenproben können diese Korrelation deshalb nicht unterscheiden. [S2, § 6]

**Bildlich:** Zwei Programme liefern bei einem eingeschränkten Testsatz dieselbe Ausgabe, besitzen aber unterschiedliche interne Zustände. Ein vollständigeres Experiment kann sie auseinanderhalten. Hier ist die exakte fehlende Testinformation das Quartikpolynom.

### 16.6 Der energetische Tensor ist eine bestimmte Codekombination

$$
\boxed{\mathsf T=8(2e_4+3d_4).}
$$

Nach Normierung entsteht genau Ψ₄. Derselbe Tensor ist also

```text
Dreierkodierung  V△
         ╲
          ╲
      gemeinsamer Tensor 𝒯  ─────► eindeutige Viererbindung Ψ₄
          ╱
         ╱
kohärente Kombination der beiden Codeprojektionen
```

Der allein normierte d₄ Zustand hat Überlappungsquadrat 24/25 mit Ψ₄, aber nicht eins. Die exakte Übereinstimmung benötigt die angegebene Kombination. Die Koeffizienten zwei und drei sind Normierungsdaten dieser Amplitudentensoren, keine zusätzliche Ableitung von Farbladung und schwachem Isospin.

---

<a id="hoehere-ordnung"></a>
## 17. Höhere Ordnung, kleine Graphen und Grenzen der Rekursion

### 17.1 Ein verträglicher Schleifenterm in dritter Ordnung

Im mikroskopischen Austauschmodell liefert der Beitrag, der drei verschiedene Dreieckskanten je einmal benutzt,

$$
H^{(3)}_{\mathrm{Dreieck}}
=\frac{6144g_{12}g_{23}g_{31}}{\Delta^2}
\sum_A R_A\otimes R_A\otimes R_A.
$$

Der Faktor ist 6 · 16³/(2Δ)²: sechs Reihenfolgen, die lokale Antwortamplitude 16 an drei Zellen und zwei virtuelle Zwischenenergien 2Δ. [S2, § 7]

Für die Dreierkodierung gilt

$$
\left(\sum_AR_A^{\otimes3}\right)V_\triangle=\frac{15}{4}V_\triangle.
$$

Dieser konkrete Term wirkt im Grundraum nur als Energieverschiebung. Wiederholte Einzelkanten liefern weitere Terme derselben Ordnung. Die Verträglichkeit dieses einen Schleifenbeitrags beweist deshalb nicht den Abschluss sämtlicher höherer Ordnungen.

### 17.2 Vergleich kleiner effektiver Graphen

Die folgenden Zusatzrechnungen diagonalisierten ΣK auf festen kleinen Graphen. Bei H = −JΣK ist der größte Eigenwert von ΣK die negative Grundenergie in Einheiten J. Die nicht rational ausgewiesenen Zahlen sind numerische Befunde, keine zusätzliche behauptete exakte Spektrallösung. [S2, Prüfpaket; erneut berechnet: A1]

| Graph | Zellen | Kanten | Größter Eigenwert von ΣK | Grundraumdimension, numerisch |
|---|---:|---:|---:|---:|
| Einzelbindung | 2 | 1 | 6 | 1 |
| Pfad | 3 | 2 | 9,386000936329 | 5 |
| Dreieck | 3 | 3 | 13,5 | 5 |
| Pfad | 4 | 3 | 14,783658759954 | 1 |
| Stern | 4 | 3 | 13,5 | 1 |
| Viererzyklus | 4 | 4 | 18,772001872659 | 1 |
| Vollständiger Vierergraph | 4 | 6 | 27 | 1 |

Ein Vergleich von Energien pro Kante ist keine automatische Auswahl eines globalen Graphen. Ändert sich die Zahl der Kanten, braucht es eine physische Regel für deren Kosten beziehungsweise Zulässigkeit.

### 17.3 Monogamie verhindert perfekte unabhängige Bindungen an jeder Kante

Für P_ij = |Ω₅⟩⟨Ω₅| auf einem Paar gilt auf drei Zellen

$$
P_{12}P_{23}P_{12}=P_{12}/25,\qquad
\|P_{12}+P_{23}\|=6/5.
$$

Daher

$$
\langle P_{12}\rangle+\langle P_{23}\rangle\le6/5.
$$

Beide Bindungswahrscheinlichkeiten können nicht gleichzeitig eins sein. Ein aus vielen unabhängig perfekten Ω₅ Bindungen an derselben ganzen Zelle gebautes Netz ist ausgeschlossen. Der Vierertensor verwendet echte Mehrparteienkorrelationen, nicht eine Verletzung dieses Satzes. [S2, § 8; L8]

### 17.4 Trotzdem gewinnt bei reiner Attraktion der vollständige Graph

Da K ≥ 3I/2, gilt für eine zusätzliche, kostenlos zugelassene Kante mit J_ij > 0

$$
\boxed{E_0(G+ij)\le E_0(G)-3J_{ij}/2.}
$$

Jede neue Kante senkt die Grundenergie. Sind alle Kanten frei wählbar und ist −ΣJ_ijK_ij die ganze Graphenenergie, wird der vollständige Graph bevorzugt. Monogamie allein erzeugt keine räumliche Sparsität.

Die Zentrierung K_c = K − 12I/5 ist bei einem festen Graphen eine konstante Energieverschiebung. Bei dynamischer Kantenzahl ist sie eine **zusätzliche Energie von 12J/5 pro Kante**. Sie darf dort nicht als folgenlose Wahl des Energienullpunkts ausgegeben werden. [S2, § 8]

### 17.5 Die naive Reed–Muller Vergrößerung ist eine andere Sackgasse

Die direkte Fortsetzung RM(1,3) → RM(1,m), in L = 2^(m−2) Viererblöcke zerlegt, ergibt nach doppelter binärer Kodierung und Projektion

$$
|\chi_m\rangle=2^{m-5}\sum_{i=0}^4w_i^{1-L/2}|i\rangle^{\otimes L},
\qquad w=(4,12,12,12,24).
$$

Für zwei Blöcke entstehen gleiche Amplituden und damit Ω₅. Für vier Blöcke ist der konditionierte Zustand

$$
\frac{6|0000\rangle+2|1111\rangle+2|2222\rangle+2|3333\rangle+|4444\rangle}{7}.
$$

Das ist ein gewichteter globaler GHZ Zustand, kein daraus abgeleitetes lokales Raumnetz. Für m > 3 ist RM(1,m) in dieser Familie außerdem nicht mehr selbstdual. Seine Dimension m + 1 ist nicht die halbe Länge 2^(m−1). Die C₁₆ Konstruktion ist deshalb eine strukturell andere Fortsetzung. [S2, § 9]

---

<a id="6561"></a>
## 18. Der Test bis 6561 Knoten

### 18.1 Welche Familie wirklich getestet wurde

Als eine ausdrücklich gewählte symmetrische Weitergabe der Dreierblöcke wurde die kartesische Produktfamilie

$$
H(n,3)=\underbrace{K_3\square\cdots\square K_3}_{n\ \mathrm{Faktoren}}
$$

betrachtet. Ihre Knoten sind Wörter der Länge n über drei Zeichen. Zwei Wörter sind benachbart, wenn sie sich in genau einer Koordinate unterscheiden.

Daraus folgen

$$
N_n=3^n,\qquad\deg=2n,\qquad|E|=n3^n.
$$

Diese Produktregel ist eine Modellwahl. Sie folgt nicht eindeutig aus V_△ oder allein aus einer S₃ Symmetrie. Der Test falsifiziert diese Fortsetzung als behauptete automatisch dreidimensionale Geometrie, nicht jede denkbare ternäre Fortsetzung. [S3; A1]

### 18.2 Vollständiges Laplacespektrum

Für den kombinatorischen Laplaceoperator mit Einheitsgewichten gilt

$$
\lambda_k=3k,\qquad
m_k=\binom nk2^k,\qquad k=0,\ldots,n.
$$

Die mittlere Rückkehrwahrscheinlichkeit ist damit exakt

$$
\boxed{P_n(\tau)=\frac1{3^n}\operatorname{Tr}e^{-\tau L_n}
=\left(\frac{1+2e^{-3\tau}}3\right)^n.}
$$

Die skalenabhängige spektrale Dimension ist

$$
\boxed{d_s(\tau)=-2\frac{d\ln P_n}{d\ln\tau}
=\frac{12n\tau e^{-3\tau}}{1+2e^{-3\tau}}.}
$$

Für jedes feste n geht sie bei sehr kleiner und sehr großer τ gegen null. Ein isolierter Durchgang durch den Wert drei wäre kein makroskopischer Dimensionsbeweis.

### 18.3 Das Maximum ist analytisch bestimmbar

Mit W₀ als reellem Hauptzweig der Lambert W Funktion folgt

$$
\tau_*=\frac{1+W_0(2/e)}3=0.48768517112185\ldots,
$$

$$
\boxed{d_{s,\max}(n)=2nW_0(2/e)
=0.92611102673110\ldots\ n.}
$$

Das Maximum wächst linear mit n; es konvergiert nicht zu drei.

| n | Knoten 3ⁿ | Grad | Kanten | Maximum d_s |
|---:|---:|---:|---:|---:|
| 1 | 3 | 2 | 3 | 0,9261110267 |
| 2 | 9 | 4 | 18 | 1,8522220535 |
| 3 | 27 | 6 | 81 | 2,7783330802 |
| 4 | 81 | 8 | 324 | 3,7044441069 |
| 5 | 243 | 10 | 1215 | 4,6305551337 |
| 6 | 729 | 12 | 4374 | 5,5566661604 |
| 7 | 2187 | 14 | 15309 | 6,4827771871 |
| 8 | 6561 | 16 | 52488 | 7,4088882138 |

### 18.4 Was „6561 Zellen geprüft“ hier bedeutet

Der ursprüngliche Geometriecode wertete die analytische Spektralformel und die daraus folgende Diffusion aus. Er simulierte nicht 6561 miteinander wechselwirkende Quantenzellen in einem Hilbertraum der Dimension 5^6561.

Bei dieser Konsolidierung wurde zusätzlich die dünnbesetzte 6561 × 6561 Adjazenzmatrix von H(8,3) aufgebaut: 52488 ungerichtete Kanten, Grad 16, symmetrische Adjazenz. Die Laplacemultiplizitäten

```text
k:              0    1    2    3     4     5     6     7    8
Eigenwert:      0    3    6    9    12    15    18    21   24
Multiplizität:  1   16  112  448  1120  1792  1792  1024  256
```

wurden mit Dimension und Spur sowie den Wärmeformeln gegengeprüft. Es wurde kein vollständiges Quantenvielteilchenspektrum dieser Größe behauptet. [A1]

### 18.5 Die zweite ausgeschlossene Zahlenabkürzung

Würde man 12/7 als räumlichen linearen Blockfaktor interpretieren, ergäbe sich aus drei Unterzellen pro Block

$$
d_H=\frac{\ln3}{\ln(12/7)}=2.03825495559750\ldots,
$$

nicht drei. Diese Rechnung zeigt, dass die vorgeschlagene Interpretation nicht das gewünschte Ergebnis liefert. Sie beweist nicht von sich aus eine fraktale physische Welt mit Dimension 2,038.


---

<a id="doily"></a>
## 19. Doily, Tutte Coxeter und das lokale Routing

### 19.1 Aus den tatsächlichen Antwortmatrizen konstruiert

Die fünfzehn R_A werden als Knoten genommen. Zwei verschiedene Knoten werden verbunden, wenn ihr Matrixkommutator verschwindet. Daraus entstehen

$$
15\ \text{Knoten},\quad45\ \text{Kanten},\quad\deg=6.
$$

Die fünfzehn Dreiecke des Kommutationsgraphen sind die maximalen kommutierenden Dreierkontexte. Jeder Kanal gehört zu drei Kontexten. Das ist das generalisierte Viereck GQ(2,2), auch W(3,2) oder Doily genannt, in seiner Punktkollinearitätsdarstellung. Die Verbindung zur Zweiqubit Pauli Kommutation ist bekannte endliche Geometrie. [S3; A1; L6]

Sein Adjazenzspektrum ist

$$
6^{\times1},\quad1^{\times9},\quad(-3)^{\times5}.
$$

### 19.2 Punkt und Kontext als zwei Knotentypen

Die Inzidenzmatrix N hat fünfzehn Kanalzeilen und fünfzehn Kontextspalten. N_pL = 1 genau dann, wenn p im Kontext L liegt. Es gilt

$$
NN^\mathsf T=3I+A,
$$

wobei A der Kommutationsgraph ist. Deshalb

$$
\operatorname{spec}(NN^\mathsf T)=9^{\times1},4^{\times9},0^{\times5},
\qquad\operatorname{rank}N=10.
$$

Der bipartite Graph hat Adjazenzmatrix

$$
B_{\mathrm{inc}}=\begin{pmatrix}0&N\\N^\mathsf T&0\end{pmatrix}.
$$

Er besitzt

$$
30\ \text{Knoten},\quad45\ \text{Kanten},\quad\deg=3,
$$

und das exakte Spektrum

$$
\boxed{3^{\times1},2^{\times9},0^{\times10},(-2)^{\times9},(-3)^{\times1}.}
$$

Zusätzlich wurden bei der Konsolidierung kombinatorisch Umfang acht und Durchmesser vier bestätigt. Sein graphentheoretischer Zyklenrang ist 45 − 30 + 1 = 16. Diese letzte 16 ist zunächst nur eine Eulerzählung, keine nachgewiesene Identifikation mit sechzehn Pauliadressen oder einem Fermionenspinor. [A1]

### 19.3 Ein konkreter Bauplan des Tutte Coxeter Graphen

Man kann denselben Inzidenzgraphen ohne Pauli Matrizen beschreiben: Eine Knotenseite besteht aus den fünfzehn Zweiermengen einer Sechsermenge, die andere aus ihren fünfzehn perfekten Matchings. Eine Zweiermenge ist mit einem Matching verbunden, wenn sie zu dessen drei Paaren gehört.

Diese Duad und Matching Darstellung ist der Tutte Coxeter Graph. Sie macht zugleich klar, dass die endliche Struktur nicht als neue Graphenart entdeckt wurde. Der konkrete TFPT Anschluss liegt in der Identifikation mit den tatsächlich berechneten Antwortmatrizen und Quellenrichtungen.

### 19.4 Die lokale Routingregel

Für jeden Kanal p und jeden Dreierkontext L mit p ∉ L gibt es genau ein q ∈ L, das mit p kompatibel ist:

$$
\boxed{\#\{q\in L:q\sim p\}=1.}
$$

Es gibt 15 · 12 = 180 solcher Paare. Alle wurden erneut exakt geprüft. [A1]

```text
externer Kanal p              vorgegebener Kontext L
                                  {a, b, c}
        │                            │
        └──────── Kompatibilität ────┘
                         │
                         ▼
                 genau ein passendes q
```

Die Eindeutigkeit ist eines der definierenden Inzidenzaxiome des generalisierten Vierecks. Sie ist kein zusätzlicher unabhängiger physikalischer Mechanismus.

### 19.5 Was die Regel nicht entscheidet

Die Regel setzt voraus, dass L bereits gewählt ist. Soll q ein bestimmtes Kind einer Dreierkodierung bezeichnen, muss zusätzlich festgelegt sein, wie die drei Elemente von L mit den drei physischen Kindpositionen identifiziert werden. V_△ ist selbst in seinen drei Ausgängen symmetrisch.

Außerdem fehlen die Fälle p ∈ L als Teil einer vollständigen Routingdynamik, eine Regel für die Erzeugung und Löschung von Kanten, Transport und Orientierung der Labels, sowie die Entscheidung, wann zwei Wege wieder dasselbe Ereignis oder dieselbe Zelle erreichen.

Die behauptete Begrenzung auf drei gleichzeitig zulässige Nachbarn folgt ebenfalls nicht allein aus der Kommutation. Dafür müsste beispielsweise verboten werden, denselben Kanal mehrfach zu benutzen, und die Zuordnung „ein Kanal entspricht einer räumlichen Kante“ müsste physisch begründet sein.

**Korrektur der früheren stärkeren Formulierung:** Gefunden wurde eine eindeutige lokale Auswahl innerhalb eines gewählten Kontexts. Nicht gefunden wurde damit bereits die vollständige globale Adressierung des Universalraums.

### 19.6 Warum ein kubischer Graph nicht automatisch dreidimensional ist

Grad drei zählt direkte Nachbarn. Räumliche Dimension beschreibt unter anderem Volumenwachstum, lange Wellen und Diffusion über viele Skalen. Diese Größen sind nicht gleich.

Als unmarkierter zusammenhängender kubischer Graph hat die Inzidenzstruktur einen universellen Überlagerungsbaum vom Grad drei. Dessen Kugeln wachsen wie

$$
|B(r)|=1+3(2^r-1),
$$

also exponentiell, nicht wie r³. Diese Überlagerung erhält die lokale graphentheoretische Umgebung, aber nicht die global geschlossenen Achterzyklen als geschlossene Zyklen. Um sie wieder zu schließen, sind zusätzliche globale Identifikationen erforderlich.

Die endliche Geometrie kann als sphärisches Building vom Typ C₂ eingeordnet werden. Auch diese bekannte Einordnung liefert keinen automatischen Übergang zu einem euklidischen oder Lorentzschen Kontinuum. Die Umdeutung von Dreierkontexten zu physikalischen Flächen ist eine weitere Modellentscheidung.

### 19.7 Die Zahl 30 und E₈

Hier entsteht 30 als 15 Kanäle plus 15 Kontexte. Im E₈ Zusammenhang ist 30 die Coxeterzahl. In dieser Untersuchungsfolge wurde **kein Intertwiner und keine natürliche Orbitidentifikation** zwischen diesen beiden Verwendungen von 30 konstruiert.

Deshalb ist die Gleichheit eine vermerkte Zahlengleichheit, keine zusätzliche bestätigte Verbindung. Der bereits belegte Hamming und Quellenanschluss an E₈ bleibt davon unberührt.

---

<a id="quotient"></a>
## 20. Operationspfade und der noch offene Raumquotient

### 20.1 Die zuletzt vorgeschlagene Idee

Anstatt räumliche Punkte als immer neu erzeugte Knoten einzuführen, könnte man mit Operationswörtern beginnen:

$$
g_{A_1}g_{A_2}\cdots g_{A_n}.
$$

Zunächst bilden mögliche Wörter einen großen Verzweigungsraum. Tatsächliche Relationen identifizieren Wörter, beispielsweise

$$
g_Ag_B=g_Bg_A
$$

bei geeigneter Kommutation. Der vorgeschlagene Raum wäre dann schematisch

$$
\mathcal X=\frac{\text{zulässige Operationspfade}}{\text{begründete Wirkungsgleichheit}}.
$$

Das ist ein **Kandidat**, keine im Gespräch abgeschlossene Konstruktion eines physikalischen Raums. In den letzten beiden Forschungsantworten liegt kein zusätzlicher ausgeführter Prüflauf vor, der diese Lücke geschlossen hätte.

### 20.2 Was ein solcher Quotient erhalten muss

Es reicht nicht, dass zwei Zustände gerade dieselbe Paaranzeige liefern. Sie müssten bezüglich sämtlicher später erlaubter Fortsetzungen dieselben operationalen Vorhersagen liefern. Als konservative Formulierung:

$$
s\sim s'
\quad\Longrightarrow\quad
\text{alle zulässigen zukünftigen Versuche unterscheiden }s,s'\text{ nicht}.
$$

Dabei gehören Phase, Quelle, Rahmen, Ereignisaufzeichnung und die erlaubte Kopplung an weitere Systeme gegebenenfalls zum Zustand. Eine globale Phase eines isolierten Zustands und eine relative Phase zwischen interferierenden Pfaden sind nicht dasselbe.

Mathematisch muss die Äquivalenz mit der vorgesehenen Komposition verträglich sein. Sonst kann ein Quotient heute gleiche Punkte morgen unterschiedlich weiterentwickeln lassen, ohne diesen Unterschied noch darstellen zu können.

### 20.3 Ein bereits dokumentiertes Gegenbeispiel zur zu starken Reduktion

Die ergänzende Quellenherleitung [S4] enthält zwei unnormierte Quellen

$$
z=(1,2,4,8)^\mathsf T,
\qquad z'=(I\otimes X)z=(2,1,8,4)^\mathsf T.
$$

Für die dort definierten Quartikpolynome f = (p,a,b,c,d) gilt

$$
f(z)=f(z')=(4369,6168,1632,768,1536)^\mathsf T.
$$

Unter demselben Quellenoperator H_src = I ⊗ Z, also ż = −iH_srcz, folgt dagegen

$$
\dot f(z)=(15420i,0,5760i,0,0)^\mathsf T,
\qquad\dot f(z')=-\dot f(z).
$$

Die Differenz ist nicht nur eine gemeinsame Phase oder Normänderung. Nach Normierung beider Quellen bleibt der Widerspruch bestehen.

**Folgerung:** Für diese Quellenentwicklung existiert kein eindeutiges autonomes Bewegungsgesetz allein in den reduzierten Quartikkoordinaten. Gleiche momentane Auslesung bedeutet nicht gleiche Zukunft. Der Quellenlift beziehungsweise ein hinreichender Rahmen muss erhalten bleiben. [S4, § 6]

### 20.4 Der lineare Antwortbereich wächst bereits auf 35 Dimensionen

Für die infinitesimalen Quellenoperationen zᵢ∂/∂zⱼ gilt in [S4]

$$
\operatorname{span}_{\mathbb C}\{f_a,z_i\partial_{z_j}f_a\}
=\operatorname{Sym}^4(\mathbb C^4)^*,\qquad\dim=35.
$$

Der zusätzliche symmetrische 30erraum ist damit ein tatsächlicher linearer Antwortsektor der Quelle, nicht automatisch eine Sammlung von dreißig Teilchen.

Auch ein kontinuierlicher linearer Fluss, der die ganze feste Igusa Hyperfläche erhält, ist projektiv trivial: Der Koeffizientenvergleich in

$$
\nabla F(x)\cdot Ax=\kappa F(x)
$$

liefert nur A = κI/4. Das betrifft genau diese feste lineare Darstellung. Diskrete Operationen, nichtlineare Lifts und bewegte Codes sind dadurch nicht ausgeschlossen. [S4, § 6]

### 20.5 Eliminierte Information kehrt als Gedächtnis zurück

Für einen tatsächlich gewählten Hamiltonoperator H und die Zerlegung P, Q = I − P gilt die exakte Resolventenidentität

$$
P(\zeta-H)^{-1}P=
\bigl[\zeta-PHP-PHQ(\zeta-QHQ)^{-1}QHP\bigr]^{-1}.
$$

Der Rückwirkungsterm hängt von ζ ab. Er enthält Information über den entfernten Sektor. Eine konstante gedächtnislose Ersetzung ist eine zusätzliche Näherung, nicht die automatische Folge einer Projektion.

Hier verbindet sich die Quotientenfrage direkt mit den früheren Carry und Phasenproblemen: Wer einen Unterschied entfernt, der unter erlaubter Dynamik später wieder sichtbar wird, braucht entweder zusätzliche Zustandsvariablen oder einen Gedächtniskern.

### 20.6 Warum ein Gruppenquotient nicht von selbst unendlichen Raum erzeugt

Wenn man nur Wörter einer festen endlichen Pauli oder Quellenreflexionsgruppe nach exakter Operatorgleichheit identifiziert, erhält man höchstens die entsprechende endliche Gruppe beziehungsweise einen endlichen Orbit. Die Pauli Gruppe mit Phasen hat hier Ordnung 64; die untersuchte Quellenreflexionsgruppe Ordnung 46080. Ein Quotient ihrer Wörter erzeugt nicht allein eine unendliche dreidimensionale Ortsmenge. [S4, § 3; einfache Folgerung aus Endlichkeit]

Lässt man stattdessen die volle kontinuierliche Kontrollgruppe zu, erhält man zunächst einen Raum interner Operationen, nicht automatisch einen Ortsraum. Lässt man die Zahl der Tensorfaktoren wachsen, muss eine Kompositionsregel für diese verschiedenen Träger angegeben werden.

Der Begriff „Ort = Wirkungsklasse“ wird damit erst zu einer mathematisch prüfbaren Raumdefinition, wenn auch die Träger, die zulässigen Ereignisse, die Zeitordnung und die metrikbestimmende Dynamik festliegen.

### 20.7 Der konkrete noch fehlende Herkunftssatz

Eine tragfähige Quotientenkonstruktion müsste gleichzeitig zeigen, dass die Äquivalenz wohldefiniert ist, erlaubte Komposition respektiert, relevante Phasen und Zukunftsunterschiede erhält, eine wachsende lokale Familie erzeugt und deren Kontinuumsdaten festlegt.

Im vorliegenden Stand ist keine solche eindeutige globale Regel bewiesen. Diese Aussage verwirft den Quotientenansatz nicht; sie benennt genau, was er leisten muss, bevor er als Lösung gelten kann.

---

<a id="sieben"></a>
## 21. Eine alternative geschützte Quelle mit sieben Registern

Dieses Kapitel gehört zur tatsächlich gelesenen ergänzenden Herleitung [S0, § 11; S4, §§ 7–9]. Es ist ein anderer, ausdrücklich definierter Quellschutzansatz. Seine Parameter und Spektren dürfen nicht mit denen der vierregisterbasierten Fünferrekursion vermischt werden.

### 21.1 Der verkürzte Hamming Zusammenhang

Der binäre Zeilenraum C der Matrix

```text
H7 =
1 1 1 1 0 0 0
1 1 0 0 1 1 0
1 0 1 0 1 0 1
```

ist selbstorthogonal. Seine sieben nichtnull Wörter haben Gewicht vier und schneiden sich paarweise in zwei Positionen. Ihre Dreierkomplemente sind die Fano Linien.

Es gilt als Gleichheit konkreter binärer Mengen

$$
\{(c,0)+b\mathbf1_8:c\in C,\ b\in\mathbb F_2\}=RM(1,3).
$$

Derselbe Hamming Ausgangscode, der die E₈ Wurzeln trägt, liefert also kompatible Quartikchecks nach Verkürzung.

### 21.2 Sieben Ququarts erhalten eine logische Viererquelle

Zwei bekannte Steane Kodierungen werden zu sieben vierdimensionalen Registern zusammengefasst. Der Encoder lautet

$$
V_7|ab\rangle=\frac18\sum_{u,v\in C}
|2(u+a\mathbf1)+(v+b\mathbf1)\rangle,\qquad a,b\in\{0,1\}.
$$

Die binären Additionen geschehen modulo zwei. Der logische Hilbertraum ist ℂ⁴. Beliebige Fehler an einem einzelnen physischen Ququartregister sind korrigierbar. Diese Codefamilie ist bekannte Quantenfehlerkorrektur; der hier untersuchte Anschluss betrifft dieselbe TFPT Quellenwirkung. [S0, § 11; L9]

### 21.3 Ein kompatibler positiver Parent

Für jede der sieben Vierermengen S sei Q_S der Pauli Quartikprojektor. Die Checks kommutieren, und

$$
H_F=\sum_S(I-Q_S)
$$

hat das vollständige Spektrum

| Energie | Multiplizität |
|---:|---:|
| 0 | 4 |
| 4 | 420 |
| 6 | 5880 |
| 7 | 10080 |

Die Multiplizitäten summieren sich zu 4⁷ = 16384. Die Lücke ist vier.

Der Unterschied zum unmöglichen Überlappungsversuch ist wesentlich: Hier werden kompatible Q Checks benutzt, nicht gleichzeitig die volle lokale Symmetrisierung S jedes überlappenden Fünferblocks erzwungen.

### 21.4 Bedingte Minimalität der Sieben

In der benannten Klasse doppelt gerader selbstorthogonaler binärer CSS Checks mit demselben Checkraum für beide Pauliarten, mindestens einem logischen Qubit und Korrektur eines unbekannten Einzelfehlers ist sieben die minimale Länge.

Für Checkrang r und Länge n braucht man n − 2r ≥ 1. Die Checkspalten müssen verschieden und nichtnull sein, also n ≤ 2ʳ − 1. Für n ≤ 6 sind diese Anforderungen in der angegebenen nichttrivialen Klasse unvereinbar; n = 7 erlaubt r = 3 und alle sieben nichtnull Spalten von 𝔽₂³.

Das ist eine Minimalität innerhalb einer Informationsaufgabe. Es leitet nicht aus P1/P2 ab, dass die Natur diese Aufgabe oder sieben Register auswählt. Die drei Checkkoordinaten sind keine bewiesenen Raumdimensionen.

### 21.5 Die ursprüngliche Quellenwirkung bleibt erhalten

Für alle sechzig vorhandenen Quellenreflexionen wurde in [S0] exakt geprüft

$$
U^{\otimes7}V_7=V_7\overline U.
$$

Nach zweimaliger Kodierung folgt algebraisch

$$
U^{\otimes49}V_{49}=V_{49}U.
$$

Die komplexe Konjugation ist Teil des Ergebnisses und darf bei orientierten oder geladenen Anschlüssen nicht weggelassen werden. Der Vorteil dieser Alternative: Die ursprüngliche ℂ⁴ Darstellung samt zentralen Phasen bleibt verfügbar, statt durch den quartischen Fünferquotienten ersetzt zu werden.

### 21.6 Voller logischer Quellenaustausch in dritter Ordnung

Für zwei getrennte Siebenregisterblöcke wird in [S4] definiert

$$
H_0=\Delta_F(H_F^A+H_F^B),
$$

$$
V_g=g\sum_{r=1}^7\sum_{a=1}^{15}A_{a,r}^AA_{a,r}^B
=g\sum_{r=1}^7(4\operatorname{SWAP}_r-I).
$$

Erste Ordnung verschwindet; zweite Ordnung ist skalar:

$$
H_{\mathrm{eff}}^{(2)}=-\frac{105g^2}{8\Delta_F}I.
$$

In dritter Ordnung entsteht

$$
\boxed{H_{\mathrm{eff}}^{(3)}=\frac{g^3}{\Delta_F^2}
\left(\frac{21}{8}\operatorname{SWAP}_{\mathrm{logisch}}-\frac{63}{16}I\right).}
$$

Die führende nichttriviale Kopplung ist J_eff = 21g³/(8Δ_F²). Die Restordnung ist O(g⁴/Δ_F³) im festen endlichen Modell, keine behauptete uniforme thermodynamische Schranke.

Die Pfadzählung umfasst 105 elementare Fehlermuster. In dritter Ordnung treten 1470 geordnete Pfade an derselben Registerposition mit skalarem Phasenbeitrag −210 sowie 630 geordnete Pfade auf Fano Linien auf. Beide virtuellen Nenner betragen 8Δ_F. Die Pauli Identität ΣA_a* ⊗ A_a* = 4SWAP − I liefert die Koeffizienten.

Eine unabhängige Einpauli Gegenprobe benutzt ein acht dimensionales Syndrommodell mit

$$
E_\xi=\frac{M+6\xi g-\sqrt{(M+6\xi g)^2+28g^2}}2,
\qquad M=8\Delta_F,\quad\xi=\pm1.
$$

Seine Entwicklung ist −7g²/M + 42ξg³/M² + O(g⁴/M³). Dies bestätigt den entsprechenden Einzelbeitrag, nicht allein die gesamte Fünfzehnkanalsumme.

### 21.7 Gleicher Code, unterschiedliche Dynamik

Die Familie

$$
H_r=r(S-P)+(I-S),\qquad r>0
$$

hat denselben Fünfergrundraum und dieselbe betrachtete Symmetrie, aber unterschiedliche relative Anregungsenergien. Für das frühere Zweilinksmodell lauten die Koeffizienten

$$
C_0=-\frac{5r^2+10r+1}{8r(r+1)},
$$

$$
C_1=\frac{(r-1)(5r+3)}{8r(r+1)},\qquad
C_2=-\frac{5r^2+2r+9}{8r(r+1)}.
$$

Bei r = 1/2 ist C₂ = −15/8, bei r = 1 ist C₂ = −1. Die endliche Codealgebra allein legt also nicht sämtliche Kopplungen fest. Dies ist kein allgemeiner Unmöglichkeitsbeweis für TFPT, sondern eine konkrete Unterbestimmtheit der bisher verwendeten Daten. [S4, § 10]

---

<a id="entropie"></a>
## 22. Entropie, Clock und Informationsgeometrie

### 22.1 Der Punkt t = 1/27

Für einen getrennt definierten Kontrastqubit seien λ_X = 2/3, λ_Z = 1/3 und λ_Y = 6t. Die Pauliwahrscheinlichkeiten seines normierten Choi Zustands sind

$$
p_0=(1+x+y+z)/4,\quad p_X=(1+x-y-z)/4,
$$

$$
p_Y=(1-x+y-z)/4,\quad p_Z=(1-x-y+z)/4.
$$

Entropiestationarität verlangt p_Xp_Z = p₀p_Y. Bei den vorgegebenen x und z führt dies eindeutig zu

$$
\boxed{t=1/27,\qquad\lambda_Y=2/9,}
$$

mit

$$
p=(5/9,5/18,1/18,1/9).
$$

Strikte Konkavität sichert die Eindeutigkeit im zulässigen Intervall. Das Entropieobjekt ist hier genau dieser normierte Choi Zustand, nicht irgendeine beliebige Ereignisverteilung. [S0, § 13]

### 22.2 Eine konkrete Markovrealisierung

Am dimensionslosen Einheitszeitpunkt erzeugt

$$
\mathcal L(\rho)=\frac{\ln3}{2}(X\rho X-\rho)
+\frac{\ln(3/2)}2(Z\rho Z-\rho)
$$

die Faktoren

$$
\lambda_X=2/3,\qquad\lambda_Z=1/3,\qquad
\lambda_Y=\lambda_X\lambda_Z=2/9.
$$

Eine unabhängige Y Sprungrate ist hier null. Das liefert einen Generator für den gewählten Kontrastkanal. Es leitet weder eine physische Zeiteinheit noch den gesamten Quellenprozess ab. Vollständige Positivität allein erzwingt die zusätzliche Regel zweier unabhängiger Sprungarten nicht. [S0, § 13; S1, § 8]

### 22.3 Verschiedene Entropieaufgaben haben verschiedene Maxima

Der Vorbericht nennt für seine genau definierten weiteren Ausführungen numerische Maxima bei t ≈ 0,0357983733 für sechs Ereignisse und t ≈ 0,0365656628 für den dortigen vollständigen Dreiniveau Choi Kanal. Diese Werte sind keine Alternativen desselben unveränderten Optimierungsproblems. Ihre Eingabeobjekte unterscheiden sich.

Eine im Gespräch angedeutete Gleichsetzung mit einem Jarlskog Invarianten wurde in diesem Quellenbestand nicht neu zertifiziert. Ein konjugationsinvariantes Entropiefunktional kann zudem nicht ohne weitere orientierende Daten das Vorzeichen einer konjugationsungeraden Größe auswählen. [S0, § 13]

### 22.4 Informationsmetrik ist noch keine Raumzeitmetrik

Für die kollektive Orientierung des ursprünglichen Codes gilt

$$
P\,d\Gamma_4(X)\,P=\operatorname{tr}(X)P.
$$

Für spurfreie Hermitesche X,Y liefert die betrachtete Familie

$$
g(X,Y)=8\operatorname{tr}(XY),\qquad F_Q=\frac45g.
$$

Das ist eine positive Informationsmetrik in einem 15 dimensionalen inneren Tangentialraum. Sie ist nicht automatisch eine Lorentzmetrik. [S0, § 12]

Die Berry Verbindung der kollektiv bewegten Basis U⊗⁴V lautet

$$
\mathcal A=\operatorname{tr}(U^\dagger dU)I_5.
$$

Auf SU(4) verschwindet sie; in der betrachteten U(4) Familie ist ihre lokale Berry Krümmung ebenfalls null. Diese reine kollektive Orientierungsfamilie erzeugt deshalb allein kein kontinuierliches nichtabelsches Eichfeld. Diskrete Holonomie in einem Quotienten wird dadurch nicht ausgeschlossen. Berry Krümmung und Riemannsche Krümmung der Informationsmetrik sind verschiedene Größen.

### 22.5 Zeit darf nicht nur umbenannt werden

Ein Hamiltonoperator definiert bereits eine Entwicklung bezüglich eines Zeitparameters. Ihn hinzuschreiben und danach „Zeit entsteht aus Zustandsänderung“ zu sagen, ist noch keine Herleitung dieses Parameters.

Ebenso führt die Reihenfolge beliebiger reversibler Operationen nicht automatisch zu einer kausalen partiellen Ordnung ohne Zyklen. Dafür müssen Ereignisse, Abhängigkeiten, zulässige Rückwirkungen und die Relation zwischen physischer Zeit und mathematischem Parameter genau definiert werden.

---

<a id="muster"></a>
## 23. Die Zahlen und ihre wirklichen Verbindungen

### 23.1 Musterkarte

| Muster | Konkrete Herkunft | Belegstand und Grenze |
|---|---|---|
| 4 → 256 → 35 → 5 | Vier Ququarts, symmetrische vierte Potenz, quartischer Code | Explizite Räume und Projektoren. Keine Raumdimensionen. |
| [8,4,4] → 240 → 60 | Hamming, E₈ Wurzeln, komplexe Phasenorbits | Expliziter Code und deklarierte komplexe Struktur. |
| 60 → 15 × 4 | Quellenprojektion und endliche Quotientenwirkungen | Konkrete vierfache Urbilder; die jeweiligen Zielobjekte müssen unterschieden werden. |
| 5 → 3+2 | Rang 2 zweite Antwort im Fünfer | Operatorielle Zerlegung, keine vollständige Materieherleitung. |
| 2 / 3 / 4 | Paarsteuerung, Dreiregisterrekonstruktion, quartische Codeauswahl | Kodierungsspezifische Ordnungshierarchie. |
| 25 = 1+9+5+10 | Vollständiger logischer Operatorraum | Identität, sichtbare Paarinformation und zwei Blindsektoren. |
| 10 gleichwinklige Linien | Bell Paarmessung | Explizite W₁₀ Matrix. |
| 6 Simplexmarkierungen ↔ 6 Petersenrahmen | Vorzeichengleichung s_q = W₁₀u_q/2 | Direkte Abbildung, nicht nur gleiche Anzahl. |
| 15₃ ↔ Igusa ↔ Doily | Punkte, Singularlinien und Kompatibilität | Explizite Inzidenz; keine globale Raumdimension. |
| 2/3 ↔ 4/9 | Normierter Singularwert und Rückkomposition | Quadratbeziehung, keine universelle Clockgleichsetzung. |
| 3 Fünfer → 1 Fünfer | Dreiecksgrundraum | Exakte Isometrie, Lücke 3J. |
| 7/12 und 49/144 | Blockkompression von Antwort und bilinearer Kante | λ_K = λ_Y²; noch keine räumlichen kritischen Exponenten. |
| C₁₆ und H₈ ⊕ H₈ | Zwei selbstduale Codekonstruktionen | Gleiches vollständiges Gewichtspolynom zweiter Ordnung, unterschiedliche Blocktensoren. |
| d₄ − e₄ = −𝓘/48 | Unterschied spezieller projizierter Codeamplituden | Exakte unsichtbare Quartikrichtung. |
| 𝒯 = 8(2e₄+3d₄) | Energetische Viererbindung | Exakte kohärente Kombination; zwei und drei sind hier keine Eichgruppenableitung. |
| 8,12,20,24 | Quellengrad vier mal symmetrische Grade 2,3,5,6 | Vollständiger Invariantenring der benannten endlichen Quellenwirkung. |
| 30 = 15+15 und h(E₈)=30 | Inzidenzknoten versus Coxeterzahl | Zahlengleichheit; keine bewiesene Objektidentifikation. |
| 16 = 45−30+1 | Zyklenrang des endlichen Inzidenzgraphen | Reine Graphenzählung; nicht mit Spinor oder Pauligruppe identifiziert. |
| 7 und 49 | Alternative Hamming Quellkodierung, zweimalige Konjugation | Bedingte Schutzkonstruktion, keine Raum und Zeitmaße. |
| 6561 = 3⁸ | Größe der getesteten kartesischen Graphenfamilie | Kontrollierter Gegencheck, kein Quantenvielteilchenbeweis. |

### 23.2 Eine weitere mathematische Brücke zu sechzehn Ladungszuständen

Unter einer **zusätzlich gewählten** fundamentalen 3+2 Markierung von ℂ⁵ kann man die gerade äußere Algebra bilden:

$$
\Lambda^{\mathrm{even}}\mathbb C^5
=\Lambda^0\mathbb C^5\oplus\Lambda^2\mathbb C^5\oplus\Lambda^4\mathbb C^5,
$$

$$
\dim=1+10+5=16.
$$

Die Ladung auf einem äußeren Produkt ist die Summe seiner Einzelwerte. Damit entsteht die bekannte Darstellungsliste:

| Teilraum | Darstellung unter SU(3) × SU(2) | Y |
|---|---|---:|
| Λ⁰ | (1,1) | 0 |
| Zwei Farbslots | (3̄,1) | −2/3 |
| Ein Farbslot und ein schwacher Slot | (3,2) | +1/6 |
| Zwei schwache Slots | (1,1) | +1 |
| Λ⁴, fehlender Farbslot | (3̄,1) | +1/3 |
| Λ⁴, fehlender schwacher Slot | (1,2) | −1/2 |

Dies ist die bekannte algebraische Struktur 1 ⊕ 10 ⊕ 5̄. Sie erklärt, warum ein Fünfer mit dieser Ladungsmarkierung natürlich Anschluss an übliche vereinheitlichte Darstellungen besitzt. Die äußere Algebra, ihre Feldstatistik und ihre raumzeitliche Realisierung sind hier jedoch zusätzliche Konstruktionen. Drei Generationen, chirale Dynamik, Massen und Kopplungen folgen nicht aus der bloßen Zahl sechzehn. [S0, § 7; L10; direkte äußere Algebra Rechnung]

### 23.3 Was „alles ist dasselbe Objekt“ sinnvoll heißen kann

Mehrere Strukturen stammen aus denselben Ausgangsdaten und sind durch explizite Abbildungen verbunden. Das ist stärker als eine Analogie. Es bedeutet aber nicht, dass Quelle, Code, Invariantenring, Hilbertraum, Graph und physische Feldtheorie wörtlich dasselbe Objekt sind.

Die richtige Form ist ein **Diagramm nachgewiesener Abbildungen mit bekannten Informationsverlusten**. Manche Pfeile sind Isometrien, manche Projektionen, manche Quotienten und manche zusätzliche Modellwahlen. Gerade diese Unterschiede entscheiden über Dynamik und physische Bedeutung.

---

<a id="synthese"></a>
## 24. Was die Gesamtsynthese jetzt trägt

### 24.1 Die belastbare geschlossene Struktur

$$
\boxed{
\text{Hamming / Quellen}
\longrightarrow
\text{quartischer Code}
\longrightarrow
\text{Auslesung und Antworten}
\longrightarrow
\text{definierte Bindung}
\longrightarrow
\text{rekursive Kodierung}
}
$$

Parallel sind die Antwort und Quellenstrukturen durch die Igusa Geometrie, den Invariantenring, die Doily und die Codegewichtspolynome miteinander verbunden.

Die geschlossene endliche Aussage besteht aus fünf miteinander verbundenen Teilen:

**Schutz:** Der Code ist explizit definiert und besitzt eine positive gewählte Energie mit Lücke.  
**Information:** Die Auslesekanäle zeigen genau, was lokal sichtbar und unsichtbar ist.  
**Transformation:** Symmetrisierte Paaroperationen erlauben vollständige logische Steuerung.  
**Relation:** Definierte mikroskopische Kopplungen erzeugen nichttriviale effektive Bindungen.  
**Rekursion:** Bestimmte gekoppelte Blöcke tragen wieder eine Fünferdarstellung mit berechenbarem Operatortransport.

### 24.2 Was daran der konkrete Fortschritt ist

Der Fortschritt liegt nicht in der erstmaligen Entdeckung von Hamming Codes, der Igusa Quartik, S₆ oder dem Tutte Coxeter Graphen. Diese Gegenstände sind bekannt.

Der konkrete Untersuchungsgewinn besteht in den gemeinsam ausgeschriebenen Realisierungen: der Momentenidentität, den Schutz und Überlappungssätzen, den Antwortprojektoren, dem globalen Zweizellenbindungsbeweis, der Dreierisometrie, dem Vierertensor, der Codeprojektion und den klaren Gegenbeispielen zu zu starken Raum und Dynamikinterpretationen.

Ob einzelne Kombinationen darüber hinaus wissenschaftliche Originalität besitzen, verlangt eine eigenständige Literatur und Prioritätsprüfung. Das wird nicht durch die Anzahl bestandener Skriptbedingungen entschieden.

### 24.3 Die mögliche physische Architektur

Als Forschungshypothese kann man notieren

$$
\mathfrak M=(\mathcal C,\mathcal A,\mathcal R,\omega,\mathcal H),
$$

mit zulässigen Code beziehungsweise Quellenzuständen 𝒞, erlaubten Operationen 𝒜, Kompositions und Relationsregeln ℛ, einem Zustand ω und einer tatsächlich ausgewählten Dynamik ℋ.

Die kürzere Skizze (𝒞,𝒜,ℛ) beschreibt eine sinnvolle algebraische Architektur. Für eine physische Theorie fehlen darin als explizite Daten aber mindestens die Zustands und Dynamikauswahl. Ein Code legt nicht allein fest, was in der Welt tatsächlich passiert.

```text
Regel für Information
       │
       ▼
zulässige Zustände und Operationen
       │
       ▼
verträgliche Bindungen und Komposition
       │
       ⋮  gemeinsame Auswahlregel noch zu beweisen
       ▼
großes lokales dynamisches System
       │
       ⋮  kontrollierter Kontinuumsgrenzwert noch zu beweisen
       ▼
Raumzeit, chirale Felder und Geometriedynamik
```

### 24.4 Die Stellung von E₈

Für diese Fortsetzung ist es produktiv, nicht alles unmittelbar als Physik einer ungebrochenen E₈ Eichgruppe zu lesen. Der nachgewiesene E₈ Anschluss organisiert diskrete Quellen und Invarianten.

Die stärkere Aussage „E₈ ist endgültig nur ein vollständiger Transformationsraum des Codes“ wäre jedoch ebenfalls nicht bewiesen. Präzise dokumentiert wird, welche E₈ Daten, welche endliche Reflexionsgruppe und welche Quotientendarstellungen tatsächlich in den jeweiligen Pfeilen vorkommen.

---

<a id="offene-tore"></a>
## 25. Verworfene Abkürzungen und verbleibende Beweisaufgaben

### 25.1 Die Gegenproben gehören zum Ergebnis

| Frühere Abkürzung | Präzisiertes Ergebnis |
|---|---|
| Ein positiver Momentenoperator ist automatisch das physische Energiegesetz. | Er ist ein konsistenter Kandidat; die Auswahl seiner Funktion und Skala bleibt zusätzlich. |
| Drei Register reichen für Auslesung, also auch für die Auswahl des gesamten Grundraums. | Nein. Gleiche Dreiermarginalen verhindern genau diese Grundraumisolierung. |
| PHP zeigt bereits eine ausführbare codeerhaltende Operation. | Nein. Ein isolierter Paarpuls kann den Code verlassen. Symmetrisierung liefert hier die echte Lösung. |
| Jede Ladung braucht drei Register. | Falsch verallgemeinert. Die Antwortmarkierung Y_A liegt bereits in der Paarspanne; eine andere markierte Ladung nicht. |
| Gleiche lokale Ausgabe bedeutet gleicher Zustand. | Nein. Die sechs Simplexzustände und der Quellenzweigtest liefern konkrete Gegenbeispiele. |
| Die Quartik ist der gesamte erlaubte Zustandsraum. | Nein. Paarpulse erzeugen Codezustände außerhalb ihrer Quellenmannigfaltigkeit. |
| Jeder perfekte Fünferblock kann Register mit Nachbarblöcken teilen. | In der identisch orientierten direkten Einbettung unmöglich. |
| Der exakte mikroskopische Zweiergrundzustand ist bei endlichem g einfach Ω₅. | Er enthält einen exakt bestimmten Anregungsanteil; seine konditionierte Codekomponente ist Ω₅. |
| Maximal verschränkte Paare können alle Kanten eines Netzes unabhängig erfüllen. | Monogamie verhindert das für dieselbe ganze Zelle. |
| Monogamie hält den attraktiven Graphen automatisch dünn. | Nein. Jede zusätzliche kostenlose attraktive Kante senkt die Energie. |
| V_△ erzeugt eine vollständige physische RG. | Bewiesen sind eine Isometrie und führende Kompressionsidentitäten, nicht alle höheren Ordnungen. |
| Die neue Dreierzelle hat denselben Fehlerschutz wie der ursprüngliche Code. | Nein. Ihr Einzelregisterkanal hat vollen linearen Rang. |
| Drei Kinder oder Grad drei bedeuten drei Raumdimensionen. | Nein. Die getestete kartesische Familie besitzt kein stabiles dreidimensionales Plateau. |
| α ≈ 1/2 und 2α ≈ 1 sind schon räumliche kritische Exponenten. | Ohne abgeleiteten linearen Längenfaktor sind es Abschwächungsexponenten pro Blattzahl. |
| Das Routing bestimmt die globale Verklebung. | Es wählt nur innerhalb eines bereits gewählten und markierten Kontexts einen Kanal. |
| Wirkungsklassen endlicher Gruppen erzeugen automatisch unendlichen Raum. | Ohne zusätzliche Träger und Kompositionsregel bleibt der Quotient endlich. |
| Drei Raumbeweise würden Gravitation automatisch erledigen. | Eine universell gekoppelte masselose Spin 2 Dynamik bleibt ein eigener Herkunftssatz. |

### 25.2 Was eine vollständige physische Lösung zusätzlich liefern muss

**Gemeinsame Herkunft.** Dieselben unabhängigen TFPT Ausgangsdaten müssen Registerfaktorisierung, Quellenregel, Energien, relative Koeffizienten, Zustand und zulässige Komposition auswählen. Unterschiedliche passende Modellentscheidungen dürfen nicht nachträglich als ein einziger Zwang behandelt werden.

**Autonome lokale Struktur.** Ein großer Verbund muss ohne vorgegebenes räumliches Gitter, ohne kostenlosen Graphenkollaps, ohne willkürlich gewählten Baum und ohne bloßes Nebeneinander isolierter Dimere entstehen. Lokale Verträglichkeit und globale Auswahl sind getrennt nachzuweisen.

**Räumlicher Kontinuumsgrenzwert.** Eine wachsende Familie muss über zunehmende Skalen konsistente räumliche Dimension drei, geeignetes Volumenwachstum und eine entsprechende langwellige Dynamik zeigen. Ein einzelner Eigenwert, Grad oder Kurvenschnitt reicht nicht.

**Zeit und Relativität.** Die Zeit beziehungsweise Ereignisordnung, ein universeller Ausbreitungskegel und die relativistische Symmetrie müssen zur gleichen Konstruktion gehören. Ein endlicher Geschwindigkeitsrand allein wäre noch keine volle Lorentzinvarianz; eine positive Informationsmetrik noch keine Lorentzsignatur.

**Materie und Chiralität.** Es braucht eine lokale graduierte Feldalgebra mit den beobachteten chiralen Darstellungen. Die algebraische 1 ⊕ 10 ⊕ 5̄ Struktur, ein Rang 2 Projektor oder eine zufällig auftauchende 16 ersetzen keine Feldstatistik, keine Anomaliekontrolle und keine Herleitung dreier Familien.

**Parameter und Spektrum.** Massen, Mischungen, Neutrinoeigenschaften und die unabhängigen Kopplungen müssen im gleichen physikalischen Wörterbuch hergeleitet werden. Nachträgliche Normierung auf eine bekannte Zahl ist keine Vorhersage.

**Gravitation.** Schwankungen einer Graphenstruktur werden erst dann zu einer gravitativen Theorie, wenn die richtigen langwelligen Freiheitsgrade, eine masselose Spin 2 Mode, universelle Kopplung, konsistente Zwangsbedingungen und der passende effektive Dynamikgrenzwert gezeigt werden.

**Gemeinsamer Zustand und überprüfbare Vorhersagen.** Alle Auslesungen müssen aus demselben Zustand und demselben Erzeugungsprozess stammen. Danach braucht es unabhängig prüfbare physische Vorhersagen. Interne algebraische Konsistenz ist notwendig, aber nicht allein empirische Bestätigung.

Diese Punkte sind keine Behauptung, dass das Vorhaben unmöglich sei. Sie sind die noch nicht durch die hier dokumentierten Rechnungen ersetzten Schlussfolgerungen.

### 25.3 Der unmittelbar nächste mathematische Test

Für den begonnenen Raumansatz lautet die fehlende Eingabe nicht „mehr Knoten“, sondern eine **vollständige lokale Kompositions und Identifikationsregel**. Ein reproduzierbarer nächster Lauf müsste deshalb zuerst genau angeben:

```text
Eingabe
  lokale Quellen und erlaubte Operationen
  Kanten beziehungsweise Ereignislabels
  Regel für den Transport dieser Labels
  Gleichheitsregel für wieder zusammentreffende Pfade
  dynamisches Gewicht oder Auswahlprinzip

Prüfung
  widerspruchsfreie endliche Fortsetzungen
  Eindeutigkeit oder explizite Mehrdeutigkeit
  Wachstum und Gradkontrolle
  Informations und Phasentreue der Quotienten
  erst danach Spektren und Kontinuumsgrößen
```

Mehrere unterschiedliche globale Fortsetzungen mit denselben lokalen Regeln wären selbst ein wichtiges Ergebnis: Sie würden präzise zeigen, welche zusätzliche Auswahl noch fehlt. Eine gewünschte dreidimensionale Familie per Hand herauszugreifen würde diese Frage nicht lösen.

---

<a id="hylaean"></a>
## 26. Bedeutung für Hylæan

Die hier dokumentierten mathematischen Ergebnisse liefern keine nachgewiesene Überlegenheit einer KI Architektur. Sie liefern aber eine konkrete Entwurfsregel, die in der vorherigen Diskussion leicht verwässert werden konnte:

> Zustände dürfen nur dann zusammengefasst werden, wenn keine für zukünftige erlaubte Operationen relevante Unterscheidung verloren geht.

### 26.1 Die übertragbare Struktur

Eine kompakte Auslesung darf nicht mit dem vollständigen ausführbaren Zustand verwechselt werden. Phasen, Quellenzweige oder andere latente Unterschiede können zunächst unsichtbar und später wirksam sein. Eine feste Quellenmannigfaltigkeit kann eine Klasse von Eingaben beschreiben, ohne sämtliche dynamisch erreichbaren Zustände zu enthalten.

Für eine lernende Architektur spricht dies für getrennte Begriffe: latenter Zustand, aktueller Readout, ausführbare Operationen, überprüfte Kompositionsregeln und ein Mechanismus zur Erweiterung des Zustands, sobald Gegenbeispiele auftreten.

### 26.2 Was daraus nicht folgt

Die Normierung auf eine Einheitskugel ist nicht an sich ein Fehler. Auch normierte Quantenzustände liegen auf einer Einheitssphäre. Problematisch wäre, entscheidungsrelevante Größen wie Amplitude, Kontext, relative Phase oder Gedächtnis zu entfernen, obwohl die spätere Dynamik davon abhängt.

Ebenso ist eine allgemeine Zustandsdimension fünf, sechzig oder 205 nicht allein deshalb für KI geeignet, weil sie in einem verwandten mathematischen Modell auftritt. Für 205 liegt in der hier ausgewerteten Gesprächslinie keine zusätzliche verifizierte Rechnung vor; diese Zahl wird deshalb nicht zu einem neuen Ergebnis dieser Datei gemacht.

### 26.3 Ein prüfbarer Architekturtransfer

Ein tatsächlicher KI Test müsste gleiche aktuelle Auslesung bei verschiedener zukünftiger Wirkung gezielt erzeugen. Das System müsste den Unterschied erkennen, seinen Zustandsraum passend aufspalten und die daraus gewonnene Regel auf neue Aufgaben übertragen. Erst gemessene Generalisierung, Rechenaufwand und Vergleich mit geeigneten Baselines entscheiden über einen Vorteil.

Die mathematische Lehre ist somit konkret. Ein allgemeiner Quantenvorteil, eine selbstlernende Weltformel oder ein wirtschaftlicher Durchbruch von Hylæan ist durch diese Rechnungen nicht bewiesen.

---

<a id="glossar"></a>
## 27. Glossar

| Begriff | Bedeutung in dieser Datei |
|---|---|
| Register | Ein gewählter Tensorfaktor des Modells, hier zunächst ℂ⁴. Nicht automatisch ein räumlicher Ort. |
| Qubit / Ququart | Zwei beziehungsweise vier orthogonale Basiszustände eines Quantensystems. |
| Code | Ein ausgezeichneter Unterraum mit bestimmten Schutz oder Darstellungsmerkmalen. |
| Projektor | Operator P mit P² = P = P†; er identifiziert einen Unterraum. |
| Isometrie | Lineare Einbettung V mit V†V = I; sie erhält innere Produkte. |
| Moment M₄ | Mittelwert der vierten Tensorpotenzen der Quellenprojektoren. |
| Parent Energie | Bewusst konstruierter Hamiltonoperator mit dem gewünschten Grundraum. |
| Lücke | Abstand der niedrigsten Energie zur nächsthöheren Energie. |
| Leakage / Austritt | Zwischenzeitliche oder bleibende Besetzung außerhalb des betrachteten Codeunterraums. |
| Marginale | Reduzierter Zustand nach Ausblenden anderer Register. |
| Readout / Auslesung | Welche Information ein definierter Mess oder Reduktionskanal zugänglich macht. |
| Paarspanne | Linearer Raum der im Modell durch Paaroperationen darstellbaren logischen Operatoren. |
| Zentralisator | Transformationen, die mit einem gewählten Operator kommutieren. |
| Kontrollalgebra | Durch steuerbare Generatoren und deren Kommutatoren erzeugbare Dynamik. |
| Eichsymmetrie | Lokale Redundanz einer physikalischen Feldbeschreibung; nicht identisch mit Kontrollalgebra. |
| Igusa Quartik | Die hier auftretende algebraische Relation der speziellen Quellenpräparation. |
| Simplex | Symmetrische Anordnung von sechs nichtorthogonalen Richtungen in einem Fünferraum. |
| Doily | Endliche Punkt und Liniengeometrie GQ(2,2) beziehungsweise W(3,2). |
| Tutte Coxeter Graph | Ihr kubischer bipartiter Inzidenzgraph mit 30 Knoten. |
| Matching | Aufteilung einer Sechsermenge in drei disjunkte Zweierpaare. |
| Virtueller Prozess | Effektive tiefe Wirkung über zwischenzeitlich angeregte Zustände. |
| Schrieffer Wolff Entwicklung | Kontrollierte Methode zur Beschreibung des tiefen Energiesektors. |
| Kohärente Summe | Summe von Amplituden mit ihren relativen Phasen, nicht statistisches Gemisch. |
| Gewichtspolynom | Kodierung der Häufigkeiten verschiedener Symbolmuster eines klassischen Codes. |
| RG / Blockkompression | Zusammenfassung kleiner Skalen mit Transport der wirksamen Operatoren. |
| Spektrale Dimension | Aus der Skalierung einer Diffusionsrückkehrfunktion definierte Größe. |
| Quellenlift | Zusätzliche Information, die eine reduzierte Auslesung wieder an ihren Ursprung bindet. |
| Holonomie | Wirkung eines geschlossenen Transportwegs; je nach Konstruktion diskret oder kontinuierlich. |
| Physischer Herkunftssatz | Beweis, dass die Modellbestandteile aus denselben ursprünglichen Daten folgen und die behauptete physische Bedeutung haben. |

---

<a id="pruefstand"></a>
## 28. Prüfstand und Reproduktion

### 28.1 Tatsächlich vorhandene Eingabedateien

Diese Zusammenstellung hat die bereitgestellten Dateien

```text
TFPT_Rekursion/HERLEITUNG.md
TFPT_Rekursion/README.md
TFPT_Rekursion/WEITERFUEHRUNG_6561.md
TFPT_Rekursion_Quartik_Codes_20260926.zip
TFPT_Rekursion_6561_Test.zip
```

sowie die bibliografisch in Kapitel 29 bezeichneten Vorberichte verwendet. Die Kopie unter `tfpt_fortsetzung_20260926/HERLEITUNG.md` enthält denselben bereitgestellten Rekursionsbericht und wurde nicht als unabhängiger zusätzlicher Beweis gezählt.

### 28.2 Neue Ausführung in einer getrennten Arbeitskopie

`run_all.py` startet die vier Programme `explore.py`, `exact_triangle.py`, `source_and_hamming.py` und `code16.py`. Diese wurden im normalen Modus und mit `python -OO` erneut erfolgreich ausgeführt.

| Ergebnisdatei | Zwischen beiden neuen Läufen bytegleich |
|---|---|
| exploration_results.json | Ja |
| exact_triangle_results.json | Ja |
| source_hamming_results.json | Ja |
| code16_results.json | Ja |

Die 60 Prüfbedingungen des exakten Dreierprogramms enthalten die vollständige Spektralzertifizierung, die 45 Antwortkompressionen, die Isometriemetrik, die Viererzustandsbedingungen und das Eindeutigkeitszertifikat.

Der Adapter von den ursprünglichen Ququart Paulis zu den Matchingprojektoren wird zusätzlich numerisch geprüft. Sein Fehler liegt in der Größenordnung 10⁻¹⁶. Diese numerische Adaptierung wird nicht als neue phasentreue Vollprüfung sämtlicher ursprünglicher TFPT Repositorymodule ausgegeben.

### 28.3 Eigenständige Konsolidierungsprüfung A1

Der zusätzliche Prüfer dieser Zusammenstellung bestätigt 230 Bedingungen. Darunter befinden sich sämtliche 180 lokalen Routingfälle, die genaue Matrixidentität NNᵀ = 3I + A, das exakte 30er Spektrum, Zusammenhang, Umfang und Durchmesser des Inzidenzgraphen, die explizite Adjazenz von H(8,3) und die Konsistenz von Wärmeformel und Spektralmultiplizitäten.

**Wichtige Bestandspräzisierung:** Im bereitgestellten ursprünglichen `recursive_geometry_test.py` sind die fünfzehn Kanäle, fünfzehn Dreierkontexte und die analytische Hamming Diffusion implementiert. Die Aussagen über die 30er Inzidenz und 180 Routen stehen im Bericht, waren aber in diesem konkreten Skript noch nicht als entsprechende eigene Ausgaben enthalten. Deshalb wurden sie hier separat rekonstruiert und geprüft.

Das ursprüngliche Geometrieskript verwendet zudem `assert` für einige lokale Bedingungen. Solche Bedingungen werden unter `-OO` deaktiviert. Die behauptete Bytegleichheit der vier zentralen Rekursionsdateien betrifft die expliziten vier Programme von `run_all.py`; sie ist kein Beleg dafür, dass Assertions in beliebigen Zusatzskripten erhalten bleiben. Der zusätzliche A1 Prüfer verwendet explizite Ausnahmen statt abschaltbarer Assertions.

### 28.4 Was nicht erneut ausgeführt wurde

Die historischen Prüfstände der früheren Quellenberichte, einschließlich der 385 beziehungsweise 1065 dort berichteten Bedingungen und der ursprünglichen vollständigen Zweizellenabschätzung, werden hier als Quellenbefunde behandelt. Die entsprechenden Texte wurden gelesen; nicht jedes frühere Prüfarchiv wurde in diesem Lauf erneut ausgeführt.

Eine formale Lean oder Coq Verifikation des gesamten neuen Modells liegt nicht vor. Eine frühere Gaußsche Codebrücke berichtet separat eigene formale Sätze. Das ist nicht mit einer Formalisierung der hier späteren Quantendynamik gleichzusetzen.

### 28.5 Ausführung der eingebetteten Rekursionsprogramme

Die vollständigen verfügbaren Programme dieses Zweigs sind im Anhang eingebettet. Für eine Nachrechnung werden Python 3, NumPy, SciPy und SymPy benötigt. Die Programme sind so angeordnet, dass sie ihre Arbeitsmatrizen selbst erzeugen.

```bash
python -m pip install numpy scipy sympy
cd TFPT_Rekursion
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python run_all.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -OO run_all.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python recursive_geometry_test.py
```

Der eigene Konsolidierungsprüfer erwartet das Verzeichnis `TFPT_Rekursion` neben sich. Die zusätzlich enthaltene Extraktionshilfe legt diese Anordnung aus den eingebetteten Programmblöcken an. Sie erzeugt keine neue physische Annahme, sondern stellt die vorhandenen Prüfungen bereit.

### 28.6 Prüfsummen der beiden bereitgestellten Archive

```text
TFPT_Rekursion_Quartik_Codes_20260926.zip
Bytes: 38209
SHA256:
297c5f6fde0dc40c07522310ba787479c74c6af144d09dfd20e5dc2af4993f84

TFPT_Rekursion_6561_Test.zip
Bytes: 44193
SHA256:
c287ad60af0b234bbf94d969d0af35c545d8b15785615a58f70f42b189423768
```

Diese Werte wurden aus den tatsächlich vorhandenen Bytes berechnet. Sie identifizieren die Eingaben, nicht deren physische Richtigkeit.

---

<a id="quellen"></a>
## 29. Quellen und Versionszuordnung

### 29.1 Dokumentierte eigene Grundlagen

Die Kürzel im Haupttext zeigen auf konkrete Dokumente und Abschnitte. Die Quellen sind Projekt und Gesprächsdokumentation, keine unabhängige externe Begutachtung ihrer TFPT Behauptungen.

**[S0] TFPT_Quartik_Fortsetzung_Herleitungen_20260926.md.** Titel: „TFPT: Quartikcode, Prozessauslesung und quellentreue Komposition“. Fassung vom 26. September 2026. Vollständig gelesen. Themen: expliziter Code, Auslesekanäle, Petersen, Simplex, 2/3 und 4/9, echte Paarsteuerung, markierte Ladung, Überlappung, Zweilinksmodell, sieben Register, Informationsmetrik und Entropie. Bibliotheksdatei `file_00000000d5208210a30c83a6e9950055`, Version 1.

**[S1] HERLEITUNG(2).md.** Titel: „TFPT: quartischer Code, Igusa-Geometrie und ausgewählte Bindungsdynamik“. Fassung vom 26. September 2026. Vollständig gelesene Ausgangsherleitung dieser Gesprächsfolge. Themen: Momentenparent, minimale Schutzordnung, fünfzehn Antworten, explizite Igusa Karte, virtuelle Kopplung, exakter globaler Zweizellenbindungssatz und Hamming Projektion. Bibliotheksdatei `file_000000009a4c81f48becdbc1d98f72d2`, Version 1.

**[S2] TFPT_Rekursion/HERLEITUNG.md.** Titel: „TFPT: exakte Dreizellen-Rekursion, Quartiktensor und ein weiterer selbstdualer Code“. Fassung vom 26. September 2026, 468 Textzeilen der bereitgestellten Datei. Vollständig gelesen; vorhandenes Prüfpaket erneut ausgeführt. Themen: Matchingdarstellung, Dreierspektrum, V_△, Operatortransport, Viererzustand, C₁₆, dritte Ordnung und negative Kontrollen. Bereitgestellte Datei `file_0000000098bc81f4bd31bd114bf7f7d7`.

**[S3] TFPT_Rekursion/WEITERFUEHRUNG_6561.md.** Titel: „TFPT Rekursive Geometrie: Test bis 6561 Zellen“. Bereitgestellte Fassung mit 66 Textzeilen. Vollständig gelesen und gegen die verfügbaren Programme geprüft. Die Einschränkungen zu Routing, globaler Auswahl und RG Exponenten werden im vorliegenden Dokument präzisiert. Bereitgestellte Datei `file_00000000125482109857b3b749389111`.

**[S4] TFPT_Igusa_Quellendynamik_Herleitung_20260926.md.** Titel: „TFPT: Igusa Geometrie, vollständiger Invariantenring und geschützte Quellendynamik“. Fassung vom 26. September 2026. Vollständig gelesen. Ergänzende Grundlagen zu Invariantenring, Quellenreflexionen, Spiegeln, Bellquadriken, Quellenzweigen, 35er Antwortabschluss, sieben Registern und dem logischen Austausch dritter Ordnung. Bibliotheksdatei `file_0000000098188246952655cd44f6d20a`, Version 1. Die darin berichteten 1065 Prüfbedingungen wurden bei dieser Zusammenstellung nicht erneut ausgeführt.

**[S5] note_e8_gaussian_code(20260821-102224).pdf.** Titel: „The Gaussian code bridge: E8 over Z[i], the extended Hamming code, and a four-bit information layer“, Stefan Hamann, datiert 3. August 2026. Der im Gespräch vorhandene Abstract und Anfang wurden für den begrenzten E₈ Anschluss verwendet. Keine vollständige erneute Prüfung des PDFs, der dortigen ursprünglichen Programme oder der genannten formalen Sätze. Bibliotheksdatei `file_000000000cd08243b1af5809f632e517`, Version 1.

**[A1] Konsolidierungsprüfer und neue Laufprotokolle dieser Datei.** Eigenständige Rekonstruktion der endlichen Inzidenz und Routen sowie der Hamming Adjazenz, zusätzlich zu den erneut ausgeführten Rekursionsprogrammen. Quellcode und kompakte Ergebnisdaten stehen unten in den Anhängen. Er prüft keine nicht angegebene globale Raumkonstruktion.

Die zuletzt im Gespräch nur vorgeschlagenen Operationspfadquotienten werden als **Gesprächshypothese** geführt. Die leeren beziehungsweise abgebrochenen Antworten am Ende der Forschungsfolge liefern keinen zusätzlichen Ergebnisbestand.

### 29.2 Primärliteratur zur mathematischen Einordnung

Die folgenden Arbeiten belegen bekannte Gegenstände und Methoden. Sie beweisen nicht automatisch die TFPT spezifischen neuen Koeffizienten oder ihre physische Interpretation.

**[L1]** Huangjun Zhu, Richard Kueng, Markus Grassl, David Gross: *The Clifford group fails gracefully to be a unitary 4-design*. arXiv:1609.08172. Allgemeiner Hintergrund zu vierten Cliffordmomenten und zusätzlichen Stabilisatorsektoren.

**[L2]** Gabriele Nebe, E. M. Rains, N. J. A. Sloane: *The invariants of the Clifford groups*. arXiv:math/0001038. Zusammenhang von Clifford Invarianten und vollständigen Gewichtspolynomen selbstdualer Codes.

**[L3]** David Eklund: *Curves on Heisenberg invariant quartic surfaces in projective 3-space*. arXiv:1010.4058. Klassische Heisenberg Invarianten und Igusa Geometrie.

**[L4]** Gilberto Bini, Bert van Geemen: *Geometry and Arithmetic of Maschke's Calabi-Yau Threefold*. arXiv:1110.0106. Insbesondere der Quotienten und Invariantenanschluss.

**[L5]** Sergey Bravyi, David P. DiVincenzo, Daniel Loss: *Schrieffer-Wolff transformation for quantum many-body systems*. arXiv:1105.0675. Rahmen kontrollierter effektiver Hamiltonoperatoren.

**[L6]** Michel Planat und Metod Saniga: *Pauli graph and finite projective lines/geometries*. arXiv:quant-ph/0703154. Endliche Geometrie der Pauli Kommutation. Ergänzend: Metod Saniga, Frédéric Holweck, Petr Pracna, *Veldkamp Spaces: From (Dynkin) Diagrams to (Pauli) Groups*, arXiv:1605.02001.

**[L7]** Ben Howard, John Millson, Andrew Snowden, Ravi Vakil: *A description of the outer automorphism of S6, and the invariants of six points in projective space*. arXiv:0710.5916. Einordnung der besonderen S₆ Klassen und Invariantenverbindungen.

**[L8]** A. Kay, D. Kaszlikowski, R. Ramanathan: *Optimal Cloning and Singlet Monogamy*. arXiv:0901.3626. Allgemeiner Monogamiekontext; die konkrete Fünferschranke wird in S2 auch direkt berechnet.

**[L9]** Andrew Steane: *Multiple Particle Interference and Quantum Error Correction*. arXiv:quant-ph/9601029. Ursprung der verwendeten siebenstelligen Quantenkodierung.

**[L10]** John C. Baez, John Huerta: *The Algebra of Grand Unified Theories*. arXiv:0904.1556. Äußere Algebren und bekannte vereinheitlichte Materiedarstellungen.

**[L11]** Howard Barnum, Emanuel Knill: *Reversing quantum dynamics with near-optimal quantum and classical fidelity*. arXiv:quant-ph/0004088. Hintergrund der verwendeten Transpose beziehungsweise Petz Rückabbildung.

**[L12]** Bryan Eastin, Emanuel Knill: *Restrictions on Transversal Encoded Quantum Gate Sets*. arXiv:0811.4262. Die hier verwendeten gekoppelten Paar und Dreierkontrollen sind nicht transversal; es wird kein Widerspruch zu diesem Satz behauptet.

**[L13]** Jianxin Chen, Zhengfeng Ji, Bei Zeng, D. L. Zhou: *From Ground States to Local Hamiltonians*. arXiv:1110.6583. Hintergrund zum Zusammenhang von Marginaldaten und lokalen Grundzustandsbedingungen.

### 29.3 Reichweite der Literaturprüfung

Bei der Konsolidierung wurden die öffentlich auffindbaren Primärreferenzen zu Cliffordmomenten, Invarianten, Igusa, Schrieffer Wolff und Pauli Geometrie abgeglichen. Es wurde keine vollständige systematische Prioritätsrecherche zu sämtlichen denkbaren Kombinationen vorgenommen. Die im Haupttext als Quellenbefund bezeichneten weiteren Literaturanschlüsse stammen aus den vollständig gelesenen Projektberichten.

---

<a id="schlussbild"></a>
## 30. Schlussbild

Die einfache Geschichte lautet nicht mehr: „Viele schöne Zahlen ergeben zusammen eine Weltformel.“

Sie lautet:

> Eine konkrete diskrete Quellenstruktur erzeugt einen geschützten Informationsraum. Dessen Auslesung, erlaubte Antworten und Korrelationen sind mathematisch eng miteinander verbunden. Bestimmte Kopplungen binden solche Räume zu größeren Objekten, die wieder eine verwandte Informationsstruktur besitzen.

Das ist der belegte Kern.

```text
                 EIN GEMEINSAMER DISKRETER AUSGANGSPUNKT
                                  │
             ┌────────────────────┼────────────────────┐
             ▼                    ▼                    ▼
       E₈ Quellenbild       Quartischer Code      Hamming Schutz
                                  │
                  ┌───────────────┼────────────────┐
                  ▼               ▼                ▼
              Auslesung        Antwort          Igusa Geometrie
                  │               │                │
                  └───────────────┼────────────────┘
                                  ▼
                          konkrete Bindungen
                                  │
                                  ▼
                        rekursive Fünferstruktur
                                  │
                  gemeinsame physische Auswahl fehlt noch
                                  ⋮
                          Raumzeit und Materie
                                  ⋮
                              Gravitation
```

**Was sich geschlossen hat:** mehrere endliche algebraische und dynamische Teilkonstruktionen, einschließlich einer exakten Blockkodierung und einer expliziten Verbindung zweier Codekonstruktionen mit dem Bindungstensor.

**Was nicht durch Erzählung geschlossen werden darf:** die eindeutige globale Komposition, die physische Zeit, der räumliche Grenzwert, chirale Felder und gravitative Dynamik.

Die offene Gesamtlösung ist damit nicht auf eine weitere passende Zahl reduziert. Sie verlangt eine gemeinsame Kompositions und Herkunftsregel, welche die bereits vorhandenen exakten Bausteine zu derselben physikalischen Welt verbindet.

---

<a id="anhang-a"></a>
# Anhang A: Reproduktionsdaten der Konsolidierung

Die folgenden Daten stammen aus dem bei dieser Zusammenstellung ausgeführten A1 Prüfer. Die 230 Bedingungen sind nicht 230 unabhängige Entdeckungen. Ein großer Teil betrifft die 180 einzeln überprüften Routingfälle.


## A.1 Ergebnis des unabhängigen Prüfers

```json
{
  "check_count": 230,
  "incidence": {
    "nodes": 30,
    "edges": 45,
    "degree": 3,
    "spectrum": {
      "3": 1,
      "-3": 1,
      "2": 9,
      "-2": 9,
      "0": 10
    },
    "rank_N": 10,
    "girth": 8,
    "diameter": 4,
    "cycle_rank": 16,
    "routes": 180
  },
  "hamming": {
    "nodes": 6561,
    "edges": 52488,
    "degree": 16,
    "laplacian_multiplicities": [
      1,
      16,
      112,
      448,
      1120,
      1792,
      1792,
      1024,
      256
    ],
    "tau_max": 0.48768517112184967,
    "ds_max_per_n": 0.9261110267310978,
    "ds_max_n8": 7.408888213848782,
    "table": [
      {
        "n": 1,
        "vertices": 3,
        "degree": 2,
        "edges": 3,
        "ds_max": 0.9261110267310978
      },
      {
        "n": 2,
        "vertices": 9,
        "degree": 4,
        "edges": 18,
        "ds_max": 1.8522220534621956
      },
      {
        "n": 3,
        "vertices": 27,
        "degree": 6,
        "edges": 81,
        "ds_max": 2.7783330801932933
      },
      {
        "n": 4,
        "vertices": 81,
        "degree": 8,
        "edges": 324,
        "ds_max": 3.704444106924391
      },
      {
        "n": 5,
        "vertices": 243,
        "degree": 10,
        "edges": 1215,
        "ds_max": 4.630555133655489
      },
      {
        "n": 6,
        "vertices": 729,
        "degree": 12,
        "edges": 4374,
        "ds_max": 5.556666160386587
      },
      {
        "n": 7,
        "vertices": 2187,
        "degree": 14,
        "edges": 15309,
        "ds_max": 6.4827771871176845
      },
      {
        "n": 8,
        "vertices": 6561,
        "degree": 16,
        "edges": 52488,
        "ds_max": 7.408888213848782
      }
    ]
  },
  "source_archives": {
    "TFPT_Rekursion_6561_Test.zip": {
      "sha256": "c287ad60af0b234bbf94d969d0af35c545d8b15785615a58f70f42b189423768",
      "bytes": 44193
    },
    "TFPT_Rekursion_Quartik_Codes_20260926.zip": {
      "sha256": "297c5f6fde0dc40c07522310ba787479c74c6af144d09dfd20e5dc2af4993f84",
      "bytes": 38209
    }
  },
  "scope": "Exact finite incidence checks and symbolic spectrum; sparse H(8,3) topology and analytic diffusion. No many-body 5^6561 simulation, no geometry selection or continuum physics proved."
}
```

## A.2 Vollständige Kernprotokolle

Die folgenden Ausgaben wurden für diese Zusammenstellung erneut erzeugt. Numerische Näherungswerte und exakte rationale Werte sind in den Feldern getrennt bezeichnet. Die 60 Bedingungen des Dreierprogramms sind vollständig aufgeführt.

<details>
<summary>exploration_results.json</summary>

```json
{
  "matchings": [
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
  "K_spectrum": {
    "6": 1,
    "7/2": 9,
    "3/2": 15
  },
  "Gram_spectrum": {
    "12": 1,
    "2": 9,
    "0": 5
  },
  "rank_certificates": {
    "collective": {
      "rank": 24,
      "gram_determinant": "118949136087104392221226823334324257051984246587596941578463084544000000000",
      "gram_bound": 360000
    },
    "common_R": {
      "rank": 24,
      "gram_determinant": "16203331038469208522385436742240156250000",
      "gram_bound": 1500
    },
    "conjugate": {
      "rank": 24,
      "gram_determinant": "317035834045690853597177343939603039923809327159218192328504578054197402920978300636683232324721049600000",
      "gram_bound": 7290000
    }
  },
  "networks": {
    "bond": {
      "n": 2,
      "edges": [
        [
          0,
          1
        ]
      ],
      "max_K": 6.000000000000002,
      "degeneracy": 1,
      "max_K_per_edge": 6.000000000000002
    },
    "path3": {
      "n": 3,
      "edges": [
        [
          0,
          1
        ],
        [
          1,
          2
        ]
      ],
      "max_K": 9.386000936329388,
      "degeneracy": 5,
      "max_K_per_edge": 4.693000468164694
    },
    "triangle3": {
      "n": 3,
      "edges": [
        [
          0,
          1
        ],
        [
          1,
          2
        ],
        [
          0,
          2
        ]
      ],
      "max_K": 13.500000000000012,
      "degeneracy": 5,
      "max_K_per_edge": 4.500000000000004
    },
    "path4": {
      "n": 4,
      "edges": [
        [
          0,
          1
        ],
        [
          1,
          2
        ],
        [
          2,
          3
        ]
      ],
      "max_K": 14.783658759953997,
      "degeneracy": 1,
      "max_K_per_edge": 4.9278862533179995
    },
    "star4": {
      "n": 4,
      "edges": [
        [
          0,
          1
        ],
        [
          0,
          2
        ],
        [
          0,
          3
        ]
      ],
      "max_K": 13.500000000000018,
      "degeneracy": 1,
      "max_K_per_edge": 4.500000000000006
    },
    "cycle4": {
      "n": 4,
      "edges": [
        [
          0,
          1
        ],
        [
          1,
          2
        ],
        [
          2,
          3
        ],
        [
          0,
          3
        ]
      ],
      "max_K": 18.772001872658784,
      "degeneracy": 1,
      "max_K_per_edge": 4.693000468164696
    },
    "complete4": {
      "n": 4,
      "edges": [
        [
          0,
          1
        ],
        [
          0,
          2
        ],
        [
          0,
          3
        ],
        [
          1,
          2
        ],
        [
          1,
          3
        ],
        [
          2,
          3
        ]
      ],
      "max_K": 27.000000000000018,
      "degeneracy": 1,
      "max_K_per_edge": 4.500000000000003
    }
  },
  "monogamy_max": 1.2
}
```

</details>

<details>
<summary>exact_triangle_results.json</summary>

```json
{
  "checks": {
    "H4 self-adjoint metric": true,
    "triangle top eigenspace": true,
    "isometry metric": true,
    "compressed_R_0_site_0": true,
    "compressed_R_0_site_1": true,
    "compressed_R_0_site_2": true,
    "compressed_R_1_site_0": true,
    "compressed_R_1_site_1": true,
    "compressed_R_1_site_2": true,
    "compressed_R_2_site_0": true,
    "compressed_R_2_site_1": true,
    "compressed_R_2_site_2": true,
    "compressed_R_3_site_0": true,
    "compressed_R_3_site_1": true,
    "compressed_R_3_site_2": true,
    "compressed_R_4_site_0": true,
    "compressed_R_4_site_1": true,
    "compressed_R_4_site_2": true,
    "compressed_R_5_site_0": true,
    "compressed_R_5_site_1": true,
    "compressed_R_5_site_2": true,
    "compressed_R_6_site_0": true,
    "compressed_R_6_site_1": true,
    "compressed_R_6_site_2": true,
    "compressed_R_7_site_0": true,
    "compressed_R_7_site_1": true,
    "compressed_R_7_site_2": true,
    "compressed_R_8_site_0": true,
    "compressed_R_8_site_1": true,
    "compressed_R_8_site_2": true,
    "compressed_R_9_site_0": true,
    "compressed_R_9_site_1": true,
    "compressed_R_9_site_2": true,
    "compressed_R_10_site_0": true,
    "compressed_R_10_site_1": true,
    "compressed_R_10_site_2": true,
    "compressed_R_11_site_0": true,
    "compressed_R_11_site_1": true,
    "compressed_R_11_site_2": true,
    "compressed_R_12_site_0": true,
    "compressed_R_12_site_1": true,
    "compressed_R_12_site_2": true,
    "compressed_R_13_site_0": true,
    "compressed_R_13_site_1": true,
    "compressed_R_13_site_2": true,
    "compressed_R_14_site_0": true,
    "compressed_R_14_site_1": true,
    "compressed_R_14_site_2": true,
    "complete spectral polynomial": true,
    "spectrum dimensions": true,
    "ground dimension5": true,
    "triangle_loop_same_code_eigen15over4": true,
    "four_tensor_symmetric_0": true,
    "four_tensor_symmetric_1": true,
    "four_tensor_symmetric_2": true,
    "tetrahedron_triangle_0": true,
    "tetrahedron_triangle_1": true,
    "tetrahedron_triangle_2": true,
    "tetrahedron_triangle_3": true,
    "unique_tetrahedron_intersection_rank24": true
  },
  "D_denominator": 9,
  "D_norm_squared": "40/3",
  "triangle_spectrum": {
    "9/2": 11,
    "5": 18,
    "6": 25,
    "15/2": 42,
    "9": 10,
    "19/2": 9,
    "21/2": 5,
    "27/2": 5
  },
  "triangle_gap_in_J": "3",
  "compressed_R": "(7/12) R +(1/6) I",
  "compressed_Y": "(7/12) Y",
  "compressed_interblock_K": "(49/144) K +(19/12) I",
  "local_channel_spectrum": {
    "1": 1,
    "19/60": 5,
    "7/12": 9,
    "17/60": 10
  },
  "third_order_triangle_loop_code_eigenvalue": "15/4",
  "four_cell_top_K": "27",
  "four_cell_uniqueness_gram_determinant": "81022932193691788224111404588851001362533516683261178109254037538305820155454478253132583618463742739978584298672986521600000000000",
  "four_cell_uniqueness_columns": [
    0,
    6,
    18,
    24,
    12,
    20,
    22,
    21,
    23,
    16,
    15,
    17,
    11,
    10,
    1,
    13,
    19,
    14,
    2,
    4,
    3,
    8,
    9,
    7
  ]
}
```

</details>

<details>
<summary>source_hamming_results.json</summary>

```json
{
  "source_adapter_max_error": 4.949528148480988e-16,
  "distinct_matches": 15,
  "source_support_sizes": [
    4,
    12,
    12,
    12,
    24
  ],
  "RM_generalization": {
    "3": {
      "blocks": 2,
      "exact_counts": {
        "0": 16,
        "1": 48,
        "2": 48,
        "3": 48,
        "4": 96
      },
      "projection_probability": 0.3125,
      "conditional_probability_c0": 0.2
    },
    "4": {
      "blocks": 4,
      "exact_counts": {
        "0": 64,
        "1": 192,
        "2": 192,
        "3": 192,
        "4": 384
      },
      "projection_probability": 0.021267361111111112,
      "conditional_probability_c0": 0.7346938775510203
    },
    "5": {
      "blocks": 8,
      "exact_counts": {
        "0": 256,
        "1": 768,
        "2": 768,
        "3": 768,
        "4": 1536
      },
      "projection_probability": 0.0002451505517109268,
      "conditional_probability_c0": 0.9958803816516894
    }
  },
  "number_sites_exponent_log12over7_div_log3": 0.4906157579814925
}
```

</details>

<details>
<summary>code16_results.json</summary>

```json
{
  "count": 256,
  "weights": {
    "0": 1,
    "8": 198,
    "4": 28,
    "12": 28,
    "16": 1
  },
  "valid_word_pairs": 65536,
  "projection_probability": 0.043402777777777776,
  "coefficients_A_C": [
    0.027777777777777752,
    -0.08333333333333313
  ],
  "fit_residual": 2.5995053408730264e-16,
  "tetrahedron_ground_overlap_squared": 0.9599999999999999,
  "exact_integer_tensor_identity": true,
  "exact_CWE2_equality": true,
  "CWE2_distinct_monomials": 45,
  "projected_D_tensor": "(A-3 C)/36",
  "projected_E_average_tensor": "A/48",
  "difference_diagonal_polynomial": "-Igusa/48",
  "energy_tensor_combination": "T = 8*(2 E_average+3 D_projected)",
  "exact_projection_probability": "25/576",
  "exact_ground_overlap_squared": "24/25"
}
```

</details>

<details>
<summary>recursive_geometry_results.json</summary>

```json
{
  "doily": {
    "vertices": 15,
    "degree": 6,
    "edges": 45,
    "triangles": 15,
    "adjacency_eigenvalues": [
      -3.0,
      -3.0,
      -3.0,
      -3.0,
      -3.0,
      1.0,
      1.0,
      1.0,
      1.0,
      1.0,
      1.0,
      1.0,
      1.0,
      1.0,
      6.0
    ]
  },
  "natural_symmetric_recursion": [
    {
      "n": 1,
      "N": 3,
      "degree": 2,
      "ds_max": 0.9261110158084387,
      "tau_at_max": 0.48762324944910096,
      "ds_max_over_n": 0.9261110158084387
    },
    {
      "n": 2,
      "N": 9,
      "degree": 4,
      "ds_max": 1.8522220316168774,
      "tau_at_max": 0.48762324944910096,
      "ds_max_over_n": 0.9261110158084387
    },
    {
      "n": 3,
      "N": 27,
      "degree": 6,
      "ds_max": 2.778333047425316,
      "tau_at_max": 0.48762324944910096,
      "ds_max_over_n": 0.9261110158084387
    },
    {
      "n": 4,
      "N": 81,
      "degree": 8,
      "ds_max": 3.7044440632337547,
      "tau_at_max": 0.48762324944910096,
      "ds_max_over_n": 0.9261110158084387
    },
    {
      "n": 5,
      "N": 243,
      "degree": 10,
      "ds_max": 4.630555079042193,
      "tau_at_max": 0.48762324944910096,
      "ds_max_over_n": 0.9261110158084387
    },
    {
      "n": 6,
      "N": 729,
      "degree": 12,
      "ds_max": 5.556666094850632,
      "tau_at_max": 0.48762324944910096,
      "ds_max_over_n": 0.9261110158084387
    },
    {
      "n": 7,
      "N": 2187,
      "degree": 14,
      "ds_max": 6.482777110659072,
      "tau_at_max": 0.48762324944910096,
      "ds_max_over_n": 0.9261110158084388
    },
    {
      "n": 8,
      "N": 6561,
      "degree": 16,
      "ds_max": 7.4088881264675095,
      "tau_at_max": 0.48762324944910096,
      "ds_max_over_n": 0.9261110158084387
    }
  ],
  "analytic_return_probability": "P_n(t)=((1+2 exp(-3t))/3)^n",
  "analytic_spectral_dimension": "d_s=12 n t exp(-3t)/(1+2 exp(-3t))",
  "rg": {
    "lambda_Y": 0.5833333333333334,
    "lambda_K": 0.3402777777777778,
    "x_Y": 0.4906157579814925,
    "x_K": 0.9812315159629852,
    "b_if_inverse_Y": 1.7142857142857142,
    "d_H_if_b": 2.0382549555974983
  },
  "conclusion": "Natural fully S3-symmetric Cartesian recursion does not converge to finite spectral dimension; ds scales linearly with recursion depth. A crossing near 3 at finite n is not a dimension plateau."
}
```

</details>

## A.3 Sämtliche lokalen Routingfälle

Die Indizes laufen von 0 bis 14 und beziehen sich auf die vom eingebetteten Matchingprogramm erzeugte Reihenfolge. Eine Zeile `[p, L, q]` bedeutet: Der nicht auf Kontext L liegende Kanal p besitzt genau den kompatiblen Anschluss q in L. Diese Tabelle definiert keine darüber hinausgehende globale Verklebung.

<details>
<summary>15 Kontexte und 180 eindeutige Routen</summary>

```json
{
  "contexts": [
    [0, 1, 2],
    [0, 3, 6],
    [0, 11, 14],
    [1, 4, 9],
    [1, 8, 13],
    [2, 5, 12],
    [2, 7, 10],
    [3, 4, 5],
    [3, 10, 13],
    [4, 7, 14],
    [5, 8, 11],
    [6, 7, 8],
    [6, 9, 12],
    [9, 10, 11],
    [12, 13, 14]
  ],
  "routes": [
    [0, 3, 1],
    [0, 4, 1],
    [0, 5, 2],
    [0, 6, 2],
    [0, 7, 3],
    [0, 8, 3],
    [0, 9, 14],
    [0, 10, 11],
    [0, 11, 6],
    [0, 12, 6],
    [0, 13, 11],
    [0, 14, 14],
    [1, 1, 0],
    [1, 2, 0],
    [1, 5, 2],
    [1, 6, 2],
    [1, 7, 4],
    [1, 8, 13],
    [1, 9, 4],
    [1, 10, 8],
    [1, 11, 8],
    [1, 12, 9],
    [1, 13, 9],
    [1, 14, 13],
    [2, 1, 0],
    [2, 2, 0],
    [2, 3, 1],
    [2, 4, 1],
    [2, 7, 5],
    [2, 8, 10],
    [2, 9, 7],
    [2, 10, 5],
    [2, 11, 7],
    [2, 12, 12],
    [2, 13, 10],
    [2, 14, 12],
    [3, 0, 0],
    [3, 2, 0],
    [3, 3, 4],
    [3, 4, 13],
    [3, 5, 5],
    [3, 6, 10],
    [3, 9, 4],
    [3, 10, 5],
    [3, 11, 6],
    [3, 12, 6],
    [3, 13, 10],
    [3, 14, 13],
    [4, 0, 1],
    [4, 1, 3],
    [4, 2, 14],
    [4, 4, 1],
    [4, 5, 5],
    [4, 6, 7],
    [4, 8, 3],
    [4, 10, 5],
    [4, 11, 7],
    [4, 12, 9],
    [4, 13, 9],
    [4, 14, 14],
    [5, 0, 2],
    [5, 1, 3],
    [5, 2, 11],
    [5, 3, 4],
    [5, 4, 8],
    [5, 6, 2],
    [5, 8, 3],
    [5, 9, 4],
    [5, 11, 8],
    [5, 12, 12],
    [5, 13, 11],
    [5, 14, 12],
    [6, 0, 0],
    [6, 2, 0],
    [6, 3, 9],
    [6, 4, 8],
    [6, 5, 12],
    [6, 6, 7],
    [6, 7, 3],
    [6, 8, 3],
    [6, 9, 7],
    [6, 10, 8],
    [6, 13, 9],
    [6, 14, 12],
    [7, 0, 2],
    [7, 1, 6],
    [7, 2, 14],
    [7, 3, 4],
    [7, 4, 8],
    [7, 5, 2],
    [7, 7, 4],
    [7, 8, 10],
    [7, 10, 8],
    [7, 12, 6],
    [7, 13, 10],
    [7, 14, 14],
    [8, 0, 1],
    [8, 1, 6],
    [8, 2, 11],
    [8, 3, 1],
    [8, 5, 5],
    [8, 6, 7],
    [8, 7, 5],
    [8, 8, 13],
    [8, 9, 7],
    [8, 12, 6],
    [8, 13, 11],
    [8, 14, 13],
    [9, 0, 1],
    [9, 1, 6],
    [9, 2, 11],
    [9, 4, 1],
    [9, 5, 12],
    [9, 6, 10],
    [9, 7, 4],
    [9, 8, 10],
    [9, 9, 4],
    [9, 10, 11],
    [9, 11, 6],
    [9, 14, 12],
    [10, 0, 2],
    [10, 1, 3],
    [10, 2, 11],
    [10, 3, 9],
    [10, 4, 13],
    [10, 5, 2],
    [10, 7, 3],
    [10, 9, 7],
    [10, 10, 11],
    [10, 11, 7],
    [10, 12, 9],
    [10, 14, 13],
    [11, 0, 0],
    [11, 1, 0],
    [11, 3, 9],
    [11, 4, 8],
    [11, 5, 5],
    [11, 6, 10],
    [11, 7, 5],
    [11, 8, 10],
    [11, 9, 14],
    [11, 11, 8],
    [11, 12, 9],
    [11, 14, 14],
    [12, 0, 2],
    [12, 1, 6],
    [12, 2, 14],
    [12, 3, 9],
    [12, 4, 13],
    [12, 6, 2],
    [12, 7, 5],
    [12, 8, 13],
    [12, 9, 14],
    [12, 10, 5],
    [12, 11, 6],
    [12, 13, 9],
    [13, 0, 1],
    [13, 1, 3],
    [13, 2, 14],
    [13, 3, 1],
    [13, 5, 12],
    [13, 6, 10],
    [13, 7, 3],
    [13, 9, 14],
    [13, 10, 8],
    [13, 11, 8],
    [13, 12, 12],
    [13, 13, 10],
    [14, 0, 0],
    [14, 1, 0],
    [14, 3, 4],
    [14, 4, 13],
    [14, 5, 12],
    [14, 6, 7],
    [14, 7, 4],
    [14, 8, 13],
    [14, 10, 11],
    [14, 11, 7],
    [14, 12, 12],
    [14, 13, 11]
  ]
}
```

</details>

---

<a id="anhang-b"></a>
# Anhang B: Vollständige verfügbare Prüfprogramme dieses Zweigs

Diese sieben Programme sind Bestandteil dieser einen Markdown Datei. Die sechs Programme im Unterverzeichnis `TFPT_Rekursion` stammen unverändert aus dem bereitgestellten Archiv. `audit_summary.py` ist die ergänzende Konsolidierungsprüfung. Ihre Archivprüfsummen sind optionale Herkunftsdaten: Ohne Originalarchive werden diese Felder als nicht verfügbar markiert; die algebraischen und kombinatorischen Prüfungen benötigen sie nicht.

Die Programme bilden den hier erneut ausgeführten Rekursionszweig ab. Sie enthalten nicht die gesamten historischen Quellprogramme der früheren Berichte S0, S1 und S4. Deren Aufnahme als mathematische Quellen ist kein Anspruch, alle früheren Prüfmodule in dieser Datei auszuliefern.

Die Dateien werden ausschließlich durch die im nächsten Anhang enthaltene Extraktionshilfe geschrieben. Das Öffnen dieses Markdown Dokuments führt keinen Code aus. Python Programme sollten vor ihrer eigenen Ausführung gelesen werden.

## B.1 `TFPT_Rekursion/run_all.py`

<details>
<summary>Vollständiger Python Quelltext</summary>

<!-- TFPT_FILE_BEGIN: TFPT_Rekursion/run_all.py -->
```python
"""Rebuild all operators and certificates; no files outside this directory change."""
import os,subprocess,sys
from pathlib import Path
root=Path(__file__).resolve().parent
env=dict(os.environ,OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1')
flags=['-OO'] if sys.flags.optimize>=2 else []
for name in ['explore.py','exact_triangle.py','source_and_hamming.py','code16.py']:
    print('\n=== '+name+' ===',flush=True)
    subprocess.run([sys.executable,*flags,str(root/name)],cwd=root,env=env,check=True)
print('\nAll verification programs completed.',flush=True)
```
<!-- TFPT_FILE_END -->

</details>

## B.2 `TFPT_Rekursion/explore.py`

<details>
<summary>Vollständiger Python Quelltext</summary>

<!-- TFPT_FILE_BEGIN: TFPT_Rekursion/explore.py -->
```python
import itertools,json
from pathlib import Path
import numpy as np
import scipy.linalg as la
import sympy as s
out=Path(__file__).parent

def matchings(xs):
    if not xs:
        yield [];return
    a=xs[0]
    for j,b in enumerate(xs[1:],1):
        for rest in matchings(xs[1:j]+xs[j+1:]):yield [(a,b)]+rest
ms=list(matchings(list(range(6))))
E=np.vstack([np.eye(5,dtype=np.int64),-np.ones((1,5),dtype=np.int64)])
G=E.T@E;Gi6=6*np.eye(5,dtype=np.int64)-np.ones((5,5),dtype=np.int64)
I=np.eye(5,dtype=np.int64)
T=[]
for m in ms:
    t=np.zeros((6,6),dtype=np.int64)
    for a,b in m:t[a,b]=t[b,a]=1
    T.append((t@E)[:5])
R2=[I+t for t in T]
K4=sum(np.kron(r,r) for r in R2)
Gram4=np.array([[np.trace(a@b) for b in R2] for a in R2])
ke=s.Matrix(K4).eigenvals()
if ke!={24:1,14:9,6:15}:raise RuntimeError('K spectrum mismatch')
print('K spectrum',ke,flush=True)
ge=s.Matrix(Gram4).eigenvals()
if ge!={48:1,8:9,0:5}:raise RuntimeError('Gram spectrum mismatch')
print('Gram spectrum',ge,flush=True)
print('sumR',np.array_equal(sum(R2),12*I),flush=True)
# 24 traceless basis matrices. Any identity component is a trivial collective phase.
Xs=[]
for a,b in itertools.product(range(5),repeat=2):
    if a==b:continue
    x=np.zeros((5,5),dtype=np.int64);x[a,b]=1;Xs.append(x)
for a in range(4):
    x=np.zeros((5,5),dtype=np.int64);x[a,a]=1;x[4,4]=-1;Xs.append(x)
certs={}
for kind in ['collective','common_R','conjugate']:
    cols=[]
    for x in Xs:
        if kind=='common_R':
            cols.append(np.concatenate([(r@x-x@r).ravel() for r in R2]));continue
        A=np.kron(x,I)+np.kron(I,x) if kind=='collective' else 6*np.kron(x,I)-np.kron(I,Gi6@x.T@G)
        cols.append((K4@A-A@K4).ravel())
    C=np.array(cols).T
    # All entries and integer products stay below int64 overflow (explicit check).
    bound=int(C.shape[0])*int(np.max(abs(C)))**2
    if bound>=2**63:raise OverflowError('Gram bound')
    gram=C.T@C
    det=s.Matrix(gram.tolist()).det(method='domain-ge')
    if not det:raise RuntimeError('No full-rank certificate')
    certs[kind]={'rank':24,'gram_determinant':str(det),'gram_bound':bound}
    print(kind,'rank24 certified; det digits',len(str(det)),flush=True)
results={'matchings':ms,'K_spectrum':{'6':1,'7/2':9,'3/2':15},'Gram_spectrum':{'12':1,'2':9,'0':5},'rank_certificates':certs}
B=la.null_space(np.ones((1,6)));rn=[]
for m in ms:
    t=np.zeros((6,6))
    for a,b in m:t[a,b]=t[b,a]=1
    rn.append(B.T@((np.eye(6)+t)/2)@B)
kn=sum(np.kron(r,r) for r in rn)
np.savez(out/'operators.npz',R=np.array(rn),K=kn,B=B,R2_integer=R2,K4_integer=K4,metric=G)

def lift_pair(h,ij,n):
    d=5;ij=list(ij);others=[a for a in range(n) if a not in ij];order=ij+others
    ar=np.kron(h,np.eye(d**(n-2))).reshape([d]*(2*n));perm=[order.index(a) for a in range(n)]
    return ar.transpose(perm+[n+p for p in perm]).reshape((d**n,d**n))
networks={'bond':(2,[(0,1)]),'path3':(3,[(0,1),(1,2)]),'triangle3':(3,[(0,1),(1,2),(0,2)]),'path4':(4,[(0,1),(1,2),(2,3)]),'star4':(4,[(0,1),(0,2),(0,3)]),'cycle4':(4,[(0,1),(1,2),(2,3),(0,3)]),'complete4':(4,list(itertools.combinations(range(4),2)))}
results['networks']={}
for name,(n,edges) in networks.items():
    h=sum(lift_pair(kn,e,n) for e in edges);eig=la.eigvalsh(h)
    results['networks'][name]={'n':n,'edges':edges,'max_K':float(eig[-1]),'degeneracy':int(np.sum(abs(eig-eig[-1])<1e-8)),'max_K_per_edge':float(eig[-1]/len(edges))}
    print(name,results['networks'][name],flush=True)
omega=np.eye(5).reshape(-1)/np.sqrt(5);bell=np.outer(omega,omega)
mon=lift_pair(bell,(0,1),3)+lift_pair(bell,(1,2),3)
results['monogamy_max']=float(la.eigvalsh(mon)[-1]);print('Bell sum max',results['monogamy_max'],flush=True)
(out/'exploration_results.json').write_text(json.dumps(results,indent=2))
```
<!-- TFPT_FILE_END -->

</details>

## B.3 `TFPT_Rekursion/exact_triangle.py`

<details>
<summary>Vollständiger Python Quelltext</summary>

<!-- TFPT_FILE_BEGIN: TFPT_Rekursion/exact_triangle.py -->
```python
"""Exact certificates for the three-cell block in rational zero-sum coordinates."""
import itertools,json,math
from functools import reduce
from pathlib import Path
import numpy as np
import sympy as sp
p=Path(__file__).parent
z=np.load(p/'operators.npz');R2=z['R2_integer'];K4=z['K4_integer'];G=z['metric'];d=5;I=np.eye(d,dtype=np.int64);G3=np.kron(np.kron(G,G),G)

def lift(h,ij,n):
    ij=list(ij);order=ij+[a for a in range(n) if a not in ij]
    ar=np.kron(h,np.eye(d**(n-2),dtype=np.int64)).reshape([d]*(2*n));perm=[order.index(a) for a in range(n)]
    return ar.transpose(perm+[n+k for k in perm]).reshape(d**n,d**n)
H4=sum(lift(K4,e,3) for e in [(0,1),(0,2),(1,2)])
Gi6=6*I-np.ones((5,5),dtype=np.int64)
A6=np.stack([np.kron(Gi6.ravel(),I[:,i])+np.kron(I[:,i],Gi6.ravel())+np.einsum('ac,b->abc',Gi6,I[:,i]).ravel() for i in range(d)],axis=1)
q6=6*np.eye(6,dtype=np.int64)[:5,:]-np.ones((5,6),dtype=np.int64)
C1296=sum(np.outer(np.kron(np.kron(q,q),q),q@G) for q in q6.T)
Dnum=108*A6-C1296;den=648
common=reduce(math.gcd,[den]+[abs(int(x)) for x in Dnum.ravel()]);Dnum//=common;den//=common
print('D rational denominator',den,'max numerator',abs(Dnum).max(),flush=True)
checks={}
def check(name,v):
    if not bool(v):raise RuntimeError('FAILED '+name)
    checks[name]=True
check('H4 self-adjoint metric',np.array_equal(H4.T@G3,G3@H4))
check('triangle top eigenspace',np.array_equal(H4@Dnum,54*Dnum))
check('isometry metric',np.array_equal(3*Dnum.T@G3@Dnum,40*den**2*G))
# Exact response: D^sharp R D = 40/3 * (7/12 R + I/6), V=sqrt(3/40)*D
for ri,r2 in enumerate(R2):
    for site in range(3):
        rsite=np.kron(np.kron(r2,I),I) if site==0 else np.kron(np.kron(I,r2),I) if site==1 else np.kron(np.kron(I,I),r2)
        lhs=3*Gi6@Dnum.T@G3@rsite@Dnum
        rhs=20*den**2*(7*r2+4*I)
        check(f'compressed_R_{ri}_site_{site}',np.array_equal(lhs,rhs))
# Prove the complete spectrum via annihilating polynomial and spectral multiplicities.
evs=[18,20,24,30,36,38,42,54]
def safe_mm(a,b):
    # Use Python arbitrary precision if the conservative int64 bound is too large.
    if a.dtype==object or b.dtype==object or int(a.shape[1])*int(np.max(abs(a)))*int(np.max(abs(b)))>=2**63:
        return a.astype(object)@b.astype(object)
    return a@b
prod=np.eye(125,dtype=np.int64)
for v in evs:prod=safe_mm(prod,H4-v*np.eye(125,dtype=np.int64))
check('complete spectral polynomial',not np.any(prod))
mult={}
for v in evs:
    mat=np.eye(125,dtype=np.int64);div=1
    for u in evs:
        if u==v:continue
        mat=safe_mm(mat,H4-u*np.eye(125,dtype=np.int64));div*=v-u
    tr=sum(int(mat[i,i]) for i in range(125))
    if tr%div:raise RuntimeError('noninteger spectral multiplicity')
    mult[str(sp.Rational(v,4))]=tr//div
print('exact spectrum',mult,flush=True)
check('spectrum dimensions',sum(mult.values())==125)
check('ground dimension5',mult['27/2']==5)
L8=sum(np.kron(np.kron(r,r),r) for r in R2)
check('triangle_loop_same_code_eigen15over4',np.array_equal(L8@Dnum,30*Dnum))
# Four-cell invariant tensor is vectorization of D with its last input index raised.
Tnum=(Dnum@Gi6).reshape(5,5,5,5)
for a in range(3):check(f'four_tensor_symmetric_{a}',np.array_equal(Tnum,np.swapaxes(Tnum,a,a+1)))
# Each triple achieves 27/2, hence 6 edges have maximum27 exactly.
for omitted in range(4):
    order=[i for i in range(4) if i!=omitted]+[omitted]
    arr=Tnum.transpose(order).reshape(125,5)
    check(f'tetrahedron_triangle_{omitted}',np.array_equal(H4@arr,54*arr))

# Exact uniqueness of the four-cell ground state: intersection of two overlapping
# top triangle sectors has dimension1. Restrict second constraint to D tensor I.
embed=np.kron(Dnum,I)
arr=embed.reshape(5,125,25)
constraint=np.einsum('ab,ibc->iac',H4-54*np.eye(125,dtype=np.int64),arr).reshape(625,25)
# Numeric pivot selection, followed by an exact integer positive determinant.
from scipy.linalg import qr
_,_,pivot=qr(constraint.astype(float),pivoting=True,mode='economic')
sel=[int(x) for x in pivot[:24]]
small=constraint[:,sel]
certificate=sp.Matrix((small.T@small).tolist()).det(method='domain-ge')
check('unique_tetrahedron_intersection_rank24',certificate!=0)
# The known nonzero tensor supplies the matching upper rank bound24.

# Triangle channel full exact spectrum in rational matrix coordinates.
# Heisenberg channel = (3/(40*den^2))*G^-1 D.T G3 (X x I x I)D.
channel_num=[]
for a,b in itertools.product(range(5),repeat=2):
    x=np.zeros((5,5),dtype=np.int64);x[a,b]=1
    channel_num.append((Gi6@Dnum.T@G3@np.kron(np.kron(x,I),I)@Dnum).ravel())
Cn=np.array(channel_num).T;Cd=80*den**2
ce=sp.Matrix(Cn.tolist()).eigenvals()
ce={str(sp.Rational(int(k),Cd)):int(m) for k,m in ce.items()}
print('exact local channel eigenvalues',ce,flush=True)
np.savez(p/'exact_triangle_operators.npz',Dnum=Dnum,Dden=den,H4=H4,G=G,G3=G3,channel_num=Cn,channel_den=Cd,Tnum=Tnum)
res={'checks':checks,'D_denominator':den,'D_norm_squared':'40/3','triangle_spectrum':mult,'triangle_gap_in_J':'3','compressed_R':'(7/12) R +(1/6) I','compressed_Y':'(7/12) Y','compressed_interblock_K':'(49/144) K +(19/12) I','local_channel_spectrum':ce,'third_order_triangle_loop_code_eigenvalue':'15/4','four_cell_top_K':'27','four_cell_uniqueness_gram_determinant':str(certificate),'four_cell_uniqueness_columns':sel}
(p/'exact_triangle_results.json').write_text(json.dumps(res,indent=2))
print(len(checks),'exact checks passed',flush=True)
```
<!-- TFPT_FILE_END -->

</details>

## B.4 `TFPT_Rekursion/source_and_hamming.py`

<details>
<summary>Vollständiger Python Quelltext</summary>

<!-- TFPT_FILE_BEGIN: TFPT_Rekursion/source_and_hamming.py -->
```python
"""Independent source adapter and exact Hamming/RM block counts."""
import itertools,math,json
from pathlib import Path
from collections import Counter
import numpy as np
p=Path(__file__).parent
# Original four-ququart code from the supplied derivation.
words=list(itertools.product(range(4),repeat=4));supports=[]
for k in range(5):
    ss=[]
    for i,w in enumerate(words):
        co=Counter(w)
        if k==0 and len(co)==1:ss.append(i)
        if k in [1,2,3] and len(co)==2 and set(co.values())=={2} and (list(co)[0]^list(co)[1])==k:ss.append(i)
        if k==4 and len(co)==4:ss.append(i)
    supports.append(ss)
weights=[len(q) for q in supports]
V=np.zeros((256,5))
for k,ss in enumerate(supports):V[ss,k]=1/np.sqrt(weights[k])
I=np.eye(2);X=np.array([[0,1],[1,0]]);Y=np.array([[0,-1j],[1j,0]]);Z=np.diag([1,-1]);one=[I,X,Y,Z]
paulis=[np.kron(a,b) for a in one for b in one][1:]
W=np.array([[np.sqrt(3)/6,-.5,-.5,-.5,0],[np.sqrt(3)/6,-.5,.5,.5,0],[np.sqrt(3)/6,.5,-.5,.5,0],[np.sqrt(3)/6,.5,.5,-.5,0],[-np.sqrt(3)/3,0,0,0,np.sqrt(2)/2],[-np.sqrt(3)/3,0,0,0,-np.sqrt(2)/2]])
match=json.loads((p/'exploration_results.json').read_text())['matchings']
Q=np.eye(6)-np.ones((6,6))/6
rr=[]
for m in match:
    T=np.zeros((6,6))
    for a,b in m:T[a,b]=T[b,a]=1
    rr.append((np.eye(6)+T)/2-np.ones((6,6))/6)
errs=[];chosen=[]
for A in paulis:
    DV=np.zeros((256,5),complex)
    for site in range(4):
        op=np.array([[1.]])
        for j in range(4):op=np.kron(op,A if j==site else np.eye(4))
        DV+=op@V
    R=(DV.conj().T@DV)/16
    ar=W@R@W.T;ds=[np.linalg.norm(ar-r) for r in rr];chosen.append(int(np.argmin(ds)));errs.append(min(ds))
if len(set(chosen))!=15 or max(errs)>1e-12:raise RuntimeError('source adapter mismatch')
# RM(1,m) pairs split into L=2^(m-2) blocks over two free input bits.
# All projected words have a single common logical label. Count exactly.
ham={}
for m in [3,4,5]:
    points=list(itertools.product([0,1],repeat=m))
    code=[]
    for coef in itertools.product([0,1],repeat=m+1):
        code.append(tuple((coef[0]+sum(a*b for a,b in zip(coef[1:],x)))%2 for x in points))
    # Last two coordinates vary within each block.
    L=2**(m-2);counts=Counter()
    for c in code:
        for dd in code:
            w=[2*a+b for a,b in zip(c,dd)];labels=[]
            for block in range(L):
                t=w[4*block:4*block+4];co=Counter(t)
                if len(co)==1:k=0
                elif len(co)==2 and set(co.values())=={2}:k=list(co)[0]^list(co)[1]
                elif len(co)==4:k=4
                else:raise RuntimeError('word outside code support')
                labels.append(k)
            if len(set(labels))!=1:raise RuntimeError('non-diagonal logical word')
            counts[labels[0]]+=1
    expected={i:4**(m-2)*weights[i] for i in range(5)}
    if dict(counts)!=expected:raise RuntimeError('wrong counts')
    # unnormalized projected coefficients = 2^(m-5)*w^(1-L/2).
    coeff=[2.**(m-5)*w**(1-L/2) for w in weights]
    prob=sum(x*x for x in coeff)
    ham[str(m)]={'blocks':L,'exact_counts':dict(counts),'projection_probability':prob,'conditional_probability_c0':coeff[0]**2/prob}
res={'source_adapter_max_error':max(errs),'distinct_matches':len(set(chosen)),'source_support_sizes':weights,'RM_generalization':ham,'number_sites_exponent_log12over7_div_log3':math.log(12/7)/math.log(3)}
(p/'source_hamming_results.json').write_text(json.dumps(res,indent=2));print(json.dumps(res,indent=2))
```
<!-- TFPT_FILE_END -->

</details>

## B.5 `TFPT_Rekursion/code16.py`

<details>
<summary>Vollständiger Python Quelltext</summary>

<!-- TFPT_FILE_BEGIN: TFPT_Rekursion/code16.py -->
```python
import itertools,collections,json
from pathlib import Path
import numpy as np, scipy.linalg as la
import sympy as sp
p=Path(__file__).parent
# Binary doubly-even self-dual length16 code: doubled even length8 code plus alternating coset.
C=[]
alt=np.tile([1,0],8)
for bits in itertools.product([0,1],repeat=8):
    if sum(bits)%2:continue
    row=np.repeat(bits,2)
    C.extend([row,row^alt])
C=np.array(C,dtype=np.int64)
print('len',len(C),'weights',dict(collections.Counter(C.sum(axis=1))),flush=True)
print('self orthogonal',np.max((C@C.T)%2)==0,flush=True)
# support label lookup for four-ququart words
lookup=np.full(256,-1,dtype=int)
for w in itertools.product(range(4),repeat=4):
    c=collections.Counter(w);k=-1
    if len(c)==1:k=0
    elif len(c)==2 and set(c.values())=={2}:k=list(c)[0]^list(c)[1]
    elif len(c)==4:k=4
    lookup[np.dot(w,[64,16,4,1])]=k
counts=np.zeros((5,5,5,5),dtype=np.int64)
valid=0
for c in C:
    words=2*c[None,:]+C
    labels=lookup[words.reshape(256,4,4)@np.array([64,16,4,1])]
    good=np.all(labels>=0,axis=1);a=labels[good];np.add.at(counts,tuple(a.T),1);valid+=sum(good)
w=np.array([4,12,12,12,24]);norm=np.sqrt(np.einsum('a,b,c,d->abcd',w,w,w,w))
raw=counts/norm/256
print('valid',valid,'prob',np.sum(raw**2),'nnz',np.count_nonzero(counts),flush=True)
# Transform c-basis -> orthonormal H6 basis used in the other files.
W=np.array([[np.sqrt(3)/6,-.5,-.5,-.5,0],[np.sqrt(3)/6,-.5,.5,.5,0],[np.sqrt(3)/6,.5,-.5,.5,0],[np.sqrt(3)/6,.5,.5,-.5,0],[-np.sqrt(3)/3,0,0,0,np.sqrt(2)/2],[-np.sqrt(3)/3,0,0,0,-np.sqrt(2)/2]])
B=np.load(p/'operators.npz')['B'];U=B.T@W
r=np.einsum('ia,jb,kc,ld,abcd->ijkl',U,U,U,U,raw,optimize=True)
I=np.eye(5);A=np.einsum('ij,kl->ijkl',I,I)+np.einsum('ik,jl->ijkl',I,I)+np.einsum('il,jk->ijkl',I,I)
C4=sum(np.einsum('a,b,c,d->abcd',q,q,q,q) for q in B)
D=A-2*C4
coef=la.lstsq(np.stack([A.ravel(),C4.ravel()],axis=1),r.ravel())[0]
print('coeff A,C',coef,'res',la.norm(r-coef[0]*A-coef[1]*C4),flush=True)
print('ground overlap squared',abs(np.vdot(r,D))**2/np.vdot(r,r)/np.vdot(D,D),flush=True)
np.savez(p/'code16_operators.npz',counts=counts,raw=raw,transformed=r)
res={'count':len(C),'weights':{str(k):int(v) for k,v in collections.Counter(C.sum(axis=1)).items()},'valid_word_pairs':int(valid),'projection_probability':float(np.sum(raw**2)),'coefficients_A_C':[float(x) for x in coef],'fit_residual':float(la.norm(r-coef[0]*A-coef[1]*C4)),'tetrahedron_ground_overlap_squared':float(abs(np.vdot(r,D))**2/np.vdot(r,r)/np.vdot(D,D))}
(p/'code16_results.json').write_text(json.dumps(res,indent=2))

# Exact integer certificate for the projected length16 code tensor.
L=np.array([[1,-3,-3,-3,0],[1,-3,3,3,0],[1,3,-3,3,0],[1,3,3,-3,0],[-2,0,0,0,6],[-2,0,0,0,-6]],dtype=np.int64)
Cscaled9=sum(np.einsum('a,b,c,d->abcd',q,q,q,q) for q in L)
Ascaled=np.zeros((5,5,5,5),dtype=np.int64)
for a,b,c,d in itertools.product(range(5),repeat=4):
    if a==b and c==d:Ascaled[a,b,c,d]+=w[a]*w[c]
    if a==c and b==d:Ascaled[a,b,c,d]+=w[a]*w[b]
    if a==d and b==c:Ascaled[a,b,c,d]+=w[a]*w[b]
if not np.array_equal(27*counts,192*Ascaled-64*Cscaled9):raise RuntimeError('exact code16 tensor identity failed')
# Verify the full genus2 complete weight enumerator, not only the ordinary weights.
pts=list(itertools.product([0,1],repeat=3));C8=[]
for co in itertools.product([0,1],repeat=4):
    C8.append(tuple((co[0]+sum(a*b for a,b in zip(co[1:],x)))%2 for x in pts))
C88=np.array([a+b for a in C8 for b in C8],dtype=np.int64)
def cwe2(code):
    result=collections.Counter()
    for a in code:
        words=2*a[None,:]+code
        for row in np.stack([np.sum(words==i,axis=1) for i in range(4)],axis=1):
            result[tuple(int(x) for x in row)]+=1
    return result
cwD=cwe2(C);cwE=cwe2(C88)
if cwD!=cwE:raise RuntimeError('genus2 cwe differ')
# Exact TypeII properties: closed linear code from its explicit construction, |C|=256,
# self orthogonality implies self duality since length=16 and dim=8.
if len({tuple(x) for x in C})!=256 or np.any((C@C.T)%2) or np.any(C.sum(axis=1)%4):raise RuntimeError('TypeII check failed')
res['exact_integer_tensor_identity']=True
res['exact_CWE2_equality']=True
res['CWE2_distinct_monomials']=len(cwD)
res['projected_D_tensor']='(A-3 C)/36'
res['projected_E_average_tensor']='A/48'
res['difference_diagonal_polynomial']='-Igusa/48'
res['energy_tensor_combination']='T = 8*(2 E_average+3 D_projected)'
res['exact_projection_probability']='25/576'
res['exact_ground_overlap_squared']='24/25'
(p/'code16_results.json').write_text(json.dumps(res,indent=2))
print('Exact tensor identity and complete genus2 enumerator equality verified;',len(cwD),'monomials',flush=True)
```
<!-- TFPT_FILE_END -->

</details>

## B.6 `TFPT_Rekursion/recursive_geometry_test.py`

<details>
<summary>Vollständiger Python Quelltext</summary>

<!-- TFPT_FILE_BEGIN: TFPT_Rekursion/recursive_geometry_test.py -->
```python
import json, math, itertools
from pathlib import Path
import numpy as np
p=Path(__file__).parent
z=np.load(p/'operators.npz')
R2=z['R2_integer']
# Doily compatibility graph: commute iff matrix commutator vanishes
A=np.zeros((15,15),dtype=int)
for i,j in itertools.combinations(range(15),2):
    if np.array_equal(R2[i]@R2[j],R2[j]@R2[i]): A[i,j]=A[j,i]=1
assert np.all(A.sum(1)==6)
ev=np.linalg.eigvalsh(A)
# triangles
tris=[]
for i,j,k in itertools.combinations(range(15),3):
    if A[i,j] and A[i,k] and A[j,k]: tris.append((i,j,k))
assert len(tris)==15
assert all(sum(v in t for t in tris)==3 for v in range(15))
# Natural S3-symmetric recursion from triangle block + identity transport of a coarse edge:
# each level adds a K3 Cartesian factor => H(n,3), N=3^n, Laplacian spectrum 3k mult C(n,k)2^k.
def ds(n,t):
    q=math.exp(-3*t)
    return 12*n*t*q/(1+2*q)
def ret(n,t): return ((1+2*math.exp(-3*t))/3)**n
ts=np.logspace(-4,2,20000)
h=[]
for n in range(1,9):
    vals=np.array([ds(n,float(t)) for t in ts])
    im=int(vals.argmax())
    h.append({'n':n,'N':3**n,'degree':2*n,'ds_max':float(vals[im]),'tau_at_max':float(ts[im]),
              'ds_max_over_n':float(vals[im]/n)})
# RG scaling data from exact triangle certificate
lamY=7/12; lamK=49/144
xY=-math.log(lamY)/math.log(3); xK=-math.log(lamK)/math.log(3)
# If inverse attenuation is interpreted as a linear block scale, implied Hausdorff exponent
b=1/lamY; dH=math.log(3)/math.log(b)
res={'doily':{'vertices':15,'degree':6,'edges':int(A.sum()//2),'triangles':len(tris),'adjacency_eigenvalues':np.round(ev,12).tolist()},
     'natural_symmetric_recursion':h,
     'analytic_return_probability':'P_n(t)=((1+2 exp(-3t))/3)^n',
     'analytic_spectral_dimension':'d_s=12 n t exp(-3t)/(1+2 exp(-3t))',
     'rg':{'lambda_Y':lamY,'lambda_K':lamK,'x_Y':xY,'x_K':xK,'b_if_inverse_Y':b,'d_H_if_b':dH},
     'conclusion':'Natural fully S3-symmetric Cartesian recursion does not converge to finite spectral dimension; ds scales linearly with recursion depth. A crossing near 3 at finite n is not a dimension plateau.'}
(p/'recursive_geometry_results.json').write_text(json.dumps(res,indent=2))
print(json.dumps(res,indent=2))
```
<!-- TFPT_FILE_END -->

</details>

## B.7 `audit_summary.py`

<details>
<summary>Vollständiger Python Quelltext</summary>

<!-- TFPT_FILE_BEGIN: audit_summary.py -->
```python
"""Independent consolidation checks. Does not change the input archives."""
from pathlib import Path
from itertools import combinations
from collections import Counter, deque
import hashlib,json,math
import numpy as np
import scipy.sparse as ss
from scipy.special import lambertw
import sympy as sp
root=Path(__file__).resolve().parent
p=root/'TFPT_Rekursion'
R2=np.load(p/'operators.npz')['R2_integer']
checks={}
def check(name,ok):
    if not bool(ok): raise RuntimeError(name)
    checks[name]=True
A=np.zeros((15,15),dtype=np.int64)
for i,j in combinations(range(15),2):
    A[i,j]=A[j,i]=int(np.array_equal(R2[i]@R2[j],R2[j]@R2[i]))
contexts=[c for c in combinations(range(15),3) if all(A[i,j] for i,j in combinations(c,2))]
check('15_contexts',len(contexts)==15)
check('commutation_degree6',np.all(A.sum(1)==6))
N=np.array([[int(v in c) for c in contexts] for v in range(15)],dtype=np.int64)
B=np.block([[np.zeros((15,15),dtype=np.int64),N],[N.T,np.zeros((15,15),dtype=np.int64)]])
check('incidence_degree3',np.all(B.sum(1)==3))
check('incidence_edges45',B.sum()==90)
check('NNt_equals_3I_plus_A',np.array_equal(N@N.T,3*np.eye(15,dtype=int)+A))
vals=sp.Matrix(B).eigenvals()
check('exact_incidence_spectrum',vals=={sp.Integer(3):1,sp.Integer(2):9,sp.Integer(0):10,sp.Integer(-2):9,sp.Integer(-3):1})
routes=[]
for v in range(15):
    for ell,c in enumerate(contexts):
        if v in c: continue
        targets=[q for q in c if A[v,q]]
        check(f'route_{v}_{ell}',len(targets)==1)
        routes.append([v,ell,targets[0]])
check('180_routes',len(routes)==180)
# Girth and diameter by BFS. Exact combinatorial checks.
girth=1000; diameter=0
for origin in range(30):
    dist=[-1]*30; parent=[-1]*30; dist[origin]=0; q=deque([origin])
    while q:
        u=q.popleft()
        for v in np.flatnonzero(B[u]):
            if dist[v]<0:
                dist[v]=dist[u]+1;parent[v]=u;q.append(v)
            elif parent[u]!=v:
                girth=min(girth,dist[u]+dist[v]+1)
    check(f'connected_from_{origin}',min(dist)>=0)
    diameter=max(diameter,max(dist))
check('girth8',girth==8)
check('diameter4',diameter==4)
# Explicit H(8,3) sparse adjacency, not a many-body quantum Hilbert space.
n=8; size=3**n; rows=[];cols=[]
for v in range(size):
    place=1
    for _ in range(n):
        digit=(v//place)%3
        for nd in range(3):
            if nd!=digit: rows.append(v);cols.append(v+(nd-digit)*place)
        place*=3
AH=ss.csr_matrix((np.ones(len(rows),dtype=np.int8),(rows,cols)),shape=(size,size))
check('hamming_sparse_degree16',np.all(np.asarray(AH.sum(1)).ravel()==16))
check('hamming_sparse_symmetric',(AH-AH.T).nnz==0)
mult=[math.comb(n,k)*2**k for k in range(n+1)]
check('hamming_dimension_sum',sum(mult)==size)
check('hamming_laplacian_trace',sum(3*k*m for k,m in enumerate(mult))==2*n*size)
for tau in [1e-4,.01,.1,.5,1,3,10]:
    spectral=sum(m*math.exp(-3*k*tau) for k,m in enumerate(mult))/size
    product=((1+2*math.exp(-3*tau))/3)**n
    check(f'heat_trace_{tau}',abs(spectral-product)<1e-14)
w=float(lambertw(2/math.e).real)
tau=(1+w)/3
report={
 'checks':checks,'check_count':len(checks),
 'incidence':{'nodes':30,'edges':45,'degree':3,'spectrum':{str(k):int(v) for k,v in vals.items()},'rank_N':int(sp.Matrix(N).rank()),'girth':girth,'diameter':diameter,'cycle_rank':45-30+1,'routes':180},
 'hamming':{'nodes':size,'edges':AH.nnz//2,'degree':16,'laplacian_multiplicities':mult,'tau_max':tau,'ds_max_per_n':2*w,'ds_max_n8':16*w,'table':[{'n':j,'vertices':3**j,'degree':2*j,'edges':j*3**j,'ds_max':2*j*w} for j in range(1,9)]},
 'source_archives':{},
 'scope':'Exact finite incidence checks and symbolic spectrum; sparse H(8,3) topology and analytic diffusion. No many-body 5^6561 simulation, no geometry selection or continuum physics proved.'}
for name in ['TFPT_Rekursion_6561_Test.zip','TFPT_Rekursion_Quartik_Codes_20260926.zip']:
    # Archive hashes are optional provenance; the mathematical checks above
    # need only the matrices independently rebuilt by TFPT_Rekursion/run_all.py.
    candidates=(root/name, root.parent/name, Path('/mnt/data')/name)
    path=next((candidate for candidate in candidates if candidate.is_file()), None)
    if path is None:
        report['source_archives'][name]={'available':False}
    else:
        report['source_archives'][name]={'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'bytes':path.stat().st_size}
(root/'audit_summary.json').write_text(json.dumps(report,indent=2,ensure_ascii=False))
(root/'routing_table.json').write_text(json.dumps({'contexts':contexts,'routes':routes},indent=2))
ss.save_npz(root/'hamming_8_3_adjacency.npz',AH)
print(json.dumps({k:v for k,v in report.items() if k!='checks'},indent=2))
```
<!-- TFPT_FILE_END -->

</details>

## B.8 Prüfsummen der eingebetteten Programme

Die Prüfsummen beziehen sich auf UTF 8 Text mit genau einem abschließenden Zeilenumbruch, so wie die Extraktionshilfe ihn schreibt.

```json
{
  "TFPT_Rekursion/run_all.py": "f687a5ff5c421a0efa0f204caa4b1d7b0fffb41c544ce703eb164ed08ca18bdd",
  "TFPT_Rekursion/explore.py": "574cbd21b6b2b22b24e330a8db316d5c19ef7fe0b0c677e08a33fae417ad4858",
  "TFPT_Rekursion/exact_triangle.py": "ea12735a35bdc1f277b1466411a3003502616734703d34bcb9811c6c7ba82de9",
  "TFPT_Rekursion/source_and_hamming.py": "bebe15095e193e320f0b91f6a976eec6e86c238f0e7be6f634cb465850df617c",
  "TFPT_Rekursion/code16.py": "ccf4fde7d13890b5a0553071b2f8689b29109abc8162ab7e9406b58b0207cdb8",
  "TFPT_Rekursion/recursive_geometry_test.py": "749aee80a225cac4a6ab600fef001430efea28ab532615a2a48d4310ac4489a2",
  "audit_summary.py": "f7be101f7c96a106eb1dd26ddee975ef772f2d243dbae7081ac8a04dcaae39a0"
}
```

---

<a id="anhang-c"></a>
# Anhang C: Programme aus dieser Datei gewinnen und nachrechnen

## C.1 Extraktionshilfe

Den folgenden Code als `extract_tfpt.py` speichern. Er liest die ausdrücklich markierten Python Blöcke aus dieser Markdown Datei und legt sie in einem neuen Arbeitsverzeichnis ab. Vorhandene abweichende Dateien werden ohne `--overwrite` nicht überschrieben. Er prüft Pfade und Python Syntax, führt aber kein extrahiertes Programm aus. Für die Extraktionshilfe wird Python 3.10 oder neuer verwendet.

```python
"""Extract the explicitly embedded Python files from the TFPT Markdown report.

This utility writes files only. It does not execute extracted code.
Example:
    python extract_tfpt.py TFPT_Gesamtdokumentation.md tfpt_pruefung
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path, PurePosixPath

PATTERN = re.compile(
    r"<!-- TFPT_FILE_BEGIN: ([^\r\n]+) -->\s*"
    r"```python\r?\n(.*?)\r?\n```\s*"
    r"<!-- TFPT_FILE_END -->",
    flags=re.DOTALL,
)


def extract(markdown: Path, destination: Path, *, overwrite: bool = False) -> int:
    text = markdown.read_text(encoding="utf-8")
    matches = PATTERN.findall(text)
    if not matches:
        raise ValueError("Keine markierten Python Dateien gefunden.")
    root = destination.resolve()
    root.mkdir(parents=True, exist_ok=True)
    pending: list[tuple[Path, str]] = []
    seen: set[Path] = set()
    for name, code in matches:
        relative = PurePosixPath(name)
        if relative.is_absolute() or ".." in relative.parts or relative.suffix != ".py":
            raise ValueError(f"Unzulaessiger relativer Programmpfad: {name!r}")
        target = root.joinpath(*relative.parts).resolve()
        if not target.is_relative_to(root):
            raise ValueError(f"Programmpfad verlaesst das Zielverzeichnis: {name!r}")
        if target in seen:
            raise ValueError(f"Doppelter Programmpfad: {name!r}")
        seen.add(target)
        data = code + "\n"
        compile(data, str(target), "exec")  # Syntax validation; no execution.
        if target.exists() and not overwrite:
            if not target.is_file() or target.read_text(encoding="utf-8") != data:
                raise FileExistsError(f"Vorhandene abweichende Datei: {target}")
        pending.append((target, data))
    for target, data in pending:
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(data, encoding="utf-8")
    return len(pending)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("markdown", type=Path)
    parser.add_argument("destination", type=Path)
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args()
    count = extract(args.markdown, args.destination, overwrite=args.overwrite)
    print(f"{count} Python Dateien geschrieben; kein Programm ausgefuehrt.")


if __name__ == "__main__":
    main()
```

## C.2 Beispielaufrufe

Dateinamen mit Leerzeichen müssen in Anführungszeichen gesetzt werden. Die folgende Reihenfolge erzeugt zuerst die benötigten Matrizen, prüft dann die ursprüngliche Geometrieausgabe und schließlich die zusätzliche Inzidenz und Routingkontrolle.

```bash
python extract_tfpt.py TFPT_Gesamtdokumentation_Code_Quartik_Rekursion_2026-09-26.md tfpt_pruefung
python -m pip install numpy scipy sympy
cd tfpt_pruefung
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python TFPT_Rekursion/run_all.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -OO TFPT_Rekursion/run_all.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python TFPT_Rekursion/recursive_geometry_test.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python audit_summary.py
```

Die vorangestellte Schreibweise für Umgebungsvariablen gehört zu einer Unix Shell. In PowerShell können stattdessen vorab `$env:OPENBLAS_NUM_THREADS="1"` und `$env:OMP_NUM_THREADS="1"` gesetzt und danach die gleichen `python` Aufrufe verwendet werden.

Für einen eigenen Bytevergleich der normalen und optimierten Ausführung die vier `*_results.json` Dateien nach dem ersten Lauf separat sichern. Der zweite Lauf schreibt sie erneut. Die in Kapitel 28 dokumentierte Bytegleichheit wurde mit zwei tatsächlich getrennt gesicherten Ergebnissätzen geprüft.

## C.3 Erwartete Prüfausgaben

Der Hauptlauf beendet alle vier Programme ohne ausgelöste Prüfexception. Das Dreierprotokoll enthält 60 erfolgreiche Bedingungen. `audit_summary.py` meldet `check_count: 230`, `routes: 180`, `nodes: 6561`, `edges: 52488` für H(8,3) sowie `ds_max_n8: 7.408888213848782` innerhalb der dargestellten numerischen Genauigkeit.

Die erzeugte Datei `hamming_8_3_adjacency.npz` ist die dünn besetzte Adjazenzmatrix eines gewählten kombinatorischen Graphen. Sie ist keine Speicherung des Quantenzustands von 6561 Fünferzellen. `routing_table.json` enthält die im Anhang A wiedergegebenen endlichen Anschlüsse. Die Programme erzeugen ihre Arbeitsdateien nur in den angegebenen lokalen Verzeichnissen.

Auch die Extraktion aus dieser fertigen Markdown Datei wurde getestet: Alle sieben Programmdateien wurden in ein separates Verzeichnis geschrieben, der Hauptlauf und beide Geometrieprüfer ausgeführt. Die vier zentralen Ergebnisdateien stimmen byteweise mit dem zuvor geprüften Arbeitslauf überein.

Ein erfolgreicher Lauf bestätigt die dargestellten endlichen Rechnungen. Er beweist weder die physische Auswahl der Modellannahmen noch eine vollständige Raumzeit oder Quantengravitation.

---

**Ende der konsolidierten Gesamtdokumentation.**
