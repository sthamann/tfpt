// Reuse only pinned integer geometry/protocol primitives, never an old output.
#include <gmpxx.h>
#define main round47_unused_main
#include "../bulk-word-round47/group_suffix.cpp"
#undef main
#include "cubic_orbits.hpp"
static_assert(std::numeric_limits<long>::digits>=std::numeric_limits<int64_t>::digits,
              "GMP signed-long conversion requires an exact 64-bit long");

struct Candidate {
    Flux shift;
    int64_t weight;
    int energy;
    Key occupation;
};
struct Successors {
    uint64_t raw_slots=0;
    std::vector<Candidate> active;
};
int word_energy(std::vector<Mode> const& word) {
    int e=0;
    for(int j=0;j<3;j++) e+=(j==0?1:-1)*(word[j][3]?9600:25);
    return e;
}
Key word_key(std::vector<Mode> const& word) {
    Key key; for(auto m:word) key.insert(key.end(),m.begin(),m.end()); return key;
}
void pack_flux(Key& k,Flux const& f) {
    k.push_back(int(f.size()));
    for(auto const& [e,v]:f) { k.insert(k.end(),e.begin(),e.end()); k.push_back(v); }
}
Flux unpack_flux(Key const& k,size_t& i) {
    int n=k.at(i++); Flux f;
    for(int j=0;j<n;j++) {
        Edge e; for(auto& x:e) x=k.at(i++);
        f[e]=k.at(i++);
    }
    return f;
}
void write_big(std::ostream& out,mpz_class const& z) {
    size_t count=0; std::vector<unsigned char> bytes((mpz_sizeinbase(z.get_mpz_t(),2)+7)/8);
    mpz_export(bytes.data(),&count,1,1,1,0,z.get_mpz_t());
    need(count<=8192,"bounded exact integer output");
    write<int32_t>(out,z<0?-int32_t(count):int32_t(count));
    out.write(reinterpret_cast<char const*>(bytes.data()),count); need(bool(out),"big integer output");
}
int main(int argc,char** argv) {
    try {
        need(argc>=4 && argc<=6,"usage: group_second output.bin depth cache_limit [direct_degree [orbit_block]]");
        int depth=std::stoi(argv[2]), cache_limit=std::stoi(argv[3]);
        need(depth>=0 && depth<=2 && cache_limit>=0 && cache_limit<=200000,"depth/cache domain");
        int degree=argc>=5?std::stoi(argv[4]):-1, order=4+depth;
        need(degree==-1 || (degree>=0 && degree<=100),"direct degree domain");
        bool direct=degree>=0;
        int orbit_block=argc==6?std::stoi(argv[5]):0;
        need(orbit_block>=0 && orbit_block<=2000000 && (!orbit_block || direct),"orbit block domain");
        std::ios::sync_with_stdio(false);
        need(read<uint32_t>(std::cin)==0x50504654,"Round50 protocol magic");
        need(read<int32_t>(std::cin)==3 && read<int32_t>(std::cin)==4 && read<int32_t>(std::cin)==2,"one-E leaf family");
        std::map<Mode,std::vector<Hop>> rows;
        std::unordered_map<Key,Successors,Hash> cache;
        std::unordered_map<Key,int64_t,Hash> groups;
        std::unordered_map<Key,int64_t,Hash> seed_groups;
        std::unordered_map<Key,std::array<mpz_class,2>,Hash> vectors,kernels;
        std::unordered_map<Key,std::array<mpz_class,2>,Hash> orbit_vectors;
        std::map<int,mpz_class> absolute_by_radius;
        mpz_class denominator=1; std::vector<mpz_class> factors;
        if(direct) {
            mpz_class fact=1,power=1,hop=1,smallfact=1;
            for(int j=1;j<=order+degree;j++) fact*=j;
            for(int j=0;j<degree;j++) power*=2400;
            for(int j=0;j<order;j++) hop*=576;
            for(int j=1;j<=order;j++) smallfact*=j;
            denominator=fact*power*hop;
            mpz_class factor=fact/smallfact*power;
            for(int m=0;m<=degree;m++) {
                factors.push_back(factor);
                if(m<degree) factor/=2400*(order+m+1);
            }
        }
        auto kernel=[&](Key const& f)->std::array<mpz_class,2> const& {
            auto found=kernels.find(f); if(found!=kernels.end()) return found->second;
            std::vector<mpz_class> h(degree+1); h[0]=1;
            for(auto x:f) for(int j=1;j<=degree;j++) h[j]+=x*h[j-1];
            std::array<mpz_class,2> z;
            for(int j=0;j<=degree;j++) {
                int phase=(order+j)%4; mpz_class value=h[j]*factors[j];
                if(phase<2) value=-value;
                z[phase%2]+=value;
            }
            need(kernels.size()<200000,"200k distinct exact phase kernels");
            return kernels.emplace(f,std::move(z)).first->second;
        };
        auto live=[&]() { return orbit_block?orbit_vectors.size():(direct?vectors.size():groups.size()); };
        uint64_t orbit_flushes=0,peak_buffer=0,forbidden_orbit_contributions=0;
        auto fold_orbits=[&]() {
            if(vectors.empty()) return;
            orbit_flushes++;
            for(auto const& [key,z]:vectors) {
                Orbit orbit=cubic_orbit(key);
                if(!orbit.sign) { forbidden_orbit_contributions++; continue; }
                auto it=orbit_vectors.try_emplace(orbit.key).first;
                it->second[0]+=orbit.sign*z[0]; it->second[1]+=orbit.sign*z[1];
                if(it->second[0]==0 && it->second[1]==0) orbit_vectors.erase(it);
            }
            vectors.clear();
            need(orbit_vectors.size()<=20000000,"20M exact orbit-vector gate");
        };
        uint64_t seeds=0,first_steps=0,raw_slots=0,active=0,hits=0,misses=0,clears=0;
        uint64_t zero_seeds=0,zero_group_cancellations=0,peak_groups=0;
        auto row=[&](Mode m)->std::vector<Hop> const& {
            if(!rows.count(m)) rows.emplace(m,make_row(m));
            return rows.at(m);
        };
        auto successors=[&](std::vector<Mode> const& word) {
            Successors result; std::vector<Mode> flips;
            for(int leg=0;leg<3;leg++) for(auto const& hop:row(word[leg])) {
                result.raw_slots++;
                auto next=word; next[leg]=hop.next;
                int parity=action(next,flips); if(!parity) continue;
                Key occupancy{int(flips.size())};
                for(auto m:flips) occupancy.insert(occupancy.end(),m.begin(),m.end());
                result.active.push_back({leg==0?inverse(hop.shift):hop.shift,
                    int64_t(parity)*(leg==0?hop.weight:-hop.weight),word_energy(next),occupancy});
            }
            return result;
        };
        while(true) {
            int64_t w=read<int64_t>(std::cin); if(!w) break;
            need(++seeds<=2000000 && w!=std::numeric_limits<int64_t>::min(),"bounded seed stream");
            std::vector<Mode> word(3);
            for(auto& m:word) {
                for(auto& x:m) x=read<int32_t>(std::cin);
                need(m[3]==0 || m[3]==1,"species");
                for(int j=0;j<3;j++) need(std::abs(m[j])<=20,"coordinate envelope");
            }
            std::vector<Flux> prefixes;
            for(int j=0;j<4;j++) prefixes.push_back(read_flux(std::cin));
            std::array<Key,2> frequencies{Key(5),Key(5)}; std::array<int,2> signs;
            for(int b=0;b<2;b++) {
                for(auto& f:frequencies[b]) { f=read<int32_t>(std::cin); need(std::abs(f)<=100000,"frequency envelope"); }
                signs[b]=read<int32_t>(std::cin); need(std::abs(signs[b])==1,"phase sign");
            }
            // The two annihilator legs can be antisymmetrized before the
            // complete M derivation. This is a whole-operator identity.
            if(word[1]==word[2]) { zero_seeds++; continue; }
            int parity=1;
            if(word[2]<word[1]) { std::swap(word[1],word[2]); parity=-1; }
            for(int b=0;b<2;b++) {
                Key key=word_key(word); pack_flux(key,prefixes.back());
                std::vector<Key> pairs;
                for(int j=0;j<5;j++) {
                    Key pair{frequencies[b][j]}; pack_flux(pair,j?prefixes[j-1]:Flux{});
                    pairs.push_back(pair);
                }
                // Sort frequency AND its spectral prefix together. Sorting
                // frequencies alone here would corrupt later flux shifts.
                std::sort(pairs.begin(),pairs.end());
                for(auto const& pair:pairs) key.insert(key.end(),pair.begin(),pair.end());
                auto it=seed_groups.try_emplace(key,0).first;
                add(it->second,times(w,parity*signs[b]));
                if(!it->second) seed_groups.erase(it);
            }
            need(seed_groups.size()<=4000000,"4M exact seed-class gate");
        }
        need(std::cin.peek()==std::char_traits<char>::eof(),"unexpected trailing input");
        // Deterministic class order, independently of hash iteration order.
        std::vector<std::pair<Key,int64_t>> ordered_seeds(seed_groups.begin(),seed_groups.end());
        seed_groups.clear(); seed_groups.rehash(0);
        std::sort(ordered_seeds.begin(),ordered_seeds.end());
        uint64_t processed=0;
        for(auto const& [packed,w]:ordered_seeds) {
            if(processed%1000==0) {
                std::ofstream progress(std::string(argv[1])+".progress.json");
                progress<<"{\"processed_seed_classes\":"<<processed<<",\"total_seed_classes\":"<<ordered_seeds.size()
                        <<",\"live_groups\":"<<live()<<",\"peak_groups\":"<<peak_groups
                        <<",\"unprojected_buffer\":"<<vectors.size()<<",\"orbit_flushes\":"<<orbit_flushes<<"}\n";
                need(bool(progress),"progress output failed");
            }
            processed++;
            size_t at=0; std::vector<Mode> word(3);
            for(auto& m:word) for(auto& x:m) x=packed.at(at++);
            Flux original_final=unpack_flux(packed,at);
            Key frequencies; std::vector<Flux> prefixes;
            for(int j=0;j<5;j++) {
                frequencies.push_back(packed.at(at++)); prefixes.push_back(unpack_flux(packed,at));
            }
            need(at==packed.size(),"exact seed-class decoder");
            auto collect=[&](Candidate const& last,Flux const& first,int first_energy,int64_t weight) {
                active++;
                Flux shift=merge(first,last.shift), middle=merge(original_final,first);
                Flux final=merge(original_final,shift);
                Key key0=last.occupation; key0.push_back(int(final.size()));
                for(auto const& [e,v]:final) { key0.insert(key0.end(),e.begin(),e.end()); key0.push_back(v); }
                Key delta(5,0);
                for(int j=0;j<5;j++) delta[j]=24*dot(prefixes[j],shift);
                {
                    Key f=frequencies;
                    if(depth) {
                        for(int j=0;j<5;j++) f[j]+=delta[j];
                        if(depth==2) f.push_back(12*dot(middle,middle)+first_energy+24*dot(middle,last.shift));
                        f.push_back(12*dot(final,final)+last.energy);
                    }
                    std::sort(f.begin(),f.end()); auto signed_weight=times(weight,last.weight);
                    if(direct) {
                        auto const& z=kernel(f);
                        auto it=vectors.try_emplace(key0).first;
                        long exact_weight=static_cast<long>(signed_weight);
                        it->second[0]+=exact_weight*z[0]; it->second[1]+=exact_weight*z[1];
                        if(it->second[0]==0 && it->second[1]==0) { vectors.erase(it); zero_group_cancellations++; }
                        int radius=0; for(auto x:f) radius=std::max(radius,std::abs(x));
                        mpz_class mag=exact_weight; if(mag<0) mag=-mag;
                        absolute_by_radius[radius]+=mag;
                        peak_buffer=std::max(peak_buffer,uint64_t(vectors.size()));
                        if(orbit_block && vectors.size()>=size_t(orbit_block)) fold_orbits();
                    } else {
                        Key key=key0; key.insert(key.end(),f.begin(),f.end());
                        auto it=groups.try_emplace(key,0).first;
                        add(it->second,signed_weight);
                        if(!it->second) { groups.erase(it); zero_group_cancellations++; }
                    }
                }
                peak_groups=std::max(peak_groups,uint64_t(live()));
                need(live()<=size_t(direct?40000000:180000000),"exact representation resource gate");
            };
            if(depth==0) {
                raw_slots++; std::vector<Mode> flips; int parity=action(word,flips);
                if(parity) {
                    Key k{int(flips.size())}; for(auto m:flips) k.insert(k.end(),m.begin(),m.end());
                    collect({{},parity,word_energy(word),k},{},0,w);
                }
            } else if(depth==1) {
                auto s=successors(word); raw_slots+=s.raw_slots;
                for(auto const& c:s.active) collect(c,{},0,w);
            } else {
                for(int leg=0;leg<3;leg++) for(auto const& hop:row(word[leg])) {
                    first_steps++; auto next=word; next[leg]=hop.next;
                    Flux first=leg==0?inverse(hop.shift):hop.shift;
                    auto weight=times(w,leg==0?hop.weight:-hop.weight);
                    Key key=word_key(next); auto found=cache.find(key);
                    Successors scratch; Successors const* s;
                    if(found!=cache.end()) { hits++; s=&found->second; }
                    else {
                        misses++; scratch=successors(next);
                        if(cache_limit) {
                            if(cache.size()>=size_t(cache_limit)) { cache.clear(); clears++; }
                            s=&cache.emplace(key,std::move(scratch)).first->second;
                        } else s=&scratch;
                    }
                    raw_slots+=s->raw_slots;
                    for(auto const& c:s->active) collect(c,first,word_energy(next),weight);
                }
            }
        }
        std::ofstream out(argv[1],std::ios::binary); need(bool(out),"output file");
        if(direct) {
            if(orbit_block) { fold_orbits(); peak_groups=std::max(peak_groups,uint64_t(live())); }
            auto const& result=orbit_block?orbit_vectors:vectors;
            std::vector<Key const*> keys; keys.reserve(result.size());
            for(auto const& entry:result) keys.push_back(&entry.first);
            std::sort(keys.begin(),keys.end(),[](Key const* a,Key const* b) { return *a<*b; });
            write<uint32_t>(out,orbit_block?0x4F5A4654:0x5A504654); write_big(out,denominator); write<uint64_t>(out,keys.size());
            for(auto key:keys) {
                write<int32_t>(out,key->size()); for(auto x:*key) write<int32_t>(out,x);
                auto const& z=result.at(*key); write_big(out,z[0]); write_big(out,z[1]);
            }
        } else {
        std::vector<std::pair<Key,int64_t>> sorted; sorted.reserve(groups.size());
        for(auto& [key,value]:groups) if(value) sorted.emplace_back(key,value);
        std::sort(sorted.begin(),sorted.end());
        write<uint64_t>(out,sorted.size());
        for(auto const& [key,value]:sorted) {
            write<int32_t>(out,key.size()); for(auto v:key) write<int32_t>(out,v); write<int64_t>(out,value);
        }
        }
        std::cerr<<"{\"seed_records\":"<<seeds<<",\"first_M_steps\":"<<first_steps
                 <<",\"canonical_seed_classes\":"<<ordered_seeds.size()<<",\"whole_operator_zero_seeds\":"<<zero_seeds
                 <<",\"represented_canonical_final_M_slots\":"<<raw_slots<<",\"nonzero_bare_actions\":"<<active
                 <<",\"cache_hits\":"<<hits<<",\"cache_misses\":"<<misses<<",\"cache_clears\":"<<clears
                 <<",\"exact_zero_group_cancellations\":"<<zero_group_cancellations<<",\"peak_groups\":"<<peak_groups
                 <<",\"groups_before_cancellation\":"<<live()<<",\"groups\":"<<live()
                 <<",\"direct_degree\":"<<degree<<",\"frequency_kernels\":"<<kernels.size()
                 <<",\"orbit_block\":"<<orbit_block<<",\"orbit_flushes\":"<<orbit_flushes
                 <<",\"peak_unprojected_buffer\":"<<peak_buffer
                 <<",\"forbidden_orbit_contributions\":"<<forbidden_orbit_contributions
                 <<",\"gmp_version\":\""<<gmp_version<<"\",\"absolute_by_radius\":{";
        bool comma=false;
        for(auto const& [radius,weight]:absolute_by_radius) {
            if(comma) std::cerr<<','; comma=true;
            std::cerr<<'"'<<radius<<"\":\""<<weight.get_str()<<'"';
        }
        std::cerr<<"}}\n";
    } catch(std::exception const& e) { std::cerr<<e.what()<<"\n"; return 1; }
}
