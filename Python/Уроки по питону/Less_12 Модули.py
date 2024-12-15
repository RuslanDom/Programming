# Модули

import datetime as dt,sys, os, platform

print(dt.datetime.now())
print(dt.datetime.now().time())

print(sys.platform)
print(platform.system())

from math import sqrt as sq, log

print(log(8,2))
print(sq(49))

import My_module as my

res = my.delenie(10,5)
print(res)




