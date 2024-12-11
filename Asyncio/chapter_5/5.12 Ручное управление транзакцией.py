import asyncio, asyncpg
from asyncpg.transaction import Transaction


async def main():
    connection: asyncpg.Connection = await asyncpg.connect(
        host="127.0.0.1",
        port=5432,
        user='postgres',
        database='products',
        password='password'
    )
    transaction: Transaction = connection.transaction()  # Создаём экземпляр транзакции
    await transaction.start()  # Стартуем транзакцию в ручном управлении
    try:
        await connection.execute("INSERT INTO brand VALUES(DEFAULT, brand_HotDog)")
        await connection.execute("INSERT INTO brand VALUES(DEFAULT, brand_BigDog)")
    except asyncpg.PostgresError:
        print('Ошибка, транзакция откатывается')
        await transaction.rollback()  # Откат при исключении
    else:
        print("Успешно, транзакция прошла!")
        await transaction.commit()  # Фиксация транзакции

    query = """SELECT brand_name FROM brand
               WHERE brand_name LIKE 'brand%'
            """
    brands = await connection.fetch(query)
    print(brands)
    await connection.close()


if __name__ == "__main__":
    asyncio.run(main())
