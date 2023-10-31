import localFont from "next/font/local";

export const GeistSans = localFont({
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
  variable: "--font-geist-sans",
  fallback: [
    "ui-sans-serif",
    "system-ui",
    "-apple-system",
    "BlinkMacSystemFont",
    "Inter",
    "Segoe UI",
    "Roboto",
    "sans-serif",
    "Apple Color Emoji",
    "Segoe UI Emoji",
    "Segoe UI Symbol",
    "Noto Color Emoji",
  ],
});

export const GeistMono = localFont({
  src: [
    {
      path: "./fonts/geist-mono/GeistMono-Thin.woff2",
      weight: "100",
      style: "normal",
    },
    {
      path: "./fonts/geist-mono/GeistMono-UltraLight.woff2",
      weight: "200",
      style: "normal",
    },
    {
      path: "./fonts/geist-mono/GeistMono-Light.woff2",
      weight: "300",
      style: "normal",
    },
    {
      path: "./fonts/geist-mono/GeistMono-Regular.woff2",
      weight: "400",
      style: "normal",
    },
    {
      path: "./fonts/geist-mono/GeistMono-Medium.woff2",
      weight: "500",
      style: "normal",
    },
    {
      path: "./fonts/geist-mono/GeistMono-SemiBold.woff2",
      weight: "600",
      style: "normal",
    },
    {
      path: "./fonts/geist-mono/GeistMono-Bold.woff2",
      weight: "700",
      style: "normal",
    },
    {
      path: "./fonts/geist-mono/GeistMono-Black.woff2",
      weight: "800",
      style: "normal",
    },
    {
      path: "./fonts/geist-mono/GeistMono-UltraBlack.woff2",
      weight: "900",
      style: "normal",
    },
  ],
  variable: "--font-geist-mono",
  adjustFontFallback: false,
  fallback: [
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
});
