from typing import Dict
from Skillbox.Telegram_bot.Finally_module.Project_bot.utils.parser_films import parser


def search(query) -> Dict:
    """
    Поиск через API по названию
    :param query: str
    :return: Dict
    """
    url = f"https://api.kinopoisk.dev/v1.4/movie/search?query={query}"
    return parser(url=url)





