import requests
from typing import Dict, List
from config import URL, API_KEY


def api_request(endpoint: str, params={}) -> requests.Response:
    params['key'] = API_KEY
    return requests.get(f"{URL}/{endpoint}", params=params)


def get_langs() -> List:
    response = api_request('getLangs')
    return response.json()


def lookup(lang, text, ui='ru') -> Dict:
    response = api_request('lookup', params={
        "lang": lang,
        "ui": ui,
        "text": text
    })
    return response.json()




