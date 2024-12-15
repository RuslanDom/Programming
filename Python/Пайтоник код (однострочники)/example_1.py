from functools import reduce
from sys import stdout
from loguru import logger

logger.add(sink=stdout, format='{time} {level} {message}', level='DEBUG')


x1, x2, x3 = list(map(int, input('Enter number: ').strip().split()))
print(x1)

all_x = list(map(int, input('Enter number: ').strip().split()))
print(all_x)


# reduce() - принимает функцию, которая перемножает элементы переданной последовательности, и саму последовательность.
# map() - также принимает функцию (func=int) и последовательность, которую преобразует.
volume = reduce(lambda x, y: x * y, map(int, input('Enter number: ').strip().split()))

logger.debug(f"Volume is equal = {volume}")
