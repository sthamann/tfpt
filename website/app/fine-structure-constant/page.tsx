import { TopicGuide } from "@/components/TopicGuide";
import { topicGuide } from "@/lib/topic-guides";
import { pageMetadata } from "@/lib/seo";

export const metadata = pageMetadata("/fine-structure-constant");

export default function FineStructureConstantPage() {
  return <TopicGuide guide={topicGuide("alpha")} />;
}
