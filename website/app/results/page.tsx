import type { Metadata } from "next";
import { pageMetadata } from "@/lib/seo";
import ResearchPortal from "@/components/results/ResearchPortal";
import RawResearchRecords from "@/components/results/RawResearchRecords";
export const metadata:Metadata=pageMetadata("/results");
export const dynamic="force-dynamic";
export default async function ResultsPage({searchParams}:{searchParams:Promise<Record<string,string|string[]|undefined>>}){
 const original=await searchParams;const params=Object.fromEntries(Object.entries(original).map(([key,value])=>[key,typeof value==="string"?value:undefined]));
 if(params.view==="ledger"||params.type==="ledger"||/^[A-Z][A-Z0-9_]*(?:\.[A-Z0-9_]+)+$/.test(params.search||"")) return <RawResearchRecords searchParams={Promise.resolve(original)}/>;
 if(params.search?.startsWith("finding:")) params.record=params.search;
 return <ResearchPortal params={params}/>;
}
