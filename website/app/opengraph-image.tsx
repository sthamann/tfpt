import { shareImage } from "@/lib/share-image";

export const runtime = "edge";
export const alt = "TFPT — Topological Fixed-Point Theory: research papers, predictions and verification.";
export const size = { width: 1200, height: 630 };
export const contentType = "image/png";

export default function OpengraphImage() {
  return shareImage({ title: "Two axioms. One compiler. A testable Standard-Model skeleton." });
}
