# Bootcamp Repository

This repository separates instructor-provided materials, submitted homework, and the ongoing financial engineering project.

## Folder Structure

- `class_materials/` - original course files grouped by stage. Keep these files unchanged and local only.
- `homework/` - submitted work, with one folder per assignment (`homework0`, `homework1`, and so on).
- `project/` - the persistent project that grows across lifecycle stages.

## Homework Folder Rules

1. Copy any starter file from `class_materials/` into the matching `homework/homeworkN/` folder.
2. Edit only the homework copy.
3. Include every file required for grading and commit the completed folder.

## Class Materials Rules

1. Store each stage in its own folder, such as `class_materials/stage03_python-fundamentals/`.
2. Keep the reading, lecture notebook, homework sheet, project instructions, and supporting data together.
3. Run lecture notebooks from their stage folder so relative data paths resolve correctly.
4. Never commit `class_materials/`; the root `.gitignore` excludes it.

## Project Folder Rules

- `project/data/raw/` stores immutable source data.
- `project/data/processed/` stores reproducible derived data.
- `project/notebooks/` contains project analysis and experiments.
- `project/src/` contains reusable Python code.
- `project/docs/` contains framing, assumptions, risks, and design notes.
- `project/reports/` contains stakeholder-facing outputs.
- `project/model/` contains model artifacts created in later stages.

## Environment

Create or update the course environment from the repository root:

```powershell
conda env create -f environment.yml
conda activate bootcamp_env
```

Local configuration belongs in `.env`; the safe template is `.env.example`. Never commit the real `.env` file.

## GitHub

Course repository: <https://github.com/SunChuyun/bootcamp_project>
