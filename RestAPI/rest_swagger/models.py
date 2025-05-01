from dataclasses import dataclass
import sqlite3
from typing import Optional
from config import CONFIG
from utils import division_name

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
    with sqlite3.connect(CONFIG["DB_NAME"]) as conn:
        cursor = conn.cursor()
        cursor.execute(
            f"""
            SELECT name FROM sqlite_master WHERE type='table' AND name={CONFIG['OWNERS_TABLE']};
            """
        )
        exists = cursor.fetchone()
        if exists is None:
            cursor.execute(
                f"""
                CREATE TABLE '{CONFIG['OWNERS_TABLE']}' (
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
                    INSERT INTO '{CONFIG['OWNERS_TABLE']}' (
                    first_name, last_name)
                    VALUES (?, ?)
                    """,
                    (owner.first_name, owner.last_name)
                )


def init_table_pet(initial_data):
    with sqlite3.connect(CONFIG["DB_NAME"]) as conn:
        cursor = conn.cursor()
        cursor.execute(
            f"""
            SELECT name FROM sqlite_master WHERE type='table' AND name='{CONFIG['PETS_TABLE']}';
            """
        )
        exists = cursor.fetchone()
        if exists is None:
            cursor.execute(
                f"""
                CREATE TABLE '{CONFIG["PETS_TABLE"]}' (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(50) NOT NULL,
                owner INTEGER NOT NULL ON DELETE CASCADE,
                FOREIGN KEY (owner) REFERENCES '{CONFIG['OWNERS_TABLE']}' (id)
                )
                """
            )
            for item in initial_data:

                cursor.execute(
                    f"""
                    INSERT INTO '{CONFIG["PETS_TABLE"]}' (name, owner)
                    VALUES (?, ?)
                    """,
                    ()
                )


def get_owner_by_name(name):
    with sqlite3.connect(CONFIG["DB_NAME"]) as conn:
        cursor = conn.cursor()
        cursor.execute(
            f"""
            SELECT * FROM '{CONFIG['OWNERS_TABLE']}'
            """
        )
        exists = cursor.fetchone()
        if exists is None:
            add_owner(name)



def add_owner(owner_data):
    with sqlite3.connect(CONFIG["DB_NAME"]) as conn:
        cursor = conn.cursor()
        owner = division_name(owner_data)
        cursor.execute(
            f"""
            INSERT INTO '{CONFIG['OWNERS_TABLE']}' (first_name, last_name)
            VALUES (?, ?)
            """,
            (owner.first_name, owner.last_name)
        )
        conn.commit()
        id = cursor.lastrowid
        return get_owner_by_id(id)



def get_owner_by_id(id):
    with sqlite3.connect(CONFIG["DB_NAME"]) as conn:
        cursor = conn.cursor()
        cursor.execute(
            f"""
            SELECT * FROM '{CONFIG['OWNERS_TABLE']}'
            WHERE id = '{id}'
            """
        )
        exists = cursor.fetchone()
        if exists:
            return Owner(id=exists[0], first_name=exists[1], last_name=exists[2])
