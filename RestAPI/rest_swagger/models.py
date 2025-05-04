from dataclasses import dataclass
import sqlite3
from typing import Optional
from config.my_conf import *

DATA = [
    {"name": "Jerry", "owner": "John Doe"},
    {"name": "Buddy", "owner": "Mister Adams"},
    {"name": "Cuzko", "owner": "Bob Sicklar"}
]



@dataclass
class Pet:
    name: str
    owner: int
    id: Optional[int] = None

    def __getitem__(self, item):
        return getattr(self, item)


@dataclass
class Owner:
    first_name: str
    last_name: Optional[str]
    id: Optional[int] = None

    def __getitem__(self, item):
        return getattr(self, item)


def init_table_owner(initial_data):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(
            f"""
            SELECT name FROM sqlite_master WHERE type='table' AND name='{OWNERS_TABLE}';
            """
        )
        exists = cursor.fetchone()
        if exists is None:
            cursor.execute(
                f"""
                CREATE TABLE '{OWNERS_TABLE}' (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name VARCHAR(50) NOT NULL,
                last_name VARCHAR(50)
                )
                """
            )
            for item in initial_data:
                owner: Optional[Owner] = division_name(item["owner"])
                cursor.execute(
                    f"""
                    INSERT INTO '{OWNERS_TABLE}' 
                    (first_name, last_name)
                    VALUES (?, ?)
                    """,
                    (owner.first_name, owner.last_name)
                )
            conn.commit()


def init_table_pet(initial_data):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(
            f"""
            SELECT name FROM sqlite_master WHERE type='table' AND name='{PETS_TABLE}';
            """
        )
        exists = cursor.fetchone()
        if exists is None:
            cursor.execute(
                f"""
                CREATE TABLE '{PETS_TABLE}' (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(50) NOT NULL,
                owner INTEGER NOT NULL,
                FOREIGN KEY (owner) REFERENCES '{OWNERS_TABLE}' (id) ON DELETE CASCADE
                )
                """
            )
            for item in initial_data:
                owner: Optional[Owner] = division_name(item["owner"])
                exists: Optional[Owner] = get_owner_by_name(owner.last_name)
                if exists is None:
                    pass
                    # owner = add_owner(owner)
                    # owner_id = owner.id
                else:
                    owner_id = exists.id
                cursor.execute(
                f"""
                    INSERT INTO '{PETS_TABLE}' (name, owner)
                    VALUES (?, ?)
                    """,
          (item["name"], owner_id)
                )
            conn.commit()



def get_owner_by_name(name) -> Optional[Owner]:
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(
            f"""
            SELECT * FROM '{OWNERS_TABLE}'
            WHERE last_name = '{name}';
            """
        )
        exists = cursor.fetchone()
        if exists:
            return Owner(id=exists[0], first_name=exists[1], last_name=exists[2])



def add_owner(owner_data: Owner) -> Optional[Owner]:
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(
            f"""
            INSERT INTO '{OWNERS_TABLE}' (first_name, last_name)
            VALUES (?, ?)
            """,
            (owner_data.first_name, owner_data.last_name)
        )
        conn.commit()
        id = cursor.lastrowid
        return get_owner_by_id(id)


def get_owner_by_id(id) -> Optional[Owner]:
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(
            f"""
            SELECT * FROM '{OWNERS_TABLE}'
            WHERE id = '{id}'
            """
        )
        exists = cursor.fetchone()
        if exists:
            return Owner(id=exists[0], first_name=exists[1], last_name=exists[2])


def division_name(name: str) -> Optional[Owner]:
    data_name = name.split()
    if len(data_name) > 1:
        return Owner(first_name=data_name[0], last_name=data_name[1])
    elif len(data_name) == 1:
        return Owner(first_name=data_name[0], last_name=None)
    else:
        return None