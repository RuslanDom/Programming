import sqlite3
from dataclasses import dataclass
from typing import Optional, List

DATA = (
    {"name": "Buddy", "kind": "dog", "age": 2, "owner": "Alex"},
    {"name": "Lucky", "kind": "dog", "age": 1, "owner": "Bob"},
    {"name": "Sara", "kind": "cat", "age": 3, "owner": "Stanly"},
    {"name": "Dingo", "kind": "dog", "age": 4, "owner": "Dick"},
)

ENABLE_FOREIGN_KEYS = "PRAGMA foreign_keys = ON;"
DATABASE = "light_app.db"
OWNERS_TABLE = "owners"
PETS_TABLE = "pets"

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
    age: Optional[int] = None
    owner: str = None

    def __getitem__(self, item):
        return getattr(self, item)


def init_table_owners(init_data):
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute(
            f"""
            SELECT name FROM sqlite_master WHERE type='table' AND name='{OWNERS_TABLE}'
            """
        )
        existing_owners = cursor.fetchall()
        if not existing_owners:
            cursor.execute(
                f"""
                CREATE TABLE '{OWNERS_TABLE}' (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(50)
                )
                """
            )
            conn.commit()
            for item in init_data:
                cursor.execute(
                    f"""
                    INSERT INTO '{OWNERS_TABLE}' (name)
                    VALUES (?)
                    """,
                    (item["owner"],)
                )

            conn.commit()


def init_table_pets(init_data):
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute(
            f"""
            SELECT name FROM sqlite_master WHERE type='table' AND name='{PETS_TABLE}'
            """
        )
        existing_pets = cursor.fetchall()
        if not existing_pets:
            cursor.execute(
                f"""
                CREATE TABLE '{PETS_TABLE}' (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(50) NOT NULL,
                kind VARCHAR(50) NOT NULL,
                age INTEGER NOT NULL,
                owner VARCHAR(50) NOT NULL,
                FOREIGN KEY (owner) REFERENCES '{OWNERS_TABLE}' (name) ON DELETE CASCADE
                )
                """
            )
            conn.commit()
            for item in init_data:
                cursor.execute(
                    f"""
                    INSERT INTO '{PETS_TABLE}' (name, kind, age, owner)
                    VALUES (?, ?, ?, ?)
                    """,
                    (item["name"], item["kind"], item["age"], item["owner"])
                )
            conn.commit()


def add_owner(data: Owner) -> Owner:
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute(
            f"""
            SELECT * FROM '{OWNERS_TABLE}'
            WHERE name = ?
            """,
            (data.name,)
        )
        res = cursor.fetchone()
        if res is None:
            cursor.execute(
                f"""
                INSERT INTO '{OWNERS_TABLE}' (name)
                VALUES (?)
                """,
                (data.name,)
            )
            conn.commit()
        cursor.execute(
            f"""
            SELECT * FROM '{OWNERS_TABLE}'
            WHERE name = '{data.name}'
            """
        )
    return _get_owner_obj(cursor.fetchone())


def add_pet(data: Pet) -> Pet:
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute(
            f"""
            SELECT * FROM '{OWNERS_TABLE}'
            WHERE name = '{data.owner}'
            """
        )
        res = cursor.fetchone()
        if res is None:
            cursor.execute(
                f"""
                INSERT INTO '{OWNERS_TABLE}' (name)
                VALUES (?)
                """,
                (data.owner,)
            )
            conn.commit()
        cursor.execute(
            f"""
            INSERT INTO '{PETS_TABLE}' (name, kind, age, owner)
            VALUES (?, ?, ?, ?)
            """,
            (data.name, data.kind, data.age, data.owner)
        )
        conn.commit()
        cursor.execute(
            f"""
            SELECT * FROM '{PETS_TABLE}'
            WHERE id = {cursor.lastrowid}
            """
        )
        raw_data = cursor.fetchone()
    return _get_pet_obj(raw_data)


def _get_pet_obj(data: tuple) -> Optional[Pet]:
    return Pet(id=data[0], name=data[1], kind=data[2], age=data[3], owner=data[4])


def _get_owner_obj(data: tuple) -> Optional[Owner]:
    return Owner(id=data[0], name=data[1])

# GET
def get_all_pets() -> List[Pet]:
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute(
            f"""
            SELECT * FROM '{PETS_TABLE}'
            """
        )
        pets = cursor.fetchall()
        return [_get_pet_obj(pet) for pet in pets]

def get_all_owners() -> List[Owner]:
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute(
            f"""
            SELECT * FROM '{OWNERS_TABLE}'
            """
        )
        owners = cursor.fetchall()
        return [_get_owner_obj(owner) for owner in owners]


