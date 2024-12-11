import multiprocessing
from multiprocessing import Pool

def say_hello(name: str) -> str:
    return f'Привет, {name}'



if __name__ == "__main__":
    """
    При вызове Pool() будет запущено столько процессов сколько физических ядер на машине
    Посмотреть кол-во ядер можно при помощи multiprocessing.cpu_count()
    С использованием Pool также можно получить значение функции в отличие от стандартной схемы start() join()
    """
    print("Кол-во ядер:", multiprocessing.cpu_count())
    with Pool() as process_pool:
        # Метод apply() блокирует выполнение функций (выполнение будет последовательное, а не параллельное)
        hi_bro = process_pool.apply(say_hello, args=("Bro",))
        hi_alex = process_pool.apply(say_hello, args=("Alex",))
        hi_stan = process_pool.apply(say_hello, args=("Stan",))
        print(hi_bro)
        print(hi_alex)
        print(hi_stan)