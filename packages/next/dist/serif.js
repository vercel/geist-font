import localFont from "next/font/local";

export const GeistSerif = localFont({
  src: "./fonts/geist-serif/GeistSerifVF.woff2",
  variable: "--font-geist-serif",
  weight: "400",
  fallback: ["Times New Roman", "Times", "serif"],
  adjustFontFallback: "Times New Roman",
});
