from pathlib import Path

import pandas as pd
from loguru import logger

from prophet.config import Config
from prophet.text_classifier import TextClassifier


def train(data_dir: Path, save_dir: Path):
    logger.debug("Model training started...")
    Config.Path.MODELS_DIR.mkdir(parents=True, exist_ok=True)
    model = TextClassifier()
    train_df = pd.read_parquet(data_dir / Config.Dataset.TRAIN_FILE)
    test_df = pd.read_parquet(data_dir / Config.Dataset.TEST_FILE)
    model.fit(train_df, test_df)
    model.save(save_dir / Config.Model.FILE_NAME)
    logger.debug(f"Model training completed (saved at {save_dir / Config.Model.FILE_NAME})")
