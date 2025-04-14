import logging
from typing import Callable
import requests
import time
import threading

# logging.basicConfig(level=logging.DEBUG)

def api_timer(func: Callable):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        response = func(*args, **kwargs)
        end_time = time.time()
        print(round(end_time - start_time, 5))
        return response
    return wrapper



class BookClient:
    URL = 'http://127.0.0.1:5000/api/books'
    TIMEOUT = 5

    def __init__(self):
        self.session = requests.Session()

    def get_all_books(self, *args, **kwargs):
        resp = self.session.get(self.URL, timeout=self.TIMEOUT)
        return resp.json()

    def add_book_session(self, book: dict):
        resp = self.session.post(self.URL, json=book, timeout=self.TIMEOUT)
        if resp.status_code == 201:
            return resp.json()
        else:
            return ValueError("Wrong parameters: {}".format(resp.json()))

    def get_book_by_id(self, book_id: int):
        resp = self.session.get(self.URL + "/{}".format(book_id), timeout=self.TIMEOUT)
        if resp.status_code == 200:
            return resp.json()
        else:
            return ValueError("Error 404. Not found.")

    def put_book(self, book_id: int, data: dict):
        resp = self.session.put(self.URL + "/{}".format(book_id), json=data, timeout=self.TIMEOUT)
        if resp.status_code == 200:
            return resp.json()
        else:
            return ValueError("Error 404. Not found.")

    def patch_book(self, book_id: int, data: dict):
        resp = self.session.patch(self.URL + "/{}".format(book_id), json=data, timeout=self.TIMEOUT)
        if resp.status_code == 200:
            return resp.json()
        else:
            return ValueError("Error 404. Not found.")

    def delete_book(self, book_id: int):
        resp = self.session.delete(self.URL + "/{}".format(book_id), timeout=self.TIMEOUT)
        if resp.status_code == 204:
            return "Success, book {} deleted".format(book_id)


class AuthorClient:
    URL = 'http://127.0.0.1:5000/api/authors'
    TIMEOUT = 5
    def __init__(self):
        self.session = requests.Session()
        self.request = requests

    def get_all_authors(self, *args, **kwargs):
        resp = self.session.get(self.URL, timeout=self.TIMEOUT)
        return resp.json()

    def add_author(self, author: dict):
        resp = self.session.post(self.URL, json=author, timeout=self.TIMEOUT)
        if resp.status_code == 201:
            return resp.json()
        else:
            return ValueError("Wrong parameters: {}".format(resp.json()))

    def get_all_books_by_author_id(self, author_id: int):
        resp = self.session.get(self.URL + "/{}".format(author_id), timeout=self.TIMEOUT)
        if resp.status_code == 200:
            return resp.json()

    def delete_author_by_id(self, author_id: int):
        resp = self.session.delete(self.URL + "/{}".format(author_id), timeout=self.TIMEOUT)
        if resp.status_code == 204:
            return "Success, author {} deleted".format(author_id)


class ApiTest:
    def __init__(self):
        self.book_client = BookClient()
        self.author_client = AuthorClient()

    @api_timer
    def repeat_count(self, number: int, func):
        for _ in range(number):
            func(self.book_client.URL)

    @staticmethod
    @api_timer
    def use_threading(number: int, func, *args):
        threads = []
        for i in range(number):
            thread = threading.Thread(target=func, args=args)
            thread.start()
            threads.append(thread)
        for thread in threads:
            thread.join(timeout=5)

    def check_api(self):
        self.repeat_count(10, self.book_client.get_all_books)
        self.repeat_count(100, self.book_client.get_all_books)
        self.repeat_count(1000, self.book_client.get_all_books)

    def check_api_with_session(self):
        self.repeat_count(10, self.book_client.session.get)
        self.repeat_count(100, self.book_client.session.get)
        self.repeat_count(1000, self.book_client.session.get)

    def check_api_with_threads(self):
        print("Стандартно")
        self.use_threading(10, self.book_client.get_all_books)
        self.use_threading(100, self.book_client.get_all_books)
        self.use_threading(1000, self.book_client.get_all_books)
        print("В сессии")
        self.use_threading(10, self.book_client.session.get, self.book_client.URL)
        self.use_threading(100, self.book_client.session.get, self.book_client.URL)
        self.use_threading(1000, self.book_client.session.get, self.book_client.URL)





if __name__ == '__main__':
    API_TEST = ApiTest()
    print("Стандартное выполнение requests запросов в одном потоке")
    API_TEST.check_api()
    print("Выполнение запросов с использованием session в одном потоке")
    API_TEST.check_api_with_session()
    print("Выполнение запросов с использованием многопоточности")
    API_TEST.check_api_with_threads()



