import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, ContentType
from config import BOT_TOKEN, admin_id
from handlers.basic import run_bot, my_location
from aiogram.filters import Command
from handlers.callback import name_lastname
from utils.commands import set_command
from handlers.pay import (order_cat, pre_checkout_query, success_pay, shipping_check, order_boxing_gloves, pay_lot_1,
                          pre_checkout_query_for_lot, success_payment_lot1)
import logging
from middlewares.officehours import OfficeHoursMiddleware

from handlers import form
from state.states_form import StepsForm

from handlers.send_media import get_audio, get_media_group, get_video, get_sticker, get_photo, get_audio_playlist1


async def start(bot: Bot):
    await bot.send_message(admin_id, text="<b>Бот</b> запущен")
    await set_command(bot)


async def stop(bot: Bot):
    await bot.send_message(admin_id, text='<b>Бот</b> пошёл спать')


async def lets_go():
    bot = Bot(token=BOT_TOKEN, parse_mode='html')
    dp = Dispatcher()
    # dp.update.middleware.register(OfficeHoursMiddleware()) - будет все объекты регулировать middleware
    dp.message.middleware.register(OfficeHoursMiddleware())  # Бот будет работать только в установленные часы
    dp.startup.register(start)
    # Регистрация команды start
    dp.message.register(run_bot, Command(commands=['start', 'run']))
    dp.callback_query.register(name_lastname)

    # Регистрация Машины состояний
    dp.message.register(form.get_form, Command(commands='form'))
    dp.message.register(form.get_name, StepsForm.name)
    dp.message.register(form.get_lastname, StepsForm.lastname)
    dp.message.register(form.get_age, StepsForm.age)

    dp.message.register(my_location, Command(commands='location'))
    # Регистрация handlers на оплату
    dp.message.register(order_cat, Command(commands='pay'))
    dp.message.register(order_boxing_gloves, Command(commands='box'))
    dp.shipping_query.register(shipping_check)
    dp.pre_checkout_query.register(pre_checkout_query)
    dp.message.register(pay_lot_1, Command(commands='lot1'))
    dp.pre_checkout_query.register(pre_checkout_query_for_lot)
    dp.message.register(success_payment_lot1, F.content_type == ContentType.SUCCESSFUL_PAYMENT)
    dp.message.register(success_pay, F.content_type == ContentType.SUCCESSFUL_PAYMENT)

    # Регистрация handlers по отправке файлов
    dp.message.register(get_photo, Command(commands='photo'))
    dp.message.register(get_video, Command(commands='video'))
    dp.message.register(get_audio, Command(commands='audio'))
    dp.message.register(get_sticker, Command(commands='sticker'))
    dp.message.register(get_media_group, Command(commands='media'))
    dp.message.register(get_audio_playlist1, Command(commands='slipknot'))

    dp.shutdown.register(stop)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    try:
        logging.basicConfig(level=logging.INFO)
        asyncio.run(lets_go())
    except KeyboardInterrupt:
        print('Finish')

# import asyncio

# import Telegram.Aiogram.Lesson_on_aiogram.handlers
# import aiogram
# from Telegram.Aiogram.Lesson_on_aiogram.config import admin_id
# from aiogram.filters import CommandStart, Command
# from aiogram.types import Message
# # from Telegram.Aiogram.Lesson_on_aiogram.loader import bot, dp
# from Telegram.Aiogram.Lesson_on_aiogram.utils.commands import set_commands
# from aiogram import Bot, Dispatcher
# from Telegram.Aiogram.Lesson_on_aiogram.config import BOT_TOKEN
#
# bot = Bot(token=BOT_TOKEN, parse_mode='html')
# dp = Dispatcher()
#
# async def start_bot():
#     await set_commands(bot)
#     await bot.send_message(admin_id, text='Бот запущен')
#
#
# async def main():
#     dp.startup.register(start_bot)
#     try:
#         await dp.start_polling(bot)
#     finally:
#         await bot.session.close()
#
#
# if __name__ == "__main__":
#     try:
#         logging.basicConfig(level=logging.INFO)
#         asyncio.run(main())
#     except KeyboardInterrupt:
#         print('EXIT')
