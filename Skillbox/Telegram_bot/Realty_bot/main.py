import asyncio

from Realty_bot.loader import run
from loguru import logger
import sys


logger.add(sink=sys.stdout, format="{time}{level}{message}", level="DEBUG")


if __name__ == "__main__":
    try:
        asyncio.run(run())
    except:
        print('Работа бота завершена')

