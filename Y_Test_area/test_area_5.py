import asyncio
import multiprocessing
from random import randint

async def printed_symbol():
    try:
        while True:
            print(randint(0, 9), end="")
            await asyncio.sleep(0.0000001)
    except asyncio.CancelledError:
        raise

async def cancel_task_timer(second):
    await asyncio.sleep(second)

async def main():
        t1 = asyncio.create_task(printed_symbol())
        await cancel_task_timer(5)

        try:
            await t1
        except asyncio.CancelledError:
            pass



if __name__ == "__main__":
    asyncio.run(main())

