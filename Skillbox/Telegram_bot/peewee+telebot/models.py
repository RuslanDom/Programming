from peewee import (
    AutoField,
    BooleanField,
    CharField,
    DateField,
    ForeignKeyField,
    IntegerField,
    Model,
    SqliteDatabase,
)


from config import DATE_FORMAT, DB_PATH
db = SqliteDatabase(DB_PATH)


# Опишем модели, которые нам понадобятся. Сначала создадим базовый класс BaseModel:
class BaseModel(Model):
    class Meta:
        database = db


# Создадим модель пользователя:
class User(BaseModel):
    user_id = IntegerField(primary_key=True)
    username = CharField(null=True)
    firstname = CharField(null=True)
    lastname = CharField(null=True)


# user_id — первичный ключ модели, будет совпадать с Telegram ID. Это значит, что он будет уникальным для всей таблицы.
# username — никнейм в Telegram.
# first_name — имя в Telegram.
# last_name — фамилия в Telegram. Может быть не указана, поэтому ставим null=True.


# Создадим модель задачи:
class Task(BaseModel):
    task_id = AutoField()
    user = ForeignKeyField(User, backref='tasks')
    title = CharField
    due_data = DateField()
    is_done = BooleanField(default=False)

    def __str__(self):
        return '{task_id}. {check}{title} - {due_data}'.format(
            task_id=self.task_id,
            check="[V]" if self.is_done else '[ ]',
            title=self.title,
            due_data=self.due_data.strftime(DATE_FORMAT)
            # due_data=self.due_data.adapt(DATE_FORMAT)
        )

# task_id — ID задачи. AutoField показывает, что это первичный ключ,
# а значение будет автоматически увеличиваться на единицу. Аналог PRIMARY KEY AUTOINCREMENT.

# user — внешний ключ, ссылающийся на пользователя; backref создаёт обратную ссылку:
# мы сможем получить задачи пользователя с помощью user.tasks.

# title — название задачи.
# due_date — назначенная дата выполнения задачи.
# is_done — указание, выполнена ли задача.


def create_models():
    db.create_tables(BaseModel.__subclasses__())
