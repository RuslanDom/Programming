import asyncio
from Asyncio.chapter_1.util import delay


async def main():
    sleep_three_sec = asyncio.create_task(delay(3))
    sleep_again = asyncio.create_task(delay(2))
    sleep_once_more = asyncio.create_task(delay(4))

    await sleep_three_sec
    await sleep_again
    await sleep_once_more

asyncio.run(main())

print("---***---" * 7)

async def write_every_second():
    for _ in range(3):
        await asyncio.sleep(1)
        print('Сплю 1 секунду')

async def example():
    sleep_three_sec = asyncio.create_task(delay(3))
    sleep_again = asyncio.create_task(delay(3))

    await write_every_second()
    await sleep_three_sec
    await sleep_again

asyncio.run(example())

print("---***---" * 7)


async def _main():
    sleep_for_three = asyncio.create_task(delay(3))
    sleep_for_two = asyncio.create_task(delay(2))
    print("Этот код выполнился раньше")
    task1 = await sleep_for_three
    task2 = await sleep_for_two
    print(task1)
    print(task2)


asyncio.run(_main())




