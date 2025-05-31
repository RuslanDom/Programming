import asyncio, asyncpg
from Asyncio.chapter_1.util import async_timer


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

@async_timer()
async def query_product(pool):
    # Сопрограмма acquire захватывает соединение из пула и позволяет выполнить какие-либо действия
    # после использования соединение возвращается в пул
    async with pool.acquire() as connection:
        return await connection.fetchrow(product_query)

# Синхронно
@async_timer()
async def query_product_synchronously(pool, queries):
    return [await query_product(pool) for _ in range(queries)]


# Асинхронно
async def query_product_concurrently(pool, queries):
    # В конкурентном исполнении query_product запускается в gather
    queries = [query_product(pool) for _ in range(queries)]
    return await asyncio.gather(*queries)

async def main():
    # Создать пул с 6 подключениями
    async with asyncpg.create_pool(
        host='127.0.0.1',
        port=5432,
        user='postgres',
        database='products',
        password='password',
        min_size=6,
        max_size=6
    ) as pool:
        # Синхронно и конкурентно выполнить 2 сопрограммы по 100 запросов
        await query_product_synchronously(pool, 100)
        await query_product_concurrently(pool, 100)

if __name__ == "__main__":
    asyncio.run(main())