/**
 * The promotion pipeline as a static SVG: sandbox → probe (kill criteria
 * declared) → suite module → ledger → generated mirrors, with the graveyard
 * branch drawn as a first-class outcome (negatives are published, not
 * deleted). Server component, no motion — safe under prefers-reduced-motion.
 */

const STAGES: {
  x: number;
  title: string;
  sub: string[];
  accent: string;
}[] = [
  {
    x: 10,
    title: "experiments/",
    sub: ["sandbox · firewall", "no claims made here"],
    accent: "#fbbf24",
  },
  {
    x: 202,
    title: "probe",
    sub: ["kill criteria declared", "before the run"],
    accent: "#a78bfa",
  },
  {
    x: 394,
    title: "verification/vN",
    sub: ["deterministic suite", "status markers typed"],
    accent: "#34d399",
  },
  {
    x: 586,
    title: "status_ledger.csv",
    sub: ["single source of truth", "one row per claim"],
    accent: "#60a5fa",
  },
  {
    x: 778,
    title: "papers + website",
    sub: ["generated mirrors", "never hand-edited"],
    accent: "#526278",
  },
];

function Arrow({ x1, x2, y }: { x1: number; x2: number; y: number }) {
  return (
    <g stroke="#475569" strokeWidth="1.5" fill="#475569">
      <line x1={x1} y1={y} x2={x2 - 7} y2={y} />
      <path d={`M ${x2 - 7} ${y - 4} L ${x2} ${y} L ${x2 - 7} ${y + 4} Z`} />
    </g>
  );
}

export function MethodPipeline() {
  return (
    <div className="overflow-hidden rounded-2xl border border-slate-300/50 bg-slate-50/60 p-4 sm:p-6">
      <svg
        viewBox="0 0 960 258"
        role="img"
        aria-label="The promotion pipeline: exploratory work starts in the experiments sandbox behind a firewall; a probe declares its kill criteria before running; only surviving results are promoted to a verification module in the deterministic suite; every claim becomes a row of the status ledger, the single source of truth; papers and website are generated mirrors of the ledger. Probes that die are published in the graveyard, not deleted."
        className="w-full"
      >
        {STAGES.map((s) => (
          <g key={s.title}>
            <rect
              x={s.x}
              y={44}
              width={172}
              height={86}
              rx={14}
              fill="#ffffff"
              stroke="#334155"
              strokeWidth="1.5"
            />
            <rect x={s.x} y={44} width={172} height={4} rx={2} fill={s.accent} />
            <text
              x={s.x + 86}
              y={78}
              textAnchor="middle"
              fill="#263b53"
              fontSize="14"
              fontWeight="600"
              fontFamily="var(--font-mono, monospace)"
            >
              {s.title}
            </text>
            {s.sub.map((line, i) => (
              <text
                key={line}
                x={s.x + 86}
                y={98 + i * 15}
                textAnchor="middle"
                fill="#526278"
                fontSize="11"
              >
                {line}
              </text>
            ))}
          </g>
        ))}
        <Arrow x1={182} x2={202} y={87} />
        <Arrow x1={374} x2={394} y={87} />
        <Arrow x1={566} x2={586} y={87} />
        <Arrow x1={758} x2={778} y={87} />

        {/* graveyard branch: a probe that dies is published, not deleted */}
        <g stroke="#fb7185" strokeWidth="1.5" strokeDasharray="4 4" fill="none">
          <path d="M 288 130 L 288 176" />
          <path
            d="M 284 169 L 288 176 L 292 169"
            fill="#fb7185"
            stroke="none"
          />
        </g>
        <rect
          x={192}
          y={178}
          width={364}
          height={62}
          rx={14}
          fill="#ffffff"
          stroke="#fb7185"
          strokeOpacity="0.45"
          strokeWidth="1.5"
          strokeDasharray="4 4"
        />
        <text
          x={374}
          y={204}
          textAnchor="middle"
          fill="#fda4af"
          fontSize="13"
          fontWeight="600"
          fontFamily="var(--font-mono, monospace)"
        >
          the graveyard
        </text>
        <text x={374} y={224} textAnchor="middle" fill="#526278" fontSize="11">
          a probe that hits its kill criterion is published as a negative — not deleted
        </text>

        {/* audit back-edge: the mirrors are checked against the ledger */}
        <g stroke="#475569" strokeWidth="1.2" strokeDasharray="2 4" fill="none">
          <path d="M 864 130 C 864 166, 700 158, 672 138" />
        </g>
        <text x={800} y={172} textAnchor="middle" fill="#64748b" fontSize="10.5">
          bash build.sh audit → AUDIT OK
        </text>
      </svg>
    </div>
  );
}
