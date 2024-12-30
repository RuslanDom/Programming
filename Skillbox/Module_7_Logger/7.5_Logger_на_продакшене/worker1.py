import logging, time, datetime

logger = logging.getLogger('main.worker1')

def worker1(x: int, y: int) -> int:
    logger.debug(f"Entered worker1({x}, {y})")

    # emulate a heisenbug (эмуляция не постоянной ошибки)
    current_ts = datetime.datetime.utcnow().timestamp()

    if int(current_ts) % 2 == 0 and x == y:
        raise OSError("Something went wrong")
    time.sleep(0.5)

    result = x ** y  # Верно

    logger.debug(f"Calculation result of worker1({x},{y}) = {result}")
    return result
