# Deployment Handoff Plan

- Create `bootcamp_env`, then install `project/requirements.txt`.
- Run `notebooks/project_pipeline.ipynb` top to bottom to rebuild data, model, and reports.
- Confirm the final artifact check is fully `True` before starting the API.
- Start the service with `python app.py` from `project/` and verify `GET /health`.
- Use the request example in `README.md` to test `POST /predict`.
- Send data, model, system, and business alerts to the owners named in `docs/monitoring_plan.md`.
- For a failed batch, inspect `reports/pipeline.log`, retry once, and record the incident.
- For a bad release, stop the service, restore the last tagged commit, rebuild the model, and repeat the health check.
- Keep assumptions, incident evidence, and approval decisions in repository issues.
