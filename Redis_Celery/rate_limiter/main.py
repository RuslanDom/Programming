from contextlib import asynccontextmanager
from functools import lru_cache

from redis.asyncio import Redis
from typing import Annotated

from config import Settings
from time import time
import random
from fastapi import FastAPI, Depends, HTTPException, Request, Body, status

"""
ОГРАНИЧИТЕЛЬ ЗАПРОСОВ КЛИЕНТОВ
"""

settings = Settings()

class RedisClient:
    def get_client(self):
        return Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT)

    def get_rate_limiter(self):
        return RateLimiter(self.get_client())


redis_client = RedisClient()

# @lru_cache
# def get_redis():
#     return Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT)
#
#
# @lru_cache
# def get_rate_limiter():
#     return RateLimiter(get_redis())

class RateLimiter:

    def __init__(self, redis: Redis):
        self._redis = redis


    async def is_limited(
            self,
            ip_address: str,
            endpoint: str,
            max_requests: int,
            delta_time_ms: int
    ) -> bool:
        key = f'rate_limiter:{endpoint}:{ip_address}'

        current_time = time() * 1000  # Текущее время
        time_start = current_time - delta_time_ms * 1000  # Начало окошка времени
        current_request = f'{time() * 1000}-{random.randint(0, 100000)}'  # Текущий запрос


        async with self._redis.pipeline() as pipe:
            # Очистить память до начала окошка запросов
            await pipe.zremrangebyscore(key, 0, time_start)
            # Получить кол-во запросов в окошке(длинна списка запросов-словарей по ключу rate_limiter)
            await pipe.zcard(key)
            # Добавить новый запрос по ключу rate_limiter
            await pipe.zadd(key, {current_request: current_time})
            # Очистка окошка запросов через delta_time_ms (5 сек), чтобы запросы не хранились вечно в памяти
            await pipe.expire(key, delta_time_ms)
            # Выполнить транзакцию
            result = await pipe.execute()

        # Получение результата выполненной транзакции
        _, current_count, _, _ = result

        # Если код-во запросов превысило max_requests, больше нельзя поместить в окошко запрос
        return current_count >= max_requests



@asynccontextmanager
async def lifespan(app: FastAPI):
    redis = redis_client.get_client()
    # redis = get_redis()
    await redis.ping()
    print("Redis is work!")
    yield
    await redis.aclose()
    print("Redis closed!")

app = FastAPI(lifespan=lifespan) # lifespan - жизненный цикл FastApi


# Фабрика зависимостей
def rate_limiter_factory(
        endpoint: str,
        max_requests: int,
        delta_time_ms: int,
):
    async def dependency(
            request: Request,
            rate_limiter: Annotated[RateLimiter, Depends(redis_client.get_rate_limiter)]
            # rate_limiter: Annotated[RateLimiter, Depends(get_rate_limiter)]
    ):
        ip_address = request.client.host
        limited = await rate_limiter.is_limited(
            ip_address,
            endpoint,
            max_requests,
            delta_time_ms
        )

        if limited:
            raise HTTPException(
                status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                detail="Too many requests, try again later"
            )
    return dependency


rate_limiter_sql = rate_limiter_factory(
    endpoint='sql_code',
    max_requests=5,
    delta_time_ms=5
)

rate_limiter_python = rate_limiter_factory(
    endpoint='python_code',
    max_requests=3,
    delta_time_ms=10
)

@app.post("/sql_code", dependencies=[Depends(rate_limiter_sql)])
async def send_sql_code(code: str = Body(embed=True)): # embed=True - принимать не просто str, а json

    ...
    return {"ok": True}


@app.post("/python_code", dependencies=[Depends(rate_limiter_python)])
async def send_python_code(code: str = Body(embed=True)): # embed=True - принимать не просто str, а json

    ...
    return {"ok": True}





