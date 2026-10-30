import localFont from "next/font/local";

export const GeistPixelLine = localFont({
  src: "./fonts/geist-pixel/GeistPixel-Line.woff2",
  variable: "--font-geist-pixel-line",
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
