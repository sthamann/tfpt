import type { Metadata } from "next";
import { pageMetadata } from "@/lib/seo";
import ResearchPortal from "@/components/results/ResearchPortal";
import RawResearchRecords from "@/components/results/RawResearchRecords";
import FoundationAtlas from "@/components/results/FoundationAtlas";
export const metadata:Metadata=pageMetadata("/results");
export const dynamic="force-dynamic";
export default async function ResultsPage({searchParams}:{searchParams:Promise<Record<string,string|string[]|undefined>>}){
 const original=await searchParams;const params=Object.fromEntries(Object.entries(original).map(([key,value])=>[key,typeof value==="string"?value:undefined]));
 if(params.view==="ledger"||params.type==="ledger") return <RawResearchRecords searchParams={Promise.resolve(original)}/>;
 if(/^[A-Z][A-Z0-9_]*(?:\.[A-Z0-9_]+)+$/.test(params.search||"")) params.claim=params.search;
 if(params.search?.startsWith("claim:")) params.claim=params.search.slice(6);
 if(params.search?.startsWith("finding:")) params.record=params.search;
 if(params.claim||params.coverage==="1"||params.tab==="foundation"||params.mapping==="unmapped"||(params.topic&&!params.tab&&!params.question&&!params.record&&!params.pattern)) return <FoundationAtlas params={params}/>;
 return <ResearchPortal params={params}/>;
}
