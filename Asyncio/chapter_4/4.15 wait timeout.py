import asyncio, aiohttp, logging
from Asyncio.chapter_1.util import fetch_status


async def main():
    async with aiohttp.ClientSession() as session:
        fetchers = [
            asyncio.create_task(fetch_status(session, 'https://example.com', sec_delay=1)),
            asyncio.create_task(fetch_status(session, 'https://example.com', sec_delay=3)),
            asyncio.create_task(fetch_status(session, 'https://example.com', sec_delay=3)),
            asyncio.create_task(fetch_status(session, 'https://example.com', sec_delay=1)),
        ]

        done, pending = await asyncio.wait(fetchers, return_when=asyncio.ALL_COMPLETED, timeout=2)
        print(f"Число завершившихся задач: {len(done)}")
        print(f"Число ожидающих задач: {len(pending)}")
        for done_task in done:
            if done_task.exception() is None:
                print(done_task.result())
            else:
                logging.error('Получено исключение', exc_info=done_task.exception())

        for pending_task in pending:
            pending_task.cancel()




if __name__ == "__main__":
    asyncio.run(main())
