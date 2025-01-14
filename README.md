# 🔬 Leukemia Classifier API

This repository contains a **FastAPI** application that provides an endpoint for classifying blood cells as either **healthy** or indicative of **acute lymphoblastic leukemia** (ALL).

## 🌟 Features

- Accepts image files of blood cells for classification.
- Configurable feature extraction model and classifier via `config.yaml`, pre-trained on the [Leukemia Classification Dataset](https://www.kaggle.com/datasets/andrewmvd/leukemia-classification).
- Preprocesses the image, extracts relevant features and scales them for optimal classification.
- Deployable with **Docker** for easy setup and containerization.
- A **request rate limiter** has been implemented to ensure the API fair access.
- A **file validation** mechanism has been implemented to ensure that the uploaded files are valid images, mitigating potential security risks by rejecting unwanted or malicious files.
- An **error handling middleware** logic has been implemented to ensure centralized error handling across all endpoints.

## ⚙️ Configuration

The `config.yaml` file allows you to specify the feature extraction model and its parameters, and the classifier. For example:

```yaml
feature_extractor:
  name: "resnet50"
  parameters:
    weights: "imagenet"
    include_top: false
    pooling: "avg"
classifier_filename: "svm.joblib"
```

<!--

## 📊 Dataset

The classifier was trained using
the [Leukemia Classification Dataset](https://www.kaggle.com/datasets/andrewmvd/leukemia-classification) available on
Kaggle.  
This dataset contains labeled images of blood cells, including both healthy samples and samples indicative of ALL.

## 🛠️ Classifier Pipeline

The SVM classifier was trained using the following pipeline:

1. **Image pre-processing, noise removal and segmentation**:
    - Applied a Gaussian filter with a kernel size of `(13, 13)` and a median filter with a kernel size of `(11, 11)`.
    - Performed binary thresholding and cropping to isolate the region of interest.

2. **Feature Extraction**:
    - Features were extracted using the model specified in the `config.yaml` file (e.g., `resnet50` with pre-trained
      weights on [ImageNet](https://www.image-net.org)).

3. **Feature Scaling**:
    - A **min-max scaling** approach was used to scale the features for each sample.

4. **Dimensionality Reduction**:
    - Used **Principal Component Analysis (PCA)** to reduce the feature set to the 100 most meaningful components.

5. **Stratified k-Fold Cross Validation**:
    - Used stratified k-fold cross-validation with `k = 5` to ensure robust performance evaluation.

### 📈 Performance Metrics

The classifier achieves the following performance on the test set (mean ± standard deviation across the folds):

- **Accuracy**: 0.870 ± 0.003
- **Precision**: 0.867 ± 0.003
- **Recall**: 0.967 ± 0.001
- **F1-Score**: 0.914 ± 0.002

-->

## 🚀 Usage

### 🐳 Running with Docker

You can use Docker to build and run the application. Run the docker daemon and then:

1. **Build the Docker Image**:
    ```bash
    docker build -t leukemia-classifier .
    ```

2. **Run the Docker Container**:
    ```bash
    docker run -d -p 80:80 leukemia-classifier
    ```

3. **Access the API**:
   The application will be running at `http://localhost:80`.

4. **Test the API**:
   Use a tool like **Postman**, **curl**, or the built-in Swagger UI (`http://localhost:80/docs`) to interact with the
   API. You can use images provided.

   #### Example Request:
   **Endpoint**: `POST /classify`  
   **Content-Type**: `multipart/form-data`  
   **Body**: Upload an image file of a blood cell.

   #### Example Response:
    ```json
    {
        "prediction": true
    }
    ```
    - `true`: Indicates acute lymphoblastic leukemia.
    - `false`: Indicates healthy cells.
