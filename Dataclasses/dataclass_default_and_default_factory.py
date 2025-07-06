from dataclasses import dataclass, field

"""Использование аргумента default.
Этот параметр задает значение по умолчанию для атрибута, если при создании объекта значение не задано.Подобно параметрам в функции, поля
со значением по умолчанию должны следовать за любыми полями без значения по умолчанию."""

@dataclass
class Article:
    title: str
    language: str = field(default='Python3')

article = Article("User Types")
print(article)
# Article(title='User Types', language='Python3')

"""Использование аргумента default_factory.
Аргумент default_factory должен быть вызываемый объект без аргументов и будет вызываться, когда для этого
поля потребуется значение по умолчанию.  Возвращаемое значение будет установлено как значение
по умолчанию для атрибута при создании объекта.Ошибочно указывать и default и default_factory
одновременно.Необходимо предоставить либо вызываемый объект фабричной
функции default_factory, либо предоставить значение default для атрибута."""

from random import choice


def get_language():
    languages = ['Python3', 'Java', "C++", "C#", "Javascript", "Go", "Kotlin", "PHP"]
    return choice(languages)


@dataclass
class Article:
    title: str
    language: str = field(default_factory=get_language)

article_1 = Article("User Types")
print(article_1)
# Article(title='User Types', language='Java')
