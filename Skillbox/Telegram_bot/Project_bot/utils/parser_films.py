import json
from bs4 import BeautifulSoup
import requests
from Project_bot.config_data.config import API_KEY
from loguru import logger


def parser(year='2024', type_="movie", genres="комедия", countries="США") -> None:
    """
    Функция парсит сайт с фильмами с использованием lxml, а также библиотек requests и BeautifulSoup,
    собирает информацию название, альтернативное название, тип, год, рейтинг,
    страна производства, жанры, возрастное ограничение и ссылку на постер. Полученные данные сохраняются в JSON файле
    по адресу 'database\films.json'
    :param year: str - поле года выхода фильма
    :param type_: str - поле типа (фильм или сериал)
    :param genres: str - поле жанр
    :param countries: str - поле страны производства
    :return:
    """
    dict_with_films = {}
    url = f"https://api.kinopoisk.dev/v1.4/movie?year={year}&type={type_}&genres.name={genres}&countries.name={countries}"
    headers = {"X-API-KEY": API_KEY}
    response = requests.get(url=url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "lxml")
        data = json.loads(soup.text)
        for k, values in data.items():
            if k == "docs":
                for i_film in values:
                    dict_with_films[i_film["id"]] = {
                        "name": i_film["name"],
                        "alternativeName": i_film["alternativeName"],
                        "type": i_film["type"],
                        "year": str(i_film["year"]),
                        "rating": i_film["rating"],
                        "ageRating": i_film["ageRating"]
                    }

                    try:
                        dict_with_films[i_film["id"]].update(
                            {"poster": i_film["poster"]["url"]}
                        )
                    except KeyError:
                        dict_with_films[i_film["id"]].update({"poster": "null"})
                    try:
                        dict_with_films[i_film["id"]].update(
                            {"genres": [i_name["name"] for i_name in i_film["genres"]]}
                        )
                    except KeyError:
                        dict_with_films[i_film["id"]].update({"genres": "null"})
                    try:
                        dict_with_films[i_film["id"]].update(
                            {"countries": i_film["countries"][0]["name"]}
                        )
                    except KeyError:
                        dict_with_films[i_film["id"]].update({"countries": "null"})

        for k, film in data.items():
            logger.info(film)

        with open(r"database\films.json", "w", encoding="utf-8") as file:
            json.dump(dict_with_films, file, indent=4, ensure_ascii=False)

    else:
        pass

