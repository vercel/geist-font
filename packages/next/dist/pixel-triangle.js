import localFont from "next/font/local";

export const GeistPixelTriangle = localFont({
  src: "./fonts/geist-pixel/GeistPixel-Triangle.woff2",
  variable: "--font-geist-pixel-triangle",
  weight: "500",
  fallback: [
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
  ],
  adjustFontFallback: false,
});
