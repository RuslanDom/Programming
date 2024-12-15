from aiogram import Router, Bot
from Project_bot.models.models import *
from aiogram.types import Message
from aiogram.filters import Command
from Project_bot.handlers.basic_handlers import last_query


router = Router()


@router.message(Command(commands="history"))
async def send_history(message: Message, bot: Bot):
    """
    Функция записи в БД и вывода истории команд пользователя
    :param message:
    :param bot:
    :return:
    """
    if not last_query:
        await bot.send_message(message.from_user.id, "Нет истории")
    else:
        with db:
            UserHistory(user_id=message.from_user.id, user_history=last_query).save()

    data = UserHistory.select()
    for i in data:
        await message.answer(f"ID пользователя {i.user_id}\n{i.user_history}")
        # logger.info(i.user_id, i.user_history)
    last_query.clear()
