from keras.src.applications import ResNet50, ResNet101, VGG19

from src.implementations.neural_network_features_extractor import NeuralNetworkFeaturesExtractor
from src.interfaces.features_extractor import FeaturesExtractor


class FeaturesExtractorFactory:

    @staticmethod
    def get_extractor(model: dict) -> FeaturesExtractor:
        model_name = model['name']
        parameters = model['parameters']

        if model_name == "resnet50":
            extractor = ResNet50(**parameters)
            feature_size = 2048
        elif model_name == "resnet101":
            extractor = ResNet101(**parameters)
            feature_size = 2048
        elif model_name == "vgg19":
            extractor = VGG19(**parameters)
            feature_size = 512
        else:
            raise ValueError(f"Unsupported model: {model_name}")

        return NeuralNetworkFeaturesExtractor(extractor, feature_size)
