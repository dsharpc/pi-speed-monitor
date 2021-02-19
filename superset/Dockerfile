FROM python:3.8-slim
RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get install -y build-essential libssl-dev libffi-dev python-dev python-pip libsasl2-dev libldap2-dev
RUN pip install --upgrade setuptools pip
RUN pip install psycopg2-binary apache-superset
RUN superset db upgrade
ENV FLASK_APP=superset
RUN superset fab create-admin \
    --username admin \
    --firstname admin \
    --lastname admin \
    --email admin@admin.com \
    --password admin
RUN superset init
COPY dashboards /dashboards
ARG DB_STRING
RUN superset set-database-uri -d speed_test -u $DB_STRING
RUN superset import-dashboards -p /dashboards
CMD superset run -h 0.0.0.0 -p 8088 --with-threads --reload --debugger

