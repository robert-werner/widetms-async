FROM python:3.9.5-slim

ENV DB_NAME=rasterdb_test
ENV DB_USER=raster
ENV DB_PWD=7BWC9C63HXFeS79B
ENV DB_HOST=178.170.193.192
ENV DB_PORT=5432
ENV CELERY_BROKER_URL=amqps://pifetvkg:9groQdpQEjZf5I9U1I74akdGk9JQzKui@beaver.rmq.cloudamqp.com/pifetvkg
ENV CELERY_RESULT_URL=mongodb://widetms:JNmzd4YQFJMVxD38@widecluster.gr0kr.mongodb.net/widetms_db
ENV FRONTEND_PORT=8000

COPY . .
RUN pip install -r ./requirements.txt
ENTRYPOINT ["python", "main.py"]