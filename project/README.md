# Financial Engineering Project
**Stage:** Problem Framing & Scoping (Stage 01)

## Problem Statement
<1–2 paragraphs: what problem & why it matters>

## Stakeholder & User
<Who decides? Who uses the output? Timing & workflow context>

## Useful Answer & Decision
<Descriptive / Predictive / Causal; metric; artifact to deliver>

## Assumptions & Constraints
<Bullets: data availability, capacity, latency, compliance, etc.>

## Known Unknowns / Risks
<Bullets: what’s uncertain; how you’ll test or monitor>

## Lifecycle Mapping
Goal → Stage → Deliverable
- <Goal A> → Problem Framing & Scoping (Stage 01) → <Deliverable X>

## Repo Plan
`data/`, `src/`, `notebooks/`, `docs/`, `reports/`, and `model/`; update the README whenever a lifecycle stage adds a new deliverable.

## Local Configuration

Project code uses `python-dotenv` to read settings from the repository-root
`.env` file. A safe template is provided at `../.env.example`.

For a new local checkout, run this command from the repository root:

```powershell
Copy-Item .env.example .env
```

Then edit `.env` if needed:

- `ALPHAVANTAGE_API_KEY` may contain a personal Alpha Vantage API key. Leaving
  it empty allows course examples to use their documented fallback.
- `DATA_DIR_RAW` and `DATA_DIR_PROCESSED` point to the project data folders.
- `DATA_DIR` points to the project-level data directory.

Never commit `.env`: it is intentionally ignored by Git. Update the root
`.env.example` whenever the project needs a new configuration variable, and
keep all example values free of real credentials.

## Folder Responsibilities

- `data/raw/` - immutable source data.
- `data/processed/` - outputs reproducible from raw data and code.
- `notebooks/` - project narratives, analysis, and experiments.
- `src/` - reusable functions and scripts.
- `docs/` - stakeholder context, assumptions, risks, and design notes.
- `reports/` - final charts, summaries, and delivery artifacts.
- `model/` - serialized model artifacts created in later stages.

The angle-bracket placeholders above remain intentionally unfilled until the project problem and stakeholder are chosen.
