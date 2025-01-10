import joblib
import numpy as np
from PIL import Image

from src.preprocessing.images import crop_image_
from src.services.feature_extraction import FeatureExtractor


def preprocess_data(image: Image.Image) -> np.array:
    image = np.array(image)
    image = crop_image_(image)
    return image


class ImageClassifier:
    def __init__(self, classifier_filename: str, feature_extractor: FeatureExtractor):
        self.classifier = joblib.load(classifier_filename)
        self.extractor = feature_extractor

    def predict(self, image: Image.Image) -> bool:
        image_array = preprocess_data(image)
        features = self.extractor.extract_features(image_array)

        # The predict method allows it to handle both single and batch predictions uniformly.
        # However, when dealing with single predictions (just one input sample),
        # you need to explicitly extract the first value using [0]
        prediction = self.classifier.predict(features)
        return prediction[0]
