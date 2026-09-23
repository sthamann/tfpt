"""Numerical/table checks and math assets for the integrated paper; not TOE closure.

Run with a Python environment containing mpmath, SymPy, matplotlib, and Pillow.
No existing source is imported or modified. All output paths are explicit.
"""
from pathlib import Path
import hashlib
import json
import os
import re
import sys
import mpmath as m
import sympy as s

ROOT = Path(__file__).resolve().parents[3]
DATE = os.environ.get('TFPT_PAPER_DATE','2026-09-13')
if not re.fullmatch(r'\d{4}-\d{2}-\d{2}',DATE):
    raise ValueError('invalid paper date')
SOURCE = ROOT / f'docs/TFPT_COMPILER_UNIVERSALRAUM_PAPER_{DATE}.md'
OUT = ROOT / 'output/pdf'
ASSETS = ROOT / f'tmp/pdfs/tfpt_compiler_universalraum_{DATE.replace("-","")}'
CHECKS = []


def require(name, condition):
    if not condition:
        raise ValueError(name)
    CHECKS.append(name)


def main():
    m.mp.dps = 70
    c = 1 / (8*m.pi)
    phi = 1/(6*m.pi) + 48*c**4
    lam = m.sqrt(phi*(1-phi))

    def F(a):
        q = 48*c**4*m.exp(-2*a)
        seam = 1/(6*m.pi)+q*(1-q)**(-m.mpf(5)/4)
        return a**3-2*c**3*a**2-m.mpf(4)/5*41*c**6*m.log(1/seam)

    alpha = m.findroot(F, (m.mpf('.007'), m.mpf('.008')))
    require('positive target root and high precision residual',
            alpha > 0 and abs(F(alpha)) < m.mpf('1e-65'))
    require('published inverse-alpha rounded value',
            abs(1/alpha-m.mpf('137.0359992168407')) < m.mpf('1e-12'))
    require('root sign bracket', F(m.mpf('.00729735256220970')) < 0
            < F(m.mpf('.00729735256221000')))
    s12, s23, s13 = lam, phi/(1+lam), lam**3/3
    c12, c23, c13 = [m.sqrt(1-x*x) for x in (s12,s23,s13)]
    delta = m.pi/3+3*lam**2
    phase = m.exp(1j*delta)
    V = m.matrix([
        [c12*c13, s12*c13, s13/phase],
        [-s12*c23-c12*s23*s13*phase,
         c12*c23-s12*s23*s13*phase, s23*c13],
        [s12*s23-c12*c23*s13*phase,
         -c12*s23-s12*c23*s13*phase, c23*c13]])
    require('standard CKM unitarity', m.norm(V*V.H-m.eye(3)) < m.mpf('1e-65'))
    gamma = m.arg(-V[0,0]*m.conj(V[0,2])/(V[1,0]*m.conj(V[1,2])))
    require('gamma is not delta', abs(gamma-delta) > m.mpf('1e-6'))
    # Rational anomaly checks in all-left-handed Weyl convention.
    Y = list(map(s.Rational, ['1/6','-2/3','1/3','-1/2','1','0']))
    dim = [6,3,3,2,1,1]
    require('one family has 16 components', sum(dim) == 16)
    require('mixed gravitational U1 anomaly', sum(d*y for d,y in zip(dim,Y)) == 0)
    require('cubic U1 anomaly', sum(d*y**3 for d,y in zip(dim,Y)) == 0)
    require('SU3 squared U1 anomaly', 2*Y[0]+Y[1]+Y[2] == 0)
    require('SU2 squared U1 anomaly', 3*Y[0]+Y[3] == 0)
    require('SU3 cubic anomaly', 2-1-1 == 0)
    require('even count weak doublets', (3+1) % 2 == 0)
    require('canonical hypercharge trace', sum(d*y*y for d,y in zip(dim,Y)) == s.Rational(10,3))
    x = s.Symbol('x')
    R = s.Matrix([[1,3,0],[1,5,2],[2,5,3]])
    require('flavor determinant', R.det() == 8)
    require('flavor characteristic polynomial', R.charpoly(x).as_expr() == x**3-9*x**2+10*x-8)
    require('E8 branching dimension', 45+15+16*4+16*4+10*6 == 248)

    values = {
        'c3':c, 'phi0':phi, 'lambda_C':lam, 'alpha_inverse':1/alpha,
        'alpha_CODATA2022_experimental_sigma_only':(1/alpha-m.mpf('137.035999177'))/m.mpf('.000000021'),
        'CKM_s23':s23, 'CKM_s13':s13, 'CKM_delta_deg':m.degrees(delta),
        'CKM_gamma_deg':m.degrees(gamma), 'CKM_delta_minus_gamma_deg':m.degrees(delta-gamma),
        'CKM_Vcb_modulus':abs(V[1,2]), 'CKM_Vub_modulus':abs(V[0,2]),
        'mu_tau':m.mpf(8)/7*phi, 'e_mu':m.mpf(12)/7*phi**2,
        'u_d':m.mpf(55)/117, 'c_s':m.mpf(34)/47/phi, 't_b':m.mpf(3)/26/phi**2,
        'PMNS_s12_squared':m.mpf(1)/3-phi/2,
        'PMNS_s13_squared':phi*m.exp(-m.mpf(5)/6),
        'beta_deg':m.degrees(phi/(4*m.pi)),
        'Omega_b':(1-1/(4*m.pi))*phi,
        'ns_N50':1-m.mpf(2)/50, 'ns_N60':1-m.mpf(2)/60,
        'r_N50':m.mpf(12)/50**2, 'r_N60':m.mpf(12)/60**2,
        'As_N51p4':m.mpf('51.4')**2*c**7/(24*m.pi**2),
        'scalaron_over_reduced_planck':c**(m.mpf(7)/2),
        'vacuum_density_over_reduced_planck_fourth':3*m.exp(-2/alpha)/(4*m.pi**2),
    }
    report = {'scope':'Frozen formula evaluation and internal SM dictionary; no physical gate closure',
              'precision_digits':m.mp.dps, 'checks':CHECKS,
              'values':{k:m.nstr(v,32) for k,v in values.items()}, 'T1_T8_closed':[]}
    OUT.mkdir(parents=True, exist_ok=True)
    ASSETS.mkdir(parents=True, exist_ok=True)
    (OUT/f'tfpt_compiler_universalraum_{DATE}_numbers.json').write_text(
        json.dumps(report, indent=2, ensure_ascii=False)+'\n')
    if '--numbers-only' not in sys.argv:
        import matplotlib
        matplotlib.use('Agg')
        from matplotlib.mathtext import math_to_image, MathTextParser
        from matplotlib.font_manager import FontProperties, findfont
        (ASSETS/'fonts.json').write_text(json.dumps({
            'body':findfont(FontProperties(family='DejaVu Sans')),
            'bold':findfont(FontProperties(family='DejaVu Sans',weight='bold'))}))
        equations = re.findall(r'^\$\$(.*?)\$\$$', SOURCE.read_text(), re.MULTILINE)
        # Require braces for font commands in the mathtext rendering dialect.
        equations = [re.sub(r'\\(mathcal|mathsf|mathbb) ([A-Za-z])',r'\\\1{\2}',eq)
                     for eq in equations]
        parser = MathTextParser('path')
        for eq in equations:
            parser.parse('$'+eq+'$')
        for index, eq in enumerate(equations):
            math_to_image('$'+eq+'$', ASSETS/f'equation_{index:02}.png',
                          prop=FontProperties(size=13), dpi=230, color='#183047')
        report['equations_rendered'] = len(equations)
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
