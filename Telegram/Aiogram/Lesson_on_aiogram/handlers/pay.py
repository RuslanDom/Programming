from aiogram import Bot
from aiogram.types import Message, LabeledPrice, PreCheckoutQuery, ShippingOption, ShippingQuery
from Telegram.Aiogram.Lesson_on_aiogram.config import SBER_TOKEN, U_KASSA
from aiogram.utils.keyboard import InlineKeyboardBuilder


# LabeledPrice - объект с помощью которого можно формировать цену на наш продукт


def get_keyboard():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(
        text='Оплатить',
        pay=True
    )
    keyboard.button(
        text='link',
        url='https://i.pinimg.com/736x/e6/98/bc/e698bc2a2c851be5138472f4da775290.jpg'
    )


RU_SHIPPING = ShippingOption(
    id='ru',
    title='Доставка по России',
    prices=[
        LabeledPrice(
            label="Доставка Почтой России",
            amount=20000
        )
    ]
)

BY_SHIPPING = ShippingOption(
    id='by',
    title='Доставка Белпочтой',
    prices=[
        LabeledPrice(
            label='Доставка в Беларусь',
            amount=50000
        )
    ]
)


async def shipping_check(query: ShippingQuery, bot: Bot):
    shipping_options = []
    countries = ['BY', 'RU']
    if query.shipping_address.country_code not in countries:
        return await bot.answer_shipping_query(query.id, ok=False, error_message='В эту страну доставки нет')
    if query.shipping_address.country_code == 'BY':
        shipping_options.append(BY_SHIPPING)
    if query.shipping_address.country_code == 'RU':
        shipping_options.append(RU_SHIPPING)

    await bot.answer_shipping_query(shipping_query_id=query.id, ok=True, shipping_options=shipping_options)



async def order_cat(message: Message, bot: Bot):
    print(U_KASSA)
    await bot.send_invoice(
        chat_id=message.chat.id,  # Чат куда отправлять счёт за оплату
        title='Котик программист',
        description='Купи себе котика с мяу-буком. Ограниченная коллекция.',
        payload='Используется для внутренних целей пользователь её не видит',
        provider_token=U_KASSA,
        currency='rub',
        prices=[
            LabeledPrice(
                label='Цена',
                amount=90000
            ),
            LabeledPrice(
                label='НДС',
                amount=15000
            ),
            LabeledPrice(
                label='Скидка',
                amount=10000
            )
        ], max_tip_amount=500,  # Максимальная сумма чаевых
        suggested_tip_amounts=[100, 200, 300, 400],  # Список предлагаемых сумм для чаевых max 4 elements
        start_parameter=None,
        # поведение кнопки оплатить при переходе в другой чат, можно добавить ссылку нат бота
        provider_data=None,  # Если нужно отправить какие-нибудь данные передаваемые провайдером
        photo_url="https://i.pinimg.com/736x/e6/98/bc/e698bc2a2c851be5138472f4da775290.jpg",
        photo_size=100,
        photo_height=300,
        photo_width=300,
        need_name=True,  # Если нужно полное имя пользователя
        need_phone_number=True,
        need_email=False,
        need_shipping_address=False,  # Если нужен адрес для доставки продукта
        send_phone_number_to_provider=False,
        # Если платёжный провайдер просит вас отправить ему номер телефона пользователя
        send_email_to_provider=False,  # Если платежный провайдер требует передать ему email пользователя
        is_flexible=False,  # Если конечная цена зависит от способа доставки
        disable_notification=True,  # Сообщение будет доставлено без звука
        protect_content=False,  # Если нужно защитить от пересылки и копирования поста
        reply_to_message_id=None,  # Если нужно цитировать сообщение, нужно указать id
        allow_sending_without_reply=True,  # Отправить счёт на оплату даже если цитируемое сообщение не найдено
        reply_markup=None,
        request_timeout=10  # Тайм-аут запросы
    )


#  Отвечаем pre_checkout_query событие которое отправляет телеграм ok=True если готовы выслать продукт
async def pre_checkout_query(checkout_query: PreCheckoutQuery, bot: Bot):
    await bot.answer_pre_checkout_query(checkout_query.id, ok=True)


# Запускается в случае успешной оплаты продукта пользователем
async def success_pay(message: Message):
    text = (f'Спасибо за заказ {message.successful_payment.total_amount // 100}\n'
            f'Наш консультант сейчас с вами свяжется по телефону')
    await message.answer(text)


async def order_boxing_gloves(message: Message, bot: Bot):
    await bot.send_invoice(
        chat_id=message.chat.id,
        title='Боксерские перчатки',
        currency='rub',
        photo_url='https://cdn1.ozone.ru/s3/multimedia-p/6682562053.jpg',
        description='Перчатки размер 14oz, для детей и взрослых',
        photo_size=100,
        photo_width=300,
        photo_height=300,
        payload='Белые',
        provider_token=U_KASSA,
        prices=[
            LabeledPrice(
                label='Стоимость',
                amount=99000
            )],
        max_tip_amount=10000,
        suggested_tip_amounts=[1000, 3000, 5000, 10000],
        is_flexible=True,
        need_name=True,
        need_phone_number=False,
        need_email=False,
        need_shipping_address=True,
        protect_content=False,
        reply_markup=get_keyboard(),
        request_timeout=10
    )


async def pay_lot_1(message: Message, bot: Bot):
    await bot.send_invoice(
        chat_id=message.chat.id,
        title='lot1',
        description='--***---',
        payload='Nothing',
        provider_token=SBER_TOKEN,
        start_parameter=None,
        prices=(
            [LabeledPrice(
                label='Стоимость',
                amount=50000
            ),
            LabeledPrice(
                label='Скидка',
                amount=10000
            )]
        ),
        currency='rub',
        reply_to_message_id=False,
        is_flexible=False,
        max_tip_amount=50000,
        suggested_tip_amounts=[10000, 20000, 30000, 50000],
        photo_url='https://cs4.pikabu.ru/post_img/big/2015/01/14/1/1421189020_1885344578.jpg',
        photo_size=100,
        photo_height=300,
        photo_width=300,
        need_name=True,
        need_email=True,
        need_phone_number=False,
        need_shipping_address=False,
        send_email_to_provider=False,
        send_phone_number_to_provider=False,
        provider_data=None,
        reply_markup=None,
        disable_notification=False,
        request_timeout=12
    )


async def pre_checkout_query_for_lot(checkout_query: PreCheckoutQuery, bot: Bot):
    await bot.answer_pre_checkout_query(checkout_query.id, ok=True)


async def success_payment_lot1(message: Message):
    await message.answer(text=f'Оплата в размере {message.successful_payment.total_amount//100}'
                              f'{message.successful_payment.currency}] успешно прошла')




