# Begrenzte Prüfung der neuen Kimi-/Opus-Q3-Behauptungen

Die Spektralpassagen von `antwort_kimi.md` und `antwort_opus.md` sowie die
betreffenden Originalprüfer wurden gelesen. Es wurden keine fremden Dateien
geändert und keine langen Fremdprüfer ausgeführt.

## Opus: Der angeblich zertifizierte Gap ist nicht geschlossen

Quelle: `experiments/theory-contracts/universalraum-followups-closure-20260914/quartet_cert.py`.

Der Prüfer berechnet mit `eigsh` vierzehn Näherungspaare. Um Zeilen
1294–1319 wird `next_cluster_lower` aus der Residualeinschließung des
**nächsten gefundenen** Eigenwertclusters gebildet und als Temple-Separator
verwendet. Eine Residualeinschließung beweist die Existenz eines Eigenwerts
im jeweiligen Intervall. Sie beweist nicht, dass kein unentdeckter Eigenwert
zwischen dem Quartett und diesem Intervall oder unterhalb des Quartetts liegt.
Ohne vollständige Eigenwertzählung bzw. separaten sektorweiten Bound ist
der benötigte Temple-Separator nicht bewiesen.

Folglich ist 0,5504253482676765 durch diesen Code **kein zertifizierter
globaler Spektralgap**, selbst wenn alle gemessenen Residuen und
Rundungsabschätzungen stimmen.

Zusätzlich wird in `character_certificate` der Charakter eines numerisch nur
annähernd invarianten Viererspanns gerundet. Die anschließend ganzzahlige
Charakterskalarproduktrechnung ist exakt **für die gerundete Liste**. Sie
beweist allein keine exakte Invarianz des ursprünglichen näherungsweisen
Eigenraums. Eine exakte Projektor-/Multiplizitätsrechnung wäre nötig, wie
sie in den eigenen reduzierten Blöcken separat durchgeführt wurde.

Der Opus-Operator ist außerdem H0+F4_shared/800. Die hier ausgeführten neuen
edge-Bounds werden nicht als Zertifikate für diesen anderen Operator benutzt.

## Kimi: Existenz im Standardtyp ist noch nicht exakt vierfach global

Quelle: `experiments/theory-contracts/universalraum-followup-solutions-20260914/certify_quartet.py`,
insbesondere Zeilen 638–699.

Die gerichteten Intervalle und die Projektor-Defektabschätzung haben die
richtige Zielrichtung: Sie sollen einen Eigenwert des exakten
Standard-Multiplizitätsoperators im angegebenen Fenster nachweisen. Selbst
wenn sämtliche Rundungsdetails dieser Konstruktion stimmen, folgt aus
einem solchen Existenzsatz zunächst **Vielfachheit mindestens vier**.

Die Formulierung in Zeilen 693–696, der Eigenwert sei dadurch `EXACTLY
4-fold` als Eigenwert des gesamten trunkierten Singulettoperators, lässt
zwei Pflichten aus: Einfachheit im 80D-Multiplizitätsblock sowie Ausschluss
gleicher Eigenwerte in anderen Symmetrietypen. Die spätere explizite
Zählklausel im selben Prüfer erkennt einen Teil der offenen Gesamtrechnung
an, korrigiert aber den zu starken vorherigen Satz nicht automatisch.

Die eigenen Zertifikate beweisen inzwischen die Einfachheit des korrigierten
Standardblocks und die relevante Ordnung zunächst in 348, jetzt in 1764
Dimensionen. Für die übrigen 22260 Singulettdimensionen bleibt der globale
Koinzidenz-/Ordnungsnachweis offen. Keine Behauptung aus den Fremdtexten wird
als Ersatz für diesen Nachweis übernommen.
