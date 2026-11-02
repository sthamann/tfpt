"use client";

import { useEffect } from "react";

const destinations: Record<string, string> = {
  "step-two-numbers": "/explain#inputs",
  "step-compiler": "/explain#e8",
  "step-outputs": "/explain#theory-map",
  "step-not-numerology": "/explain#status",
  "step-seam": "/explain#inputs",
  "step-check-yourself": "/verification#first-check",
  "step-how-it-dies": "/explain#status",
  "step-still-open": "/explain#source",
  "step-two-bridges": "/explain#source",
  "step-join-in": "/verification#first-check",
};
const currentAnchors = new Set(["inputs", "e8", "matter", "flavor", "alpha", "clocks", "quantum", "source", "status", "theory-map"]);

/** Translate legacy fragments before navigating to the current learning route. */
export function LegacyTourRedirect() {
  useEffect(() => {
    const fragment = window.location.hash.slice(1);
    const destination = destinations[fragment] ?? (currentAnchors.has(fragment) ? "/explain#" + fragment : "/explain");
    window.location.replace(destination);
  }, []);
  return null;
}
