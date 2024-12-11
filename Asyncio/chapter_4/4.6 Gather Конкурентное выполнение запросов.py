import asyncio, aiohttp
from aiohttp import ClientSession
from Asyncio.util import fetch_status, async_timer

"""
gather хоть и не детерминирован, но возвращает результаты работы сопрограмм в том порядке 
в котором получил в отличии от as_completed
"""


@async_timer()
async def main():
    async with ClientSession() as session:
        urls = ['https://www.example.com' for _ in range(1000)]
        requests = [fetch_status(session, url) for url in urls]  # Генерирует список сопрограмм для каждого запроса
        """return_exception=False or True
        В случае False обработает первое попавшееся исключение, остальные запросы будут выполнены до конца
        В случае True исключение будет являться результатом сопрограммы, а значит получим все имеющиеся исключения 
        запросы также не будут приостановлены, а выполнятся до конца"""
        status_code = await asyncio.gather(*requests, return_exceptions=True)  # Ждать завершения всех запросов
        exception_results = [res for res in status_code if isinstance(res, Exception)]
        successful_results = [res for res in status_code if not isinstance(res, Exception)]
        print(f"Успешные результаты: {successful_results}\nРезультаты с исключениями: {exception_results}")

if __name__ == "__main__":
    asyncio.run(main())
