import socket
import selectors
from selectors import SelectorKey
from typing import List, Tuple

selector = selectors.DefaultSelector()  # Используем класс DefaultSelector

server = socket.socket()
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_address = ("127.0.0.1", 5000)
server.setblocking(False)
server.bind(server_address)
server.listen()

selector.register(server, selectors.EVENT_READ)  # Регистрация сокета, который будет отслеживаться

while True:
    events: List[Tuple[SelectorKey, int]] = selector.select(timeout=5)  # Создать селектор с таймаутом

    if len(events) == 0:  # Сообщает, что ничего не произошло (можно только с timeout)
        print("Событий пока что нет!")

    for event, _ in events:
        event_socket = event.fileobj
        if event_socket == server:  # Если событие произошло с серверным сокетом, значит попытка подключения
            connection, client_address = server.accept()
            connection.setblocking(False)
            print(f"Запрос на подключение {client_address}")
            selector.register(connection, selectors.EVENT_READ)  # Регистрирует клиента подключившегося к сокету
        else:
            data = event_socket.recv(1024)
            print(f"Получение данных: {data.decode()}")
            event_socket.send(data)