import "server-only";
import { readFileSync } from "node:fs";
import { join } from "node:path";

export interface FoundationTopic { id: string; titleEN: string; claimIds: string[]; researchFindingCount: number; }
export interface FoundationClaim { id: string; topicIds: string[]; moduleIds: string[]; sectionIds: string[]; activeSectionIds: string[]; explicitClaimSectionIds: string[]; sharedScriptSectionIds: string[]; topicMappingState: string; }
export interface FoundationModule { id: string; filename: string; path: string; cluster: string; synopsis: string; publicationNotes: string[]; sourceHref: string; snapshotSourceHref?:string; pubMirrorHref?:string; pubMirrorHash?:string; pubMirrorMatchesSnapshot?:boolean; sourceSha256: string; linkedClaimIds: string[]; sectionIds: string[]; activeSectionIds: string[]; evidenceId: string; reviewState: string; }
export interface FoundationNode { id: string; labelEN: string; state: string; summaryEN: string; stage: string; lane: string; relatedIDs: string[]; scopeNote: string; sourceRefIDs: string[]; reviewState: string; }
export interface FoundationEdge { id: string; from: string; to: string; labelEN: string; kind: string; conditions: string[]; sourceRefIDs: string[]; reviewState: string; }
export interface FoundationSourceRef { id: string; path: string; sha256: string; actualSha256?: string; lineStart: number; lineEnd: number; freshness: string; href: string | null; publicationState: string; }
export interface FoundationCoverage {
  activeClaims: number; registeredModules: number; authoredTopicMappedClaims: number; unmappedClaimIds: string[];
  explicitClaimCitationCount: number; activeDocumentExplicitClaimCitationCount: number;
  claimsWithPaperNavigation: number; modulesWithPaperNavigation: number;
  publicPaperRegistry: { physical_sections: number; document_views: number; active_document_views: number; complete_semantic_review: boolean; proofs_checked: boolean; [key: string]: unknown; };
  semanticReviewedPaperSections: number; proofsChecked: boolean; notice: string;
  moduleSourceChecks: unknown[]; sourceOmissions: unknown[]; modulePublication?:{moduleCount:number;matchingPublicationMirrorCount:number;olderPublicationMirrorCount:number;olderPublicationMirrorIds:string[];notice:string};
}
export interface FoundationIndex {
  schemaVersion: number;
  meta: { generatedAt: string; sourceRevision: string; sourceCommit: string; publicSourceCommit: string; notice: string; };
  topics: FoundationTopic[];
  topicClaimLinks: { topicId: string; claimId: string; basis: string; authoringRecordId: string; authoringPath: string; }[];
  claims: FoundationClaim[]; modules: FoundationModule[];
  theoryMap: { nodes: FoundationNode[]; edges: FoundationEdge[]; sourceRefs: FoundationSourceRef[]; stages: { id: string; labelEN: string; }[]; lanes: { id: string; labelEN: string; }[]; states: { id: string; labelEN: string; }[]; };
  coverage: FoundationCoverage;
  inputHashes: Record<string, string>; registryHref: string; registrySha256: string;
}

let cached: FoundationIndex | undefined;
/** The source index stays on the server; pages render only the selected records. */
export function foundationIndex(): FoundationIndex {
  return cached ??= JSON.parse(readFileSync(join(process.cwd(), "lib/foundation-index.json"), "utf8"));
}
