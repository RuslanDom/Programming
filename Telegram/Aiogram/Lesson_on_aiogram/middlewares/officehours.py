from datetime import datetime
from aiogram import BaseMiddleware
from typing import Dict, Callable, Any, Awaitable
from aiogram.types import Message, TelegramObject


def office_hours() -> bool:
    return True
    # return datetime.now().hour in ([i for i in (range(7, 24))])


class OfficeHoursMiddleware(BaseMiddleware):
    async def __call__(self,
                       # Чтобы все объекты фильтровал middleware, нужно заменить Message на TelegramObject
                       handler: Callable[[Message, Dict[str, Any]], Awaitable],  # Message = TelegramObject
                       event: Message,  # Message = TelegramObject
                       data: Dict[str, Any]
                       ):
        if office_hours():
            return await handler(event, data)

        await event.answer('Время работы бота с 7 до 22')
