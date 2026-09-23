"""Versioned full main + update + simple text and PDF, preserving prior history.

For these formula-heavy papers Pandoc/XeLaTeX is used rather than rasterizing
formulas in ReportLab. Python PDF validation uses the bundled runtime.
"""
from pathlib import Path
from hashlib import sha256
import subprocess
import json
import re
import os

HERE=Path(__file__).resolve().parent
OUT=HERE/'deliverables'
PDF=HERE/'output/pdf'
TEMP=HERE/'tmp/pdfs'
PREFIX='TFPT_Universalraum_Gemeinsamer_Prozess_'
SUFFIX='_2026-09-15_v1.6.8'
PANDOC=HERE.parent/'universalraum-singlet-observable-20260915/tmp/pandoc_runtime/pypandoc/files/pandoc'
FONTS='/Users/stefanhamann/.cache/codex-runtimes/codex-primary-runtime/dependencies/native/libreoffice-headless/libreoffice/LibreOfficeDev.app/Contents/Resources/fonts/truetype/'

def main():
    for p in (OUT,PDF,TEMP):p.mkdir(parents=True,exist_ok=True)
    replay=json.loads((HERE/'replay_manifest.json').read_text())
    if replay['status']!='PASS':raise RuntimeError('No successful replay')
    old=(HERE/'sources/baseline_v167.md').read_text()
    body=(HERE/'RESULTS.md').read_text()
    body+='\n\n---\n\n'+(HERE/'LATE_UPDATES.md').read_text()
    body+='\n\n### Automatisch aus dem abgeschlossenen Replay\n\n'
    body+='| Eigener Strang | Exakte Bedingungen | Numerische Bedingungen |\n|---|---:|---:|\n'
    for name,record in replay['reports'].items():
        body+=f"| {name} | {record['exact_checks']} | {record['numerical_checks']} |\n"
    body+=f"\nJe normalem und optimiertem Lauf: {replay['own_exact_checks_per_variant']} eigene exakte beziehungsweise faktische und {replay['own_numerical_checks_per_variant']} numerische Bedingungen. Die erste Kategorie enthält Quellenpins und Strukturprüfungen, nicht nur mathematische Identitäten. Hinzu kommen 17 erhaltene native Konstruktorguards und 1239 erhaltene Spurnetzwerk-Quellguards, separat 57 Synthese- und 20 historische Kettenbedingungen.\n"
    for label,path in [
        ('Teilbericht A: ursprünglicher Mechanismus und Referenzbilanz','agents/mechanism/REPORT.md'),
        ('Teilbericht B: vollständige innere Schattenkarte','agents/shadows/REPORT.md'),
        ('Teilbericht C: kausaler Eingriff','agents/causal/REPORT.md'),
        ('Teilbericht D: derselbe Dreizustandsraum für Schatten und Eingriff','agents/causal/ADDENDUM_COMMON3.md'),
        ('Nachtragsprüfung A: neue fünfte Norm und richtige Antwortzustände','agents/mechanism/LATE_A_AUDIT.md'),
        ('Nachtragsprüfung B: Feldprojektor und Lorentz-Händigkeit','agents/shadows/LATE_B_AUDIT.md'),
        ('Nachtragsprüfung C: fundamentale Reduktion und globale Quelle','agents/causal/LATE_C_AUDIT.md')]:
        body+='\n\n---\n\n# '+label+'\n\n'+(HERE/path).read_text()
    body+='\n\n---\n\n# Historischer Teil: vollständige Hauptfassung v1.6.7\n\n'
    body+=('Die folgende Fassung bleibt wortgetreu erhalten. Den aktuellen Stand liefern '
           'die vorangestellten Kapitel v1.6.8. Frühere Aussagen, Fragen und Vorhaben '
           'werden dadurch nicht rückwirkend neu bewiesen. Die neue Synthese ist separat '
           'vollständig im eingefrorenen Prüfpaket enthalten.\n\n')
    body+=old
    if old not in body:raise RuntimeError('Historical text lost')
    documents={'Konsolidierung':body,'Update':(HERE/'UPDATE.md').read_text(),
               'Einfach':(HERE/'EINFACH.md').read_text()}
    manifest={}
    env=dict(os.environ)
    env['PATH']='/Library/TeX/texbin:'+env.get('PATH','')
    for kind,text in documents.items():
        stem=PREFIX+kind+SUFFIX
        md=OUT/(stem+'.md');md.write_text(text)
        # Markdown source is byte-faithful. PDF typography normalizes exotic
        # dashes and the doubly-escaped math fences in the supplied chat paste.
        clean=text.replace('\u2011','-').replace('\u2013','-').replace('\u2014','-')
        clean=clean.replace('\\\\[','\\[').replace('\\\\]','\\]').replace('\\\\(','\\(').replace('\\\\)','\\)')
        source=TEMP/(stem+'.md');source.write_text(clean)
        tex=TEMP/(stem+'.tex')
        args=[str(PANDOC),str(source),'-f','markdown+tex_math_single_backslash+tex_math_dollars+pipe_tables',
              '-t','latex','-s','--syntax-highlighting=none','--lua-filter='+str(HERE/'pdf-code.lua'),
              '-H',str(HERE/'pdf-header.tex'),'-V','documentclass=article','-V','papersize=a4',
              '-V','geometry:margin=22mm','-V','fontsize=10pt','-V','mainfont=DejaVuSans',
              '-V','mainfontoptions=Path='+FONTS+',Extension=.ttf,BoldFont=DejaVuSans-Bold,ItalicFont=DejaVuSans-Oblique,BoldItalicFont=DejaVuSans-BoldOblique',
              '-V','monofont=DejaVuSansMono',
              '-V','monofontoptions=Path='+FONTS+',Extension=.ttf,BoldFont=DejaVuSansMono-Bold,ItalicFont=DejaVuSansMono-Oblique,BoldItalicFont=DejaVuSansMono-BoldOblique', '-V','colorlinks=true',
              '-M','lang=de-DE','-o',str(tex)]
        if kind=='Konsolidierung':args+=['--toc','--toc-depth=2']
        converted=subprocess.run(args,capture_output=True,env=env,timeout=120)
        (TEMP/(kind+'_pandoc.log')).write_bytes(converted.stdout+converted.stderr)
        if converted.returncode:raise RuntimeError(converted.stderr.decode())
        # Bare direct sums in supplied table cells otherwise form a single
        # unbreakable text word. Only the generated typography is changed.
        generated=tex.read_text().replace('⊕','⊕\\allowbreak{}')
        # Keep the complete historical heading in the body, but use a short
        # table-of-contents entry so its datestamp cannot collide with page 100+.
        generated=generated.replace('\\section{Zwischenbericht: TFPT/Universalraum - fundamentale Lösung,',
            '\\section[Historischer Zwischenbericht vom 15.09.2026]{Zwischenbericht: TFPT/Universalraum - fundamentale Lösung,')
        # This unbroken arithmetic string in the frozen report is typography,
        # not a prose word. Display it without changing the Markdown source.
        generated=generated.replace('4096−736=3360=(256−46)·16.',
            '\\[4096-736=3360=(256-46)\\cdot16.\\]')
        tex.write_text(generated)
        # Explicit compilation retains logs for overfull-box and missing-glyph QA.
        for run in range(6):
            proc=subprocess.run(['/Library/TeX/texbin/xelatex','-interaction=nonstopmode','-halt-on-error',
                                 '-output-directory',str(TEMP),str(tex)],capture_output=True,env=env,timeout=120)
            (TEMP/(kind+f'_xelatex_{run}.log')).write_bytes(proc.stdout+proc.stderr)
            if proc.returncode:raise RuntimeError(proc.stdout.decode(errors='replace')[-6500:])
            log=proc.stdout.decode(errors='replace')
            if run>=1 and 'Label(s) may have changed' not in log and 'Column widths have changed' not in log:
                break
        else:raise RuntimeError('PDF cross-references did not stabilize')
        target=PDF/(stem+'.pdf');target.write_bytes((TEMP/(stem+'.pdf')).read_bytes())
        manifest[kind]={'markdown':str(md.relative_to(HERE)),'pdf':str(target.relative_to(HERE)),
                        'md_sha256':sha256(md.read_bytes()).hexdigest(),'pdf_sha256':sha256(target.read_bytes()).hexdigest()}
    (HERE/'documents_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    print(json.dumps(manifest,indent=2))

if __name__=='__main__':main()
