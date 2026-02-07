import time

'''
Ручное профилирование
'''
def profiler(func):
    def wrapper(*args, **kwargs):
        before = time.time()
        f = func(*args, **kwargs)
        after = time.time()
        print(after - before)
    return wrapper


@profiler
def hello_buddy():
    time.sleep(1)
    print("Hello Buddy")



class Cocktail:
    def do(self):
        pass


class Barman:
    def __init__(self):
        self.no_cocktails()

    def no_cocktails(self):
        self.cocktails = []

    def add_cocktail_order(self, cocktail):
        self.cocktails.append(cocktail)

    def do_cocktails(self):
        [cocktail.do() for cocktail in self.cocktails]
        self.no_cocktails()

def start_barman():
    barman = Barman()
    for c in range(10):
        barman.add_cocktail_order(Cocktail())
    barman.do_cocktails()

if __name__ == '__main__':
    hello_buddy()
    print("-----------------------")
    start_barman()







