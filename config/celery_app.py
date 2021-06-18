from celery import Celery
from config.environment import CELERY_RESULT_URL, CELERY_BROKER_URL

app = Celery(broker=CELERY_BROKER_URL, backend=CELERY_RESULT_URL)