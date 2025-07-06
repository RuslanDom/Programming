import redis

LOCAL_HOST = "localhost"
LOCAL_PORT = 6379

with redis.Redis(LOCAL_HOST, LOCAL_PORT) as client:
    while True:
        problem = client.brpop("problems")[1].decode("utf-8")
        answer = eval(problem)

        client.lpush("answers", answer)
