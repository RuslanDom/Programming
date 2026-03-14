from random import random
from celery import Celery
from celery.schedules import crontab

app = Celery(
    main="Планирование_celery_beat",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)
"""
Запустить Redis
    CMD: docker start my_redis
Запустить Celery
    ИЗ ДИРЕКТОРИИ С ФАЙЛОМ ВЫПОЛНИТЬ №1 и №2 --pool=solo (работает в Windows):
    №1: celery -A Планирование_celery_beat worker --pool=solo
    №2: celery --app Планирование_celery_beat beat
    можно так
    celery -A Планирование_celery_beat worker -B
"""
@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(5.0, check_cat.s())
    sender.add_periodic.task(
        crontab(hour=0, minute=0, day_of_week=4),
        check_cat.s()
    )


@app.task
def check_cat():
    if random() < 0.5:
        print("Кот ничего не сломал")
    else:
        print("Кот что то сломал...")
