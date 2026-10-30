![](https://raw.githubusercontent.com/vercel/geist-font/main/packages/next/images/hero.png)

# Geist Sans, Geist Mono, Geist Pixel & Geist Serif

Geist is a font family created by [Vercel](https://vercel.com/design). Geist Sans and Geist Mono were created in collaboration with [Basement Studio](https://basement.studio/). Geist Pixel was created in collaboration with [Andrés Briganti](https://briganti.works). Geist Serif was created in collaboration with [Andrés Briganti](https://briganti.works) and [Mark Davis](https://designermarkdavis.com/Cal-Sans).

Geist Sans is a sans-serif typeface designed for legibility and simplicity. It is modern, geometric, and based on the principles of classic Swiss typography. It is designed to be used in body copy, headlines, logos, posters, and other large display sizes.

Geist Mono is a monospaced typeface, crafted to be the perfect partner to Geist Sans. It is designed to be used in code editors, diagrams, terminals, and other text-based interfaces where code is rendered.

Geist Pixel is a display typeface family featuring five unique pixel-based variants, each with a distinct visual style. It is designed for decorative use in headlines, logos, and other display contexts where a pixelated aesthetic is desired.

Geist Serif is a high-contrast display serif with fine, saw-toothed serifs and sharp hairlines. Its Regular and Square variants are suited to primary typography, while Triangle and Heart offer more decorative alternatives.

### Installation

```sh
npm install geist
```

### Using with Next.js

`GeistSans` is exported from `geist/font/sans` and `GeistMono` from `geist/font/mono`. Geist Pixel and Geist Serif each ship a variable entry point (`geist/font/pixel/variable`, `geist/font/serif/variable`) and one entry point per variant (e.g. `geist/font/pixel/grid`, `geist/font/serif/square`), so you only emit and preload the files you import. All are `NextFontWithVariable` instances. You can learn more by [reading the `next/font` docs](https://nextjs.org/docs/app/building-your-application/optimizing/fonts).

#### Geist Serif Variants

Use `GeistSerif` to load one variable font and select its shape through `ELSH`:

```jsx
import { GeistSerif } from "geist/font/serif/variable";
```

| Shape    | `ELSH` value |
| -------- | ------------ |
| Regular  | `0`          |
| Square   | `25`         |
| Triangle | `50`         |
| Heart    | `100`        |

Geist Serif includes four distinct variants: Regular with round dots (the default), Square, Triangle (a nod to the Vercel logo), and Heart. Use their individual entry points to emit and preload only the fonts you import:

| Export               | Entry point                 | CSS Variable                  |
| -------------------- | --------------------------- | ----------------------------- |
| `GeistSerifRegular`  | `geist/font/serif/regular`  | `--font-geist-serif-regular`  |
| `GeistSerifSquare`   | `geist/font/serif/square`   | `--font-geist-serif-square`   |
| `GeistSerifTriangle` | `geist/font/serif/triangle` | `--font-geist-serif-triangle` |
| `GeistSerifHeart`    | `geist/font/serif/heart`    | `--font-geist-serif-heart`    |

```jsx
import { GeistSerifRegular } from "geist/font/serif/regular";
import { GeistSerifSquare } from "geist/font/serif/square";
import { GeistSerifTriangle } from "geist/font/serif/triangle";
import { GeistSerifHeart } from "geist/font/serif/heart";
```

If you need the variable font and all four static variants, the aggregate entry point is available for convenience:

```jsx
import {
  GeistSerif,
  GeistSerifRegular,
  GeistSerifSquare,
  GeistSerifTriangle,
  GeistSerifHeart,
} from "geist/font/serif";
```

The aggregate entry point includes all five font files. Prefer `/variable` or an individual static entry point when you only need one.

#### Geist Pixel Variants

Use `GeistPixel` to load one variable font and select its shape through `ELSH`:

```jsx
import { GeistPixel } from "geist/font/pixel/variable";
```

| Shape    | `ELSH` value |
| -------- | ------------ |
| Regular  | `0`          |
| Square   | `1`          |
| Circle   | `20`         |
| Grid     | `40`         |
| Triangle | `60`         |
| Line     | `80`         |

Geist Pixel includes five distinct variants. Use their individual entry points to emit and preload only the fonts you import:

| Export               | Entry point                 | CSS Variable                  |
| -------------------- | --------------------------- | ----------------------------- |
| `GeistPixelSquare`   | `geist/font/pixel/square`   | `--font-geist-pixel-square`   |
| `GeistPixelGrid`     | `geist/font/pixel/grid`     | `--font-geist-pixel-grid`     |
| `GeistPixelCircle`   | `geist/font/pixel/circle`   | `--font-geist-pixel-circle`   |
| `GeistPixelTriangle` | `geist/font/pixel/triangle` | `--font-geist-pixel-triangle` |
| `GeistPixelLine`     | `geist/font/pixel/line`     | `--font-geist-pixel-line`     |

```jsx
import { GeistPixelSquare } from "geist/font/pixel/square";
import { GeistPixelGrid } from "geist/font/pixel/grid";
import { GeistPixelCircle } from "geist/font/pixel/circle";
import { GeistPixelTriangle } from "geist/font/pixel/triangle";
import { GeistPixelLine } from "geist/font/pixel/line";
```

The aggregate `geist/font/pixel` entry point remains available for backwards compatibility, but it includes all five static font files. The variable font stays isolated at `geist/font/pixel/variable`.

#### App Router

In `app/layout.js`:

```jsx
import { GeistSans } from "geist/font/sans";

export default function RootLayout({ children }) {
  return (
    <html lang="en" className={GeistSans.className}>
      <body>{children}</body>
    </html>
  );
}
```

#### Pages Router

In `pages/_app.js`:

```jsx
import { GeistSans } from "geist/font/sans";

export default function MyApp({ Component, pageProps }) {
  return (
    <main className={GeistSans.className}>
      <Component {...pageProps} />
    </main>
  );
}
```

If you're using a version of Next.js that's older than 15, then in `next.config.js` or `next.config.mjs` add:

```diff js
/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
+  transpilePackages: ["geist"],
};

export default nextConfig;
```

This is required to fix errors like:

- `TypeError: next_font_local__WEBPACK_IMPORTED_MODULE_0___default(...) is not a function`
- `SyntaxError: Cannot use import statement outside a module`

#### With Tailwind CSS

All Geist fonts can be used through CSS variables.

- `GeistSans`: `--font-geist-sans`
- `GeistMono`: `--font-geist-mono`
- `GeistPixel`: `--font-geist-pixel`
- `GeistPixelSquare`: `--font-geist-pixel-square`
- `GeistPixelGrid`: `--font-geist-pixel-grid`
- `GeistPixelCircle`: `--font-geist-pixel-circle`
- `GeistPixelTriangle`: `--font-geist-pixel-triangle`
- `GeistPixelLine`: `--font-geist-pixel-line`
- `GeistSerif`: `--font-geist-serif`
- `GeistSerifRegular`: `--font-geist-serif-regular`
- `GeistSerifSquare`: `--font-geist-serif-square`
- `GeistSerifTriangle`: `--font-geist-serif-triangle`
- `GeistSerifHeart`: `--font-geist-serif-heart`

In `app/layout.js`:

```jsx
import { GeistSans } from "geist/font/sans";
import { GeistMono } from "geist/font/mono";
import { GeistPixelSquare } from "geist/font/pixel/square";
import { GeistSerif } from "geist/font/serif/variable";

export default function RootLayout({ children }) {
  return (
    <html
      lang="en"
      className={`${GeistSans.variable} ${GeistMono.variable} ${GeistPixelSquare.variable} ${GeistSerif.variable}`}
    >
      <body>{children}</body>
    </html>
  );
}
```

##### Tailwind CSS V4

Then in `tailwind.css`:

```css
@theme {
  /* rest of your theme config */

  --font-sans: var(--font-geist-sans);
  --font-mono: var(--font-geist-mono);
  --font-serif: var(--font-geist-serif);
  --font-pixel-square: var(--font-geist-pixel-square);
  --font-pixel-grid: var(--font-geist-pixel-grid);
  --font-pixel-circle: var(--font-geist-pixel-circle);
  --font-pixel-triangle: var(--font-geist-pixel-triangle);
  --font-pixel-line: var(--font-geist-pixel-line);

  /* rest of your theme config */
}
```

##### Tailwind CSS V3

Then in `tailwind.config.js`:

```javascript
module.exports = {
  theme: {
    extend: {
      fontFamily: {
        sans: ["var(--font-geist-sans)"],
        mono: ["var(--font-geist-mono)"],
        serif: ["var(--font-geist-serif)"],
        "pixel-square": ["var(--font-geist-pixel-square)"],
        "pixel-grid": ["var(--font-geist-pixel-grid)"],
        "pixel-circle": ["var(--font-geist-pixel-circle)"],
        "pixel-triangle": ["var(--font-geist-pixel-triangle)"],
        "pixel-line": ["var(--font-geist-pixel-line)"],
      },
    },
  },
};
```

### License

The Geist font family is free and open sourced under the [SIL Open Font License](../../LICENSE.txt).

### Inspiration

Geist has been influenced and inspired by the following typefaces: [Inter](https://rsms.me/inter), [Univers](https://www.linotype.com/1567/univers-family.html), [SF Mono](https://developer.apple.com/fonts/), [SF Pro](https://developer.apple.com/fonts/), [Suisse International](https://www.swisstypefaces.com/fonts/suisse/), [ABC Diatype Mono](https://abcdinamo.com/typefaces/diatype), and [ABC Diatype](https://abcdinamo.com/typefaces/diatype). We thank the creators of these typefaces for their craft.
