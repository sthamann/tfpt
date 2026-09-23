# Prüfung der beiden eingegangenen positiven Seam-Spiegelungsberichte

15. September 2026 · ergänzt die Quellenneustart-Notiz `RESULTS.md`

## Kurzurteil

**Die Rechnung lässt sich reproduzieren. Die Überschrift »ursprüngliche Seam vollständig nachgewiesen« geht über sie hinaus.** Beide Texte verweisen auf denselben Quellordner und dieselben 331 Prüfungen. Eine zusätzliche unabhängig behauptete Kleinrechnung wurde nicht als eigener Checker mitgeliefert und wird hier nicht als zweite unabhängige Reproduktion gezählt.

Die gesamte gelieferte Rechnung wurde normal und mit `-OO` wiederholt; beide Resultate stimmen bytegenau mit den gelieferten JSON-Dateien überein. Ihr gemeinsamer Hash ist

`93302953e3519a79c6d13ff819eebd35857ae0e0e94b053aae25e6386553ffe5`.

Originaldateien blieben unverändert. Eingaben, Ausgaben und Prüfentscheidungen sind unter `received_reflection/` dokumentiert.

## 1. Was übernommen wird

| Befund | Entscheidung |
|---|---|
| Vier gleichmäßig platzierte Intervalle und ihre vier Lücken besitzen die versetzte Ecken-/Kantenpermutation | Exakt in der angegebenen Ringgeometrie; unten auf alle zulässigen Größen erweitert |
| Der gewählte antiperiodische Ring besitzt einen reellen involutiven Spiegelungslift und eine Clock mit ρ⁴=−I | Richtig; Antiperiodizität ist dabei eine Voraussetzung |
| Der gewählte freie Zustand ist spiegelungsinvariant | Reproduziert; unten zusätzlich analytisch begründet |
| Sechs fünfstellige Permutationen invertieren den inneren Clock und erhalten W durch einen Paarlift | Reproduziert für diese aufgezählte Permutationsklasse |
| Die Rang- und Gleichgewichtsaussagen des Zweinachbarrahmens | Richtig innerhalb U=aI+bR und der verwendeten zeilenweisen Kovarianzforderung |
| Die ursprüngliche rohe Seam erzwingt gerade dieses Ringmodell und η=−1 | Durch diese Quellen nicht nachgewiesen |
| Eine identifizierte gemeinsame Feld-, Zustands- und Operationskarte zwischen Ring und W-Bank | Nicht konstruiert; beide Objekte werden separat geprüft |

»331 exakte Bedingungen« ist als pauschale Typisierung ungenau: Die vier Zustandsinvarianztests verwenden Fließkomma-Toleranzen. Viele weitere Bedingungen prüfen kleine ganzzahlige Permutationsmatrizen, die in Fließkomma gespeichert sind. Die Aussagen müssen nach Inhalt, nicht nur nach dem JSON-Feldnamen `exact_checks`, eingeordnet werden.

## 2. Der wichtigste Quellenfehler: v480 wählt Antiperiodizität, es leitet sie hier nicht her

`verification/v480_multilocal_four_interval.py`, Zeilen 8–9 und 42–47, sagt ausdrücklich, dass die rohe Seam-Prämisse offen bleibt. In Zeile 61 wird

\[
k_m=2\pi(m+1/2)/N
\]

direkt eingesetzt. Das sind bereits antiperiodische Impulse. Es wird weder ein periodisches Gegenmodell auf Reflexionspositivität getestet noch ein Satz bewiesen, der aus RP allein diese Wahl erzwingt.

Der neue Bericht macht aus »auf einem antiperiodischen, RP-zulässigen Ring« die stärkere Aussage »RP lässt nur diesen Ring zu«. Das ist ein logisch anderer Satz. Die periodische Kontrolle des neuen Prüfers testet nur die anderen Wickelvorzeichen, nicht deren RP-Unzulässigkeit. Die weitergehende Herkunftsbehauptung steht dort im **Namen einer Prüfbedingung**, wird von deren booleschem Ausdruck aber nicht getestet.

Auch allgemein verbietet Reflexionspositivität nicht allein Nullenergie. Schon eine Hilbertraumrekonstruktion mit H=0 und normiertem Ω liefert positive Zeitreflexions-Grams ⟨AᵢΩ,AⱼΩ⟩. Für Ω=(1,0) und A=I,σₓ,σ_z sind deren Eigenwerte exakt 0,1,2. Dieses kleine Gegenbeispiel ersetzt keine Prüfung zusätzlicher spezieller geometrischer Seam-Anforderungen; es zeigt, warum ein allgemeines Nullmodenverbot ohne solche Anforderungen nicht verwendet werden darf.

**Korrekte Form:** Wenn die ursprüngliche Seam diesen antiperiodischen Ring realisiert, wird η=−1 vom Ring geerbt. Die neue Rechnung verbessert die Konsequenzseite dieser Aussage. Ihre Voraussetzung ist nicht durch den Verweis auf v480 beseitigt.

## 3. Eigene Weiterführung: der geometrische Teil gilt für alle Größen

Sei N=4Q, 0<ℓ<Q. Vier Intervalle seien

\[
I_j=\{p+jQ+u:0\le u<\ell\}\pmod N,
\]

und die Lücken

\[
G_j=\{p+jQ+\ell+v:0\le v<Q-\ell\}\pmod N.
\]

Eine Ringreflexion s↦c−s muss den Anfang eines belegten Intervalls auf das Ende eines belegten Intervalls abbilden. Daher kommen genau

\[
c_k=2p+\ell-1+kQ\pmod N,\quad k=0,1,2,3
\]

infrage. Einsetzen zeigt für jeden dieser vier Werte

\[
I_j\longmapsto I_{k-j},\qquad
G_j\longmapsto G_{k-j-1},
\]

jeweils modulo vier. Innerhalb eines Intervalls wird u auf ℓ−1−u abgebildet; innerhalb einer Lücke v auf Q−ℓ−1−v. Damit sind Existenz und Vollständigkeit bewiesen — nicht nur an fünf Beispielen beobachtet. Der Ecken-/Kantenversatz ist tatsächlich rein geometrisch.

Für k=0 haben die Intervalle zwei Fixlabels; die Lücken haben keine. Die Formulierung des zweiten Kurzberichts, derselbe Spiegel gehe durch zwei Stühle **und** zwei gegenüberliegende Lücken, ist daher bildlich ungenau: Er **vertauscht** die Lücken, statt ihre Mittelpunkte auf der Spiegelachse festzuhalten.

Zusätzlich wurden 88 unterschiedliche Größen-/Längen-/Platzierungskombinationen unabhängig mit Ganzzahlmengen geprüft. Die allgemeine Aussage beruht auf der Formel, nicht auf deren Zahl.

### 3.1 Der antiperiodische Lift

Auf Funktionen des überdeckenden Ganzzahlrings mit f(s+N)=−f(s) definiere

\[
(\mathcal S_cf)(s)=f(c-s),\qquad(\mathcal T_Qf)(s)=f(s+Q).
\]

Dann gelten unmittelbar \(\mathcal S_c^2=I\), \(\mathcal T_Q^4=-I\) und
\(\mathcal S_c\mathcal T_Q\mathcal S_c^{-1}=\mathcal T_Q^{-1}\).
Für die branch-cut-kompatible Platzierung 0≤p und p+ℓ≤Q ergeben sich am k=0-Spiegel die Stationsvorzeichen (1,−1,−1,−1), zusätzlich zur internen Umkehrung des jeweiligen Intervalls. Eine Reduktion auf genau einen Modenvektor je Intervall muss diese interne Umkehrung berücksichtigen; symmetrische Profile sind beispielsweise geeignet.

Geometrisch gibt es vier reflektierende Zentren modulo N. Im gelifteten Operatorverband liegen zusätzlich deren Negative, also acht Spiegelungselemente der Diedergruppe mit insgesamt 16 Elementen. »Genau vier« bezieht sich auf die geometrischen Zentren mit gewählten Liftrepräsentanten.

### 3.2 Die Zustandsinvarianz hat einen analytischen Beweis

Der geprüfte freie Korrelator ist c(d)=N⁻¹Σₖ∈occ exp(ikd). Die besetzte Impulsmenge ist unter k↦−k invariant; daher c(−d)=c(d). Antiperiodizität liefert c(d+N)=−c(d). Bei der Spiegelung wird ein Differenzargument zu −d plus einer ganzzahligen Zahl von Umläufen. Die dabei entstehenden Zeichen werden durch genau die beiden Liftzeichen der Endpunkte kompensiert. Folglich gilt SCS*=C exakt für diesen Zustand und jede regionerhaltende Spiegelung.

Die reproduzierten 10⁻¹⁴-Abweichungen sind damit numerische Restfehler eines exakten modellinternen Sachverhalts. Dieser Beweis zeigt **nicht**, dass der freie Ringzustand der Grundzustand des W-Fock-Hamiltonoperators ist.

## 4. Wo die gemeinsame Operatorzuordnung noch fehlt

`raw_seam()` arbeitet auf vier Intervallen des freien Fermionrings. `native_source()` arbeitet auf 64 Moden des eigenständig quantisierten W-Modells und konstruiert sechs innere fünfstellige Spiegelungen. Die Funktion überträgt weder Ringfelder noch ihren Zustand auf diese Moden. Die beiden Clock-Ordnungen bleiben verschieden; das wird im gelieferten Bericht selbst anerkannt.

In `selection()` wird anschließend L=RJ aus der Stationsmatrix definiert. Die Funktion verwendet die tatsächlichen Lückenprofile und deren Liftzeichen nicht. In der gelieferten JSON-Datei lauten die Lückenzeichen des maßgeblichen Spiegels sogar

```text
[null, -1, -1, null]
```

`null` bedeutet hier: Innerhalb der betreffenden Lücke wechseln die Zeichen über den gewählten Branch Cut. Das ist kein Rechenfehler und kein Beweis gegen eine konsistente Bündelbeschreibung. Es zeigt aber, dass die **Permutation ganzer Lücken** nicht bereits die vollständige Wirkung auf einen ausgewählten Paarkanalmode liefert. Ein Paarfeld kann zudem einen anderen Twist als ein einzelnes Fermion tragen. Genau diese Feld- und Profilzuordnung muss mitgeführt werden.

Der unveränderte native W-Intertwiner ist ein wertvolles positives Teilresultat. Ihn und die Ringpermutation getrennt zu konstruieren ist aber noch keine quellenseitige Abbildung zwischen ihnen. Ein gemeinsames zusammengesetztes Modell lässt sich unter zusätzlichen Kompositionsannahmen bauen; das ist nicht dasselbe wie seine eindeutige Herleitung.

## 5. Die Mischungswahl bleibt sauber bedingt

Für U=aI+bR und die ausgewählte zeilenweise Paar-Kovarianz bleibt die Obstruktion a²−b², und das Gegenmodell 3/5,4/5 liefert −7/25. Unter Gleichgewicht und der zusätzlichen Forderung nach keiner freien Richtung bleibt der antiperiodische Zweinachbarrahmen übrig. Diese Aussagen werden übernommen.

Sie beweisen keine allgemeine Aussage »Reflexion allein erzwingt nur diese lokale Quelle«. Der Bericht selbst behält den Zweinachbaransatz als Voraussetzung. Andere Stützstellen, andere Felddarstellungen, zusätzliche Profile oder andere symmetrische Kopplungsfunktionen wurden durch diese vier Zeilen nicht klassifiziert.

Darum ist auch »nur noch eine W-Bank pro Link herleiten, dann ist die lokale Quelle vollständig aus TFPT abgeleitet« zu stark. Die Quelle benötigt außerdem die korrekte Feld-/Zustandszuordnung und die bislang gesetzte Dynamik. Ein solcher Schluss kann nicht aus einer Ortszählung folgen.

## 6. Wie das mit der eigenen einfacheren Fortsetzung zusammenpasst

Die eigene Quellenprüfung hat W ohne zusätzliche Banken in seiner vorhandenen 16⊗4-Struktur zerlegt. Sie hat außerdem alle 480 Vorzeichen als einen E₈-Strom-Operatorproduktkanal rekonstruiert. In dieser Randfeldalgebra sind die Paarströme bereits aus den vorhandenen Feldern rekonstruierbar:

\[
K_A(w)=\frac18\sum_{r<s}W_{A,rs}\operatorname{Res}_{z=w}I_r(z)I_s(w).
\]

Damit liegt eine kleinere mögliche Fortsetzung auf dem Tisch: Die Paarobjekte zunächst als **abgeleitete Feldkanäle** behandeln, statt pro gezeichneter Lücke eine neue unabhängige Oszillatorbank einzuführen. Die Formel ist innerhalb der gewählten affinen Randrealisierung exakt. Sie liefert noch keine Operation über zwei endlich getrennte Lücken und keinen vollständigen Bulkadapter.

Die beiden Arbeiten widersprechen sich daher nicht in ihrer korrekten Mathematik: Die eingegangene Arbeit klärt die Geometrie eines gesetzten Ringmodells; die eigene Arbeit klärt den ursprünglichen inneren Tensor und seinen Feldtyp. Der mögliche Anschluss muss genau diese verschiedenen Rollen erhalten. Vier räumliche Intervalle, vier innere SU(4)-Komponenten und vier äußere Banken sind nicht automatisch dieselben vier Dinge.

## Integrationsentscheidung

Übernommen werden die Ringgeometrie, ihr Lift, die sechs W-Symmetrien und die bedingte Mischungsrechnung. Ergänzt werden der allgemeine Ringbeweis und die analytische Zustandsinvarianz. **Nicht übernommen** werden die aus v480 behauptete RP-Auswahl der Antiperiodizität, die vollständige rohe Seam-Identifikation und die pauschale Beschreibung aller 331 Tests als exakt.

Keine Beförderung in `verification/`, keine Statusänderung eines T1–T8-Ziels und keine Änderung der bereits ausgelieferten PDFs.
