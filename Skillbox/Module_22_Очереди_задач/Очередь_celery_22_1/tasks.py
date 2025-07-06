# 1) Установка redis

# Чтобы загрузить образ, выполните команду
#       CMD: docker pull redis
# Чтобы запустить новый контейнер Redis, выполните команду
#       CMD: docker run -p 6379:6379 --name my_redis -d redis
#       ,если есть такой контейнер то используем docker start my_redis
# Эта команда запускает новый контейнер Redis в фоновом режиме и назначает ему имя my-redis.
# Флаг -d указывает Docker запустить контейнер в фоновом режиме. Флаг -p прокидывает порт 6379 из контейнера на порт 6379 локальной машины.
# Чтобы проверить, что контейнер Redis запущен и работает правильно, мы можем выполнить команду docker ps,
# которая показывает список запущенных контейнеров на машине.
#       CMD: docker ps

# 2) Установка Celery:
#       pip install celery
# Для запуска рабочих процессов Celery, которые будут обрабатывать задачи, выполните команду
#       python_terminal: ~/PycharmProjects/Programming/Skillbox/Module_22_Очереди_задач/Очередь_celery_22_1$ celery --app tasks worker
# Теперь очередь задач готова к работе. Вы можете добавлять задачи и выполнять их


from celery import Celery

app = Celery(
    "tasks",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0",
)
@app.task
def add(x, y):
    return x + y

@app.task
def hello():
    return 'hello world'

# tasks — название нашего Celery-приложения.
# broker — URL брокера сообщений.
# backend — URL хранилища результатов; можно указать URL брокера.

