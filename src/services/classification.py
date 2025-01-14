import hashlib
from distutils.util import strtobool

from src.classifiers.image_classifier import ImageClassifier
from src.services.feature_extraction import FeatureExtractor
from src.utils.config import load_config
from src.utils.logging_config import logger
from src.utils.redis_client import redis_client


class ClassificationService:
    def __init__(self, config_path: str):
        config = load_config(config_path)
        classifier_filename = config["classifier_filename"]
        feature_extractor = FeatureExtractor(config["feature_extractor"])
        self.classifier = ImageClassifier(classifier_filename, feature_extractor)

    def classify(self, image) -> bool:
        image_hash = hashlib.sha256(image.tobytes()).hexdigest()
        # logger.info(f"Image hash: {image_hash}")

        cached_result = redis_client.get(image_hash)

        if cached_result:
            logger.info("Cache hit")
            return bool(strtobool(cached_result))  # https://stackoverflow.com/a/18472142/17082611

        logger.info("Cache miss. Performing prediction...")
        prediction = self.classifier.predict(image)

        redis_client.set(image_hash, str(prediction))
        logger.info(f"Result {prediction} saved in cache")
        return prediction
