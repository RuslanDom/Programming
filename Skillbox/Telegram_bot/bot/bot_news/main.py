import asyncio
from bot.bot_news.loader import run


if __name__ == '__main__':
    try:
        asyncio.run(run())
    except KeyboardInterrupt:
        print('THE END')
