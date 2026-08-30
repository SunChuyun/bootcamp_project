# Homework 2: Tooling Setup

This folder provides a reproducible Python setup for the bootcamp assignments. It keeps configuration in a local `.env` file, centralizes access in `src/config.py`, and verifies the environment with a Jupyter notebook.

## Folder Structure

- `data/raw/` - original local inputs.
- `data/processed/` - cleaned or transformed outputs.
- `docs/` - supporting notes.
- `model/` - saved model artifacts.
- `notebooks/` - optional working notebooks.
- `reports/images/` - generated report figures.
- `src/` - reusable configuration code.
- `homework02_tooling-setup_submission.ipynb` - graded setup check.
- `.env.example` - safe configuration template.
- `requirements.txt` - frozen package versions from `bootcamp_env`.

Empty scaffold folders contain `.gitkeep` files so the complete required structure remains visible in Git.

## Run

```powershell
conda activate bootcamp_env
cd homework/homework02
jupyter lab
```

Open `homework02_tooling-setup_submission.ipynb` and run all cells. The notebook checks the Python environment and configuration without displaying the secret value.

The real `.env` file is local and excluded by the repository `.gitignore`.
