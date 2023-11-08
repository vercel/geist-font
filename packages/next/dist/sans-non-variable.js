import localFont from "next/font/local";

export const GeistSansNonVariable = localFont({
  src: [
    {
      path: "./fonts/geist-sans/Geist-Thin.woff2",
      weight: "100",
      style: "normal",
    },
    {
      path: "./fonts/geist-sans/Geist-UltraLight.woff2",
      weight: "200",
      style: "normal",
    },
    {
      path: "./fonts/geist-sans/Geist-Light.woff2",
      weight: "300",
      style: "normal",
    },
    {
      path: "./fonts/geist-sans/Geist-Regular.woff2",
      weight: "400",
      style: "normal",
    },
    {
      path: "./fonts/geist-sans/Geist-Medium.woff2",
      weight: "500",
      style: "normal",
    },
    {
      path: "./fonts/geist-sans/Geist-SemiBold.woff2",
      weight: "600",
      style: "normal",
    },
    {
      path: "./fonts/geist-sans/Geist-Bold.woff2",
      weight: "700",
      style: "normal",
    },
    {
      path: "./fonts/geist-sans/Geist-Black.woff2",
      weight: "800",
      style: "normal",
    },
    {
      path: "./fonts/geist-sans/Geist-UltraBlack.woff2",
      weight: "900",
      style: "normal",
    },
  ],
  variable: "--font-geist-sans-non-variable",
});
