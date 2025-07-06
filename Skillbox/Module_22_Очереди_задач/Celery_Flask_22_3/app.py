import random
from flask import Flask, request, jsonify
from celery import Celery, group
import time
from rembg import remove

app = Flask(__name__)
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'

# КОНФИГУРАЦИЯ Celery
celery = Celery(
    app.name,
    broker=app.config['CELERY_BROKER_URL'],
    backend=app.config['CELERY_RESULT_BACKEND']
)

# ЗАДАЧИ Celery ДЛЯ ОБРАБОТКИ ИЗОБРАЖЕНИЙ
@celery.task
def process_image(image_id: str):
    try:
        output_img = f"{image_id.split(".")[0]}.png"
        with open(image_id, 'rb') as img:
            with open(output_img, 'wb') as f:
                input = img.read()
                time.sleep(1)
                output = remove(input)
                time.sleep(1)
                f.write(output)
    except Exception as e:
        print(f"Error: {e}")
