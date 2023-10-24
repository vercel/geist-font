import { NextFont } from "@next/font";

declare module "geist/font" {
  /**
   * Geist Sans
   *
   * Includes 9 weights: 100, 200, 300, 400, 500, 600, 700, 800, 900
   *
   * You can download the latest font files from {@link https://github.com/vercel/geist-font/releases}
   */
  export const sansFont: NextFont;
  /**
   * Geist Mono
   *
   * Includes 9 weights: 100, 200, 300, 400, 500, 600, 700, 800, 900
   *
   * You can download the latest font files from {@link https://github.com/vercel/geist-font/releases}
   */
  export const monoFont: NextFont;
}
