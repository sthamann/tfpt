# TFPT: Prüfung der lokalen Randzeit und ihres Ursprungs

21. September 2026 · Contract **UR.SOURCE.LOCAL_TIME_ORIGIN.01** · Verdict **PARTIAL**

## Ergebnis und Auftrag

Der untersuchte Text ist der am 21. September eingereichte Anhang „Der neue Befund lässt sich konstruktiv weiterführen: Die chirale Polarisation …“. Sein mathematischer Kern ist richtig: In einer genau beschriebenen skalaren Scheibenklasse lässt sich klassifizieren, wann der positive geometrische Randoperator der Betrag einer lokalen Zeit erster Ordnung ist. Die zusätzliche geometrische Vierteldrehung reduziert diese Klasse auf eine konstante Randdichte.

Das ist eine bedingte Auswahlregel, noch keine Herleitung der geladenen TFPT-Quelle. Der Abgleich mit den Originalen liefert zwei konkrete Ergebnisse: Der bekannte Recovery-Transfer ist nicht direkt die Zeit eines einzigen solchen Kreisprozesses; die P1-Nahtwindung ist nicht identisch mit der determinantentreuen Hypercharge-Schleife. Der im Original beschriebene andere Kandidat mit ungerader Determinantenklasse bestimmt durchaus eine interne Bündelklasse. Ihre Verknüpfung mit der ursprünglichen Quelle, der Feldstatistik und der räumlichen Spinstruktur ist noch zu beweisen.

Ziel bleibt der vorwärts hergeleitete gemeinsame Datensatz aus Feldern, Zustand, Ladungen, Produkten, Gram-Matrix und Zeitantwort. Weder ein gewünschter RR-Block noch Gamma, Vaux oder die Energien 3,4,5 wurden eingesetzt. Bestehende algebraische Flavor-/Yukawa-Ergebnisse werden hier nicht neu berechnet oder als physischer Quellennachweis umgedeutet.

## 1. Der lokale Zeitsatz: exakter Beweis mit Operatorbereichen

Sei \(q\in C^\infty(S^1,\mathbb R)\) strikt positiv, \(\rho=q^{-1}\), und
\[
H_\rho=L^2(S^1,\rho\,d\theta),\qquad D=-i\partial_\theta,
\qquad\Lambda_\rho=q|D|.
\]
Es gelten periodische skalare Randbedingungen. Der Operator \(\Lambda_\rho\) ist die positive selbstadjungierte Realisierung des skalaren DtN-Operators einer konformen Scheibenfüllung. Seine Form ist
\[
\langle f,\Lambda_\rho g\rangle_\rho
=\langle f,|D|g\rangle_{L^2(d\theta)}.
\]
Insbesondere liegt die Konstante in seinem Kern. Unter der unitären Abbildung \(f\mapsto\rho^{1/2}f\) auf den ungewichteten Raum wird daraus \(\rho^{-1/2}|D|\rho^{-1/2}\). \(q|D|\) ohne diese Gewichtsinformation wäre im Allgemeinen nicht symmetrisch im ungewichteten Raum.

**Satz.** Ein skalarer selbstadjungierter Differentialoperator erster Ordnung \(h\), mit glatten Koeffizienten und periodischer Domäne, erfüllt \(|h|=\Lambda_\rho\) genau dann, wenn
\[
q(\theta)=q_0+a\cos\theta+b\sin\theta,
\qquad q_0>\sqrt{a^2+b^2}.
\]
In diesem Fall sind genau \(h=\pm qD\) möglich. Die Gleichheit meint vollständige Operatorgleichheit, nicht bloße Isospektralität.

**Notwendige Form von h.** Weil \(1\in\ker\Lambda_\rho\), gilt \(h1=0\). Schreibt man \(h=a_1(\theta)D+b_0(\theta)\), verschwindet folglich \(b_0\). Formale Selbstadjungiertheit verlangt reelles \(a_1\) und \((\rho a_1)'=0\), also \(a_1=cq\) mit reeller Konstante \(c\). Der Vergleich der führenden Symbole von \(h^2\) und \(\Lambda_\rho^2\) liefert \(c^2=1\). Damit ist \(h=\pm qD\).

**Vollständige Fourierbedingung.** Auf glatten Funktionen ist
\[
h^2=\Lambda_\rho^2
\quad\Longleftrightarrow\quad
DqD=|D|q|D|.
\]
Für \(q(\theta)=\sum_k q_ke^{ik\theta}\) hat die Differenz im ungewichteten Fourierkoordinatensystem die Matrix
\[
A_{mn}=(|m||n|-mn)q_{m-n}.
\]
Für beliebiges \(k\ge2\), \(m=1\), \(n=1-k\), ist
\[
A_{1,1-k}=2(k-1)q_k.
\]
Die Gleichheit erzwingt deshalb alle \(q_k=0\) für \(k\ge2\); die Realität von \(q\) erledigt \(k\le-2\). Umgekehrt kann der Vorfaktor nur für strikt entgegengesetzte Vorzeichen von \(m,n\) ungleich null sein. Dann ist \(|m-n|\ge2\). Bei Fourierträger \(\{-1,0,1\}\) verschwinden also alle Matrixelemente, nicht nur ein endlicher Testblock.

**Domänen und Hinreichendheit.** Für glattes positives \(q\) sind beide Operatoren elliptisch erster Ordnung mit periodischer Sobolevdomäne \(H^1\); ihre Quadrate haben Domäne \(H^2\), und glatte Funktionen sind gemeinsame Kerne im Sinne der graphnormdichten Ausgangsbereiche. Die bewiesene Gleichheit auf diesem Bereich geht auf die selbstadjungierten Quadrate über. Weil \(\Lambda_\rho\ge0\), gilt die eindeutige positive Quadratwurzel \(\Lambda_\rho=\sqrt{h^2}=|h|\).

**Vierteldrehung.** Erst unter der zusätzlichen Identifikation der Compilerclock mit der geometrischen Wirkung \(\theta\mapsto\theta+\pi/2\) muss \(q\) viertelinvariant sein. Dann sind nur Indizes in \(4\mathbb Z\) zulässig. Der Schnitt mit \(\{-1,0,1\}\) ist \(\{0\}\): \(q=\kappa\), \(h=\pm\kappa D\). Der Gesamtmaßstab \(\kappa=2\pi/L\) wird damit noch nicht bestimmt.

Der Beweis wurde unabhängig geprüft. Er verwendet wesentlich die periodische skalare Nullmode. Er darf nicht unverändert auf antiperiodische Spinorfelder, matrixwertige Diracoperatoren oder allgemeine nichtlokale Operatoren übertragen werden. Das später gesondert untersuchte Spektrum eines **gewählten** antiperiodischen \(qD\) ist davon zu unterscheiden.

Die Fourierklasse ist mit bekannter Steklov-Starrheit verbunden. Jollivet–Sharafutdinov beschreiben in Theorem 1.2 genau die ersten Harmonischen als Nullklasse der Steklov-Zetainvarianten. Die hier ausgeschriebene Operatorrechnung prüft den konkreten Zeitvertrag; sie ist kein Neuheitsanspruch auf diese mathematische Klasse. [Primärquelle](https://arxiv.org/pdf/1611.05919).

## 2. Zwei Gegenproben, unterschiedliche Bedeutung

Für die additive Probe \(L_\epsilon=|D|+\epsilon\cos4\theta\) gilt \(L_\epsilon1\ne0\). Die Kompression auf \(1\) und die normierte vierte Kosinusmode ist
\[
\begin{pmatrix}0&\epsilon/\sqrt2\\\epsilon/\sqrt2&4\end{pmatrix}.
\]
Sie hat den negativen Eigenwert \(2-\sqrt{4+\epsilon^2/2}\). Bei \(\epsilon=0.3\) ist er etwa \(-0.0112185361\). Damit ist dieser additive Operator kein positiver masseloser skalarer DtN.

Die neue **multiplikative** Probe ist dagegen geometrisch zulässig:
\[
q=1+0.3\cos4\theta>0,\qquad\Lambda_\rho=q|D|.
\]
Eine glatte konforme Diskmetrik mit dieser Randdichte kann durch glatte Fortsetzung des logarithmischen Randfaktors in das Innere realisiert werden. Der Operator ist auf \(H_\rho\) positiv, annihiliert die Konstante und respektiert die Vierteldrehung. Dennoch ist
\[
A_{1,-3}=6q_4=6(0.15)=0.9.
\]
Er scheidet für den zusätzlichen lokalen Zeitvertrag aus. Er widerlegt nicht die Weylinvarianz bei festgehaltener Randmetrik, denn seine Randmetrik ist geändert.

## 3. Abgleich mit dem ursprünglichen Transfer: ein bedingter Ausschluss

Die Originale `verification/v221_seam_qecc.py` und `verification/v814_k5_sixstep_transport.py` enthalten auf dem dreidimensionalen Cusp-Gewichtsraum
\[
B=\frac1{18}\begin{pmatrix}13&1&4\\1&13&4\\4&4&10\end{pmatrix},
\quad T=B^6,
\quad\operatorname{spec}T=\{1,64/729,1/729\}.
\]
Dies ist ein Recovery-/Vergessenskanal. **Weder die Anlage noch diese beiden Originale behaupten bereits, dass T die physische Feldzeit ist.** Der folgende Test prüft eine mögliche zusätzliche direkte Anschlussbedingung.

Für jeden glatten positiven Faktor \(q\) macht der Bogenkoordinatenwechsel
\[
s(\theta)=\int_0^\theta q(t)^{-1}dt,
\quad L=s(2\pi),\quad qD=-i\partial_s
\]
den Kreisoperator unitär zu einem konstanten Ableitungsoperator. Periodische Energien sind \(\kappa|n|\); für den separat gewählten antiperiodischen Operator sind sie \(\kappa|n+1/2|\), mit \(\kappa=2\pi/L\). Positive Energien und ihre gewöhnlichen freien Fock-Summen haben rationale Verhältnisse. Zusätzliche sektorabhängige Verschiebungen oder Geschwindigkeiten gehören nicht zu dieser Klasse.

Eine gemeinsame Isometrie \(J\) und Schrittweite \(\tau>0\) mit
\[
e^{-\tau|h|}J=JT
\]
würden daher rationale Gitterexponenten für beide Abklingfaktoren erzwingen. Nach Beseitigung der Nenner müsste für positive ganze \(m,n\)
\[
(2/3)^{6m}=(1/3)^{6n}
\]
gelten. Die Zweierbewertung ist links \(6m\), rechts null: unmöglich. Äquivalent ist \(\log3/\log(3/2)\) irrational. Für den gewählten NS-Einteilchenraum fehlt zusätzlich eine Nullmode für den stationären Eigenwert; bereits die beiden positiven Raten reichen aber zum Ausschluss.

**Zwei Zeitpunkte genügen.** Für einen positiven selbstadjungierten Transfer \(S\), eine Isometrie \(J\) und \(P=JJ^*\) erzwingen bereits
\[
J^*SJ=T,\qquad J^*S^2J=T^2
\]
den direkten Intertwiner. Denn
\[
0=J^*S^2J-(J^*SJ)^2
=((I-P)SJ)^*((I-P)SJ).
\]
Daraus folgt \(SJ=JT\). Ein einziger passender komprimierter Zeitschritt würde diese Schlussfolgerung nicht erlauben.

**Reichweite.** Ausgeschlossen ist die direkte Realisierung beider ursprünglicher Recovery-Moden in einer einzigen solchen Kreiszeit mit gemeinsamer Schrittweite, auch wenn statt des Intertwiners nur beide exakten Zeitmomente gefordert werden. Nicht ausgeschlossen sind ein anderer tatsächlich hergeleiteter physischer Transfer, eine abgeleitete Beziehung zwischen Recovery und Feldzeit, nichtlokale oder wechselwirkende Dynamik oder begründete zusätzliche Sektoren. Die Anlage bleibt als bedingte Konstruktion richtig. Dies ist kein allgemeiner TFPT-Gegenbeweis und keine Begründung, passende zusätzliche Frequenzen frei einzubauen.

## 4. Die Windungsfrage am Original, einschließlich des positiven Kandidaten

### 4.1 Drei typverschiedene Objekte

Die Originale enthalten:

1. Die P1-Seamklasse \([u_\Sigma]=1\in K^1(S^1)\), beschrieben durch relativen Spektralfluss. Beleg: `_archive/paper-latex/tfpt-42.tex`, Zeilen 2319–2355.
2. Die P2-Hypercharge-Schleife \(g_Y(u)=\operatorname{diag}(u^{-2}I_3,u^3I_2)\). Sie hat \(\det g_Y=1\), also Determinantenwindung null.
3. Die später behauptete interne Clutching-Klasse \(c_1(\det E_2)=1\), \(c_1(\det E_3)=0\) über der kompaktierten Normalfläche. Beleg: `tfpt-42.tex`, Zeilen 3900–3979.

Die Quellfassung führt Spektralfluss und Determinantengrad ausdrücklich als getrennte Defektkoordinaten: `_archive/tfpt-45/source_extracts/01_boundary_kernel_source.tex`, Zeilen 543–559. Damit ist die Gleichsetzung von 1 und 3 eine zu beweisende Quellenabbildung; Objekt 2 kann sie wegen seines Grades null nicht einfach ersetzen.

### 4.2 Exakter interner Spin-Lift

Für einen diagonalen \(U(5)\)-Loop mit ganzzahligen Gewichten \(w_i\) und \(d=\sum_iw_i\) ist der lokale Halbspin-Lift
\[
S^+=\det(E)^{-1/2}\Lambda^{\rm even}E.
\]
Seine 16 Gewichte sind \(\sum_{i\in I}w_i-d/2\) für gerade \(|I|\). Nach einem Vollumlauf liefert jeder Zustand das Vorzeichen \((-1)^d\).

Für die Hypercharge-Gewichte \((-2,-2,-2,3,3)\) ist \(d=0\), also das Vorzeichen **+1**. Für einen hypothetischen blockskalaren Loop mit \(3a+2b=1\) gilt dagegen \((a,b)=(1+2k,-1-3k)\). Seine Ganzzahlfreiheit liegt in der spurfreien Hypercharge-Richtung. Ein solches Urbild ist noch nicht durch die P1-Quelle ausgewählt.

### 4.3 Was die Determinantenklasse bereits konstruktiv liefert

Hier ist eine Präzisierung gegenüber dem ersten Audit wichtig: Auf \(S^2\) bestimmt der Rang zusammen mit \(c_1\) das komplexe Bündel bis Isomorphie. Für \(r\ge2\) induziert \(\det:U(r)\to U(1)\) einen Isomorphismus auf \(\pi_1\): Das folgt aus der Faserung mit einfach zusammenhängender Faser \(SU(r)\). Die Clutching-Klassifikation auf der Kugel genügt daher.

**Wenn** die originale Behauptung \((c_1(E_3),c_1(E_2))=(0,1)\) gilt, ist bereits
\[
E\cong\underline{\mathbb C}^{3}\oplus
(L\oplus\underline{\mathbb C}),\qquad c_1(L)=1
\]
festgelegt. Ein Repräsentant ist \(g_E=\operatorname{diag}(1,1,1,u,1)\). Seine konkrete Diagonalform ist eine Darstellungswahl, keine zusätzliche physische Auswahlpflicht. Fehlende explizite Matrixeinträge sind somit **keine eigene topologische Lücke**.

Es fehlt aber weiterhin der Beweis, dass diese Klasse das tatsächlich induzierte materielle Bild von \([u_\Sigma]\) ist, mit der vorgeschriebenen Blockmarkierung, Feldwirkung und Dynamik. Gleiche ganze Klassenzahlen ersetzen keine solche Abbildung. Eine abstrakte Bott-/Clutching-Zuordnung darf mathematisch konstruiert werden; ihr Einsatz als physischer Quellfunktor bleibt zu begründen.

### 4.4 Spin und Spin-c dürfen hier nicht vertauscht werden

Für das reelle Bündel eines komplexen Bündels gilt \(w_2(E_\mathbb R)=c_1(E)\bmod2\). Beim Kandidaten mit Grad eins ist dies ungleich null. Anschaulich erzeugt der obige Repräsentant eine volle Rotation in genau einer reellen Zweiebene: Sein Spin-Lift endet bei \(-1\), schließt also nicht als Spin-Loop. Ein globaler reiner interner \(\mathrm{Spin}(10)\)-Lift über dieser Kugel existiert nicht.

Die komplexe Struktur liefert dagegen einen kanonischen \(\mathrm{Spin}^c\)-Modul, in der hier verwendeten Polarisationskonvention \(\Lambda^*E\). Der gerade Teil ist ein globales Bündel vom Rang 16. Für den obigen Repräsentanten ist seine Übergangsmatrix \(\Lambda^{\rm even}g_E\) periodisch; sie ist nicht der offene lokale Lift \(\det(g_E)^{-1/2}\Lambda^{\rm even}g_E\). Der extra \(U(1)\)-Faktor in Spin-c kompensiert gerade das Vorzeichen.

Das liefert eine konkrete mögliche globale Trägerstruktur, ohne die CAR-Statistik oder eine räumliche NS-Randbedingung herzuleiten. Die algebraischen Hyperladungen bleiben dabei unverändert: In Ganzzahleinheiten sind ihre Multiplizitäten \(0:1,-4:3,1:6,6:1,2:3,-3:2\). Eine zusätzliche Kopplung an ein räumliches Spin-/Ladungsbündel muss mit ihren Übergängen ausgewiesen werden; der interne Vorzeichenbefund allein bestimmt sie nicht.

## 5. Was an Polarisation, CAR und Windung bestätigt ist

Auf dem Kreis mit abgespaltener Nullmode vertauscht die komplexe Konjugation \(K\) die chiralen Projektoren \(P_\pm\). Für jeden beschränkten \(K\)-reellen Operator \(C\) sind die Abstände zu beiden Projektoren gleich. Da \(\|P_--P_+\|=1\), ergibt die Dreiecksungleichung
\[
\|C-P_-\|\ge\tfrac12.
\]
Die Schranke ist mit \(C=I/2\) scharf. Insbesondere kann ein reeller Funktionalkalkül eines reellen skalaren Operators keine chirale Polarisation auf festen Moden erzeugen. Die Einbeziehung der Orientierung verlässt diese Klasse und wird durch das Argument nicht ausgeschlossen.

Der im Anhang gewählte komplexe CAR-Kreisprozess mit \(C=P_-+\nu P_0\), \(h=\kappa D\), ist konsistent. Reine komplexe quasifreie Zustände haben \(\nu=0\) oder \(1\). Für die leere Nullmode und den bilateralen Shift \(Ue_n=e_{n+1}\) gilt
\[
UCU^*-C=P_0,\quad \operatorname{Tr}(UCU^*-C)=1,
\quad RUR^*=iU,\quad[h,U]=\kappa U.
\]
Im endlichen zyklischen Regulator \(-N,\ldots,N\) ist die Differenz dagegen \(P_0-P_{-N}\) und hat Spur null. Ein netter Ladungswechsel des unendlichen Sees darf nicht als endliche Spuridentität ausgegeben werden. Für Majorana-/selbstduale CAR braucht man zusätzlich die passende Konjugation; der komplexe Multiplikator \(U\) kommutiert nicht mit der gewöhnlichen komplexen Konjugation.

**Die Statistik bleibt eine Herkunftsfrage.** Aus einem bloßen positiven Einteilchenkern mit positiver Zeit erhält man sowohl symmetrische als auch antisymmetrische Fock-Fortsetzungen. Beide stimmen auf dem Einteilchenraum, seiner Gruppenwirkung und seinem Transfer überein; die Produkte unterscheiden sich. Damit ist die Statistik aus genau diesen reduzierten Daten nicht bestimmt. Dies ist keine Aussage, dass eine vollständig spezifizierte ursprüngliche Algebra mit allen P1/P2-Bedingungen niemals CAR auswählen könnte.

Die Originale passen zu dieser Grenze: `tfpt-42.tex`, Zeilen 7624–7673, nehmen einen fermionischen CAR-Kern an; Zeilen 13993–14047 setzen gradierte Symmetrie bei der Rekonstruktion voraus. `tfpt_1_architecture_e8.tex`, Zeilen 1615–1636, führt den freien Majorana-Netzanschluss als bedingten Gate-A-Pfad. Die Lean-Schnittstelle `SeamWindingInterface.lean`, Zeilen 5–44 und 56–86, erhält bereits Ladungsdaten und beweist nicht ihre Gewinnung aus der P1-Windung.

## 6. Identischer skalarer Randkern, verschiedener Quantenfaktor

Für die glatte Diskmetrikänderung \(g'=e^{2\sigma}g\) mit
\[
\sigma(r)=\epsilon(1-r^2)^2
\]
verschwinden \(\sigma\) und \(\partial_n\sigma\) am Rand. Der vollständige masselose skalare DtN bleibt deshalb unverändert. Die innere Dirichletdeterminante verändert sich dennoch. Direkt ist
\[
\int_D|\nabla\sigma|^2,dA
=2\pi\epsilon^2\int_0^1 16r^3(1-r^2)^2,dr
=\frac{4\pi}{3}\epsilon^2.
\]
Die Polyakov–Alvarez-Formel reduziert sich beim flachen Ausgangsdisk und diesen Randwerten auf
\[
\Delta\log\det_\zeta\Delta_D
=-\frac1{12\pi}\int_D|\nabla\sigma|^2dA
=-\frac{\epsilon^2}{9}.
\]
Für den realen gaußschen Skalar ist daher \(\Delta\log Z=\epsilon^2/18\). Der normierte Randquotient \(Z[f]/Z[0]\) ist identisch, der absolute Faktor nicht. Die verwendete glatte Dirichletformel ist der Spezialfall ohne Kegelterme von Theorem 1.4 bei Aldana–Kirsten–Rowlett. [Primärquelle](https://arxiv.org/pdf/2010.02776).

Diese Rechnung bestätigt den Anhang. Sie entscheidet weder die gesamte TFPT-Maßwahl noch mögliche Aufhebungen durch weitere Sektoren und beweist keine quantisierte Gravitation. Eine Lösung der skalaren Randrekonstruktion allein entfernt die Frage der vollständigen Quantenwirkung nicht.

## 7. Verifikation und Herkunft

Der eingereichte Text enthält als Literatur- und Dateilinks nur nicht auflösbare `:chatgpt-content-reference`-Platzhalter. Das dort erwähnte Paket und seine 256 Vierpunktkontrollen wurden daher nicht als vorhandene Prüfer übernommen. Die hier dokumentierten Formeln wurden unabhängig kontrolliert; allgemeine Aussagen stehen in den obigen Beweisen.

Der beigefügte `checker.py` prüft mit rationaler Arithmetik die Fourierzeugen, beide Kosinusproben, den Determinantenintegralwert, das ursprüngliche \(B^6\), interne Spin-/Außenalgebra-Gewichte und die endliche Windungsgegenladung. Er ist ein Reproduktionsprüfer für diese konkreten Rechnungen. Endliche Fenster beweisen weder den allmodigen Satz noch einen Kontinuumsgrenzwert; beides wird hier nicht verwechselt. Er prüft außerdem Hashes der verwendeten Originale und des Anhangs. Normaler Lauf und `-OO` müssen identische Ergebnisse liefern.

Der unabhängige Review bestätigt den lokalen Klassifikationssatz einschließlich seiner Domänen und verlangt ausdrücklich die hier enthaltene Begrenzung des Recovery-Zeittests. Die Quelleninventur umfasste neun gezielt ausgewählte Text-/Lean-Originale; für den Zeittest wurden zusätzlich v221 und v814 geprüft. Keine vollständige neue Prüfung aller TFPT-Claims wurde durchgeführt.

## 8. Was als Nächstes tatsächlich schließen muss

Die drei vom Nutzer verlangten Schritte bleiben der Maßstab:

1. **Quelle zu Feldern:** Aus dem originalen Nahtdatum muss eine markierte Abbildung auf das interne Bündel und die tatsächliche geladene Feldalgebra folgen. Der topologische Kandidat \(\mathbb C^3\oplus(L\oplus\mathbb C)\) ist jetzt explizit; die physische Assoziation, Spin-/Spin-c-Kopplung und Statistik müssen am ursprünglichen Kern nachgewiesen werden.
2. **Gemeinsame Zeitkorrelatoren:** Der physische Transfer muss auf diesem selben Feldraum wirken. Der bekannte Recovery-Kanal darf wegen seiner anderen Rolle nicht einfach als eine Kreiszeit eingesetzt werden. Soll er mit der Feldzeit verbunden werden, braucht es eine abgeleitete Abbildung mit konkreten gemeinsamen Zeitantworten.
3. **Rückverbindung des Randkandidaten:** Erst die daraus gewonnenen Operatoren können ohne Zielblöcke hinsichtlich Ladungen, Produkten, Gram-Matrix und Zeitantwort mit dem bestehenden Kandidaten verglichen werden. Die Energien 3,4,5 bleiben dessen Test, keine allgemeine Vorgabe.

Der sinnvollste nächste Herkunftsschritt ist damit der Nachweis, dass das bereits postulierte beziehungsweise bedingt rekonstruierte P1-Nahtsystem wirklich den markierten Spin-c-/CAR-Träger mit einer eigenen Zeit liefert. Eine weitere freie Kreisquelle mit passend gewählten Geschwindigkeiten würde genau diese offene Identifikation umgehen. Die aktuelle Arbeit liefert einen bestätigten Auswahlvertrag und konkrete Ausschlüsse falscher Identifikationen; **sie schließt weder die Quellenfrage noch T1–T8 vollständig**.

Firewall: ausschließlich Forschungscontract unter `experiments/`; keine Promotion in Ledger, Paper oder empirische Scorecard, keine Veröffentlichung.
