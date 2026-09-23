"""Build v1.5, require baseline coverage, render all pages, and emit provenance.

Run with the bundled document Python (pypdf/Pillow), LuaLaTeX and Poppler installed.
This builds documents; it does not rerun scientific checks or promote theory claims.
"""
from pathlib import Path
from collections import Counter
import subprocess, hashlib, json, re, shutil
from pypdf import PdfReader
from PIL import Image, ImageDraw

HERE = Path(__file__).resolve().parent
SRC = HERE / 'main-v1.5'
BASE = HERE.parent / 'universalraum-five-source-frontier-20260914' / 'main-v1.4'
QA = HERE / 'qa'
QA.mkdir(exist_ok=True)
LATEX = shutil.which('lualatex') or '/Library/TeX/texbin/lualatex'
POPPLER = shutil.which('pdftoppm') or '/Users/stefanhamann/.cache/codex-runtimes/codex-primary-runtime/dependencies/bin/override/pdftoppm'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
heading = re.compile(r'\\(?:chapter|section|subsection)\*?\{([^\n]*)\}')
coverage = []
for f in sorted((BASE / 'chapters').glob('*.tex')):
    current = SRC / 'chapters' / f.name
    old, new = f.read_text(), current.read_text()
    missing = list((Counter(heading.findall(old)) - Counter(heading.findall(new))).elements())
    if missing:
        raise RuntimeError('Missing baseline headings: ' + str((f.name, missing)))
    coverage.append(dict(file=f.name, baseline_sha256=sha(f), current_sha256=sha(current),
                         baseline_headings=len(heading.findall(old)), missing_headings=missing))
if not coverage:
    raise RuntimeError('Missing baseline chapter sources')
for f in sorted((BASE / 'figures').iterdir()):
    if f.is_file() and f.read_bytes() != (SRC / 'figures' / f.name).read_bytes():
        raise RuntimeError('Baseline figure changed: ' + f.name)
page_counts = {}
for name in ['main', 'update']:
    for run in range(3):
        result = subprocess.run([LATEX, '-no-shell-escape', '-interaction=nonstopmode',
                                 '-halt-on-error', name + '.tex'], cwd=SRC,
                                stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        (QA / f'{name}-build-{run}.log').write_bytes(result.stdout)
        if result.returncode:
            raise RuntimeError(f'{name}: build failed, see qa log')
    log = (SRC / (name + '.log')).read_text()
    for marker in ['There were undefined references', 'Overfull \\hbox',
                   'Overfull \\vbox', 'Missing character:']:
        if marker in log:
            raise RuntimeError(f'{name}: {marker}')
    reader = PdfReader(SRC / (name + '.pdf'))
    texts = [p.extract_text() or '' for p in reader.pages]
    if any('??' in t for t in texts) or any(len(t.strip()) < 15 for t in texts):
        raise RuntimeError(name + ': unresolved reference or blank page')
    page_counts[name] = len(texts)
    (QA / (name + '_text.txt')).write_text('\n\n'.join(texts))
    render_dir = QA / name
    render_dir.mkdir(exist_ok=True)
    subprocess.run([POPPLER, '-r', '72', '-png', str(SRC / (name + '.pdf')),
                    str(render_dir / 'page')], check=True)
    pages = sorted(render_dir.glob('page-*.png'))
    if len(pages) != len(texts):
        raise RuntimeError('Unexpected render page count')
    for offset in range(0, len(pages), 12):
        sheet = Image.new('RGB', (1200, 1760), '#dddddd')
        draw = ImageDraw.Draw(sheet)
        for j, p in enumerate(pages[offset:offset + 12]):
            im = Image.open(p).convert('RGB')
            im.thumbnail((386, 410))
            x = j % 3 * 400 + (400 - im.width) // 2
            y = j // 3 * 440 + 22
            sheet.paste(im, (x, y))
            draw.text((j % 3 * 400 + 12, j // 3 * 440 + 4), p.stem, fill='black')
        sheet.save(QA / f'{name}-contact-{offset // 12 + 1:02}.png')
    print(name, len(texts), 'pages', flush=True)
manifest = dict(
    version='1.5', baseline='complete main book v1.4, 126 pages',
    baseline_chapter_coverage=coverage, all_baseline_figures_byte_preserved=True,
    page_counts=page_counts,
    scientific_work_completed_before_pdf_authoring=True,
    source_hashes={p.name: sha(p) for p in sorted((HERE / 'sources').glob('N*.md'))},
    pdfs={n: sha(SRC / (n + '.pdf')) for n in ['main', 'update']},
    checks={name:json.loads((HERE / path).read_text()) for name,path in {
        'root':'root_replay.json','controls':'controls/verification.json',
        'scaling':'scaling/replay.json','quartet':'quartet/replay.json'}.items()},
    exact_spectral_certificate=json.loads((HERE / 'quartet/exact_polynomial.json').read_text()),
    T1_T8_closed=[], visual_review='pending rendered-page inspection')
(HERE / 'release_manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(page_counts))
