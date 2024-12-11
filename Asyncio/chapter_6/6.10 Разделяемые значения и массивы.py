from multiprocessing import Process, Value, Array


"""
Для использования в разделяемой памяти
Метод get_lock() предназначен для блокирования участка кода или каких то данных
для того чтобы избежать ошибки при обращении к устаревшим данным
(пока 1-ый процесс не закончит выполнять свои действия с данными, 
2-ой процесс не сможет получить эти данные)
"""

def increment_value(shared_int: Value):
    shared_int.get_lock().acquire()  # Захватить в блокировку
    shared_int.value = shared_int.value + 1  # В данном примере эта строка кода <критическая секция>
    shared_int.get_lock().release()  # Освободить из блокировки
    # <КРИТИЧЕСКУЮ СЕКЦИЮ> может выполнять только один процесс

    # С использованием context manager
    # with shared_int.get_lock():
    #     shared_int.value = shared_int.value + 1


def increment_array(shared_array: Array):
    for index, integer in enumerate(shared_array):
        shared_array[index] = integer + 1


if __name__ == "__main__":
    integer = Value('i', 0)
    integer_array = Array('i', [0, 0])

    procs = [Process(target=increment_value, args=(integer, )),
             Process(target=increment_array, args=(integer_array, ))]

    [proc.start() for proc in procs]
    [proc.join() for proc in procs]

    print(integer.value)
    print(integer_array[:])

    print("---***---" * 8)

    """
    6.11
    Параллельное инкрементирование разделяемого счетчика
    т.е. изменение значения Value из разных процессов параллельно
    """

    for _ in range(100):
        integer = Value('i', 0)
        procs = [
            Process(target=increment_value, args=(integer, )),
            Process(target=increment_value, args=(integer, )),
            Process(target=increment_value, args=(integer, ))
        ]
        [proc.start() for proc in procs]
        [proc.join() for proc in procs]

        print(integer.value, end='')
        assert(integer.value == 3)



