import time
from multiprocessing import Process

def count(count_to: int) -> int:
    start = time.time()
    counter = 0
    while counter < count_to:
        counter += 1
    end = time.time()
    print(f"Закончен счёт до {count_to}, затраченное время: {end - start}")
    return counter


if __name__ == "__main__":
    start_time = time.time()

    # Создание процесса
    func_1 = Process(target=count, args=(100000000, ), daemon=True)  # С daemon=True можно не join - ить
    func_2 = Process(target=count, args=(100000000, ), daemon=True)
    # Запуск процесса
    func_1.start()
    func_2.start()
    # Ждать завершения процесса.
    # Этот метод блокирует выполнение, пока процесс не завершится
    func_1.join()
    func_2.join()

    end_time = time.time()
    print(f"Полное время работы: {end_time - start_time}")