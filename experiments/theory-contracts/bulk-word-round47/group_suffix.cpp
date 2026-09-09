// Integer-only physical-column grouping. No numerical phase approximation here.
#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <limits>
#include <map>
#include <stdexcept>
#include <string>
#include <unordered_map>
#include <vector>

using Site=std::array<int32_t,3>;
using Mode=std::array<int32_t,4>;
using Edge=std::array<int32_t,4>;
using Flux=std::map<Edge,int32_t>;
using Key=std::vector<int32_t>;
struct Hash {
    size_t operator()(Key const& v) const {
        uint64_t h=1469598103934665603ULL;
        for(auto x:v) { h^=static_cast<uint32_t>(x); h*=1099511628211ULL; }
        return h;
    }
};
void need(bool ok,std::string const& msg) { if(!ok) throw std::runtime_error(msg); }
template<class T> T read(std::istream& in) {
    T value{}; in.read(reinterpret_cast<char*>(&value),sizeof(value));
    need(bool(in),"truncated integer input"); return value;
}
template<class T> void write(std::ostream& out,T value) {
    out.write(reinterpret_cast<char const*>(&value),sizeof(value));
    need(bool(out),"integer output failed");
}
int64_t times(int64_t a,int64_t b) {
    int64_t value; need(!__builtin_mul_overflow(a,b,&value),"weight multiplication overflow"); return value;
}
void add(int64_t& a,int64_t b) {
    int64_t value; need(!__builtin_add_overflow(a,b,&value),"group accumulation overflow"); a=value;
}
Site site(Mode m) { return {m[0],m[1],m[2]}; }
Mode mode(Site s,int species) { return {s[0],s[1],s[2],species}; }
Flux merge(Flux a,Flux const& b) {
    for(auto const& [edge,value]:b) { a[edge]+=value; if(!a[edge]) a.erase(edge); }
    return a;
}
Flux inverse(Flux a) { for(auto& [edge,value]:a) value=-value; return a; }
Flux transport(Site target,Site source) {
    int axis=-1;
    for(int k=0;k<3;k++) if(target[k]!=source[k]) {
        need(axis<0 && std::abs(target[k]-source[k])==1,"nearest-neighbor transporter"); axis=k;
    }
    need(axis>=0,"nonzero transporter"); Site lo=std::min(target,source);
    return {{{lo[0],lo[1],lo[2],axis},source>target?-1:1}};
}
int dot(Flux const& a,Flux const& b) {
    int result=0;
    for(auto const& [edge,value]:a) { auto it=b.find(edge); if(it!=b.end()) result+=value*it->second; }
    return result;
}
std::vector<Site> neighbors(Site s) {
    std::vector<Site> out;
    for(int axis=0;axis<3;axis++) for(int sign:{-1,1}) { Site t=s; t[axis]+=sign; out.push_back(t); }
    return out;
}
struct Hop { Mode next; Flux shift; int weight; };
std::vector<Hop> make_row(Mode m) {
    std::vector<Hop> out; Site s=site(m);
    for(auto middle:neighbors(s)) {
        Flux outer=transport(s,middle);
        if(m[3]==1) { out.push_back({mode(middle,0),outer,24}); continue; }
        out.push_back({mode(middle,0),outer,48});
        out.push_back({mode(middle,1),outer,24});
        for(auto source:neighbors(middle)) if(source!=s)
            out.push_back({mode(source,0),merge(outer,transport(middle,source)),1});
    }
    return out;
}
// Finitely many occupation flips relative to uniform bare-low filling.
// The parity equals an embedding in any sufficiently large odd-side cube
// with even half-width. No inert site list or finite physical box is used.
int action(std::vector<Mode> const& word,std::vector<Mode>& flips) {
    flips.clear(); int parity=1;
    for(int j=int(word.size())-1;j>=0;j--) {
        Mode m=word[j]; bool create=(j==0 || (word.size()==5 && j==2));
        auto it=std::lower_bound(flips.begin(),flips.end(),m);
        bool changed=(it!=flips.end() && *it==m);
        bool occupied=(m[3]==0)^changed;
        if(occupied==create) return 0;
        int count=m[0]+m[1]+m[2]+m[3]+int(it-flips.begin());
        if(count%2) parity=-parity;
        if(changed) flips.erase(it); else flips.insert(it,m);
    }
    return parity;
}
Flux read_flux(std::istream& in) {
    int n=read<int32_t>(in); need(n>=0 && n<=12,"prefix current size"); Flux result;
    for(int i=0;i<n;i++) {
        Edge e; for(auto& x:e) x=read<int32_t>(in);
        int v=read<int32_t>(in);
        need(e[3]>=0 && e[3]<3 && v && std::abs(v)<=12,"integer link current");
        need(!result.count(e),"unique link in prefix"); result[e]=v;
    }
    return result;
}
int main(int argc,char** argv) {
    try {
        need(argc==3,"usage: group_suffix output.bin suffix_steps");
        int steps=std::stoi(argv[2]); need(steps==0 || steps==1,"executed suffix depth 0 or 1");
        std::ios::sync_with_stdio(false);
        need(read<uint32_t>(std::cin)==0x47504654,"protocol magic");
        int arity=read<int32_t>(std::cin), order=read<int32_t>(std::cin), branches=read<int32_t>(std::cin);
        need((arity==3 && order==4 && branches==2)||(arity==5 && order==3 && branches==4),"declared raw seed family");
        std::unordered_map<Key,int64_t,Hash> groups; groups.reserve(1000000);
        std::map<Mode,std::vector<Hop>> rows;
        uint64_t seeds=0, extensions=0, active=0;
        std::vector<Mode> flips;
        while(true) {
            int64_t weight=read<int64_t>(std::cin); if(!weight) break; seeds++;
            need(seeds<=2000000 && weight!=std::numeric_limits<int64_t>::min(),"bounded seed input");
            std::vector<Mode> word(arity);
            for(auto& m:word) { for(auto& x:m) x=read<int32_t>(std::cin);
                need(m[3]==0 || m[3]==1,"species");
                for(int k=0;k<3;k++) need(std::abs(m[k])<=20,"declared coordinate envelope"); }
            std::vector<Flux> prefixes; for(int j=0;j<order;j++) prefixes.push_back(read_flux(std::cin));
            std::vector<Key> frequencies(branches,Key(order+1)); std::vector<int> signs(branches);
            for(int b=0;b<branches;b++) { for(auto& f:frequencies[b]) f=read<int32_t>(std::cin);
                signs[b]=read<int32_t>(std::cin); need(std::abs(signs[b])==1,"branch sign"); }
            auto collect=[&](std::vector<Mode> const& updated,Flux const& shift,int64_t w) {
                extensions++; int parity=action(updated,flips); if(!parity) return; active++;
                Flux final=merge(prefixes.back(),shift);
                int energy=0;
                for(int j=0;j<arity;j++) energy+=(j==0 || (arity==5 && j==2)?1:-1)*(updated[j][3]?9600:25);
                Key prefix; prefix.push_back(int(flips.size()));
                for(auto m:flips) prefix.insert(prefix.end(),m.begin(),m.end());
                prefix.push_back(int(final.size()));
                for(auto const& [e,v]:final) { prefix.insert(prefix.end(),e.begin(),e.end()); prefix.push_back(v); }
                Key delta(order+1,0);
                for(int j=0;j<order;j++) delta[j+1]=24*dot(prefixes[j],shift);
                for(int b=0;b<branches;b++) {
                    Key f=frequencies[b];
                    if(steps) { for(int j=0;j<=order;j++) f[j]+=delta[j]; f.push_back(12*dot(final,final)+energy); }
                    std::sort(f.begin(),f.end()); Key key=prefix; key.insert(key.end(),f.begin(),f.end());
                    add(groups[key],times(w,parity*signs[b]));
                }
                need(groups.size()<=12000000,"physical group resource gate exceeded");
            };
            if(!steps) collect(word,{},weight);
            else for(int leg=0;leg<arity;leg++) {
                Mode m=word[leg]; if(!rows.count(m)) rows.emplace(m,make_row(m));
                bool create=(leg==0 || (arity==5 && leg==2));
                for(auto const& hop:rows.at(m)) {
                    auto updated=word; updated[leg]=hop.next;
                    collect(updated,create?inverse(hop.shift):hop.shift,times(weight,create?hop.weight:-hop.weight));
                }
            }
        }
        need(std::cin.peek()==std::char_traits<char>::eof(),"unexpected trailing input");
        std::vector<std::pair<Key,int64_t>> sorted; sorted.reserve(groups.size());
        for(auto& [key,value]:groups) if(value) sorted.emplace_back(key,value);
        std::sort(sorted.begin(),sorted.end());
        std::ofstream out(argv[1],std::ios::binary); need(bool(out),"output file");
        write<uint64_t>(out,sorted.size());
        for(auto const& [key,value]:sorted) {
            write<int32_t>(out,key.size()); for(auto x:key) write<int32_t>(out,x); write<int64_t>(out,value);
        }
        std::cerr<<"{\"seed_records\":"<<seeds<<",\"raw_extensions\":"<<extensions
                 <<",\"nonzero_bare_actions\":"<<active<<",\"groups_before_cancellation\":"<<groups.size()
                 <<",\"groups\":"<<sorted.size()<<"}\n";
    } catch(std::exception const& e) { std::cerr<<e.what()<<"\n"; return 1; }
}
