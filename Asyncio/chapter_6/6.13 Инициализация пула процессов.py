from concurrent.futures import ProcessPoolExecutor
import asyncio
from multiprocessing import Value


shared_counter: Value

def init(counter: Value) -> None:
    global shared_counter
    shared_counter = counter

def increment() -> None:
    with shared_counter.get_lock():
        shared_counter.value += 1

async def main():
    counter = Value('d', 0)
    loop = asyncio.get_running_loop()
    with ProcessPoolExecutor(initializer=init, initargs=(counter,)) as pool:  # Пул должен выполнить init с аргументом counter
        await loop.run_in_executor(pool, increment)
        print(counter.value)



if __name__ == "__main__":
    asyncio.run(main())

