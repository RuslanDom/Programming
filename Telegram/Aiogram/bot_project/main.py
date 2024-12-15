import asyncio
from loader import bot_job

if __name__ == "__main__":
    try:
        asyncio.run(bot_job())
    except KeyboardInterrupt:
        print('FINISH')
