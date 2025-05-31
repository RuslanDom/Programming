import asyncio
from aiohttp import ClientSession
import aiohttp
from Asyncio.chapter_1.util import async_timer

async def fetch_status(session: ClientSession, url: str, sec_delay: int=0) -> int:
    await asyncio.sleep(sec_delay)
    async with session.get(url) as result:
        return result.status

@async_timer()
async def main():
    async with aiohttp.ClientSession() as session:
        fetchers = [
            fetch_status(session, 'https://www.example.com', 1),
            fetch_status(session, 'https://www.example.com', 4),
            fetch_status(session, 'https://www.example.com', 2),
            fetch_status(session, 'https://www.example.com', 1),
            fetch_status(session, 'https://www.example.com', 2),
        ]
        # Выполнение через gather.
        # Выполняется конкурентно, но результат можно получить только тогда когда завершится выполнение
        # последней сопрограммы
        # res = await asyncio.gather(*fetchers)
        # print(res)

        # Выполнение через as_completed.
        # Выполняется конкурентно и результаты будут получены не детерминированно, в соответствие с тем, которые сопрограммы
        # уже выполнены те и будут выведены в результатах
        for finished_task in asyncio.as_completed(fetchers, timeout=3):
            try:
                print(await finished_task)
            except asyncio.TimeoutError:
                print('Произошёл таймаут')

        for task in asyncio.all_tasks():
            print(task)

if __name__ == "__main__":
    asyncio.run(main())

