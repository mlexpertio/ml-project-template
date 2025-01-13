# ML Project Template

Starter template for your Machine Learning/AI projects.

Features:

- [`dvc`](https://dvc.org/) for data versioning and pipeline management (reproducibility)
- [`FastAPI`](https://fastapi.tiangolo.com/) for serving the model
- [`uv`](https://docs.astral.sh/uv/) package manager
- [`ruff`](https://docs.astral.sh/ruff/) for linting and formatting
- [`pytest`](https://docs.pytest.org/en/stable/) for testing
- [`loguru`](https://loguru.readthedocs.io/en/stable/) for logging
- [`Docker`](https://www.docker.com/) for containerization


## Install

Make sure you have [`uv` installed](https://docs.astral.sh/uv/getting-started/installation/).

Clone the repository:

```bash
git clone git@github.com:mlexpertio/ml-project-template.git .
cd ml-project-template
```

Install Python:

```bash
uv python install 3.12.8
```

Create and activate a virtual environment:

```bash
uv venv
source .venv/bin/activate
```

Install dependencies:

```bash
uv sync
```

Install package in editable mode:

```bash
uv pip install -e .
```

Install pre-commit hooks:

```bash
uv run pre-commit install
```

## Reproduce

The project contains three different stages defined in `dvc.yaml`.

- Create a dataset from the raw data:

```bash
uv run dvc repro build-dataset
```

- Train a model using the dataset:

```bash
uv run dvc repro train-model
```

- Evaluate the model using the test dataset:

```bash
uv run dvc repro evaluate
```

## API server

Start the FastAPI server:

```bash
uv run python app.py
```

Test the API:

```bash
curl -X POST "http://localhost:8000/predict" \
     -H "Content-Type: application/json" \
     -d '{"text": "lets launch now"}'
```

## Tests

```bash
uv run pytest
```

## Docker

The template includes a `Dockerfile` to build a Docker image:

```bash
docker build -t prophet:latest .
```

Run the Docker container:

```bash
docker run -d -p 8000:8000 --name prophet prophet:latest
```