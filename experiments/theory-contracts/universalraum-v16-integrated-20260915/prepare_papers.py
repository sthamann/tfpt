"""Preserve every v1.5 chapter; weave authored v1.6 fragments into context."""
from pathlib import Path
import shutil,json,hashlib
HERE=Path(__file__).resolve().parent
BASE=HERE.parent/'universalraum-native-closure-20260914/main-v1.5'
DST=HERE/'main-v1.6'
DST.mkdir(exist_ok=True)
(DST/'chapters').mkdir(exist_ok=True)
if not (DST/'figures').exists():
    shutil.copytree(BASE/'figures',DST/'figures')
placements={
 '01_idee.tex':('\\section{TFPT als Grammatik und als Übersetzung}','01_idea'),
 '02_algebra.tex':('\\section{Wurzeln und Generatoren sind verschiedene Zählungen}','02_order'),
 '03_prozess.tex':('\\section{Warum Symmetrie die Gewichte noch nicht auswählt}','03_selection'),
 '04_zellen.tex':('\\section{Warum Austausch allein die Zelle nicht herstellt}','04_preparation'),
 '05_kopplung.tex':('\\section{Warum viele Zellen noch ein eigener Schritt sind}','05_transport'),
 '06_zeit_echo.tex':('\\section{Die wirklichen Erfolgswahrscheinlichkeiten}','06_records'),
 '07_seam.tex':('\\section{Die Chiralitätslücke}','07_fields'),
 '08_rekonstruktion.tex':('\\section{Teilsysteme aus Beziehungen erkennen}','08_process'),
 '09_physik.tex':('\\section{Der präzise nächste Schritt: den Kegel aus der Ausbreitung gewinnen}','09_cone'),
 '10_ausblick.tex':('\\section{Ein priorisiertes, entscheidbares Anschlussprogramm}','10_fronts'),
 '13_schatten_quanten.tex':('\\section{Verschränkung legt die Zusammensetzung fest}','13_gaussian'),
 '14_schatten_dimension.tex':(None,'14_dimensions'),
}
for p in sorted((BASE/'chapters').glob('*.tex')):
    content=p.read_text()
    if p.name in placements:
        heading,name=placements[p.name]
        inclusion='\n\\input{revisions/'+name+'}\n'
        if heading is None:
            content+=inclusion
        else:
            if content.count(heading)!=1: raise RuntimeError('Ambiguous insertion '+p.name)
            content=content.replace(heading,heading+inclusion,1)
    # A second local integration belongs next to the existing cosmology table.
    if p.name=='09_physik.tex':
        h='\\section{Kosmologie und große Hierarchien}'
        content=content.replace(h,h+'\n\\input{revisions/09_cosmology}\n',1)
    for prefix in ['Aktueller Stand v','Aktueller Forschungsauftrag v']:
        content=content.replace(prefix,prefix.replace('Aktueller','Historischer'))
    (DST/'chapters'/p.name).write_text(content)
for p in BASE.glob('*.tex'):
    if p.name not in ['main.tex','update.tex']:
        shutil.copy2(p,DST/p.name)
main=(BASE/'main.tex').read_text()
for old,new in [
 ('Forschungsstand 14. September 2026','Forschungsstand 15. September 2026'),
 ('FORSCHUNGSBUCH · 14. SEPTEMBER 2026','FORSCHUNGSBUCH · 15. SEPTEMBER 2026'),
 ('vollstaendiges Hauptdokument v1.5','vollstaendiges Hauptdokument v1.6'),
 ('Version 1.5: Feste Ausfuehrung, exakte Symmetrie und kritische Dynamik','Version 1.6: Matrixordnung, native Operationen, Zustandsauswahl und vollstaendige Konsolidierung'),
 ('Version 1.5 · Vollständiges Hauptdokument','Version 1.6 · Vollständiges Hauptdokument'),
]: main=main.replace(old,new)
main=main.replace('\\section*{Wie man die Evidenz liest}', '\\input{front_v16}\n\\section*{Wie man die Evidenz liest}')
main=main.replace('\\section*{Umfang und Versionsgrenze}', '\\section*{Umfang und Versionsgrenze}\n\\begingroup\\small')
main=main.replace('\\tableofcontents','\\endgroup\n\\tableofcontents')
main=main.replace('\\appendix','\n'.join('\\input{chapters/'+n+'}' for n in [
    '26_v16_labor','27_v16_matrix','28_v16_operations','29_v16_state','30_v16_program'])+'\n\\appendix')
main=main.replace('\\end{document}','\\input{chapters/31_v16_evidence}\n\\end{document}')
(DST/'main.tex').write_text(main)
update=(BASE/'update.tex').read_text()
update=update.replace('v1.5','v1.6').replace('v1.4','v1.5').replace('14. September 2026','15. September 2026').replace('update_body_v15','update_body_v16')
(DST/'update.tex').write_text(update)
print('25 baseline chapters preserved; 13 context insertions; separate v1.6 main and update sources prepared.')
