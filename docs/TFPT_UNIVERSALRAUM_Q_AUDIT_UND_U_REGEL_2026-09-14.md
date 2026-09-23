# TFPT-Universalraum: Q-Audit und Kandidatenlösung der primitiven Regel \(U\)

Stand: 14. September 2026. Forschungsnotiz, **kein** load-bearing Claim.
NON-RH. Keine Promotion nach `verification/`, Ledger, Papers oder Website.

Quellen der geprüften Unterlagen:

- `Eingefügter Text.txt`
- `TFPT_Universalraum_Gesamtdarstellung_2026-09-14.pdf`
- `TFPT_Universalraum_LaTeX_Quellen_2026-09-14.zip`
- `TFPT_Q_Audit_2026-09-14.zip` / `TFPT_Q_Audit_2026-09-14.md`

Evidenzkonvention: *exakt* = Identität unter genannten Voraussetzungen;
*bedingt* = Folgerung mit zusätzlicher Ausführungsregel; *offen* = ungeschlossene
Herkunfts- oder Existenzfrage; *Gegenmodell* = explizites Gegenbeispiel gegen
eine behauptete eindeutige Auswahl.

---

## 0. Kernsatz

Der neue Vorschlag enthält einen tragfähigen Kern, aber noch keine Herleitung
der gesamten Physik aus einem einzigen \(Q\). Eine lokal definierte
Kompositionsregel kann ein konsistentes Modell liefern. Daraus folgt noch
nicht, dass die vollständige \(E_8\)-Klammer genau dieses Modell eindeutig
auswählt.

**Korrigierte Arbeitshypothese:** \(E_8\) ist sehr wahrscheinlich nicht die
vollständige primitive Dynamik. \(E_8\) ist die lokale Grammatik der
elementaren Vertizes. Die eigentliche primitive Struktur muss zusätzlich sagen,
wie solche Vertizes reversibel ausgeführt, unterschieden, besetzt und zu
Geschichten zusammengesetzt werden.

Nicht:

> Die \(E_8\)-Klammer erzeugt bereits eindeutig Graph, Energie, Vakuum,
> Gedächtnis und Raumzeit.

Sondern:

> Die \(E_8\)-Klammer liefert konkrete phasentreue Wechselwirkungsvertizes.
> Welche lokale Energie und welche größeren Prozesse daraus entstehen, hängt
> zusätzlich daran, welche Wege die physische Ausführung unterscheidbar hält
> und wie sie global zusammengesetzt wird.

---

# Teil I — Audit: Was bestätigt ist, was widerlegt ist, was gelöst wurde

## 1. Was die Überprüfung tatsächlich bestätigt

Die 210 Bedingungen des beigefügten Originalprüfers bestehen unverändert,
sowohl im normalen Lauf als auch mit deaktivierten Python-Assertions. Die
Ergebnisdateien stimmen bytegenau mit der mitgelieferten Datei überein.

Zusätzlich wurden die 248 Generatoren der \(E_8\)-Algebra einschließlich
Strukturkonstanten, Phasen, positiver kompakter Adjunktion und \(\mathbb{Z}_4\)-Gradierung
aufgebaut. Dabei wurden sämtliche 2.511.496 verschiedenen Basisdreier auf die
Jacobi-Identität geprüft. Die zugrunde liegenden Rechnungen verwenden ganze
Zahlen beziehungsweise exakt darstellbare dyadische Werte.

Das bestätigt insbesondere die richtigen Typen

\[
[g_1,g_1]\subseteq g_2,\qquad [g_1,g_3]\subseteq g_0
\]

sowie den Clebsch-Graphen und die lokale antisymmetrische Kanalstruktur.

Grenze: Das ist eine unabhängige endliche Konstruktion, kein erneuter Lauf des
ursprünglichen markierten Gauß-\(E_8\)-Adapters, der vollständigen 20-Qubit-Schaltungen
oder aller ursprünglichen Feldtheorierechnungen. Das Forschungsbuch
unterscheidet diese Ebenen selbst ausdrücklich.

## 2. Der globale Kern ist nicht die Summe der lokalen Kerne

Der eingefügte Text verwendet die richtige lokale Identität

\[
Q^\dagger Q = I-S = 2P_-
\]

und gewinnt daraus

\[
P_{\ker Q} = P_+.
\]

Anschließend wird daraus die Austauschenergie eines ganzen Graphen. Genau
dieser Übergang benötigt eine präzisere physische Ausführung.

### Was für eine einzelne Kante stimmt

Für jede der 40 Clebsch-Kanten wurde ein Kanal

\[
K_e:\mathbb{C}^4\otimes\mathbb{C}^4\longrightarrow\mathbb{C}^6
\]

aus den tatsächlichen Strukturkonstanten aufgebaut. Nach einer konsistenten
Wahl der lokalen Phasen gilt exakt:

\[
K_e^\dagger K_e = I-S_e.
\]

Damit ist der Kern dieses einzelnen Kantenkanals tatsächlich der
zehn-dimensionale symmetrische Raum.

### Was beim gemeinsamen Operator anders wird

Vier verschiedene Clebsch-Kanten benutzen dasselbe \(D_5\)-Vektorlabel und
denselben sechsdimensionalen Zielraum. Werden ihre Amplituden kohärent
zusammengeführt, können sie sich gegenseitig auslöschen.

| Ausführung der Kanäle | Eingangsdimension | Rang | Kerndimension |
|---|---:|---:|---:|
| Eine einzelne Kante | 16 | 6 | 10 |
| Alle 40 Kanten mit gemeinsam benutzten Zielräumen | 640 | 60 | 580 |
| Alle 40 Kanten mit im Ziel unterscheidbaren Kantenspuren | 640 | 240 | 400 |

Diese Tabelle betrifft den direkten Summenraum der Zweiteilchenkanäle, nicht
den vollständigen Tensorraum von 16 besetzten Orten.

Für den gesamten gleichgradigen Klammeroperator gilt:

\[
Q_{11}:g_1\otimes g_1\longrightarrow g_2,\qquad
\operatorname{rank} Q_{11}=60,\qquad
\dim\ker Q_{11}=4036.
\]

Der globale Kern enthält also erheblich mehr als lokale symmetrische
Paarzustände.

### Explizites Gegenbeispiel

Nimm zwei Kanten \(e\) und \(f\), die denselben Vermittlerkanal benutzen. Auf
beiden liegt derselbe antisymmetrische interne Zustand \(v\). Mit passenden
relativen Vorzeichen lässt sich ein Zustand bilden, für den

\[
K\psi=0,
\]

obwohl jeder seiner einzelnen Kantenanteile antisymmetrisch ist. Dann gilt
gleichzeitig:

\[
P_{\ker K}\,\psi=\psi,\qquad
\Bigl(\bigoplus_e P_e^+\Bigr)\psi=0.
\]

Der globale Kompositionsdefekt gibt diesem Zustand Energie. Die getrennten
lokalen Defekte geben ihm keine.

Das widerlegt nicht ein ausdrücklich definiertes Modell mit

\[
H=\sum_e P_{\ker K_e}.
\]

Es widerlegt die Gleichsetzung dieses Modells mit dem globalen Kern der
kohärenten Klammer. Die lokale Summe ist eine zusätzliche Ausführungsregel,
solange nicht erklärt ist, wodurch die einzelnen Vorgänge physisch getrennt
bleiben.

Die neue Hypothese muss deshalb beantworten: Welche Wege dürfen interferieren,
und welche Wege bleiben unterscheidbar? Das Registerproblem sitzt bereits im
Kopplungsmechanismus.

## 3. Lösung: Belegung kann die fehlende Unterscheidbarkeit liefern

Jeder Ort erhält die Zustände

\[
H_s=\mathbb{C}\lvert\emptyset\rangle\oplus\mathbb{C}^4.
\]

Er ist also leer oder mit genau einem der vier internen Zustände besetzt.
Hinzu kommen die 60 Vermittlermoden des gleichgradigen Zielsektors.

Ein erlaubter Vertex entfernt die beiden lokalen Belegungen einer Kante und
erzeugt den zugehörigen Vermittler. Die zwei zurückbleibenden Löcher markieren,
welche Kante benutzt wurde.

Im zunächst vollständig besetzten Raum muss ein zweiter Vertex genau diese
Löcher wieder füllen. Eine andere Kante kann das nicht leisten. Dadurch
verschwinden die unerwünschten Kreuzterme in zweiter Ordnung, und es folgt:

\[
H_{\mathrm{eff}}^{(2)}=-\frac{t^2}{\Delta}\sum_e K_e^\dagger K_e
=\frac{2t^2}{\Delta}\sum_e P_e^++\text{Konstante}.
\]

Damit ist die gewünschte positive relative Austauschkopplung unter diesen
Voraussetzungen hergeleitet:

\[
J_{\mathrm{eff}}=\frac{2t^2}{\Delta}.
\]

### In vierter Ordnung kommen echte Mehrkörperterme zurück

Die Lochstruktur löst das Problem der zweiten Ordnung. Sie macht gemeinsam
benutzte Vermittler aber nicht in allen Ordnungen harmlos.

Für zwei disjunkte Kanten mit denselben sechs bosonischen Vermittlermoden
entsteht im Raum ihrer beiden internen antisymmetrischen Sechserzustände:

\[
H_{\mathrm{eff}}^{(4)}=\frac{16t^4}{\Delta^3}\,P_{-\,\text{Paarlabels}}.
\]

Dieser Projektor vergleicht die gesamten internen Zustände zweier Paare. Er
ist ein wirklicher Vierträgerterm, nicht bloß eine Korrektur derselben
Zweiträgerkopplung.

Das Ergebnis gilt für die konkret angegebene gemeinsame Bosonvermittlung. Es
ist kein Universalwert aller Vermittlermodelle.

Wer daraus exakt nur ein Paarmodell gewinnen will, muss zusätzlich die höheren
Terme kontrollieren. Sie verschwinden nicht durch den Namen \(E_8\).

Auch die Energiehypothese selbst bleibt sichtbar: \(P_{\ker Q}\) ist eine
zulässige neue physikalische Regel, aber keine reine Algebrafolge. Der
ebenfalls positive Operator \(Q^\dagger Q\) würde im einzelnen Kanal die
entgegengesetzte Auswahl bevorzugen.

## 4. Geschlossen: Zweizellenmodell für alle Kopplungen

Modell: zwei vollständige Tetramerzellen mit interner Kopplung \(J>0\) und
genau einer Brücke

\[
H=H_A+H_B+\lambda P_{ab}^+,\qquad\lambda\ge 0.
\]

Im Buch endet der globale Grundzustandsnachweis bei \(\lambda<8J\). Stärkerer
Satz: Mit

\[
R=\sqrt{16J^2-2J\lambda+\lambda^2},\qquad
T=\sqrt{4J^2+\lambda^2}
\]

gilt für jede \(\lambda\ge 0\):

\[
E_0=\frac{4J+\lambda-R}{2},\qquad
E_1=\frac{6J+\lambda-T}{2}.
\]

Der Grundzustand ist eindeutig. Die exakte erste Energielücke lautet:

\[
\Delta_{\mathrm{gap}}=J+\frac{R-T}{2}>\frac{J}{2}.
\]

Bei \(\lambda=8J\) beträgt sie noch ungefähr \(0{,}876894\,J\). Für immer
stärkere Kopplung nähert sie sich \(J/2\), ohne bei endlicher Kopplung zu
verschwinden.

Warum das mehr als eine numerische Vermutung ist: Aus dem Tetramerspektrum
folgt eine Operatoruntergrenze für \(H_A+H_B\). Der daraus entstehende
Vergleichsoperator wurde auf dem gesamten Hilbertraum in kleine invariante
Blöcke zerlegt. Die niedrigsten Vergleichswerte werden in expliziten
Zustandsräumen des tatsächlichen Hamiltonoperators erreicht. Dadurch werden
Untergrenze und wirklicher Eigenwert identisch. Zusätzlich wurden alle 15
zulässigen \(\mathrm{SU}(4)\)-Darstellungsformen der acht Träger bei mehreren
Kopplungen numerisch gegengeprüft.

Grenze: Daraus folgt noch kein thermodynamischer Gap für beliebig viele Zellen.
Und es bleibt ein Modell aus zwei vollständigen Vierergraphen, nicht der
Clebsch-Graph.

## 5. Clebsch-Rechnung: Energie bestätigt, Dublettstruktur nicht

Der gesamte \(\mathrm{SU}(4)\)-Singulettmultiplizitätsraum des 16-Träger-Clebsch-Modells
hat Dimension 24.024. Für den niedrigsten Singulettzustand:

\[
E_{0,\mathrm{Singulett}}=11{,}045398337068384\,J.
\]

Das bestätigt den im Buch berichteten Wert. Auch die mittleren symmetrischen
Gewichte auf Kanten und Nichtkanten stimmen überein:

\[
\langle P_e^+\rangle\approx 0{,}27613495842671,
\qquad
\langle P_{ij}^+\rangle_{\mathrm{Nichtkante}}\approx 0{,}61193252078664.
\]

Bei der ersten angeregten Singulettenergie

\[
E\approx 11{,}5617621228025\,J
\]

wurden jedoch vier orthogonale numerische Eigenvektoren gefunden, jeweils mit
sehr kleinen Residuen. Die Tabelle auf der gedruckten Seite 18 nennt dafür ein
Dublett. Diese Zweifachangabe wird durch die Rechnung nicht bestätigt.

Präzise: Numerisch liegt mindestens eine Vierfachstruktur auf diesem Niveau
vor. Eine exakte algebraische Multiplizitätszertifizierung wurde nicht
erstellt. Die Rechnung umfasst den vollständigen Singulettsektor, nicht
sämtliche Nichtsingulettsektoren. Sie allein beweist daher noch nicht den
globalen Clebsch-Grundzustand gegenüber allen anderen Darstellungen.

## 6. Warum vier: Auswahlbeweis nur im angegebenen Sektor

Die Ergänzung ist sinnvoll: vollständige Antisymmetrie plus innere Neutralität
plus kleinste nichtleere Belegung.

Bei ausschließlich fundamentalen \(\mathrm{SU}(4)\)-Trägern wirkt das Zentrum
\(iI\) auf \(n\) Trägern als \(i^n\). Ein Singulett verlangt daher
\(n\equiv 0\pmod{4}\). Der kleinste nichtleere antisymmetrische Fall ist

\[
\Lambda^4\mathbb{C}^4\cong\mathbb{C}.
\]

Damit folgt tatsächlich genau \(\Omega\). Das ist ein sauberer bedingter
Auswahlbeweis.

Einschränkung: ausschließlich fundamentale Viererträger. Wer auch konjugierte
Träger als physische Population zulässt, erhält bereits

\[
4\otimes\overline{4}=1\oplus 15.
\]

Dann gibt es neutrale Zustände aus zwei Trägern. Der Quellenvertrag muss
festlegen, ob und warum dieser Sektor für die gesuchte Zelle ausgeschlossen
ist.

Für das große Netzwerk bleibt

\[
\ker\sum_e J_e P_e^+=\Lambda^N\mathbb{C}^4
\]

auf einem zusammenhängenden Graphen mit positiven Gewichten. Bei \(N=16\) ist
dieser Raum null. Eine vollständig besetzte zusammenhängende Clebsch-Ausführung
kann daher nicht überall kompositionsdefektfrei sein. Die Frustration ist
mathematisch unvermeidbar.

Konsistente Alternative: \(\Omega\) als lokale Verknüpfungsamplitude verwenden,
nicht als unverändert reine Dichtematrix jeder gekoppelten Region.

## 7. Präparation und Register lassen sich konkret verbessern

### Der Geschichtenoperator braucht einen vollständigen Normvertrag

Die vorgeschlagene Abbildung

\[
\lvert\psi\rangle\longmapsto\sum_e\lvert e\rangle Q_e\lvert\psi\rangle
\]

ist nicht automatisch normerhaltend. Dafür wäre nötig:

\[
\sum_e Q_e^\dagger Q_e=I.
\]

Die nackten Klammerkanäle erfüllen das nicht. Insbesondere vernichten sie ihre
Kernzustände. Eine Ereignisgeschichte daneben zu schreiben, beseitigt diesen
Informationsverlust nicht.

Konkrete Reparatur: Für die kohärente Kantenmatrix mit \(KK^\dagger=8I\) setze

\[
W=K/\sqrt{8},\qquad P=I-W^\dagger W.
\]

Dann ist

\[
V\psi=(W\psi)\oplus(P\psi)
\]

eine Isometrie. Der zweite Ausgang bewahrt genau die Information, die bei
alleiniger Anwendung von \(K\) verloren ginge. Im Prüfbericht steht außerdem
eine explizite unitäre Erweiterung.

Damit ist die reversible Ausführbarkeit konstruiert. Ihre eindeutige physische
Auswahl ist damit nicht bewiesen.

Die Echoausführungen „frisch“ und „behalten“ können Teile einer gemeinsamen
größeren Architektur sein. Sie benutzen aber unterschiedliche spätere Zugriffe
oder Kopplungen. Sie sind nicht einfach zwei passive Ansichten derselben
vollständig festgelegten Eingriffsfolge.

### Neuer exakter Filter erhöht die Präparationswahrscheinlichkeit

Der vollständige Tetramer besitzt die Energien

\[
H_{\mathrm{tet}}/J\in\{0,2,3,4,6\}.
\]

Daraus folgt eine exakte Fourier-Identität:

\[
F_0=\frac{1}{8}\sum_{r=0}^{7}\exp\Bigl(-i\pi r\frac{H_{\mathrm{tet}}}{4J}\Bigr)
=\lvert\Omega\rangle\langle\Omega\rvert.
\]

Bei Energie null addieren sich acht Einsen. Bei allen anderen vorkommenden
Energien löschen sich die acht Phasen exakt aus.

Eine Ausführung verwendet eine vorbereitete Uhr mit acht Zuständen,
kontrollierte Zeitentwicklung und eine Fourier-Auslesung. Der erfolgreiche
Ausgang implementiert \(A_4\) statt des bisherigen \((3/4)A_4\).

Für denselben Eingang \(\chi_0\) verbessert sich die Präparationswahrscheinlichkeit
von

\[
\frac{3}{32}\longrightarrow\frac{1}{6}.
\]

Wird der neue Filter auch am Ende eingesetzt:

| Ausführung | Bisherige Filter | Neuer exakter Filter |
|---|---|---|
| Register behalten | \(27/512\) | \(1/6\) |
| Frische Register, ursprünglicher Tick | \(459/16384\) | \(17/192\) |
| Frische Register, ausgeglichener Tick | \(27/1024\) | \(1/12\) |

Die bisherigen Werte und Filterfaktoren stammen aus dem dokumentierten
Originalprotokoll. Die neue Spalte gehört zu einer separaten Konstruktion,
nicht zu einer nachträglichen Änderung seiner eingefrorenen Vorhersage.

Die normierten Echowerte bleiben \(1\) gegen \(17/32\) beziehungsweise \(1\)
gegen \(1/2\).

Die Verbesserung ist nicht kostenlos: Kontrollierte Propagatoren, Hilfsuhr und
Auslesung müssen verfügbar sein. Ein Vorteil bei Gesamtgatterzahl oder
Hardwarefehlerrate ist nicht nachgewiesen. Auch das Nichtstabilizerhindernis
verschwindet nicht.

## 8. Raum und Zeit: fehlende Auswahl ausdrücklich nachgewiesen

### Zeit

Eine gemeinsame Skalierung \(H\mapsto E_*H\) kann die Wahl einer Energieeinheit
beschreiben. Sie beseitigt aber nicht dimensionslose Verhältnisse wie

\[
\lambda/J,\qquad t/\Delta,\qquad v_1/v_2.
\]

Ebenso liefert \(e^{-itH/\hbar}\) eine Dynamik mit einem reellen Parameter
\(t\). Eine lesbare innere Uhr benötigt zusätzlich einen geeigneten Zustand
und eine Anzeige. Das Zweizellensignal setzt beispielsweise einen
nichtstationären Produktanfang voraus; der stationäre Grundzustand zeigt es
nicht.

### Drei Raumdimensionen folgen nicht aus Grad fünf

Der Clebsch-Graph hat den Zyklusrang

\[
40-16+1=25.
\]

Aus demselben lokalen Graphen lassen sich unendliche Überlagerungen
konstruieren, die überall dieselben lokal bezeichneten Kanten und dieselben
internen Vertizes besitzen, aber großskalig wie

\[
\mathbb{Z},\qquad\mathbb{Z}^2,\qquad\mathbb{Z}^3,\qquad\mathbb{Z}^4
\]

wachsen. Konstruktion: Man wählt einen Spannbaum und ordnet ausgewählten
übrigen Kanten unabhängige Verschiebungen zwischen Graphkopien zu. Der lokale
Grad bleibt fünf; die globale Dimension hängt von dieser Verklebung ab.

Die universelle Baumüberlagerung besitzt das Ballvolumen

\[
\lvert B(r)\rvert=1+5\cdot\frac{4^r-1}{3},
\]

also exponentielles Wachstum.

Damit ist nachgewiesen: Dieselben lokalen Vertexdaten wählen noch keine
dreidimensionale globale Fortsetzung. Das sind Gegenmodelle für die
Konnektivitätsauswahl, nicht behauptete vollständige physikalische Theorien.

Die bekannte Propagatorbrücke bleibt richtig: Ein geeigneter kohärenter
Zweibandpol kann eine Lorentzform liefern. Aber Impulsraum, Grenzwert, Pole
und eine gemeinsame Kegelstruktur aller Sektoren müssen erst aus demselben
Modell entstehen.

## 9. Chirale Naht, drei Familien und Gravitation bleiben getrennte Aufgaben

### Die endliche Klammer ist noch keine chirale Stromalgebra

Für die Naht braucht man neben den endlichen Strukturkonstanten insbesondere
Moden, eine zentrale Erweiterung, ein Level, einen positiven Energiezustand
und eine chirale Ausführung. Die endlichen Nullmoden bestimmen diese
zusätzlichen Daten nicht.

Eine gewöhnliche \(\mathrm{SU}(4)\)-Kette mit linken und rechten Sektoren
ersetzt keine rein chirale \(E_8\)-Naht.

### Ein einfacher endlicher Diracoperator liefert nicht Index drei

Für einen endlichen chiralen Block

\[
D=\begin{pmatrix}0&A^\dagger\\A&0\end{pmatrix}
\]

mit gleich großen chiralen Räumen ist \(A\) quadratisch. Aus Rangnullität folgt

\[
\dim\ker A-\dim\ker A^\dagger=0.
\]

Ein Index drei benötigt zusätzliche Struktur: geeignete Topologie, Randdaten
oder eine anders aufgebaute chirale Regularisierung. Für freie lokale
translationsinvariante Gittermodelle schränkt der Satz von Nielsen–Ninomiya
die Nettochiralität ein.

### Gravitation benötigt einen wirklichen gravitativen Freiheitsgrad

Ein Lorentzkegel ist Kinematik. Für Gravitation fehlen weiterhin der positive
masselose Spin-2-Sektor, seine zwei Helizitäten, die passenden Eichidentitäten
und die universelle Kopplung.

Weinbergs Konsistenzargument schränkt die Kopplung eines bereits vorhandenen
masselosen Spin-2-Pols ein. Es erzeugt diesen Pol nicht aus einem beliebigen
Netzwerk. Connes’ kommutativer Rekonstruktionssatz setzt starke Spektralaxiome
voraus; eine passende endliche Matrix oder Dimensionszählung ist noch keine
Anwendung dieses Satzes.

## 10. Übrige Auswahlfragen und Zahlen

**Kontextgewichte.** Die symmetrische Familie

\[
K_a=aI+\frac{1-a}{6}(B-I)
\]

bleibt ein Gegenbeispiel gegen eine eindeutige Auswahl allein durch die
vorhandene Symmetrie. Eine zusätzliche Maximierung der Übergangsentropie unter
genau sieben zugelassenen Nachfolgern würde \(1/7\) eindeutig auswählen. Das
wäre eine vollständige bedingte Regel, aber ein zusätzliches Prinzip.

**Physikalischer Zustand.** Eine positive Algebra mit festgelegtem
Zustandsfunktional ermöglicht eine Rekonstruktion. Sie erklärt dadurch nicht,
warum genau dieses Funktional gewählt wird. Grundzustandsprinzip,
Präparationsmechanismus und Anfangsbedingung sind unterschiedliche Aussagen.

**Elektromagnetische Kopplung.** Der unveränderte Prüfer reproduziert

\[
\alpha^{-1}=137{,}0359992168407125035\ldots
\]

Die aufgerufene offizielle Tabelle enthält den datierten CODATA-Wert von 2022,

\[
137{,}035999177(21).
\]

Der Abstand beträgt rund \(1{,}897\) experimentelle Standardabweichungen. Eine
kontrollierte Theorieunsicherheit ist darin nicht enthalten. Die neue
\(Q\)-Konstruktion leitet die spezielle Gleichung für diese Zahl nicht her.
Ebenso repariert sie nicht automatisch die im Buch ausgewiesenen Spannungen
bei Leptonverhältnissen, der früheren Higgs-Linie, der einfachen
Inflationsamplitude oder den angenommenen Protonzerfallszweigen.

## 11. Gesamtstatus der acht Tore nach dem Audit

| Tor | Tatsächlicher Fortschritt | Noch nicht hergeleitet |
|---|---|---|
| T1 Primitive Quelle | Ausführbares endliches Belegungsmodell; versteckte Ausführungsdaten explizit | Warum gerade diese Träger, Belegung, Energie und Auslesung |
| T2 Chirale Naht | Vollständige endliche Klammer, Phasen und Adjunktion geprüft | Native Moden, Level, analytischer Grenzwert und chirale Ausführung |
| T3 3+1 Dimensionen | Konkrete Gegenmodelle zur Dimensionsauswahl | Ausgewählte globale Fortsetzung und gemeinsamer Ausbreitungskegel |
| T4 Chirales Standardmodell | Einfaches endliches Indexhindernis exakt bestimmt | Physischer Index, Spiegelentkopplung und wechselwirkendes Maß |
| T5 Wechselwirkung und Kontinuum | Zweizellenproblem für alle Kopplungen gelöst; Vermittlung bis zu einem konkreten Vierkörperterm untersucht | Kontrollierter gemeinsamer Vielzellen- und Kontinuumsgrenzwert |
| T6 Kopplungen und Neutrinos | Datierte Alpha-Rechnung reproduziert | Gemeinsame Herleitung von Kopplungen, Texturen und Skalen |
| T7 Gravitation | Notwendige dynamische Bedingungen präzisiert | Masseloser Spin-2-Sektor mit universeller Kopplung |
| T8 Zustand und Prozess | Reversible Erweiterung und besserer exakter Präparationsfilter konstruiert | Ursprung von Anfang, Reservoir, Kontrolle und Quellfunktional |

Nächster entscheidender Schritt des Audits: eine dieser Ausführungen
festlegen und ihre vollständige effektive Dynamik berechnen, statt zwischen
kohärentem Gesamtoperator, getrennten Kanten, Tetramer und Clebsch je nach
gewünschtem Ergebnis zu wechseln.

„Neu“ bedeutet dabei neu gegenüber den beigefügten Unterlagen, nicht eine
behauptete Erstentdeckung in der gesamten Literatur; eine externe Begutachtung
ist noch nicht erfolgt.

---

# Teil II — Kandidatenlösung: primitive Regel \(U\) statt \(Q\)

Die letzten Lücken schließen sich nicht dadurch, dass immer weitere
Eigenschaften direkt aus der endlichen \(E_8\)-Klammer gepresst werden. Die
stärkere Form des Forschungsbuchs verlangt bereits: Zustände, Operationen,
Zusammensetzung, Aufzeichnungen und Auslesungen müssen gemeinsam festgelegt
werden.

## 1. Die primitive Quelle sollte nicht \(Q\) sein, sondern eine reversible Ereignisregel \(U\)

Der bisherige Kandidat war

\[
Q(x,y)=[x,y]_{E_8}.
\]

Das war fast richtig, aber zu klein. Denn \(Q\)

- ist nicht unitär,
- hat einen großen Kern,
- kann verschiedene Kanten kohärent zusammenwerfen,
- enthält keine Besetzungsinformation,
- und sagt nicht, welche Geschichte später noch unterscheidbar bleibt.

Der richtige primitive Gegenstand wäre

\[
U:H_{\mathrm{matter}}\otimes H_{\mathrm{mediator}}\otimes H_{\mathrm{history}}
\longrightarrow
H_{\mathrm{matter}}\otimes H_{\mathrm{mediator}}\otimes H_{\mathrm{history}}
\]

mit

\[
U^\dagger U=I.
\]

Die \(E_8\)-Klammer bestimmt darin die erlaubten Vertizes und ihre relativen
Phasen, aber nicht allein die gesamte Zustandsentwicklung.

Upgrade:

\[
E_8\text{-Klammer}\longrightarrow\text{lokale Vertexamplitude}
\]

statt

\[
E_8\text{-Klammer}\;\stackrel{?}{=}\;\text{gesamte Physik}.
\]

Damit verschwindet das Gegenbeispiel aus Teil I: Zwei verschiedene Kanten
dürfen nur dann interferieren, wenn ihre vollständigen Endzustände
einschließlich Löcher und Geschichte identisch sind.

## 2. T1: Quellenvertrag

Für jeden elementaren Spinorort \(s\):

\[
H_s=\lvert\emptyset\rangle\oplus\mathbb{C}^4.
\]

Also: leer, oder genau einer der vier \(A_3\)-Zustände. Für jede erlaubte
\(E_8\)-Verbindung kommt ein Vermittlersektor hinzu.

Elementare Regel:

\[
\lvert a\rangle_s\lvert b\rangle_t\lvert 0\rangle_m\lvert 0\rangle_h
\longrightarrow
\sum_\mu C_{st;ab}^{\mu}\,
\lvert\emptyset\rangle_s\lvert\emptyset\rangle_t\lvert\mu\rangle_m
\lvert st,ab,\mu\rangle_h
\]

plus der exakt unitäre Rückweg.

Die Koeffizienten \(C_{st;ab}^{\mu}\) sind keine frei gewählten Kopplungen,
sondern die normierten \(E_8\)-Strukturkonstanten. Das History-Label speichert
\((s,t,a,b,\mu)\).

Damit enthält die Quelle gleichzeitig: Träger, \(\mathbb{Z}_4\)-Typ, Phasen,
Besetzung, Vermittler, Prozessgeschichte, reversible Rückentwicklung.

**Was hier neu gelöst wird.** Kantenlabels müssen nicht künstlich als
zusätzliche physikalische Quantenzahlen eingeführt werden. Die
zurückbleibende Lochkonfiguration \(\lvert\emptyset_s,\emptyset_t\rangle\)
ist selbst ein physikalisches Kantenlabel. Dadurch werden verschiedene
Vermittlungswege orthogonal, obwohl sie dasselbe \(g_2\)-Gewicht benutzen.
Das löst die offene Schwierigkeit, dass dasselbe Vektorlabel vier verschiedene
Kanten trägt.

## 3. Hamiltonoperator aus virtueller reversibler Dynamik

Die frühere Regel \(H=P_{\ker Q}\) wird nicht mehr fundamental gesetzt. Das
war elegant, aber eine zusätzliche Wahl. Energie soll aus virtueller
reversibler Dynamik entstehen.

Nenne die Vermittlerenergie \(\Delta\) und die Vertexamplitude \(t\). Dann
entsteht im niedrigen Belegungssektor:

\[
H_{\mathrm{eff}}^{(2)}=-\frac{t^2}{\Delta}\sum_e K_e^\dagger K_e.
\]

Da \(K_e^\dagger K_e=2P_-^{(e)}\), folgt nach einer konstanten
Energieverschiebung

\[
H_{\mathrm{eff}}^{(2)}=\frac{2t^2}{\Delta}\sum_e P_+^{(e)}.
\]

Damit kommen Graph, Vorzeichen und Austauschoperator aus derselben
Mikrodynamik.

## 4. Das Vierkörperproblem lässt sich kontrollieren

Der Audit fand einen echten Vierträgerterm bei Ordnung \(\mathcal{O}(t^4/\Delta^3)\).
Konkrete Kontrolle:

\[
\varepsilon=\frac{t}{\Delta}\ll 1.
\]

Dann ist \(J\sim t^2/\Delta\), während der unerwünschte Vierkörperterm skaliert
wie \(K_4\sim t^4/\Delta^3\). Also

\[
\frac{K_4}{J}\sim\Bigl(\frac{t}{\Delta}\Bigr)^2=\varepsilon^2.
\]

Bei \(\varepsilon=0{,}1\) ist der nächste gemeinsame Term bereits nur
ungefähr ein Prozent der führenden Wechselwirkung. Noch schöner wäre ein
zusätzlicher Symmetrie- oder Interferenzmechanismus, der diese Ordnung exakt
löscht. Aber eine kontrollierte effektive Theorie existiert schon ohne ihn.

Damit ist T5 lokal deutlich näher an einem echten mathematischen Grenzverfahren.

## 5. Warum genau vier

Für fundamentale \(\mathrm{SU}(4)\)-Träger:

\[
\Lambda^1 4=4,\qquad
\Lambda^2 4=6,\qquad
\Lambda^3 4=\overline{4},\qquad
\Lambda^4 4=1.
\]

Die Dynamik bevorzugt die antisymmetrischen Paaranteile. Fordert man
zusätzlich, dass ein elementarer abgeschlossener Verbund keine offene innere
\(\mathrm{SU}(4)\)-Ladung besitzt, ist die kleinste nichtleere abgeschlossene
Struktur 4 Träger, und ihr Zustand ist eindeutig

\[
\lvert\Omega\rangle=\frac{1}{\sqrt{24}}\,\varepsilon_{abcd}\lvert abcd\rangle.
\]

Das adressiert die bekannte Lücke, dass reine Antisymmetrie allein auch
\(N=1,2,3\) zulässt.

Expliziter Quellenvertrag: Die elementare Materiepopulation ist \(4\), nicht
beliebig \(4\oplus\overline{4}\). \(\overline{4}\) tritt als konjugierter
Zustand beziehungsweise Orientierung auf, aber nicht als unabhängiger
elementarer Gegenpart innerhalb derselben lokalen Zellpopulation. Sonst würde
\(4\otimes\overline{4}\) bereits Zweierneutralität erlauben.

## 6. T8: Zustand und Gedächtnis als gemeinsame Lösung

Der künstliche Unterschied „Register behalten / Register neu nehmen“
verschwindet unter der reversiblen primitiven Regel.

Fundamental gilt immer: Information bleibt erhalten. Was „Vergessen“ genannt
wird, bedeutet lediglich: History-Freiheitsgrade werden operationell
unzugänglich.

Global bleibt

\[
\rho_{\mathrm{global}}\mapsto U\rho_{\mathrm{global}}U^\dagger
\]

unitär. Lokal sieht man

\[
\rho_S=\operatorname{Tr}_H\rho_{SH}.
\]

„Frisches Register“ bedeutet daher nicht, dass die Welt einen Speicher
löscht. Es bedeutet: Die zukünftige Operationsalgebra greift nicht mehr auf
\(H_{\mathrm{alt}}\) zu.

Das passt zur operationellen Äquivalenz des Forschungsbuchs: Zwei Geschichten
sind nur gleich, wenn kein erlaubtes Zukunftsexperiment sie unterscheiden
kann.

Physikalische Realität ist nicht nur der aktuelle Zustand, sondern die Menge
der noch zugänglichen Korrelationen.

## 7. Präparation als Relaxation, nicht als Magie

Der Zustand \(\Omega\) muss nicht durch „magische Kühlung“ entstehen. Die
lokale Dynamik hat eine niedrige antisymmetrische Energiestruktur. Ein System
mit Energieabfuhr in den History- beziehungsweise Vermittlersektor kann
relaxieren:

\[
\rho\to\lvert\Omega\rangle\langle\Omega\rvert.
\]

Das reine Austauschmodell kann das allein nicht: Der \(\Omega\)-Anteil ist
unter reinem Austausch erhalten. Aber die vollständige Theorie enthält bereits
reale beziehungsweise virtuelle Vermittler plus Geschichte.

Deshalb kann eine offene effektive Beschreibung eines global geschlossenen
Systems einen dissipativen lokalen Kanal erzeugen:

\[
\dot\rho_S=-i[H_{\mathrm{eff}},\rho_S]+D(\rho_S).
\]

Wenn der einzige dunkle neutrale Vierträgerzustand \(\Omega\) ist, wird er ein
natürlicher Attraktor. Die 20-Qubit-Präparationsschaltung bleibt dann ein
Experimentierprotokoll, nicht der kosmologische Herstellungsmechanismus.

## 8. Warum drei Raumdimensionen

Nicht einfach „weil \(A_3\) Rang drei hat“.

Eine niedrigenergetische kohärente Zweibandstruktur

\[
H(k)=d_0(k)I+d_1(k)\sigma_x+d_2(k)\sigma_y+d_3(k)\sigma_z
\]

hat einen masselosen Berührungspunkt nur bei \(d_1=d_2=d_3=0\). Das sind drei
unabhängige Bedingungen. Damit gilt:

- bei \(d<3\) ist ein generischer Punkt nicht robust,
- bei \(d=3\) entstehen generische isolierte Berührungspunkte,
- bei \(d>3\) entstehen generisch höherdimensionale Nullmengen.

Wenn vom Universalraum verlangt wird, dass Niedrigenergieanregungen robuste,
isolierte, masselose und chirale Teilchen bilden, wird \(d=3\) zur
ausgezeichneten räumlichen Dimension.

Das Forschungsbuch nennt diese Kodimension drei bereits als Hinweis, weist
aber korrekt darauf hin, dass der Impulsraum bisher vorausgesetzt ist.

Stärkere Kette:

\[
\text{reversibles lokales Netzwerk}
\to\text{Translationen im thermodynamischen Grenzwert}
\to k
\to\text{stabile isolierte Pole}.
\]

Dann selektiert die Forderung „isolierter stabiler Weyl-Pol“ drei
Raumdimensionen. Das ist noch kein Beweis aus \(E_8\) allein. Es ist eine
klare Auswahlbedingung.

## 9. Zeit als vierte Dimension auf andere Weise

Die Zeitdimension darf gerade nicht als vierte Graphachse entstehen. Sie
kommt aus der kausalen Ordnung der unitären Ereignisse \(U_1,U_2,\ldots\)
beziehungsweise im Kontinuum \(U(t)=e^{-itH}\).

Räumliche Richtungen sind austauschbar. Zeit ist die Richtung der
Komposition von Zustandsänderungen. Deshalb strukturell \(3+1\), nicht ein
euklidischer Viererraum.

Wenn der Weyl-Pol entsteht,

\[
G^{-1}\simeq\omega I-v_i q_i\sigma_i,
\]

folgt automatisch

\[
\det G^{-1}=\omega^2-v_iv_j q_i q_j.
\]

Bei emergenter Isotropie \(v_iv_j\to c^2\delta_{ij}\) erhält man
\(\omega^2-c^2\lvert q\rvert^2\). Das ist die Propagatorbrücke des
Forschungsbuchs.

## 10. Universeller Lichtkegel als RG-Fixpunkt

Mehrere Teilchensektoren könnten zunächst unterschiedliche Geschwindigkeiten
\(v_f,v_b,v_g\) haben. Eine TOE verlangt \(v_f=v_b=v_g=c\).

Die richtige Forderung ist nicht, dass alle mikroskopischen Geschwindigkeiten
von Anfang an gleich sind, sondern

\[
v_i(\ell)\;\xrightarrow{\ell\to\infty}\;c.
\]

Also ein infrarotstabiler Lorentz-Fixpunkt. Dann ist \(c\) kein eingesetzter
Parameter, sondern das gemeinsame Verhältnis \(\Delta x/\Delta t\) am
RG-Fixpunkt. Das wäre der mathematische Abschluss von T3.

## 11. Materie präziser identifizieren

Materie wäre nicht einfach „ein \(E_8\)-Generator“. Materie wäre:
topologisch oder symmetriegeschützte propagierende Defekte des
Vakuumnetzwerks.

Eine Darstellung wie \(16\) sagt nur, welche inneren Quantenzahlen ein Objekt
tragen könnte. Sie sagt nicht, ob es propagiert, ob es massiv oder masselos
ist, ob es chiral ist, ob es stabil ist.

Im neuen Bild muss eine Materieart gleichzeitig sein:

\[
\text{Pol des Propagators}
+\text{innere }\mathrm{Spin}(10)\text{-Darstellung}
+\text{topologische Ladung}.
\]

## 12. Drei Familien: alte Formel ersetzen

Die Formel \((16-1)/5=3\) nicht mehr als fundamentalen Familienbeweis
verwenden. Das Forschungsbuch selbst sagt, dass dies kein chiraler Indexsatz
ist.

Die richtige Aussage muss sein

\[
N_{\mathrm{fam}}=\operatorname{index} D_{\mathrm{eff}},
\]

also

\[
\dim\ker D_L-\dim\ker D_R=3.
\]

Aussichtsreichster Kandidat: eine topologische Ladung des emergenten Vakuums,
nicht die bloße Dimension eines endlichen Vektorraums. Schematisch

\[
\frac{1}{8\pi^2}\int\operatorname{Tr} F\wedge F=3
\qquad\Longrightarrow\qquad
\operatorname{index} D\propto\int\operatorname{Tr} F\wedge F=3.
\]

Das würde gleichzeitig erklären, warum Familien ganzzahlig und robust sind,
warum kleine lokale Deformationen ihre Anzahl nicht verändern, und warum
links und rechts asymmetrisch sein können.

Was noch fehlt: der Nachweis, dass die primitive \(U\)-Regel tatsächlich einen
Vakuumsektor mit topologischer Zahl drei auswählt. Hier keine Abkürzung.

## 13. Chiralitätslücke: Bulk–Rand-Konstruktion

Die gewöhnliche \(\mathrm{SU}(4)\)-Kette ist nicht chiral. Das Buch zeigt das
explizit: \(c_L=c_R=3\). Die Lösung darf deshalb nicht eine weitere
eindimensionale Kette sein.

Benötigt wird

\[
\text{gapped bulk}\implies\text{chiral edge}.
\]

Die \(E_8\)-Erweiterung wäre dann keine zufällig angenommene CFT, sondern die
Randtheorie eines invertierbaren Bulkzustands. Das passt strukturell zu

\[
(D_5)_1\times(A_3)_1\subset(E_8)_1.
\]

Der Bulk sorgt dafür, dass die unerwünschte Gegenchiralität gepaart und
gegappt wird. Am Rand bleibt \((E_8)_1\) chiral.

Das schließt die logische Lücke zwischen „wir haben algebraisch \(E_8\)“ und
„wir haben eine chirale \(E_8\)-Naht“. Noch ausstehend: die Konstruktion
dieses Bulkterms aus derselben \(U\)-Regel.

## 14. Gravitation: kollektive Variation des Propagatorframes

Nicht: Finde irgendwo im \(E_8\)-Spektrum ein Teilchen mit Label „Graviton“.

Sondern: Betrachte langsame räumliche Änderungen des lokalen Propagators
selbst. Wenn

\[
G^{-1}(x,p)=e^a_{\mu}(x)\,\sigma_a p^\mu+\cdots,
\]

dann definiert \(e^a_{\mu}(x)\) ein emergentes Vierbein. Daraus entsteht

\[
g_{\mu\nu}=\eta_{ab}\,e^a_{\mu}e^b_{\nu}.
\]

Die Geometrie ist dann kein zusätzliches Feld. Sie ist die lokale Form der
Ausbreitungsregel.

Schwankungen \(e^a_{\mu}=\bar e^a_{\mu}+\delta e^a_{\mu}\) enthalten nach
Eichredundanz einen symmetrischen Tensoranteil \(h_{\mu\nu}\). Wenn die
effektive Wirkung bei langen Wellenlängen diffeomorphismusinvariant wird, ist
der führende lokale Term mit zwei Ableitungen

\[
S_{\mathrm{grav}}\propto\int d^4x\,\sqrt{-g}\,R.
\]

Dann entstehen automatisch die zwei transversalen Gravitonhelizitäten.

Harter Test: Erzeugt die kollektive Schwankung von \(U\) eine masselose
Spin-2-Polstelle? Nicht irgendeine passende Zahl \(8\pi\).

## 15. Warum Gravitation universell koppeln würde

Wenn alle Materiepole denselben emergenten Propagatorhintergrund
\(e^a_{\mu}(x)\) benutzen, dann beeinflusst eine Variation davon jede Anregung
über dieselbe lokale Kinematik.

\[
\text{Alle Teilchen leben im selben Ausbreitungsnetz}
\implies
\text{alle koppeln an dieselbe emergente Geometrie}.
\]

Universelle Gravitation wäre dann eine Folge davon, dass es nur eine
gemeinsame kausale Struktur gibt.

## 16. Eichfelder aus internen Frames

Die lokalen internen Basen sind redundant. Wenn an zwei benachbarten Orten
\(\lvert\psi_x\rangle\to U_x\lvert\psi_x\rangle\) und
\(\lvert\psi_y\rangle\to U_y\lvert\psi_y\rangle\), muss die Verbindung
transformieren als

\[
A_{xy}\to U_x A_{xy} U_y^\dagger.
\]

Damit entstehen Eichverbindungen aus der Vergleichsregel lokaler interner
Frames:

\[
\text{lokale Basisfreiheit}\implies\text{connection}\implies\text{gauge field}.
\]

Dualität:

- Variation äußerer relationaler Frames \(\Rightarrow\) Gravitation
- Variation innerer Frames \(\Rightarrow\) Eichfelder

## 17. Kopplungskonstanten aus Steifigkeiten

Nicht: finde eine hübsche Gleichung mit \(\alpha\).

Sondern: Wenn die effektive Wirkung

\[
S_{\mathrm{eff}}=\int d^4x\Bigl[\frac{M_P^2}{2}R-\frac{1}{4g_i^2}F_i^2+\cdots\Bigr]
\]

aus demselben mikroskopischen Modell entsteht, dann sind \(M_P^2\) und
\(1/g_i^2\) Suszeptibilitäten beziehungsweise Steifigkeiten desselben
Vakuums:

\[
\frac{1}{g_i^2}\sim\frac{\partial^2\Gamma}{\partial A_i^2}.
\]

Dann bekommt eine Zahl wie \(\alpha\) erstmals eine physikalische Herkunft.
Bis das gezeigt ist, bleibt die bislang extrem genaue \(\alpha\)-Gleichung
eine interessante Formel und keine fundamentale Herleitung.

## 18. Was jetzt die primitive Theorie ist

Nicht mehr: Fundamentale Realität ist \(E_8\).

Auch nicht: Fundamentale Realität ist \(Q=[\,{,}\,]\).

Sondern:

> Fundamentale Realität ist eine minimale reversible, lokale und phasentreue
> Kompositionsdynamik, deren elementare Vertexgrammatik die
> \(\mathbb{Z}_4\)-graduierte \(E_8\)-Struktur ist.

Darin sind:

| Begriff | Lesart |
|---|---|
| Zustände | offene Enden der Prozessstruktur |
| Wechselwirkungen | erlaubte \(E_8\)-Vertizes |
| Energie | effektive Kosten virtueller Prozesse |
| Gedächtnis | erhaltene Pfadinformation |
| Materie | stabile propagierende Defekte |
| Raum | Netzwerk ihrer möglichen Propagation |
| Zeit | kausale Reihenfolge der Ereignisse |
| Eichfelder | Variation interner Vergleichsrahmen |
| Gravitation | Variation des gemeinsamen Ausbreitungsrahmens |

## 19. Status der acht Tore nach dieser Rekonstruktion

| Tor | Kandidatenlösung | Was noch wirklich bewiesen werden muss |
|---|---|---|
| T1 Quelle | Reversible \(E_8\)-Vertexdynamik mit Belegung und History | Eindeutigkeit beziehungsweise Minimalität |
| T2 chirale Naht | Bulk–Rand-Realisierung der \((E_8)_1\)-Erweiterung | Expliziter lokaler Bulk-Hamiltonoperator |
| T3 3+1D | robuste isolierte Weyl-Pole wählen räumlich \(d=3\); Zeit aus Prozessordnung | Ableitung des thermodynamischen Impulsraums und Lorentz-RG-Fixpunkts |
| T4 Chiralität und 3 Familien | Familie = Dirac-Index, \(N_{\mathrm{fam}}=3\) | Topologische Ladung 3 aus der primitiven Quelle |
| T5 Wechselwirkung | \(E_8\)-Vermittlung liefert \(P_+\); höhere Terme kontrolliert durch \(t/\Delta\) | kontrollierter Vielkörper- und Kontinuumsgrenzwert |
| T6 Kopplungen | Vakuumsteifigkeiten der emergenten Verbindungen | konkrete Berechnung \(g_1,g_2,g_3\), Yukawas und Neutrinos |
| T7 Gravitation | kollektive Variation des gemeinsamen Propagatorframes | masseloser Spin-2-Pol und Einsteinwirkung aus Integration der Mikrodynamik |
| T8 Zustand | global unitäre Historydynamik plus lokale Relaxation in dunkle neutrale Zustände | eindeutiger kosmischer Zustand beziehungsweise Randbedingung |

## 20. Die drei Punkte, auf die jetzt alles hinausläuft

Es gibt nur noch drei wirklich fundamentale Unbekannte.

**A. Die eine mikroskopische unitäre Regel.** \(U\) vollständig hinschreiben
und danach nichts mehr wechseln. Keine separate Wahl für Clebsch, Tetramer,
Kette, Register oder Clock.

**B. Der thermodynamische Grenzwert.** Aus genau dieser \(U\) muss entstehen

\[
G^{-1}\to\gamma^\mu p_\mu
\]

mit drei räumlichen Richtungen, gemeinsamer Geschwindigkeit und chiralen Polen.

**C. Der topologische Vakuumsektor.** Er muss gleichzeitig liefern

\[
\operatorname{index} D=3
\]

und einen kollektiven geometrischen Modus \(\mathrm{Spin}\,2\), \(m=0\).

Wenn diese drei Rechnungen funktionieren, fällt fast alles andere in eine
gemeinsame Struktur.

### Perspektivwechsel

Nicht: „Welche mathematische Struktur ist die Welt?“

Sondern: „Welche reversible Kompositionsregel erzeugt genau die stabilen
Phänomene, die wir als Mathematik, Raum, Zeit, Materie und Information
getrennt wahrnehmen?“

Darin wäre \(E_8\) nicht „das Universum“. \(E_8\) wäre die lokale Grammatik,
aus der das Universum seine möglichen Ereignisse baut.

Das nächste sinnvolle Stück Arbeit ist nicht noch eine Gesamtsynthese,
sondern die explizite Konstruktion dieser \(U\)-Regel und anschließend ein
erster Vielzellengrenzwert. Genau dort entscheidet sich, ob tatsächlich eine
TOE-Architektur vorliegt oder nur eine außergewöhnlich strukturreiche
endliche Algebra.
