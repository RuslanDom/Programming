from celery import group, chain
from tasks import *

t1 = buy_milk.s(5)
t2 = buy_bread.s(3)
task_group = group(t1, t2)
result = task_group.apply_async()
print(result.get())  # ['Купил 5 литр(ов) молока', 'Купил 3 булку(ок) хлеба']

t3 = fetch_name.s(1)
t4 = greeting_user.s()

task_chain = chain(t3 | t4)
result_chain = task_chain.apply_async()
print(result_chain.get())  # Здравствуй, Пётр 1Первый!

