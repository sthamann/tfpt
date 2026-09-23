# Arithmetik, Quantenchaos und Geometrie: ein Atlas tatsächlich tragender Übersetzungen

Stand: 10. September 2026. Unabhängige Literaturprüfung anhand der unten verlinkten Originalarbeiten und von Autoren verfassten Darstellungen ihrer eigenen Ergebnisse. Die gelesenen Stellen stehen in `sources.json`. Historische Ergebnisstände werden nicht als vollständiger heutiger Forschungsstand ausgegeben. Die TFPT-Anschlüsse sind ausdrücklich Forschungsvorschläge; in dieser Teilprüfung wurde kein TFPT-Operator mit einem Literaturmodell identifiziert.

Der gemeinsame Mechanismus ist in vielen Fällen bereits bekannt: **Einzelne unzerlegbare Objekte und ihre Wiederholungen werden durch eine erzeugende Funktion erfasst; eine Spurformel übersetzt diese Zählung in Operatoren und Spektren.** Ein zweiter Mechanismus übersetzt lokale Kongruenzdaten in Symmetrien, Darstellungen und geometrische Kohomologie. Diese Übersetzungen können Probleme tatsächlich lösen. Ihre Existenz bedeutet jedoch noch keine vollständige oder effizient berechenbare Äquivalenz beliebiger Probleme.

## Acht Kernfälle

| Fall | Tatsächlich übersetzte Objekte | Gesicherter Kern | Grenze der Aussage |
|---|---|---|---|
| 1 | Primzahlpotenzen ↔ Zeta-Nullstellen | Explizite Formeln mit korrekten Testfunktionen | Das gesuchte positive Hilbert-Pólya-System folgt daraus nicht |
| 2 | Normierte Nullstellenabstände ↔ GUE-Korrelationen | Montgomerys Satz unter RH, eingeschränkter Fourierbereich | Volle GUE-Statistik ist eine stärkere Vermutung; Numerik ist kein RH-Beweis |
| 3 | Klassisch chaotische Bahnen ↔ Quantenspektren | Semiklassische Beiträge periodischer Bahnen | Universelle Statistik verlangt Symmetrie- und Grenzwertkontrolle |
| 4 | Geschlossene Geodäten ↔ Laplace-Spektrum | Selbergs Spurformel; arithmetische Längenkorrelationen | Arithmetische Flächen zeigen gerade nicht generisch GUE/GOE |
| 5 | Ganzzahlige Torusabbildungen ↔ endliche unitäre Operatoren | Exakte Egorov-Identität; Hecke-Equidistribution | Die Quantisierung ist keine Gleichheit der gesamten klassischen und Quantenalgebra |
| 6 | Multiplikative Zahlenstruktur ↔ KMS-Thermodynamik | Bost–Connes-System, Zeta-Zustandssumme, Phasenübergang | Das ist eine konstruierte arithmetische Thermodynamik, keine identifizierte Raumzeit |
| 7 | Adelenklassen ↔ explizite Spurformel | Lokale und endliche semilokale Spurformeln | Die globale positive Identifikation bleibt die entscheidende Verpflichtung |
| 8 | Punktzählung über endlichen Körpern ↔ Frobenius-Spektrum | Kohomologische Spurformel und Weil-Schranken | Der Beweis für endliche Körper überträgt sich nicht automatisch auf Spec(Z) |

### 1. Warum Primzahlen als Frequenzen auftreten

Für Re(s)>1 gilt exakt

\[
-\frac{\zeta'(s)}{\zeta(s)}=\sum_p\sum_{r\ge1}(\log p)p^{-rs}.
\]

Eindeutige Primfaktorzerlegung erklärt das Eulerprodukt; logarithmische Ableitung erklärt die Wiederholungen und das Gewicht log p. Mit u=log x wird die multiplikative Skala additiv. Die expliziten Formeln verknüpfen die resultierende gewichtete Primzahlpotenzverteilung mit Nullstellen, Pol und archimedischem Beitrag. Die vollständige Nullstellenformulierung braucht RH nicht. Montgomery unterscheidet das ausdrücklich in seiner expliziten Formel. [Montgomery, §2, S. 185–186](https://www.extrabyte.info/paircor1.pdf)

Berry–Keating vergleichen diese Struktur mit periodischen Bahnen: Primzahl p entspricht hypothetisch einer primitiven Bahn, p^r ihrer r-fachen Wiederholung und log p deren Grundperiode. Dabei ist die Oszillationsperiode in der Spektralvariablen **2π/log p**, während die im Bahnvergleich benutzte Länge **log p** ist. Die Autoren nennen zwei konkrete Schwierigkeiten: Das Vorzeichen der Zeta-Beiträge passt nicht naiv zu wiederholten Maslov-Phasen; außerdem stimmt die exakte Primzahl-Amplitude nicht unmittelbar mit dem gewöhnlichen Stabilitätsdeterminanten überein. Die unsmoothe Primzahlsumme auf der kritischen Linie ist divergent. [Berry–Keating, §2, insbesondere (2.6), (2.14) und S. 243](https://michaelberryphysics.wordpress.com/wp-content/uploads/2013/06/berry307.pdf)

**Erhalten:** die getestete arithmetische Verteilung, sofern alle Terme und Konvergenzbedingungen mitgeführt werden. **Offen:** ein unabhängig definiertes selbstadjungiertes System, dessen vollständige spektrale Identität die richtigen Nullstellen erzwingt. **TFPT-Prüfung:** Gewichte, Wiederholungen, Vorzeichen und archimedischen Term vergleichen; eine Liste von log-p-Frequenzen allein reicht nicht.

### 2. Zeta-Nullstellen und GUE: Statistik ist eine schwächere Übersetzung

Montgomery beweist unter RH für den normierten Formfaktor im Bereich 0≤α<1 die führende Funktion α, mit einem zusätzlichen konzentrierten Diagonalterm. Für größere Fourierparameter formuliert er eine Vermutung; daraus ergibt sich der bekannte Paar-Kern 1−(sin(πu)/(πu))². Dyson identifizierte denselben Kern bei großen komplex-hermiteschen Zufallsmatrizen. Der Originaltext unterscheidet ausdrücklich Satz, Heuristik und Vermutung. [Montgomery, S. 181–184, 190](https://www.extrabyte.info/paircor1.pdf)

Odlyzko testete Abstandsstatistiken an 100.000 Anfangsnullstellen und an 100.000 Nullstellen ab Index 10^12+1. Die Übereinstimmung verbessert sich bei größeren Höhen; langreichweitige Abweichungen werden über Primzahlen erklärt. Das ist numerische Evidenz für Statistik, keine Herstellung eines Operators. [Odlyzko, Abstract, §§1–2](https://www-users.cse.umn.edu/~odlyzko/doc/arch/zeta.zero.spacing.pdf)

**Erhalten:** nach Normierung bestimmte Korrelationsstatistiken, nicht einzelne Zustände oder sämtliche Operationsantworten. **Offen:** die unbeschränkte Statistik und der vollständige spektrale Realisierungsbeweis. **TFPT-Prüfung:** GUE als Diagnose nur nach Entfaltung der mittleren Dichte, Symmetrietrennung und Kontrollmodellen; keine GUE-Übereinstimmung als Quellidentifikation verwenden.

### 3. Allgemeines Quantenchaos: der Mechanismus ist Interferenz

Bohigas–Giannoni–Schmit berichten 1984, dass die Fluktuationen des Quanten-Sinai-Billards mit dem **orthogonalen** Ensemble GOE verträglich sind. Hier unterscheidet sich die relevante Symmetrieklasse von der Zeta/GUE-Analogie. Der Originalartikel formuliert daraus eine Universalitätsvermutung. [BGS, Originalabstract](https://doi.org/10.1103/PhysRevLett.52.1)

Müller und Mitautoren leiten im semiklassischen Ansatz Beiträge zum spektralen Formfaktor aus Paaren periodischer Bahnen ab. Nahe Selbstbegegnungen erlauben fast gleiche Wirkungen und damit Interferenz; ihre kombinatorische Ordnung reproduziert die kleine-Zeit-Entwicklung der Zufallsmatrixvorhersage. Das ist ein konkreter Erklärungsmechanismus. Der Aufsatz kennzeichnet seine Grundlage als semiklassisch und lässt größere Zeiten ausdrücklich für weitere Arbeit offen. [Müller et al., (1)–(2), Anfang und Schluss](https://arxiv.org/pdf/nlin/0401021)

**Erhalten:** semiklassische, gemittelte Spektralkorrelationen unter den jeweiligen Voraussetzungen. **Offen:** ein Modellbeweis benötigt Kontrolle der verwendeten Approximationen und Grenzwerte. **TFPT-Prüfung:** Zunächst überhaupt eine native klassische Grenzdynamik, Beobachtbarenalgebra und Symmetrieklasse bestimmen. Klassische Instabilität plus Primzahlen sind noch keine vollständige Quantenbeschreibung.

### 4. Selberg und das arithmetische Gegenbeispiel zur pauschalen Chaosregel

Für eine kompakte hyperbolische Fläche ohne Rand verknüpft die Selberg-Spurformel exakt Laplace-Eigenwerte mit primitiven geschlossenen Geodäten und Wiederholungen. Bei Spitzen, elliptischen Punkten oder Rand kommen entsprechende Terme hinzu. In der modularen Situation übersetzt

\[
2\cosh(\ell/2)=|\operatorname{tr}M|
\]

eine hyperbolische ganzzahlige Matrix in eine geodätische Länge. Die ganzzahligen Spuren erzwingen starke Längenentartungen. Bogomolny–Leyvraz–Schmit untersuchen deshalb Poisson-artige Nahstatistik und arithmetische Fernoszillationen, obwohl die klassische Dynamik chaotisch ist. [BLS, §§1–2, (2.5), (2.9), (2.14)–(2.18)](https://arxiv.org/pdf/chao-dyn/9509019)

Manfred Peter beweist anschließend eine Eulerproduktformel für die Korrelation der gewichteten Geodätenmultiplizitäten. Er trennt explizit diesen bewiesenen zweiten Schritt von der schwierigen heuristischen Übertragung auf die vollständigen Eigenwertkorrelationen. Die Primzahlen treten in seinem Satz als lokale Kongruenzfaktoren auf. [Peter, Einleitung und Theorem](https://arxiv.org/pdf/math/0104234)

**Erhalten:** die Spuridentität beziehungsweise die konkret definierte Längenkorrelation. **Offen:** der vollständige Statistiktransfer folgt nicht schon aus der Spurformel. **TFPT-Prüfung:** Gleichheit von Spektren erst nach Prüfung versteckter kommutierender Hecke-artiger Operatoren beurteilen. Dieser Fall widerlegt die Schlussregel „chaotisch, also automatisch GUE“.

### 5. Quanten-Cat-Maps: eine tatsächlich exakte Dynamikübersetzung

Eine geeignete hyperbolische ganzzahlige Torusabbildung A wird auf einem N-dimensionalen Hilbertraum quantisiert. Für die festgelegte Quantisierung gilt exakt

\[
U_N(A)^{-1}\operatorname{Op}_N(f)U_N(A)=\operatorname{Op}_N(f\circ A).
\]

Kurlberg–Rudnick weisen auf die besondere Linearität hin, die diese exakte Egorov-Eigenschaft ermöglicht. Spektrale Entartungen hängen an der Ordnung von A modulo 2N; zusätzliche kommutierende Hecke-Operatoren machen die Arithmetik sichtbar. Für ihre Voraussetzungen beweisen sie Equidistribution aller gemeinsamen Hecke-Eigenzustände. Ein Satz über diese Zustände ist nicht automatisch ein Satz über jede Wahl innerhalb großer entarteter Eigenräume. [Kurlberg–Rudnick, (1.2), Theorem 1 und Remark 1.1](https://arxiv.org/pdf/chao-dyn/9901031)

Eine aktuelle Erweiterung beweist unter ihren Annahmen Gleichverteilung aller Eigenfunktionen höherdimensionaler Cat-Maps entlang einer Folge von N mit Dichte eins; nicht für beliebige N ohne Bedingungen. Ihre Beweise nutzen unter anderem Tensorzerlegungen und Kongruenzsummen. [Kurlberg–Ostafe–Rudnick–Shparlinski 2025, Abstract und §§2–4](https://www.math.tau.ac.il/~rudnick/papers/On_Quantum_Ergodicity_for_Higher_Dimensional_Cat_Maps.pdf)

**Erhalten:** die zeitliche Wirkung auf quantisierte Beobachtbare. **Offen für TFPT:** ein echter Intertwiner zwischen nativen Generatoren und einer solchen Abbildung, einschließlich Zustand und Zulässigkeitsbedingungen. **Nutzen:** Vorbild für eine überprüfbare Transformation; Primmoduln liefern lokale Körper und kontrollierbare Exponentialsummen, keine mysteriösen Zusatzkräfte.

### 6. Bost–Connes: Primzahlen organisieren eine bewiesene Thermodynamik

Auf ℓ²(N≥1) ist H|n⟩=(log n)|n⟩. Eindeutige Faktorisierung erlaubt die Interpretation als Besetzungszahlen von Primmoden mit Energien log p. Für β>1 ist

\[
\operatorname{Tr}(e^{-\beta H})=\zeta(\beta).
\]

Das vollständige Bost–Connes-System ergänzt die multiplikativen Verschiebungen um additive rationale Phasen. Es besitzt eine eindeutige KMS-Phase für 0<β≤1 und viele Extremalphasen für β>1, parametrisiert durch cyclotomische Einbettungen; die Galois-Symmetrie wirkt auf ihnen. **Die bloße unabhängige Prim-Bosonen-Algebra hat diese volle Symmetriebrechung noch nicht:** der Originaltext trennt sie vom späteren Hecke-System. [Bost–Connes, §2, Theorem 5, Theorem 25 und Ende §7](https://repo-archives.ihes.fr/FONDS_IHES/I_Prepublications/CONNES/1994-1998/M_95_38/M_95_38_web.pdf)

**Erhalten:** Multiplikation, rationale Phasen, Zeitentwicklung und die jeweils definierten KMS-Zustände. **Offen für TFPT:** Gleichheit der gesamten Algebra und des Zustands, nicht nur H∼log n. Bei einer nativen Energie log(content) können unendlich viele primitive Nullenergiemoden auftreten; die Zeta-Zustandssumme der einfachen Zahlenbasis darf dann nicht ungeprüft übernommen werden. Das Modell ist eine starke mathematische Erklärung arithmetischer Thermodynamik, aber identifiziert weder physikalische Temperatur noch Gravitation.

### 7. Connes: Arithmetik ist bereits geometrisch formuliert

Connes betrachtet den nichtkommutativen Quotienten der Adelen durch die multiplikative Wirkung des Zahlkörpers; die Idelklassengruppe wirkt darauf. Kritische Nullstellen erscheinen als fehlende Spektrallinien eines Absorptionsbildes, mögliche nichtkritische Nullstellen als Resonanzen. Die Vorzeichenfrage ist damit Teil der Konstruktion. Lokale und endliche semilokale Spurformeln werden bewiesen. Der Übergang zur globalen Spuridentität wird als RH-äquivalente Beweisaufgabe herausgearbeitet; in positiver Charakteristik wird die entsprechende Äquivalenz in Theorem 5 präzise formuliert und danach die Zahlkörperbehandlung erläutert. [Connes, Einleitung, §§III, V, VII–VIII](https://alainconnes.org/wp-content/uploads/selecta.ps-2.pdf)

**Erhalten:** lokale Beiträge der expliziten Formel sowie die spezifizierte Darstellung und ihre regulierten Spuren. **Offen:** die globale positive Identifikation. **TFPT-Prüfung:** Ein nativer endlicher oder semilokaler Positivitätssatz braucht einen expliziten, dichten globalen Testbereich und kontrollierten Grenzübergang. Der attraktive Gedanke „Arithmetik in Geometrie verwandeln“ ist hier schon realisiert; der nächste Durchbruch muss die zusätzliche globale Aussage beweisen.

### 8. Endliche Körper: das erfolgreiche Vorbild eines gelösten RH-Analogons

Für X über F_q werden die Zahlen #X(F_(q^n)) zu

\[
Z(X,t)=\exp\!\left(\sum_{n\ge1}\#X(\mathbb F_{q^n})\frac{t^n}{n}\right)
\]

zusammengefasst. Geschlossene Punkte sind die primitiven Frobenius-Orbits. Die kohomologische Spurformel macht daraus ein alternierendes Produkt endlicher Determinanten von Frobenius auf ℓ-adischen Kohomologieräumen. Delignes Satz für glatte projektive X sagt, dass die Eigenwerte in Grad i sämtlich komplexen Betrag q^(i/2) haben. Für Kurven liefert dies das RH-Analogon und konkrete Schranken für Punktzahlen. [Deligne, §1, (1.1)–(1.6)](https://www.numdam.org/item/PMIHES_1974__43__273_0.pdf)

**Erhalten:** alle Punktzahlen, Zeta-Faktoren und die passenden Frobenius-Spuren. **Warum es funktioniert:** Neben der Übersetzung existiert ein starker geometrischer Satz über die Lage der Eigenwerte. **TFPT-Prüfung:** Nach einem vollständigen Analogon dieser Zusatzstruktur suchen: nicht nur Zeta-Produkt oder endliche Monodromie, sondern ein begründeter Reinheits-/Positivitätssatz auf dem tatsächlich erforderlichen Raum. Das endliche-Körper-Ergebnis ist keine bewiesene Identifikation mit der Riemann-Zeta-Funktion über Q.

## Drei ergänzende Verbindungen

**Primzahlen und Knoten.** Morishita konstruiert gruppen- und kohomologische Analogien: Trägheit ↔ Meridian, Frobenius ↔ Longitude, verzweigte Zahlkörpererweiterung ↔ verzweigte Überlagerung. Unter angegebenen Bedingungen, etwa p,q≡1 mod 4, wird das Legendre-Symbol als mod-2-Verknüpfungszahl dargestellt. Bereits die lokalen Relationen unterscheiden sich: die Randtorusgruppe ist abelsch, die zahme lokale Galoisgruppe enthält die Frobeniuswirkung auf Trägheit. Somit ist dies keine kanonische Abbildung „jede Primzahl ist ein gewöhnlicher Knoten im selben S³“ mit Erhaltung beliebiger Probleme. **Prüfvorschlag:** native Verzweigungs-, Cup-Produkt- und Reziprozitätsdaten vergleichen. [Morishita, §§1–3, (1.2), (2.1)–(2.2)](https://arxiv.org/pdf/0904.3399)

**Fourier–Poisson/Tate.** Tates tatsächliche Übersetzung hebt Hecke-Zeta-Funktionen zu Idelintegralen. Additive Fouriertransformation und Poisson-Summation liefern analytische Fortsetzung und Funktionalgleichung samt lokalen Faktoren. Hier ist der Nutzen bewiesen: Der Darstellungswechsel vereinfacht und verallgemeinert einen Beweis. Er bringt allein noch keine Nullstellenpositivität. **Prüfvorschlag:** zuerst tatsächliche Dualität, Haarmaß und lokale Fourierfaktoren der Quelle herstellen. [Tate, §§1.2, 4.2, Hauptsatz 4.4.1](https://sites.math.rutgers.edu/~alexk/2023S572/Tate1950.pdf)

**Langlands.** Die ursprüngliche Konstruktion verknüpft arithmetische/Galois-Daten und automorphe Darstellungen über abgestimmte lokale L-Faktoren. Die Leitfrage ist nicht, jede Zahl beliebig geometrisch umzubenennen, sondern diese lokal-globalen Entsprechungen einschließlich ihrer L-Funktionen nachzuweisen. Das Originalprogramm ist keine heute pauschal offene oder pauschal bewiesene Einzelvermutung; der Status hängt vom präzisen Feld, der Gruppe und der Korrespondenz ab. **Prüfvorschlag:** konkrete Hecke-/Frobenius-Daten in TFPT identifizieren und deren lokale charakteristische Polynome vergleichen. [Langlands, §§1, 7–8](https://publications.ias.edu/sites/default/files/problems-in-the-theory-of-automorphic-forms_rpl_8.pdf)

## Was der kleinste gemeinsame Nenner leisten kann

Die Literatur legt drei verschiedene Arten von Übersetzung nahe. **Operatorische Äquivalenz** kann die gesamten zulässigen Operationsantworten erhalten. **Spur- oder Zeta-Identität** erhält bestimmte globale Zählungen. **Statistische Universalität** erhält Grenzverteilungen nach Normierung. Diese Ebenen sind unterschiedlich stark. Aus einer gleichen Statistik lässt sich keine operatorische Äquivalenz folgern.

Eine einfache endliche Identität zeigt den häufigen Kern ohne neue Vermutung. Für eine endliche Matrix B und |u| klein gilt

\[
\det(I-uB)^{-1}=\exp\left(\sum_{n\ge1}\frac{u^n}{n}\operatorname{Tr}B^n\right).
\]

Begründung: Die logarithmische Ableitung beider Seiten ist Tr(B(I−uB)⁻¹), und beide haben bei u=0 den Wert eins. Ist B eine Übergangsmatrix eines endlichen gerichteten Graphen, zählt Tr(B^n) gewichtete geschlossene Wege mit markiertem Start. Gruppiert man sie nach primitiven zyklischen Klassen und Wiederholungen, erhält man das entsprechende Eulerprodukt. Das erklärt eine gemeinsame Form. Es beweist weder, dass Graph-„Primwege“ gewöhnliche Primzahlen sind, noch dass ein endliches rationales Zeta-Objekt die gesamte Riemann-Zeta-Funktion realisiert.

Für eine problemlösende Transformation müssen daher sechs Dinge explizit werden:

1. Welches Eingabeobjekt und welches Zielobjekt werden aus den verfügbaren Daten konstruiert?
2. Welche Operationen werden vollständig transportiert?
3. Welche konkrete Behauptung ist vor und nach der Übersetzung äquivalent?
4. Welcher starke Satz im Zielraum beweist diese Behauptung?
5. Wie wird eine Lösung wieder ausgelesen, ohne sie bereits in die Kodierung einzubauen?
6. Was kosten Kodierung, Zielrechnung, Genauigkeit und Rückübersetzung in der ursprünglichen Eingabelänge?

**Arbeitsfolgerung:** Der aussichtsreiche gemeinsame Gegenstand ist ein Prozess mit Algebra, Zustand, Dynamik und kontrollierten Darstellungen. Ein bloßer Raum oder ein gemeinsames Spektrum enthält weniger Information. Für RH fehlt bei vielen vorhandenen Transformationen gerade der globale Positivitäts-/Reinheitssatz; für Faktorisierung kann die teure Arbeit in der Konstruktion oder Auslese versteckt bleiben. Die Quellen bieten konkrete Prüfwerkzeuge, aber keine automatische Erledigung dieser Zusatzaufgaben oder der TFPT-Gravitation.

## Unabhängige Prüfung der endlichen Graph-Kontrolle des Hauptagenten

Diese algebraische Rechnung wurde unabhängig von dessen Programm geprüft. Für A=A*, q>0, T=A/√q und

\[
W=\begin{pmatrix}T&-I\\ I&0\end{pmatrix},\qquad
H=\begin{pmatrix}I&-T/2\\-T/2&I\end{pmatrix}
\]

gilt durch Blockmultiplikation W*HW=H. Auf einer A-Eigenrichtung λ sind die beiden H-Eigenwerte 1±λ/(2√q). Folglich ist H genau im strikt beschränkten Spektralbereich |λ|<2√q positiv definit. Dort ist H^(1/2)WH^(-1/2) unitär.

Am Rand λ=±2√q wird H singulär. Der entsprechende 2×2-Block von W besitzt einen nichttrivialen Jordanblock bei ±1: sein charakteristisches Polynom ist (z∓1)², aber W ist nicht ±I. Seine Potenzen wachsen, also kann keine andere positiv definite, von W erhaltene Form diese Grenzblöcke unitär machen. Die allgemeine nicht-strikte Ramanujan-Schranke allein reicht für diese konkrete H-Unitarisierung somit nicht. Bei (q+1)-regulären Graphen mit q>1 muss außerdem der triviale Eigenwert q+1, bei bipartiten Graphen auch −(q+1), vor dem Vergleich mit der nichttrivialen Schranke behandelt werden. Dies ist eine endliche Kontrollrechnung, kein RH-Beweis.
