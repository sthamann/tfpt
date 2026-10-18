#!/usr/bin/env python3
"""One-shot mechanical extraction used for the documented 643a342 migration.

Module files retain original UTF-8 bytes, in order. The manifest stores only
hashes and spans. Later editing belongs in the modules; do not rerun this script
on already modular entry points. Use --check for ongoing structural integrity.
"""
from __future__ import annotations
from pathlib import Path
import hashlib,json,os,re,subprocess,sys
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'verification'))
from tex_sources import read_tex, TexSourceError


def digest(b):return hashlib.sha256(b).hexdigest()
def read(p):return p.read_bytes().decode('utf-8')
def conditional_depths(text):
    """TeX conditional depth at each line boundary, ignoring newif declarations.

    TeX does not expand input commands while skipping a false branch; therefore
    a matching fi must never be placed behind another module input. Macro-style
    tests taking brace arguments (etoolbox/ifthen) are not primitive conditionals.
    """
    macro_tests={r'\ifthenelse',r'\ifdef',r'\ifdefstring',r'\ifstrempty',r'\ifstrequal',r'\ifboolexpr',r'\ifblank',r'\ifcsdef',r'\ifnumcomp',r'\ifdimcomp',r'\ifnumequal',r'\ifdimequal',r'\ifnumless',r'\ifnumgreater',r'\ifdimless',r'\ifdimgreater',r'\ifbool',r'\iftoggle',r'\ifundef',r'\ifcsundef',r'\ifdefempty',r'\ifdefvoid',r'\ifcsempty',r'\ifcsvoid',r'\ifpatchable',r'\ifinlist',r'\ifinlistcs',r'\iff'}
    depth=0;result=[];skip_operands=0;newif=False;verbatim=None
    verbatim_names={'verbatim','verbatim*','Verbatim','MyVerbatim','lstlisting','minted','comment'}
    verbatim_names.update(re.findall(r'\\DefineVerbatimEnvironment\{([^{}]+)\}',text))
    for line in text.splitlines(keepends=True):
        result.append(depth)
        if verbatim:
            if '\\end{'+verbatim+'}' in line:verbatim=None
            continue
        block=re.search(r'\\begin\{([^{}]+)\}',line)
        if block and block[1] in verbatim_names:
            verbatim=block[1]
            if '\\end{'+verbatim+'}' in line:verbatim=None
            continue
        tokens=re.findall(r'\\(?:[A-Za-z@]+|.)|[{}%]|.',line)
        tokens=tokens[:tokens.index('%')] if '%' in tokens else tokens
        for token in tokens:
            if token.isspace():continue
            if newif:
                newif=False
                continue
            if skip_operands:
                skip_operands-=1
                continue
            if token==r'\newif':newif=True;continue
            if token==r'\fi':depth-=1;continue
            if token.startswith(r'\if') and token not in macro_tests:
                depth+=1
                if token in {r'\if',r'\ifx',r'\ifcat'}:skip_operands=2
                elif token==r'\ifdefined':skip_operands=1
    result.append(depth)
    return result

def safe_boundaries(text):
    lines=text.splitlines(keepends=True); brace=0;env=[];math=False;candidates={0};headings=set();conditional=conditional_depths(text)
    safe_env={'document','keybox','keyboxnb','winbox','winboxnb','gapbox','gapboxnb','navbox','auditbox','audbox','resbox','roadbox','itemize','enumerate','description','center','flushleft','flushright'}
    for i,line in enumerate(lines):
        tokens=re.findall(r'\\(?:[A-Za-z@]+|.)|[{}%]|.',line)
        tokens=tokens[:tokens.index('%')] if '%' in tokens else tokens
        clean=''.join(tokens)
        if brace==0 and conditional[i]==0 and not math and all(x in safe_env for x in env):
            if not line.strip() or re.match(r'\s*\\(?:part|chapter|(?:sub)*section)\*?(?:\[|\{)',line) or re.match(r'\s*\\(?:par\\smallskip\\noindent\\textbf|noindent\\textbf|emph)\{',line):candidates.add(i)
            if re.match(r'\s*\\(?:part|chapter|(?:sub)*section)\*?(?:\[|\{)',line):headings.add(i)
        for m in re.finditer(r'\\(begin|end)\{([^}]+)\}',clean):
            if m[1]=='begin':env.append(m[2])
            elif env and env[-1]==m[2]:env.pop()
        # Literal display delimiters cannot be crossed by a split.
        for tok in tokens:
            if tok in ('\\[','\\]'):math=tok=='\\['
        if clean.count('$$')%2:math=not math
        brace+=tokens.count('{')-tokens.count('}')
    candidates.add(len(lines));return lines,sorted(candidates),headings


def partitions(text):
    lines,candidates,headings=safe_boundaries(text);n=len(lines)
    begin=next((i for i,l in enumerate(lines) if re.search(r'\\begin\{document\}',l)),None)
    conditional=conditional_depths(text)
    if begin is not None and conditional[begin]:
        begin=next((i for i in candidates if i>begin and conditional[i]==0),None)
    if r'\ifdefined\ChangelogImported' in text:
        begin=next((i for i,l in enumerate(lines) if l.startswith(r'\subsection')),begin)
    ranges=[];start=0
    # Preamble remains a distinct original span; cross-file TeX groups are preserved.
    if begin and begin>0:ranges.append((0,begin,'preamble'));start=begin
    while start<n:
        if n-start<=440:end=n
        else:
            options=[x for x in candidates if start+180<=x<=start+420]
            preferred=[x for x in options if x in headings]
            if preferred:end=min(preferred,key=lambda x:abs(start+370-x))
            elif options:end=max(x for x in options if x<=start+400) if any(x<=start+400 for x in options) else min(options)
            else:end=next((x for x in candidates if x>start+400),n)
        if end<=start:raise RuntimeError('No forward safe partition')
        ranges.append((start,end,'body'));start=end
    # Avoid a tiny tail when it fits the same bounded source module.
    if len(ranges)>1 and ranges[-1][1]-ranges[-1][0]<70 and ranges[-2][2]=='body' and ranges[-1][1]-ranges[-2][0]<=480:
        ranges[-2]=(ranges[-2][0],ranges[-1][1],'body');ranges.pop()
    return lines,ranges


def doc_id(path):
    s=str(path.with_suffix('')).replace('_archive/','archive/').replace('/','--')
    return s


def split_document(rel,is_standalone):
    p=ROOT/rel;raw=p.read_bytes();text=raw.decode('utf-8');identifier=doc_id(Path(rel));directory=ROOT/'documents'/identifier
    if directory.exists():raise RuntimeError(f'Refuse to overwrite existing {directory}')
    directory.mkdir(parents=True);(directory/'sections').mkdir()
    compile_dir=p.parent if is_standalone else ROOT/'_archive/tfpt-45';lines,ranges=partitions(text);modules=[];includes=[];body_index=0
    offsets=[0]
    for line in lines:offsets.append(offsets[-1]+len(line.encode('utf-8')))
    for start,end,role in ranges:
        if role=='preamble':q=directory/'preamble.tex'
        else:
            body_index+=1
            first_heading=next((l.strip() for l in lines[start:end] if re.match(r'\\(?:part|chapter|(?:sub)*section)',l.strip())),None)
            slug=re.sub(r'[^a-z0-9]+','-',(first_heading or 'source').lower()).strip('-')[:56]
            q=directory/'sections'/f'{body_index:03d}-{slug}.tex'
        payload=''.join(lines[start:end]).encode('utf-8');q.write_bytes(payload)
        inc=os.path.relpath(q,compile_dir).replace(os.sep,'/');includes.append('\\input{'+inc+'}')
        modules.append({'path':q.relative_to(ROOT).as_posix(),'role':role,'original_path':rel,'original_line_start':start+1,'original_line_end':end,'original_byte_start':offsets[start],'original_byte_end':offsets[end],'bytes':len(payload),'sha256':digest(payload)})
    main=directory/'main.tex';main.write_text(''.join(includes),encoding='utf-8')
    # No added newline/comment: literal expansion must reconstruct original bytes.
    wrapper='\\input{'+os.path.relpath(main,compile_dir).replace(os.sep,'/')+'}'
    if digest(b''.join((ROOT/m['path']).read_bytes() for m in modules))!=digest(raw):raise RuntimeError('Raw source reconstruction failed before replacing '+rel)
    p.write_text(wrapper,encoding='utf-8')
    return {'id':identifier,'entry_point':rel,'compile_dir':compile_dir.relative_to(ROOT).as_posix(),'standalone':is_standalone,'original_bytes':len(raw),'original_lines':len(lines),'original_sha256':digest(raw),'main':main.relative_to(ROOT).as_posix(),'wrapper_sha256':digest(wrapper.encode()),'source_modules':modules}


def main():
    manifest_path=ROOT/'documents/source_manifest.json'
    if '--check' in sys.argv:
        manifest=json.loads(manifest_path.read_text());bad=[]
        for doc in manifest['documents']:
            payload=b''.join((ROOT/m['path']).read_bytes() for m in doc['source_modules'])
            if digest(payload)!=doc['original_sha256']:bad.append(doc['entry_point']+': original source content changed')
            baseline=doc.get('expanded_before_sha256')
            if baseline:
                try:now=digest(read_tex(ROOT/doc['entry_point'], compile_dir=ROOT/doc['compile_dir']).encode('utf-8'))
                except TexSourceError as e:bad.append(str(e));continue
                if now!=baseline:bad.append(doc['entry_point']+': expanded source changed')
        print(json.dumps({'documents_checked':len(manifest['documents']),'failures':bad},indent=2));return int(bool(bad))
    if manifest_path.exists():raise RuntimeError('Manifest exists: migration is one-shot; use --check')
    tracked=subprocess.check_output(['git','ls-files','*.tex'],cwd=ROOT,text=True).splitlines();inventory=[];selected=[]
    snapshot_markers=['/source-snapshots/','/sources/input_','/context/','/external/exchange/source/','/universalraum-native-exterior-reset-20260915/sources/']
    for rel in tracked:
        p=ROOT/rel;text=read(p);standalone=bool(re.search(r'(?m)^\s*\\documentclass(?:\[|\{)',text))
        if not standalone:continue
        size=p.stat().st_size;series=bool(re.match(r'_archive/tfpt-45/0[0-7]_',rel));frozen=any(m in '/'+rel for m in snapshot_markers)
        selected_now=(size>=20000 or series or '/' not in rel) and not frozen
        reason='modularized authored standalone' if selected_now else ('immutable historical/source snapshot; bytes preserved' if frozen else 'short existing standalone below 20KB; left intact')
        inventory.append({'entry_point':rel,'bytes':size,'sha256':digest(p.read_bytes()),'selected':selected_now,'reason':reason})
        if selected_now:selected.append((rel,True))
    # Long original source fragments behind the archived series are owned content too.
    for p in sorted((ROOT/'_archive/tfpt-45/source_extracts').glob('*.tex')):
        if p.stat().st_size>=20000:selected.append((p.relative_to(ROOT).as_posix(),False))
    # Capture expanded baselines before ANY wrapper replacement, including shared dependencies.
    baselines={}
    for rel,standalone in selected:
        try:baselines[rel]={'expanded_before_sha256':digest(read_tex(ROOT/rel).encode('utf-8'))}
        except TexSourceError as e:baselines[rel]={'preexisting_expansion_error':str(e)}
    documents=[split_document(rel,standalone) for rel,standalone in selected]
    for d in documents:d.update(baselines[d['entry_point']])
    manifest={'schema_version':1,'source_commit':'643a3421017524d626457a2598403e6c1a7c801d','method':'Exact contiguous UTF-8 source spans, no new scientific content; original input order and compile directory retained. Module input directives contain no synthesized whitespace.','target_lines':400,'documents':documents}
    manifest_path.write_text(json.dumps(manifest,indent=2)+'\n');(ROOT/'documents/standalone_inventory.json').write_text(json.dumps({'source_commit':manifest['source_commit'],'documents':inventory},indent=2)+'\n')
    print('Modularized',len(documents),'sources;',sum(len(d['source_modules']) for d in documents),'exact original modules; inventory',len(inventory),'standalones')
    return main_check()


def main_check():
    # Repeat the exact-preservation check only after all nested source fragments moved.
    sys.argv.append('--check');return main()

if __name__=='__main__':raise SystemExit(main())
