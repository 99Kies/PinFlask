FROM python:3.7-alpine

COPY app /app

USER root

COPY _flag_xxxxxxx_.txt /_flag_xxxxxxx_.txt

COPY requirements.txt /requirements.txt

RUN pip install -r requirements.txt

COPY docker-entrypoint.sh /docker-entrypoint.sh

RUN chmod 777 /docker-entrypoint.sh

RUN adduser -D huctf

EXPOSE 5000

ENTRYPOINT ./docker-entrypoint.sh
