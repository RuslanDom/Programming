import asyncio, asyncpg


async def main():
    connection: asyncpg.Connection = await asyncpg.connect(
        host='127.0.0.1',
        port=5432,
        user='postgres',
        database='products',
        password='password'
    )
    query = "SELECT product_id, product_name FROM product"
    async with connection.transaction():
        async for product in connection.cursor(query):
            print(product)
        """Перемещение курсора
        cursor = await connection.cursor(query)  Создать курсор для запроса
        await cursor.forward(500)  Сдвинуть курсор на 500 записей вперёд
        products = await cursor.fetch(100)  Получить 100 записей
        for product in products:
            print(product) 
        """
    await connection.close()

if __name__ == "__main__":
    asyncio.run(main())
