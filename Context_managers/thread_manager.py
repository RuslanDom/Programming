import threading
import time



def my_func():
    return sum(map(lambda x: x * 2, [i for i in range(1000)]))


class ThreadManager:
    def __init__(self, func):
        self.task = threading.Thread(target=func)

    def __enter__(self):
        print('Function run...')
        self.start_timer = time.time()
        self.task.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        ended_time = time.time() - self.start_timer
        self.task.join()
        print(f'Function stop. Time work: {round(ended_time, 4)}')




if __name__ == "__main__":
    with ThreadManager(my_func) as f:
        print(f)


