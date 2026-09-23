# Die Quellzeit: vollständiger Logarithmus-Ausschluss und markierte Fortsetzung

22. September 2026 · **UR.SOURCE.CONTINUOUS_MARKED_TIME.01 · PARTIAL**

## Auftrag und Entscheidung

Gesucht bleibt die gemeinsame physische TFPT-Herleitung. Die neuen Anhänge
liefern eine endliche graduierte Quellenklasse, aber noch keine ausgewählten
geladenen Materiefelder. Der bereits bewiesene Spin(10)-Zentraltest verhindert,
dass beliebig komplizierte Operatorwörter in demselben 32er-Raum diese Lücke
schließen. Auch das ältere ungerade 64er-Randfeld, seine W-Produkte und sein
CAR/CCR-Fehler sind bekannt. Diese Konstruktionen werden hier nicht wiederholt.

Die konkrete Frage dieser Fortsetzung betrifft eine **zusätzliche mögliche
Identifikation**: Kann der markierte diskrete Quellenkanal gleichzeitig der
stetige, zeitunabhängige Quanten-Markovprozess auf derselben Algebra sein?
Der Originalbestand enthält eine klassische Recovery-Halbgruppe für B und T.
Ihre Übertragung auf die neue M4-Karte ist kein automatischer Schritt.

Erfolgskriterium: vollständige Entscheidung dieser Identifikation, anschließend
Bestimmung der tatsächlich zulässigen Fortsetzungen derselben markierten
Auslesedaten in einer expliziten Klasse vorhandener Quelloperatoren.
Abbruchkriterium: weder einen gewünschten RR-Block noch zusätzliche Materiefelder,
Geometrien oder Umgebungen zur Reparatur einsetzen; eine gewählte Optimierungs-
Zielfunktion nicht als physisches Auswahlgesetz ausgeben.

**Ergebnis:** Kein Logarithmuszweig der Karte oder einer positiven ganzzahligen
Potenz ist ein GKSL-Generator auf demselben M4. Dies gilt ohne vorausgesetzte
Kovarianz der Zwischenzeiten. Zugleich ist der ursprüngliche B-Transfer selbst
mit kontinuierlichen Quantenprozessen vereinbar. In der Klasse der fünf
bereits vorhandenen Clifford-Sprungoperatoren wird der ganze zulässige
Ratenbereich exakt bestimmt. Eine zusätzliche, klar bezeichnete Forderung
an den vollständigen markierten M2-Unterprozess wählt dort eine einfache
kontinuierliche Fortsetzung aus.

**Das schließt weder den GNS-Hamiltonoperator noch TFPT aus.** Positiver
Hilberttransfer, reduzierte Quantenoperation und unitäre Feldzeit sind
verschiedene Objekte. Diese Fortsetzung entscheidet die Markov-Identifikation;
sie konstruiert keine geladenen Spin(10)-Felder und keine vollständige Theorie.

## 1. Gepinnte Quelle, nicht neue Pauli-Koordinaten

Die fünf hermiteschen Matrizen Γj werden aus den originalen q*=0-Wörtern
des Compilers rekonstruiert. Es gilt {Γi,Γj}=2δij I. Die vorhandene Karte ist

\[
\Phi(X)=\frac7{12}X+\frac1{12}\sum_{j=1}^5\Gamma_jX\Gamma_j.
\]

Auf dem reellen Raum hermitescher Matrizen zerfällt sie in die drei
orthogonalen Eigenräume 1+5+10 mit Eigenwerten 1,1/3,2/3. Schreibe
a=log 3 und b=log(3/2). Alle Logarithmen verwenden eine dimensionslose
Transfer-Schritteinheit; eine physische Zeiteinheit wird nicht festgelegt.

Die ursprünglichen markierten Wörter sind A=i P_A_BIT und F=P_FSIG.
Sie sind hermitesche antikommutierende Einheiten. Ohne Änderung der Quelle
kann man die fünf Vektoren so ordnen und ihre Basisphasen so wählen, dass

\[
F=\Gamma_1,\qquad G=iAF=\Gamma_2,\qquad A=i\Gamma_1\Gamma_2.
\]

Der Checker leitet diese Identitäten aus den tatsächlichen ursprünglichen
Wortmatrizen ab. Es handelt sich nicht um eine frei gewählte neue Feldbank.

## 2. Warum auch andere Logarithmuszweige nicht helfen

Angenommen, ein endlicher zeitunabhängiger GKSL-Generator L auf M4 erfülle
exp L=Φ^n für n>0. Für ganzzahlige n ist die Endkarte CP. Der Beweis gilt
auch für andere positive n, sofern überhaupt eine CP-Endkarte vorliegt.

1. L kommutiert mit exp L=Φ^n. Wegen der drei verschiedenen Eigenwerte
   erhält L die drei Eigenräume V0,V5,V10. Als hermitizitätserhaltende
   Abbildung ist L auf deren hermiteschen Basen reell.
2. In einem d-dimensionalen Block gilt exp Lr=λ^n I. Daher
   exp(tr_R Lr)=det(exp Lr)=λ^(nd). Die reelle Exponentialfunktion ist
   injektiv; somit tr_R Lr=nd log λ. Dies erfasst sämtliche reellen
   Rotationsblöcke und Logarithmuszweige, ohne einen Zweig abzuschneiden.
3. Mittelt man L über die Clifford-Konjugationen und die markierten
   Permutationen der fünf Γj, bleibt ein GKSL-Generator erhalten. Die
   GKSL-Klasse ist unter unitärer Konjugation und konvexer Mittelung stabil.
   Pauli-Konjugationen diagonalieren jede Superoperatormatrix in der
   Wortbasis. Die anschließenden Permutationen haben genau die Orbits
   1,5,10 und ersetzen jeden Diagonalblock durch seinen mittleren Spurwert.
4. Wegen Schritt 2 ist dieser gemittelte Generator genau
   Lbar=n log_principal Φ. Es wird **nicht** die im Allgemeinen falsche
   Gleichung exp(average L)=average(exp L) benutzt. Die Gleichheit folgt
   aus den Blockspuren und der tatsächlichen endlichen Gruppenwirkung.

Die finite Twirl-Aussage wird an sämtlichen 16 ursprünglichen Wortmatrizen
geprüft: die 16 Vorzeichencharaktere sind orthogonal; vier benachbarte
Clifford-Transpositionen verbinden genau die 5er- und 10er-Orbits. Alternativ
liefert die Spin(5)-Mittelung dasselbe Ergebnis durch Schurs Lemma.

Für einen solchen isotropen Generator ist die kanonische Form

\[
\overline L=\alpha\sum_j(\operatorname{Ad}\Gamma_j-\mathrm{id})+
\beta\sum_{j<k}(\operatorname{Ad}(i\Gamma_j\Gamma_k)-\mathrm{id}).
\]

Die traceless Hermitesche Wortbasis ist vollständig und orthogonal. Die
beiden kanonischen Kossakowski-Blöcke verlangen α,β≥0. Ihre Eigenwerte auf
V5,V10 sind −8(α+β) und −4α−12β. Die festgelegten Blockspuren erzwingen

\[
\alpha=\frac{n(3a-2b)}{16},\qquad
\boxed{\beta=\frac{n(2b-a)}{16}=\frac n{16}\log\frac34<0.}
\]

Äquivalent ist β der zehnfach entartete negative Choi-Tangentenwert auf
dem zur Identität orthogonalen Unterraum. Also kann Lbar kein GKSL-Generator
sein. Dies widerspricht Schritt 3 und beweist:

\[
\boxed{\Phi^n\text{ besitzt keinen zeitunabhängigen GKSL-Logarithmus auf }M_4
\text{ für jedes positive ganzzahlige }n.}
\]

Insbesondere hilft weder das Zusammenfassen von sechs Schritten noch eine
andere Logarithmusphase. Der alte Ausschluss betraf nur orbit-skalare
Zwischenzeiten; diese Einschränkung ist jetzt entfernt. Der Beweis ist
eine vollständige Strukturaussage, keine Suche bis zu einer endlichen
Logarithmus-Verzweigungszahl.

Falls eine graduierte Cl5-Fortsetzung zu allen Zwischenzeiten die gerade
M4-Unteralgebra invariant lässt und dort bei Zeit n dieselbe Φ^n liefert,
gilt derselbe Ausschluss durch Einschränkung. Insbesondere liefert ein
paritätserhaltender CP-Halbgruppenlift auf dieser Cl5-Algebra keine Reparatur.
Ein größerer Prozess, der zwischenzeitlich diese Algebra verlässt, ist damit
nicht beurteilt.

## 3. Unabhängiger Ein-Schritt-Beweis über die Kraus-Produkte

Dies ist ein zusätzlicher Beweis für Φ, nicht der Beweis für alle Potenzen.
Für eine endliche zeitunabhängige CP-Halbgruppe in Schrödingerform schreibe

\[
L_*(\rho)=D\rho+\rho D^\dagger+\sum_\mu V_\mu\rho V_\mu^\dagger.
\]

Die Dyson-/Quanten-Sprungentwicklung bei t>0 hat als minimalen linearen
Kraus-Träger Kt den Raum exp(tD) A. Hier ist A die unital-assoziative Algebra,
die alle exp(−sD)Vμ exp(sD) erzeugen. Um die vollständige Algebra und nicht
nur zeitgeordnete Produkte zu erhalten, betrachtet man für jede endliche
Label-Folge die gesamte analytische Funktion ihrer Zeitvariablen: Ein
lineares Funktional, das sie auf dem offenen geordneten Simplex annihiliert,
annihiliert sie identisch. Deshalb haben geordnete und beliebige endliche
Produkte denselben linearen Span. Positivität der Dyson-Beiträge verhindert
eine Auslöschung dieser Kraus-Richtungen in der Choi-Summe.

Wenn I∈Kt, dann exp(−tD)∈A. Jede unital-endliche Matrixalgebra enthält
das Inverse jedes ihrer invertierbaren Elemente, durch Cayley–Hamilton.
Also exp(tD)∈A und Kt=A. **Ein Kraus-Träger, der I enthält, muss in dieser
Situation somit eine Algebra sein.**

Für Φ ist K=span{I,Γ1,…,Γ5}, Dimension sechs. Γ1Γ2 steht senkrecht auf K;
bereits die Zweierprodukte spannen ganz M4, Dimension 16. K ist keine
Algebra. Das beweist den Ein-Schritt-Ausschluss erneut ohne Symmetrieannahme.
Für Φ² ist der Kraus-Träger bereits M4; deshalb würde dieser zweite Beweis
allein das Zusammenfassen von Schritten nicht ausschließen. Dafür wird
ausdrücklich der Twirl-Beweis aus Abschnitt 2 verwendet.

## 4. Was ausdrücklich gültig bleibt

Auf dem GNS-/Hilbert-Schmidt-Raum ist H_GNS=−log Φ positiv selbstadjungiert,
mit Spektrum 0,a,b. exp(−t H_GNS) ist ein gültiger positiver **Hilberttransfer**.
exp(it H_GNS) ist dort unitär. Der zugehörige linksmultiplikative
Operatorprozess aus dem Anhang wird durch Abschnitt 2 nicht widerlegt.

Ebenso ist log B auf dem originalen klassischen Dreizustandsraum ein
Markovgenerator. Seine Offdiagonalen sind a/3 sowie b/2−a/6. Letztere sind
positiv, weil 3b−a=log(9/8)>0. Das originale T=B^6 behält seine
klassische Recovery-Halbgruppe und seine Lücke 6b. Die ursprüngliche
DYN.SEMIGROUP.01-Aussage über diesen klassischen Block wird nicht als
M4-Aussage umgedeutet oder verworfen.

Nicht ausgeschlossen sind ein zeitabhängiger GKSL-Prozess, eine begründete
größere Systemdynamik oder eine physisch anders gewählte Zeitinterpretation.
Insbesondere folgt kein Beweis diskreter physischer Zeit. Die allgemeine
Unterscheidung und das Logarithmus-Einbettungsproblem sind Gegenstand von
[Wolf et al., Assessing non-Markovian dynamics](https://arxiv.org/abs/0711.3172)
und [Wolf–Cirac, Dividing Quantum Channels](https://arxiv.org/abs/math-ph/0611057).
Der konkrete Allzweig-Beweis oben wird selbst gegeben; er wird nicht diesen
Quellen als dortiger TFPT-Satz zugeschrieben.

## 5. Exakte Suche mit denselben fünf Quelloperatoren

Um den Widerspruch richtig zu lokalisieren, wird anschließend nur eine
begrenzte Frage gelöst: Welche kontinuierlichen Recovery-Generatoren aus
den fünf vorhandenen Γj erhalten den originalen markierten B-Ausleseprozess?
Die **zusätzlich erklärte Suchklasse** ist

\[
L_\lambda=\sum_{j=1}^5\lambda_j(\operatorname{Ad}\Gamma_j-\mathrm{id}),
\qquad\lambda_j\ge0.
\]

Sie enthält weder neue Operatoren noch ein angehängtes System. Sie ist
gleichwohl eine gewählte Klasse, nicht aus P1/P2 als vollständige Menge
aller physischen Generatoren hergeleitet. Insbesondere muss exp Lλ nicht
auf ganz M4 gleich Φ sein; dies wäre nach Abschnitt 2 unmöglich.

Für die originalen Ausleseoperatoren A,F ergeben sich genau zwei Bedingungen:

\[
\lambda_1+\lambda_2=b/2,\qquad
\lambda_2+\lambda_3+\lambda_4+\lambda_5=a/2.
\]

Der zulässige Bereich ist ein dreidimensionales beschränktes Polytope.
Seine **sechs** Ecken werden vollständig durch Aufzählung aller möglichen
Zweiersupports des linearen Systems berechnet. Es gibt keine numerische
Optimierungstoleranz und keinen zufälligen Startwert. Die parametrische Form ist

\[
\lambda_2=t\in[0,b/2],\quad\lambda_1=b/2-t,\quad
\lambda_3+\lambda_4+\lambda_5=a/2-t.
\]

Fordert man zusätzlich Rotationskovarianz auf dem dreidimensionalen
Komplement der markierten Γ1/Γ2-Ebene, werden λ3=λ4=λ5. Es bleibt genau
die gesamte Familie

\[
\lambda(t)=\left(b/2-t,\ t,\ (a/2-t)/3,\ (a/2-t)/3,\ (a/2-t)/3\right).
\]

Schon diese ganze Familie hat dieselbe ursprüngliche B-Auslesung für alle
Zeiten und denselben stationären Spurzustand; ihre vier oder fünf positiven
unabhängigen Clifford-Sprünge erzeugen M4. B allein wählt t also nicht aus.
Das ist eine exakte Nicht-Eindeutigkeit innerhalb einer konkreten Klasse,
kein behauptetes Gegenmodell gegen sämtliche TFPT-Prinzipien.

## 6. Die zusätzliche Produktantwort bestimmt den verbleibenden Parameter

Der vorhandene GNS-Anhang legt mehr fest als B: Er bestimmt auch die
Transferantwort von G=iAF. Der produktgeschlossene markierte Unterraum ist

\[
\mathcal S=\operatorname{alg}(A,F)=\operatorname{span}\{I,A,F,G\}
\cong M_2\otimes I_2\subset M_4.
\]

In der Familie aus Abschnitt 5 ist Lλ(G)=−(a+b−4t)G. Die vorhandene
markierte GNS-Antwort verlangt hingegen −aG. Sie erzwingt t=b/4.
Ein einfaches Wort, das diese Information liest, ist

\[
C_{FAAF}(u,v,w)=\frac14\operatorname{Tr}
\left[F e^{uL_\lambda}\left(Ae^{vL_\lambda}
\left(Ae^{wL_\lambda}(F)\right)\right)\right]
=e^{-a(u+w)}e^{-(a+b-4t)v}.
\]

Die ursprüngliche positive GNS-Fortsetzung liefert bei u=v=w=1 genau
1/27. Die B-kompatible Familie reicht hier von 2/81 bis 1/18. Das
zusätzliche Vierpunktdatum wählt darin eindeutig 1/27 und t=b/4.

Somit ergibt sich innerhalb der erklärten Suchklasse plus Komplementsymmetrie

\[
\boxed{L_{\mathrm{mark}}=
\frac{\log(3/2)}4\sum_{j=1}^2(\operatorname{Ad}\Gamma_j-\mathrm{id})+
\frac{\log6}{12}\sum_{j=3}^5(\operatorname{Ad}\Gamma_j-\mathrm{id}).}
\]

Beide Raten sind positiv: etwa 0,1013662770 und 0,1493132891.
Alle fünf Sprünge sind hier aktiv. Der gemeinsame Kommutant ist skalar,
also ist I4/4 der einzige stationäre Dichteoperator. Die kleinste positive
Zerfallsrate bleibt b; in sechs Schritt-Einheiten bleibt sie 6b.

Weil S unter Produkten, Adjungieren und beiden Transfers geschlossen ist,
folgt per Induktion die Gleichheit **jedes** verschachtelten Spur-Transferwortes
mit Einfügungen aus S und beliebigen nichtnegativen Zeitintervallen.
Dies ist mehr als ein Zweipunkt-Fit. Es ist keine Gleichheit beliebiger
Instrument-Prozesstensoren oder sämtlicher M4-Wörter: Solche Eingriffe dürfen
S verlassen. Die verwendeten GNS-Wörter werden nicht als unabhängig
gemessene Rohdaten des P1-Nahtkerns ausgegeben.

Außerhalb von S unterscheiden sich die Kanäle konkret:

| Operatorsektor | Dimension | Zerfallsrate von L_mark |
|---|---:|---:|
| I | 1 | 0 |
| Γ1,Γ2 | 2 | a |
| Γ3,Γ4,Γ5 | 3 | 2(a+b)/3 |
| iΓ1Γ2 | 1 | b |
| iΓpΓq, p≤2<q | 6 | (a+b)/3 |
| iΓpΓq, 3≤p<q | 3 | (2a−b)/3 |

Zum Beispiel beträgt die normierte Γ3-Zweipunktantwort nach einer Einheit

\[
\frac14\operatorname{Tr}[\Gamma_3e^{L_{\mathrm{mark}}}(\Gamma_3)]
=(2/9)^{2/3}=0{,}3668808054\ldots
\]

statt 1/3 beim ursprünglichen vollständigen Φ-Kandidaten. Dieser eine
Quellwert entscheidet zwischen diesen beiden Fortsetzungen. L_mark
erhält eine markierte 2+3-Aufspaltung statt der vollen Fünfer-Isotropie.
Diese internen Clifford-Richtungen werden **nicht** mit Farb-, schwachen
oder Raumzeitdimensionen identifiziert. Eine solche physische Gruppenabbildung
müsste separat bewiesen werden.

## 7. Bedeutung für die Gesamtlösung und die Algorithmenwahl

Die Suche liefert zwei entscheidbare Aussagen, aber keine Auswahl der
vollständigen physischen Quelle:

- Wer den ganzen vorgelegten Φ-Kanal beibehält, kann ihm keine
  zeitunabhängige Markoventwicklung auf demselben M4 zuschreiben. Alle
  Logarithmuszweige und alle ganzzahligen Gruppierungen sind erfasst.
- Wer nur B und den vorhandenen markierten M2-GNS-Unterprozess festhält,
  besitzt eine explizite kontinuierliche Fortsetzung mit denselben
  Quelloperatoren. Ihre Klassenannahme und Komplementsymmetrie bleiben
  zusätzlich; ihre weitergehenden Γ3-Antworten sind andere.

Damit wird die Ursache lokalisiert: Die klassische Nahtzeit ist nicht
widersprüchlich. Die zusätzliche vollisotrope Quantenfortsetzung und ihre
Interpretation als derselbe Markovprozess passen nicht zusammen. Der
GNS-Ausweg ist mathematisch gültig, benötigt aber weiterhin seinen
physisch begründeten Feld- und Zeitintertwiner.

Ein genetischer Algorithmus wäre hier weniger aussagekräftig: Die
Logarithmusfrage besitzt einen analytischen Ausschluss für eine unendliche
Klasse. Das Ratenproblem ist exakt linear lösbar. Mit ausschließlich B als
Fitnessdaten lägen unendlich viele Kandidaten mit exakt gleichem Fehler null
vor; eine Optimierung würde nur ein zusätzliches Auswahlkriterium verstecken.
Die neue Vierpunktbedingung zeigt stattdessen, welches Datum den Parameter
t entscheidet. Es wurde deshalb symbolisch gelöst und vollständig enumeriert.

Die weiter offene konkrete Ursprungsaufgabe lautet: Aus dem ursprünglichen
Naht-/Collar-Funktional die gemeinsame nichtkommutative Antwort der markierten
Operatoren und des Komplements gewinnen, einschließlich zulässiger
Einfügungen und physischer Zeit. Erst diese Antwort kann die vollständige
Fortsetzung auswählen. Sie ist in den bisher verwendeten B-Daten nicht
enthalten. Danach bleiben der tatsächlich geladene Sektorwechsel und die
native Materie-/Familienabbildung erforderlich; L_mark liefert sie nicht.

E8-Compiler, bekannte Flavor-Verhältnisse und Kopplungs-Fixpunkte werden
durch diesen Test nicht zurückgenommen. Ebenso bleiben deren offene
gemeinsame physische Realisierung, die vierdimensionale chirale Feldtheorie,
Gravitation und übrigen T1–T8-Verpflichtungen erhalten. **Keine endgültige
TFPT-Lösung und keine Schließung eines physischen Tores.**

## 8. Reproduktion und Prüfgrenzen

`checker.py` verwendet die gepinnten ursprünglichen Wortmatrizen, ihre
Markierungen und die ursprüngliche B-Matrix. Exakte symbolische Identitäten
prüfen Twirl-Orbits, den Choi-Tangentenwert, alle Ecken des Ratenbereichs,
die eindeutige bedingte Fortsetzung, ihren gesamten endlichen Generator und
die markierten Produkte. Dezimalzahlen sind reine Ausgaben exakter
Logarithmen. Der allgemeine Allzweig- und Allwortsatz steht in diesem Text;
eine endliche Testzählung ersetzt seinen Beweis nicht.

Normal- und -OO-Lauf werden byteweise verglichen. Eine unabhängige
mathematische Agentenprüfung ist in `INDEPENDENT_REVIEW.md` dokumentiert.
Das ist weder externe Peer Review noch eine Beweisassistenten-Formalisation.
Forschung ausschließlich unter `experiments/`; kein Paper-/Ledger-/Scorecard-
Status wird aufgewertet.
