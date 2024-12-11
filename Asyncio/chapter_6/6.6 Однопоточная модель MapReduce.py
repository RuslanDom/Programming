# MapReduce предназначен для того чтобы большой набор данных разбить на меньшие части,
# решить задачи для поднабора данных (отображение mapping), а затем объединить полученные результаты
# в окончательный ответ (редукция reducing)

import functools
from typing import Dict


def map_frequency(text: str) -> Dict[str, int]:
    words = text.split(" ")
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] = frequency[word] + 1  # Увеличить счётчик, е сли слово есть в словаре
        else:
            frequency[word] = 1  # Добавить слово в словарь со значением 1, если слова нет в словаре
    return frequency

def merge_dictionaries(first: Dict[str, int],
                       second: Dict[str, int]) -> Dict[str, int]:
    merged = first
    for key in second:
        if key in merged:
            merged[key] = merged[key] + second[key]
        else:
            merged[key] = second[key]
    return merged

test_text = ["I know what I know",
             "I know that I know",
             "I don`t know much",
             "They don`t know much"]

mapped_results = [map_frequency(line) for line in test_text]

for result in mapped_results:
    print(result)

print("Результат через reduce()", functools.reduce(merge_dictionaries, mapped_results))




