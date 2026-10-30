import localFont from "next/font/local";

export const GeistSerifTriangle = localFont({
  src: "./fonts/geist-serif/GeistSerif-Triangle.woff2",
  variable: "--font-geist-serif-triangle",
  weight: "400",
  fallback: ["Times New Roman", "Times", "serif"],
  adjustFontFallback: "Times New Roman",
});
