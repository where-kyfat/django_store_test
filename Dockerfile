FROM python:3.11.3-slim-buster

RUN mkdir -p /app
WORKDIR /app

COPY ./requirements.txt .
RUN pip install -r requirements.txt