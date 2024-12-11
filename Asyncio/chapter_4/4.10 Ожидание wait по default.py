import asyncio, aiohttp
import logging

from Asyncio.util import async_timer, fetch_status


@async_timer()
async def main():
    async with aiohttp.ClientSession() as session:
        fetchers = [
            asyncio.create_task(fetch_status(session, 'https://www.example.com')),
            asyncio.create_task(fetch_status(session, 'python://www.example.com')),
            asyncio.create_task(fetch_status(session, 'http://example.com')),
        ]
        done, pending = await asyncio.wait(fetchers)
        print(f"Число завершившихся задач: {len(done)}")
        print(f"Число ожидающих задач: {len(pending)}")
        for done_task in done:
            # result = await done_task  # Возбудит исключение, если оно имеется
            if done_task.exception() is None:
                print(done_task.result())
            else:
                logging.error("При выполнение запроса возникло исключение",
                              exc_info=done_task.exception())


if __name__ == "__main__":
    asyncio.run(main())
