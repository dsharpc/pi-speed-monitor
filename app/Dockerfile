FROM arm32v6/python:3.8-alpine

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY speed_monitor /speed_monitor

WORKDIR /speed_monitor