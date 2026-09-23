"""Versioned full main, focused update and simple account; no overwrite of history."""
from pathlib import Path
from hashlib import sha256
import json
import os
import subprocess

HERE=Path(__file__).resolve().parent
OLD=HERE.parent/'universalraum-source-composition-20260915'
PANDOC=HERE.parent/'universalraum-singlet-observable-20260915/tmp/pandoc_runtime/pypandoc/files/pandoc'
FONTS='/Users/stefanhamann/.cache/codex-runtimes/codex-primary-runtime/dependencies/native/libreoffice-headless/libreoffice/LibreOfficeDev.app/Contents/Resources/fonts/truetype/'
OUT=HERE/'deliverables';PDF=HERE/'output/pdf';TMP=HERE/'tmp/pdfs'
BASE=OLD/'deliverables/TFPT_Universalraum_Quellkomposition_Konsolidierung_2026-09-15_v1.6.9.md'
PREFIX='TFPT_Universalraum_Spinlift_';SUFFIX='_2026-09-15_v1.6.10'


def main():
    for d in (OUT,PDF,TMP):d.mkdir(parents=True,exist_ok=True)
    replay=json.loads((HERE/'REPLAY.json').read_text())
    if replay['status']!='PASS':raise RuntimeError('no verified replay')
    verification=json.loads((HERE/'verification_normal.json').read_text())
    if sha256(BASE.read_bytes()).hexdigest()!='7a70b0a3c5cf1cc8861c3eeb5c328e7681e781da7d8c8ae9f0e527ed12b17a8d':
        raise RuntimeError('baseline differs from delivered v1.6.9')
    old=BASE.read_text()
    research=(HERE/'RESULTS.md').read_text()
    research+='\n\n### Abgeschlossener eigener Replay\n\n'
    research+=f"{verification['exact_checks']} explizite Bedingungen normal und optimiert, byteidentische Ergebnisdateien. Darin enthalten sind wiederholte Quellen-, Vorzeichen- und CAR-Prüfungen; die Zahl zählt keine unabhängigen Theoreme. Der allgemeine Grundzustands- und Antwortbeweis ist in Abschnitten 5-7 ausgeschrieben.\n"
    research+=f"Die Zusatzprüfung der beiden späten Perspektivtexte umfasst {replay['late_proposals']['normal']['exact_checks']} weitere Bedingungen, ebenfalls normal/optimiert byteidentisch. Ihre allgemeinen Voraussetzungen und Grenzen stehen in Abschnitt 14.\n"
    research+=f"Die anschließende Auswahlprüfung umfasst {replay['reflection_selection']['normal']['exact_checks']} weitere exakte Bedingungen; Gegenmodell und bedingter Spiegelungs-Auswahlsatz stehen in Abschnitt 15.\n"
    history='\n\n\\newpage\n\n# Historischer Bestand: vollständige Hauptfassung v1.6.9\n\n'
    history+='Die vorherige Hauptfassung folgt vollständig und unverändert. Ihr offener allgemeiner Quellen-/Grundzustandsstatus wird durch v1.6.10 nur für den vorn ausdrücklich definierten Viererzyklus und Kopplungsbereich ergänzt. Aussagen über N=64, g/Delta=1/20, Lorentzfelder und größere Systeme bleiben in ihrem ursprünglichen Vertrag. Die neue N=256-Konstruktion darf nicht rückwirkend in diese alten Sätze eingesetzt werden.\n\n'
    documents={'Hauptdokument':research+history+old,'Update':(HERE/'UPDATE.md').read_text(),'Einfach':(HERE/'EINFACH.md').read_text()}
    if old not in documents['Hauptdokument']:raise RuntimeError('lost baseline text')
    (TMP/'header.tex').write_text((OLD/'pdf-header.tex').read_text().replace('v1.6.9','v1.6.10'))
    manifest={}
    env=dict(os.environ);env['PATH']='/Library/TeX/texbin:'+env.get('PATH','')
    for kind,body in documents.items():
        stem=PREFIX+kind+SUFFIX
        md=OUT/(stem+'.md');md.write_text(body)
        clean=body.replace('\u2011','-').replace('\u2013','-').replace('\u2014','-')
        clean=clean.replace('\\\\[','\\[').replace('\\\\]','\\]').replace('\\\\(','\\(').replace('\\\\)','\\)')
        src=TMP/(stem+'.md');src.write_text(clean)
        tex=TMP/(stem+'.tex')
        args=[str(PANDOC),str(src),'-f','markdown+tex_math_single_backslash+tex_math_dollars+pipe_tables','-t','latex','-s',
              '--syntax-highlighting=none','--lua-filter='+str(OLD/'pdf-code.lua'),'-H',str(TMP/'header.tex'),
              '-V','documentclass=article','-V','papersize=a4','-V','geometry:margin=22mm','-V','fontsize=10pt',
              '-V','mainfont=DejaVuSans','-V','mainfontoptions=Path='+FONTS+',Extension=.ttf,BoldFont=DejaVuSans-Bold,ItalicFont=DejaVuSans-Oblique,BoldItalicFont=DejaVuSans-BoldOblique',
              '-V','monofont=DejaVuSansMono','-V','monofontoptions=Path='+FONTS+',Extension=.ttf,BoldFont=DejaVuSansMono-Bold,ItalicFont=DejaVuSansMono-Oblique,BoldItalicFont=DejaVuSansMono-BoldOblique',
              '-V','colorlinks=true','-M','lang=de-DE','-o',str(tex)]
        if kind=='Hauptdokument':args+=['--toc','--toc-depth=2']
        p=subprocess.run(args,capture_output=True,env=env,timeout=120)
        (TMP/(kind+'_pandoc.log')).write_bytes(p.stdout+p.stderr)
        if p.returncode:raise RuntimeError(p.stderr.decode())
        generated=tex.read_text().replace('⊕','⊕\\allowbreak{}')
        if kind=='Hauptdokument':generated=generated.replace('\\tableofcontents\n','\\tableofcontents\n\\clearpage\n')
        generated=generated.replace('\\section{Zwischenbericht: TFPT/Universalraum - fundamentale Lösung,',
          '\\section[Historischer Zwischenbericht vom 15.09.2026]{Zwischenbericht: TFPT/Universalraum - fundamentale Lösung,')
        generated=generated.replace('4096−736=3360=(256−46)·16.','\\[4096-736=3360=(256-46)\\cdot16.\\]')
        # The extended book exposes three legacy compound words in narrower
        # line/table positions. Discretionary breaks change typography only.
        for word,breakable in [('Ritz-Näherungszustand','Ritz-Nähe\\-rungs\\-zustand'),
                               ('Clock-Auslesung','Clock-Aus\\-le\\-sung'),
                               ('Ein-Kopie-Vektoransatz','Ein-Kopie-Vek\\-tor\\-ansatz')]:
            generated=generated.replace(word,breakable)
        tex.write_text(generated)
        for run in range(6):
            p=subprocess.run(['/Library/TeX/texbin/xelatex','-interaction=nonstopmode','-halt-on-error','-output-directory',str(TMP),str(tex)],capture_output=True,env=env,timeout=120)
            (TMP/(kind+f'_xelatex_{run}.log')).write_bytes(p.stdout+p.stderr)
            if p.returncode:raise RuntimeError(p.stdout.decode(errors='replace')[-6000:])
            log=p.stdout.decode(errors='replace')
            if run>=1 and 'Label(s) may have changed' not in log and 'Column widths have changed' not in log:break
        else:raise RuntimeError('references did not stabilize')
        if 'Overfull \\hbox' in log or 'Missing character:' in log:raise RuntimeError('PDF typography warning '+kind)
        pdf=PDF/(stem+'.pdf');pdf.write_bytes((TMP/(stem+'.pdf')).read_bytes())
        manifest[kind]={'markdown':str(md.relative_to(HERE)),'pdf':str(pdf.relative_to(HERE)),
                        'md_sha256':sha256(md.read_bytes()).hexdigest(),'pdf_sha256':sha256(pdf.read_bytes()).hexdigest()}
        print(kind+' built',flush=True)
    manifest['baseline']={'path':str(BASE),'sha256':sha256(BASE.read_bytes()).hexdigest(),'full_text_preserved':True}
    (HERE/'documents_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')


if __name__=='__main__':main()
