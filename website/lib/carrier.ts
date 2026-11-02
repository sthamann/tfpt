export const bitCount = (mask: number) => Array.from({ length: 5 }, (_, i) => Number(Boolean(mask & (1 << i)))).reduce((a, b) => a + b, 0);
export const evenMasks = Array.from({ length: 32 }, (_, mask) => mask).filter(mask => bitCount(mask) % 2 === 0);
export const chargeSectors = [
  { label: "νᶜ", mask: 0, multiplicity: 1, x: 0, contribution: 0 },
  { label: "uᶜ", mask: 3, multiplicity: 3, x: -4, contribution: 48 },
  { label: "Q", mask: 9, multiplicity: 6, x: 1, contribution: 6 },
  { label: "eᶜ", mask: 24, multiplicity: 1, x: 6, contribution: 36 },
  { label: "L", mask: 15, multiplicity: 2, x: -3, contribution: 18 },
  { label: "dᶜ", mask: 27, multiplicity: 3, x: 2, contribution: 12 },
];
