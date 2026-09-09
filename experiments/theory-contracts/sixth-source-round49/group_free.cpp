// Integer-only grouping of final free-source actions; no hopping or physics approximation.
#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <limits>
#include <stdexcept>
#include <unordered_map>
#include <vector>
using Mode=std::array<int32_t,4>;
using Key=std::vector<int32_t>;
struct Hash { size_t operator()(Key const& v) const {
    uint64_t h=1469598103934665603ULL;
    for(auto x:v) { h^=static_cast<uint32_t>(x); h*=1099511628211ULL; }
    return h;
}};
void need(bool ok,char const* message) { if(!ok) throw std::runtime_error(message); }
template<class T> T read() { T x{}; std::cin.read(reinterpret_cast<char*>(&x),sizeof(x)); need(bool(std::cin),"truncated input"); return x; }
template<class T> void write(std::ostream& out,T x) { out.write(reinterpret_cast<char const*>(&x),sizeof(x)); need(bool(out),"output write"); }
int action(std::vector<Mode> const& word,std::vector<Mode>& flips) {
    flips.clear(); int sign=1;
    for(int j=int(word.size())-1;j>=0;j--) {
        auto m=word[j]; bool create=(j==0 || (word.size()==5 && j==2));
        auto it=std::lower_bound(flips.begin(),flips.end(),m);
        bool changed=it!=flips.end() && *it==m;
        if(((m[3]==0)^changed)==create) return 0;
        if((m[0]+m[1]+m[2]+m[3]+int(it-flips.begin()))%2) sign=-sign;
        if(changed) flips.erase(it); else flips.insert(it,m);
    }
    return sign;
}
int main(int argc,char** argv) {
    try {
        need(argc==2,"usage: group_free output.bin"); std::ios::sync_with_stdio(false);
        need(read<uint32_t>()==0x49504654,"protocol magic");
        int arity=read<int32_t>(),n=read<int32_t>(),branches=read<int32_t>();
        need((arity==3 && n==5 && branches==2)||(arity==5 && n==4 && branches==4),"declared sixth-source family");
        std::unordered_map<Key,int64_t,Hash> groups; groups.reserve(1000000);
        uint64_t count=0,active=0; std::vector<Mode> flips;
        while(true) {
            int64_t w=read<int64_t>(); if(!w) break;
            need(w!=std::numeric_limits<int64_t>::min() && ++count<=30000000,"seed resource/weight guard");
            std::vector<Mode> word(arity);
            for(auto& m:word) {
                for(auto& x:m) x=read<int32_t>();
                need(m[3]==0 || m[3]==1,"species");
                for(int j=0;j<3;j++) need(m[j]>=-30 && m[j]<=30,"coordinate envelope");
            }
            Key flux;
            for(int j=0;j<n;j++) {
                int size=read<int32_t>(); need(size>=0 && size<=16,"prefix size"); Key current{size};
                for(int k=0;k<size;k++) {
                    int32_t e[5]; for(auto& x:e) x=read<int32_t>();
                    for(int l=0;l<3;l++) need(e[l]>=-30 && e[l]<=30,"edge envelope");
                    need(e[3]>=0 && e[3]<3 && e[4]!=0 && e[4]>=-16 && e[4]<=16,"edge current");
                    current.insert(current.end(),e,e+5);
                }
                if(j==n-1) flux=current;
            }
            int parity=action(word,flips); if(parity) active++;
            Key prefix{int(flips.size())};
            for(auto m:flips) prefix.insert(prefix.end(),m.begin(),m.end());
            prefix.insert(prefix.end(),flux.begin(),flux.end());
            for(int b=0;b<branches;b++) {
                Key f(n+1); for(auto& x:f) { x=read<int32_t>(); need(x>=-100000 && x<=100000,"frequency envelope"); }
                int sign=read<int32_t>(); need(sign==1 || sign==-1,"branch sign");
                if(!parity) continue;
                std::sort(f.begin(),f.end()); Key key=prefix; key.insert(key.end(),f.begin(),f.end());
                int64_t addend=w*(parity*sign),value;
                need(!__builtin_add_overflow(groups[key],addend,&value),"signed group overflow"); groups[key]=value;
            }
            need(groups.size()<=15000000,"physical group resource guard");
        }
        need(std::cin.peek()==std::char_traits<char>::eof(),"trailing input");
        std::vector<std::pair<Key,int64_t>> sorted; sorted.reserve(groups.size());
        for(auto const& [k,v]:groups) if(v) sorted.emplace_back(k,v);
        std::sort(sorted.begin(),sorted.end());
        std::ofstream out(argv[1],std::ios::binary); need(bool(out),"output file");
        write<uint64_t>(out,sorted.size());
        for(auto const& [key,w]:sorted) { write<int32_t>(out,key.size()); for(auto x:key) write(out,x); write(out,w); }
        std::cerr<<"{\"seed_records\":"<<count<<",\"nonzero_bare_actions\":"<<active
                 <<",\"groups_before_cancellation\":"<<groups.size()<<",\"groups\":"<<sorted.size()<<"}\n";
    } catch(std::exception const& e) { std::cerr<<e.what()<<"\n"; return 1; }
}
