from celery import Celery

app = Celery(
    "tasks",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)

@app.task
def buy_milk(value: int):
    return f"Купил {value} литр(ов) молока"

@app.task
def buy_bread(count: int):
    return f"Купил {count} булку(ок) хлеба"

@app.task
def fetch_name(id: str):
    return f"Пётр {id}Первый"

@app.task
def greeting_user(name: str):
    return f"Здравствуй, {name}!"
