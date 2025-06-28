import requests
from dotenv import load_dotenv

load_dotenv()

url = "https://api.telegram.org/bot"

def sendMessage(token, channel, text):
    try:
        return requests.post(
            url=f"{url}{token}/sendMessage",
            data={
                'chat_id': channel,
                'text': text,
                'parse_mode': 'HTML'
            }
        ).json()
    except Exception as e:
        return e

def sendMessagePhoto(token, channel, photo, caption):
    try:
        data = {"chat_id": channel, "caption": caption}
        link = f"{url}{token}/sendPhoto?chat_id={channel}"
        with open(photo, "rb") as image_file:
            result = requests.post(url=link, data=data, files={"photo": image_file})
        return result.json()
    except Exception as e:
        return e

# "7588767494:AAGcaYbJ11W_JGntkDjbuHTSE3Mdcspklog"











