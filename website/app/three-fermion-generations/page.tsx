import { TopicGuide } from "@/components/TopicGuide";
import { topicGuide } from "@/lib/topic-guides";
import { pageMetadata } from "@/lib/seo";

export const metadata = pageMetadata("/three-fermion-generations");

export default function ThreeFermionGenerationsPage() {
  return <TopicGuide guide={topicGuide("families")} />;
}
