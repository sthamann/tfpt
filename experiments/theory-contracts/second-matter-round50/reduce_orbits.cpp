// Whole-cubic invariant-column Gram: exact orbit sums, not a state-space cutoff.
#include <gmpxx.h>
#define main round47_unused_main
#include "../bulk-word-round47/group_suffix.cpp"
#undef main
#include "cubic_orbits.hpp"

mpz_class read_big(std::istream& in) {
    int32_t signed_count=read<int32_t>(in);
    need(signed_count>=-8192 && signed_count<=8192,"bounded exact integer");
    size_t count=std::abs(signed_count); std::vector<unsigned char> bytes(count);
    in.read(reinterpret_cast<char*>(bytes.data()),count); need(bool(in),"complete exact integer");
    mpz_class z; mpz_import(z.get_mpz_t(),count,1,1,1,0,bytes.data());
    if(signed_count<0) z=-z; return z;
}
struct Entry { std::array<mpz_class,2> z; int size=0; };
int main(int argc,char** argv) {
    try {
        need(argc==3,"usage: reduce_orbits result.json new_orbit_vector_or_none");
        std::ios::sync_with_stdio(false);
        need(read<uint32_t>(std::cin)==0x4F504654,"orbit input magic");
        mpz_class denominator=read_big(std::cin); need(denominator>0,"positive common denominator");
        std::unordered_map<Key,Entry,Hash> states;
        uint64_t contributions=0,forbidden=0,peak=0;
        auto accumulate=[&](Key const& key,std::array<mpz_class,2> const& z,int multiplier=1) {
            contributions++; need(contributions<=200000000,"bounded source contribution stream");
            Orbit orbit=cubic_orbit(key);
            if(!orbit.sign) { forbidden++; return; }
            auto it=states.try_emplace(orbit.key).first;
            need(it->second.size==0 || it->second.size==orbit.size,"consistent orbit stabilizer");
            it->second.size=orbit.size;
            for(int j=0;j<2;j++) it->second.z[j]+=orbit.sign*multiplier*z[j];
            if(it->second.z[0]==0 && it->second.z[1]==0) states.erase(it);
            peak=std::max(peak,uint64_t(states.size())); need(states.size()<=20000000,"20M exact orbit gate");
        };
        while(true) {
            int length=read<int32_t>(std::cin); if(!length) break;
            need(length>=2 && length<=200,"physical key size"); Key key(length);
            for(auto& x:key) x=read<int32_t>(std::cin);
            std::array<mpz_class,2> z{read_big(std::cin),read_big(std::cin)}; accumulate(key,z);
        }
        need(std::cin.peek()==std::char_traits<char>::eof(),"trailing orbit input");
        auto norm=[&]() {
            mpz_class numerator=0; uint64_t physical_count=0;
            for(auto const& [key,entry]:states) {
                numerator+=(24/entry.size)*(entry.z[0]*entry.z[0]+entry.z[1]*entry.z[1]);
                physical_count+=entry.size;
            }
            mpq_class q(numerator,24*denominator*denominator); q.canonicalize();
            return std::make_pair(q,physical_count);
        };
        auto old=norm(); auto old_orbits=states.size();
        if(std::string(argv[2])!="none") {
            std::ifstream in(argv[2],std::ios::binary); need(bool(in),"new orbit source file");
            need(read<uint32_t>(in)==0x4F5A4654,"new orbit vector magic");
            mpz_class d=read_big(in); need(d>0 && denominator%d==0,"exact new-source common denominator");
            mpz_class factor=denominator/d;
            uint64_t count=read<uint64_t>(in); need(count<=20000000,"new source orbit count");
            for(uint64_t j=0;j<count;j++) {
                int length=read<int32_t>(in); need(length>=2 && length<=200,"new orbit key size");
                Key key(length); for(auto& x:key) x=read<int32_t>(in);
                std::array<mpz_class,2> z{read_big(in),read_big(in)};
                z[0]*=factor; z[1]*=factor;
                // All original seeds with the first +x hop: C4 invariant.
                // The six original cosets therefore contribute 6 orbit sums.
                accumulate(key,z,6);
            }
            need(in.peek()==std::char_traits<char>::eof(),"trailing new source");
        }
        auto updated=norm();
        std::ofstream out(argv[1]); need(bool(out),"orbit result file");
        out<<"{\"baseline_probability\":\""<<old.first.get_str()<<"\",\"baseline_output_count\":"<<old.second
           <<",\"probability\":\""<<updated.first.get_str()<<"\",\"output_count\":"<<updated.second
           <<",\"baseline_orbits\":"<<old_orbits<<",\"final_orbits\":"<<states.size()
           <<",\"peak_orbits\":"<<peak<<",\"contributions\":"<<contributions
           <<",\"forbidden_stabilizer_contributions\":"<<forbidden<<",\"proper_group_order\":24}\n";
        need(bool(out),"complete orbit result");
    } catch(std::exception const& e) { std::cerr<<e.what()<<"\n"; return 1; }
}
