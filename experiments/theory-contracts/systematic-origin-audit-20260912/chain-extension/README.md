# Von einem geschlossenen Block zu einer ganzen Kette

12. September 2026. NON-RH. Bedingte alternierende Bell-Spinkette, keine
Herleitung ihrer physischen Auswahl aus TFPT und keine T1–T8-Schließung.

## Zusammenfassung

Die endliche Reparatur ist nicht auf fünf Stellen beschränkt. Eine einzige
Paarungsregel liefert auf jeder ungeraden Kettenlänge einen exakt unter den
Bell-Kopplungen invarianten Raum. Seine Größe wird allgemein bewiesen, nicht
aus einer Zahlenfolge extrapoliert. Das starre Anhängen von Zuständen verträgt
sich dagegen nicht exakt mit der neu eingeschalteten Verbindung.

Ein wesentlicher positiver Schritt besteht im Wechsel der richtigen
Grenzwertfrage: Auf der **vollen Algebra lokaler Observablen** besitzt die
festgelegte beschränkte Nachbarschaftswechselwirkung einen wohldefinierten
unendlichen Zeitentwicklungsgrenzwert. Dafür braucht man keine exakt
dynamikerhaltende Vorschrift zum Anhängen eines bestimmten Zustandsvektors.
Das folgt aus einem bekannten mathematischen Satz mit hier explizit geprüften
Voraussetzungen, nicht aus endlichen Simulationen.

## 1. Einfache Regel, beliebig viele endliche Stellen

Auf n=2m+1 alternierenden Faktoren V,V*,V,... betrachten wir nichtkreuzende
Paarungen mit genau einer freien, durchgehenden Linie. **Keine Paarung darf
diese freie Linie überspannen.** Jede Paarung identifiziert zwei Indexwerte;
der ungepaarte Index trägt den logischen Eingang aus C^d.

Die Zahl der Diagramme ist C_(m+1), die entsprechende Catalan-Zahl. Schließt
man die freie Linie mit einem zusätzlichen letzten Punkt, erhält man genau
die nichtkreuzenden vollständigen Paarungen auf 2m+2 Punkten. Somit

    C_k = binomial(2k,k)/(k+1),
    dim(Planarraum auf 2m+1 Stellen)=d C_(m+1),  d>=2.

| Stellen | Planare Paarungsrichtungen | Dimension bei d=4 |
| --- | --- | --- |
| 1 | 1 | 4 |
| 3 | 2 | 8 |
| 5 | 5 | 20 |
| 7 | 14 | 56 |
| 9 | 42 | 168 |

Allgemeine Unabhängigkeit: Bei d=2 verwandelt ein fester invertierbarer
epsilon-Basiswechsel an allen geraden Stellen die geschlossenen Bell-Paare
in Produkte von Klammern [ij]=x_i y_j-y_i x_j, bis auf Vorzeichen. In der
lexikographischen Variablenordnung x1>y1>x2>y2>... besitzt jede nichtkreuzende
Paarung ein anderes führendes Monom: x steht an linken, y an rechten
Paarendpunkten. Das zugehörige Dyck-Wort bestimmt die Paarung eindeutig.
Verschiedene führende Monome beweisen lineare Unabhängigkeit. Eine Relation
bei d>2 würde nach Projektion aller Indizes auf einen festen zweidimensionalen
Teilraum eine verbotene Relation bei d=2 liefern.

Die Gram-Kontraktion zweier Diagrammabbildungen ist ein skalares Schleifengewicht
mal I_d. Deshalb impliziert diese Unabhängigkeit die volle Rangformel d C_(m+1).
Der Nachbarprojektor verbindet bestehende Partner um oder verschiebt die freie
Linie; er verlässt die planare Klasse nicht. Die bekannte TL-Relationsfamilie
bleibt auf jeder Länge exakt. Gram-Orthonormalisierung liefert wie beim
Fünferblock eine isometrische Beschreibung mit exaktem H-Intertwining.

**Nicht behauptet:** Dieser Raum ist für d>2 der vollständige fundamentale
U(d)-Darstellungssektor; nichtplanare Abbildungen können weitere Kopien liefern.
Auch die minimale H-Hülle beliebiger Startzustände ist hiermit nicht auf jeder
Länge klassifiziert. Die Dimension wächst; ein gleich großer Viererraum wird
nicht auf allen Stufen erzwungen. Siehe [diagrams.md](diagrams.md).

## 2. Anhängen ist nicht Einschalten

Die normierte Anhängeisometrie lautet W_n psi=psi tensor Phi_d. Für die
einheitliche Kette H_n=sum_(j=1)^(n-1)(I-P_j,j+1) gilt exakt

    W_n* H_(n+2) W_n=H_n+cI,    c=1-1/d².

Das neue letzte Paar ist bereits im Grundzustand. Die einzige neue wirksame
Stelle ist die Verbindung vom bisherigen Endpunkt zum angehängten Paar.
Setzt man D=H_(n+2)W_n-W_n H_n, dann

    D*D=cI,
    (D-cW_n)*(D-cW_n)=c(1-c)I=(d²-1)/d^4 I.

Bei d=4 bleibt nach bestmöglicher skalarer Energiesubtraktion eine
Leckage-Grammatrix 15/256 I. Sie wird nicht dadurch kleiner, dass die alte
Kette länger wird. Ein kompatibler Hilbertraum-Inklusionsplan ist deshalb
noch keine exakt kompatible Folge verbundener Zeitentwicklungen.

Eine konstruktive Alternative existiert schon beim ersten Wachstumsschritt:
Für H_lambda=lambda(I-P12)+(I-P23), lambda zwischen0 und1, gibt es einen
glatten, durchgehend separierten Grundraumweg vom angehängten Paar zum
Dreier-Grundencoder. Die exakte minimale Lücke ist

    min gap = 2 sqrt(d²-1)/d² >0.

Das ist ein möglicher langsamer, **extern gesteuerter** Zustandsaufbau, kein
Beweis autonomer Verfeinerung und keine längenunabhängige Schranke für weitere
Schritte. Eine echte adiabatische Fehler-/Laufzeitbehauptung braucht zusätzlich
einen Zeitplan und die entsprechenden Fehlerabschätzungen; vgl.
[Jansen–Ruskai–Seiler](https://arxiv.org/abs/quant-ph/0603175).
Exakte Rechnung und Kontrollen: [append.md](append.md).

## 3. Lokale Beobachtungen brauchen keinen starren Zustands-Anhängeplan

Betrachte A am ersten Faktor. Vergleiche seine Heisenbergentwicklung in einer
n-gliedrigen und einer um zwei Faktoren verlängerten offenen Kette. Die
Einbettung der Observablen ist immer A -> A tensor I, unabhängig vom Zustand.

Ein Kommutator mit einer Nachbarschaftskopplung kann die Unterstützung höchstens
um eine Stelle erweitern. Deshalb stimmen die ersten verschachtelten
Kommutatoren ad_H^k(A) für k<n exakt überein. Erst bei Ordnung n kann die neue
Verbindung am bisherigen rechten Rand auftauchen. Dies folgt allgemein aus
Unterstützung und Kommutativität disjunkter Faktoroperatoren.

`local_response.py` bestätigt die Aussage mit konkretem nichttrivialem
Endpunktoperator und prüft zugleich, dass die Randwirkung nicht für immer
verschwindet. Bei n=3 tritt sie in Ordnung3 auf, bei n=5 in Ordnung5.
Für d=4,n=3 hat der Unterschied in Ordnung3 die normierte quadratische
Hilbert-Schmidt-Norm3/2048, also ist er exakt ungleich null.

Eine solche Aussage ist kein scharfer relativistischer Lichtkegel. Sie erklärt,
warum die lokale Antwort auf entfernte Randänderungen kontrolliert werden kann,
obwohl endliche Zeitentwicklungen nicht exakt unter Volumeninklusion identisch sind.

## 4. Bedingte Existenz einer unendlichen Dynamik ist damit abschließbar

Fixiere jetzt ausdrücklich die Halbgerade Gamma=N mit Abstand|x-y|, an jedem
Ort die Algebra M4 und die lokalen Einbettungen A_X -> A_X tensor I.
Ihre Normvervollständigung ist die quasilokale Spin-Algebra. Setze

    Phi({j,j+1})=I-P_j,j+1,   sonst Phi(X)=0.

Die Beiträge sind selbstadjungiert, haben Norm1 und Reichweite1. Mit
F(r)=(1+r)^(-2) gelten die expliziten Voraussetzungen:

* sup_x sum_y F(|x-y|) <= pi²/3-1 <infty.
* Der F-Faltungskonstante genügt C_F<=8||F||: Teile die Summationsstellen
  danach, welcher der beiden Abstände wenigstens die Hälfte von|x-y| ist.
* Die Interaktionsnorm ||Phi||_F ist höchstens4: am selben Punkt höchstens
  zwei Kanten, für Nachbarn ein Beitrag geteilt durch F(1)=1/4, sonst null.
* Für F_mu(r)=exp(-mu r)F(r) funktioniert dieselbe Abschätzung mit
  ||Phi||_(F_mu)<=4exp(mu).

Der Satz von Nachtergaele–Sims, §3.1, Theorem3.1, liefert deshalb den Normgrenzwert

    alpha_t(A)=lim_(Lambda -> N) exp(it H_Lambda) A exp(-it H_Lambda)

für jedes lokale A und anschließend auf der Normvervollständigung. Der
Grenzwert ist von der wachsenden Ausschöpfungsfolge unabhängig, gleichmäßig
auf kompakten Zeitintervallen und eine stark stetige Gruppe von
*-Automorphismen. Sie erfüllt eine Lieb–Robinson-Abschätzung.
[Primärquelle und Theorem](https://arxiv.org/pdf/1004.2086).

Damit ist **die Existenz einer wohldefinierten unendlichen lokalen Dynamik
für dieses ausdrücklich gewählte eindimensionale Modell** begründet. Der
lokale Generator lautet

    delta(A)=i sum_(Kanten mit Kontakt zu supp(A)) [Phi(Kante),A],

eine endliche Summe. Die formale unendliche Energiesumme muss nicht als
beschränkter Operator existieren. Für einen lokalen Träger von Intervalllänge
ell gilt bei einheitlicher KantennormJ außerdem

    ||delta^k(A)|| <= (2J)^k product_(r=0)^(k-1)(ell+2r+1) ||A||,

was lokale analytische Vektoren für die Ableitung liefert. Die Dynamik ist
für die festgelegte Wechselwirkung bestimmt, nicht durch die Symmetrie allein.

Dieser Grenzwert benutzt die **volle lokale Observable-Algebra**, nicht nur
die kleineren planaren Zustandsräume aus Abschnitt1. Er behauptet deshalb
keinen bereits konstruierten unendlichen planaren Grundzustand und keine
Kompatibilität ihrer Anhängeisometrien mit der Zeitentwicklung.

Die externe theoremgestützte Ableitung ist getrennt von den endlichen
Prüfprogrammen zu bewerten. Ein grüner Prüfer beweist den externen Satz nicht.

### 4.1 Mindestens ein unendlicher Grundzustand und ein positiver Generator

Wähle zu jedem H_N eine Grunddichtematrix rho_N und erweitere sie außerhalb
des Intervalls durch einen festen Produktzustand. Die separable quasilokale
Algebra hat einen schwach-* kompakten, metrisierbaren Zustandsraum. Daher
konvergiert eine Teilfolge gegen einen Zustand omega.

Für A mit Träger in1,...,k gilt ab N>=k+1 bereits exakt [H_N,A]=-i delta(A).
Mit E_N=min spectrum(H_N) folgt

    -i omega_N(A* delta(A))
      =Tr[rho_N A*(H_N-E_N)A] >=0.

Der Teilfolgengrenzwert erfüllt dieselbe Grundzustandsbedingung. Für die
vorausgesetzte beschränkte endliche Reichweite ist die lokale Algebra ein
Ableitungskern. Standard-GNS-Rekonstruktion liefert dann

    pi_omega(alpha_t(A))=exp(it K_omega) pi_omega(A) exp(-it K_omega),
    K_omega>=0,    K_omega Omega_omega=0.

Quellen: Nachtergaeles
[Vorlesungen, Propositionen6.1/6.3 und §7](https://www.math.ucdavis.edu/~bxn/LectureNotes/JvN_lecture_notes_S2016_abcde.pdf).
Der dortige Kommutatorgenerator ohne i erklärt den Faktor -i hier.

Dies beweist die Existenz mindestens eines stationären positiven Energieträgers
für die gewählte Kette. Es bestimmt weder einen eindeutigen Grenzzustand noch
eine explizite Wellenfunktion, Konvergenzrate, Reinheit oder Spektrallücke.
K_omega ist ein relativer Anregungsenergie-Generator, kein Normgrenzwert der
extensiven H_N. Keine physische TFPT-Auswahl wird daraus abgeleitet.

## 5. Was damit gelöst ist und was offen bleibt

Gelöst im vorausgesetzten Kettenmodell:

- Planare Bell-Operationsräume auf jeder ungeraden endlichen Länge, mit
  allgemeinem Dimensions- und Invarianzbeweis.
- Exakte Grenze des starren Anhängens und ein separierter erster Aufbaupfad.
- Existenz der unendlichen quasilokalen Dynamik aus einer Standardtheorie
  mit explizit erfüllten Voraussetzungen.
- Nichtkonstruktive Existenz mindestens eines unendlichen Grundzustands mit
  positiver unitärer Energiedarstellung für genau diese Dynamik.

Offen bleibt die entscheidende TFPT-Auswahl: Warum diese physischen Faktoren,
diese Nachbarschaft, genau diese Kopplung, Präparation und Zeiteinheit? Eine
eindimensionale Spin-Dynamik ist weder3+1D-Raumzeit noch chirales Standardmodell,
Gravitation, RH-Positivität oder ein Faktorisierungsalgorithmus.

Auch ein eindeutiger unendlicher Grundzustand, eine längenunabhängige
Spektrallücke, Zustandsrekonstruktion auf dem Rand, ein Kontinuums-/Skalenlimit
und effizienter physischer Zugriff sind nicht durch den Dynamikexistenzsatz
mitgeliefert. Thermodynamischer Grenzwert und Kontinuumsgrenzwert sind verschieden.

Die präzisere Suchrichtung lautet deshalb: **Eine gemeinsame Algebra lokaler
Operationen mit konsistenter Dynamik**, und erst darauf ausgewählte Zustände
und deren geometrische Beschreibungen. Dies ist eine kontrollierte Modellroute,
kein als universelle Lösung validiertes fundamentales Objekt.

## Reproduktion und Evidenzklassen

`run_checks.py` führt die drei neuen Prüfer jeweils normal und unter -OO aus.
Alle sechs Ausführungen bestehen mit identischen JSON-Ergebnissen je Paar.
`verification.json` hält Ergebnis und Code-Hashes fest. Die Diagrammprüfung
umfasst 3535 exakte Kontrollen, die Anhängeprüfung124; hinzu kommen die
lokalen Kommutatorprüfungen. Die allgemeinen Beweise stehen in den Notizen.

Die fünf vorherigen Dynamik-Reparaturprüfer wurden ebenfalls in zehn
Ausführungen erfolgreich wiederholt (`previous_dynamical_verification.json`).
Damit sind die aktuellen beiden Suiten in16 Ausführungen geprüft. Die
Anwendung des externen unendlichen Grenzwertsatzes ist eine analytische
Voraussetzungsprüfung, kein durch diese Skripte maschinell bewiesener Satz.
Kein vollständiger TFPT-, Vakuum-, Streuungs- oder Kontinuumstest wird behauptet.
