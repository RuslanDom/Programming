from typing import Dict, Optional
from fastapi import FastAPI
from fastapi.params import Query, Path

app = FastAPI()


@app.get("/")
async def hello_async() -> Dict[str, str]:
    return {"msg": "Hello Buddy!"}

@app.get("/name/{who}")
async def hello_who_is_this(
                            who: int = Path(
                                    ...,
                                    title="Name for message",
                                    ge=0,
                                    le=5
                                    ),
                            msg: Optional[str] = Query(
                                None,
                                title="Message title",
                                regex="^[a-z0-9]+$"
                                )
                            ) -> Dict[str, str]:

    fake_user_db = {1: "admin", 2: "Ruslan"} # Словарь со значениями
    user = fake_user_db.get(who, 'DEFAULT VALUE') # Получение значения через get (если ключа нет получим дефолтное значение)
    return {"log": f'{msg}, {user}'}

# ЗАПУСК:  uvicorn src:app --reload

