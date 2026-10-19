import localFont from "next/font/local";

export const GeistPixelGrid = localFont({
  src: "./fonts/geist-pixel/GeistPixel-Grid.woff2",
  variable: "--font-geist-pixel-grid",
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
