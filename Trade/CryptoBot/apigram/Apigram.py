import requests
from requests import Response


class ApigramApp:
    def __init__(self, bot_token: str, chat_id:str) -> None:
        self.__BOT_TOKEN = bot_token
        self.__chat_id = chat_id
        self.__URL = "https://api.telegram.org/bot"

    def send_message(self, message: str) -> Response:
        final_url = self.__URL + self.__BOT_TOKEN + "/sendMessage?chat_id={}&text={}".format(str(self.__chat_id), str(message))
        resp = requests.post(final_url)
        return resp

