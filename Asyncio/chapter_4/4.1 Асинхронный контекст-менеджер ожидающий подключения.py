import asyncio, socket
from typing import Optional, Type
from types import TracebackType

class ConnectedSocket:
    def __init__(self, server_socket):
        self._connection = None
        self._server_socket = server_socket

    """Сопрограмма  вызывается при входе в блок with"""
    async def __aenter__(self):
        print("Вход в контекстный менеджер. Ожидание подключения...")
        loop = asyncio.get_running_loop()
        connection, address = loop.sock_accept(self._server_socket)
        self._connection = connection
        print("Подключение подтверждено")
        return self._connection

    """Сопрограмма вызывается при выходе из with, производит очистку ресурса и закрывает подключение"""
    async def __aexit__(self,
                        exc_type: Optional[TracebackType],
                        exc_val: Optional[TracebackType],
                        exc_tb: Optional[TracebackType]):
        print("Выход из контекстного менеджера")
        self._connection.close()
        print("Подключение закрыто")

async def main():
    loop = asyncio.get_running_loop()
    server_socket = socket.socket()
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.setblocking(False)
    server_socket.bind(("127.0.0.1", 5000))
    server_socket.listen()

    async with ConnectedSocket(server_socket) as connection:
        message = await loop.sock_recv(connection, 1024)
        print(message.decode())

if __name__ == '__main__':
    asyncio.run(main())
