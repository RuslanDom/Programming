import asyncio
import socket
from asyncio import AbstractEventLoop
import logging

async def echo(connection: socket, loop: AbstractEventLoop):
    # Тоже самое что и эта запись
    # data = await loop.sock_recv(1024)
    # while data:
    try:
        while data := await loop.sock_recv(connection, 1024):  # Бесконечный цикл ожидает данные от клиента
            if data.decode() == "boom":
                raise Exception('Fake ERROR!!!')
            await loop.sock_sendall(connection, data)  # Отправляет назад как ЭХО данные полученные от клиента
    except Exception as ex:
        logging.exception(ex)
    finally:
        connection.close()

async def listen_for_connection(server: socket, loop: AbstractEventLoop):
    while True:
        connection, client_address = await loop.sock_accept(server)
        connection.setblocking(False)
        print(f"Получен запрос на подключение от {client_address}")
        asyncio.create_task(echo(connection, loop))

async def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_address = ("127.0.0.1", 5000)
    server.setblocking(False)
    server.bind(server_address)
    server.listen()

    await listen_for_connection(server, asyncio.get_running_loop())

if __name__ == '__main__':
    asyncio.run(main())



