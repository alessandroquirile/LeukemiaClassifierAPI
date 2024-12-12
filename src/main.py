import io

import joblib
import numpy as np
import yaml
from PIL import Image
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse

from src.factories.feature_extractor_factory import FeaturesExtractorFactory
from src.interfaces.features_extractor import FeaturesExtractor
from src.preprocessing.data_utils import scale_per_sample
from src.preprocessing.images import crop_image_


def load_config(config_path):
    with open(config_path, "r") as file:
        return yaml.safe_load(file)


def preprocess_data(image):
    image = np.array(image)
    image = crop_image_(image)
    return image


def extract_features(image: np.array, extractor: FeaturesExtractor):
    features = extractor.extract(image)
    features = features.reshape(1, -1)  # (1, n_features)
    features = scale_per_sample(features)
    return features


app = FastAPI()

classifier = joblib.load("svm.joblib")

config = load_config("config.yaml")
model = config["feature_extraction_model"]
extractor = FeaturesExtractorFactory.get_extractor(model)


@app.post("/classify")
async def classify_image(file: UploadFile = File(...)):
    image = await file.read()
    image = Image.open(io.BytesIO(image))

    image_array = preprocess_data(image)
    features = extract_features(image_array, extractor)

    # The predict method allows it to handle both single and batch predictions uniformly.
    # However, when dealing with single predictions (just one input sample),
    # you need to explicitly extract the first value using [0].
    prediction = classifier.predict(features)
    prediction = bool(prediction[0])  # Convert numpy.bool_ to native Python bool
    return JSONResponse({"prediction": prediction})
