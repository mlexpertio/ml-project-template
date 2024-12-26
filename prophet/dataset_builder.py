from pathlib import Path

import pandas as pd
from loguru import logger

from prophet.config import Config
from prophet.data import EXAMPLES


def build_dataset(save_dir: Path) -> pd.DataFrame:
    logger.debug(f"Building dataset at {save_dir}")
    Config.Path.DATA_DIR.mkdir(parents=True, exist_ok=True)
    rows = [{"text": r["text"], "label": r["label"].value} for r in EXAMPLES]
    df = pd.DataFrame(rows)
    df_train = df.sample(frac=1.0 - Config.Dataset.TEST_SIZE)
    df_test = df.drop(df_train.index)
    df_train.to_parquet(save_dir / Config.Dataset.TRAIN_FILE)
    df_test.to_parquet(save_dir / Config.Dataset.TEST_FILE)
    return df
