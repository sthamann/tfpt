"""Explicit metadata-only rebind; the exact Lean adapter bytes must be unchanged.

No fresh proof is claimed by this operation. It preserves the prior full
source build and axiom audit, and refuses every change to executable types,
rules, imports, audited declarations or the adapter generator itself.
"""
from copy import deepcopy

from .common import HERE, DATA, digest, dump, need, read, sha
from .kernel_audit import adapter_source, check_receipt


def rebind():
    knowledge = read(HERE / 'knowledge.json')
    old = read(DATA / 'kernel_receipt.json')
    need(adapter_source(knowledge) == (DATA / 'RuleAdapters.lean.txt').read_text(),
         'METADATA_REVIEW_CHANGED_LEAN_INPUT; run audit instead')
    new = deepcopy(old)
    new['metadata_reviews'] = [*new.get('metadata_reviews', []), {
        'previous_knowledge_fingerprint': old['knowledge_fingerprint'],
        'next_knowledge_fingerprint': digest(knowledge),
        'scope': 'Explicit metadata review; exact adapter bytes and all proof inputs unchanged'}]
    new['knowledge_fingerprint'] = digest(knowledge)
    new['code_hashes'][str(HERE / 'knowledge.json')] = sha(HERE / 'knowledge.json')
    # This validates every source/code hash, archived adapter, full audit log,
    # typed registry and allowed axiom list, not merely the adapter comparison.
    check_receipt(new, knowledge)
    dump(DATA / 'kernel_receipt.json', new)
    return new
