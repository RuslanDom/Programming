from telebot import TeleBot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import Message, CallbackQuery
from telebot.handler_backends import State, StatesGroup
from telebot.custom_filters import StateFilter

bot = TeleBot("7481064908:AAHWXW91OY4LAW7gP3MpsynXs6k_2DcfoOs")  # Токен, полученный от BotFather


# Состояние для диалога
class KeyboardState(StatesGroup):
    buttons_count = State()
    keyboard_text_and_callback = State()
    send_keyboard = State()


def generator_markup(buttons_info):
    # Создаём объект клавиатуры
    keyboard = InlineKeyboardMarkup()

    for text_keyboard, callback_keyboard in buttons_info.items():
        # Создаём объект кнопки и добавляем его к клавиатуре
        button = InlineKeyboardButton(text=text_keyboard,
                                      callback_data=callback_keyboard)
        keyboard.add(button)
    return keyboard


@bot.message_handler(commands=['create_markup'])
def handle_start_message(message: Message):
    # Присваиваем состояние
    bot.set_state(message.from_user.id, KeyboardState.buttons_count, message.chat.id)
    bot.send_message(message.from_user.id,
                     "Привет! Я помогу тебе сформировать инлайн-клавиатуру\n"
                     "Введи количество кнопок для будущей клавиатуры")


# Ловим его в одном из нескольких handlers
@bot.message_handler(state=KeyboardState.buttons_count)
def handle_buttons_count(message: Message):
    if message.text.isdigit():
        bot.set_state(message.from_user.id,
                      KeyboardState.keyboard_text_and_callback,
                      message.chat.id)

        with bot.retrieve_data(message.from_user.id) as data:
            # Сохраняем информацию и делаем заготовки объектов, который нужны для нашего сценария
            data['buttons_count'] = int(message.text)
            data['buttons'] = {}
            data['temp_keyboard_data'] = []

        bot.send_message(message.from_user.id,
                         "Теперь введите текст для кнопки")
    else:
        bot.send_message(message.from_user.id, "Только числовые значения")


@bot.message_handler(state=KeyboardState.keyboard_text_and_callback)
def handle_keyboard_text_and_callback(message: Message):
    # Удерживаем пользователя в этом состоянии, пока не получим всё, что нужно.
    with bot.retrieve_data(message.from_user.id) as data:
        temp_keyboard_data = data['temp_keyboard_data']

        if not temp_keyboard_data:
            temp_keyboard_data.append(message.text)
            bot.send_message(message.from_user.id,
                             f"Укажи callback для кнопки {message.text}")
        elif len(temp_keyboard_data) == 1:
            temp_keyboard_data.append(message.text)

            key, value = temp_keyboard_data
            data["buttons"][key] = value
            temp_keyboard_data.clear()
            data["buttons_count"] -= 1

            if data["buttons_count"]:
                bot.send_message(message.from_user.id,
                                 "Данные сохранены! Введи  текст для следующей кнопки")

            else:
                bot.set_state(message.from_user.id, KeyboardState.send_keyboard)
                bot.send_message(
                    message.from_user.id,
                    "Кнопки, которые ты хотел создать",
                    reply_markup=generator_markup(data["buttons"])
                )


# В callback_query_handler ловим состояние.
# Так как нам не нужен дополнительный фильтр, указываем функцию как None.
@bot.callback_query_handler(func=None, state=KeyboardState.send_keyboard)
def handle_buttons(callback_query: CallbackQuery):
    with bot.retrieve_data(callback_query.from_user.id) as data:
        pressed_button_name = None
        for key, value in data["buttons"].items():
            if callback_query.data == value:
                bot.answer_callback_query(callback_query.id,
                                          f'Поймал нажати на кнопку {key}',
                                          show_alert=True)

        data["buttons"].pop(pressed_button_name, None)
        bot.edit_message_reply_markup(
            callback_query.from_user.id,
            callback_query.message.message_id,
            reply_markup=generator_markup(data["buttons"])
        )
    if not data['buttons']:
        bot.send_message(callback_query.from_user.id, "Все кнопки были нажаты")
        bot.delete_state(callback_query.from_user.id)


# Перед запуском бота подключаем фильтр состояний.
bot.add_custom_filter(StateFilter(bot))
bot.infinity_polling()









































