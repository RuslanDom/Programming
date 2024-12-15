"""В контексте деревьев префиксы — части или подстроки, которые являются начальными фрагментами других строк.
В деревьях префиксов каждый узел представляет префикс строки, а пути от корня до листьев образуют полные строки.
Само дерево префиксов — структура данных, используемая для эффективного хранения и поиска строк или
последовательностей символов. Это древовидная структура, в которой каждый узел представляет префикс или часть строки.
Каждый узел может иметь несколько потомков, которые представляют следующие символы в строке."""

class HashTable:
    def __init__(self):
        # Создаём пустой список, который будет использоваться в качестве основы хеш-таблицы
        self.table = [None] * 10  # Изначально устанавливаем размер таблицы — 10 элементов

    def _hash_function(self, key):
        # Хеш-функция преобразует ключ в индекс таблицы
        # Простейшая хеш-функция — остаток от деления на размер таблицы
        return hash(key) % len(self.table)

    def _get_index(self, key):
        # Получаем индекс элемента в таблице по ключу
        hash_value = self._hash_function(key)
        # Если по этому индексу ещё нет элемента или ключи совпадают, возвращаем индекс
        if self.table[hash_value] is None or self.table[hash_value][0] == key:
            return hash_value
        else:
            index = (hash_value + 1) % len(self.table)  # Используем линейное пробирование
            while self.table[hash_value] is None or self.table[hash_value][0] != key:
                index = (index + 1) % len(self.table)
            return index

    def insert(self, key, value):
        # Вставляем элемент в хеш-таблицу
        index = self._get_index(key)
        self.table[index] = (key, value)

    def search(self, key):
        # Ищем элемент в хеш-таблице по ключу
        index = self._get_index(key)
        print(f"Индекс: {index}")
        if self.table[index] is not None and self.table[index][0] == key:
            return self.table[index][1]  # Возвращаем значение элемента, если он найден
        else:
            return None  # Возвращаем None, если элемент не найден

    def delete(self, key):
        # Удаляем элемент из хеш-таблицы по ключу
        index = self._get_index(key)
        if self.table[index] is not None and self.table[index][0] == key:
            self.table[index] = None  # Просто удаляем элемент, присваивая ему значение None


# Создаём экземпляр хеш-таблицы
hash_table = HashTable()

# Вставляем элементы в хеш-таблицу
hash_table.insert("apple", 1)
hash_table.insert("banana", 2)
hash_table.insert("orange", 3)

# Ищем элементы в хеш-таблице
# print(hash_table.search("apple"))  # Вывод: 1
# print(hash_table.search("banana"))  # Вывод: 2
# print(hash_table.search("orange"))  # Вывод: 3
# print(hash_table.search("grape"))  # Вывод: None

# Удаляем элемент из хеш-таблицы
hash_table.delete("banana")

# Проверяем, что элемент удалён
# print(f'Удаленный элемент: {hash_table.search("banana")}')  # Вывод: None


"""Библиотека pygtrie"""
from pygtrie import Trie

# Создание экземпляра дерева префиксов
trie = Trie()

# Вставка элементов в дерево
trie["apple"] = 1
trie["banana"] = 2
trie["orange"] = 3

# Проверка наличия элементов
print("apple" in trie)  # Вывод: True
print("pear" in trie)  # Вывод: False

# Получение значения элемента
print(trie["banana"])  # Вывод: 2

# Удаление элемента
del trie["banana"]
print("banana" in trie)  # Вывод: False

# Поиск всех элементов с заданным префиксом
prefix_items = trie.items("a")
print(list(prefix_items)) # Вывод: [(('a', 'p', 'p', 'l', 'e'), 1)]

# Автодополнение
prefix = "app"
matching_suggestions = list(trie.iterkeys(prefix))
print(matching_suggestions)  # Вывод: [('a', 'p', 'p', 'l', 'e')]

"""В этом примере мы:
    - создали дерево префиксов,
    - вставили несколько элементов,
    - проверили наличие элементов,
    - получили значение элемента,
    - удалили элемент,
    - выполнили поиск элементов с заданным префиксом,
    - получили автодополнение для заданной последовательности символов."""


"""Библиотека marisa-trie"""
"""Предоставляет эффективную реализацию компактных деревьев префиксов в Python.
 Она может быть полезна при работе с большими объёмами данных, например словарями или наборами строк.
 Библиотека marisa-trie обладает высокой производительностью и экономично использует память.p"""
print("Библиотека marisa-trie:")
import marisa_trie

# Создание экземпляра дерева префиксов
trie = marisa_trie.Trie(["apple", "banana", "orange", "app", "strawberry", "blueberry"])

# Проверка наличия элементов
print("apple" in trie)  # Вывод: True
print("pear" in trie)  # Вывод: False

# Получение значения элемента
print(trie["banana"])  # Вывод: 4
print(trie["app"])  # Вывод: 0
print(trie["orange"])  # Вывод: 1
print(trie["strawberry"])  # Вывод: 2
print(trie["apple"])  # Вывод: 3
print(trie["blueberry"])  # Вывод: 4

# Поиск всех элементов с заданным префиксом
prefixes = trie.items("app")
print(list(prefixes))  # Вывод: [('app', 0), ('apple', 3)]

# Автодополнение
suggestions = trie.keys("app")
print(list(suggestions))  # Вывод: ['app', 'apple']
