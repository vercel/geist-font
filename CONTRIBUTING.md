# Contributing to Geist Font

## Development

### Prerequisites

- Python 3.10
- Node.js (supported version in `.nvmrc`, prefer using [fnm](https://github.com/Schniz/fnm) for installing)
- pnpm (via [corepack](https://github.com/nodejs/corepack))

### Building Fonts

```bash
make build
```

This will:

1. Build font files from source into `fonts/`
2. Copy and rename fonts for the npm package into `packages/next/dist/fonts/`
3. Create `geist-font.zip` with all of the fonts neatly packaged together

## Release Process

This project uses [Changesets](https://github.com/changesets/changesets) to manage versioning and releases. When changes are merged to `main`, CI will automatically handle npm publishing and GitHub releases.

### Adding a Changeset

When making changes that should be released, add a changeset:

```bash
cd packages/next
# If you haven't installed dependencies already:
pnpm install
pnpm changeset
```

You'll be prompted to:

1. Select the type of change (`patch`, `minor`, or `major` - read more about SemVer at [semver.org](https://semver.org/))
2. Write a summary of the changes

This creates a markdown file in `packages/next/.changeset/` describing your change.

### Version Guidelines

- **patch**: Bug fixes, font corrections, minor adjustments
- **minor**: New font weights, new features, backward-compatible additions
- **major**: Breaking changes to the npm package's API or major font structure changes

### Version Numbers

Three version numbers live in this repo. They must all describe the same release:

1. **Package version**: `version` in `packages/next/package.json`, managed by Changesets and published as the npm `geist` semver (e.g. `1.8.1`).
2. **Font binary version**: `versionMajor`/`versionMinor` in each `sources/*.glyphspackage/fontinfo.plist`, baked into the built fonts as `head.fontRevision` and name ID 5. This is what an OS or design tool reports for an installed font (e.g. `Version 1.801`).
3. **GitHub release tag**: `v$VERSION`, matching the package version (e.g. `v1.8.1`). Since [#233](https://github.com/vercel/geist-font/pull/233) Changesets creates it; don't create releases by hand.

The font binary version follows the package version: `M.X.Y` → `versionMajor = M`, `versionMinor = X * 100 + Y`. For example, `1.7.0` ↔ `1.700`, `1.8.0` ↔ `1.800`, `1.8.1` ↔ `1.801`. This works while `X` ≤ 9 and `Y` ≤ 99.

CI rebuilds Geist and Geist Mono from `sources/` for every npm release, so every release ships new binaries. Whenever you add a changeset, set `versionMinor` in all Geist and Geist Mono sources (roman and italic) to the version the next release will get, including families whose glyphs didn't change. If another pending changeset already did this, there's nothing to change.

Geist Pixel is the exception: its static fonts and webfonts are exported by hand from Glyphs and committed (see the `Makefile`), so its version only changes when those files are re-exported.

### How Releases Work

1. **On every push**: The CI builds fonts and runs tests
2. **On push to `main`**:
   - If there are changeset files, the CI creates a PR titled "changesets: update versions of packages for release"
   - When that PR is merged, the CI publishes to npm (named [geist](https://www.npmjs.com/package/geist?activeTab=readme)) and creates a GitHub release
   - An additional step attaches a zip file containing only the relevant font files to the GitHub release

### Manual Steps

1. Create a PR with your changes and a changeset file
2. Get the PR reviewed and merged to `main`
3. A PR titled "changesets: update versions of packages for release" will automatically be raised — review and merge it
4. Upon merging the PR, CI will automatically publish to npm and create the GitHub release

