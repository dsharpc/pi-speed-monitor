FROM python:3.8-alpine

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY speed_monitor /speed_monitor

WORKDIR /speed_monitor

# CRON to run periodically
RUN mkdir /logs
COPY crontab /etc/crontabs/root
RUN chmod 0644 /etc/crontabs/root
ENV PYTHONUNBUFFERED 1
CMD crond -f
