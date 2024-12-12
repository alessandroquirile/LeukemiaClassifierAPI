from src.classifiers.image_classifier import ImageClassifier


class ClassificationService:
    def __init__(self):
        self.classifier = ImageClassifier(model_path="svm.joblib", config_path="config.yaml")

    def classify(self, image) -> bool:
        return self.classifier.predict(image)
