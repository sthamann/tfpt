# TFPT: Drei Familien und derselbe wechselwirkende Zustand

21. September 2026 · Forschungsfortsetzung · **PARTIAL**

Forschungs-ID: **UR.RR.THREE_FAMILY_STATE.01**

## Ergebnis und Bedeutung für den Gesamtauftrag

Der geometrische Dreifamilienraum lässt sich exakt in die vorhandene native W-Dynamik einsetzen. Seine Fockdarstellung mit 48 Fermion- und 30 Bosonmoden bildet einen geschlossenen Sektor des unveränderten Hamiltonoperators. Es wird dafür weder ein Kopplungstensor angepasst noch ein weiterer Oszillator eingeführt.

Der bereits bewiesene wechselwirkende Grundzustand der Vierfamilienbank liegt jedoch in einem anderen Sektor. Für diesen Zustand bleibt eine konkrete gekoppelte Reststruktur erhalten. Ihre Entfernung verändert bereits die zweite Zeitantwort der drei behaltenen Familien. Die exakte richtige Zerlegung wird hier angegeben; sie bewahrt den bisherigen Zustand und alle Wechselwirkungen.

Damit sind zwei bisher leicht verwechselbare Aufgaben getrennt: Die geometrisch markierte Dreifamilienauswahl ist mit W verträglich. Die Auswahl ihrer physischen Darstellung und ihres Zustands folgt daraus noch nicht. Die vollständige TFPT-Lösung ist nicht erreicht. Die vorhandenen Flavor-/Yukawa-Ergebnisse werden nicht neu berechnet oder widerrufen.

## 1. Herkunft des Dreierraums

Für die vier Marken D={1,i,-1,-i} hat eine logarithmische Differentialform auf der Sphäre die Darstellung

    omega(z) = sum_a r_a dz/(z-a),       sum_a r_a = 0.

Die letzte Gleichung folgt aus der Regularität bei Unendlich: Mit w=1/z wäre der führende Term dort minus (sum r_a) dw/w. Somit ist der bereits vorhandene Raum H^0(P^1,K(D)) über seine Residuen genau der dreidimensionale Augmentationsraum

    F4 = C^4,   u = (1,1,1,1)/2,   U = u^perp.

Das orthogonale Komplement verwendet die im nativen Tensorvertrag vorhandene Einheitsmetrik. Der Kern der Summenabbildung selbst benötigt diese Metrikwahl nicht. Jede Permutation der vier Marken erhält u und U. Es handelt sich um den Familienraum, nicht um den ebenfalls dreidimensionalen Farbraum des RR-Trägers E.

Der frühere Residuenvertrag verwendet für Funktionen zusätzlich einen Spiegelungscharakter chi. Bei logarithmischen Formen wird dieser durch dz/z ausgeglichen. Die hier verwendete Familienwirkung ist die wirkliche Permutationswirkung auf den logarithmischen Residuen; sie ist nicht stillschweigend die unverdrehte Wirkung auf meromorphen Funktionen.

## 2. Exakte, wechselwirkungsverträgliche Reduktion

Der vorhandene native Vertrag lautet

    F = S+_16 tensor F4,       B = V10 tensor Lambda^2 F4,
    P_A = sum_(i<j) W_Aij f_j f_i,
    H = Delta N_b + g sum_A b_A^dagger P_A + conjugate(g) sum_A P_A^dagger b_A,
    Q = N_f + 2 N_b.

W ist der unabhängig archivierte reale Tensor mit WW^dagger=8 I_60. Im Folgenden wird derselbe Tensor verwendet. Eine gemeinsame Bosonenphase kann g reell wählen; die unten angegebenen Bewegungsgleichungen verwenden diese Konvention. Seine bereits bewiesene gl(4)-Kovarianz liefert für p0=|u><u|

    A0 = I_16 tensor p0,
    B0 = I_10 tensor dGamma_2(p0),
    W dGamma_2(A0) = B0 W.

Der nichtnegative Zahloperator

    Z = f^dagger A0 f + b^dagger B0 b

zählt Fermionen in der Familienmittelrichtung und Bosonen in u wedge U. Auf dem gemeinsamen endlichen Teilchenkern gilt [Z,H]=0. Die Aussage wird sektorweise in den endlichdimensionalen Q-Blöcken fortgesetzt; sie behauptet keine unkontrollierte Rechnung mit unbeschränkten Operatoren.

Da beide Summanden von Z nichtnegativ sind,

    ker Z = Fock_CAR(S+_16 tensor U) tensor Fock_CCR(V10 tensor Lambda^2 U).

Damit ist die Reduktion auf **48 Fermionmoden und 30 Bosonmoden exakt invariant**. Sie behält g und Delta. Der eingeschränkte Tensor W3 hat Format 30 x 1128 und

    W3 W3^dagger = 8 I_30,      rank W3 = 30,      dim ker W3 = 1098.

Eine reelle Hadamardbasis mit erster Spalte u macht die Rechnung rational und vollständig prüfbar. In dieser Basis hat W3 240 getragene Koeffizienten. Die Tensorprüfung vergleicht die gesamte Abbildung, nicht nur Dimensionen oder das Spektrum.

**Hodge-Konvention:** Der vorher verwendete Familien-Hodge-Operator K vertauscht Lambda^2 U und u wedge U. Wer W durch W-sharp=(I_10 tensor K)W ersetzt, muss daher B0 und den Bosonenprojektor ebenfalls mit K konjugieren. Dieselben Zahlenindizes mit unverändertem Projektor würden den falschen Dreißigerraum auswählen.

## 3. Der bekannte Grundzustand wählt diesen Sektor nicht

Der bereits vorhandene Grundzustandssatz besagt für 0<|g|/Delta<=1/20: Der globale Grundzustand Omega der vollen nativen Bank ist eindeutig, hat Q=64 und ist Spin(10) x SU(4)-invariant. Dieser Satz wird übernommen und nicht als neue Herleitung ausgegeben.

Zerlege p0=I_4/4+t0 mit spurlosem t0. Die Fermionen tragen Familiengewicht 1, die Bosonen Gewicht 2. Deshalb gilt

    Z = Q/4 + J(t0).

Auf dem SU(4)-Singulett verschwindet J(t0). Also

    Z Omega = 16 Omega.

Insbesondere ist die Projektion von Omega nach ker Z exakt null. Eine Reduktion nach ker Z kann nicht gleichzeitig behaupten, den bisherigen nativen Grundzustand zu erhalten. Diese Aussage ist auf den genannten Grundzustandsbereich und diesen Hamiltonoperator begrenzt; sie ist kein allgemeines Verbot einer physischen Dreifamilientheorie.

## 4. Was bei Erhaltung des Zustands tatsächlich übrig bleibt

Im geometrisch angepassten Familienrahmen unterscheiden wir die dunklen Indizes a=1,2,3 und den Mittelindex 0. Der tatsächliche Sektor Z=16 zerfällt als graduierter Tensorraum in den Drei-Familien-Fockraum und

    H_aux,16 = direct_sum_(k=0)^16 [Lambda^k C^16 tensor Sym^(16-k) C^30].

Dies sind die schon vorhandenen f_(alpha,0) und b_(v,0a), unter der exakten Bedingung N_(f,0)+N_(b,0U)=16. Es werden keine neuen Freiheitsgrade hinzugefügt. Die Zusatzstruktur ist endlichdimensional, aber nicht eindimensional. Ihre Dimension beträgt sum_k binomial(16,k) binomial(45-k,16-k) = 60 057 253 665 323. Die exakte Zerlegung ist daher keine Behauptung, dass man diesen Raum einfach vollständig diagonalisieren könnte.

Der unveränderte Hamiltonoperator zerfällt exakt in

    H|_(Z=16) = H3 + Delta N_b,0U + H_mix.

H_mix enthält die ursprünglichen W-Koeffizienten der Terme b_(v,0a)^dagger f_(beta,a) f_(alpha,0) und ihre Adjungierten. Insbesondere bleibt b_(v,0a)^dagger f_(alpha,0) Z-neutral. Selbst eine Mittelung über die von Z erzeugte U(1)-Wirkung entfernt diesen zusammengesetzten Operator und seine Wechselwirkung nicht. Diese mathematische Mittelung wird hier nicht als aus P1 hergeleitete physische Eichbedingung ausgegeben.

Das ist die richtige Ausgangsform für eine zustandserhaltende Eliminierung: Die drei Familien behalten eine Rückwirkung aus derselben Bank. Ein dreifamiliger, zeitlokaler W-Hamiltonoperator allein ist auf diesem Zustand nicht die exakte Reduktion.

## 5. Die ausgelassene Rückwirkung ist bereits in der ersten Feldableitung messbar

Die ursprüngliche CAR/CCR-Normalordnung gibt [H,f_r]=-g D_r mit

    D_r = sum_(A,j) (M_A)_rj b_A f_j^dagger,
    {D_r,D_s^dagger} = sum M_A,rj M_B,sk
        [delta_AB f_j^dagger f_k + delta_jk b_B^dagger b_A].

Hier erweitert M_A die archivierte W-Zeile antisymmetrisch. Für r in einer behaltenen Familie zerfällt D_r=D3_r+Dmix_r. Von den 15 ursprünglichen Kopplungen gehören zehn zu den behaltenen Familien und fünf zur Mittelrichtung. Die Tensorprüfung bestätigt diese Summen als volle Gram-Matrizen.

Die Kreuzorthogonalität von D3 und Dmix gilt bereits operatoralgebraisch: In der obigen Antikommutatorformel sind sowohl die Bosonenindizes A als auch die kontrahierten Fermionindizes j der beiden Teile disjunkt. Im SU(4)-invarianten Grundzustand sind zudem die Einteilchenkovarianzen skalar. Setze bbar=<N_b>, nu=1-bbar/32 und n_b=bbar/60. Mit dem positiven Antikommutator-Skalarprodukt ergibt sich

    ||D_r||_Omega^2     = 15(nu+n_b) = S,
    ||D3_r||_Omega^2    = 10(nu+n_b) = 2S/3,
    ||Dmix_r||_Omega^2  =  5(nu+n_b) = S/3,
    (D3_r,Dmix_r)_Omega = 0,
    S = 15 - 7 bbar/32 >= 8.

Die letzte Schranke folgt aus Q=64 und 0<=N_b<=32. Damit ist die quadrierte Norm des beim schlichten Weglassen der Mittelrichtung ausgelassenen Feld-Zeitableitungsanteils mindestens

    |g|^2 S/3 >= (8/3)|g|^2 > 0.

Das ist genau ein Drittel der ursprünglichen quadrierten Norm dieser Ableitung. Es bedeutet weder ein Drittel der Teilchenmasse noch ein Drittel jeder Korrelationsfunktion. Auf dem ursprünglichen stationären Zustand ist S|g|^2 das bekannte zweite Spektralmoment; die isolierte reduzierte Zustandsdichte muss für H3 nicht stationär sein.

Der Vergleich lässt sich ohne zusätzliche Stationaritätsannahme direkt als gemeinsame Zeitkorrelation schreiben: Für C_r(t,s)=< {f_r(t),f_r^dagger(s)} > auf demselben Omega gilt bei t=s=0 die gemischte Ableitung partial_t partial_s C_r = |g|^2 S. Nach bloßem Entfernen von H_mix bei unverändertem g liefert dieselbe Rechnung 2|g|^2 S/3. Das ist ein konkreter Unterschied zwischen zwei Zeitantworten auf demselben Zustand. Eine Anpassung von g könnte diese einzelne Zahl nachbilden, aber nicht den folgenden vollständigen Operatorfehler beseitigen.

Auch eine neue skalare Kopplung g-prime behebt den Operatorfehler nicht: Wegen der Orthogonalität ist die Fehlersumme

    |g-g-prime|^2 (2S/3) + |g|^2 S/3.

Zusätzliche reine Fermionkinetik kann diesen Rest ebenfalls nicht kompensieren, weil die linearen f-Operatoren zu D3 und Dmix im gleichen Antikommutator-Skalarprodukt orthogonal sind. Dies schließt nur diese zeitlokale native Form aus; andere nichtlineare effektive Operatoren oder eine exakte Gedächtnisdynamik werden dadurch nicht ausgeschlossen.

## 6. Was dies löst, und was weiterhin zuerst hergeleitet werden muss

Die geometrisch vorgegebene Dreifamilienauswahl und der vorhandene W-Tensor sind nun auf der Ebene der vollständigen Fock-Wechselwirkung miteinander verbunden. Gleichzeitig ist entschieden, welche Darstellung den bekannten Grundzustand bewahrt. Eine behauptete physische Rückverbindung muss angeben, ob die Rohquelle den leeren Mittelrichtungssektor Z=0 oder den gekoppelten Sektor Z=16 mit seiner zusätzlichen Antwort erzeugt. Eine Wahl allein aufgrund der gewünschten Familienzahl wäre nicht hergeleitet.

Die parallel erneuerte Originalquellenprüfung findet weiterhin kein unabhängig definiertes geladenes Funktional, das diesen Zustand, die gemeinsame Zeit und g/Delta auswählt. P1 beschreibt einen reflexionspositiven Kern mit Einheitswindung und Normierung. Der vorhandene freie DtN-Zweig und der separat berechnete affine Kubiktensor sind noch nicht als dieselbe geladene Quelle identifiziert. Das vorhandene Clock-Variationsfunktional enthält diese Auswahl ebenfalls nicht.

Die passende Rekonstruktionstheorie setzt eine hinreichend vollständige Familie von Greenfunktionen samt Positivität und Regularität voraus; sie ergänzt keine fehlenden geladenen Quelldaten. Siehe [Osterwalder und Schrader, Axioms for Euclidean Green's Functions II (1975)](https://projecteuclid.org/journals/communications-in-mathematical-physics/volume-42/issue-3/Axioms-for-Euclidean-Greens-functions-II-with-an-Appendix-by/cmp/1103899050.pdf).

Der nächste Herkunftsbeweis muss daher eine konkrete Formel für dieselbe graduierte Quelle liefern und darin den Familienprojektor, die Zustandsregel und den gemischten infinitesimalen Transfer auswerten. Ein aus H3 oder H_W zurückdefinierter Transfer wäre zirkulär. Die Formel ist im geprüften Bestand noch nicht vorhanden. Auch die darüber hinaus verlangten lokalen 3+1D-, chiralen, Kontinuums-, Gravitations- und kosmologischen Anschlüsse bleiben Bestandteile des Gesamtauftrags.

## 7. Quellen und Prüfgrenze

- `rr-residue-memory-20260921/HERLEITUNG.md`: tatsächliche Residuenwirkung, Augmentationsraum und Hodge-Konvention.
- `rr-continuous-clock-20260921/RR_VORAUSSETZUNGEN.md`: RR-Träger, 3+2 und vollständiger W-Anschluss.
- `rr-continuous-clock-20260921/HERLEITUNG.md`: gl(4)-Kovarianz und Grenze zwischen interner Uhr und physischer Zeit.
- `universalraum-native-ground-response-20260915/RESULTS.md`, Abschnitte 3-5: übernommener Grundzustandssatz, Operatorantwort und S.
- `primitive-charged-source-response-20260921/SOURCE_PROVENANCE.md`: P1 und Transfer auf ihren tatsächlichen Quellenräumen.
- `source-stable-low-charge-reconstruction-20260921/HERLEITUNG.md`: bestehender bedingter Rekonstruktionssatz, kein neuer Herkunftsbeweis.
- `original_source_audit.md`: erneuter begrenzter Audit von 15 Originaldateien, mit Zeilenbelegen und Hashes.

Der neue Rechner prüft den vollen gepinnten endlichen W-Tensor mit exakter rationaler beziehungsweise skalierter Ganzzahlarithmetik. Allgemeine Fock-, Zustands- und Normaussagen folgen aus den ausgeschriebenen Beweisen und ihren Voraussetzungen. Es gibt keine Promotion in Paper oder Statusledger und keinen behaupteten Abschluss der physischen T1-T8-Gates.
