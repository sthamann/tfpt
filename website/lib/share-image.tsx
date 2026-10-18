import { ImageResponse } from "next/og";

export function shareImage({
  title,
  label = "TOPOLOGICAL FIXED-POINT THEORY",
  description = "Research papers, testable predictions and open verification.",
}: {
  title: string;
  label?: string;
  description?: string;
}) {
  // Plain display text avoids remote fallback-font requests for math glyphs.
  const displayTitle = title.normalize("NFKC").replace(/α/g, "alpha").replace(/μ/g, "mu");
  return new ImageResponse(
    <div style={{ display: "flex", width: "100%", height: "100%", flexDirection: "column", background: "#fcfbf8", color: "#172b43", padding: "56px 64px", fontFamily: "sans-serif", borderTop: "10px solid #1d4ed8" }}>
      <div style={{ display: "flex", alignItems: "center", gap: 18 }}>
        <div style={{ display: "flex", alignItems: "center", justifyContent: "center", width: 66, height: 66, background: "#1d4ed8", borderRadius: 16, color: "white", fontSize: 24, fontWeight: 700 }}>TFPT</div>
        <div style={{ display: "flex", fontSize: 18, letterSpacing: 2, color: "#526278" }}>{label}</div>
      </div>
      <div style={{ display: "flex", flex: 1, alignItems: "center", fontSize: displayTitle.length > 85 ? 54 : 68, lineHeight: 1.12, letterSpacing: -2, fontWeight: 700, maxWidth: 1056 }}>{displayTitle}</div>
      <div style={{ display: "flex", fontSize: 25, lineHeight: 1.4, color: "#475569", maxWidth: 1040 }}>{description}</div>
      <div style={{ display: "flex", justifyContent: "space-between", marginTop: 26, paddingTop: 22, borderTop: "1px solid #cbd5e1", fontSize: 19, color: "#526278" }}>
        <span>Stefan Hamann &amp; Alessandro Rizzo</span>
        <span>fixpoint-theory.com</span>
      </div>
    </div>,
    { width: 1200, height: 630 },
  );
}
