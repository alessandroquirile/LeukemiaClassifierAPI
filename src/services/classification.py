from src.classifiers.image_classifier import ImageClassifier
from src.services.feature_extraction import FeatureExtractor
from src.utils.config import load_config


class ClassificationService:
    def __init__(self, config_path: str):
        config = load_config(config_path)
        classifier_filename = config["classifier_filename"]
        feature_extractor = FeatureExtractor(config["feature_extractor"])
        self.classifier = ImageClassifier(classifier_filename, feature_extractor)

    def classify(self, image) -> bool:
        return self.classifier.predict(image)
