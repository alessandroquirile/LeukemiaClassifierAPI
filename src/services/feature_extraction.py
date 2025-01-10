import numpy as np

from src.factories.feature_extractor_factory import FeaturesExtractorFactory
from src.preprocessing.data_utils import scale_per_sample


class FeatureExtractor:
    def __init__(self, extractor):
        self.extractor = FeaturesExtractorFactory.get_extractor(extractor)

    def extract_features(self, image: np.array) -> np.array:
        features = self.extractor.extract(image)
        features = features.reshape(1, -1)  # (1, n_features)
        features = scale_per_sample(features)
        return features
