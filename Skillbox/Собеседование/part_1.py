import sys
import time
from multiprocessing import Pool

dict_ = {
	1: 3,
	2: 2,
	3: 1
}
print(max(dict_))  #
print(max(dict_, key=lambda key: dict_[key]))

print("---***---" * 5)

# Разница is и ==
a = [1, 2, 3]
b = [1, 2, 3]
print("a is b : {}".format(a is b))
print("a == b : {}".format(a == b))

# Итераторы это объект имеющий методы __iter__ и __next__ позволяющий проходить по элементам коллекции
class Iters:
	def __init__(self, max):
		self.max = max
		self.current = 0

	def __iter__(self):
		return self

	def __next__(self):
		if self.current <= self.max:
			self.current += 1
			return self.current
		else:
			raise StopIteration

iter = Iters(3)
for i in iter:
	print(i)

print("---***---" * 5, "\nРазница list и tuple")
# Разница list и tuple
# 1. list изменяемый тип данных, а tuple неизменяемый
# 2. list занимает больше памяти чем tuple
# 3. Итерация list занимает больше времени

a = ['apple', 'banana', 'orange']
b = ('apple', 'banana', 'orange')
print("Занимаемая память объектом {}: {}".format(type(a), sys.getsizeof(a)))
print("Занимаемая память объектом {}: {}".format(type(b), sys.getsizeof(b)))

a = list(range(10000000))
b = tuple(range(10000000))

def timer(obj):
	start = time.time_ns()
	for i in obj:
		a = obj[i]
	res = time.time_ns() - start
	return f"Время итерации {type(obj)}: {res} наносекунд"

with Pool(5) as pool:
	print(pool.map(timer, [a, b]))

print("---***---" * 5, "\nГенератор")
# Разница итератора и генератора. Что такое генератор.
# Генератор это объект который может останавливаться и возобновляться,
# он создаёт итератор для создания последовательности значений, использует ключевое слово yield
def my_generator(n):
	for i in range(n + 1):
		yield i

my_gen = my_generator(5)
for i in my_gen:
	print(i)