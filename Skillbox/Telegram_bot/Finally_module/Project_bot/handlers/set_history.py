from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from Skillbox.Telegram_bot.Finally_module.Project_bot.database.commands_data import get_history, history_insert, clear_all_history

router = Router()


@router.message(Command(commands="history"))
async def send_history(message: Message) -> None:
    """
    Функция вывода истории команд пользователя
    :param message: str
    :return: None
    """
    history_insert(message.from_user.id, message.text)
    result = get_history(message.from_user.id)
    for i in result:
        await message.answer(f"Пользователь ID: {i['user_id']}---[Сообщение]: {i['user_history']}")


@router.message(Command(commands="clear_history"))
async def delete_history(message: Message):
    clear_all_history()
    await message.answer('История удалена')

