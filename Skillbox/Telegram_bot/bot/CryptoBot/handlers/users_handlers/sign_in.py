from telebot.types import Message, CallbackQuery
from loader import bot
from keyboard.inline.sign_in_buttons import sign_in, registration
from models.users import User


@bot.message_handler(commands='sign_in')
def sign_and_registration(message: Message):
    bot.set_state(message.from_user.id, User.user_id, message.chat.id)
    bot.send_message(message.from_user.id, 'Войдите в систему', reply_markup=get_id(message))


@bot.message_handler(state=User.user_id)
def get_id(message: Message):
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['user_id'] = message.from_user.id
        bot.send_message(message.from_user.id, data['user_id'])
        bot.send_message(message.from_user.id, reply_markup=registration())


@bot.callback_query_handler(lambda callback: callback.data == 'sign')
def callback_sign(callback: CallbackQuery):
    bot.edit_message_reply_markup(callback.from_user.id, callback.message.message_id)
    bot.send_message(callback.from_user.id, 'Успешный вход')


@bot.callback_query_handler(lambda callback: callback.data == 'reg')
def callback_registration(callback: CallbackQuery):
    bot.edit_message_reply_markup(callback.from_user.id, callback.message.message_id)
    with bot.retrieve_data(callback.from_user.id, callback.message.chat.id) as data:
        data['username'] = callback.from_user.username
        data['firstname'] = callback.from_user.first_name
        data['lastname'] = callback.from_user.last_name
    bot.set_state(callback.from_user.id, User.wallet, callback.message.chat.id)
    bot.send_message(callback.from_user.id, "Введите номер своего кошелька:\n")


# Получение кошелька и запись номера телефона
@bot.message_handler(state=User.wallet)
def get_wallet(message: Message):
    bot.send_message(message.from_user.id, "Кошелёк сохранён")

    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['wallet'] = str(message.text)
        data["phone_number"] = message.contact.phone_number













