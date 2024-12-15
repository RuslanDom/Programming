from Bot_CatPush.keyboards.reply.contact import request_contact
from Bot_CatPush.loader import bot
from Bot_CatPush.states.contact_information import UserInfoState
from telebot.types import Message


@bot.message_handler(commands=['survey'])
def survey(message: Message) -> None:
    bot.set_state(message.from_user.id, UserInfoState.name, message.chat.id)
    bot.send_message(message.from_user.id, f'Привет, {message.from_user.username} введи своё имя:')


@bot.message_handler(state=UserInfoState.name)
def get_name(message: Message) -> None:
    if message.text.isalpha():
        bot.send_message(message.from_user.id, "Спасибо, записал. Введи свой возраст:")
        bot.set_state(message.from_user.id, UserInfoState.age, message.chat.id)

        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['name'] = message.text

    else:
        bot.send_message(message.from_user.id, 'Имя может содержать только буквы!')


@bot.message_handler(state=UserInfoState.age)
def get_age(message: Message) -> None:
    if message.text.isdigit() and 1 < int(message.text) < 99:
        bot.send_message(message.from_user.id, "Возраст успешно сохранён! Введите страну проживания:")
        bot.set_state(message.from_user.id, UserInfoState.country, message.chat.id)

        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['age'] = message.text

    else:
        bot.send_message(message.from_user.id, "Возраст содержит только цифры от 1 до 99")


@bot.message_handler(state=UserInfoState.country)
def get_country(message: Message) -> None:
    if message.text.isalpha():
        bot.send_message(message.from_user.id, "Страна сохранена. Укажите город:")
        bot.set_state(message.from_user.id, UserInfoState.city, message.chat.id)

        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['country'] = message.text.capitalize()

    else:
        bot.send_message(message.from_user.id, "В название страны используйте буквы")


@bot.message_handler(state=UserInfoState.city)
def get_city(message: Message) -> None:
    if message.text.isalpha():
        bot.send_message(message.from_user.id,
                         'Город успешно добавлен. Отправь свой номер телефона, нажав на кнопку!',
                         reply_markup=request_contact())
        bot.set_state(message.from_user.id, UserInfoState.phone_number, message.chat.id)

        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data["city"] = message.text.capitalize()

    else:
        bot.send_message(message.from_user.id, "Название города может содержать только буквы!")


@bot.message_handler(content_types=['text', 'contact'], state=UserInfoState.phone_number)
def get_phone_number(message: Message) -> None:
    if message.content_type == 'contact':
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data["phone_number"] = message.contact.phone_number
            text = (f'Спасибо за предоставленную информацию\n'
                    f'Ваши данные:\n'
                    f'\tИмя: {data['name']}\t'
                    f'\tВозраст: {data['age']}\n'
                    f'\tСтрана: {data['country']}\t'
                    f'\tГород: {data['city']}\n'
                    f'\tНомер телефона: {data['phone_number']}\n')
            bot.send_message(message.from_user.id, text)
    else:
        bot.send_message(message.from_user.id, "Чтобы отправить контакт нажмите на кнопку!")