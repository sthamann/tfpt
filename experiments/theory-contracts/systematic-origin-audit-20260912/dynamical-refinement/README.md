# Dynamikerhaltende Reparatur des bedingten Fünferblocks

12. September 2026. NON-RH. Fortsetzung von [refinement](../refinement/README.md).
**Ein bestimmtes endliches Schließungsproblem ist konstruktiv gelöst; der
physische TFPT-Ursprung und T1–T8 sind nicht gelöst.**

## Ergebnis

Die bisherige gemeinsame 12-dimensionale Spanne der drei Verfeinerungen ist
nicht dynamisch geschlossen. Ihr kleinster gemeinsamer invarianter Raum unter
dem **unveränderten** gleichgewichteten Fünfer-Bell-Hamiltonoperator hat
Dimension 20. Wir konstruieren eine Isometrie in diesen Raum und einen
Hermiteschen effektiven Hamiltonoperator, welche die Zeitentwicklung exakt
ineinander überführen. Das ist keine weitere bloße Kompression erster Ordnung.

Der Preis ist konkret: fünf Multiplikitätsrichtungen statt einer oder drei.
Die lokale vierdimensionale logische Information bleibt als Faktor erhalten.
Dieser zusätzliche Faktor ist keine abgeleitete räumliche fünfte Dimension.
Die Einfachheit des Hamiltonoperators wird nicht durch eine künstliche
Gegenkopplung gerettet; die bisher verworfenen dynamisch benötigten Zustände
werden mitgeführt.

## 1. Exakte dynamische Hülle

Sei D die Matrix der fünf unnormierten Bell-Kontraktionsdiagramme aus
`refinement/ternary.py`, jeweils mit freiem logischen Index in C^d. Es gilt

    D*D=G tensor I_d,    H_5 D=D(h tensor I_d).

G ist für jedes ganzzahlige d>=2 positiv definit. Die führenden Hauptminoren
sind d², d²(d²−1), d²(d²−1)², (d²−1)^4, (d²−1)^4(d²−2).
Die fünf Diagramme sind deshalb unabhängig, der Raum hat Dimension5d.

Wiederholtes Anwenden von h auf die L-Koordinaten erzeugt alle fünf Richtungen.
Der zugehörige Krylov-Determinant ist

    -2(d+1)(d²+4)/d^9 != 0.

Dasselbe gilt für R. M und der symmetrische kohärente Mittelwert erzeugen
jeweils drei Richtungen. Der kohärente Mittelwert ist kein Eigenzustand.
Also ist die kleinste H_5-invariante Hülle der gemeinsamen drei Bilder
genau Ran(D). Bei d=4 bedeutet dies 12 -> 20 Dimensionen.

Wähle G=C*C mit invertiblem C, zum Beispiel durch Cholesky-Zerlegung. Dann

    J=D(C^(-1) tensor I_d),     K=C h C^(-1)

erfüllen

    J*J=I_(5d),    K*=K,
    H_5 J=J(K tensor I_d).

Damit folgt für jedes reelle t **exakt**

    exp(-it H_5) J=J exp[-it(K tensor I_d)].

Kein kleines t, keine schwache Kopplung, kein nachträglich verworfener Rest
ist für diese endliche Identität erforderlich. G und h sind vollständig aus
dem bereits festgelegten bedingten Modell bestimmt. Andere Quadratwurzeln
des Gram-Operators ändern nur die orthonormale Koordinatenwahl.

Wichtig: K wirkt auf dem Multiplikitätsfaktor, auf der logischen C^d steht I_d.
Die logische Information ist in diesem Sektor unter H_5 inert. Das ist
Informationserhaltung, keine hergeleitete universelle logische Berechnung.
Der Raum ist nicht der vollständige physische d^5-Raum und nicht unter allen
denkbaren lokalen Observablen invariant. Die vollständigen lokalen M_d-
Algebren erzeugen M_(d^5); keine echte Teilraumreduktion kann alle diese
Operatoren als invariante Einschränkungen behalten. Eine dynamische Hülle
ist deshalb noch kein vollständiger markierter Universalraum.

Details, allgemeiner Beweis und unabhängige direkte physische Kontrollen:
[hull.md](hull.md), `hull.py`.

## 2. Einfaches Umgewichten scheitert schon am zweiten Moment

Für positive reflexionssymmetrische Kopplungen

    H(a,b)=a[(I-P12)+(I-P45)]+b[(I-P23)+(I-P34)]

und unveränderte L,M-Einbettungen ergibt sich

    M*H M-L*H L=(2a-b)(d-1)(d+2)/(4d(d+1)) I.

Nur a=b/2 gleicht die mittlere Energie an. Dort bleibt jedoch

    M*H² M-L*H² L= -b²(d-1)/(8d²(d+1)) I !=0.

Bei d=4,b=1 haben beide den Mittelwert27/20; ihre Varianzen sind aber
243/3200 und57/800. Jede mit H kommutierende Unitäre müsste alle H-Momente
erhalten. Deshalb kann keine positive Wahl a,b diese beiden unveränderten
Codierungen dynamikerhaltend identifizieren. Ein Energie-Offset behebt die
Varianzdifferenz nicht. Dieser Ausschluss betrifft diese Familie, keine
beliebigen neuen Hamiltonoperatoren, zusätzlichen Terme oder neuen Codierungen.

[weights.md](weights.md) und `weights.py` beweisen die allgemeine Formel und
prüfen die ersten sechs Momente direkt im endlichen physischen Modell.

## 3. Ein gemeinsamer Grundraum ist erreichbar, aber Filterung hat Kosten

Die fünf Diagrammrichtungen haben bei d=4 die exakten Eigenwerte

    (19-sqrt(41))/8, (10-sqrt(5))/4, 9/4,
    (10+sqrt(5))/4, (19+sqrt(41))/8.

Jeder trägt einen vierdimensionalen logischen Faktor. Der kleinste Eigenwert
dieses Sektors ist E0=(19-sqrt(41))/8. Ein unnormierter Koeffizientenvektor ist

    v=((5+sqrt(41))/2,1,(7+sqrt(41))/2,(5+sqrt(41))/2,1).

Alle drei Codierungen projizieren auf dieselbe normierte Isometrie dieses
untersten Sektors, bis auf Phase. Ihre exakten Erfolgswahrscheinlichkeiten
für die entsprechende Projektionsmessung lauten

    p_L=p_R=363/800+2223 sqrt(41)/32800 ≈0.887717840848,
    p_M=9/25+39 sqrt(41)/1025 ≈0.603631068546.

Die Normierung eines erfolgreichen Ausgangs beseitigt nicht die jeweilige
Fehlerwahrscheinlichkeit. Die konkrete Projektionsoperation ist kein
deterministischer geschlossener Prozess. Allgemeine Literatur zur gesonderten
Implementierung nichtunitärer Filter:
[Kosugi et al., probabilistic imaginary-time evolution](https://arxiv.org/abs/2111.12471).
Hier wurde keine solche experimentelle Implementierung durchgeführt.

`filter.py` kontrolliert diese Sektorformeln exakt und diagonalisiert unabhängig
den vollständigen 1024-dimensionalen H_5 numerisch. Dabei liegt das Minimum
bei1.574609470321, numerisch vierfach, mit Abstand0.366373535304 zur nächsten
Energie. **Die Identifikation als globales Minimum ist in diesem Prüfer eine
Gleitkomma-Diagnose, kein zertifizierter exakter Spektralbeweis.**

Nach Einschränkung auf diesen einen Eigenraum ist H nur E0 I. Eine erfolgreiche
Grundraumpräparation repariert deshalb keine nichttriviale autonome logische
Dynamik. Vor allem darf Präparation nicht mit Zeitentwicklung verwechselt werden.

## 4. Positive Alternative: deterministisches Auslesen mit einem Hilfssystem

Die vorherigen Ergebnisse verbieten keinen offenen Wiederherstellungskanal.
Für A_1=L,A_2=M,A_3=R gilt

    A_alpha* A_beta=C_(alpha,beta) I_d,
    C=(1-q)I_3+q 11*, q=(3d+5)/(4(d+1)).

Setze F=[L M R](C^(-1/2) tensor I_d). F ist isometrisch. Die drei Bilder
lassen sich darin schreiben als

    A_alpha psi=F(C^(1/2)|alpha> tensor psi).

Ein Decoder kann diesen Multiplikitätsfaktor in einem Hilfssystem behalten,
den logischen Zustand lesen und in eine beliebig festgelegte Zielisometrie B
überführen. Die Hilfszustände sind nicht orthogonal; sie bewahren Information
über den Aufbau, keine perfekt unterscheidbaren klassischen Etiketten.

Dimension3 des Hilfssystems ist für diese reine Zielabbildung auf allen drei
Bildern notwendig und hinreichend, weil Rang(C)=3. Für den gesamten reparierten
5×d-Raum benötigt ein Reset aller Multiplikitätszustände bei reinem festem
logischem Ziel ein Hilfssystem der Dimension mindestens5. Die logische
Information muss dafür nicht nachselektiert werden. Der Vorgang ist jedoch
keine isolierte, energieerhaltende autonome Unitäre auf dem ursprünglichen
System; Hilfssystem, Ansteuerung und gegebenenfalls Reset bleiben Ressourcen.

[recovery.md](recovery.md) und `recovery.py` prüfen die endliche deterministische
Rekonstruktion und ihre Voraussetzungen. Der Kanal ersetzt nicht die noch
fehlende native physische Bereitstellung seiner Operationen.

## 5. Der nächste Operator-Test ist ebenfalls entschieden

Ein stärkerer allgemeiner Satz präzisiert die verbleibende Grenze: Für eine
offene n-gliedrige Bell-Kette mit sämtlich von null verschiedenen Kantengewichten
erzeugen **H zusammen mit der vollen lokalen Matrixalgebra am ersten Faktor**
die gesamte endliche *-Algebra M_(d^n). Man muss dafür nicht schon alle
lokalen Operationen an allen Stellen voraussetzen.

Beweis: Jeder gemeinsame Kommutant X hat zunächst Form I_1 tensor Y, weil
er mit M_d am ersten Faktor kommutiert. Die erste Bell-Kopplung besitzt
Entwicklung P12=(1/d)sum_(a,b) E_ab tensor E_ab. Im Kommutator [X,H] können
deren nichtdiagonale E_ab-Koeffizienten auf Faktor1 nicht durch spätere
Kanten kompensiert werden, die auf Faktor1 Identität tragen. Deshalb
kommutiert Y mit allen nichtdiagonalen Matrixeinheiten auf Faktor2. Diese
erzeugen einschließlich ihrer Produkte M_d, also X=I_1 tensor I_2 tensor Z.
Induktion entlang der nichtverschwindenden Kanten zeigt X skalar. Die erzeugte
finite *-Algebra ist somit die volle Matrixalgebra (in ihrer Blockzerlegung
würde jeder echte Teilblock oder jede Multiplizität einen nichtskalaren
Kommutanten liefern). Auch ein nichttrivialer gemeinsamer invarianter
Teilraum ist ausgeschlossen: Sein Projektor würde zur Kommutante gehören.

Die tatsächlichen vier Compiler-Generatoren erzeugen am ersten Faktor M4.
Damit fordert dieser stärkere Vertrag für n=5 den vollständigen 1024-dimensionalen
Raum, nicht nur den exakt H-invarianten 20-dimensionalen Sektor. Schon ein
lokaler tatsächlicher g1 verlässt diesen Sektor; `hull.py` prüft das separat.
`boundary_access.py` verifiziert Quellenpins, vollständige lokale Erzeugung
und die Koeffizientenargumente für d=2,3,4. Der allgemeine Satz folgt aus
der obigen Induktion, nicht aus einer endlichen numerischen Hochrechnung.

Das ist eine Aussage über Algebra und invariante Unterräume, **kein Beweis
effizienter Gate-Synthese, Lie-Kontrollierbarkeit, nativer physischer
Zugänglichkeit oder universeller problemlösender Rechenleistung**. Bei
unterbrochenen Kanten oder eingeschränkten Randoperationen gelten andere
Voraussetzungen. Die geschlossene 20D-Reparatur von H wird nicht widerlegt;
ihre Grenze gegenüber vollständigem operativem Zugriff wird exakt bestimmt.

## 6. Nächste Entscheidung statt weiterer Zahlenähnlichkeit

Der bedingte H_5-Schließungsfehler ist auf Ran(D) behoben. Offen bleiben:

1. **Markierte Observable:** Welche Quelloperationen bleiben im selben Raum,
   welche erweitern ihn? Nicht nur H, sondern auch Vorbereitung und Messung
   müssen einen verträglichen gemeinsamen Vertrag haben.
2. **Weitere Verfeinerung:** Eine Familie solcher Räume und Abbildungen über
   längere Ketten muss nachweislich kompatibel sein. Der Fünferbeweis beweist
   weder einen konstanten Speicherbedarf noch einen Kontinuumsgrenzwert.
3. **Physischer Ursprung:** Volle aktive U(4), alternierende Faktoren,
   Nachbarschaft, Kopplungsvorzeichen und Zeiteinheit sind weiterhin Zusatzannahmen.
4. **Zugänglicher Decoder:** Eine abstrakte endliche Isometrie muss nicht
   lokal oder effizient ausführbar sein. Ressourcen dürfen nicht verschwinden.

Kein RH-/Faktorisierungsverfahren wird hier vorgeschlagen. T1–T8 bleiben offen.
Die alten Prüfer, Paper, Webseite und Beweisstatusmarker werden nicht verändert.

## Verifikation

`run_checks.py` führt fünf neue Prüfer jeweils normal und unter -OO aus:
zehn erfolgreiche Ausführungen mit identischen JSON-Ergebnissen je Paar.
`verification.json` enthält die Ergebnisse, Code-Hashes und Evidenzklassen.
Zusätzlich wurden die vier vorherigen Verfeinerungsprüfer in acht Ausführungen
erneut erfolgreich geprüft (`previous_refinement_verification.json`).
Das sind 18 Ausführungen der aktuellen beiden Suiten, keine vollständige
TFPT- oder Kontinuumsprüfung. Die numerische globale Spektraldiagnose ist im
Bericht ausdrücklich von den exakten Sektor- und Operatoridentitäten getrennt.
