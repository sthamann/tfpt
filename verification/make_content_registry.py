#!/usr/bin/env python3
"""Deterministic physical-source registry for the complete authored TeX corpus.

This is a static navigation index, not a TeX interpreter or proof checker.
Public input = tracked TeX + explicit modular sources. Gitless exports use the
shipped source_inventory.json. --include-local writes a separate ignored view.
Only explicit source tokens form citation edges; lexical topics and joins are
labelled separately. Status text is copied from the original claim ledger.
"""
from __future__ import annotations

import argparse
from bisect import bisect_right
from collections import Counter, defaultdict
import csv
import fnmatch
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys

from tex_sources import dependency_paths, literal_includes, source_chunks, TexSourceError

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "docs/registry"
CONFIG = OUT / "config.json"
HEADINGS = re.compile(r"\\(part|chapter|section|subsection|subsubsection|paragraph|subparagraph)\*?\s*(?:\[[^\]\n]*\]\s*)?\{")
FILE_TOKEN = re.compile(r"(?<![\w])(?:[\w.+-]+/)*[\w.+-]+\.(?:py|lean|wl|wls|md|json|csv|txt)(?![\w])")
SHORT_V = re.compile(r"(?<![\w])v(\d{1,5})(?![\w.])")
DECL = re.compile(r"^\s*(?:(?:private|protected|noncomputable|unsafe|partial)\s+)*(theorem|lemma|def|abbrev|axiom|opaque|structure|class|inductive|instance)\s+([\w'.]+)", re.M)
WL_HEADING = re.compile(r"^\s*\(\*\s*(?:[-=]+\s*)?\(?v\d+[^\n]*(?:\n(?:(?!\*\)).)*?)*?\*\)", re.M)
RELATION_KINDS = {
    "explicit_file_citation", "explicit_script_identifier", "explicit_claim_identifier",
    "explicit_lean_symbol", "explicit_source_identifier", "cross_reference_join",
    "tex_label_reference", "includes_source", "contains_declaration",
}


def dumps(value):
    return json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n"


def digest(data):
    if isinstance(data, str): data = data.encode("utf-8")
    return hashlib.sha256(data).hexdigest()


def rel(path):
    return Path(path).resolve().relative_to(ROOT.resolve()).as_posix()


def git_files(*patterns, untracked=False, deleted=False):
    args = ["git", "-C", str(ROOT), "ls-files", "-z"]
    if untracked: args += ["--others", "--exclude-standard"]
    if deleted: args += ["--deleted"]
    args += ["--", *patterns]
    try:
        return sorted(x for x in subprocess.check_output(args, stderr=subprocess.DEVNULL).decode().split("\0") if x)
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None


def is_git_root():
    marker=ROOT/".tfpt-shadow-export"
    if marker.is_file():
        try:state=json.loads(marker.read_text())
        except (OSError,ValueError)as error:raise ValueError("Invalid shadow export ownership marker")from error
        if not isinstance(state,dict)or state.get("owner")!="tfpt-shadow-export"or state.get("source_repository")!="sthamann/tfpt":
            raise ValueError("Unrecognized shadow export ownership marker")
        # The destination's old Git index predates the files just exported.
        # The shipped source inventory owns this tree, including before git add.
        return False
    return (ROOT / ".git").exists()


def allowed(path, config):
    p = Path(path)
    return not p.is_absolute() and not any(part in config["excluded_components"] for part in p.parts) and ".." not in p.parts and not any(p.as_posix()==v or p.as_posix().startswith(v+"/") for v in config.get("vendor_roots",[]))


def research_evidence_paths(paths, config, local_deleted_paths=(), registered_scripts=(), omissions=None):
    """Use the same research scope in Git and exports; missing sources fail."""
    excluded=config.get("excluded_evidence_roots",["website"])
    selected=sorted({p for p in paths if allowed(p,config)and not any(p==root or p.startswith(root+"/")for root in excluded)})
    missing=[p for p in selected if not(ROOT/p).is_file()]
    canonical={"verification/"+name+".py"for name in registered_scripts}
    local_omissions=[p for p in missing if p in local_deleted_paths and p not in canonical and not p.endswith((".lean",".wl",".wls",".tex")) and p not in {"verification/script_registry.csv","verification/status_ledger.csv"}]
    if omissions is not None:
        omissions.extend({"kind":"local_missing_noncanonical_evidence","source":p,"reason":"Git-declared working-tree deletion; omitted only from the local supplement, never the public registry or Gitless export","current_proof_coverage":False}for p in local_omissions)
    missing=[p for p in missing if p not in local_omissions]
    if missing:raise ValueError("Missing declared research evidence sources: "+", ".join(missing))
    return [p for p in selected if p not in local_omissions]


def historical_snapshot_info(path, provenance=None):
    """Classify replay bytes without importing their old ledger/script status."""
    if not path.startswith("verification/historical_replay/"):
        return None
    provenance=provenance or {}
    return {"role":"historical_snapshot","claim_ids":[],
            "ledger_status_not_inherited":True,"current_proof_coverage":False,
            "ownership":{"owner":"TFPT historical replay inputs",
                         "relation":"Frozen compatibility source; not the current verification module or active claim ledger"},
            "historical_provenance_as_recorded":{
                key:provenance[key] for key in ("kind","path","historical_sha256","historical_source_commit") if key in provenance}}


def manifest_paths(config):
    path = ROOT / config["module_manifest"]
    if not path.exists(): return set()
    data = json.loads(path.read_text())
    result = set()
    def visit(value):
        if isinstance(value, str) and value.endswith(".tex") and allowed(value, config) and (ROOT / value).is_file():
            result.add(value)
        elif isinstance(value, dict):
            for child in value.values(): visit(child)
        elif isinstance(value, list):
            for child in value: visit(child)
    visit(data)
    return result


def discover(config, include_local=False):
    if is_git_root():
        # The module manifest is authoritative during a rename even before
        # staging; retired generated module paths must not survive as owners.
        public = {p for p in (git_files("*.tex") or []) if not p.startswith("documents/")}
    else:
        inventory = OUT / "source_inventory.json"
        if not inventory.exists():
            raise ValueError("Gitless export requires docs/registry/source_inventory.json; refusing an unscoped filesystem scan")
        public = set(json.loads(inventory.read_text())["tex_sources"])
    public |= manifest_paths(config)
    public |= {p for p in config.get("explicit_public_sources", []) if (ROOT / p).is_file()}
    public = {p for p in public if allowed(p, config)}
    missing = sorted(p for p in public if not (ROOT / p).is_file())
    if missing: raise ValueError("Missing public TeX sources: " + ", ".join(missing))
    if include_local:
        candidates = git_files("*.tex", untracked=True)
        if candidates is None: raise ValueError("--include-local requires a Git checkout")
        def local_root(p):
            if "/" not in p: return "." in config["local_authored_roots"]
            return p.split("/", 1)[0] in config["local_authored_roots"]
        local={p for p in candidates if p not in public and allowed(p, config) and local_root(p)}
        local_config={**config,"module_manifest":"documents/local/source_manifest.json"}
        local|=manifest_paths(local_config)
        return sorted(p for p in local if p not in public), sorted(public)
    return sorted(public), sorted(public)


def mask_tex_comments(text):
    """Remove comments without moving offsets/line numbers; escaped percent stays."""
    out=list(text);position=0
    while position<len(text):
        if text[position]!="%":position+=1;continue
        backslashes=0;before=position-1
        while before>=0 and text[before]=="\\":backslashes+=1;before-=1
        if backslashes%2:position+=1;continue
        end=text.find("\n",position)
        if end<0:end=len(text)
        out[position:end]=" "*(end-position);position=end
    return "".join(out)


def mask_lean_comments(text):
    out = list(text); i = 0; depth = 0; string = False
    while i < len(text):
        if depth:
            if text.startswith("/-", i):
                out[i:i+2] = "  "; depth += 1; i += 2; continue
            if text.startswith("-/", i):
                out[i:i+2] = "  "; depth -= 1; i += 2; continue
            if text[i] != "\n": out[i] = " "
            i += 1; continue
        if not string and text.startswith("--", i):
            end = text.find("\n", i)
            if end < 0: end = len(text)
            out[i:end] = " " * (end-i); i = end; continue
        if not string and text.startswith("/-", i):
            out[i:i+2] = "  "; depth = 1; i += 2; continue
        if text[i] == '"' and (i == 0 or text[i-1] != "\\"): string = not string
        i += 1
    return "".join(out)


def braced(text, start):
    depth = 0
    for i in range(start, len(text)):
        if text[i] in "{}" and (i == 0 or text[i-1] != "\\"):
            depth += 1 if text[i] == "{" else -1
            if depth == 0: return text[start+1:i], i+1
    raise ValueError("Unbalanced literal brace group")


def normalize_refs(text):
    return re.sub(r"\\(?:allowbreak|discretionary)\b[ \t]*", "", mask_tex_comments(text)).replace("\\_", "_").replace("\\-", "")


def file_citations(text):
    """Yield filename tokens and original line offsets, including split texttt."""
    masked=normalize_refs(text);spans=[]
    for match in re.finditer(r"\\(?:texttt|path|nolinkurl|url|detokenize)\s*\{",masked):
        try:body,end=braced(masked,match.end()-1)
        except ValueError:continue
        flat=re.sub(r"\\[A-Za-z@]+\b", "", body)
        flat="".join(flat.replace("{", "").replace("}", "").split())
        tokens=list(FILE_TOKEN.finditer(flat))
        if tokens:
            spans.append((match.start(),end))
            for token in tokens:yield token[0],masked.count("\n",0,match.start())
    for match in FILE_TOKEN.finditer(masked):
        if not any(start<=match.start()<end for start,end in spans):
            yield match[0],masked.count("\n",0,match.start())


def plain_tex(text):
    text = mask_tex_comments(text)
    # Never flatten a fraction or a superscript into a different number/claim.
    # Display excerpts omit formula spans explicitly; exact raw source is linked.
    text = re.sub(r"(?<!\\)\$\$?[\s\S]*?(?<!\\)\$\$?|\\\([\s\S]*?\\\)|\\\[[\s\S]*?\\\]", " [formula in source] ", text)
    text = re.sub(r"\\(?:[dt]?frac|sqrt)\s*\{[^{}]*\}(?:\s*\{[^{}]*\})?", " [formula in source] ", text)
    text = re.sub(r"\\begin\{(equation\*?|align\*?|tikzpicture|lstlisting|verbatim|minted)\}[\s\S]*?\\end\{\1\}", " ", text)
    text = re.sub(r"\\(?:documentclass|usepackage|input|include|label|ref|eqref|pageref|bibliography|bibliographystyle|newcommand|renewcommand|providecommand|def|definecolor|setlength|setcounter|addtocounter|hypersetup|tikzset|titleformat|pagestyle|geometry)\b[^\n]*", " ", text)
    text = re.sub(r"\\(?:begin|end)\{[^}]+\}(?:\[[^\]]*\])?", " ", text)
    text = text.replace("\\_", "_").replace("~", " ").replace("---", "—").replace("--", "–")
    text = re.sub(r"\\(?:[A-Za-z@]+)\*?(?:\[[^\]]*\])?", " ", text)
    return " ".join(text.replace("{", "").replace("}", "").replace("$", "").split())


def opening_excerpt(text):
    clean = mask_tex_comments(text)
    for block in re.split(r"\n\s*\n", clean):
        prose = plain_tex(block)
        words = re.findall(r"[A-Za-zÀ-ž]{3,}", prose)
        if len(words) >= 7 and not re.match(r"^(?:tikz|pgf|font|fontenc|T1\b|utf8\b)", prose):
            return prose[:420], "opening prose excerpt; TeX formatting stripped and formulas explicitly omitted; no semantic paraphrase"
    return "", "no sufficiently long opening prose found; support/formula-only content is not paraphrased"


def pure_wrapper(text):
    masked=mask_tex_comments(text)
    for start,end,_ in reversed(literal_includes(text)):
        masked=masked[:start]+" "*(end-start)+masked[end:]
    return bool(literal_includes(text)) and not masked.strip()


def source_role(path, config, text):
    if path in config["generated_tex"]: return "generated"
    if path.startswith("_archive/"): return "archive"
    if path.startswith("documents/"):
        return "module_preamble" if path.endswith("/preamble.tex") else "module_entry" if path.endswith("/main.tex") else "module_fragment"
    if path in config["active_entry_points"]:
        return "active_wrapper" if pure_wrapper(text) else "active_document"
    if path.startswith("tex-artefacts/"):
        return "research_fragment" if re.search(r"^\\(?:section|subsection)", text, re.M) else "shared_support"
    if path.startswith("experiments/"): return "exploration"
    return "research_document" if "\\documentclass" in mask_tex_comments(text) else "support"


def file_info(path):
    data = (ROOT / path).read_bytes()
    return {"path": path, "sha256": digest(data), "bytes": len(data), "line_count": max(1, len(data.decode("utf-8", errors="replace").splitlines()))}


def resolve_include(raw, path, available, compile_dir=None):
    if Path(raw).is_absolute(): return None
    candidates = []
    for parent in [compile_dir or str(Path(path).parent), str(Path(path).parent), "."]:
        for name in [raw, raw + ".tex"]:
            candidate=(ROOT/parent/name).resolve()
            if candidate.is_relative_to(ROOT.resolve()):candidates.append(candidate.relative_to(ROOT.resolve()).as_posix())
    return next((p for p in candidates if p in available), None)


def parse_tex(path, config):
    text = (ROOT/path).read_text(encoding="utf-8")
    masked = mask_tex_comments(text)
    row = file_info(path)
    row.update(id="tex:"+path, role=source_role(path, config, text), owner_documents=[], primary_owner=None,
               section_ids=[], includes=[], title="", title_latex="", alias_of=None, is_wrapper=pure_wrapper(text))
    title = re.search(r"\\title(?:\[[^\]]*\])?\s*\{", masked)
    if title:
        try:
            row["title_latex"]=braced(masked,title.end()-1)[0]
            row["title"]=plain_tex(row["title_latex"])
        except ValueError: pass
    if row["is_wrapper"]:
        return row,[],text
    marks = []
    for m in HEADINGS.finditer(masked):
        try: title, end = braced(masked, m.end()-1)
        except ValueError: continue
        marks.append((m.start(), end, m[1], plain_tex(title)))
    bounds = [0, *[m[0] for m in marks], len(text)]
    records = []; seen = Counter()
    for n in range(len(bounds)-1):
        start, stop = bounds[n], bounds[n+1]
        if start == stop: continue
        kind, title, prose_start = ("frontmatter", row["title"] or "Front matter / support", start) if n == 0 else (marks[n-1][2], marks[n-1][3], marks[n-1][1])
        seen[(kind, title)] += 1
        sid = "section:"+digest(path+"\0"+kind+"\0"+title+"\0"+str(seen[(kind,title)]))[:20]
        body = text[start:stop]
        excerpt, excerpt_method = opening_excerpt(text[prose_start:stop])
        line = text.count("\n", 0, start)+1
        last = text.count("\n", 0, stop) + int(not text[:stop].endswith("\n"))
        labels = sorted(set(re.findall(r"\\label\{([^{}]+)\}", mask_tex_comments(body))))
        record = {"id":sid,"source":path,"line_start":line,"line_end":max(line,last),"byte_start":len(text[:start].encode()),"byte_end":len(text[:stop].encode()),"kind":kind,"title":title,"occurrence":seen[(kind,title)],"summary_excerpt":excerpt,"summary_method":excerpt_method,"labels":labels,"status_markers_as_written":sorted(set(re.findall(r"\\m[ECOXILNFAP]\b|\[(?:E|C|O|X|I|L|N|F|A|P)\]",mask_tex_comments(body)))),"owner_documents":[],"topic_suggestions":[],"relation_ids":[],"semantic_review":False}
        records.append((record,body));row["section_ids"].append(sid)
    return row, records, text


def parse_lean(path):
    text=(ROOT/path).read_text(encoding="utf-8");clean=mask_lean_comments(text)
    symbols=[];matches=list(DECL.finditer(clean))
    context=[{"line":clean.count("\n",0,m.start())+1,"source_text":m[0].strip()} for m in re.finditer(r"^\s*(?:variable|variables|axiom|axioms)\b[^\n]*",clean,re.M)]
    namespaces=[];ns_at={};decl_by_pos={m.start():m for m in matches}
    token=re.compile(r"^\s*(namespace|section|end)\b\s*([\w.]*)",re.M)
    events=sorted([(m.start(),"scope",m)for m in token.finditer(clean)]+[(m.start(),"decl",m)for m in matches],key=lambda x:x[0])
    scopes=[]
    for _,kind,m in events:
        if kind=="scope":
            if m[1]=="end":
                if scopes:scopes.pop()
            else:scopes.append((m[1],m[2]))
        else:ns_at[m.start()]=".".join(name for typ,name in scopes if typ=="namespace" and name)
    for i,m in enumerate(matches):
        end=matches[i+1].start()if i+1<len(matches)else len(clean)
        body=clean[m.start():end];head=re.split(r":=|\bwhere\b",body,maxsplit=1)[0].strip()
        prefix=ns_at[m.start()];name=m[2] if "."in m[2]or not prefix else prefix+"."+m[2]
        symbols.append({"id":"lean-symbol:"+path+":"+name,"type":"lean_declaration","path":path,"name":m[2],"qualified_name":name,"declaration_kind":m[1],"line_start":clean.count("\n",0,m.start())+1,"line_end":clean.count("\n",0,end),"statement_as_written":head[:12000],"statement_truncated":len(head)>12000,"module_context_as_written":context,"contains_sorry_or_admit":bool(re.search(r"\b(?:sorry|admit)\b",body)),"checked_by_registry":False,"status_basis":"source declaration only; registry does not run Lean or certify assumptions"})
    return symbols,text


def parse_wolfram(path):
    text=(ROOT/path).read_text(encoding="utf-8");marks=list(WL_HEADING.finditer(text));sections=[]
    for i,m in enumerate(marks):
        end=marks[i+1].start()if i+1<len(marks)else len(text)
        body=text[m.start():end];line=text.count("\n",0,m.start())+1
        sections.append({"id":"wolfram-section:"+path+":"+str(line),"type":"wolfram_section","path":path,"line_start":line,"line_end":text.count("\n",0,end),"heading_as_written":" ".join(m[0].split()),"check_labels_as_written":re.findall(r'\bcheck(?:Exact)?\[\s*"([^"\n]+)"',body),"python_identifiers_in_heading":sorted(set("v"+x for x in re.findall(r"\bv(\d+)\b",m[0]))),"checked_by_registry":False,"status_basis":"source section and check labels only; no execution or equivalence assertion"})
    return sections,text


def build(config, paths, public_paths, include_local=False):
    inputs={};sources=[];sections=[];bodies={};raw_sources={};source_by_path={};diagnostics=[]
    for p in paths:
        row,records,text=parse_tex(p,config);sources.append(row);source_by_path[p]=row;raw_sources[p]=text;inputs[p]=row["sha256"]
        for record,body in records:sections.append(record);bodies[record["id"]]=body
    available=set(paths)|set(public_paths)
    manifest_path=ROOT/config["module_manifest"]
    manifest_data=json.loads(manifest_path.read_text()) if manifest_path.exists() else {}
    local_manifest=ROOT/"documents/local/source_manifest.json"
    if include_local and local_manifest.exists():
        manifest_data={**manifest_data,"documents":[*manifest_data.get("documents",[]),*json.loads(local_manifest.read_text()).get("documents",[])]}
    compile_dirs={m["path"]:d["compile_dir"] for d in manifest_data.get("documents",[]) for m in d.get("source_modules",[])}
    compile_dirs.update({d["entry_point"]:d["compile_dir"] for d in manifest_data.get("documents",[])})
    compile_dirs.update({d["main"]:d["compile_dir"] for d in manifest_data.get("documents",[])})
    for row in sources:
        for start,end,raw in literal_includes(raw_sources[row["path"]]):
            target=resolve_include(raw,row["path"],available,compile_dirs.get(row["path"]))
            inc={"literal":raw,"line":raw_sources[row["path"]].count("\n",0,start)+1,"target":target,"relation_type":"includes_source"}
            row["includes"].append(inc)
        if row["is_wrapper"]:
            row["alias_of"]=next((x["target"]for x in row["includes"]if x["target"]and x["target"].startswith("documents/")and x["target"].endswith("/main.tex")),None)
    by_section={s["id"]:s for s in sections};documents=[]
    standalone_path=ROOT/"documents/standalone_inventory.json"
    known_standalones={r["entry_point"] for r in json.loads(standalone_path.read_text()).get("documents",[])} if standalone_path.exists() else set()
    module_manifest=ROOT/config["module_manifest"]
    if module_manifest.exists():
        manifest=manifest_data
        known_standalones|={r["entry_point"] for r in manifest.get("documents",[]) if r.get("standalone")}
        module_by_path={m["path"]:{"logical_owner":r["id"],"legacy_entry_point":r["entry_point"],"compile_dir":r["compile_dir"],"original_source_span":{k:v for k,v in m.items() if k.startswith("original_")}} for r in manifest.get("documents",[]) for m in r.get("source_modules",[])}
        for source in sources:
            if source["path"]in module_by_path:source["modular_ownership"]=module_by_path[source["path"]]

    roots=[s for s in sources if s["path"]in config["active_entry_points"]or s["path"]in known_standalones or("\\documentclass"in mask_tex_comments(raw_sources[s["path"]])and not s["path"].startswith("documents/"))]
    include_contexts=defaultdict(set)
    for source in roots:
        entry=source["path"];did="document:"+entry.removesuffix(".tex");owners=[];spans=[];status="complete_literal_expansion";err=None
        try:
            # TeX resolves nested inputs from the containing document's compile
            # directory. A fragment's static include row is not its closure.
            compile_dir=compile_dirs.get(entry,str(Path(entry).parent))
            dependencies=dependency_paths(ROOT/entry,compile_dir=ROOT/compile_dir)
            for dependency in dependencies:
                p=rel(dependency)  # also rejects dependencies outside the repository
                if p not in source_by_path:
                    raise ValueError("include outside declared authored source inventory: "+p)
            chunks=source_chunks(ROOT/entry,compile_dir=ROOT/compile_dir)
            owners.extend(rel(p)for p in dependencies)  # retain empty/pure include sources
            for p in owners:include_contexts[p].add(compile_dir)
            for chunk in chunks:
                try:p=rel(chunk.path)
                except ValueError:raise ValueError("expansion escaped repository")
                if p not in source_by_path:continue
                spans.append({"source":p,"line_start":chunk.start_line,"line_end":chunk.end_line,"byte_start":chunk.start_byte,"byte_end":chunk.end_byte})
                owners.append(p)
                for ancestor in chunk.include_chain:
                    try:ancestor_path=rel(ancestor)
                    except ValueError:continue
                    if ancestor_path in source_by_path:owners.append(ancestor_path)
        except (TexSourceError,ValueError)as e:
            status="incomplete_literal_expansion";err=str(e).replace(str(ROOT)+"/","")
            # Inventory remains complete even when a historical document cannot expand.
            seen=set()
            def fallback(p):
                if p in seen or p not in source_by_path:return
                seen.add(p);owners.append(p)
                row=source_by_path[p];spans.append({"source":p,"line_start":1,"line_end":row["line_count"],"byte_start":0,"byte_end":row["bytes"]})
                for inc in row["includes"]:
                    if inc["target"]:fallback(inc["target"])
            fallback(entry)
            diagnostics.append({"kind":"document_expansion_incomplete","source":entry,"detail":err})
        contents=[]
        for span in spans:
            for sid in source_by_path[span["source"]]["section_ids"]:
                section=by_section[sid]
                if section["byte_start"]<span["byte_end"]and section["byte_end"]>span["byte_start"]and sid not in contents:contents.append(sid)
        for p in set(owners):source_by_path[p]["owner_documents"].append(did)
        for sid in contents:by_section[sid]["owner_documents"].append(did)
        raw_title=source["title_latex"]or next((source_by_path[p]["title_latex"]for p in owners if source_by_path[p]["title_latex"]),"")
        nav_title=config.get("document_titles",{}).get(entry,Path(entry).stem.replace("_"," "))
        documents.append({"id":did,"entry_point":entry,"canonical_source":source["alias_of"]or entry,"role":"active"if entry in config["active_entry_points"]else source["role"],"title":nav_title,"title_latex_as_written":raw_title,"title_basis":"curated navigation title"if entry in config.get("document_titles",{})else"source filename; original mathematical title preserved separately","compile_dir":compile_dirs.get(entry,str(Path(entry).parent)),"expansion_status":status,"expansion_error":err,"physical_sources":list(dict.fromkeys(owners)),"ordered_section_ids":contents,"source_spans":spans})
    # Source-level include navigation follows the actual owning compile contexts.
    # Shared fragments can have several contexts; never guess when they disagree.
    for source in sources:
        contexts=include_contexts.get(source["path"],())
        for inc in source["includes"]:
            if contexts:
                targets={resolve_include(inc["literal"],source["path"],available,c)for c in contexts}
                inc["target"]=next(iter(targets))if len(targets)==1 else None
                if len(targets)>1:inc["context_targets"]=sorted(t for t in targets if t is not None)
            if inc["target"]is None:
                diagnostics.append({"kind":"unresolved_include","source":source["path"],"line":inc["line"],"token":inc["literal"],"resolution":"not uniquely resolved within the declared authored source inventory and owning compile contexts; conditional/dynamic/historical inputs are not executed"})
    for source in sources:
        source["owner_documents"]=sorted(set(source["owner_documents"]))
        source["primary_owner"]=source["owner_documents"][0]if len(source["owner_documents"])==1 else "shared-source:"+source["path"]if source["owner_documents"]else "unreferenced-source:"+source["path"]
    for s in sections:
        s["owner_documents"]=sorted(set(s["owner_documents"]))
        text=s["title"]+" "+s["summary_excerpt"]+" "+s["source"]
        s["topic_suggestions"]=[{"topic_id":t["id"],"relation_type":"lexical_topic_suggestion","match_basis":"curated regex over source path, heading and opening excerpt; not semantic review"}for t in config["topics"]if re.search(t["pattern"],text,re.I)]
    evidence_paths=git_files("*.py","*.lean","*.wl","*.wls")if is_git_root()else json.loads((OUT/"source_inventory.json").read_text()).get("evidence_sources",[])
    if is_git_root():
        cited_aux={Path(token).name for body in raw_sources.values() for token,_ in file_citations(body) if not token.endswith((".py",".lean",".wl",".wls"))}
        evidence_paths+= [p for p in (git_files("*.md","*.json","*.csv","*.txt")or[])if Path(p).name in cited_aux and not p.startswith("docs/registry/")]
    historical_manifest=ROOT/"verification/historical_replay/manifest.json"
    historical_inputs={}
    if historical_manifest.exists():
        inputs["verification/historical_replay/manifest.json"]=digest(historical_manifest.read_bytes())
        historical_inputs={row["snapshot"]:row for row in json.loads(historical_manifest.read_text()).get("inputs",[]) if row.get("snapshot")}
        evidence_paths+= [path for path in historical_inputs if allowed(path,config)and(ROOT/path).is_file()]
    reg_path=ROOT/"verification/script_registry.csv";ledger_path=ROOT/"verification/status_ledger.csv"
    with reg_path.open()as stream:registry=list(csv.DictReader(stream))
    with ledger_path.open()as stream:ledger=list(csv.DictReader(stream))
    local_deleted=set(git_files("*",deleted=True)or[])if include_local and is_git_root()else set()
    evidence_paths=research_evidence_paths(evidence_paths or [],config,local_deleted,{r["script"]for r in registry},diagnostics)
    for optional in [config["module_manifest"], "documents/standalone_inventory.json", "docs/editions.json", "verification/project_scope.json"]:
        if (ROOT/optional).exists():inputs[optional]=digest((ROOT/optional).read_bytes())
    if include_local and local_manifest.exists():inputs["documents/local/source_manifest.json"]=digest(local_manifest.read_bytes())
    for p in ["verification/script_registry.csv","verification/status_ledger.csv", "docs/registry/config.json", "verification/make_content_registry.py", "verification/tex_sources.py"]:inputs[p]=digest((ROOT/p).read_bytes())
    reg={r["script"]:r for r in registry};claimrows={r["claim_id"]:r for r in ledger};claimby=defaultdict(list)
    for row in ledger:
        for script in re.findall(r"v\d+_[A-Za-z0-9_]+\.py",row.get("script","")):claimby[script].append(row["claim_id"])
    evidence=[];e_byid={};filemap={};basenames=defaultdict(list);shorts=defaultdict(list);lean_symbols=defaultdict(list);filetext={};lean_records=[];wolfram_records=[]
    for path in evidence_paths:
        row=file_info(path);inputs[path]=row["sha256"]
        historical=historical_snapshot_info(path,historical_inputs.get(path))
        canonical=not historical and path=="verification/"+Path(path).name and Path(path).stem in reg
        typ="historical_source_snapshot"if historical else"lean_module"if path.endswith(".lean")else"wolfram_file"if path.endswith((".wl",".wls"))else"source_document_or_data"if not path.endswith(".py")else"python_verification"if canonical else"python_source_copy"if Path(path).stem in reg else"python_exploration"if path.startswith("experiments/")else"python_source"
        eid=typ+":"+path;row.update(id=eid,type=typ,claim_ids=claimby.get(Path(path).name,[])if canonical else[],checked_by_registry=False)
        if historical:row.update(historical)
        if typ=="python_source_copy":row.update(canonical_source="verification/"+Path(path).name,ledger_status_not_inherited=True,ownership={"owner":"This experiment snapshot owns these exact bytes","canonical_owner":"TFPT verification registry","relation":"Same filename, separately stored source; no status transfer or byte equality presumed"})
        if typ=="python_verification":row.update(cluster=reg[Path(path).stem]["cluster"],description_excerpt=reg[Path(path).stem]["what_web"][:420])
        key=path if path in config["shared_python_ownership"]else re.match(r"v\d+",Path(path).stem)[0]if re.match(r"v\d+",Path(path).stem)else""
        if not historical and key in config["shared_python_ownership"]:row["ownership"]=config["shared_python_ownership"][key]
        evidence.append(row);filemap[path]=eid;basenames[Path(path).name].append(eid)
        if typ=="python_verification":shorts[re.match(r"v\d+",Path(path).stem)[0]].append(eid)
        if typ=="lean_module":
            symbols,text=parse_lean(path);filetext[eid]=text;row["declaration_ids"]=[r["id"]for r in symbols];lean_records.extend(symbols)
            for symbol in symbols:
                for k in {symbol["name"],symbol["qualified_name"]}:lean_symbols[k].append(symbol["id"])
        if typ=="wolfram_file":
            parts,text=parse_wolfram(path);filetext[eid]=text;row["section_ids"]=[r["id"]for r in parts];wolfram_records.extend(parts)
    evidence+=lean_records+wolfram_records
    for row_number,row in enumerate(ledger,2):
        eid="claim:"+row["claim_id"]
        evidence.append({"id":eid,"type":"claim_ledger_row","claim_id":row["claim_id"],"path":"verification/status_ledger.csv","row_number":row_number,"status_as_recorded":row["status"],"canonical_status_as_recorded":row.get("canonical_status",""),"active_as_recorded":row.get("active",""),"scripts_as_recorded":row.get("script",""),"dependencies_as_recorded":row.get("dependencies",""),"location_as_recorded":row.get("location",""),"external_data_as_recorded":row.get("external_data",""),"claim_excerpt":row["claim"][:420],"checked_by_registry":False})
    e_byid={e["id"]:e for e in evidence};relations={};unresolved={}
    def link(frm,to,kind,basis,line=None,token=None,via=None):
        key=(frm,to,kind,basis)
        if key not in relations:relations[key]={"id":"relation:"+digest("\0".join(key))[:20],"from":frm,"to":to,"relation_type":kind,"match_basis":basis,"line_numbers":[],"tokens":[],"occurrences":0}
        row=relations[key];row["occurrences"]+=1
        if line and line not in row["line_numbers"]and len(row["line_numbers"])<12:row["line_numbers"].append(line)
        if token and token not in row["tokens"]and len(row["tokens"])<8:row["tokens"].append(token)
        if via:row["via"]=via
        return row["id"]
    def unmatched(section,token,kind,line,candidates=None):
        key=(section,token,kind)
        if key not in unresolved:unresolved[key]={"kind":kind,"source_section":section,"token":token,"line":line,"occurrences":0,"candidate_ids":candidates or [],"resolution":"unresolved/ambiguous explicit citation; no proof edge asserted"}
        unresolved[key]["occurrences"]+=1
    def resolve_file(token):
        token=token.rstrip(".")
        if token in filemap:return[filemap[token]]
        if "/"not in token and "verification/"+token in filemap:return[filemap["verification/"+token]]
        suffix=[eid for p,eid in filemap.items()if p.endswith("/"+token)]
        return suffix or basenames.get(Path(token).name,[])
    for symbol in lean_records:link(filemap[symbol["path"]],symbol["id"],"contains_declaration","literal Lean declaration")
    for part in wolfram_records:
        for token in part["python_identifiers_in_heading"]:
            for target in shorts.get(token,[]):link(part["id"],target,"explicit_source_identifier","Wolfram section comment names Python identifier",part["line_start"],token)
    for eid,text in filetext.items():
        if e_byid[eid]["type"]=="lean_module":
            for m in SHORT_V.finditer(text):
                for target in shorts.get("v"+m[1],[]):link(eid,target,"explicit_source_identifier","Lean module source/comment names Python identifier",text.count("\n",0,m.start())+1,m[0])
    for section in sections:
        body=bodies[section["id"]];norm=normalize_refs(body);base=section["line_start"]
        ids=[]
        for token,line_offset in file_citations(body):
            line=base+line_offset;targets=resolve_file(token)
            if len(targets)==1:ids.append(link(section["id"],targets[0],"explicit_file_citation","literal source filename/path in TeX",line,token))
            else:unmatched(section["id"],token,"ambiguous_file_citation"if targets else"unmatched_file_citation",line,targets)
        for m in SHORT_V.finditer(norm):
            token="v"+m[1];targets=shorts.get(token,[]);line=base+norm.count("\n",0,m.start())
            if len(targets)==1:ids.append(link(section["id"],targets[0],"explicit_script_identifier","literal short identifier uniquely resolves in local script registry",line,token))
            else:unmatched(section["id"],token,"ambiguous_script_identifier"if targets else"unmatched_script_identifier",line,targets)
        for claim in sorted(set(re.findall(r"(?<![A-Za-z0-9_.])(?:[A-Z][A-Z0-9_]*\.){1,}[A-Z0-9_]+(?![A-Za-z0-9_.])",norm))):
            if claim not in claimrows:
                if re.fullmatch(r"(?:V\d+|[IVX]+\d*|[A-Z]\d+)\.\d+",claim):
                    section.setdefault("numbered_or_version_tokens_as_written",[]).append(claim)
                    continue
                # Claim-shaped prose alone is not enough; uppercase identifiers with digits are candidates only.
                if re.search(r"\.\d+$",claim):unmatched(section["id"],claim,"unmatched_claim_identifier",base+norm.count("\n",0,norm.find(claim)))
                continue
            ids.append(link(section["id"],"claim:"+claim,"explicit_claim_identifier","exact local ledger claim identifier",base+norm.count("\n",0,norm.find(claim)),claim))
        for m in re.finditer(r"\\texttt\s*\{([^{}]+)\}",norm):
            token=m[1].strip().removeprefix("#check ")
            if len(token)<7 or not("_"in token or "."in token):continue
            if not re.search(r"Lean|lean|\.lean\b|#check|theorem|lemma",norm[max(0,m.start()-600):m.end()+600]):continue
            targets=sorted(set(lean_symbols.get(token,[])))
            if len(targets)>1:
                context=norm[max(0,m.start()-600):m.end()+600]
                module_tokens=[name for name,_ in file_citations(context)if name.endswith(".lean")]
                selected=[eid for eid in targets if any(e_byid[eid]["path"].endswith("/"+name)or e_byid[eid]["path"]==name for name in module_tokens)]
                if len(selected)==1:targets=selected
            if len(targets)==1:ids.append(link(section["id"],targets[0],"explicit_lean_symbol","exact texttt symbol under explicit Lean/theorem context",base+norm.count("\n",0,m.start()),token))
            elif len(targets)>1:unmatched(section["id"],token,"ambiguous_lean_symbol",base+norm.count("\n",0,m.start()),targets)
        section["relation_ids"]=sorted(set(ids))
    # A shared named script is a navigation join, never a proof correspondence.
    reverse_script=defaultdict(list)
    for row in list(relations.values()):
        if row["relation_type"]=="explicit_source_identifier":reverse_script[row["to"]].append(row["from"])
    relation_lookup={r["id"]:r for r in relations.values()}
    for section in sections:
        joins=[]
        for rid in list(section["relation_ids"]):
            record=relation_lookup[rid]
            if record["to"]not in reverse_script:continue
            for target in sorted(set(reverse_script[record["to"]])):
                joins.append(link(section["id"],target,"cross_reference_join","TeX and evidence source explicitly name the same Python identifier; statement equivalence not inferred",via=[rid,record["to"]]))
        section["relation_ids"]=sorted(set(section["relation_ids"]+joins))
    rows=sorted(relations.values(),key=lambda r:r["id"]);reverse={"by_topic":defaultdict(list),"by_evidence":defaultdict(list),"by_label":defaultdict(list),"by_source":{},"by_document":{},"by_script":defaultdict(list)}
    for s in sections:
        for t in s["topic_suggestions"]:reverse["by_topic"][t["topic_id"]].append(s["id"])
        for label in s["labels"]:reverse["by_label"][label].append(s["id"])
    for source in sources:reverse["by_source"][source["path"]]=source["section_ids"]
    for doc in documents:reverse["by_document"][doc["id"]]=doc["ordered_section_ids"]
    for row in rows:
        reverse["by_evidence"][row["to"]].append(row["id"])
        if row["from"].startswith("section:")and e_byid.get(row["to"],{}).get("type")=="python_verification":reverse["by_script"][Path(e_byid[row["to"]]["path"]).stem].append(row["from"])
    reverse={kind:{key:sorted(set(value))for key,value in sorted(mapping.items())}for kind,mapping in reverse.items()}
    # Containment is not a document citation. A module listing a theorem does
    # not establish which theorem (if any) supports a manuscript statement.
    cited={r["to"] for r in rows if r["from"].startswith("section:")}
    unmapped=[e["id"]for e in evidence if e["id"]not in cited and e["type"]in{"python_verification","lean_module","lean_declaration","wolfram_section"}]
    diagnostics+=sorted(unresolved.values(),key=lambda x:(x["source_section"],x["line"],x["token"]))
    project_path=ROOT/"verification/project_scope.json"
    project=json.loads(project_path.read_text()) if project_path.exists() else {}
    external_names=set(project.get("external_module_names",[]))
    external_paths=project.get("excluded_active_paths",[])
    external_short={re.match(r"v\d+",p)[0] for p in external_names if re.match(r"v\d+",p)}
    for diagnostic in diagnostics:
        source=diagnostic.get("source")
        if diagnostic.get("source_section")in by_section:source=by_section[diagnostic["source_section"]]["source"]
        row=source_by_path.get(source,{})
        origin=row.get("modular_ownership",{}).get("legacy_entry_point",source or "")
        if origin.startswith("_archive/"):scope="archive_historical"
        elif Path(origin).name=="changelog.tex" or "Sitzungsdokumentation"in origin:scope="dated_historical_record"
        elif origin in config["active_entry_points"] or any(owner.removeprefix("document:")+".tex"in config["active_entry_points"] for owner in row.get("owner_documents",[])):scope="active_document"
        elif origin.startswith("experiments/"):scope="exploration"
        else:scope="support_or_other_authored_source"
        diagnostic["origin_scope"]=scope
        token=diagnostic.get("token","");stem=Path(token).stem
        known_external=stem in external_names or token in external_short or token.startswith(("PRIME.","FORM.PRIME."))
        if known_external:
            diagnostic["resolution_scope"]="known_external_prime_front"
            diagnostic["resolution"]="Recorded Prime Front ownership; not a missing local TFPT proof. No sibling status or statement equivalence imported."
            diagnostic["external_project"]="Prime Front"
            diagnostic["external_candidate_paths"]=[p for p in external_paths if Path(p).stem==stem or(Path(p).stem.startswith(token+"_")if token.startswith("v")and token[1:].isdigit()else False)]
        else:diagnostic["resolution_scope"]="ambiguous_local_reference"if diagnostic.get("candidate_ids")else"unresolved_local_or_historical_reference"
        diagnostic["severity"]="source_navigation_diagnostic_not_a_mathematical_verdict"
    diagnostics.append({"kind":"evidence_without_incoming_citation","entity_ids":sorted(unmapped),"meaning":"No indexed citation edge; this is not evidence of absence of a proof or of an invalid result."})
    for doc in documents:
        doc["topic_ids"]=sorted({t["topic_id"] for sid in doc["ordered_section_ids"] for t in by_section[sid]["topic_suggestions"]})
        doc["section_count"]=len(doc["ordered_section_ids"])
    input_manifest={key:inputs[key]for key in sorted(inputs)}
    registry_out={"schema_version":"1.0","publication_scope":"local_supplement"if include_local else"public_authored_sources","generator":{"path":"verification/make_content_registry.py","parser":"literal static source index; no macro evaluation, proof execution or semantic review","input_fingerprint":digest(dumps(input_manifest)),"inputs":input_manifest},"coverage":{"tex_sources":len(sources),"physical_sections":len(sections),"document_views":len(documents),"active_document_views":sum(d["role"]=="active"for d in documents),"roles":dict(sorted(Counter(s["role"]for s in sources).items())),"registered_python_scripts":len(registry),"ledger_rows":len(ledger),"lean_modules":sum(e["type"]=="lean_module"for e in evidence),"lean_declarations":len(lean_records),"wolfram_files":sum(e["type"]=="wolfram_file"for e in evidence),"wolfram_sections":len(wolfram_records),"relations":len(rows),"unresolved_explicit_citations":len(unresolved),"citation_diagnostics_by_scope":dict(sorted(Counter(d["origin_scope"]+":"+d["resolution_scope"]for d in diagnostics if d.get("source_section")).items())),"evidence_without_incoming_citation":len(unmapped),"complete_semantic_review":False,"proofs_checked":False},"editions":json.loads((ROOT/"docs/editions.json").read_text()).get("editions",[]) if (ROOT/"docs/editions.json").exists() else [],"topics":[{**t,"relation_type":"lexical_topic_suggestion"}for t in config["topics"]],"sources":sources,"documents":documents,"sections":sections,"evidence":evidence,"relations":rows,"reverse_indexes":reverse,"diagnostics":diagnostics}
    ids={s["id"]for s in sections}|{e["id"]for e in evidence}|{s["id"]for s in sources}
    if len({s["id"]for s in sections})!=len(sections):raise ValueError("Duplicate physical section IDs")
    if len(e_byid)!=len(evidence):raise ValueError("Duplicate evidence IDs")
    for edge in rows:
        if edge["from"]not in ids or edge["to"]not in ids:raise ValueError("Dangling registry edge: "+edge["id"])
        if edge["relation_type"]not in RELATION_KINDS:raise ValueError("Unknown relation kind")
    return registry_out,evidence_paths


def markdown_outputs(data):
    c=data["coverage"];byid={s["id"]:s for s in data["sections"]}
    lines=["# TFPT LaTeX content registry","","Generated by `python3 verification/make_content_registry.py`. Edit owning sources/config, then regenerate.","","This registry locates authored content and its actual source references. It does not verify a theorem, equate a numerical check with a proof, or promote any ledger status. Topic matches and same-identifier joins are explicitly separate from citations.","",f"**{c['tex_sources']} physical TeX sources · {c['physical_sections']} section records · {c['document_views']} document views · {c['registered_python_scripts']} registered Python scripts · {c['lean_modules']} Lean modules · {c['wolfram_files']} Wolfram files.**","","- [Machine-readable registry](registry.json)","- [Complete source inventory](source_inventory.json)","- [Schema](schema.json)","- [Relation types and reading guide](RELATIONS.md)","- [LaTeX maintenance](../LATEX_MAINTENANCE.md)","- [Unresolved references and mapping coverage](UNRESOLVED.md)","","## Find content","","```sh","python3 verification/make_content_registry.py --query 'Pascal'","python3 verification/make_content_registry.py --topic e8-geometry","python3 verification/make_content_registry.py --document introduction","python3 verification/make_content_registry.py --query 'carrier_rank_pascal_unique' --json","python3 verification/make_content_registry.py --check","```","","## Topics","","These are lexical navigation suggestions from a small curated taxonomy, not reviewed theorem classifications.",""]
    for t in data["topics"]:lines.append(f"- **[{t['id']} — {t['title']}](topics/{t['id']}.md)**: {len(data['reverse_indexes']['by_topic'].get(t['id'],[]))} section matches; query with `--topic {t['id']}`.")
    lines += ["","## Active document owners","","One section body is stored only once at its physical source. Legacy entry points preserve compile directories; wrappers/compiled views list ordered section IDs rather than copying content.","","| Entry point | Source owner | Sections in view | Expansion |","|---|---|---:|---|"]
    for d in data["documents"]:
        if d["role"]=="active":lines.append(f"| [{d['entry_point']}](../../{d['entry_point']}) | [{d['canonical_source']}](../../{d['canonical_source']}) | {len(d['ordered_section_ids'])} | {d['expansion_status']} |")
    lines += ["","## Complete source inventory","","See [SOURCES.md](SOURCES.md) for every physical source, its role and document-owner count. The machine-readable inventory and registry retain the complete records."]
    source_lines=["# Complete physical TeX source inventory","","[Compact registry entry](INDEX.md). Generated from the central registry; inclusion does not endorse a historical claim.","","| Source | Role | Physical sections | Document views |","|---|---|---:|---:|"]
    for s in data["sources"]:source_lines.append(f"| [{s['path']}](../../{s['path']}) | {s['role']} | {len(s['section_ids'])} | {len(s['owner_documents'])} |")
    topic_pages={}
    evidence_by_id={e["id"]:e for e in data["evidence"]}
    relations_by_id={r["id"]:r for r in data["relations"]}
    for topic in data["topics"]:
        matches=[byid[sid] for sid in data["reverse_indexes"]["by_topic"].get(topic["id"],[])]
        matches.sort(key=lambda s:(s["source"],s["line_start"]))
        page=["# "+topic["title"],"","[Registry index](../INDEX.md) · Topic ID: `"+topic["id"]+"`","",f"{len(matches)} physical section matches. Topic assignment is a lexical navigation suggestion, not semantic review. The excerpts and citations below come from source; no proof or status promotion is asserted.",""]
        for section in matches:
            page += ["## "+section["title"],"",f"[{section['source']}:{section['line_start']}-{section['line_end']}](../../../{section['source']}#L{section['line_start']}) · `{section['id']}` · {section['kind']}","",section["summary_excerpt"] or "No opening prose excerpt; see the source.",""]
            direct=[relations_by_id[rid] for rid in section["relation_ids"] if relations_by_id[rid]["relation_type"]!="cross_reference_join"]
            if direct:
                page += ["Explicit source references:",""]
                seen_targets=set()
                for edge in direct:
                    if edge["to"] in seen_targets:continue
                    seen_targets.add(edge["to"]);e=evidence_by_id[edge["to"]];path=e.get("path","");line=e.get("line_start",e.get("row_number",1));name=e.get("qualified_name",e.get("claim_id",path))
                    # Keep one status authority, rather than repeating long
                    # ledger paragraphs in every lexical topic view.
                    status=" · original status at linked ledger row" if "status_as_recorded"in e else ""
                    page.append(f"- [{name}](../../../{path}#L{line}) · {edge['relation_type']}{status}")
                page.append("")
            joined=[relations_by_id[rid] for rid in section["relation_ids"] if relations_by_id[rid]["relation_type"]=="cross_reference_join"]
            if joined:
                page += ["Navigation joins (both sources name the same Python identifier; statement equivalence is not inferred):",""]
                for edge in joined:
                    e=evidence_by_id[edge["to"]];line=e.get("line_start",1);path=e["path"];page.append(f"- [{e.get('qualified_name',e.get('heading_as_written',path))}](../../../{path}#L{line})")
                page.append("")
        full="\n".join(page)+"\n";parts=full.split("\n## ");header=parts[0]
        blocks=["## "+block for block in parts[1:]]
        entry=[header,"","## Bounded reading parts","","Each part contains at most 100 physical section records and their actual explicit source references. Use the CLI for a smaller query.",""]
        for number,start in enumerate(range(0,len(blocks),100),1):
            name=f"part-{number:03d}.md"
            entry.append(f"- [Part {number}: section matches {start+1}–{min(start+100,len(blocks))}]({topic['id']}/{name})")
            part_header=f"# {topic['title']} — part {number}\n\n[Topic entry](../{topic['id']}.md) · [Registry entry](../../INDEX.md)\n\nExact ledger statuses remain at the linked original rows and in registry.json. Citations are source links, not proof certification.\n\n"
            topic_pages[f"topics/{topic['id']}/{name}"]=part_header+"\n".join(blocks[start:start+100]).replace("](../../../","](../../../../")
        entry += ["","## First 20 source locations","","| Source | Heading |","|---|---|"]
        for section in matches[:20]:
            title=section['title'].replace('|','/').replace('\n',' ')[:160]
            entry.append(f"| [{section['source']}:{section['line_start']}](../../../{section['source']}#L{section['line_start']}) | {title} |")
        topic_pages["topics/"+topic["id"]+".md"]="\n".join(entry)+"\n"
    diag=["# Unresolved references and coverage","","Generated source-navigation diagnostics; unresolved means no unique local target was asserted. Historical/moved-project references may be intentional. Absence of a citation is not absence of a proof.","",f"Unresolved explicit citation groups: **{c['unresolved_explicit_citations']}**. Evidence entities without incoming indexed citation: **{c['evidence_without_incoming_citation']}**.","","The full precise list (section IDs, physical lines, tokens, candidates) is in `registry.json` → `diagnostics`. This page groups repeated tokens for readability.","","| Kind | Token | Section groups |","|---|---|---:|"]
    counts=Counter((d["kind"],d.get("token",d.get("source","")))for d in data["diagnostics"]if d["kind"]!="evidence_without_incoming_citation")
    for(kind,token),count in sorted(counts.items()):diag.append(f"| {kind} | `{token.replace('|','/').replace('`','')}` | {count} |")
    return {"INDEX.md":"\n".join(lines)+"\n","SOURCES.md":"\n".join(source_lines)+"\n","UNRESOLVED.md":"\n".join(diag)+"\n",**topic_pages}


def query(data,args):
    sections={s["id"]:s for s in data["sections"]};evidence={e["id"]:e for e in data["evidence"]};result={}
    if args.document:
        term=args.document.removesuffix(".tex").removeprefix("document:")
        result["documents"]=[d for d in data["documents"]if term in{d["id"].removeprefix("document:"),d["entry_point"].removesuffix(".tex"),Path(d["entry_point"]).stem}]
        ids=list(dict.fromkeys(sid for d in result["documents"]for sid in d["ordered_section_ids"]))
        if not ids and args.document in data["reverse_indexes"]["by_source"]:ids=data["reverse_indexes"]["by_source"][args.document]
    elif args.topic:
        ids=data["reverse_indexes"]["by_topic"].get(args.topic,[])
        if args.topic not in{t["id"]for t in data["topics"]}:raise ValueError("Unknown topic: "+args.topic)
    else:
        tokens=args.query.casefold().split();ids=[s["id"]for s in data["sections"]if all(t in(s["title"]+" "+s["summary_excerpt"]+" "+s["source"]+" "+" ".join(s["labels"])).casefold()for t in tokens)]
        matches=[e for e in data["evidence"]if all(t in dumps(e).casefold()for t in tokens)]
        result["evidence_matches"]=matches[:args.limit]
        evidence_ids={e["id"]for e in matches}
        ids+= [r["from"]for r in data["relations"]if r["to"]in evidence_ids and r["from"]in sections]
    ids=list(dict.fromkeys(ids));result["total_section_matches"]=len(ids);result["sections"]=[sections[i]for i in ids[:args.limit]]
    relation_ids={rid for s in result["sections"]for rid in s["relation_ids"]}
    matched_relations=[r for r in data["relations"]if r["id"]in relation_ids]
    result["total_relation_matches"]=len(matched_relations);result["relations"]=matched_relations[:args.relation_limit]
    target_ids=list(dict.fromkeys(r["to"]for r in matched_relations if r["to"]in evidence))
    result["total_evidence_matches"]=len(target_ids);result["evidence"]=[evidence[eid]for eid in target_ids[:args.evidence_limit]]
    if "documents"in result:result["documents"]=[{k:d[k]for k in["id","title","entry_point","canonical_source","role","section_count","topic_ids","expansion_status"]}for d in result["documents"]]
    result["sections"]=[{k:s[k]for k in["id","source","line_start","line_end","kind","title","summary_excerpt","owner_documents"]}for s in result["sections"]]
    result["scope_note"]="Citations, joins and topics retain their recorded relation types; no proof validation or status promotion. Result limits apply independently to sections, relations and evidence."
    if args.json:print(dumps(result),end="")
    else:
        print(result["scope_note"]);print(f"{len(result['sections'])} of {len(ids)} section matches shown")
        for d in result.get("documents",[]):print("DOCUMENT",d["id"],d["canonical_source"])
        for s in result["sections"]:print(f"{s['source']}:{s['line_start']}-{s['line_end']}  {s['kind']} — {s['title']}\n  {s['summary_excerpt']}")
        for e in result.get("evidence_matches",[]):print("EVIDENCE",e["id"],e.get("status_as_recorded",e.get("status_basis","")))
    return 0


def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check",action="store_true");parser.add_argument("--include-local",action="store_true");parser.add_argument("--output",type=Path)
    group=parser.add_mutually_exclusive_group();group.add_argument("--query");group.add_argument("--topic");group.add_argument("--document")
    parser.add_argument("--json",action="store_true");parser.add_argument("--limit",type=int,default=20)
    parser.add_argument("--evidence-limit",type=int,default=20);parser.add_argument("--relation-limit",type=int,default=80)
    args=parser.parse_args(argv);config=json.loads(CONFIG.read_text());target=args.output or(OUT/"local"if args.include_local else OUT)
    scope_path=ROOT/"verification/project_scope.json"
    if scope_path.exists():config["vendor_roots"]=json.loads(scope_path.read_text()).get("vendor_roots",[])
    if min(args.limit,args.evidence_limit,args.relation_limit)<1:parser.error("result limits must be positive")
    if args.query or args.topic or args.document:
        data=json.loads((target/"registry.json").read_text());return query(data,args)
    paths,public=discover(config,args.include_local);data,evidence=build(config,paths,public,args.include_local)
    summary={"schema_version":data["schema_version"],"publication_scope":data["publication_scope"],"coverage":data["coverage"],"input_fingerprint":data["generator"]["input_fingerprint"],"documents":[{key:doc[key]for key in["id","title","entry_point","canonical_source","role","topic_ids","section_count","expansion_status"]}for doc in data["documents"]],"topics":[{"id":t["id"],"title":t["title"],"relation_type":t["relation_type"],"section_count":len(data["reverse_indexes"]["by_topic"].get(t["id"],[])),"navigation_path":"topics/"+t["id"]+".md"}for t in data["topics"]],"editions":data["editions"],"full_registry":"registry.json","query":"python3 verification/make_content_registry.py --query TEXT --limit 20 --json","notice":"Compact derived navigation only; citations, statuses and unresolved details live in the central registry. No proof check or semantic review."}
    outputs={"registry.json":json.dumps(data,ensure_ascii=False,sort_keys=True,separators=(",",":"))+"\n","summary.json":dumps(summary),**markdown_outputs(data),"source_inventory.json":dumps({"schema_version":"1.0","scope":data["publication_scope"],"basis":"Git tracked TeX plus explicitly declared modular sources; Gitless exports use this shipped inventory", "tex_sources":paths,"evidence_sources":evidence,"excluded_nonresearch_evidence_roots":config.get("excluded_evidence_roots",["website"]),"availability_policy":"Every declared research source must exist; source bytes are hashed in Git and Gitless exports alike. Editor/agent configuration and website mirrors are outside evidence scope."})}
    stale=[]
    for extra in (target/"topics").rglob("*.md") if (target/"topics").exists() else []:
        if extra.relative_to(target).as_posix() not in outputs:
            if args.check:stale.append(str(extra))
            else:extra.unlink()
    for name,content in outputs.items():
        path=target/name
        if not path.exists()or path.read_text()!=content:
            if args.check:stale.append(str(path.relative_to(ROOT))if path.is_relative_to(ROOT)else str(path))
            else:path.parent.mkdir(parents=True,exist_ok=True);path.write_text(content)
    if stale:
        print("CONTENT REGISTRY STALE:\n"+"\n".join(stale));return 1
    print("CONTENT REGISTRY "+("CHECK PASS"if args.check else"WRITTEN")+": "+dumps(data["coverage"]).strip())
    return 0


if __name__=="__main__":
    try:sys.exit(main())
    except(ValueError,OSError,KeyError)as error:print("CONTENT REGISTRY ERROR:",error,file=sys.stderr);sys.exit(2)
