// Exact proper-cubic action on finite particle/hole flips and oriented currents.
#pragma once
struct CubicRotation { std::array<int,3> p,s; };
inline std::vector<CubicRotation> const& cubic_rotations() {
    static auto rotations=[] {
        std::vector<CubicRotation> out; std::array<int,3> p{0,1,2};
        do {
            int parity=1;
            for(int i=0;i<3;i++) for(int j=i+1;j<3;j++) if(p[i]>p[j]) parity=-parity;
            for(int x:{-1,1}) for(int y:{-1,1}) for(int z:{-1,1})
                if(parity*x*y*z==1) out.push_back({p,{x,y,z}});
        } while(std::next_permutation(p.begin(),p.end()));
        need(out.size()==24,"proper cubic group order"); return out;
    }();
    return rotations;
}
inline Site cubic_point(Site x,CubicRotation const& g) {
    return {g.s[0]*x[g.p[0]],g.s[1]*x[g.p[1]],g.s[2]*x[g.p[2]]};
}
struct Orbit { Key key; int sign=0,size=0; };
inline Orbit cubic_orbit(Key const& key) {
    size_t at=0; int n=key.at(at++); need(n>=1 && n<=5 && n%2,"odd physical flip count");
    std::vector<Mode> modes(n);
    for(auto& m:modes) {
        for(auto& x:m) x=key.at(at++);
        need(m[3]==0 || m[3]==1,"physical species");
    }
    need(std::is_sorted(modes.begin(),modes.end()) &&
         std::adjacent_find(modes.begin(),modes.end())==modes.end(),"canonical unique physical flips");
    int links=key.at(at++); need(links>=0 && links<=30,"physical current count");
    std::vector<std::pair<Edge,int>> flux;
    for(int j=0;j<links;j++) {
        Edge e; for(auto& x:e) x=key.at(at++);
        int v=key.at(at++); need(e[3]>=0 && e[3]<3 && v,"oriented current");
        flux.emplace_back(e,v);
    }
    need(at==key.size(),"physical key length");
    need(std::is_sorted(flux.begin(),flux.end()),"canonical physical current");
    for(size_t j=1;j<flux.size();j++) need(flux[j-1].first!=flux[j].first,"unique physical current link");
    Key best_matter; std::vector<std::pair<size_t,int>> candidates;
    auto const& rotations=cubic_rotations();
    for(size_t r=0;r<rotations.size();r++) {
        auto transformed=modes;
        for(auto& m:transformed) { auto x=cubic_point(site(m),rotations[r]); m=mode(x,m[3]); }
        int sign=1;
        for(int i=0;i<n;i++) for(int j=i+1;j<n;j++) if(transformed[j]<transformed[i]) sign=-sign;
        std::sort(transformed.begin(),transformed.end());
        Key matter{n}; for(auto m:transformed) matter.insert(matter.end(),m.begin(),m.end());
        if(candidates.empty() || matter<best_matter) { best_matter=std::move(matter); candidates={{r,sign}}; }
        else if(matter==best_matter) candidates.emplace_back(r,sign);
    }
    Orbit result; int multiplicity=0; bool forbidden=false;
    for(auto [r,sign]:candidates) {
        std::vector<std::pair<Edge,int>> rotated;
        for(auto const& [e,v]:flux) {
            Site a{e[0],e[1],e[2]},b=a; b[e[3]]++;
            a=cubic_point(a,rotations[r]); b=cubic_point(b,rotations[r]);
            int axis=0; while(axis<3 && a[axis]==b[axis]) axis++;
            need(axis<3,"rotated link axis"); auto lo=std::min(a,b);
            rotated.push_back({{lo[0],lo[1],lo[2],axis},a<b?v:-v});
        }
        std::sort(rotated.begin(),rotated.end());
        Key target=best_matter; target.push_back(links);
        for(auto const& [e,v]:rotated) { target.insert(target.end(),e.begin(),e.end()); target.push_back(v); }
        if(!multiplicity || target<result.key) { result={target,sign,0}; multiplicity=1; forbidden=false; }
        else if(target==result.key) { multiplicity++; forbidden|=result.sign!=sign; }
    }
    need(multiplicity>0 && 24%multiplicity==0,"integer cubic orbit size");
    result.size=24/multiplicity; if(forbidden) result.sign=0;
    return result;
}
