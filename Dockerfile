FROM python:3.11

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
COPY ./svm.joblib /app/svm.joblib
COPY ./config.yaml /app/config.yaml

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Solves import error for open cv
# https://stackoverflow.com/a/63377623/17082611
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6 -y

COPY ./src /app/src

# Configure PYTHONPATH to include the /app/src directory
# in Python's module search paths. This ensures that the project's
# modules can be imported correctly.
ENV PYTHONPATH="/app/src"

CMD ["uvicorn", "src.main:app", "--port", "80", "--host", "0.0.0.0"]
