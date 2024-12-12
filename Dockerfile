FROM python:3.11-slim

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
COPY ./svm.joblib /app/svm.joblib
COPY ./config.yaml /app/config.yaml

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Solves import error and cleanup apt cache to reduce image size
# https://stackoverflow.com/a/63377623/17082611
RUN apt-get update && apt-get install --no-install-recommends -y ffmpeg libsm6 libxext6
RUN rm -rf /var/lib/apt/lists/*

COPY ./src /app/src

# Configure PYTHONPATH to include the /app/src directory
ENV PYTHONPATH="/app/src"

CMD ["uvicorn", "src.main:app", "--port", "80", "--host", "0.0.0.0"]