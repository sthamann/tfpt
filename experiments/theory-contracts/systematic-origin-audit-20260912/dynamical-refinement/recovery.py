"""Exact logical recovery with an environment, not ground-state postselection.

NON-RH. Derives the three-branch Gram from the pinned finite source.
Checks the decoder in normalized multiplicity coordinates, not a physical
implementation or a fresh full-H5 spectral proof. The five-dimensional
reset is a generic subsystem channel; its source hull is proved separately.
"""
import ast
import hashlib
import json
from pathlib import Path
import sympy as s

SOURCE = Path(__file__).resolve().parent.parent/'refinement/ternary.py'
PIN = '9fbafd5778fc630883046f492f2a86d6693a04ac2a077d93b5ab0738b2db5b31'


def require(ok, label):
    if not ok:
        raise ValueError(label)


def clean(matrix):
    return matrix.applyfunc(s.simplify)


def reset_channel(m, d):
    """C^m tensor C^d -> C^d, with an explicit pure-output dilation.

    Output logical identity is later re-encoded by any selected target B.
    Isometry swaps multiplicity into the environment, rather than deleting it.
    """
    eye = s.eye(d)
    dilation = s.SparseMatrix(m*d,m*d,
        {(d_index*m+tree,tree*d+d_index):1
         for tree in range(m) for d_index in range(d)})
    kraus = [s.kronecker_product(s.eye(m)[j,:],eye) for j in range(m)]
    require(dilation.T*dilation == s.eye(m*d),'logical/environment swap is isometric')
    require(sum((k.H*k for k in kraus),s.zeros(m*d)) == s.eye(m*d),
            'logical recovery channel trace preserving')
    # For a pure logical input, m mutually orthogonal multiplicity states all
    # have the same pure logical output. Isometric dilation must retain their
    # orthogonality in the environment; hence environment dimension >=m.
    logical0 = s.eye(d)[:,0]
    flags = s.Matrix.hstack(*[
        dilation*s.kronecker_product(s.eye(m)[:,j],logical0) for j in range(m)])
    require(flags.H*flags == s.eye(m),'m independent reset records retained in environment')
    require(flags.rank() == m,'conditional minimal environment dimension')
    return dilation,kraus


def main():
    raw = SOURCE.read_bytes()
    require(hashlib.sha256(raw).hexdigest() == PIN,'ternary source pin')
    tree = ast.parse(raw)
    names = {'DIAGRAMS','SELECTION'}
    nodes = [node for node in tree.body if
        (isinstance(node,ast.Assign) and any(isinstance(t,ast.Name) and t.id in names
                                             for t in node.targets))
        or (isinstance(node,ast.FunctionDef) and node.name == 'symbolic_gram')]
    require(len(nodes) == 3,'only reviewed source data and Gram contraction selected')
    env = {'s':s,'require':require}
    exec(compile(ast.Module(body=nodes,type_ignores=[]),str(SOURCE),'exec'),env)
    d = 4
    gram5 = env['symbolic_gram'](s.Integer(d))
    selection = env['SELECTION']
    C = selection*gram5*selection.T/(4*(d+1)**2)
    q = s.Rational(17,20)
    require(C == (1-q)*s.eye(3)+q*s.ones(3),'actual three-branch overlap Gram')
    require(C.det() == s.Rational(243,4000),'three independent tree directions')
    lower = C.cholesky()
    flags = lower.T
    require(clean(flags.H*flags) == C,'exact nonorthogonal Cholesky flag Gram')
    require(all(flags[:,j].H*flags[:,j] == s.ones(1) for j in range(3)),
            'all environment flags normalized')
    require(q != 0 and q != 1,'flags are neither orthogonal classical labels nor identical')
    # Normalized source-span coordinates: the abstract source isometry F
    # satisfies A_j = F (flag_j tensor I4). F is determined on the span by
    # the actual Gram identity; no ambient 1024-space map is silently asserted.
    branches = [s.kronecker_product(flags[:,j],s.eye(d)) for j in range(3)]
    dilation,kraus = reset_channel(3,d)
    for j,branch in enumerate(branches):
        require(clean(branch.H*branch) == s.eye(d),'normalized branch embedding')
        require(clean(dilation*branch) == s.kronecker_product(s.eye(d),flags[:,j]),
                'same logical output with correct nonorthogonal environment flag')
        require(all(clean(k*branch) == flags[r,j]*s.eye(d) for r,k in enumerate(kraus)),
                'all logical matrix units and external references recovered by channel')
    for i in range(3):
        for j in range(3):
            require(clean(branches[i].H*branches[j]) == C[i,j]*s.eye(d),
                    'coherent cross-branch overlaps retained by dilation')
    require(flags.rank() == 3,'pure-target branch recovery needs environment dimension at least three')
    reset_channel(5,d)
    print(json.dumps({'scope':'NON-RH exact abstract subsystem decoder from pinned branch Gram',
        'source_pin':PIN,'d':d,'three_branch_overlap':'17/20',
        'three_branch_span_dimension':12,'minimal_pure_target_environment_three_branches':3,
        'flags_perfectly_distinguishable':False,
        'decoder_trace_preserving':True,'postselection_required_for_this_channel':False,
        'source_physical_implementation_derived':False,
        'five_multiplicity_hull_dimension_if_identified':20,
        'minimal_pure_target_environment_arbitrary_five_multiplicity_reset':5,
        'full_H5_ground_spectrum_recomputed':False,'T1_T8_closed':[]},sort_keys=True))


if __name__ == '__main__':
    main()
