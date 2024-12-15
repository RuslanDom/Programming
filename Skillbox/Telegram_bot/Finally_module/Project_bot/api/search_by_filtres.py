from typing import Dict
from Finally_module.Project_bot.utils.parser_films import parser


def get_search_by_filter(year='2024', type_="movie", genres="комедия", countries="США") -> Dict:
    """
    :param year: str - поле года выхода фильма
    :param type_: str - поле типа (фильм или сериал)
    :param genres: str - поле жанр
    :param countries: str - поле страны производства
    :return: Dict
    """

    url = f"https://api.kinopoisk.dev/v1.4/movie?year={year}&type={type_}&genres.name={genres}&countries.name={countries}"
    return parser(url=url)

