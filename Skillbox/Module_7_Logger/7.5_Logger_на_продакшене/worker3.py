import logging

logger = logging.getLogger('main.worker3')

def worker3(x: int, y: int) -> int:
    logger.debug(f"Entered worker3({x}, {y})")
    result = x ** x # Неверно
    logger.debug(f"Calculation result of worker3({x},{y}) = {result}")
    return result


