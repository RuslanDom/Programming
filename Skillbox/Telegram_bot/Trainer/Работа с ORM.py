# import peewee
# print(peewee.__version__)

from peewee import Model, CharField, IntegerField, SqliteDatabase

# подключаемся к базе данных my_database.db
db = SqliteDatabase('my_database.db')


# создаём модель User
class User(Model):
    # имя пользователя, CharField -- строка
    name = CharField()
    # возраст пользователя, IntegerField -- целое число
    age = IntegerField()

    # во внутреннем классе Meta указываем нашу базу данных
    class Meta:
        database = db


class Friends(Model):
    name = CharField()
    age = IntegerField()
    surname = CharField()
    job = CharField()

    class Meta:
        database = db


# создаём таблицу users в базе данных
db.create_tables([User])
db.create_tables([Friends])

# Добавим пользователей в базу данных:
# user1 = User(name='Руслан', age=34)
# user1.save()
# user2 = User(name='Кристина', age=34)
# user2.save()
# user3 = User(name='Злата', age=14)
# user3.save()
#
# friend1 = Friends(name='Anton', surname='Hariyanov', age=34, job='Woodmaker')
# friend1.save()
# friend2 = Friends(name='Yriy', surname='Afanasiev', age=36, job='Police detective')
# friend2.save()

# Выведем данные БД
users = User.select()

for user in users:
    print(f"Имя: {user.name}... Возраст: {user.age};")
    # Имя: Руслан... Возраст: 34;
    # Имя: Кристина... Возраст: 34;
    # Имя: Злата... Возраст: 14;

# Для получения объекта из базы используется метод .get с перечислением критериев поиска:
retrieved_user = User.get(User.name == "Руслан")
print(retrieved_user, retrieved_user.name, retrieved_user.age)  # 1 Руслан 34

# Изменить модель так же просто, как и создать её:
# retrieved_user.name = "Рус"
# retrieved_user.save()

# Удалить модель можно с помощью метода .delete_instance:
# user1.delete_instance()

