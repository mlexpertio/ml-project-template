import json
from pathlib import Path

import pandas as pd
from loguru import logger

from prophet.config import Config
from prophet.text_classifier import TextClassifier


def evaluate(test_data_file: Path, model_file: Path, report_path: Path) -> float:
    df = pd.read_parquet(test_data_file)
    logger.debug(f"Evaluating model with {len(df)} samples")
    Config.Path.REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    classifier = TextClassifier.load(model_file)
    correct = 0
    for _, item in df.iterrows():
        prediction = classifier.predict(item.text)
        if prediction == item.label:
            correct += 1
    accuracy = correct / len(df)
    metrics = {"accuracy": accuracy}
    logger.debug(f"Model metrics: {metrics}")
    report_path.write_text(json.dumps(metrics))
