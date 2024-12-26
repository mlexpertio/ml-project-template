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

```bash
uv run dvc repro build-dataset
```

## Tests

```bash
uv run pytest
```