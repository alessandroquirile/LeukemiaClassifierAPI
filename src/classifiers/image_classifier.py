import joblib
import numpy as np
import yaml
from PIL import Image

from src.factories.feature_extractor_factory import FeaturesExtractorFactory
from src.preprocessing.data_utils import scale_per_sample
from src.preprocessing.images import crop_image_


def load_config(config_path):
    with open(config_path, "r") as file:
        return yaml.safe_load(file)


def preprocess_data(image: Image.Image) -> np.array:
    image = np.array(image)
    image = crop_image_(image)
    return image


class ImageClassifier:
    def __init__(self, model_path: str, config_path: str):
        self.classifier = joblib.load(model_path)
        self.config = load_config(config_path)
        self.extractor = FeaturesExtractorFactory.get_extractor(self.config["feature_extraction_model"])

    def predict(self, image: Image.Image) -> bool:
        image_array = preprocess_data(image)
        features = self.extract_features(image_array)

        # The predict method allows it to handle both single and batch predictions uniformly.
        # However, when dealing with single predictions (just one input sample),
        # you need to explicitly extract the first value using [0]
        prediction = self.classifier.predict(features)
        return bool(prediction[0])  # Convert numpy.bool_ to native Python bool

    def extract_features(self, image: np.array) -> np.array:
        features = self.extractor.extract(image)
        features = features.reshape(1, -1)  # (1, n_features)
        features = scale_per_sample(features)
        return features
