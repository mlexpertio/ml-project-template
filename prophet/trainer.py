from pathlib import Path

from loguru import logger

from prophet.config import Config
from prophet.text_classifier import TextClassifier


def train(train_file: Path, save_dir: Path):
    logger.debug("Model training started...")
    Config.Path.MODELS_DIR.mkdir(parents=True, exist_ok=True)
    model = TextClassifier()
    model.fit(train_file)
    model.save(save_dir / Config.Model.FILE_NAME)
    logger.debug(f"Model training completed (saved at {save_dir / Config.Model.FILE_NAME})")
