FROM python:3.12-slim as base-project-template-python

WORKDIR /app

COPY requirements.txt .

RUN pip install -r ./requirements.txt

RUN pip install gunicorn

COPY . .

CMD gunicorn --bind 0.0.0.0:8080 app:app