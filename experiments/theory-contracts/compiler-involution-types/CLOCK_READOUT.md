# Clock-Information lebt hier zuerst in nichtneutralen Bilinearen

2026-09-08. Exakte endliche Darstellungsaussage aus derselben 16-Majorana-Quelle.
Keine Identifikation mit E8-Ladungsfeldern, kein ausgewählter Vielteilchenzustand.

Fortsetzung: [vollständige endliche Dynamik, Gibbs-Antwort und Vakuumgrenze](../clock-bilinear-response/README.md).
Die unten formulierte Prüfung wurde dort ausgeführt; ihr positiver thermischer
Ausgang schließt den weiterhin blinden Boundary-Zugang nicht.

Der andere Geometrie-Zweig hat gezeigt: O P_B=P_B und [O,H]=0.
Damit bleiben H^n im(P_B) und die daraus erzeugte neutrale Randinformation
im Fixraum von O. Die [Quelldaten](../../double-cover-rh-audit-2026-09-08/GEOMETRIE_UND_READOUT.md)
werden hier nicht durch eine andere Randmessung ersetzt.

## Neuer exakter Zensus

Für die originale Permutationsmatrix O ergibt die erneute exakte Rechnung

    det(z I-O)=(z-1)^10 (z+1)^2 (z^2+z+1)^2.

Mit omega=exp(2 pi i/6) sind die Dimensionen der omega^k-Eigenräume:

| Clock-Grad k | 0 | 1 | 2 | 3 | 4 | 5 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Komplexifizierte Majorana-Koordinaten V | 10 | 0 | 2 | 2 | 2 | 0 |
| Äußeres Quadrat Lambda^2 V | 50 | 4 | 21 | 20 | 21 | 4 |

Die zweite Zeile folgt durch Addition der Grade modulo 6 für verschiedene
Basisvektoren. Unabhängig wurde die vollständige 120x120-Matrix aus den
2x2-Minoren von O aufgebaut und ihr charakteristisches Polynom geprüft:

    (z-1)^50 (z+1)^20 (z^2+z+1)^21 (z^2-z+1)^4.

Dies ist mehr als eine beliebige neue Zustandsraum-Verdopplung. In der
Clifford-/CAR-Algebra der bereits vorhandenen Majorana-Koordinaten entspricht
v wedge w dem antisymmetrisierten Produkt

    [gamma(v), gamma(w)]/2.

Diese lineare Einbettung von Lambda^2 V in den Grad-2-Teil der Clifford-Algebra
ist injektiv und O-äquivariant; das folgt unmittelbar aus einer orthonormalen
Majorana-Basis und den CAR. Die vier primitiven Grad-1-Operatoren entstehen
aus V_3 wedge V_4, die vier Grad-5-Operatoren aus V_2 wedge V_3.
Sie sind fermionparität-gerade, aber nicht Clock-neutral. Adjungieren
vertauscht Grad 1 und 5. Ein solches geladenes Eigenoperator-Element allein
ist deshalb nicht hermitesch; seine hermiteschen Real-/Imaginärteile sind
zulässige algebraische Messkandidaten, sofern die physikalischen Constraints
sie zulassen.

Die Konstruktion braucht keine Gleichsetzung der 16 reellen Koordinaten mit
16 Erzeugungsmoden. Sie identifiziert auch nicht die 16-dimensionalen
E8-Ladungszeichen-Zustände mit einem Majorana-Fockraum.

## Auswahlregel und nächster Test

Für eine C6-Wirkung auf einer Operatoralgebra ist

    A_m=(1/6) sum_(j=0)^5 omega^(-mj) alpha_O^j(A)

exakt vom Clock-Grad m. Für End(V) ist alpha_O(A)=O A O^-1;
damit O A_m P_B=omega^m A_m P_B. Also ist A_m P_B=0 für m=1,5,
weil diese Zielräume dort fehlen, nicht notwendig A_m=0 auf ganz End(V).
In der Majorana-Algebra sind die oben
angegebenen Bilineare dagegen nicht null. Für eine O-invariante Präparation
verschwindet ihr Einpunktmittel, nicht notwendig ihre neutrale Zweipunkt-
Antwort <A_m^* A_m>. Positivität allein garantiert keine von null
verschiedene Antwort in einem bestimmten Zustand.

**Konkreter neuer Ansatz:** die primitiven Clock-Komponenten in diesen
vorhandenen Carrier-Bilinearen suchen und ihre dynamische Antwort unter
dem unveränderten H prüfen, statt in einem nachweislich blinden neutralen
Boundary-Readout. Zuerst sind Lokalität, Ladung/Gaussbedingungen und die
aus TFPT bestimmte Präparation zu prüfen. Die Verbindung zum E8-Carry und
geladenen Skalierungsfeld bleibt eine weitere Pflicht. Dies repariert
nicht automatisch den 12+4/8+8-Involutionskonflikt.

Der exakte Zensus und die algebraische Möglichkeit sind erreicht. Eine
physikalisch ausgewählte, messbare Clock-Antwort wurde noch nicht berechnet.

Ein scharfer bedingter Dynamiktest in einer ausdrücklich gewählten treuen
endlichen Gibbs-Präparation rho ist rho([H,A_m]^* [H,A_m])>0.
Anders als das schon aus A_m!=0 folgende rho(A_m^* A_m)>0 zeigt er
nichtstatische Antwort. Auch dieser Test ersetzt keine TFPT-Zustandsauswahl.

## Reproduktion

    python3 -B experiments/theory-contracts/compiler-involution-types/clock_selection.py --output experiments/theory-contracts/compiler-involution-types/clock_selection_validation.json
    python3 -B -m unittest discover -s experiments/theory-contracts/compiler-involution-types -p 'test_*.py'
    python3 -B -OO -m unittest discover -s experiments/theory-contracts/compiler-involution-types -p 'test_*.py'

Neun Involutionstests plus drei neue Clock-Tests pro Modus. Quelle und
Quellextraktor unverändert; Pins werden vor der Konstruktion geprüft.
Zensus, Clifford-Einbettung, Adjungiertenaussage und Auswahlregel wurden
anschließend unabhängig mathematisch gegengelesen; keine Korrektur nötig.
