import logging
import time
import os
import requests
from rich.progress import track
import threading, multiprocessing

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

URL = "https://cataas.com/cat"
OUT_PATH = './temp/{}.jpeg'

def get_image(url: str, result_path: str):
    response = requests.get(url)
    if response.status_code != 200:
        return None
    with open(result_path, 'wb') as file:
        file.write(response.content)


def load_images_sequential():
    start = time.time()
    for i in track(range(10), description="Загрузка images ..."):
        get_image(URL, OUT_PATH.format(i))
    logger.info("Done in {:.4}".format(time.time() - start))


def load_images_multithreading():
    start = time.time()
    threads = []
    for i in track(range(10), description="Загрузка images thread ..."):
        thread = threading.Thread(target=get_image, args=(URL, OUT_PATH.format(i)))
        thread.start()
        threads.append(thread)
    # Нельзя вызывать join сразу start иначе потоки будут выполняться последователь и
    # новый поток будет ждать окончание работы предыдущего, поэтому сначало сохраняем объекты потоков в список
    # затем перебираем список и закрываем все потоки
    for thread in threads:
        thread.join()
    logger.info("Done in {:.4}".format(time.time() - start))


def load_images_multiprocessing():
    start = time.time()
    all_process = []
    logger.info("Start programm...")
    for i in track(range(10), description="Загрузка images multiprocess ..."):
        process = multiprocessing.Process(target=get_image, args=(URL, OUT_PATH.format(i)))
        process.start()
        all_process.append(process)
    for proc in all_process:
        proc.join()
    logger.info("Done in {:.4}".format(time.time() - start))


if __name__ == '__main__':
    if not os.path.exists('temp'):
        os.mkdir('temp')
    # load_images_sequential()
    # load_images_multithreading()
    load_images_multiprocessing()






