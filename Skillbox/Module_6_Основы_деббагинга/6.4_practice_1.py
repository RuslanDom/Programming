import heapq
import logging
import json
from datetime import datetime
from typing import List
from flask import Flask, request
import time

# curl -X POST http://localhost:5000/bubble/ --data "[7, 3, 1, 4, 2, 8]"
# curl -X POST http://localhost:5000/tim/ --data "[7, 3, 1, 4, 2, 8]"
# curl -X POST http://localhost:5000/heap/ --data "[7, 3, 1, 4, 2, 8]"

app = Flask(__name__)
logger = logging.getLogger(name="sort")

def bubble_sort(array: List[int]) -> List[int]:
    start = time.time()
    logger.info(f"Starting {bubble_sort.__name__} in {datetime.now()}")
    n = len(array)
    for i in range(0, n):
        for j in range(i + 1, n):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
    logger.info(f"Work time: {time.time() - start}")
    return array

def tim_sort(array: List[int]) -> List[int]:
    start = time.time()
    logger.info(f"Starting {tim_sort.__name__} in {datetime.now()}")
    array.sort()
    logger.info(f"Work time: {time.time() - start}")
    return array

def heapq_sort(array: List[int]) -> List[int]:
    start = time.time()
    logger.info(f"Starting {heapq_sort.__name__} in {datetime.now()}")
    data = []
    for value in array:
        heapq.heappush(data, value)  # heapq.heappush() - помещает элемент в кучу(heap)
    logger.info(f"Work time: {time.time() - start}")
    return [heapq.heappop(data) for _ in range(len(array))]  # heapq.heappop() - получает самый маленький элемент из кучи

algorithms = {
    "bubble": bubble_sort,
    "tim": tim_sort,
    "heapq": heapq_sort
}

@app.route("/<algorithm>/", methods=["POST"])
def sort_endpoint(algorithm: str):
    if algorithm not in algorithms:
        return f"This is algorithm not exist. Allowable algorithms: {algorithms.keys()}", 400
    # Получить все аргументы переданные в запросе в виде str
    form_data = request.get_data(as_text=True)
    # Запись str с args-ми в формате json-строки
    array = json.loads(form_data)
    # Вызов func-ции из словаря с алгоритмами
    result = algorithms[algorithm](array)
    # Возврат str-строки переведённой из json-строки
    return json.dumps(result)



def main():
    print(bubble_sort([4,7,2,3,1,9,0,8,12]))
    print(tim_sort([4,7,2,3,1,9,0,8,12]))
    print(heapq_sort([4,7,2,3,1,9,0,8,12]))

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logging.info("Started sort server")
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)
    # main()