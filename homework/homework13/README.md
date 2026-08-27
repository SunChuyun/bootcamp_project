# Stage 13 Productization Homework

This API serves predictions from a two-feature synthetic linear regression. The model is trained in the submission notebook and loaded once when Flask starts.

## Start

From `homework/homework13/`, run:

```powershell
python app.py
```

## POST route

```python
import requests
requests.post("http://127.0.0.1:5002/predict", json={"features": [0.2, -0.1]}).json()
```

Example response: `{"prediction": -4.604...}`

## GET route

```python
requests.get("http://127.0.0.1:5002/predict/0.2/-0.1").json()
```

Example response: `{"prediction": -4.604...}`

Missing, nonnumeric, or incorrectly sized input returns JSON with an `error` field and HTTP status 400.
