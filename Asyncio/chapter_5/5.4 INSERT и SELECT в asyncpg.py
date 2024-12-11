import asyncio, asyncpg
from typing import List


async def main():
    connection = await asyncpg.connect(
        host='127.0.0.1',
        port=5432,
        user='postgres',
        database='products',
        password='password'
    )
    try:
        await connection.execute("INSERT INTO brand VALUES(DEFAULT, 'Levis')")
        await connection.execute("INSERT INTO brand VALUES(DEFAULT, 'Seven')")

        brand_query = 'SELECT brand_id, brand_name FROM brand'
        result: List[asyncpg.Record] = await connection.fetch(brand_query)

        product_color_query = 'SELECT product_color_id, product_color_name FROM product_color'
        result_color: List[asyncpg.Record] = await connection.fetch(product_color_query)

        for brand in result:
            print(f"id: {brand['brand_id']}, name: {brand['brand_name']}")

        for product in result_color:
            print(f"id: {product['product_color_id']}, color: {product['product_color_name']}")

    finally:
        await connection.close()


if __name__ == "__main__":
    asyncio.run(main())