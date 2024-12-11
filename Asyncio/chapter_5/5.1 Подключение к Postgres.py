import asyncio
import asyncpg

async def main():
    connection = await asyncpg.connect(
        host='127.0.0.1',
        user='postgres',
        database='postgres',
        password='password'
    )
    version = connection.get_server_version()
    print(f"Подключено! Версия Postgres == {version}")
    await connection.close()


if __name__ == "__main__":
    asyncio.run(main())
