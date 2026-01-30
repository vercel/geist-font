import localFont from "next/font/local";

const monoFallback = [
  "Geist Mono",
  "ui-monospace",
  "SFMono-Regular",
  "Roboto Mono",
  "Menlo",
  "Monaco",
  "Liberation Mono",
  "DejaVu Sans Mono",
  "Courier New",
  "monospace",
];

export const GeistPixelSquare = localFont({
  src: "./fonts/geist-pixel/GeistPixel-Square.woff2",
  variable: "--font-geist-pixel-square",
  weight: "500",
  fallback: monoFallback,
  adjustFontFallback: false,
});

export const GeistPixelGrid = localFont({
  src: "./fonts/geist-pixel/GeistPixel-Grid.woff2",
  variable: "--font-geist-pixel-grid",
  weight: "500",
  fallback: monoFallback,
  adjustFontFallback: false,
});

export const GeistPixelCircle = localFont({
  src: "./fonts/geist-pixel/GeistPixel-Circle.woff2",
  variable: "--font-geist-pixel-circle",
  weight: "500",
  fallback: monoFallback,
  adjustFontFallback: false,
});

export const GeistPixelTriangle = localFont({
  src: "./fonts/geist-pixel/GeistPixel-Triangle.woff2",
  variable: "--font-geist-pixel-triangle",
  weight: "500",
  fallback: monoFallback,
  adjustFontFallback: false,
});

export const GeistPixelLine = localFont({
  src: "./fonts/geist-pixel/GeistPixel-Line.woff2",
  variable: "--font-geist-pixel-line",
  weight: "500",
  fallback: monoFallback,
  adjustFontFallback: false,
});
