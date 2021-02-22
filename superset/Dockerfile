FROM ubuntu:20.04
RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get install -y build-essential libssl-dev libffi-dev python3-dev python3-pip libsasl2-dev libldap2-dev libpq-dev
RUN pip3 install --upgrade setuptools pip
RUN pip3 install psycopg2-binary apache-superset
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

