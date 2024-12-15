from telebot.types import Message, CallbackQuery
from Bot_CatPush.keyboards.reply.animals import cat_dog
from Bot_CatPush.loader import bot


@bot.message_handler(commands=['pets'])
def my_pets(message: Message):
    bot.send_message(message.from_user.id, "Выберите вашего дружка.", reply_markup=cat_dog())


@bot.callback_query_handler(func=lambda callback_query: callback_query.data == 'cat')
def cat(callback_query: CallbackQuery):
    # Удаляем клавиатуру
    bot.edit_message_reply_markup(callback_query.from_user.id,
                                  callback_query.message.message_id)
    bot.send_message(callback_query.from_user.id, "Я тоже люблю кошек!")


@bot.callback_query_handler(func=lambda callback_query: callback_query.data == 'dog')
def dog(callback_query: CallbackQuery):
    bot.edit_message_reply_markup(callback_query.from_user.id,
                                  callback_query.message.message_id)
    bot.send_message(callback_query.from_user.id, "Собаки мои любимые животные!")




