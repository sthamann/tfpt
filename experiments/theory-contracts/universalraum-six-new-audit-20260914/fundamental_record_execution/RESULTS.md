# Die Wedge-Kopplung selbst als Aufzeichnung: keine zusätzliche kohärente Q-Primitive

14. September 2026, Fortsetzung nach Forschungsrevision v1.6.

## Ergebnis

**Für den konkret geforderten Präparations-/Mehrzeit-/Endversuch genügt die
Belegung des ursprünglichen Vermittlers als Aufzeichnungsregister.** Ein
zusätzlicher kohärenter Q_occ-Pointer-Schalter und ein getrenntes kohärentes
Pointerbit werden dafür nicht gebraucht. Die zuvor als eigene Primitive
behandelte Aufzeichnung lässt sich auf dem tatsächlich erreichten Träger
durch die vorhandene Wedge-Kopplung selbst realisieren.

Die verbleibende Auslese muss die Vermittlerbelegung farbblind und
nondestruktiv messen. Das ist eine ausdrücklich zusätzliche
Instrumentannahme, keine hier aus P1/P2 bewiesene Messdynamik. Adressierung,
t-an/aus, Pulse, Cliffordvorbereitung und Reset bleiben ebenfalls benannt.

Der neue Ablauf hat dieselben Materiekanäle und klassischen Rohendstatistiken
wie der v1.6-Versuch: 9/64 behalten, 153/2048 aufgezeichnet; Verhältnis 17/32.
Er beansprucht nicht dieselben nachträglich frei kohärent bedienbaren externen
Pointerregister. Diese Unterscheidung ist Teil des Ergebnisses.

## 1. Der passende Träger war schon in der Quelle vorhanden

Sei W:C4⊗C4→Λ²C4 die normierte Wedge-Abbildung,
W|a,b⟩=(|a∧b⟩)/√2 für a<b und mit negativem Vorzeichen für a>b.
Dann gelten exakt

\[
WW^\dagger=I_6,\qquad W^\dagger W=P^-,\qquad P^+=I-P^-.
\]

Die physische Kante besitzt nicht von vornherein ein freies 16×2-Register,
sondern 16 Materiezustände plus sechs Vermittlerzustände:

\[
\mathcal H_{\rm edge}
=\operatorname{Sym}^2(\mathbb C^4)
\oplus\big(\Lambda^2(\mathbb C^4)\otimes\mathbb C^2_{\rm occ}\big),
\qquad \dim=10+6\cdot2=22.
\]

Die sechs antisymmetrischen Materiezustände können in sechs entsprechend
markierte Vermittlerzustände übergehen. Die zehn symmetrischen Zustände
bleiben dunkel. Der Besetzungswechsel speichert daher bereits die
Symmetrieinformation. Das ist keine neue Zuordnung beliebiger Labels:
Es ist die tatsächlich im vorhandenen Vertex verwendete Abbildung W.

## 2. Eine kleine kanonische Involution aus dem Quellenoperator

Die Ein-Kanten-Hamiltonmatrix ist

\[
H=\begin{pmatrix}0&gW^\dagger\\gW&\Delta I_6\end{pmatrix},
\quad N=\begin{pmatrix}0&0\\0&I_6\end{pmatrix},
\quad g=\sqrt2t.
\]

Der reine Wedge-Anteil D=H−ΔN hat Eigenwerte 0,+g,−g. Die Nullrichtung
ist der symmetrische Materieraum. Deshalb ist

\[
\boxed{A=P_{\ker D}+D/g
=\begin{pmatrix}P^+&W^\dagger\\W&0\end{pmatrix}.}
\]

Aus WW†=I und W†W=P− folgt sofort A†=A und A²=I.
Dies ist die kanonische Polar-/Involutionskonstruktion des tatsächlichen
Wedge-Operators; die Definition fügt keine gewünschte Ω-Projektion hinzu.

Für einen anfangs nackten Materiezustand schreibt A dessen symmetrischen
Anteil in „Vermittler leer“ und den antisymmetrischen Anteil in „Vermittler
belegt“. Die Farbinformation bleibt kohärent im Vermittler enthalten.
Unter der natürlichen isometrischen Einbettung in Materie×Record wirkt A
wie R auf dem **erlaubten 22D-Unterraum**. Zehn zusätzliche symmetrische
Zustände mit Pointer 1 des freien 32D-Trägers fehlen physisch; sie werden
nicht als implementiert ausgegeben.

## 3. A ist auch mit positiver Zeit bei festem Δ ausführbar

Die algebraische Definition D=H−ΔN behauptet nicht, dass negative
Driftzeit als physische Primitive verfügbar sei. Stattdessen wird A aus
positiven Vorwärtsintervallen von H_on und H_off=ΔN gebaut.

Bereits freies Parken liefert

\[
e^{-i\pi H_{\rm off}/\Delta}=I_{16}\oplus(-I_6).
\]

Damit brauchen die Z-Besetzungskicks kein Hilfsbit und keinen Q-Schalter.
Auf jedem hellen Zweiraum ist H_on=[[0,g],[g,Δ]]. Setze
ω=√(Δ²+4g²), θ=arctan(2g/Δ), n=(sinθ,0,−cosθ). Der Blochvektor
wird durch On-Pulse um n und durch Off-π-Kicks um die z-Achse gedreht.

Nach k π/ω-Pulsen mit jeweiligen Z-Kicks liegt er bei
(sin(2kθ),0,cos(2kθ)). Für
k=floor(π/(2θ))−1 konstruieren zwei weitere positive On-Winkel den
exakten Übergang zum Südpol. Die geschlossenen Ausdrücke für acos und
atan2 stehen im Prüfer. Sie entstehen aus der Bedingung, dass nach dem
Zwischen-Z der projizierte Achsenanteil demjenigen des Südpols entspricht;
die letzte Rotation verbindet dann zwei Punkte desselben Rotationskreises.

Der so erhaltene Zweiraumpropagator U hat verschwindende Diagonale. Für
a=U21 und b=U12 sind |a|=|b|=1. Ein Off-Intervall vor und eines nach U
mit Zeiten arg(b)/Δ beziehungsweise arg(a)/Δ, jeweils modulo 2π/Δ,
machen beide Transferamplituden genau eins. Somit wird der gewünschte
Operator A einschließlich der beiden relativen Phasen realisiert.

Für t/Δ=1/20 ergeben sich zwölf On-Pulse und dreizehn Off-Intervalle,
insgesamt **25πℏ/Δ** pro A. Die vollständige 22D-Matrix und ihre 352D-
Erweiterung mit den zwei weiteren Materieträgern wurden numerisch aus den
tatsächlichen Propagatoren geprüft, Fehler unter 3·10⁻¹². Die Konstruktion
ist analytisch durch die Block- und Rotationsidentitäten begründet; es
wird kein formaler Intervallbeweis aller transzendenten Pulse behauptet.

### Wichtig: die übrigen Vermittler haben eine echte Minusphase

Auf einem hellen Zweiraum hat A Determinante −1. Daher muss die gesamte
Driftzeit modulo 2π/Δ eine ungerade π-Zeit sein. Nicht adressierte
Vermittler gleicher Energie erhalten deshalb **−1**, nicht +1.

Im vollständigen 544D-Sternträger ist die Operation, nach geeignetem
Sortieren der Basis, A352⊕(−I192). Der Prüfer führt diese Phase mit und
weist den falschen Identitäts-Zuschauer als Negativkontrolle zurück.
Aus nackten Eingängen werden diese fremden Vermittler während eines
isolierten Kantenaufrufs nicht erreicht. Vor jedem Kantenwechsel oder
Cliffordtick wird die aktive Aufzeichnung vollständig zurückgerechnet.
Bei Leakage dürfen die Zuschauer nicht stillschweigend entfernt werden.

## 4. Präparation, Aufzeichnung und Endtest aus derselben Operation

Sei N1=N und N0=I−N. Auf nackten Materieeingängen gilt

\[
A N_1 A=P^-,\qquad A N_0 A=P^+,
\]

wobei auf der rechten Seite die zurückgekehrten Materieblöcke gemeint sind.
Beide Zweige haben am Ende wieder leere Vermittler.

**Start:** ξ herstellen, A03, N1-Ausgang auswählen, A03. Aus der schon
exakt geprüften Identität P−03ξ=−√(3/8)Ω folgt genaue Ω-Präparation
mit Wahrscheinlichkeit 3/8.

**Behaltenes Echo:** C3, zweimal A01 ohne Zwischenmessung, C3 inverse.
Die beiden A heben sich auf.

**Aufgezeichnetes Echo:** C3, A01, farbblinde Belegungsmessung mit beiden
Ausgängen, A01, C3 inverse. Die Materie erfährt exakt
P+ρP++P−ρP−. Das ist derselbe reduzierte Materiekanal wie beim alten
Zwei-frische-Pointer-Versuch. Ein klassisches Ergebnis kann als 00 bzw.
11 gespeichert werden. Beliebige spätere kohärente Eingriffe auf zwei
externe Pointer werden dadurch nicht implementiert.

**Ende:** A03, N1-Ausgang, A03, inverse ξ-Schaltung, acht Nullbits.
Der ausgeführte Effekt ist wieder (3/8)PΩ auf jedem nackten Materieeingang.

Alle 256 Basiszeilen dieses Endtests und die gesamten rationalen
Rohwahrscheinlichkeiten sind geprüft: 9/64 behalten, 153/2048 aufgezeichnet.
Ein kompletter nicht vorzeitig abgebrochener Versuch benötigt sechs A,
also **150πℏ/Δ** Hamiltonzeit statt der bisherigen vier 70π-Records.
Messung, Cliffordgatter, Reset und Steuerung sind darin nicht enthalten.

Wird nach beiden Präp-Ausgängen grundsätzlich zurückgerechnet, sind im
Mittel 16/3 A bis zur Präparation und 28/3 bis zum anschließenden Echo-End-
Versuch nötig. Bei frühem Präp-Abbruch nach N0 kann das zweite A entfallen,
weil der symmetrische Zweig bereits nackte Materie ist: dann 11/3 bzw.
23/3 A. Diese verschiedenen Ablaufverträge werden nicht vermischt.

## 5. Der nun präzise fehlende Informationsteil

Der Detektor darf **nur die Belegung**, nicht die Vermittlerfarbe lernen.
Die eigenen Negativkontrollen zeigen auf demselben Start:

| Tatsächliches Instrument im belegten Sektor | Heraldwahrscheinlichkeit | Bedingte Ω-Fidelity nach Rückkehr |
|---|---:|---:|
| Farbblinde Lüdersmessung | 3/8 | 1 |
| Farbe zusätzlich gemessen und Ergebnis verworfen | 3/8 | 1/6 |
| Vollständig SU(4)-kovariante Depolarisation der Vermittlerfarbe | 3/8 | 1/36 |

Die identische Energie-/Belegungsstatistik beweist also keine richtige
Quantenpräparation. Selbst vollständige Symmetrie und Wiederholbarkeit
der Belegungsmessung wählen den ersten Kanal nicht aus: Depolarisation
innerhalb des belegten sechs-dimensionalen Sektors ist ebenfalls kovariant
und lässt seine Belegung unverändert.

Hier liegt ein konkretes **kleines Informationsprinzip als Kandidat**:

> Außer der ausdrücklich aufgezeichneten Belegung darf keine weitere
> Information an unbeobachtete Freiheitsgrade abgegeben werden.

Als mathematischer Zusatzvertrag bedeutet dies hier ein effizientes
Instrument, also einen Krausoperator pro sichtbarem Ausgang. Zusätzlich
werden eine exakte Belegungs-POVM, Wiederholbarkeit der Belegung und volle
SU(4)-Kovarianz vorausgesetzt. Für die 352D-Ausführung muss die Messung
außerdem kantenlokal sein und auf den beiden übrigen Materieträgern als
Identität wirken; andernfalls reicht der folgende Schur-Schluss nicht.
Unter diesen Voraussetzungen wirkt der belegte Krausoperator
nach Schur auf der irreduziblen 6 nur als Phase mal Identität. Der leere
Zweig des tatsächlichen A-Eingangs liegt vollständig in der irreduziblen
Sym10 und hat dieselbe Eigenschaft. Für genau diese Eingänge entsteht
dadurch der benötigte Paritäts-Lüderskanal.

**Dieser Zusatzvertrag ist nicht aus der ursprünglichen endlichen
Compilergruppe abgeleitet.** Auf beliebigen leeren 16D-Eingängen können
außerdem relative Phasen zwischen Sym10 und Anti6 verbleiben. Der
bedingte Satz ist weder ein universelles Messpostulat aus TFPT noch
eine vollständige T1/T8-Schließung. Er benennt aber erstmals den präzisen
Informationstransfer, der statt einer allgemeinen unbekannten Q-Gate-
Maschine bewiesen oder experimentell geprüft werden müsste.

## 6. Fazit der Herkunftsfrage

Die vorhandene Wedge-Struktur liefert bereits einen natürlichen
**kohärenten Record auf ihrem eigenen Träger**. Eine zusätzliche Kopie
dieser Information in einem separat frei steuerbaren Pointer war für
den verlangten Versuch eine stärkere Anforderung als nötig.

Offen bleiben die quellenseitige Berechtigung der Steuerung, die Auswahl
des effizienten farbblinden Ausleseinstruments, die Anfangs-/Resetressourcen
und der gemeinsame physische Skalierungsursprung. Die Vereinfachung
schließt einen konkreten bedingten Ausführungsschritt; sie behauptet
nicht, dass Primzahlen, RH, Faktorisierung oder die ganze TOE dadurch
bereits hergeleitet wären.

Belege: `mediator_record.py`, `verification.json` und
`verification.optimized.json`. Der Prüfer trennt exakte rationale
Operationsidentitäten von numerischen Propagatorresttests und nennt
sämtliche weiterhin angenommenen Ressourcen.
