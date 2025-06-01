import asyncio
from Asyncio.chapter_1.util import delay

#2.21

async def main():
    await asyncio.sleep(1)

loop = asyncio.new_event_loop()

try:
    loop.run_until_complete(main())
finally:
    loop.close()

# 2.22

def my_call_later():
    print('Меня вызову в будущем!')

async def main():
    my_loop = asyncio.get_running_loop()
    my_loop.call_soon(my_call_later)
    await delay(2)

asyncio.run(main(), debug=True)