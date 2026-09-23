# Abgleich mit der gemeinsamen Quellwirkung

20. September 2026. Ergänzung zu UR.SOURCE.BOUNDARY_SELECTION.01.
Gelesene neue Eingabe: `TFPT_Lane_Korrelation_2026-09-20/SYNTHESE.md`
und `REVIEW.md` aus der vom Nutzer angegebenen Task. Die dortige Priorität
einer vollständigen, phasenerhaltenden Quellreduktion wird übernommen.

## 1. Der Zusatzsektor besteht einen konkreten Ladungstest nur mit einer Bedingung

Die Randkonstruktion hatte bisher ihre globale Teilchenzahl festgelegt.
Für einen Anschluss an das ursprüngliche TFPT-Ladungswörterbuch ist eine
andere Prüfung nötig. Verwende die ursprüngliche Hyperladung auf den
ersten fünf Trägerkoordinaten,

    Y8=(-1/3,-1/3,-1/3,1/2,1/2,0,0,0).

Angenommen, das zusätzliche R/L-Paar ist ein Farb- und schwaches Singulett
und vektorartig: beide ursprünglichen Komponenten tragen dieselbe
Hyperladung y. Dann ist die volle Ladungsfunktion

    Y10=(Y8,y,y).

Für die unveränderte Wechselwirkungsrichtung folgt exakt

    Y10.n = -2+2y.

Eine hyperladungsneutrale Wechselwirkung verlangt daher **y=1**. Mit einem
hyperladungsneutralen Zusatzpaar wäre der Cosinus im gegebenen Wörterbuch
nicht eichinvariant. Dies ist eine bedingte Notwendigkeit innerhalb der
festgelegten Singulett-/Vektorpaarklasse, kein Beweis, dass die Quelle ein
solches Paar erzeugt.

Der Test betrifft nicht bloß einen ausgewählten Spinor. Für jeden E8-Vektor
und die symmetrische Abbildung F_aux=T_a-k_a n gilt

    Y10.F_aux(p) = Y8.p-k_a(p)(-2+2y).

Somit erhält **y=1 das gesamte Hyperladungswörterbuch**. Alle 240 Wurzeln
werden im Checker genau geprüft. Der lokale Vierervertreter b_aux hat
dann Y=3(-1/3)+1=0, genau wie s=(1/2)^8. In den zerlegten Gitterkoordinaten
tragen e_R=-e9 und m=n+e9 die Ladungen -1 und +1; ihre Summe n ist neutral.
Nach der üblichen Teilchen-Loch-Konvention ist das das massive Dirac-Paar
mit Einheitsladung. Sein 1+1-dimensionaler Randursprung bleibt erhalten:
Es wird nicht als neues vierdimensionales Elektron identifiziert.

Dies verbindet die bisher getrennte Frage nach dem massiven Komplement
mit einem tatsächlichen Compiler-Ladungstest. Ein solcher Zusatzsektor
kann auf einen Hyperladungs-Hintergrund reagieren. Das liefert weder eine
vierdimensionale Anomalie noch einen bereits ausgewählten Beitrag zu alpha.

## 2. Wann der massive Faktor eine relative Flavorphase wirklich beeinflusst

Die Lane-Synthese führt korrekt die vollständige Schur-Identität an:

    det D = det D_QQ det(D_PP-D_PQ D_QQ^(-1)D_QP).

Sie gilt bei den angegebenen invertiblen endlichen Blöcken. Die vollständige
Wirkung muss beide Faktoren berücksichtigen. Bei Nullmoden oder chiralen
unendlichen Determinanten sind Regulator, Determinantenlinie und Ward-
Identitäten zusätzliche Aufgaben; ein Hamiltonresolvent ersetzt sie nicht.

Am exakt zerlegten Punkt unserer vorhandenen Randkonstruktion ist die
Aussage noch konkreter. Für ausschließlich reine E8-Proben j und unabhängig
gesetzte Parameter lambda des massiven Paars faktorisiert das regulierte
Funktional bei kompatibler Produktzustands-/Randbedingung:

    Z[j;lambda]=Z_E8[j] Z_m[lambda].

Der Faktor Z_m kann zur vollständigen Wirkung beitragen, obwohl er aus
Z[j;lambda]/Z[0;lambda] herausfällt. Das entspricht dem Hinweis der Synthese.
Für eine RELATIVE Down-/Leptonphase muss jedoch zusätzlich gelten:

    Xi(theta)=Z_d(theta) Z_e(0)/(Z_e(theta) Z_d(0)).

Wenn beide Deformationen denselben Faktor Z_m(theta) enthalten, kürzt er
sich aus Xi exakt heraus, selbst wenn er komplex und parameterabhängig ist.
Eine gemeinsame Zusatzphase ist also kein Ursprung einer unterschiedlichen
Down-/Leptonphase. Das bedeutet nicht, dass sie für alle anderen Antworten
oder für die volle Wirkung bedeutungslos wäre.

Eine nichtverschwindende Komplementwirkung auf diese relative Phase verlangt
stattdessen eine aus der Quelle gewonnene unterschiedliche Abhängigkeit,
etwa D_m,d(theta) gegenüber D_m,e(theta), oder eine echte Kopplung zwischen
E8-Deformation und dem massiven Sektor. Sie darf nicht einfach als freier
Flavorfaktor in den Kandidaten eingesetzt werden. Der genaue Test lautet

    Im partial_theta [log det D_m,d - log det D_m,e]

gemeinsam mit dem entsprechenden effektiven Anteil und den Ward-Termen.
Die geordnete Vierpunktphase eines Current-Wortes beweist diese
Massendeformation nicht: räumliche Einfügungen, Flavormassen und physische
Zeit sind verschiedene Argumente eines Funktionals.

## 3. Eine komplexe Massenschreibweise erzeugt die Phase nicht von selbst

Das zusätzliche Paar besitzt am zerlegten Punkt eine reale konstante Masse.
Selbst der testweise Ersatz durch eine konstante Phase reicht im flachen,
hintergrundfreien freien Dirac-Sektor nicht: Für den vorhandenen Modenkern

    h_theta(k)=k sigma_z+m cos(theta) sigma_x+m sin(theta) sigma_y

gilt h_theta=U_theta h_0 U_theta^*, U_theta=exp(-i theta sigma_z/2).
Der endliche Matsubara-Block hat deshalb

    det(i omega I-h_theta)=-(omega²+k²+m²),

unabhängig von theta. Die Identität wird symbolisch geprüft. Eine konstante
Umphasierung dieser Art liefert keine relative Flavorphase. Eine
ortsabhängige Massentextur, nichttriviale Eichhintergründe, ein anomalie-
gerechter Regulator oder nichtgleichartige Deformationen ändern die
Voraussetzungen und müssen aus der tatsächlichen Quelle kommen. Sie
werden hier nicht als kostenlos verfügbare Erklärung eingeführt.

## 4. Aktualisierter Stand der Compiler-Lane

Die neuen Originaldateien zu **UR.COMPILER.FOUR_FOLLOWUPS.28** bestätigen,
dass die zehn zuvor offenen K3-Masken des endlichen Vierquellensystems
ausgeschlossen wurden. Die dortigen Beweise geben den vollständigen
Grundraum bei J=mu=0 und die Eindeutigkeit mit Lücke >=mu/8 auf
J=mu=epsilon kappa, 0<epsilon<=10^-8 an. Diese bestehenden Herleitungen
wurden gelesen und im Graphen abgeglichen; ihre aufwendigen Checker werden
hier nicht als erneut ausgeführt ausgegeben.

Die große Paketkompression liefert die Suchbedingung 2mu=kappa+9J. Ihre
Grundlage bleibt eine nichtinvariante Kompression mit quantifizierter
Leckage. Die Schur-Rückwirkung ist hier ein Vielteilchenoperator; die
gaußsche Determinantenzerlegung aus dem anderen Modell berechnet ihn nicht
automatisch. Der frühere Strahl J=mu mit kappa>0 liegt zudem nicht auf dieser
kritischen Bedingung. Der kontrollierte kleine Vierquellenbefund darf daher
nicht als Nachweis des kritischen großen Zweigs gelesen werden.

## 5. Eine gemeinsame nächste Herleitung

Der überprüfbare Anschluss ist jetzt enger als „ein unsichtbarer Sektor
könnte eine Phase liefern“: Die vollständige Quelle muss das geladene
Zusatzpaar und die Rekonstruktionsphase hervorbringen und gleichzeitig
zwei unterschiedliche, physisch identifizierte Down-/Lepton-Deformationen
auf demselben Operator definieren. Danach kann die volle relative Ward-
Antwort einschließlich Komplement ausgewertet werden.

Die neue Hyperladungsbedingung ist ein konkreter Test für diese Abbildung.
Die Faktoraufhebung verhindert eine nur scheinbare Lösung durch eine
gemeinsame Phase. Beides verändert den mathematischen Arbeitsauftrag,
ohne die verschiedenen Quellen bereits zu einem einzigen Weltmodell zu
erklären. Eine vollständige TFPT-/TOE-Schließung liegt weiterhin nicht vor.
