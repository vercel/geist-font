import localFont from "next/font/local";

export const GeistSerifSquare = localFont({
  src: "./fonts/geist-serif/GeistSerif-Square.woff2",
  variable: "--font-geist-serif-square",
  weight: "400",
  fallback: ["Times New Roman", "Times", "serif"],
  adjustFontFallback: "Times New Roman",
});
