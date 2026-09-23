# Übersehene Verbindung: dieselbe Quelle, derselbe Zustand, dieselbe modulare Dynamik

17. September 2026. Contract-Verdict: **PARTIAL**. Keine Ledger-/Paper-Promotion;
`closed_gate_ids=[]`. Gegencheck normal und mit `-OO` byteidentisch.

## 1. Ergebnis für den eigentlichen Lösungsweg

Der aktuelle D4-Vorschlag und die ältere modulare Rekonstruktionsroute müssen
mit den bereits bekannten Zustands-/Quellenausschlüssen zusammen gelesen werden.
Die entscheidende Aufgabe ist eine gemeinsame lokale, zustandserhaltende
Quellenabbildung. Die Suche nach immer weiteren endlichen Hamiltonoperatoren
bearbeitet diese Aufgabe nicht. Dies ist eine Schlussfolgerung aus vorhandenen
Strukturen und dem folgenden neuen Gegencheck, kein neuer physikalischer Selektor.

Die kompakte Erklärung: Eine Landkarte und ein Motor können einzeln korrekt sein
und trotzdem zu verschiedenen Fahrzeugen gehören. Genau dieses Zusammenfügen
getrennter Zeugen passiert in v438. Benötigt wird derselbe zugrunde liegende
Prozess, aus dem Algebra, Zustand und Zeitentwicklung gemeinsam hervorgehen.

## 2. Konkreter neu reproduzierter Fehler in v438

Quelle: `verification/v438_seam_hsmi_borchers.py`, insbesondere Zeilen 86–95
und 119–139; Hash im Checker. Der Originalaufruf ergibt 5 passed, 0 failed.
Er definiert K als reelle Diagonalmatrix und P als Raising-Shift und prüft

    [K,P]=P,
    exp(i t K) P exp(-i t K) = exp(i t) P.

Seine Ausgabe behauptet stattdessen die reelle Streckung

    Delta^(it) P Delta^(-it) = exp(-t) P.

Bei t=0.37 liefert derselbe Operator:

| Gegenprüfung | Maximaler Eintragsfehler |
|---|---:|
| Tatsächlich getestete Phasendrehung | 3.885780586188048e-16 |
| Gedruckte reelle Streckung | 0.43489413138931043 |
| Selbstadjungiertheit P=P* | 1.0 |

Das symmetrisierte P hat kleinsten Eigenwert -0.9876883405951377 und ist
ebenfalls kein positiver Translationsgenerator. Positivität des separat
gebauten P_line ändert die Eigenschaften dieses P nicht. Der spätere Boolean
`standard_pair` kombiniert Zeugnisse verschiedener Operatoren und beweist
kein gemeinsames Standardpaar und keine Inklusion von lokalen Algebren.

Mit nichtunitärer Konjugation exp(-tK) P exp(tK) folgt tatsächlich exp(-t)P
(Fehler 2.22e-16). Das ist imaginäre Zeit/analytische Fortsetzung; sie darf
nicht stillschweigend als die reelle modulare Automorphismengruppe gelten.

**Exakte normtheoretische Kontrolle:** Für jedes beschränkte P und unitäre U
gilt ||UPU*||=||P||. Aus UPU*=aP mit 0<a<1 folgt daher P=0. Sogar

    ||UPU* - aP|| >= (1-a)||P||.

Für diesen Shift ||P||=1 und a=exp(-0.37) ist die Schranke 0.3092656693626453.
Ein genauer nichttrivialer Borchers-Translationsgenerator muss folglich
unbeschränkt sein; größere endliche Matrizen können höchstens einen geeignet
kontrollierten, domänensensitiven Grenzwert darstellen. Die Quelle erwähnt
selbst eine offene kontinuierliche Montage. Der Befund widerlegt die konkrete
Bezeichnung des Phasenchecks, nicht den echten kontinuierlichen Satz.

**Korrekte Konvention:** Bei U(s)=exp(isP), P>=0, lautet die Borchers-Relation
Delta^(it) U(s) Delta^(-it)=U(exp(-2 pi t)s). Somit gilt auf geeigneter
gemeinsamer Domäne [log Delta,P]=2 pi i P. Für Delta=exp(-K) folgt
[K,P]=-2 pi i P und Delta^(it)=exp(-itK). Ein reelles Umskalieren von t
entfernt 2 pi, aber niemals den Unterschied zwischen exp(it) und exp(-t).

Primärquelle: [Araki–Zsido, Theorem 2.1 und Einleitung](https://arxiv.org/html/math/0412061v3).
Die Voraussetzungen umfassen gemeinsame lokale Algebren und einen gemeinsamen
zyklisch-separierenden Zustand bzw. ein gemeinsames treues Gewicht.

## 3. Warum der D4-Hom-Raum noch nicht die richtige Auswahlaufgabe ist

Der vorherige Contract `universalraum-d4-torsor-seam-20260917` findet korrekt
dim Hom=8192 und schlägt zusätzliche W-/Casimir-/Clock-Bedingungen vor. Solche
Bedingungen sind nur dann diskriminierend, wenn die verglichenen Operatoren
auf BEIDEN Seiten unabhängig vorliegen.

Sei X eine beliebige invertierbare Zuordnung. Definiert man einen noch fehlenden
rohen Operator nachträglich als A_raw=X^(-1) A_bank X, dann ist
X A_raw=A_bank X identisch erfüllt. Für einen Paarkanal gilt entsprechend

    W_raw = Y^(-1) W_bank (Lambda^2 X).

Damit ist auch Y W_raw=W_bank (Lambda^2 X) eine Tautologie. Der Zieloperator
kann seine eigene Herkunft nicht selektieren. Zuerst muss der rohe Operator
aus dem ursprünglichen Kernel und dessen Algebra kommen.

Umgekehrt ist dim Hom>1 allein kein Beweis für physisch verschiedene Welten:
verschiedene Koordinatenrepräsentanten können dieselben gesamten Prozesswerte
darstellen. Ob der Rest Eichfreiheit ist, entscheidet ein gemeinsamer
zustands-/operations-/lokalitätserhaltender Vergleich, nicht die Dimension
eines einzelnen Hom-Raums.

## 4. Ein bestehendes negatives Resultat war im Graphen praktisch unsichtbar

`universalraum-source-equivalence-decision-20260915/RESULTS.md` schließt eine
direkte lineare/Bogoliubov-Identifikation der freien gaußschen Seam-CAR-Felder
mit dem nativen Wechselwirkungsmodell aus, wenn dieselbe Abbildung den Zustand
erhält. Am dort abgesicherten Prüfpunkt g/Delta=1/20 gilt:

    Prob_native(ungerade Fermionzahl)=0,
    Prob_Gauss_mit_gleicher_Kovarianz(ungerade Fermionzahl)>0.47684946.

Zusätzlich unterscheidet der native W-Kanal die helle Zwei-Loch-Struktur von
rein zahl-/paritätsabhängigen Reparaturen. Das gilt in der dort genau definierten
64-CAR/60-CCR-Modellklasse, nicht für jede E8-Quelle oder alle nichtlinearen
Feldwörterbücher. Dieser alte Grundzustandsbeweis wurde hier gelesen, nicht neu
vollständig gerechnet.

Vor diesem Audit war sein Knoten `unknown`, ohne getestete Claim-Verknüpfung.
Die neue Indexdatei macht Frage, negatives Verdict und Scope auffindbar.
Insbesondere schließt das Resultat nicht die lokale E8-Simple-Current-Erweiterung
aus: diese erweitert die Feldalgebra, statt nur freie CAR-Moden umzubenennen.
Der W/E8-Vorzeichenanschluss war ebenfalls bereits bekannt und wird hier nicht
als neue Entdeckung ausgegeben.

## 5. Die vorhandene positive Struktur und ihre genaue Grenze

Die bestehende Kette `ARCH.CFT.01`, `GATE.METRIC.06`,
`SEAM.EQUIV.LATTICEVOA.01`, `SEAM.EQUIV.CROSSEDPRODUCT.01` und
`SEAM.EQUIV.UNIQ.01` verknüpft die ursprüngliche D5/A3/μ4-Struktur mit dem
holomorphen E8-Level-1-Netz. In dieser Klasse sind die Zentralzahlen 5+3=8,
die lokale Index-4-Erweiterung und ihre 248 Gewicht-eins-Ströme passend.
Die 128 ergänzenden Spinorfelder haben Gewicht eins und bosonische lokale
Statistik; sie sind keine 128 zusätzlichen linearen CAR-Erzeuger.
Voraussetzungen, Zitiertheoreme und die offene rohe Realisierung bleiben bestehen.

Bei gewähltem affine E8-Level-1-Vakuumnetz liefert Sugawara den konformen
Stresstensor T(z)=1/62 sum_a :J^a J^a:(z) in Standardnormierung und die
zugehörige Rotationsdynamik. Die Ganzzahligkeit und konforme Einbettung sind
keine neue TFPT-Herleitung. Zur lokalen Erweiterung siehe auch
[Chu–Zheng](https://arxiv.org/abs/0808.1458).

**Rekonstruktionskompression:** Angenommen Φ ist eine lokale normale
*-Isomorphie der tatsächlichen Netze und erhält den Zustand. Dann bestimmt
V(A Omega_raw)=Φ(A) Omega_E8 die unitäre GNS-Abbildung. Auf dem Tomita-Kern
gilt V S_raw=S_E8 V; nach Abschluss folgt

    V Delta_raw V* = Delta_E8,
    V J_raw V* = J_E8.

Die modulare Dynamik ist dann keine zusätzliche unabhängige Auswahl mehr.
Das setzt wirklich dieselbe Algebra mit demselben Zustand und kontrollierten
Abschlüssen voraus; einige endliche Korrelatoren reichen nicht.
Holomorphie allein wählt keinen normalen Zustand. KMS bezüglich der eigenen
modularen Gruppe ebenfalls nicht. Eine eigene physische Zeit-/Kernelzuordnung
außerhalb dieses Vakuumnetz-Vertrags bleibt gesondert nachzuweisen.

## 6. Der jetzt gerechtfertigte entscheidende Ansatz

Die Rohquelle muss eine gemeinsame lokale Zustandsfunktion liefern. An ihr
sind zwei verbundene, aber logisch verschiedene Anforderungen zu prüfen:

1. Eine echte halbseitige modulare Inklusion mit gemeinsamem Omega und positivem
   Translationsgenerator. Geometrisch passende Intervalle teilen einen Endpunkt,
   z.B. N=A((1,infinity)) innerhalb M=A((0,infinity)). Bei obiger Konvention
   Delta_M^(-it) N Delta_M^(it) subset N für t>=0. Beliebige kompakt ineinander
   liegende Intervalle erfüllen diese Bedingung NICHT automatisch.
2. Die unabhängige E8-Identifikation dieses Netzes: lokale μ4-Erweiterung,
   Niveau, 248 Stromgeneratoren samt den 128 Spinorströmen, gemeinsamer Zustand,
   Isotonie, Adjunktion und kontinuierlicher Grenzwert. HSMI allein wählt E8
   nicht; viele andere konforme Netze besitzen dieselbe Rekonstruktionsstruktur.

Die Stromgeneratoren sind ein entscheidender früher Falsifikationstest.
Ein Erfolg nur auf endlichen Matrizen oder einzelnen Stromkorrelatoren wäre
noch kein vollständiger Netzbeweis. Eine unabhängig bewiesene normale lokale
Φ mit Zustandserhaltung hingegen nimmt die modulare Dynamik automatisch mit.

Damit ist eine falsche vorhandene Brücke nachgewiesen und die nächste
Auswahlaufgabe präzisiert. Die physische rohe Quellenfunktion, 3+1D, chirales
Maß, wechselwirkendes Kontinuum und die übrigen T1–T8-Schlüsse sind hierdurch
nicht konstruiert. Es wird keine vollständige Lösung behauptet.
