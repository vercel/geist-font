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

### How Releases Work

1. **On every push**: The CI builds fonts and runs tests
2. **On push to `main`**:
   - If there are changeset files, the CI creates a "Version Packages" PR that bumps versions
   - When that PR is merged, the CI publishes to npm (named [geist](https://www.npmjs.com/package/geist?activeTab=readme)) and creates a GitHub release
   - An additional step attaches a zip file containing only the relevant font files to the GitHub release

### Manual Steps

1. Create a PR with your changes and a changeset file
2. Get the PR reviewed and merged to `main`
3. A "Version Packages" PR will automatically be raised — review and merge it
4. Upon merging the PR, CI will automatically publish to npm and create the GitHub release
