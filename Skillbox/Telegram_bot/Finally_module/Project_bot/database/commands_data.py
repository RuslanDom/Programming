import json
from typing import Dict
from Finally_module.Project_bot.models.models import FoundItems, db, UserHistory


def history_insert(user_id, message) -> None:
    """
    Функция записи истории в БД
    :param user_id: int
    :param message: str
    :return: None
    """
    with db:
        UserHistory.insert(user_id=int(user_id), user_history=message).execute()


def get_history(user_id) -> None:
    """
    Функция получения истории из БД
    :param user_id: int
    :return: None
    """
    data = UserHistory.select().where(UserHistory.user_id == int(user_id))
    return data.dicts()


def insert_data(user_id, get_result: Dict) -> None:
    """
    Функция записи результатов поиска в БД
    :param user_id: int
    :param get_result: dict[str]
    :return: None
    """
    with db:
        FoundItems.insert(user_id=int(user_id), result_data=json.dumps(get_result)).execute()


def get_data(user_id) -> Dict or bool:
    """
    Общая функция получения последних данных из БД
    :param user_id: int
    :return: dict[str] or bool
    """
    try:
        data = FoundItems.select().where(FoundItems.user_id == int(user_id))
        res = json.loads(data[-1].result_data)

        return res
    except:
        return False


def clear_search_data(user_id) -> None:
    """
    Функция очистки БД
    :param user_id: int
    :return: None
    """
    with db:
        print("База данных очищена")
        FoundItems.delete().where(FoundItems.user_id == int(user_id)).execute()


def clear_all_history() -> None:
    """
    Функция удаления истории пользователя
    :return: None
    """
    with db:
        UserHistory.delete().execute()
