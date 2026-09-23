// Independent exact contraction u = T T^dagger v2 without materialising v3.
// Input: native 480 rows A i j sign. No external files are written.
#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <unordered_map>
#include <vector>
struct Pair {int a,i,j,w; uint64_t mask;};
struct Key {uint64_t mask; int code; bool operator==(const Key&o)const{return mask==o.mask&&code==o.code;}};
struct Hash {size_t operator()(const Key&k)const{return (k.mask^(k.mask>>33))*0xff51afd7ed558ccdULL+uint64_t(k.code)*0x9e3779b97f4a7c15ULL;}};
using State=std::unordered_map<Key,int64_t,Hash>;
int sign(uint64_t mask,int i){return (__builtin_popcountll(mask&((uint64_t(1)<<i)-1))&1)?-1:1;}
int up(uint64_t mask,const Pair&p){return sign(mask,p.j)*sign(mask|(uint64_t(1)<<p.j),p.i);}
int down(uint64_t mask,const Pair&p){return sign(mask,p.i)*sign(mask^(uint64_t(1)<<p.i),p.j);}
int weight(int code){return code/60==code%60?2:1;}
int64_t norm(const State&s){__int128 n=0;for(const auto&[k,a]:s)n+=(__int128)a*a*weight(k.code);if(n>INT64_MAX)throw 1;return (int64_t)n;}
int main(){
 std::vector<Pair> p;std::array<std::vector<Pair>,60> channels;
 int A,i,j,w;while(std::cin>>A>>i>>j>>w){Pair x{A,i,j,w,(uint64_t(1)<<i)|(uint64_t(1)<<j)};p.push_back(x);channels[A].push_back(x);}
 if(p.size()!=480)throw 2;
 State v2;v2.reserve(140000);
 for(const auto&x:p)for(const auto&y:p)if(!(x.mask&y.mask)){
  int a=std::min(x.a,y.a),b=std::max(x.a,y.a);
  v2[{x.mask|y.mask,a*60+b}]+=x.w*y.w*up(x.mask,y);
 }
 for(auto it=v2.begin();it!=v2.end();)if(it->second==0)it=v2.erase(it);else++it;
 State u;u.reserve(180000);uint64_t raising=0,lowering=0;
 for(const auto&[key,amp]:v2){
  for(const auto&x:p)if(!(key.mask&x.mask)){
   ++raising;const uint64_t m3=key.mask|x.mask;
   const int64_t a3=amp*x.w*up(key.mask,x);
   std::array<int,3> bs{key.code/60,key.code%60,x.a};std::sort(bs.begin(),bs.end());
   for(int slot=0;slot<3;++slot){
    if(slot&&bs[slot]==bs[slot-1])continue;
    const int B=bs[slot];int mult=0;for(int b:bs)mult+=b==B;
    std::array<int,2> remain{};int n=0;for(int k=0;k<3;++k)if(k!=slot)remain[n++]=bs[k];
    const int code=remain[0]*60+remain[1];
    for(const auto&y:channels[B])if((m3&y.mask)==y.mask){
     ++lowering;u[{m3^y.mask,code}]+=a3*mult*y.w*down(m3,y);
    }
   }
  }
 }
 for(auto it=u.begin();it!=u.end();)if(it->second==0)it=u.erase(it);else++it;
 __int128 vu=0;for(const auto&[k,a]:v2){auto it=u.find(k);if(it!=u.end())vu+=(__int128)a*it->second*weight(k.code);}
 std::cout<<"{\"v2_entries\":"<<v2.size()<<",\"v2_norm2\":"<<norm(v2)<<",\"u_entries\":"<<u.size()<<",\"u_norm2\":"<<norm(u)<<",\"v2_dot_u\":"<<(int64_t)vu<<",\"raising_transitions\":"<<raising<<",\"lowering_transitions\":"<<lowering<<"}\n";
}
