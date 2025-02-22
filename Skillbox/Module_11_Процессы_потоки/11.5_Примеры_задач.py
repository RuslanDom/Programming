import threading, logging, random, time


logging.basicConfig(level=logging.INFO)
logger  =logging.getLogger(__name__)


class Philospher(threading.Thread):
    running = True

    def __init__(self, left_fork: threading.Lock, right_fork: threading.Lock):
        super().__init__()
        self.left_fork = left_fork
        self.right_fork = right_fork

    def run(self):
        while self.running:
            logger.info(f"Philosopher {self.name} start thinking")
            time.sleep(random.randint(1, 10))
            logger.info(f"Philosopher {self.name} is hungry")
            try:
                self.left_fork.acquire()
                logger.info(f"Philosopher {self.name} avquired left fork")
                if self.right_fork.locked():  # Возращает булевое значение состояние замка
                    continue
                try:
                    self.right_fork.acquire()
                    logger.info(f"Philosopher {self.name} avquired right fork")
                    self.dinning()
                finally:
                    self.right_fork.release()
            finally:
                self.left_fork.release()


    def dinning(self):
        logger.info(f"Philosopher {self.name} start eating")
        time.sleep(random.randint(1, 10))
        logger.info(f"Philosopher {self.name} finish eating")


def main():
    forks = [threading.Lock() for _ in range(5)]
    
    philosophers = [
        Philospher(forks[i % 5], forks[i + 1] % 5) 
        for i in range(5)
    ]

    Philospher.running = True

    for p in philosophers:
        p.start()
    time.sleep(200)
    Philospher.running = False
    logger.info("Now we`re finish")

if __name__ == "__main__":
    main()