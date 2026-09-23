# TFPT: Quellenantwort und Operatoranschluss

21. September 2026 · Fortsetzung auf Basis des eingesandten Nichtlinearitäts-/Möbiustests

**Gesamturteil: PARTIAL. Die vollständige physikalische TFPT-Herleitung ist nicht erreicht. Zwei endliche algebraische Anschlussfragen sind jetzt geschlossen; die vorhandene bedingte Quelle liefert zusätzlich eine gemeinsame Paar-/Vermittler-Zeitantwort mit kontrolliertem Grenzwert.**

## Was sich gegenüber dem letzten Gesamt-PDF geändert hat

### 1. Der vollständige W-Vorzeichenanschluss ist jetzt geprüft

Das bisherige PDF ließ beim rohen affinen E8-Stromkanal einen basis- und kokzyklusgenauen Restvergleich offen. Dieser Vergleich wurde nun an der unveränderten archivierten nativen Tensorbank ausgeführt.

Ergebnis: Die E8-Stromklammer ohne zusätzliche ungerade Felddressierung und der native 60×2016-Tensor W stimmen in einer gemeinsamen Basiskonvention überein. Geprüft sind alle 480 nichtverschwindenden Einträge und alle 120480 Nulleinträge. Eine gemeinsame Lösung von 2032 Vorzeichengleichungen in 176 Basiszeichen, Rang 167, erhält zugleich die 40 nichtdiagonalen Spin(10)-Wurzelwirkungen und die zwölf SU(4)-Wurzelwirkungen auf Fermion- und Vermittlerlabels. Die Cartanmarkierungen bleiben dieselben.

Das schließt eine tatsächliche endliche Restlücke. Es bestimmt keine physikalische Zeit, keine mikroskopisch ausgewählte Phasenkonvention und keine CAR-Feldinterpretation der bosonischen affinen Ströme. Der vollständige signierte Vergleich im **ungerade dressierten** Randmodell existierte bereits vorher; neu ist der ausdrückliche Rückzug auf die rohe affine Klammer und ihr Vergleich mit derselben nativen Bank.

### 2. Die Nichtlinearität des nativen Modells ist explizit und am signierten Tensor bestätigt

Für die antisymmetrischen Paarmatrizen Q_A mit P_A=Σ_(i<j)(Q_A)_ij f_j f_i und a_A=P_A/√8 gilt

\[
[a_A,a_B^\dagger]
=\delta_{AB}I-\frac18 f^\dagger Q_B^\dagger Q_Af.
\]

Die Reihenfolge Q_B†Q_A ist wesentlich und wurde durch eine direkte komplexe CAR-Kontrolle samt falscher Reihenfolge als Gegenprobe überprüft. Am vollständigen signierten Tensor gelten

\[
\operatorname{Tr}(Q_B^\dagger Q_A)=16\delta_{AB},\qquad
\sum_A Q_A^\dagger Q_A=15I_{64}.
\]

Die im Eingangstext angegebene Summenregel folgt deshalb exakt:

\[
\sum_A[a_A,a_A^\dagger]=60I-\frac{15}{8}N_f.
\]

Die Gleichung ist keine neue Sättigungsannahme. Sie ist eine Folge der kanonischen Fermionrelationen innerhalb des nativen Modells. Aus ihr folgt weiterhin nicht, dass die ursprüngliche Naht diese kanonischen Felder oder H+ erzeugt. Insbesondere darf ein Mittelwert der Pauliantwort nicht an Stelle des Operators in die Bewegungsgleichung eingesetzt werden.

### 3. Eine gemeinsame Zustands- und Zeitrekonstruktion gelingt aus vorhandenen Quellenfeldern

Für die bereits bestehende zehnkanalige Randkonstruktion war die vollständige bilokale Paarantwort schon bekannt:

\[
G(v)=d(v)I+o(v)W^\dagger W,
\quad d(v)=\frac{v^2(2-v)}{2(1-v)^3},
\quad o(v)=\frac{2-v}{2(1-v)^2}.
\]

Diese alte Grundlage wurde frisch reproduziert. Neu wurde der lokale Vermittlerzustand aus derselben Quelle **gemeinsam** mit den bilokalen Paarzuständen behandelt. Ihre Überlappung wird erhalten und durch die positive Gram-Matrix normiert.

Für jeden endlichen Abstand hat die gemeinsame Einsetzung vollen Rang

\[
2016+60=2076.
\]

Im kontrollierten Koinzidenzgrenzwert bleiben 60 Quellenzustände der Energie 3, 60 erste Nachfahren der Energie 4 und 1956 dunkle Zustände der Energie 5. Alle diese Zustände waren bereits in der Quelle vorhanden. Ein zusätzlicher Oszillator ist für diesen Zustandsanschluss nicht nötig.

Für das ausdrücklich einzeln normierte, symmetrisch orthogonalisierte Einsetzungsprotokoll ergibt sich der helle Block

\[
K_{b,0}=\begin{pmatrix}7/2&-1/2\\-1/2&7/2\end{pmatrix},
\qquad K_{d,0}=5I_{1956}.
\]

Die gesamte Antwort bei endlichem Abstand ist ebenfalls ausgeschrieben. Mit rho als Quadrat des Einfügeabstands gilt die gleichmäßige Echtzeitkontrolle

\[
\sup_t\|R_\rho(it)-e^{-itK_0}\|
\le\min\{2,4\rho+\sqrt{3\rho}\}.
\]

Dies ist ein bedingter Satz mit derselben Quelle, demselben Zustand und derselben zugeordneten Zeit. Die endliche Separation selbst besitzt weiter eine unendliche Spektralleiter; ihr erster Zeitmoment ist nicht schon ein autonomer endlicher Hamiltonoperator.

## Die entscheidende Grenze dieser positiven Konstruktion

Die neue Polarabbildung erhält Zustandsnormen, Gruppenwirkung und Zeit im Grenzwert. Sie erhält nicht automatisch die ursprünglichen Feldprodukte. Ihre unabhängigen hellen Zustände sind Superpositionen aus lokalem Primärzustand und dessen Nachfahren.

Ein strenger Kontrolltest verhindert deshalb eine falsche Schlussfolgerung: Ändert man nur das relative Gewicht der beiden Einsetzungen um lambda, bleiben die Quellenenergien drei und vier unverändert. Der aus den orthogonalisierten Labels abgelesene maximale Austausch ändert sich jedoch zu

\[
P_{\max}(\lambda)=\frac{4\lambda^2}{(1+\lambda^2)^2}.
\]

Bei lambda=1 ergibt sich vollständiger Austausch; bei lambda=2 nur 16/25. **Ein perfekter Austausch in dieser Darstellung ist damit noch keine von der Quelle ausgewählte elementare Wechselwirkung.** Die bekannte native Fock-Vakuumtheorie darf nicht über diese Zustandsabbildung übertragen werden.

Auch die relative Schur-Sättigung löst die Ursprungsfrage nicht: Nach Abzug der zwei Einteilchenenergien erscheint im hellen Block ein rang-eins Rest. Der absolute Quellenblock hat aber Energien drei und vier. Der relative Abzug ist weder eine neue globale Vakuumenergie noch eine Herleitung genau des alten H+ auf dem vollen Fockraum.

## Was der eingesandte Text bestätigt und was nicht übernommen wurde

Die Schranke 8/27 für die festgehaltene affine Möbiuszuordnung und der zweite Zeitjet diag(0,6|xi|²) wurden symbolisch nachgeprüft. Der Positivitätsschluss bei eindeutigem Vakuum gilt auf der angegebenen Formdomäne: Eine zum Vakuum orthogonale Nullrichtung eines positiven komprimierten Blocks wäre eine echte zusätzliche Nullrichtung. Für einen durch Delta nach unten beschränkten angeregten Quellraum folgt die angegebene Schur-Ungleichung durch Einsetzen des Vektors (x,−Omega_b^−1 Cx) in die quadratische Form.

Diese Aussagen werden mit ihren Voraussetzungen übernommen. Die im Eingangstext genannten externen 36 CAR-Checks und numerischen Leiterläufe waren nicht als separate Dateien beigefügt; sie werden nicht als hier ausgeführte Läufe verbucht. Stattdessen wurden die oben benannten eigenen Kontrollen und der vorhandene Originalchecker ausgeführt.

## Der verbleibende Ursprungsschritt

Die erste zusätzlich gewählte Struktur ist weiterhin die physische zehnkanalige Randquelle einschließlich ihrer geladenen Sektoren. Innerhalb dieses Kandidaten folgen weitere freie Daten: die Randenergie Vaux beziehungsweise ihre zulässigen Deformationen, der Zustand, die konkrete Zeitzuordnung und das Präparations-/Ableseprotokoll.

Der nächste gültige Herleitungsschritt ist daher konkret:

1. Aus dem unabhängig definierten ursprünglichen Nahtkern und Transfer die tatsächlichen geladenen Feldoperatoren und ihren Zustand bestimmen.
2. Mit diesen Operatoren deren gemeinsame Zeitkorrelatoren berechnen, ohne Gamma, Vaux oder einen gewünschten RR-Block einzusetzen.
3. Für eine behauptete Rückverbindung **dieses** Randkandidaten die Ladungen, Produkte, Gram-Matrix und Zeitantwort vergleichen. Die Energien 3,4,5 sind dabei ein Test dieses Kandidaten, kein vorgeschriebenes Ergebnis jeder möglichen TFPT-Lösung.

Solange dieser Pfeil fehlt, würde eine Erweiterung des jetzt gefundenen Zweiteilchenblocks zu einem beliebigen Vielteilchenmodell wieder eine zusätzliche Modellannahme einführen. Diese Erweiterung wurde nicht vorgenommen.

**Damit sind der signierte algebraische Quellenanschluss und die native Pauliantwort gesichert, und ein gemeinsamer bedingter Zustands-/Zeitanschluss ist konstruiert. Die physische Auswahl dieser Quelle und die vollständige gemeinsame 3+1D-Theorie bleiben offen. T1–T8 sind nicht geschlossen.**

## Belege

Die beigefügte ausführliche Herleitung `JOINT_RESPONSE_PROOF.md`, der native Vorzeichenaudit, das Quellenaudit, das unabhängige Review und die normal/optimiert identischen Zertifikate dokumentieren Voraussetzungen und Prüfgrenzen. Das Paket ist unter `UR.SOURCE.JOINT_RESPONSE.01` als `PARTIAL` auffindbar; keine Paper- oder Ledgerpromotion.
