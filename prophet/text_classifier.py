import json
from pathlib import Path
from typing import Set

import pandas as pd

from prophet.data import Label


class TextClassifier:
    def __init__(self, positive_words: Set[str] = set(), negative_words: Set[str] = set()):
        self.positive_words = positive_words
        self.negative_words = negative_words

    def fit(self, train_data: pd.DataFrame, test_data: pd.DataFrame):
        self.positive_words = set()
        self.negative_words = set()

        for _, item in train_data.iterrows():
            words = item.text.lower().split()
            if item.label == Label.JUST_DO_IT:
                self.positive_words.update(words)
            else:
                self.negative_words.update(words)

        # Remove words that appear in both categories as they're not discriminative
        common_words = self.positive_words.intersection(self.negative_words)
        self.positive_words -= common_words
        self.negative_words -= common_words

    def predict(self, text) -> Label:
        words = set(text.lower().split())

        positive_matches = len(words.intersection(self.positive_words))
        negative_matches = len(words.intersection(self.negative_words))

        return Label.JUST_DO_IT if positive_matches > negative_matches else Label.STOP

    def save(self, filepath: Path):
        data = {
            "positive_words": list(self.positive_words),
            "negative_words": list(self.negative_words),
        }
        filepath.write_text(json.dumps(data))

    @staticmethod
    def load(filepath: Path) -> "TextClassifier":
        data = json.loads(filepath.read_text())
        return TextClassifier(set(data["positive_words"]), set(data["negative_words"]))
