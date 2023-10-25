import { NextFont } from "@next/font";

declare module "geist/font" {
  /**
   * Geist Sans font, with `className` and `variable` properties,
   * meant to be attached to DOM elements via `className`
   *
   * Included weights: 100, 200, 300, 400, 500, 600, 700, 800, 900
   *
   * * {@link https://github.com/vercel/geist-font/releases Download font files}
   *
   * * {@link https://www.npmjs.com/package/geist#with-tailwind-css View Tailwind example}
   */
  export const GeistSans: NextFont;
  /**
   * Geist Mono font, with `className` and `variable` properties,
   * meant to be attached to DOM elements via `className`
   *
   * Included weights: 100, 200, 300, 400, 500, 600, 700, 800, 900
   *
   * * {@link https://github.com/vercel/geist-font/releases Download font files}
   *
   * * {@link https://www.npmjs.com/package/geist#with-tailwind-css View Tailwind example}
   */
  export const GeistMono: NextFont;
}
