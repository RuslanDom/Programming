import asyncio, os
from aiohttp import ClientSession
import time
from typing import Callable, Any, List
import functools

async def delay(delay_seconds:int):
    print(f"Засыпаю на {delay_seconds} с")
    await asyncio.sleep(delay_seconds)
    print(f"Сон в течении {delay_seconds} с")
    return delay_seconds

def async_timer():
    def wrapper(func: Callable) -> Callable:
        functools.wraps(func)
        async def wrapped(*args, **kwargs) -> Any:
            print(f"Выполняется функция {func} с аргументами: {args} {kwargs}")
            start = time.time()
            try:
                return await func(*args, **kwargs)
            finally:
                end = time.time() - start
                print(f"Время работы кода: {end}")
        return wrapped
    return wrapper


async def fetch_status(session: ClientSession, url: str, sec_delay: int=0) -> int:
    await asyncio.sleep(sec_delay)
    async with session.get(url) as result:
        return result.status


def load_common_words() -> List[str]:
    with open(os.path.join('../chapter_5/random_words.txt'), 'r') as file:
        res = [word.strip('\n') for word in file.readlines()]
        return res

