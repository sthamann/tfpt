#!/usr/bin/env python3
"""Export a bounded public scientific inventory, or reproduce/check its frozen snapshot.

Live mode reads only the explicit authoring ledger, reviewed program and their
cited source ranges. It never imports the generated/private Atlas graph. Source
SHA-256 values and inclusive ranges are checked before publication. A frozen
snapshot and excerpt manifest make subsequent builds independent of the local
research checkout. This is a coverage/source check, not a fresh proof execution.
"""
from __future__ import annotations
import argparse, collections, csv, hashlib, io, json, re, subprocess, sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote

WEBSITE = Path(__file__).resolve().parents[1]
PUBLIC = WEBSITE / 'public/research'
DATA = WEBSITE / 'lib/research-inventory.json'
SUMMARY = WEBSITE / 'lib/research-summary.json'
SNAPSHOT = PUBLIC / 'research-snapshot.json'
APPROVED = ('experiments/theory-contracts/', 'experiments/lean4-carrier-rigidity/',
            'documents/', 'verification/', 'docs/research/', 'tex-artefacts/', 'tfpt_explorer/')
ADMIN_IDS = {
 'finding:four-session-summaries-remain-covered-with-superseded-norm-selection-task':
 'Administrative continuity and private session-map coverage; scientific Hardy result remains covered by its own reviewed records.'
}
# These patterns remove conversation/agent provenance, personal filesystem paths,
# and execution identifiers from distributed excerpts, never mathematical symbols.
PRIVATE = re.compile(r'(?i)(?:\b(?:stefan|user|nutzer|chatgpt|claude\w*|codex|grok\w*|kimi)\b|/Users/|/home/|local_private|\.env\b|session[ _-]?(?:id|uuid)|[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}|(?:api[_-]?key|access[_-]?token|authorization)\s*[:=])')
NARRATIVE = re.compile(r'(?i)(?:\b(?:session|sitzung|consultation|conversation|chat|collaboration|reviewer|prompt|task.workspace|raw.task|raw.output)\b|(?:round|runde)\s*\d+)')

def sha(data): return hashlib.sha256(data).hexdigest()
def encode(v): return (json.dumps(v, ensure_ascii=False, indent=2) + '\n').encode()
def load(p): return json.loads(p.read_text())
def git(root, *args): return subprocess.check_output(['git', *args], cwd=root, text=True).strip()
def write(p, data):
 p.parent.mkdir(parents=True, exist_ok=True); p.write_bytes(data)
def english(v): return v.get('en') or v.get('de') or ''
def historical(path): return bool(re.search(r'(?i)(?:archive|historical)', path))

def safe_text(value):
 """Omit personal/agent attributions in a public *derived* display field.
 Exact original mathematical statement and scope are otherwise preserved.
 """
 text = english(value)
 edits = []
 substitutions = [
  (r'R058 user-steered priority is original process localization before further geometric Higgs optimization\.', ''),
  (r'All twelve sections and submitted findings, outstanding notebook checks, counterexamples and prioritized source tests are retained in the source-path review\.', ''),
  (r'Two user syntheses', 'Two source syntheses'),
  (r'User instruction stops further spinor/dressing/sector/gauge search at this explicit definition gap\.', ''),
  (r'Corrects an overstrong Codex premise', 'Corrects an overstrong premise'),
  (r'Recurring research stopped at user request without scientific completion\.', ''),
  (r'User direction17Oct:', 'Accepted field-algebra scope:'),
  (r'User instruction6868e83518Oct replaces automatic next origin classification with equivalence test forq2,3,4,5 and globalS01\.', 'Comparison scope: q2,3,4,5 and globalS01.'),
  (r"Under the user's23Oct2026 decision,", 'Within the stated mathematical scope,'),
  (r"Claude\d*['’]?s?", 'The reviewed'),
  (r'Grok\d*', 'the reviewed source'),
 ]
 for pattern,replacement in substitutions:
  new,n=re.subn(pattern,replacement,text,flags=re.I)
  if n: edits.append('Non-scientific attribution omitted from public display.');text=new
 return text.strip(), list(dict.fromkeys(edits))

def excerpt_bytes(path, raw, start, end):
 lines=raw.decode('utf-8').splitlines(); chosen=lines[start-1:end]
 # Text paragraphs retain complete proof context. If a paragraph contains private
 # or conversation metadata, omit that paragraph explicitly, retaining line nums.
 omitted=set()
 if Path(path).suffix.lower() in ('.md','.txt','.tex'):
  blocks=[];block=[]
  for i,line in enumerate(chosen,start):
   if not line.strip():
    if block:blocks.append(block);block=[]
   else:block.append((i,line))
  if block:blocks.append(block)
  for block in blocks:
   if any(PRIVATE.search(line) or NARRATIVE.search(line) for _,line in block):
    omitted.update(i for i,_ in block)
 else:
  for i,line in enumerate(chosen,start):
   if PRIVATE.search(line) or NARRATIVE.search(line):omitted.add(i)
 # Source paths and immutable whole-file digest are public provenance. These
 # excerpts are inert text, never advertised as executable source replacements.
 header=[f'TFPT scientific source excerpt',f'Original repository path: {path}',
         f'Original file SHA-256: {sha(raw)}',f'Inclusive original lines: {start}-{end}',
         'Line numbers below refer to the original source.',
         'This bounded excerpt is source evidence; it is not a new proof/checker run.',
         'Conversation metadata and personal execution details are omitted where indicated.', '']
 body=[]
 for i,line in enumerate(chosen,start):
  body.append(f'{i:06d} | ' + ('[OMITTED: non-scientific conversation or execution metadata]' if i in omitted else line))
 return ('\n'.join(header+body)+'\n').encode(), sorted(omitted)

def freeze(root):
 program_raw=(root/'semantic_explorer/research/program.json').read_bytes(); program=json.loads(program_raw)
 ledger_raw=(root/'verification/status_ledger.csv').read_bytes()
 ledger=list(csv.DictReader(io.StringIO(ledger_raw.decode())))
 registry_raw=(root/'verification/script_registry.csv').read_bytes()
 registry=list(csv.DictReader(io.StringIO(registry_raw.decode())))
 predictions_raw=(root/'verification/predictions_frozen.json').read_bytes();predictions=json.loads(predictions_raw)
 source_head=git(root,'rev-parse','HEAD'); public_head=git(root,'rev-parse','origin/main')
 tree={}
 for line in git(root,'ls-tree','-r',public_head).splitlines():
  meta,path=line.split('\t',1);tree[path]=meta.split()[2]
 rawcache={};sources={};errors=[];artifacts=[]
 def source(s):
  path=s['path'];a=s['line_start'];b=s['line_end'];key=f"{path}:{s['sha256']}:{a}:{b}"
  ident='source:'+sha(key.encode())[:24]
  if ident in sources:return sources[ident]
  q=Path(path)
  if q.is_absolute() or '..' in q.parts or not path.startswith(APPROVED):
   errors.append({'sourceId':ident,'path':path,'reason':'outside approved scientific publication roots'})
   item={'id':ident,'path':path,'sha256':s['sha256'],'lineStart':a,'lineEnd':b,'href':None,'freshness':'not-published','publicationState':'withheld-root'}
   sources[ident]=item;return item
  if path not in rawcache:rawcache[path]=(root/path).read_bytes()
  raw=rawcache[path];actual=sha(raw);n=len(raw.splitlines())
  if actual!=s['sha256'] or not 1<=a<=b<=n:
   raise ValueError(f'Invalid source SHA/range: {path}:{a}-{b}; expected {s["sha256"]}, actual {actual}, lines {n}')
  payload,omitted=excerpt_bytes(path,raw,a,b);filename=f'sources/{ident.split(":")[1]}.txt'
  write(PUBLIC/filename,payload);artifacts.append({'path':filename,'sha256':sha(payload)})
  blob=hashlib.sha1(f'blob {len(raw)}\0'.encode()+raw).hexdigest()
  remote=f'https://github.com/sthamann/tfpt/blob/{public_head}/{quote(path)}#L{a}-L{b}' if tree.get(path)==blob else None
  item={'id':ident,'path':path,'sha256':actual,'lineStart':a,'lineEnd':b,'href':'/research/'+filename,
        'freshness':'current-at-snapshot','publicationState':'bounded-sanitized-excerpt' if omitted else 'bounded-excerpt',
        'excerptSha256':sha(payload),'omittedOriginalLines':omitted,'remoteHref':remote,
        'historicalSource':historical(path)}
  sources[ident]=item;return item
 findings=[];problems=[];display_edits=[];excluded=[]
 for p in program['problems']:
  findings_ids=[]
  for f in p['findings']:
   if f['id'] in ADMIN_IDS:
    excluded.append({'id':f['id'],'reason':ADMIN_IDS[f['id']],'status':f['status']});continue
   textfields={};edits=[]
   for name in ('title','statement','scope'):
    textfields[name+'EN'],removed=safe_text(f[name]);edits+=removed
   if edits:display_edits.append({'id':f['id'],'reason':list(dict.fromkeys(edits))})
   refs=[source(s) for s in f['sources']]
   findings.append({'id':f['id'],**textfields,'status':f['status'],'problemId':p['id'],'topicIds':p['topics'],
     'goalIds':p['goals'],'premiseIds':f['premise_ids'],'attemptIds':f['attempt_ids'],'sources':refs,
     'historical':all(s['historicalSource'] for s in refs),
     'publicationNotes':list(dict.fromkeys(edits)),'language':'en' if f['statement'].get('en') else 'de'})
   findings_ids.append(f['id'])
  problems.append({'id':p['id'],'titleEN':english(p['title']),'questionEN':english(p['question']),
    'topicIds':p['topics'],'goalIds':p['goals'],'acceptedPremiseIds':p['accepted_premise_ids'],
    'findingIds':findings_ids,
    'tasks':[{'id':t['id'],'titleEN':english(t['title']),'status':t['status'],
      'resolutionIds':t.get('resolution_ids',[]),'requiredPremiseIds':t.get('required_premise_ids',[])} for t in p['tasks']]})
 used={i for f in findings for i in f['premiseIds']}|{i for p in problems for i in p['acceptedPremiseIds']}|{i for p in problems for t in p['tasks'] for i in t['requiredPremiseIds']}
 premises=[{'id':p['id'],'titleEN':safe_text(p['title'])[0],'statementEN':safe_text(p['statement'])[0]} for p in program['premises'] if p['id'] in used]
 ledgers=[{'id':r['claim_id'],'claim':r['claim'],'status':r['status'],'canonicalStatus':r['canonical_status'],
    'dependencies':r['dependencies'],'scripts':[x.strip() for x in re.split('[;,]',r['script']) if x.strip() and x.strip()!='-'],
    'script':r['script'],'location':r['location'],'externalData':r['external_data'],'supersedes':r['supersedes'],
    'active':r['active'].lower()=='true','historical':r['active'].lower()!='true',
    'sourceHref':'/research/status-ledger.csv','sourceLine':i+2} for i,r in enumerate(ledger)]
 write(PUBLIC/'status-ledger.csv',ledger_raw);artifacts.append({'path':'status-ledger.csv','sha256':sha(ledger_raw)})
 write(PUBLIC/'predictions-frozen.json',predictions_raw);artifacts.append({'path':'predictions-frozen.json','sha256':sha(predictions_raw)})
 manifest={
  'allReviewedFindingIds':[f['id'] for p in program['problems'] for f in p['findings']],
  'eligibleFindingIds':[f['id'] for f in findings], 'excludedFindings':excluded,
  'allLedgerIds':[r['claim_id'] for r in ledger], 'activeLedgerIds':[r['claim_id'] for r in ledger if r['active']=='true'],
  'problemIds':[p['id'] for p in program['problems']], 'premiseIds':[p['id'] for p in premises],
  'sourceRefIds':list(sources),
  'findingContracts':{f['id']:{'status':f['status'],'scopeSha256':sha(english(f['scope']).encode()),'premiseIds':f['premise_ids'],
    'sourceCount':len(f['sources'])} for p in program['problems'] for f in p['findings'] if f['id'] not in ADMIN_IDS},
  'predictionIds':{k:[r['id'] for r in predictions[k]] for k in ('predictions','assigned_texture_values','conditional_bands','derived_variants_not_predictions')},
  'sourceOmissions':errors,'publicDisplayEdits':display_edits,
  'privacyPolicy':'Only reviewed scientific records and bounded cited scientific excerpts. No generated AI annotations, private paper inputs, chats, credentials or complete private Atlas overlay. Excerpt omissions are explicit by original line.',
  'omittedPremiseAttributions':[p['id'] for p in program['premises'] if p['id'] in used and (safe_text(p['title'])[1] or safe_text(p['statement'])[1])],
  'scope':'Exact coverage of the frozen active/inactive ledger and eligible reviewed decision records, not every paper section or all unreviewed attempts; no fresh proof execution.'
 }
 snap={'schemaVersion':1,'meta':{'generatedAt':datetime.now(timezone.utc).isoformat(),'sourceRevision':program['revision'],
  'sourceCommit':source_head,'publicSourceCommit':public_head,
  'inputHashes':{'reviewedProgram':sha(program_raw),'statusLedger':sha(ledger_raw),'scriptRegistry':sha(registry_raw),'predictions':sha(predictions_raw)},
  'notice':'Statuses remain in their original stated scope. A reviewed decision or a matching source hash is not a fresh proof run or closure of its parent physical goal.'},
  'ledger':ledgers,'findings':findings,'problems':problems,'premises':premises,'predictions':predictions,
  'scripts':[{'id':r['script'],'cluster':r['cluster'],'descriptionEN':r['what_web']} for r in registry],
  'sourceRefs':list(sources.values()),'expectedCoverage':manifest,'artifacts':artifacts}
 # No read after this point may mix a later authoring revision into this snapshot.
 if (root/'semantic_explorer/research/program.json').read_bytes()!=program_raw:
  raise ValueError('Reviewed authoring program changed during freeze; no coherent snapshot published. Retry live export.')
 return snap

def build(snap):
 manifest=snap['expectedCoverage'];counts={'ledgerTotal':len(snap['ledger']),'ledgerActive':sum(r['active'] for r in snap['ledger']),
 'reviewedFindings':len(snap['findings']),'reviewedFindingsBeforePrivacyFilter':len(manifest['allReviewedFindingIds']),
 'reviewedProblems':len(snap['problems']),'premises':len(snap['premises']),'registeredScripts':len(snap['scripts']),
 'sourceRefs':len(snap['sourceRefs']),'sourceFiles':len({s['path'] for s in snap['sourceRefs']}),
 'findingStatuses':dict(collections.Counter(f['status'] for f in snap['findings'])),
 'predictionCategories':{k:len(v) for k,v in manifest['predictionIds'].items()},
 'excludedAdministrativeFindings':len(manifest['excludedFindings']),
 'sourcesWithExplicitOmissions':sum(bool(s.get('omittedOriginalLines')) for s in snap['sourceRefs'])}
 coverage={**manifest,'counts':counts,'checks':{'exactLedgerIds':True,'exactEligibleFindingIds':True,
 'exactProblemIds':True,'exactPremiseIds':True,'exactSourceRefIds':True,'allSourceHashesAndRangesValidatedAtFreeze':True,
 'allExcerptHashesValidated':True,'allPremisesResolved':True,'statusScopeAndSourcesPresent':True},
 'freshProofExecution':False}
 data={k:snap[k] for k in ['schemaVersion','ledger','findings','problems','premises','predictions','scripts','sourceRefs']}
 data['meta']={**snap['meta'],'counts':counts,'snapshotSha256':sha(encode(snap))};data['coverage']=coverage
 return data,coverage

def validate(snap, data):
 m=snap['expectedCoverage']
 for key,expected in [('ledger','allLedgerIds'),('findings','eligibleFindingIds'),('problems','problemIds'),('premises','premiseIds'),('sourceRefs','sourceRefIds')]:
  ids=[r['id'] for r in data[key]]
  assert len(ids)==len(set(ids)), f'duplicate {key} IDs'
  assert set(ids)==set(m[expected]),f'missing/extra {key} IDs'
 assert {r['id'] for r in data['ledger'] if r['active']}==set(m['activeLedgerIds'])
 assert set(m['allReviewedFindingIds'])==set(m['eligibleFindingIds'])|{r['id'] for r in m['excludedFindings']}
 premises={p['id'] for p in data['premises']};sourceids={s['id'] for s in data['sourceRefs']}
 for f in data['findings']:
  contract=m['findingContracts'][f['id']]
  assert f['status']==contract['status'] and f['premiseIds']==contract['premiseIds'] and len(f['sources'])==contract['sourceCount'],f['id']
  assert all(f.get(k) for k in ('id','titleEN','statementEN','scopeEN','status','problemId','sources'))
  assert set(f['premiseIds'])<=premises,f['id']
  assert all(s['id'] in sourceids and s['sha256'] and 1<=s['lineStart']<=s['lineEnd'] for s in f['sources'])
 raw_ledger=list(csv.DictReader(io.StringIO((PUBLIC/'status-ledger.csv').read_text())))
 assert len(raw_ledger)==len(data['ledger'])
 for r,original in zip(data['ledger'],raw_ledger):
  assert r['id']==original['claim_id'] and r['claim']==original['claim'] and r['status']==original['status'] and r['canonicalStatus']==original['canonical_status'] and r['dependencies']==original['dependencies'] and r['script']==original['script'],'ledger original text/status changed'
  assert r['sourceHref']
 for ref in data['sourceRefs']:
  assert ref['path'].startswith(APPROVED) and ref['freshness']=='current-at-snapshot' and ref.get('excerptSha256')
  text=(PUBLIC/ref['href'].removeprefix('/research/')).read_text()
  assert not PRIVATE.search('\n'.join(text.splitlines()[8:])),f'private text in excerpt {ref["id"]}'
 for artifact in snap['artifacts']:
  p=PUBLIC/artifact['path'];assert p.is_file() and sha(p.read_bytes())==artifact['sha256'],f'changed/missing excerpt {p}'
 for k,ids in m['predictionIds'].items():assert [r['id'] for r in data['predictions'][k]]==ids
 assert not any(PRIVATE.search(f[k]) for f in data['findings'] for k in ('titleEN','statementEN','scopeEN')), 'Private or personal narrative remains in public finding text'
 assert not any('/Users/' in str(x) or 'local_private' in str(x) for x in [data['ledger'],data['premises']])

def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--source-root',type=Path);ap.add_argument('--frozen-input',type=Path,default=SNAPSHOT);ap.add_argument('--check',action='store_true');args=ap.parse_args()
 if args.source_root and not args.check:
  snap=freeze(args.source_root.resolve());write(SNAPSHOT,encode(snap))
 else:snap=load(args.frozen_input)
 data,coverage=build(snap);validate(snap,data)
 if args.check:
  assert DATA.read_bytes()==encode(data),'generated inventory differs from frozen input'
  assert SUMMARY.read_bytes()==encode(data['meta']),'generated summary differs from frozen meta'
  assert (PUBLIC/'inventory.json').read_bytes()==encode(data),'download differs from UI inventory'
  assert (PUBLIC/'coverage.json').read_bytes()==encode(coverage),'coverage differs from frozen input'
  if args.source_root:
   live=load(args.source_root/'semantic_explorer/research/program.json')
   print(json.dumps({'frozenRevision':snap['meta']['sourceRevision'],'liveRevision':live['revision'],
    'addedReviewedFindingIds':sorted({f['id'] for p in live['problems'] for f in p['findings']}-set(snap['expectedCoverage']['allReviewedFindingIds']))}))
 else:
  write(DATA,encode(data));write(SUMMARY,encode(data['meta']));write(PUBLIC/'inventory.json',encode(data));write(PUBLIC/'coverage.json',encode(coverage))
 print(json.dumps({'ok':True,'mode':'check' if args.check else 'build','revision':data['meta']['sourceRevision'],'counts':data['meta']['counts']}))
if __name__=='__main__':
 try:main()
 except (AssertionError,ValueError,FileNotFoundError,KeyError) as e:sys.exit(f'Inventory validation FAILED: {e}')
