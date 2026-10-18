import { papers } from "@/lib/papers";
import { shareImage } from "@/lib/share-image";

export const runtime = "edge";
export const alt = "TFPT research document preview";
export const size = { width: 1200, height: 630 };
export const contentType = "image/png";

export default async function PaperOgImage({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  const paper = papers.find((entry) => entry.slug === slug);
  return shareImage({ title: paper?.title ?? "TFPT research papers", label: "TFPT RESEARCH PAPERS" });
}
