# TFPT: Vorwärtsprüfung des Dirac-Quellenanschlusses

21. September 2026 · UR.SOURCE.YUKAWA_FORWARD_GATE.01 · PARTIAL

**Die vollständige physische Lösung ist nicht gefunden. Die vorhandenen Flavor-/Yukawa-Ergebnisse bleiben bestehen. Der direkte Anschluss des vorhandenen freien NS-Quellenfensters über den Logarithmus seiner Vakuumkovarianz liefert aber keinen endlichen Diracblock bei festem Maßstab.** Die fehlende Herkunft kann nicht durch die bereits korrekte Rückrechnung in v258 ersetzt werden.

## Was erhalten bleibt

Das erneut geprüfte Originalledger führt die Quarkverhältnisse auf dem hergeleiteten Selektorstratum unter FLAV.QRATIO.01 und FLAV.RIGID.02 als geschlossen. FLAV.LEPTONC.01 führt die exakten Leptonkoeffizienten (16/7,4/3,7/6). FLAV.UPOINT.01 führt die Reduktion der neun geladenen Amplituden auf den gemeinsamen Anker v_geo als [I]+[A]. Das sind die bestehenden typisierten Ergebnisse, keine neuen unabhängigen Beweise dieser Runde.

CONTRACT.QFT4D.DIRAC.01 unterscheidet ausdrücklich zwischen diesen vorhandenen Daten und der Konsistenz ihres Operatoranschlusses. Auch die endlichen positiven NCG-/Higgsbefunde bleiben erhalten. Das neue symmetrische E8-Stromprodukt liefert weiterhin den vollständigen 100+720-Kanal; sein Operatoranschluss im bedingten D8-Modell wird nicht zurückgenommen. Keines dieser Ergebnisse bestimmt automatisch den ursprünglichen physischen Feldzustand und dessen gemeinsame Zeit.

## Der konkrete Vorwärtsversuch

Verwendet wurde die bereits vorhandene, unveränderte QWZ-Quelle des Vertrags `microscopic-charged-car-limit`: Breite 8, Masse 1, Sektor 1. Ihr wirklicher gefüllter Zustand ist der negative Spektralprojektor P_N des Quell-Hamiltonoperators. Ihre Zeit wird vom ursprünglichen reskalierten Operator D_N=N H_N/(2π) erzeugt.

Die eingebetteten Felder stammen aus dem bereits zuvor untersuchten rohen Fourierblock j=(-1,0,1). Seine Gram-Matrix ist bis zu etwa 6×10^-16 die Identität. Eine Gram-Normierung verändert daher nur die Basisnormierung. **Diese drei Moden sind räumliche Fouriermoden, keine drei Teilchenfamilien und nicht der physische 48-/96-dimensionale Materieträger.** Genau dieser feste Quellenanschluss wird geprüft.

Die Kompression wurde direkt aus dem gefüllten Quellenzustand berechnet:

  A_N=S_N† P_N S_N.

Es wurden weder Zielmassen noch eine Yukawamatrix noch Gamma, Vaux oder ein gewünschter RR-Block eingesetzt. Der volle Logit wurde ohne Eigenwert-Clipping ausgewertet.

| N | Eigenwerte von A_N | Kleinster Betrag eines Logit-Eigenwerts |
|---:|---|---:|
| 8 | 0,000149250; 0,0339818; 0,992739 | 3,34736 |
| 16 | 0,0000104625; 0,00398832; 0,999332 | 5,52039 |
| 32 | 0,000000689909; 0,000343003; 0,999950 | 7,97743 |

Die tatsächlichen dimensionslosen Zeiteigenwerte im Grenzblock sind dagegen (-3/4,1/4,5/4). Der Zustand nähert sich einem reinen Projektor mit Eigenwerten (0,0,1); sein modularer Logarithmus nähert sich keinem endlichen Matrixblock. Die ursprüngliche QWZ-Wirkung liefert für theta=2π(j−1/4)/N exakt den Mittelwert −N sin(theta)/(2π) und die Varianz [N(1−cos(theta))/(2π)]². Daraus folgt die Schranke

\[
\|A_N-\operatorname{diag}(0,0,1)\|
\le b_N=\tan^2\!\left(\frac{5\pi}{4N}\right)\longrightarrow0.
\]

Für N≥8 besitzt deshalb jeder endliche Logit-Eigenwert mindestens den Betrag log[(1−b_N)/b_N], der gegen unendlich geht. Das ist ein analytischer Grenzschluss. Dasselbe Argument gilt für jedes andere feste vollständige endliche Fourierfenster; eine andere feste Modenzahl löst dieses Problem nicht. Andere lokale oder nichtinvariante Teilkompressionen werden dadurch nicht ausgeschlossen.

## Exakter Test der gemeinsamen Quelle

Für jede reine globale Kovarianz C²=C und jede orthogonale Trägerprojektion P gilt, auf PH und mit Q=I-P,

  C_F(1-C_F)=(QCP)†(QCP),    C_F=PCP|PH.

Ein treuer reduzierter Zustand 0<C_F<I benötigt also nichtverschwindende Kreuzkorrelationen mit dem ausgeschnittenen Rest. In der geprüften Quelle verschwindet dieser Gram im Grenzwert. Numerisch stimmt die Identität bis etwa 3×10^-16.

Die wirkliche Zeit liefert einen zweiten, unabhängigen Test:

  Ph²P-(PhP)²=(QhP)†(QhP).

Dieser Defekt stimmt in der Quellenrechnung bis etwa 9×10^-15 mit dem direkt berechneten Gram überein. Er darf beim Vergleich der Zeitantwort nicht weggelassen werden.

Eine exakt autonome komprimierte unitäre Zeit erfordert QhP=0. Ist C der Spektralprojektor desselben h, dann bleibt C_F selbst ein Projektor. Deshalb können in dieser direkten endlichen CAR-Kompression reine globale Quelle, exakt autonome komprimierte physische Zeit und treuer endlicher KMS-Dirac nicht gleichzeitig vorliegen. Das ist eine Aussage über diese präzisen Voraussetzungen, kein allgemeines No-go für TFPT, lokale Typ-III-Netze, gemischte Zustände, Kasparov-Produkte oder einen kontrollierten wechselwirkenden IR-Grenzwert.

Für eine nichtinvariante Kompression muss die gesamte komprimierte Resolvente verglichen werden:

  P(z-h)^-1P = [z-PhP-PhQ(z-QhQ)^-1QhP]^-1.

Der zweite Term hält die Wirkung des übrigen Quellraums fest. Das ist der bekannte Feshbach-Schur-Zusammenhang; er wird hier als Prüfregel verwendet, nicht als neu erfundene TFPT-Dynamik.

Außerdem gilt für den vollen endlichen Logit die genaue Chiralitätsbedingung

  gamma logit(C_F) gamma = -logit(C_F)
  genau dann, wenn gamma C_F gamma = I-C_F.

Die Chiralität einer unabhängig berechneten Quellenkovarianz muss somit selbst geprüft werden. Ein nachträgliches Wegprojizieren ihres geraden Anteils stellt keine vollständige KMS-Inversion her.

## Was die thermische Lesart ändert

Als ausdrücklich bedingter Kontrollzweig wurde derselbe Grenzgenerator h in seinem KMS-Zustand betrachtet. Dann ist C_beta=(I+exp(beta h))^-1 treu und logit(C_beta)=beta h. Bei beta=1 ergibt der feste Block die Besetzungen (0,222700;0,437823;0,679179) und den Logit (5/4,1/4,-3/4).

Damit verschwindet das Singularitätsproblem, aber es erscheint genau das schon vorhandene Modenspektrum. Diese Rechnung wählt weder einen physischen thermischen Zustand aus der ursprünglichen Naht aus noch erzeugt sie eine neue Flavorhierarchie. Beta oder mu_geo wurden nicht aus der Rohquelle hergeleitet. Ein Quellenzustand darf nicht allein deswegen gewählt werden, weil sein Logit die gewünschten Yukawas zurückliefert.

## Was für einen Abschluss weiterhin konkret fehlt

Die Originalquellen und die einschlägigen späteren Verträge liefern im geprüften Pfad noch nicht gemeinsam:

1. den unabhängig definierten vollständigen rohen Nahtoperator beziehungsweise das geladene Quellenfunktional;
2. eine daraus ausgewählte Abbildung auf die tatsächlichen lokalen chiralen Materiefelder, einschließlich des physischen Trägers und der Higgsantwort;
3. den Nachweis, dass dieselbe Abbildung Produkte, Zustand, Ladungen und physische Zeit trägt;
4. den anschließenden Vergleich mit der bereits festgelegten TFPT-Yukawastruktur.

Die ursprüngliche P1-Formulierung deklariert Orientierung, Reflexionspositivität, Einheitswindung und c3. Der vorhandene Drei-Zustands-Transfer bestimmt seine endliche Auslesedynamik. Beide sind wertvolle festgelegte Daten, enthalten im geprüften Quellenpfad aber noch keine vollständige Vorschrift für das oben verlangte geladene Funktional. Das ist die belegte Herkunftslücke; ihre Unmöglichkeit wird nicht behauptet.

Dieser Befund beendet die direkte Identifikation des reinen festen NS-Modenfensters mit einem endlichen KMS-Yukawablock. Er rechtfertigt keine weitere Anpassung dieses Fensters an Zielmassen. Die offene physische Aufgabe bleibt die Quellenherleitung des richtigen Materieträgers samt Zustand und Dynamik. Sie wird hier ausdrücklich nicht als erledigt ausgegeben. Auch ein künftiger positiver Diracanschluss würde die weiteren 3+1D-, Chiralitäts-, Kontinuums- und Gravitationspflichten nicht ohne deren eigene Beweise schließen.

## Belege

- `PROOF.md`: ausgeschriebene endliche Kompressions-, Chiralitäts- und Zeitargumente.
- `native_covariance/RESULT.md`, `checker.py`, `results.json`: ursprüngliche Quellparameter, tatsächliche Kompression, Zeitmomente und analytische QWZ-Schranke.
- `covariance_compression_review_20260921.md`: unabhängige mathematische Prüfung.
- `yukawa_source_provenance_20260921.md`: Quellenprüfung einschließlich der vorhandenen Lean-Schnittstellen und der früheren zielunabhängigen modularen Konstruktion v724.
- [Peschel: Calculation of reduced density matrices from correlation functions](https://arxiv.org/abs/cond-mat/0212631): Standardgrundlage des modularen Logarithmus im quasifreien reduzierten Zustand.
- [Dusson, Sigal, Stamm: The Feshbach-Schur map and perturbation theory](https://arxiv.org/abs/2105.02058): Standardgrundlage des effektiven Resolventenoperators.

Quellen werden mit Hashes dokumentiert. Die endlichen Zahlen sind numerische Auswertungen; die allgemeinen Identitäten und die Grenzwertschranke sind analytische Argumente. Keine Paper-/Ledger-Promotion, kein empirischer Anspruch, kein geschlossenes physisches T1–T8-Gate.
