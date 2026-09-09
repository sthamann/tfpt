# Inter-Sheet-Dynamik: Prüfung der vier Fotos im Sessionskontext

8. September 2026. Lokaler HEAD b803b7e5. Die ausgewerteten neuen Forschungsordner
anderer Sessions sind teilweise uncommitted. Diese Untersuchung ergänzt nur
diesen eigenen Ordner; keine Theorie-Abschlussmarker geändert.

## Ergebnis

Der Ansatz enthält richtige Blockalgebra. Die Aussage »Dynamik ist immer
Übergang zwischen den Sheets« folgt aber nicht aus der angegebenen
Antikommutation. Die μ4-umkehrende Zusatzsymmetrie existiert in einem
vorhandenen E8-Modell bereits. Ihre Gleichsetzung mit der Dynamikreflexion
scheitert auf den bisher verwendeten vollständigen 16D-Darstellungen an
einem exakten Typunterschied. Offen ist eine gemeinsame physikalische
Darstellung mit ausgewähltem Zustand, Transport und Readout.

## 1. Symmetrie-Eigenräume sind nicht automatisch geometrische Blätter

Für eine lineare selbstadjungierte unitäre Involution Γ ergibt ihre
Eigenraumzerlegung H+⊕H− die Darstellung Γ=diag(I,−I). Aus ΓDΓ=−D und D*=D folgt

    D = [[0,A],[A*,0]],       D² = diag(AA*,A*A),    A:H−→H+.

Endlichdimensional ist das unmittelbar Blockalgebra. Bei unbeschränkten
Operatoren gehören ein dichter Γ-invarianter Definitionsbereich,
Abgeschlossenheit und die passende Adjungiertenrelation zur Konstruktion.

H+ und H− sind Symmetrie-Eigenräume. Bei einem geometrischen Blattwechsel
enthalten sie symmetrische beziehungsweise antisymmetrische Funktionen auf
beiden Blättern. Sie sind nicht automatisch Funktionen auf jeweils einem
Blatt. Eine zusammenhängende Überlagerung muss auch nicht global als zwei
getrennte Kopien trivialisiert sein.

Exaktes Gegenbeispiel mit zwei tatsächlichen Sheet-Basiszuständen:

    S = [[0,1],[1,0]],       D = [[1,0],[0,−1]].

SDS=−D, aber exp(−itD)=diag(exp(−it),exp(it)): Die Übergangsamplitude von
Sheet 1 nach Sheet 2 ist identisch null. Erst der Hadamard-Basiswechsel
diagonalisiert S und macht D off-diagonal. Umgekehrt ist D=S ein reiner
Hoppingoperator, der mit S kommutiert. Antikommutation mit dem Blattwechsel
ist weder notwendig noch hinreichend für diese konkrete Bedeutung von
Inter-Sheet-Hopping. Foto 3 enthält somit eine falsche allgemeine Folgerung.

## 2. Quadrat, Index und Zeit

AA* und A*A haben dieselben positiven Eigenwerte samt Multiplizitäten,
können aber verschiedene Nullmoden haben. Für A:C²→C³ mit Spalten e1,2e2
lauten die Spektren {1,4,0} und {1,4}. Diese Nullmodendifferenz trägt den
Index. Ein endliches quadratisches A hat Index null; ein unendlicher
Fredholmindex benötigt zusätzliche analytische Voraussetzungen.
Dies ist klassische supersymmetrische Quantenmechanik:
[Cooper–Khare–Sukhatme](https://arxiv.org/abs/hep-th/9405029).

D² ist ein positiver Operator auf beiden Symmetriesektoren. Es ist weder
eine Wahrscheinlichkeit noch automatisch ein klassischer Grenzwert.
Auch der Quotient liefert nicht von selbst klassische Physik. Die
Born-Regel benötigt Zustand und Messoperator. Schon σx und σy haben
dasselbe Quadrat I, ohne bis auf ein Vorzeichen identisch zu sein:
Beim Quadrieren können mehr Daten als ein einzelnes Vorzeichen verloren gehen.

Für unitäres Γ gilt Γexp(−itD)Γ=exp(+itD). Das ist algebraische
Parameterumkehr, noch keine physikalische Zeitumkehr. Die übliche
Zeitumkehr Θ ist antiunitär und erfüllt bei Zeitumkehrinvarianz ΘHΘ⁻¹=H.
Der Zeitwechsel folgt aus ΘiΘ⁻¹=−i. Die unitäre Antikommutation wird als
chirale/Sublattice-Symmetrie bezeichnet. Foto 4 korrigiert diesen Punkt
zutreffend. [Ryu et al., Gleichungen 3–5 und Diskussion](https://arxiv.org/html/0912.2157v2).

Die Rollen von D als Diracoperator, als Einteilchen-Hamiltonian und von
D² als positivem Hamiltonian sind explizit zu wählen. Ein nichttrivialer
nichtnegativer H kann selbst keine exakte unitäre Antikommutation besitzen.
Ein Einteilchenspektrum mit ±-Paaren ist dagegen üblich; seine physikalische
Interpretation benötigt Vielteilchenkonstruktion und Präparation.

## 3. Auch die spätere Chat-Antwort ist zu korrigieren

Die zusätzlich gelesene letzte Nachricht in **TFPT Quantendynamik Vergleichen**
macht »holomorph oder antiholomorph?« zum unentschiedenen Kill-Test für die
gesamte Dirac-Spur. Auf einer realen Tangentialebene mit J=[[0,−1],[1,0]]
gilt tatsächlich

    (−I)J(−I)=J,       KJK=−J für K=diag(1,−1).

Das widerlegt nur die Identifikation der ersten Wirkung mit einem
J-ungeraden Generator auf diesem Raum. Ein Diracoperator auf einem
Spinorbündel oder einer anderen Darstellung ist dadurch nicht ausgeschlossen.

Die Projektquellen unterscheiden außerdem mehrere Überlagerungen:

- [tfpt_research_contracts.tex](/Users/stefanhamann/Projekte/tfpt-theoryv4/tfpt_research_contracts.tex:1492)
  behandelt die Clock-Wurzel und ab Zeile 1501 den freien Collar-Deckwechsel
  als Halbperiodentranslation des Seam-Doppels. Dieser ist nicht pauschal
  die verzweigte Torusinvolution z→−z.
- Derselbe [Text ab Zeile 379](/Users/stefanhamann/Projekte/tfpt-theoryv4/tfpt_research_contracts.tex:379)
  beschreibt das Kandidatenmodell y³=x⁴−1 und eine bereits konstruierte
  antiholomorphe Realstruktur R. Das Modell ist ausdrücklich noch nicht
  mit dem physikalischen Seam identifiziert.
- [Architekturtext ab Zeile 296](/Users/stefanhamann/Projekte/tfpt-theoryv4/tfpt_1_architecture_e8.tex:296)
  nennt den konstruierten Reflexionsgenerator und dessen Bereichsgrenze.

Die abstrakte Existenz einer antiholomorphen Reflexion ist daher nicht die
offene Gesamtfrage. Offen ist die Identifikation der unterschiedlichen Wirkungen.

## 4. μ4-Konjugation existiert bereits, aber auf einem bestimmten Raum

Die heutige [Carrier-Konjugationsrechnung](../theory-contracts/carrier-module-conjugation/README.md)
konstruiert auf dem E8-Gitter

    K(q1,...,q8)=(q1,−q2,q3,−q4,q5,−q6,q7,−q8).

K²=I und KJK⁻¹=−J; Norm, vorhandener Ladungscharakter und Familienwirkung
bleiben erhalten. Hier hat K vier positive und vier negative Eigenrichtungen.
Die vorhandene Cocycle-Hebung schickt einen geladenen Verschieber U_s nach
U_delta U_s, wobei delta eine echte neutrale Gitterverschiebung ist.

J als reeller komplexer Strukturgeber, J als Gitterautomorphismus und die
zentrale komplexe Phase iI auf einem komplexen Darstellungsraum sind
unterschiedlich. Jeder komplex-lineare Operator kommutiert mit iI.
U(iI)U⁻¹=−iI benötigt Antilinearität, sofern iI die Skalarmultiplikation ist.
Eine Gitterkonjugation kann hingegen komplex-linear auf |q>-Basiszuständen
implementiert sein. Beim Heben müssen die Operatorrelationen neu geprüft werden.

Der [Involutionstyp-Beweis](../theory-contracts/compiler-involution-types/README.md)
zeigt: Die vier dort zugelassenen kohärenten K-Lifts auf 16 Ladungszeichen-
Zuständen haben Eigenraumdimensionen **12+4**. Jede Involution, die den
invertierbaren Operator auf den 16 Majorana-Koordinaten umkehrt, hat **8+8**.
Kein invertierbarer Ganzraum-Intertwiner kann das angleichen.

Direkte zusätzliche Folgerung für Foto 4: Auf dem 12+4-Raum gibt es keinen
invertierbaren linearen J mit ΓJ=−JΓ. J müsste die beiden Eigenräume bijektiv
vertauschen. Insbesondere sind J²=−I und diese Antikommutation dort zusammen
unmöglich. Das negiert nicht die richtige 4+4-Gitterrelation; es verbietet
deren unveränderte Übertragung auf diesen anderen Raum.

Jeder Γ-ungerade selbstadjungierte D auf 12+4 hat Rang höchstens 8 und
mindestens acht Nullmoden. Das ist scharf. Größere, unendliche, Fock- oder
anders typisierte Konstruktionen sind nicht ausgeschlossen.

Selbst auf einem passenden Raum liefert die einfachste Wahl D0=ΓJ bei
orthogonalem J zwar einen selbstadjungierten Γ-ungeraden Operator, aber
D0²=I. Eine Clifford-Struktur allein erzeugt noch kein nichttriviales
Energiespektrum oder räumliche Ableitung.

## 5. Was die anderen Sessions bereits leisten

Aufgaben wurden gelesen, nicht angeschrieben oder umgelenkt. Bei den drei
langen aktiven Forschungsaufgaben lieferte die API leere jüngste Turn-Items;
dort wurden ergänzend die aktuellen konkreten Dateien gelesen. Diese Aufnahme
ist kein Audit aller laufenden Prozesse.

| Quelle / Aufgabe | Belastbarer Zusammenhang |
|---|---|
| TFPT Quantendynamik Vergleichen | Ausgangshypothese und spätere holomorph/antiholomorph-Behauptung geprüft; Korrekturen oben. |
| Aufgabe mit zehn Foto-Anhängen; [Geometrie und Readout](../double-cover-rh-audit-2026-09-08/GEOMETRIE_UND_READOUT.md) | Rationale Boundary-erhaltende Reflexion kehrt H und Clock um. Alle drei Markierungen zugleich zu erhalten scheitert am Dreiecks-Spurinvarianten. Der Boundary-Readout bleibt im zehn-dimensionalen Clock-Fixraum; sechs nichttriviale Moden bleiben unsichtbar. |
| Finde TFPT-Lösungen zur vollen TOE; [Compiler-Clifford-Brücke](../theory-contracts/compiler-clifford-bridge/README.md) | Existierende Compilerdaten erzeugen bereits endliche Clifford-Algebra und formales Lorentz-Symbol. Dieselbe Algebra erlaubt euklidische Signatur. Physikalischer Transport, Zustand, Nettochiralität und 3+1D-Grenztheorie bleiben zusätzliche Pflichten. |
| [Clock-Readout](../theory-contracts/compiler-involution-types/CLOCK_READOUT.md) | Vorhandene Majorana-Bilineare tragen primitive C6-Grade 1 und 5. Zulässigkeit, dynamische Antwort und Quellenzustand müssen noch nachgewiesen werden. |
| Finde fehlende RH-Bausteine in TFPT | Neuester Nulltemperaturbericht verlangt eine exakte Momentenidentität eines positiven Effekts mit ausgewähltem Zustand. Beliebige Positivität von D² genügt nicht. |
| Untersuche TFPT und neue Faktorisier | Geometrie-Reuse-Bericht optimiert kleine Phasenrekursion; kein belegter Vorteil gegenüber direkter Faktorsuche und kein Faktorzugriff aus dem Double Cover. |
| Pi-Primzahl-Korrelationen prüfen | Abgeschlossener Fourier/Sieb-Vergleich erzeugt dieselben Kandidaten; Fourier benötigt rund 14 Prozent mehr Validierungs-Gesamtzeit. Die neue Ziffern-Vorhersagerunde war in Bearbeitung und ist hier nicht bewertet. |

Aktuelle Quellen:
[RH-Nulltemperaturbericht](/Users/stefanhamann/Documents/Codex/2026-09-04/scha-2/outputs/RH_Nulltemperatur_und_Ereigniscompiler_2026-09-08.md),
[Geometrie-Reuse-Ergebnisse](/Users/stefanhamann/Documents/Codex/2026-09-05/unt/work/geometry_reuse_search_20260908f/ERGEBNISSE.md),
[Spektralkostenvergleich](../pi-prime-event-log-2026-09-08/spectral-cost-gate/README.md).
Fremde Zeitmessungen wurden gelesen, nicht erneut gemessen.

## 6. Präziser Anschluss an das neueste RH-Ziel

Die RH-Session verwendet

    B(x)=xi(1/2+sqrt(x))/xi(1/2),    G(x)=B'(x)/B(x),
    c_m=(-1)^(m−1) G^(m−1)(4)/(m−1)!,
    q_n=4^n c_(n+1)/c_1.

Ihr Auftrag ist ein unabhängig aus der Quelle gewonnenes 0≤T≤I und ein
Einheitsvektor v mit <v,T^n v>=q_n für **alle** n. Die allgemeine
RH-Äquivalenz wird dort argumentiert; sie wurde hier nicht formal neu
bewiesen oder durch endliche Matrixprüfungen zertifiziert.

Für einen selbstadjungierten Kandidaten D wäre ein möglicher Anschluss
T=(I+D²/4)⁻¹. T ist automatisch ein positiver Effekt. Keine der benötigten
Quellenmomentenidentitäten folgt daraus automatisch. D und v aus gewünschten
Nullstellen oder einer erst angenommenen positiven Zielverteilung zu
rekonstruieren wäre keine unabhängige TFPT-Herleitung.

Auf dem 12+4-Träger hat T mindestens acht Eigenrichtungen zum Wert 1.
Das Zielmaß hat dort keinen Atom (entspräche einer Nullstelle bei s=1/2).
Ein v orthogonal zu den D-Nullmoden kann sie aber unsichtbar machen:
Dies ist eine Bedingung an den Readout, kein allgemeiner RH-Ausschluss.
Ein fester endlicher Spektralträger kann ohnehin nicht die volle unendliche
Zielverteilung reproduzieren.

Ein verlorenes Vorzeichen ist nicht die gegenwärtige RH-Lücke. Offen bleibt
die Identifikation einer unabhängig positiven Quelle mit genau dem
vollständigen arithmetischen Objekt. Schon det(I+4zσx)=1−16z² ist gerade,
mit Nullstellen z=±1/4. Für s=1/2+z liegen diese abseits der kritischen Linie.
Symmetrie allein erzwingt die benötigte Lage nicht.

## 7. Nächste Prüfung und Abbruchkriterien

Die gemeinsame Fortsetzung sollte den vorhandenen geladenen Operator-/
Bilinearzweig verwenden: Raum und Symmetrie typgerecht festlegen, zulässigen
Transport und Zustand aus derselben Quelle gewinnen und eine nichtstatische,
nichtverschwindende Antwort berechnen. Auf einer ausdrücklich gewählten
treuen endlichen Gibbs-Präparation wäre <[H,A]*[H,A]> > 0 ein erster
Dynamiktest; er ersetzt nicht die Auswahl dieses Zustands durch TFPT.

Für Quantendynamik müssen die Daten eine physikalische Hamilton-/Dirac-
Interpretation mit Zustand und Observable tragen. Für RH kommt die
allordentliche Momentenidentität hinzu, für Faktorisierung ein aus N
berechenbarer Mechanismus samt vollständiger Kosten.

Die konkrete einfache Variante endet bei unverändertem 12+4→8+8-
Ganzraum-Gleichsetzen, bloßer Wahl D=ΓJ mit D²=I, erneut ausschließlich
Clock-blindem Boundary-Zugriff oder nachträglichem Einsetzen des Zielspektrums.
Das schließt diese Varianten aus, nicht jede mögliche TFPT-Quantendynamik.

## 8. Hier tatsächlich nachgerechnet

- [probe.py](probe.py): 26 exakte symbolische Identitäten/Gegenmodelle,
  Ergebnisse und Quellhash in [results.json](results.json).
- Vorhandene Involutions-/Clock-Suite: erneut 12 Tests bestanden.
- Vorhandene Compiler-Clifford-Suite: erneut 18 Tests bestanden.
- Vorhandener separater Geometriezertifikatsprüfer: rationale Reflexion,
  Spurhindernisse, Boundary-Erreichbarkeit und symbolischer QWZ-Zylinder bestätigt.

Die Involutions-Suite gibt beim Import einen ResourceWarning über eine
nicht explizit geschlossene Quelldatei aus; alle Tests bestehen. Die
Importstelle wurde nicht geändert. Eigene Gegenmodelle und fremde Quellen-
Regressionen ersetzen keine physikalische Herleitung oder Fachbegutachtung.

Reproduktion vom Repo-Stamm:

    python3 -B experiments/inter-sheet-dynamics-audit-2026-09-08/probe.py
    python3 -B -m unittest discover -s experiments/theory-contracts/compiler-involution-types -p 'test_*.py'
    python3 -B -m unittest discover -s experiments/theory-contracts/compiler-clifford-bridge -p 'test_checker.py'
    python3 -B experiments/double-cover-rh-audit-2026-09-08/check_geometry_certificate.py

