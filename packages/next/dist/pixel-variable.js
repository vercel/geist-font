import localFont from "next/font/local";

export const GeistPixel = localFont({
  src: "./fonts/geist-pixel/GeistPixelVF.woff2",
  variable: "--font-geist-pixel",
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
