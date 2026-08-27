# Homework 2: Tooling Setup

This folder provides a reproducible Python setup for the bootcamp assignments. It keeps configuration in a local `.env` file, centralizes access in `src/config.py`, and verifies the environment with a Jupyter notebook.

## Folder Structure

- `data/` - local assignment data.
- `notebooks/` - environment and configuration checks.
- `src/` - reusable configuration code.
- `.env.example` - safe configuration template.
- `requirements.txt` - frozen package versions from `bootcamp_env`.

## Run

```powershell
conda activate bootcamp_env
cd homework/homework2
jupyter lab
```

Open `notebooks/00_project_setup.ipynb` and run all cells. The notebook should print `API_KEY present: True`.

The real `.env` file is local and excluded by the repository `.gitignore`.
