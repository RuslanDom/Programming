from aiogram.types import Message
from aiogram import Bot
from Telegram.Aiogram.Lesson_on_aiogram.keyboards.inline import make_inline_keyboard
from Telegram.Aiogram.Lesson_on_aiogram.keyboards.reply import send_location
import sqlite3


async def run_bot(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, text=f"Привет <em><b>{message.from_user.username}</b></em>")
    with sqlite3.connect(database=r'C:\Users\Admin\Desktop\Programming\Telegram\Aiogram\Lesson_on_aiogram\database\database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS telegram_users (id INTEGER PRIMARY KEY AUTOINCREMENT, '
                       'users_ID INTEGER, username varchar(20), first_name varchar(20), phone_number INTEGER(12))')
        conn.commit()
    await message.answer_photo(
        photo='AgACAgIAAxkBAAIF_WbW4SlJwNnE-v4DwSxqJLSBjOdzAAK05DEbrle4Ss9eRAaBPl7PAQADAgADcwADNQQ',
        caption='И от котика привет', reply_markup=make_inline_keyboard()
    )


async def my_location(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, text='Получить локацию', reply_markup=send_location())































# from aiogram.types import Message
# from aiogram import F
# from aiogram.filters import CommandStart, Command
# from aiogram import Bot, Dispatcher
#
# dp = Dispatcher()
#
# @dp.message(Command('start'))
# async def cmd_start(message: Message, bot: Bot):
#     await bot.send_message(message.from_user.id, f'Good morning {message.from_user.id}')
#
#
# @dp.message(Command('help'))
# async def info(message: Message, bot: Bot):
#     text = f"/start - Начало работы бота\n/help - помощь - справка"
#     await message.answer(text)
#
#
# @dp.message(F.text == 'How?')
# async def how_are_you(message: Message, bot: Bot):
#     await message.answer('I`m OK!')
#
#
# @dp.message(F.photo)
# async def get_photo(message: Message, bot: Bot):
#     id_photo = message.photo[-1].file_id
#     await message.answer('Картинку получил:) ID: {}'.format(id_photo))
#     await bot.download_file(id_photo,
#                             destination=r'C:\Users\Admin\Desktop\Programming\Telegram\Aiogram\Lesson_on_aiogram\img\photo.jpg')
#
#
# @dp.message(Command('send_image'))
# async def send_photo(message: Message, bot: Bot):
#     await message.answer_photo(
#         photo="AgACAgIAAxkBAAID-2bU00CX-QVSnytrskgEY0L_N_SjAAKW5TEbRjioStNQt3UPDOY7AQADAgADbQADNQQ",
#         caption='Это заголовок!')
