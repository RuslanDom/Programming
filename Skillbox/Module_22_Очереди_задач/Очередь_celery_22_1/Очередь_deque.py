# Responsibility - ответственность
# Responsiveness - отзывчивость, восприимчивость
# Deque - двусторонняя очередь, штраф
# Queue - очередь
# Celery - сельдерей

import math
import time
from collections import deque
from dataclasses import field, dataclass
from typing import Callable, Tuple, Dict

@dataclass
class Task:
    func: Callable
    args: Tuple = field(default_factory=tuple)
    kwargs: Dict = field(default_factory=dict)

    def execute(self) -> None:
        self.func(*self.args, **self.kwargs)

    def __str__(self):
        task_str = self.func.__name__ + "("
        f_args = ", ".join(map(repr, self.args))
        task_str += f_args

        if self.kwargs:
            f_kwargs = ", ".join(f"{k}={v!r}" for k, v in self.kwargs.items())
            task_str += ", " + f_kwargs

        task_str += ")"
        return task_str

class TaskQueue:
    def __init__(self):
        self.queue = deque()

    def add_task(self, task: Task) -> None:
        print(f"Adding task: {task}")
        self.queue.append(task)

    def execute_task(self) -> None:
        while self.queue:
            task = self.queue.popleft()
            print(f"Executing task: {task}")
            task.execute()
        print(f"Finished executing all tasks!")

if __name__ == "__main__":
    queue = TaskQueue()
    queue.add_task(
        Task(func=time.sleep, args=(1,))
    )
    queue.add_task(
        Task(func=print, args=("Hello", "World"), kwargs={"sep": "_"})
    )
    queue.add_task(
        Task(func=math.factorial, args=(50,))
    )
    queue.execute_task()

# Celery — одна из наиболее распространённых систем, с помощью которой легко находить
# решения для работы с очередями задач в Python. Она предоставляет простой и удобный интерфейс для создания и планирования асинхронных задач.
# Celery поддерживает различные брокеры сообщений, такие как:
#     RabbitMQ,
#     Redis,
#     Amazon SQS.
# Брокер сообщений — это компонент, который служит посредником между различными компонентами распределённой системы.