from aiogram import Router, Bot
from aiogram.types import Message

router = Router()


@router.message()
async def echo_answer(message: Message, bot: Bot) -> None:
    """
    ЗХО функция
    :param message: str сообщение пользователя
    :param bot: aiogram.Bot
    :return: None
    """
    await message.reply(message.text)
    await bot.send_message(message.from_user.id,
                           'Что же это значило, я пока что глупый и не догоняю, что вы имели ввиду')