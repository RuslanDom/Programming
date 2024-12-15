import sqlite3
import os
from aiogram import Bot
from aiogram.types import Message
from datetime import datetime


async def run(message: Message, bot: Bot):
    await message.answer(text=f'Сегодня:\n{datetime.now()}')
    with sqlite3.connect(os.path.join(r'database\userdata.db')) as conn:
        cur = conn.cursor()
        try:
            cur.execute('CREATE TABLE IF NOT EXISTS userdata (user_id INTEGER, name varchar(20), username varchar(50))')
            conn.commit()
            cur.execute(f'SELECT * FROM userdata WHERE user_id == "{message.from_user.id}"')
            user_id = cur.fetchall()

            if str(message.from_user.id) not in str(user_id):
                cur.execute(f'INSERT INTO userdata (user_id, name, username) VALUES ("{message.from_user.id}", '
                            f'"{message.from_user.first_name}", "{message.from_user.username}")')
                conn.commit()

            else:
                await bot.send_message(message.from_user.id, f'Привет {user_id[0][1]}')

        finally:
            await bot.send_message(message.from_user.id, f'Добро пожаловать')

