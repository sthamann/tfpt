# Woher könnte die Clock-Wechselwirkung kommen?

2026-09-08. Quellen-Audit nach
[clock-neutral-access](../clock-neutral-access/README.md). Keine neue
Wechselwirkung in eine bestehende Quelldatei eingesetzt.

**Ergebnis:** Die ursprüngliche 16-Majorana-Quelle erzeugt den vorgeschlagenen
gemischten Viererterm nicht durch quadratische Evolution, Lie-Abschluss oder
gaußsches Integrieren. Diese Grenze lässt sich exakt beweisen. Im getrennten,
bereits vorhandenen kompakten-U(1)-Gitterparent gibt es dagegen eine echte
nichtgaußsche Eingangskante: elektrische Dynamik macht die Transport-
Koeffizienten nichtkommutativ und erzeugt einen nachgerechneten quartischen
Anteil. Dessen Zuordnung zur 16-Majorana-Clock ist noch nicht hergeleitet.

## 1. Die ursprüngliche Quelle ist tatsächlich quasifrei

In `seam_state_derivation_probe.py` wird A_int in Zeilen 608–617 als reelle
antisymmetrische **16x16-Matrix** aufgebaut; A0 folgt in 618–627. Der Name
`A_int` bedeutet dort Kanal-Mischung, nicht eine quartische CAR-Wechselwirkung.
Mit D=u A0+t A_int lautet die schon geprüfte Hebung

    H(D)=(i/4) gamma^T D gamma.

Die Funktion `kms_A_gen` in Zeilen 634–639 diagonalisiert eine Einteilchen-
matrix und wendet die Fermi-Funktion an. `pf4_of` in 658–664 bildet einen
Vierpunkt-Pfaffian aus dieser Kovarianz. `wick_factory` in 687–706 berechnet
höhere Momente ausdrücklich durch Wick-Rekursion. Das sind keine neuen
Hamiltonian-Terme. Auch `reduced` in 1034–1046 verwendet nur eine reduzierte
Kovarianz und deren **Einteilchen**-Modularmatrix.

Der Prüfer liest dieselbe bereits gepinnte Quelle über den unveränderten
Präfix-Adapter. Es gilt exakt [A0,A_int]=0; beide Matrizen sind linear
unabhängig. Der Lie-Abschluss genau dieser beiden dynamischen Generatoren
ist daher sogar nur zweidimensional und abelsch.

Die QWZ-Quelle `verification/v988_psi_lambda_reduction.py:77` und der
gleichlautende Aufbau in `v1033_charged_disorder.py:147` bleiben bei
Einteilchen-Hoppingmatrizen und Slater-Präparationen. Eine komplizierte
Determinantenkorrelation oder ein zusammengesetztes geladenes Feld allein
macht deren Hamiltonian nicht nichtgaußsch.

## 2. Exakte Gaussian-Closure-Barriere und ihre Voraussetzungen

Seien gamma_i die vorhandenen CAR-Generatoren mit
{gamma_i,gamma_j}=2 delta_ij. Für antisymmetrische Matrizen D,E mit
**zentralen skalaren Koeffizienten** gilt direkt aus den CAR:

    [H(D),gamma(v)] = i gamma(Dv),
    [H(D),H(E)] = i H([D,E]).

Die 120 quadratischen Basis-Monome gamma_i gamma_j schließen damit unter
Kommutatoren. Der Prüfer kontrolliert alle 120²=14400 geordneten Zellen;
3360 sind nichtnull, jede davon wieder quadratisch. Keine enthält einen
quartischen Anteil. Die beiden Originalgeneratoren bilden nur den oben
genannten kleinen Unterraum dieser Algebra.

Folglich erhalten zeitabhängige quadratische Hamiltonians mit skalaren
Koeffizienten den linearen Majorana-Raum. Ihre Zeitordnungsprodukte und
stetigen Gaussian-BCH-Generatoren bleiben quasifrei. Eine neue quartische
Wechselwirkung entsteht dadurch nicht. Gemeint ist der stetige Lie- bzw.
BCH-Zweig, nicht jede willkürliche Matrixlogarithmus-Verzweigung eines
endlichen Unitärs: Ein zusätzlicher 2pi-wertiger Projektor im Logarithmus
wäre neue Generatorwahl, keine Herleitung.

**Assoziativer Produktabschluss ist etwas anderes.** Schon
q_boundary q_dark ist ein Produkt zweier quadratischer Observablen und
daher in deren assoziativer Algebra vorhanden. Das ist keine Aussage,
dass dieses Produkt im Hamiltonian oder in dessen Lie-Abschluss vorkommt.
Ebenso ist im Allgemeinen

    [dGamma(h)]² != dGamma(h²).

In einer diagonalen Basis beträgt die Differenz
2 sum_(i<j) epsilon_i epsilon_j n_i n_j. Das Quadrieren des
Vielteilchen-Hamiltonians wäre eine neue Dynamikregel. Das Quadrieren
seiner Einteilchenmatrix und anschließende dGamma-Heben bleibt quadratisch.

### Gaußsche Elimination schließt dieselbe Lücke nicht

Für eine endliche Grassmann-Gaussian mit festem invertierbarem Fastblock

    M = [[A,B],[-B^T,D]]

liefert die Integration der Fastvariablen exakt

    Pf(D) exp[ (1/2) xi^T (A+B D^-1 B^T) xi ].

Der Logarithmus des normierten Integranden ist weiterhin quadratisch.
Die entsprechende komplexe Fermionversion hat det(D) und den üblichen
Schur-Kern A-B D^-1 C. Bei singulärem Fastblock muss die Gaussian-Grenze
bzw. der verbleibende Nullmodenraum separat behandelt werden; man darf
nicht einfach D^-1 einsetzen. Reguläre Gaussian-Teilspuren und lineare
CAR-Restriktionen behalten ihre quasifreie Struktur.

Der unabhängige kleine Prüfer expandiert die Grassmann-Gaussian einer
**tatsächlichen sechs-koordinatigen Restriktion** von A0+A_int/8,
integriert zwei Koordinaten und nimmt anschließend den Grassmann-Logarithmus.
Der rohe verbleibende Grad-4-Koeffizient ist nichtnull, aber sein verbundener
Grad-4-Koeffizient im Logarithmus ist exakt null. Der Rest ist genau der
Schur-Kern. Das prüft gezielt die Verwechslung von Wick-Produkt und
Wechselwirkungsvertex; die allgemeine Identität liefert den Dimensionsbeweis.

Die Grenze gilt **nicht** für beliebige Viele-Teilchen-Feshbach-Projektionen,
nichtgaußsche Messungen, postselektierte Zahlensektoren, eine Mischung
verschiedener Gaußzustände oder die Elimination eines Bosons mit bereits
fermion-bilinearer Quelle. Bei Letzterem war die gemeinsame Wirkung schon
nicht quadratisch in allen Variablen. Auch ein von zurückgehaltenen
Ladungsoperatoren abhängiger Determinantenfaktor ist nicht die konstante
Normierung in der obigen rein fermionischen Gaussian-Identität.

## 3. Der vorhandene Clock-Registerterm ist noch keine solche Kante

`verification/v1033_charged_disorder.py:307` baut

    H_register = I tensor h_base + Z tensor h_forward
                 + Z* tensor h_forward*,
    Z=diag(1,i,-1,-i).

Alle Registerkoeffizienten I,Z,Z* kommutieren. Die Konstruktion ist
sektorenweise quasifrei. Der mit Z nichtkommutierende Shift tritt erst in
Zeilen 406–420 als `full_disorder`-**Observable** und dessen Kommutator auf,
nicht als zusätzliches Register-Hamiltonian. Eine vorhandene algebraische
Shift-Wirkung ist deshalb noch kein elektrischer Clock-Generator.

Ein Trace über ein solches nichtfermionisches Register könnte nach Wahl
einer gemeinsamen Register/Fock-Hebung und Präparation eine nichtgaußsche
Materiemischung erzeugen. Das wäre keine rein gaußsche CAR-Elimination.
Diese Hebung, der Trace-Vertrag und seine physikalische Auswahl werden in
der genannten Einteilchenrechnung nicht hergeleitet. Insbesondere sind
C4 tensor Fock(V) und Fock(C4 tensor V) verschiedene Räume.

## 4. Eine echte Eingangskante aus einem bereits vorhandenen anderen Parent

Der kompakte U(1)-Parent enthält wirklich dynamische Rotoren. Konkrete
Quelle: `local-window-round37/checker.py`, unveränderte Koeffizienten in
Zeile 18, originale Hoppingterme in 76–90 und elektrische Energie in
208–218. Die transitive Import-/Pin-Kette wird mitgeprüft. Die Fortsetzung
[Round43](../matter-resummation-round43/MATTER_RESUMMATION.md), insbesondere
Abschnitte 1 und 6, trennt bereits materielle und elektrische Zweige und
belegt deren nichtkommutierende Koeffizienten.

Auf einem tatsächlich vorhandenen Link 0 -> 1 stehen

    [E,U]=U,
    H_E=(kappa/2)E²,
    V=a(U c_1* c_0+U* c_0* c_1),
    a=1/12,  kappa=1/100.

Hier bezeichnen c_0,c_1 die zwei Low-Moden dieses Links. Die beiden
ursprünglichen High-Moden werden bei der Prüfung nicht gelöscht.
Bereits [H_E,V] enthält nichtzentrale Koeffizienten U(E+1/2) usw.
Der nächste Kommutator ergibt exakt

    [V,[H_E,V]]
      = kappa a² [n0+n1-2n0 n1+2E(n0-n1)]
      = kappa a² [1/2-2q0 q1+2E(q0-q1)].

Somit tritt tatsächlich ein reiner fermionischer Grad-4-Anteil auf:

    -2 kappa a² q0 q1 = -(1/7200) q0 q1.

Dies ist keine eingesetzte freie Vierfermion-Kopplung. Es ist eine exakt
aus zwei vorhandenen Quellteilen gebildete Kommutatorkomponente. Der Prüfer
wendet die ORIGINALEN Link-Listen und ihre CAR-Vorzeichen auf alle 16
Fock-Masken (L0,L1,H0,H1) und einen symbolischen beliebigen ganzzahligen
Fluss E an, ohne Flux-Cutoff. Zusätzlich wird der Koeffizient q_L0 q_L1
im doppelten Kommutator der **gesamten ursprünglichen Kanten-Hoppingliste**
projiziert: Er bleibt -1/7200; die anderen vorhandenen Low/High-Hoppings
löschen ihn nicht aus.
Die unbeschränkten elektrischen Kommutatoren sind Identitäten auf dem
gemeinsamen invarianten Kern endlich unterstützter Rotorvektoren tensor
dem vollständigen Viermoden-Fockraum. Eine darüber hinausgehende
Domänen-/Eliminationstheorie wird nicht aus dem endlichen Test behauptet.

Die Gaussian-Barriere ist hier nicht verletzt: Die Koeffizienten sind
nicht mehr zentral und kommutierend. Das elektrische Feld ist die erste
konkrete zusätzliche Eingangskante. Der berechnete Kommutator wird nicht
als schon gewonnener statischer effektiver Hamiltonian verkauft; dessen
Koeffizient, Zeitordnung, Gauss-Reduktion und kontrollierte Elimination
wären zusätzlich zu bestimmen.

**Typgrenze:** Dieser Link lebt auf vier komplexen L/H-Moden an zwei
Raumpunkten plus einem unendlichen U(1)-Rotor. Er ist nicht der Raum der
sechzehn Clock-Majoranas und trägt noch keine nachgewiesene Abbildung ihrer
Boundary-, O-, O²-, E8- und Ladungsmarkierungen. Auch der gesamte kompakte
Parent ist im Repo als deklarierter Kandidat, nicht als eindeutig aus
allen TFPT-Axiomen ausgewählter Parent, ausgewiesen.

Andere gefundene quartische Ausdrücke ändern diesen Befund nicht:

| Bestehende Quelle | Was dort tatsächlich geschieht |
| --- | --- |
| `local-gaussian-elimination-round24/PROOF.md:7` und Abschnitt 3 | Skalare Gaussian bei gegebenen bewegten ganzzahligen Ladungen; ladungsabhängiger Determinant bleibt erhalten. Keine reine 16-CAR-Elimination. |
| `local-parent-round15/PROOF.md`, Gleichungen (1),(8) | Explizites bosonisches TT/Skalar-Modell mit quadratischem Stress sigma und bereits gesetztem g; cubic/quartic Gesamtwirkung, kein hergeleiteter Clock-CAR-Term. |
| `toe-bridge-round30/FLAVOR_STATE.md`, Abschnitt 3 | Ein vorhandenes neutrinoartiges B12* B12 ist als Composite zulässig, sein Kopplungskoeffizient aber ausdrücklich noch nicht abgeleitet. |

Dies ist ein gezielter Quellpfad-Audit, kein Vollständigkeitsbeweis über
jede jemals im Repository erwähnte Theorievariante.

## 5. Kann der volle 81-dimensionale Raum mehr als der QND-Zeuge?

Ja, begrenzt: Der frühere besetzungsdiagonale Zeuge ist nicht der ganze
O,N-invariante Raum. Neben der vorhandenen dunklen Mode d_+ mit Clock-Grad
2 gibt es d_- mit Grad 4 und Energien u+sqrt(3)t bzw. u-sqrt(3)t.
Die Klassenrichtung

    W=b1* b2* d_- d_+,
    K_pair=W+W*

liegt im schon klassifizierten quartischen Raum, erhält O und N, und
kommutiert sogar mit H0: Beide Paarsummen sind 2u. Aber
[K_pair,n_+] und [K_pair,n_-] sind nichtnull. Sie kann neutrale Pair-
Kohärenz und Boundary/Carrier-Paartransfer tragen statt bloß Besetzungen
zu messen. Diese Richtung wird nur als Klassengegenbeispiel geprüft,
nicht in H0 eingesetzt und nicht als neu gefundener Quellterm gezählt.

Da K -> [K,n_+] linear ist und an diesem Zeugen nicht verschwindet,
bilden die entsprechenden QND-Richtungen einen echten linearen Unterraum
des 81-dimensionalen Raums. Außerhalb dieses Unterraums, also in diesem
präzisen generischen Sinn, ist mehr als der alte QND-Zugriff möglich.
Das beweist keine generische vollständige Kontrollierbarkeit oder
Erzeugtheit einer ganzen Observable-Algebra.

Eine stärkere Grenze gilt ohnehin in jeder Ordnung. Die Clock-Wirkung
O³ ist nur auf der einzigen komplexen Grad-3-Mode ungerade. Ihr CAR-Lift
ist bis zu einem irrelevant skalaren Faktor

    P3=(-1)^n3=1-2n3.

Der Prüfer bestätigt P3 gamma_i P3=alpha_(O³)(gamma_i) auf allen sechzehn
Originalgeneratoren. Daraus folgt auf der ganzen Algebra: Jedes
O-invariante Element kommutiert mit n3. Diese Besetzung ist zentral in
der O-fixen Algebra, nicht erst im gewählten QND-Modell. Eine O-invariante
Dynamik mit O-invariantem Boundary-Zugriff erzeugt ausschließlich diese
fixe Algebra und niemals einen primitiven geladenen Einzeloperator.
Ob die fixe Observable-Algebra das physikalisch richtige Ziel ist, muss
die TFPT-Constraint-/Feldzuordnung entscheiden.

## 6. Der erste offene Anschluss ist jetzt konkret

Die Option »weitere Gaussian-Manipulationen erzeugen den Viererterm« ist
für die ausdrücklich angegebene Klasse geschlossen negativ. Die tatsächlich
vorhandene Alternative ist **dynamischer Transport mit nichtkommutierenden
Koeffizienten**, wie im elektrischen Rotorparent.

Der nächste Gate ist deshalb eine quellenbestimmte Zuordnung dieses
elektrischen/Transport-Trägers zur Clock-CAR-Algebra, einschließlich O-
Ladung, Gauss-Gesetz, Boundary-Support und Zustand. Erst daraus dürfte ein
Clock-Viererterm samt Koeffizient folgen. Ein numerisches Angleichen des
nachgerechneten -1/7200 an einen frei gewählten g3/g4-Wert wäre keine Lösung.

## Reproduktion und Integrität

    python3 -B experiments/theory-contracts/clock-interaction-provenance/checker.py
    python3 -B -m unittest discover -s experiments/theory-contracts/clock-interaction-provenance -p test_checker.py
    python3 -B -OO -m unittest discover -s experiments/theory-contracts/clock-interaction-provenance -p test_checker.py

Exakte Integer-/Rational-/Grassmann-/CAR-Prüfungen, kein Parameterfit,
keine Rotor-Trunkierung und keine neue Quelldynamik. Quellenpins,
abschließende Tests und Ergebnisdaten stehen in `TEST_RESULTS.md` und
`validation.json`. Der bekannte unveränderte Legacy-ResourceWarning kann
sichtbar sein; die Legacy-Quelle selbst wurde nicht OO-gehärtet.

Die Codegraph-Suche erfolgte zuerst gemäß Skill und AGENTS.md. Die
Projektliste enthielt TFPT nicht, der Suchaufruf bestätigte den fehlenden
Index; danach erfolgte gezielter Quelldatei-Fallback. Kein Index neu
aufgebaut, keine fremde Session oder Quelldatei verändert. Nur dieses neue
Experimentverzeichnis geschrieben; kein Commit/Push und keine Statuspromotion.
