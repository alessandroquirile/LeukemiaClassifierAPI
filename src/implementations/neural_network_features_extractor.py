import cv2 as cv
import numpy as np
from keras.applications.resnet import preprocess_input

from src.interfaces.features_extractor import FeaturesExtractor


class NeuralNetworkFeaturesExtractor(FeaturesExtractor):
    def __init__(self, model, features):
        self._model = model
        self.features = features

    def extract(self, image) -> np.ndarray:
        size = (224, 224)
        resized_image = cv.resize(image, size)
        reshaped_image = resized_image.reshape(-1, *size, 3)
        reshaped_image = preprocess_input(reshaped_image)
        features = self._model(reshaped_image, training=False)
        features = features.numpy().reshape(self.features, )
        return features
