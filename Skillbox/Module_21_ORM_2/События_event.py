from sqlalchemy import event, Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return f"<User(name='{self.name}')>"

# Строка sqlite:///:memory: в контексте SQLite указывает на создание базы данных,
# которая существует только в оперативной памяти (RAM) и не сохраняется на диск.
# При закрытии соединения с такой базой данных, вся информация в ней теряется.

engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Подписка на событие before_insert выполняется до добавления записи в БД
@event.listens_for(User, 'before_insert')
def before_insert_user(mapper, connection, target):
    print(f"Перед вставкой пользователя: {mapper}\n{connection}\n{target}")

# Выполняется после вставки записи в БД
@event.listens_for(User, 'after_insert')
def receive_after_insert(mapper, connection, target):
    print("listen for the 'after_begin' event")

# Создание и сохранение объекта
user = User(name='John')
session.add(user)
session.commit()

# Вывод:
# Перед вставкой пользователя: Mapper[User(users)]
# <sqlalchemy.engine.base.Connection object at 0x7b6b4af8cf50>
# <User(name='John')>



