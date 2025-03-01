import keyboard
from time import sleep
import threading

"""Ставит на паузу, не завершая программу, мб кому-то пригодится"""

def main():
    while pause.wait():
        sleep(1)
        print('Hello')


def off():
    while True:
        if keyboard.wait('Ctrl + 1') is None: # активация цикла на Ctrl + 1
            pause.set()
        if keyboard.wait('Ctrl + 2') is None: # остановка цикла на Ctrl + 2
            pause.clear()


pause = threading.Event()
thread1 = threading.Thread(target=main)
thread2 = threading.Thread(target=off)

thread1.start()
thread2.start()

thread1.join()
thread2.join()