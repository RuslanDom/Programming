
print("________________________СИНХРОННЫЙ________________________")
def positive_integers(until: int):
    for integer in range(until):
        yield integer

positive_iterator = positive_integers(10)

print(next(positive_iterator))  # 0
print(next(positive_iterator))  # 1
print(next(positive_iterator))  # 2
print(next(positive_iterator))  # 3

for i in positive_iterator:
    print("for", i)
"""
for 4
for 5
for 6
for 7
for 8
for 9
"""
print("________________________АСИНХРОННЫЙ________________________")
import asyncio
from Asyncio.util import delay, async_timer

async def positive_integers_async(until: int):
    for integer in range(until):
        await delay(integer)
        yield integer

@async_timer()
async def main():
    async_generator = positive_integers_async(3)
    print(type(async_generator))
    async for number in async_generator:
        print(f'Получено число: {number}')

asyncio.run(main())





