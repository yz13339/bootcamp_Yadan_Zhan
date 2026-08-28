# Homework 13: Productization

This API serves a two-feature linear regression trained on reproducible synthetic data. The model is loaded once when `app.py` starts and reused for every request.

Start it from this directory:

```bash
python app.py
```

POST route:

```bash
curl -X POST http://127.0.0.1:5050/predict -H 'Content-Type: application/json' -d '{"features":[0.25,-0.4]}'
# {"prediction":-7.698750717752957}
```

GET route:

```bash
curl http://127.0.0.1:5050/predict/0.25/-0.4
# {"prediction":-7.698750717752957}
```

Missing `features`, the wrong number of features, or nonnumeric values return JSON containing `error` with HTTP status 400 rather than a traceback.
