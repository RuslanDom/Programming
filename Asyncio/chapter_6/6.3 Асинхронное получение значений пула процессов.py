from multiprocessing import Pool


def  say_hello(name: str) -> str:
    return f"Hello, {name}"


if __name__ == "__main__":
    with Pool() as process_pool:
        # apply_async() - выполняется конкурентно
        hi_bro = process_pool.apply_async(say_hello, args=("Bro",))
        hi_alex = process_pool.apply_async(say_hello, args=("Alex",))
        hi_stan = process_pool.apply_async(say_hello, args=("Stan",))

        # get() - будет выполняться последовательно
        print(hi_bro.get())
        print(hi_alex.get())
        print(hi_stan.get())