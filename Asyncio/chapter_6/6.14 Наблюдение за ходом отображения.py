import asyncio
from asyncio import AbstractEventLoop
from concurrent.futures import ProcessPoolExecutor
from functools import partial, reduce
from typing import List, Dict
import time
from multiprocessing import Value

map_progress: Value

def init(progress: Value):
    global map_progress
    map_progress = progress


def partition(data: List, chunk_size: int):
        for i in range(0, len(data), chunk_size):
            yield data[i:i + chunk_size]


def map_frequencies(chunk):
    counter = {}
    for word in chunk:
        if counter.get(word):
            counter[word] = counter[word] + 1
        else:
            counter[word] = 1
    # Выделяем критическую секцию для map_progress
    with map_progress.get_lock():
        map_progress.value += 1
    return counter


async def progress_reporter(total_partitions: int):
    while map_progress.value < total_partitions:
        print(f'Завершено операций отображения:{map_progress.value}/{total_partitions}')
        await asyncio.sleep(0.1)


def merge_dicts(first: Dict[str, int], second: Dict[str, int]) -> Dict[str, int]:
    merged = first
    for key in second:
        if key  in merged:
            merged[key] = merged[key] + second[key]
        else:
            merged[key] = second[key]
    return merged

async def main(partition_size):
    global map_progress
    with open('random_words.txt', 'r', encoding='utf-8') as f:
        data = [word.strip('\n') for word in f.readlines()]
        loop: AbstractEventLoop = asyncio.get_running_loop()
        tasks = []
        map_progress = Value('i', 0)
        start = time.time()
        with ProcessPoolExecutor(initializer=init, initargs=(map_progress,)) as pool:
            total_partitions = len(data) // partition_size
            reporter = asyncio.create_task(progress_reporter(total_partitions))
            for chunk in partition(data, partition_size):
                tasks.append(loop.run_in_executor(pool, partial(map_frequencies, chunk)))
            intermediate_result = await asyncio.gather(*tasks)
            await reporter
            final_result = reduce(merge_dicts, intermediate_result)
            print(f"Слово dolor встречается {final_result['dolor']} раз")
            end = time.time()
            print(f"Время MapReduce: {(end - start):.4f} секунд")


if __name__ == "__main__":
    asyncio.run(main(50000))
