import requests


"""
Примеры запросов:

GET https://botapi.max.ru/messages/{messageId}?access_token={your_token} — получить сообщения
POST https://botapi.max.ru/messages?access_token={your_token} — отправить сообщения
PATCH https://botapi.max.ru/chats/{chatId}?access_token={your_token} — изменить информацию о чате
В ответ сервер вернёт JSON-объект с запрошенными данными или сообщение об ошибке, если что-то пойдёт не так
"""

class BOT_TOKEN():
    def __init__(self, bot_token):
        self.bot_token = bot_token


    def send_message(self, chat_id, message):
        url = f"https://botapi.max.ru/messages?"
        data = {
            "access_token": self.bot_token,
            "chat_id": chat_id,
            "message": message
        }
        message = requests.post(url=url, data=data).json()