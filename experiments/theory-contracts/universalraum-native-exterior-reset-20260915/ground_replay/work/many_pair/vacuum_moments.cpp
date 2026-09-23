#include <algorithm>
#include <array>
#include <bit>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <limits>
#include <map>
#include <vector>
#include <dispatch/dispatch.h>
struct Pair {int u,v,sign; uint64_t mask,lower;};
struct Term {uint64_t mask; int coefficient;};
using State=std::vector<Term>;
std::array<std::array<Pair,8>,60> channels;
State create(const State& initial,int a){
  State temp;temp.reserve(initial.size()*8);
  for(const auto& term:initial)for(const auto& p:channels[a]){
    if(term.mask&p.mask)continue;
    int sign=(std::popcount(term.mask&p.lower)%2)?-1:1;
    temp.push_back({term.mask|p.mask,term.coefficient*p.sign*sign});
  }
  std::sort(temp.begin(),temp.end(),[](const Term&a,const Term&b){return a.mask<b.mask;});
  State out;out.reserve(temp.size());
  for(const auto&t:temp){if(!out.empty()&&out.back().mask==t.mask)out.back().coefficient+=t.coefficient;else out.push_back(t);}
  out.erase(std::remove_if(out.begin(),out.end(),[](const Term&t){return t.coefficient==0;}),out.end());return out;
}
uint64_t norm(const State&s){uint64_t n=0;for(const auto&t:s)n+=(int64_t)t.coefficient*t.coefficient;return n;}
int factorial(int n){int a=1;for(int i=2;i<=n;i++)a*=i;return a;}
struct Job {std::array<int,4> a;int n;};
int repeated_factor(const Job&j){int f=1,count=1;for(int i=1;i<j.n;i++){if(j.a[i]==j.a[i-1])count++;else{f*=factorial(count);count=1;}}return f*factorial(count);}
struct Context {std::vector<Job>*jobs;std::vector<uint64_t>*values;std::vector<State>*pairs;std::array<std::array<int,60>,60>*indices;};
void perform(void* raw,size_t k){auto*c=(Context*)raw;const auto&job=(*c->jobs)[k];State s=(*c->pairs)[(*c->indices)[job.a[0]][job.a[1]]];for(int j=2;j<job.n;j++)s=create(s,job.a[j]);int fact=factorial(job.n);(*c->values)[k]=norm(s)*(fact*fact/repeated_factor(job));}
int main(int argc,char**argv){
  int order=argc>1?std::stoi(argv[1]):3;
  if(order<2||order>4)return 2;
  std::ifstream input("work/many_pair/pair_channels.txt");
  for(auto&channel:channels)for(auto&p:channel){input>>p.u>>p.v>>p.sign;p.mask=(1ULL<<p.u)|(1ULL<<p.v);p.lower=((1ULL<<p.u)-1)^((1ULL<<p.v)-1);}
  if(!input)return 3;
  std::vector<State> pairs;std::array<std::array<int,60>,60> indices;
  for(int a=0;a<60;a++)for(int b=a;b<60;b++){indices[a][b]=pairs.size();pairs.push_back(create(create({{0,1}},a),b));}
  std::vector<Job> jobs;
  for(int a=0;a<60;a++)for(int b=a;b<60;b++){
    if(order==2)jobs.push_back({{a,b,0,0},2});
    else for(int c=b;c<60;c++){
      if(order==3)jobs.push_back({{a,b,c,0},3});
      else for(int d=c;d<60;d++)jobs.push_back({{a,b,c,d},4});
    }
  }
  std::vector<uint64_t> values(jobs.size());Context context{&jobs,&values,&pairs,&indices};
  dispatch_apply_f(jobs.size(),dispatch_get_global_queue(DISPATCH_QUEUE_PRIORITY_HIGH,0),&context,perform);
  uint64_t total=0;for(uint64_t v:values){if(std::numeric_limits<uint64_t>::max()-total<v)return 5;total+=v;}
  std::ofstream raw("work/many_pair/vacuum_values_"+std::to_string(order)+".bin",std::ios::binary);
  raw.write(reinterpret_cast<const char*>(values.data()),values.size()*sizeof(uint64_t));
  std::cout<<"{\"order\":"<<order<<",\"boson_configurations\":"<<jobs.size()<<",\"squared_norm\":"<<total<<"}\n";
}
