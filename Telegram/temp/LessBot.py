import telebot
import webbrowser
from telebot import types

# Загружаем токен бота
bot = telebot.TeleBot('6854171945:AAFMTrTIc7jHzo7G5JDv1-FYiX0HmKdMfKc')



# Декоратор для функции @
# Обработка команды start  и любых других
@bot.message_handler(commands=['start'])

# Функция принимает параметр который будет хранить всю информацию про пользователя который работает с ботом
def main(message):
    # .send_message отправка ботом сообщений 1ый параметр ID чата с пользователем 2ой текст
    bot.send_message(message.chat.id, 'Привет, я Куки и я хочу пиццу с сыром. А что хочешь ты?')


@bot.message_handler(commands=['go'])
def go(message):
    # Создание кнопок у поля ввода текста
    markUp = types.ReplyKeyboardMarkup()
    but_1 = types.KeyboardButton('Поиграем?')
    but_2 = types.KeyboardButton('Поучим английский?')
    markUp.add(but_1, but_2)
    bot.send_message(message.chat.id, 'Что будем делать?', reply_markup=markUp)


    # Регистрируем полученный ответ с кнопки
    bot.register_next_step_handler(message, func_1)


# ССЫЛКА НА САЙТ МУЗЫКИ
@bot.message_handler(commands=['musik'])
def muzofond(message):
    bot.send_message(message.chat.id, 'Послушаем музыку 🎧')
    file2 = open('Telegram/temp/image/disc-cat.png', 'rb')
    bot.send_photo(message.chat.id, file2)
    webbrowser.open('https://muzofond.fm/personal-music/playlists/458874')


# ФОТО!!!!!!!!!!!!! КАРТИНКИ!!!!!
@bot.message_handler(commands=['who'])
def func_2(message):

    # Отправим пользователям картинку ('rb' для чтения) ПИШЕМ ПОЛНЫЙ ПУТЬ!!!!
    file1 = open('Telegram/temp/image/animals-cat.png', 'rb')
    bot.send_photo(message.chat.id, file1)

def func_1(message):
    if message.text == 'Поиграем?':
        bot.send_message(message.chat.id, 'Может быть позже')
    elif message.text == 'Поучим английский?':
        bot.send_message(message.chat.id, 'Что то лень')
    bot.register_next_step_handler(message, func_1)



# Отслеживание получения файлов photo, video, audio
@bot.message_handler(content_types=['photo'])
def get_photo(message):
    # Создание кнопок и их расположение
    markUp = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton('США', url='https://ru.usembassy.gov/ru/visas-ru/')
    but_2 = types.InlineKeyboardButton('Канада', url='https://www.canada.ca/en/services/immigration-citizenship.html')
    but_3 = types.InlineKeyboardButton('Австралия', url='https://australia-vac.ru/posolstvo-avstralii-v-moskve/')
    but_4 = types.InlineKeyboardButton('Если хочешь можешь удалить своё фото', callback_data='delete')
    but_5 = types.InlineKeyboardButton('Изменить фото', callback_data='edit')

    # Добавление кнопок
    markUp.add(but_1)
    markUp.add(but_2, but_3)
    markUp.add(but_4, but_5)
    bot.reply_to(message, 'Какое красивое фото! В какую страну ты хотел(а) бы отправиться? ', reply_markup=markUp)

# Функция для обрабатывания callback_data='' delete_message удаляет сообщение edit_message_text изменит сообщение
@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    elif callback.data == 'edit':
        bot.edit_message_text('Это точно ты?', callback.message.chat.id, callback.message.message_id)

# Ссылка на сайты
@bot.message_handler(commands=['porn'])
def pornsite(message):
    webbrowser.open('https://www.xvideos.com/lang/russian')

@bot.message_handler(commands=['youtube'])
def youtubesite(message):
    webbrowser.open('https://www.youtube.com/')

@bot.message_handler(commands=['can'])
# parse_mode='html' можно работать с текстом в формате html
def main(message):
    bot.send_message(message.chat.id, 'Я умею многое, например играть в <em>"Угадай число"</em>', parse_mode='html')


@bot.message_handler(commands=['infouser'])
def main(message):
    bot.send_message(message.chat.id, message)




@bot.message_handler(commands=['hello', 'привет'])
def main(message):
    bot.send_message(message.chat.id, f'Ну привет, привет {message.from_user.first_name} {message.from_user.last_name}. Давай знакомиться, скинь мне своё фото;)')




# Обработка произвольного текста (не команд)
@bot.message_handler()
def info(message):
    if message.text.lower() == 'что ты умеешь':
        bot.send_message(message.chat.id, 'Я умею многое, например играть в <em>"Угадай число"</em>', parse_mode='html')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')
    elif message.text.lower() == 'возможности':
        bot.send_message(message.chat.id, 'Я умею многое, например играть в <em>"Угадай число"</em>', parse_mode='html')




# Команда для постоянной работы боты
bot.polling(none_stop=True)
# Тоже самое что и .polling()
# bot.infinity_polling()



