import os
import random
import sys
from pathlib import Path

import numpy as np
from loguru import logger


class Config:
    SEED = 42

    class Path:
        APP_HOME = Path(os.getenv("APP_HOME", Path(__file__).parent.parent))
        ARTEFACTS_DIR = APP_HOME / "artefacts"
        DATA_DIR = ARTEFACTS_DIR / "data"
        MODELS_DIR = ARTEFACTS_DIR / "models"
        REPORTS_DIR = ARTEFACTS_DIR / "reports"

    class Dataset:
        TEST_SIZE = 0.2
        TRAIN_FILE = "train.parquet"
        TEST_FILE = "test.parquet"

    class Model:
        FILE_NAME = "model.json"

    class Evaluation:
        REPORT_FILE = "evaluation.json"


def seed_everything(seed: int = Config.SEED):
    random.seed(seed)
    np.random.seed(seed)


def configure_logging():
    config = {
        "handlers": [
            {
                "sink": sys.stdout,
                "colorize": True,
                "format": "<green>{time:YYYY-MM-DD - HH:mm:ss}</green> | <level>{level}</level> | {message}",
            },
        ]
    }
    logger.configure(**config)
