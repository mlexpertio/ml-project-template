from prophet.data import Label
from prophet.text_classifier import TextClassifier


def test_untrained_classifier_should_predict_stop():
    classifier = TextClassifier()
    assert classifier.predict("What do you think?") == Label.STOP
