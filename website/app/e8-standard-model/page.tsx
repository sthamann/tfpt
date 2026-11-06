import { TopicGuide } from "@/components/TopicGuide";
import { topicGuide } from "@/lib/topic-guides";
import { pageMetadata } from "@/lib/seo";
import { E8Construction } from "@/components/topic/TopicConstruction";

export const metadata = pageMetadata("/e8-standard-model");

export default function E8StandardModelPage() {
  return <TopicGuide guide={topicGuide("e8")} sectionContent={{
    glue: <E8Construction part="roots" />,
    carrier: <><E8Construction part="spinor" /><E8Construction part="charges" /></>,
  }} />;
}
