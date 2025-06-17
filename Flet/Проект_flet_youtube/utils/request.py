import requests
import os
from dotenv import load_dotenv
load_dotenv()

url = "https://api.telegram.org/bot"
def get_update(token):
    result = requests.get(f"{url}{token}/getUpdates").json()
    print(result)

get_update("7588767494:AAGcaYbJ11W_JGntkDjbuHTSE3Mdcspklog")