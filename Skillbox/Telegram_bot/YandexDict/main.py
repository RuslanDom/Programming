import json
import telebot
from telebot.types import Message
from telebot import custom_filters
from telebot.storage import StateMemoryStorage

import api
from config import BOT_TOKEN, DEFAULT_LANG
from states import States


state_storage = StateMemoryStorage()
bot = telebot.TeleBot(BOT_TOKEN, state_storage=state_storage)

all_langs = api.get_langs()


@bot.message_handler(commands=['start'])
def start(message: Message) -> None:
    bot.send_message(message.from_user.id, f'Добро пожаловать в бот переводчик\n'
                                           f'/lang Выбрать языки лоя перевода - [{DEFAULT_LANG}]'
                                           f'/go Перевести слово или текст')
    bot.set_state(message.from_user.id, States.base, message.chat.id)


@bot.message_handler(commands=['lang'])
def get_lang(message: Message) -> None:
    list_with_langs = ','.join(all_langs)
    bot.send_message(message.from_user.id, f'Выберите доступную пару языков:\n{list_with_langs}')
    bot.set_state(message.from_user.id, States.lang, message.chat.id)


@bot.message_handler(state=States.lang)
def set_lang(message: Message):
    chosen_lang = message.text
    if chosen_lang not in all_langs:
        bot.send_message(message.from_user.id, "Такой пары языков для перевода нет")
        return

    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['lang'] = message.text

    bot.send_message(message.from_user.id, 'Для перевода команда - /go')
    bot.set_state(message.from_user.id, States.base, message.chat.id)


@bot.message_handler(commands=['go'])
def translate(message: Message) -> None:
    bot.send_message(message.from_user.id, 'Введите слово или текст для перевода:\n')
    bot.set_state(message.from_user.id, States.lookup, message.chat.id)


@bot.message_handler(state=States.lookup)
def lookup(message: Message):
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        result = api.lookup(lang=data.get('lang', DEFAULT_LANG), text=message.text)
        json_row = json.dumps(result, ensure_ascii=False, indent=2)
        bot.send_message(message.from_user.id, f'<pre>{json_row}</pre>', parse_mode="html")
    bot.send_message(message.from_user.id, "Введите слово или текст для перевода:\n")


if __name__ == '__main__':
    bot.add_custom_filter(custom_filters.StateFilter(bot))
    bot.set_my_commands([
        telebot.types.BotCommand('lang', "Выбор направления языка"),
        telebot.types.BotCommand('go', "Перевод слова или фразы")
    ])
    bot.polling()











