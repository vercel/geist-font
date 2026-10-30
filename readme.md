# Geist

![The word "Geist." set in bold Geist Sans. Below are four font specimens, each showing the alphabet in uppercase and lowercase, numbers, and symbols:
Sans - A modern sans-serif typeface. Serif - A high-contrast display serif. Mono - A monospaced typeface with fixed-width spacing ideal for coding. Pixel - A pixelated bitmap-style typeface with a retro digital aesthetic.](./documentation/img/geist-banner--light.png#gh-light-mode-only)
![The word "Geist." set in bold Geist Sans. Below are four font specimens, each showing the alphabet in uppercase and lowercase, numbers, and symbols:
Sans - A modern sans-serif typeface. Serif - A high-contrast display serif. Mono - A monospaced typeface with fixed-width spacing ideal for coding. Pixel - A pixelated bitmap-style typeface with a retro digital aesthetic.](./documentation/img/geist-banner--dark.png#gh-dark-mode-only)

# Geist Sans, Geist Mono, Geist Pixel & Geist Serif

Geist is a font family created by [Vercel](https://vercel.com/design). Geist Sans and Geist Mono were created in collaboration with [Basement Studio](https://basement.studio/). Geist Pixel was created in collaboration with [Andrés Briganti](https://briganti.works). Geist Serif was created in collaboration with [Andrés Briganti](https://briganti.works) and [Mark Davis](https://designermarkdavis.com/Cal-Sans).

Geist Sans is a sans-serif typeface designed for legibility and simplicity. It is a modern, geometric typeface that is based on the principles of [classic Swiss typography](https://en.wikipedia.org/wiki/International_Typographic_Style). It is designed to be used in headlines, logos, posters, and other large display sizes.

Geist Mono is a monospaced typeface that has been crafted to be the perfect partner to Geist Sans. It is designed to be used in code editors, diagrams, terminals, and other textbased interfaces where code is represented.

Geist Pixel is a pixel typeface designed to complement the Geist font family, built on the same principles of minimalism, precision, and simplicity that define the universe. Conceived as a display font, it pays homage to the pixel font genre while expressing the brand’s future-forward, visionary spirit, and is available in five stylistic variants for a wide range of applications.

Geist Serif is a high-contrast display serif with fine, saw-toothed serifs and sharp hairlines. Its Regular and Square variants are suited to primary typography, while Triangle and Heart offer more decorative alternatives.

### Installation

Download the latest release from the [releases page](https://github.com/vercel/geist-font/releases/latest) and install the fonts on your system.

**Via npm package:**

```
npm i geist
```

Geist Pixel and Geist Serif have scoped entry points, so you can import a single variant and ship only its font file, for example `geist/font/pixel/grid` or `geist/font/serif/square`, or the variable font from `geist/font/pixel/variable` and `geist/font/serif/variable`. View the npm README for full instructions [here](https://www.npmjs.com/package/geist).

**Via Google Fonts:**

[Geist](https://fonts.google.com/specimen/Geist), [Geist Mono](https://fonts.google.com/specimen/Geist+Mono), and [Geist Pixel](https://fonts.google.com/specimen/Geist+Pixel) are available on Google Fonts. On Google Fonts, Geist Pixel ships as one variable family that selects its shape through the `ELSH` axis. Geist Serif is not on Google Fonts yet; install it from the releases page or via npm.

### Inspiration

Geist has been influenced and inspired by the following typefaces: [Inter](https://rsms.me/inter/), [Univers](https://www.linotype.com/1212814/univers-family.html), [SF Mono](https://developer.apple.com/fonts/), [SF Pro](https://developer.apple.com/fonts/), [Suisse International](https://www.swisstypefaces.com/fonts/suisse/), [ABC Diatype Mono](https://abcdinamo.com/typefaces/diatype), and [ABC Diatype](https://abcdinamo.com/typefaces/diatype). We thank the creators of these typefaces for their craft.

## Building

Fonts are built automatically by GitHub Actions - take a look in the "Actions" tab for the latest build.

If you want to build fonts manually on your own computer:

- `make build` will produce font files.
- `make test` will run [Fontspector](https://github.com/fonttools/fontspector)'s quality assurance tests.
- `make proof` will generate HTML proof files.

The proof files and QA tests are also available automatically via GitHub Actions - look at https://vercel.github.io/geist-font/.

## License

This Font Software is licensed under the SIL Open Font License, Version 1.1.
This license is available with a FAQ at
https://scripts.sil.org/OFL

## Repository Layout

This font repository structure is inspired by [Unified Font Repository v0.3](https://github.com/unified-font-repository/Unified-Font-Repository), modified for the Google Fonts workflow.
