# TFPT: zwei analytische Teilbrücken und ein konkreter Clock-Zugang

2026-09-08, lokal auf b803b7e5. Unveränderte Originalquellen; kein
T1–T8-/TOE-/RH-Abschluss, kein Commit/Push, kein Paper-/Webseitenupdate.

## Was sich tatsächlich geändert hat

| Offene Teilfrage dieser Forschungslinie | Ergebnis dieser Runde | Grenze |
| --- | --- | --- |
| Endliche Current-Referenz gegen unendlichen geglätteten Current | Vollständiger komplexer Wortvergleich analytisch kontrolliert; endpunktuniform | Referenzmodell, noch keine mikroskopische Feldidentifikation |
| Gekrümmte Quellenenergie gegen linearisierten Rand | Globale Same-P-Abschätzung, vollständiger Historienfehler O(N^-1/4), normierter Beitrag O(N^-1/16) | Die rohen Quellenoperatoren müssen noch verglichen werden |
| Neutraler Zugang zu primitiver Clock-Information | Minimaler O,N-erhaltender Grad vier; expliziter Randzugriff auf ein Korrelationsgewicht | Zusätzliche Kopplung und Präparation nicht aus TFPT ausgewählt; keine volle Erzeugtheit |

### 1. Endliche Current-Referenz: die gesamte Amplitude

[Beweis](../current-truncation-bridge/README.md): Die bisherige endliche
Determinante ist exakt eine normalgeordnete Fock-Galerkin-Kompression mit
außen eingefrorener Besetzung. Das erste fehlende Teilchen-Loch-Paar kostet
mindestens M+1 relative Energie. Ein gewichteter kohärenter Energie-Tail
kontrolliert die vollständige Duhamel-Differenz, einschließlich ihrer Phase.

Für das neue mesoskope Vergleichsfenster
M=min(floor(N/8),floor(sqrt N)), t=4N^(1/4), gilt nach Normierung

```
sup_(a,b) Z_t² |C_finite - C_current|
 = O(N^(3/16) sqrt(log N) exp(-N^(1/4)/4)).
```

Die Aussage gilt auch bei zusammenrückenden Endpunkten; sie macht nicht den
singulären finalen Kontinuumskern zu einer gleichmäßig konvergenten Funktion.
Der falsche Ersatz durch Kompression einer bereits exponentierten
Multiplikationsunitären wurde unabhängig als Zweikanten-Operation erkannt.

### 2. Quelle: die Dispersion ist nun ein kontrollierter Fehler

[Beweis](README.md): Dieselbe Quellenpolarisierung P und dieselben echten
Randquasimoden J definieren Hsharp=J diag(-p_j)J*+RHR. Global gilt
||H-Hsharp||op=O(N^-3/2). Gaussian-Duhamel kontrolliert damit nicht nur den
statischen Kreuzblock, sondern den vollständigen mitbewegten P/Q-Verlauf.
Sein Fehler I_lin=O(N^-1/4) ist klein genug für die vorhandene normierte
Vakuumschranke; der Beitrag verschwindet mindestens wie O(N^-1/16).

Die explizite obere Schranke ist bei den kleinen gerechneten N sehr grob
und teils größer als eins. Der asymptotische Satz kommt aus der Rechnung
mit N-unabhängigen Konstanten, nicht aus einem numerischen Fit.

**Erster verbleibender Beweisschritt in dieser Kette:** Unter Hsharp die
tatsächlichen gefilterten Rampen-/Top-Arc-Operatoren gegen
J T_a J*+R Phi_Hsharp(ramp)R vergleichen. Benötigt wird noch
I_sharp,ref=o(N^-3/16), einschließlich Restsektor, J/R-Leckage und
diagonalem Transport. Diese Pflicht wurde weder angenommen noch geschlossen.

Ein präziser Folgeansatz ist die exakte diskrete Fourierform des skalaren
longitudinalen Rampen-/Arc-Symbols: seine Halbzellphase ist eine gemeinsame
Translation, nicht eine frei angepasste Paarphase. Danach bleiben
transversale Randprofile und Restsektor wirklich zu kontrollieren.
Das ist hier ein Folgeansatz, kein zusätzlicher bewiesener Quellenvergleich.

### 3. Clock: ein kleiner überprüfbarer Kopplungsvertrag

[Exakte Algebra und Antwort](../clock-neutral-access/README.md): Volle
O- und N-Erhaltung verbietet quadratische Boundary/Dark-Kopplung. Unter O²
allein gilt dieses Verbot nicht. Im vollständigen O,N-erhaltenden reinen
quartischen Raum gibt es 81 gemischte Richtungen. Ein kleiner Zeuge ist

```
K = (n_b1-1/2) [g3(n_d3-1/2) + g4(n_d4-1/2)].
```

Alle Moden stammen aus der ursprünglichen 16-Majorana-Algebra. Ein neutraler
Boundary-Transfer zeigt bei nichtentarteten g3,g4 vier bedingte Linien und
rekonstruiert bei bekannter Produktpräparation das Gewicht
<A* A>=<n3(1-n4)>. Das ist ein konkreter möglicher Zugriff auf zuvor dunkle
Information, keine Umbenennung eines geladenen Operators in einen neutralen.

Im bisherigen Quellen-Gibbs-Zustand sind die Randmoden gleich besetzt:
Korrelation vorhanden, retardierter X-Kommutator null. Eine explizite
besetzte Probe-Präparation erlaubt Antwort. Das unveränderte Vakuum bleibt
auch unter den kleinen Zeugenkopplungen dunkel. K und die Präparation
müssen erst aus TFPT gerechtfertigt werden. n3,n4 verbleiben zudem im
Kommutanten der erzeugten Boundary-Algebra; volles Erzeugtheitsproblem offen.

## Einordnung in die TOE-Arbeit

Die Fortschritte betreffen einen lasttragenden Feldvergleich und den
Zugang zum vorhandenen Clock-Sektor. Sie ersetzen nicht die gemeinsame
3+1D-Parent-Konstruktion, Rekonstruktion/Positivität, chirale Materie ohne
Spiegel, Flavour-/Massenmechanismen oder Spin-2-/Gravitationsnachweis.
Getrennte Vergleichsmodelle werden nicht zu einer TOE addiert.

Die nächste Priorität ist der genannte mikroskopische Operatorvergleich.
Parallel ist für den Clock-Zeugen die Quellenableitung der quartischen
Kopplung samt Präparation zu prüfen, nicht ihre Konstanten passend zu wählen.

Reproduktionen und Prüfgrenzen stehen in [TEST_RESULTS.md](TEST_RESULTS.md).
