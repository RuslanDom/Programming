



def simple_generator():
    yield 'Something'


print(type(simple_generator)) # <class 'function'>
print(type(simple_generator())) # <class 'generator'>
g = simple_generator()
print(g.__iter__()) # <generator object simple_generator at 0x0000024B685E0250>
print(g.__next__()) # Something
# print(g.__next__()) # Traceback: StopIteration


import inspect

def get_states():
    for i in range(3):
        yield i


new_g = get_states()
print(inspect.getgeneratorstate(new_g)) # GEN_CREATED
next(new_g)
print(inspect.getgeneratorstate(new_g)) # GEN_SUSPENDED
next(new_g)
next(new_g)
try:
    next(new_g)
except StopIteration:
    pass
finally:
    print(inspect.getgeneratorstate(new_g)) # GEN_CLOSED

print(' *** '.join(dir(new_g)))

def gen_send_method():
    something = yield
    print(something)

send_g = gen_send_method()
next(send_g)
# send_g.send("Hi, Buddy!!!")

print('-------------------------------------------------------------')
def sub_gen():
    # for i in range(3):
    #     yield i
    val = yield
    print(f'val: {val}')

def main_gen():
    g = sub_gen()
    # for i in g:
    #     yield i
    yield from g


gen = main_gen()
gen.send(None)
gen.send('From main_gen')
