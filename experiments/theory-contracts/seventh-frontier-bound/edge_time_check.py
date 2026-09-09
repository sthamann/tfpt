"""Independent finite-time full E0 operator comparison, original physical edge.

This finite check does not stand in for the cubic norm derivation or readout.
"""
from collections import defaultdict
from fractions import Fraction as F
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('bound_for_edge_time',HERE/'checker.py')
r=importlib.util.module_from_spec(spec);spec.loader.exec_module(r)

def edge_sources(parents):
    r49,r48,r47,r46,r45,r44,r43,r42,r41,r40,r39,r38,parent=parents
    data=r43.geometry(parent,'edge');row=r40.parent_rows(data)
    def first(depth):
        def walk(mode,flux,prefixes,modes,weight):
            if len(prefixes)==depth:
                base=(-9600,)+tuple(12*(2*r42.dot(p,flux)-r42.dot(p,p))-(25 if m[1]==0 else 9600) for p,m in zip(prefixes,modes))
                for a,b,current,w,dots in r42.force_terms(r40,row,prefixes,range(2)):
                    final=r40.merge(flux,current);word=(a,b,mode)
                    f=base+(12*r42.dot(final,final)+r42.energy(word),)
                    delta=(0,)+tuple(24*d for d in dots)+(0,)
                    yield {'kind':'M'*depth+'E','word':word,'flux':final,'weight':(-1)**(depth-1)*weight*w,
                           'order':depth+1,'prefixes':prefixes+(final,),'dots':(dots+(0,),),
                           'frequencies':(f,tuple(x+y for x,y in zip(f,delta))),'signs':(1,-1)}
                return
            for target,current,w in row(mode):
                final=r40.merge(flux,current)
                yield from walk(target,final,prefixes+(final,),modes+(target,),weight*w)
        return walk((0,1),(),(),(),1)
    def append_E(paths):
        for p in paths:
            for a,b,current,w,dots in r42.force_terms(r40,row,p['prefixes'],range(2)):
                final=r40.merge(p['flux'],current);word=(a,b)+p['word']
                creates=(True,False)*((len(word)-1)//2)+(False,)
                energy=sum((1 if c else -1)*(25 if m[1]==0 else 9600) for m,c in zip(word,creates))
                firsts=tuple(f+(12*r42.dot(final,final)+energy,) for f in p['frequencies'])
                delta=(0,)+tuple(24*d for d in dots)+(0,)
                seconds=tuple(tuple(x+y for x,y in zip(f,delta)) for f in firsts)
                yield {**p,'kind':p['kind']+'E','word':word,'flux':final,'weight':p['weight']*w,'order':p['order']+1,
                       'prefixes':p['prefixes']+(final,),'dots':tuple(d+(0,) for d in p['dots'])+(dots+(0,),),
                       'frequencies':firsts+seconds,'signs':p['signs']+tuple(-x for x in p['signs'])}
    by_word={}
    def extend(word,paths):
        paths=list(paths);by_word[word]=paths
        grade=word.count('M')+2*word.count('E')
        if grade+1<=7:extend(word+'M',r49.append_M(r45,r42,r40,paths,row))
        if grade+2<=7:extend(word+'E',append_E(paths))
    for depth in range(1,6):extend('M'*depth+'E',first(depth))
    r.require(len(by_word)==26,'complete finite source language')
    return data,by_word

def run():
    third,parents,third_record=r.inherited()
    r49,r48,r47,r46,r45,r44,r43,r42,r41,r40,r39,r38,parent=parents
    data,by_word=edge_sources(parents)
    frontier=json.loads((HERE.parent/'seventh-frontier-edge/validation.json').read_text())
    r.require({w:len(by_word[w]) for w in r.WORDS}==frontier['counts'],'independent complete grade7 raw edge census')
    full=r38.tree_model(parent,1,center=False);charged=r38.tree_model(parent,1,particles=1,center=False)
    columns=[j for j,(_,flux) in enumerate(full['basis']) if flux==(0,)]
    source=[[(F(0),F(0)) for _ in columns] for _ in range(4)]
    def add_word(word,flux,value):
        creates=(True,False)*((len(word)-1)//2)+(False,)
        for col,j in enumerate(columns):
            mask=full['basis'][j][0];sign=1
            for (site,species),create in zip(word[::-1],creates[::-1]):
                step=r41.fermion_action(mask,site+2*species,create)
                if step is None:break
                mask,parity=step;sign*=parity
            else:
                output=charged['index'][mask,(dict(flux).get(0,0),)]
                source[output][col]=r41.add(source[output][col],tuple(sign*x for x in value))
    linear=r43.compile_resummed(r41,r38,parent,data,degree=120)
    for (mode,flux),value in linear['coefficients'].items():add_word((mode,),flux,tuple(F(x,linear['denominator']) for x in value))
    groups=defaultdict(int)
    for paths in by_word.values():
        for p in paths:
            for f,sign in zip(p['frequencies'],p['signs']):groups[p['word'],p['flux'],p['order'],tuple(sorted(f))]+=sign*p['weight']
    kernels={};electric_tail=F(0)
    for (word,flux,n,f),w in groups.items():
        if not w:continue
        key=n,f
        if key not in kernels:
            value,tail=r39.simplex_integral(tuple(F(x,2400) for x in f),F(1),100)
            phase=((-1,0),(0,-1),(1,0),(0,1))[n%4]
            kernels[key]=r41.multiply(phase,value),tail
        value,tail=kernels[key];weight=F(w,576**n)
        add_word(word,flux,tuple(weight*x for x in value));electric_tail+=abs(weight)*tail
    def evolution(model,time):
        matrix=[[(F(0),F(0)) for _ in model['basis']] for _ in model['basis']]
        for j in range(len(model['basis'])):
            initial=([int(i==j) for i in range(len(model['basis']))],[0]*len(model['basis']))
            a,b,den,tail,_=r38.evolve(model['rows'],initial,F(time),120)
            for i in range(len(a)):matrix[i][j]=F(a[i],den),F(b[i],den)
        return matrix,tail
    neutral,eta_n=evolution(full,1);left,eta_q=evolution(charged,-1)
    physical=[[(F(0),F(0)) for _ in columns] for _ in range(4)]
    for position,j in enumerate(columns):
        for k,(mask,flux) in enumerate(full['basis']):
            step=r41.fermion_action(mask,2)
            if step is None:continue
            out,sign=step;l=charged['index'][out,flux]
            for i in range(4):physical[i][position]=r41.add(physical[i][position],tuple(sign*x for x in r41.multiply(left[i][l],neutral[k][j])))
    squared=sum((a-c)**2+(b-d)**2 for row,actual in zip(source,physical) for (a,b),(c,d) in zip(row,actual))
    numerical=2*(linear['numerical_error']+electric_tail+eta_n+eta_q+eta_n*eta_q)
    error=r38.sqrt_interval(squared)[1]+numerical
    bound=r.certificate(third,parents,third_record)['upper']
    r.require(0<error<bound,'finite-time whole E0 operator error fits independently derived cubic envelope')
    return r38.encode({'verdict':'FULL_FINITE_TIME_EDGE_E0_OPERATOR_CHECKED',
        'source_matrix':source,'physical_matrix':physical,'E0_input_count':len(columns),
        'source_word_counts':{word:len(paths) for word,paths in by_word.items()},
        'difference_Frobenius_squared':squared,'numerical_Frobenius_error_upper':numerical,
        'whole_E0_operator_error_upper':error,'conditional_full_cubic_envelope':bound,
        'new_cubic_readout_evaluated':False,'T1_T8_solved':False,
        'sources':{name:hashlib.sha256((HERE/name).read_bytes()).hexdigest() for name in ('edge_time_check.py','checker.py','test_edge_time.py')}})

def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--output',type=Path);args=parser.parse_args()
    value=json.dumps(run(),sort_keys=True,indent=2)+'\n'
    if args.output:args.output.write_text(value)
    else:print(value,end='')

if __name__=='__main__':main()
