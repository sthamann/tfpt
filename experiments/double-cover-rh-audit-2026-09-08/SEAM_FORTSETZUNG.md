# Quellenprüfung der Seam-Kovarianz und ihrer Reflexion

**Weiterführende Rechnung:** [GEOMETRIE_UND_READOUT.md](GEOMETRIE_UND_READOUT.md)
liefert inzwischen eine explizite Boundary-erhaltende rationale Reflexion,
ein exaktes Hindernis für gleichzeitige 3+2-Erhaltung und eine QWZ-Umkehr
zwischen entgegengesetzten Holonomien. Die Boundary-Mischung des unten
beschriebenen ersten Zeugen ist somit nicht notwendig.

Stand: 8. September 2026. Fortsetzung der [Screenshot-Analyse](ANALYSE.md).
Lokaler Forschungsbefund im eigenen Auditordner; keine Statuspromotion.

**Der vorgeschlagene Kovarianztest gelingt für eine explizite räumliche
Reflexion des vorhandenen endlichen QWZ-Modells. Im gekoppelten 16D-Compiler
ist eine clock-erhaltende lineare Reflexion dagegen exakt ausgeschlossen.
Eine clock-umkehrende algebraische Reflexion existiert dort, ist aber noch
keine identifizierte geometrische TFPT-Involution.**

Das ist eine konkrete Eingrenzung der Screenshot-Idee. Es liefert weder eine
Identifikation mit der vollständigen Zeta-Funktion noch einen neuen
Faktorisierungsmechanismus. Die Rechnungen benötigen keine Primzahlen oder
Riemann-Nullstellen als Eingaben. „Aus der Quelle“ bedeutet hier: aus den
vorhandenen endlichen Modellkonstruktoren, nicht aus bereits bewiesenen
vollständigen physikalischen TFPT-Gleichungen.

## 1. Der tatsächlich geprüfte Satz

Für eine treue endliche Kovarianz, also \(0<C<I\), sei

\[
K(C)=\log((I-C)C^{-1}).
\]

Eine unitäre Involution \(U\) mit \(UCU^{-1}=I-C\) erfüllt dann
\(UK(C)U^{-1}=-K(C)\). Für
\(C_\beta=(I+e^{\beta H})^{-1}\), \(\beta>0\), sind Komplementierung von
\(C_\beta\) und Vorzeichenwechsel von \(H\) äquivalent. Die Umkehrformel
ist endlichdimensionaler Funktionalkalkül; der Inhalt des Tests ist die
unabhängige Herkunft von \(H\), \(C\) und \(U\).

[`v258_dirac_covariance_induction.py`](../../verification/v258_dirac_covariance_induction.py)
demonstriert die Inversion an aus vorgegebenem \(H\) erzeugten Zuständen.
[`v440_seam_lto_rp_beta.py`](../../verification/v440_seam_lto_rp_beta.py)
verwendet ein Spielmodell mit bereits eingebautem Vorzeichenwechsel.
Beide werden hier nicht als unabhängige Herleitung einer Seam-Reflexion gezählt.

## 2. Gekoppelter 16D-Compiler: ein exaktes Hindernis

Die Integer-Matrizen stammen aus dem unveränderten Konstruktionspräfix von
[`seam_state_derivation_probe.py`](../tfpt-discovery/seam_state_derivation_probe.py):
Bitform, Arf-Auswahl, Duaden, C6-Wirkung und Orbitverdrahtung. Der Extraktor
[`seam_source.py`](seam_source.py) endet vor der numerischen KMS-Konstruktion
und protokolliert Quellhash und fünf originale Quellprüfungen.

Mit \(J_2=\begin{pmatrix}0&1\\-1&0\end{pmatrix}\) lautet die untersuchte Familie

\[
A_0=\bigoplus_{j=1}^8J_2,\qquad B=A_{\rm int},\qquad
H(u,t)=-i(uA_0+tB).
\]

\(A_0,B\) sind reell antisymmetrisch und kommutieren mit der realen orthogonalen
C6-Matrix \(O\). Der naheliegende Paarwechsel \(U_0=I_8\otimes\sigma_x\)
kehrt \(A_0\) um, aber nicht \(B\). Bei \(u=1,t=1/8,\beta=1\) ist sein
größter Eintragsfehler in \(U_0CU_0+C-I\) rund **0,04908**.

Das Scheitern ist unter einer präzisen Zusatzbedingung allgemein:

\[
\operatorname{Tr}(OA_0)=0,\qquad
\operatorname{Tr}(OB)=-6,\qquad
\operatorname{Tr}(OH)=6it.
\]

Gäbe es einen invertierbaren **komplex-linearen** Operator \(U\) mit
\(UOU^{-1}=O\) und \(UHU^{-1}=-H\), müsste Spurkonjugation
\(\operatorname{Tr}(OH)=-\operatorname{Tr}(OH)\) liefern. Für \(t\ne0\)
ist das unmöglich. Dies schließt alle solchen linearen Operatoren aus, nicht
nur Paarwechsel oder eine bestimmte Parametrisierung.

**Geltungsbereich:** genau diese gekoppelte Familie und Clock-Erhaltung.
Eine Reflexion mit \(UOU^{-1}=O^{-1}\) ist nicht ausgeschlossen. Bei
\(\beta=0\) ist \(C=I/2\) trivial komplementär. Für antiunitäre Operatoren
gilt das obige Spurargument nicht.

Tatsächlich gilt für komplexe Konjugation automatisch
\(\overline H=-H\) und \(\overline C=I-C\). Das folgt schon aus der reellen
Majorana-Antisymmetrie. Es darf nicht als Nachweis eines räumlichen Blattwechsels,
einer TFPT-spezifischen Dualität oder einer Reflexionspositivität ausgegeben werden.

## 3. Derselbe Compiler erlaubt eine Clock-Umkehr

Die exakten linearen Bedingungen

\[
M=M^T,\quad MA_0=-A_0M,\quad MB=-BM,\quad MO=O^TM
\]

haben in der reell symmetrischen Klasse einen 18-dimensionalen Lösungsraum.
Eine dokumentierte Linearkombination der Nullraumbasis mit Koeffizienten
\(1,\ldots,18\) liefert ein invertierbares \(M\) mit

\[
\det M=1673473636107010048407789888.
\]

Die vollständige rationale Matrix steht im [Ergebniszertifikat](seam_covariance_results.json).
Ein zuvor untersuchter Koeffizientenvektor aus Einsen war singulär; die Auswahl
ist ausdrücklich keine Eindeutigkeits- oder Kanonizitätsaussage.

Durch Funktionalkalkül folgt aus dem exakten Zertifikat

\[
U=M(M^2)^{-1/2},\qquad U^2=I,\qquad U^T=U,
\]
\[
UA_0U=-A_0,\qquad UBU=-B,\qquad UOU=O^{-1}.
\]

Damit komplementiert \(U\) die ganze thermische Familie, nicht nur einen
numerischen Zustand. Es wurden keine gewünschten Eigenwerte vorgegeben.
Die numerischen Eintragsfehler liegen unter \(5\cdot10^{-15}\).

**Die physikalische Lücke bleibt konkret:** dieser Zeuge mischt die zehn
Carrier- mit den sechs Boundary-Komponenten. Sein Kommutator mit dem
Boundary-Projektor hat maximalen Eintrag rund **0,3955**. Eine geometrische
Lokalität, ein kanonisches Auswahlprinzip oder die Identität mit dem angehobenen
\((12Y-I)/5\) sind nicht bewiesen.

Die separate Parent-Kovarianzfamilie aus
[`v911_wiring_freedom.py`](../../verification/v911_wiring_freedom.py) besitzt
hingegen bereits eine rahmenabhängige Lösung: Für
\(A_{\rm parent}=\begin{pmatrix}\kappa C_C&tV\\-tV^T&mB_B\end{pmatrix}\)
komplementiert der transportierte Paarwechsel
\(U_{\rm frame}=gU_0g^T\), \(g=\operatorname{diag}(C_C,I_6)\), die Kovarianz
\((I+iA_{\rm parent})/2\), sofern diese treu ist. Das wurde symbolisch geprüft.
Diese Familie ist nicht die vollständige gekoppelte KMS-Familie oben; das
Rahmenargument hebt deren Clock-Hindernis nicht auf.

## 4. QWZ-Seam: explizite räumliche Lösung

Für den aktuellen Streifen-Konstruktor aus
[`v998_seam_modular_closure.py`](../../verification/v998_seam_modular_closure.py)
mit homogener reeller Masse und symmetrischen offenen Querrändern setze

\[
U_y=R_y\otimes\sigma_y,
\]

wobei \(R_y\) die Reihenfolge der Querpositionen umkehrt. Das ist ein
komplex-linearer unitärer Operator. Er vertauscht die beiden Ränder und
wirkt zusätzlich auf den zweikomponentigen Spinor.

Die Onsite-Matrix lautet
\(\sin(p)\sigma_x+(M-\cos p)\sigma_z\), die gerichtete Querkopplung
\(T_y=\sigma_y/(2i)-\sigma_z/2\). Exakt gelten

\[
\sigma_y\sigma_x\sigma_y=-\sigma_x,\quad
\sigma_y\sigma_z\sigma_y=-\sigma_z,\quad
\sigma_yT_y^\dagger\sigma_y=-T_y.
\]

Die Ortsreflexion vertauscht die beiden Kopplungsrichtungen. Deshalb gilt
\(U_yH(p)U_y=-H(p)\) für alle Impulse, jede endliche Breite und jede
homogene reelle Masse. Für den Zylinder funktioniert
\(I_{N_x}\otimes U_y\) auch mit dem vorhandenen Twist in Längsrichtung.
Somit folgen bei endlichem \(\beta\) Komplementierung und modularer
Vorzeichenwechsel. Die Reflexion wurde direkt aus Orts- und Pauli-Struktur
gebildet, nicht durch Anpassen von Eigenvektoren an ein Ziel.

Eine einseitige skalare Randstörung \(0{,}1I_2\) bricht die Identität;
\(\operatorname{Tr}H\) wird 0,2. Dieser Kontrollfall zeigt die Bedeutung der
Randannahmen. Er ist nicht als unter allen TFPT-Axiomen zulässige Störung
ausgewiesen. Auch eine solche chirale Symmetrie beweist keine positive
Weil-Form und identifiziert keinen Zeta-Operator.

## 5. Beide Ränder sind für den Readout wesentlich

Ein fester zweidimensionaler Unterraum \(W\) aus oberem Randspinor
\((1,-1)/\sqrt2\) und unterem Randspinor \((1,1)/\sqrt2\) erfüllt
\(U_yW=W\sigma_y\). Diese Vektoren sind die Randanker bei \(p=0,M=1\);
für andere Impulse werden sie nur als fester Kompressionsraum verwendet,
nicht als behauptete exakte Eigenmoden.

Für \(C_W=W^\dagger CW\) folgt damit

\[
\sigma_yC_W\sigma_y=I_2-C_W,\qquad
\sigma_yK(C_W)\sigma_y=-K(C_W).
\]

Ein einzelner Rand ist unter \(U_y\) nicht invariant. Beispielsweise beträgt
der skalare Komplementierungsfehler bei Breite 8, \(p=0{,}7,\beta=1\)
rund **0,3102**. Eine interne Ein-Rand-Reflexion folgt hier nicht.

Außerdem gilt im Allgemeinen
\(K(W^\dagger CW)\ne W^\dagger K(C)W\). Im selben Beispiel beträgt
der größte Eintragsunterschied rund **0,002753**. Für einen komprimierten
modularen Readout muss der Logarithmus nach der Kompression berechnet werden.

Der volle Grundzustandsprojektor hat Eigenwerte 0 und 1. Sein globaler
endlicher modularer Logarithmus ist daher nicht definiert. Unsere Rechnung
verwendet endliche Temperatur und schneidet keine Eigenwerte künstlich ab.
Eine komprimierte Grundzustandskovarianz müsste separat auf Treue geprüft werden.

## 6. Bedeutung und nächster Entscheidungspunkt

| Zweig | Ergebnis dieser Fortsetzung | Noch fehlender Übergang |
|---|---|---|
| TFPT-Seam | Explizite räumliche Reflexion des endlichen QWZ-Regulators; algebraische Clock-Umkehr des 16D-Compilers | Quellbegründete Identifikation der Trägerräume, Randabbildungen und konkreten TFPT-Involution |
| RH | Der endliche modulare Vorzeichenwechsel kann ohne Zeta-Nullstellen als Eingabe gelingen | Unendlicher kompatibler Skalenraum, Maß/Zentrierung, exakte arithmetische Spur und globale Positivität mit vollständiger Nullstellenzuordnung |
| Faktorisierung | Kein neuer N-abhängiger Rechenweg untersucht oder gewonnen | Effiziente Gewinnung faktortragender Daten aus N einschließlich aller Vorbereitungs- und Regulatorkosten |

Der nächste lokale Entscheidungspunkt ist **ein Intertwiner zwischen der
konkreten Carrier-/Boundary-Konstruktion und dem reflektierten Seam-Readout**.
Er muss die betroffenen Räume, die Clock-Wirkung und die Involution gleichzeitig
abbilden. Dabei ist zuerst festzulegen und aus der Quelle zu begründen, ob der
geometrische Blattwechsel die Clock erhält oder umkehrt. Das ist keine freie
Umetikettierung: Erhaltung ist für die gekoppelte Compilerfamilie bereits
ausgeschlossen.

Insbesondere kommutiert die oben gefundene QWZ-Querreflexion mit der
Längstranslation. Eine exakte Identifikation, die zugleich Compiler-Clock mit
dieser Translation und Compiler-Reflexion mit dieser Querreflexion identifiziert,
kann bei nichtverschwindender Kopplung nicht funktionieren, sofern der
identifizierte Unterraum invariant ist. Andere Abbildungen, Clock-Umkehr oder
andere Unterräume sind dadurch nicht pauschal ausgeschlossen.

Erst eine solche kompatible Abbildung würde die zwei positiven endlichen
Konstruktionen zu einem gemeinsamen TFPT-Mechanismus verbinden. Wiederholtes
Prüfen gerader Determinanten würde diese Lücke nicht schließen.

## 7. Reproduktion und Evidenzgrenze

Aus dem Repository-Stamm:

```sh
experiments/tfpt-discovery/.venv/bin/python experiments/double-cover-rh-audit-2026-09-08/seam_covariance_probe.py
experiments/tfpt-discovery/.venv/bin/python experiments/double-cover-rh-audit-2026-09-08/check_seam_certificate.py
```

- [Hauptprobe](seam_covariance_probe.py): **32/32 Prüfungen bestanden**;
  darunter exakte Matrixrelationen, 60 thermische Streifenfälle und sechs
  Zylinderfälle. [Protokoll](seam_covariance.log).
- [Separater Zertifikatsprüfer](check_seam_certificate.py): gespeicherten
  rationalen Zeugen ohne erneute Nullraumsuche geprüft; symbolische
  QWZ-Streifen mit freien Onsite-Parametern unabhängig zusammengesetzt.
  [Protokoll](seam_certificate.log).
- Die beiden Prüfer teilen den Extraktor der originalen 16D-Quelle. Die
  Zertifikatsprüfung ist daher keine unabhängige Herleitung dieser Quelle.
- [Messdaten und Quellhashes](seam_covariance_results.json), SymPy 1.14.0,
  NumPy 2.4.6. Quellhashänderungen lassen die Zertifikatsprüfung fehlschlagen.

Die allgemeinen endlichen Aussagen beruhen auf den angegebenen algebraischen
Identitäten und dem Funktionalkalkül. Numerische Gitter sind Regressionen,
kein Beweis eines unendlichen Grenzübergangs. Bestehende globale Verifier und
Faktorisierungsbenchmarks wurden in dieser Fortsetzung nicht erneut ausgeführt.
