import { changelogSearchIndex } from "@/lib/changelog-navigation";

// Built once with the site and requested only when the global filters are used.
export const dynamic = "force-static";

export function GET() {
  return Response.json(changelogSearchIndex());
}
