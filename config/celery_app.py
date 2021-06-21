from celery import Celery
from config.environment import CELERY_RESULT_URL, CELERY_BROKER_URL

app = Celery('widetms.producer', broker=CELERY_BROKER_URL, backend=r"redis://172.17.0.1:6379")

app.conf.update(
    task_serializer='pickle',
    result_serializer='pickle',
    accept_content=['pickle']
)

app.conf.task_routes = {'widetms.worker.tile': {'queue': 'tiler'},
                        'widetms.builder.build': {'queue': 'builder'}}
