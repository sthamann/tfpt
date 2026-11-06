/** Authored steps reuse the existing constructions. The canvas is a reading aid. */
export type JourneyStep = {
  short: string;
  from?: readonly number[];
  additional?: string;
  title: string;
  body: string;
  input: string;
  operation: string;
  output: string;
  formula: string;
  detail: string;
  href: string;
};
export type JourneySpec = { name: string; steps: readonly JourneyStep[] };
export type JourneyComparison = { predicted: number; central: string; uncertaintyMinus: string; date: string; measured: string };
export type DrawKit = {
  ctx: CanvasRenderingContext2D;
  progress: number;
  active: boolean;
  color: string;
  text: (value: string, x: number, y: number, size?: number, color?: string, weight?: number) => void;
  dot: (x: number, y: number, radius: number, color: string, stroke?: string) => void;
  line: (x1: number, y1: number, x2: number, y2: number, color?: string, dashed?: boolean) => void;
  bar: (x: number, y: number, width: number, height: number, fraction: number, color?: string) => void;
};
export const journeyColors = ["#a8c7ff", "#79dcc5", "#eec29c", "#c4b1ee"];
export const clampJourney = (value: number) => Math.max(0, Math.min(1, value));
export const easeJourney = (value: number) => 1 - (1 - clampJourney(value)) ** 3;
