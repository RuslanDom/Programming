import asyncio, aiohttp
from aiohttp import ClientSession
from Asyncio.util import async_timer

@async_timer()
async def fetch_status(session: ClientSession, url: str) -> int:
    my_timeout = aiohttp.ClientTimeout(total=.01)  # Добавим собственный таймаут
    async with session.get(url=url, timeout=my_timeout) as result:
        return result.status

@async_timer()
async def main():
    session_timeout = aiohttp.ClientTimeout(total=1, connect=.1)  # Таймаут для сессии
    async with aiohttp.ClientSession(timeout=session_timeout) as session:
        url = 'http://www.example.com'
        status = await fetch_status(session, url)
        print(f"Состояние для {url} равно {status}")


if __name__ == "__main__":
    asyncio.run(main())
