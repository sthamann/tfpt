import { TopicGuide } from "@/components/TopicGuide";
import { topicGuide } from "@/lib/topic-guides";
import { pageMetadata } from "@/lib/seo";

export const metadata = pageMetadata("/e8-standard-model");

export default function E8StandardModelPage() {
  return <TopicGuide guide={topicGuide("e8")} />;
}
