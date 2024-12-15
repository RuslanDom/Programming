import os.path
import json
from aiogram import Router
from aiogram.utils.markdown import hbold, hlink
from aiogram.filters import Command
from aiogram.types import Message
import datetime


router = Router()
path = os.path.join(r'..\bot_news\utils')


@router.message(Command(commands='all_news'))
async def get_all_news(message: Message):
    with open(path+r'\news_dict.json', encoding='utf-8') as file:
        news_dict = json.load(file)
    for key, values in sorted(news_dict.items()):
        news = (f'{hbold(datetime.datetime.fromtimestamp(values['datetime']))}\n'
                f'{hlink(title=values["title"], url=values["link"])}')
        await message.answer(news)


@router.message(Command(commands='fresh'))
async def fresh_news(message: Message):
    with open(path+r'\update_list.json', encoding='utf-8') as file:
        news_dict = json.load(file)
    for key, values in sorted(news_dict.items())[-3:]:
        news = (f'{hbold(datetime.datetime.fromtimestamp(values['datetime']))}\n'
                f'{hlink(title=values["title"], url=values["link"])}')
        await message.answer(news)


