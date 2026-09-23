"""Build, text-audit and render the paired research release; does not modify theory."""
from pathlib import Path
from collections import Counter
import subprocess, hashlib, json, re
from pypdf import PdfReader
from PIL import Image, ImageOps, ImageDraw
HERE=Path(__file__).resolve().parent
SRC=HERE/"main-v1.3"
OLD=HERE/"source-v1.1/TFPT_Universalraum_LaTeX_2026-09-14"
QA=HERE/"qa";QA.mkdir(exist_ok=True)
coverage=[]
heading=re.compile(r"\\(?:chapter|section|subsection)\*?\{([^\n]*)\}")
for f in sorted((OLD/"chapters").glob("*.tex")):
    old=f.read_text();new=(SRC/"chapters"/f.name).read_text()
    missing=list((Counter(heading.findall(old))-Counter(heading.findall(new))).elements())
    if missing:raise RuntimeError("missing original headings "+str((f.name,missing)))
    coverage.append({"file":f.name,"original_bytes":len(f.read_bytes()),
                     "current_bytes":len((SRC/"chapters"/f.name).read_bytes()),
                     "original_headings":len(heading.findall(old)),"missing_headings":missing,
                     "byte_unchanged":old==new})
for f in (OLD/"figures").iterdir():
    if f.read_bytes()!=(SRC/"figures"/f.name).read_bytes():raise RuntimeError("original figure changed "+f.name)
for doc in ["main","update"]:
    for run in range(3):
        proc=subprocess.run(["/Library/TeX/texbin/lualatex","-no-shell-escape","-interaction=nonstopmode","-halt-on-error",doc+".tex"],
                            cwd=SRC,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        (QA/(doc+"-build-"+str(run)+".log")).write_bytes(proc.stdout)
        if proc.returncode:raise RuntimeError("PDF build failed "+doc)
    log=(SRC/(doc+".log")).read_text()
    for marker in ["There were undefined references","Overfull \\hbox","Overfull \\vbox","Missing character:"]:
        if marker in log:raise RuntimeError(doc+" layout/reference issue: "+marker)
    reader=PdfReader(SRC/(doc+".pdf"))
    texts=[p.extract_text() or "" for p in reader.pages]
    if any("??" in t for t in texts):raise RuntimeError("unresolved PDF reference")
    if any(len(t.strip())<15 for t in texts):raise RuntimeError("empty PDF page")
    (QA/(doc+"_text.txt")).write_text("\n\n".join(texts))
    dest=QA/doc;dest.mkdir(exist_ok=True)
    subprocess.run(["/Users/stefanhamann/.cache/codex-runtimes/codex-primary-runtime/dependencies/bin/override/pdftoppm",
                    "-r","72","-png",str(SRC/(doc+".pdf")),str(dest/"page")],check=True)
    pages=sorted(dest.glob("page-*.png"))
    for k in range(0,len(pages),12):
        sheet=Image.new("RGB",(1200,1760),"#dddddd");draw=ImageDraw.Draw(sheet)
        for j,p in enumerate(pages[k:k+12]):
            im=Image.open(p).convert("RGB");im.thumbnail((386,410))
            x=(j%3)*400+(400-im.width)//2;y=(j//3)*440+22
            sheet.paste(im,(x,y));draw.text(((j%3)*400+12,(j//3)*440+4),p.stem,fill="black")
        sheet.save(QA/(doc+"-contact-"+str(k//12+1).zfill(2)+".png"))
    print(doc,len(reader.pages),"pages",flush=True)
manifest={
 "version":"1.3","base":"90-page main book v1.1, not compact compiler v1.2",
 "original_chapter_files":coverage,
 "original_main_chapters":21,"original_appendix_chapters":4,
 "all_original_figures_byte_preserved":True,
 "main_pages":len(PdfReader(SRC/"main.pdf").pages),"update_pages":len(PdfReader(SRC/"update.pdf").pages),
 "sources":{f.name:hashlib.sha256(f.read_bytes()).hexdigest()
            for f in sorted((HERE/"new-input-audit/sources").iterdir())},
 "pdfs":{name:hashlib.sha256((SRC/name).read_bytes()).hexdigest() for name in ["main.pdf","update.pdf"]},
 "checks":json.loads((HERE/"new-input-audit/replay.json").read_text()),
 "singlet":json.loads((HERE/"new-input-audit/singlet_f4.json").read_text()),
 "visual_review":"contact sheets and representative full pages pending human/model inspection"
}
(HERE/"release_manifest.json").write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+"\n")
print(json.dumps({k:v for k,v in manifest.items() if k in ["main_pages","update_pages","all_original_figures_byte_preserved"]}))

