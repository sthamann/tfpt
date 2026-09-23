"""Broad source inventory plus separately attested kernel declarations.

Lexical discovery is deliberately NOT an inference rule or a Lean parser.
Only the separate fresh adapter audit authorizes the planner to apply a rule.
"""
from __future__ import annotations

from collections import Counter, defaultdict
import os
from pathlib import Path
import re

from .common import DATA, REPO, digest, dump, need, read, sha

EXCLUDED = {'.lake', '.git', 'node_modules', '.venv', 'venv', 'vendor', '__pycache__'}
DOCS = Path('/Users/stefanhamann/Documents/Codex')
TASK = DOCS / '2026-09-04/scha-2'
DECL = re.compile(r'^\s*(?:(?:private|protected|noncomputable|unsafe|partial)\s+)*'
                  r'(theorem|lemma|def|abbrev|axiom|structure|inductive|class)\s+([^\s(:{\[]+)', re.M)


def strip_lean(text):
    """Remove nested comments and strings, preserving character/line offsets."""
    chars = list(text)
    i = 0
    while i < len(text):
        start = i
        if text.startswith('/-', i):
            level = 1
            i += 2
            while i < len(text) and level:
                if text.startswith('/-', i): level += 1; i += 2
                elif text.startswith('-/', i): level -= 1; i += 2
                else: i += 1
            need(level == 0, 'UNTERMINATED_LEAN_COMMENT')
        elif text.startswith('--', i):
            end = text.find('\n', i)
            i = end if end >= 0 else len(text)
        elif text[i] == '"':
            i += 1
            closed = False
            while i < len(text):
                if text[i] == '\\': i += 2
                elif text[i] == '"': i += 1; closed = True; break
                else: i += 1
            need(closed, 'UNTERMINATED_LEAN_STRING')
        else:
            i += 1
            continue
        for j in range(start, min(i, len(text))):
            if chars[j] != '\n': chars[j] = ' '
    return ''.join(chars)


def source_declarations(source):
    """Navigation records only; exact applied types come from the Lean adapter."""
    text = strip_lean(source)
    out = []
    for match in DECL.finditer(text):
        start = match.start(1)
        end = text.find(':=', match.end())
        next_decl = DECL.search(text, match.end())
        if end < 0 or next_decl and end > next_decl.start():
            end = next_decl.start() if next_decl else len(text)
        header = source[start:end].strip()
        out.append({'kind': match.group(1), 'local_name': match.group(2),
                    'line': source.count('\n', 0, start) + 1,
                    'source_header': header, 'status': 'LEXICAL_NOT_PROOF_CHECKED'})
    flags = []
    for kind, pattern in [('placeholder', r'\b(?:sorry|admit)\b'),
                          ('native_evaluation', r'\bnative_decide\b')]:
        for m in re.finditer(pattern, text):
            flags.append({'kind': kind, 'line': source.count('\n', 0, m.start()) + 1})
    return out, flags


def files_under(root):
    root = Path(root)
    need(root.is_dir(), 'LEAN_SOURCE_ROOT_UNAVAILABLE: ' + str(root))
    for directory, dirs, names in os.walk(root, followlinks=False):
        dirs[:] = sorted(x for x in dirs if x not in EXCLUDED)
        for name in sorted(names):
            if name.endswith('.lean') and name != 'lakefile.lean':
                p = Path(directory) / name
                need(not p.is_symlink(), 'LEAN_SOURCE_SYMLINK_REQUIRES_REVIEW: ' + str(p))
                yield p


def discover(repo=REPO, docs=DOCS, task=TASK):
    rows = []
    for root in [Path(repo) / 'rh/lean', Path(repo) / 'experiments/lean4-carrier-rigidity', Path(docs)]:
        for path in files_under(root):
            if path.is_relative_to(Path(repo) / 'rh/lean'):
                scope = 'rh_main'
                module = path.relative_to(root).with_suffix('').as_posix().replace('/', '.')
            elif path.is_relative_to(Path(repo) / 'experiments/lean4-carrier-rigidity'):
                scope = 'tfpt_carrier'
                module = path.relative_to(root).with_suffix('').as_posix().replace('/', '.')
            else:
                scope = 'current_task' if path.is_relative_to(task) else 'other_workspace_or_archive'
                module = None
            before = sha(path)
            source = path.read_text(encoding='utf-8')
            decls, flags = source_declarations(source)
            need(before == sha(path), 'LEAN_SOURCE_CHANGED_DURING_READ: ' + str(path))
            catalog_path = str(path.relative_to(repo)) if path.is_relative_to(repo) else str(path)
            rows.append({'path': str(path), 'catalog_path': catalog_path, 'module': module,
                         'scope': scope, 'sha256': before, 'lines': len(source.splitlines()),
                         'declarations': decls, 'flags': flags,
                         'review_status': 'DISCOVERED_NOT_SEMANTICALLY_REVIEWED'})
    need(len({r['path'] for r in rows}) == len(rows), 'DUPLICATE_DISCOVERY_SCOPE')
    return sorted(rows, key=lambda r: r['path'])


def drafts(rows):
    """All live Lean sources discoverable in rhcat; archives remain in registry."""
    result = []
    for row in rows:
        if row['scope'] == 'other_workspace_or_archive': continue
        path = row['catalog_path']
        result.append({
            'path': path, 'round': 'lean-source-discovery', 'role': 'lean_module',
            'ledger_ids': [], 'status_raw': 'SOURCE_INDEX_ONLY; individual assumptions and proofs require review',
            'kind': 'FORMALIZATION', 'family': 'LEAN_FORMALIZATION', 'family_secondary': [],
            'question': 'Which declarations and explicit assumptions does this Lean source contain?',
            'mechanism': 'Hash-bound source and declaration inventory; no automatic theorem promotion.',
            'result_verdict': 'DISCOVERED_NOT_REVIEWED', 'outcome': 'OPEN', 'solved': '',
            'failed_because': 'Source discovery alone does not establish any theorem or concrete mathematical applicability.',
            'failure_class': 'NOT_APPLICABLE', 'rh_relevance': 'INFRASTRUCTURE',
            'artifacts': {'probe': None, 'result_json': 'rh/catalog/proof_search/generated/registry.json',
                          'tex': None, 'lean': [path], 'figures': []},
            'reusable': 'Exact source path, hash and declaration navigation; see the separate audited rule registry.',
            'depends_on': [], 'readme_lines': '', 'confidence': 'low', 'draft': True, 'needs_review': True})
    return result


def make_registry(rows, kernel=None):
    duplicates = defaultdict(list)
    for row in rows: duplicates[row['sha256']].append(row['path'])
    sources = {r['path']: r['sha256'] for r in rows}
    counts = {}
    for scope in sorted({r['scope'] for r in rows}):
        group = [r for r in rows if r['scope'] == scope]
        counts[scope] = {'files': len(group), 'unique_contents': len({r['sha256'] for r in group}),
                         'lexical_declarations': sum(len(r['declarations']) for r in group),
                         'flags': dict(Counter(f['kind'] for r in group for f in r['flags']))}
    return {'schema_version': 1, 'claim_boundary': 'Source/declaration registry, not a universal Lean or RH proof',
            'source_fingerprint': digest(sources), 'source_hashes': sources, 'scopes': counts,
            'files': rows, 'duplicate_groups': [p for p in duplicates.values() if len(p) > 1],
            'catalog_records': drafts(rows), 'kernel_snapshot': kernel or None,
            'lexical_entries_are_proofs': False, 'all_sources_semantically_reviewed': False}


def refresh():
    kernel = read(DATA / 'kernel_receipt.json') if (DATA / 'kernel_receipt.json').exists() else None
    result = make_registry(discover(), kernel)
    dump(DATA / 'registry.json', result)
    return result


def check():
    rows = discover()
    current = {r['path']: r['sha256'] for r in rows}
    saved = read(DATA / 'registry.json')
    need(current == saved['source_hashes'], 'LEAN_REGISTRY_STALE_OR_SCOPE_CHANGED')
    kernel = read(DATA / 'kernel_receipt.json') if (DATA / 'kernel_receipt.json').exists() else None
    need(saved == make_registry(rows, kernel), 'LEAN_REGISTRY_CONTENT_OR_AUDIT_STALE')
    return saved
