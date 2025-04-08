import sqlite3
from dataclasses import dataclass
from typing import List

ENABLE_FOREIGN_KEY = "PRAGMA foreign_keys = ON;"
DATABASE = "M_18_pets.db"
TABLE_OWNER = "owner"
TABLE_PETS = "pets"
DATA = [
    {"name": "Тузик", "kind": "собака", "age": 3, "owner": "Сергей"},
    {"name": "Чайник", "kind": "кот", "age": 1, "owner": "Егор"},
    {"name": "Сачок", "kind": "собака", "age": 2, "owner": "Виктор"}
]

@dataclass
class Owner:
    id: int = None
    name: str = None

    def __getitem__(self, item):
        return getattr(self, item)

@dataclass
class Pet:
    id: int = None
    name: str = None
    kind: str = None
    age: int = None
    owner: str = None

    def __getitem__(self,item):
        return getattr(self, item)


def init_table_owner(initial_data: list):
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute(
            f"""
            SELECT name FROM sqlite_master WHERE type='table' AND name='{TABLE_OWNER}';
            """
        )
        exists = cursor.fetchone()
        if not exists:
            cursor.execute(
                f"""
                CREATE TABLE '{TABLE_OWNER}' (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(50) NOT NULL
                )
                """
            )
            conn.commit()
            for item in initial_data:
                cursor.execute(
                    f"""
                    SELECT * FROM '{TABLE_OWNER}'
                    WHERE name='{item["owner"]}';
                    """
                )
                exist = cursor.fetchone()
                if exist:
                    continue
                cursor.execute(
                    f"""
                                    INSERT INTO '{TABLE_OWNER}' (name) 
                                    VALUES (?)
                                    """,
                    (item["owner"],)
                )
                conn.commit()


def init_table_pet(initial_data: list):
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute(
            f"""
            SELECT name FROM sqlite_master WHERE type='table' AND name='{TABLE_PETS}';
            """
        )
        exists = cursor.fetchone()
        if not exists:
            cursor.execute(
                f"""
                CREATE TABLE '{TABLE_PETS}' (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(50) NOT NULL,
                kind VARCHAR(50),
                age INTEGER,
                owner VARCHAR(50) NOT NULL,
                FOREIGN KEY(owner) REFERENCES '{TABLE_OWNER}'(name) ON DELETE CASCADE
                )
                """
            )
            for item in initial_data:
                cursor.execute(
                    f"""
                    SELECT * FROM '{TABLE_PETS}'
                    WHERE name='{item["name"]}' and owner='{item["owner"]}';
                    """
                )
                exist = cursor.fetchone()
                if exist:
                    continue
                cursor.execute(
                    f"""
                    INSERT INTO '{TABLE_PETS}' (name, kind, age, owner) 
                    VALUES (?, ?, ?, ?)
                    """,
                    (item["name"], item["kind"], item["age"], item["owner"])
                )
                conn.commit()

# POST
# Добавляем владельца (owner)
def add_owner(data: Owner) -> Owner:
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute(
            f"""
            SELECT * FROM '{TABLE_OWNER}'
            WHERE name = '{data.name}'
            """
        )
        exist = cursor.fetchone()
        if exist:
            return None
        cursor.execute(
            f"""
            INSERT INTO '{TABLE_OWNER}' (name) VALUES (?)
            """,
            (data.name, )
        )
        conn.commit()
    return get_owner_obj(cursor.lastrowid)

# Добавляем животное (pet)
def add_pet(data: Pet) -> Pet:
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute(
            f"""
            SELECT * FROM '{TABLE_OWNER}'
            WHERE name = '{data.owner}'
            """
        )
        exist = cursor.fetchone()
        if exist is None:
            add_owner(Owner(name=data.owner))
        cursor.execute(
            f"""
            INSERT INTO '{TABLE_PETS}' (name, kind, age, owner) 
            VALUES (?, ?, ?, ?)
            """,
        (data.name, data.kind, data.age, data.owner))
        conn.commit()
        return get_pet_obj(cursor.lastrowid)


def get_owner_obj(owner_id) -> Owner:
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute(
            f"""
            SELECT * FROM '{TABLE_OWNER}'
            WHERE id = {owner_id} """
        )
        owner = cursor.fetchone()
    return Owner(id=owner[0], name=owner[1])

def get_pet_obj(pet_id) -> Pet:
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute(
            f"""
            SELECT * FROM '{TABLE_PETS}'
            WHERE id = {pet_id}
            """
        )
        pet = cursor.fetchone()
    return Pet(id=pet[0], name=pet[1], kind=pet[2], age=pet[3], owner=pet[4])


# GET
# Получаем всех pets
def get_all_pets() -> List[Pet]:
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute(
            f"""
            SELECT * FROM '{TABLE_PETS}'
            """
        )
        all_pets = cursor.fetchall()
    return [get_pet_obj(pet[0]) for pet in all_pets]

# Получаем всех owners
def get_all_owners() -> List[Owner]:
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute(
            f"""
            SELECT * FROM '{TABLE_OWNER}'
            """
        )
        all_owners = cursor.fetchall()
    return [get_owner_obj(owner[0]) for owner in all_owners]


# DELETE
# Удаляем животное
def delete_pet(pet_id: int):
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        exists = get_pet_obj(pet_id)
        if exists:
            cursor.execute(
                f"""
                DELETE FROM '{TABLE_PETS}'
                WHERE id = '{pet_id}'
                """
            )
            conn.commit()
            return {"Delete": "Success"}, 204
        else:
            return None, 404


