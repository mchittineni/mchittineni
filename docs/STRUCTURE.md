# 📁 Repository Structure

This is a **GitHub special profile repository** (`mchittineni/mchittineni`) — its
`README.md` renders directly on the [profile page](https://github.com/mchittineni).
Everything here exists to build, refresh, and display that page automatically.

```text
mchittineni/
├── README.md                     # The profile page rendered on github.com/mchittineni
├── LICENSE                       # MIT
├── .gitignore                    # Ignores local/editor/agent artifacts
│
├── .github/
│   └── workflows/
│       ├── metrics.yaml          # Generates GitHub metrics SVGs + monthly reports
│       └── snake.yaml            # Generates the contribution-snake animation
│
├── assets/
│   ├── metrics/                  # Auto-generated metric SVGs (committed by CI)
│   │   ├── github-metrics.svg    # Full terminal dashboard
│   │   ├── metrics.plugin.*.svg  # Calendars, languages, habits, topics, stargazers
│   │   └── README.md             # Reference for each generated asset
│   └── snake/                    # Auto-generated contribution-snake animation
│
└── docs/
    └── STRUCTURE.md              # This file
```

## How it stays up to date

| Workflow        | Trigger                          | Output                         |
| --------------- | -------------------------------- | ------------------------------ |
| `metrics.yaml`  | Monthly (1st @ 00:00) + manual   | `assets/metrics/*.svg`         |
| `snake.yaml`    | Every 12h + push to `main`       | `assets/snake/*`               |

## Conventions

- **Generated files** live under `assets/` and are committed by CI — do not edit by hand.
- **Hand-authored content** lives in `README.md` and `docs/`.
- Workflows are pinned to descriptive `name:` values and share a `concurrency`
  group so overlapping runs never race on committed SVGs.

## Required secrets

| Secret           | Used by        | Purpose                                            |
| ---------------- | -------------- | -------------------------------------------------- |
| `METRICS_TOKEN`  | `metrics.yaml` | PAT for the `lowlighter/metrics` action            |
| `GITHUB_TOKEN`   | `metrics.yaml` | Built-in token for issue/contributor reports       |
