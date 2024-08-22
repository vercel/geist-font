![The words “Geist” written as ASCII art in Geist Mono resembling Geist Sans. After this is a demonstration of Geist Sans in regular and bold face that shows alphanumeric characters and some symbols, notably a symbol for Shift, a right arrow, and the Vercel logo. Below is some text written in Geist - a heading: “Geist truly represents the coding and design spirit within Vercel's creator community.”, one paragraph: “At Vercel, we've developed Geist, a typeface specifically designed for developers and designers. We began by creating a monospace version that prioritized readability and seamlessly integrated into coding environments. After perfecting the monospace variant, we expanded Geist into a Sans version, adding versatility to its capabilities.”, and another next to it: “Geist embodies our design principles of simplicity, minimalism, and speed, drawing inspiration from the renowned Swiss design movement. With precision, clarity, and functionality at its core, Geist enhances the visual experience of developers and designers, empowering them to effectively communicate their ideas.”](./.docs/img/geist-banner--light.png#gh-light-mode-only)
![The words “Geist” written as ASCII art in Geist Mono resembling Geist Sans. After this is a demonstration of Geist Sans in regular and bold face that shows alphanumeric characters and some symbols, notably a symbol for Shift, a right arrow, and the Vercel logo. Below is some text written in Geist - a heading: “Geist truly represents the coding and design spirit within Vercel's creator community.”, one paragraph: “At Vercel, we've developed Geist, a typeface specifically designed for developers and designers. We began by creating a monospace version that prioritized readability and seamlessly integrated into coding environments. After perfecting the monospace variant, we expanded Geist into a Sans version, adding versatility to its capabilities.”, and another next to it: “Geist embodies our design principles of simplicity, minimalism, and speed, drawing inspiration from the renowned Swiss design movement. With precision, clarity, and functionality at its core, Geist enhances the visual experience of developers and designers, empowering them to effectively communicate their ideas.”](./.docs/img/geist-banner--dark.png#gh-dark-mode-only)

# Geist Sans & Geist Mono
Geist is a new font family for Vercel, created by [Vercel](https://vercel.com/design) in collaboration with [Basement Studio](https://basement.studio/).

Geist Sans is a sans-serif typeface designed for legibility and simplicity. It is a modern, geometric typeface that is based on the principles of [classic Swiss typography](https://en.wikipedia.org/wiki/International_Typographic_Style). It is designed to be used in headlines, logos, posters, and other large display sizes.

Geist Mono is a monospaced typeface that has been crafted to be the perfect partner to Geist Sans. It is designed to be used in code editors, diagrams, terminals, and other textbased interfaces where code is represented.

### Download

Download the latest release from the [releases page](https://github.com/vercel/geist-font/releases/latest) and install the fonts on your system.
* [Download Geist Sans](https://github.com/vercel/geist-font/releases/download/1.3.0/Geist-1.3.0.zip)
* [Download Geist Mono](https://github.com/vercel/geist-font/releases/download/1.3.0/GeistMono-1.3.0.zip)

### Installation
#### Use in Next.js
GeistSans is exported from geist/font/sans, and GeistMono can be found in geist/font/mono. Both are NextFontWithVariable instances. You can learn more by [reading the next/font docs.](https://nextjs.org/docs/app/building-your-application/optimizing/fonts)
```sh
npm install geist
```

##### App Router
In ```app/layout.js```:

```js
import { GeistSans } from "geist/font/sans";

export default function RootLayout({
  children,
}) {
  return (
    <html lang="en" className={GeistSans.className}>
      <body>{children}</body>
    </html>
  )
}
```

##### Pages Router
In ```pages/_app.js```:

```js
import { GeistSans } from "geist/font/sans";

export default function MyApp({ Component, pageProps }) {
  return (
    <main className={GeistSans.className}>
      <Component {...pageProps} />
    </main>
  )
}
```
##### With Tailwind CSS
```GeistSans``` and ```GeistMono``` can be used through a CSS variable.

- ```GeistSans```: ```--font-geist-sans```
- ```GeistMono```: ```--font-geist-mono```
   
In ```app/layout.js```:
```js
import { GeistSans } from 'geist/font/sans'
import { GeistMono } from 'geist/font/mono'

export default function RootLayout({
  children,
}) {
  return (
    <html lang="en" className={`${GeistSans.variable} ${GeistMono.variable}`}>
      <body>{children}</body>
    </html>
  )
}
```
Then in ```tailwind.config.js```:

```js
module.exports = {
  theme: {
    extend: {
      fontFamily: {
        sans: ['var(--font-geist-sans)'],
        mono: ['var(--font-geist-mono)'],
      },
    },
  },
}
```

#### Use in Astro 

You can download the font and add it manually to your project with @font-face . You can learn more by
[reading MDN’s web fonts guide.](https://developer.mozilla.org/en-US/docs/Web/CSS/@font-face)
Another choice Generate CSS for your font with [Font Squirrel’s Webfont Generator.](https://www.fontsquirrel.com/tools/webfont-generator) better one Using [fontsource](https://fontsource.org/)

##### Using Fontsource

```sh
npm install @fontsource/geist-sans 
```
```sh
npm install @fontsource/geist-mono
```

In ```src/layouts/MainLayout.astro```:
```js
import '@fontsource/geist-mono';
import '@fontsource/geist-sans';
```

In ```src/styles/global.css```:
```css
body {
  font-family: 'Geist Sans', sans-serif;
}

/* or */

body {
  font-family: 'Geist Mono';
}
```

### License
The Geist font family is free and open sourced under the [SIL Open Font License](./LICENSE.txt).

### Inspiration
Geist has been influenced and inspired by the following typefaces: [Inter](https://rsms.me/inter/), [Univers](https://www.linotype.com/1212814/univers-family.html), [SF Mono](https://developer.apple.com/fonts/), [SF Pro](https://developer.apple.com/fonts/), [Suisse International](https://www.swisstypefaces.com/fonts/suisse/), [ABC Diatype Mono](https://abcdinamo.com/typefaces/diatype), and [ABC Diatype](https://abcdinamo.com/typefaces/diatype). We thank the creators of these typefaces for their craft.
