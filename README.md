# ML Project Template

Starter template for your Machine Learning/AI projects.

## Install

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

## Reproduce

The project contains three different stages defined in `dvc.yaml`.

- `dataset`: Creates a dataset from the raw data:

```bash
uv run dvc repro dataset
```

- `train`: Trains a model using the dataset:

```bash
uv run dvc repro train
```

- `eval`: Evaluates the model using the test dataset:

```bash
uv run dvc repro eval
```

## API server

Start the FastAPI server:

```bash
uv run python app.py
```

## Tests

```bash
uv run pytest
```