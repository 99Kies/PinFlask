FROM python:3.7-alpine

COPY app /app

USER root

COPY requirements.txt /requirements.txt

RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

COPY docker-entrypoint.sh /docker-entrypoint.sh

RUN chmod 777 /docker-entrypoint.sh

EXPOSE 5000

ENTRYPOINT ./docker-entrypoint.sh
