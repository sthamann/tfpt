#!/usr/bin/env python3
"""Export a bounded public scientific inventory, or reproduce/check its frozen snapshot.

Live mode reads reviewed research authoring and cited source ranges from the
research root, and published ledger/registry/module inputs from the publication
checkout. It never imports the generated/private Atlas graph. Source
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
ATLAS = WEBSITE / 'lib/semantic-atlas.json'
FOUNDATION = WEBSITE / 'lib/foundation-index.json'
SNAPSHOT = PUBLIC / 'research-snapshot.json'
APPROVED = ('experiments/theory-contracts/', 'experiments/lean4-carrier-rigidity/',
            'documents/', 'verification/', 'docs/research/', 'tex-artefacts/', 'tfpt_explorer/')
# Explicit public source owners cited by reviewed findings. This is not approval
# of either entire archive/discovery tree; all other paths keep their boundary.
APPROVED_FILES = {
 '_archive/paper-latex/old/improvedcubic.tex',
 'experiments/tfpt-discovery/tfpt2p1d_master_assembly_probe.py',
 'experiments/tfpt-discovery/spin10_det16_projector_probe.py',
}
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
def science_allowed(path): return path.startswith(APPROVED) or path in APPROVED_FILES

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
  (r'the next F1 wording is corrected to the new user request', 'the next F1 wording is corrected to the current source-identification question'),
  (r';user request unfulfilled\.', ';the primitive source-identification objective remains open.'),
  (r"although the user's actual viewed article is not uniquely known", 'although the specific press article is not uniquely identified'),
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

def semantic_snapshot(root, program, findings, premises, source_refs):
 """Public authored semantics plus original inventoried attempt metadata.

 Never read papers.json, annotation caches, embeddings or the private overlay.
 Historical source pins are checked but are not silently refreshed: stale pins
 remain stale handles. Attempt verdicts retain their unreviewed source status.
 """
 paths=['semantic_explorer/orientation.json','semantic_explorer/theory_map.json',
        'semantic_explorer/data/context.json']
 raw={p:(root/p).read_bytes() for p in paths}
 orientation=json.loads(raw[paths[0]]);theory=json.loads(raw[paths[1]]);context=json.loads(raw[paths[2]])
 src_index={s['id']:s for s in context['sources']};handles={s['id']:dict(s) for s in source_refs}
 omitted=[];file_cache={}
 def clean(value, record_id, field):
  if value is None:return None
  text=safe_text({'en':str(value)})[0]
  if PRIVATE.search(text) or (field not in ('titleEN','questionEN') and NARRATIVE.search(text)):
   omitted.append({'id':record_id,'field':field,'reason':'Non-scientific or personal provenance omitted.'})
   return None
  return text
 def handle(ref):
  original_id=ref if isinstance(ref,str) else ref.get('source_id') or ref.get('id')
  s=src_index.get(ref) if isinstance(ref,str) else ref
  if not s:return None
  path=s.get('path','')
  if Path(path).is_absolute():
   try:path=str(Path(path).relative_to(root))
   except ValueError:return None
  if '..' in Path(path).parts or not path or 'local_private' in path or path.startswith(('semantic_explorer/','_newest','private/')):
   return None
  a=s.get('line_start');b=s.get('line_end');expected=s.get('sha256')
  ident=original_id or 'semantic-source:'+sha(f'{path}:{expected}:{a}:{b}'.encode())[:24]
  if ident in handles:return ident
  if path not in file_cache:
   q=root/path;file_cache[path]=q.read_bytes() if q.is_file() else None
  body=file_cache[path];actual=sha(body) if body is not None else None
  valid_range=bool(body is not None and isinstance(a,int) and isinstance(b,int) and 1<=a<=b<=len(body.splitlines()))
  freshness='missing-source' if body is None else 'source-stale' if expected and expected!=actual else 'invalid-range' if a is not None and not valid_range else 'current-at-snapshot' if expected else 'unhashed-navigation'
  matching=next((r for r in source_refs if r['path']==path and r['sha256']==expected and r['lineStart']==a and r['lineEnd']==b),None)
  handles[ident]={'id':ident,'path':path,'sha256':expected,'actualSha256':actual,'lineStart':a,'lineEnd':b,
   'freshness':freshness,'publicationState':'public-provenance-metadata','href':matching['href'] if matching else None,
   'notice':'Historical source metadata only; no execution or reviewed conclusion inferred.'}
  return ident
 def refs(items):return list(dict.fromkeys(i for r in items if (i:=handle(r))))
 topics=[]
 for t in orientation['topics']:
  topics.append({'id':t['id'],'titleEN':clean(t.get('label_en') or t['label'],t['id'],'titleEN') or t['id'],
   'summaryEN':clean(t.get('summary_en') or t['summary'],t['id'],'summaryEN') or '',
   'orientation':{k:clean(v,t['id'],k) for k,v in t.get('topic_orientation',{}).items() if k.endswith('_en')},
   'problemIds':[p['id'] for p in program['problems'] if t['id'] in p['topics']],
   'findingIds':[f['id'] for f in findings if t['id'] in f['topicIds']],
   'reviewState':'authored-navigation','sourceRefIds':refs(t.get('source_refs',[]))})
 goals=[{'id':g['id'],'titleEN':g.get('label_en') or g['label'],'summaryEN':g.get('summary_en') or g['summary'],
  'status':g['status'],'topicIds':g.get('topic_ids',[]),'claimIds':g.get('claim_ids',[]),
  'sourceRefIds':refs(g.get('source_refs',[])),'reviewState':'authored-navigation'} for g in orientation['goals']]
 structures=[{'id':s['id'],'titleEN':s.get('label_en') or s['label'],'summaryEN':s.get('summary_en') or s['summary'],
  'epistemic':s.get('epistemic'),'topicIds':s.get('topic_ids',[]),'claimIds':s.get('claim_ids',[]),
  'sourceRefIds':refs(s.get('source_refs',[])),'reviewState':'authored-navigation'} for s in orientation['structures']]
 tasks=[];strategies=[];connections=[];problems=[];relations=[]
 def relation(a,b,kind,review='reviewed-authored',native_id=None,**extra):
  relations.append({'id':native_id or 'semantic-edge:'+sha(f'{a}|{b}|{kind}'.encode())[:24],
   'from':a,'to':b,'type':kind,'reviewState':review,**extra})
 for p in program['problems']:
  pf=[f['id'] for f in findings if f['problemId']==p['id']]
  problems.append({'id':p['id'],'titleEN':english(p['title']),'questionEN':english(p['question']),
   'topicIds':p['topics'],'goalIds':p['goals'],'acceptedPremiseIds':p['accepted_premise_ids'],
   'findingIds':pf,'taskIds':[t['id'] for t in p['tasks']],'strategyIds':[s['id'] for s in p['strategies']],
   'connectionIds':[c['id'] for c in p.get('connections',[])],'reviewedAttemptIds':p.get('reviewed_attempt_ids',[]),
   'reviewState':'reviewed-authored'})
  for tid in p['topics']:relation(p['id'],tid,'about_topic')
  for gid in p['goals']:relation(p['id'],gid,'addresses_goal')
  for t in p['tasks']:
   tasks.append({'id':t['id'],'problemId':p['id'],'titleEN':clean(english(t['title']),t['id'],'titleEN') or t['id'],
    'kind':t.get('kind'),'status':t['status'],'dependsOn':t.get('depends_on',[]),'resolutionIds':t.get('resolution_ids',[]),
    'requiredPremiseIds':t.get('required_premise_ids',[]),'successCriterionEN':clean(english(t.get('success_criterion',{})),t['id'],'successCriterionEN'),
    'nextActionEN':clean(english(t.get('next_action',{})),t['id'],'nextActionEN'),'reviewState':'reviewed-authored'})
   for dep in t.get('depends_on',[]):relation(t['id'],dep,'depends_on')
   for resolved in t.get('resolution_ids',[]):relation(t['id'],resolved,'resolved_by')
   for prem in t.get('required_premise_ids',[]):relation(t['id'],prem,'requires_premise')
  for s in p['strategies']:
   strategies.append({'id':s['id'],'problemId':p['id'],'titleEN':clean(english(s['title']),s['id'],'titleEN') or s['id'],
    'outcome':s['outcome'],'premiseIds':s.get('premise_ids',[]),'findingIds':s.get('finding_ids',[]),
    'explanationEN':clean(english(s.get('explanation',{})),s['id'],'explanationEN'),
    'changesRequiredEN':clean(english(s.get('changes_required',{})),s['id'],'changesRequiredEN'),'reviewState':'reviewed-authored'})
   for fid in s.get('finding_ids',[]):relation(s['id'],fid,'records_outcome')
  for c in p.get('connections',[]):
   connections.append({'id':c['id'],'problemId':p['id'],'targetProblemId':c['target_problem_id'],'kind':c['kind'],
    'premiseIds':c.get('premise_ids',[]),'findingIds':c.get('finding_ids',[]),
    'explanationEN':clean(english(c.get('explanation',{})),c['id'],'explanationEN'),'reviewState':'reviewed-authored'})
   relation(p['id'],c['target_problem_id'],c['kind'],native_id=c['id'],premiseIds=c.get('premise_ids',[]),findingIds=c.get('finding_ids',[]))
 for f in findings:
  relation(f['problemId'],f['id'],'records_finding')
  for prem in f['premiseIds']:relation(f['id'],prem,'requires_premise')
  for aid in f['attemptIds']:relation(f['id'],aid,'source_review_of')
 attempts=[]
 for n in context['nodes']:
  if n['type']!='attempt':continue
  a=n['attrs'];ident=n['id'];sources=refs(a.get('source_refs',[]))
  attempts.append({'id':ident,'titleEN':clean(a.get('name') or n['label'],ident,'titleEN') or ident,
   'questionEN':clean(a.get('question') or a.get('observable'),ident,'questionEN'),
   'date':a.get('date'),'kind':a.get('attempt_kind'),'status':a.get('status'),
   'verdictRaw':clean(a.get('verdict_raw'),ident,'verdictRaw'),'verdictClass':a.get('verdict_class'),
   'stage':a.get('stage'),'evidenceClass':a.get('evidence_class'),'domain':a.get('domain'),
   'scopeEN':clean(a.get('scope') or a.get('claim_scope'),ident,'scopeEN'),
   'sourceRefIds':sources,'historical':True,'reviewState':'inventoried-not-reviewed',
   'reviewedFindingIds':[f['id'] for f in findings if ident in f['attemptIds']],
   'notice':'Original historical attempt metadata. A reported PASS is not a reviewed theorem, a fresh run or physical completion.'})
 attemptids={a['id'] for a in attempts}
 for ident in sorted({a for f in findings for a in f['attemptIds']}-attemptids):
  attempts.append({'id':ident,'titleEN':ident,'kind':'referenced-attempt','reviewState':'referenced-without-inventory',
   'historical':False,'sourceRefIds':[],'reviewedFindingIds':[f['id'] for f in findings if ident in f['attemptIds']],
   'notice':'Referenced by a reviewed finding; no original attempt inventory record is available in this frozen context.'})
 for e in context['edges']:
  if e['src'] not in attemptids and e['dst'] not in attemptids:continue
  method=e.get('attrs',{}).get('method')
  # Topic mapping/candidate/LLM edges are not established semantic relationships.
  if method in ('topic_mapping','llm') or e['type']=='about':continue
  relation(e['src'],e['dst'],e['type'],'inventoried-not-reviewed',e['id'])
 patterns=[]
 for c in theory.get('patterns',[]):
  if not c.get('reviewed'):continue
  patterns.append({'id':c['id'],'titleEN':c.get('label_en'),'summaryEN':c.get('summary_en'),'kind':c['kind'],
   'relatedIds':c.get('related_ids',[]),'conditions':[r.get('label_en') or r.get('label_de') for r in c.get('conditions',[])],
   'counterevidence':[r.get('label_en') or r.get('label_de') for r in c.get('counterevidence',[])],
   'sourceRefIds':refs(c.get('source_refs',[])),'reviewState':'source-reviewed-relationship',
   'reviewScope':c.get('review_scope')})
 for e in orientation.get('relations',[]):
  relation(e['src'],e['dst'],e['type'],'authored-navigation',
   explanationEN=clean(e.get('explanation_en'),e['src'],'relationExplanation'),
   explanationDE=clean(e.get('explanation'),e['src'],'relationExplanation'),
   conditionsDE=[clean(c,e['src'],'relationCondition') for c in e.get('conditions',[])],
   sourceRefIds=refs(e.get('source_refs',[])))
 included={r['id'] for group in (topics,goals,structures,problems,findings,premises,tasks,strategies,connections,attempts) for r in group}
 external=sorted({r[k] for r in relations for k in ('from','to') if r[k] not in included})
 for r in relations:
  r['fromState']='included' if r['from'] in included else 'external-reference'
  r['toState']='included' if r['to'] in included else 'external-reference'
 sem={'schemaVersion':1,'topics':topics,'goals':goals,'structures':structures,'problems':problems,
  'findings':[{**{k:v for k,v in f.items() if k!='sources'},'sourceRefIds':[s['id'] for s in f['sources']],'reviewState':'reviewed-authored'} for f in findings],
  'premises':premises,'tasks':tasks,'strategies':strategies,'connections':connections,'patterns':patterns,
  'attempts':attempts,'relations':relations,'sourceRefs':list(handles.values()),
  'coverage':{'attemptInventoryDate':context['meta'].get('generated_at'),'attemptInventoryIds':sorted(attemptids),
   'excludedAdministrativeRecordIds':list(ADMIN_IDS),
   'externalRelationEndpointIds':external,
   'omittedNonScientificFields':omitted,'sourceFreshness':dict(collections.Counter(s['freshness'] for s in handles.values())),
   'notice':'Exact authored memberships and typed research connections. Historical inventory excludes inferred topic/LLM edges. No private paper overlay or generated AI science annotations.'},
  'inputHashes':{p:sha(b) for p,b in raw.items()}}
 for path,body in raw.items():
  if (root/path).read_bytes()!=body:raise ValueError(f'Semantic authoring source changed during freeze: {path}')
 return sem

def module_publication_snapshot(root, snap, foundation):
 """Add source documents for older executable mirrors, without changing science.

 This also supports augmentation of an existing coherent snapshot. Only the
 bytes already identified by its frozen module source digest may be read in.
 """
 older=[]
 for module in foundation['modules']:
  mirror=WEBSITE/'public/verification'/module['filename']
  assert mirror.is_file(),f'Missing public module mirror: {module["id"]}'
  mirror_hash=sha(mirror.read_bytes());matches=mirror_hash==module['sourceSha256']
  module.update(pubMirrorHref='/verification/'+module['filename'],pubMirrorHash=mirror_hash,
   pubMirrorMatchesSnapshot=matches,snapshotSourceHref='/verification/'+module['filename'])
  if matches:continue
  raw=(root/module['path']).read_bytes()
  assert sha(raw)==module['sourceSha256'],f'Original module changed since freeze: {module["id"]}; cannot augment snapshot'
  a,b=1,len(raw.splitlines());payload,omitted=excerpt_bytes(module['path'],raw,a,b)
  filename='sources/module-'+module['sourceSha256'][:24]+'.txt';write(PUBLIC/filename,payload)
  module.update(snapshotSourceHref='/research/'+filename,snapshotSourceLineStart=a,snapshotSourceLineEnd=b,
   snapshotExcerptSha256=sha(payload),snapshotOmittedOriginalLines=omitted,
   publicationNotice='The executable publication mirror is older than the frozen source. The line-numbered text is an inert source document, not an executed or newly validated checker.')
  artifact={'path':filename,'sha256':sha(payload)}
  snap['artifacts']=[x for x in snap['artifacts'] if x['path']!=filename]+[artifact]
  older.append(module['id'])
 foundation['coverage']['modulePublication']={'moduleCount':len(foundation['modules']),
  'matchingPublicationMirrorCount':len(foundation['modules'])-len(older),'olderPublicationMirrorCount':len(older),
  'olderPublicationMirrorIds':older,
  'notice':'Publication source correspondence only. Matching bytes and inert source documents do not assert successful execution or promote scientific status.'}

def foundation_snapshot(root, snap, publication_root=None):
 """Join published citations/modules to research-authored navigation."""
 publication_root=(publication_root or WEBSITE.parent).resolve()
 paths=['docs/registry/registry.json','semantic_explorer/orientation.json',
        'semantic_explorer/corpus_aspects.json','semantic_explorer/theory_map.json']
 input_roots={p:publication_root if p==paths[0] else root for p in paths}
 raw={p:(input_roots[p]/p).read_bytes() for p in paths}
 registry,orientation,aspects,theory=[json.loads(raw[p]) for p in paths]
 assert registry['publication_scope']=='public_authored_sources'
 active={r['id']:r for r in snap['ledger'] if r['active']}
 sections={s['id']:s for s in registry['sections']}
 evidence={e['id']:e for e in registry['evidence']}
 active_sections={i for d in registry['documents'] if d.get('role')=='active' for i in d['ordered_section_ids']}
 cited=collections.defaultdict(set)
 for r in registry['relations']:
  if r['relation_type'] in ('explicit_claim_identifier','explicit_file_citation','explicit_script_identifier'):
   assert r['from'] in sections and r['to'] in evidence
   cited[r['to']].add(r['from'])
 links=[]
 def memberships(record,basis,path):
  topics=record.get('topic_ids',[])+[i for i in record.get('related_ids',[]) if i.startswith('topic:')]
  claims=record.get('claim_ids',[])+[i.removeprefix('claim:') for i in record.get('related_ids',[]) if i.startswith('claim:')]
  for topic in dict.fromkeys(topics):
   for claim in dict.fromkeys(claims):
    if claim in active:links.append({'topicId':topic,'claimId':claim,'basis':basis,'authoringRecordId':record['id'],'authoringPath':path})
 for r in orientation['structures']:memberships(r,'authored_structure',paths[1])
 for r in aspects['aspects']:memberships(r,'source_reviewed_aspect',paths[2])
 for r in theory['nodes']+theory.get('patterns',[]):memberships(r,'authored_map_membership',paths[3])
 topicclaims=collections.defaultdict(set)
 for r in links:topicclaims[r['topicId']].add(r['claimId'])
 modules=[];source_checks=[]
 for s in snap['scripts']:
  path='verification/'+s['id']+'.py';eid='python_verification:'+path;e=evidence[eid]
  actual=sha((publication_root/path).read_bytes());source_checks.append({'id':s['id'],'path':path,'expectedSha256':e['sha256'],'actualSha256':actual,'current':actual==e['sha256']})
  assert actual==e['sha256'],f'Public registry module source is stale: {path}'
  synopsis,edits=safe_text({'en':s['descriptionEN']})
  if PRIVATE.search(synopsis) or NARRATIVE.search(synopsis):synopsis='';edits.append('Non-scientific synopsis omitted.')
  ids=sorted(cited[eid])
  modules.append({'id':s['id'],'filename':Path(path).name,'path':path,'cluster':s['cluster'],
   'synopsis':synopsis,'publicationNotes':edits,'sourceHref':'/documentation?evidence='+quote(eid,safe=''),
   'sourceSha256':actual,'linkedClaimIds':[i for i in e.get('claim_ids',[]) if i in active],
   'sectionIds':ids,'activeSectionIds':sorted(set(ids)&active_sections),'evidenceId':eid,
   'reviewState':'registered-source-not-executed'})
 modulemap={m['id']:m for m in modules};claims=[]
 for ident,r in active.items():
  mids=[m['id'] for m in modules if ident in m['linkedClaimIds']]
  direct=set(cited['claim:'+ident]);shared={i for m in mids for i in modulemap[m]['sectionIds']}
  ids=direct|shared;topics=sorted(t for t,c in topicclaims.items() if ident in c)
  claims.append({'id':ident,'topicIds':topics,'moduleIds':mids,'sectionIds':sorted(ids),
   'activeSectionIds':sorted(ids&active_sections),'explicitClaimSectionIds':sorted(direct),
   'sharedScriptSectionIds':sorted(shared-direct),'topicMappingState':'authored' if topics else 'unmapped'})
 source_refs={};omissions=[]
 def refs(items):
  result=[]
  for s in items:
   path=s.get('path','')
   if Path(path).is_absolute():
    try:path=str(Path(path).relative_to(root))
    except ValueError:path=''
   if not path or '..' in Path(path).parts or not science_allowed(path):
    omissions.append({'reason':'Outside public scientific provenance roots','path':path or '[non-public path omitted]'});continue
   a,b=s.get('line_start'),s.get('line_end');expected=s.get('sha256')
   ident=s.get('source_id') or 'foundation-source:'+sha(f'{path}:{expected}:{a}:{b}'.encode())[:24]
   body=(root/path).read_bytes();actual=sha(body)
   state='source-stale' if expected and expected!=actual else 'invalid-range' if a is not None and not (isinstance(a,int) and isinstance(b,int) and 1<=a<=b<=len(body.splitlines())) else 'current-at-snapshot' if expected else 'unhashed-navigation'
   source_refs[ident]={'id':ident,'path':path,'sha256':expected,'actualSha256':actual,'lineStart':a,'lineEnd':b,'freshness':state,
    'href':'/documentation?source='+quote(path,safe=''),'publicationState':'public-provenance-metadata'}
   result.append(ident)
  return list(dict.fromkeys(result))
 def text(v):
  if isinstance(v,dict):v=v.get('label_en') or v.get('en') or v.get('label_de') or v.get('de') or ''
  value=safe_text({'en':v or ''})[0]
  return '' if PRIVATE.search(value) or NARRATIVE.search(value) else value
 nodes=[{'id':n['id'],'labelEN':text(n.get('label_en')),'state':n.get('state'),'summaryEN':text(n.get('summary_en')),
  'stage':n.get('stage'),'lane':n.get('lane'),'relatedIDs':n.get('related_ids',[]),'scopeNote':text(n.get('scope_note')),
  'sourceRefIDs':refs(n.get('source_refs',[])),'reviewState':'authored-navigation'} for n in theory['nodes']]
 edges=[{'id':'map-edge:'+sha(f'{i}:{e["from"]}:{e["to"]}:{e["kind"]}'.encode())[:24],
  'from':e['from'],'to':e['to'],'labelEN':text(e.get('label_en')),'kind':e['kind'],
  'conditions':[text(c) for c in e.get('conditions',[])],'sourceRefIDs':refs(e.get('source_refs',[])),
  'reviewState':'authored-navigation'} for i,e in enumerate(theory['edges'])]
 topics=[{'id':t['id'],'titleEN':t.get('label_en') or t['label'],'claimIds':sorted(topicclaims[t['id']]),
  'researchFindingCount':sum(t['id'] in f['topicIds'] for f in snap['findings'])} for t in orientation['topics']]
 mapped={i for v in topicclaims.values() for i in v}
 coverage={'activeClaims':len(active),'registeredModules':len(modules),'authoredTopicMappedClaims':len(mapped),
  'unmappedClaimIds':sorted(set(active)-mapped),'explicitClaimCitationCount':sum(bool(c['explicitClaimSectionIds']) for c in claims),
  'activeDocumentExplicitClaimCitationCount':sum(bool(set(c['explicitClaimSectionIds'])&active_sections) for c in claims),
  'claimsWithPaperNavigation':sum(bool(c['sectionIds']) for c in claims),
  'modulesWithPaperNavigation':sum(bool(m['sectionIds']) for m in modules),
  'publicPaperRegistry':registry['coverage'],'semanticReviewedPaperSections':0,'proofsChecked':False,
  'moduleSourceChecks':source_checks,'sourceOmissions':omissions,
  'notice':'Exact authored topic memberships and literal public citations. Shared script joins are navigation, not theorem equivalence, causality, proof execution or a reviewed assignment of all claims to topics.'}
 result={'schemaVersion':1,'topics':topics,'topicClaimLinks':links,'claims':claims,'modules':modules,
  'theoryMap':{'nodes':nodes,'edges':edges,'sourceRefs':list(source_refs.values()),
   **{k:[{'id':v['id'],'labelEN':v.get('label_en') or v.get('label_de')} for v in theory[k]] for k in ('stages','lanes','states')}},
  'coverage':coverage,'inputHashes':{p:sha(b) for p,b in raw.items()},
  'inputOwners':{p:'publication' if p==paths[0] else 'research' for p in paths},
  'registryHref':'/documentation/registry.json','registrySha256':sha(raw[paths[0]])}
 module_publication_snapshot(publication_root,snap,result)
 for filename in ('registry.json','summary.json'):
  body=raw[paths[0]] if filename=='registry.json' else (publication_root/'docs/registry'/filename).read_bytes()
  write(WEBSITE/'public/documentation'/filename,body)
  snap['artifacts'].append({'path':'../documentation/'+filename,'sha256':sha(body)})
 for path,body in raw.items():assert (input_roots[path]/path).read_bytes()==body,f'Foundation input changed during snapshot: {path}'
 return result

def freeze(root, publication_root=None):
 publication_root=(publication_root or WEBSITE.parent).resolve()
 previous=load(SNAPSHOT) if SNAPSHOT.exists() else None
 program_raw=(root/'semantic_explorer/research/program.json').read_bytes(); program=json.loads(program_raw)
 ledger_raw=(publication_root/'verification/status_ledger.csv').read_bytes()
 ledger=list(csv.DictReader(io.StringIO(ledger_raw.decode())))
 registry_raw=(publication_root/'verification/script_registry.csv').read_bytes()
 registry=list(csv.DictReader(io.StringIO(registry_raw.decode())))
 predictions_raw=(publication_root/'verification/predictions_frozen.json').read_bytes();predictions=json.loads(predictions_raw)
 publication_inputs={'verification/status_ledger.csv':ledger_raw,
  'verification/script_registry.csv':registry_raw,'verification/predictions_frozen.json':predictions_raw}
 source_head=git(root,'rev-parse','HEAD'); public_head=git(publication_root,'rev-parse','origin/main')
 tree={}
 for line in git(publication_root,'ls-tree','-r',public_head).splitlines():
  meta,path=line.split('\t',1);tree[path]=meta.split()[2]
 rawcache={};sources={};errors=[];source_issues=[];artifacts=[]
 def source(s):
  path=s['path'];a=s['line_start'];b=s['line_end'];key=f"{path}:{s['sha256']}:{a}:{b}"
  ident='source:'+sha(key.encode())[:24]
  if ident in sources:return sources[ident]
  q=Path(path)
  if q.is_absolute() or '..' in q.parts or not science_allowed(path):
   errors.append({'sourceId':ident,'path':path,'reason':'outside approved scientific publication roots'})
   item={'id':ident,'path':path,'sha256':s['sha256'],'lineStart':a,'lineEnd':b,'href':None,'freshness':'not-published','publicationState':'withheld-root','historicalSource':historical(path)}
   sources[ident]=item;return item
  if path not in rawcache:rawcache[path]=(root/path).read_bytes()
  raw=rawcache[path];actual=sha(raw);n=len(raw.splitlines())
  if actual!=s['sha256'] or not 1<=a<=b<=n:
   prior=next((r for r in (previous or {}).get('sourceRefs',[]) if r['id']==ident and r.get('excerptSha256') and r.get('href')),None)
   excerpt=PUBLIC/prior['href'].removeprefix('/research/') if prior else None
   if not prior or not excerpt.is_file() or sha(excerpt.read_bytes())!=prior['excerptSha256']:
    raise ValueError(f'Invalid source SHA/range without a previously validated excerpt: {path}:{a}-{b}; expected {s["sha256"]}, actual {actual}, lines {n}')
   item={**prior,'freshness':'source-stale','publicationState':'retained-previously-validated-excerpt',
    'actualSha256':actual,'currentLineCount':n,
    'previouslyValidatedAt':prior.get('previouslyValidatedAt') or previous['meta']['generatedAt'],
    'lastValidatedRevision':prior.get('lastValidatedRevision') or previous['meta']['sourceRevision'],
    'notice':'The current working source differs from the reviewed pin. This unchanged excerpt was validated in the stated earlier snapshot; it is not claimed source-current.'}
   sources[ident]=item
   artifacts.append({'path':prior['href'].removeprefix('/research/'),'sha256':prior['excerptSha256']})
   source_issues.append({'sourceId':ident,'path':path,'lineStart':a,'lineEnd':b,'expectedSha256':s['sha256'],
    'actualSha256':actual,'currentLineCount':n,'currentRangeValid':1<=a<=b<=n,
    'state':'retained-previously-validated-excerpt','lastValidatedRevision':item['lastValidatedRevision']})
   return item
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
  'sourceOmissions':errors,'sourceIssues':source_issues,'publicDisplayEdits':display_edits,
  'privacyPolicy':'Only reviewed scientific records and bounded cited scientific excerpts. No generated AI annotations, private paper inputs, chats, credentials or complete private Atlas overlay. Excerpt omissions are explicit by original line.',
  'omittedPremiseAttributions':[p['id'] for p in program['premises'] if p['id'] in used and (safe_text(p['title'])[1] or safe_text(p['statement'])[1])],
  'scope':'Exact coverage of the frozen active/inactive ledger and eligible reviewed decision records, not every paper section or all unreviewed attempts; no fresh proof execution.'
 }
 snap={'schemaVersion':1,'meta':{'generatedAt':datetime.now(timezone.utc).isoformat(),'sourceRevision':program['revision'],
  'sourceCommit':source_head,'publicSourceCommit':public_head,
  'publicationInputsCommit':git(publication_root,'rev-parse','HEAD'),
  'inputHashes':{'reviewedProgram':sha(program_raw),'statusLedger':sha(ledger_raw),'scriptRegistry':sha(registry_raw),'predictions':sha(predictions_raw)},
  'inputOwners':{'reviewedProgram':'research','statusLedger':'publication','scriptRegistry':'publication','predictions':'publication','publicDocumentRegistry':'publication'},
  'notice':'Statuses remain in their original stated scope. A reviewed decision or a matching source hash is not a fresh proof run or closure of its parent physical goal.'},
  'ledger':ledgers,'findings':findings,'problems':problems,'premises':premises,'predictions':predictions,
  'scripts':[{'id':r['script'],'cluster':r['cluster'],'descriptionEN':r['what_web']} for r in registry],
  'sourceRefs':list(sources.values()),'expectedCoverage':manifest,'artifacts':artifacts}
 snap['semanticAtlas']=semantic_snapshot(root,program,findings,premises,list(sources.values()))
 snap['foundationIndex']=foundation_snapshot(root,snap,publication_root)
 snap['meta']['inputHashes']['publicDocumentRegistry']=snap['foundationIndex']['registrySha256']
 snap['expectedCoverage']['semanticExpectedIds']={k:[r['id'] for r in snap['semanticAtlas'][k]] for k in
  ('topics','goals','structures','problems','findings','tasks','strategies','connections','patterns','attempts','relations','sourceRefs')}
 # No read after this point may mix a later authoring revision into this snapshot.
 if (root/'semantic_explorer/research/program.json').read_bytes()!=program_raw:
  raise ValueError('Reviewed authoring program changed during freeze; no coherent snapshot published. Retry live export.')
 for path,body in publication_inputs.items():
  if (publication_root/path).read_bytes()!=body:
   raise ValueError(f'Publication input changed during freeze: {path}; retry live export.')
 return snap

def build(snap):
 manifest=snap['expectedCoverage'];counts={'ledgerTotal':len(snap['ledger']),'ledgerActive':sum(r['active'] for r in snap['ledger']),
 'reviewedFindings':len(snap['findings']),'reviewedFindingsBeforePrivacyFilter':len(manifest['allReviewedFindingIds']),
 'reviewedProblems':len(snap['problems']),'premises':len(snap['premises']),'registeredScripts':len(snap['scripts']),
 'sourceRefs':len(snap['sourceRefs']),'sourceFiles':len({s['path'] for s in snap['sourceRefs']}),
 'findingStatuses':dict(collections.Counter(f['status'] for f in snap['findings'])),
 'predictionCategories':{k:len(v) for k,v in manifest['predictionIds'].items()},
 'excludedAdministrativeFindings':len(manifest['excludedFindings']),
 'sourcesWithExplicitOmissions':sum(bool(s.get('omittedOriginalLines')) for s in snap['sourceRefs']),
 'reviewedSourceFreshness':dict(collections.Counter(s['freshness'] for s in snap['sourceRefs']))}
 coverage={**manifest,'counts':counts,'checks':{'exactLedgerIds':True,'exactEligibleFindingIds':True,
 'exactProblemIds':True,'exactPremiseIds':True,'exactSourceRefIds':True,
 'allSourceReferencesAuditedAtFreeze':True,'allSourceHashesAndRangesValidatedAtFreeze':not manifest.get('sourceIssues') and not manifest.get('sourceOmissions'),
 'allExcerptHashesValidated':True,'allPremisesResolved':True,'statusScopeAndSourcesPresent':True},
 'freshProofExecution':False}
 data={k:snap[k] for k in ['schemaVersion','ledger','findings','problems','premises','predictions','scripts','sourceRefs']}
 data['meta']={**snap['meta'],'counts':counts,'snapshotSha256':sha(encode(snap))};data['coverage']=coverage
 return data,coverage

def build_semantics(snap, meta):
 sem=dict(snap['semanticAtlas'])
 sem['meta']={**meta,'counts':{k:len(sem[k]) for k in
  ('topics','goals','structures','problems','findings','tasks','strategies','connections','patterns','attempts','relations','sourceRefs')},
  'notice':'Reviewed findings, authored navigation and historical unreviewed attempts retain distinct reviewState values. Typed edges are not automatic proofs.'}
 return sem

def build_foundations(snap,meta):
 result=dict(snap['foundationIndex'])
 result['meta']={k:meta[k] for k in ('generatedAt','sourceRevision','sourceCommit','publicSourceCommit')}
 result['meta']['notice']='Public authored foundation navigation and original registered source synopsis. Current ledger statuses are separate. No fresh proof execution.'
 return result

def validate_source_ref(ref, omissions, artifacts):
 if ref['publicationState']=='withheld-root':
  metadata={'id','path','sha256','lineStart','lineEnd','href','freshness','publicationState','historicalSource'}
  assert set(ref)<=metadata and ref['href'] is None and ref['freshness']=='not-published',f'withheld source carries publication payload: {ref["id"]}'
  assert ref['historicalSource']==historical(ref['path'])
  assert any(o['sourceId']==ref['id'] and o['path']==ref['path'] and o.get('reason') for o in omissions),f'missing withheld-source reason: {ref["id"]}'
  filename='sources/'+ref['id'].split(':',1)[1]+'.txt'
  assert not any(a['path']==filename for a in artifacts) and not (PUBLIC/filename).exists(),f'withheld source has an excerpt artifact: {ref["id"]}'
  return
 assert science_allowed(ref['path']) and ref['freshness'] in ('current-at-snapshot','source-stale') and ref.get('excerptSha256')
 if ref['freshness']=='source-stale':
  assert ref['publicationState']=='retained-previously-validated-excerpt' and ref.get('previouslyValidatedAt') and ref.get('lastValidatedRevision')
  assert ref.get('actualSha256') and ref['actualSha256']!=ref['sha256']
 text=(PUBLIC/ref['href'].removeprefix('/research/')).read_text()
 assert not PRIVATE.search('\n'.join(text.splitlines()[8:])),f'private text in excerpt {ref["id"]}'

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
  validate_source_ref(ref,m.get('sourceOmissions',[]),snap['artifacts'])
 for artifact in snap['artifacts']:
  p=PUBLIC/artifact['path'];assert p.is_file() and sha(p.read_bytes())==artifact['sha256'],f'changed/missing excerpt {p}'
 for k,ids in m['predictionIds'].items():assert [r['id'] for r in data['predictions'][k]]==ids
 assert not any(PRIVATE.search(f[k]) for f in data['findings'] for k in ('titleEN','statementEN','scopeEN')), 'Private or personal narrative remains in public finding text'
 assert not any('/Users/' in str(x) or 'local_private' in str(x) for x in [data['ledger'],data['premises']])
 sem=snap['semanticAtlas'];known=set()
 for k,ids in m['semanticExpectedIds'].items():
  got=[r['id'] for r in sem[k]]
  assert len(got)==len(set(got)) and set(got)==set(ids),f'Semantic duplicate/missing {k}'
  known.update(got)
 assert {r['id'] for r in sem['findings']}==set(m['eligibleFindingIds'])
 assert set(sem['coverage']['attemptInventoryIds'])<={a['id'] for a in sem['attempts']}
 assert all(a['reviewState'] in ('inventoried-not-reviewed','referenced-without-inventory') for a in sem['attempts'])
 assert not any('/Users/' in str(r) or '/home/' in str(r) or 'local_private' in str(r) or 'relations_llm' in str(r) for r in [sem])
 for group in ('topics','findings','goals','structures','patterns','attempts'):
  for r in sem[group]:assert set(r.get('sourceRefIds',[]))<={s['id'] for s in sem['sourceRefs']}
 foundation=snap['foundationIndex'];active={r['id'] for r in data['ledger'] if r['active']}
 for group in ('topics','claims','modules'):
  ids=[r['id'] for r in foundation[group]];assert len(ids)==len(set(ids)),f'Foundation duplicate {group}'
 assert {r['id'] for r in foundation['claims']}==active
 assert {r['id'] for r in foundation['modules']}=={r['id'] for r in snap['scripts']}
 mapped={r['claimId'] for r in foundation['topicClaimLinks']}
 assert mapped|set(foundation['coverage']['unmappedClaimIds'])==active
 assert not mapped&set(foundation['coverage']['unmappedClaimIds'])
 registry_bytes=(WEBSITE/'public/documentation/registry.json').read_bytes()
 assert sha(registry_bytes)==foundation['registrySha256'],'Public source library differs from frozen foundation registry'
 registry=json.loads(registry_bytes);section_ids={s['id'] for s in registry['sections']}
 for r in foundation['claims']+foundation['modules']:
  assert set(r['sectionIds'])<=section_ids and set(r['activeSectionIds'])<=set(r['sectionIds'])
 assert all(c['current'] for c in foundation['coverage']['moduleSourceChecks'])
 older=[]
 for module in foundation['modules']:
  body=(WEBSITE/'public'/module['pubMirrorHref'].lstrip('/')).read_bytes()
  assert sha(body)==module['pubMirrorHash'],f'Changed publication mirror: {module["id"]}'
  assert module['pubMirrorMatchesSnapshot']==(module['pubMirrorHash']==module['sourceSha256'])
  assert module['snapshotSourceHref']
  if module['pubMirrorMatchesSnapshot']:
   assert module['snapshotSourceHref']==module['pubMirrorHref']
  else:
   older.append(module['id'])
   body=(WEBSITE/'public'/module['snapshotSourceHref'].lstrip('/')).read_bytes()
   assert sha(body)==module['snapshotExcerptSha256']
   assert not PRIVATE.search('\n'.join(body.decode().splitlines()[8:])),f'Private metadata in module source excerpt: {module["id"]}'
   assert 1==module['snapshotSourceLineStart']<=module['snapshotSourceLineEnd']
   assert module['sourceSha256'] in body.decode().splitlines()[2]
 assert older==foundation['coverage']['modulePublication']['olderPublicationMirrorIds']
 assert len(older)==foundation['coverage']['modulePublication']['olderPublicationMirrorCount']
 assert not any('/Users/' in str(r) or '/home/' in str(r) or 'local_private' in str(r) for r in [foundation])

def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--source-root',type=Path,help='Research authoring and reviewed source root for a live freeze');ap.add_argument('--publication-root',type=Path,help='Published ledger, registry and module checkout (defaults to this website parent)');ap.add_argument('--frozen-input',type=Path,default=SNAPSHOT);ap.add_argument('--check',action='store_true');ap.add_argument('--augment-module-publication',action='store_true',help='Add only frozen-digest-matching module source documents, without refreshing the research snapshot');args=ap.parse_args()
 if args.augment_module_publication:
  module_root=args.publication_root or args.source_root
  assert module_root and not args.check,'Module publication augmentation requires --publication-root or --source-root and is separate from --check'
  snap=load(args.frozen_input);before=encode(snap['meta'])
  module_publication_snapshot(module_root.resolve(),snap,snap['foundationIndex'])
  assert encode(snap['meta'])==before,'Research cutoff changed during publication augmentation'
  write(SNAPSHOT,encode(snap))
 elif args.source_root and not args.check:
  snap=freeze(args.source_root.resolve(),args.publication_root);write(SNAPSHOT,encode(snap))
 else:snap=load(args.frozen_input)
 data,coverage=build(snap);validate(snap,data);semantics=build_semantics(snap,data['meta']);foundations=build_foundations(snap,data['meta'])
 if args.check:
  assert DATA.read_bytes()==encode(data),'generated inventory differs from frozen input'
  assert SUMMARY.read_bytes()==encode(data['meta']),'generated summary differs from frozen meta'
  assert ATLAS.read_bytes()==encode(semantics),'generated semantic atlas differs from frozen input'
  assert (PUBLIC/'semantic-atlas.json').read_bytes()==encode(semantics),'semantic download differs from frozen input'
  assert FOUNDATION.read_bytes()==encode(foundations),'foundation index differs from frozen input'
  assert (PUBLIC/'foundation-index.json').read_bytes()==encode(foundations),'foundation download differs from frozen input'
  assert (PUBLIC/'inventory.json').read_bytes()==encode(data),'download differs from UI inventory'
  assert (PUBLIC/'coverage.json').read_bytes()==encode(coverage),'coverage differs from frozen input'
  if args.source_root:
   live=load(args.source_root/'semantic_explorer/research/program.json')
   print(json.dumps({'frozenRevision':snap['meta']['sourceRevision'],'liveRevision':live['revision'],
    'addedReviewedFindingIds':sorted({f['id'] for p in live['problems'] for f in p['findings']}-set(snap['expectedCoverage']['allReviewedFindingIds']))}))
 else:
  write(DATA,encode(data));write(SUMMARY,encode(data['meta']));write(PUBLIC/'inventory.json',encode(data));write(PUBLIC/'coverage.json',encode(coverage))
  write(ATLAS,encode(semantics));write(PUBLIC/'semantic-atlas.json',encode(semantics))
  write(FOUNDATION,encode(foundations));write(PUBLIC/'foundation-index.json',encode(foundations))
 print(json.dumps({'ok':True,'mode':'check' if args.check else 'build','revision':data['meta']['sourceRevision'],'counts':data['meta']['counts']}))
if __name__=='__main__':
 try:main()
 except (AssertionError,ValueError,FileNotFoundError,KeyError) as e:sys.exit(f'Inventory validation FAILED: {e}')
