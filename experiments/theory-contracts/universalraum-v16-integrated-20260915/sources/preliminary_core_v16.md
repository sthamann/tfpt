# TFPT / Universalraum: Kernprobleme, neue externe Befunde und eigene Fortsetzung

Forschungsrevision **v1.6**, 14. September 2026.

Diese Revision konsolidiert zehn externe Texte, darunter die nachgereichten
Berichte von Kimi und Opus, und die eigenen parallelen Nachrechnungen. Sie ist
ein Forschungsbericht mit reproduzierbaren Belegen, **kein Beweis einer TOE**.
Die bisherigen Haupt- und Update-PDFs v1.5 bleiben erhalten und wurden in dieser
Runde zugunsten der vom Nutzer priorisierten Kernforschung nicht neu gesetzt.
Dieser Text ersetzt nicht stillschweigend das umfangreiche Hauptdokument.

## 1. Das wichtigste Ergebnis: eine lange Schleife fällt weg

Im bereits ausdrücklich definierten mikroskopischen Labor lässt sich der
nackte Vierfarbensingulettzustand Ω **mit einem einzigen Record exakt
heraldieren**. Ein zweiter, konstruktiv ausgeschriebener Einsatz derselben
Primitive liefert eine allgemeine destruktive Endmessung. Zusammen mit zwei
Echo-Aufrufen ergibt sich ein vollständiger endlicher Präparations-,
Aufzeichnungs- und Mehrzeitversuch, ohne angenommenen Ω-Projektor und ohne
unendlich lange Filterfolge.

Die Ergebnisse sind nicht nur jeweils getrennt passende Zahlen: Der
vollständige kohärente Schaltablauf mit seinen Recordregistern und sämtlichen
Abbruchgewichten wurde mit rationalen Amplituden gerechnet.

| Größe | Exaktes Ergebnis |
|---|---:|
| Ein-Record-Präparation gelingt | 3/8 |
| Präparation wird verworfen | 5/8 |
| Bedingte ideale Präparationsinfidelität | 0 |
| Endmessung als Effekt auf beliebigem Materiezustand | (3/8) PΩ |
| Roh-Erfolg, behaltenes Echo-Register | 9/64 |
| Roh-Erfolg, zwei frische Echo-Register | 153/2048 |
| Verhältnis frisch/behalten | 17/32 |
| R-Aufrufe im nicht vorzeitig abgebrochenen Ablauf | 4 |

**Was damit geschlossen ist:** die endliche, exakt ausgerechnete gemeinsame
Ausführung dieser drei Laboraufgaben unter dem benannten Ressourcenvertrag.
**Was damit nicht geschlossen ist:** die Ableitung dieser Ressourcen aus den
tatsächlichen P1/P2-Compileroperationen, die Präparation des ursprünglichen
C16-Grundzustands oder die Erzeugung einer physikalischen 3+1D-Welt.

Beleg: [vollständiger Prüfer](/Users/stefanhamann/Projekte/tfpt-theoryv4/experiments/theory-contracts/universalraum-six-new-audit-20260914/exact_one_record_protocol.py),
[531 exakte Bedingungen und Rohstatistiken](/Users/stefanhamann/Projekte/tfpt-theoryv4/experiments/theory-contracts/universalraum-six-new-audit-20260914/exact_one_record_protocol.json).

## 2. Der neue kleine Schaltablauf, vollständig hergeleitet

Wir verwenden vier Ququarts, jeweils durch zwei Bits dargestellt; das erste
Bit jedes Ququarts ist das niederwertige Bit. Definiere

\[
|\Omega\rangle=\frac1{\sqrt{24}}
\sum_{\pi\in S_4}\operatorname{sgn}(\pi)
|\pi(0),\pi(1),\pi(2),\pi(3)\rangle,
\qquad P^-_{ij}=\frac{I-S_{ij}}2.
\]

Die im nachgelieferten Forschungsfortsetzungstext vorgeschlagene Quelle ist

\[
|\xi\rangle=\frac14\sum_{d=0}^3\sum_{u,v=0}^1(-1)^{u+v}
|d,d\oplus2\oplus u,d\oplus1\oplus2v,d\oplus3\oplus u\oplus2v\rangle.
\]

Sie ist ein Stabilizerzustand. Eine vollständig überprüfte Herstellung aus
acht Nullbits benötigt vier H, sechs CNOT, vier X und zwei Z:

1. H auf Bits 0, 1, 2, 5.
2. Z auf Bits 2, 5.
3. CNOT 0→2, 1→3, 0→4, 1→5, 2→6, 5→7.
4. X auf Bits 3, 4, 6, 7.

Der eigene zusätzliche Befund ist die ganze Vektoridentität

\[
\boxed{P^-_{03}|\xi\rangle=-\sqrt{3/8}|\Omega\rangle.}
\]

Mit ξ_num=4ξ und Ω_num=√24Ω ist dies schlicht
(I−S03)ξ_num=−Ω_num, eine ganzzahlige Gleichung auf allen 256 Komponenten.
Die 16 Ausgangswörter enthalten zwölf Permutationen und vier Kollisionswörter;
die antisymmetrische Projektion auf genau dieser Kante erzeugt die vollständige
24-Wörter-Kombination mit den richtigen Vorzeichen.

### 2.1 Start: ein Record, keine approximative Kühlung

Die bereits konstruierte Primitive lautet

\[
R_{ij}=P^+_{ij}\otimes I_{\rm ptr}+P^-_{ij}\otimes X_{\rm ptr}.
\]

Herstellung von ξ, Pointerstart 0, R03 und Pointerausgang 1 liefern exakt Ω.
Der Ausgang 0 wird als Fehlversuch mit Wahrscheinlichkeit 5/8 protokolliert.
Die mittlere Zahl der Versuche bis zum Erfolg ist 8/3; dies ist keine
deterministische Präparation in einer fest begrenzten Zahl von Versuchen.

### 2.2 Ende: ein aus Operationen gebauter Effekt, kein hineingesetzter Projektor

Die adjungierte Identität lautet

\[
\langle\xi|P^-_{03}=-\sqrt{3/8}\langle\Omega|.
\]

Am Ende werden R03 mit neuem Pointer, der Ausgang 1, die inverse ξ-Schaltung
und anschließend acht Nullbits verlangt. Der erfolgreiche Krausoperator ist

\[
K_{\rm end}=-\sqrt{3/8}|0^8\rangle\langle\Omega|,
\qquad K_{\rm end}^{\dagger}K_{\rm end}=\frac38P_\Omega.
\]

Der Prüfer berechnet diese Zeile aus der wirklichen Schaltung für **jeden der
256 Basiszustände**. Linearität beweist damit den Effekt auf beliebigen
Zuständen, auch wenn das Materieregister mit einem anderen System verschränkt
ist. PΩ ist hier das nachträglich bewiesene Ergebnis, keine eingesetzte
Operationsressource.

Die Endmessung ist destruktiv und hat auch auf Ω nur Effizienz 3/8. Sie ist
keine perfekte nondestruktive Lüdersmessung mit Ausgangszustand Ω.

### 2.3 Mehrzeitvergleich einschließlich aller Register

Nach erfolgreichem Start wird C=(0 1 2) auf dem ersten Ququart angewendet,
zweimal R01 ausgeführt und anschließend C inverse. Im behaltenen Fall benutzt
man zweimal denselben **unvermessenen kohärenten** Pointer. Dann ist R²=I.
Im frischen Fall verwendet man zwei unabhängige Pointer und summiert die
Endwahrscheinlichkeiten über ihre Ausgänge.

Die Rohwahrscheinlichkeiten einschließlich Start- und Endineffizienz sind
9/64 und 153/2048. Nach Konditionierung nur auf den erfolgreichen Start sind
es 3/8 und 51/256. Erst nach zusätzlicher Kalibrierung der Endeffizienz 3/8
lauten die Rückkehrwerte 1 und 17/32. Diese drei Normierungen dürfen nicht
miteinander verwechselt werden.

Eine Zwischenmessung des behaltenen Pointers würde den kohärenten Echo-Test
ändern; bloßes Aufbewahren eines bereits klassischen Bits ist nicht derselbe
Versuch. Alle Vorbereitungsabbrüche sowie alle Endausgänge summieren sich im
Prüfer exakt zu Wahrscheinlichkeit eins.

### 2.4 Anschluss an das bereits konstruierte feste-Δ-Makro

Der v1.5-Vertrag für R enthält 70πℏ/Δ Hamiltonzeit einschließlich der endlichen
Q-Fenster. Er braucht weder Resonanzumschaltung noch negative Hamiltonzeit.
Die vollständigen 44D-/88D-Matrizen einschließlich Zuschauerphasen waren dort
geprüft; die aktuelle Robustheitsrechnung baut das Makro zusätzlich erneut auf.

Daraus folgen hier 280πℏ/Δ für einen nicht abgebrochenen Vier-R-Ablauf und
(17/3)·70πℏ/Δ für Präparation bis zum Erfolg plus einen anschließenden
Echo-und-Endversuch. Nicht enthalten sind ξ- und C-Gatter, Messung, Resets,
Schaltflanken oder Steuerung. Diese bleiben bezahlte Ressourcen.

Nicht mehr nötig für diesen Versuch: kontrollierte Gesamt-H-Entwicklung,
ein PΩ als Primitive, ein spektraler Produktfilter oder K^n mit n→∞.
Weiter nötig: adressiertes R, kohärentes belegungsabhängiges Q, die angegebenen
Cliffordoperationen, Pointer, Auslesen und eine Reset-/Steuerungsumgebung.

## 3. Die Quelle ξ ist optimal in der benannten Stabilizerklasse

Für beliebige reine oder gemischte Acht-Bit-Stabilizerzustände gilt

\[
\max_{\rho\in\mathrm{Stab}}\operatorname{Tr}(P_\Omega\rho)=3/8.
\]

Eine Clifford-Codeisometrie reduziert Ω auf den Vier-Bit-Zustand mit den
sechs vorzeichenbehafteten Trägern {6,7,9,11,13,14}. Konkret ist
V|b,c⟩=(1/2)Σa|a,a⊕b,a⊕c,a⊕b⊕c⟩. Das Bild ist ein Stabilizercode.
Projektion eines Stabilizerzustands auf diesen Code liefert null oder einen
unnormierten logischen Stabilizerzustand. Die Projektionswahrscheinlichkeit
ist höchstens eins und kann den folgenden Überlappbound nicht vergrößern.

Stabilizerzustände haben auf einem affinen Träger gleich große Beträge.
Die vollständige Enumeration der 307 affinen Teilräume von F2^4 gibt für
Dimension k=0,…,4 die maximalen Schnittgrößen 1,2,3,4,6. Damit ist
|Schnitt|²/(6·2^k) in jeder Dimension höchstens 3/8. ξ erreicht den Bound.
Die verwendete Normalform ist eine Standardaussage der Stabilizertheorie;
siehe [Dehaene und De Moor](https://arxiv.org/abs/quant-ph/0304125).

Das ist ein Optimalitätssatz für diesen Ressourcenvertrag, nicht für beliebige
Quantenpräparation. Insbesondere kann eine zusätzliche Nicht-Clifford-Ressource
den Vergleich ändern.

Die zuvor weitergerechnete K-Folge bleibt als mathematisches Kontrollresultat:

\[
p_n=\frac38+\frac3{128}64^{-(n-1)},\qquad
1-F_n=\frac1{1+2^{6n-2}},\quad n\ge1.
\]

Der Prüfer beweist dafür exakt Kr=−r/8 und Orthogonalität des Restes, nicht
nur einige Stichproben. Für die tatsächliche ξ-Präparation ist diese Folge
jetzt jedoch überflüssig. Belege: [Quelle und Optimalität](/Users/stefanhamann/Projekte/tfpt-theoryv4/experiments/theory-contracts/universalraum-six-new-audit-20260914/seed_and_protocol.py),
[all-n-Daten](/Users/stefanhamann/Projekte/tfpt-theoryv4/experiments/theory-contracts/universalraum-six-new-audit-20260914/seed_and_protocol.json).

### 3.1 Eine präzisere Herkunftsfrage für T1

Der vollständige Flagzeuge
W=|acc⟩⟨acc|⊗(PΩ−3I/8) hat Spektraldurchmesser eins. Auf einem
Stabilizereingang hat jedes vollständige Stabilizerinstrument Erwartung ≤0.
Der neue Ein-Record-Ablauf hat dagegen Erwartung

\[
\boxed{\langle W\rangle=15/64.}
\]

Somit beträgt der Abstand zu jeder solchen Stabilizerrealisierung mindestens
15/64 in halber Diamantnorm. Postselektion ist korrekt durch unnormierte
Erfolgszweige berücksichtigt. Eine ausschließlich stabilisierende Bedienung
kann diesen Record folglich nicht beliebig genau realisieren. Daraus folgt
**kein** Verbot allgemeiner P1/P2-Operationen: Deren tatsächliche erlaubte
Operationsklasse muss erst identifiziert werden.

Nebenbei wurde eine weitere Schaltungsvereinfachung exakt nachgerechnet:
CNOT(a→b), Fredkin(c;a,b), CNOT(a→b) ergibt Toffoli(c,b→a). Ein Fredkin ist
H am Pointer, R, H am Pointer. Also ein R, zwei CNOT und zwei Pointer-H,
ohne zusätzliches sauberes Hilfsbit. Dies ist kein Faktorisierungsalgorithmus
und kein Beweis polynomialer Gesamtressourcen.

## 4. Bauweise: was die E8-Wurzeln beweisen — und was nicht

Kimi favorisiert eine kantengetrennte Vermittlerbauweise; Opus erklärt eine
gemeinsam genutzte Zellbank für zwingend. Beide Schlussketten enthalten
zusätzliche physikalische Annahmen. Wurzelzählungen allein entscheiden die
Belegung, Statistik und räumliche Modenvielfalt nicht.

### 4.1 Fehlende Wurzelsumme ist kein Hard-Core-Beweis

Wähle E8-Wurzeln α=(1/2)^8 und
β=(1/2,1/2,1/2,1/2,1/2,−1/2,−1/2,1/2).
Ihre Summe ist keine Wurzel, ihre Differenz schon. Zwar verschwindet
[Eα,Eβ], aber

\[
\operatorname{ad}E_\alpha\operatorname{ad}E_\beta(E_{-\alpha})=-E_\beta\ne0.
\]

Im expliziten A2-Matrixbeispiel gilt [E12,E13]=0, jedoch
[E12,[E13,E21]]=−E13. Ein verschwundener Kommutator verbietet nicht das
Operatorprodukt oder eine gemeinsame Belegung. Opus' Hard-Core-Folgerung ist
dadurch als Folgerung widerlegt, nicht jedes Modell mit postuliertem Hard Core.

### 4.2 Ein innerer Wurzelgenerator ist nicht automatisch genau eine Raummode

dim gα=1 ist mit vier räumlichen Kopien desselben inneren Generators vereinbar,
etwa in g⊗C^4. Diese vier Labels sind zusätzliche Struktur, erhöhen aber nicht
die innere Wurzelraumdimension auf vier. Erst die zusätzliche Vorgabe
„Fockraum über genau einer endlichen Adjungierten pro Zelle und keine weitere
Multiplizität“ fixiert diese konkrete Modenzählung.

Eine zweite explizite Gegenkonstruktion zeigt: Ein geteilter Bosonmodus plus
Materielochlabels und der normierte Shift b†(n+1)^−1/2 reproduziert eine
bestimmte vierdimensionale Kantenmatrix; der lineare b†-Vertex liefert wegen
√2 dagegen eine andere Matrix. Das Gegenmodell bezahlt einen neuen
belegungsabhängigen Vertex. Es zeigt Nicht-Eindeutigkeit der Ableitung aus
den Wurzelzahlen, nicht Gleichheit mit der ursprünglichen linearen Quelle.

### 4.3 Was unter expliziten lokalen Ladungsannahmen tatsächlich folgt

Für additive volle Ladungsoperatoren Qv=nf,v+b†qvb und lineare unabhängige
Wedge-Vertices b†CeKe erzwingt Ladungserhaltung
(qv−ae(v)I)Ce=0. Verschiedene Endpunktladungen ergeben orthogonale aktive
Vermittlerbilder, auch ohne diagonale qv vorauszusetzen. Die aktive
Einbosondimension ist deshalb mindestens Σe rank Ce. Bei sechs voll aktiven
unabhängigen Wedge-Farbkanälen pro Kante wird daraus die Untergrenze 6|E|.

Dies ist ein echter bedingter Satz, aber keine Ableitung der gesamten
Fock-Tensorfaktorisierung. Im bereits auf Qv=1 eingeschränkten Raum ist eine
Prüfung von [H,Qv]=0 allein tautologisch und beweist die volle Quellherkunft
nicht. Belege: [Ursprungsaudit](/Users/stefanhamann/Projekte/tfpt-theoryv4/experiments/theory-contracts/universalraum-six-new-audit-20260914/core_origin_audit.py),
[nichtdiagonaler Ladungssatz](/Users/stefanhamann/Projekte/tfpt-theoryv4/experiments/theory-contracts/universalraum-six-new-audit-20260914/native/RESULTS.md),
[unabhängige Gegenprüfung](/Users/stefanhamann/Projekte/tfpt-theoryv4/experiments/theory-contracts/universalraum-six-new-audit-20260914/cell_coupling/SOURCE_CLAIMS.md).

## 5. Echte Dynamik aus der Quelle: Transport ist vorhanden, aber nicht allein

Eine Drei-Orte-Kette mit dem tatsächlichen Wedge-Vertex besitzt im lokalen
Qv=1-Raum 112 Zustände. Die Matrix B12 B01† ist nicht null, sondern hat
vollen Rang 24; ihr Betragsquadrat hat Spektrum 1 zwanzigfach und 4 vierfach.
Die Quellbindung erzeugt somit bereits Vermittler-Monomer-Transport.

Bei t/Δ=0,05 und Zeit ℏ/Δ ist die explizit nachgerechnete
Transportwahrscheinlichkeit etwa 2,95072·10⁻⁶; Entfernen der Zielkante
setzt sie auf null. Lokale Ladungserhaltung verbietet diesen Vorgang nicht:
Das Monomer trägt genau die Gegenänderung zum Vermittler. Ein frei hinzugefügtes
Bosonhopping ist dafür nicht nötig. Dies beweist noch keine abgeleitete
makroskopische Geometrie oder einen universellen Lichtkegel.

### 5.1 Zwei tatsächliche Sternzellen statt frei gewählter Transferparameter

Hier wechseln wir zur führenden Superaustauschordnung des nackten
256D-Laborsterns. Projiziert wird die Bindung λP+, nicht der volle
544D-Wedgeoperator. Die Zweisterne-Geometrie ist kein bereits hergeleitetes
C16-Tiling und die 31D-Kompression keine Fortsetzung desselben 112D-Trägers.

Der nackte Originalstern besitzt H*=JΣj P+0j, Grundzustand Ω und erste
Anregungslücke g=J/2 mit 30 Zuständen. Wir behalten Ω plus das **ganze**
erste Band: 31 Zustände pro Zelle, 961 für zwei Zellen.

Die Projektion einer ursprünglichen Blatt-Blatt-Bindung λP+ ergibt gemeinsam:

| Anteil | Fest berechneter Wert |
|---|---:|
| Transfer zwischen hellen Anregungen | λ/9, Rang 15 |
| Für diese Bindung dunkle erste Kanäle | 15 |
| Transfer bei Zentrum-Zentrum-Anschluss im ersten Band | 0 |
| Paarerzeugungsnorm aus ΩΩ | λ√15/9 |
| Bindungserwartung in ΩΩ | 5λ/8 |

Die Zahl λ wird im Quellenvergleich auf J gesetzt, nicht zur Kritikalität
nachjustiert. Die exakten Blattvektoren χi^A=P1 Ti^AΩ erfüllen
⟨χi^A,χj^B⟩=δAB/9 für dasselbe Blatt und −δAB/18 für verschiedene Blätter.
Zentralvektoren haben keinen Anteil im ersten Band.

**Pro hellem Farbkanal betragen Paarerzeugungs- und Transfermatrixelement
beide λ/9; die gesamte Paarerzeugungsnorm ist λ√15/9.**
Der volle projizierte Operator enthält zudem Farbwechselwirkungen und
Ein-/Zweianregungsübergänge. Das zahlenerhaltende Modell der vorigen Revision
kann deshalb nicht ungeprüft als native Dynamik übernommen werden.

Nur sein zahlenerhaltendes Kettenstück hätte κ/g=2/9 und Bandminimum 5J/18;
bei verschiedenen Blattanschlüssen J/3. Das ist kein Gapbeweis für die ganze
wechselwirkende Quelle. Die vollständige 961D-Kompression hat bei λ=J
numerisch E0=0,41666666666666646J und E1=0,75207294645443J. Das sind
Eigenwerte der expliziten Kompression, noch keine kontrollierten Eigenwerte
des vollen, vermittelnd gedressten Zweizellenmodells.

Belege: [Herleitung](/Users/stefanhamann/Projekte/tfpt-theoryv4/experiments/theory-contracts/universalraum-six-new-audit-20260914/cell_coupling/RESULTS.md),
[vollständige projizierte Matrizen](/Users/stefanhamann/Projekte/tfpt-theoryv4/experiments/theory-contracts/universalraum-six-new-audit-20260914/cell_coupling/projected_pair.npz).

## 6. Spektrale Ordnung: echte Zertifikate statt nur gefundener Eigenvektoren

Für den **kantenlokalen trunkierten** C16-Operator bei t/Δ=1/20,
Htr=H0+F4/800, ist jetzt der **gesamte 24024-dimensionale Singulettsektor**
kontrolliert. Darin liegen genau fünf Eigenwerte
unter 12,45J: ein einfaches Grundniveau und ein exakt vierfaches Niveau.

\[
11.960507412<E_0/J<11.960507414,
\]
\[
12.4469215409<E_1/J<12.4470238436,
\quad (E_1-E_0)/J>0.4864141269280.
\]

Die 28- und 80-dimensionalen Multiplizitätsblöcke wurden tatsächlich mit
vollständigen 24024D-Intertwineridentitäten konstruiert. Für den ersten Block
gibt es ein vollständiges ganzzahliges Polynom; für das korrigierte Quartett
exakte positive Spektralmomente, eine unabhängig bewiesene nächste
Niveauuntergrenze und daraus einen gültigen Templebound.

Fünf weitere primitive Youngblöcke der Größen 86,80,66,42,8 wurden vollständig
gebaut und ausgeschlossen. Ihre Htr-Untergrenzen sind 13,4888025606;
13,9820689612; 14,7757785284; 15,575089001; 17,5052599124. Die Beweise
verwenden ganze Gruppenalgebraidentitäten, vollständige modulare Matrizen,
CRT mit vorab bewiesenen Größenschranken und rationale Wurzelzählungen.
Ein unabhängiger Tr(X^32)-Bound kontrolliert ebenfalls sämtliche Eigenwerte
jedes neuen Blocks, nicht nur gefundene Ritzvektoren.

Die anschließende parallele Fortsetzung hat auch **alle elf übrigen
Singuletttypen mit 22260 Dimensionen** ausgeschlossen. Gewichtete
Translationsmittel und primitive S4- beziehungsweise S2×S3-Projektoren
liefern die Multiplizitätsgrößen 54/176/124/194/72 und
124/262/140/106/232/126. Für jeden wurden vollständige modulare Matrizen
mit Projektor- und Intertwineridentitäten aufgebaut. Sechs CRT-Primzahlen
plus eine unbenutzte Kontrollprime rekonstruieren Tr(X^32) exakt und
begrenzen damit sämtliche Eigenwerte.

Die schwächste neue Htr-Untergrenze ist **13,10732519J**, also noch
0,6603013464568J oberhalb der Quartettobergrenze. Zusammen mit den
vorigen Nullimpulszertifikaten schließt dies die gesamte
**Singulett-Zählpflicht**. 95 Projektorbedingungen und 166 Bedingungen
der abschließenden Momentenprüfung sind dokumentiert.

**Noch nicht geschlossen:** die Nichtsinguletts und der Transfer vom
trunkierten zum vollen mikroskopischen Operator. Ein Singulett-Grundzustand
ist ohne den ersten Nachweis nicht automatisch der globale Grundzustand.

Die Originalprüfer der externen Berichte wurden gezielt gelesen:

- Opus verwendet den nächsten **gefundenen** Ritzcluster als Temple-Separator.
  Ohne vollständige Zählung ist das keine untere Schranke an das nächste
  tatsächliche Niveau. Der so gemeldete globale Gap ist nicht zertifiziert.
- Kimi folgert aus einem Standard-Multiplizitätsniveau unmittelbar global
  „exakt vierfach“. Dazu fehlen ohne weitere Arbeit Einfachheit innerhalb
  des Blocks und der Ausschluss fremder Sektorkoinzidenzen.

Die neuen eigenen Zertifikate beheben diese Pflichten im ausdrücklich
kontrollierten Raum. Sie zertifizieren nicht rückwirkend den anderen,
geteilten Operator von Opus. Siehe [Spektralbericht](/Users/stefanhamann/Projekte/tfpt-theoryv4/experiments/theory-contracts/universalraum-six-new-audit-20260914/spectral/RESULTS.md),
[Nullimpuls-Erweiterung](/Users/stefanhamann/Projekte/tfpt-theoryv4/experiments/theory-contracts/universalraum-six-new-audit-20260914/spectral/global_followup/RESULTS.md),
[vollständiger Singulett-Abschluss](/Users/stefanhamann/Projekte/tfpt-theoryv4/experiments/theory-contracts/universalraum-six-new-audit-20260914/spectral/nonzero_followup/RESULTS.md) und
[externes Beweisaudit](/Users/stefanhamann/Projekte/tfpt-theoryv4/experiments/theory-contracts/universalraum-six-new-audit-20260914/spectral/global_followup/EXTERNAL_Q3_AUDIT.md).

Eine separate exakte Matching-Layer-Rechnung liefert für die kantenlokale
Qv=1-Konstruktion eine äußere Bandtrennung von 0,76Δ über acht rationale
LDL-Pivots. Bei 0,77 scheitert diese konkrete hinreichende Schranke bereits
am dritten Pivot. Äußere Bandtrennung ist nicht innere Anregungslücke und
nicht automatisch eine Schranke am dynamischen Schrieffer-Wolff-Rest.
Beleg: [Matching-Bandprüfung](/Users/stefanhamann/Projekte/tfpt-theoryv4/experiments/theory-contracts/universalraum-six-new-audit-20260914/matching_band.json).

## 7. Fehler, Kopplung und die Grenze unabhängiger Zellpräparation

Für einen vollständigen akzeptierten Zweig mit idealer Erfolgsmasse p0,
idealer Fehlmasse b0, kohärentem Gesamtfehler η und zusätzlicher
Instrumentdistanz q gilt

\[
p\ge(\sqrt{p_0}-\eta)_+^2-q,\quad
p_{\rm bad}\le(\sqrt{b_0}+\eta)^2+q.
\]

Die bedingte Infidelität wird erst **danach** durch Division mit der positiven
Erfolgsuntergrenze begrenzt. Für die neue Präparation ist p0=3/8, b0=0.
Über das ganze 70π-Makro genügen δH/Δ≤10⁻⁶ und zusätzliche Readoutdistanz
q≤10⁻⁷ für bedingte Infidelität ≤3,95914·10⁻⁷, sofern die übrigen
Ressourcen ideal sind. Die Hamiltonnormschranke umfasst nichtkommutierende
Leakage, nicht bloß einen gemeinsamen Zeitfehler.

Bei ausschließlich symmetrisch falsch gelesenen Recordbits mit
Wahrscheinlichkeit f gilt sogar exakt 1−Fcond=5f/(3+2f).

Der ganze Vier-Record-Versuch besitzt außerdem einen gemeinsamen robusten
Rohvergleich. Bei kohärentem Gesamtfehler η und weiterer vollständiger
Instrumentdistanz q je Modus gilt im relevanten kleinen Fehlerbereich

\[
p_K-p_F\ge\frac{135}{2048}
-2\left(\sqrt{9/64}+\sqrt{153/2048}\right)\eta-2q.
\]

Mit η≤280πδH/Δ, δH/Δ≤10⁻⁵ und q≤10⁻⁴ bleiben mindestens
0,05431202432 Rohabstand. Zusätzliche ξ-, Tick-, Decoder-, Schalt- und
Steuerfehler müssen in η oder q mitgezählt werden. Dies gilt pro gestartetem
Versuch einschließlich Präparationsabbruch, nicht ohne Weiteres für einen
unbeschränkt wiederholten Retry-Prozess. Ein solcher benötigt zusätzlich einen
uniformen Reset-/Speichervertrag. Beleg: [vollständiger End-to-End-Fehlerreview](/Users/stefanhamann/Projekte/tfpt-theoryv4/experiments/theory-contracts/universalraum-six-new-audit-20260914/robustness/ONE_RECORD_END_REVIEW.md).

### 7.1 Nicht jede alte Filterabkürzung ist mit ξ kompatibel

Die optimale Quelle enthält auch den nackten M=6-Sektor. Der alte
Neunfaktorenfilter auf einem kleineren erreichbaren Raum akzeptiert diesen
nicht korrekt: Die unabhängig gerechnete Kombination erzeugt etwa **1,67 %**
bedingte Fehlmasse. Der Prüfbericht enthält korrigierte F10-/F13-Alternativen;
für den neuen Ein-Record-Versuch werden diese Filter überhaupt nicht benötigt.
Ein kleiner erreichbarer Raum eines festen Protokolls ist außerdem nicht
unter beliebigen Recordkanten abgeschlossen. Ein expliziter S03-Eingriff
erzeugt den zuvor ausgeschlossenen M=2-Anteil.

### 7.2 Echte gekoppelte Dynamik und anschließendes Feedback

Für P_i=PΩ,i und eine Brücke V=P+ gilt
||P_i V(I−P_i)||=√15/8 exakt. In einem Vertrag aus **Kopplungsphase, dann
lokaler Kühlung** folgt

\[
q_{m+1}\le r(\sqrt{q_m}+\nu)^2+\epsilon,
\quad r=(187+3\sqrt{17})/256,
\quad \nu=z\lambda\tau\sqrt{15}/(8\hbar).
\]

Hier ist in einfacher Form r=(187+3√17)/256≈0,7787863941. Der positive
Kontraktionsfaktor gehört zum **dreifachen Stern-K-Feedback mit Reset auf ξ**,
nicht zum einzelnen neuen Präparationsrecord. P−03 allein hat Rang 96 und
liefert keine solche allgemeine Ω-Kühlrate.

Der positive Fixpunkt in x=√q ist
x*=[rν+√(rν²+(1−r)ε)]/(1−r); eine endliche Hülle ist
√qm≤x*+r^(m/2)(√q0−x*)+.

Mit τ=210πℏ/Δ, J/Δ=0,005, ε=0 und
zλ/J≤4,169130197908833·10⁻⁵ garantieren 61 Zyklen lokale Fehlmasse
unter 10⁻⁶ aus jedem Eingang. Das ist eine ausreichende, konservative
Garantie, keine Aussage, dass größere Kopplungen physikalisch scheitern.
Gleichzeitig aktive Brücken während aller Kontrollpulse sind damit nicht
ohne zusätzlichen Kompositionsbeweis behandelt.

Für den konkreten Anfang ΩΩ gibt es ein stärkeres neues Ein-Zyklus-Ergebnis:

\[
q_A'=q_B'=\frac{645}{1024}\sin^2(\lambda\tau/(2\hbar)),
\]

also Kontraktion 43/64 statt der allgemeinen 0,778786-Garantie. Dies wurde
auf allen 65536 Amplituden ganzzahlig nachgerechnet. Es ist noch kein
Mehrzyklenbeweis für den wechselwirkenden Grundzustand. Die lokale Kühlung
nach Ω und das Präparieren des tatsächlichen gekoppelten Grundzustands sind
unterschiedliche Aufgaben.

Belege: [vollständiger Fehlervertrag](/Users/stefanhamann/Projekte/tfpt-theoryv4/experiments/theory-contracts/universalraum-six-new-audit-20260914/robustness/RESULTS.md),
[Ein-Record- und Kopplungsfortsetzung](/Users/stefanhamann/Projekte/tfpt-theoryv4/experiments/theory-contracts/universalraum-six-new-audit-20260914/robustness/RESULTS_COUPLED.md).

## 8. Kosmologie: der vollständige lineare Modentransfer repariert die Spannung nicht

Die Datenprüfung geht nun über führende oder korrigierte Slow-Roll-Formeln
hinaus. Für das festgelegte Starobinsky-Potential
V=(3/4)M²(1−exp(−√(2/3)φ))² mit M²=c3^7 und c3=1/(8π) wurden
das volle homogene Hintergrundsystem sowie die skalaren Mukhanov-Sasaki-
und Tensor-Modengleichungen numerisch integriert.

Als explizites Vergleichsziel dienen die P-ACT-LB2-Zentralwerte
ln(10^10 As)=3,062 und ns=0,9752. Diese Daten und ihre Unsicherheiten
stehen in [ACT, Tabelle 5](https://arxiv.org/pdf/2503.14452v2).
Die Moden- und Vollpotentialperspektive ist außerdem in der geprüften
[primären Starobinsky-Analyse](https://arxiv.org/html/2510.18656v1) beschrieben.

| Bedingung | N* | As | ns | r |
|---|---:|---:|---:|---:|
| As auf den Zielzentralwert eingestellt | 54,24134 | 2,1370255·10⁻⁹ | 0,96442129 | 0,00364472 |
| ns auf den Zielzentralwert eingestellt | 78,53130 | 4,3792172·10⁻⁹ | 0,97520000 | 0,00179288 |

Bei passender Neigung ist die Amplitude somit **2,04921-mal zu groß**.
Bei passender Amplitude bleibt die Neigung deutlich unter dem gewählten
Zentralwert. Nicht nur ein vergessener führender 1/N-Term verursacht das.

Kontrollen: Bunch-Davies-Start bei k/(aH)=300,1000,3000; engere
Integratortoleranzen; zwei Schrittweiten der logarithmischen Ableitung;
unabhängige Integration der Krümmungs- statt Feldgleichung; geänderte
Hintergrundstarts; analytisch lösbare Power-Law-/Hankel-Normalisierung.
Die zwei skalaren Formulierungen stimmen beim Amplitudentest relativ auf
etwa 1,3·10⁻¹³ überein. Die verbleibende finite-Start-Abhängigkeit bei den
feineren Läufen liegt relativ unter 10⁻⁶ in As und unter 10⁻⁸ in ns.

Dies ist eine konvergenzgeprüfte numerische Rechnung, **kein Intervallbeweis,
keine vollständige Datenlikelihood und keine all-orders-Schleifenrechnung**.
Die Einstein-FLRW-Beschreibung und das Potential sind weiterhin vorgegebene
effektive Voraussetzungen, nicht aus der Mikroquelle abgeleitete Ergebnisse.

### 8.1 c3 kann nicht nur für die Kosmologie verstellt werden

Eine separate 70-stellige implizite Rechnung verfolgt dieselbe Parameteränderung
in die dokumentierte elektromagnetische Matchingformel. Die führende
Zentralwertanpassung verlangt c3≈0,0359650 statt 1/(8π), also etwa −9,61 %.
Bei unveränderter EM-Zuordnung wandert α inverse dann von
137,03599921684 auf etwa **167,80329863**. Die logarithmische lokale
Empfindlichkeit beträgt −2,00482144 und wurde unabhängig durch Differenzen
geprüft. Die vollpotentiale erste-Slow-Roll-Retuningsvariante ergibt sogar
etwa 168,67144505. Letzteres ist keine vollständige Modentransfer-Neuanpassung.

Es muss deshalb die gemeinsame physikalische Matchingableitung geprüft werden;
eine getrennte Anpassung derselben angeblich universellen Konstante ist keine
erhaltene Vorhersage. Gleichzeitig sind aus einer Zentralwertrechnung keine
präzisen Ausschlusssigmen ohne gemeinsame Likelihood abzuleiten.

Belege: [Modentransfer und Kontrollen](/Users/stefanhamann/Projekte/tfpt-theoryv4/experiments/theory-contracts/universalraum-six-new-audit-20260914/cosmology/RESULTS.md),
[numerische Daten](/Users/stefanhamann/Projekte/tfpt-theoryv4/experiments/theory-contracts/universalraum-six-new-audit-20260914/cosmology/verification.json),
[gekoppelte Parameterprüfung](/Users/stefanhamann/Projekte/tfpt-theoryv4/experiments/theory-contracts/universalraum-six-new-audit-20260914/parameter_transfer.json).

## 9. Kimi und Opus: wichtige Beiträge, aber einige Schließungen tragen nicht

Die beiden Texte wurden vollständig gelesen und ausgewählte zentrale
Originalprüfer direkt kontrolliert. Ihre gesamten externen Prüfsuiten wurden
nicht pauschal als unabhängig reproduziert ausgegeben. Detailurteile stehen
in [SOURCE_AUDIT.md](/Users/stefanhamann/Projekte/tfpt-theoryv4/experiments/theory-contracts/universalraum-six-new-audit-20260914/SOURCE_AUDIT.md).

Übernommen werden die nützlichen konkreten Gegenprüfungen, Bedingungslisten
und reproduzierbaren Operatorvorschläge. Nicht übernommen werden insbesondere:

- die allein aus Wurzelzählung erzwungene physische Bankarchitektur;
- der Schluss „Wurzelsumme fehlt, daher Hard Core“;
- ein global zertifiziertes Quartett aus unvollständigen Ritz-Clustern;
- ein vollständiges chirales 3+1D-Eichmaß aus endlichen Ketten mit gleich
  großen Links-/Rechtssektoren;
- eine universelle T2-Schließung aus dem Gewicht des **halbierten ganzen**
  Gluevektors: (1/2)^8 hat h=1, (1/4)^8 dagegen h=1/4. Dies sind
  verschiedene Vektoren; der tatsächliche physikalische Ladungsoperator fehlt;
- „genau ein zusätzlicher Flavourparameter fehlt“ aus einem endlichen
  Einparameterscan. Ein Scan zählt keine grundsätzlich benötigten Parameter;
- eine minimale Wärmemenge aus der bloßen Zahl verfügbarer Registerbits;
- eine universelle Fehlerbodenbehauptung aus dem Unterschied zwischen
  Produktvakuum und wechselwirkendem Grundzustand.

Ein weiterer einfacher Flavourtest bleibt wichtig: Wenn Yu=cuY0 und Yd=cdY0
auf demselben Profil beruhen, kommutieren die zugehörigen linken
Massenquadrate. Bei nichtentarteten Massen entsteht daraus keine physische
CKM-Mischung und keine CKM-CP-Verletzung. Mehr Profilparameter müssen also
auch die Ausrichtung zwischen Sektoren tatsächlich ändern, nicht bloß zwei
hierarchische Zahlen passend machen.

## 10. Gesamtstatus und die nächsten entscheidenden Beweise

**Die Laborstrecke ist deutlich einfacher und endlich exakt geworden. Die
Herkunft der bedienbaren Operationen und die gemeinsame skalierende Physik
sind weiterhin die zentralen offenen Schritte.** Keiner der T1–T8-Marker
wurde aufgrund dieser Revision auf geschlossen gesetzt.

Die nächste Reihenfolge ist sachlich konkreter als „noch mehr ähnliche Zahlen“:

1. **Die kleinste benötigte Primitive aus der Quelle gewinnen.** Ziel ist
   jetzt das eine R03 samt ξ-Cliffords, Q, Pointer und Auslesevertrag. Die
   starke 15/64-Ressourcenschranke sagt, welche rein stabilisierende
   Herkunftsbehauptung nicht genügen kann. Jede zusätzliche Operation
   benötigt ein Quellwort oder muss als neue physikalische Annahme erscheinen.
2. **Die tatsächlichen gekoppelten Zellen lösen.** Den nun abgeleiteten
   Transfer λ/9, die gleichzeitige Paarerzeugung und alle Farbterme gemeinsam
   behalten. Zuerst Fehler der 31-Zustände-Kompression kontrollieren, dann
   wachsende Systeme und mögliche kritische Punkte untersuchen. Kein frei
   eingesetztes κ und kein behauptetes unverändertes Produktvakuum.
3. **Vom vollständig gezählten Singulettsektor zum ganzen Modell.**
   Nichtsinguletts mit ausreichenden unteren Schranken ausschließen und
   mikroskopische Restintervalle übertragen. Die elf restlichen
   Singuletttypen sind in dieser Runde bereits erledigt. Jeder weitere
   ausgeschlossene Block muss sämtliche Eigenwerte erfassen. Für die
   Nichtsinguletts genügte der noch unbewiesene nackte Bound H0≥11,58J.
   Dort einseitige verschobene/Chebyshev-Zertifikate oder Inertia einsetzen:
   Die singulettspezifische beidseitige Normschranke darf wegen großer,
   energetisch harmloser positiver X-Eigenwerte nicht blind übertragen werden.
4. **Geladene Felder statt bloßer Ladungslabels konstruieren.** Der T2-Test
   bleibt das renormierte Half-Charge-Feld zwischen tatsächlichen Sektoren
   mit Energie-, Adjungierten- und Quellzuordnung. Danach dasselbe System
   auf chirale Materie, Eichmaß und Dimension prüfen.
5. **Die eine Parametermap bewähren oder korrigieren.** Mikroskopische
   Herkunft von M²=c3^7 und der EM-Zuordnung gemeinsam prüfen. Reheating,
   Datenlikelihood und mögliche physikalisch hergeleitete Korrekturen
   explizit behandeln; nicht mit getrennten Nachjustierungen ersetzen.
6. **Steuerung, Zeit und Gedächtnis in denselben Träger bringen.** Eine
   gebaute Uhr kann ein hineingeschriebenes Programm abspielen. Es fehlen
   weiter die quellenseitige Auswahl des Programms, Zustand, Referenz,
   Auslesung und der Ort, an den die verworfene Information abgegeben wird.

Für RH fehlt weiterhin das aus der tatsächlichen Quelle abgeleitete
arithmetische Testobjekt mit Vorzeichen- und Grenzwertkontrolle. Für
Faktorisierung fehlen eine vollständige Schaltung, Bitkomplexität und
Erfolgsausbeute; Toffoli-Zugang ist nicht deren Ersatz. Für P versus NP
liegt kein Beweis vor. Für Hylæan ist in dieser Runde kein neues System-
oder Konsolidierungsexperiment ausgeführt worden.

Die RH-/Faktorisierungsgraph-Skills wurden zur Neuheits-/Herkunftsprüfung
verwendet; ihre konfigurierten Forschungsquellen waren hier nicht verfügbar.
Deshalb wird weder ein aktualisierter Gesamtstand dieser Programme noch
eine Neuheitsgarantie aus den fehlenden Graphdaten behauptet.

### 10.1 Tatsächliche T1–T8-Anforderungen, nicht umbenannte Ersatzfragen

Die Zuordnung folgt der vom aktuellen `docs/OPEN_PROBLEMS.md` benannten
`RESEARCH_2026-09-09.md`, Abschnitt „Current T1–T8 acceptance map“.

| Tor | Tatsächliche offene Verpflichtung | Beitrag dieser Revision und Grenze |
|---|---|---|
| T1 | P1/P2, Dimensions- und Compilerentscheidungen herleiten | Kleinerer genauer Zielvertrag, 15/64-Ressourcenzeuge; Herkunft weiterhin offen |
| T2 | Wirkliche halbgeladene markierte E8-Seamalgebra und Limes samt Energie, Adjungierten, Ladung/Cocycle | Falsche Gleichsetzung zweier Gluevektoren ausgeräumt; das physische Feld bleibt ungebaut |
| T3 | Ein ausgewählter lokaler/quasi-lokaler unitärer 3+1D-Ursprung für alle Sektoren | Echte Zellbindung berechnet; Dimension und gemeinsamer Ursprung nicht hergeleitet |
| T4 | Chirales SM-Eich-/Weylmaß, Anomalien/Index und uniforme Spiegelentkopplung | Ein endlicher vektorartiger Kettenbefund ersetzt diese Pflichten nicht |
| T5 | Wechselwirkender Kontinuumslimes, Lorentzverhalten, Confinement/Clustering, Streuung | Ganze Singulett-Zählung und Quellenkopplung vorangebracht; weder Kontinuum noch Confinement bewiesen |
| T6 | Alle drei Eichkopplungen und vollständige Neutrinotextur samt Skala intern herleiten | Gemeinsame Parametervariation als Konsistenztest; keine Erledigung von Eich-/Neutrinomatching |
| T7 | Masseloser quantisierter Spin zwei, beide Helizitäten, universelle Kopplung aus demselben Ursprung | Kein neuer dynamischer Spin-2-Nachweis; Tensorprojektor allein genügt nicht |
| T8 | Physischen Anfangszustand auswählen und ein Quellenfunktional für sämtliche Auslesungen herleiten | Ein gemeinsamer endlicher Laborablauf ist konstruiert; natürliche Auswahl und universelles Quellenfunktional bleiben offen |

T6 ist in dieser Karte ausdrücklich **nicht bloß Kosmologiematching**.
Kein Tor wird durch das Umbenennen seiner Abnahme in einen kleineren
endlichen Test geschlossen. Der unabhängige [Protokollreview](/Users/stefanhamann/Projekte/tfpt-theoryv4/experiments/theory-contracts/universalraum-six-new-audit-20260914/protocol_review/RESULTS.md)
prüft diese Zuordnung und den vollständigen Ein-Record-Versuch erneut.

## 11. Reproduzierbarkeit und Evidenzklassen

Alle eigenen Änderungen dieser Runde liegen in diesem neuen Forschungsordner.
Fremde Änderungen, Ledger, Website, alte Papers und Commits wurden nicht
stillschweigend verändert. Die zehn Eingabetexte sind in `sources/` separat
erhalten; ihre Behauptungen sind Quellenmaterial, keine bindenden Anweisungen.

Die normalen und optimierten Läufe des 531-Bedingungen-End-to-End-Prüfers
liefern bytegleiche JSON-Ergebnisse. Er enthält Negativkontrollen gegen
fehlende ξ-Phase, falsche Recordkante und fehlende inverse Phase. Weitere
Module haben eigene genaue Prüfprotokolle; deren Zählungen sind keine
prozentuale Fertigstellungsanzeige der Theorie.

Ein abschließender [Kernreplay](/Users/stefanhamann/Projekte/tfpt-theoryv4/experiments/theory-contracts/universalraum-six-new-audit-20260914/core_replay.json) führt 14 gezielte Befehle
erfolgreich aus, einschließlich der unabhängigen 264-Bedingungen-Protokollrechnung,
der Herkunftsgegenbeispiele und des vollständigen Singulett-Zertifikats.
Fünf normale/optimierte Ergebnispaare sind bytegleich. Die vollständige
kosmologische Integration und alle externen Prüfsuiten sind nicht Teil
dieses kurzen Replays; ihre tatsächlich ausgeführten Prüfungen sind getrennt
dokumentiert.

| Teil | Evidenzklasse |
|---|---|
| Ein-Record-Start, Endeffekt, vollständiger Echovergleich | Exakte rationale Schaltung, 256D vollständig |
| Stabilizeroptimum, all-n-Rest, Toffoli-Konjugation | Exakte endliche Algebra plus benannte Normalform |
| Hard-Core-/Wurzelraum-Gegenzeugen | Exakte algebraische Gegenbeispiele |
| Aktive Vermittlerbilder und 112D-Transport | Bedingter Quellsatz plus expliziter dynamischer Test |
| Zweizellenkopplung | Exakte Projektoren/Koeffizienten; 961D-Energien numerisch |
| Quartett im genannten Spektralraum | Exakte Ganzzahl-/CRT-/Wurzelzählzertifikate |
| Robustheit | Bewiesene ausreichende Normschranken, explizite Fehlerverträge |
| Kosmologische Modeentwicklung | Konvergenzgeprüfte numerische effektive Theorie |
| Vollständige TOE, gemeinsamer 3+1D-Ursprung | Offen |

Die einzelnen Berichte und Prüfer sind Teil des Forschungsstands. Alte,
inzwischen überholte Laborwege bleiben zur Nachvollziehbarkeit erhalten und
werden nicht als aktuelle Mindestanforderung ausgegeben.
