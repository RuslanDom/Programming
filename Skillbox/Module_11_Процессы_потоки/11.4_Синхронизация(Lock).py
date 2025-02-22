import threading
import time
from rich.progress import track
import logging, random
from threading import Lock


logging.basicConfig(level=logging.INFO,
                    format="%(name)s | %(asctime)s | %(levelname)s | %(message)s"
                    )
logger = logging.getLogger(__name__)

COUNTER = 1
LOCK = Lock()

def worker_one():
    global COUNTER
    with LOCK:
        while COUNTER < 10:
            COUNTER += 1

            logger.info(f"Worker one incremented counter to {COUNTER}")
            time_shift = random.randint(0, 1)
            time.sleep(time_shift)


def worker_two():
    global COUNTER
    with LOCK:
        while COUNTER > -10:
            COUNTER -= 1

            logger.info(f"Worker two decremented counter to {COUNTER}")
            time_shift = random.randint(0, 1)
            time.sleep(time_shift)


def main():
    start = time.time()
    thread_1 = threading.Thread(target=worker_one)
    thread_2 = threading.Thread(target=worker_two)

    thread_1.start()
    thread_2.start()

    thread_1.join()
    thread_2.join()

    logger.info("Execution time {:.4}".format(time.time() - start))


if __name__ == "__main__":
    main()












