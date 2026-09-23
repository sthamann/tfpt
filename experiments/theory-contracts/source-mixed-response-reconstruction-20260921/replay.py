#!/usr/bin/env python3
"""Portable targeted replay; requires Python 3 and numpy. No source derivation."""
from pathlib import Path
import importlib.util, contextlib, io, json, hashlib
ROOT=Path(__file__).resolve().parent

def load(name):
    p=ROOT/name/'checker.py'
    spec=importlib.util.spec_from_file_location('mixed_'+name,p)
    mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    return mod

def main():
    algebra=load('algebra'); algebra.NATIVE_TENSOR=ROOT/'native_tensor.npz'
    buf=io.StringIO()
    with contextlib.redirect_stdout(buf): algebra.main()
    inv=load('invariant'); inv.TENSOR=ROOT/'native_tensor.npz'
    inv.SOURCE_CERT=ROOT/'continuous_clock_certificate.json'
    result=inv.main()
    result['pins']['native_tensor']='native_tensor.npz'
    result['pins']['continuous_symmetry_certificate']='continuous_clock_certificate.json'
    payload={'algebra':json.loads(buf.getvalue()),'invariant':result,
             'source_values':{'D_F':None,'g_F':None,'status':'NOT_DERIVED'},
             'complete_TFPT_solution':False,'T1_T8_closed':False}
    print(json.dumps(payload,ensure_ascii=False,indent=2,sort_keys=True))
if __name__=='__main__': main()
