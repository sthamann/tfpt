#!/usr/bin/env python3
"""Local, bounded, proof-obligation planner and Lean registry. NO RH CLAIM."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from proof_search.common import HERE, CATALOG, DATA, REPO, digest, dump, need, read, resolve, sha
from proof_search import registry
from proof_search.kernel_audit import audit, check_receipt
from proof_search.planner import Planner, assess, controls, generate_candidates


def material_inputs():
    files = [*HERE.glob('*.py'), *HERE.glob('*.json'), Path(__file__),
             DATA / 'registry.json', DATA / 'kernel_receipt.json', DATA / 'kernel_declarations.json',
             DATA / 'RuleAdapters.log', DATA / 'RuleAdapters.lean.txt',
             DATA / 'negative_controls.json',
             CATALOG / 'rh_semantic_catalog.json', CATALOG / 'map/rh_concept_map.json',
             CATALOG / 'analysis/research_followups_20260909.json']
    constraints = read(HERE / 'constraints.json')['constraints']
    files += [resolve(c['source']) for c in constraints]
    return {str(p): sha(p) for p in sorted(set(files))}


def prior_art():
    """Offline lexical retrieval over the COMPLETE catalog; never a proof gate."""
    import rhcat
    records = read(CATALOG / 'rh_semantic_catalog.json')['records']
    answer = []
    for recipe in read(HERE / 'knowledge.json')['recipes']:
        tokens = set(rhcat.tokenize(' '.join([recipe['id'], recipe['difference'], *recipe['requires']])))
        ranked = sorted(((rhcat.overlap_score(tokens, r)[0], r['path'], r) for r in records),
                        key=lambda x: (-x[0], x[1]))[:8]
        answer.append({'recipe': recipe['id'], 'retrieval': 'OFFLINE_LEXICAL_NOT_EXHAUSTIVE_SEMANTIC_REVIEW',
                       'hits': [{'path': r['path'], 'round': r['round'], 'score': score,
                                 'outcome': r['outcome'], 'failure_class': r['failure_class'],
                                 'failed_because': r['failed_because']} for score, _, r in ranked]})
    return answer


def make_plan(beam=8, max_expansions=500):
    from proof_search.lean_controls import check_controls
    negative_controls = check_controls()
    index = registry.check()
    knowledge = read(HERE / 'knowledge.json')
    receipt = read(DATA / 'kernel_receipt.json')
    planner = Planner(knowledge, receipt, beam=beam, max_expansions=max_expansions)
    before = material_inputs()
    graph = read(CATALOG / 'map/rh_concept_map.json')
    nodes = {n['id']: n for n in graph['nodes']}
    mappings = {g: v['graph_id'] for g, v in knowledge['goals'].items() if v.get('graph_id')}
    need(set(mappings.values()) <= nodes.keys(), 'PROOF_GOAL_MISSING_FROM_CONCEPT_GRAPH')
    for goal in planner.facts:
        need(nodes[mappings[goal]]['status'] == 'FORMALIZED_LEAN', 'PROVED_GOAL_GRAPH_STATUS_STALE: ' + goal)
    need(nodes[mappings['arch_fixed_constant']]['status'] == 'KILLED_HERE', 'OLD_FIXED_CONSTANT_HISTORY_LOST')
    report = planner.report(['rh', 'native_positive', 'boundary_window', 'positive_bottom'])
    proposals = generate_candidates(knowledge)
    constraints = read(HERE / 'constraints.json')
    report.update(schema_version=1, input_hashes=before, graph_goal_mapping=mappings,
                  registry_scopes=index['scopes'], constraints=constraints,
                  candidates=[{**assess(c, knowledge, planner.facts), 'proposal': c,
                               'obligations': planner.expand(c['target'])} for c in proposals],
                  controls=[assess(c, knowledge, planner.facts) for c in controls(knowledge)],
                  real_lean_negative_controls=negative_controls,
                  prior_art=prior_art(), candidate_kind='CONSTRUCTION_TEMPLATES_NOT_EXPLICIT_NEW_OPERATORS',
                  constraints_are_registered_scope_filters_not_kernel_proofs=True,
                  automatic_external_execution=False, code_generation_or_genetic_evolution=False)
    need(len({r['id'] for r in report['candidates']}) == len(proposals), 'DUPLICATE_CANDIDATE_OBJECT')
    need(material_inputs() == before, 'PLANNER_INPUTS_CHANGED_DURING_RUN')
    dump(DATA / 'plan.json', report)
    (DATA / 'PLAN.md').write_text(render(report), encoding='utf-8')
    dump(DATA / 'plan_receipt.json', {'input_hashes': before,
        'outputs': {str(p): sha(p) for p in [DATA / 'plan.json', DATA / 'PLAN.md']}})
    return report


def render(report):
    knowledge = read(HERE / 'knowledge.json')
    def label(key):
        if key.startswith('prove_recipe:'):
            recipe = key.partition(':')[2]
            return 'Beweis, dass die vorgeschlagene Konstruktion diese Zutaten tatsächlich zum Ziel verbindet (' + recipe + ')'
        return knowledge['goals'].get(key, {}).get('label', key)
    lines = ['# RH: geprüfte Bausteine und nächste Beweispflichten', '',
             '**Kein RH-Beweis.** Dieser Lauf plant Forschung; er startet keine numerischen Jobs.', '',
             '## Was der Planer verwenden darf', '',
             'Nur exakt typisierte, frisch in Lean geprüfte Regeln. Alle Voraussetzungen werden gemeinsam benötigt. '
             'Ein Graphpfad, ein offenes Prop, eine numerische Stichprobe und eine Rezeptliste erzeugen keinen Satz.', '',
             'Bewiesen und wiederverwendbar: ' + '; '.join(label(g) for g in report['known_facts']) + '.', '',
             'Die ARCH-Konstante darf vom festen Test abhängen; FREQ und globale Positivität bleiben offen.', '',
             '## Priorisierte Forschungsrichtungen', '']
    labels = {'rh': 'Vollständige rationale Gabor-Positivität', 'native_positive': 'Native Positivität',
              'boundary_window': 'Vollständige neue Randankopplung', 'positive_bottom': 'Schranken nur für tatsächliche Minimierer'}
    for goal, routes in report['targets'].items():
        lines += ['### ' + labels[goal], '']
        for i, route in enumerate(routes, 1):
            lines += [f"Weg {i}: Alle folgenden Pflichten müssen erfüllt sein.", '']
            lines += ['- ' + label(g) + '.' for g in route['unresolved']]
            lines.append('')
    lines += ['## Grenzen und Kontrolle', '',
              f"{len(report['candidates'])} unterscheidbare Konstruktionsvorlagen, keine neu gefundenen Operatoren oder Beweise. "
              f"{len(report['controls'])} bekannte Grenz- und Fehlerfälle werden getrennt klassifiziert. "
              'Die Einstufung OPEN_CONSTRUCTION bedeutet nur, dass die registrierten Filter diese genaue Vorlage nicht ausschließen.', '',
              'Rangfolge und Kosten sind transparente heuristische Prioritäten, keine gemessenen Durchbruchswahrscheinlichkeiten. '
              'Die Suche ist begrenzt; sie beweist keine Vollständigkeit über alle möglichen Ansätze.', '',
              'Das breite Register erfasst auch nicht einzeln geprüfte und historische Lean-Dateien. '
              'Nur die gesondert attestierten Regeln sind Beweisschritte; Quellenkopien zählen nicht als unabhängige Belege.', '',
              'Vollständige maschinenlesbare Pflichten, Typen, Quellenabdrücke, Katalogtreffer und Kontrollfälle stehen in plan.json.']
    return '\n'.join(lines) + '\n'


def check():
    from proof_search.lean_controls import check_controls
    check_controls()
    registry.check()
    check_receipt(read(DATA / 'kernel_receipt.json'), read(HERE / 'knowledge.json'))
    receipt = read(DATA / 'plan_receipt.json')
    need(receipt['input_hashes'] == material_inputs(), 'PROOF_PLAN_INPUTS_STALE')
    for p, h in receipt['outputs'].items():
        need(Path(p).is_file() and sha(p) == h, 'PROOF_PLAN_OUTPUT_CHANGED: ' + p)
    return True


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('command', choices=['audit', 'index', 'plan', 'check', 'search', 'review-metadata', 'controls'])
    p.add_argument('query', nargs='?', default='')
    p.add_argument('--beam', type=int, default=8)
    p.add_argument('--max-expansions', type=int, default=500)
    args = p.parse_args()
    if args.command == 'audit':
        result = audit(); print('FRESH LEAN RULE AUDIT OK', len(result['modules']), len(result['audits']))
    elif args.command == 'controls':
        from proof_search.lean_controls import run_controls
        print(run_controls()['status'])
    elif args.command == 'review-metadata':
        from proof_search.metadata_review import rebind
        rebind(); print('METADATA REVIEW OK; unchanged exact Lean input; no new proof claimed')
    elif args.command == 'index':
        print(json.dumps(registry.refresh()['scopes'], indent=2))
    elif args.command == 'plan':
        r = make_plan(args.beam, args.max_expansions)
        print(json.dumps({k: r[k] for k in ['status', 'RH_proved', 'known_facts', 'expansions', 'seconds']}, indent=2))
    elif args.command == 'check':
        check(); print('PROOF SEARCH CHECK OK; freshness and rule eligibility, NO RH CLAIM')
    else:
        index = registry.check()
        query = args.query.casefold()
        need(query, 'SEARCH_QUERY_REQUIRED')
        results = [{**d, 'path': row['path'], 'scope': row['scope'], 'sha256': row['sha256']}
                   for row in index['files'] for d in row['declarations']
                   if query in (d['local_name'] + ' ' + d['source_header']).casefold()]
        print(json.dumps(results[:100], ensure_ascii=False, indent=2))
        print(f'Matches: {len(results)}; displayed at most 100; lexical navigation, not proof authorization')


if __name__ == '__main__':
    main()
