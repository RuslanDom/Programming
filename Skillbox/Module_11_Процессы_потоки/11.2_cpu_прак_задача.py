import threading, multiprocessing, time
from rich.progress import track
import logging

logging.basicConfig(level=logging.INFO, format="%(name)s | %(asctime)s | %(levelname)s | %(message)s")
logger = logging.getLogger(__name__)

def task(number):
    return sum(i ** i for i in range(number))

def use_threads():
    start = time.time()
    logger.info(f"Strat function {__name__}")
    threads = []
    for i in track(range(10), description="Выполнение процесса ..."):
        thread = threading.Thread(target=task, args=(10000, ))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
    logger.info("Done in {:.4}".format(time.time() - start))


def use_multiprocessing():
    start = time.time()
    logger.info(f"Start function {__name__}")
    proces = []
    for i in track(range(10), description="Выполнение процесса ..."):
        proc = multiprocessing.Process(target=task, args=(10000, ))
        proc.start()
        proces.append(proc)
    for proc in proces:
        proc.join()
    logger.info("Done in {:.4}".format(time.time() - start))



if __name__ == "__main__":
    # use_threads()
    use_multiprocessing()
