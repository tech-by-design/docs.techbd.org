# TechBD's public documentation site

## 🚀 Project Structure

You'll see the following folders and files:

```
.
├── assurance/
│   └── 1115-waiver/ahc-hrsn/screening/regression-test-prime/
│       ├── fhir-service-prime/
│       │   └── src/
│       │       └── YYYY-MM-DD/
|       └── regression-test.sh
├── public/
│   └── assurance/1115-waiver/ahc-hrsn/screening/regression-test-prime/
│       └── fhir-service-prime/
│           └── results/
│               ├── YYYY-MM/YYYY-MM-DD-HH-MM-SS/
│               |   └── src -> /assurance/1115-waiver/ahc-hrsn/screening/regression-test-prime/YYYY-MM-DD/ (symlink to test scripts and fixtures) 
│               └── latest -> YYYY-MM/YYYY-MM-DD-HH-MM-SS/ (symlink to most recent execution)
├── src/
│   ├── assets/
│   ├── content/
│   │   ├── docs/
│   │   └── config.ts
│   └── env.d.ts
├── astro.config.mjs
├── package.json
└── tsconfig.json
```

Starlight looks for `.md` or `.mdx` files in the `src/content/docs/` directory. Each file is exposed as a route based on its file name.

Images can be added to `src/assets/` and embedded in Markdown with a relative link.

Static assets, like favicons, can be placed in the `public/` directory.

## 🧞 Commands

All commands are run from the root of the project, from a terminal:

| Command                    | Action                                           |
| :------------------------- | :----------------------------------------------- |
| `pnpm install`             | Installs dependencies                            |
| `pnpm run dev`             | Starts local dev server at `localhost:4321`      |
| `pnpm run build`           | Build your production site to `./dist/`          |
| `pnpm run preview`         | Preview your build locally, before deploying     |
| `pnpm run astro check`     | Validate documentation build artifacts           |
| `pnpm run astro ...`       | Run CLI commands like `astro add`, `astro check` |
| `pnpm run astro -- --help` | Get help using the Astro CLI                     |

Special commands

| Command                            | Action                                                      |
| :--------------------------------- | :---------------------------------------------------------- |
| `pnpm gen-regression-test-results` | Generate all regression test results in `public/assurance`  |

## 👀 Want to learn more?

Check out [Starlight’s docs](https://starlight.astro.build/), read [the Astro documentation](https://docs.astro.build), or jump into the [Astro Discord server](https://astro.build/chat).

[![Built with Starlight](https://astro.badg.es/v2/built-with-starlight/tiny.svg)](https://starlight.astro.build)
