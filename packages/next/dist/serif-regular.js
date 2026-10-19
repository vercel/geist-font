import localFont from "next/font/local";

export const GeistSerifRegular = localFont({
  src: "./fonts/geist-serif/GeistSerif-Regular.woff2",
  variable: "--font-geist-serif-regular",
  weight: "400",
  fallback: ["Times New Roman", "Times", "serif"],
  adjustFontFallback: "Times New Roman",
});
