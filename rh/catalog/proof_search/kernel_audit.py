"""Fresh out-of-tree builds and Lean-checked adapters for every executable rule.

No lake update/download, no mutation of original .lean/.olean files. General
candidate code is NOT executed. Only reviewed, source-pinned adapter templates
in knowledge.json are compiled. Numerical search never creates a proof receipt.
"""
from __future__ import annotations

import os
from pathlib import Path
import re
import subprocess
import tempfile
import time

from .common import HERE, DATA, REPO, digest, dump, need, read, sha

STANDARD = {'propext', 'Classical.choice', 'Quot.sound'}
ROOT = REPO / 'rh/lean'
LEAN = Path('/Users/stefanhamann/.elan/bin/lean')


def source_for(module, knowledge):
    if module.startswith('RH.'):
        root = ROOT
    elif module.startswith('TfptCarrier.'):
        root = REPO / 'experiments/lean4-carrier-rigidity'
    else:
        root = Path(knowledge['external_pack'])
    source = root.joinpath(*module.split('.')).with_suffix('.lean')
    need(source.is_file(), 'LEAN_MODULE_SOURCE_MISSING: ' + str(source))
    return source, root


def dependencies(knowledge):
    result, active, done = [], set(), set()
    def visit(module):
        if module in done: return
        need(module not in active, 'LEAN_IMPORT_CYCLE: ' + module)
        active.add(module)
        source, root = source_for(module, knowledge)
        for line in source.read_text().splitlines():
            match = re.fullmatch(r'\s*import\s+([\w.]+)\s*', line)
            if not match: continue
            child = match.group(1)
            if child.startswith(('RH.', 'TfptCarrier.')) or (Path(knowledge['external_pack']) / (child + '.lean')).is_file():
                visit(child)
        active.remove(module)
        done.add(module)
        result.append((module, source, root))
    for module in knowledge['imports']: visit(module)
    return result


def adapter_source(knowledge):
    lines = ['import Lean', *('import ' + x for x in knowledge['imports']),
             'open scoped Topology', 'namespace RHProofSearch']
    for key, goal in knowledge['goals'].items():
        if goal.get('lean'):
            need(re.fullmatch(r'[a-z][a-z0-9_]*', key), 'BAD_GOAL_ID')
            lines.append('def ' + key + ' : Prop := ' + goal['lean'])
    for rule in knowledge['rules']:
        need(re.fullmatch(r'[a-z][a-z0-9_]*', rule['id']), 'BAD_RULE_ID')
        for g in [*rule['requires'], rule['conclusion']]:
            need(knowledge['goals'].get(g, {}).get('lean'), 'RULE_REQUIRES_A_TYPED_GOAL: ' + g)
        inputs = ' '.join(f'(h{i} : {key})' for i, key in enumerate(rule['requires']))
        lines += [f"theorem {rule['id']} {inputs} : {rule['conclusion']} := by", '  ' + rule['proof']]
    lines.append('end RHProofSearch')
    names = ['RHProofSearch.' + r['id'] for r in knowledge['rules']] + knowledge['audit_targets']
    lines += ['#print axioms ' + name for name in names]
    lines += ["", 'open Lean Elab Command in', 'run_cmd do', '  let env ← getEnv',
              '  for name in [' + ', '.join('`' + n for n in names) + '] do',
              '    let some info := env.find? name | throwError "Missing audited declaration"',
              '    let typeText ← liftTermElabM <| do pure (← Meta.ppExpr info.type).pretty',
              '    let row := Json.mkObj [("name", toJson name.toString), ("type", toJson typeText)]',
              '    logInfo m!"TYPE_RECORD {row.compress}"']
    # Exact types for navigation. Deliberately no all-declaration axiom audit:
    # only the selected rule adapters below are authorized for inference.
    modules = [m for m, _, _ in dependencies(knowledge)]
    lines += ['open Lean Elab Command in', 'run_cmd do', '  let env ← getEnv',
              '  for (name, info) in env.constants.toList do',
              '    let moduleName := match env.getModuleIdxFor? name with',
              '      | some idx => env.header.moduleNames[idx.toNat]!.toString',
              '      | none => ""',
              '    if (' + repr(modules).replace("'", '"') + ' : List String).contains moduleName then',
              '      let kind := match info with',
              '        | .thmInfo _ => "theorem"',
              '        | .defnInfo _ => "definition"',
              '        | .axiomInfo _ => "axiom"',
              '        | .opaqueInfo _ => "opaque"',
              '        | .inductInfo _ => "inductive"',
              '        | _ => "generated"',
              '      if kind != "generated" && !name.toString.startsWith "_private" then',
              '        let typeText ← liftTermElabM <| do pure (← Meta.ppExpr info.type).pretty',
              '        let row := Json.mkObj [("name", toJson name.toString), ("module", toJson moduleName), ("kind", toJson kind), ("type", toJson typeText)]',
              '        logInfo m!"KERNEL_RECORD {row.compress}"']
    return '\n'.join(lines) + '\n'


def parse_audits(log):
    import json
    rows = {}
    for name, text in re.findall(r"'([^']+)' depends on axioms:\s*\[([^]]*)\]", log):
        need(name not in rows, 'DUPLICATE_AXIOM_AUDIT: ' + name)
        axioms = sorted(a.strip() for a in text.split(',') if a.strip())
        rows[name] = {'name': name, 'axioms': axioms,
                      'standard_only': set(axioms) <= STANDARD}
    for line in log.splitlines():
        if line.startswith('TYPE_RECORD '):
            row = json.loads(line[len('TYPE_RECORD '):])
            need(row['name'] in rows, 'TYPE_WITHOUT_AXIOM_AUDIT')
            rows[row['name']]['type'] = row['type']
    return rows


def command(args, cwd, env, log, timeout):
    with log.open('w') as stream:
        try:
            run = subprocess.run([str(a) for a in args], cwd=cwd, env=env,
                                 stdout=stream, stderr=subprocess.STDOUT, timeout=timeout)
            return run.returncode
        except subprocess.TimeoutExpired:
            return None


def audit(total_seconds=1800, per_module_seconds=240):
    knowledge = read(HERE / 'knowledge.json')
    plan = dependencies(knowledge)
    before = {str(p): sha(p) for _, p, _ in plan}
    code_hashes = {str(p): sha(p) for p in [HERE / 'knowledge.json', Path(__file__), HERE / 'common.py']}
    version = subprocess.run([str(LEAN), '--version'], cwd=ROOT, capture_output=True, text=True, check=True).stdout.strip()
    run_dir = Path(tempfile.mkdtemp(prefix='rh-proof-search-'))
    build = run_dir / 'objects'
    build.mkdir()
    paths = [build, *sorted((ROOT / '.lake/packages').glob('*/.lake/build/lib/lean'))]
    env = dict(os.environ, LEAN_PATH=':'.join(map(str, paths)))
    rows = []
    started = time.monotonic()
    for module, source, source_root in plan:
        remaining = total_seconds - (time.monotonic() - started)
        need(remaining > 0, 'FRESH_BUILD_TOTAL_BUDGET_EXHAUSTED: ' + str(run_dir))
        obj = build.joinpath(*module.split('.')).with_suffix('.olean')
        obj.parent.mkdir(parents=True, exist_ok=True)
        log = run_dir / (module + '.log')
        t = time.monotonic()
        code = command([LEAN, '-M', '8192', '-DautoImplicit=false', '-R', source_root, '-o', obj, source],
                       ROOT, env, log, min(per_module_seconds, remaining))
        rows.append({'module': module, 'source': str(source), 'sha256': before[str(source)],
                     'exit_code': code, 'seconds': round(time.monotonic()-t, 3), 'log': str(log)})
        dump(run_dir / 'progress.json', rows)
        print(f"fresh {module}: exit={code} seconds={rows[-1]['seconds']}", flush=True)
        need(code == 0, 'FRESH_LEAN_BUILD_FAILED: ' + str(log))
    adapter = run_dir / 'RuleAdapters.lean'
    adapter.write_text(adapter_source(knowledge))
    log = run_dir / 'RuleAdapters.log'
    remaining = total_seconds - (time.monotonic() - started)
    need(remaining > 0, 'FRESH_AUDIT_TOTAL_BUDGET_EXHAUSTED')
    code = command([LEAN, '-M', '8192', adapter], ROOT, env, log, min(240, remaining))
    need(code == 0, 'LEAN_RULE_ADAPTER_AUDIT_FAILED: ' + str(log))
    audits = parse_audits(log.read_text())
    expected = ['RHProofSearch.' + r['id'] for r in knowledge['rules']] + knowledge['audit_targets']
    need(all(n in audits and 'type' in audits[n] for n in expected), 'INCOMPLETE_RULE_AUDIT')
    for rule in knowledge['rules']:
        need(audits['RHProofSearch.' + rule['id']]['standard_only'], 'RULE_USES_UNAPPROVED_AXIOMS: ' + rule['id'])
    need(all(sha(p) == h for p, h in before.items()), 'LEAN_SOURCE_CHANGED_DURING_BUILD')
    need(all(sha(p) == h for p, h in code_hashes.items()), 'ADAPTER_CODE_CHANGED_DURING_BUILD')
    import json
    declarations = [json.loads(line[len('KERNEL_RECORD '):]) for line in log.read_text().splitlines()
                    if line.startswith('KERNEL_RECORD ')]
    need(declarations, 'MISSING_TYPED_NAVIGATION_RECORDS')
    dump(DATA / 'kernel_declarations.json', {
        'status': 'FRESH_IMPORTED_TYPES_NOT_ALL_AXIOM_AUDITED',
        'source_hashes': before, 'declarations': sorted(declarations, key=lambda r: r['name']),
        'authorized_inference_rules': [r['id'] for r in knowledge['rules']],
        'includes_generated_helpers': True, 'private_declarations_included': False})
    receipt = {'schema_version': 1, 'status': 'FRESH_ADAPTERS_KERNEL_CHECKED', 'RH_proved': False,
               'lean_version': version, 'source_hashes': before, 'code_hashes': code_hashes,
               'knowledge_fingerprint': digest(knowledge), 'modules': rows, 'audits': audits,
               'adapter_source': str(adapter), 'adapter_sha256': sha(adapter),
               'adapter_log': str(log), 'adapter_log_sha256': sha(log),
               'run_dir': str(run_dir), 'mathlib_cache_rebuilt': False,
               'kernel_declarations_sha256': sha(DATA / 'kernel_declarations.json'),
               'rules_are_conditional_not_premise_proofs': True,
               'seconds': round(time.monotonic()-started, 3)}
    dump(DATA / 'kernel_receipt.json', receipt)
    # Durable small replay evidence, no copies of original proof sources.
    (DATA / 'RuleAdapters.lean.txt').write_text(adapter.read_text())
    (DATA / 'RuleAdapters.log').write_text(log.read_text())
    return receipt


def check_receipt(receipt, knowledge, check_files=True):
    need(receipt.get('status') == 'FRESH_ADAPTERS_KERNEL_CHECKED', 'NO_FRESH_ADAPTER_RECEIPT')
    need(receipt.get('knowledge_fingerprint') == digest(knowledge), 'KNOWLEDGE_CHANGED_SINCE_LEAN_CHECK')
    if check_files:
        need(set(receipt['source_hashes']) == {str(p) for _, p, _ in dependencies(knowledge)}, 'AUDIT_SOURCE_SCOPE_CHANGED')
        need(set(receipt['code_hashes']) == {str(p) for p in [HERE / 'knowledge.json', Path(__file__), HERE / 'common.py']}, 'AUDIT_CODE_SCOPE_CHANGED')
        for p, h in {**receipt['source_hashes'], **receipt['code_hashes']}.items():
            need(Path(p).is_file() and sha(p) == h, 'LEAN_RULE_DEPENDENCY_CHANGED: ' + p)
        need(sha(DATA / 'RuleAdapters.lean.txt') == receipt['adapter_sha256'], 'ARCHIVED_ADAPTER_CHANGED')
        need(sha(DATA / 'RuleAdapters.log') == receipt['adapter_log_sha256'], 'ARCHIVED_AUDIT_LOG_CHANGED')
        need((DATA / 'RuleAdapters.lean.txt').read_text() == adapter_source(knowledge), 'ADAPTER_NOT_CURRENT_TEMPLATE')
        need(parse_audits((DATA / 'RuleAdapters.log').read_text()) == receipt['audits'], 'AUDIT_RECORD_LOG_MISMATCH')
        need(sha(DATA / 'kernel_declarations.json') == receipt['kernel_declarations_sha256'], 'KERNEL_TYPE_REGISTRY_CHANGED')
    for rule in knowledge['rules']:
        row = receipt['audits'].get('RHProofSearch.' + rule['id'])
        need(row and row.get('type') and set(row['axioms']) <= STANDARD, 'UNATTESTED_RULE: ' + rule['id'])
    return True
