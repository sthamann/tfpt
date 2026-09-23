"""Incremental full-text navigation over declared RH/TFPT sources.

Every discovered file is hashed in full. Large text and binary files explicitly
report partial/hash-only indexing; their original paths remain available. FTS
retrieval never confers semantic review or theorem status.
"""
from collections import Counter
import os
from pathlib import Path
import re
import sqlite3

from proof_search.common import CATALOG, REPO, digest, dump, need, read, sha

BASE = CATALOG / 'research_engine'
GENERATED = BASE / 'generated'
DB = GENERATED / 'sources.sqlite'
CONFIG = BASE / 'source_scope.json'
TEXT = {'.md', '.tex', '.lean', '.py', '.json', '.jsonl', '.csv', '.toml', '.yaml', '.yml', '.txt', '.sty'}
EXCLUDED = {'.git', '.lake', '.venv', 'venv', 'node_modules', '__pycache__', '.pytest_cache',
            '.mypy_cache', '.cache', 'vendor', 'site-packages', 'dist', 'build', '_newest', '.DS_Store'}


def discover(config=None):
    config = config or read(CONFIG)
    files, skipped = {}, []
    for scope in config['roots']:
        base = Path(scope['path'])
        need(base.is_dir(), 'INDEX_ROOT_UNAVAILABLE: '+str(base))
        for directory, dirs, names in os.walk(base, followlinks=False):
            dirs[:] = sorted(d for d in dirs if d not in EXCLUDED
                             and not (Path(directory)/d/'pyvenv.cfg').is_file())
            # Catalog generated snapshots are indexed as a selected source below,
            # not recursively (which would index this database into itself).
            if Path(directory) == CATALOG:
                dirs[:] = ['analysis', 'fragments']
            for d in list(dirs):
                if (Path(directory)/d).is_symlink():
                    skipped.append(str(Path(directory)/d)); dirs.remove(d)
            for name in sorted(names):
                path = Path(directory)/name
                if name in EXCLUDED or path.is_symlink():
                    if path.is_symlink(): skipped.append(str(path))
                    continue
                if path.is_file() and path.suffix in set(config['extensions']):
                    files[str(path)] = {'scope': scope['id']}
    for source in config['explicit_files']:
        path = Path(source)
        need(path.is_file() and not path.is_symlink(), 'INDEX_SOURCE_UNAVAILABLE: '+str(path))
        files[str(path)] = {'scope': 'registered-knowledge'}
    # Other already registered Lean lanes are available without sweeping unrelated projects.
    registry_path = CATALOG/'proof_search/generated/registry.json'
    if config.get('include_registered_lean', False) and registry_path.is_file():
        for source in read(registry_path)['source_hashes']:
            path = Path(source)
            need(path.is_file() and not path.is_symlink(), 'REGISTERED_LEAN_SOURCE_UNAVAILABLE: '+source)
            files[source] = {'scope': 'registered-lean'}
    for result_path in sorted((BASE/'results').glob('*.json')) if config.get('include_result_evidence', False) else []:
        files[str(result_path)] = {'scope': 'candidate-result-receipt'}
        result = read(result_path)
        path = Path(result['evidence'])
        if path.is_file() and not path.is_symlink():
            files[str(path)] = {'scope': 'candidate-result-evidence'}
        else:
            skipped.append('MISSING_RESULT_EVIDENCE:'+str(path))
    if config.get('include_result_evidence', False):
        for path in sorted((BASE/'submissions').glob('*.json')):
            files[str(path)] = {'scope': 'explicit-research-object'}
    for source, metadata in files.items():
        path = Path(source)
        a = path.stat(); hashed = sha(path); b = path.stat()
        need((a.st_size, a.st_mtime_ns)==(b.st_size, b.st_mtime_ns), 'SOURCE_CHANGED_DURING_INDEX: '+source)
        metadata.update(sha256=hashed, bytes=b.st_size)
    return {'files': files, 'skipped_symlinks': sorted(skipped), 'config': config,
            'fingerprint': digest({'files':files, 'config':config, 'skipped':sorted(skipped)})}


def connection(path=DB, *, readonly=False):
    path = Path(path)
    if readonly:
        return sqlite3.connect('file:'+str(path)+'?mode=ro', uri=True)
    path.parent.mkdir(parents=True, exist_ok=True)
    con = sqlite3.connect(path)
    con.execute('CREATE TABLE IF NOT EXISTS files(path TEXT PRIMARY KEY, sha TEXT, bytes INTEGER, indexed_bytes INTEGER, scope TEXT)')
    con.execute('CREATE VIRTUAL TABLE IF NOT EXISTS content USING fts5(path UNINDEXED, title, body, tokenize="unicode61")')
    return con


def refresh(snapshot=None, *, database=DB, publish=True):
    snapshot = snapshot or discover()
    con = connection(database)
    old = {p: h for p, h in con.execute('SELECT path,sha FROM files')}
    changed, deleted = [], sorted(set(old)-set(snapshot['files']))
    coverage = Counter()
    with con:
        for path in deleted:
            con.execute('DELETE FROM content WHERE path=?', (path,))
            con.execute('DELETE FROM files WHERE path=?', (path,))
        for source, info in sorted(snapshot['files'].items()):
            p = Path(source)
            cap = snapshot['config']['document_text_cap'] if p.suffix in {'.tex','.lean','.md'} else snapshot['config']['other_text_cap']
            amount = min(info['bytes'], cap) if p.suffix in TEXT else 0
            kind = 'full_text' if amount == info['bytes'] else 'partial_text' if amount else 'hash_only'
            coverage[kind] += 1
            if old.get(source) == info['sha256']:
                existing = con.execute('SELECT indexed_bytes FROM files WHERE path=?', (source,)).fetchone()
                if existing and existing[0] == amount: continue
            text = ''
            if amount:
                with p.open('rb') as stream: raw = stream.read(amount)
                text = raw.decode('utf-8', errors='replace')
                need(sha(p)==info['sha256'], 'SOURCE_CHANGED_BEFORE_TEXT_INDEX: '+source)
            if source in old:
                con.execute('DELETE FROM content WHERE path=?', (source,))
            con.execute('INSERT INTO content VALUES(?,?,?)', (source, p.name, text))
            con.execute('INSERT OR REPLACE INTO files VALUES(?,?,?,?,?)',
                        (source, info['sha256'], info['bytes'], amount, info['scope']))
            changed.append(source)
    con.close()
    report = {'source_fingerprint': snapshot['fingerprint'], 'file_count': len(snapshot['files']),
              'file_bytes': sum(v['bytes'] for v in snapshot['files'].values()),
              'coverage': dict(coverage), 'changed_files': changed, 'deleted_files': deleted,
              'skipped_symlinks': snapshot['skipped_symlinks'],
              'all_sources_semantically_reviewed': False, 'all_data_loaded_into_model_context': False,
              'retrieval': 'FTS5 lexical retrieval; source hashes and paths, not complete semantic understanding'}
    if publish:
        dump(GENERATED/'source_manifest.json', snapshot)
        dump(GENERATED/'source_index_status.json', report)
    return report


def search(query, limit=8, *, database=DB):
    need(type(limit) is int and 0 < limit <= 50, 'BAD_RETRIEVAL_LIMIT')
    terms = list(dict.fromkeys(re.findall(r'[\w]{2,}', query.casefold())))[:20]
    if not terms: return []
    con = connection(database, readonly=True)
    try:
        mode='ALL_TERMS'
        for operator in (' AND ', ' OR '):
            expression=operator.join('"'+word+'"' for word in terms)
            rows = con.execute('SELECT path, snippet(content,2,"[", "]"," … ",36), bm25(content,0,4,1) '
                               'FROM content WHERE content MATCH ? ORDER BY bm25(content,0,4,1),path LIMIT ?',
                               (expression, min(500,limit*12))).fetchall()
            if rows: break
            mode='ANY_TERM_FALLBACK'
        unique={}
        for p,excerpt,score in rows:
            content_hash=con.execute('SELECT sha FROM files WHERE path=?',(p,)).fetchone()[0]
            if content_hash in unique:
                unique[content_hash]['identical_source_paths'].append(p)
            elif len(unique)<limit:
                unique[content_hash]={'path':p, 'excerpt':excerpt, 'lexical_rank':score,
                                      'match_mode':mode, 'identical_source_paths':[p],
                                      'semantic_review':'NOT_INFERRED'}
        return list(unique.values())
    finally: con.close()
