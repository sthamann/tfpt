"""Independent, small exact CAR review of the parent's complex Gram convention.

No parent helper, tensor archive, repository import or numerical tolerance.
Six fermion modes and two pair channels suffice to distinguish C^dagger C
from C C^dagger. This is a regression cross-check, not by itself a general
proof and not an additional native-W certificate.

Use --replay --output review_parent.json to seal normal/-OO equality.
"""
from pathlib import Path
from hashlib import sha256
from itertools import combinations
import argparse
import ast
import json
import subprocess
import sys
import sympy as s

CHECKS=[]


def need(ok,label):
    if not bool(ok):
        raise RuntimeError(label)
    CHECKS.append(label)


def direct_car(matrices,internal_dimension,sites):
    """Execute f_j f_i on bitmask triples, including both CAR signs.

    This intentionally does not use the parent's three-term cubic helper.
    Row order is site, pair-channel, remaining internal fermion.
    """
    n=internal_dimension*sites
    triples=list(combinations(range(n),3))
    out=s.zeros(n*len(matrices),len(triples))
    for column,triple in enumerate(triples):
        original=sum(1<<j for j in triple)
        for channel,M in enumerate(matrices):
            for i,j in combinations(range(n),2):
                mask=original
                coefficient=M[i,j]
                for operator in [i,j]:
                    if not (mask>>operator)&1:
                        coefficient=0
                        break
                    coefficient*=(-1)**((mask&((1<<operator)-1)).bit_count())
                    mask^=1<<operator
                if coefficient:
                    remaining=mask.bit_length()-1
                    row=(remaining//internal_dimension)*(len(matrices)*internal_dimension)
                    row+=channel*internal_dimension+remaining%internal_dimension
                    out[row,column]+=coefficient
    return out


def certificate():
    C=s.Matrix([[1,s.I],[s.I,0]])
    matrices=[s.Matrix([[0,1,0],[-1,0,0],[0,0,0]]),
              s.Matrix([[0,0,1],[0,0,0],[-1,0,0]])]
    need(C.T==C,"complex site tensor symmetric")
    need(all(A.T==-A and A==A.conjugate() for A in matrices),"both internal pair tensors real antisymmetric")
    need(s.Matrix(2,2,lambda i,j:s.trace(matrices[i]*matrices[j].H)/2)==s.eye(2),
         "internal two-particle Gram is identity in this small witness")
    native=direct_car(matrices,3,1)
    need(native.shape==(6,1) and native.rank()==1,"direct native bitmask contraction dimensions and rank")
    K=s.eye(6)-native*native.H
    independent_blocks=s.BlockMatrix([[B.H*A for B in matrices] for A in matrices]).as_explicit()
    need(K==independent_blocks,"independent CAR block identity K_AB=A_B_dagger A_A")
    lifted=direct_car([s.kronecker_product(C,A) for A in matrices],3,2)
    need(lifted.shape==(12,20),"all twenty three-fermion states and twelve boson-fermion states included")
    G=lifted*lifted.H
    Q=C.H*C
    normalization=s.trace(Q)
    need(normalization==3,"unnormalized site tensor Frobenius square is three")
    correct=normalization*s.eye(12)-s.kronecker_product(Q,K)
    wrong=normalization*s.eye(12)-s.kronecker_product(C*C.H,K)
    need(G==correct,"direct bitmask CAR Gram uses C_dagger C in annihilator convention")
    need((G-wrong).rank()==12,"wrong C C_dagger conjugation has full-rank residual")
    need(G/3==s.eye(12)-s.kronecker_product(Q/3,K),"unit-Frobenius normalization restores identity leading term")
    need(s.trace(K)==4,"internal partial-trace normalization independently nonzero")
    recovered=s.Matrix(2,2,lambda x,y:s.trace((normalization*s.eye(12)-G)[6*x:6*(x+1),6*y:6*(y+1)])/s.trace(K))
    need(recovered==Q,"basis-resolved partial trace recovers the full complex site Gram")
    need(not any(isinstance(node,ast.Assert) for node in ast.walk(ast.parse(Path(__file__).read_text()))),
         "review checker has no optimization-sensitive assert")
    return {"status":"PASS","independent_exact_checks":len(CHECKS),"numerical_checks":0,"checks":CHECKS,
            "C":str(C),"Q_C_dagger_C":str(Q),"wrong_conjugation_residual_rank":12,
            "full_coupling_dimensions":[12,20],"site_Frobenius_norm_squared":3,
            "reviewed_parent_source_sha256":"2fb3b99f5649f04d4ce1cd204d9a6359554157a566c3193eddf50846f5767f25",
            "scope":["independent tiny CAR convention regression, not the full native-W proof",
                     "general leading term includes the site Frobenius norm squared",
                     "inversion uses the matrix-resolved Gram and the declared site tensor factorization",
                     "parent 0 versus 64 at energy Delta requires Delta nonzero and g nonzero",
                     "not counted among the prior 270 source-composition guards"]}


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--replay",action="store_true")
    parser.add_argument("--output",type=Path)
    args=parser.parse_args()
    if args.replay:
        path=Path(__file__).resolve()
        runs=[]
        outputs=[]
        for label,flags in [("normal",[]),("optimized",["-OO"])]:
            result=subprocess.run([sys.executable,"-B",*flags,str(path)],capture_output=True,text=True)
            if result.returncode!=0:
                raise RuntimeError(label+" failed: "+result.stderr)
            if result.stderr:
                raise RuntimeError(label+" unexpected stderr: "+result.stderr)
            outputs.append(result.stdout)
            runs.append({"mode":label,"exit_code":result.returncode,"stdout_sha256":sha256(result.stdout.encode()).hexdigest()})
        if outputs[0]!=outputs[1]:
            raise RuntimeError("normal and optimized certificates differ")
        value={"status":"PASS","normal_optimized_identical":True,"script_sha256":sha256(path.read_bytes()).hexdigest(),
               "runs":runs,"certificate":json.loads(outputs[0])}
    else:
        value=certificate()
    encoded=json.dumps(value,indent=2,sort_keys=True)+"\n"
    if args.output:
        if args.output.exists() and args.output.read_text()!=encoded:
            raise RuntimeError("refusing to overwrite a different sealed review output")
        args.output.write_text(encoded)
    print(encoded,end="")


if __name__=="__main__":
    main()
