import itertools

colors = ['red', 'blue', 'green', 'yellow', 'black']
numbers = [1, 2, 3, 4]
# Получить все возможные варианты размещения цветов без повторений r: - кол-во позиций
for item in itertools.permutations(colors, 3):
    print(item)
for item in itertools.permutations(colors, 2):
    print(item)

print('=' * 60)
# В combinations() позиция элемента роли не играет
for item in itertools.combinations(numbers, 3):
    print(item)

print('=' * 60)
# cycle - кольцевой итератор
my_cycle = itertools.cycle(['раз', 'два', 'три'])
print(my_cycle)
print(next(my_cycle))
print(next(my_cycle))
print(next(my_cycle))
print(next(my_cycle))


