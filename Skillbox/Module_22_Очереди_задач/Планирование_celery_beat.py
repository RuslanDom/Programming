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
    ИЗ ДИРЕКТОРИИ С ФАЙЛОМ ВЫПОЛНИТЬ:
    celery -app Планирование_celery_beat beat
    можно так
    celery -A Планирование_celery_beat worker -B
"""
@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(60, check_cat.s())
    sender.add_periodic.task(
        crontab(hour=8, minute=11, day_of_week=7),
        check_cat.s()
    )


@app.task
def check_cat():
    if random() < 0.5:
        print("Кот ничего не сломал")
    else:
        print("Кот что то сломал...")
