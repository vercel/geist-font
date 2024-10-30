# Geist

[![][Fontbakery]](https://vercel.github.io/geist-font/fontbakery/fontbakery-report.html)
[![][Universal]](https://vercel.github.io/geist-font/fontbakery/fontbakery-report.html)
[![][Shaping]](https://vercel.github.io/geist-font/fontbakery/fontbakery-report.html)

[Fontbakery]: https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fvercel%2Fgeist-font%2Fgh-pages%2Fbadges%2Foverall.json
[Outline Correctness]: https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fvercel%2Fgeist-font%2Fgh-pages%2Fbadges%2FOutlineChecks.json
[Shaping]: https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fvercel%2Fgeist-font%2Fgh-pages%2Fbadges%2FShapingChecks.json
[Universal]: https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fvercel%2Fgeist-font%2Fgh-pages%2Fbadges%2FUniversalProfileChecks.json

![The words “Geist” written as ASCII art in Geist Mono resembling Geist Sans. After this is a demonstration of Geist Sans in regular and bold face that shows alphanumeric characters and some symbols, notably a symbol for Shift, a right arrow, and the Vercel logo. Below is some text written in Geist - a heading: “Geist truly represents the coding and design spirit within Vercel's creator community.”, one paragraph: “At Vercel, we've developed Geist, a typeface specifically designed for developers and designers. We began by creating a monospace version that prioritized readability and seamlessly integrated into coding environments. After perfecting the monospace variant, we expanded Geist into a Sans version, adding versatility to its capabilities.”, and another next to it: “Geist embodies our design principles of simplicity, minimalism, and speed, drawing inspiration from the renowned Swiss design movement. With precision, clarity, and functionality at its core, Geist enhances the visual experience of developers and designers, empowering them to effectively communicate their ideas.”](./documentation/img/geist-banner--light.png#gh-light-mode-only)
![The words “Geist” written as ASCII art in Geist Mono resembling Geist Sans. After this is a demonstration of Geist Sans in regular and bold face that shows alphanumeric characters and some symbols, notably a symbol for Shift, a right arrow, and the Vercel logo. Below is some text written in Geist - a heading: “Geist truly represents the coding and design spirit within Vercel's creator community.”, one paragraph: “At Vercel, we've developed Geist, a typeface specifically designed for developers and designers. We began by creating a monospace version that prioritized readability and seamlessly integrated into coding environments. After perfecting the monospace variant, we expanded Geist into a Sans version, adding versatility to its capabilities.”, and another next to it: “Geist embodies our design principles of simplicity, minimalism, and speed, drawing inspiration from the renowned Swiss design movement. With precision, clarity, and functionality at its core, Geist enhances the visual experience of developers and designers, empowering them to effectively communicate their ideas.”](./documentation/img/geist-banner--dark.png#gh-dark-mode-only)

# Geist Sans & Geist Mono
Geist is a new font family for Vercel, created by [Vercel](https://vercel.com/design) in collaboration with [Basement Studio](https://basement.studio/).

Geist Sans is a sans-serif typeface designed for legibility and simplicity. It is a modern, geometric typeface that is based on the principles of [classic Swiss typography](https://en.wikipedia.org/wiki/International_Typographic_Style). It is designed to be used in headlines, logos, posters, and other large display sizes.

Geist Mono is a monospaced typeface that has been crafted to be the perfect partner to Geist Sans. It is designed to be used in code editors, diagrams, terminals, and other textbased interfaces where code is represented.

### Installation

Download the latest release from the [releases page](https://github.com/vercel/geist-font/releases/latest) and install the fonts on your system.

### Inspiration
Geist has been influenced and inspired by the following typefaces: [Inter](https://rsms.me/inter/), [Univers](https://www.linotype.com/1212814/univers-family.html), [SF Mono](https://developer.apple.com/fonts/), [SF Pro](https://developer.apple.com/fonts/), [Suisse International](https://www.swisstypefaces.com/fonts/suisse/), [ABC Diatype Mono](https://abcdinamo.com/typefaces/diatype), and [ABC Diatype](https://abcdinamo.com/typefaces/diatype). We thank the creators of these typefaces for their craft.

## Building

Fonts are built automatically by GitHub Actions - take a look in the "Actions" tab for the latest build.

If you want to build fonts manually on your own computer:

* `make build` will produce font files.
* `make test` will run [FontBakery](https://github.com/googlefonts/fontbakery)'s quality assurance tests.
* `make proof` will generate HTML proof files.

The proof files and QA tests are also available automatically via GitHub Actions - look at https://guidoferreyra.github.io/Geist.git.

## Changelog

When you update your font (new version or new release), please report all notable changes here, with a date.
Changelog example:

**26 May 2021. Version 2.13**
- MAJOR Font turned to a variable font.
- SIGNIFICANT New Stylistic sets added.

## License

This Font Software is licensed under the SIL Open Font License, Version 1.1.
This license is available with a FAQ at
https://scripts.sil.org/OFL

## Repository Layout

This font repository structure is inspired by [Unified Font Repository v0.3](https://github.com/unified-font-repository/Unified-Font-Repository), modified for the Google Fonts workflow.
