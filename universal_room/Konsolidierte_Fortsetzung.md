# TFPT und Universalraum: verifizierte Konsolidierung und konstruktive Fortsetzung

**Stand: 14. September 2026. Für Stefan Hamann.**

Forschungsmanuskript. Eigene Herleitungen und endliche Gegenrechnungen, nicht extern begutachtet. NON RH. Keine Änderung eines Repositorys, Ledgers, Papers oder einer Website. Die hier behaupteten Resultate gelten in den jeweils definierten Modellen. Eine vollständige TOE wird nicht behauptet.

## 1. Ergebnis

Die sieben Anhänge enthalten einen belastbaren endlichen Kern, aber keine bereits gemeinsame vollständige Physik. Die jüngste Konsolidierung übernimmt außerdem einen Fehler aus dem zweiten Teil des Q Audits: Ein Register, das die geordneten inneren Eingänge eines antisymmetrischen Vertex unterscheidet, verändert dessen Gramoperator. Der gewünschte Austausch entsteht dann nicht mehr.

Diese Fortsetzung liefert dazu vier konkrete Verbesserungen:

1. Ein notwendiges und hinreichendes Kriterium für kohärenzverträgliche Aufzeichnung und eine explizite unitäre Reparatur des einzelnen Vertex.
2. Den vollständigen kanonischen effektiven Operator vierter Ordnung des in [S6, §1.2] festgelegten harten C16 Referenzmodells. Er enthält 40 Einzelkantenbeiträge, 160 Beiträge über zwei überlappende Kanten und 60 Beiträge über disjunkte Kanten mit gemeinsamem Vermittlertyp. Die bisher isolierte Vierkörperrechnung erfasst davon nur die letzte Klasse.
3. Eine unabhängige numerische Rechnung im vollständigen 24.024 dimensionalen SU(4) Singulettsektor, einschließlich der ersten Änderung der Singulettlücke durch diesen vollständigen Operator vierter Ordnung.
4. Eine exakte Lösung des isolierten mikroskopischen Vierersterns im vom besetzten Eingang erreichbaren Sektor, sowie einen konkreten hinreichenden Relaxationskanal für das ideale Vierträgersystem. Der zusätzliche Reservoirzugriff bleibt als Annahme sichtbar.

Der Unterschied zwischen „ausführbare Reparatur“ und „aus den bisherigen TFPT Daten notwendigerweise ausgewählte Naturdynamik“ bleibt entscheidend. Eine fundamentale Theorie darf Axiome besitzen. Neu gesetzte Axiome dürfen nur nicht rückwirkend als schon bewiesene Konsequenzen schwächerer Ausgangsdaten gelten.

## 2. Quellen und Prüfumfang

### 2.1 Die sieben tatsächlichen Anhänge

| Kürzel | Datei | Rolle |
|---|---|---|
| S1 | `TFPT_UNIVERSALRAUM_KONSOLIDIERUNG_2026-09-14_fable.md` | Konsolidierung mit Konflikttabelle und Vorschlag einer U Regel |
| S2 | `TFPT_Universalraum_Rekonstruktion_2026-09-14_sol.md` | Kanonische Rekonstruktion, Zugriffsklassen, Quellenvertrag |
| S3 | `TFPT_Universalraum_Konsolidierung_2026-09-14.md` | Kurze Konsolidierung, enthält erneut einen falschen Klammerkanal |
| S4 | `TFPT_UNIVERSALRAUM_Q_AUDIT_UND_U_REGEL_2026-09-14.md` | Globaler Klammerkern, Belegung und spekulative U Regel |
| S5 | `TFPT_Rekonstruktion_2026-09-14.md` | Beweis des allkoppligen Zweizellensatzes und Architekturprüfung |
| S6 | `TFPT_Sechs_Pruefpunkte_Analyse.md` | Konkreter mikroskopischer Referenzoperator und Sternprotokoll |
| S7 | `TFPT_Universalraum_Gesamtdarstellung_2026-09-14.pdf` | Forschungsbuch v1.1, 90 PDF Seiten, 21 Kapitel und Anhänge |

Die PDF Tabelle auf gedruckter Seite 18, physischer PDF Seite 25, nennt noch ein Dublett. Die spätere Vierfachkorrektur ist nicht bloß eine redaktionelle Umbenennung, sondern wurde hier unabhängig numerisch überprüft. Die alte Grenze bei Lambda gleich 8J gehört zum damaligen Beweis, nicht zu einem nachgewiesenen Phasenübergang.

### 2.2 Tatsächlich in dieser Runde ausgeführt

`verify_independent.py` besteht 89 benannte endliche Prüfungen. Normale Ausführung und `python -OO` erzeugen bytegleiche Ergebnisdateien. Dies sind teils ganzzahlige Identitäten, teils Gleitkomma oder hochpräzise numerische Rechnungen, nicht 89 unabhängige physikalische Bestätigungen.

Geprüft wurden der lokale Klammergramoperator, die Wirkung geordneter History, die unitäre Reparatur, Tetramer und Stern, beide vollständigen Pointerfortsetzungen, die 60 Strahlen und 15 Kontexte, die Wurzelgradierung, alle 15 erlaubten Youngsektoren der acht Träger an elf Kopplungen, ein vollständiger 469 dimensionaler Zweibondbaustein und ein 544 dimensionaler mikroskopischer Sternbaustein. Die Alpha Gleichung wurde mit 80 Stellen Arbeitspräzision gelöst.

`microscopic_fourth.py` prüft mit exakter Ganzzahl beziehungsweise Bruchrechnung vier vollständige Matrixspalten des gesamten C16 Operators vierter Ordnung gegen unabhängige CAR und Bosonenpfade. Außerdem werden zwölf ausgewählte Hermitizitätspaare und sämtliche 40 alternativen Kantenpaarungen der viergliedrigen Zyklen auf Vermittlertypverträglichkeit geprüft. Normale und optimierte Ausgabe sind bytegleich. Der Operator ist als Formel auf dem ganzen Raum definiert; es wurden nicht alle 4^16 Matrixspalten aufgezählt.

`verify_clebsch_singlet.py` diagonalisiert den vollständigen Singulettmultiplizitätsraum mit Dimension 24.024 und berechnet die Projektion des vollständigen Operators vierter Ordnung auf Grundzustand und erstes angeregtes Quartett. Die Youngdarstellung wurde vorher gegen unabhängige dichte Achtträgermatrizen geprüft. Diese Rechnung ist numerisch, nicht intervallarithmetisch zertifiziert.

Nicht erneut ausgeführt wurden die Originalprüfer, sämtliche Jacobi Tripel, der originale phasentreue TFPT Adapter, die ursprüngliche 20 Qubit Schaltung, alle 64 SU(4) Sektoren des C16, Hardware, ursprüngliche Schleifenläufe, ein thermodynamischer Grenzwert oder ein Gravitationsgrenzwert. Die in den Anhängen genannten alten Prüfzähler werden nicht zu unseren eigenen Läufen umetikettiert.

## 3. Konsolidierter Kern

### 3.1 Algebra und Prozess

Die markierte Erweiterung des positiven Gitters D5 plus A3 bleibt richtig. Mit

\[
q_{D_5}(k)=5k^2/8,\qquad q_{A_3}(k)=3k^2/8
\]

ist die passende diagonale Z4 Klasse isotrop. Der Erweiterungsindex vier ergibt Determinante eins. Unter den angegebenen Markierungen entsteht das gerade unimodulare Gitter E8. Die typgerechte Zerlegung ist

\[
\mathfrak e_8=(45,1)\oplus(1,15)\oplus(10,6)
\oplus(16,4)\oplus(\overline{16},\overline4).
\]

Es gilt `[g1,g1]` nach `g2`, aber `[g1,g3]` nach `g0`. Die eigene Wurzelenumeration findet 960 geordnete Summen für den ersten Kanal und 832 für den gemischten Kanal. Das kontrolliert die Gradierung, nicht sämtliche Originalphasen des Focklifts.

Für den festen Prozess auf 60 Strahlen gilt

\[
T=\frac{C^TBC+F^TF}{28},\quad CT=\frac B7 C,\quad FT=\frac37F,
\]

mit Spektrum

\[
\{1^1,(3/7)^{15},(2/7)^9,(-2/7)^5,0^{30}\}.
\]

Die linearen Dimensionen 240, 60, 45 und 30 beziehen sich auf unterschiedliche Zustands und Zugriffsklassen, nicht auf konkurrierende universelle Raumdimensionen. Der Wert `a=1/7` ist innerhalb

\[
K_a=aI+\frac{1-a}{6}(B-I)
\]

die einzige Wahl mit Rang 30 des induzierten Strahlenprozesses. Bei `a=1/3` ist der Rang 55, sonst im betrachteten Intervall 60. Maximale Übergangsentropie oder maximaler einmaliger Rangverlust können als zusätzliche Auswahlprinzipien dienen. Ihre Übereinstimmung in dieser eingeschränkten Familie beweist keine allgemeine Gleichwertigkeit der beiden Prinzipien.

### 3.2 Zelle und Graph

Mit `P_e^+=(I+S_e)/2` gilt auf einem zusammenhängenden positiv gewichteten Graphen

\[
\ker\sum_eJ_eP_e^+=\Lambda^N\mathbb C^4.
\]

Für vier Träger bleibt genau Omega, für mehr als vier kein Nullzustand. Der vollständige Tetramer besitzt das Spektrum

\[
J\{0^1,2^{45},3^{40},4^{135},6^{35}\}.
\]

Der Viererstern besitzt dagegen

\[
\{0^1,(J/2)^{30},J^{45},(3J/2)^{40},(2J)^{15},(5J/2)^{90},(3J)^{35}\}.
\]

Clebsch, vollständiger Tetramer und uniforme Kette bleiben verschiedene Hamiltonmodelle. Gleicher lokaler Träger und derselbe isolierte Nullzustand machen ihre Anregungen nicht gleich.

### 3.3 Zweizellenmodell für alle positiven Brückenkopplungen

Für zwei vollständige Tetramer und eine Brücke `lambda P_ab^+` setze

\[
R=\sqrt{16J^2-2J\lambda+\lambda^2},\qquad Q=\sqrt{4J^2+\lambda^2}.
\]

Dann sind

\[
E_0=\frac{4J+\lambda-R}{2},\quad
E_1=3J+\frac\lambda2-\frac Q2,
\quad\Delta=J+\frac{R-Q}{2}>J/2.
\]

Der globale Beweis in S5 trägt: Der zweidimensionale Singulettblock erreicht E0. Der Vergleichsoperator im adjungierten Sektor liefert E1 als scharfe Untergrenze und ein ausdrücklich konstruierter Zweierblock erreicht diese Grenze. Alle übrigen Darstellungen beginnen mindestens bei 3J. Die Identität

\[
R^2-(Q-J)^2=11J^2+2J(Q-\lambda)>0
\]

beweist die strikte Lückenschranke. Die hier ausgeführte Enumeration sämtlicher 15 Youngformen summiert sich, gewichtet mit ihren SU(4) Dimensionen, zu 65.536. Sie bestätigt die beiden Energien an elf Werten zwischen 0 und 100. Diese Stichprobe ergänzt den Beweis, ersetzt ihn nicht.

Bei `lambda=8J` ist die Lücke ungefähr `0.876894374 J`. Eine Behauptung, dort werde der Grundzustand instabil, ist für dieses Modell falsch. Ein allkoppliger thermodynamischer Satz folgt daraus nicht.

## 4. Neue Korrektur: Zu genaue History zerstört den Austausch

### 4.1 Das konkrete Gegenbeispiel

S4 Teil II §2 und S1 §5.2 verwenden Historylabels der Form `|st,ab,mu>`. Wenn verschiedene geordnete Paare darin orthogonale Zustände bezeichnen, gilt für einen einzelnen antisymmetrischen Kanal nicht mehr dieselbe Interferenzregel.

Ohne solche Aufzeichnung gilt für `a<b`

\[
K|ab\rangle=|a\wedge b\rangle,\qquad
K|ba\rangle=-|a\wedge b\rangle,
\]

also

\[
K^\dagger K=I-S.
\]

Mit einer geordneten History erhält man

\[
\widetilde K|ab\rangle=|a\wedge b\rangle|h_{ab}\rangle,
\quad
\widetilde K|ba\rangle=-|a\wedge b\rangle|h_{ba}\rangle.
\]

Für orthogonale Aufzeichnungen fällt der Kreuzterm weg. Mit

\[
D_{\rm diag}=\sum_a|aa\rangle\langle aa|
\]

folgt stattdessen

\[
\boxed{\widetilde K^\dagger\widetilde K=I-D_{\rm diag}.}
\]

Das ist eine basisabhängige Bedingung „beide Werte sind verschieden“, kein SU(4) invarianter antisymmetrischer Projektor. Der Kommutator mit einem kollektiven SU(4) Generator ist nicht null. Bei einem reellen Historyüberlapp `eta` gilt allgemeiner

\[
\widetilde K^\dagger\widetilde K
=I-D_{\rm diag}-\eta(S-D_{\rm diag}),\qquad 0\leq\eta\leq1.
\]

Nur `eta=1` reproduziert den ursprünglichen Vertexgramoperator.

### 4.2 Die Folge ist dynamisch, nicht nur sprachlich

Setze `kappa=t^2/Delta`. Der falsch aufgezeichnete Vermittler erzeugt auf dem vollständigen Vierergraphen

\[
H_{\rm bad}=-\kappa\sum_{i<j}(I-D_{ij}).
\]

Jedes der 24 Wörter, in denen alle vier Farben genau einmal vorkommen, hat Energie `-6 kappa`. Der Grundraum ist somit 24 dimensional statt eindimensional. Omega ist darin nur eine von vielen Superpositionen. Auf dem Viererstern ist der entsprechende Grundraum sogar `4*3^3=108` dimensional.

Diese Aussagen wurden durch vollständige Enumeration der 256 Basiswörter geprüft. Sie zeigen, dass die vorgeschlagene Historydefinition nicht unverändert zusammen mit dem behaupteten Austausch und der eindeutigen Omega Auswahl verwendet werden darf.

### 4.3 Notwendiges und hinreichendes Reparaturkriterium

Für zwei lineare Vertexabbildungen K und L gilt:

\[
L^\dagger L=K^\dagger K
\quad\Longleftrightarrow\quad
L=VK
\]

mit einer Isometrie V auf dem Bild von K.

Beweis: Definiere `V(K psi)=L psi`. Die Gleichheit der Gramoperatoren macht die Definition unabhängig von der Wahl von psi und erhält sämtliche Skalarprodukte. Die Umkehrung folgt unmittelbar aus `V^dagger V=I` auf dem Bild.

Damit ist präzise festgelegt, welche History zulässig ist: Sie darf einen kohärenten Vertexausgang isometrisch erweitern, aber nicht zwei Eingänge auseinanderziehen, die K bereits bis auf Vorzeichen identifiziert. Für die Kopplungsrechnung genügt die vorhandene Lochkonfiguration als Kantenmarkierung. Eine zusätzliche dauerhaft unterscheidbare Geschichte virtueller Ereignisse ist nicht nötig und könnte auch höhere Ordnungen verändern.

### 4.4 Explizite unitäre Ausführung

Setze `W=K/sqrt(2)`. Dann gelten `W^dagger W=P_-` und `WW^dagger=I_6`. Auf dem direkten Summenraum des besetzten Paars und seines Vermittlers ist

\[
\boxed{
U_W=\begin{pmatrix}P_+&-W^\dagger\\W&0\end{pmatrix}
}
\]

unitär. Der symmetrische Kern geht nicht verloren, sondern bleibt im ersten Ausgang. Die beiden antisymmetrischen Reihenfolgen bleiben kohärent.

Eine energetische Realisierung lautet

\[
H_{22}=\begin{pmatrix}0&gW^\dagger\\gW&\Delta I_6\end{pmatrix}.
\]

Hier entstehen Unitarität, Rückweg und die relative Absenkung des antisymmetrischen Sektors aus einem expliziten selbstadjungierten Operator. Die Wahl von g, Delta, seiner Einbettung und seiner Steuerung ist damit nicht aus E8 abgeleitet. Der isolierte Austauschkoeffizient ist exakt

\[
j(g,\Delta)=\frac{\sqrt{\Delta^2+4g^2}-\Delta}{2}
=\frac{g^2}{\Delta}-\frac{g^4}{\Delta^3}+O(g^6).
\]

Die Gleichsetzung dieses ganzen Ausdrucks mit `2t^2/Delta` in S3 ist nur in führender Ordnung richtig, wenn `g=sqrt(2)t`.

## 5. Neue Herleitung: der vollständige C16 Operator vierter Ordnung

### 5.1 Unveränderter Referenzvertrag

Hier wird genau die konkrete Modellklasse von S6 §1.2 verwendet, nicht eine behauptete vollständige E8 Eichdynamik:

* 16 Spinorgewichtsorte des Clebsch Graphen, 40 Kanten;
* vier fermionische Farben je Ort, harte Belegung höchstens eins;
* 60 harmonische Vermittler, `r=s_i+s_j` und antisymmetrisches Farbpaar;
* Ladung `N_f+2N_b=16`;
* gemeinsame positive Energie Delta pro Vermittler und Vertexamplitude t;
* CAR Reihenfolge `4*site+colour` und die dort angegebene positive Kantenkonvention;
* keine zusätzliche History der geordneten inneren Farben oder dauerhaft protokollierter virtueller Schrittfolgen.

Der Operator ist

\[
H=\Delta N_b+t(B^\dagger+B),\qquad
B^\dagger=\sum_{e,A}b^\dagger_{r(e),A}K_{e,A}.
\]

P bezeichnet alle einfach besetzten Orte ohne Vermittler, Qn den Sektor mit genau n Vermittlern. Weil Gesamtladung und Ortszahl fest sind, ist der vollständige Raum endlich. Es existiert daher ein gewöhnlicher selbstadjungierter Matrixoperator, auch wenn seine vollständige Matrix praktisch nicht gespeichert wird.

### 5.2 Allgemeine Formel mit allen virtuellen Pfaden

Definiere die dimensionslosen Operatoren

\[
M=Q_1B^\dagger P,\quad N=Q_2B^\dagger Q_1,
\quad \mathcal D=M^\dagger M,\quad\mathcal C=NM.
\]

Die kanonische effektive Entwicklung auf dem identifizierten niedrigen P Band lautet für das feste endliche Modell

\[
\boxed{
H_{\rm eff}=-\frac{t^2}{\Delta}\mathcal D
+\frac{t^4}{\Delta^3}\left(\mathcal D^2-\frac12\mathcal C^\dagger\mathcal C\right)
+O(t^6/\Delta^5).
}
\]

Der Ausdruck enthält nicht nur einen ausgewählten Zweibondcluster. M und N summieren alle zulässigen Kanten und alle Besetzungswege.

Eine direkte Herleitung folgt aus dem Schurkomplement. Bis zur relevanten Ordnung ist

\[
H_F(E)=-\frac{t^2}{\Delta}\mathcal D
-\frac{t^2E}{\Delta^2}\mathcal D
-\frac{t^4}{2\Delta^3}\mathcal C^\dagger\mathcal C+\cdots.
\]

Die Energiegleichung ist damit ein verallgemeinertes Eigenwertproblem mit Metrik `I+t^2 D/Delta^2`. Die symmetrische Normalisierung dieser Metrik erzeugt den positiven Term `t^4 D^2/Delta^3`. Der Faktor ein halb im anderen Term stammt aus der Zwischenenergie `2 Delta`. Ungerade Beiträge verschwinden durch Vermittlerparität. Die Zuordnung zum ursprünglichen P Raum ist die kanonisch symmetrisch normalisierte Wahl; andere effektive Basen können unitär äquivalente Operatorformeln besitzen. Der allgemeine rigorose Rahmen ist die Arbeit von Bravyi, DiVincenzo und Loss [W1].

### 5.3 Vollständige lokale Auswertung für C16

Setze

\[
E_e=I-S_e=2P^-_e,\qquad \mathcal D=\sum_eE_e.
\]

Für disjunkte Kanten `e=(i,j)` und `f=(k,l)` vertauscht `T_ef` die gesamten Paare, also die Plätze i mit k und j mit l. Es ist nicht der Swap einer einzelnen Farbe.

Dann ergibt die vollständige Pfadauswertung

\[
\boxed{
F_4=
2\sum_eE_e
+\sum_{\substack{e<f\\e\cap f\ne\varnothing}}\{E_e,E_f\}
-2\sum_{\substack{e<f\\r(e)=r(f)}}E_eE_fT_{ef},
\qquad H^{(4)}=\frac{t^4}{\Delta^3}F_4.
}
\]

Hier ist `{A,B}=AB+BA`. Die drei Summen enthalten genau **40, 160 und 60** Beiträge.

Der Beweis zerlegt alle Pfade:

**Einzelkante.** `E_e^2=2E_e` ergibt die 40 ersten Terme.

**Zwei überlappende Kanten.** Beide Paare können wegen der harten Belegung nicht gleichzeitig entfernt werden. Der Beitrag aus `C^dagger C` fehlt. Der gefaltete Term aus `D^2` bleibt als Antikommutator. Für `e=(i,j), f=(j,k)` ist dies

\[
\{E_{ij},E_{jk}\}=2I-2S_{ij}-2S_{jk}+S_{ij}S_{jk}+S_{jk}S_{ij}.
\]

Er wirkt auf drei Träger und enthält beide Orientierungen eines Dreierzyklus. Da jeder Ort fünf Kanten besitzt, gibt es `16*binom(5,2)=160` solche Paare.

**Disjunkte Kanten mit verschiedenen Vermittlertypen.** Die beiden unabhängigen Zeitordnungen der Erzeugung und Rückkehr liefern einen Beitrag, der sich mit dem entsprechenden Teil von `D^2` genau aufhebt.

**Disjunkte Kanten mit gleichem Vermittlertyp.** Die bosonische Symmetrisierung lässt einen zusätzlichen Austausch der gesamten Sechserzustände übrig. Er ist genau `-8 P_e^- P_f^- T_ef`, also der letzte Summand oben. Jeder der zehn Vektortypen wird von vier disjunkten Kanten geteilt, daher `10*binom(4,2)=60` Beiträge.

**Keine weiteren umgepaarten Viereckwege in dieser Typisierung.** Verschiedene perfekte Paarungen derselben vier Löcher können nicht dieselbe Multimenge von Vektorlabels besitzen: Eine andere Kante mit demselben Label und einem gemeinsamen Endpunkt würde aus `s_i+s_j=s_i+s_k` die falsche Gleichheit `s_j=s_k` verlangen. Damit können keine zusätzlichen Rückpaarungen unter Erhaltung beider Vermittlerlabels beitragen. Diese Aussage wurde für die konkreten viergliedrigen C16 Zyklen zusätzlich vollständig enumeriert.

Das ist ein Operatorbeweis auf dem ganzen P Raum. Die exakten Matrixspalten und die vollständigen kleinen Cluster sind unabhängige Kontrollen des Beweises, nicht sein Ersatz.

### 5.4 Was die beiden früheren Vierkörperformeln wirklich bedeuten

Auf dem 36 dimensionalen Raum zweier antisymmetrischer Paare gilt

\[
-8t^4S_6/\Delta^3
=16t^4P_-^{\rm Paar}/\Delta^3-8t^4I_{36}/\Delta^3.
\]

Beim Einbetten in alle vier Ququarts wird `I_36` zum Projektor

\[
\Pi=P^-_eP^-_f,
\]

nicht zur Identität des ganzen 256 dimensionalen Raums. Diesen Term darf man dort nicht als belanglose Konstante streichen.

Vollständig lautet der Zweibondbeitrag in unserer Normierung

\[
F_4^{ef}=4(P^-_e+P^-_f)-8\Pi T_{ef}\Pi.
\]

Auf dem Sektor, in dem beide Paare antisymmetrisch sind, wird daraus `16 P_-^{Paar}`. Nach Abzug beider Einzelbondkorrekturen bleibt dagegen der verbundene Term `-8 S_6`. Die Quellenformeln sind also vereinbar, wenn der eingeschränkte Träger und die Subtraktion der Einzelbeiträge ausdrücklich mitgeführt werden.

Der gesamte Zweibondraum mit beiden Paarsektoren hat 469 Zustände: 256 ohne, 192 mit einem und 21 mit zwei Vermittlern. Die direkte Diagonalisierung dieses vollständigen Blocks bestätigt den Operator vierter Ordnung. Für `t/Delta=0.025,0.05,0.1` betragen die maximalen Abweichungen zwischen den 256 niedrigen exakten Energien und der Entwicklung bis zur vierten Ordnung ungefähr `3.11e-8,1.95e-6,1.16e-4`, jeweils in Einheiten Delta. Ihre Skalierung ist konsistent mit Ordnung sechs; das ist eine endliche numerische Kontrolle, keine globale Fehlerschranke.

### 5.5 Fehlerkontrolle: ein Prozent pro Cluster ist keine Gesamtaussage

Der einzelne verbundene Koeffizient erfüllt

\[
\frac{8t^4/\Delta^3}{J}=4(t/\Delta)^2,\qquad J=2t^2/\Delta.
\]

Bei `t/Delta=0.05` sind dies ein Prozent, bei `0.1` vier Prozent. Hinzu kommen jedoch alle überlappenden Kanten und alle anderen Cluster. Schon die elementare Dreiecksabschätzung gibt

\[
\|F_4\|\leq160+1280+480=1920,
\quad \frac{\|H^{(4)}\|}{J}\leq960(t/\Delta)^2.
\]

Diese konservative globale Schranke beträgt bei 0.05 noch 2.4 und zertifiziert keine kleine Störung relativ zur Singulettlücke. Sie zeigt nicht, dass die reale Störung so groß ist. Sie zeigt, warum ein lokaler Prozentwert kein globales Zertifikat ist.

Auch die frühere Bedingung `||V||<Delta` wurde für den gesamten C16 bei 1/20 hier nicht bewiesen. Die explizite vierte Ordnung ist geschlossen; eine vollständige Restabschätzung aller höheren Ordnungen und ein thermodynamisch gleichmäßiger Kontrollsatz sind davon getrennte Aufgaben.

## 6. Neue numerische Konsequenz für die C16 Singulettlücke

Die unabhängige Rechnung ergibt im vollständigen Singulettsektor:

\[
E_{0,s}/J=11.04539833706842,
\]

\[
E_{1,s}/J=11.56176212280254
\]

mit vier orthogonalen gefundenen Zuständen auf dem zweiten Niveau. Die Residuen der ersten fünf Zustände sind kleiner als `3.4e-14`; die Orthogonalitätsabweichung aller zehn berechneten Vektoren ist kleiner als `6.7e-15`. Damit ist die frühere Dublettangabe numerisch widerlegt. Ein algebraischer Beweis der exakten Multiplizität und ein Ausschluss aller Nichtsinguletts sind andere Aussagen und wurden nicht geliefert.

Für den vollständigen Operator F4 erhält man

\[
\langle0_s|F_4|0_s\rangle\approx555.488500363836,
\]

während seine vier Eigenwerte im ersten angeregten Quartett numerisch alle

\[
583.29203866638
\]

betragen. Es zeigt sich keine Aufspaltung dieses Quartetts in erster Störungsordnung.

Mit `epsilon=t/Delta` und der festen Energieverschiebung aus H2 gilt

\[
H_{\rm eff}/J+40I=H_C/J+\frac{\epsilon^2}{2}F_4+O(\epsilon^4).
\]

Daraus folgt für die verfolgte Singulettlücke

\[
\boxed{
\Delta_s/J=0.51636378573412
+13.9017691513\,\epsilon^2+O(\epsilon^4).
}
\]

Bei epsilon gleich 0.05 liefert die erste Korrektur `0.551118208612 J`, also rund 6.73 Prozent mehr als der führende Singulettabstand. Dies ist **keine** exakte Lücke des vollständigen Mikromodells bei 0.05: Der Term der Ordnung epsilon hoch vier und sämtliche Nichtsingulettkonkurrenten sind darin nicht kontrolliert. Der Wert zeigt aber eine konkrete, berechnete Konsequenz der zuvor fehlenden 160 Beiträge und der übrigen vierten Ordnung.

## 7. Exakter mikroskopischer Stern statt stiller Gleichsetzung mit dem idealen Stern

Schaltet man einen Viererstern ausdrücklich isoliert, entfernen alle drei erlaubten Vertizes denselben Mittelpunkt. Nach einer Erzeugung eines Vermittlers ist dieser Mittelpunkt leer. Ein weiterer Paarabbau ist daher im vom vollen Eingang erreichbaren Sektor unmöglich.

Eine geschlossene Blockdarstellung, die den vom besetzten Eingang erreichbaren Raum enthält, lautet exakt

\[
H_\star^{\rm mic}=\begin{pmatrix}0&tM^\dagger\\tM&\Delta I\end{pmatrix},
\qquad M^\dagger M=6I-2G_\star,
\quad G_\star=H_\star/J.
\]

Die Dimensionen dieser Darstellung sind 256 und 288. M hat Rang 221; die zusätzlich mitgeführten 67 dunklen Richtungen des oberen Sektors bleiben bei Energie Delta und werden von P aus nicht angeregt. Nach kanonischer Identifikation seines niedrigen Bands lautet die allordentliche effektive Matrix

\[
\boxed{
H_{\star,\rm eff}^{\rm mic}
=\frac{\Delta I-\sqrt{\Delta^2I+4t^2(6I-2G_\star)}}2.
}
\]

Dies wurde durch direkte Diagonalisierung des 544 dimensionalen Blocks überprüft. Die niedrigen Werte sind

\[
E_d=\frac{\Delta-\sqrt{\Delta^2+4t^2d}}2,
\quad d=0,1,\ldots,6.
\]

Der Grundzustand gehört eindeutig zu `d=6`, die erste Anregung zu `d=5`. Die exakte Lücke ist

\[
\Delta_\star^{\rm mic}=
\frac{\sqrt{\Delta^2+24t^2}-\sqrt{\Delta^2+20t^2}}2.
\]

Für Delta gleich eins und t gleich 0.05 ergibt sich `0.00243396875137`, nicht exakt das führende `J/2=0.0025`.

Der mikroskopische Grundzustand ist angekleidet: Sein Gewicht im nackten vollen Belegungsraum ist

\[
\frac12\left(1+\frac\Delta{\sqrt{\Delta^2+24t^2}}\right)
=0.9856429311786321
\]

bei den genannten Werten. Seine Materiekomponente ist Omega, aber der volle Zustand enthält Vermittler und Löcher. Deshalb wird der ideale Achtpunktfilter nicht allein durch Umbenennung von J zu einem exakten Filter des mikroskopischen Spektrums: Die Wurzelabstände sind nicht mehr gleichmäßig kommensurabel. Man benötigt einen passend ausgelegten Filter, kontrollierte Entkleidung oder eine explizite Näherungsanalyse.

Die Isolation des Sterns ist hier weiterhin ein Steuerzugriff. Diese Lösung darf nicht als exakter Teiloperator eines unverändert überall eingeschalteten C16 ausgegeben werden.

## 8. Präparation: ein echtes Hindernis und eine ausdrückliche hinreichende Lösung

### 8.1 Vermittlerverluste allein wählen Omega nicht

Für jeden vollständig symmetrischen Farbzustand psi auf den besetzten Orten gilt

\[
K_{e,A}\psi=0\quad\text{für alle Kanten und Farben}.
\]

Mit Vermittlervakuum ist deshalb `H_mic(psi tensor vacuum)=0`. Werden lediglich gewöhnliche Verlustsprünge `L_mu=b_mu` ergänzt, vernichten auch diese den Zustand. Der gesamte symmetrische Raum bleibt dunkel.

Für vier Träger hat dieser Raum Dimension `binom(7,3)=35`; für 16 Träger Dimension `binom(19,3)=969`. Es gibt also schon eine große explizite Familie anderer stationärer Zustände. Zudem ist der nackte Omega Zustand nicht dunkel unter Paarabbau: Auf vier vollständig verbundenen Trägern ist `sum_e <K_e^dagger K_e>=12`.

Dies widerlegt nicht die Möglichkeit eines geeigneten Reservoirs. Es widerlegt den Schluss, seine bloße Erwähnung liefere automatisch einen eindeutigen Omega Attraktor. Ein temperaturgerechter Kanal auf angekleideten Eigenzuständen, ein Rückpumpmechanismus oder eine andere Kopplung muss tatsächlich spezifiziert werden.

### 8.2 Ein basisunabhängig formulierter Relaxationskanal

Für das ideale Vierträgersystem sei G ein positiver dimensionsloser Elternoperator mit eindeutigem Nullzustand Omega; zum Beispiel der Stern oder Tetramer. Setze `A=|Omega><Omega|` und nehme einen zusätzlichen positiven Reservoirparameter kappa an. Dann definiert

\[
\boxed{
\mathcal L_G(\rho)=
-\frac{iJ}{\hbar}[G,\rho]
+\kappa A\,\operatorname{tr}(G\rho)
-\frac\kappa2\{G,\rho\}
}
\]

einen expliziten Lindbladgenerator.

Eine Kraus beziehungsweise Sprungdarstellung erhält man bei `G=sum_eP_e^+` durch

\[
L_{e,a}=\sqrt\kappa\,|\Omega\rangle\langle a|P_e^+,
\]

wobei a eine vollständige Vierträgerbasis durchläuft. Die Summe ist unabhängig von dieser Hilfsbasis. Es gelten

\[
\sum_{e,a}L_{e,a}^\dagger L_{e,a}=\kappa G,
\qquad
\sum_{e,a}L_{e,a}\rho L_{e,a}^\dagger
=\kappa A\operatorname{tr}(G\rho).
\]

Die vollständige Lösung lautet mit

\[
F_t=e^{-(iJ/\hbar+\kappa/2)Gt}
\]

\[
\boxed{
\rho(t)=F_t\rho(0)F_t^\dagger+
[1-\operatorname{tr}(F_t\rho(0)F_t^\dagger)]A.
}
\]

Für die dimensionslose Lücke delta von G folgt

\[
1-\langle\Omega|\rho(t)|\Omega\rangle
\leq e^{-\kappa\delta t}
[1-\langle\Omega|\rho(0)|\Omega\rangle].
\]

Omega ist eindeutig stationär und global attraktiv. Beim Stern ist delta gleich ein halb, beim Tetramer gleich zwei.

Das ist eine konstruktive Lösung der endlichen Präparationsaufgabe **nach Ergänzung eines konkret definierten Reservoirzugriffs**. Die Sprünge sind nicht die bloßen bosonischen Verlustoperatoren des Mikromodells; sie wirken auf die ganze Vierträgerzelle. Der Reservoirzustand und seine Kopplung sind neue Daten. Bei einem großen Netz wäre zusätzlich die Lokalität einer solchen Konstruktion zu prüfen. Die allgemeine Idee dissipativer Zustandspräparation ist etabliert [W2]; hier wird ein expliziter Kanal für den vorliegenden Elternoperator angegeben.

### 8.3 Ein einziges autonomes U für die endlichen Laborprotokolle ist konstruierbar

Man kann die erlaubten unitären Gatter des idealen Präparations und Echoprotokolls `G_0,...,G_(L-1)` in einen festen autonomen Schritt einbauen:

\[
U_{\rm aut}=\sum_{j=0}^{L-1}|j+1\bmod L\rangle\langle j|\otimes G_j.
\]

Wegen der orthogonalen Clockzustände gilt exakt `U_aut^dagger U_aut=I`. Die Liste kann Hadamards der Filterregister, kontrollierte Potenzen der Sternentwicklung, den lokalen Tick, zwei Pointerkopplungen und den inversen Tick enthalten. Separate Anfangsregister für den ersten und letzten Filter erlauben, alle Ausgänge erst am Ende zu lesen. Erfolgsselektion ist dann eine gemeinsam definierte Endauslesung, kein versteckter Reset unterwegs.

Ein Programmregister kann die zweite Pointeradresse kontrollieren: behalten oder frisch sind dann unterschiedliche deklarierte Eingänge desselben größeren Operators. Sie sind nicht zwei passive Ansichten derselben vollständig festgelegten Eingriffsfolge.

Damit ist die Existenz eines einzigen endlichen reversiblen Laborausführers mathematisch geschlossen. Das Programm, die initialisierten Register, die zugelassenen kontrollierten Entwicklungen und der Anfangszustand stammen dadurch noch nicht aus der E8 Klammer. Der diskrete externe Schritt und eine physische Sekunde werden ebenfalls nicht gleichgesetzt.

### 8.4 Die eingefrorenen Echozahlen bleiben getrennt

Im idealen Modell ergeben sich unverändert:

| Protokoll | Behalten, bedingt | Frisch, bedingt | Neue Rohwerte pro begonnenem Versuch |
|---|---:|---:|---:|
| Dreierzyklus | 1 | 17/32 | 1/6 gegen 17/192 |
| Ausgeglichener CNOT Tick | 1 | 1/2 | 1/6 gegen 1/12 |

Die alten Filter ergeben dagegen `27/512` gegen `459/16384`, beziehungsweise `27/512` gegen `27/1024`. Beide vollständigen Pointerfolgen wurden hier direkt im gemeinsamen System mit zwei Pointerplätzen ausgeführt. Diese Zahlen testen das definierte Quantenprotokoll. Sie sind keine zusätzliche unabhängige Naturkonstante und unterscheiden nicht ohne weitere Vergleichsvorhersagen TFPT von gewöhnlicher Quantenmechanik.

## 9. Symmetrie und Architektur

### 9.1 Der volle Kommutant ist nicht die gesuchte physische Symmetriegruppe

Die in S1 vorgeschlagene Rechnung „Kommutante von H bestimmen; erwartet SU(4) mal W(D5)“ ist so nicht richtig formuliert. Für

\[
H=\sum_EE P_E
\]

enthält der volle unitäre Kommutant stets beliebige Unitaries innerhalb jedes Energieeigenraums, also Faktoren `U(rank P_E)`. Schon unabhängig wählbare Phasen der Energieprojektoren sind viel größer als eine vorgegebene lokale Symmetriegruppe.

Zu untersuchen sind stattdessen etwa ortsweise Tensorproduktwirkungen, Graphautomorphismen und die Erhaltung der gesamten Vertexfamilie. Für einen verbundenen gewöhnlichen Austauschgraphen gilt für eine ortsweise infinitesimale Wirkung `sum_s A_s`: Der Zweiträgeroperatorvergleich erzwingt entlang jeder Kante, dass `A_s-A_t` skalar ist. Nach Entfernen skalarer Gesamtphasen bleibt dieselbe su(4) Wirkung an jedem Ort. Das ist **globale SU(4)**, keine bereits dynamische lokale SU(4) Eichsymmetrie.

### 9.2 Die Spin(10) Belegungsobstruktion bleibt bestehen

Die feste Belegung jedes Spinorgewichtsplatzes ist nicht invariant unter gewöhnlichen kontinuierlichen Spin(10) Mischungen dieser Plätze. Bei der weichen Darstellung mit `H_U=U/2 sum(n_s-1)^2` erzeugt `T_ss'=sum_a c_sa^dagger c_s'a` ein Loch und eine Doppelbelegung, und

\[
[H_U,T_{ss'}]P=U T_{ss'}P\ne0.
\]

Es gibt weiterhin zwei saubere, verschiedene Wege: Clebsch als endliches Kopplungslabor mit kombinatorischer Spinorherkunft; oder Spin(10) als wirkliche innere Materiedarstellung an anderen, noch zu begründenden räumlichen Trägern. Die zweite Lesart erhält nicht automatisch den eben abgeleiteten einfachen SU(4) Austausch: Ein vollständiger Spinorindex verändert den Zweiträgerkanal. Ein Wechsel der Lesart ist eine neue Modellkonstruktion, keine redaktionelle Umbenennung.

## 10. Die korrekten Aufgaben auf dem Weg zur TOE

### 10.1 Raumzeit

Die Identität `det(tI+x.sigma)=t^2-|x|^2` bleibt kinematisch richtig. Die lokalen Clebsch Daten wählen aber keine drei großskaligen Raumrichtungen. Verschiedene Überlagerungen mit derselben lokalen Gradzahl liefern verschiedene Wachstumsdimensionen.

Das Kodimension drei Argument ist nur unter seinen Voraussetzungen ein Selektor: gegebener thermodynamischer Impulsraum, generischer kohärenter Zweikomponentensektor, transversal isolierter Weylpunkt. Es ist kein allgemeiner Dimensionssatz für beliebige Vakuummodelle. Weitere Symmetrien, mehr Komponenten oder nichtisolierte Nullmengen verändern die Aussage.

Ein gemeinsamer Lorentzfixpunkt muss an tatsächlichen Renormierungsflüssen mehrerer Sektoren gezeigt werden. Es gibt keinen allgemeinen Automatismus, nach dem beliebige Geschwindigkeiten unter jeder Wechselwirkung zusammenlaufen. Ein stabiler vollständig gapped Tetramerproduktbereich kann als kontrollierter Startpunkt dienen, enthält aber gerade nicht die verlangten beliebig energiearmen Photon und Gravitonmoden. Die Stabilitätssätze von Yarotsky gelten in ihrer erklärten Gitter und Kleinheitsklasse [W3].

### 10.2 Chirale E8 Naht und vierdimensionale Materie sind zwei Aufgaben

Die positive gerade Gitterkonstruktion liefert die abstrakte unitäre Vertexalgebra V_E8 [W4]. Die Erweiterung von D5_1 und A3_1 ist eine konforme Erweiterung mit passenden Z4 Sektoren, kein ausstehender Kondo Fluss.

Ein invertierbarer Bulk in 2+1 Dimensionen kann einen chiralen E8 Rand in 1+1 Dimensionen tragen [W5]. Dies ist eine konkrete Architektur für die Naht. Sie ersetzt keinen Nachweis von chiralen propagierenden Standardmodellfeldern in 3+1 Dimensionen. Die jeweiligen Dimensionen, Defekte, Randbedingungen und Anomalien müssen durch einen ausdrücklichen Adapter verbunden werden.

Die in S5 zitierte Arbeit von Araki und Mitautoren wurde extern überprüft: Sie existiert als Preprint vom 30. August 2026 und simuliert ein zweidimensionales euklidisches Gitter. Ihr gezieltes Gappen der Spiegelwand ist ein nützlicher Mechanismustest, kein fertiger vierdimensionaler Standardmodellnachweis [W6].

### 10.3 Drei Familien: nicht jeden Diracindex als Familienzahl lesen

Die Ersetzung der Zählformel `(16-1)/5` durch einen geschützten Index ist als Richtung sinnvoll. Die schematische Folgerung aus einer vierdimensionalen Instantonzahl drei zu drei Familien ist aber nicht gerechtfertigt.

Ein Raumzeitinstantonindex zählt chirale Nullmoden eines schon gewählten Fermionoperators im jeweiligen Hintergrund. Die Darstellung geht über ihren Dynkinindex ein; im üblichen flachen SU(N) Fall lautet der Beitrag `2 T(R) Q` [W7]. Mehrere Nullmoden eines bereits vorhandenen Feldes sind nicht automatisch mehrere dauerhaft propagierende Familien dieses Feldes.

Für eine echte Familienrekonstruktion braucht man beispielsweise

\[
\Psi(x,y)=\sum_{a=1}^{3}\psi_a(x)\chi_a(y)+\text{massive Moden},
\qquad D_{\rm int}\chi_a=0,
\]

wobei die drei internen oder transversal lokalisierten Moden nachweislich drei unabhängige vierdimensionale Felder mit den richtigen Ladungen tragen. Ein interner Index kann unter solchen Voraussetzungen die Nettozahl schützen [W8]. Die primitive Regel muss zusätzlich diesen Sektor auswählen, Spiegelpartner kontrollieren und mögliche zusätzliche vektorartige Paare ausschließen. `index=3` allein ist auch dann nicht die ganze Spektralaussage.

### 10.4 Eichfelder und Gravitation

Lokale Basisfreiheit liefert zunächst eine Transformationsregel für Verbindungen. Daraus folgen nicht allein propagierende Eichbosonen, ein Gaussgesetz, ein kinetischer Term oder gemessene Kopplungen.

Für Gravitation muss aus einem abgeleiteten physikalischen Korrelator ein positiver masseloser Spin zwei Pol folgen. Eine diagnostische Form ist

\[
\langle h_{\mu\nu}h_{\rho\sigma}\rangle(p)
\sim\frac{Z_g\Pi^{(2)}_{\mu\nu,\rho\sigma}}{p^2+i0},\qquad Z_g>0.
\]

Zusätzlich braucht man die physische Zustandsreduktion auf zwei Helizitäten, Ward Identitäten, eine gemeinsame universelle Kopplung und einen kontrollierten quantisierten Grenzwert. Weinbergs weiches Emissionsargument beschränkt die Kopplung eines bereits vorhandenen masselosen Spin zwei Teilchens; es erzeugt dieses Teilchen nicht [W9]. Eine gemeinsame Kegelkinematik reicht auch nicht aus, um sämtliche nichtminimalen oder sektorabhängigen Wechselwirkungen auszuschließen.

Eine Spektralwirkung kann ein effektives Ziel organisieren. Die Mannigfaltigkeit, der Diracoperator, seine Darstellung, die Spektralfunktion und ihr Zustand dürfen dabei nicht unbemerkt als zusätzliche fertige Physik eingesetzt werden.

### 10.5 Kopplungen, Skalen und kosmologischer Zustand

Die Alpha Gleichung wurde erneut gelöst:

\[
\alpha^{-1}=137.03599921684071250353786030380388037\ldots.
\]

Die offizielle datierte CODATA Tabelle 2022 nennt `137.035999177(21)` [W10]. Der Abstand ist `1.8971768` experimentelle Standardunsicherheiten. Das ist ein historischer Formelvergleich, kein hier neu erhobener Messwert und keine kontrollierte Theorieunsicherheit.

Dass Alpha auf beiden Seiten einer impliziten Gleichung vorkommt, ist für sich kein Fehler. Das offene Problem ist die Herleitung genau dieser Gleichung als physikalische Thomson Kopplung einschließlich Schema, Schwellen und Fehlerrechnung. Es wäre falsch, dieses Problem allein durch das Verbot einer Selbstkonsistenzgleichung lösen zu wollen.

Die ungünstigen historischen Zweige bleiben erhalten: Myon zu Tau Verhältnis, ältere Higgswerte, einfache Inflationsamplitude und zu kurze Protonlebensdauern der benannten geeichten SO(10) Modelle. Diese Zahlen wurden nicht durch neue Schleifenläufe korrigiert. Frei nachgewählte Transfers sind keine Vorhersagen.

Auch alle Vakuumantworten zusammen wählen nicht automatisch den kosmologischen Anfangszustand. Die Erklärung des Zeitpfeils benötigt Randbedingungen, Reservoirzustand oder einen kontrollierten Grenzprozess. Die Born Regel ist in den verwendeten Matrixmodellen vorausgesetzt; eine eigenständige Herleitung aus anderen Axiomen wäre ein zusätzliches Programm.

### 10.6 Weitere finale Fragen

| Frage | Präziser noch fehlender gemeinsamer Mechanismus |
|---|---|
| Dunkle Materie | Ein konkreter stabiler Sektor, dessen gravitative und sichtbare Kopplungen sowie kosmologische Produktion berechnet werden; ein ungelesenes Register genügt nicht. |
| Dunkle Energie | Eine effektive Vakuumwirkung mit Zustandsgleichung und radiativ stabiler kleiner Energiedichte; kein frei passender Zusatzterm. |
| Materieüberschuss | Symmetrieverletzung, Nichtgleichgewicht und quantitative Ausbeute aus derselben Dynamik. |
| Starke CP Frage | Ein Schutzmechanismus im tatsächlichen fermionischen Maß einschließlich Quarkmassenphasen und Renormierung. |
| Schwarze Löcher | Zunächst der gravitative Sektor, dann Horizonte, Flächenentropie, Verdampfung und Informationstransfer. |
| Arithmetik und RH | Ein nativer phasentreuer Adapter des gesamten relevanten Funktionals. Endliche E8 Identitäten oder positive Gramwerte sind kein RH Beweis. |
| Faktorisierung und P gegen NP | Eigene Algorithmen und Komplexitätsbeweise in der Eingabelänge; eine physikalische TOE impliziert diese Ergebnisse nicht automatisch. |

Diese Anforderungen stammen aus dem umfassenderen Umfang von S5 und S7, nicht erst aus dieser Fortsetzung. Ihre Erfüllung wird hier nicht behauptet.

## 11. Abschließender Status der acht Tore

| Tor | Präziser Zugewinn dieser Runde | Verbleibender Abschluss |
|---|---|---|
| T1 Quelle | Kohärenzverträglicher Vertex, unitäre Reparatur, vollständig deklarierter endlicher Operator | Native Auswahl der Architektur, Belegung, Parameter, Statistik und Zugriffe |
| T2 Naht | Korrekte Trennung von Gitteralgebra, 1+1 Rand und höherdimensionaler Realisierung | Phasentreuer nativer Skalierungsnachweis mit richtiger chiraler Ausführung |
| T3 Raumzeit | Keine Rückkehr zu falschen Grad oder Rangargumenten; klare Propagatortests | Ausgewählte skalierende Geometrie und gemeinsamer Lorentzkegel |
| T4 Materie | Präzisierung des benötigten Familienindex und der Rolle interner Moden | Drei propagierende Familien, Spiegelentkopplung und konsistentes Maß |
| T5 Dynamik | Vollständiger C16 Koeffizient vierter Ordnung; numerische Singulettantwort; exakter isolierter mikroskopischer Stern | Restabschätzung, alle Sektoren, lokaler Vielzellen und Kontinuumsgrenzwert |
| T6 Parameter | Historische Alpha Gleichung reproduziert, kein falsches Verbot impliziter Gleichungen | Physischer Transfer aller Kopplungen, Massen und Skalen mit Unsicherheiten |
| T7 Gravitation | Existenz des Pols klar von Kinematik und universeller Kopplung getrennt | Der tatsächliche quantisierte gravitative Sektor |
| T8 Zustand | Explizites Hindernis für einfache Verluste; hinreichender endlicher Relaxationskanal; autonomer Laborcompiler | Herkunft von Reservoir, Anfangszustand und gemeinsamem kosmologischen Funktional |

Die Reduktion auf drei Überschriften A, B und C ist eine Organisationshilfe, kein Satz, dass danach alle übrigen Fragen automatisch beantwortet seien. Besonders Parameterantworten, Maß, Zustandswahl und empirische Bewährung bleiben eigene Beweislasten.

## 12. Unmittelbar ausführbare Konsequenz

Die neue vierte Ordnung kann den isolierten Zweibondplatzhalter im Referenzvertrag ersetzen. Die falsche geordnete History muss entweder entfernt oder ausdrücklich als anderes, dephasierendes Modell geführt werden. Das nächste gemeinsame Spektralobjekt ist der eben definierte Operator, nicht ein passend gewählter Wechsel zwischen Tetramer, Kette und Clebsch.

Vor einer Behauptung eines kontrollierten C16 Mikromodells bei `t/Delta=1/20` bleiben insbesondere eine Restschranke, die Konkurrenz der Nichtsinguletts und der Abgleich mit den tatsächlichen TFPT Phasen erforderlich. Vor einem physikalischen Vielzellenlimes muss die Vermittlerlokalität festgelegt sein: 60 global geteilte Moden über beliebig viele Zellen erzeugen andere, möglicherweise nicht extensive Wechselwirkungen als lokale Moden pro Zelle mit kontrolliertem Transport. Diese Alternativen dürfen nicht denselben Namen tragen und dann als identischer Ursprung behandelt werden.

**Gesamturteil:** Ein wesentlicher Teil der mikroskopischen Anschlussrechnung ist jetzt tatsächlich weiter geschlossen. Die vollständige TOE ist nicht durch diese endlichen Resultate bewiesen. Der erzielte Fortschritt ist ein reparierter kohärenter Vertex, eine vollständig ausgeschriebene effektive Dynamik bis zur vierten Ordnung und neue daraus berechnete Spektralfolgen. Genau diese überprüfbaren Verbindungen sind belastbarer als eine weitere Gleichsetzung großer Strukturnamen.

## 13. Externe Primärquellen

Die Literatur bestätigt den allgemeinen mathematischen Rahmen, nicht die Herkunft der TFPT Modellwahl und nicht die eigenen hier neu formulierten C16 Resultate.

* W1: Sergey Bravyi, David DiVincenzo, Daniel Loss, *Schrieffer-Wolff transformation for quantum many-body systems*, Annals of Physics 326 (2011), arXiv:1105.0675.
* W2: Frank Verstraete, Michael M. Wolf, J. Ignacio Cirac, *Quantum computation, quantum state engineering, and quantum phase transitions driven by dissipation*, arXiv:0803.1447; Nature Physics 5 (2009).
* W3: Dmitry Yarotsky, *Ground states in relatively bounded quantum perturbations of classical lattice systems*, Communications in Mathematical Physics 261 (2006), arXiv:math-ph/0412040.
* W4: Chongying Dong, Xingjun Lin, *Unitary vertex operator algebras*, arXiv:1308.2361.
* W5: Eugeniu Plamadeala, Michael Mulligan, Chetan Nayak, *Short-Range Entangled Bosonic States with Chiral Edge Modes and T-duality of Heterotic Strings*, Physical Review B 88 (2013), arXiv:1304.0772.
* W6: Sho Araki, Hidenori Fukaya, Tetsuya Onogi, Satoshi Yamaguchi, *Symmetric Mass Generation for Domain-Wall Fermions*, arXiv:2608.29963, 30. August 2026. Preprint, zweidimensionales euklidisches Gitter.
* W7: Pablo Sesma, *A functional treatment of small instanton-induced axion potentials*, JHEP 03 (2025) 026, arXiv:2411.00101. Darstellung und Hintergrundabhängigkeit der Fermionnullmoden.
* W8: *Number of Generations in Free Fermionic String Models*, arXiv:hep-th/9502153. Interner Diracindex in der dort vorausgesetzten Stringkonstruktion; keine TFPT Ableitung.
* W9: Steven Weinberg, *Photons and Gravitons in S-Matrix Theory: Derivation of Charge Conservation and Equality of Gravitational and Inertial Mass*, Physical Review 135 (1964), B1049, DOI:10.1103/PhysRev.135.B1049.
* W10: NIST, vollständige Tabelle der CODATA Anpassung 2022, Zeile *inverse fine-structure constant*, abgerufen am 14. September 2026. Referenzwert 137.035999177 und Standardunsicherheit 0.000000021.
