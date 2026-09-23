#!/usr/bin/env python3
"""Single entry for graph-bound RH refresh, retrieval and bounded exploration.

The scheduled Codex agent supplies semantic review and new mathematics. This
runner handles provenance, deterministic controls, retrieval, diversity and
checkpoints. It never executes code carried inside a candidate submission.
"""
import argparse
from contextlib import contextmanager
from datetime import datetime, timezone
import fcntl
import json
import os
from pathlib import Path
import subprocess
import sys

from proof_search.common import CATALOG, REPO, digest, dump, need, read, sha
from research_engine import source_index, explorer

BASE = CATALOG/'research_engine'
GENERATED = BASE/'generated'


@contextmanager
def locked(path=GENERATED/'cycle.lock'):
    path = Path(path); path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('a+') as stream:
        try: fcntl.flock(stream, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError: raise ValueError('ANOTHER_RESEARCH_CYCLE_IS_RUNNING')
        try:
            yield
        finally: fcntl.flock(stream, fcntl.LOCK_UN)


def sync(mode):
    result = subprocess.run([sys.executable,'-B',str(CATALOG/'sync_research.py'),mode],
                            cwd=REPO, text=True, capture_output=True, timeout=600)
    return result


def cycle(limit=6):
    with locked():
        checked = sync('--check')
        rebuilt = False
        if checked.returncode:
            rebuilt = True
            result = sync('--refresh')
            need(result.returncode==0, 'REFRESH_REQUIRES_ATTENTION:\n'+result.stdout[-1600:]+result.stderr[-3600:])
            checked = sync('--check')
        need(checked.returncode==0, 'FINAL_GRAPH_CHECK_FAILED:\n'+checked.stderr[-3000:])
        print('Graph and paper source check passed. Updating the declared source index.', flush=True)
        index = source_index.refresh()
        print('Source index ready. Preparing the bounded cross-family review queue.', flush=True)
        queue = explorer.explore(limit)
        status = {'completed_at': datetime.now(timezone.utc).isoformat(), 'status': 'CYCLE_COMPLETE_RESEARCH_ONLY',
                  'graph_rebuilt': rebuilt, 'source_index': index,
                  'candidate_count': queue['unique_objects'], 'selected': len(queue['selected']),
                  'selected_domains': sorted({x['proposal']['domain'] for x in queue['selected']}),
                  'source_fingerprint': index['source_fingerprint'],
                  'paper_claims': read(BASE/'generated/papers.json')['summary'],
                  'proof_accepted': False, 'RH_proved': False,
                  'next_action': 'Scheduled agent reads relevant originals and performs one bounded explicit-object investigation; records every outcome.'}
        dump(GENERATED/'cycle_status.json', status)
        lines = ['# RH: aktueller autonomer Forschungsdurchgang', '',
                 'Keine neuen Beweisfakten. Vorschläge benötigen Quellen- und Vorarbeitsprüfung.', '',
                 f"Quellen: {index['file_count']}; Textabdeckung: {index['coverage']}. Alle Quellen semantisch geprüft: nein.", '',
                 '## Arbeitsaufträge', '']
        for i, row in enumerate(queue['selected'],1):
            c = row['proposal']
            lines += [f"### {i}. {c['domain']} / {c['method']}", '', c['object'], '',
                      'Kleinster nächster Test: '+c['next_test'], '', 'Abbruch: '+c['stop_condition'], '',
                      'Alle offenen Voraussetzungen:', '', *('- '+o for o in row['assessment']['unresolved']), '',
                      'Vorhandene Vorarbeiten (Originale lesen):', '',
                      *('- '+str(h['round'])+' / '+str(h['failure_class'])+': '+h['path'] for h in row['catalog_precedents']), '']
        (GENERATED/'NEXT.md').write_text('\n'.join(lines)+'\n', encoding='utf-8')
        return status


def submit(path):
    candidate = explorer.validate(read(path))
    candidate['kind'] = 'AGENT_SUBMITTED_EXPLICIT_OBJECT'
    candidate['proof_accepted'] = False; candidate['RH_proved'] = False
    cid = explorer.identifier(candidate)
    destination = BASE/'submissions'/f'{cid}.json'
    if destination.exists():
        need(read(destination)==candidate, 'SAME_OBJECT_DIFFERENT_METADATA: preserve the original submission and record a follow-up result')
    else: dump(destination, candidate)
    return {'id': cid, 'path': str(destination), 'status': 'SUBMITTED_NOT_PROVED'}


def record_result(candidate_id, result, evidence):
    need(len(candidate_id)==20 and all(c in '0123456789abcdef' for c in candidate_id), 'BAD_CANDIDATE_ID')
    allowed = {'REFUTED_SCOPED','FINITE_PASS','INCONCLUSIVE','DUPLICATE','REVIEWED_CANDIDATE'}
    need(result in allowed, 'UNSUPPORTED_RESEARCH_OUTCOME')
    source = Path(evidence).resolve()
    need(source.is_file(), 'EVIDENCE_FILE_MISSING')
    candidates = {explorer.identifier(c):c for c in explorer.generate(
        read(BASE/'motifs.json')['motifs'], read(BASE/'motifs.json')['methods'])}
    candidates.update({p.stem:read(p) for p in (BASE/'submissions').glob('*.json')})
    need(candidate_id in candidates, 'UNKNOWN_CANDIDATE_RESULT')
    # Preserve the exact generated object before recording its first result.
    if not (BASE/'submissions'/f'{candidate_id}.json').exists():
        submit_candidate = {**candidates[candidate_id], 'kind': 'REVIEWED_GENERATED_CONTRACT'}
        dump(BASE/'submissions'/f'{candidate_id}.json', submit_candidate)
    receipt = {'candidate_id': candidate_id, 'result': result, 'evidence': str(source),
               'evidence_sha256': sha(source), 'scope': candidates[candidate_id]['scope'],
               'proof_accepted': False, 'automatic_mathematical_adjudication': False}
    key = digest(receipt)[:20]
    destination = BASE/'results'/f'{candidate_id}-{key}.json'
    if not destination.exists(): dump(destination, receipt)
    history = read(GENERATED/'history.json') if (GENERATED/'history.json').exists() else {}
    history.setdefault(candidate_id,{})['result']=result
    history[candidate_id]['result_evidence']=str(source)
    history[candidate_id]['result_evidence_sha256']=receipt['evidence_sha256']
    dump(GENERATED/'history.json', history)
    return receipt


def concise(result):
    """Keep the full manifest on disk, not in every agent context."""
    if not isinstance(result, dict) or 'source_index' not in result:
        return result
    index=dict(result['source_index'])
    for key in ('changed_files','deleted_files','skipped_symlinks'):
        if key in index:
            index[key+'_count']=len(index.pop(key))
    return {**result, 'source_index':index, 'full_checkpoint':str(GENERATED/'cycle_status.json')}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=['cycle','check','search','claim','status','submit','record-result','controls'])
    parser.add_argument('query', nargs='?', default='')
    parser.add_argument('--limit', type=int, default=6)
    parser.add_argument('--result'); parser.add_argument('--evidence')
    args = parser.parse_args()
    if args.command == 'cycle':
        result = cycle(args.limit)
    elif args.command == 'check':
        checked=sync('--check')
        need(checked.returncode==0, checked.stdout[-2000:]+checked.stderr[-3500:])
        actual=source_index.discover()
        need(read(GENERATED/'source_manifest.json')['fingerprint']==actual['fingerprint'], 'SOURCE_INDEX_STALE_RUN_CYCLE')
        result={'status':'GRAPH_AND_INDEX_CURRENT', 'all_sources_semantically_reviewed':False}
    elif args.command == 'search':
        result=source_index.search(args.query,args.limit)
    elif args.command == 'claim':
        import paper_knowledge
        paper_knowledge.check()
        result=[c for c in read(paper_knowledge.OUTPUT)['claims'] if args.query.lower() in json.dumps(c).lower()]
    elif args.command == 'submit':
        with locked(): result=submit(args.query)
    elif args.command == 'record-result':
        with locked(): result=record_result(args.query,args.result,args.evidence)
    elif args.command == 'controls': result=explorer.exact_controls()
    else:
        result=read(GENERATED/'cycle_status.json') if (GENERATED/'cycle_status.json').exists() else {'status':'NOT_RUN'}
    print(json.dumps(concise(result), ensure_ascii=False, indent=2))


if __name__=='__main__':
    try: main()
    except (ValueError, OSError, subprocess.SubprocessError) as exc:
        print('RESEARCH CYCLE STOP: '+str(exc),file=sys.stderr)
        raise SystemExit(1)
