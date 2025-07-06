import redis

LOCAL_HOST = "localhost"
LOCAL_PORT = 6379

with redis.Redis(LOCAL_HOST, LOCAL_PORT) as client:
    while True:
        problem = input(":::")
        client.lpush("problems", problem)

        answer = client.brpop("answers")[1].decode("utf-8")
        print("Answer: {}".format(answer))