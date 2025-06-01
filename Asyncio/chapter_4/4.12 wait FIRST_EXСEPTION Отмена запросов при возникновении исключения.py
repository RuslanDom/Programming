import asyncio
from aiohttp import ClientSession
import logging
from Asyncio.chapter_1.util import fetch_status, async_timer

@async_timer()
async def main():
    async with ClientSession() as session:
        fetchers = [
            asyncio.create_task(fetch_status(session, 'python://bad.com')),
            asyncio.create_task(fetch_status(session, 'https://example.com', sec_delay=3)),
            asyncio.create_task(fetch_status(session, 'https://example.com', sec_delay=3)),
        ]
        done, pending =await asyncio.wait(fetchers, return_when=asyncio.FIRST_EXCEPTION)  # Запросы будут выполняться до первого исключения
        print(f"Число завершившихся задач: {len(done)}")
        print(f"Число ожидающих задач: {len(pending)}")

        for done_task in done:
            if done_task.exception() is None:
                print(done_task.result())
            else:
                logging.error("Возникло исключение: ", exc_info=done_task.exception())

        for pending_task in pending:
            pending_task.cancel()


if __name__ == "__main__":
    asyncio.run(main())
