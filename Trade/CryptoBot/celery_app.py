import os

from celery import Celery
from dotenv import load_dotenv


class CeleryApp:
    load_dotenv()

    def __init__(self, broker=os.getenv('REDIS_URL'), backend=os.getenv('CELERY_RESULT_BACKEND')):
        self.app = Celery(
            main="main",
            broker=broker,
            backend=backend
        )

    def get_celery_app(self):
        return self.app



