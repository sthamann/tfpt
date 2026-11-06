/** Numerical views of the existing public constructions, not new physical models. */
export type Root = { vector: number[]; coset: number };
export function makeE8Roots(): Root[] {
  const roots: Root[] = [];
  for (let i = 0; i < 8; i++) for (let j = i + 1; j < 8; j++) {
    for (const a of [-1, 1]) for (const b of [-1, 1]) {
      const vector = Array<number>(8).fill(0); vector[i] = a; vector[j] = b;
      roots.push({ vector, coset: i < 5 && j >= 5 ? 2 : 0 });
    }
  }
  for (let mask = 0; mask < 256; mask++) {
    const vector = Array.from({ length: 8 }, (_, i) => mask & (1 << i) ? -.5 : .5);
    if (vector.filter(x => x < 0).length % 2 === 0) {
      roots.push({ vector, coset: vector.slice(0, 5).filter(x => x < 0).length % 2 ? 3 : 1 });
    }
  }
  return roots;
}
export const E8_ROOTS = makeE8Roots();
export const inner = (a: number[], b: number[]) => a.reduce((sum, x, i) => sum + x * b[i], 0);
export const C3 = 1 / (8 * Math.PI);
export const FIXED_SEED = 1 / (6 * Math.PI) + 48 * C3 ** 4;
export function alphaResidual(alpha: number) {
  const q = 48 * C3 ** 4 * Math.exp(-2 * alpha);
  const response = 1 / (6 * Math.PI) + q * (1 - q) ** (-5 / 4);
  return alpha ** 3 - 2 * C3 ** 3 * alpha ** 2 - (4 / 5) * 41 * C3 ** 6 * Math.log(1 / response);
}
export function alphaRoot() {
  let lo = 1 / 145, hi = 1 / 130;
  for (let i = 0; i < 80; i++) {
    const mid = (lo + hi) / 2;
    if (alphaResidual(mid) > 0) hi = mid; else lo = mid;
  }
  return (lo + hi) / 2;
}
export const TRANSFER_RATES = [1, (2 / 3) ** 6, (1 / 3) ** 6] as const;
export function familyTransfer(initial: number[], n: number) {
  const u2 = [1 / Math.sqrt(2), -1 / Math.sqrt(2), 0];
  const u3 = [1 / Math.sqrt(6), 1 / Math.sqrt(6), -2 / Math.sqrt(6)];
  const a2 = inner(initial, u2), a3 = inner(initial, u3);
  const average = initial.reduce((sum, x) => sum + x, 0) / 3;
  return initial.map((_, i) => average + a2 * TRANSFER_RATES[1] ** n * u2[i] + a3 * TRANSFER_RATES[2] ** n * u3[i]);
}
export const seedReadouts = (u: number) => [
  Math.sqrt(u * (1 - u)), u * Math.exp(-5 / 6), u / (4 * Math.PI) * 180 / Math.PI, (1 - 1 / (4 * Math.PI)) * u,
];
