from typing import Dict


def set_string(v: Dict) -> str:
    """
    Функция форматирования ответа результатов поиска
    :param v: Dict[str]
    :return: str
    """
    response = (
        f"Название: {v['name']} (альтернативное: {v['alternativeName']})\n"
        f"Год производства: {str(v['year'])}\nРейтинг:\n\tKP: {v['rating']['kp']}\n\t"
        f"IMDB: {v['rating']['imdb']}\n\tFilmsCritics: {v['rating']['filmCritics']}\n"
        f"Страна производства: {v['countries']}\nЖанр: {v['genres']}\n"
        f"{v['poster']}"
    )
    return response
