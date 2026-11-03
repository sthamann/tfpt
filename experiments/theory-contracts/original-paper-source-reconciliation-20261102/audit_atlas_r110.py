from pathlib import Path
from hashlib import sha256
from collections import Counter
import json,re,csv

ROOT=Path('/Users/stefanhamann/Projekte/tfpt-theoryv4')
OUT=Path(__file__).resolve().parent
program=json.loads((ROOT/'semantic_explorer/research/program.json').read_text())
plan=json.loads((ROOT/'docs/research/fundamental-plan/progress.json').read_text())
premises={p['id'] for p in program['premises']}
findings=[(p,f) for p in program['problems'] for f in p.get('findings',[])]
finding_ids={f['id'] for p,f in findings}
task_ids={t['id'] for p in program['problems'] for t in p.get('tasks',[])}
issues=[]; ref_count=0;checked=set();cache={};missing_hash=[]
def issue(kind,owner,detail):issues.append({'kind':kind,'owner':owner,'detail':detail})
def contents(path):
    if path not in cache:
        b=path.read_bytes();cache[path]=(sha256(b).hexdigest(),len(b.splitlines()))
    return cache[path]
def check_source(s,owner):
    global ref_count
    if not isinstance(s,dict) or 'path' not in s:return
    ref_count+=1
    path=Path(s['path']);path=path if path.is_absolute() else ROOT/path
    sig=(str(path),s.get('sha256'),s.get('line_start'),s.get('line_end'))
    checked.add(sig)
    if not path.is_file():issue('missing_source',owner,str(path));return
    digest,lines=contents(path)
    if s.get('sha256') and digest!=s['sha256']:issue('source_hash_mismatch',owner,s['path'])
    if not s.get('sha256'):missing_hash.append({'owner':owner,'source':s['path']})
    lo,hi=s.get('line_start'),s.get('line_end')
    if lo is not None and (not isinstance(lo,int) or lo<1):issue('invalid_line_start',owner,str(s))
    if hi is not None and (not isinstance(hi,int) or hi>lines or (lo is not None and hi<lo)):
        issue('invalid_line_end',owner,str(s)+' actual_lines='+str(lines))
all_records=[]
for p in program['problems']:
    for x in p.get('accepted_premise_ids',[]):
        if x not in premises:issue('missing_premise',p['id'],x)
    for typ in ('findings','tasks','strategies'):
        for x in p.get(typ,[]):
            all_records.append(x['id'])
            for k in ('premise_ids','required_premise_ids'):
                for xref in x.get(k,[]):
                    if xref not in premises:issue('missing_premise',x['id'],xref)
            for k in ('resolution_ids','finding_ids'):
                for xref in x.get(k,[]):
                    if xref not in finding_ids:issue('missing_finding',x['id'],xref)
            for xref in x.get('depends_on',[]):
                if xref not in task_ids:issue('unresolved_task_dependency',x['id'],xref)
            for src in x.get('sources',[]):check_source(src,x['id'])
for ident,n in Counter(all_records).items():
    if n>1:issue('duplicate_record_id',ident,n)
f1=next(t for t in plan['tasks'] if t['id']=='F1')
if len(f1['completed_subtasks'])!=52:issue('unexpected_completed_count','F1',len(f1['completed_subtasks']))
if plan.get('current_atlas_revision')!=program['revision']:issue('plan_atlas_revision','plan',{'plan':plan.get('current_atlas_revision'),'atlas':program['revision']})
results=(ROOT/'docs/research/fundamental-plan/RESULTS.md').read_text()
missing_results=[rid for rid in plan['result_ids'] if rid not in results]
# Wording checks are warnings, not automatic scientific verdict changes.
wording=[]
for name in ('PLAN.md','RESULTS.md','SEARCH-METHODS.md','SOURCE-DICTIONARY.md'):
    for line_no,line in enumerate((ROOT/'docs/research/fundamental-plan'/name).read_text().splitlines(),1):
        if re.search(r'52 erledigten physischen|52 physischen',line):wording.append({'path':name,'line':line_no,'text':line})
recent=next(p for p in program['problems'] if p['id']=='problem:original-det16-vertex-source-identification')
ledger=list(csv.DictReader((ROOT/'verification/status_ledger.csv').open()))
selected={x['claim_id']:{k:x.get(k) for k in ('status','canonical_status','active')} for x in ledger
          if x['claim_id'] in ('AX.P1.01','AX.P2.01','EM.FP.01','CHIRAL4D.NOMIRROR.01','TFPT.TOE.COMPLETE.01')}
report={'scope':'All current durable Atlas research records: provenance and internal references. No fresh semantic proof of every theorem, no full Lean/Python/Wolfram rerun.',
 'atlas_revision':program['revision'],'plan_revision':plan['revision'],'problems':len(program['problems']),
 'findings':len(findings),'premises':len(premises),'records':len(all_records),
 'source_references':ref_count,'unique_source_intervals':len(checked),'unique_source_files':len(cache),
 'issues':issues,'unhashed_source_references':missing_hash,'missing_plan_result_mentions':missing_results,
 'wording_warnings':wording,'F1_completed':len(f1['completed_subtasks']),'F1_status':f1['status'],
 'recent_findings':[{'id':f['id'],'status':f['status']} for f in recent['findings']],
 'ledger_scope_snapshot':selected}
(OUT/'atlas-audit.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k not in ('recent_findings','ledger_scope_snapshot')},ensure_ascii=False,indent=2))
print('LEDGER',json.dumps(selected,ensure_ascii=False))
