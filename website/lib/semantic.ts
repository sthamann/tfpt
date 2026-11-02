import "server-only";
import { readFileSync } from "node:fs";
import { join } from "node:path";
import type { FindingRecord, ResearchSource } from "./research";
export interface AtlasTopic { id:string;titleEN:string;summaryEN:string;orientation:Record<string,string>;problemIds:string[];findingIds:string[]; }
export interface AtlasProblem { id:string;titleEN:string;questionEN:string;topicIds:string[];goalIds:string[];acceptedPremiseIds:string[];findingIds:string[];taskIds:string[];strategyIds:string[];connectionIds:string[];reviewedAttemptIds:string[]; }
export interface AtlasFinding extends Omit<FindingRecord,"sources"> { sourceRefIds:string[];attemptIds:string[];reviewState:string; }
export interface AtlasTask { id:string;problemId:string;titleEN:string;kind:string;status:string;dependsOn:string[];resolutionIds:string[];requiredPremiseIds:string[];successCriterionEN:string;nextActionEN:string; }
export interface AtlasStrategy { id:string;problemId:string;titleEN:string;outcome:string;premiseIds:string[];findingIds:string[];explanationEN:string;changesRequiredEN:string; }
export interface AtlasAttempt { id:string;titleEN:string;questionEN:string|null;date:string|null;kind:string;status:string|null;verdictRaw:string|null;verdictClass:string;stage:string|null;evidenceClass:string|null;domain:string|null;scopeEN:string|null;sourceRefIds:string[];reviewedFindingIds:string[];notice:string; }
export interface AtlasPattern { id:string;titleEN:string;summaryEN:string;relatedIds:string[];conditions:string[];counterevidence:string[];sourceRefIds:string[];reviewState:string; }
export interface AtlasConnection { id:string;problemId:string;targetProblemId:string;kind:string;premiseIds:string[];findingIds:string[];explanationEN:string; }
export interface SemanticAtlas { meta:{generatedAt:string;sourceRevision:string;counts:Record<string,number>;notice:string};topics:AtlasTopic[];problems:AtlasProblem[];findings:AtlasFinding[];tasks:AtlasTask[];strategies:AtlasStrategy[];attempts:AtlasAttempt[];patterns:AtlasPattern[];connections:AtlasConnection[];premises:{id:string;titleEN:string;statementEN:string}[];sourceRefs:(ResearchSource & {remoteHref?:string;historicalSource?:boolean})[];coverage:Record<string,unknown>; }
let cached:SemanticAtlas|undefined;
export function semanticAtlas():SemanticAtlas {return cached ??= JSON.parse(readFileSync(join(process.cwd(),"lib/semantic-atlas.json"),"utf8"));}
