FROM python:3.11

# Imposta la cartella di lavoro
WORKDIR /app

# Copia dei file di requirements e delle risorse
COPY ./requirements.txt /app/requirements.txt
COPY ./svm.joblib /app/svm.joblib
COPY ./config.yaml /app/config.yaml

# Installa le dipendenze
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Evita import error su open cv
# https://stackoverflow.com/a/63377623/17082611
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6 -y

# Copia il codice sorgente nella directory /app/src
COPY ./src /app/src

# Configura PYTHONPATH per includere la directory /app/src
# nei percorsi di ricerca dei moduli Python. Questo garantisce
# che i moduli del progetto possano essere importati correttamente
ENV PYTHONPATH="/app/src"

# Avvia l'app
CMD ["uvicorn", "src.main:app", "--port", "80", "--host", "0.0.0.0"]
