def count_unique_characters(origin_text: str) -> int:
    # Приводим текст к нижнему регистру и удаляем из текста пробелы
    text = origin_text.lower().replace(' ', '')
    # Создаём словарь для хранения символов
    dict_of_letters = dict()
    # Добавляем в словарь символы в виде ключа, а в значение помещаем число их повторений в тексте
    for i_letter in text:
        dict_of_letters[i_letter] = dict_of_letters.setdefault(i_letter, 0) + 1
    # Используем фильтр для получения списка символов которые повторялись лишь единожды
    # Длинна этого списка и есть кол-во не повторяющихся символов
    return len(list(filter(lambda letter: dict_of_letters[letter] == 1, dict_of_letters)))


# Пример использования:
message = "Today is a beautiful day! The sun is shining and the birds are singing."

unique_count = count_unique_characters(message)
print("Количество уникальных символов в строке:", unique_count)