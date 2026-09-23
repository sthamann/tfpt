"""Numerical whole-H5 ground diagnostic and ground-filter success probabilities.

NON-RH conditional Bell model. Float diagnostics, NOT an exact spectral proof.
All full 1024-dimensional eigenvalues are computed independently of diagrams.
"""
import hashlib
import importlib.util
import json
from pathlib import Path
import numpy as np
import scipy.linalg as la
import sympy as s

HERE = Path(__file__).resolve().parent
SOURCE = HERE.parent/'refinement/ternary.py'
PIN = '9fbafd5778fc630883046f492f2a86d6693a04ac2a077d93b5ab0738b2db5b31'


def require(ok, message):
    if not ok:
        raise ValueError(message)


def main():
    require(hashlib.sha256(SOURCE.read_bytes()).hexdigest() == PIN, 'source pin')
    spec = importlib.util.spec_from_file_location('frozen_ternary', SOURCE)
    source = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(source)
    d = 4
    exact_h = source.chain_action(s.Integer(d))
    exact_g = source.symbolic_gram(s.Integer(d))
    h = np.array(exact_h).astype(float)
    gram = np.array(exact_g).astype(float)
    # Exact spectral formulas in the five-diagram invariant sector. The
    # statement that this is the FULL-space ground remains numerical below.
    root = s.sqrt(41)
    exact_energy = (19-root)/8
    exact_v = s.Matrix([(5+root)/2,1,(7+root)/2,(5+root)/2,1])
    require(s.simplify(exact_h*exact_v-exact_energy*exact_v) == s.zeros(5,1),
            'exact sector ground vector')
    exact_p = [s.Rational(363,800)+s.Rational(2223,32800)*root,
               s.Rational(9,25)+s.Rational(39,1025)*root,
               s.Rational(363,800)+s.Rational(2223,32800)*root]
    for j in range(3):
        amp = (exact_v.T*exact_g*source.SELECTION.T[:,j]/10)[0]
        require(s.simplify(amp**2/(exact_v.T*exact_g*exact_v)[0]-exact_p[j]) == 0,
                'exact sector-filter success formula')
    # h is not Euclidean Hermitian: diagonalize the Hermitian pencil G h,G.
    require(np.max(np.abs(gram@h-h.T@gram)) < 1e-12, 'physical adjoint metric')
    energies, vectors = la.eigh(gram@h, gram)
    v0 = vectors[:, 0]
    branches = np.array(source.SELECTION.T).astype(float)/(2*(d+1))
    amplitudes = v0@gram@branches
    probabilities = amplitudes**2
    require(np.max(np.abs(probabilities-np.array([float(x) for x in exact_p]))) < 1e-12,
            'floating independent eigenvector probabilities match exact formulas')
    require(np.all(probabilities > 0) and np.all(probabilities < 1),
            'ground filtering has nonzero failure probability for every branch')
    # Independent physical Hamiltonian in the full 4^5 Hilbert space.
    phi = np.eye(d).reshape(d*d)/np.sqrt(d)
    pair = np.outer(phi, phi)
    physical = 4*np.eye(d**5)
    for j in range(4):
        physical -= np.kron(np.kron(np.eye(d**j), pair), np.eye(d**(3-j)))
    all_energies = la.eigvalsh(physical, check_finite=False)
    require(abs(all_energies[0]-energies[0]) < 1e-10,
            'lowest multiplicity energy agrees with full-space numerical minimum')
    require(np.max(np.abs(all_energies[:d]-energies[0])) < 1e-10
            and all_energies[d]-energies[0] > 0.1,
            'numerically isolated fourfold full-space ground band')
    diagrams = np.hstack([np.array(source.diagram_matrix(item,d)).astype(float)
                           for item in source.DIAGRAMS])
    ground = diagrams@np.kron(v0.reshape(5,1), np.eye(d))
    require(np.max(np.abs(ground.T@ground-np.eye(d))) < 1e-11, 'normalized ground encoding')
    require(np.max(np.abs(physical@ground-energies[0]*ground)) < 1e-11,
            'ground encoder intertwines only scalar logical H')
    for j in range(3):
        branch = diagrams@np.kron(branches[:,j].reshape(5,1),np.eye(d))
        filtered = ground@(ground.T@branch)
        require(np.max(np.abs(filtered-amplitudes[j]*ground)) < 1e-11,
                'all projected branches have one common normalized ground encoding up to phase')
        require(np.max(np.abs(filtered.T@filtered-probabilities[j]*np.eye(d))) < 1e-11,
                'success probability independent of logical input')
    print(json.dumps({'scope':'NON-RH floating-point full-H5 diagnostic, not certified bounds',
        'source_pin':PIN, 'd':d, 'full_dimension':d**5,
        'sector_eigenvalues':[round(float(x),12) for x in energies],
        'full_lowest_eigenvalues':[round(float(x),12) for x in all_energies[:8]],
        'full_numerical_ground_gap':round(float(all_energies[d]-all_energies[0]),12),
        'filter_success_L_M_R':[round(float(x),12) for x in probabilities],
        'exact_sector_lowest_energy':'(19-sqrt(41))/8',
        'exact_sector_filter_success_L_M_R':[str(x) for x in exact_p],
        'same_normalized_projected_encoding':True,
        'deterministic_H_preserving_filter':False,
        'ground_logical_H_is_scalar':True, 'T1_T8_closed':[]},sort_keys=True))


if __name__ == '__main__':
    main()
