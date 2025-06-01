import asyncio, aiohttp
from Asyncio.chapter_1.util import fetch_status, async_timer


@async_timer()
async def main():
    async with aiohttp.ClientSession() as session:
        pending = [
            asyncio.create_task(fetch_status(session, 'https://www.example.com')),
            asyncio.create_task(fetch_status(session, 'https://www.example.com')),
            asyncio.create_task(fetch_status(session, 'https://www.example.com'))
        ]
        while pending:
            done, pending = await asyncio.wait(pending, return_when=asyncio.FIRST_COMPLETED)
            print(f"Число завершившихся задач: {len(done)}")
            print(f"Число ожидающих задач: {len(pending)}")
            for done_task in done:
                print(await done_task)


if __name__ == "__main__":
    asyncio.run(main())
