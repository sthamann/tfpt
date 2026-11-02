import Link from "next/link";
import { ChargeExplorer } from "./InteractiveReadouts";
import { BudgetBridge } from "./DerivationFigures";

export function DerivationPreview() {
  return <div className="guide-shell"><section className="guide-section" id="charge-builder">
    <h2>Build a component. See the whole family.</h2>
    <p className="guide-lead">Choose slots to add their charges. One colour slot and one weak slot give a quark component. Every even selection has its place in the same sixteen component family.</p>
    <p className="figure-note">Given here: the five internal slots, their 3+2 marking and normalized hypercharge. <Link className="guide-link" href="/explain#inputs">Where these inputs enter the theory</Link>.</p>
    <ChargeExplorer />
  </section><BudgetBridge /></div>;
}
