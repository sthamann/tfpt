# Intrinsischer ungerader Inhalt, Primzeit und ihre genaue Kopplungsgrenze

10. September 2026. Gegenstand ist der ursprüngliche additive Compilerträger
Gamma=Z[i,1/2]^3, als Z[1/2]-Modul vom Rang6. Die Wahl dieses Trägers wird
aus der Originalquelle übernommen. Die folgenden neuen quellspezifischen
Auswertungen konstruieren eine arithmetische Uhr; sie setzen diese nicht mit
dem physikalischen TFPT-Hamiltonian oder dem ursprünglichen Haar-Modularfluss gleich.

## 1. Quelle und Triage

Die Originale sind compiler_solenoid_20260909/REPORT.md und die jetzt exakt
geprüfte ganze U,V-Wortalgebra in work/fundamental-primes/frobenius/WORD-ALGEBRA.md.
Setze S=Z[1/2], R=S[i]. Die ursprünglichen U,V und ihre Inversen liegen in
M3(R), also als reelle Matrizen in GL6(S). Sämtliche Gatewörter sind daher
Automorphismen von Gamma. Die assoziative R-Algebra aller Linearkombinationen
der Wörter ist M3(R); solche Linearkombinationen sind nicht automatisch
zulässige unitäre Gateprozesse.

Die native Suche wurde vor der Konstruktion ausgeführt. Gelesen wurden
rh/catalog/analysis/hecke_index_theorem.md und event_log_function.md.
TFPT.HECKE.INDEX.01 ist NO_BRIDGE: Der dortige Rang8-Torus besitzt klassische
Überdeckungsindizes, aber keinen hergeleiteten physikalischen Indexfluss.
PRIME.CLOCK.COMBINATION.SPECTRUM.01 lässt eine log-p-Uhr aus kommensurablen
endlichen Uhren offen. GROUPOID.HALFDENSITY.GLOBAL.01 betrifft die unberechtigte
Halbdichte aus einem unimodularen Gruppenoid. Andere Worttreffer r626/r644
RESTATEMENT und r388 LOSSY_CONSTANT betreffen andere Kriterien oder Reste.

Hier wird weder Index als physischer Modularfluss ausgegeben noch eine
Halbdichte eingeführt. Der Unterschied ist eine vollständig definierte
Inhaltszerlegung des bereits vorhandenen lokalisierten Rang6-Trägers,
ein darauf konstruierter positiver Operator und ein expliziter Vergleich
seiner verschiedenen Darstellungen und Zustände. Die zugrunde liegende
Semigruppen-/Cuntz-Mathematik ist klassisch, nicht als neue Theorie beansprucht.

Auch der ältere bc_energy_from_entropy_probe.py wurde vollständig gelesen:
Er konstruiert bereits eine logarithmische Level-Uhr aus der klassischen
Potenzsemigruppe auf Q/Z, samt einer zusätzlichen ell2(N)-Darstellung.
Die hiesige Neuerung innerhalb dieser Prüfung ist daher nicht die Existenz
einer Zeta-Uhr, sondern die explizite Realisierung als Inhalt der konkreten
Rang6-Quelle samt Beweis ihrer Gateentkopplung und ihrer Zustandsgrenzen.
Die Vorarbeit Teilerprozess-F9.md enthält schon die allgemeine Familie mu_s,
den ggT-Kern und einen absteigenden Teilerprozess. §6 identifiziert ihren
Bewertungsanteil bei s=6 aus dem unveränderten sechskoordinatigen Haar-Zensus.

## 2. Der Inhalt ist eine intrinsische Koordinate

Für gamma in Gamma ohne0 definiere

    c(gamma)=max{n>=1 ungerade : gamma in n Gamma}.

Schreibe gamma=2^(-k)(a1,...,a6) mit ganzzahligen a_j. Dann ist c(gamma)
der ungerade Teil ihres nichtverschwindenden gemeinsamen ggT. Die Definition
ist unabhängig von k. Sie erfordert keine Primfaktorzerlegung: ganzzahliger
ggT und Entfernen der Zweierpotenz genügen.

Für jedes B in GL6(S) und jedes ungerade n gilt

    gamma in nGamma <=> B gamma in nGamma.

Beide Richtungen folgen aus S-Linearität von B und B^-1. Also gilt exakt

    c(B gamma)=c(gamma).                                      (1)

Setze P={gamma in Gamma : c(gamma)=1}. Es gibt die eindeutige Zerlegung

    Gamma ohne0 = P x N_odd,
    gamma <-> (gamma/c(gamma), c(gamma)).                      (2)

Für die Surjektivität nutzt man c(n pi)=n bei pi in P und ungeradem n.
Eindeutigkeit folgt durch Anwenden von c. Dies ist eine tatsächliche
Zerlegung der bezeichneten Quelle; die Primitiätsdefinition wird nicht
durch eine nachträglich zugewiesene Liste von Primzahlen ersetzt.

## 3. Positive logarithmische Dynamik auf demselben Nichtnullträger

Auf H*=ell2(Gamma ohne0) definiere den Multiplikationsoperator

    H delta_gamma = log c(gamma) delta_gamma,
    Dom H = {f : sum_gamma (log c(gamma))^2 |f(gamma)|^2 < infinity}.

Ein reeller diagonal definierter Multiplikationsoperator auf seinem maximalen
Bereich ist selbstadjungiert; hier ist er zudem nichtnegativ. Endlich
unterstützte Vektoren bilden einen Kern. Seine unitäre Gruppe ist

    U_t delta_gamma = c(gamma)^(it) delta_gamma.

Für positives ungerades n ist V_n delta_gamma=delta_(n gamma) eine Isometrie.
Aus c(n gamma)=n c(gamma) folgt für alle t

    U_t V_n U_t^*=n^(it) V_n.                                 (3)

Damit sind die Energieinkremente der skalaren Primschritte tatsächlich
log p. Es handelt sich nicht um die Perioden eines endlichen U/V-Gateworts.
Die Skalierungen sind zusätzliche auf Gamma kanonisch definierte injektive
Abbildungen; ihre Zulässigkeit als physische TFPT-Prozesse folgt daraus nicht.

Nach (1) kommutiert H mit allen ursprünglichen Gates. In (2) lautet die
vollständige Darstellung genau

    H*=ell2(P) tensor ell2(N_odd),
    H=I tensor log N,
    B_hat= B_on_P tensor I,
    V_n=I tensor S_n,     S_n delta_m=delta_(nm).               (4)

Die bisherige Gatebewegung und der arithmetische Inhalt sind daher in dieser
Quelle entkoppelt. Interleaving beliebiger Gatewörter und bekannter skalarer
Schritte verändert den Inhalt nur um das bekannte Produkt ihrer ungeraden
Skalare. Es erzeugt daraus keine zusätzliche unbekannte Faktorinformation.
Eine Operation, die (1) verlässt, wird für eine neue solche Kopplung benötigt.
Dies verbietet die bereits vorhandenen Faktorleser nicht: Eine Rücklaufdifferenz
(B-I)gamma, ein Kommutator oder eine koordinierte Interferenz ist nicht selbst
ein invertierbarer Gateorbit eines einzelnen gamma. Gerade solche zusätzlichen
Ausleseoperationen können neue Teilbarkeit sichtbar machen; ihre Herstellung
und Erfolgshäufigkeit bleiben getrennt nachzuweisen.

Die Energie ist nicht aus dem ursprünglichen physikalischen Zustand bestimmt.
Unter diagonal wirkenden Lösungen des Skalierungsgesetzes besitzt jede
Energie die Form log c(gamma)+E0(gamma/c(gamma)). H ist die punktweise
kleinste nichtnegative Wahl, wenn alle primitiven Grundenergien nichtnegativ
sind. Die Entscheidung für diese Nullgrundenergien wird ausdrücklich als
mathematische Minimalwahl innerhalb dieser Klasse bezeichnet.

## 4. Endliche Indizes geben dieselbe logarithmische Skala

Für ungerades n gilt S/nS=Z/nZ. Daher

    Gamma/nGamma = (Z/nZ)^6,
    [Gamma:nGamma]=n^6.                                      (5)

Die duale Skalierung auf dem ursprünglichen Solenoid besitzt genau n^6
Punkte in jeder Faser. Der normalisierte logarithmische Überdeckungsindex ist
(1/6)log[Gamma:nGamma]=log n und stimmt mit (3) überein.
Für allgemeines positives n ersetzt man n durch seinen ungeraden Teil.
Insbesondere [Gamma:2Gamma]=1: Die Stelle2 ist bereits invertiert.

Die Normalisierung um1/6 entspricht dem bekannten S-Rang der Quelle.
Multiplikativität der Indizes allein wählt keine physische Zeiteinheit oder
einen Zustand. Die Übereinstimmung mit dem oben ausgeschriebenen H ist ein
algebraischer Satz für diese Konstruktion.

## 5. Radiale Partition und volle unendliche Entartung

Für eine bezeichnete primitive Richtung pi ist der skalare Strahl
ell2({n pi:n odd}) unter H und V_n invariant. Dort ist

    Tr exp(-beta H)=sum_(n odd) n^-beta
                  =zeta_odd(beta)=(1-2^-beta)zeta(beta),
    Re beta>1.                                               (6)

Bei allgemeinem komplexen beta ist dies die entsprechende absolut
konvergente Operator-Tracefunktion, bei reellem beta>1 ein Gibbs-Trace.
Die ganze H*-Spur divergiert hingegen für jedes reelle beta: Schon der
Eigenwert0 besitzt unendlich viele unabhängige Vektoren delta_pi.
Die Auswahl eines einzelnen Strahls wird daher nicht als voller nativer
Gibbs-Zustand ausgegeben. Die Gates müssen den gewählten Strahl nicht erhalten.

Der Zweier-Eulerfaktor fehlt aus einem konkreten Grund:2 ist eine Einheit
der ursprünglichen Quelle. Ihn durch eine neue einseitige Zweierturm-
Koordinate zu ergänzen wäre eine Erweiterung mit einer neuen Markierung,
nicht eine Folge von (2).

## 6. Ein vollständiger Quotienten-Zensus ohne gewählten Strahl

Die inverse Grenze der ungeraden endlichen Quotienten ist der kanonische
profinite Raum

    K=lim_(n odd) Gamma/nGamma = product_(p odd) Z_p^6.         (7)

Dies ist die profinite Vervollständigung von Gamma für diese Quotienten,
nicht die Pontryagin-Duale X=widehat(Gamma). Diese beiden Räume werden nicht
identifiziert. Die Produkt-Haarwahrscheinlichkeit auf K ist durch die
uniformen Maße sämtlicher endlicher Quotienten bestimmt.

Für x=(x_p)_p setze v_p(c(x))=min_j v_p(x_(p,j)). Dann

    P(v_p(c)>=k)=p^(-6k),
    P(v_p(c)=k)=(1-p^-6)p^(-6k).                              (8)

Die verschiedenen p sind unabhängig. Da sum_p p^-6 endlich ist, sind
fast sicher nur endlich viele dieser Bewertungen positiv; jede einzelne
ist fast sicher endlich. c(x) ist daher fast sicher eine endliche ungerade
Zahl. Die Wahrscheinlichkeiten aller einzelnen Inhalte sind exakt

    P(c=n)=n^-6 / zeta_odd(6),    n odd.                      (9)

Das Produkt der lokalen Konstanten ist1/zeta_odd(6); die Summenmasse ist1.
Insbesondere zeta_odd(6)=pi^6/960. Die vollständige Inhaltsantwort ist

    E[c^-s] = zeta_odd(6+s)/zeta_odd(6),   Re s > -5.         (10)

Hier stammen die Eulergewichte aus den tatsächlichen sechs lokalen
Koordinaten. Es wurde weder ein einzelner primitiver Strahl gewählt noch
eine Primzahlreihe als Eingabe zum Zustandszensus benutzt. Die Eulerzerlegung
ist der Beweis der geschlossenen Formel, keine Annahme über berechenbare
Nullstellen. Gleichung(10) ist eine Laplace-/Mellinantwort eines positiven
Zensus; sie besitzt nicht deshalb einen RH-Spektral- oder Positivitätsbeweis.

## 6a. Eine vollständig definierte Primzahl-Sprungdynamik

Die obige Inhaltsverteilung besitzt die absolut konvergente Logarithmusform

    log E[c^-s] = sum_(p odd,k>=1) p^(-6k)/k [exp(-s k log p)-1],
    Re s > -5.                                               (10a)

Die Identität folgt durch logarithmisches Entwickeln jedes lokalen
geometrischen Faktors; im genannten Halbebenenbereich sind beide Reihen
absolut konvergent. Setze nu(p^k)=p^(-6k)/k. Die gesamte Sprungrate ist

    lambda=sum nu=log zeta_odd(6)<infinity.

Ziehe eine Poissonzahl mit Mittel tau*lambda und multipliziere so viele
unabhängige Sprünge q=p^k mit Wahrscheinlichkeit nu(q)/lambda. Das definiert
für alle tau>=0 einen multiplikativen Prozess C_tau mit C_0=1, unabhängigen
stationären Inkrementen und endlich vielen Sprüngen auf endlichen Zeitstrecken.
Sein Generator auf beschränkten Funktionen der ungeraden positiven Zahlen ist

    (L f)(n)=sum_(q odd prime power) Lambda(q)/(q^6 log q)
                                        * [f(nq)-f(n)].       (10b)

Dabei ist Lambda(p^k)=log p, sonst null. Also ist genau die Mangoldt-Funktion
der gewichtete Sprungträger. Die Reihe definiert einen beschränkten Operator
mit Norm höchstens2*lambda und damit eine eindeutige gleichmäßig stetige
Markov-Halbgruppe zu diesem angegebenen Generator. Aus dem Poissonprodukt
folgt die ganze Antwort

    E[C_tau^-s] = exp(tau * die Logreihe in (10a)).             (10c)

Diese Schreibweise legt für komplexes s den Zweig fest. Bei tau=1 ist das
Gesetz von C_1 exakt das Haar-Inhaltsgesetz aus (9). Dies wählt keine Dynamik
unter beliebigen Prozessen mit demselben Endgesetz aus; vorausgesetzt sind
hier die angegebenen unabhängigen stationären multiplikativen Sprünge.

Ein tatsächlich ausführbarer endlicher Zugang benötigt keine unbekannten
Teiler einer Eingabe N: Für ein ganzzahliges R>=1 werden die öffentlichen
Primzahlpotenzen q<=R durch ein gewöhnliches Sieb erzeugt. Behalte nur diese
Sprünge. Durch Kopplung derselben behaltenen Poissonereignisse gilt für die
ganze Fehlerwahrscheinlichkeit bis Zeit tau und somit für die
Totalvariationsdistanz der Endgesetze

    error <= 1-exp(-tau*sum_(q>R)nu(q))
          <= tau*sum_(m>R)m^-6 <= tau/(5R^5).                 (10d)

Die letzte Schranke folgt aus dem Integral einer fallenden Funktion.
Sie ist ein bezahlter Cutofffehler; Rundungsfehler eines numerischen
Samplers müssen zusätzlich bezahlt werden. Der beigefügte Prüfer wertet
die entsprechende endliche Laplaceantwort mit Arb-Intervallen aus.
Für die verwendeten Testfunktionen n^-s mit reellem s>=0 ist der
Erwartungsfehler ebenfalls höchstens die angegebene Kopplungsschranke.

Diese Konstruktion ist die klassische unendliche Teilbarkeit der
Zetaverteilung auf der hier quellbestimmten ungeraden Stelle und dem
Rangparameter6. Sie wird nicht als neue Wahrscheinlichkeitstheorie
beansprucht: [Saito–Tanaka, Theorem2.5](https://www.cc.kyoto-su.ac.jp/~tatsushi/inf_div.pdf)
behandeln die allgemeine Zetaverteilung;
[Aoyama–Nakamura, Proposition1.11](https://arxiv.org/pdf/1204.4042)
geben die ungerade Primstellenform an. Der quellspezifische Anschluss
an Gamma und die Operationsgrenzen sind hier gesondert bewiesen.

Der alte F9-Prozess g->g/p^k mit Rate log p benutzt dagegen ausschließlich
Primzahlpotenzteiler des aktuellen Eingangs g. Seine richtige erste
Sprungauswahl kann bereits faktorisieren. (10b) ist ein Aufwärtsprozess
mit eingabeunabhängigen Sprüngen. Beide besitzen Mangoldtgewichte,
aber sie haben unterschiedliche Zustände, Richtungen und Zugangsprobleme.
Das hier vollständig zugängliche Sprunggesetz darf deshalb nicht als
Lösung des dort noch offenen Teiler-Samplers ausgegeben werden.

## 7. Die volle affine Algebra erzwingt einen anderen thermischen Anschluss

Auf ell2(Gamma) einschließlich0 seien T_a delta_gamma=delta_(gamma+a) und
V_n delta_gamma=delta_(n gamma). Die Translationen sind unitär, V_n isometrisch.
Für n odd gilt

    V_n T_a = T_(na) V_n,
    sum_(a in Gamma/nGamma) T_a V_n V_n* T_a* = I.             (11)

Die Summanden sind die orthogonalen Projektionen auf die n^6 Restklassen.
Angenommen, ein KMS_beta-Zustand phi existiert für eine Dynamik alpha_t
mit alpha_t(T_a)=T_a und alpha_t(V_n)=n^(it)V_n. Für die analytischen
Generatoren gibt die KMS-Identität

    phi(V_n V_n*)=n^-beta phi(V_n*V_n)=n^-beta.

Ein zeitfester unitärer T_a liegt im Zentralisator von phi; deshalb hat
jeder übersetzte Summand denselben Erwartungswert. Aus (11) folgt

    1=n^6 n^-beta, also beta=6.                              (12)

Das ist eine notwendige Bedingung. Existenz, Eindeutigkeit, Normalität in der
angegebenen Darstellung oder eine TFPT-Identifikation werden nicht daraus
abgeleitet. Die unterliegende ax+b-/Cuntz-Konstruktion und ihre Indexzeiten
sind klassisch; siehe Cuntz, arXiv:math/0611541, Abschnitte3–4.

Unter der anderen Zeiteinheit alpha_t(V_n)=n^(6it)V_n wäre die notwendige
inverse Temperatur1. Zugleich würde der radiale Trace (6) zu zeta_odd(6beta),
mit Polstelle beta=1/6. Das Verhältnis der KMS-Stelle zur radialen
Tracepolstelle bleibt6. Eine reine Änderung der Zeiteinheit identifiziert
die beiden Zustandskonstruktionen daher nicht.

Für2 ist V_2 in dieser Darstellung sogar unitär. Würde man dennoch
alpha_t(V_2)=2^(it)V_2 und beta!=0 verlangen, ergäbe KMS
1=2^-beta, ein Widerspruch. Ein solcher Zweier-Energiekanal braucht eine
geänderte Skalierungsalgebra mit einem Träger, in dem2 keine Einheit ist,
oder einen geänderten Zeit-/Zustandsvertrag. Ein bloßer Darstellungswechsel
derselben unitalen Algebra hebt die Unitarität von V_2 nicht auf.

## 8. Warum die positive Uhr nicht still auf die ganze affine Quelle übergeht

H* ist nicht unter allen T_a invariant: T_a delta_(-a)=delta0 für a!=0.
Der ausgeschlossene Nullvektor ist der konstante Fouriermodus des ursprünglichen
Solenoids; seine Entfernung darf bei einer Zustands-/Observablenidentifikation
nicht verborgen werden.

Für festes ungerades n>1 ist der einzige Einheitkreis-Punkteigenwert von V_n
auf ell2(Gamma) die1, getragen von delta0. Tatsächlich gilt
intersection_(k>=0) n^k Gamma={0}; auf Gamma ohne0 zerfällt V_n in reine
einseitige Verschiebungen und hat keinen Einheitkreis-Eigenvektor.
Eine hypothetische unitäre Implementierung alpha_t(V_n)=n^(it)V_n auf
diesem ganzen Hilbertraum müsste aber die Punkteigenwertmenge{1} nach
{n^(it)} verschieben. Unitäre Konjugation erhält sie. Für geeignetes t ist
dies unmöglich.

Die obige Argumentation verbietet keine abstrakte äußere Zeitautomorphie
einer Semigruppenalgebra oder ihre Implementierung in einer anderen GNS-
Darstellung. Sie zeigt genau, warum H auf H* und die ganze affine Darstellung
einschließlich0 nicht ohne zusätzlichen Übergang dieselbe Zeitrealisierung sind.

## 9. Die konkrete nächste Kopplungsfrage

Der mathematische log-p-Schritt ist auf dem bezeichneten Nichtnullträger
jetzt explizit konstruiert. Die bisherigen Gates verändern die Prim-Inhalts-
Koordinate jedoch nicht. Eine neue Problemlösungsoperation muss diesen
entkoppelten Anteil mit der übrigen Operationsstruktur verbinden.

Affine Translationen oder nichtinvertierbare Projektionen können c ändern.
Zum Beispiel hat (3,5,0,0,0,0) Inhalt1, während die Projektion auf die erste
Koordinate Inhalt3 liefert. Dies ist kein Faktoralgorithmus: Die Information
stand bereits in der ausgewählten Koordinate. Für ein unbekanntes Eingabe-N
müssen Herstellung, Auswahl und Auslese eines solchen Zustands vollständig
aus N erklärt und bepreist werden. Die algebraische Existenz aller Matrix-
einheiten aus der Neunerbasis ist keine kostenlose physische Implementierung.

Für TFPT fehlt ein typgerechter physischer Anschluss der arithmetischen
Skalierungen und eines nichttrivialen gekoppelten Zustands. Für RH fehlen
die volle vorzeichenrichtige Arch-/Prim-/Polantwort und ihr globaler
Positivitätsbeweis. Für P versus NP wird aus keiner dieser Konstruktionen
ein allgemeiner Laufzeit- oder unterer Schrankenbeweis abgeleitet.

## 10. Ein tatsächlich zugänglicher Faktorantwort-Sampler und seine Kosten

Die unabhängige Ergänzung CONTENT-RESPONSE-COST.md beweist den vollständigen
Ausleseanschluss. Für N=pq mit verschiedenen ungeraden Primzahlen setze
a=(1-p^-6)^tau und b=(1-q^-6)^tau. Dann gilt exakt

    P(1<gcd(N,C_tau)<N)=a+b-2ab.                              (13)

Bei tau=1 ist der Erfolg p^-6+q^-6-2N^-6. Dieselbe Antwortverteilung erhält
man aus sechs unabhängigen uniformen Resten x_j modulo N und
G=gcd(N,x_1,...,x_6): Für jeden d|N ist P(d|G)=d^-6. Die vollständige
G-Verteilung folgt aus endlicher Teilerinversion, ohne dass der Algorithmus
die Teilerliste erhält. Sechs uniforme Ziehungen und ggT sind ein tatsächlich
zugänglicher N-only-Sampler; er erzeugt nur die Antwort, nicht den ganzen
unendlichen Primzahlprozess oder einen ganzen C_1-Integer.

Für balancierte p<q<=2p folgt jedoch

    P(proper gcd at tau)<=3645/448 * tau * N^-3 <9 tau N^-3.

Konstante Markovzeit besitzt damit bei wachsenden Eingaben verschwindende
Erfolgschance. Eine feste positive Endpunktchance benötigt hier tau=Theta(N^3).
Bei tau=N^3 ist sie mindestens
exp(-729/728)*(1-exp(-1))>0.2322; für tau/N^3->infinity fällt sie wiederum
gegen0, weil schließlich beide Faktoren enthalten sind. Explizite
Sprungsimulation benötigt im Erwartungswert lambda*tau Sprünge. Dies ist
keine allgemeine Bitkomplexitätsuntergrenze für jede mögliche direkte
Simulation des Endgesetzes. Wiederholung des obigen tau=1-Samplers benötigt
Theta(N^3) Versuche auf dieser balancierten Klasse.

Die Schranke betrifft genau diesen gemeinsamen Inhaltsleser. Schon ein
anderer Leser, gcd(N,x_1), hat bei uniformem x_1 eine andere, etwa N^-1/2
skalierende Erfolgschance. Aus (13) folgt kein Verbot aller Raumoperationen.
Der neue vollständige Anschluss erklärt zugleich die konkrete notwendige
Veränderung: Eine nützliche Quelle muss die gezielten Teilbarkeitsantworten
anders gewichten oder anders auslesen; der natürliche Rang6-Haarinhalt allein
liefert die benötigte Konzentration auf unbekannte Faktoren nicht.

## 11. Prüfung

check_prime_time.py besteht mit1043 Kontrollen: ganze endliche Quotienten,
ursprüngliche U/V-Wörter, exakte Poisson-Koeffizienten und rigorose
Arb-Laplaceauswertung mit unabhängig bezahltem unendlichen Cutoff. Bei
R=1024 werden188 öffentliche Primzahlpotenzsprünge benutzt; die ganze
Kopplungs-/Totalvariationsfehlerschranke bis tau=1 ist kleiner als1.78e-16,
die numerischen Rundungsradien liegen unter1.2e-77. Diese endlichen Kontrollen
ersetzen die obigen All-n-/Allzeitbeweise nicht. Eine unabhängige Agentenprüfung
hat die Beweise gelesen und die korrigierte Zweier-Einheitsgrenze verlangt.
Es wird weder eine formale Lean-Prüfung noch externe Begutachtung behauptet.
