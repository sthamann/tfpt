import { TopicGuide } from "@/components/TopicGuide";
import { topicGuide } from "@/lib/topic-guides";
import { pageMetadata } from "@/lib/seo";
import { FamilyConstruction } from "@/components/topic/TopicConstruction";

export const metadata = pageMetadata("/three-fermion-generations");

export default function ThreeFermionGenerationsPage() {
  return <TopicGuide guide={topicGuide("families")} sectionContent={{ "same-divisor": <FamilyConstruction /> }} />;
}
