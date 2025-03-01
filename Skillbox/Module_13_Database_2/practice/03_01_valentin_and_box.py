# Начинающий боксёр Валентин прикинул: чтобы стать чемпионом мира в своём весе,
# ему надо победить 21 соперника (последний бой — с действующим держателем пояса).
# Валентин очень целеустремлённый — он составил БД со списком соперников.
# На сегодняшний день он победил уже в шести поединках.
# Помогите Валентину вычеркнуть побеждённых соперников из списка, пока он на тренировке.

import sqlite3
from typing import List

defeated_enemies = [
    "Иванов Э.",
    "Петров Г.",
    "Левченко Л.",
    "Михайлов М.",
    "Яковлев Я",
    "Кузнецов К.",
]


def remove_all_defeated_enemies(
        cursor: sqlite3.Cursor,
        defeated_enemies: List[str]
) -> None:
    for enemy in defeated_enemies:
        sql = ("DELETE FROM table_enemies WHERE name LIKE ?;")
        cursor.execute(sql, (enemy, ))


if __name__ == "__main__":
    with sqlite3.connect("practise.db") as conn:
        cursor = conn.cursor()
        remove_all_defeated_enemies(cursor, defeated_enemies)
        conn.commit()
