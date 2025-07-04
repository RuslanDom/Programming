import asyncio
import asyncpg
from watchfiles import awatch

from Asyncio.chapter_1.util import async_timer
from typing import List, Dict
from concurrent.futures import ProcessPoolExecutor


product_query = \
"""
SELECT
p.product_id,
p.product_name,
p.brand_id,
s.sku_id,
pc.product_color_name,
ps.product_size_name 
FROM product as p
JOIN sku as s on s.product_id = p.product_id
JOIN product_color as pc on pc.product_color_id = s.product_color_id
JOIN product_size as ps on ps.product_size_id = s.product_size_id
WHERE p.product_id = 100
"""


async def query_product(pool: asyncpg.Pool):
    async with pool.acquire() as connection:
        return await connection.fetchrow(product_query)


@async_timer()
async def query_products_concurrently(pool: asyncpg.Pool, queries):
    queries = [query_product(pool) for _ in range(queries)]
    return await asyncio.gather(*queries)


def run_in_new_loop(num_queries: int) -> List[Dict]:
    async def run_queries():
        async with asyncpg.create_pool(
            host='127.0.0.1',
            port=5432,
            user='postgres',
            database='products',
            password='password',
            min_size=6,
            max_size=6
        ) as pool:
            return await query_products_concurrently(pool, num_queries)
    # Выполнять запросы в новом цикле событий и преобразовывать их в словари
    result = [dict(result) for result in asyncio.run(run_queries())]
    return result


@async_timer()
async def main():
    loop = asyncio.get_running_loop()
    pool = ProcessPoolExecutor()
    # Создать 5 процессов, каждый со своим циклом событий для выполнения запросов
    tasks = [loop.run_in_executor(pool, run_in_new_loop, 1000) for _ in range(5)]
    all_results = await asyncio.gather(*tasks)
    total_queries = sum(len(res) for res in all_results)
    print(f'Извлечено товаров из базы данных: {total_queries}')


if __name__ == "__main__":
    asyncio.run(main())