import asyncio
import os
import loguru, sys
from apigram import ApigramApp
from broker import BrokerBybit
from dotenv import load_dotenv

from broker import PumpsScreener
from broker import HIOrdersScreener
from database import User, DataBase, UserHandler, UserSchema, UserSchemaGet
from celery_app import CeleryApp


# ❌✅

load_dotenv()



logger = loguru.logger
logger.remove()
custom_format = (
    "🕒<green>{time: DD-MM-YYYY HH:mm:ss}</green> | "
    "📊<level>{level: <8}</level> | "
    "🗂️<cyan>{name}</cyan> - "
    "💬<level>{message}</level>"
)

logger.add(sys.stderr, format=custom_format, colorize=True)
TOKEN = os.getenv("BOT_TOKEN")


# app = Apigram(bot_token=TOKEN, chat_id="123456")
logger.info(TOKEN)

# app_celery = CeleryApp().get_celery_app()
#
# @app_celery.on_after_configure.connect
# def setup_period(sender, **kwargs):
#     sender.add_periodic_task(5, start_app.s())
#
#
# @app_celery.task
# def start_app():
#     broker = BrokerBybit()
#     broker.get_symbol_current_price()
#     broker.get_last_klines()


# №1 celery -A main worker --pool=solo (дополнительно можно использовать -E эвенты и -l "info" логгирование)
# №2 celery -A main beat



async def main():
    # ✅
    # await DataBase.create_db()

    user_handler = UserHandler()

    # ✅
    # rec = await user_handler.add_user(
    #     username="asDDD",
    #     password="123",
    #     chat_id="1dswsb",
    #     email="rrr@df.vf"
    # )
    # logger.info(f"RESULT: {rec.username}")

    # ✅
    # r = await user_handler.get_all_users()
    # result_with_pydantic = [UserSchemaGet.model_validate(user, from_attributes=True) for user in r]
    # print(result_with_pydantic)


    # ✅
    # a = await user_handler.get_user(
    #     username="DDD",
    #     password="123"
    # )
    # print("RESPONSE:\n{}\n{}\n{}\n{}\n{}".format(a.username, a.password, a.chat_id, a.id, a.email))

    # ✅
    # a = await user_handler.set_user(
    #     email="dfsfs@fvd",
    #     id=2
    # )
    # if a:
    #     print(a.username)
    #     print(a.password)
    #     print(a.email)
    #     print(a.status)

    # ✅
    # a = await user_handler.delete_user(id=1)

    # ✅
    # a = await user_handler.set_status_user(id=2, status=False)
    # print(a.status)

    # ✅
    data = {
        "username": "Kit",
        "password": "333",
        "email": "re@ds.com",
        "chat_id":"238832"
    }
    validated_data = UserSchema(**data)
    user = validated_data.model_dump()
    resp = await user_handler.add_user(**user)
    print(UserSchemaGet.model_validate(resp, from_attributes=True))


if __name__ == '__main__':
    h = HIOrdersScreener()
    b = BrokerBybit()
    p = PumpsScreener()
    asyncio.run(main())
    # p.run()
    # p.get_symbol_current_price()
    # print(p.get_all_symbols_name())

    # b.get_last_klines()
    # print(h.get_hi_order(limit=3))