import asyncio
from Asyncio.chapter_1.util import delay

#2.13

async def main():
    task = asyncio.create_task(delay(5))
    try:
        # shield() игнорирует запросы на снятие
        result = await asyncio.wait_for(asyncio.shield(task), 3)
        print(result)
    except TimeoutError:
        print(f"Задача заняла более 3 сек, скоро закончится")
        # Дорабатывает до конца в блоке except
        result = await task
        print(result)


if __name__ == "__main__":
    asyncio.run((main()))
