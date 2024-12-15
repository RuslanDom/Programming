import sys
from aiogram import Bot, Router, F
import os
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from utils.parser import main
from keyboard.inline.inline_country import set_country
# from states.search_command import Search
# from aiogram.fsm.context import FSMContext

router = Router()
path_data = os.path.join(r'..\Realty_bot\database\content_data.db')


@router.message(Command(commands='set_data'))
async def set_data(message: Message, bot: Bot):
    await message.answer("Выберите страну которую вы рассматриваете", reply_markup=set_country())


@router.callback_query(F.data.startswith('country_'))
async def loading_data(call: CallbackQuery):
    country = call.data.replace('country_', '')
    await call.message.answer(f'Загружаем базу данных для {country}\n'
                              f'Дождитесь сообщение об окончании загрузки...')

    for i in range(1, 2):
        main(country, str(i))
    await call.message.edit_reply_markup()
    await call.message.answer('Загрузка закончена!\n'
                              'Чтобы получить объявления введите команду /get')




