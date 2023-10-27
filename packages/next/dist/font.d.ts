import { NextFontWithVariable } from "@next/font";

declare module "geist/font" {
  /**
   * Geist Sans font, with `className` and `variable` properties,
   * meant to be attached to DOM elements via `className`
   *
   * Included weights: 100, 200, 300, 400, 500, 600, 700, 800, 900
   *
   * * {@link https://www.npmjs.com/package/geist?activeTab=readme#app-router View App Router Example}
   *
   * * {@link https://www.npmjs.com/package/geist?activeTab=readme#with-tailwind-css View Tailwind Example}
   *
   * * {@link https://www.npmjs.com/package/geist?activeTab=readme#pages-router View Pages Router Example}
   *
   * * {@link https://github.com/vercel/geist-font/releases Download Font Files}
   */
  export const GeistSans: NextFontWithVariable;
  /**
   * Geist Mono font, with `className` and `variable` properties,
   * meant to be attached to DOM elements via `className`
   *
   * Included weights: 100, 200, 300, 400, 500, 600, 700, 800, 900
   *
   * * {@link https://www.npmjs.com/package/geist?activeTab=readme#app-router View App Router Example}
   *
   * * {@link https://www.npmjs.com/package/geist?activeTab=readme#with-tailwind-css View Tailwind Example}
   *
   * * {@link https://www.npmjs.com/package/geist?activeTab=readme#pages-router View Pages Router Example}
   *
   * * {@link https://github.com/vercel/geist-font/releases Download Font Files}
   */
  export const GeistMono: NextFontWithVariable;
}
