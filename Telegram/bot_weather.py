import telebot
import requests
import json

bot = telebot.TeleBot('6810749735:AAHNXFI4x1tBk_IQa7UJJrjCO8swfD1zl7A')
API = 'e93d99bb6863b1a797d261f54cccb745'
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет. В каком городе хочешь узнать погоду?')

@bot.message_handler(content_types=['text'])


def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:

        data = json.loads(res.text)
        temp = data["main"]["temp"]
        bot.reply_to(message, f'В {city}  сейчас температура: {temp} скорость ветра: {data["wind"]["speed"]}')
        image = 'pushin_hot_weather.png' if temp > 15.0 else 'pushin_cold_weather.png'
        file = open('temp/image/' + image, 'rb')
        bot.send_photo(message.chat.id, file)
    else:
        bot.reply_to(message, "Такого города не существует!")



bot.polling(none_stop=True)