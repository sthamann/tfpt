"""Root-paper claim provenance; no automatic mathematical promotion.

Reviewed annotations are pinned to exact source bytes. Source drift invalidates
their applicability while preserving the previous review, rather than silently
blessing the changed paper. The regular refresh publishes this state.
"""
from pathlib import Path
import re

from proof_search.common import CATALOG, REPO, digest, dump, need, read, sha

REVIEWS = CATALOG / 'research_engine/paper_reviews.json'
OUTPUT = CATALOG / 'research_engine/generated/papers.json'


def inputs(repo=REPO, reviews=REVIEWS):
    data = read(reviews)
    paths = {Path(reviews)}
    for doc in data['papers']:
        paths.update(Path(repo) / p for p in [doc['path'], *doc.get('aliases', [])])
    # All root papers/PDFs and TeX dependencies: newly added papers invalidate
    # freshness even before someone writes a semantic annotation for them.
    paths.update(Path(repo).glob('*.tex'))
    paths.update(Path(repo).glob('*.pdf'))
    base = Path(repo) / 'tex-artefacts'
    if base.exists():
        paths.update(base.rglob('*.tex'))
        paths.update(base.rglob('*.sty'))
    return sorted(paths)


def build(repo=REPO, reviews=REVIEWS):
    data = read(reviews)
    documents, claims, records, review_queue = [], [], [], []
    for doc in data['papers']:
        path = Path(repo) / doc['path']
        text = path.read_text(encoding='utf-8') if path.is_file() else ''
        actual = sha(path) if path.is_file() else None
        fresh = actual == doc['review_sha256']
        aliases = [{'path': p, 'identical': (Path(repo)/p).is_file() and sha(Path(repo)/p) == actual}
                   for p in doc.get('aliases', [])]
        # Aliases may be different versions; retain both, never silently merge.
        documents.append({**doc, 'current_sha256': actual,
                          'review_state': 'SCOPE_REVIEWED_NOT_REFEREED' if fresh else 'STALE_SOURCE',
                          'aliases_current': aliases})
        records.append(record(doc['path'], doc['title'], doc['path'],
                              'Paper source and partial scope review, not a complete proof audit.',
                              [], fresh=False))
        for item in doc['claims']:
            anchor = item.get('anchor', '')
            found = text.find(anchor) if anchor else 0
            state = item['state'] if fresh and found >= 0 else 'STALE_SOURCE'
            claim = {**item, 'paper': doc['path'], 'state': state,
                     'source_line': text.count('\n', 0, found)+1 if found >= 0 else None,
                     'review_sha256': doc['review_sha256'], 'source_sha256': actual,
                     'premise_logic': 'ALL_REQUIRED', 'proof_rule_eligible': False,
                     'scope_review_only': True}
            claims.append(claim)
            records.append(record(doc['path']+'#'+item['id'], item['title'], doc['path'],
                                  item['statement'], item['requires'], fresh=state != 'STALE_SOURCE',
                                  refuted=state == 'REFUTED', claim_id=item['id']))
        # Lexical discovery, not TeX execution or mathematical adjudication.
        # Unreviewed bodies remain fully retrievable and cannot become premises.
        environments = {'theorem', 'lemma', 'proposition', 'corollary', 'conjecture', 'problem', 'definition', 'remark'}
        environments.update(re.findall(r'\\newtheorem\*?\{([^}]+)\}', text))
        pattern = r'\\begin\{('+'|'.join(re.escape(e) for e in sorted(environments))+r')\}(.*?)\\end\{\1\}'
        for match in re.finditer(pattern, text, re.S):
            body = match.group(2)
            labels = re.findall(r'\\label\{([^}]+)\}', body)
            if any(item.get('anchor') and item['anchor'] in body for item in doc['claims']):
                continue
            cid = 'paper-discovered-'+digest([doc['path'], labels or body])[:18]
            title = doc['title']+' / '+(labels[0] if labels else match.group(1)+' at line '+str(text.count('\n',0,match.start())+1))
            statement = 'Unreviewed source statement: '+body.strip()
            claims.append({'id':cid, 'paper':doc['path'], 'title':title, 'state':'SOURCE_DISCOVERED',
                           'statement':statement, 'source_body':body, 'anchor':match.group(0)[:120],
                           'source_line':text.count('\n',0,match.start())+1, 'source_sha256':actual,
                           'requires':['Extract and verify all assumptions, domain restrictions and proof dependencies.'],
                           'premise_logic':'ALL_REQUIRED', 'proof_rule_eligible':False, 'scope_review_only':False})
            records.append(record(doc['path']+'#'+cid,title,doc['path'],statement,[],fresh=False,claim_id=cid))
        for match in re.finditer(r'\\((?:sub)*section)\*?\{([^}\n]+)\}', text):
            review_queue.append({'paper':doc['path'], 'heading':match.group(2),
                                 'source_line':text.count('\n',0,match.start())+1,
                                 'source_sha256':actual, 'semantic_review_complete':False})
    submissions = []
    from research_engine.explorer import validate
    for p in sorted((CATALOG/'research_engine/submissions').glob('*.json')):
        proposal = validate(read(p))
        results = []
        for result_path in sorted((CATALOG/'research_engine/results').glob(p.stem+'-*.json')):
            result = read(result_path)
            evidence = Path(result['evidence'])
            current = sha(evidence) if evidence.is_file() else None
            result['current_evidence_sha256'] = current
            result['effective_result'] = result['result'] if current == result['evidence_sha256'] else 'STALE_EVIDENCE'
            result['record_path'] = str(result_path.relative_to(REPO))
            results.append(result)
            row = record(result['record_path'], 'Reported candidate result '+result['effective_result'], '',
                         'Source-attributed scoped research result; not independently adjudicated.', [], fresh=False)
            row['result_verdict'] = 'REPORTED_'+result['effective_result']
            row['depends_on'] = [str(p.relative_to(REPO)), str(evidence)]
            records.append(row)
        submissions.append({'id': p.stem, 'path': str(p.relative_to(REPO)), 'proposal': proposal, 'results': results})
        records.append(record(str(p.relative_to(REPO)), 'Explicit research candidate '+p.stem, '',
                              proposal['object'], proposal['obligations'], fresh=False))
    records.append(record('rh/catalog/research_cycle.py', 'Graph-bound adaptive research campaign', '',
                          'Source retrieval, scoped constraints and adaptive candidate queue; no autonomous proof promotion.', [], fresh=True))
    known = {d['path'] for d in data['papers']}
    inventory = {str(p.relative_to(repo)): sha(p) if p.is_file() else None
                 for p in inputs(repo, reviews) if p != Path(reviews)}
    return {'schema_version': 1, 'claim_boundary': 'SOURCE REVIEW IS NOT A PROOF; NO RH CLAIM',
            'documents': documents, 'claims': claims, 'records': records, 'submissions': submissions,
            'section_review_queue': review_queue,
            'source_hashes': inventory, 'source_fingerprint': digest(inventory),
            'unreviewed_root_tex': sorted(p.name for p in Path(repo).glob('*.tex') if p.name not in known),
            'summary': {'papers': len(documents), 'claims': len(claims),
                        'scope_reviewed_claims': sum(c['state'] in {'SOURCE_REVIEWED','OPEN','REFUTED'} for c in claims),
                        'discovered_claims_need_review': sum(c['state']=='SOURCE_DISCOVERED' for c in claims),
                        'section_review_targets': len(review_queue),
                        'stale_claims': sum(c['state']=='STALE_SOURCE' for c in claims),
                        'proof_rules_added': 0, 'all_papers_fully_refereed': False}}


def record(path, title, paper, statement, requirements, *, fresh, refuted=False, claim_id=''):
    return {'path': path, 'round': 'paper-claim-audit-20260909', 'role': 'paper_claim' if claim_id else 'paper_source',
            'ledger_ids': [], 'status_raw': 'SCOPE_REVIEWED' if fresh else 'DISCOVERED_NOT_FULLY_REVIEWED',
            'kind': 'DOCUMENTATION', 'family': 'OTHER', 'family_secondary': [],
            'question': 'Scope and dependencies of '+title,
            'mechanism': 'Hash-pinned paper assertion; complete statement and conjunctive prerequisites in research_engine/generated/papers.json.',
            'result_verdict': 'SCOPED_REFUTATION' if refuted else 'SOURCE_SCOPE_ONLY',
            'outcome': 'KILLED' if refuted else 'RESTATED' if fresh else 'OPEN',
            'solved': 'Paper statement and scope transcribed, not independently formalized.' if fresh else '',
            'failed_because': 'The universal rank-two indefiniteness sentence has an exact negative-definite counterexample.' if refuted else '',
            'failure_class': 'STRUCTURAL_MISMATCH' if refuted else 'NOT_APPLICABLE',
            'rh_relevance': 'FINITE_FRAGMENT' if claim_id else 'INFRASTRUCTURE',
            'artifacts': {'probe': None, 'result_json': 'rh/catalog/research_engine/generated/papers.json',
                          'tex': paper, 'lean': [], 'figures': []},
            'reusable': 'Read the unabridged claim, all premises, source hash and review status before use.',
            'depends_on': [paper] if claim_id else [], 'readme_lines': '',
            'confidence': 'high' if fresh else 'low', 'needs_review': not fresh, 'draft': not fresh}


def refresh():
    payload = build()
    dump(OUTPUT, payload)
    return payload


def check():
    need(read(OUTPUT) == build(), 'PAPER_SOURCE_OR_REVIEW_DRIFT')
    return True


def graph_rows():
    payload = read(OUTPUT)
    nodes, edges = [], []
    for doc in payload['documents']:
        nodes.append({'id': doc['id'], 'type': 'METHOD', 'name': doc['title'], 'aliases': [Path(doc['path']).stem],
                      'definition': 'Paper source with hash-bound partial scope review. Individual claims retain separate assumptions, evidence kinds and open limits.',
                      'status': 'OPEN', 'sources': [doc['path']], 'tags': ['root-paper', 'partial-review']})
        edges.append((doc['id'], 'research-question', 'INSTANCE_OF', 'HEURISTIC', doc['path'], 'Document navigation, not proof.'))
        edges.append((doc['id'], doc['path'], 'USED_BY', 'HEURISTIC', doc['path'], 'Canonical paper record.'))
    docs = {d['path']: d for d in payload['documents']}
    for claim in payload['claims']:
        nodes.append({'id': claim['id'], 'type': 'BARRIER' if claim['state']=='REFUTED' else 'METHOD',
                      'name': claim['title'], 'aliases': [claim.get('anchor', '').replace('\\','')],
                      'definition': ' '.join(claim['statement'].split()[:50])+' Full statement and all prerequisites are in paper_claims.json.',
                      'status': 'KILLED_HERE' if claim['state']=='REFUTED' else 'OPEN',
                      'sources': [claim['paper']+':'+str(claim['source_line'] or 1), 'rh/catalog/research_engine/paper_reviews.json'],
                      'tags': ['paper-claim', claim['state'].lower(), 'not-an-executable-proof']})
        edges.append((claim['id'], docs[claim['paper']]['id'], 'SPECIAL_CASE_OF', 'HEURISTIC', claim['paper'], 'Claim in source document.'))
        edges.append((claim['id'], claim['paper']+'#'+claim['id'], 'USED_BY', 'HEURISTIC', claim['paper'], 'Read full claim and prerequisites.'))
        for target in claim.get('graph_requires', []):
            edges.append((claim['id'], target, 'REQUIRES', 'CONDITIONAL', claim['paper'],
                          'All listed requirements are conjunctive. This edge is not a proof adapter.'))
    source = 'rh/catalog/research_cycle.py'
    campaign = 'graph-bound-adaptive-rh-search'
    nodes.append({'id': campaign, 'type': 'METHOD', 'name': 'Graph-bound adaptive RH candidate search', 'aliases': [],
                  'definition': 'Recurring source refresh, lexical retrieval, constrained cross-family contracts and agent-submitted explicit objects. Candidate scores and finite controls never become proof rules.',
                  'status': 'OPEN', 'sources': [source], 'tags': ['autonomous-research', 'no-proof-promotion']})
    edges.append((campaign, source, 'USED_BY', 'HEURISTIC', source, 'Executable research infrastructure, not a theorem prover.'))
    for doc in payload['documents']:
        edges.append((campaign, doc['id'], 'REQUIRES', 'HEURISTIC', source, 'Consume source versions and claim scopes, not just filenames.'))
    for item in payload.get('submissions', []):
        cid = 'candidate-'+item['id']
        nodes.append({'id': cid, 'type': 'METHOD', 'name': 'Research candidate '+item['id'], 'aliases': [],
                      'definition': ' '.join(item['proposal']['object'].split()[:45])+' Source-attributed proposal, not proved.',
                      'status': 'OPEN', 'sources': [item['path']], 'tags': ['agent-submission', 'unproved']})
        edges.append((cid, campaign, 'INSTANCE_OF', 'HEURISTIC', item['path'], 'Exact object and complete conjunctive obligations in source.'))
        edges.append((cid, item['path'], 'USED_BY', 'HEURISTIC', item['path'], 'Result reports retain separate scope and evidence hashes.'))
        for result in item['results']:
            rid = 'candidate-result-'+digest(result['record_path'])[:20]
            nodes.append({'id':rid, 'type':'METHOD', 'name':'Reported result: '+result['effective_result'],
                          'aliases':[], 'definition':'Scoped research result with immutable evidence hash. A report is not an independently accepted proof; read the exact object, scope and original evidence.',
                          'status':'OPEN', 'sources':[result['record_path'],result['evidence']],
                          'tags':['candidate-result',result['effective_result'].lower(),'source-report-not-proof']})
            edges.append((rid,cid,'CO_OCCURS','HEURISTIC',result['record_path'],'Result for this exact candidate; navigation only, not proof implication.'))
            edges.append((rid,result['record_path'],'USED_BY','HEURISTIC',result['record_path'],'Read the outcome, scope and current evidence validity.'))
    return nodes, edges
