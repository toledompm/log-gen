FROM python:alpine

WORKDIR /app

COPY log-gen.py /app/log-gen.py

ENTRYPOINT ["python", "log-gen.py"]
