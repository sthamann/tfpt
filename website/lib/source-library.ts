import "server-only";
import { readFileSync } from "node:fs";
import { join } from "node:path";
export interface SourceDocument { id:string;title:string;entry_point:string;canonical_source:string;role:string;ordered_section_ids:string[];topic_ids:string[]; }
export interface SourceSection { id:string;title:string;source:string;line_start:number;line_end:number;owner_documents:string[];summary_excerpt:string;semantic_review:boolean;topic_suggestions:{topic_id:string;relation_type:string;match_basis:string}[]; }
export interface SourceRelation { id:string;from:string;to:string;relation_type:string;match_basis:string;tokens?:string[]; }
export interface SourceEvidence { id:string;type:string;path?:string;claim_ids?:string[];sha256?:string; }
export interface SourceLibrary { documents:SourceDocument[];sections:SourceSection[];relations:SourceRelation[];evidence:SourceEvidence[];sources:unknown[];topics:{id:string;title:string;relation_type:string}[];coverage:Record<string,unknown>;reverse_indexes:{by_script:Record<string,string[]>;by_topic:Record<string,string[]>;by_evidence:Record<string,string[]>}; }
let library:SourceLibrary|undefined;
export function sourceLibrary():SourceLibrary{return library??=JSON.parse(readFileSync(join(process.cwd(),"public/documentation/registry.json"),"utf8"));}
export function repositorySource(path:string,line?:number){return `https://github.com/sthamann/tfpt/blob/main/${path.split("/").map(encodeURIComponent).join("/")}${line?`#L${line}`:""}`;}
export function documentPdf(document:SourceDocument){return document.role==="active"?`/papers/${document.entry_point.replace(/\.tex$/, ".pdf")}`:undefined;}
