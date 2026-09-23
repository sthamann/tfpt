# Elektrische Energie vor Parameterselektion: die fehlende Domänenbrücke

12. September 2026. NON-RH. Konkrete notwendige Kompatibilitätsprüfung
der renormierten Collar-Familie mit dem vorhandenen Rotor-Testparent.

## Ergebnis

**Kein kappa>0 macht den konstruierten Collar-Grundzustand zu einem
Zustand endlicher elektrischer E^2-Energie unter der direkten Zuordnung
Fourierzahl k = Rotorfluss E.** Die Suche nach dem „richtigen kappa“
kann diese konkrete Brücke deshalb nicht reparieren.

Das widerspricht nicht der Stabilität des renormierten Randoperators:
Seine Energie ist ein anderer, durch Gegenbeiträge definierter Operator.
Es widerspricht auch nicht allen möglichen Abbildungen zwischen den
Quellen. Ein neuer Intertwiner müsste aber die physische elektrische
Observable und deren Formdomäne ausdrücklich mitführen.

Eine positive Alternative auf dem Kreis ist exakt konstruierbar, wenn
man einen quadratischen elektrischen Term bereits im Grundoperator
behält. Dann braucht die Punktwechselwirkung keinen neuen singulären
Bindungsparameter. Der Preis ist nicht null: Die Zuordnung dieses
Kreisterms zum nativen Rotor und seine Koeffizienten müssen hergeleitet
werden; bloßes Addieren ist ein Kandidatenansatz.

## 1. Tatsächlicher Energievertrag des vorhandenen Parents

Die eingesehene Quelle `../neutral-ground-state/README.md`, §§1–2,
enthält auf endlichen Tori

    H_native = (kappa_native/2) sum_links E_l^2 + B,

mit endlichdimensionalen Materiefaktoren und beschränktem B. Die dortigen
Modellwerte sind kappa_native=1/100, a=1/12, eta=1/2, beta=1/4,
M=4, epsilon_L=1/96. kappa_native ist NICHT unser kappa_bind des
renormierten Collars. Die Bezeichnung darf keine Identifikation suggerieren.

Der Bericht `../parent-selection-audit/README.md` benennt diesen Parent
selbst als deklariertes Testmodell, nicht als eindeutig aus TFPT hergeleitet.
Seine offene physische Operatorzuordnung wird hier nicht als erledigt
vorausgesetzt. Die beschränkten Hops können auf einem endlichen Torus
eine divergierende positive elektrische Erwartung nicht kompensieren.

## 2. Ausschluss der direkten Zuordnung für ALLE Bindungsparameter

Der zuvor konstruierte normierte Collar-Grundzustand ist

    psi(k)=Z_kappa^(-1/2) 1_(k in4Z)/(|k|+kappa),
    Z_kappa=1/kappa^2+2 sum_(n>=1)1/(4n+kappa)^2 < infinity.

Aber

    <E^2> = [2 sum_(n>=1)(4n)^2/(4n+kappa)^2]/Z_kappa = infinity.

Jeder Summand im Zähler geht gegen 2. Schon für n>=kappa/4 ist
2(4n)^2/(4n+kappa)^2>=1/2. Außerdem gilt
Z_kappa<=1/kappa^2+1/4, weil sum n^-2<=2. Dies liefert eine explizite
linear divergierende untere Schranke für normierte Cutoff-Zustände.

Ebenso divergiert die bare |D|-Erwartung logarithmisch. Die endliche
renormierte Gesamtenergie beruht auf deren kontrollierter Kompensation,
nicht auf endlichen einzelnen positiven elektrischen Beiträgen.

Auch eine affine Fluxzuordnung E=ak+b mit a!=0 beseitigt die quadratische
Divergenz nicht. Eine beliebige nichtdiagonale Abbildung ist durch dieses
Argument dagegen nicht ausgeschlossen. Ihre Observable darf nicht einfach
neu als E bezeichnet werden, wenn sie den originalen Rotor nicht erhält.

## 3. Positive Alternative: elektrische Regularität behalten

Nimm auf demselben Kreis ausdrücklich als Kandidat

    A_eta=|D|+eta D^2, eta>0,
    q_(eta,eps)(f)=sum_k (|k|+eta k^2)|fhat_k|^2
                       +eps sum_j |f(theta_j)|^2, eps>=0.

Die Formdomäne ist H1(S1). Punktauswertung ist dort stetig:

    |f(theta)|^2 <= [sum_k (1+eta k^2)|fhat_k|^2]
                       [sum_k 1/(1+eta k^2)],

und die letzte Reihe konvergiert. Da der Punktterm positiv und bezüglich
der Grundformnorm beschränkt ist, ist die Gesamtform abgeschlossen und
nach unten beschränkt. Sie definiert genau einen selbstadjungierten
Operator über den Formdarstellungssatz; seine Formdomäne bleibt H1.
Es folgt <D^2><infinity für seine Zustände endlicher Formenergie.

Der kompakte Einbettungssatz H1->L2 liefert kompakten Resolventen. Für
eps>0 gibt es keinen Nullvektor der Form: q0=0 erzwingt Konstanz, die
Punktbeiträge erzwingen dann null. Also ist der niedrigste Eigenwert
positiv. Eine allgemeine Grundzustands-Einfachheit wird hier nicht aus
endlichen Eigenwerttests behauptet. Wärme- und unitäre Zeitentwicklung
existieren durch den Spektralsatz.

Dies ist eine klassische Formkonstruktion, keine neu beanspruchte
allgemeine Mathematik. Primärer Kontext für die Bedeutung von H1 bei
eindimensionalen Deltaformen: https://arxiv.org/abs/1403.1401 , dort
Gleichungen (1.5)–(1.6). Die Kreis-/|D|+eta D^2-Aussage wird hier direkt
über die ausgeschriebene Abschätzung begründet.

## 4. Punktwechselwirkung bleibt bei festem eta erhalten

Mit R_eta=(A_eta+I)^(-1) ist nun bereits

    G_eta=V*R_eta V

als vierdimensionale Matrix endlich: die Summanden fallen wie k^-2.
Die Spalten B_eta=R_eta V gehören zu l2. Der Resolvent lautet

    (H_(eta,eps)+I)^(-1)
      =R_eta-B_eta(eps^(-1)I+G_eta)^(-1)B_eta*   (eps>0).

Für den Fouriercutoff M gehen die beiden fehlenden Enden gegen null mit

    ||G_eta-G_(eta,M)|| <=8/(eta M),
    ||B_eta-B_(eta,M)||^2 <=8/(3 eta^2 M^3).

Die Schranken folgen aus den Spurnormen, |k|+eta k^2+1>=eta k^2 und
den Integralschranken für sum_(k>M) k^-2 beziehungsweise k^-4. Inversen
haben Norm höchstens eps. Damit folgt Normresolventenkonvergenz zu dem
nichttrivialen Punktoperator für festes eta>0 ohne laufenden Gegenparameter.

### Warum man eta im Grenzübergang nicht unbemerkt weglassen darf

Bei eta->0 gilt ||R_eta-R_0||<=eta. Die Gram-Eigenwerte in allen vier
Restklassen divergieren dagegen monoton, während ||B_eta||^2<=12 bleibt.
Die Resolventenkorrektur geht deshalb gegen null, auch wenn die positive
Punktkopplung dabei variiert. Übrig bleibt wieder der freie |D|-Operator.

Der elektrische Term kann also in einer Niederfrequenzentwicklung klein
sein und trotzdem die Existenz der Punktwechselwirkung bei beliebig hohen
Frequenzen entscheiden. Ihn zuerst wegzulassen ist für diese Frage keine
kontrollierte Näherung.

## 5. Was dies für die Lösungsarbeit entscheidet

1. **Nicht weiter nur kappa fitten:** Die direkte Collar-/Rotor-Zuordnung
   scheitert für die gesamte renormierte Familie an derselben positiven
   elektrischen Energiepflicht.
2. **Ein möglicher Reparaturmechanismus ist konstruiert:** Bei tatsächlich
   hergeleitetem eta D^2 kann eine positive Punktwechselwirkung ohne
   zusätzlichen singulären Bindungsparameter bestehen.
3. **Keine Vorwärtsherleitung erschlichen:** eta=1/200 im Prüfer ist nur
   der vorhandene native Modellwert als kontrollierter Kandidat. Ein
   Seam-/Link-Intertwiner wurde dadurch nicht gebaut. Ebenso ist eps=0.4
   ein übernommener v331-Testwert, keine Naturkonstante.

Die vorhandene Recovery-Zahl 6 log(3/2) aus v302 wird deshalb NICHT
einfach kappa oder einem neuen Eigenwert gleichgesetzt. Der dortige
Verifier bestätigt die bezeichnete Zahl aus vorgegebenen Transferspektren;
er liefert keine Abbildung ihrer Moden auf die hiesigen Rand-/Rotorzustände.

Das nächste echte Abnahmekriterium ist eine quellenseitig definierte
Abbildung, die Clock, Ladung UND elektrische Formdomäne gemeinsam erhält.
Weitere Anpassung eines einzelnen Eigenwerts würde dieses Kriterium nicht
ersetzen. Keine T1–T8-Schließung, kein Vollständigkeitsmarker.

## Prüfung

`electric_domain.py` prüft rationale divergierende Energieschranken,
positive endliche Kandidatenmatrizen, ihre Uhrkovarianz, direkte gegen
Woodbury-Inversion und die rationalen Schwanzabschätzungen. Die allgemeinen
Aussagen folgen aus den Beweisen oben; numerische Cutoff-Proben werden
nicht als Beweis für den gesamten Grenzübergang ausgegeben.
