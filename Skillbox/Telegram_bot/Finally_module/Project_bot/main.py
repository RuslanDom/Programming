import asyncio
from Skillbox.Telegram_bot.Finally_module.Project_bot.loader import run

if __name__ == "__main__":
    try:
        asyncio.run(run())
    except KeyboardInterrupt:
        print('THE END')
