from abc import abstractmethod


class FeaturesExtractor:

    @abstractmethod
    def extract(self, image):
        pass
