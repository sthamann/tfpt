import { TopicGuide } from "@/components/TopicGuide";
import { topicGuide } from "@/lib/topic-guides";
import { pageMetadata } from "@/lib/seo";
import { ALPHA_CONTENTS, AlphaDerivation } from "@/components/explain/AlphaDerivation";

export const metadata = pageMetadata("/fine-structure-constant");

export default function FineStructureConstantPage() {
  return <TopicGuide guide={topicGuide("alpha")} contents={ALPHA_CONTENTS}>
    <AlphaDerivation />
  </TopicGuide>;
}
