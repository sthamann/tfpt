# Audit des gemischten Rekonstruktionssatzes

## Ergebnis

Der algebraische Kern des eingefügten Satzes ist korrekt, sofern die
Darstellungs- und Definitionsbereichsannahmen explizit gemacht werden. Er gilt
sogar ohne vorherige Polynomannahme:

* endlich viele CAR- und CCR-Moden;
* die **volle irreduzible Fockdarstellung** dieser kanonischen Felder;
* ein selbstadjungierter Operator `H`, der stark mit
  `Q = N_f + 2 N_b` kommutiert;
* alle verschachtelten Klammern sind Operatoridentitäten auf dem gemeinsamen
  algebraischen Endlichteilchenkern `D_fin`.

Dann bestimmen die beiden unteren Antworten und die gemischte Antwort `H` bis
auf eine reelle additive Konstante. Diese Aussage ist eine Zielseiten-Aussage
über kanonische Operatoren. Sie leitet weder diese Felder noch `W`, `g`, den
Zustand, die Zeit oder die Darstellung aus P1/P2 beziehungsweise einer
primitiven Quelle her.

## Präziser Satz

Sei

`F = Lambda(C^n_f) tensor Gamma_s(C^n_b)`

die irreduzible gemischte Fockdarstellung und `D_fin` ihr algebraischer
Endlichteilchenkern. Sei `H=H*`, stark `Q`-erhaltend. Für ein antisymmetrisches
`W_Aij` setze

`P_A = sum_(i<j) W_Aij f_j f_i`.

Gelten auf `D_fin`

```
{[f_i,H],f_j^dagger} = epsilon_f delta_ij I,
[[b_A,H],b_B^dagger] = epsilon_b delta_AB I,
Gamma_Aij := {[[b_A,H],f_i^dagger],f_j^dagger} = g W_Aij I,
```

dann

```
H = c I + epsilon_f N_f + epsilon_b N_b
    + sum_A (g b_A^dagger P_A + conjugate(g) P_A^dagger b_A),
```

mit `c` reell. Bei selbstadjungiertem `H` ist die adjungierte
Gamma-Identität die Adjungierte der angezeigten Identität. Ohne
Selbstadjungiertheit muss sie separat gefordert werden.

## Kompakter Beweis

1. Subtrahiere den angezeigten Kandidaten und nenne den Rest `R`. Alle drei
   Antworten von `R` verschwinden.

2. Die normalgeordneten CAR-Wörter `f_I^dagger f_J` bilden eine Basis der
   endlichen Fermionoperatoralgebra. Die Abbildung

   `R -> { [f_i,R], f_j^dagger }`

   ist die gemischte Grassmann-Ableitung nach einer Erzeuger- und einer
   Vernichtervariablen. Ihr gemeinsamer Kernel besteht genau aus Wörtern mit
   `I=empty` oder `J=empty`. Daher enthält `R` nach der ersten Antwort keine
   gemischten Fermionwörter.

3. Für jeden verbleibenden bosonischen Koeffizienten `T` gilt

   `[[b_A,T],b_B^dagger]=0`.

   Falls `[N_b,T]=mT` mit `m>0`, kommutiert `U_A=[b_A,T]` mit allen
   Erzeugern. Auf dem Polynomkern ist deshalb `U_A` Multiplikation mit dem
   homogenen Polynom `G_A(b^dagger)=U_A|0>` vom Grad `m-1`. Jacobi liefert
   `partial_A G_B = partial_B G_A`. Mit

   `F=(1/m) sum_A b_A^dagger G_A`

   und der Euler-Identität folgt `[b_B,F]=G_B`. Der Rest `T-F` kommutiert mit
   allen Vernichtern und erhöht die Bosonenzahl um `m`. Induktion über die
   Eingangs-Bosonenzahl zeigt `T-F=0`: sein Bild müsste zugleich Vakuum und
   von positiver Teilchenzahl sein. Für `m=0` folgt entsprechend `T=cI`; für
   `m<0` gilt die adjungierte Aussage. Damit ist kein analytischer oder
   unendlichgradiger Rest möglich.

4. `Q`-Erhaltung klassifiziert den verbliebenen Rest vollständig:

   ```
   R = cI + sum_(m=1)^(floor(n_f/2))
       sum_(|alpha|=m, |I|=2m)
       (C_(alpha,I) (b^dagger)^alpha f_I + adjoint).
   ```

   Weil ein CAR-Wort keine Mode doppelt enthalten kann, gilt bei 64
   Fermionmoden exakt `m <= 32`. Die zunächst beliebige Gradfrage ist damit
   auf endlich viele Koeffizienten reduziert.

5. `Gamma` ist auf diesem Raum die Ableitung nach einem Bosonerzeuger und zwei
   Fermionvernichtern. Sie ist auf allen `m>=1`-Umwandlungskomponenten
   injektiv. Bei `m=1` liest sie genau den kubischen Koeffizienten; bei `m>=2`
   bliebe ein nichtkonstanter operatorwertiger Beitrag. `Gamma(R)=0` setzt
   daher alle `C_(alpha,I)` gleich null. Nur `cI` bleibt.

Die Koeffizienten vor dem Gamma-Schritt sind bereits in den endlichen
`Q`-Sektoren bis `Q=64` sichtbar:

`C_(alpha,I) = <alpha Bosonen|H|I Fermionen>/sqrt(alpha!)`.

Somit kann oberhalb `Q=64` keine weitere, durch die drei Antworten unsichtbare
Umwandlung beginnen. Die Abschließung von `H` ist die direkte Summe der
endlichdimensionalen `Q`-Blockmatrizen. Diese Aussage ersetzt keine globale
Domain-Annahme: starke `Q`-Kommutation und die Identitäten auf `D_fin` sind
wesentlich.

## Unverzichtbare Irreduzibilität

Ohne volle irreduzible Fockdarstellung ist die Schlussfolgerung „bis auf
`cI`“ falsch. Auf `F tensor K` mit kanonischen Feldern `a tensor I_K` hat

`H = H_target tensor I_K + I_F tensor D`

für jeden nichtskalaren selbstadjungierten Zuschaueroperator `D` exakt
dieselben drei Antwortfamilien wie `H_target`. Der unsichtbare Rest liegt dann
im Kommutanten der Feldalgebra, nicht nur in den Skalaren. Eine verborgene
Quellenlinie, ein zusätzlicher Oszillator oder eine Zuschauer-Algebra darf
deshalb nicht stillschweigend entfernt werden. Der Satz rekonstruiert die
volle Zeitentwicklung nur, wenn die getesteten Felder irreduzibel die gesamte
Hilbertstruktur erzeugen oder der Kommutant unabhängig kontrolliert ist.

## Symmetrieform höherer Umwandlungen

Nach den beiden unteren Antworten, aber vor `Gamma`, liegt die Ordnung `m` in

`Sym^m(B) tensor Lambda^(2m)(F*)`

plus Adjungiertem. Bei einer Symmetriegruppe `G` sind genau die Invarianten

`(Sym^m(B) tensor Lambda^(2m)(F*))^G`

zulässig. Dies charakterisiert mögliche höhere Umwandlungen, wählt aber keine
davon aus. Die vollständige gemischte Antwort beseitigt alle `m>=2`-Anteile.

## Exakte Kontrollen

`checker.py` arbeitet ohne Fließkomma-Rangentscheidung:

* Für `n_b=1`, `n_f=4`, Gesamtgrad höchstens 8 werden genau 326
  ladungsneutrale normalgeordnete Monome gefunden. Die vollständige
  Antwortabbildung aus beiden unteren Tensoren, `Gamma` und der adjungierten
  Antwort hat modulo der Primzahl 2147483647 Rang 325. Ein modularer
  Rang-325-Minor ist auch über den rationalen Zahlen ungleich null; da die
  Identität sichtbar im Kernel liegt, ist der rationale Rang exakt 325 und
  der Kernel exakt `span{I}`.
* Die CAR-Vorzeichen wurden durch unabhängige Operatormatrizen geprüft:
  `[f_j f_i,f_k^dagger]=delta_ik f_j-delta_jk f_i` für `i<j`.
* Der native Tensor hat den erwarteten SHA-256, Form `60 x 2016`, 480
  nichtverschwindende obere Einträge und exakt `W W*=8 I_60`.
* Alle `60*64*64 = 245760` geordneten Gamma-Komponenten wurden aufgebaut.
  Das obere Dreieck reproduziert `W` einschließlich aller Nullkomponenten und
  Vorzeichen; die geordnete antisymmetrische Fortsetzung hat 960
  nichtverschwindende Einträge. Bei Einheitskopplung ergibt die Projektion
  `sum conjugate(W) Gamma / 480` exakt 1.
* Normaler Lauf und `python3 -OO` erzeugen byteidentische Ausgabe.

Diese Kontrollen belegen den algebraischen Zielseitensatz. Sie sind kein
Nachweis, dass die primitive TFPT-Quelle die getesteten Operatoren oder
`Gamma=gW` erzeugt.

## Stärker nach den unteren Antworten: ein vollbesetzter Übergang genügt

Nach den beiden unteren **Operatoridentitäten** ist keine treue Gesamtstate
mehr nötig. Sei

`|F> = f_1^dagger ... f_64^dagger |0_f,0_b>`

der vollbesetzte Fermionzustand. Für den oben klassifizierten Rest

`sum C_(alpha,I) (b^dagger)^alpha f_I + adjoint`

bildet `Gamma_Aij` einen Term der Ordnung `m` auf einen Zustand mit
`m-1` Bosonen und `2m-2` Fermionlöchern ab. Bei festem `(A,i,j)` sind die
Bilder verschiedener `(alpha,I)` orthogonal: Ihr vollständiges Label ist

`(A,i,j,alpha-e_A,I\{i,j})`.

Für `D_(alpha,I)=C_(alpha,I)-gW_Aij` bei `m=1` und
`D_(alpha,I)=C_(alpha,I)` bei `m>=2` folgt deshalb exakt

```
E_Gamma(F;g)
  = sum_(A,i<j) ||(Gamma_Aij-gW_Aij)F||^2
  = sum_(m=1)^32 m^2(2m-1)
      sum_(|alpha|=m,|I|=2m) alpha! |D_(alpha,I)|^2.
```

Das Gewicht ist positiv und hat keine versteckte Interferenz:

```
sum_A alpha_A^2 (alpha-e_A)! = m alpha!,
binomial(2m,2) = m(2m-1).
```

Also gilt nach den unteren Operatorantworten bereits

`E_Gamma(F;g)=0`

genau dann, wenn der kubische Koeffizient `gW` ist und alle höheren
Umwandlungen verschwinden. Die adjungierten Umwandlungen tragen nicht direkt
zu `Gamma` bei, weil sie nur Bosonvernichter enthalten; Selbstadjungiertheit
von `H` bindet ihre Koeffizienten jedoch an die bereits bestimmten
Vorwärtskoeffizienten. Der vollbesetzte Zustand trennt somit den relevanten
Rest, obwohl er die gesamte Operatoralgebra nicht trennt.

Noch einfacher lässt sich sogar `Gamma` als vorausgesetzte Antwort vermeiden.
Setze

```
X = sum_A b_A^dagger P_A,
|v> = X|F>,                 ||v||^2 = 480,
E_F = <F|H|F> = c + 64 epsilon_f,
g_F = <v|H|F>/480,

D_F = ||(H-E_F)F||^2 - |<v|H|F>|^2/480 >= 0.
```

Dies ist wieder ein orthogonaler Projektionsrest. Die adjungierten
Umwandlungen vernichten `|F>`; alle übrigen `(alpha,I)` erzeugen
untereinander orthogonale Bosonen-/Lochzustände. Daher gilt unter den beiden
unteren Operatoridentitäten

`D_F=0`

genau dann, wenn alle Ordnungen `m>=2` verschwinden und der `m=1`-Vektor
`g_FW` ist. Damit ist der native Generator bis auf `cI` rekonstruiert und
`Gamma=g_FW` folgt anschließend, statt vorausgesetzt zu werden. Dieser eine
positive Test benötigt nur Energievarianz im Zustand `F` und den Übergang in
die bekannte Richtung `v`.

Für die konkrete Störung

`H_eta = H_target + eta (X^2 + (X^dagger)^2)`

gilt

```
D_F(H_eta) = 439680 eta^2,
E_Gamma(F;g) = 12 D_F(H_eta) = 5276160 eta^2.
```

Der Wert `||X^2F||^2=439680` ist im vorhandenen nativen
Ground-Response-Artefakt durch vollständige Enumeration der 1830
Zwei-Bosonkonfigurationen ausgewiesen; er wurde in diesem kleinen Audit nicht
erneut voll enumeriert. Der Faktor 12 folgt hier neu und exakt aus dem
allgemeinen Gewicht für `m=2`.

`F` ist dabei ein algebraischer Diagnosezustand. Es wird weder behauptet, dass
er der physische Weltanfangszustand sei, noch dass primitive Quellenfelder,
`F`, `X` oder die angezeigten Defekte bereits aus P1/P2 hergeleitet oder
quellenseitig ausgewertet wurden.

## Allgemeiner, aber stärker voraussetzender positiver Quellenvertrag

Wenn auch die beiden unteren Operatoridentitäten durch Zustandsdaten ersetzt
werden sollen, kann man alle drei Antworten bedingt durch **ein einziges
positives Defektfunktional** prüfen. Dafür ist im Gegensatz zum speziellen
vollbesetzten Test Treue beziehungsweise Separierung erforderlich.

Sei `omega` ein normierter Zustand auf der von den Antwortoperatoren erzeugten
Algebra. Für die unabhängigen Komponenten `S={(A,i,j): i<j}` gilt
`sum_S |W_Aij|^2=480`. Setze

```
g_omega = (sum_S conjugate(W_Aij) omega(Gamma_Aij))/480,

E_Gamma = sum_S omega(Gamma_Aij^dagger Gamma_Aij)
          - |sum_S conjugate(W_Aij) omega(Gamma_Aij)|^2/480.
```

Im direkten GNS-Summenraum ist dies genau das Quadrat des orthogonalen
Abstands der Vektorfamilie `Gamma_Aij Omega` von der eindimensionalen Richtung
`W_Aij Omega`:

`E_Gamma = sum_S ||(Gamma_Aij-g_omega W_Aij)Omega||^2 >= 0`.

Daher gilt exakt

`E_Gamma=0  <=>  (Gamma_Aij-g_omega W_Aij)Omega=0` für alle `S`.

Ist `omega` auf der Antwortalgebra treu, folgt daraus
`Gamma_Aij=g_omega W_Aij I`. Gleichwertig genügt, dass `Omega` für die
Algebra der Defektoperatoren separierend ist. Für unbeschränkte lokal
affiliierte Defekte müssen zusätzlich ein gemeinsamer invarianter Kern, die
Zugehörigkeit von `Omega` zu allen benötigten Domains und Endlichkeit der
angezeigten quadratischen Formen vorausgesetzt werden.

Die unteren Antworten erhalten dieselbe Form. Mit

```
F_ij = {[f_i,H],f_j^dagger},
B_AB = [[b_A,H],b_B^dagger],

epsilon_f,omega = (sum_i omega(F_ii))/n_f,
E_f = sum_ij omega(F_ij^dagger F_ij)
      - |sum_i omega(F_ii)|^2/n_f,

epsilon_b,omega = (sum_A omega(B_AA))/n_b,
E_b = sum_AB omega(B_AB^dagger B_AB)
      - |sum_A omega(B_AA)|^2/n_b.
```

Damit ist

`E_source := E_f + E_b + E_Gamma >= 0`.

Unter Treue beziehungsweise Separierung gilt `E_source=0` genau dann, wenn
alle drei vollständigen Antworttensoren ihre vorgeschriebene skalare Form
haben. Zusammen mit Selbstadjungiertheit, `Q`-Erhaltung, irreduzibler
Fockdarstellung und den Domainannahmen greift dann der Rekonstruktionssatz.
Operational entspricht `E_Gamma` einer positiven normierten
Sechseinfügungs-Antwort: Es wird die Norm des gemischten Defekts gemessen,
nicht nur sein Vakuummittel.

### Warum Mittelwert und Vakuumnorm nicht genügen

Schon in `M_2(C)` hat `X=diag(1,-1)` im treuen Spurzustand Mittelwert null,
aber `omega(X^dagger X)=1`: Ein bloßer Mittelwert übersieht den Defekt, die
positive Norm erkennt ihn.

Der reine Vakuumzustand einer endlichen irreduziblen Fockdarstellung ist
dagegen nicht treu und sein Vektor nicht separierend für die volle
Operatoralgebra. Für `Omega=e_0` und den nichtverschwindenden Operator
`X=|e_0><e_1|` gilt `X Omega=0`; sowohl Mittelwert als auch quadratischer
Vakuumdefekt verschwinden. Entsprechend kann auch der Gamma-Defekt eines
höheren invarianten Terms, etwa eines als `X^2` bezeichneten Terms, das leere
Fockvakuum vernichten und damit unsichtbar bleiben, obwohl die
Operatoridentität falsch ist.

Ein treuer gemischter Zustand liefert im endlichen Fockmodell ein gültiges
Diagnostikum für alle drei Antworten zugleich. Die Separierung eines lokalen
AQFT-Vakuums kann unter den üblichen lokalen Algebra- und Domainvoraussetzungen
ebenfalls genügen. Daraus folgt keine Separierung für die globale endliche
Fockalgebra und keine bereits ausgeführte Quellenmessung. `E_source` ist der
allgemeine Quellenvertrag; `D_F` ist der schwächer voraussetzende Spezialtest
nach bereits bewiesenen unteren Operatorantworten. Keiner der beiden Werte
wurde hier aus der primitiven Quelle bestimmt.
