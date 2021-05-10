FROM python:3

ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y postgresql-client

COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

WORKDIR /app
