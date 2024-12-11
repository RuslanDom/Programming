import asyncio
import functools
import time
from concurrent.futures import ProcessPoolExecutor
from typing import List, Dict



def partition(data: List, chunk_size: int) -> List:
    for i in range(0, len(data), chunk_size):
        yield data[i:i + chunk_size]


def map_frequencies(chunk: List[str]) -> Dict[str, int]:
    counter = {}

    for word in chunk:
        if counter.get(word):
            counter[word] = counter[word] + 1
        else:
            counter[word] = 1
    return counter


def merged_dictionaries(first: Dict[str, int],
                        second: Dict[str,int]) -> Dict[str, int]:
    merged = first
    for key in second:
        if key in merged:
            merged[key] = merged[key] + second[key]
        else:
            merged[key] = second[key]
    return merged


async def main(partition_size: int):
    with open("random_words.txt", 'r', encoding='utf-8') as f:  # Открыли текстовый файл
        contents = [el.strip('\n') for el in f.readlines()]  # Преобразовали текст в список слов и удалили "\n"
        loop: asyncio.AbstractEventLoop = asyncio.get_running_loop()  # Создаём event loop
        tasks = []
        start = time.time()
        with ProcessPoolExecutor() as pool:  # Открываем пул мультипроцессинга
            for chunk in partition(contents, partition_size):  # Разделяем на порции (chunk) весь контент
                tasks.append(loop.run_in_executor(pool,  # Собираем partial и pool, закидываем в исполнитель (executor) и добавляем в список tasks
                                                  functools.partial(map_frequencies, chunk)))
            intermediate_result = await asyncio.gather(*tasks)  # С помощью gather выполняем tasks
            final_result = functools.reduce(merged_dictionaries, intermediate_result)  # Получившиеся словари объединяем с помощью reduce
            print(f"Слово dolor встречается {final_result['dolor']} раз")
            end = time.time()
            print(f"Время MapReduce: {(end - start):.4f} секунд")


if __name__ == "__main__":
    asyncio.run(main(partition_size=60000))
