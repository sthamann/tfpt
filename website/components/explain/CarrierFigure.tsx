import { bitCount, evenMasks } from "@/lib/carrier";

export function CarrierFigure({ selectedMask, introductory = false }: { selectedMask?: number; introductory?: boolean }) {
  return <figure className="carrier-figure">
    <div className="carrier-key"><span><i className="carrier-dot is-colour" /> Colour slot</span><span><i className="carrier-dot is-weak" /> Weak slot</span></div>
    <div role="img" aria-label="All sixteen even combinations of five internal slots: one empty selection, ten pairs and five selections of four. Filled dots are selected slots.">
      {[0, 2, 4].map(degree => <div className="carrier-degree" key={degree}>
        <div className="carrier-degree-label"><span>Λ{degree === 0 ? "⁰" : degree === 2 ? "²" : "⁴"}</span><span>{degree === 0 ? "Empty" : degree === 2 ? "Pairs" : "Four slots"}</span></div>
        <div className="carrier-combinations">{evenMasks.filter(mask => bitCount(mask) === degree).map(mask => <div key={mask} data-mask={mask} className={`carrier-state${mask === selectedMask ? " is-current" : ""}`}>
          {[0, 1, 2, 3, 4].map(i => <span key={i} className={`carrier-dot ${mask & (1 << i) ? i < 3 ? "is-colour" : "is-weak" : ""}`} />)}
        </div>)}</div>
        <span className="carrier-count">{degree === 0 ? 1 : degree === 2 ? 10 : 5}</span>
      </div>)}
    </div>
    <div className="carrier-equation">1 + 10 + 5 = 16 <span>components in one family</span></div>
    <figcaption>{introductory ? "Internal components of the given five slot carrier. In the wider construction, E₈ is the lattice consistency structure; the physical gauge interpretation has its own conditions." : "The even exterior representation of the given five slot carrier. These are internal components."}</figcaption>
  </figure>;
}
