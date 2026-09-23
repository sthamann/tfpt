# Flavor-/Quellen-Delta nach dem 104er-Zertifikat

**Research-ID:** `UR.SOURCE.FLAVOR_DELTA_AUDIT.20260920`  
**Verdict:** `NO_NEW_SOURCE_DERIVED_FLAVOR_COUPLING; NEW_GRADED_LOCALITY_OBSTRUCTION`

## 1. Byte-Delta des bisherigen Flavor-Vertrags

Im Vertrag `UR.SOURCE.FLAVOR_ORIGIN.01` hat sich gegenüber dem gepinnten
104er-Zertifikat kein Byte der vier maßgeblichen Artefakte geändert:

| Artefakt | SHA-256 | Delta |
|---|---|---|
| `PROOF.txt` | `328158deea8bab9ac552c1d4f44eb64f79724264501a5d8a7276e873c5c9b314` | keines |
| `contract_index.json` | `c5893a43e40f48483c7577eac0e1c70e0b477593f3f2cf79d6bb9067aa404fe2` | keines; derselbe Hash stand bereits im alten Source-Manifest |
| `certificate.optimized.json` | `3efa28973698464e873b0ae2bde82469a73e1f1bf3543c85a33e63bfe931a9ca` | keines |
| `source_manifest.json` | `85bce198a39e27d388f9c09beec4050f44e399f5964b96829cae93d2f2800530` | keines |

Damit enthält dieser Vertrag selbst seit dem Zertifikat keine neue
Familienmarkierung, keinen neuen Operator und kein neues Matrixelement.

## 2. Tatsächlich neue Aussage im Folgecontract

Neu ist `UR.SOURCE.GRADED_LOCALITY.01`:

- `source-graded-locality-20260920/PROOF.txt`, SHA-256
  `669309ea7f240397b2eb49c61e02b5224d4b9d1c15d50aeca30668fa97fa41bb`;
- `source-graded-locality-20260920/contract_index.json`, SHA-256
  `59d28c4f50af42375f89257c1f349367ab87ffd6026c80486d03b059429ebfb5`.

Der Fortschritt ist ein Operator-/Locality-Ausschluss:

1. Das volle lokale Quellgitter ist nicht einfach ein Produkt der projizierten
   Sektoren. Es enthält vier Glue-Klassen über
   `T(D8) direct_sum (Z n + Z z)`. Der Checker rekonstruiert den Index vier
   und die Repräsentanten `0,f,b,f+b` exakt.
2. Die halbe Monodromie der projizierten D8-Vektor- und Spinorlinien wird
   durch die neutrale Ebene kompensiert. Das Komplement trägt damit echte
   Locality-Daten, aber keine Yukawa-Phase.
3. Im `E8 direct_sum I(1,1)`-Rahmen ist jeder reine E8-Vertex gerade. Alle
   acht transportierten mikroskopischen ungeraden Felder besitzen explizit
   einen ungeraden massiven Paaranteil.
4. Unterhalb der massiven Schwelle ist der leichte Projektor daher vollständig
   gerade. Für einen paritätserhaltenden Hamiltonoperator gilt exakt

   `P H Q_odd = 0`.

   Die im vorigen Flavor-Vertrag nur algebraisch diagnostizierten
   Komplementblöcke `b,c` sind in der wörtlichen Identifikation
   „reine E8-Light-Legs plus ein massives ungerades Leg“ paritätsverboten.
   Eine Schur-/Feshbach-Elimination erzeugt keine fehlenden ungeraden Vektoren
   im leichten Raum.

Das ist strenger als das frühere `Q H P=0` aus der faktorisierten
quadratischen Wirkung: Der neue Satz benutzt die geerbte mikroskopische
Parität und schließt die wörtliche Mass-Map auch für jede gerade Kopplung aus,
solange der Odd-Gap und der gerade leichte Projektor erhalten bleiben.

## 3. Prüfung der scheinbar neuen Kopplungskandidaten

### Zusätzliche Occupation-Markierung

Der ältere Phasenvertrag enthält den quadratischen Zeugen
`X=2 Nc Nw-3`. Er wirkt auf dem internen Carrier, nicht auf dem
Familien-Tripel, und fällt bereits durch die feste Ein-Higgs-Yukawa-
Kompatibilität. Für jede solche interne Matrix `X` gilt weiterhin

`(X tensor A(h))(u tensor h)=Xu tensor A(h)h=0`.

Sie erreicht die bewiesene Familien-Nullrichtung daher nicht.

### Native Paket-Flip-Kopplung

`UR.COMPILER.FOUR_FOLLOWUPS.28` besitzt tatsächlich den nativen
Paket-Flip-Koeffizienten `-mu/8`. Das ist eine echte Matrixkomponente der
Paketzuordnung, aber kein Flavor-Operator: Der Vertrag gibt keinen
`SU(3)_family`-/SM-/Chiralitäts-Intertwiner und keine Wirkung auf `h` an;
außerdem ist die Paketkompression im Vollraum nicht invariant. Diese
Kopplung darf nicht als Yukawa-Matrixelement umbenannt werden.

### Kritischer n/z-Punkt

Der neue Locality-Vertrag führt die gewählte Konkurrenzmetrik

`V_c=K+2 K v v^T K`, `v=(n-z)/2`,

ein. Exakt gilt dort `Delta(n)=Delta(z)=1`. Das liefert den bekannten
bedingten neutralen Ising-/Majorana-Diagnostikpunkt, aber keine neue
quellenselektierte Flavor-Kopplung:

- `u=(n+z)/2` und `v=(n-z)/2` sind keine integralen mikroskopischen
  Gittervektoren;
- `n` und `z` sind beide `q=Y=0`, also neutral;
- `n` ist charakteristisch, `z` nicht; deshalb erzwingt keine integrale
  mikroskopische Isometrie die Gleichheit ihrer Kopplungen;
- die Metrik ist gewählt, nicht aus P1/P2 oder der Quelle selektiert;
- das neutrale effektive Majoranafeld trägt nicht die benötigte
  Spin(10)-/SM-Materiedarstellung.

In der bisherigen blockgetrennten Paarboost-Familie bleibt der einzigartige
Glue-kompatible Konkurrent `z` sogar bei `Delta(z)>=8`. Der kritische Punkt
ändert deshalb ausdrücklich die Metrikprämisse; er ist keine Aktivierung
durch die bereits vorhandene Paarwirkung.

## 4. Präziser Fortschritt und nächster Akzeptanztest

Es gibt **keine neue source-derived Flavor-Kopplung**. Die erste neue
belastbare Aussage ist die Paritätsobstruktion der zuvor erwogenen
Komplement-Mass-Map.

Vor jeder weiteren Yukawa- oder Rangrechnung muss die Quelle nun einen
leichten lokalen ungeraden Operator liefern und für ihn gleichzeitig zeigen:

1. tatsächliche Spin(10)- beziehungsweise SM-Darstellung;
2. korrekte Ladungen und geerbte Fermionparität;
3. verträgliche Locality-/Glue-Klasse;
4. endliche leichte Skalendimension im selben physikalischen Zustand;
5. ein nichtverschwindendes Matrixelement, das die Familienrichtung `h`
   erreicht.

Ohne dieses Objekt würden neue `b,c`, Ising-Majoranas oder Paket-Flips nur
anders benannte Hilfsoperatoren darstellen.

## Reproduktion

`python3 -B checker.py`

Die Prüfsumme und Checkzahl stehen in `replay.txt` und `certificate.json`.
Keine Repository-, Paper-, Ledger- oder Graphdatei wurde verändert.
