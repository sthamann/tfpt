"""Small deterministic helpers; validation remains active under python -OO."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
CATALOG = HERE.parent
REPO = CATALOG.parent.parent
DATA = HERE / 'generated'


def need(condition, message):
    if not condition:
        raise ValueError(message)


def read(path):
    return json.loads(Path(path).read_text(encoding='utf-8'))


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, ensure_ascii=False,
                                    separators=(',', ':')).encode()).hexdigest()


def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()


def dump(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False) + '\n'
    temporary = path.with_suffix(path.suffix + '.pending')
    temporary.write_text(text, encoding='utf-8')
    temporary.replace(path)


def resolve(path):
    path = Path(path)
    return path if path.is_absolute() else REPO / path
