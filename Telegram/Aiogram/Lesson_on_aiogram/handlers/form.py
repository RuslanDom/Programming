from aiogram.types import Message
from aiogram.fsm.context import FSMContext  # Отвечает за реализацию машины состояний
from Telegram.Aiogram.Lesson_on_aiogram.state.states_form import StepsForm
from aiogram import Bot


async def get_form(message: Message, state: FSMContext):
    await message.answer(f'Заполняем машину состояний.\nВведите своё имя: ')
    await state.set_state(StepsForm.name)


async def get_name(message: Message, state: FSMContext):
    await message.answer(f'Вы ввели: {message.text}\nТеперь введите вашу фамилию:')
    # Сохранение в машину состояний данных в виде словаря
    await state.update_data(name=message.text)
    # Назначение нового состояния пользователю
    await state.set_state(StepsForm.lastname)


async def get_lastname(message: Message, state: FSMContext):
    await message.answer(f'Вы ввели фамилию: {message.text}\nТеперь введите ваш возраст:')
    await state.update_data(lastname=message.text)
    await state.set_state(StepsForm.age)


async def get_age(message: Message, state: FSMContext, bot: Bot):
    await message.answer(f'Ваш возраст {message.text} сохранён')
    await state.update_data(age=message.text)
    # Все данные машины состояний сохранили в переменной context_data, через get получаем по ключу
    context_data = await state.get_data()
    await bot.send_message(message.from_user.id, text=f"Ваши данные:\nИмя: {context_data.get('name')}\n"
                                                      f"Фамилия: {context_data.get('lastname')}\n"
                                                      f"Возраст: {context_data.get('age')}")

    # Очистка машины состояний
    await state.clear()











