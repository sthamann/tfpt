# Was dahintersteckt: kontrollierte Phasen, Aufzeichnungen und ihre Zusammensetzung

13. September 2026. Fortsetzung von [CONTEXT_INSTRUMENT.md](CONTEXT_INSTRUMENT.md).
NON-RH. Exakte endliche Quantenkonstruktion unter benannten zusätzlichen
Ausführungsprämissen; keine Herleitung der mikroskopischen TFPT-Dynamik.

## 1. Eine Korrektur der Aussage „Die Matrizen sind schon vorhanden“

Die Einzelspiegelungen R_j=I-2 Pi_j und der Registerbasiswechsel
W=J4/2-I liegen im Quellbaukasten. Daraus folgt **nicht**, dass die
kontrollierte gemeinsame Operation zwischen zwei Registern schon verfügbar ist.
Sie lautet

\[
Q_C=\sum_j |j\rangle\langle j|_A\otimes R_{C,j}
=I-2P_{\rm gleich},\qquad
P_{\rm gleich}=\sum_j|j\rangle\langle j|_A\otimes\Pi_{C,j}.
\]

P_gleich ist ein Rang-vier-Projektor auf dem 16-dimensionalen gemeinsamen
Raum. Q_C gibt genau den passenden Register/System-Basispositionen ein
Minuszeichen. Es ist eine echte Wechselwirkung zwischen den Registern,
nicht nur eine andere Schreibweise für getrennte Einzeloperationen.

Im rechnerischen Kontext hat Q_C Operator-Schmidt-Rang vier. Jede reine
Produktoperation U_A tensor U_S hat dagegen Rang eins; auch jede endliche
Folge ausschließlich solcher lokalen Operationen bleibt ein Produkt.
Damit ist die bisher offene Interregister-Kopplung präzise identifiziert.
Dass sie einfach ist, beweist noch nicht ihre Herkunft.

## 2. Die Kopplung besitzt eine überraschend kurze Gate-Zerlegung

Für zwei Zwei-Bit-Register a=(a0,a1), b=(b0,b1) ist das Vorzeichen

\[
(-1)^{\delta_{a,b}},\qquad
\delta_{a,b}=(1+a_0+b_0)(1+a_1+b_1)\pmod2.
\]

Dies ist ein quadratisches Binärpolynom. Die exakte Gate-Zerlegung lautet,
bis auf die ausdrücklich eingeschlossene globale Phase,

\[
Q=-Z_{a0}Z_{a1}Z_{b0}Z_{b1}
\,CZ_{a0,a1}CZ_{b0,b1}
\,CZ_{a0,b1}CZ_{a1,b0}.
\]

Nur die letzten beiden CZ-Gates verbinden verschiedene Register.
Die anderen Faktoren sind registerlokale Clifford-Operationen. Die
Vorzeichenwahrheitstabelle wird für alle 16 Basiszustände exakt geprüft.

**Der Gate-Typ selbst ist nicht neu:** CZ=I4-2|11><11| ist eine der
ursprünglichen Koordinaten-Wurzelspiegelungen. Neu vorausgesetzt wird seine
Anwendung auf ein Qubit des ersten und eines des zweiten Registers.
Wenn ein skalierbarer Compiler solche registerübergreifenden Verbindungen
bereits zulässt, kann er Q daraus bauen. Genau diese Freiheit der Verbindung
ist aber nicht durch das Vorhandensein eines isolierten Viererträgers
bewiesen. Die Herkunftslücke betrifft hier die erlaubte Zusammensetzung
und physische Kopplung der Träger, nicht eine noch unbekannte Einzelmatrix.

Für alle 15 ursprünglichen, aus den E8-Wurzeln rekonstruierten Kontexte
wurde außerdem die zugehörige vollständige Vor-Messoperation direkt auf
den acht Pauli-Generatoren der vier Qubits geprüft: Jede Konjugation ergibt
wieder ein Pauli-Wort bis auf Vorzeichen. Die Konstruktion ist damit eine
Clifford-Schaltung, nicht nur numerisch ähnlich zu einer solchen.

**Einordnung:** Unter Stabilizer-Präparationen, solchen Gates und
Pauli-/Stabilizer-Messungen bleibt dieser Teil klassisch effizient
simulierbar. Das ist etablierte Quanteninformatik, keine neue universelle
Rechenmethode; siehe [Aaronson–Gottesman](https://arxiv.org/abs/quant-ph/0406196).
Hier bleibt die Auswahl der nächsten Kontexte eine klassische Steuerung
nach K. Eine kohärente Sieben-Wege-Auswahl wird nicht hergeleitet oder
stillschweigend in den Clifford-Nachweis aufgenommen. Beliebige
Nicht-Stabilizer-Eingaben oder zusätzliche Gates liegen außerhalb dieser
Simulierbarkeitsaussage. Keine Aussage über universelle TFPT-Physik folgt daraus.

## 3. Ein exakt reversibler Messbaustein

Mit R0=I-2|0><0| auf dem Register und A=R0 W gilt A|0>=|+4>.
Definiere

\[
U_C=(W\otimes I)Q_C(A\otimes I).
\]

Dann gilt für jeden Systemvektor psi

\[
U_C(|0\rangle\otimes\psi)
=\sum_j|j\rangle\otimes\Pi_{C,j}\psi.
\]

Das ist eine Vor-Messung: Information wird zwischen System und Register
korreliert, nicht global vernichtet. Erst der Vertrag über das Auslesen
oder Weglassen des Registers bestimmt den reduzierten Messprozess.

Hier gilt sogar U_C²=I. Denn R0 auf dem Register kommutiert mit Q_C,
beide quadrieren zu I, und W²=I. Diese Identität wurde für alle 15
Quellkontexte geprüft. Sie betrifft diesen konkreten unitären Ausbau,
nicht jede denkbare physische Implementierung einer Messung.

## 4. Zusammensetzung hängt vom Zustand der Register ab

### Dasselbe kohärente Register wiederverwenden

Starte im rechnerischen Kontext mit |0>_A tensor |+4>_S.
Nach einer Anwendung steht dort der maximal verschränkte Zustand
sum_j |j,j>/2. Das System allein sieht aus wie I4/4.
Nach einer zweiten Anwendung desselben U_C erhält man aber exakt den
ursprünglichen reinen Zustand zurück, denn U_C²=I.

### Ein frisches Register pro Schritt verwenden

Mit zwei anfangs unkorrelierten |0>-Registern entstehen zwei
Aufzeichnungen. Nach ihrem Weglassen bleibt das System I4/4.
Die reduzierte Abbildung ist Delta_C(rho)=sum_j Pi_j rho Pi_j und
Delta_C²=Delta_C, nicht die Identität.

Der Prüfer unterscheidet exakt die Systemreinheiten:

| Ablauf | Reinheit Tr(rho²) |
|---|---:|
| Ein Schritt, Register weggelassen | 1/4 |
| Zweiter Schritt mit demselben weiterhin kohärenten Register | 1 |
| Zwei Schritte mit frischen Registern, beide weggelassen | 1/4 |

Es werden keine gemessenen Ergebnisse „magisch gelöscht“. Die Rückkehr
zum reinen Zustand verlangt Zugriff auf das noch kohärente erste Register.
Nach irreversibler Abgabe dieser Kohärenz steht diese Rückrechnung nicht
einfach zur Verfügung.

**Folgerung:** Die vorige Halbgruppen-/Markov-Beschreibung benötigt eine
Prämisse über frische, zurückgesetzte oder effektiv unkorrelierte Register.
Das ist kein automatisches Gesetz einer beliebig oft wiederholten
geschlossenen Matrix. Zurücksetzen kann Information an weitere Systeme
abgeben; deren physische Realisierung ist hier nicht konstruiert.

## 5. Die vollständige Kompositionsregel für beliebig viele Schritte

Für eine festgelegte Kontextfolge C1,...,Cn und frische Register gilt

\[
V_{C_n}\cdots V_{C_1}\psi
=\sum_{j_1,\ldots,j_n}
|j_1,\ldots,j_n\rangle\otimes
\Pi_{C_n,j_n}\cdots\Pi_{C_1,j_1}\psi.
\]

Dies folgt durch Induktion aus der geprüften Ein-Schritt-Isometrie.
Die Normquadrate der einzelnen Zweige sind die Wahrscheinlichkeiten
aufgezeichneter Messhistorien. Das Weglassen aller Register summiert
deren Dichtematrizen, nicht deren Amplituden. Die explizite Schaltung
verwendet n Register; eine Behauptung, dieser Speicherumfang sei unter
jedem anderen Zugriffsvertrag minimal, wird nicht gemacht.

Nach der ersten Rang-eins-Messung liegt das System auf einem der
ursprünglichen Strahlen. Bei klassischer Kontextwahl K folgen die
weiteren aufgezeichneten Übergänge deshalb genau der zuvor geprüften
60-Zustands-Matrix T. Für adaptiv gewählte Kontexte muss die jeweilige
Steuerungsregel explizit in die Historie eingehen.

Eine Projektion des ersten Registers auf |+4> würde stattdessen
Amplituden mit einem Faktor 1/2 addieren. Das ist eine postselektierte
andere Messung, nicht dasselbe wie Weglassen. Die Identität
sum_j Pi_(D,k) Pi_(C,j)=Pi_(D,k) rechtfertigt keine Gleichsetzung dieser
beiden Versuchsarten.

## 6. Ein einfaches Kompositionsgesetz des nichtselektiven Schattens

Jede Delta_C erhält genau die Identität und die drei Pauli-Komponenten
des Kontextes C. Alle anderen Pauli-Komponenten verschwinden. Folglich

\[
\Delta_D\Delta_C
=\text{orthogonale Projektion auf die gemeinsamen Pauli-Achsen}.
\]

Alle 225 Paare wurden als exakte Superoperatoren geprüft. Daher
kommutieren **alle diese nichtselektiven Kontextmessabbildungen**.
Bei zwei Kontexten bleiben:

- derselbe Kontext: Identität plus drei Pauli-Komponenten;
- ein gemeinsamer Pauli: Identität plus diese eine Komponente;
- disjunkte Kontexte: nur die Identität, also vollständige Depolarisierung.

Für beliebig viele festgelegte Kontexte bleibt der Schnitt ihrer
erhaltenen Pauli-Achsen. Das ist ein kleines algebraisches
Kompositionsgesetz, keine neue komplizierte Dynamikmaschine.

**Die vollständigen Instrumente sind trotzdem nicht vertauschbar.**
Für zwei Quellprojektoren P,Q mit Tr(PQ)=1/2 und Eingang rho=P gilt:

\[
\Pr(P\text{ dann }Q)=1/2,\qquad
\Pr(Q\text{ dann }P)=1/4.
\]

Die Kontexte sind hier vorgegeben; dies sind bedingte Ergebniswahrscheinlichkeiten,
ohne zusätzliche Kontextwahlfaktoren. Das gemittelte Endsystem verliert die
Reihenfolgeinformation, während benannte Ergebnisse sie weiterhin zeigen.
Gleiche nichtselektive Kanäle sind deshalb keine Gleichheit aller Protokolle.

## 7. Was das über den gesuchten fundamentalen Baustein sagt

Der genaue endliche Kandidat lässt sich jetzt kurz beschreiben:

> Kontext wählen; Register und System durch eine Gleichheitsphase koppeln;
> kohärente Aufzeichnung behalten, auslesen oder an andere Freiheitsgrade abgeben.

Die überprüften E8-Daten organisieren seine Basen und Spiegelungen.
Der reversible Teil ist eine konkrete Clifford-Kopplung; der irreversible
Schatten hängt vom Umgang mit Aufzeichnungen ab. Dies ist weder eine
Herleitung der Quantenmechanik selbst noch von Raumzeit oder Gravitation.

Die erste fehlende Herkunftsverbindung ist nun ausdrücklich die
**gemeinsame Kopplung Q_C mitsamt Zustands-/Registervertrag und Kontextwahl**.
Vorhandene lokale Spiegelungen allein reichen dafür nicht. Ein nächster
entscheidender Nachweis müsste Q_C oder einen operational gleichwertigen
Prozess aus den tatsächlichen mikroskopischen Quelloperationen gewinnen,
ohne die kontrollierte Kopplung als neues Gate vorauszusetzen.
Anschließend muss dieselbe Quelle erklären, wohin Aufzeichnungen gehen
oder wie sie zurückgesetzt werden; erst dann ist dauerhafte reduzierte
Markov-Dynamik durch die Konstruktion begründet.

## 8. Reproduktion

Der neue Prüfer besteht mit **640 eigenen exakten Guards** und 1.073
erneut ausgeführten Guards des Quellpräfixes. Normaler Lauf und -OO liefern
byte-identisches JSON. Der gemeinsame Vier-Prüfer-Lauf erkennt elf gezielte
Mutationen. Die drei neuen verwechseln die selektive Reihenfolge, ersetzen
die kohärente Wiederverwendung durch den Ein-Schritt-Zustand oder entfernen
eine der beiden gemeinsamen CZ-Kopplungen. Insbesondere würde die reine
Gleichheit der gemittelten Kanäle die falsche selektive Reihenfolge nicht
erkennen; der Test der tatsächlichen Zweischritt-Isometrie erkennt sie.

`record_composition.py` pinnt den vorherigen Quelladapter, der seinerseits
v783 pinnt. P0/P1 werden im Speicher mit immer aktiven Guards wiederholt.
Neue Prüfungen betreffen 15 unitäre Vor-Messungen, 120 Pauli-Konjugationen,
alle 225 Schatten-Kompositionen, kontrollierte Phasen und Registergegenproben.
Die allgemeinen Induktions- und Produktraumargumente stehen oben; endliche
Tests werden nicht als alleiniger Beweis aller n ausgegeben.

```sh
python3 -B experiments/theory-contracts/compiler-origin-audit-20260913/record_composition.py
python3 -B -OO experiments/theory-contracts/compiler-origin-audit-20260913/record_composition.py
```

Alle T1–T8 bleiben offen. Keine RH-Mechanismussuche und keine Übertragung
als RH-, Faktorisierungs-, P-vs-NP- oder Hylæan-Lösung.
