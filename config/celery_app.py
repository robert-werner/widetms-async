from celery import Celery
from config.environment import CELERY_RESULT_URL, CELERY_BROKER_URL

app = Celery('widetms.producer', broker=CELERY_BROKER_URL, backend=CELERY_RESULT_URL)

app.config_from_object('config.celeryconfig')

app.conf.task_routes = {'widetms.worker.tile': {'queue': 'tiler'},
                        'widetms.builder.build': {'queue': 'builder'}}
