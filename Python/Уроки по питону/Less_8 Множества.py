# Множества set и frozenset

data = {12,5,6,'Hello', True, 5,'Name',2,4,3,7,1,5,3,4,7,6,4} # Если не указывать ключи, то получается множество
data_1 = set('3,6,reno,54,3,6,8,2,True')
print(data)
print(data_1)
# В множестве нельзя обращаться по индексу data[1]

data.add(44)
data.update([22,33,44,55,66])
data.remove(22)
data.pop() # Удалит первый элемент
# data.clear()
print(data)

nums = [1,2,3,4,5,6,7,6,5,12,13,14,22,12]
nums = set(nums)
print(nums)

#frozenset
# Нельзя ничего удалять, добавлять и видоизменять, множество имеет свойства кортежей
newNums = frozenset(nums)
print(newNums)