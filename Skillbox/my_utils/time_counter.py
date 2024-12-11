import time
from typing import Callable
import functools

def my_timer(func: Callable) -> Callable:
    functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        delay = time.time() - start
        return delay
    return wrapper


