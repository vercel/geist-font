import localFont from "next/font/local";

export const GeistSerif = localFont({
  src: "./fonts/geist-serif/GeistSerifVF.woff2",
  variable: "--font-geist-serif",
  weight: "400",
  fallback: ["Times New Roman", "Times", "serif"],
  adjustFontFallback: "Times New Roman",
});

export const GeistSerifRegular = localFont({
  src: "./fonts/geist-serif/GeistSerif-Regular.woff2",
  variable: "--font-geist-serif-regular",
  weight: "400",
  fallback: ["Times New Roman", "Times", "serif"],
  adjustFontFallback: "Times New Roman",
});

export const GeistSerifSquare = localFont({
  src: "./fonts/geist-serif/GeistSerif-Square.woff2",
  variable: "--font-geist-serif-square",
  weight: "400",
  fallback: ["Times New Roman", "Times", "serif"],
  adjustFontFallback: "Times New Roman",
});

export const GeistSerifTriangle = localFont({
  src: "./fonts/geist-serif/GeistSerif-Triangle.woff2",
  variable: "--font-geist-serif-triangle",
  weight: "400",
  fallback: ["Times New Roman", "Times", "serif"],
  adjustFontFallback: "Times New Roman",
});

export const GeistSerifHeart = localFont({
  src: "./fonts/geist-serif/GeistSerif-Heart.woff2",
  variable: "--font-geist-serif-heart",
  weight: "400",
  fallback: ["Times New Roman", "Times", "serif"],
  adjustFontFallback: "Times New Roman",
});
