# 📁 Repository Structure

This is a **GitHub special profile repository** (`mchittineni/mchittineni`) — its
`README.md` renders directly on the [profile page](https://github.com/mchittineni).
Everything here exists to build, refresh, and display that page automatically.

```text
mchittineni/
├── README.md                     # Modern profile page for Senior Platform, Cloud & DevOps Engineer
├── LICENSE                       # MIT
├── .gitignore                    # Ignores local/editor/agent artifacts
│
├── .github/
│   └── workflows/
│       ├── metrics.yaml          # Generates GitHub metrics SVGs + monthly activity reports
│       └── snake.yaml            # Generates the contribution-snake animation
│
├── assets/
│   ├── metrics/                  # Auto-generated metric SVGs (committed by CI)
│   │   ├── github-metrics.svg    # Full metrics dashboard
│   │   ├── metrics.plugin.isocalendar.fullyear.svg  # Full-year contribution calendar
│   │   ├── metrics.plugin.habits.*.svg              # Coding-habit charts & facts
│   │   └── README.md             # Reference for each generated asset
│   └── snake/                    # Auto-generated contribution-snake animation
│       ├── snake.svg             # Light mode contribution snake
│       ├── snake-dark.svg        # Dark mode contribution snake
│       └── snake.gif             # Animated GIF version
│
└── docs/
    └── STRUCTURE.md              # This file
```

## How it stays up to date

| Workflow        | Trigger                          | Output                         |
| --------------- | -------------------------------- | ------------------------------ |
| `metrics.yaml`  | Monthly (1st @ 00:00) + manual   | `assets/metrics/*.svg`         |
| `snake.yaml`    | Every 12h + push to `main`       | `assets/snake/*`               |

## Content & Profile Features

The profile `README.md` features a high-impact, modern design representing expertise across:
- **Multi-Cloud Platform Engineering**: AWS, Microsoft Azure, Google Cloud Platform (GCP), Oracle Cloud Infrastructure (OCI).
- **Data Platforms**: Databricks (Unity Catalog, clusters, jobs), Snowflake, Redshift.
- **Infrastructure as Code & Kubernetes**: Reusable Terraform modules (25+ modules), Terragrunt, Pulumi, AWS CDK, GKE/EKS/AKS.
- **GenAI, Agentic AI & LLMOps**: Claude API & Claude Code, OpenAI APIs, Model Context Protocol (MCP), Amazon Bedrock & GCP Vertex AI.
- **DevSecOps, SRE & FinOps**: Zero Trust architecture, Wiz CSPM, Workload Identity Federation (keyless WIF CI/CD), 25%–45% cloud cost reduction.

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
