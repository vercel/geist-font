import localFont from "next/font/local";

export const GeistPixelCircle = localFont({
  src: "./fonts/geist-pixel/GeistPixel-Circle.woff2",
  variable: "--font-geist-pixel-circle",
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
