# q* als Randmarkierung: exakter positiver Teil und genaue Grenzen

2026-09-14. NON-RH, Quellenprüfung und kleine endliche Algebra. Keine
Paper-/Markeränderung, keine neue Großkonstruktion und keine physische
Präparation, Zeit oder Chiralität aus endlichen Identitäten abgeleitet.

## Ergebnis

**Ja, für einen konkret vorhandenen Teil der Quelle:** Die ursprüngliche
15-Klassen-Verknüpfung ist unabhängig von q*. Alle sechs Arf-1-Markierungen
können nur in Randpräparation und Auslese stehen, während genau dieselbe
Verknüpfung ihre volle unmarkierte symplektische Symmetrie behält.

**Nein, nicht automatisch für alle zusätzlich markierten Strukturen:** Die
Selektorbedingungen, eine festgehaltene reelle signierte Wortalgebra, die
Familienoperation sigma und ein Gate-Zulassungstest, der q* erhalten muss,
sind zusätzliche Daten. Ihre volle gemeinsame Symmetrie ist kleiner. Eine
mittransformierte Familie q-abhängiger Regeln ist keine einzige q-unabhängige
Grundregel.

**Neuer konkreter Randzeuge:** Die sechs Ensembles aus jeweils fünf
ursprünglichen MUB-Kontexten, also zwanzig tatsächlichen Gaussian-Strahlen,
haben denselben mittleren Zustand, denselben Zweikopienmoment und denselben
nichtselektiven Messkanal. Ihre korrelierten Dreikopienmomente sind dagegen
verschieden. Dafür genügt bereits die Auslese am ursprünglichen Strahl e0.

## 1. Was die Originalquellen tatsächlich markieren

| Struktur | Ursprüngliche Formel bzw. Aussage | Rolle von q* |
|---|---|---|
| Symplektische Klassenverknüpfung | B_xy=[hb(x,y)=0], v774:883–941 | Kein q im Operator; q wählt einen Ovoid-Eigenvektor. |
| Sechs äquivalente Bezugspunkte | Sp(4,2) wirkt als S6 auf sechs Arf-1-Formen, v774:629–708 | Ohne Markierung kein bevorzugter Punkt. |
| Selektor | sigma-Invarianz, q(A)=1, q(F_Sigma)=0, v774:714–736 | Die Prämissen wählen genau eine Form. |
| Gewicht-/Trägerdictionary | iota=(f1,f2,f3,a,sum bits), q=wt(iota)/2, v774:437–439,759–781 | Die markierte Fünfslot-Zuordnung enthält q. |
| 1+5+10-Zerlegung | Stab(q*) hat Ordnung120 und wirkt als S5, v774:786–824 | Eine Zerlegung relativ zum festgehaltenen Bezugspunkt. |
| Hyperladungsdictionary | X=(-2,-2,-2,3,3), X(v)=X·iota(v), v774:1004–1041 | Benötigt zusätzlich die 3+2-Slotwahl, nicht nur q. |
| Gaussian-Reflexionen | R_z=I−zz†/2 für ||z||²=4, v783:608–629 | Kein q im Reflexionsoperator oder in der Definition der60 Strahlen. |
| Voller unmarkierter Compiler | G31/mu4=Clifford/U(1), Quotient Sp(4,2), v783:716–738,803–810 | Trägergruppe ohne q-Fixierung; kein Satz über eine ausgewählte physische Ablaufregel. |
| Metaplektischer Zulassungstest | rhoV(lift)q*=q*, v798:61–77,983–1025 | q ist hier eine Operator-Zulassungsbedingung, nicht bloß ein Randlabel. |

Die Quelle benennt die verbleibende Wahl selbst besonders klar:
[v776:735](/Users/stefanhamann/Projekte/tfpt-theoryv4/verification/v776_boundary_hamming_uniqueness.py:735)
prüft, dass A gegenüber A+F_Sigma eine andere eindeutige Form auswählt, und
bezeichnet die flag-root-Ankerbenennung als tragenden Teil des eingefrorenen
Selektors. Die Prämisse, dass die Naht überhaupt die betreffende Type-II-
Codebuchhaltung realisiert, bleibt in v776:12–27 und:900–932 ausdrücklich
offen. Daher ist »der Selektor ist unter seinen Prämissen eindeutig« nicht
»der unmarkierte Compiler wählt physisch selbst q*«.

## 2. Eine einzige q-unabhängige Grundregel mit markiertem Rand

Auf den fünfzehn nichtnull Klassen V\{0} setze die bereits ursprüngliche
Regel

    K_xy = [hb(x,y)=0]/7.

Für jede der sechs Arf-1-Formen q sei O_q={x!=0:q(x)=0}, |O_q|=5. Die
Quelle zählt unabhängig vom konkreten q:

    x in O_q:      1 Nachfolger in O_q,     6 außerhalb;
    x außerhalb:  3 Nachfolger in O_q,     4 außerhalb.

Damit ist die exakte, für alle sechs q identische Kompression

    K_coarse = (1/7) [[1,6],[3,4]].

Das ist nicht bloß eine kovariante Familie K_q: **die volle15×15-Matrix K
ist buchstäblich dieselbe**. Quelle:
[v779:1312](/Users/stefanhamann/Projekte/tfpt-theoryv4/verification/v779_gnet_gns_arf.py:1312).
Der neue Checker prüft alle sechs Partitionen und alle720 symplektischen
Permutationen, nicht nur eine beispielhafte Markierung.

Konkrete reine Randwahl: Präpariere die klassische Klassenverteilung
p_q(x)=1_{O_q}(x)/5 und lies nach n Anwendungen des festen K wieder O_q
aus. Dann exakt

    Pr_q[O_q nach n Schritten] = 1/3 + (2/3)(−2/7)^n.

q kommt nur in Startverteilung und Endereignis vor. Die gleichen Raten
folgen hier aus der festen Quelle K, nicht aus Kovarianz allein. Eine
Interpretation dieser Klassenverteilung als physisch ausführbare
Randpräparation ist weiterhin eine Zugangsprämisse.

Positivitätspräzision: K ist ein nichtnegativer Markovoperator, aber wegen
des Eigenwerts −2/7 kein positiver Hilbertraumoperator. Der ebenfalls bereits
in [v779:1334](/Users/stefanhamann/Projekte/tfpt-theoryv4/verification/v779_gnet_gns_arf.py:1334)
berechnete Doppelschritt erfüllt

    T=K²=(4I+3J)/49=(4/49)I+(45/49)Pi_uniform >= 0,
    T_coarse=(1/49)[[19,30],[15,34]].

Auch dieser positive, stochastische Transfer ist dieselbe q-unabhängige
Matrix. Die Wahl, dass genau ein solcher Schritt physisch abläuft, und
seine Zeitdauer sind damit nicht hergeleitet.

## 3. Kovarianz, feste Markierung und echte q-Unabhängigkeit

Für g in Sp(4,2) ist q^g=q∘g^{-1}; dann O_(q^g)=g O_q. Der ursprüngliche
Selektor transportiert korrekt, wenn **alle** Inputs transportiert werden:

    (sigma,A,F_Sigma,q) -> (g sigma g^-1,gA,gF_Sigma,q^g).

Alle720 Fälle sind exakt geprüft. Die Orbitgröße der q-Markierung allein
ist6; ihre festgehaltene Stabilisatorgruppe ist S5 mit Ordnung120. Werden
zusätzlich q und sigma festgehalten, bleiben nur6 Symmetrien. Das entspricht
der ursprünglichen, explizit stärker markierten Aut(C_fin)-Definition in
[v888:913](/Users/stefanhamann/Projekte/tfpt-theoryv4/verification/v888_finite_pfaffian_signature.py:913).
Ein zusätzlich festgehaltenes vollständiges Selektortupel (sigma,A,F_Sigma)
ist noch feiner: sein hier geprüfter Orbit hat240 Elemente. Diese Gruppen
dürfen nicht pauschal alle »die Compilersymmetrie« heißen.

Allgemeine Kovarianz allein genügt nicht: Der Markovprojektor P_q, der
innerhalb O_q und innerhalb seines Komplements jeweils gleichmäßig mittelt,
ist positiv, stochastisch und erfüllt P_(q^g)=g P_q g^-1. Dennoch ist
P_(q^g) ungleich P_q für geeignete g. q ist dann ein Programmparameter im
Operator. Der Checker weist diesen Unterschied exakt nach. Ihn in ein
klassisches Register zu verschieben und anschließend eine einzige größere
kontrollierte Matrix zu schreiben beseitigt diese Ressource nicht.

Die sechs gleichartigen Markierungen sind auch nicht mit allen16
quadratischen Verfeinerungen zu verwechseln. Die anderen10 haben Arf0 und
einen anderen Nullmengentyp; Sp transportiert die beiden Typen nicht
ineinander.

Eine weitere ursprüngliche q-Unabhängigkeit existiert auf geschlossenen
binären Supports: Für jeden Hamming-Codevektor c mit Summe der getragenen
V-Klassen gleich0 ist sum_x c_x q(x) unabhängig von der Verfeinerung.
Denn q'−q=hb(.,a), also verschwindet der Unterschied auf dem Nullsummen-
Support. Das ist genau die Canonicity Lemma in
[v852:458](/Users/stefanhamann/Projekte/tfpt-theoryv4/verification/v852_arf_vacuum_ovoid.py:458),
hier auf allen2048 Supports und allen16 Verfeinerungen geprüft. Das ist
eine Aussage über diesen binären geschlossenen Support, nicht über sämtliche
geordneten komplexen Loopamplituden.

## 4. Wo q die reelle Operatorstruktur tatsächlich trägt

Der konkrete geordnete Clifford-Cocycle ist eine **spätere algebraische
Erweiterung**, nicht die Operatorformel von v774 selbst:
[compiler-clifford-bridge/checker.py:60](/Users/stefanhamann/Projekte/tfpt-theoryv4/experiments/theory-contracts/compiler-clifford-bridge/checker.py:60)
deklariert epsilon(v,w)=sum_i v_i w_i+sum_(i>j) v_i w_j und die
Generatorquadrate g_i²=−I. Die ursprüngliche Gewichtsform aus v774 liefert
epsilon(v,v)=q*(v). Daher gelten in dieser signierten Erweiterung

    U_v²=(−1)^q(v)I,    U_v†=(−1)^q(v)U_v.

Ein reell-signierter Operatortransport U_v -> ±U_gv muss diese Quadrate
erhalten. Notwendig ist q(gv)=q(v). Volles Sp bei festgehaltener reeller
signierter Struktur ist somit ausgeschlossen; die q-erhaltende Gruppe ist
die richtige Grenze. Ein konkretes v,gv mit verschiedenem q steht in JSON.

Komplexe mu4-Phasen erlauben zwar U'_v=i^{ell(v)}U_v für eine lineare
F2-Funktion ell. Dann

    q'=q+ell,
    epsilon'(v,w)=epsilon(v,w)+ell(v)ell(w) mod2.

Die Kommutatorform bleibt, Quadrate und adjungierte Basisrelation ändern
sich mit q. Das ist ein Wechsel der reellen signierten Form innerhalb der
komplexen Algebra, nicht der Beweis, dass die reelle Markierung lediglich
in Zuständen vorkomme oder bedeutungslos sei.

Zusätzliche Transportgrenze: Die ursprüngliche Gaussian-Quotientenwirkung
auf V und die Wirkung auf einzelnen Pauli-Operatorlabels sind nicht dieselbe
Sp-Darstellung. v783:875–936 berechnet Hom-Dimension0; die korrekte
ursprüngliche Zuordnung ist **Klasse zu Pauli-Kontext**, nicht Klasse zu
Pauli-Punkt. Deshalb wird hier die spätere signierte Wortrealisierung nicht
stillschweigend mit der ursprünglichen G31-Wirkung auf C4 identifiziert.

Ein ausdrücklich ursprüngliches Operatorhindernis zeigt
[v798:1020](/Users/stefanhamann/Projekte/tfpt-theoryv4/verification/v798_seam_clifford_modular_s.py:1020):
Unter dem dortigen gesamten festen Stack — fehlender Clifford-Coset,
involutives metaplektisches Lift, Theta-Reellheit, q*-Fixierung und passende
T-Paarung — ist die Kandidatenmenge leer. Diese spezielle Obstruktion trifft
die Forderung nach einem q-erhaltenden Lift, nicht jede mögliche
q-unabhängige Randtheorie. Der volle46080-Census wurde hier gelesen, nicht
erneut ausgeführt.

## 5. q wird in drei korrelierten Randkopien sichtbar

Die originale class-to-context-Zuordnung wird unverändert aus
[v783:538](/Users/stefanhamann/Projekte/tfpt-theoryv4/verification/v783_two_qubit_clifford.py:538)
und dem hashgeprüften vorhandenen Source-Loader rekonstruiert. Für jede
Markierung q bilden die fünf Ovoid-Klassen fünf gegenseitig unverzerrte
Kontextbasen. Schreibe ihre20 echten normierten Gaussian-Projektoren als
P_r und

    M_k(q) = (1/20) sum_(r in20(q)) P_r^tensor k.

Der direkte exakte4×4-/16×16-Check ergibt für alle sechs q:

    M1(q)=I4/4,
    M2(q)=(I16+Swap)/20,
    D_q(rho)=(1/5)sum_r P_r rho P_r
            =rho/5+Tr(rho)I4/5.

Damit ist auch der **gesamte** nichtselektive gemittelte Messkanal gleich,
nicht nur sein stationärer Zustand. Selektive Outcome-/Kontextaufzeichnungen
sind damit gerade nicht gleichgesetzt.

Wähle für die Dreikopienauslese den originalen Strahl psi=e0. Dann

    p_q=<psi^tensor3|M3(q)|psi^tensor3>
       =(1/20)sum_r |<psi|r>|^6
       =1/16    falls der psi-Kontext in O_q liegt,
       =7/160   andernfalls.

Der erste Wert tritt für2 Markierungen auf, der zweite für4. Erklärung
direkt aus tatsächlichen Überlappungen: Im ersten Fall tragen der
Selbsttreffer und16 Überlappungen1/4 bei; im zweiten sechs Überlappungen1/2
undacht Überlappungen1/4. Für jeden der60 originalen Teststrahlen ist die
entsprechende Formel geprüft. Jeder Paarvergleich verschiedener q besitzt
einen solchen Strahlzeugen, aber ein einziges festes e0 ist allein kein
vollständiger Sechswege-Decoder.

Zusätzlich exakt, ohne64×64-Matrix:

    Tr M3(q)²=1/16,
    Tr(M3(q) M3(q'))=19/400      (q!=q'),
    ||M3(q)−M3(q')||_HS²=3/100.

**Wichtige Ressource:** M3 bedeutet drei Präparationen mit derselben
verborgenen Strahlwahl. Der Präparator darf diese Wahl klassisch behalten
und dreimal denselben bekannten Zustand herstellen; ein universelles
Klonen unbekannter Zustände wird nicht angenommen. Unabhängiges Neuziehen
des Strahls bei jeder Kopie liefert stattdessen (I4/4)^tensor k und löscht
q für jedes k. Bei zugänglichen Kontextlabels ist die Markierung bereits
am ersten Randrecord statistisch sichtbar. »Erstmals bei drei« gilt nur
für die genannten unbeschrifteten, gemeinsam korrelierten Ensembles.

## 6. Negatives Ergebnis: kein Rang16-Projektor aus der Reinheit

Die zusätzliche Vermutung M3(q)²=M3(q)/16 ist **falsch**. Es wurde dafür
nicht aus der Reinheit auf den Rang geschlossen, sondern der tatsächliche
20×20-Gram der symmetrischen Würfel gebildet:

    G_ab=<r_a|r_b>³.

Die Projektorvermutung würde G²=(5/4)G erzwingen. Für jedes der sechs q
liefert die exakte Rechnung dagegen

    (G²−5G/4)_(0,1)=3/16,
    ||G²−5G/4||_F²=45/4.

Die konkreten Strahlindizes stehen im JSON. Somit ist der behauptete
normierte Rang16-Projektor ausgeschlossen, und aus dieser Vermutung folgt
kein vierdimensionaler fehlender Korrelationsraum. Keine weitere Rang- oder
Spektralsuche wurde angeschlossen. Die gleichen ersten beiden Momente und
die unterschiedlichen dritten Momente bleiben uneingeschränkt bestehen.

## Reproduktion und Reichweite

- `checker.py`:2299 exakte Prüfungen; unveränderte ursprüngliche S2/S3-
  Teilabschnitte mit5 eigenen Quellchecks. Normal/-OO-JSON byteidentisch.
- `boundary_moments.py`:132 exakte Prüfungen; ursprüngliche v783-P0/P1-
  Teilabschnitte mit7 Quellchecks, unveränderter hashgeprüfter Source-Loader.
  Auch hier Normal/-OO-JSON byteidentisch.
- Quellpins, alle sechs Ensemblemitglieder, sämtliche60 Teststrahlwerte,
  Gegenbeispiele und Operatoridentitäten sind in den JSON-Dateien enthalten.
- Keine v774/v783-Vollsuite, keine physische Naht-/Clock-Realisierung, keine
  code-to-matter-Promotion. Die kleine positive Konstruktion zeigt genau,
  wie q in Randwahl und höherer Randkorrelation sitzen **kann**, nicht dass
  die ursprüngliche Naht diese Randwahl bereits physisch erzeugt.

## Unabhängige Prüfung des kleinen POVM-Korollars

Der von Root vorgeschlagene Folgeschritt benötigt keine zusätzliche
Spektralbehauptung und ist korrekt: Für Mbar=(1/6)sum_q M3(q) liefert der
obige Gram Tr(Mbar²)=1/20. Weil Mbar positiv, spurnormiert und auf
Sym³(C4), Dimension20, getragen ist, erzwingt die Gleichheit im
Reinheitsminimum Mbar=Pi_sym/20. Deshalb definieren

    E_q=(10/3)M3(q),     sum_q E_q=Pi_sym

einen Sechsausgangs-POVM auf dem symmetrischen Teilraum. Die Lüdersmessung
am Eingang Pi_sym/20 gibt jeden q-Record mit1/6 und konditional genau M3(q).
Die zugehörige Pretty-Good-Measurement für die gleichwahrscheinlichen
M3(q) erkennt den richtigen q mit5/24; jeder falsche einzelne r tritt
mit19/120 auf. Das ist keine perfekte Dekodierung.

Auf dem vollständigen Drei-Kopien-Raum ist ein zusätzlicher Ausgang
E_perp=I64−Pi_sym erlaubt. Eine vollständig explizite Instrumentvariante
hat Krausoperatoren

    K_(q,r)=P_r^tensor3/sqrt(6)    für r in20(q),
    K_perp=I64−Pi_sym.

Jeder der60 Quellstrahlen gehört zu genau zwei Markierungen, und aus der
Mittelwertidentität folgt sum_(r in60)P_r^tensor3=3Pi_sym. Die Krausoperatoren
sind daher vollständig. Am Eingang I64/64 sind die Wahrscheinlichkeiten
p(q)=5/96 und p(perp)=11/16; bedingt auf q entsteht M3(q). Hier braucht der
Eingang keine zuvor korrelierte verborgene Strahlwahl: Das Instrument erzeugt
die Korrelationen in seinem konditionierten Ausgang.

Die Beschränkungen sind wesentlich: Diese Krausvariante ist auf allgemeinen
Eingängen nicht dasselbe Instrument wie die Lüdersvariante, obwohl beide auf
dem genannten maximalgemischten Eingang dieselben bedingten Zustände geben.
Kovarianz wählt keines von beiden eindeutig aus. Die q-Labels sind jetzt
wirklich symmetrisch behandelte **Ausgänge**, keine vorgegebenen q-Werte im
Gesetz; dennoch bleiben der Drei-Kopien-Tensorzugang und die tatsächliche
Ausführbarkeit des Instruments zusätzliche physische Ressourcen. Die
ursprüngliche eindeutige sigma-/Anker-Selektion von q* ist nicht durch diese
bedingte, zufällige Randmarkierung hergeleitet.
