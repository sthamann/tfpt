import { Fragment } from "react";
import { Math } from "@/components/Math";

/** Only explicit authored inline math is rendered; ordinary text stays intact. */
export function ReadingText({ text }: { text: string }) {
  return <>{text.split(/\\\((.*?)\\\)/gs).map((part, index) => index % 2
    ? <Math key={index}>{part}</Math>
    : <Fragment key={index}>{part}</Fragment>)}</>;
}
