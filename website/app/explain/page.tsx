import type { Metadata } from "next";
import { pageMetadata } from "@/lib/seo";
import { TheoryGuide } from "@/components/explain/TheoryGuide";
export const metadata: Metadata = pageMetadata("/explain");
export default function ExplainPage() { return <TheoryGuide />; }
