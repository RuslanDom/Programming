import random, threading, requests
import time

endpoints = ['index', 'one', 'two', 'about', 'error']

def run():
    while True:
        try:
            target = random.choice(endpoints)
            requests.get("http://app:5000/%s" % target, timeout=1)

        except:
            pass


if __name__ == '__main__':
    for _ in range(4):
        thread = threading.Thread(target=run, daemon=True)
        thread.start()

    while True:
        time.sleep(1)