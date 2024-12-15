import telebot
from telebot.types import Message, CallbackQuery


bot = telebot.TeleBot("7481064908:AAHWXW91OY4LAW7gP3MpsynXs6k_2DcfoOs")  # Токен, полученный от BotFather


def generator_inline_markups():
    keyboard = telebot.types.InlineKeyboardMarkup(row_width=2)
    button_1 = telebot.types.InlineKeyboardButton('green', callback_data='green')
    button_2 = telebot.types.InlineKeyboardButton('red', callback_data='red')
    keyboard.add(button_1, button_2)
    return keyboard


def gen_reply_markup():
    # Создаём объекты кнопок
    button_1 = telebot.types.KeyboardButton(text='Собака')
    button_2 = telebot.types.KeyboardButton(text='Кошка')

    # Создаём объект клавиатуры
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    # Добавляем кнопки
    keyboard.add(button_1, button_2)
    return keyboard


@bot.message_handler(commands=['start'])
def send_welcome(message: Message):
    bot.send_message(message.from_user.id,
                     'Привет, друг!\nКакое животное есть у тебя?',
                     reply_markup=gen_reply_markup()  # Отправили клавиатуру
                     )


@bot.message_handler(func=lambda message: message.text == 'Собака')
def answer_dog(message: Message):
    bot.send_message(message.from_user.id,
                     "У меня тоже есть собака!",
                     reply_markup=telebot.types.ReplyKeyboardRemove()  # Удаляем клавиатуру
                     )


@bot.message_handler(func=lambda message: message.text == 'Кошка')
def answer_cat(message: Message):
    bot.send_message(message.from_user.id,
                     'У меня тоже есть кот',
                     reply_markup=telebot.types.ReplyKeyboardRemove()
                     )


@bot.message_handler(commands=["color"])
def colors(message: Message):
    bot.send_message(message.from_user.id, "Выберите цвет", reply_markup=generator_inline_markups())


@bot.callback_query_handler(func=lambda callback_query: callback_query.data == 'green')
def green(callback_query: CallbackQuery):
    bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id)
    bot.send_message(callback_query.from_user.id, "Вы выбрали зелёный")


@bot.callback_query_handler(func=lambda callback_query: callback_query.data == 'red')
def red(callback_query: CallbackQuery):
    bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id)
    bot.send_message(callback_query.from_user.id, "Вы выбрали красный")


@bot.message_handler(commands=["help"])
def inf0_help(message: Message):
    text = (
        '/start - приветствие',
        '/color - выбор цвета',
        '/help - команды'
    )
    bot.send_message(message.from_user.id, '\n'.join(text))
# функция ЭХОБОТА (отвечает на любое сообщение тем же текстом сообщения)
# @bot.message_handler(func=lambda message: True)
# def echo_all(message: Message):
#     bot.reply_to(message, message.text)


if __name__ == "__main__":
    bot.infinity_polling()
