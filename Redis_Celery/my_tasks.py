from celery import Celery
from fastapi import FastAPI

app = Celery('my_tasks', broker='redis://localhost:6379', backend='redis://localhost:6379')

@app.task
def add(x, y):
    return x + y



