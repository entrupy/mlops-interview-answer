# Minimal MLOps FastAPI Project

This is a minimal, production-ready template for a text classification API using FastAPI, scikit-learn, Poetry, and Docker.

## Features

- Minimal Python code (see `src/ml_interview_project/`)
- Model is auto-trained and saved if missing (no manual step needed)
- One endpoint: `/predict` (POST)
- Simple, robust Dockerfile
- Minimal GitHub Actions CI: tests both with and without Docker

## Quickstart

### 1. Install dependencies

```bash
pip install poetry
poetry install
```

### 2. Run locally

```bash
poetry run uvicorn ml_interview_project.main:app --reload --app-dir src
```

### 3. Try the API

```bash
curl -X POST http://localhost:8000/predict -H "Content-Type: application/json" -d '{"text": "hello world"}'
```

### 4. Run tests

```bash
poetry run pytest
```

### 5. Build and run with Docker

```bash
docker build . -t ml-interview-app
# Run the container
docker run -p 8000:8000 ml-interview-app
```

### 6. Test the API in Docker

After running the container, open a new terminal and run:

```bash
curl -X POST http://localhost:8000/predict -H "Content-Type: application/json" -d '{"text": "hello world"}'
```

You should see a response like:

```json
{"prediction": "positive"}
```

## How model training works

- If the model file (`model/text_classifier.joblib`) does not exist, it is trained and saved automatically at runtime.
- No manual training step is needed.

## CI/CD: How it works

- The workflow is defined in `.github/workflows/ci.yml`.
- **When is it triggered?**
  - On every pull request to the `main` branch.
- **What does it do?**
  1. Checks out the code and sets up Python.
  2. Installs dependencies with Poetry and runs all tests (`pytest`).
  3. Builds the Docker image.
  4. Runs the Docker container, waits for it to start, and tests the `/predict` endpoint with `curl`.
  5. Cleans up the container.
- **What to expect:**
  - If any test fails or the Docker image does not build or run correctly, the workflow will fail and you will see errors in the GitHub Actions tab.
  - If everything passes, you will see a green checkmark for your PR.

---
