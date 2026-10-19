import localFont from "next/font/local";

export const GeistSerifHeart = localFont({
  src: "./fonts/geist-serif/GeistSerif-Heart.woff2",
  variable: "--font-geist-serif-heart",
  weight: "400",
  fallback: ["Times New Roman", "Times", "serif"],
  adjustFontFallback: "Times New Roman",
});
