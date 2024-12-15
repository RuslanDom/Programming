import json
import sqlite3
from aiogram import Bot, Router, F
import os
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from keyboard.inline.inline_country import get_inline_country
import time

router = Router()
path_data = os.path.join(r'..\Realty_bot\database\content_data.db')


@router.message(Command(commands='get'))
async def get_data(message: Message, bot: Bot):
    await message.answer('Выберите объявления какой страны вас интересуют', reply_markup=get_inline_country())


@router.callback_query(F.data.startswith('get_country_'))
async def get_country(call: CallbackQuery):
    country = call.data.replace('get_country_', '')
    country = country.replace('-', '_')
    await call.message.answer(country)
    await call.message.edit_reply_markup()
    with sqlite3.connect(path_data) as conn:
        cur = conn.cursor()
        try:
            cur.execute(f"SELECT * FROM {country}")
            data = cur.fetchall()
            print(data)
            for v in data:
                name = v[0]
                link = v[1]
                price = v[2]
                location = json.loads(v[3])
                data_message = f"{name}\n{price}\n{location['Country']}\n{link}"
                await call.message.answer(data_message)
        except sqlite3.OperationalError:
            await call.message.answer(f'Эта страна ещё не загружена в базу данных\n'
                                      f'Добавьте {country} через команду /set_data')


