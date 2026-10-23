import type { Metadata, Viewport } from "next";
import { Inter, Newsreader, JetBrains_Mono } from "next/font/google";
import { Analytics } from "@vercel/analytics/next";
import "./globals.css";
import "katex/dist/katex.min.css";
import "./math-fonts.css";
import { Navbar } from "@/components/Navbar";
import { Footer } from "@/components/Footer";
import { ReproducerProvider } from "@/components/Reproducer";
import { REPO_URL, SITE_URL } from "@/lib/utils";
import { SITE_VERSION } from "@/lib/version";

const inter = Inter({ subsets: ["latin"], display: "swap", variable: "--font-inter" });
const newsreader = Newsreader({ subsets: ["latin"], display: "swap", variable: "--font-newsreader" });
const mono = JetBrains_Mono({ subsets: ["latin"], weight: ["400", "500"], display: "swap", variable: "--font-jetbrains", preload: false });

const SITE_NAME = "TFPT — Topological Fixed-Point Theory";
const SITE_DESCRIPTION = "Explore Topological Fixed-Point Theory (TFPT): research papers, testable predictions and an open verification suite by Stefan Hamann and Alessandro Rizzo.";

export const viewport: Viewport = {
  themeColor: "#fcfbf8",
  width: "device-width",
  initialScale: 1,
  maximumScale: 5,
  colorScheme: "light",
};

export const metadata: Metadata = {
  metadataBase: new URL(SITE_URL),
  title: {
    default: "Topological Fixed-Point Theory (TFPT) — Research & Papers",
    template: "%s · TFPT",
  },
  description: SITE_DESCRIPTION,
  applicationName: "TFPT",
  keywords: [
    "TFPT",
    "Topological Fixed-Point Theory",
    "fine-structure constant derivation",
    "derivation of the fine-structure constant",
    "where does 137 come from",
    "why is alpha 1/137",
    "Standard Model structure from first principles",
    "discrete Standard Model structure",
    "deriving the constants of nature",
    "fundamental constants from topology",
    "Compiler closure",
    "E8 audit hull",
    "Two axioms",
    "Standard Model structure",
    "Fine-structure constant",
    "Strong CP problem",
    "θ_eff = 0",
    "Cabibbo angle",
    "PMNS matrix",
    "CKM matrix",
    "D5 A3 E8 glue",
    "Bootstrap loop",
    "Coxeter compiler",
    "Stefan Hamann",
    "Alessandro Rizzo",
    "Theoretical physics",
    "Mathematical physics",
    "α⁻¹ = 137.0359992",
    "Quantum field theory",
    `TFPT ${SITE_VERSION}`,
  ],
  authors: [
    { name: "Stefan Hamann" },
    { name: "Alessandro Rizzo" },
  ],
  creator: "Stefan Hamann & Alessandro Rizzo",
  publisher: "TFPT Collaboration",
  category: "science",
  classification: "Theoretical & Mathematical Physics",
  formatDetection: {
    email: false,
    address: false,
    telephone: false,
  },
  openGraph: {
    type: "website",
    siteName: SITE_NAME,
    title: SITE_NAME,
    description: SITE_DESCRIPTION,
    locale: "en_US",
    url: SITE_URL,
  },
  twitter: {
    card: "summary_large_image",
    title: SITE_NAME,
    description:
      SITE_DESCRIPTION,
    creator: "@tfpttheory",
  },
  robots: {
    index: true,
    follow: true,
    googleBot: {
      index: true,
      follow: true,
      "max-image-preview": "large",
      "max-snippet": -1,
      "max-video-preview": -1,
    },
  },
  alternates: {
    canonical: SITE_URL,
  },
  verification: {
    google: process.env.NEXT_PUBLIC_GOOGLE_VERIFICATION || undefined,
  },
};

const websiteJsonLd = {
  "@context": "https://schema.org",
  "@type": "WebSite",
  "@id": `${SITE_URL}/#website`,
  alternateName: "TFPT",
  name: SITE_NAME,
  url: SITE_URL,
  description: SITE_DESCRIPTION,
  inLanguage: "en",
  sameAs: [REPO_URL],
  publisher: {
    "@type": "Organization",
    name: "TFPT Collaboration",
    url: SITE_URL,
    member: [
      { "@type": "Person", name: "Stefan Hamann" },
      { "@type": "Person", name: "Alessandro Rizzo" },
    ],
  },
  potentialAction: {
    "@type": "ReadAction",
    target: [`${SITE_URL}/orientation`],
  },
};

const researchProjectJsonLd = {
  "@context": "https://schema.org",
  "@type": "ResearchProject",
  "@id": `${SITE_URL}/#research-project`,
  name: SITE_NAME,
  url: SITE_URL,
  description: SITE_DESCRIPTION,
  sameAs: [REPO_URL],
  keywords: [
    "Topological Fixed-Point Theory",
    "Compiler closure",
    "E8 audit hull",
    "Standard Model",
    "Fine-structure constant",
    "Strong CP",
    "PMNS",
    "CKM",
  ],
  member: [
    { "@type": "Person", name: "Stefan Hamann" },
    { "@type": "Person", name: "Alessandro Rizzo" },
  ],
  parentOrganization: {
    "@type": "Organization",
    name: "TFPT Collaboration",
  },
  about: [
    "Discrete compiler",
    "D5 A3 E8 glue",
    "Coxeter–cyclotomic compiler",
    "Standard Model structure",
    "Strong-CP closure",
  ],
};


export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" className={`${inter.variable} ${newsreader.variable} ${mono.variable}`}>
      <head>
        <meta name="format-detection" content="telephone=no" />
        <meta name="apple-mobile-web-app-capable" content="yes" />
        <meta name="apple-mobile-web-app-status-bar-style" content="default" />
        <meta name="apple-mobile-web-app-title" content="TFPT" />
      </head>
      <body className="font-sans antialiased text-slate-800 selection:bg-blue-500/30">
        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{ __html: JSON.stringify(websiteJsonLd) }}
        />
        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{ __html: JSON.stringify(researchProjectJsonLd) }}
        />
        <a
          href="#main"
          className="sr-only focus:not-sr-only focus:fixed focus:top-4 focus:left-4 focus:z-50 focus:rounded-md focus:bg-slate-100 focus:px-4 focus:py-2 focus:text-slate-950 focus:ring-2 focus:ring-blue-400"
        >
          Skip to main content
        </a>
        <Navbar />
        <main id="main" className="pt-16">
          <ReproducerProvider>{children}</ReproducerProvider>
        </main>
        <Footer />
        <Analytics />
      </body>
    </html>
  );
}
