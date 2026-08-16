
# Project Title
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
data/, src/, notebooks/, docs/ ; cadence for updates

## Local Configuration

The lecture notebooks use `python-dotenv` to read project-specific settings from
the root-level `.env` file. A safe template is provided in `.env.example`.

For a new local checkout, create the working configuration in PowerShell:

```powershell
Copy-Item .env.example .env
```

Then edit `.env` if needed:

- `ALPHAVANTAGE_API_KEY` may contain a personal Alpha Vantage API key. Leaving
  it empty makes the Stage 04 notebook use its `yfinance` fallback.
- `DATA_DIR_RAW` and `DATA_DIR_PROCESSED` control the Stage 05 data folders.
- `DATA_DIR` is the path value used by the Stage 02 configuration
  demonstration.

Never commit `.env`: it is intentionally ignored by Git. Commit
`.env.example` whenever the project needs a new configuration variable, but
keep all example values free of real credentials.
