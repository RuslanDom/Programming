from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel, Field

# --- SQLAlchemy часть ---
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, nullable=False, unique=True)

# --- Pydantic часть ---
class UserSchema(BaseModel):
    username: str = Field(max_length=30)

# --- Настройка подключения (пример) ---
engine = create_engine('sqlite:///example.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# --- Пример использования ---
# Допустим, данные пришли извне (например, из JSON запроса)
raw_data = {"username": "ivan_petrov"}

# 1. Валидация через Pydantic
validated_data = UserSchema(**raw_data)

# 2. Преобразование в словарь (зависит от версии Pydantic)
# Pydantic v2:
data_dict = validated_data.model_dump()
# Pydantic v1:
# data_dict = validated_data.dict()

# 3. Создание объекта SQLAlchemy
new_user = User(**data_dict)

# 4. Добавление в сессию и сохранение
session.add(new_user)
session.commit()

print(f"Пользователь {new_user.username} добавлен с id {new_user.id}")