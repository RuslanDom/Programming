from aiogram import Router, Bot
from aiogram.types import Message
from Skillbox.Telegram_bot.Finally_module.Project_bot.database.commands_data import history_insert

router = Router()


@router.message()
async def echo_answer(message: Message, bot: Bot) -> None:
    """
    ЗХО - бот функция
    :param message: str сообщение пользователя
    :param bot: aiogram.Bot
    :return: None
    """
    history_insert(message.from_user.id, message.text)
    await message.reply(message.text)
    await bot.send_message(message.from_user.id,
                           'Что же это значило, я пока что глупый и не догоняю, что вы имели ввиду')