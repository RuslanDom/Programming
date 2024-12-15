import json
from bs4 import BeautifulSoup
import requests
from Finally_module.Project_bot.config_data.config import API_KEY
from typing import Dict


def parser(url) -> Dict:
    """
    Функция парсит сайт с фильмами с использованием lxml, а также библиотек requests и BeautifulSoup,
    собирает информацию название, альтернативное название, тип, год, рейтинг,
    страна производства, жанры, возрастное ограничение и ссылку на постер.

    :return: Dict
    """
    dict_with_films = {}
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

        return dict_with_films
    else:
        pass

