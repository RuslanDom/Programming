import asyncio, asyncpg



async def take(generator, to_take: int):
    item_count = 0
    async for item in generator:
        if item_count > to_take - 1:
            return
        item_count += 1
        yield item


async def main():
    connection: asyncpg.Connection = await asyncpg.connect(
        host="127.0.0.1",
        port=5432,
        user="postgres",
        database='products',
        password='password'
    )
    async with connection.transaction():
        query = 'SELECT product_id, product_name FROM product'
        product_generator = connection.cursor(query)

        async for product in take(product_generator, 1):
            print(product)


if __name__ == "__main__":
    asyncio.run(main())
