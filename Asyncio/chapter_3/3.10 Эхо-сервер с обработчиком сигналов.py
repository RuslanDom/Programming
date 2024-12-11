import socket, asyncio, signal, logging
from asyncio import AbstractEventLoop
from typing import List


async def echo(connect: socket, loop: AbstractEventLoop):
    try:
        while message := await loop.sock_recv(connect, 1024):

                await loop.sock_sendall(connect, message)
                if message == b'boom\r\n':
                    raise Exception('Остановка программы')
    except Exception as ex:
        logging.exception(ex)
    finally:
        connect.close()

echo_tasks = []

async def listen_for_connection(server: socket, loop: AbstractEventLoop):
    while True:
        connection, address = await loop.sock_accept(server)
        print(f"Подключен {address}")
        connection.setblocking(False)

        echo_task = asyncio.create_task(echo(connect=connection, loop=loop))
        echo_tasks.append(echo_task)

class GracefullyExit(SystemExit):
    pass

def shutdown():
    raise GracefullyExit

async def close_echo_tasks(echo_tasks: List[asyncio.Task]):
    waiters = [asyncio.wait_for(task, 2) for task in echo_tasks]
    for task in waiters:
        try:
            await task
        except asyncio.TimeoutError:
            pass

async def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.setblocking(False)
    server.bind(("127.0.0.1", 5000))
    server.listen()

    for signame in {"SIGINT", "SIGTERM"}:
        loop.add_signal_handler(getattr(signal, signame), shutdown)
    await listen_for_connection(server, loop)

loop = asyncio.new_event_loop()
try:
    loop.run_until_complete(main())
except GracefullyExit:
    loop.run_until_complete(close_echo_tasks(echo_tasks))
finally:
    loop.close()
