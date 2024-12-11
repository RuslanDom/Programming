import asyncio, asyncpg
import logging


async def main():
    connection: asyncpg.Connection = await asyncpg.connect(
        host='127.0.0.1',
        port=5432,
        user='postgres',
        database='products',
        password='password'
    )
    # Начать транзакцию базы данных
    async with connection.transaction():
        # await connection.execute("INSERT INTO brand VALUES(DEFAULT, 'brand_1')")
        # await connection.execute("INSERT INTO brand VALUES(DEFAULT, 'brand_2')")
        try:
            await connection.execute("INSERT INTO brand VALUES(505, 'brand_Adidas')")
            try:
                print("--------------SAVEPOINT--------------")
                async with connection.transaction():
                    await connection.execute("INSERT INTO brand VALUES(505, 'brand_Nike')")
            except Exception as ex:
                logging.warning('Ошибка создания второй транзакции(первая транзакция прошла успешно)', exc_info=ex)
        except Exception as ex:
            logging.warning('Ошибка создания первой транзакции (такой ID уже существует)', exc_info=ex)

    query = """SELECT brand_name FROM brand
               WHERE brand_name LIKE 'brand%'"""
    brands = await connection.fetch(query)  # Выбрать марки и убедиться что транзакция зафиксирована
    print(brands)
    await connection.close()

if __name__ == "__main__":
    asyncio.run(main())
