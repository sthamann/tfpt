import type { Metadata } from "next";
import Link from "next/link";
import { LegacyTourRedirect } from "@/components/tour/LegacyTourRedirect";
import { pageMetadata } from "@/lib/seo";

export const metadata: Metadata = {
  ...pageMetadata("/explain"),
  alternates: { canonical: "/explain" },
};

export default function TourPage() {
  return <article className="reference-page">
    <LegacyTourRedirect />
    <header className="reference-header">
      <h1>Continue to the explanation</h1>
      <p>The guided tour now lives with the worked charge, alpha and clock explanations. Existing tour links open the corresponding chapter or verification tool.</p>
    </header>
    <nav className="reference-links" aria-label="Continue to the explanation">
      <Link href="/explain">Open the explanation</Link>
    </nav>
  </article>;
}
