import threading, queue
import logging, sys


logging.basicConfig(level=logging.INFO, stream=sys.stdout, format="%(levelname)s | %(message)s")
logger = logging.getLogger(__name__)

class Task:
    def __init__(self, priority, task):
        self.priority = priority
        self.task = task


TASKS = [
    Task(5, "Готовить"),
    Task(3, "Мыть"),
    Task(8, "Стирать"),
    Task(2, "Убирать"),
    Task(6, "Гладить"),
    Task(1, "Красить"),
    Task(4, "Одевать"),
    Task(7, "Носить")
]

class Administrator(threading.Thread):
    def __init__(self, q: queue.PriorityQueue):
        super().__init__()
        self.queue = q

    def run(self):
        for task in TASKS:
            self.queue.put((task.priority, task.task))
        logger.info("Список задач сформирован по приоритетности")


class Worker(threading.Thread):
    def __init__(self, q: queue.PriorityQueue):
        super().__init__()
        self.queue = q

    def run(self):
        while not self.queue.empty():
            priority, task = self.queue.get()
            logger.info(f"Выполняется приоритет {priority}: {task}")
            self.queue.task_done()
        logger.info("Все задачи выполнены")


def main():
    q = queue.PriorityQueue()
    admin = Administrator(q)
    admin.start()
    worker = Worker(q)
    worker.start()
    admin.join()
    worker.join()


if __name__ == "__main__":
    main()
