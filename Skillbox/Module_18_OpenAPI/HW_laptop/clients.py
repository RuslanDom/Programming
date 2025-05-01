import json
import time
import requests
import logging
import threading

logging.basicConfig(level=logging.DEBUG)


class ClientBook:
    URL = "http://127.0.0.1:5000"
    TIMEOUT = 5
    def __init__(self):
        self.session = requests.Session()

    def get_books(self):
        resp = self.session.get(self.URL + "/api/books", timeout=self.TIMEOUT)
        return resp.json()

    def add_book(self, data):
        resp = self.session.post(self.URL + "/api/books", json=data, timeout=self.TIMEOUT)
        if resp.status_code != 201:
            return resp.json()
        else:
            return ValueError("Wrong parameters: {}".format(resp.json()))

    def get_authors(self):
        resp = self.session.get(self.URL + "/api/authors", timeout=self.TIMEOUT)
        return resp.json()

    def add_author(self, data):
        resp = self.session.post(self.URL + "/api/authors", json=data, timeout=self.TIMEOUT)
        if resp.status_code != 201:
            return resp.json()
        else:
            ValueError("Wrong parameters: {}".format(resp.json()))


def solve_threadpool(amount: int, func):
    start = time.time()
    threads = []
    for _ in range(amount):
        thread = threading.Thread(target=func)
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
    end = time.time()
    print(end - start)


if __name__ == '__main__':
    client = ClientBook()
    solve_threadpool(amount=100, func=client.get_books)
    # response = client.get_books()
    # print(response)
    # authors_list = client.get_authors()
    # print(authors_list)


    data = {
        "title": "Green grass",
        "author": "It`s me",
    }
    # client.add_book(data)

























# class BookClient:
#     URL: str = 'http://0.0.0.0:5000/api/books'
#     TIMEOUT: int = 5
#
#     def __init__(self):
#         self.session = requests.Session()
#
#     def get_all_books(self) -> dict:
#         response = self.session.get(self.URL, timeout=self.TIMEOUT)
#         return response.json()
#
#     def add_new_book(self, data: dict):
#         response = self.session.post(self.URL, json=data, timeout=self.TIMEOUT)
#         if response.status_code == 201:
#             return response.json()
#         else:
#             raise ValueError('Wrong params. Response message: {}'.format(response.json()))
#
#
# if __name__ == '__main__':
#     client = BookClient()
#     client.session.post(
#         client.URL,
#         data=json.dumps({'title': '123', 'author': 'name'}),
#         headers={'content-type': 'application/json'}
#     )
