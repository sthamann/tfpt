import { shareImage } from "@/lib/share-image";

export const runtime = "edge";
export const alt = "A reading guide to Topological Fixed-Point Theory.";
export const size = { width: 1200, height: 630 };
export const contentType = "image/png";

export default function OrientationImage() {
  return shareImage({ title: "A reading guide to Topological Fixed-Point Theory.", description: "The claims, the evidence and the open questions. Start here." });
}
