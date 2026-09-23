# Zusammensetzung, Verfeinerung und Information: bedingter Bell-Compiler

12. September 2026. NON-RH. Forschungsergebnis mit exakten endlichen Kontrollen,
kein vollständiger TOE-Nachweis. Drei parallele Prüfstränge plus Hauptstrang.

## Ergebnis in einfachen Worten

Die vollständige Kette besitzt schon eine einfache geschlossene Operationsregel:
die bekannte Temperley–Lieb-Algebra. Die Schwierigkeiten beginnen nicht erst
bei ihrer Zusammensetzung, sondern bei der Auswahl einer physischen Realisierung
und beim Verkleinern der Zustandsräume. Ein einzelner lokaler Ausschnitt kann
Information verlieren, obwohl die vollständige Codierung sie bewahrt.

Die Resultate unterscheiden vier Fragen:

1. **Zusammensetzung:** Bell-Kontraktionen erfüllen exakt TL-Relationen.
2. **Auswahl:** Auf einem vorausgesetzten offenen Nachbarschaftsgraphen wählen
   volle aktive U(d)-Symmetrie, strikt zweikörper-lokale Unterstützung,
   Reflexion und Bell-bevorzugende Einzelkanten den Kopplungstyp bis auf Skala.
   Ohne die Lokalitätsannahme bleiben weitere einfache Invarianten möglich.
3. **Verfeinerung:** Die bisherige Dreiercodierung ist nicht strikt unabhängig
   vom Verfeinerungsbaum. Das schließt korrigierende physische Unitaries nicht aus.
4. **Information:** Die globale Baumcodierung ist isometrisch; einzelne äußere
   Endpunkte verlieren schrittweise Quantenzugriff.

Alle Aussagen betreffen das bedingte Modell aus
[COMPOSITION.md](../interaction/COMPOSITION.md), nicht einen neu aus TFPT
abgeleiteten Raumgraphen. Die Faktoren V und V*, volle aktive U(d), die
Nachbarschaft, Präparation und Bedeutung einer Zeitentwicklung sind Zusatzdaten.
Der bereits quellengeprüfte Compiler hat d=4; die folgende Konstruktion
funktioniert auch für andere d und ist deshalb kein exklusiver Fingerabdruck.

## 1. Die vollständige Algebra ist bereits einfach

Auf einer alternierenden Kette V,V*,V,... sei P_i der normierte Bell-Projektor
auf den Faktoren i,i+1, sonst Identität. Für d>1 gilt durch Indexkontraktion

    P_i^2=P_i,
    P_i P_(i+1) P_i=P_i/d^2,
    [P_i,P_j]=0 für |i-j|>1.

Mit e_i=d P_i werden dies exakt die Temperley–Lieb-Relationen

    e_i^2=d e_i,   e_i e_(i±1) e_i=e_i,   [e_i,e_j]=0 für |i-j|>1.

Damit erhält jede endliche Kettenlänge eine verträgliche Darstellung derselben
lokalen Relationsfamilie. Gemeint ist eine Darstellung, nicht hier bewiesene
Treue auf jeder Länge, ein Kontinuumslimes oder eine physische Raumkonstruktion.
Nicht gleichzeitig erfüllbare Bell-Grundbedingungen widersprechen dieser
exakten Operationsalgebra nicht. Die bekannte Frustration bleibt bestehen.

Die Identifikation ist etablierte Mathematik, keine Entdeckung einer neuen
Algebra. Primärliteratur zur TL-Algebra, Baxterisierung und gesonderten
Transfermatrix-Konstruktion: [Nepomechie–Pimenta, §2](https://arxiv.org/pdf/1601.04378).
Die dortige konkrete Spin-Darstellung wird nicht ungeprüft mit unserer
alternierenden Bell-Darstellung gleichgesetzt; verwendet werden die Relationen.

## 2. Yang–Baxter bestimmt eine Form, aber keine autonome Uhr

Für die normierte lokale Familie R_i(u)=I+f(u)e_i reduziert die additive
spektrale braid-Yang–Baxter-Gleichung auf

    f(u+v)(1-f(u)f(v))=f(u)+f(v)+d f(u)f(v).

Beweis: Mit x=f(u), y=f(v), z=f(u+v) ist die Differenz beider Matrixprodukte
genau (x+y+dxy+xyz-z)(e_i-e_(i+1)); letzterer Operator ist in der betrachteten
Darstellung nicht null. Regularität f(0)=0 und Differenzierbarkeit liefern

    f'(u)=a(1+d f(u)+f(u)^2),   a=f'(0).

Bei d=4=2 cosh(eta), eta=arcosh(2)=log(2+sqrt(3)), lautet die lokale Lösung

    f(u)=sinh(c u)/sinh(eta-c u),   c=a sinh(eta).

Der Maßstab c bleibt frei. Ein gemeinsamer nichtverschwindender skalarer
Vorfaktor r(u) bleibt ebenfalls durch YBE unbestimmt. Die neue logarithmische
Konstante folgt hier ausschließlich aus d=q+q^(-1). Keine Primzahl-, RH-,
Dirac-Großzahlen- oder physische Uhridentifikation wird daraus abgeleitet.

Für u=it und reelles c sind die beiden Eigenwerte von R gleich 1 und
sinh(eta+ict)/sinh(eta-ict), also ist R unitär. Trotzdem ist es keine
nichttriviale analytische Einparametergruppe mit demselben additiven Parameter:

    R(u+v)=R(u)R(v)
    würde f(u+v)=f(u)+f(v)+d f(u)f(v) verlangen.

Zusammen mit YBE ergäbe sich f(u)f(v)f(u+v)=0. Dies schließt eine nichttriviale
reguläre analytische f in diesem Ansatz aus. Ein skalarer Vorfaktor behebt
das Verhältnis der beiden Eigenwerte nicht. Umparametrisierung einer
einzelnen lokalen Phasenkurve ist möglich, bewahrt aber nicht automatisch
die additive spektrale YBE.

Positiv: Der Tangentengenerator an t=0 ist bei U(t)=exp(-itH) gleich
H_local=-c e_i/sinh(eta), also bis auf Skala und Offset eine Bell-Kopplung.
Ein Hamiltonoperator, eine Gatefolge und eine Transfermatrix sind jedoch
verschiedene Objekte. Eine daraus konstruierte Kettendynamik benötigt weiterhin
Graph, Randbedingungen, Kopplungsstärken und eine physische Interpretation.

`tl_clock.py` kontrolliert die Relationen exakt bei d=2,3,4, die allgemeine
hyperbolische Identität in rationalen Exponentialkoordinaten und eine
nichttriviale unitäre d=4-Kontur. Eine absichtlich eingesetzte Gruppenregel
anstelle der YBE-Regel wird verworfen.

## 3. Warum Symmetrie allein nicht alle Kopplungen auswählt

Schon auf drei Faktoren ist bei d>=3 der volle U(d)-Kommutant größer als die
von den zwei Bell-Kanten erzeugte Algebra. Die TL-Algebra dieses Abschnitts
ist span{I,P,Q,PQ,QP} mit Dimension fünf. Die Vertauschung F der beiden
äußeren Faktoren ist ein weiterer unabhängiger symmetrischer Operator.
Der volle Kommutant hat Dimension sechs (M_2 plus zwei skalare Blöcke).

Selbst Reflexion lässt neben I und P+Q weitere Hermitesche Operatoren wie
PQ+QP und F zu. Erst die ausdrücklich vorausgesetzte strikte Zweikörper-
Nachbarschaft auf dem Graphen 1--2--3 entfernt diese zusätzlichen Terme.
Gleiche Randbehandlung und Bell-bevorzugende Einzelkanten wählen dann
J[(I-P)+(I-Q)] plus Offset mit J>0. Das ist ein bedingter Auswahlsatz,
nicht die Herleitung von Raum, Lokalität, Vorzeichen oder Zeiteinheit.

Die unabhängige Kommutantenprüfung dokumentiert die genaue Zerlegung sowie
endliche positive Gegenbeispiele; siehe die `commutant`-Dateien hier.

## 4. Verfeinerungsbaum: dieselbe Regel ergibt verschiedene Einbettungen

Setze Z=(Phi_12 tensor I_3+I_1 tensor Phi_23)/sqrt(2(1+1/d)).
Z ist die bekannte Grundraumisometrie des Dreierblocks. Zweifaches Einsetzen
an drei verschiedenen Positionen ergibt fünfstellige Isometrien L,M,R.
Die mittlere Einsetzung verwendet die konjugierte Darstellung.

Der unabhängige Kontraktionsbeweis liefert

    L* M=L* R=M* R=q_d I,   q_d=(3d+5)/(4(d+1)).

Bei d=4 ist q=17/20, also sind die Einbettungen nicht gleich und nicht durch
einen bloßen logischen Basiswechsel identifizierbar. Ihre gemeinsame lineare
Spanne hat Dimension 3d=12, nicht d=4. Das ist nur die minimale Spanne,
welche alle drei unveränderten Einbettungen enthält, keine allgemeine
Untergrenze für jede denkbare physische Verfeinerung.

Es gibt dagegen physische Unitaries zwischen solchen Unterräumen. Mit
Delta=L-R ist beispielsweise

    U=I-Delta Delta*/(1-q)

eine Hermitesche unitäre Spiegelung, die L und R vertauscht und M fixiert.
Das rettet nicht die behauptete strikte Gleichheit. Es macht eine präzisere
positive Frage möglich: Können solche Umgruppierungen ausgewählte Observable
und Dynamik verträglich transportieren und auf weiteren Stufen kohärent sein?
Die Existenz einer einzelnen Umgruppierung beweist diese Bedingungen nicht.
Für den fest gewählten gleichgewichteten Fünfer-Hamiltonoperator
H_5=sum_(i=1)^4(I-P_i) ergibt die direkte Rechnung sogar einen unterscheidenden
Energietest:

    L*H_5 L=R*H_5 R=((d-1)(9d+10))/(4d(d+1)) I,
    M*H_5 M=((d-1)(5d+6))/(2d(d+1)) I.

Bei d=4 sind dies 69/40 und 39/20, mit Differenz 9/40. Deshalb existiert
**keine mit diesem H_5 kommutierende Unitäre**, die L auf M abbildet, auch
nicht mit zusätzlichem logischem Basiswechsel. Es geht um dieselbe feste
Modell-Dynamik, nicht um ein allgemeines Verbot von Umgruppierungen.
L und R lassen sich hingegen durch Spiegelung der gesamten Kette tauschen;
diese erhält H_5, vertauscht aber die markierten Endpunkte. Die explizite
Householder-Unitäre oben ist eine andere Wahl und erhält H_5 nicht.
Details und Kontrollen: [ternary.md](ternary.md), `ternary.py`.

## 5. Exakter Informationsbefund: global erhalten, lokal abgeschwächt

Für einen äußeren Ausgang des Dreierencoders gilt auf Observablen und dual
auf Zuständen der depolarisierende Kanal

    D(rho)=a rho+(1-a)Tr(rho) I/d,   a=(d+2)/(2(d+1)).

Auf einem **fest gewählten** rekursiven Baum und einem Pfad, der an jedem
Knoten einen äußeren Ausgang auswählt, gilt nach k Stufen exakt D^k mit
Parameter lambda=a^k. Dies folgt aus Komposition und Spurtreue aller
verworfenen Zweige. Es wird nicht für beliebige mittlere Pfade oder größere
Ausgangsregionen behauptet. Die komplette endliche Baumabbildung bleibt
als Zusammensetzung von Isometrien selbst isometrisch.

Für 0<=lambda<=1 ist dieser einzelne Kanal genau dann entanglement-breaking,
wenn lambda<=1/(d+1). Hier ist der Beweis, nicht bloß ein PPT-Test:

* Der normierte Choi-Zustand ist C_lambda=lambda P_Bell+(1-lambda)I/d^2.
* Seine partielle Transposition hat auf dem antisymmetrischen Raum Eigenwert
  [1-(d+1)lambda]/d^2. Oberhalb der Schwelle ist er negativ, also nicht separabel.
* Die Haar-Zweitmomentidentität integral rho_psi tensor rho_psi dpsi
  =(I+F_swap)/[d(d+1)] folgt aus unitärer Invarianz, symmetrischem Träger und
  Spur eins. Partielle Transposition gibt
  integral rho_psi tensor conjugate(rho_psi) dpsi=(I+d P_Bell)/[d(d+1)].
  Dies ist eine explizit separable Zerlegung des Choi-Zustands an der Schwelle.
* Unterhalb der Schwelle ist C_lambda die konvexe Mischung dieses Zustands
  mit I/d^2, mit Mischgewicht (d+1)lambda.

Die Gleichwertigkeit von separablem Choi-Zustand und entanglement-breaking
Kanal ist Standard: [Horodecki–Shor–Ruskai, Theorem 4](https://arxiv.org/pdf/quant-ph/0302031).

Bei d=4 gilt lambda_3=27/125>1/5 und lambda_4=81/625<1/5. Deshalb verliert
ein solcher **einzelner äußerer Endpunkt erstmals nach vier Stufen** die
Fähigkeit, Verschränkung mit einem externen Referenzsystem zu erhalten.
Er enthält weiterhin klassische Zustandsinformation; lambda ist nicht null.
Die gemeinsame Ausgabe bewahrt die volle Quanteninformation. Das beweist
weder einen physikalischen Horizont noch ein holographisches Flächengesetz.

`leaf_information.py` prüft alle Matrixeinheiten der lokalen Randabbildung,
Schwellen für d=2,3,4 und die algebraische separable Mischung. Der allgemeine
Baumbeweis und die Haar-Identität stehen oben; es wurde kein riesiger Baum
numerisch simuliert und keine Eindeutigkeit seines Grundzustands behauptet.

## 6. Was als nächstes tatsächlich entscheidet

| Frage | Nächster konkreter Nachweis | Abbruch-/Grenzkriterium |
| --- | --- | --- |
| Exakte Umgruppierung statt verlustbehaftetem Kürzen | Transport derselben markierten Operatoren und des ausgewählten Hamiltonoperators; anschließend Kohärenz auf weiteren Bäumen | Ein bloßes Mapping von Zustandsräumen oder Erhaltung der globalen Symmetrie reicht nicht. |
| Dynamik aus der Quelle | Begründe aktive Paarung, Graph, lokale Unterstützung und Zustandswahl aus den ursprünglichen Compiler-/Seam-Operationen | Frei angesetzte Daten bleiben Hypothesen; YBE-Spektralparameter nicht als Uhr umbenennen. |
| Informationszugriff | Klassifiziere rekonstruierbare gemeinsame Ausgangsregionen samt explizitem Decoder und Aufwand | Isometrie des Gesamtbaums beweist keinen effizienten oder lokalen Zugang. |
| Viele-Block-Grenze | Kontrolliere zusätzliche Operatoren, Dressing und Fehler mit wachsender Kette | Zweiblock-Schur-Eindeutigkeit und Erstordnungsfaktor 9/25 sind kein geschlossener RG-Fluss. |

Das ist ein engerer positiver Kandidat für weitere TFPT-Forschung: vollständige
Operationsalgebra plus kontrollierte Umgruppierung, statt immer mehr passende
Zahlen oder immer derselbe verkürzte Viererraum. Kein RH-/Faktorisierungs-
Mechanismus wird damit vorgeschlagen oder als geprüft ausgegeben. Alle T1--T8
bleiben offen; Paper, Webseite und physische Statusmarker werden nicht geändert.

## Reproduktion und Herkunft

`run_checks.py` führt die vier hiesigen Prüfer normal und unter -OO aus und
vergleicht ihre JSON-Ausgaben. `verification.json` hält Ergebnisse und Hashes.
Eine erfolgreiche Prüfung bestätigt diese begrenzten Aussagen, keine vollständige
TFPT-Suite. Die Ausgangskonstruktion wird in der bisherigen
`../run_verification.py` gesondert mitsamt Quellenpins geprüft.

Aktueller Replay: **vier neue Prüfer / acht Ausführungen bestanden**, jeweils
normale und optimierte Ausgabe identisch. Zusätzlich wurde der bisherige
integrierte Ursprungsaudit erneut ausgeführt: **acht Prüfer / sechzehn
Ausführungen bestanden** (`baseline_verification.json`). Somit 24 erfolgreiche
endliche Ausführungen dieser Runde; kein kompletter TFPT-/Kontinuumstest.
Die Kommutanten- und Verfeinerungsprüfer verifizieren ihre Ausgangspins,
die beiden weiteren prüfen das ausdrücklich angegebene bedingte Modell.
