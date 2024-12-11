from asyncio import Future
import asyncio


def make_request() -> Future:
    future = Future()
    asyncio.create_task(set_future_value(future))
    return future

async def set_future_value(future):
    await asyncio.sleep(2)
    future.set_result(42)

async def main():
    future = make_request()
    print(f"Объект future готов? {future.done()}")
    value_future = await future
    print(f"Объект future готов? {future.done()}")
    print(value_future)


asyncio.run(main())

