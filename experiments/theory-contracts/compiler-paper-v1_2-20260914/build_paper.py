"""Build the integrated German research manuscript with ReportLab.

First run paper_checks.py with a scientific Python environment for numbers/math.
This renderer needs reportlab, Pillow and pypdf (bundled Codex runtime).
"""
from pathlib import Path
import hashlib
import html
import json
import os
import re
import subprocess

from PIL import Image as PILImage
from reportlab.lib import colors
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, Frame, PageTemplate, Paragraph,
                                Spacer, Image, LongTable, TableStyle, PageBreak, KeepTogether)
from reportlab.platypus.tableofcontents import TableOfContents
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[3]
DATE = '2026-09-14'
if not re.fullmatch(r'\d{4}-\d{2}-\d{2}',DATE):
    raise ValueError('invalid paper date')
SOURCE = ROOT/'docs/TFPT_COMPILER_UNIVERSALRAUM_PAPER_2026-09-14_v1.2.md'
OUT = ROOT/'output/pdf'
ASSETS = ROOT/f'tmp/pdfs/tfpt_compiler_universalraum_20260914_v1_2'
PDF = OUT/f'tfpt_compiler_universalraum_2026-09-14_v1.2.pdf'
WIDTH, HEIGHT = A4
MARGIN = 52
TEXTWIDTH = WIDTH-2*MARGIN
NAVY = colors.HexColor('#17354b')
TEAL = colors.HexColor('#267d84')


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def inline(text):
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'\1', text)
    text = text.replace('`', '')
    text = html.escape(text)
    text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)
    text = re.sub(r'(https?://[^\s]+)', r'<link href="\1" color="#267d84">\1</link>', text)
    return text


class PaperDoc(BaseDocTemplate):
    def afterFlowable(self, flowable):
        if isinstance(flowable, Paragraph) and flowable.style.name == 'Section':
            title = flowable.getPlainText()
            key = 'section-'+hashlib.sha1(title.encode()).hexdigest()[:10]
            self.canv.bookmarkPage(key)
            self.canv.addOutlineEntry(title, key, 0)
            self.notify('TOCEntry', (0, title, self.page, key))


def furniture(canvas, doc):
    canvas.saveState()
    if doc.page > 1:
        canvas.setFont('Body',8)
        canvas.setFillColor(NAVY)
        canvas.drawString(MARGIN, HEIGHT-30, 'TFPT · Compiler, Clocks und Universalraum')
        canvas.setStrokeColor(colors.HexColor('#b6cbce'))
        canvas.line(MARGIN, HEIGHT-37, WIDTH-MARGIN, HEIGHT-37)
    canvas.setFont('Body',8)
    canvas.setFillColor(colors.HexColor('#60717d'))
    canvas.drawString(MARGIN, 27, f'Forschungsmanuskript · {DATE} · Physikalischer Abschluss offen')
    canvas.drawRightString(WIDTH-MARGIN,27,str(doc.page))
    canvas.restoreState()


def main():
    fonts = json.loads((ASSETS/'fonts.json').read_text())
    pdfmetrics.registerFont(TTFont('Body',fonts['body']))
    pdfmetrics.registerFont(TTFont('BodyBold',fonts['bold']))
    pdfmetrics.registerFontFamily('Body',normal='Body',bold='BodyBold',italic='Body',boldItalic='BodyBold')
    body = ParagraphStyle('Body',fontName='Body',fontSize=10.1,leading=15.3,
                          textColor=colors.HexColor('#23313b'),spaceAfter=9,
                          alignment=TA_JUSTIFY,splitLongWords=True,allowWidows=0,allowOrphans=0)
    section = ParagraphStyle('Section',parent=body,fontName='BodyBold',fontSize=16,
                             leading=21,textColor=NAVY,spaceBefore=19,spaceAfter=12,
                             keepWithNext=True,alignment=0)
    sub = ParagraphStyle('Sub',parent=section,fontSize=12,leading=17)
    cell = ParagraphStyle('Cell',parent=body,fontSize=8.4,leading=11.8,spaceAfter=0,alignment=0)
    title = ParagraphStyle('Title',parent=section,fontSize=27,leading=34,spaceBefore=55)
    subtitle = ParagraphStyle('Subtitle',parent=body,fontSize=14,leading=21,textColor=TEAL,alignment=0)
    story = []
    lines = SOURCE.read_text().splitlines()
    index = 0
    equation_index = 0
    while index < len(lines):
        line = lines[index].strip()
        if not line:
            index += 1
            continue
        if line.startswith('# '):
            story += [Paragraph(inline(line[2:]),title),Spacer(1,18)]
        elif line.startswith('## Eine integrierte'):
            story += [Paragraph(inline(line[3:]),subtitle),Spacer(1,26)]
        elif line.startswith('### Zusammenfassung'):
            story += [PageBreak(),Paragraph('Zusammenfassung',section)]
        elif line.startswith('## 1.'):
            story += [PageBreak(),Paragraph('Inhalt',sub)]
            toc = TableOfContents()
            toc.tableStyle = TableStyle([('TOPPADDING',(0,0),(-1,-1),0),('BOTTOMPADDING',(0,0),(-1,-1),0)])
            toc.levelStyles = [ParagraphStyle('TOC',fontName='Body',fontSize=9,leading=12,spaceBefore=2)]
            story += [toc,PageBreak(),Paragraph(inline(line[3:]),section)]
        elif line.startswith('## '):
            story.append(Paragraph(inline(line[3:]),section))
        elif line.startswith('### '):
            story.append(Paragraph(inline(line[4:]),sub))
        elif line.startswith('$$'):
            path = ASSETS/f'equation_{equation_index:02}.png'
            with PILImage.open(path) as img:
                w,h = img.size
            scale = min(72/230, (TEXTWIDTH-12)/w)
            story += [Spacer(1,4),Image(str(path),width=w*scale,height=h*scale),Spacer(1,12)]
            equation_index += 1
        elif line.startswith('|') and line.endswith('|'):
            rows = []
            while index < len(lines) and lines[index].strip().startswith('|') and lines[index].strip().endswith('|'):
                row = [x.strip() for x in lines[index].strip().strip('|').split('|')]
                if not all(re.fullmatch(r'[-: ]+',x) for x in row):
                    rows.append(row)
                index += 1
            n = len(rows[0])
            if rows[0][0] == 'Größe':
                ratios = [.18,.26,.20,.36]
            elif rows[0][0] == 'Tor':
                ratios = [.14,.39,.47]
            else:
                ratios = ([.25,.34,.41] if n == 3 else [1/n]*n)
            data = [[Paragraph(('<b>'+inline(x)+'</b>') if j == 0 else inline(x),cell)
                     for x in row] for j,row in enumerate(rows)]
            table = LongTable(data,colWidths=[TEXTWIDTH*x for x in ratios],repeatRows=1,hAlign='LEFT')
            table.setStyle(TableStyle([
                ('BACKGROUND',(0,0),(-1,0),colors.HexColor('#dcebed')),
                ('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,colors.HexColor('#f3f6f7')]),
                ('VALIGN',(0,0),(-1,-1),'TOP'),
                ('LEFTPADDING',(0,0),(-1,-1),7),('RIGHTPADDING',(0,0),(-1,-1),7),
                ('TOPPADDING',(0,0),(-1,-1),7),('BOTTOMPADDING',(0,0),(-1,-1),7),
                ('LINEBELOW',(0,0),(-1,0),.8,TEAL)]))
            story += [Spacer(1,5),KeepTogether([table]) if len(rows)<=5 else table,Spacer(1,14)]
            continue
        else:
            para = [line[2:] if line.startswith('- ') else line]
            while index+1 < len(lines) and lines[index+1].strip() and not lines[index+1].startswith(('#','|','$$','- ')):
                index += 1
                para.append(lines[index].strip())
            story.append(Paragraph(inline(' '.join(para)),body))
        index += 1
    doc = PaperDoc(str(PDF),pagesize=A4,leftMargin=MARGIN,rightMargin=MARGIN,
                   topMargin=53,bottomMargin=49,title='TFPT: Vom geometrischen Compiler zum Prozess mit Aufzeichnung',
                   author='TFPT Forschungsprojekt; Synthese mit Codex')
    frame = Frame(MARGIN,49,TEXTWIDTH,HEIGHT-102,id='main',leftPadding=0,rightPadding=0,topPadding=0,bottomPadding=0)
    doc.addPageTemplates(PageTemplate(id='paper',frames=frame,onPage=furniture))
    doc.multiBuild(story)
    reader = PdfReader(PDF)
    extracted = '\n'.join(p.extract_text() or '' for p in reader.pages)
    for required in ('Zusammenfassung','T1','T8','Anhang A','Reproduktion','Aufzeichnungen'):
        if required not in extracted:
            raise ValueError('missing PDF content: '+required)
    (ASSETS/'extracted.txt').write_text(extracted)
    pins = [
        'origin_theory.tex','tfpt_1_architecture_e8.tex','tfpt_2_standard_model.tex',
        'verification/tfpt_constants.py','predictions.txt','verification/status_ledger.csv',
        'docs/OPEN_PROBLEMS.md','experiments/theory-contracts/RESEARCH_2026-09-09.md',
        'docs/TFPT_UNIVERSALRAUM_SYNTHESIS_2026-09-12.md',
        'docs/TFPT_DREI_FEHLENDE_BEZIEHUNGEN_2026-09-12.md',
        'verification/v783_two_qubit_clifford.py','verification/v752_projective_hamming_incidence.py']
    here = Path(__file__).resolve().parent
    pins += [str(p.relative_to(ROOT)) for p in here.iterdir() if p.suffix in ('.py','.md','.json')]
    pins += [str(SOURCE.relative_to(ROOT))]
    if DATE == '2026-09-14':
        extension=ROOT/'experiments/theory-contracts/compiler-extension-audit-20260914'
        pins += [str(p.relative_to(ROOT)) for p in extension.iterdir() if p.suffix in ('.py','.md','.json')]
    origin=ROOT/'experiments/theory-contracts/compiler-origin-audit-20260913'
    pins += [str(p.relative_to(ROOT)) for p in origin.iterdir() if p.suffix in ('.py','.md','.json')]
    audit=ROOT/'experiments/theory-contracts/universalraum-six-source-audit-20260914'
    pins += [str(p.relative_to(ROOT)) for p in audit.rglob('*') if p.is_file() and p.suffix in ('.py','.md','.json')]
    pins += ['docs/TFPT_COMPILER_UNIVERSALRAUM_PAPER_2026-09-14.md', 'docs/TFPT_UNIVERSALRAUM_SECHS_QUELLEN_KONSOLIDIERUNG_2026-09-14.md']
    sessions=ROOT/'experiments/theory-contracts/primitive-transfer-selection-20260912/synthesis-20260912'
    pins += [str((sessions/f'session-{i}.md').relative_to(ROOT)) for i in range(1,5)
             if (sessions/f'session-{i}.md').exists()]
    manifest = {
        'version':'1.2',
        'scope':'Integrated manuscript and formula checks; no TOE closure, no full Lean or session replay',
        'base_commit':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),
        'dirty_worktree':True,'sources_sha256':{p:sha(ROOT/p) for p in sorted(set(pins))},
        'pdf_sha256':sha(PDF),'pdf_pages':len(reader.pages),'display_equations':equation_index,
        'new_checks_report_sha256':sha(OUT/f'tfpt_compiler_universalraum_2026-09-14_v1.2_numbers.json'),
        'T1_T8_closed':[]}
    (OUT/f'tfpt_compiler_universalraum_2026-09-14_v1.2_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    print(json.dumps({'pdf':str(PDF),'pages':len(reader.pages),'equations':equation_index,'text_characters':len(extracted)}))


if __name__ == '__main__':
    main()
