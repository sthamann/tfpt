# Der präzise gemeinsame E8-Kern

Stand: 10. September 2026. Eigenständige exakte Nachrechnung klassischer ADE-/Thom–Sebastiani-Strukturen, keine neue Behauptung einer Weltformel. Rechnerische Kontrolle: exact_check.py und exact_results.json. Alle Matrizen sind ganzzahlig; keine numerischen Eigenwertentscheidungen werden verwendet.

## 1. Welche Singularität gemeint ist

Wir betrachten ausdrücklich den komplexen holomorphen Funktionskeim
\[
F:(\mathbb C^3,0)\longrightarrow(\mathbb C,0),\qquad
F(x,y,z)=x^2+y^3+z^5.
\]
Die drei Zahlen allein bestimmen diesen Keim nicht: Die Wahl einer Brieskorn–Pham-Summe, der komplexen Grundstruktur und der isolierten kritischen Stelle ist Teil der Voraussetzungen.

F ist quasihomogen mit Gewichten (15,10,6) und Grad 30:
\[
15xF_x+10yF_y+6zF_z=30F.
\]
Seine Jacobi-Algebra ist
\[
\mathcal J_F=\mathbb C[x,y,z]/(F_x,F_y,F_z)
 =\mathbb C[y,z]/(y^2,z^4).
\]
Die acht Monome \(e_{ab}=y^az^b\), \(0\le a\le1\), \(0\le b\le3\), bilden eine Basis. Damit ist
\[
\mu(F)=8.
\]
Dies ist ein Dimensionssatz über den angegebenen Keim, keine zusätzliche freie Wahl einer Acht.

Eine miniverselle Deformation hat die Gestalt
\[
F_{\lambda}=F+\sum_{a=0}^1\sum_{b=0}^3\lambda_{ab}y^az^b .
\]
Die Gewichtshomogenität weist dem Parameter \(\lambda_{ab}\) das Gewicht
\[
d_{ab}=30-10a-6b
\]
zu. Sortiert erhält man
\[
\boxed{\{2,8,12,14,18,20,24,30\}.}
\]
Das ist exakt die Gradliste der grundlegenden Weyl-Invarianten von E8. Die Identifikation der miniversellen Basis mit \(\mathfrak h_{\mathbb C}/W(E_8)\), einschließlich simultaner Auflösung nach dem Weyl-Überzug, ist ein klassischer Brieskorn–Slodowy-Satz. Die explizite Rechnung hier bestimmt die acht Parameter und ihre Gewichte; sie ersetzt nicht den allgemeinen Deformationssatz. Eine aktuelle Primärquelle mit E8-Gleichung und Gradliste ist [Shepherd-Barron, §4, Tabelle auf S. 13](https://arxiv.org/pdf/1711.10439).

Wichtig: E8 ist eine einfache Singularität, besitzt also keine kontinuierliche Modalität innerhalb seines analytischen Singularitätstyps. Die acht Parameter der miniversellen Familie sind dennoch reale zusätzliche Daten bei der Auswahl einer deformierten Faser; sie sind keine acht Moduli desselben unveränderten E8-Keims.

## 2. Monodromie braucht das richtige Volumenbein

Die geometrische gewichtete Rotation
\[
h(x,y,z)=(-x,\zeta_3y,\zeta_5z)
\]
erhält F. Ihre Wirkung auf der bloßen unitalen Jacobi-Algebra ist
\[
\sigma(e_{ab})=\zeta_{30}^{10a+6b}e_{ab}.
\]
Sie hat Ordnung 15 und fixiert 1. Deshalb darf sie nicht ungeprüft mit der Ordnung-30-Wirkung auf den verschwindenden Kohomologieklassen gleichgesetzt werden.

Bei einer Gelfand–Leray-/Residuedarstellung mit dem Volumenbein
\[
\omega_{ab}=e_{ab}\frac{dx\wedge dy\wedge dz}{dF}
\]
kommt der Faktor
\[
\det h=(-1)\zeta_3\zeta_5=\zeta_{30}
\]
hinzu. Da \(h^*dF=dF\), ergibt sich
\[
T(e_{ab}\otimes\mathrm{vol})
 =\zeta_{30}^{1+10a+6b}(e_{ab}\otimes\mathrm{vol}).
\]
Die Exponenten sind
\[
\{1,7,11,13,17,19,23,29\}.
\]
Somit hat T die Ordnung 30 und das charakteristische Polynom
\[
\Phi_{30}(t)=t^8+t^7-t^5-t^4-t^3+t+1.
\]
Die Wahl der inversen geometrischen Monodromie kehrt sämtliche Eigenphasen um; die Exponentenmenge und der folgende Isomorphietyp bleiben gleich.

Der Twist ist kein nebensächlicher Vorfaktor: T ist auf diesem Modell eine lineare Wirkung auf einem mit dem Volumenbein versehenen Raum; es ist keine unitale Algebraautomorphie von \(\mathcal J_F\), denn \(T1=\zeta_{30}1\). Die gleichzeitige Erhaltung von Multiplikation, Monodromie und Auslesen verlangt daher entsprechend typisierte Räume und Abbildungen.

Für das festgelegte F und Volumenelement lautet die Grothendieck-Residuespur
\[
\operatorname{Res}_F(p)=
\frac1{(2\pi i)^3}\oint
\frac{p\,dx\,dy\,dz}{(2x)(3y^2)(5z^4)}
=\frac1{30}[yz^3]p.
\]
Also
\[
\langle e_{ab},e_{cd}\rangle_{\rm res}
=\frac1{30}\,\delta_{a+c,1}\delta_{b+d,3}.
\]
Die reelle symmetrische Matrix hat Signatur (4,4). Sie ist nicht die positive E8-Gitterform. Der volumengetwistete T erhält diese bilineare Paarung, weil die Exponenten komplementärer Monome sich zu 30 addieren. Ein positiver physischer Zustand folgt aus dieser Residueform nicht.

## 3. Ein expliziter integraler Isomorphismus erhält Paarung und ganzen Zyklus

Für \(n=3,5\) sei \(S_n\) die \((n-1)\times(n-1)\)-Matrix mit 1 auf der Diagonalen und -1 direkt darüber. Setze
\[
S=S_3\otimes S_5,\qquad B=S+S^{\mathsf T},\qquad
M=-S^{-1}S^{\mathsf T}.
\]
Der Faktor für \(x^2\) ist die skalare Seifertmatrix [1]. Dies ist die positive Cartan-/Seifert-Konvention für den Thom–Sebastiani-Tensor von \(x^2,y^3,z^5\). Die geometrische orientierte Schnittform der aufgelösten komplexen Fläche ist deren negative E8-Form; sie wird nicht mit B ohne Vorzeichen identifiziert.

Der zugehörige klassische Satz und ein anderer expliziter Basiswechsel stehen in [Brillon–Ramazashvili–Schechtman–Varchenko, §§3–4, insbesondere Satz 2 und Lemma 2](https://amj.math.stonybrook.edu/pdf-Springer-final/017-0065.pdf). Der folgende konkrete U ist unsere eigene ganzzahlige Nachrechnung in der angegebenen Knotenreihenfolge.

Sei A die E8-Cartanmatrix mit Diagonalwerten 2 und Kanten
\[
(1,3),(3,4),(4,5),(5,6),(6,7),(7,8),(2,4).
\]
Für die einfachen Spiegelungen \(s_i=I-e_iA_{i,\bullet}\) sei
\[
C=s_1s_2s_3s_4s_5s_6s_7s_8,
\]
mit Spaltenvektorkonvention. Definiere
\[
U=\begin{pmatrix}
-1&0&0&1&1&0&0&-1\\
-1&0&1&0&1&0&0&0\\
-1&0&0&1&1&1&0&-1\\
-2&0&1&1&1&1&0&-1\\
-1&-1&1&1&1&1&0&-1\\
-1&0&0&1&1&0&1&-1\\
-1&0&0&1&1&0&0&0\\
-1&0&0&0&1&0&0&0
\end{pmatrix}.
\]
Direkte ganzzahlige Multiplikation beweist
\[
\boxed{\det U=1,\qquad U^{\mathsf T}AU=B,\qquad UM=CU.}
\]
Die führenden Hauptminoren von B sind
\[
2,3,4,5,6,4,2,1.
\]
Sylvesters Kriterium zeigt \(B>0\); B ist gerade und unimodular. Damit ist U zugleich ein integraler Gitterisomorphismus und ein vollständiger Monodromie-Intertwiner. Insbesondere gilt für alle ganzen k und alle Gittervektoren p,q:
\[
U M^k=C^kU,\qquad
(M^kp)^{\mathsf T}Bq=(C^kUp)^{\mathsf T}A(Uq).
\]
Somit bleiben beliebige Kompositionen des deklarierten Zyklus und alle durch diese Paarung gebildeten Antworten erhalten. Hier wird der zentrale Universalraum-Anspruch an einer konkreten, begrenzten Struktur wirklich erfüllt.

Auch die feinere Seifertstruktur geht nicht verloren. Weil \(S(I-M)=B\) und 1 kein Eigenwert von M ist,
\[
S=B(I-M)^{-1}.
\]
Setzt man \(S_E=A(I-C)^{-1}\), folgt aus den beiden Isomorphiegleichungen
\[
U^{\mathsf T}S_EU=S.
\]
Unser exakter Prüfer kontrolliert auch diese Identität. Außerdem:
\[
M^{30}=I,\quad M^{15}=-I,\quad
\det(M^{10}-I)\ne0.
\]
Der 3er-Zyklus \(M^{10}\) ist deshalb keine Projektion auf drei Generationen. Er ist eine Ordnung-3-Wirkung auf einem acht-dimensionalen Raum und besitzt hier keine invarianten Vektoren.

Diese Brücke identifiziert polarisierte Gitter samt Monodromie. Sie identifiziert nicht automatisch die Jacobi-Multiplikation mit einer E8-Lieklammer oder einer physischen Operatoralgebra. Insbesondere ist der Tensor der Seifertmatrizen entscheidend: B ist die Symmetrisierung dieses Tensors, im Allgemeinen nicht das gewöhnliche Tensorprodukt der positiven Cartanmatrizen der Faktoren.

## 4. Die verschiedenen Vierertakte sind nicht austauschbar

Aus
\[
\operatorname{Gal}(\mathbb Q(\zeta_{30})/\mathbb Q)
\cong(\mathbb Z/30)^\times\cong C_2\times C_4
\]
folgt eine Spektrenpermutation \(g_7:\zeta_{30}\mapsto\zeta_{30}^7\) der Ordnung 4. Sie ist keine Potenz von M: Die zyklische Gruppe der Ordnung 30 hat kein Element der Ordnung 4.

Eine konkrete integrale Realisierung von \(g_7\) erhält man auf
\(\mathbb Z[t]/(\Phi_{30})\) durch \(p(t)\mapsto p(t^7)\).
Der Prüfer baut ihre Matrix P und den integralen Übergang zur Coxeterdarstellung auf. Es gilt
\[
P^4=I,\qquad PC=C^7P
\]
in den jeweiligen gleichen Koordinaten. Für den von unserer festen zyklischen E8-Basis transportierten positiven Gram G gilt jedoch \(P^{\mathsf T}GP\ne G\).
Explizit besitzt der Vektor \(1+t^2\) vor der Substitution Normquadrat 4, danach 6. Damit ist genau dieser naive Galois-Übertrag kein isometrischer TFPT-Clock. Andere zusätzliche Normalizerkonstruktionen werden damit nicht ausgeschlossen.

Noch direkter: Eine Wirkung J mit \(J^2=-I\) kann nicht zugleich
\[
JCJ^{-1}=C^7
\]
erfüllen. Zweimalige Konjugation ergäbe einerseits C, andererseits \(C^{49}=C^{19}\), im Widerspruch zur Ordnung 30. Der Galoistakt und eine gaußsche Multiplikation mit i sind daher verschiedene Verträge.

Der native aktuelle TFPT-Prüfer v1010 bestätigt außerdem einen anderen, präzise festgelegten Ausschluss: Auf seinen beiden mod-2-Modellen hat der Gaussian-Clock Ordnung 2, der gewählte Gray-Clock Ordnung 4; die CP-Nilpotentränge sind 2 beziehungsweise 4. Ein linearer Isomorphismus kann diese festgelegten Operationen nicht gleichzeitig intertwinen. Derselbe native Code weist ausdrücklich eine schwächere Brücke nach, welche das nilpotente Bein und die Paarung erhält. Unser Satz aus §3 steht dazu nicht im Widerspruch: Dort werden andere, geometrisch richtige Operationen erhalten.

## 5. Der arithmetische Übergang braucht eine gewählte integrale Struktur

Über \(\mathbb C\) darf man 2,3,5 in den partiellen Ableitungen invertieren. Über \(\mathbb Z\) ist das nicht erlaubt. Die freie Rang-8-Algebra
\[
\mathcal J^{\rm flat}=\mathbb Z[y,z]/(y^2,z^4)
\]
ist ein bewusst gewähltes integrales Modell der komplexen Jacobi-Algebra; sie entsteht durch primitive beziehungsweise saturierte Ableitungsrelationen.

Die tatsächliche Jacobi-Algebra des mod-2 reduzierten Polynoms ist dagegen
\[
\mathbb F_2[x,y,z]/(y^2,z^4),
\]
weil \(F_x=2x=0\). Sie ist unendlichdimensional. Fügt man zusätzlich F als Tjurina-Relation hinzu, erhält man
\[
\mathbb F_2[x,y,z]/(x^2,y^2,z^4)
\]
der Dimension 16. Ebenso ergeben sich in Charakteristik 3 und 5 unendliche Jacobi-Dimension und Tjurina-Dimension 12 beziehungsweise 10. Alle drei Gröbnerbasen werden exakt nachgerechnet.

Der acht-dimensionale native mod-2-„Milnor“-Träger ist deshalb nicht allein durch formales Reduzieren der komplexen Jacobi-Definition gerechtfertigt. Eine gewählte flache Integralform kann sinnvoll sein; ihre Herkunft und ihre Operationen müssen mitgegeben werden. Dieser Befund behauptet nicht, dass die reduzierte Fläche keinen rationalen Doppelpunkt mehr hat. Die schlechte Charakteristik verändert gerade die Verbindung zwischen Ableitungsalgebra, Deformation und komplexem Milnorgitter. Siehe hierzu auch [Shepherd-Barron, Einleitung und §4](https://arxiv.org/pdf/1711.10439).

## 6. Klein-Invarianten und die wirkliche Auflösung

In zwei Variablen u,v setze
\[
\begin{aligned}
f_{12}&=uv(u^{10}+11u^5v^5-v^{10}),\\
H_{20}&=-(u^{20}+v^{20})+228(u^{15}v^5-u^5v^{15})-494u^{10}v^{10},\\
T_{30}&=u^{30}+v^{30}+522(u^{25}v^5-u^5v^{25})
-10005(u^{20}v^{10}+u^{10}v^{20}).
\end{aligned}
\]
Der Prüfer beweist als reine Polynomidentitäten
\[
\operatorname{Hess}(f_{12})=121H_{20},\quad
\operatorname{Jac}(f_{12},H_{20})=20T_{30},\quad
H_{20}^3+T_{30}^2=1728f_{12}^5.
\]
Die klassische Invariantentheorie identifiziert den invarianten Ring der binären Ikosaedergruppe \(2I\subset SU(2)\) mit
\[
\mathbb C[f_{12},H_{20},T_{30}]
\cong
\mathbb C[a,b,c]/(b^3+c^2-1728a^5).
\]
Durch eine nichtverschwindende komplexe Skalierung ist dies der Keim \(x^2+y^3+z^5=0\). Die Normierungen und die Ringdarstellung sind direkt bei [Nash, §2, Gleichungen (2.4)–(2.7)](https://arxiv.org/pdf/1308.0955) nachzulesen.

Die minimale komplexe Auflösung besitzt acht rationale Ausnahmekurven, deren Schnittmatrix \(-A\) ist. Ihr Link ist die Poincaré-Homologiesphäre \(S^3/2I\), mit Fundamentalgruppe von Ordnung 120. Dies ist die präzise Bedeutung von „(2,3,5) wird durch Auflösung zu E8“: Es entsteht das E8-Schnittmuster der Ausnahmekurven; eine Auflösung erzeugt nicht von sich aus eine vierdimensionale Lorentz-Dynamik oder das Standardmodell.

Es gibt immerhin eine kurze echte Auswahlrigidität. Sind \(2\le p\le q\le r\) paarweise teilerfremde ganze Zahlen und ist
\[
\frac1p+\frac1q+\frac1r>1,
\]
so ist \((p,q,r)=(2,3,5)\). Beweis: Für \(p\ge3\) ist wegen der Teilerfremdheit \(q\ge4,r\ge5\), also die Summe höchstens \(1/3+1/4+1/5<1\). Somit p=2. Wäre q≥5, so wäre die Summe höchstens \(1/2+1/5+1/5<1\). Also q=3, und aus \(1/r>1/6\), \(r\ge3\) und der Teilerfremdheit folgt r=5. Umgekehrt ist die Summe 31/30.

Unter genau diesen Voraussetzungen ist das sphärische dreifach verzweigte Brieskorn-Modell eindeutig. Ohne Teilerfremdheit gibt es unter anderem alle sphärischen Tripel (2,2,n). Die hier benutzte positive Orbifold-Eulerzahl ist nicht ohne weiteren Satz identisch mit TFPT-Reflexionspositivität.

## 7. Was trotzdem nicht eindeutig ist

Die komplexe minimale Auflösung ist durch den Keim eindeutig bis zum passenden Isomorphismus. Das positive, vorzeichennormierte Gitter B aus §3 ist ebenfalls konkrete zusätzliche Struktur, nicht „beliebig“. Trotzdem folgt daraus keine eindeutige räumliche Riemann-Metrik.

Die Kronheimer-Realisierung verwendet Momentenniveaus
\[
\boldsymbol\zeta\in\mathfrak h_{\mathbb R}\otimes\mathbb R^3.
\]
Das sind beim markierten E8-Modell 24 reelle Periodenkoordinaten vor Weyl-/weiteren Identifikationen. Bei festgehaltener komplexer Auflösung bleiben die Kählerperioden der acht Ausnahmekurven frei innerhalb einer zulässigen Kammer. Schon gemeinsame Skalierung verändert ihre Flächen, ohne den Singularitätstyp oder die E8-Schnittmatrix zu ändern. Die nackte Zahl 24 ist daher kein Anspruch, nach allen geometrischen Quotienten stets genau 24 physisch verschiedene Parameter zu zählen. [Hitchins Primärarbeit, §§1–2](https://academic.oup.com/qjmath/article/76/1/337/7990706) erläutert die zusätzlich nötigen Twistor-, Real- und symplektischen Daten; [Yans Konstruktion, §§3 und 7](https://arxiv.org/pdf/2310.10979) hält die Momentenniveaus ausdrücklich im Bauplan.

Auch bei festem B und festem M bleiben Zustands- und Zeitdaten nicht ausgewählt. Komplexifiziere das reelle Gitter und verwende \(p^\dagger Bq\) als positive Hermiteform. M ist unitär und hat acht verschiedene Eigenlinien. Für beliebige \(p_j>0\) mit \(\sum p_j=1\) ist
\[
\rho=\sum_{j=1}^8p_jP_j
\]
ein positiver normierter, M-invarianter Zustand. Die Singularität plus ihr ganzer Zyklus wählt aus dieser Familie keinen bestimmten physikalischen Zustand aus.

Selbst wenn man zusätzlich fordert, dass eine kontinuierliche unitäre Entwicklung nach einer vorgegebenen Zeit \(\tau>0\) exakt M ergibt, sind die selbstadjungierten Generatoren nicht eindeutig. Sei \(MP_j=e^{i\theta_j}P_j\). Dann gilt für alle ganzen \(n_j\)
\[
H_{\mathbf n}=\sum_j\frac{-\theta_j+2\pi n_j}{\tau}P_j,\qquad
e^{-i\tau H_{\mathbf n}}=M.
\]
Hinreichend große \(n_j\) geben positive H. Verschiedene Branchzahlen ergeben verschiedene Zwischenzeitdynamiken bei unverändertem Gitter, Zustandsträgertyp und vollständigem diskretem Monodromieschritt. Ohne Festlegung von \(\tau\) bleibt zusätzlich die Zeitskala frei.

Eine Singularitätsauflösung ist somit ein geometrischer Konstruktionsprozess. Sie ist nicht schon ein Gesetz, mit welcher physikalischen Geschwindigkeit, welchem Zustand und welchem Wechselwirkungsterm sich die Welt entwickelt.

## 8. Das stärkste daraus tragbare Universalraum-Modell

Ein belastbarer gemeinsamer Träger ist hier das System aus
\[
\bigl(F_\lambda,\ \mathcal J_{F_\lambda},\
\text{Volumen-/Residuelinie},\
H_2(F_\lambda,\mathbb Z),\
\text{Seifert-/Schnittform},\
\text{Gauss–Manin-Transport}\bigr)
\]
über der Deformationsbasis. Die McKay-/Quiver-Seite fügt bei gewählten Momenten- und Realstrukturdatensätzen geometrische Realisierungen hinzu. „Universell“ bedeutet in diesem Satz: eine miniverselle Deformationsstruktur und ein expliziter operationserhaltender Vergleich der E8/Milnor-Darstellungen. Es bedeutet nicht Universalität für sämtliche physikalischen Prozesse.

Der Satz aus §3 liefert ein tatsächlich bezahltes Stück dieses Systems. Der nächste physische Herkunftssatz müsste aus derselben nativen Seam-Quelle zugleich die passende Integralform, den Volumentwist, die ausgewählte Familie beziehungsweise Periode und die tatsächliche Zustands-/Zeitwirkung ableiten. Die Kenntnis der gemeinsamen Acht oder des gemeinsamen 30er-Spektrums ersetzt keinen dieser Intertwiner.

## 9. Zwei vollständig bewiesene Fixpunkt-Aussagen innerhalb der Bauvorschrift

Die native Pascal-/Gluebalance aus v6 ist stärker als eine beliebige Zahlenkoinzidenz. Für positive ganze g lautet sie
\[
2^{g-1}=1+g+\binom g2=\frac{g^2+g+2}{2}.
\]
Sie besitzt genau die Lösung g=5. Zum Beweis definiere
\[
f_g=2^{g-1}-\frac{g^2+g+2}{2}.
\]
Die Werte für g=1,2,3,4 sind negativ, \(f_5=0\), und exakt gilt
\[
f_{g+1}=2f_g+\frac{g(g-1)}2.
\]
Daraus folgt induktiv \(f_g>0\) für alle g>5. Dieser Beweis umfasst alle positiven ganzen g, keinen endlichen Suchbereich. Die native Formel \(N=(2^{g-1}-1)/g\) liefert dann N=3.

Eine zweite, unmittelbare Kompatibilitätsrigidität verbindet additive Carrier-/Familien-Rank und Milnor-Rank. Vorausgesetzt seien
\[
g\ge N\ge2,\qquad F=x^2+y^N+z^g,\qquad
g+N=\mu(F)=(g-1)(N-1).
\]
Dann
\[
(g-2)(N-2)=3.
\]
Beide Faktoren sind nichtnegative ganze Zahlen; wegen \(g\ge N\) bleibt nur
\[
g-2=3,\quad N-2=1,\quad (g,N)=(5,3).
\]
Damit folgt \(\mu(F)=g+N=8\). Ohne die Ordnungskonvention kommt die vertauschte Lösung hinzu. Die Zahl 8 muss in diesem konditionalen Satz nicht vorher eingesetzt werden.

Die Grenze ist klar: Diese beiden Auswahlbeweise setzen ihre jeweilige Kompatibilitätsgleichung voraus. Dass gerade diese Rang- beziehungsweise Exterior-/Gluebalance vom rohen physikalischen Prozess notwendig erfüllt wird, ist ein eigener Herkunftssatz. Die Eindeutigkeit der Lösung einer Bauvorschrift beweist nicht die Eindeutigkeit aller möglichen Bauvorschriften.
