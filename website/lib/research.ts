import "server-only";
import { readFileSync } from "node:fs";
import { join } from "node:path";

export interface ResearchSource { id: string; path: string; sha256: string; lineStart: number; lineEnd: number; href: string | null; freshness: string; publicationState: string; omittedOriginalLines?: number[]; }
export interface LedgerRecord { id: string; claim: string; status: string; canonicalStatus: string; dependencies: string; scripts: string[]; location: string; active: boolean; sourceHref: string; sourceLine: number; }
export interface FindingRecord { id: string; titleEN: string; statementEN: string; scopeEN: string; status: string; problemId: string; topicIds: string[]; premiseIds: string[]; sources: ResearchSource[]; historical: boolean; publicationNotes: string[]; }
export interface RegisteredPrediction { id: string; observable: string; formula: string; frozen_value?: string; layer?: string; conditional_on?: string | null; experiment?: string; kill_criterion?: string; }
export interface ResearchInventory {
  meta: { generatedAt: string; sourceRevision: string; snapshotSha256: string; counts: { ledgerTotal: number; ledgerActive: number; reviewedFindings: number; reviewedFindingsBeforePrivacyFilter: number; reviewedProblems: number; registeredScripts: number; sourceRefs: number; excludedAdministrativeFindings: number; findingStatuses: Record<string,number>; } };
  ledger: LedgerRecord[]; findings: FindingRecord[];
  premises: {id: string; titleEN: string; statementEN: string}[];
  problems: {id: string; titleEN: string; questionEN: string; findingIds: string[]; tasks: {id:string;titleEN:string;status:string;resolutionIds:string[];requiredPremiseIds:string[]}[]}[];
  predictions: { freeze_date: string; predictions: RegisteredPrediction[]; assigned_texture_values: RegisteredPrediction[]; conditional_bands: RegisteredPrediction[]; derived_variants_not_predictions: RegisteredPrediction[] };
}
let inventory: ResearchInventory | undefined;
export function researchInventory(): ResearchInventory {
  // Keep the full evidence corpus on the server. Only the selected records
  // are rendered; it is not shipped in the interactive explanation bundle.
  return inventory ??= JSON.parse(readFileSync(join(process.cwd(), "lib/research-inventory.json"), "utf8"));
}
